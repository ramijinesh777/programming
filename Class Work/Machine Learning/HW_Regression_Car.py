import pandas as pd
import numpy as np 
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge
from sklearn.linear_model import Lasso
from sklearn.linear_model import ElasticNet
from sklearn.metrics import r2_score,mean_squared_error,mean_absolute_error,mean_absolute_percentage_error

# Read data :
df = pd.read_csv("Machine Learning/CAR DETAILS FROM CAR DEKHO.csv")
df = df.drop("name", axis=1)
# print(df.head(10))

# get dummies :
df = pd.get_dummies(df,columns=['fuel','seller_type','transmission','owner'],drop_first = True)
# print(df.head(10))

# Features and target :
X = df.drop(['selling_price'],axis=1)
y = df['selling_price']

# Split data :
X_train,X_test,y_train,y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Scaler :
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train,y_train)
X_test_scaled = scaler.transform(X_test)

# Function for evaluation :

# Model : 1. Simple Linear Regression
x_linear = df[['year']]
y_linear = df['selling_price']

x_train_linear, x_test_linear, y_train_linear, y_test_linear = train_test_split(
    x_linear,
    y_linear,
    test_size=0.2,
    random_state=42
)

model = LinearRegression()
model.fit(x_train_linear, y_train_linear)
pred = model.predict(x_test_linear)

print("coefficients:", model.coef_[0])
print("intercept:", model.intercept_)
print("R2 Score (Linear Regression):", r2_score(y_test_linear, pred)*100)

# Model : 2. Multiple Linear Regression
multi = LinearRegression()
multi.fit(X_train, y_train)
pred_multi = multi.predict(X_test)

print("R2 Score (Multiple Linear Regression):", r2_score(y_test, pred_multi)*100)

# Model : 3. Lasso Regression
l1 = Lasso(alpha=100, max_iter=10000)
l1.fit(X_train, y_train)
pred_lasso = l1.predict(X_test)

print("R2 Score (Lasso Regression):", r2_score(y_test, pred_lasso)*100)

# Model : 4. Ridge Regression
r1 = Ridge(alpha=1)
r1.fit(X_train, y_train)
pred_ridge = r1.predict(X_test)

print("R2 Score (Ridge Regression):", r2_score(y_test, pred_ridge)*100)
print("Mean Squared Error (Ridge Regression):", mean_squared_error(y_test, pred_ridge)*100)
print("Mean Absolute Error (Ridge Regression):", mean_absolute_error(y_test, pred_ridge)*100)
print("Mean Absolute Percentage Error (Ridge Regression):", mean_absolute_percentage_error(y_test, pred_ridge)*100)     

# Model : 5. Elastic Net Regression
el = ElasticNet(alpha=1, l1_ratio=0.5)
el.fit(X_train, y_train)
pred_elastic = el.predict(X_test)
print("R2 Score (Elastic Net Regression):", r2_score(y_test, pred_elastic)*100)

