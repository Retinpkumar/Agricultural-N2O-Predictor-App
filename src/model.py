import pickle
import os
import numpy as np

current_path = os.path.dirname(os.path.realpath(__file__))

with open('model/final_model.pickle', 'rb') as file:
    model = pickle.load(file) # importing model to predict

def predict(attributes):
    pred = model.predict(attributes)
    final_pred = round(np.square(pred)[0],2)
    return final_pred
