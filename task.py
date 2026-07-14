import pandas as pd
from sklearn.linear_model import LinearRegression

# Q1. Salary Prediction: Experience vs Salary. Predict salary for 7 years.

# data = {
#     "Experience":[1,2,3,4,5],
#     "Salary":[10000,30000,60000,80000,150000]
# }

# df = pd.DataFrame(data)
# print(df)

# X=df[["Experience"]]
# Y=df["Salary"]

# # Create Model
# model = LinearRegression()

# # Train Model
# model.fit(X,Y)

# # new data for predection
# new=pd.DataFrame({"Experience":[10]})

# # Predict
# result = model.predict(new)

# # Result
# print(result[0])
# # accuracy
# print(model.score(X,Y))


# Q2. House Price Prediction: House Size vs House Price. Predict for 1500 sq ft.

# data = {
#     "house size":[100*100,200*200,300*300],
#     "house price":[50000,80000,150000]
# }

# df=pd.DataFrame(data)
# print(df)

# x=df[["house size"]]
# y=df["house price"]

# model = LinearRegression()

# model.fit(x,y)

# new=pd.DataFrame({"house size":[5000000]})

# result = model.predict(new)

# print(result[0])

# print(model.score(x,y))



# Q3. Ice Cream Sales: Temperature vs Sales. Predict at 40°C.


# data = {
#     "temperature":[10,20,30,40],
#     "sales":[3000,50000,100000,5000000]
# }

# df=pd.DataFrame(data)
# print(df)

# x=df[["temperature"]]
# y=df["sales"]

# model = LinearRegression()

# model.fit(x,y)

# new=pd.DataFrame({"temperature":[50]})

# result = model.predict(new)

# print(result[0])

# print(model.score(x,y))


# Q4. Car Price: Car Age vs Price. Predict for 6-year-old car.

# data = {
#     "car age":[1,2,3],
#     "car price":[500000,400000,100000]
# }

# df=pd.DataFrame(data)
# print(df)

# x=df[["car age"]]
# y=df["car price"]

# model = LinearRegression()
# model.fit(x,y)

# new = pd.DataFrame({"car age":[5]})

# result = model.predict(new)

# print(result[0])


# Q5. Mobile Battery: Capacity vs Backup. Predict for 6000 mAh.


# data = {
#     "battery capacity":[5000,5500,6000,6500],
#     "Backup":[5,6,7,8]
# }

# df=pd.DataFrame(data)
# print(df)

# x=df[["battery capacity"]]
# y=df["Backup"]

# model = LinearRegression()
# model.fit(x,y)

# new = pd.DataFrame({"battery capacity":[7000]})

# result = model.predict(new)
# print(result[0])
# print(model.score(x,y))



# Q6. Advertisement Budget: Budget vs Sales. Predict for ₹80,000.


# data={
#     "buget":[10000,20000,30000],
#     "sales":[20,60,80]
# }

# df=pd.DataFrame(data)
# print(df)

# x=df[["buget"]]
# y=df["sales"]

# model = LinearRegression()
# model.fit(x,y)

# new = pd.DataFrame({"buget":[80000]})

# result = model.predict(new)
# print(result[0])
# print(model.score(x,y))

# Q7. Petrol Consumption: Distance vs Petrol Used. Predict for 600 km.

# data={
#     "distance":[10,20,30],
#     "petrol":[1,2,3]
# }

# df=pd.DataFrame(data)
# print(df)

# x=df[["distance"]]
# y=df["petrol"]

# model = LinearRegression()
# model.fit(x,y)

# new = pd.DataFrame({"distance":[600]})

# result = model.predict(new)
# print(result[0])
# print(model.score(x,y))


# Q8. Electricity Bill: Units vs Bill. Predict for 350 units.


# data={
#     "units":[1,2,3,4],
#     "bills":[8,16,24,32]
# }

# df=pd.DataFrame(data)
# print(df)

# x=df[["units"]]
# y=df["bills"]

# model = LinearRegression()
# model.fit(x,y)
# new=pd.DataFrame({"units":[350]})
# result = model.predict(new)
# print(result[0])
# print(model.score(x,y))


# Q9. Employee Bonus: Performance Score vs Bonus. Predict for score 90.
