import requests
BASE_URL ="http://api.openweathermap.org/data/2.5/weather?"
API_KEY = "05b95248341d5442fcae9c5f9b625780"
CITY =input("Enter your city")
url = BASE_URL +"appid=" + API_KEY + "&q=" +CITY
response =requests.get(url).json()
print(response)
print("Current Temperature ",response["main"]["temp"])
print("Current Temperature Feels like ",response["main"]["feels_like"])
print("Maximum Temperature ",response["main"]["temp_max"])
print("Minimum Temperature ",response["main"]["temp_min"])