import pandas as pd
import numpy as np
import pickle
import os


current_path = os.path.dirname(os.path.realpath(__file__))
def input_scaler(df):
    # opening scalar file
    with open('model/scaler.pickle', 'rb') as file:
        scaler = pickle.load(file) # importing model to predict
    # scaling input data
    scaled_input = scaler.transform(df)
    return df