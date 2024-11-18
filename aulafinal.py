pandas 
stramlit
request
urlM = ('https://dadosabertos.camara.leg.br/api/v2/deputados?siglaSexo=M&ordem=ASC&ordenarPor=nome')
urlF = ('https://dadosabertos.camara.leg.br/api/v2/deputados?siglaSexo=F&ordem=ASC&ordenarPor=nome')
resposta = req.get(urlM)
resposta2 = req.get(urlF)
dadosJSON = resposta.json()
dadosJSON2 = resposta2.json()
dadosJSON.keys()
dadosJSON2.keys()
dfmulheres = pd.DataFrame(dadosJSON2['dados'])
dfhomens = pd.DataFrame(dadosJSON['dados'])
dfhomens['sexo'] = 'M'
dfmulheres['sexo'] = 'F'  

df = pd.concat([dfmulheres, dfhomens])
opcao = st.selectbox('Escolha o gênero', df['sexo'].unique())
dfFiltro = df[df['sexo']==opcao]
st.title('deputados do sexo' + opcao)
qtde = dfFiltro['siglaUf'].value_counts()
dfUF = pd.DataFrame({'siglaUf':qtde.index, 'qtde':qtde.values})
totalHomens = dfhomens['id'].value_counts().sum()
st.metric('Total de homens', totalHomens)
totalMulheres = dfmulheres['id'].value_counts().sum()
st.metric('Total de mulheres', totalMulheres)
st.bar_chart(dfUF, x='siglaUf', y='qtde', x_label= 'UF', y_label='número de deputados')
