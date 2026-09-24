##################################################################################################
# decision tree :
##################################################################################################
data = {
    "Hours_Studied": [2, 3, 4, 5, 6, 1, 7, 2, 8, 3,
                      5, 6, 1, 4, 7, 8, 2, 3, 6, 5],

    "Attendance": [60, 65, 70, 75, 80, 50, 85, 55, 90, 60,
                   78, 82, 52, 72, 88, 92, 58, 63, 84, 76],

    "Result": ["Fail", "Fail", "Pass", "Pass", "Pass",
               "Fail", "Pass", "Fail", "Pass", "Fail",
               "Pass", "Pass", "Fail", "Pass", "Pass",
               "Pass", "Fail", "Fail", "Pass", "Pass"]
}

"""
from sklearn.tree import DecisionTreeClassifier
    1. crearea ----> geini ,entropy ,log_loss
    2. max_depth ---->    for loop  
    3. ranodm_state ---->  random forest

"""
# step :1 df 
# step :2 split 
# step :3 scaler
# step :4 model 
# step :5 fit  , predict 
# step :6 accuracy score
# step : 7 new  data   ----> 5.5 , 78 

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.tree import plot_tree

# Select D=data
df = pd.DataFrame(data)
print(df)

X = df[["Hours_Studied", "Attendance"]]
y = df["Result"]

# Spliting the data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size= 0.2,
    random_state= 42
)

# Model selection
model = DecisionTreeClassifier(
    criterion= "gini",
    max_depth= 3,
    random_state=42
)

# Train Model & prediction
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

# Accuracy score
accuracy = accuracy_score(y_test, y_pred)
print("Actual : ", list(y_test))
print("Predicted : ", list(y_pred))
print("Accuracy:", accuracy)

# feature importance :
feature_importances_ = model.feature_importances_
print("feature importance :", feature_importances_)

# graph of feature importance :

plt.bar(
    X.columns,
    feature_importances_
    
)
plt.xlabel('Features')
plt.ylabel('Importance')
plt.title('Feature importance')
plt.show()

# visualize decision tree :

plt.figure(figsize=(10,10))
plot_tree(
    model,
    feature_names=X.columns,
    class_names=['0','1'],
    filled=True,
    rounded=True,
    fontsize=8
)
plt.title('Decision Tree')
plt.show()

# Test with new data

new_student = [[5.5, 78]]
prediction = model.predict(new_student)
print("New Student Result:", prediction[0])

