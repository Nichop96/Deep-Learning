import plan
import os
import save_arrays
import numpy as np
import logistic_domain


def summary(array):
    print("min: "+str(min(array))+"\nmax: "+str(max(array))+"\nmean: "+str(sum(array)/len(array))+"\nmedian: "+str(np.median(array))+"\n1th quartile: "+str(np.percentile(array,25))+"\n3rd quartile: "+str(np.percentile(array,75))+"\n")


def init_statistics(domains):
    airplanes = [len(domain.apn) for domain in domains]
    cities = [len(domain.cit) for domain in domains]
    trucks = [len(domain.tru) for domain in domains]
    locations = [len(domain.loc) for domain in domains]
    objects = [len(domain.obj) for domain in domains]

    print("Airplanes")
    summary(airplanes)
    print("Cities")
    summary(cities)
    print("Trucks")
    summary(trucks)
    print("Locations")
    summary(locations)
    print("Objects")
    summary(objects)


def encoder(domains_list):
    apn_list = []
    for dom in domains_list:
        for a in dom.apn:
            if a not in apn_list:
                apn_list.append(a)
    save_arrays.save(apn_list, "./files/apn.obj")
    cit_list = []
    for dom in domains_list:
        for c in dom.cit:
            if c not in cit_list:
                cit_list.append(c)
    save_arrays.save(cit_list, "./files/cit.obj")
    loc_list = []
    for dom in domains_list:
        for l in dom.loc:
            if l not in loc_list:
                loc_list.append(l)
    save_arrays.save(loc_list, "./files/loc.obj")
    obj_list = []
    for dom in domains_list:
        for o in dom.obj:
            if o not in obj_list:
                obj_list.append(o)
    save_arrays.save(obj_list, "./files/obj.obj")
    tru_list = []
    for dom in domains_list:
        for t in dom.tru:
            if t not in tru_list:
                tru_list.append(t)
    save_arrays.save(tru_list, "./files/tru.obj")


def get_plans(folder):
    plan_list = [plan.Plan(folder + "/" + file) for file in os.listdir(folder) if file.endswith(".soln") or file.endswith(".SOL")]
    return plan_list


def logistics_domains(folder):
    domains_list = [logistic_domain.LogisticDomain(folder + "/" + file) for file in os.listdir(folder) if file.endswith(".pddl")]
    return domains_list


if __name__ == '__main__':
    folder = "XmlPlans"
    plans = get_plans(folder)
    domains = logistics_domains(folder)
    init_statistics(domains)
    save_arrays.save(domains, "./files/domains.obj")
    save_arrays.save(plans, "./files/piani.obj")
    encoder(domains)



