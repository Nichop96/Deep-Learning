import neuralNet
import numpy as np
import random


def getPlan(nrow, ncol, ngoal):
    x = np.zeros((nrow, ncol), dtype="float")
    for i in range(nrow):
        index = random.randint(0, ncol-1)
        x[i][index] = 1
    y = np.zeros(ngoal)
    index = random.randint(0, ngoal - 1)
    y[index] = 1
    return x, y


def create_plans(nrow, ncol, ngoal, nplans):
    plans_X = np.empty((nplans, nrow, ncol))
    plans_Y = np.empty((nplans, ngoal))
    for i in range(nplans):
        plan = getPlan(nrow, ncol, ngoal)
        plans_X[i] = plan[0]
        plans_Y[i] = plan[1]
    return plans_X, plans_Y


if __name__ == '__main__':
    X_train, Y_train = create_plans(20, 100, 5, 10)

    model = neuralNet.get_net2(5)
    model.fit(X_train, Y_train, batch_size=10, epochs=60, verbose=2)
    print("ciao")

