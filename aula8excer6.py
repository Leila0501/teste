import requests as rq
url = 'https://raw.githubusercontent.com/adrianalite/datasets/main/BR_LQs_CD2022.csv.'
resposta = rq.get(url)
!pip install streamlit

import streamlit as st
st.title("Localização das comunidades quilombolas (2022)")

import pandas as pd
df = pd.read_csv('/content/BR_LQs_CD2022i.csv')
x = st.slider('Selecione um número', 0,8441)
df.head(x)
