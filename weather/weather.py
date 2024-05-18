import requests

# Replace 'your_api_key_here' with your actual OpenWeatherMap API key
API_KEY = 'your_api_key_here'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

def get_weather(city):
    """Get the weather information for a city."""
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'  # Use 'imperial' for Fahrenheit
    }
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def display_weather(weather_data):
    """Display the weather information."""
    if weather_data:
        city = weather_data['name']
        country = weather_data['sys']['country']
        temperature = weather_data['main']['temp']
        description = weather_data['weather'][0]['description']
        humidity = weather_data['main']['humidity']
        wind_speed = weather_data['wind']['speed']

        print(f"Weather in {city}, {country}:")
        print(f"Temperature: {temperature}°C")
        print(f"Description: {description.capitalize()}")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")
    else:
        print("City not found or unable to fetch weather data.")

def main():
    while True:
        print("\nWeather Application")
        city = input("Enter city name (or 'exit' to quit): ")
        if city.lower() == 'exit':
            print("Exiting the application. Goodbye!")
            break
        weather_data = get_weather(city)
        display_weather(weather_data)

if __name__ == '__main__':
    main()
