#########################################################################################################
# LogisticRegression
#########################################################################################################

# liner_model import logistic regression 
# read
# x , y 
# split  
# model = logistic regression  
# model.fit  
# model.predict (x) 
# probability = model.predict_proba(x), 
# model.score(x,y), 


import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, classification_report

# read data
df = pd.read_csv("student_pass.csv")
print(df.head(10))

# features and target
X = df[['StudyHours']]
y = df['Pass']

# split data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# model
model = LogisticRegression()
model.fit(X_train, y_train)
y_predict = model.predict(X)

# probability
probability = model.predict_proba(X)
print("Probability:", probability)

# model score
score = model.score(X, y)
print("Model Score:", score)

# accuracy
accuracy = model.score(X_test, y_test)
print("Accuracy:", accuracy)

# Test with new data
new_student = [[4.5]]
prediction = model.predict(new_student)
probability = model.predict_proba(new_student)
print("Prediction :", prediction)
print("Probability :", probability)

import numpy as np
import matplotlib.pyplot as plt

"""
x = np.linspace(-10, 10, 200)  # start -10  end 10  step 200  ----> stop -start /step-1

y = 1 / (1 + np.exp(-x))

plt.figure(figsize=(8,5))
plt.plot(x, y)

plt.title("Sigmoid Function")
plt.xlabel("z")
plt.ylabel("Probability")
plt.grid(True)

plt.show()
"""
import matplotlib.pyplot as plt
import numpy as np

plt.scatter(X, y, color='blue', label='Actual Data')

X_test = np.linspace(X.min(), X.max(), 200).reshape(-1, 1)
y_prob = model.predict_proba(X_test)[:, 1]

plt.plot(X_test, y_prob, color='red', linewidth=2)

plt.axhline(y=0.5, color='green', linestyle='--', label='Threshold = 0.5')

plt.xlabel("Study Hours")
plt.ylabel("Probability of Passing")
plt.title("Logistic Regression with Sigmoid Curve")
plt.legend()

plt.show()