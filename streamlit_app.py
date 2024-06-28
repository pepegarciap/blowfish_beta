import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import altair as alt
import time
import zipfile

# Page title
st.set_page_config(page_title='Blowfish', page_icon='🐡')
st.title('🐡 Welcome to Blowfish!')

st.header('Step 1: Choose your starting points')

#all_iata_df = pd.read_excel("data/airport_codes.xlsx")

aeropuertos_df = pd.read_csv("data/aeropuertos_v02.csv", encoding='utf-8')


if 'counter' not in st.session_state:
    st.session_state.counter = 0

# Añadir tres campos de entrada
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    data1 = st.selectbox("Country", aeropuertos_df.Country.unique())
    data21 = st.selectbox("Country ", aeropuertos_df.Country.unique())
with col2:
    data2 = st.selectbox("City", aeropuertos_df[aeropuertos_df.Country == data1].City.unique())
    data22 = st.selectbox("City ", aeropuertos_df[aeropuertos_df.Country == data21].City.unique())
with col3:
    data3 = st.number_input("# of passengers", step=1, min_value=0, format="%d")
    data23 = st.number_input("# of passengers ", step=1, min_value=0, format="%d")
with col4:
    data4 = st.date_input("Departure date", format="DD/MM/YYYY")
    data24 = st.date_input("Departure date ", format="DD/MM/YYYY")
    if st.button("Add starting point"):
        st.session_state.counter += 1
with col5:
    data5 = st.date_input("Arrival date", format="DD/MM/YYYY")
    data25 = st.date_input("Arrival date ", format="DD/MM/YYYY")
    if st.button("Drop starting point"):
        st.session_state.counter -= 1




st.write(f"Contador: {st.session_state.counter}")








