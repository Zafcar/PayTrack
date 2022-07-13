import streamlit as st
from transaction_statistics import *
from transaction_update import *

def main_page():
    st.write("Hello")

def page2():
    st.markdown("# Page 2 ❄️")
    st.sidebar.markdown("# Page 2 ❄️")

def page3():
    st.markdown("# Page 3 🎉")
    st.sidebar.markdown("# Page 3 🎉")

all_pages_created = {
    "Main Page": main_page,
    "Page 2": page2,
    "Page 3": page3,
}


# Created a side bar to select any page 
selected_page = st.sidebar.selectbox("Select a page", all_pages_created.keys())
all_pages_created[selected_page]()