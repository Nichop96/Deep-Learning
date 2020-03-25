import numpy as np
from keras.models import Model
from keras.layers import Input
from keras.layers import Dense, LSTM
from keras.models import Sequential
from AttentionMechanism import AttentionL
import keras


def get_net(len_sequance, dim_input, dim_output):
    input = Input(shape=(len_sequance, dim_input))
    l = LSTM(64, activation="linear")(input)
    o = Dense(dim_output, activation="softmax")(l)
    model = Model(input=input, outputs=o)
    #adam = keras.optimizers.Adam(lr=0.1, beta_1=0.9, beta_2=0.999, amsgrad=False)
    sgd = keras.optimizers.SGD(lr=0.1)
    model.compile(optimizer=sgd, loss='categorical_crossentropy', metrics=['accuracy'])
    return model


def get_net2(dim_output):
    model = Sequential()
    model.add(LSTM(64, activation="linear", return_sequences=False))
    #model.add(AttentionL(64))
    model.add(Dense(dim_output, activation="softmax"))
    sgd = keras.optimizers.SGD(lr=0.1)
    model.compile(optimizer=sgd, loss='categorical_crossentropy', metrics=['accuracy'])
    return model

