# #pip install -U scikit-learn  # uncomment if sklearn is not installed
from sklearn import tree
x=[[181,80,44],[177,70,43],[160,60,38],[154,54,37],[166,65,40],[190,90,47],[175,64,39],[177,70,40],[159,55,37],[171,75,42],[181,85,43]] #this is the data contains body weight, height and foot size of male and female

y=['m','f','f','f','m','m','m','f','m','f','m'] #this is our lables of dataset (f is for female and m is for male)
prediction_data=[[181,85,43]]  #this is new data on which we will make prediction (male or female)
clf=tree.DecisionTreeClassifier() # Decision tree type

clf=clf.fit(x,y) #calling fit
prediction=clf.predict(prediction_data) #making prediction
print(prediction)
if prediction=='m': #simple if-logic
    print('male')
else:
    print("female")
          