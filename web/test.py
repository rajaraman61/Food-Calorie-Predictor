import pandas as pd

food = pd.read_csv('data_featured.csv')

food_input = input('Enter your food: ')
food_grams = input('Enter your grams: ')
food_dict = food.iterrows()

items = food[food.Food == food_input]
calorie = items.Calories.values[0]
total_calorie = calorie * int(food_grams)
print(total_calorie)
#for index, row in food.iterrows():
#    #print(row['Grams'], row['Food'], row['Calories'])
#    for item in food_input.split(','):
#        print(food.loc[food['Food'] == item])

