import datetime as dt
import requests
from geopy.geocoders import Nominatim

Base_Url ='https://api.openwathermap.org/data/3.0/weather?'

Api_Key= open('api_key.txt', 'r').read()

City = "London"
Country = "Britian"
Lookup = City + ", " + Country
locData = Nominatim(user_agent="tutorial")
locData = locData.geocode(Lookup).raw
lat = locData['lat']
long = locData['lon']

url= Base_Url + '&q=' + City + 'appid={' + Api_Key +'}'

r = requests.get(url)

print(r.json())