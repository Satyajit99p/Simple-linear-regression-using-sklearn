import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets,linear_model
from sklearn.metrics import mean_squared_error

wine=datasets.load_wine()
print(wine.data)

wine_X=wine.data[:,np.newaxis,1]

wine_X_train=wine_X[:-100]
wine_X_test=wine_X[-100:]

wine_Y_train=wine.target[:-100]
wine_Y_test=wine.target[-100:]

model=linear_model.LinearRegression()

model.fit(wine_X_train,wine_Y_train)
wine_predict=model.predict(wine_X_test)

plt.scatter(wine_X_test,wine_Y_test)
plt.plot(wine_X_test,wine_predict)
plt.show()