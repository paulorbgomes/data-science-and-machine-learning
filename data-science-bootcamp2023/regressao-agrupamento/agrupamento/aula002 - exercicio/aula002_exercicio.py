# -*- coding: utf-8 -*-
"""aula002_exercicio.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1r3qq7wX--7RVZSuep8bZvAB3qup0snd4
"""

# Bibliotecas
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
from sklearn.cluster import KMeans

# DataSet
data = pd.read_csv("Countries-exercise.csv")
plt.scatter(data["Longitude"], data["Latitude"])
plt.xlabel("Longitude", fontsize=20)
plt.ylabel("Latitude", fontsize=20)
plt.xlim(-180, 180)
plt.ylim(-90, 90)
plt.show()

# Organização das Variáveis
data
x = data.iloc[:,1:3]
x

# Agrupamento Usando K-Means
kmeans = KMeans(8)
kmeans.fit(x)
clusters = kmeans.fit_predict(x)

# Organização do Resultado como DataFrame
data_clusters = data.copy()
data_clusters["Cluster"] = clusters
data_clusters

# Visualização do Resultado
plt.scatter(data_clusters["Longitude"], data_clusters["Latitude"], c=data_clusters["Cluster"], cmap="rainbow")
plt.xlabel("Longitude", fontsize=20)
plt.ylabel("Latitude", fontsize=20)
plt.xlim(-180, 180)
plt.ylim(-90, 90)
plt.show()