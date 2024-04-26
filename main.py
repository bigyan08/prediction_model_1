from sklearn import tree


#[height,weight,shoe size]
x=[[181,80,44],[177,70,43],[160,60,38],[166,65,40],[190,90,47],[177,70,40],[171,75,42],[181,85,43]]

y=['male','female','male','male','male','female','female','male']
#decision tree
clf=tree.DecisionTreeClassifier()
clf.fit(x,y)
prediction=clf.predict([[155,75,40]])
print(prediction)





