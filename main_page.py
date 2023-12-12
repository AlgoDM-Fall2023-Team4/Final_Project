import streamlit as st
import page1, page2

st.set_page_config("Famous ArtWork Recommendation")

st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Genre based Recommendation", "Artist based Recommendation"])

st.title("Famous ArtWork Recommendation")

if page == "Genre based Recommendation":
    page1.main()
elif page == "Artist based Recommendation":
    page2.main()
