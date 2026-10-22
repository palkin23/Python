
import requests


def get_weather(city):
    geo_url = "https://geocoding-api.open-meteo.com/v1/search"
    weather_url = "https://api.open-meteo.com/v1/forecast"

    geo_params = {
        "name": city,
        "count": 1,
        "language": "en",
        "format": "json"
    }

    geo_response = requests.get(geo_url, params=geo_params, timeout=10)
    geo_response.raise_for_status()
    geo_data = geo_response.json()

    if not geo_data.get("results"):
        print("City not found!")
        return

    location = geo_data["results"][0]
    latitude = location["latitude"]
    longitude = location["longitude"]

    weather_params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m,relative_humidity_2m,wind_speed_10m"
    }

    weather_response = requests.get(
        weather_url, params=weather_params, timeout=10
    )
    weather_response.raise_for_status()
    weather_data = weather_response.json()

    current = weather_data["current"]

    print("\n--- Weather Report ---")
    print("City:", location["name"])
    print("Temperature:", current["temperature_2m"], "°C")
    print("Humidity:", current["relative_humidity_2m"], "%")
    print("Wind Speed:", current["wind_speed_10m"], "km/h")


def main():
    city = input("Enter city name: ")

    try:
        get_weather(city)
    except requests.RequestException as e:
        print("Network/API error:", e)
    except (KeyError, IndexError, ValueError) as e:
        print("Unexpected response:", e)


if __name__ == "__main__":
    main()
