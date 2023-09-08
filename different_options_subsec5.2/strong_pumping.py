import sys
sys.path.insert(0, "../anderson_junction_subsec5.1")
from default_parameters import parameters
from model import solve

parameters["P_r"] = 0.14  # 2*P_r
parameters["output_dir"] = '../output/strong_pumping'

solve(parameters)
