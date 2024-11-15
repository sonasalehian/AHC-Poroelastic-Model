import sys
sys.path.insert(0, "../anderson_junction_subsec5.1")
from default_parameters import parameters
from model import solve

parameters["P_r"] = 4*0.07  # n*P_r
parameters["T"] = 691200  # 8 days
parameters["output_dir"] = '../output/8d_4pr_pumping'

solve(parameters)
