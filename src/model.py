import joblib
import lightgbm
import os
from sklearn.preprocessing import StandardScaler
import numpy as np

current_path = os.path.dirname(os.path.realpath(__file__))

feat_scalar = joblib.load('model/standard_scalar.sav')
base_model = joblib.load('model/base_model.sav')

def predict(attributes: np.array):
    scaled_attributes = feat_scalar.transform(attributes)
    pred = base_model.predict(scaled_attributes)
    final_pred = round((np.expm1(pred)[0] - 7.415), 2)
    return final_pred