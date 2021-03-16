# imports
import streamlit as st
import cv2
import csv
from PIL import Image
import pandas as pd
from tensorflow.keras.preprocessing.text import Tokenizer
import time
import os
import numpy as np
from search_module import search
from datetime import time

# sidebar
st.sidebar.image("../../assets/logo.png")
st.sidebar.header("Search Module")
st.sidebar.subheader(
    "An interactive search application to get location, time and description of the incident in focus with just the help of a few keywords and time-frame"
)

# Data Uploads
st.header("Data Uploading")
# uploading results
st.subheader("Upload the CCTV Log here")
file = st.file_uploader("logs")
if file is not None:

    # loading results
    @st.cache
    def load_data(nrows):
        data = pd.read_csv(file, nrows=nrows)
        lowercase = lambda x: str(x).lower()
        data.rename(lowercase, axis="columns", inplace=True)
        return data

    data_load_state = st.text("")
    data = load_data(10000)

    # seeing data
    st.subheader("Raw data")
    st.write(data)

# sample cctv map
st.subheader("Upload the CCTV Co-ordinates here")
cctv_map = st.file_uploader("co-ordinates")
if cctv_map is not None:
    st.subheader("CCTV Map")
    df = pd.read_csv(cctv_map)
    st.map(df)

# Search
st.header("Searching Logs")

# keywords
st.subheader("Enter the keywords of the incident")
st.text_input("")
# time
st.subheader("The time where the incident might have occured")
footage_time = st.slider("", value=(time(9, 30), time(13, 30)))

# starting the search process
if st.button("Start Search"):
    st.write("Results")
