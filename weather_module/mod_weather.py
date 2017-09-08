import pyowm, copy, datetime
from datetime import *

#
today = datetime.today()
cur_day = int(today.day)
cur_month = today.month
cur_year = today.year
def getDate():

    return str(cur_day) + " " + str(cur_month) + " " + str(cur_year)


#date_instance = datetime.date()

api_key = "0c0db12f156ad8b51492250a9f8a0ef4"
api_instance = pyowm.OWM()

owm_object = pyowm.OWM(api_key)
owm_list = owm_object.weather_at_place('ames, ia')
weather_obj = owm_list.get_weather()


#status,

def mdaily_cast(mlocation, days):
    return copy.deepcopy(owm_object.daily_forecast(mlocation,days).get_forecast())

#displays clouds / rains / etc; unit testing method
def get_cast_status(forecast_obj):
    rtarg = str()
    for fcast in forecast_obj:
        rtarg = rtarg + " "  + " " + str(fcast.get_temperature('fahrenheit')) +'\n'
    return rtarg

#returns a dict Day : str(Status, Temp Info)

#no error handling for if forecast obj days is less than these days
def basic_weather(forecast_obj):
    #2d for delivery,
    module_data = list()
    i = 0
    for fcast in forecast_obj:
        weather = fcast.get_temperature('fahrenheit')
        #print(weather)
        module_data.append(str(fcast.get_reference_time('iso')) + " " + str(fcast.get_status()) + " min " + str(weather["min"]) + " | max " + str(weather["max"]) + "\n")

        i += 1
    return module_data

