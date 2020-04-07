import os
import logistic_domain
import numpy as np
import shutil

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

def copyFileSets(domains):
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
        #path = '/home/deeplearning/Bonassi-Onger/Fase1DL/PlanSets6/'+str(index) +'_set'
        #shutil.copy(domain.name_file, path)
        print(domain.name_file.split(".pddl")[0])

if __name__ == '__main__':
    folder = "XmlPlans"
    domains = logistics_domains(folder)
    copyFileSets(domains)
    #count_different_sets()





