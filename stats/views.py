# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from weather_module import mod_weather

# Create your views here.

def index(request):
    testWeather = mod_weather.basic_weather(mod_weather.mdaily_cast('Ames, ia', 7))
    context = {'testData': testWeather}
    return render(request, 'stats/index.html', context)
