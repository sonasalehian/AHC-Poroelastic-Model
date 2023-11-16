
Anisotropy Hydraulic Conductivity Poroelastic Model (AHC-Poroelastic-Model)
===================================

Description
===========

The AHC-Poroelastic-Model is a practical software designed for simulating AHC aquifer systems. The model incorporates Biot equations to represent poroelastic behavior, and these equations are effectively solved using the finite element method (FEM) within the Fenicsx framework. DOLFINx offers efficient and robust numerical methods for solving partial differential equations, making it well-suited for our groundwater modeling purposes. 

For a comprehensive understanding of this project, I encourage you to refer to the corresponding paper: [Insert paper Link Here].

Additionally, you can explore the project's results and accompanying figures on my Figshare account: [Insert Figshare Link Here].

Parameters (default_parameters.py)
===========



Description of files
===========
Within this repository, you will encounter four folders, each closely tied to a specific subsection within the paper. The folders are as follows:

1. anderson_junction_subsec5.1: This folder pertains to the Anderson Junction case study and its associated details.
  
2. different_options_subsec5.2: Here, you will find information relevant to the exploration of different options, as discussed in subsection 5.2 of the paper.
      
3. anisotropy_ratio_subsec5.4: This folder is dedicated to the investigation of anisotropy ratios, a focus of subsection 5.4.
       
4. figures: Within this folder, you can access all the figures referred to in the paper.
       
These folders and files collectively provide a comprehensive resource for delving into the various aspects discussed in the corresponding sections of the paper.

<table>
    <thead>
        <tr>
            <th>Folder name</th>
            <th>File name</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td rowspan=4>anderson_junction_subsec5.1</td>
            <td>01_anderson_junction.py</td>
            <td>To run the model using Anderson Junction aquifer properties and the Anderson Junction aquifer test</td>
        </tr>
        <tr>
            <td>default_parameters.py</td>
            <td>Anderson Junction properties</td>
        </tr>
        <tr>
            <td>model.py</td>
            <td>The proposed model</td>
        </tr>
        <tr>
            <td>utils.py</td>
            <td>To print in parallel running</td>
        </tr>
        <tr>
            <td rowspan=3>different_options_subsec5.2</td>
            <td>01_strong_pumping.py</td>
            <td>To examine the model using Anderson Junction aquifer properties and the Anderson Junction aquifer test but with double pumping rate</td>
        </tr>
        <tr>
            <td>01_long_pumping_8d.py</td>
            <td>To examine the model using Anderson Junction aquifer properties and the Anderson Junction aquifer test but with 8 days of pumping instead of 4 days</td>
        </tr>
        <tr>
            <td>01_long_pumping_16d.py</td>
            <td>To examine the model using Anderson Junction aquifer properties and the Anderson Junction aquifer test but with 16 days of pumping instead of 4 days</td>
        </tr>
            <tr>
            <td rowspan=2>anisotropy_ratio_subsec5.4</td>
            <td>01_anisotropy_ratio1_1.py</td>
            <td>To examine the model using the Anderson Junction aquifer test, and Anderson Junction aquifer properties but with same hydraulic conductivity in directions of x and y (isotropy)</td>
        </tr>
        <tr>
            <td>01_anisotropy_ratio3_1.py</td>
            <td>To examine the model using the Anderson Junction aquifer test, and Anderson Junction aquifer properties but with anisotropy ratio of 3:1</td>
        </tr>
        <tr>
            <td rowspan=13>figures</td>
	<tr>
            <td>02_plot_ar.py</td>
            <td>To generate anisotropy ratio subfigures (figure 15)</td>
        </tr>
         <tr>
            <td>02_plot_flux.py</td>
            <td>To generate the flux subfigures (Figure 11)</td>
        </tr>
         <tr>
            <td>02_plot_graphs.py</td>
            <td>To generate the deformation in different time in x, and y direction (Figure 12)</td>
        </tr>
         <tr>
            <td>02_plot_long_strong.py</td>
            <td>To generate the subfigures of different aquifer tests (Figures 13, and 14)</td>
        </tr>
        <tr>
            <td>02_plot_mesh_2d_en.py</td>
            <td>To plot the surface of the mesh in ENU coordinate system using Paraview software</td>
        </tr>
        <tr>
            <td>02_plot_mesh_2d_zy.py</td>
            <td>To plot the cross-section of mesh in the zy direction (figure 8)</td>
        </tr>
        <tr>
            <td>02_plot_mesh_3d.py</td>
            <td>To plot the 3D mesh (figure 8)</td>
        </tr>
            <td>data_extraction_t.py</td>
            <td>To extract surface displacement along xx’ and yy’ in time T for different anisotropy ratio. It contains “data_deformation_T” function that used in plot_ar.py</td>
        </tr>
        <tr>
            <td>data_extraction_timeseries.py</td>
            <td>To extract surface displacement along xx’ and yy’ in different times. It contains “timeseries_data” function that uses in plot_graphs.py</td>
        </tr>
        <tr>
            <td>paraview_ar.py</td>
            <td>To plot surface displacement of given anisotropy ratio result using Paraview software. It contains “extract_paraview_AR” function that uses in plot_ar.py</td>
        </tr>
        <tr>
            <td>paraview_flux.py</td>
            <td>To plot the direction and magnitude of flux by arrows using Paraview software. It contains “extract_paraview_flux" function that uses in plot_flux.py</td>
        </tr>
         <tr>
            <td>paraview_los_t.py</td>
            <td>To plot surface displacement of different options and extract surface displacement along xx’ and yy’ in time T using Paraview software. It contains “plot_LOS_T” and “data_LOS_T” functions that uses in plot_long_strong.py</td>
        </tr>
        <tr>
            <td>layers.json</td>
            <td>The preset colorbar to use for illustration</td>
        </tr>
      <tr>
            <td>output</td>
            <td></td>
            <td>All output files</td>
        </tr>
        <tr>
            <td></td>
            <td>launch_container.sh</td>
            <td>To run dolfinx using docker</td>
        </tr>
    </tbody> 
