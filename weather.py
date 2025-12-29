import requests

def get_weather(city):
    api_key = "0deb9548231b4c98ba080146250412"
    url = "https://api.weatherapi.com/v1/current.json"

    params = {
        "key": api_key,
        "q": city,
        "aqi": "no"
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()  # HTTP error check
        data = response.json()

        # API-level error
        if "error" in data:
            return f"❌ {data['error']['message']}"

        weather = {
            "City": data["location"]["name"],
            "Region": data["location"]["region"],
            "Country": data["location"]["country"],
            "Temperature": f"{data['current']['temp_c']} °C",
            "Feels Like": f"{data['current']['feelslike_c']} °C",
            "Humidity": f"{data['current']['humidity']} %",
            "Weather": data["current"]["condition"]["text"],
            "Wind Speed": f"{data['current']['wind_kph']} kph",
            "Last Updated": data["current"]["last_updated"]
        }

        return weather

    except requests.exceptions.RequestException as e:
        return f"⚠️ Network error: {e}"


# Command line testing
if __name__ == "__main__":
    city_name = input("Enter city name: ")
    result = get_weather(city_name)

    print("\n🌤 Real-Time Weather Data:")
    if isinstance(result, str):
        print(result)
    else:
        for key, value in result.items():
            print(f"{key}: {value}")
