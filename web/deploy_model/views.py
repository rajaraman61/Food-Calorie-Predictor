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
    duration = []
    # Getting the data entered by user 

    duration.append(request.GET.get('duration', 'default'))
    dummy = duration[0]

    # implementing the model 
    duration = pd.DataFrame(duration)
    predict =  model.predict(duration)
    res = float(predict)
    result = ('%.2f' % res)
    x = rm.x_train
    y = rm.y_train
    demo = model.score(x,y)
    demo = math.floor(demo*100)
    # print(type(demo))
    params = {'duration': dummy, 'result': result, 'demo':demo}


    return render(request, 'result.html', params)

    