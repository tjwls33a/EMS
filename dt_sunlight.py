#!/usr/bin/env python
# coding: utf-8

# In[58]:

import pandas as pd
import numpy as np
from database2 import Database
import matplotlib.pyplot as plt

def feature_normalize(x):
    mu = x.mean()
    sigma = x.std()
    norm_x = (x-mu)/sigma
    
    return norm_x, mu, sigma

db=Database()
train_data = np.loadtxt('data.CSV', delimiter=',')
real = list(db.show())
real_data = np.array(real)

theta = np.zeros((2,1))
xx = train_data[:, 0, np.newaxis]
y = train_data[:, 1, np.newaxis]
x, mu, sigma = feature_normalize(xx)
#real_data = real_data[np.newaxis]

real_x = (real_data-mu)/sigma
#real_x = real_x[np.newaxis]
x_0 = np.ones((x.shape[0], 1))
X = np.concatenate((x_0, x), axis=1)

real_x_0 = np.ones((real_x.shape[0], 1))
real_X = np.concatenate((real_x_0, real_x), axis=1)

def update_func(theta, x, y, alpha=0.005): 
    m = x.shape[0]
    feature = x.shape[1]
    new_theta = theta
    A = np.zeros((1,feature))
    
    b = np.dot(x, theta)
    c = b - y
    
    A = np.dot(c.T, x)
    new_theta = new_theta - (alpha/m)*A.T
    return new_theta

niter = 1000
for i in range(niter):
    new_theta = update_func(theta, X, y, alpha=0.005)
    theta = new_theta
    
Expect = np.dot(real_X,theta)
print(" <Amount of sunlight>       \n{}\n\n".format(real_data), "<Hypothesis>       \n{}".format(Expect))
Expect = Expect.tolist()
Expect = tuple(Expect)

for i in range(len(real_data)):
    a = float(Expect[i][0])
    print(a)
    db.insert2(a)


plt.ylabel('Energy produced') # y축 레이블 설정
plt.xlabel('Amount of sunlight') # x축 레이블 설정
plt.scatter(x, y, marker='x')  # Scatter 차트, 첫번째 인자는 x축에 해당하는 값을 의미, y축에 해당하는 값을 의미
                               # marker는 데이터를 차트에서 X로 표현
plt.plot(real_x,np.dot(real_X,theta),'r')





