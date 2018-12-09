import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data=pd.read_csv("Social_Network_Ads.csv");

del  data["User ID"]
del data["Purchased"]

x=data.iloc[:,0:3].values
y=data.iloc[:,-1].values

data=pd.get_dummies(data)

datax=data.iloc[:,[0,2,3]]
datay=data.iloc[:,1]

from sklearn.linear_model import LogisticRegression
classifier=LogisticRegression()
classifier.fit(datax,datay)

final=pd.concat([datax,datay],axis=1)


pred=classifier.predict([[8,0,1]])

'''
from sklearn.externals import joblib
joblib.dump(classifier,"model.pkl")
joblib.dump(data.columns,"model_columns.pkl")

'''