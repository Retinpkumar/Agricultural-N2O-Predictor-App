import joblib
from sklearn.ensemble import RandomForestRegressor
import os
import numpy as np

current_path = os.path.dirname(os.path.realpath(__file__))

base_model = joblib.load('model/base_model.sav') # importing model to predict

def predict(attributes):
    pred = base_model.predict(attributes)
    final_pred = round((np.expm1(pred)[0] - 7.415), 2) # cleaning predicted output
    return final_pred