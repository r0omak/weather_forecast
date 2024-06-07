import requests
from datetime import datetime

def get_weather(city, date, api_key):
    base_url = "http://api.weatherapi.com/v1/current.json"
    
    # Формування параметрів запиту
    params = {
        'key': api_key,
        'q': city,
        'lang': 'uk'  # Українська мова
    }
    
    # Виконання запиту
    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        # Отримання основної інформації про погоду
        weather_description = data['current']['condition']['text']
        temp = data['current']['temp_c']
        feels_like = data['current']['feelslike_c']
        humidity = data['current']['humidity']
        wind_speed = data['current']['wind_kph']
        
        # Формування та повернення результату
        result = (
            f"Погода в місті {city} на дату {date}:\n"
            f"Опис: {weather_description}\n"
            f"Температура: {temp}°C (відчувається як {feels_like}°C)\n"
            f"Вологість: {humidity}%\n"
            f"Швидкість вітру: {wind_speed} км/год"
        )
        return result
    else:
        return "Не вдалося отримати дані про погоду. Перевірте правильність введеного міста та повторіть спробу."

# Введення міста та дати
city = input("Введіть місто: ")
date = input("Введіть дату (YYYY-MM-DD): ")

# Ваш API-ключ WeatherAPI
api_key = '628568f2dc1047b8a6873444240706'

# Отримання та виведення погоди
weather_info = get_weather(city, date, api_key)
print(weather_info)

