import requests

city=input("enter your city name:")
api_key="8b06e67b75706c294ac0562d33a0025f" # paste your key here

url=f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'

response=requests.get(url)
if response.status_code==200:
   data=response.json()
   print("☁️"," weatheris",data['weather'][0]['description'])
   print("🌡️"," temperature",data['main']['temp'],"°C")
   print("💨"," wind",data['wind']['speed'])
else:
    print("city not found")   
    print(response.json())

