import requests


API_KEY = "56ea93b20c21a92f2b6ddde0bfbed20b"
BASE_URL = "https://api.openweathermap.org/data/3.0/weather"



city = input("Enter a city name: ")

request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print("Failed to retrieve data")