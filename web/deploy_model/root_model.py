# Imprting the required library
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
# import matplotlib.pyplot as plt
import joblib

# Reading the data from the file
df = pd.read_csv('deploy_model/data.csv')

# Dealing with empty values in calories
mean_calories =('%.1f' % df['Calories'].mean())
df['Calories'].fillna(mean_calories, inplace = True)

# Correction the values in duration
for x in df.index:
    if(df.loc[x, 'Duration'] > 120):
        df.loc[x, 'Duration'] = 120

# Removing the duplicates 
df.drop_duplicates(inplace=True)

# Now taking the x and y vlaue  
x = pd.DataFrame(df['Duration'])
y = pd.DataFrame(df['Calories'])

# splitting the x and y to train and test data 
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2)

# Creating the model 
model = LinearRegression()
model.fit(x_train, y_train)

# Prediction of training an test results 
y_pred = model.predict(x_test)
x_pred = model.predict(x_train)

# print(y_pred)

# # visualizing the traing set results
# plt.scatter(x_train, y_train, color="green")   
# plt.plot(x_train, x_pred, color="red")    
# plt.title("Gym data analysis")  
# plt.xlabel("Duration")  
# plt.ylabel("Calories")  
# plt.show()  

# # visualizing the testing set results
# plt.scatter(x_test, y_test, color="blue")   
# plt.plot(x_train, x_pred, color="c")    
# plt.title("Gym data analysis")  
# plt.xlabel("Duration")  
# plt.ylabel("Calories")  
# plt.show()

# scoring the model 

# accuracy = ('%.1f' % model.score(x_train, y_train))

# # Storing model to joblib 
# filename = 'calories_pedictor.sav'
# joblib.dump(model, filename)

