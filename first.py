'''Linear Regression is a supervised machine learning algorithm used to predict continuous numeric value 
formula Y=mx+C'''

import pandas as pd
from sklearn.linear_model import LinearRegression

# Dataset
data ={
    "hours" : [ 1,2,3,4,5],
    "Marks":[30,40,50,60,70]
}
df=pd.DataFrame(data)

print(df)

# Input / Output
X=df[["hours"]]
Y=df["Marks"]

# Create Model
model = LinearRegression()

# Train Model
model.fit(X,Y)

# new data for predection
new=pd.DataFrame({"hours":[10]})

# Predict
result = model.predict(new)

# Result
print(result[0])
# accuracy
print(model.score(X,Y))