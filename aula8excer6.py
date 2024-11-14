df = pd.read_csv('https://raw.githubusercontent.com/adrianalite/datasets/main/BR_LQs_CD2022.csv')
import streamlit as st
st.title("Localização das comunidades quilombolas (2022)")

import pandas as pd
df = pd.read_csv(url)
df

x = st.slider('Selecione um número', 0,100)
df.head(x)


