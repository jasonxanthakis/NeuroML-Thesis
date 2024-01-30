from pyneuroml.pynml import read_lems_file, read_neuroml2_file
from pyneuroml.plot import PlotMorphology, generate_plot
from pyneuroml.analysis import generate_current_vs_frequency_curve
from pyneuroml.analysis.NML2ChannelAnalysis import DEFAULTS, main

import numpy as np
import argparse
import os
import shutil

def command_line_parser():
    """Parse command-line arguments.

    :returns: None
    """
    parser = argparse.ArgumentParser(
        description = "A script which can generate a standardised MD document displaying all key behaviours of an NML cell model"
    )

    parser.add_argument(
        "-model",
        type = str,
        metavar = "<model>",
        help = "Get cell model name",
        required = True
    )

    parser.add_argument(
        "-filepath",
        type = str,
        metavar = "<filepath>",
        help = "Get path to channel files",
        default = "False",
        required = False
    )

    parser.add_argument(
        "-cellfile",
        type = str,
        metavar = "<cellfile>",
        help = "Get NML2 cell file",
        required = True
    )

    parser.add_argument(
        "-netfile",
        type = str,
        metavar = "<netfile>",
        help = "Get NML2 network file",
        default = "False",
        required = False
    )

    parser.add_argument(
        "-lemsfile",
        type = str,
        metavar = "<lemsfile>",
        help = "Get LEMS simulation file",
        default = "False",
        required = False
    )

    """
    parser.add_argument(
        "-nogui",
        action = "store_true",
        help = "Do not plot matplotlib generated graphs",
        default = False,
        required = False
    )
    """
    
    parser.add_argument(
        "-nosave",
        action = "store_true",
        help = "Do not save anything",
        default = False, 
        required = False
    )

    parser.add_argument(
        "-nosim",
        action = "store_true",
        help = "Do not perform simulations and use already existing files",
        default = False, 
        required = False
    )

    parser.add_argument(
        "-nopng",
        action = "store_true",
        help = "Do not store png files of the graphs made from the simulations",
        default = False,
        required = False
    )

    parser.add_argument(
        "-nomd",
        action = "store_true",
        help = "Do not create a new MD or alter an existing MD file",
        default = False,
        required = False
    )
    
    return parser.parse_args()

def extract_included_file_names(file_path):
    included_file_names = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                if 'Include' in line:
                    #Find the text between quotation marks
                    start_quote = line.find('"')
                    end_quote = line.find('"', start_quote + 1)

                    if start_quote != -1 and end_quote != -1:
                        included_file_name = line[start_quote + 1:end_quote]
                        included_file_names.append(included_file_name)

        #Filter out items that do not contain ".channel."
        included_file_names = [file_name for file_name in included_file_names if '.channel.' in file_name]

    except FileNotFoundError:
        print(f"File not found: {file_path}")

    return included_file_names

def move_files(source, destination, md_destination, name):
    #Get a list of files in the source directory that end with .png
    files_to_move = os.listdir(source)
    files_to_move = [file for file in files_to_move if file.endswith('.png')]

    #Move each file to the destination directory
    for file_name in files_to_move:
        temp = name + file_name
        source_path = os.path.join(source, file_name)
        destination_path = os.path.join(destination, temp)
        shutil.move(source_path, destination_path)

    #Move channel analysis MD file "datasheet" to destination directory
    md_file_source = "README.md"
    md_file_destination = name + "_ChannelInfo.md"

    source_path = os.path.join(source, md_file_source)
    destination_path = os.path.join(md_destination, md_file_destination)
    shutil.move(source_path, destination_path)

    return destination_path, files_to_move

def change_hyperlinks(md_file_path, old_urls, name, change="imgs/"):
    with open(md_file_path, 'r') as file:
        md_content = file.read()

    #Replace old png locations in MD with new locations
    for i in range(len(old_urls)):
        md_content = md_content.replace(old_urls[i], change + name + old_urls[i])

    with open(md_file_path, 'w') as file:
        file.write(md_content)

