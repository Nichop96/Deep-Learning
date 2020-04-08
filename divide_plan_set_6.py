import os
import logistic_domain
import numpy as np
import shutil
import plan

def logistics_domains(folder):
    domains_list = [logistic_domain.LogisticDomain(folder + "/" + file) for file in os.listdir(folder) if file.endswith(".pddl")]
    return domains_list

def different_sets(domains):
    sets = []
    for domain in domains:
        count_objects = []
        count_objects.append(len(domain.apn))
        count_objects.append(len(domain.cit))
        count_objects.append(len(domain.tru))
        count_objects.append(len(domain.loc))
        count_objects.append(len(domain.obj))
        if count_objects not in sets:
            sets.append(count_objects)
    return sets

def count_different_sets():
    print(len(different_sets()))

def copyPlansWithMaxNumberActions(plan_file, path, maxActions): #funzione che sposta i piani con numero di azioni minore di maxActions
    try:
        piano = plan.Plan(plan_file)
        if len(piano.actions) <= maxActions:
            shutil.copy(plan_file, path)
    except IOError:
        a = 1

def copyFileSets(domains, folder, maxActions):
    sets = different_sets(domains)
    for domain in domains:
        count_objects = []
        count_objects.append(len(domain.apn))
        count_objects.append(len(domain.cit))
        count_objects.append(len(domain.tru))
        count_objects.append(len(domain.loc))
        count_objects.append(len(domain.obj))
        index = str(sets.index(count_objects)+1)
        #path = 'C:\\Users\\Nicholas\\PycharmProjects\\Deep-Learning\\PlanSets6\\'+str(index) +'_set'
        path = '/home/deeplearning/Bonassi-Onger/Fase1DL/PlanSets6/'+str(index) +'_set'
        shutil.copy(domain.name_file, path)
        plan_name = domain.name_file.split(".pddl")[0]
        plan_name = plan_name.split("/")[1]
        plan_file = folder+ "/xml-FF-"+plan_name+".soln"
        copyPlansWithMaxNumberActions(plan_file, path, maxActions)
        for i in range(4):
            plan_file = folder+ "/xml-plan_"+plan_name+".pddl_"+str(i+1)+".SOL"
            copyPlansWithMaxNumberActions(plan_file,path, maxActions)


if __name__ == '__main__':
    folder = "XmlPlans"
    domains = logistics_domains(folder)
    maxActions = 50
    copyFileSets(domains, folder, maxActions)
    #count_different_sets()





