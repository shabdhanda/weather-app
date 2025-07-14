import requests

def get_weather(city):
    api_key = "ae22aed2361cda630847c1ad4f1d3ad0"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    response = requests.get(url)
    data = response.json()

    if data.get("cod") != 200:
        print("❌ Error:", data.get("message", "Unknown error"))
    else:
        weather = data["weather"][0]["description"]
        temperature = data["main"]["temp"]
        print(f"\nWeather in {city.capitalize()}: {weather}")
        print(f"Temperature: {temperature}°C")

if __name__ == "__main__":
    print("🌦️  Weather App using OpenWeatherMap API")
    city_name = input("Enter a city name: ")
    get_weather(city_name)

