import joblib
import lightgbm
import os
from sklearn.preprocessing import StandardScaler
import numpy as np

current_path = os.path.dirname(os.path.realpath(__file__))

feat_scalar = joblib.load('model/standard_scalar.sav') #importing model to scale
base_model = joblib.load('model/base_model.sav') # importing model to predict

def predict(attributes):
    scaled_attributes = feat_scalar.transform(attributes) # scaling inputs
    pred = base_model.predict(scaled_attributes) # predicting output using model
    final_pred = round((np.expm1(pred)[0] - 7.415), 2) # cleaning predicted output
    return final_pred