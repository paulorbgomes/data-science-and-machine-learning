# -*- coding: utf-8 -*-
"""aula004_exercicio.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1d8m17Qx0r4GSNF4QRQT85YXlIaEXBbLJ
"""

# Bibliotecas
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
sns.set()

from scipy import stats
stats.chisqprob = lambda chisq, df: stats.chi2.sf(chisq, df)

# Dados
raw_data = pd.read_csv("Bank-data.csv")
raw_data
data = raw_data.copy()
data = data.drop(["Unnamed: 0"], axis = 1)
data["y"] = data["y"].map({"yes":1, "no":0})
data
#data.describe()
y = data["y"]
x1 = data["duration"]

# Regressão Logística
x = sm.add_constant(x1)
results = sm.Logit(y,x).fit()
results.summary()