def generate_morphology(file, name, overview_dir, save = True, nogui = False):
    if save:
        filename = overview_dir + "/imgs/" + name + "2D.png"
    else:
        filename = None

    PlotMorphology.plot_2D(
        file,
        nogui = nogui,
        save_to_file = filename,
        title = name
        )

def get_channels_from_info(info):
    info = info.split("\n")
    channels = info[5]
    channels = eval(channels[15:])
    return channels

def run_channel_analysis(channels, filepath, overview_dir, save = False, nogui = False):
    #Create an empty argparse namespace
    args = argparse.Namespace(
        channelFiles=[],
        v=DEFAULTS["v"],
        minV=-100,
        maxV=60,
        temperature=DEFAULTS["temperature"],
        duration=DEFAULTS["duration"],
        clampDelay=DEFAULTS["clampDelay"],
        clampDuration=DEFAULTS["clampDuration"],
        clampBaseVoltage=DEFAULTS["clampBaseVoltage"],
        stepTargetVoltage=DEFAULTS["stepTargetVoltage"],
        erev=DEFAULTS["erev"],
        scaleDt=DEFAULTS["scaleDt"],
        caConc=DEFAULTS["caConc"],
        datSuffix=DEFAULTS["datSuffix"],
        norun=DEFAULTS["norun"],
        nogui=nogui,
        html=False,
        md=save,
        ivCurve=DEFAULTS["ivCurve"]
    )

    #Run through each channel individually
    channel_list = []
    for i in range(len(channels)):
        command = [filepath + str(channels[i])]

        args.channelFiles = command

        try:
            main(args=args)
            channel_list.append(channels[i])
        except:
            print("Error: problem with " + str(channels[i]))

    #Run through all the working channels together
    command = []
    for j in range(len(channel_list)):
        temp = filepath + str(channel_list[j])
        command.append(temp)

    args.channelFiles = command
    
    try:
        main(args=args)
    except:
        print("Error: problem with " + str(channel_list[j]))

    return channel_list

def generate_if_iv(file, name, overview_dir, cell, start = -0.5, end = 1, step = 0.05, time = 0.025, duration = 1000, delay = 0, save = False, pre = 0, post = 0, nogui = False):
    if save:
        vt_name = overview_dir + "/imgs/" + name + "_Vtraces.png"
        if_name = overview_dir + "/imgs/" + name + "IF.png"
        iv_name = overview_dir + "/imgs/" + name + "IV.png"
    else:
        vt_name = None
        if_name = None
        iv_name = None

    generate_current_vs_frequency_curve(
        file,
        cell,
        start_amp_nA = start,
        end_amp_nA = end,
        step_nA = step,
        dt = time,
        simulator = "jNeuroML_NEURON",
        plot_voltage_traces = not nogui,
        plot_iv = not nogui,
        plot_if = not nogui,
        analysis_duration = duration,
        analysis_delay = delay,
        save_voltage_traces_to = vt_name,
        save_if_figure_to = if_name,
        save_iv_figure_to = iv_name,
        pre_zero_pulse = pre,
        post_zero_pulse = post
        )

def generate_if_iv_custom(file, name, overview_dir, cell, custom = [-0.5,0,0.5,1], time = 0.025, duration = 1000, delay = 0, save = False, pre = 0, post = 0, nogui = False):
    if save:
        vt_name = overview_dir + "/imgs/" + name + "_Vtraces.png"
    else:
        vt_name = None

    generate_current_vs_frequency_curve(
        file,
        cell,
        custom_amps_nA = custom,
        dt = time,
        simulator = "jNeuroML_NEURON",
        plot_voltage_traces = not nogui,
        plot_iv = not nogui,
        plot_if = not nogui,
        analysis_duration = duration,
        analysis_delay = delay,
        save_voltage_traces_to = vt_name,
        pre_zero_pulse = pre,
        post_zero_pulse = post,
        font_size=10
        )

