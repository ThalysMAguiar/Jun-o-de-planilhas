import pandas as pd



despesas_comerciais = pd.read_excel('Setor_Control.xlsx')
despesas_comerciais['Setor'] = 'Control'

despesas_financeiro = pd.read_excel('Setor_Financeiro.xlsx')
despesas_financeiro['Setor'] = 'Financeiro'

despesas_agregadas = pd.concat([despesas_comerciais, despesas_financeiro], ignore_index=True)

print(despesas_agregadas) 


# Dois blocos de códigos diferentes relacionados a junção de duas ou mais planilhas.


areas = ['Control', 'Financeiro', 'RH', 'T.I']
despesas_total = pd.DataFrame()
for i in areas:
    despesa = pd.read_excel('Setor_'+i+'.xlsx')
    despesa['Setor'] = i
    despesas_total = pd.concat([despesas_total, despesa], ignore_index=True)

despesas_total.to_excel('Despesas Total.xlsx', index=False)