</table>
Note: Codes prefixed with "01_" should be executed first, as they generate outputs essential for the subsequent execution of codes prefixed with "02_". Additionally, other codes without specific prefixes contains supportive functions to run other codes. 

Getting started
===========

1. If Docker is available on your device, you can use the "launch_container.sh" script for setup. Alternatively, refer to the FEniCSx image for alternative methods to access their package.

		./launch_container.sh
Then navigate to the folder that you want to run a code.
       
2. Within the FEniCSx, you can execute the Python files denoted with an asterisk (*) in the table (except those within the figures folder). Use the following command inside the dolfinx image:

       python3 [name_of_file].py
       
3. For executing plot-related Python files in the "figures" folder:
       
- If you intend to use Paraview functions (while commenting out the scienceplots commands),  use the following command outside the dolfinx image:
       
       pvpython [name_of_file].py
       
- If you intend to use the scienceplots library (while commenting out the Paraview commands), execute the file outside the dolfinx image:
           
      python3 [name_of_file].py
	
In the first time, you need to run with paraview commands first, and then run with  	scienceplots to produce the figures. 

How to modify the model
==========

Modifying the codes to suit your specific aquifer and aquifer test requirements can be achieved through several avenues:

1. Adjusting Aquifer Properties and Test Parameters:
       To alter aquifer properties or aquifer test parameters, simply edit the file named "default_parameters.py".
       
2. Revamping Aquifer System Structure:
       For a complete overhaul of the aquifer system's structure, navigate to the "create_mesh" function within "model.py" and make the necessary adjustments.
       
3. Changing Boundary Conditions:
       To modify boundary conditions, access the "boundary_conditions" function within "model.py" and tailor them as needed.
       
4. Assigning Layer-Specific Parameters:
       When specific parameters need to be assigned to different layers, utilize the "equation_parameters" function found in "model.py".
       
5. Exploring New Scenarios:
       Should you wish to examine novel scenarios, replicate the approach used in "strong_pumping.py". Create a new file, adjust the desired parameters, and execute it to analyze the new experience.

By leveraging these code modification approaches, you can seamlessly tailor the software to suit your unique aquifer and aquifer test conditions.

Citing
===========

Please consider citing this code and related paper if you find it useful.

```
@misc{salehian_ahc-poroelastic-model_2023,
      title = {{Anisotropy} {Hydraulic} {Conductivity} { Poroelatic {Model} {(AHC-Poroelastic-Model)}},
      author = {Salehian Ghamsari, Sona, and Hale, Jack S.},
      month = sep,
      year = {2023},
      doi = {},
      keywords = {poroelastic model, anisotropy hydraulic conductivity, FEniCS, finite element methods},
}
```

along with the appropriate general `FEniCS citations <http://fenicsproject.org/citing>`_.

Authors (alphabetical)
======================

| Sona Salehian Ghamsari, University of Luxembourg, Luxembourg.
| Jack S. Hale, University of Luxembourg, Luxembourg.


License
==========

AHC-Poroelastic-Model is free software: you can redistribute it and/or modify it under the terms of the GNU Lesser General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more details.
You should have received a copy of the GNU Lesser General Public License along with AHC-Poroelastic-Model. If not, see http://www.gnu.org/licenses/.


