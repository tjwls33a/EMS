import numpy as np
import matplotlib.pyplot as myPlot
import pandas as pd
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

global Expect2

myData = pd.read_csv('consumer1.csv')
myData['date'] = pd.to_datetime(myData['date'])
myData['date'] = myData['date'].dt.month

x2 = myData.iloc[:,0:1].values
y2 = myData.iloc[:,3].values

X_poly2 = PolynomialFeatures(degree=3).fit_transform(x2)
myModel_poly = LinearRegression().fit(X_poly2,y2)
Predict2 = myModel_poly.predict(X_poly2)

SUM2 = 0
Mean2 = list()
Predict2 = list(Predict2)

for j in range(0,12):
    for i in range(j,84,12):
        SUM2 = SUM2 + Predict2[i]
    Mean2.append(SUM2 / 7)
    SUM2 = 0

MONTH2 = int(input('What month is next month? '))

Expect2 = Mean2[MONTH2-1]
print("Next month's estimated electricity consumption : ", Expect2)