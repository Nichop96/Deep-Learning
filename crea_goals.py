import neuralNet
import numpy as np
import random
import utils
import oneHot_deep
import save_arrays


if __name__ == '__main__':
    folder = "XmlPlans"
    plans = utils.get_plans(folder)
    goals = []
    for p in plans:
        if p.goals not in goals:
            goals.append(p.goals)
    save_arrays.save(goals, "goal")
    print(len(goals))
