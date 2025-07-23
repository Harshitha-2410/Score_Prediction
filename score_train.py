import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import joblib

df=pd.read_csv("students_old one.csv")
# print(df.head())
df=pd.get_dummies(df,columns=["gender"],drop_first=True)
print(df.head())
x=df.drop("score",axis=1)
y=df["score"]
# print(x)
# print(y)
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)
r=RandomForestRegressor(n_estimators=100)
r.fit(x_train,y_train)
joblib.dump(r,"score_train_model.pkl")
