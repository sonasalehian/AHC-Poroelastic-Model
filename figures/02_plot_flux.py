from paraview_flux import extract_paraview_flux
import sys
sys.path.insert(0, "../anderson_junction_subsec5.1")
from default_parameters import parameters

num_steps = parameters["num_steps"]
time_steps = [0, 1, 18, 19, 36]
for t in time_steps:
    direction = 'x'
    extract_paraview_flux(direction, t)

    direction = 'y'
    extract_paraview_flux(direction, t)
