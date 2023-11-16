import sys
sys.path.insert(0, "../anderson_junction_subsec5.1")
from default_parameters import parameters
from model import solve

parameters["T"] = 691200  # 8 days
parameters["output_dir"] = '../output/long_pumping_8d'

solve(parameters)