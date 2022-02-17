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

        st.sidebar.header("About the app")
        st.sidebar.write("""
        The app is aimed at predicting the agricultural nitrous oxide(N2O) emissions from intensively managed cropping systems.
        The dataset used for training the model has been obtained from an already existing study conducted by Debashish Saha and others.
        This model used in the app was able to improve the performance(R2 score) from 38% (that was based on the scientific study conducted) to 78%.
        """)

        st.sidebar.markdown('---')
        st.sidebar.info("### Made by:    Retin P Kumar")
        st.sidebar.markdown("[![Github](https://avatars.githubusercontent.com/u/9919?s=280&v=4)](https://github.com/Retinpkumar)")
        # run the app function 
        page['function']()