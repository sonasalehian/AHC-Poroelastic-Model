import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#  Comment when running scienceplots
# from data_extraction_timeseries import timeseries_data
##
import sys
sys.path.insert(0, "../anderson_junction_subsec5.1")
from default_parameters import parameters

import scienceplots

plt.style.use(['science'])

time_steps = np.array([6, 12, 18, 36])

directions = ['x', 'y']
for direction in directions:
    #  Comment when running scienceplots
    # timeseries_data(direction)
    ##
    uz = np.zeros((1001, 2, time_steps.shape[0]))

    if direction == 'x':
        Lw = parameters["Lyw"]
    elif direction == 'y':
        Lw = parameters["Lxw"]

    # Plot pressure x direction
    fig = plt.figure(figsize=(4, 3))

    i = 0
    for t in time_steps:
        line = pd.read_csv(f'../output/AJ/linegraph_{direction}/line{direction}_time_{t}.csv')
        data = pd.DataFrame(line, columns=['arc_length','u_n:2'])
        uz[:, :, i] = data
        i += 1

    plt.plot(uz[:, 0, 0]-Lw, uz[:, 1, 0]*-1000, label=rf'$t = T_p/3$', color='lightseagreen', linestyle='solid')
    plt.plot(uz[:, 0, 1]-Lw, uz[:, 1, 1]*-1000, label=rf'$t = 2 \ T_p/3$', color='orange', linestyle='dashed')
    plt.plot(uz[:, 0, 2]-Lw, uz[:, 1, 2]*-1000, label=rf'$t = T_p$', color='olive', linestyle='dashdot')
    plt.plot(uz[:, 0, 3]-Lw, uz[:, 1, 3]*-1000, label=rf'$t = T_e$', color='darkmagenta', linestyle='dotted')

    if direction == 'x':
        plt.xlabel(r'$y-L_{yw}$ (m)', fontsize=10)
        # plt.title(rf'z-displacement along line $yy\prime$', fontsize=10)
    elif direction == 'y':
        plt.xlabel(r'$x-L_{xw}$ (m)', fontsize=10)
        # plt.title(rf'z-displacement along line $xx\prime$', fontsize=10)
    plt.ylabel(r'$- u_z$ (mm)', fontsize=10)
    plt.legend(fontsize=10)
    plt.tight_layout()
    plt.ylim(-3.2, 0.2)

    plt.savefig(f"../output/plots/graph_{direction}.png")  # save as png
    plt.savefig(f"../output/plots/graph_{direction}.pdf", format="pdf")  # save as pdf
