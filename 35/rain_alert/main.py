import requests
import os


def get_hourly_forecast(hourly_forecast_endpoint, hourly_forecast_params):
    response = requests.get(hourly_forecast_endpoint, params=hourly_forecast_params)
    response.raise_for_status()

    weather_data = response.json()
    return(weather_data)


def get_lon_lat(lon_lat_endpoint, lon_lat_params):

    response = requests.get(lon_lat_endpoint, params=lon_lat_params)
    response.raise_for_status()

    data = response.json()

    longitude = float(data["coord"]["lon"])
    latitude = float(data["coord"]["lat"])
    return (longitude, latitude)

def get_weather_from_code(weather_code):
    match weather_code:
        case weather_code if weather_code < 200:
            return("Something has gone wrong.")
        case weather_code if weather_code < 300:
            return("It's a thunderstorm.")
        case weather_code if weather_code < 400:
            return("It's drizzing.")
        case weather_code if weather_code < 500:
            return("Something has gone wrong")
        case weather_code if weather_code < 600:
            return("It's raining.")
        case weather_code if weather_code < 700:
            return("It's snowing.")
        case weather_code if weather_code >= 700:
            return("The weather is fine.")


city_name = "Wakefield"
country = "UK"
api_key = os.environ.get("OWM_API_KEY")
lon_lat_endpoint = "https://api.openweathermap.org/data/2.5/weather"
lon_lat_params = {"q": f"{city_name}, {country}", "appid": api_key}

longitude, latitude = get_lon_lat(lon_lat_endpoint, lon_lat_params)

hourly_forecast_endpoint = "https://api.openweathermap.org/data/2.5/onecall"
hourly_forecast_params = {
    "lat": latitude,
    "lon": longitude,
    "exclude": "current,minutely,daily,alerts",
    "appid": api_key
}

weather_data = get_hourly_forecast(hourly_forecast_endpoint, hourly_forecast_params)

weather_slice = weather_data["hourly"][:12]
for hour_data in weather_slice:
    weather_code = hour_data["weather"][0]["id"]
    weather_status = get_weather_from_code(weather_code)
    print(weather_status)

