import requests

def get_weather():
    api_key = "YOUR_REAL_API_KEY"
    city = input("Enter city name: ")

    url = "AIzaSyDrwmMFesejZO5kmWxXwozCzr9NegN7_ZQ"

    params = {
        "q": city,
        "appid": api_key,
        "units": "metric",
        "lang": "en"
    }

    response = requests.get(url, params=params)
    data = response.json()

    if response.status_code == 200:
        print("\nWeather Report")
        print("City:", data["name"])
        print("Country:", data["sys"]["country"])
        print("Temperature:", data["main"]["temp"], "°C")
        print("Feels Like:", data["main"]["feels_like"], "°C")
        print("Humidity:", data["main"]["humidity"], "%")
        print("Condition:", data["weather"][0]["description"])
        print("Wind Speed:", data["wind"]["speed"], "m/s")
    else:
        print("Error:", data.get("message"))

if __name__ == "__main__":
    get_weather()
