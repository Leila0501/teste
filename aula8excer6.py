import streamlit as st
import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/adrianalite/datasets/main/BR_LQs_CD2022.csv')
x = st.slider('Selecione um número', 0,8441)
df.head(x)
