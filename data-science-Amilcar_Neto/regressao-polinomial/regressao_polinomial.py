# -*- coding: utf-8 -*-
"""regressao_polinomial.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Fm2xHTdggdIPbhpETX67Rsg1bTALbTx3
"""

# Bibliotecas
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

# Dataset
dataset = pd.read_csv("cargo_nivel_salarios.csv")
X = dataset.iloc[:,1:2].values
Y = dataset.iloc[:,2].values

plt.scatter(X, Y)
plt.title("Nível x Salário")
plt.xlabel("Nível")
plt.ylabel("Salário")
plt.show()

# Divisão do dataset em treino e teste
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=0)

# Ajustando o modelo de regressão linear para o dataset de treino
lin_reg = LinearRegression()
lin_reg.fit(X_train, Y_train)

plt.scatter(X, Y)
plt.plot(X_train, lin_reg.predict(X_train), color="red")
plt.title("Nível x Salário")
plt.xlabel("Nível")
plt.ylabel("Salário")
plt.show()

# Ajustando o modelo de regressão polinomial (grau 2) para o dataset de treino
poly_reg = PolynomialFeatures(degree=2)
X_poly = poly_reg.fit_transform(X_train)
poly_reg.fit(X_poly, Y_train)
poly_reg.fit(X_train, Y_train)
lin_reg_2 = LinearRegression()
lin_reg_2.fit(X_poly, Y_train)

plt.plot(X_train, Y_train, "Dr")
plt.plot(X_train, lin_reg_2.predict(poly_reg.fit_transform(X_train)),"^b")
plt.title("Nível x Salário")
plt.xlabel("Nível")
plt.ylabel("Salário")
plt.show()

# Ajustando o modelo de regressão polinomial (grau 4) para o dataset de treino
poly_reg = PolynomialFeatures(degree=4)
X_poly = poly_reg.fit_transform(X_train)
poly_reg.fit(X_poly, Y_train)
poly_reg.fit(X_train, Y_train)
lin_reg_2 = LinearRegression()
lin_reg_2.fit(X_poly, Y_train)

plt.plot(X_train, Y_train, "Dr")
plt.plot(X_train, lin_reg_2.predict(poly_reg.fit_transform(X_train)),"^b")
plt.title("Nível x Salário")
plt.xlabel("Nível")
plt.ylabel("Salário")
plt.show()

# Ajustando o modelo de regressão polinomial (grau 8) para o dataset de treino
poly_reg = PolynomialFeatures(degree=8)
X_poly = poly_reg.fit_transform(X_train)
poly_reg.fit(X_poly, Y_train)
poly_reg.fit(X_train, Y_train)
lin_reg_2 = LinearRegression()
lin_reg_2.fit(X_poly, Y_train)

plt.plot(X_train, Y_train, "Dr")
plt.plot(X_train, lin_reg_2.predict(poly_reg.fit_transform(X_train)),"^b")
plt.title("Nível x Salário")
plt.xlabel("Nível")
plt.ylabel("Salário")
plt.show()

# Ajustando o modelo de regressão polinomial (grau 12) para o dataset de treino
poly_reg = PolynomialFeatures(degree=12)
X_poly = poly_reg.fit_transform(X_train)
poly_reg.fit(X_poly, Y_train)
poly_reg.fit(X_train, Y_train)
lin_reg_2 = LinearRegression()
lin_reg_2.fit(X_poly, Y_train)

plt.plot(X_train, Y_train, "Dr")
plt.plot(X_train, lin_reg_2.predict(poly_reg.fit_transform(X_train)),"^b")
plt.title("Nível x Salário")
plt.xlabel("Nível")
plt.ylabel("Salário")
plt.show()