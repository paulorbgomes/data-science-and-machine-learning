# -*- coding: utf-8 -*-
"""aula002_regressaoLogistica.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1yDCFbZ0btXse4fucB4BYxtJKnouJKYwj
"""

# Bibliotecas
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
import seaborn as sns
sns.set()

# Dados
raw_data = pd.read_csv("2.01. Admittance.csv")
data = raw_data.copy()
data["Admitted"] = data["Admitted"].map({"Yes":1, "No":0})
data

# Declaração as Variáveis Dependentes e Independentes
y = data["Admitted"]
x1 = data["SAT"]
plt.scatter(x1,y)
plt.xlabel("SAT", fontsize=20)
plt.ylabel("Admitted", fontsize=20)
plt.show()

# Modelo de Regressão Logística (utilizando statsmodels)
x = sm.add_constant(x1)
results = sm.Logit(y,x).fit()
results.summary()

yhat = np.exp(results.params[0] + results.params[1]*x1) / (1 +np.exp(results.params[0] + results.params[1]*x1))
f_sorted = np.sort(yhat)
x_sorted = np.sort(np.array(x1))

plt.scatter(x1,y)
plt.xlabel("SAT", fontsize=20)
plt.ylabel("Admitted", fontsize=20)
fig = plt.plot(x_sorted,f_sorted, lw=3, c="red", label="Regressão Logística")
plt.show()