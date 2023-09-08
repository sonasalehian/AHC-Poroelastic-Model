import sys
sys.path.insert(0, "../anderson_junction_subsec5.1")
from default_parameters import parameters
from model import solve

k_x = parameters["k_x_aqfr"]
k_y = parameters["k_y_aqfr"]
parameters["k_x_aqfr"] = 1.7*3*k_y
parameters["k_y_aqfr"] = 1.7*k_y
parameters["output_dir"] = '../output/AR31_samescale'

solve(parameters)
