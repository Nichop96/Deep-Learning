import plan
import logistic_domain
import os


def get_plans(folder):
    plan_list = [plan.Plan(folder + "/" + file) for file in os.listdir(folder) if file.endswith(".soln") or file.endswith(".SOL")]
    return plan_list


def logistics_domains(folder):
    domains_list = [logistic_domain.LogisticDomain(folder + "/" + file) for file in os.listdir(folder) if file.endswith(".pddl")]
    return domains_list