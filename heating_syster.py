import numpy as np
import matplotlib.pyplot as myPlot
import pandas as pd
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

global Expect

myData = pd.read_csv('consumer1.csv')
myData['date'] = pd.to_datetime(myData['date'])
myData['date'] = myData['date'].dt.month

x = myData.iloc[:, 0:1].values
y = myData.iloc[:,2].values

X_poly = PolynomialFeatures(degree=3).fit_transform(x)
myModel_poly = LinearRegression().fit(X_poly,y)
Predict = myModel_poly.predict(X_poly)

SUM = 0
Mean = list()
Predict = list(Predict)

for j in range(0,12):
    for i in range(j,84,12):
        SUM = SUM + Predict[i]
    Mean.append(SUM / 7)
    SUM = 0

MONTH = int(input('What month is next month? '))

Expect = Mean[MONTH-1]
print("Next month's estimated heating consumption : ", Expect)