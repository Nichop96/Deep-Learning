import utils
import numpy as np
import save_arrays
import pickle
import oneHot_deep

if __name__ == '__main__':

    file = open("goal", "rb")
    goal = pickle.load(file)
    dizionario_goal = oneHot_deep.create_dictionary_goals(goal)
    dizionario_goal = oneHot_deep.shuffle_dictionary(dizionario_goal)
    oneHot_deep.completa_dizionario(dizionario_goal)
    save_arrays.save(dizionario_goal, "dizionario_goal")