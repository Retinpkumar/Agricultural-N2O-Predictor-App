import streamlit as st
from src.model import predict
from src.scaler import input_scaler
import numpy as np
import pandas as pd
import shap
import pickle
import matplotlib.pyplot as plt

# page settings
st.set_page_config(page_title="Agricultural N2O Flux Predictor",
                page_icon="🌱",
                layout="centered")
# page header
st.sidebar.title("Agricultural N2O Flux Predictor App")


with st.sidebar.form("Prediction_form"):
    # form header
    st.header("Enter the input factors:")
    # input elements
    nh4 = st.number_input("NH4: (Ammonium Nitrogen content in the top 25cm soil layer in kg/ha)")
    som = st.number_input("SOM: (Soil organic matter concentration in %)")
    pp7 = st.number_input("PP7: (Cumulative precipitation in the last week before gas sampling in mm)")
    dafsd = st.number_input("DAFSD: (Days after side dressed Nitrogen fertilization)")
    wfps = st.number_input("WFPS25cm: (Water filled pore space in the top 25cm soil layer.)")
    airt = st.number_input("AirT: (Mean daily air temperature in °C)")
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
        st.balloons()
    
st.subheader("Contribution of features to the model")
st.image("plots/summaryplot.png",use_column_width=True)

st.subheader("Feature Dependancy Plots",)
from PIL import Image
image1 = Image.open('plots/nh4_dep_plot.png')
image2 = Image.open('plots/som_dep_plot.png')
image3 = Image.open('plots/pp7_dep_plot.png')
image4 = Image.open('plots/dafsd_dep_plot.png')
image5 = Image.open('plots/wfps_dep_plot.png')
image6 = Image.open('plots/airt_dep_plot.png')
image7 = Image.open('plots/no3_dep_plot.png')

st.image(image1, caption='NH4 dependancy plot', use_column_width=True)

st.image(image2, caption='SOM dependancy plot', use_column_width=True)


st.image(image2, caption='PP7 dependancy plot', use_column_width=True)


st.image(image4, caption='DAFSD dependancy plot', use_column_width=True)


st.image(image5, caption='WFPS dependancy plot', use_column_width=True)


st.image(image6, caption='AIRT dependancy plot', use_column_width=True)


st.image(image7, caption='NO3 dependancy plot', use_column_width=True)
