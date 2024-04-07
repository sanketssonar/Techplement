import requests

def get_weather(city_name, api_key):
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city_name}"
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        weather_description = data['current']['condition']['text']
        temperature = data['current']['temp_c']
        humidity = data['current']['humidity']
        wind_speed = data['current']['wind_kph']

        
        emoji = {
            "Sunny": "☀️",
            "Partly cloudy": "⛅",
            "Cloudy": "☁️",
            "Overcast": "🌥️",
            "Mist": "🌫️",
            "Patchy rain possible": "🌦️",
            "Patchy snow possible": "🌨️",
            "Patchy sleet possible": "🌨️",
            "Patchy freezing drizzle possible": "🌨️",
            "Thundery outbreaks possible": "🌩️",
            "Blowing snow": "❄️",
            "Blizzard": "❄️",
            "Fog": "🌫️",
            "Freezing fog": "🌫️",
            "Patchy light drizzle": "🌧️",
            "Light drizzle": "🌧️",
            "Freezing drizzle": "🌧️❄️",
            "Heavy freezing drizzle": "🌧️❄️",
            "Patchy light rain": "🌧️",
            "Light rain": "🌧️",
            "Moderate rain at times": "🌧️",
            "Moderate rain": "🌧️",
            "Heavy rain at times": "🌧️",
            "Heavy rain": "🌧️",
            "Light freezing rain": "🌧️❄️",
            "Moderate or heavy freezing rain": "🌧️❄️",
            "Light sleet": "🌨️❄️",
            "Moderate or heavy sleet": "🌨️❄️",
            "Patchy light snow": "🌨️",
            "Light snow": "🌨️",
            "Patchy moderate snow": "🌨️",
            "Moderate snow": "🌨️",
            "Patchy heavy snow": "🌨️",
            "Heavy snow": "🌨️",
            "Ice pellets": "🌨️❄️",
            "Light rain shower": "🌧️",
            "Moderate or heavy rain shower": "🌧️",
            "Torrential rain shower": "🌧️",
            "Light sleet showers": "🌨️❄️",
            "Moderate or heavy sleet showers": "🌨️❄️",
            "Light snow showers": "🌨️",
            "Moderate or heavy snow showers": "🌨️",
            "Light showers of ice pellets": "🌨️❄️",
            "Moderate or heavy showers of ice pellets": "🌨️❄️",
            "Patchy light rain with thunder": "🌩️🌧️",
            "Moderate or heavy rain with thunder": "🌩️🌧️",
            "Patchy light snow with thunder": "🌩️🌨️",
            "Moderate or heavy snow with thunder": "🌩️🌨️"
        }

        
        weather_emoji = emoji.get(weather_description, "")

        print(f"Weather in {city_name}: {weather_emoji}")
        print(f"Description: {weather_description}")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} km/h")
    else:
        print("Failed to retrieve weather data.")


api_key = 'c024b81340bc498b8b9110443240704'

city_name = input("Enter the city name: ")
get_weather(city_name, api_key)

