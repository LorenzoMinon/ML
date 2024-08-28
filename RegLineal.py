import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor



# Load the data
gdp_per_capita = pd.read_excel("gdp.xlsx", thousands=',', na_values="n/a") # GDP per capita dataframe!!

# Prepare the data

country_stats = gdp_per_capita[['GDP per capita', 'Satisfaction Rate']]
country_stats = country_stats.dropna() # drop the rows with missing values
X = np.c_[country_stats['GDP per capita']] # GDP per capita
y = np.c_[country_stats['Satisfaction Rate']] # Satisfaction rate
#why np.c_?? concatenate along the second axis 
#(column-wise) and np.r_ concatenate along the first axis (row-wise)
# why X mayusc and y minusc?? X is a matrix and y is a vector.

# Visualize the data
country_stats.plot(kind='scatter', x='GDP per capita', y='Satisfaction Rate')
# plt.show()

# Select a linear model
lin_reg_model = LinearRegression()

# Train the model
lin_reg_model.fit(X, y) # fit the model to the data

#Make a prediction for Argentina 
X_new = [[23000]] # Argentina's GDP per capita
print(lin_reg_model.predict(X_new)) # Argentina's predicted satisfaction rate



# Cómo aplicar K-Nearest Neighbors en lugar de regresión lineal:

# Select a K-Nearest Neighbors model
knn_model = KNeighborsRegressor(n_neighbors=3)  # Aquí se elige k=3, pero puedes ajustar este valor
# Train the model
knn_model.fit(X, y)
# Make a prediction for Argentina
print(knn_model.predict(X_new))  # Argentina's predicted satisfaction rate


# Visualize the models
plt.scatter(X, y)
plt.plot(X, lin_reg_model.predict(X), color='red', label='Linear Regression')
plt.plot(X, knn_model.predict(X), color='green', label='K-Nearest Neighbors')
plt.xlabel('GDP per capita')
plt.ylabel('Satisfaction Rate')
plt.legend()
plt.show()