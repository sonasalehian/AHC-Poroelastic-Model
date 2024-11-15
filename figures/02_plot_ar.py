
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# paraview functions:{
from paraview_ar import extract_paraview_AR
from data_extraction_t import data_deformation_T
# }
import sys
import os
sys.path.insert(0, "../anderson_junction_subsec5.1")
from default_parameters import parameters
# # scienceplot comands:{
# import scienceplots

# plt.style.use(['science'])
# # }
num_steps = parameters["num_steps"]
time_steps = [6, 12, 18]
for t in time_steps:
    t_name = int(t)
    output_filename = f"AR31_samescale_{t_name}"
    input_filepath = '../output/AR31_samescale'
    extract_paraview_AR(input_filepath, t, output_filename)
    output_filename = f"AJ_{t_name}"
    input_filepath = '../output/AJ'
    extract_paraview_AR(input_filepath, t, output_filename)
    output_filename = f"AR11_samescale_{t_name}"
    input_filepath = '../output/AR11_samescale'
    extract_paraview_AR(input_filepath, t, output_filename)


inputfiles = ['AJ', 'AR31_samescale', 'AR11_samescale']

for inputfile in inputfiles:
    data_deformation_T(inputfile)

directions = ['x', 'y']
for direction in directions:

    uz = np.zeros((1001, 2, len(inputfiles)))

    if direction == 'x':
        Lw = parameters["Lyw"]
    elif direction == 'y':
        Lw = parameters["Lxw"]

    # Plot deformation each direction
    fig = plt.figure(figsize=(4, 3))

    i = 0
    for inputfile in inputfiles:
        line = pd.read_csv(f'../output/plots/data/{inputfile}_{direction}.csv')
        data = pd.DataFrame(line, columns=['arc_length', '-u_z'])
        uz[:, :, i] = data
        i += 1
    
    plt.plot(uz[:, 0, 0]-Lw, uz[:, 1, 0]*1000, label=r'AJ $\sim$ 24:1', color='lightseagreen', linestyle='solid')
    plt.plot(uz[:, 0, 1]-Lw, uz[:, 1, 1]*1000, label='Anisotropy ratio 3:1', color='darkmagenta', linestyle='dashed')
    plt.plot(uz[:, 0, 2]-Lw, uz[:, 1, 2]*1000, label='Anisotropy ratio 1:1', color='olive', linestyle='dashdot')
        
    if direction == 'x':
        plt.xlabel(r'$y-L_{yw}$ (m)', fontsize=10)
    elif direction == 'y':
        plt.xlabel(r'$x-L_{xw}$ (m)', fontsize=10)
    plt.ylabel(r"$- u_z$ (mm)", fontsize=10)
    # plt.title(fr'z-displacement along line ${direction}$ for different anisotropy ratio with fixed $k_y$', fontsize=10)
    plt.legend(fontsize=9)
    plt.tight_layout()
    plt.ylim(-3.2, 0.2)

    # Check whether the specified output directory exists or not
    isExist = os.path.exists("../output/plots/Anisotropy_ratio")
    if not isExist:
        # Create the directory
        os.mkdir("../output/plots/Anisotropy_ratio")

    plt.savefig(f"../output/plots/Anisotropy_ratio/graph_{direction}.png")  # save as png
    plt.savefig(f"../output/plots/Anisotropy_ratio/graph_{direction}.pdf", format="pdf")  # save as pdf

