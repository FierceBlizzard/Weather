import datetime as dt
import requests
from geopy.geocoders import Nominatim
import pyowm

#Api_Key= open('api_key.txt', 'r').read()

City = 'London'
Country = 'Britian'
Location = City + ', ' + Country

owm = pyowm.OWM('aba976c535fffdea88d6fdc84eb35947')
LocData = owm.weather_at_place('San Francisco, US')
weather = LocData.get_weather()

print(weather.get_weather('fahrenheit')['temp'])