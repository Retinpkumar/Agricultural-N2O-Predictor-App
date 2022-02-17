import streamlit as st
from PIL import Image

def app():
    st.markdown("<h2 align='center'>Model Explanation using Explainable AI</h2>", unsafe_allow_html=True)
    st.write("""
    Explainable AI helps in comprehending the model output and its expected impact. It also helps with understanding the 
    marginal contribution  of each feature that has been used for building the model.

    In this app, I have used an explainable AI tool named 'SHAP' for interpreting our model output and also in understanding the 
    interaction between the model features. The interpretation for the model output is provided alonside the model prediction.

    In this page, you will find the details regarding the importance and contribution of each feature that has been used for building
    the model. Also, you will find the interactions between various features with the help of feature dependancy plots.
    """)
    st.markdown("---")

    st.markdown("<h2>Contribution of features to the model</h2>", unsafe_allow_html=True)

    st.write("""
    This plot displays the summary of the impact of top features in a dataset on the model prediction. 
    Each dot represents each individual observation in the dataset.

    Blue points indicate those observations that fail to contribute to the model and 
    red ones indicate those that aided the model.

    The features are arranged in the decreasing order of priority and hence the topmost feature is
    the most important one.
    """)

    st.image("plots/summaryplot.png")

    st.write("""
    From the above figure, we observe that 'NH4' followed by 'SOM' and 'PP7' are the 3 the most important feature 
    that is contributing to the model.

    This supports the fact that atmospheric N2O released from intensively managed agricultural systems is due to the organic
    decomposition of ammonium rich fertilizers. 
    """)

    st.markdown('---')

    st.markdown("<h2>Feature Dependancy Plots</h2>", unsafe_allow_html=True)

    st.write(""" This plot shows the interaction between two features and the data points from this interaction 
    that are contributing to the model.
    """)

    image1 = Image.open('plots/nh4_dep_plot.png')
    image2 = Image.open('plots/som_dep_plot.png')
    image3 = Image.open('plots/pp7_dep_plot.png')
    image4 = Image.open('plots/dafsd_dep_plot.png')
    image5 = Image.open('plots/wfps_dep_plot.png')
    image6 = Image.open('plots/airt_dep_plot.png')
    image7 = Image.open('plots/no3_dep_plot.png')

    col1, col2, col3 = st.columns(3)
    with col1:
        st.image(image1, caption='NH4 dependancy plot', use_column_width=True)
    with col2:
        st.image(image2, caption='SOM dependancy plot', use_column_width=True)
    with col3:
        st.image(image3, caption='PP7 dependancy plot', use_column_width=True)

    col4, col5, col6, col7 = st.columns(4)
    with col4:
        st.image(image4, caption='DAFSD dependancy plot', use_column_width=True)
    with col5:
        st.image(image5, caption='WFPS dependancy plot', use_column_width=True)
    with col6:
        st.image(image6, caption='AIRT dependancy plot', use_column_width=True)
    with col7:
        st.image(image7, caption='NO3 dependancy plot', use_column_width=True)

    st.write("""
    It is observed that lower value of ammonium content and lower to no rainfall results in greater amount of N2O released.
    This is supportive of the fact that a heavy rainfall washes away the soil contents including the fertilizer applied.

    Soil organic matter content depends linearly on the water frontage pore space. The most contributing data points are
    observed for higher values of 'SOM' across all values of 'WFPS'.

    The contribution of 'NH4' and 'PP7' is only for a constant value of 'NH4' across lower values of 'PP7'

    Though much meaningful interaction is not observed for 'DAFSD' against 'WFPS', the remaining three plots show a
    good amount of linear dependancy for the corresponding features.
    """)