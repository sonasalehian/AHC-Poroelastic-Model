import sys
sys.path.insert(0, "../anderson_junction_subsec5.1")
from default_parameters import parameters
from model import solve

parameters["P_r"] = 8*0.07  # n*P_r
parameters["output_dir"] = '../output/strong_pumping_8times'

solve(parameters)
