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
'''print(base_credito.head(10)) #ver os 10 primeiros
print(base_credito.tail(10)) #ver os 10 ultimos
print(base_credito.describe()) #descricao geral dos dados
print(base_credito[base_credito['income'] >= 69995.685578]) #cliente com maior renda anual
print((base_credito[base_credito['loan'] <= 1.377630])) #cliente com menor divida'''

#visualizacao dos dados
print(np.unique(base_credito['default'], return_counts=True))
print(sns.countplot(x = base_credito['default']))
print(plt.hist())
