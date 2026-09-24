"""1.
Download the 'Spotify Top 50 Songs' dataset from Kaggle, load it into a pandas DataFrame, and identify 
which columns should be used as features and which as the label if you want to predict a song's 
popularity score."""

"""import pandas as pd

df = pd.read_csv("S2.1_spotify_top50.csv")          # Load dataset
# print(df.head())                                    # Display first 5 rows
# print(df.columns)                                   # Display column names

# Identify Features and Label
X = df[["danceability","energy","key","loudness","mode"]]
y = df["popularity"]

print("Features:")
print(X.head())

print("Label:")
print(y.head())"""


"""2.
Split the loaded Spotify dataset into training and test sets using sklearn's train_test_split function, 
with 80% for training and 20% for testing. Print the number of rows in each set."""
"""
import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_csv("S2.1_spotify_top50.csv")                  # Load dataset

X = df[["danceability","energy","key","loudness","mode"]]   # Identify Features and Label   
y = df["popularity"]                                        # Target

X_train, X_test, y_train, y_test = train_test_split(        # Split DataSet
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("Training rows:", len(X_train))
print("Testing rows:", len(X_test))
"""

    
"""3.
Given a simple linear regression model predicting song popularity from danceability, intentionally use 
only 5% of the data for training and 95% for testing. Observe the model's performance and explain whether 
this is likely to cause underfitting or overfitting.
Hint:Look at the accuracy or error on both train and test sets to support your answer."""
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

df = pd.read_csv("S2.1_spotify_top50.csv")                  # Load dataset

X = df[["danceability"]]                                    # Identify Features and Label   
y = df["popularity"]                                        # Target

# Split DataSet : 5% Traning & 95% Testing
X_train, X_test, y_train, y_test = train_test_split(        
    X,
    y,
    test_size=0.95,
    random_state=42
)


model = LinearRegression()                                  # Create model

model.fit(X_train,y_train)                                  # Train
y_pred_train = model.predict(X_train)                       # Predictions
y_pred_test = model.predict(X_test) 

# Evaluate traning data
r2_score_train = r2_score(y_train,y_pred_train)             # R2 Score
MSE_train = mean_squared_error(y_train,y_pred_train)        # Mean square error

# Evaluate testing data
r2_score_test = r2_score(y_test,y_pred_test)                # R2 Score
MSE_test = mean_squared_error(y_test,y_pred_test)           # Mean square error

# Print Result of traning data
print("Training Data Performance")
print("R2 Score:", r2_score_train)
print("MSE:", MSE_train)


# Print Result of testing data
print("\nTesting Data Performance")
print("R2 Score:", r2_score_test)
print("MSE:", MSE_test)
p
"""
Conclusion: The 5% training split is insufficient for the model to learn effectively, resulting in poor 
performance and underfitting. A larger training set, such as 80% training and 20% testing, would give 
more reliable results."""
    

"""4.
Draw or find a graph online that visually explains the bias variance tradeoff, and write a short 
note describing how this tradeoff would affect predictions in a Zomato restaurant rating predictor 
app."""
# Answer

"""
In a Zomato restaurant rating prediction app, the bias variance tradeoff affects how accurately the 
model predicts restaurant ratings.

High Bias → Underfitting: If the model is too simple, such as using only a few features like price 
or location, it may miss important patterns. Predictions will be inaccurate for both training and 
new restaurants.

High Variance → Overfitting: If the model is too complex, it may memorize details and noise from 
the training restaurants. It may give very accurate training predictions but perform poorly on new 
restaurants.

Optimal balance: We should choose a model that is complex enough to learn useful patterns such as 
cost, cuisine, location, votes, and restaurant type, but not so complex that it memorizes the 
training data.

Conclusion: For the Zomato app, the goal is to find the optimal model complexity that gives low 
prediction error on both training and unseen test restaurants. This provides more reliable restaurant-
rating predictions.

"""

"""5.
Give a real example (outside of healthcare/hospital) of overfitting from any app you use (e.g., Instagram, 
Flipkart, Swiggy), and explain in 2-3 lines why it might happen in that scenario."""
# Answer

"""
Real Example: Flipkart

Example: Flipkart's product recommendation system could overfit if it learns that a user always buys one 
particular brand based only on their past purchases.

Why it happens: The model may memorize the user's limited purchase history instead of learning their 
broader interests. As a result, it may recommend the same brand repeatedly and fail to suggest new 
products the user might actually like.

Simple conclusion:
Overfitting occurs when the model performs very well on past user data but performs poorly when predicting 
the user's future interests.

"""