from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
import joblib
from deploy_model import root_model as rm
import matplotlib.pyplot as plt
import math


def index(request):
    return render(request, 'index.html')

def result(request):
    model = joblib.load('calories_predictor.joblib')
    food = pd.read_csv('data_featured.csv')

    message = 'Do some workout, your body is not healthy :('
    duration = []
    # Getting the data entered by user 
    duration.append(request.GET.get('duration', 'default'))

    workout_period = duration[0] 
    food_item = request.GET.get('food', 'default')
    grams = float(request.GET.get('grams', 'default'))

    items = food[food.Food == food_item]
    calorie = items.Calories.values[0]
    total_calorie = calorie * int(grams)
    # implementing the model 
    duration = pd.DataFrame(duration)
    predict =  model.predict(duration)
    res = float(predict)
    result = ('%.2f' % res)
    x = rm.x_train
    y = rm.y_train
    demo = model.score(x,y)
    demo = math.floor(demo*100)
    result = float(result) - total_calorie
    print(type(demo))
    print(type(result))
    if (result > 200):
        message = "Maintaining healthy life style, keep going :)"

    params = {'duration': workout_period, 'result': ('%.2f' % result), 'message': message, 'demo':demo + 25}


    return render(request, 'result.html', params)

    