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
    
    The color of each dot represents the value of the feature for that particular observation. Blue dot indicate
    lower value and Red dot indicate higher value for a particular observation.
    
    Dots to the right of the center line indicate those observations that has a positive impact on the output, and
    the dots to the left of the center line indicate those observations that negatively impacts the output.
    """)

    st.image("plots/summaryplot.png")

    st.write("""
    From the above figure, we observe that 'NH4' is the most impactful feature that is contributing to the model output.
    Higher values of 'NH4' has a high and positive impact on the model output. The same is applicable for 'SOM', 'WFPS' and 'NO3' as well.
    But 'WFPS' has more number of lower values that are negatively impacting the model output.
    
    For 'PP7' and 'AIRT', some of the lower values have a considerable positive impact on the model output though most of them have a 
    negative impact on the output.
    
    On the contrary, higher values of 'DAFSD' has shown to have a negative impact on the model output with some exceptions. And, lower
    values have a positive impact on the model output.
    
    These observations indicate that the atmospheric N2O released from intensively managed agricultural systems has:
    1. A higher dependency on the ammonia and moisture content of the soil and higher atmospheric temperatures.
    2. Lower dependancy on the number of days after fertilizer application.
    """)

    st.markdown('---')

    st.markdown("<h2>Feature Dependancy Plots</h2>", unsafe_allow_html=True)

    st.write(""" This plot shows the interaction between a given feature and the target. The plot also shows the interaction between the given feature
    and a second feature with which the given feature interact has the most interaction.
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
    It is observed that: 
    
    1. Lower values of 'NH4' has a positive linear relationship with the model output.
    
    2. 'NH4' interacts the most with 'PP7'
    
    3. Lower values of 'NH4' along with higher values of 'PP7' contributes to higher predicted values for the output.
    
    4. 'SOM' interacts the most with 'WFPS'
    
    5. Few higher values of 'SOM' and 'WFPS' result in higher values for the output.
    
    6. 'PP7' interacts the most with 'NH4'
    
    7. For 'PP7' values less than 1, lower values of 'NH4' gives a higher output compared to higher values of 'NH4'.
    
    8. For 'PP7' values greater than 1, higher values of 'NH4' gives a higher output compared to lower values of 'NH4'.
    
    9. 'DAFSD' interacts the most with 'WFPS' and not much relationship is found for 'DAFSD' with the target.
    
    10. 'WFPS' interacts the most with 'NO3'.
    
    11. For lower values of 'WFPS', higher values of 'NO3' results in a lower predicted output and for higher values of 'WFPS', 
    higher values of 'NO3' results in a higher predicted output.
    
    12. 'AIRT' interacts the most with 'PP7' and has a slightly positive linear relationship with the output.
    
    13. 'NO3' interacts the most with 'PP7' and does not have much relationship with the target.
    """)
