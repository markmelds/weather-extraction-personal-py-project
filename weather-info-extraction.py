import requests   #to send requests to any website
from pprint import pprint           #when we send a requests to the api-keys page, we get a response in a JSON     format, PrettyPrint library formats that JSON response into a readable tree format


API_Key = '29e856a743b9a3d2c06b52ea262ea7dc'        #api key extraction

city = input("Enter a city: ")
base_url= "http://api.openweathermap.org/data/2.5/weather?appid="+API_Key+"&q="+city
weather_data = requests.get(base_url).json()
pprint(weather_data)