def generate_custom_plot(dat_file, delay = False, save = False, nogui = False):
    data_array = np.loadtxt(dat_file)
    l1 = int(len(data_array[:,0]) / 11)
    l2 = int(len(data_array[:,1]) / 11)
    if delay:
        data_array = data_array[l1:]

    if not save:
        file = None
    else:
        file = save

    generate_plot(
        [data_array[:, 0]], [data_array[:, 1]],
	    "Membrane potential", show_plot_already = not nogui,
        save_figure_to = file,
	    xaxis="time (s)", yaxis="membrane potential (V)"
        )

if __name__ == "__main__":
    #Parse Command Line
    args = command_line_parser()
    print(args)
    
    #NeuroML and LEMS files
    name = args.model
    file = args.netfile
    path = args.filepath
    cell_file = args.cellfile
    lems_file = args.lemsfile

    #Load NML2 and LEMS Models
    lems_model = read_lems_file(lems_file, include_includes=True)
    nml_doc = read_neuroml2_file(cell_file, include_includes=True)
    cell = nml_doc.cells[0]
    #print('%s %s' %(cell.id, cell.notes))
    print(cell.id)

    #Get Metadata
    info = nml_doc.summary(show_includes=True)
    channels = extract_included_file_names(lems_file)

    #If it is allowed to save files, set up the overview directory
    if not args.nosave:
        overview_dir = os.path.join(os.getcwd(), "Datasheets")
        overview_dir = os.path.join(overview_dir, name)
        if not os.path.isdir(overview_dir):
            os.makedirs(overview_dir)
        img_dir = os.path.join(overview_dir, "imgs")
        if not os.path.isdir(img_dir):
            os.makedirs(img_dir)

    #If running simulations is allowed; generate morphology, run channel analysis and analyse electrophysiology
    if not args.nosim:
        #Plot Morphology
        #generate_morphology(file, name, overview_dir, save = True, nogui = True)

        #Channel Analysis
        channel_list = run_channel_analysis(channels, path, overview_dir, save = True, nogui = False)
        channel_analysis_md, files_to_move = move_files("channel_summary", img_dir, overview_dir, name)
        change_hyperlinks(channel_analysis_md, files_to_move, name)

        #IV & IF Curves
        #generate_if_iv(file, name, overview_dir, cell.id, save = True, nogui = False, pre = 200, post = 200)
        #generate_if_iv_custom(file, name, overview_dir, cell.id, custom = [-1.0, -0.5, 1.0], save = True, pre = 200, post = 200, nogui = False)

        pass

    #If making a MD is allowed, make a MD file
    if not args.nomd and not args.nosave:
        file_name = overview_dir + "/" + name + ".md"

        #Create the MD file if doesn't exist
        try:
            with open(file_name, "x") as file:
                pass
        except FileExistsError:
            pass

        #Make the MD file
        with open(file_name, "w") as file:
            file.write("# " + name + "\n\n")  #Write Cell Name
            file.write('<img src="imgs/' + name + '2D.png" height="300" />' + "\n\n")
            #Add 3D Morphology
            file.write("")
            
            file.write("# Channel Information" + "\n\n")
            file.write("Ion Channels: " + str(channel_list) + "\n\n")
            file.write('<table border="1">')
            """
            file.write("    <tr>")
            file.write("        <td>Channels</td>")
            file.write("    </tr>")
            """
            file.write('</table>' + "\n\n")
            file.write("")

            file.write("# Electrophysiology" + "\n\n")
            file.write('<img src="imgs/' + name + '_Vtraces.png" />' + "\n\n")
            file.write('<img src="imgs/' + name + 'IF.png" />' + "\n\n")
            file.write('<img src="imgs/' + name + 'IV.png" />' + "\n\n")
            #Add Voltage Traces

    print("\n")