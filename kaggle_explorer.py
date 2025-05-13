import streamlit as st
import pandas as pd
import os
from kaggle.api.kaggle_api_extended import KaggleApi
from dotenv import load_dotenv

# Lade .env-Datei
load_dotenv()
username = os.getenv("KAGGLE_USERNAME")
key = os.getenv("KAGGLE_KEY")

# Authentifiziere
api = KaggleApi()
api.authenticate()

# Dataset-ID
DATASET_ID = "anderas/lego-database"
CSV_FILE = "lego/sets.csv"

# Herunterladen (falls nötig)
if not os.path.exists("lego"):
    api.dataset_download_files(DATASET_ID, unzip=True)

# Daten laden
df = pd.read_csv(CSV_FILE)

# Streamlit UI
st.title("🧱 Lego-Datensätze erkunden")
year = st.selectbox("Jahr auswählen", sorted(df['year'].dropna().unique()))
theme = st.selectbox("Thema auswählen", sorted(df['theme_id'].dropna().unique()))

filtered = df[(df['year'] == year) & (df['theme_id'] == theme)]
st.dataframe(filtered)

st.bar_chart(filtered['num_parts'])
