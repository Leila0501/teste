import streamlit as st
st.write ("Hello World!")

st.title("Este é o título do app")
st.header("Este é o subtítulo")
st.subheader("Este é o terceiro subtítulo")
st.markdown("Este é texto")
st.caption("Esta é a a legenda")
st.code("x=2021")
st.latex(r''' a+a r^1+a r^2+a r^3 ''')

x = st.slider('Selecione um número', 0,100)
st.write(x)

st.number_input('Selecione um número', 0,100)
