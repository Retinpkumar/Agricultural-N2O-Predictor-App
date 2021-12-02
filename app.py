import streamlit as st
from src.model import predict
from src.transformer import input_transformer
import numpy as np
import pandas as pd
# page settings
st.set_page_config(page_title="Agricultural N2O Flux Predictor",
                   page_icon="🌱",
                   layout="centered")
# page header
st.title(f"Agricultural Flux Predictor App")


with st.form("Prediction_form"):
    # form header
    st.header("Enter the input factors:")
    # input elements
    pp2 = st.number_input("PP2: (Cumulative precipitation in the last two days before gas sampling in mm): ")
    pp7 = st.number_input("PP7: (Cumulative precipitation in the last week before gas sampling in mm)")
    airt = st.number_input("AirT: (Mean daily air temperature in °C)")
    wfps = st.number_input("WFPS25cm: (Water filled pore space in the top 25cm soil layer.)")
    nh4 = st.number_input("NH4: (Ammonium Nitrogen content in the top 25cm soil layer in kg/ha)")
    no3 = st.number_input("NO3: (Nitrate Nitrogen content in the top 25cm soil layer in kg/ha)")
    mean_daf = st.number_input("Mean_DAF: (Average days after Nitrogen fertilization)")
    season = st.selectbox("Season: ",["Summer", "Winter", "Spring", "Fall"])
    veg = st.selectbox("Vegetation: ", ["Corn", "Others"])
    nrate = st.number_input("N_rate: (Nitrogen fertilizer application rate in kg/ha)")
    som = st.number_input("SOM: (Soil organic matter concentration in %)")
    # submitting values
    submit_val = st.form_submit_button("Predict")

if submit_val:
    # for season
    if season=='Spring':
        feat_season = 2
    elif season=='Summer':
        feat_season = 3
    elif season=='Winter':
        feat_season = 1
    else:
        feat_season = 4

    # for vegetation
    if veg=='Corn':
        feat_veg=1
    else:
        feat_veg=2

    # for nrate
    if nrate<170:
        feat_nrate=1
    else:
        feat_nrate=2

    # for som
    if som < 2:
        feat_som = 1
    else:
        feat_som = 2

    # list of features
    feats = ['pp2', 'pp7', 'airt', 'wfps', 'nh4', 'no3', 'mean_daf', 'season', 'veg', 'nrate', 'som']
    # list of corresponding input values
    attribute_vals = [pp2, pp7, airt, wfps, nh4, no3, mean_daf, feat_season, feat_veg, feat_nrate, feat_som]
    # dictionary of features and values
    attr_dict = dict(zip(feats, attribute_vals))
    # dataframe for scaling and model input
    attr_df = pd.DataFrame(attr_dict, index=[1])
    # getting values from training data to transform incoming inputs
    train_df = input_transformer()
    # transforming incoming inputs
    for feat in ['pp2', 'pp7', 'nh4', 'no3', 'mean_daf',]:
        # log transform
        attr_df[feat] = np.log1p(attr_df[feat])
        # capping upper and lower values
        attr_df[feat] = np.where(attr_df[feat]>max(train_df[feat]), max(train_df[feat]),
                            np.where(attr_df[feat]<min(train_df[feat]), min(train_df[feat]), attr_df[feat]))

    # predicted value from the model
    value = predict(attributes=attr_df)
    # results header
    st.header("Result: ")
    # output results
    st.success(f"Agricultural N2O Flux is predicted to be about {value} ppb/yr")
    st.balloons()
