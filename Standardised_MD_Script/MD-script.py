from pyneuroml.pynml import read_lems_file, read_neuroml2_file
from pyneuroml.plot import PlotMorphology, generate_plot
from pyneuroml.analysis import generate_current_vs_frequency_curve

import numpy as np
import subprocess
import argparse

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
        default = False
    )
    """
    
    parser.add_argument(
        "-nosim",
        action = "store_true",
        help = "Do not perform simulations and use already existing files",
        default = False
    )

    parser.add_argument(
        "-nomd",
        action = "store_true",
        help = "Do not create a new MD or alter an existing MD file",
        default = False
    )
    
    return parser.parse_args()

def generate_morphology(file, name, save = True, nogui = False):
    if save:
        filename = "imgs/" + name + ".png"
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

def run_channel_analysis(channels, save = False, nogui = False):
    script_name = "channel-analysis-script.sh"

    if save:
        file = "imgs/" + name + ".png"
    else:
        file = None

    #Create pynml-channelanalysis bash command
    command = "pynml-channelanalysis"
    for i in range(len(channels)):
        command = command + " generatedNeuroML2/" + str(channels[i]) + ".channel.nml"

    try:
        with open(script_name, "x") as file:
            pass
    except FileExistsError:
        pass

    with open(script_name, 'w') as file:
        file.write(command)

    result = subprocess.run(['bash', script_name], stderr="PIPE")

    if result.returncode == 0:
        print(result.stderr)

def generate_if_iv(file, name, cell, start = -0.5, end = 1, step = 0.05, time = 0.025, duration = 1000, delay = 0, save = False, pre = 0, post = 0, nogui = False):
    if save:
        vt_name = "imgs/" + name + "_Vtraces.png"
        if_name = "imgs/" + name + "IF.png"
        iv_name = "imgs/" + name + "IV.png"
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

def generate_if_iv_custom(file, name, cell, custom = [-0.5,0,0.5,1], time = 0.025, duration = 1000, delay = 0, save = False, pre = 0, post = 0, nogui = False):
    if save:
        vt_name = "imgs/" + name + "_Vtraces.png"
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
    file_name = "MD_Files/" + name + ".md"
    file = args.netfile
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
    channels = get_channels_from_info(info)

    if not args.nosim:
        #Plot Morphology
        #generate_morphology(file, name, save = True, nogui = True)

        #Channel Analysis
        #run_channel_analysis(channels, save = False, nogui = False)

        #IV & IF Curves
        #generate_if_iv(file, name, cell.id, save = True, nogui = False, pre = 200, post = 200)
        #generate_if_iv_custom(file, name, cell.id, custom = [-1.0, -0.5, 1.0], save = True, pre = 200, post = 200, nogui = False)

        pass

    if not args.nomd:
        try:
            with open(file_name, "x") as file:
                pass
        except FileExistsError:
            pass

        with open(file_name, "w") as file:
            file.write("# " + name + "\n\n")  #Write Cell Name
            file.write('<img src="../imgs/' + name + '.png" height="300" />' + "\n\n")
            #Add 3D Morphology
            #file.write("")
            
            file.write("# Channel Information" + "\n\n")
            file.write("Ion Channels: " + str(channels) + "\n\n")
            file.write('<table border="1">')
            """
            file.write("    <tr>")
            file.write("        <td>Channels</td>")
            file.write("    </tr>")
            """
            file.write('</table>' + "\n\n")
            #file.write("")

            file.write("# Electrophysiology" + "\n\n")
            file.write('<img src="../imgs/' + name + '_Vtraces.png" />' + "\n\n")
            file.write('<img src="../imgs/' + name + 'IF.png" />' + "\n\n")
            file.write('<img src="../imgs/' + name + 'IV.png" />' + "\n\n")
            #Add Voltage Traces

    print("\n")