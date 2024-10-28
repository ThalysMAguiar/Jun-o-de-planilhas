import pandas as pd

# MODO MAIS TRABALHOSO

# Lê o arquivo Excel do setor comercial
# despesas_comerciais = pd.read_excel('Setor_Control.xlsx')
# despesas_comerciais['Setor'] = 'Control'

# Lê o arquivo Excel do setor financeiro
# despesas_financeiro = pd.read_excel('Setor_Financeiro.xlsx')
# despesas_financeiro['Setor'] = 'Financeiro'

# Concatena os DataFrames e redefine os índices
# despesas_agregadas = pd.concat([despesas_comerciais, despesas_financeiro], ignore_index=True)

# Imprime o DataFrame agregado
# print(despesas_agregadas)

areas = ['Control', 'Financeiro', 'RH', 'T.I']
despesas_total = pd.DataFrame()
for i in areas:
    despesa = pd.read_excel('Setor_'+i+'.xlsx')
    despesa['Setor'] = i
    despesas_total = pd.concat([despesas_total, despesa], ignore_index=True)

despesas_total.to_excel('Despesas Total.xlsx', index=False)