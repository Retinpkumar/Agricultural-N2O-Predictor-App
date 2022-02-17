import matplotlib
import streamlit as st
from src.model import predict
from src.scaler import input_scaler
import numpy as np
import pandas as pd
import shap
import os
import pickle
import matplotlib.pyplot as plt
from PIL import Image

curr_path = os.path.dirname(os.path.realpath(__file__))

def app():
    st.markdown("<h2 align='center'> Predict the Agricultural Nitrous Oxide output</h2>", unsafe_allow_html=True)
    with st.form("Prediction_form"):
        # form header
        st.subheader("Input the data for prediction:")
        # input elements
        nh4 = st.number_input("NH4: (Ammonium Nitrogen content in the top 25cm soil layer in kg/ha)")
        som = st.slider("SOM: (Soil organic matter concentration in %)", min_value=0.00, max_value=100.00, step=0.01, value=0.00)
        pp7 = st.number_input("PP7: (Cumulative precipitation in the last week before gas sampling in mm)")
        dafsd = st.slider("DAFSD: (Days after side dressed Nitrogen fertilization)", min_value=0, max_value=365, step=1, value=0)
        wfps = st.number_input("WFPS25cm: (Water filled pore space in the top 25cm soil layer.)")
        airt = st.slider("AirT: (Mean daily air temperature in °C)", min_value=-60.0, max_value=60.0, step=0.01, value=25.0)
        no3 = st.number_input("NO3: (Nitrate Nitrogen content in the top 25cm soil layer in kg/ha)")
        # submitting values
        submit_val = st.form_submit_button("Predict")
        if submit_val:
            # list of features
            feats = ['nh4', 'pp7', 'dafsd', 'wfps', 'no3', 'som', 'airt']
            with open('model/features.pickle', 'wb') as f:
                pickle.dump(feats, f)
            # list of corresponding input values
            attribute_vals = [nh4, pp7, dafsd, wfps,  no3, som, airt]
            # dictionary of features and values
            attr_dict = dict(zip(feats, attribute_vals))
            # dataframe for scaling and model input
            attr_df = pd.DataFrame(attr_dict, index=[1])
        
            # square transform
            attr_df['wfps'] = np.square(attr_df['wfps'])
            # square root transformation
            attr_df['dafsd'] = np.sqrt(attr_df["dafsd"])
            
            # scaling input data
            scaled_df = input_scaler(attr_df)
            with open('model/scaled_df.pickle', 'wb') as f:
                pickle.dump(scaled_df, f)

            # predicted value from the model
            value = predict(attributes=scaled_df)
            
            # results header
            st.header("Result: ")
            # output results
            st.success(f"Predicted Agricultural N2O Flux: {value} ppb/yr")
            
            st.markdown('---')
    
            with open('model/final_model.pickle', 'rb') as f:
                model = pickle.load(f)

            input_attributes = np.array(attribute_vals)
            force_plot_path = '/plots/force_plot.png'

            shap_explainer = shap.TreeExplainer(model)
            shap_model_values = shap_explainer.shap_values(input_attributes)
            shap_model_expected_values = shap_explainer.expected_value

            shap.force_plot(shap_model_expected_values, 
                            shap_model_values, 
                            input_attributes,
                            feats,
                            show=False,
                            matplotlib=True).savefig(curr_path + force_plot_path, bbox_inches='tight')

            st.subheader("Marginal contribution of input features in the prediction")
            force_plot_image = Image.open(curr_path + force_plot_path)
            st.image(force_plot_image)