"""1.
List three apps you use daily (such as Zomato, Instagram, or Flipkart) and describe one feature in 
each app that likely uses machine learning. For each, state whether it is an example of supervised, 
unsupervised, or reinforcement learning."""
# Answer
"""
(1) Zomato :
ML Feature                  : Restaurant recommendations
Type of Machine Learning    : Supervised Learning
The system learns from your previous orders, ratings, and preferences to predict restaurants you may like.

(2) Instagram :
ML Feature                  : Reels/Posts recommendations
Type of Machine Learning    : Unsupervised Learning
It identifies patterns in your likes, views, follows, and interests and groups users/content with similar 
behavior.

(3) Flipkart :
ML Feature                  : Product recommendations
Type of Machine Learning    : Supervised Learning
It uses previous purchases, searches, clicks, and product interactions to predict which products you 
are likely to buy.
"""


"""2.
Given the following scenarios, classify each as supervised, unsupervised, or reinforcement learning: 
1) Netflix recommending movies based on your watch history, 2) Spotify grouping similar songs into 
playlists, 3) A self-driving car learning to park by trial and error. Write your answers with a 
one-line explanation for each choice."""
# Answer
"""
Ans : 1
Netflix recommending movies based on your watch history → Supervised Learning
The system learns from your past viewing behavior to predict which movies you may like.

Ans : 2
Spotify grouping similar songs into playlists → Unsupervised Learning
The system finds similarities and patterns among songs without needing predefined labels.

Ans : 3
A self-driving car learning to park by trial and error → Reinforcement Learning
The car learns through trial and error by receiving rewards for successful parking and penalties for 
mistakes.
"""
    
"""3.
Draw a simple diagram (hand-drawn or digital) showing the basic ML workflow: Data → Preprocessing → 
Modeling → Evaluation → Deployment. Under each step, write a one-line example of what happens at that 
stage for a food delivery app like Swiggy."""
# Answer
##################################ML Workflow For Swiggy #############################################

# (1) Data : Orders ---- User info ---- Restaurant info ---- Ratings.
#---> Collect data like past order, User location, Ratings & Restaurant Details.

# (2) Preprocessing : Handle missing values ---- Encode categories ---- Scale features .
#---> Prepare data cleaning for model training.

# (3) Modeling : Train ML Model to predict waht user order next.
#---> Build model using training data.

# (4) Evaluation : Evaluate Model using matrix like accuracy, precision or RMSE.
#---> Check how well model recommends relevant retaurants or dishes.

# (5) Deployment : Deploy the Model so it gives real time recommendations to user.
#---> Use the model in the swiggy app to show personalized restaurant or dish suggestions.


"""4.
Imagine you are building a spam filter for WhatsApp messages. Write a short paragraph explaining how 
traditional programming would approach this problem versus how machine learning would approach it.
Hint: Focus on rules vs learning from data."""

# Answer
"""
For a WhatsApp spam filter, traditional programming would use manually created rules : 
such as blocking messages containing certain words, links, or suspicious patterns. 
In contrast, machine learning would learn from a large dataset of messages already labeled as 
“spam” or “not spam.” The ML model would identify patterns automatically and use them to predict 
whether a new WhatsApp message is spam. 
So, traditional programming mainly follows fixed rules, while machine learning learns patterns from data."""
