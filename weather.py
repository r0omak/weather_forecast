import requests
from datetime import datetime

def get_weather_forecast(city, target_date, api_key):
    base_url = "http://api.weatherapi.com/v1/forecast.json"

    # Розрахунок кількості днів до цільової дати
    current_date = datetime.now().date()
    target_date_obj = datetime.strptime(target_date, "%Y-%m-%d").date()
    days_diff = (target_date_obj - current_date).days
    
    if days_diff < 0:
        return "Цільова дата повинна бути у майбутньому."

    params = {
        'key': api_key,
        'q': city,
        'days': days_diff + 1,  # API повертає прогноз на наступні дні
        'lang': 'uk'  # Українська мова
    }
    
    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        print(data)
        forecasts = data['forecast']['forecastday']
        
        for forecast in forecasts:
            if forecast['date'] == target_date:
                weather_description = forecast['day']['condition']['text']
                temp = forecast['day']['avgtemp_c']
                max_temp = forecast['day']['maxtemp_c']
                min_temp = forecast['day']['mintemp_c']
                humidity = forecast['day']['avghumidity']
                wind_speed = forecast['day']['maxwind_kph']
                
                # Формування та повернення результату
                result = (
                    f"Погода в місті {city} на дату {target_date}:\n"
                    f"Опис: {weather_description}\n"
                    f"Середня температура: {temp}°C\n"
                    f"Максимальна температура: {max_temp}°C\n"
                    f"Мінімальна температура: {min_temp}°C\n"
                    f"Вологість: {humidity}%\n"
                    f"Максимальна швидкість вітру: {wind_speed} км/год\n"
                )
                return result
        return "Прогноз для зазначеної дати не знайдено."
    else:
        return "Не вдалося отримати дані про погоду. Перевірте правильність введеного міста та повторіть спробу."

# Введення міста та дати
city = input("Введіть місто: ")
target_date = input("Введіть дату (YYYY-MM-DD): ")

# Ваш API-ключ WeatherAPI
api_key = '628568f2dc1047b8a6873444240706'

# Отримання та виведення прогнозу погоди
weather_forecast = get_weather_forecast(city, target_date, api_key)
print(weather_forecast)
