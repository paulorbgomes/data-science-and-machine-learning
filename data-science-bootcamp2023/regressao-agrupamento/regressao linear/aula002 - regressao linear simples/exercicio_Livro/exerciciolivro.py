# -*- coding: utf-8 -*-
"""exercicioLivro.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17a_wBLeHgrLNEvUdXKQ9kriMZGY8AjHr
"""

# Bibliotecas
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
import seaborn as sns
sns.set()

# Dados
data = pd.read_csv("tempo_salarios.csv")
data
data.describe()

# Visualização dos dados
x1 = data["AnosdeExperiencia"]
y = data["Salario"]
plt.scatter(x1, y)
plt.xlabel("Anos de Experiência", fontsize=20)
plt.ylabel("Salário", fontsize=20)
plt.show()

# Regressão Linear Simples (utilizando statsmodel)
x = sm.add_constant(x1)
results = sm.OLS(y, x).fit()
results.summary()

# Plotagem do Modelo de Regressão Linear Simples
plt.scatter(x1, y)
yhat = 9449.9623 * x1 + 2.579e+04
fig = plt.plot(x1, yhat, lw=4, c="orange", label="Regressão Linear Simples")
plt.xlabel("Anos de Experiência", fontsize=20)
plt.ylabel("Salário", fontsize=20)
plt.show()