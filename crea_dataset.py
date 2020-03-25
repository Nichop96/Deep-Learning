import numpy as np
import utils
import save_arrays
import pickle
import neuralNet


def get_max_lenght(plans, perc):
    max_dim = 0
    for p in plans:
        dim = np.ceil(len(p.actions)*perc)
        if max_dim < dim:
            max_dim = dim
    return max_dim


def get_actions(actions, perc, dizionario):
    size = int(np.ceil(len(actions)*perc))
    return [dizionario[a.name] for a in actions[:size]]


def fill_action_sequence(X, max_dim, actions, i):
    for j in range(max_dim):
        if j < len(actions):
            X[i][j] = actions[j]
        else:
            X[i][j] = np.zeros(shape=(len(actions[0]),))


def get_goal(g, dizionario_goal):
    goal = ""
    for subgoal in g:
        goal = goal + subgoal
    return dizionario_goal[goal]


def getDataset(plans, max_dim, dizionario, dizionario_goal, perc):
    X = np.empty((len(plans), int(max_dim), len(dizionario)))
    Y = np.empty((len(plans), len(dizionario_goal)))
    for i in range(len(plans)):
        plan = plans[i]
        actions = get_actions(plan.actions, perc, dizionario)
        fill_action_sequence(X, max_dim, actions, i)
        Y[i] = get_goal(plan.goals, dizionario_goal)
    return X, Y


if __name__ == '__main__':
    folder = "XmlPlans"
    file = open("dizionario_casuale", "rb")
    dizionario = pickle.load(file)
    file = open("dizionario_goal", "rb")
    dizionario_goal = pickle.load(file)
    plans = utils.get_plans(folder)
    max_dim = int(get_max_lenght(plans, 0.5))
    X, Y = getDataset(plans, max_dim, dizionario, dizionario_goal, 0.5)
    train_dim = int(0.8*len(X))
    X_train = X[:train_dim]
    X_test = X[train_dim:]
    Y_train = Y[:train_dim]
    Y_test = Y[train_dim:]
    model = neuralNet.get_net2(len(Y[0]))
    model.fit(X_train, Y_train, batch_size=1, epochs=60, verbose=2)




