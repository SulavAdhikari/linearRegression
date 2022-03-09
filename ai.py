import pandas as pd
import numpy as np

def line_eqn(m, x, c):
    return float(m*x + c)

def predict(X):
    df = pd.read_csv('houseprices.csv')
    Xi = df['area']
    Yi = df['price']
    N = len(Xi)

    xArray = np.array(Xi)
    yArray = np.array(Yi)

    sumX = 0 
    sumX2 = 0 
    sumY = 0 
    sumXY = 0 
    
    for i in range(N):
        sumX = sumX + xArray[i]
        sumX2 = sumX2 + xArray[i]**2
        sumY = sumY +yArray[i]
        sumXY = sumXY + xArray[i] * yArray[i]


    M = (N * sumXY - sumX * sumY) / (N * sumX2 - sumX * sumX)
    C = (sumY - M * sumX) / N

    

    y = line_eqn(M, float(X), C)
    return int(y)

