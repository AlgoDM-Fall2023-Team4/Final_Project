import streamlit as st
from streamlit_pills import pills
import re


def main():

    # Streamlit app
    

    # Title of the Page
    
    st.title("ArtWork Based on Genre")

    "### Select your Preference" 



    options = [
        "",  # Dummy option to ensure nothing is selected by default
        "Abstract",
        "Mythological Painting",
        "Bird & Flower painting",
        "Cityscape",
        "Landscape",
        "Religious Painting",
    ]

    selected = pills("Select a category", options)
    st.write("You selected:", selected)

    # Display content based on the selected pill
    if selected == "Abstract":
        st.write("Displaying content for Abstract")
        # Add content for Abstract here

    elif selected == "Mythological Painting":
        st.write("Displaying content for Mythological Painting")
        # Add content for Mythological Painting here

    elif selected == "Bird & Flower painting":
        st.write("Displaying content for Bird & Flower painting")
        # Add content for Bird & Flower painting here

    elif selected == "Cityscape":
        st.write("Displaying content for Cityscape")
        # Add content for Cityscape here

    elif selected == "Landscape":
        st.write("Displaying content for Landscape")
        # Add content for Landscape here

    elif selected == "Religious Painting":
        st.write("Displaying content for Religious Painting")
        # Add content for Religious

    # Integrate the RAG model chatbot with the below example



