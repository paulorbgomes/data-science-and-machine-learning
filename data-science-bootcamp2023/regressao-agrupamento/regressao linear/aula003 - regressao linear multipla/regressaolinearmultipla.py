# -*- coding: utf-8 -*-
"""regressaoLinearMultipla.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18Ld68SjlScpuDglRdNHfHmMmC5Vvl9Qo
"""

# Bibliotecas
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
import seaborn as sns
sns.set()

# Dados
data = pd.read_csv("1.02. Multiple linear regression.csv")
data
y = data["GPA"]
x1 = data[["SAT", "Rand 1,2,3"]]

# Regressão Linear Múltipla (utilizando o statsmodels)
x = sm.add_constant(x1)
results = sm.OLS(y, x).fit()
results.summary()