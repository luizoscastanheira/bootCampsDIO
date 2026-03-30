## Biblioteca SCIKIT-LEARN
# Muit usado em aprendizagem de máquina

import matplotlib.pyplot as plt

from sklearn.datasets import make_regression

from sklearn.linear_model import LinearRegression

x, y = make_regression(n_samples=200, n_features=1, noise=30)

# criando um modelo
modelo = LinearRegression

# mostrando no gráfico
plt.scatter(x,y)
plt.show()