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

airports_df = pd.read_excel("data/airport_codes.xlsx")

selected_origin1 = st.selectbox("Choose an option:", airports_df.Nombre)






