# #pip install -U scikit-learn  # uncomment if sklearn is not installed
from sklearn import tree 
x=[[181,80,44],[177,70,43],[160,60,38],[154,54,37],[166,65,40],[190,90,47],[175,64,39],[177,70,40],[159,55,37],[171,75,42]]
y=['1','0','0','0','1','1','1','0','1','0']   #does not work for string 
prediction_data=[[181,85,43]]        #this is new data
clf = tree.DecisionTreeRegressor() # Decision tree type
clf=clf.fit(x,y) #calling fit
prediction=clf.predict(prediction_data) 
print(prediction)
if pre==1: #simple if-logic
    print('male')
else:
    print("female")
          