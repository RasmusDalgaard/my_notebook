import requests

api_key = 'fd0741a36c4446d9df68981b7fc65946'

lat=56.162939
lon=10.203921
data = requests.get('https://api.openweathermap.org/data/2.5/weather?lat=56.162939&lon=10.203921&appid=fd0741a36c4446d9df68981b7fc65946')

print(data.text)


