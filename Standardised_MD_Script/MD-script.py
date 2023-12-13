#
#
#
#

from pyneuroml.pynml import *
from pyneuroml.plot import PlotMorphology
from pyneuroml.analysis import NML2ChannelAnalysis, generate_current_vs_frequency_curve

if __name__ == "__main__":
    #file = input("Enter the network file: ")
    #cell_file = input("Enter the cell file: ")
    #lems_file = input("Enter the LEMS file: ")

    #NeuroML and LEMS files
    #file = "../L5bPyrCellHayEtAl2011.net.nml"
    name = "Hay2011L5bPyramidalCell"
    file_name = name + ".md"
    file = "generatedNeuroML2/TestL5PC.net.nml"
    cell_file = "generatedNeuroML2/L5PC.cell.nml"
    lems_file = "generatedNeuroML2/LEMS_TestL5PC.xml"

    #Load NML2 and LEMS Models
    lems_model = read_lems_file(lems_file, include_includes=True)
    nml_doc = read_neuroml2_file(cell_file, include_includes=True)
    cell = nml_doc.cells[0]
    print('%s %s' %(cell.id, cell.notes))

    #List Channels
    #info = cell_info(cell)
    #print('%s' %(info))

    #Plot Morphology
    PlotMorphology.plot_2D(
        file,
        nogui = True,
        save_to_file="imgs/" + name + ".png",
        title = name
        )
    
    #Get Includes
    info = nml_doc.summary(show_includes=True)
    print(info)

    #IV & IF Curves
    """
    generate_current_vs_frequency_curve(
        file,
        "L5PC",
        start_amp_nA = -0.5,
        end_amp_nA = 1,
        step_nA = 0.2,
        dt=0.025,
        simulator="jNeuroML_NEURON",
        plot_voltage_traces=True,
        plot_iv = True,
        analysis_duration=1000,
        analysis_delay=0,
        save_if_figure_to="imgs/" + name + "IF.png",
        save_iv_figure_to="imgs/" + name + "IV.png"
        )
    """

    #Extract Cell Name
    #Extract Metadata
    #Get 2D/3D Morphology
    #Get list of channels, channel analysis, etc
    #Get IF & IV curves
    #Maybe: Get greater network, inputs and outputs

    try:
        with open(file_name, "x") as file:
            pass
    except FileExistsError:
        pass

    with open(file_name, "w") as file:
        file.write("# " + name + "\n\n")  #Write Cell Name
        #file.write()    #Write Metadata
        #file.write()    #Write 2D View
        #file.write()    #Write 3D View
        #file.write()    #Write List of Channels
        #file.write()    #Write Channel Analysis
        #file.write()    #Write IF Curve
        #file.write()    #Write IV Curve
        file.write("%s %s" %(cell.id, cell.notes) + "\n\n")
        file.write('<img src="imgs/' + name + '.png" height="300" />' + "\n\n")
        file.write(info + "\n\n")
        file.write("![IFplot](imgs/" + name + "IF.png)" + "\n\n")
        file.write("![IVplot](imgs/" + name + "IV.png)" + "\n\n")

    with open(file_name, "r") as file:
        print(file.read())