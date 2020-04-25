import plan
import logistic_domain
import os
from pathlib import Path


def get_plans(folder):
    plan_list = [plan.Plan(folder + "/" + file) for file in os.listdir(folder) if file.endswith(".soln") or file.endswith(".SOL")]
    return plan_list


def logistics_domains(folder):
    domains_list = [logistic_domain.LogisticDomain(folder + "/" + file) for file in os.listdir(folder) if file.endswith(".pddl")]
    return domains_list


def get_folders(argv, name):
    if len(argv) < 2:
        raise ValueError('Please specify the input folder')
    read_folder = argv[1]
    if len(argv) == 3:
        save_folder = argv[2]
        Path(save_folder).mkdir(parents=True, exist_ok=True)
        save_path = str(Path(save_folder)/name)
    else:
        save_path = Path("./")/name
    return read_folder, str(save_path)