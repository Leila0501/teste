import requests as rq
url = 'https://github.com/Leila0501/teste/blob/main/BR_LQs_CD2022.csv'
resposta = rq.get(url)

import streamlit as st
st.title("Localização das comunidades quilombolas (2022)")

import pandas as pd
df = pd.read_csv(url)
df

x = st.slider('Selecione um número', 0,100)
df.head(x)


