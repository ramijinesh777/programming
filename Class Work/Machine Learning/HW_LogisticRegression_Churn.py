########################################################################################################
# LogisticRegression ----- Churn_Modelling 
########################################################################################################
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score

# load data set :
df = pd.read_csv("Machine Learning/Churn_Modelling.csv")
# print(df.head())
# print(df.info())
# print(df.describe())

# Convert categorical values in to numerical values:
df['Gender'] = df['Gender'].replace({'Male':0,'Female':1})
df['Geography'] = df['Geography'].replace({'France':0,'Spain':1,'Germany':2})

# Features selection :
X = df[
    ['CreditScore',
     'Geography',
     'Gender',
     'Age',
     'Tenure',
     'Balance',]
]

y = df['Exited']

# Split data set :
X_train, X_test, y_train, y_test = train_test_split(X,
                                                    y,
                                                    test_size=0.2,
                                                    random_state=42)


# Scaling the features :
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Create model :
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print("prediction :", y_pred)

# Probability :
prob = model.predict_proba(X_test)
print("probability :", prob)

# Accuracy :
accuracy = accuracy_score(y_test, y_pred)
print("accuracy :", accuracy*100)

# Test with new data :
new_data = np.array([[600, 1, 0, 40, 3, 50000]])
new_data = scaler.transform(new_data)
new_pred = model.predict(new_data)
print("new prediction :", new_pred)

