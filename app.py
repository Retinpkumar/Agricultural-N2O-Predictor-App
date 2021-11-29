import streamlit as st
from src.model import predict
import numpy as np
import pandas as pd

st.set_page_config(page_title="Agricultural N2O Flux Predictor",
                   page_icon="🌱",
                   layout="centered")

st.title(f"Agricultural Flux Predictor App") # page header


with st.form("Prediction_form"):

    st.header("Enter the input factors:") # form header
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
    clay = st.number_input("Clay: (Clay content in g/kg)")
    sand = st.number_input("Sand: (Sand content in g/kg)")
    som = st.number_input("SOM: (Soil organic matter concentration in %)")

    submit_val = st.form_submit_button("Predict")

if submit_val:
    # for season
    if season=='Spring':
        feat_season = [1, 0, 0]
    elif season=='Summer':
        feat_season = [0, 1, 0]
    elif season=='Winter':
        feat_season = [0, 0, 1]
    else:
        feat_season = [0, 0, 0]

    # for vegetation
    if veg=='Corn':
        feat_veg=0
    else:
        feat_veg=1

    # for nrate
    if nrate<170:
        feat_nrate=1
    else:
        feat_nrate=0

    # for clay
    if clay<=62:
        feat_clay=[0,0]
    elif clay>62 and clay<=128:
        feat_clay=[1,0]
    else:
        feat_clay=[0,1]

    # for sand
    if sand <= 125:
        feat_sand = [0, 0]
    elif sand > 125 and sand <= 491:
        feat_sand = [1, 0]
    else:
        feat_sand = [0, 1]

    # for som
    if som < 2:
        feat_som = 0
    else:
        feat_som = 1

    # list of features
    feats = ['PP2', 'PP7', 'AirT', 'WFPS25cm', 'NH4', 'NO3', 'Mean_DAF',
             'Season_Spring', 'Season_Summer', 'Season_Winter', 'Vegetation_Others',
             'N_rate_1', 'Clay_2', 'Clay_3', 'Sand_2', 'Sand_3', 'SOM_1']

    # list of corresponding input values
    attribute_vals = [pp2, pp7, airt, wfps, nh4, no3, mean_daf,
                          feat_season[0], feat_season[1], feat_season[2],
                          feat_veg,
                          feat_nrate,
                          feat_clay[0], feat_clay[1],
                          feat_sand[0], feat_sand[1], feat_som]

    # dictionary of features and values
    attr_dict = dict(zip(feats, attribute_vals))

    # dataframe for scaling and model input
    attr_df = pd.DataFrame(attr_dict, index=[1])

    # predicted value from the model
    value = predict(attributes=attr_df)

    st.header("Here are the results: ") # results header
    # output results
    st.success(f"The Atmospheric Nitrous Oxide Concentration for the given inputs is: {value} ppb/yr")
    st.balloons()
