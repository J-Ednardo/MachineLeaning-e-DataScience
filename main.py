import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

'''
Cliente ID = identificação da pessoa
Income = Renda anual da pessoa
Age = Idade
loan = Divida que a pessoa possui
Default =  se pagou ou não o emprestimo
'''

#exploracao dos dados
base_credito = pd.read_csv('credit_data.csv')
print(base_credito.head(10)) #ver os 10 primeiros
print(base_credito.tail(10)) #ver os 10 ultimos
print(base_credito.describe()) #descricao geral dos dados
print(base_credito[base_credito['income'] >= 69995.685578]) #cliente com maior renda anual
print(base_credito[base_credito['loan'] <= 1.377630]) #cliente com menor divida

#visualizacao dos dados
np.unique(base_credito['default'], return_counts=True)
sns.countplot(x = base_credito['default'])
#plt.show()
plt.hist(x = base_credito['age'])
#plt.show()
plt.hist(x = base_credito['income'])
#plt.show()
plt.hist(x = base_credito['loan'])
#plt.show()
grafico = px.scatter_matrix(base_credito, dimensions=['age', 'income', 'loan'], color = 'default')
#grafico.show()
base_credito.loc[base_credito['age'] < 0, 'age'] = 40,92
base_credito['age'].fillna(base_credito['age'].mean(), inplace=True)
