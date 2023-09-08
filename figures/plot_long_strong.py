import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
# from paraview_LOS_T import plot_LOS_T, data_LOS_T
import sys
sys.path.insert(0, "../anderson_junction_subsec5.1")
from default_parameters import parameters
import scienceplots

plt.style.use(['science'])

inputfiles = ['AJ', 'strong_pumping', 'long_pumping_8d', 'long_pumping_16d']

Ts = np.array([345600.0, 345600.0, 691200.0, 1382400.0])

linestyles = ['solid', 'dashed', 'dashdot', 'dotted']

# Make the directory
directory = "strong_long_pumping"
    
# Parent Directory path
parent_dir = "../output/plots"
    
# Path
path = os.path.join(parent_dir, directory)
# Check whether the specified path exists or not
isExist = os.path.exists(path)
if not isExist:
    # Create the directory
    os.mkdir(path)

i = 0 
for inputfile in inputfiles:
    print(inputfile, i)
    # plot_LOS_T(inputfile, Ts[i])
    # data_LOS_T(inputfile, Ts[i])
    i += 1

directions = ['x', 'y']
for direction in directions:

    uz = np.zeros((1001, 2, Ts.shape[0]))

    if direction == 'x':
        Lw = parameters["Lyw"]
    elif direction == 'y':
        Lw = parameters["Lxw"]

    # Plot pressure x direction
    fig = plt.figure(figsize=(4.5, 3))

    i = 0
    for inputfile in inputfiles:
        line = pd.read_csv(f'../output/plots/strong_long_pumping/{inputfile}_{direction}.csv')
        data = pd.DataFrame(line, columns=['arc_length', 'f'])
        uz[:, :, i] = data
        i += 1

    plt.plot(uz[:, 0, 0]-Lw, uz[:, 1, 0]*1000, label='Anderson Junction', color='lightseagreen', linestyle='solid')
    plt.plot(uz[:, 0, 1]-Lw, uz[:, 1, 1]*1000, label='Strong pumping', color='orange', linestyle='dashed')
    plt.plot(uz[:, 0, 2]-Lw, uz[:, 1, 2]*1000, label='Long pumping, 8 days', color='olive', linestyle='dashdot')
    plt.plot(uz[:, 0, 3]-Lw, uz[:, 1, 3]*1000, label=f'Long pumping, 16 days', color='darkmagenta', linestyle='dotted')

    if direction == 'x':
        plt.xlabel(r'$y-L_{yw}$ (m)', fontsize=10)
    elif direction == 'y':
        plt.xlabel(r'$x-L_{xw}$ (m)', fontsize=10)
    plt.ylabel(r"$u_{LOS}$ (mm)", fontsize=10)
    # plt.title(rf'LOS displacement along line ${direction}$ at the end of pumping', fontsize=10)
    plt.legend(fontsize=9)
    plt.tight_layout()
    plt.ylim(-5.2, 0.2)

    plt.savefig(f"../output/plots/strong_long_pumping/graph_{direction}.png")  # save as png
    plt.savefig(f"../output/plots/strong_long_pumping/graph_{direction}.pdf", format="pdf")  # save as pdf

        
