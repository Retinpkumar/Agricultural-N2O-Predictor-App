import streamlit as st
from src.multipage import MultiPage
import model_form
from src import explain_model

# page settings
st.set_page_config(page_title="Agricultural N2O Flux Predictor",
                page_icon="🌱",
                layout="wide")

# Create an instance of the app 
app = MultiPage()

# Title of the main page

st.markdown("<h1 align='center'>🌱 Agricultural N2O flux Prediction App </h1>", unsafe_allow_html=True)
st.image("images/title_image.jpg", use_column_width=True)

st.sidebar.title("App Navigation")
# Add all your applications (pages) here
app.add_page("Make Prediction", model_form.app)
app.add_page("Understand the Model", explain_model.app)
# The main app
app.run()
