import streamlit as st
import pandas as pd
df = pd.read_csv('/content/BR_LQs_CD2022i.csv')
x = st.slider('Selecione um número', 0,8441)
df.head(x)
