import matplotlib.pyplot as plt
from matplotlib import rcParams
import numpy as np

#Extract Data from File
def extract_data(files):
    data = {files[x]:[] for x in range(len(files))}
    for i in range(len(files)):
        filename = files[i]
        data[files[i]] = np.loadtxt(filename)
    
    return data

#Create Combined Plot
def plot_points(data, name, color):
    x_points = data[:, 0]
    y_points = data[:, 1]
    plt.plot(x_points, y_points, color=color, label=name, marker="o")

if __name__ == "__main__":
    #Initiation
    rcParams.update({"font.size": 12})
    plt.figure()

    #Inputs
    filenames = ["Yao2022HumanL23VIP.if.dat", "Yao2022HumanL23SST.if.dat", "Yao2022HumanL23PV.if.dat", "Yao2022HumanL23Pyr.if.dat"]
    names = ["VIP", "SST", "PV", "Pyr"]
    colors = ['yellow','green', 'red', 'black']
    
    #Plot Lines
    data = extract_data(filenames)
    for i in range(len(filenames)):
        plot_points(data[filenames[i]], names[i], colors[i])
    
    #Set Up Plot
    plt.xlabel("Input Current (pA)")
    plt.ylabel("Firing Rate (Hz)")
    plt.legend()
    plt.grid()
    plt.savefig("Combined_IF_Graph.png", bbox_inches="tight")
    plt.show()