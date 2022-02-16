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
            'Navigation Dropdown', 
            self.pages, 
            format_func=lambda page: page['title'])
        # run the app function 
        page['function']()