import streamlit as st

# Define the multipage class to manage the multiple apps in our program 
class MultiPage: 
    def __init__(self) -> None:
        """Constructor with a list to store applications as an instance variable."""
        self.pages = []
    
    def add_page(self, title, func) -> None: 
        """Class Method to Add pages to the project"""
        self.pages.append({
                "title": title, 
                "function": func
            })

    def run(self):
        """Dropdown to select the page to run"""
        page = st.sidebar.selectbox(
            '', 
            self.pages, 
            format_func=lambda page: page['title'])
        st.sidebar.markdown('---')

        st.sidebar.markdown("## About the app")
        st.sidebar.write("""
        The app aims at predicting the agricultural nitrous oxide(N2O) emissions from intensively managed cropping systems.
        The dataset used for model training has been obtained from an already existing study conducted by Debashish Saha and others.
        This app was able to improve the model performance from 38% (that was based on the scientific study conducted) to 78%. 
        For more details regarding the codes and notebooks, visit "https://github.com/Retinpkumar".
        """)

        st.sidebar.markdown('---')
        st.sidebar.markdown("## Made by: ")
        st.sidebar.write("Retin P Kumar|November 2021")
        # run the app function 
        page['function']()