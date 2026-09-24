##################################################################################################
# KNN :
##################################################################################################

"""
Graf save karav va kayu function?
step:1 read csv 
step:2 features engineering   x = df['Study_Hours','Attendance'] y=df['Result']
        replace : pass 1 fail 0
        map : pass 1 fail 0
step :3 split : 80% train 20% test 
step :4 scale : scaler = StandardScaler() --->  fit ,transform 
step :5 model :  from  skelarn.neighbors import KNeighborsClassifier 
        knn = KNeighborsClassifier(n_neighbors=3)
        
step:6 fit : knn.fit(scale)
step:7 predict : knn.predict(scale)
step:8 accuracy : accuracy_score(y_test,y_pred)
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score

# load data set :
df = pd.read_csv("student_pass (1).csv")
# print(df.head())
# print(df.info())
# print(df.describe())

# Convert categorical values in to numerical values:
df['Result'] = df['Result'].replace({'pass':1,'fail':0})

# Features selection :
X = df[
    ['Study_Hours',
     'Attendance']
]

y = df['Result']

# Split data set :
X_train, X_test, y_train, y_test = train_test_split(X,
                                                    y,
                                                    test_size=0.2,
                                                    random_state=42)


# Scaling the features :
knn = StandardScaler()
X_train_Scale = knn.fit_transform(X_train,y_train)
X_test_Scale = knn.transform(X_test)

# Create model :
model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_train_Scale, y_train)
y_pred = model.predict(X_test_Scale)
print("prediction :", y_pred)

# Probability :
prob = model.predict_proba(X_test_Scale)
print("probability :", prob)

# Accuracy :
accuracy = accuracy_score(y_test, y_pred)
print("accuracy :", accuracy*100)

# Test with new data :
new_data = np.array([[5, 80], [2, 50], [8, 90]])
new_data_scaled = knn.transform(new_data)
new_pred = model.predict(new_data_scaled)
print("new prediction :", new_pred)

