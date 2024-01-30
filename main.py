"""
    Given a JSON file with weather data, this program that outputs the warmest, coldest, and average temperature.
    Author: Alexander Bieniek
    Date: 12/11/23
    Utilized CHATGPT for inspiration and to shorten code
    Weather data was obtained from the National Weather Service API: https://api.weather.gov/gridpoints/{office}/{gridX},{gridY}/forecast
    For Prescott, AZ, the API call is: https://api.weather.gov/gridpoints/FGZ/41,65/forecast
"""
import json
from typing import Any


def import_data() -> list:
    """Imports data from a JSON file, :return: a list of weather data periods"""
    file = 'C:/Users/awbie/Downloads/weather.json'
    with open(file, "r") as file:
        data = json.load(file)
    periods = data["properties"]["periods"]
    return periods


def warmest_temperature(periods: list) -> dict:
    """Returns the period with the warmest temperature
    :param periods: a list of weather data periods, :return: the period with the warmest temperature"""
    if not periods:
        return {}
    temperatures = [period.get("temperature") for period in periods]
    temp_check1 = list(filter(lambda temp: temp is not None, temperatures))
    if not temp_check1:
        return {}
    max_temp = temperatures.index(max(temp_check1))
    return periods[max_temp]


def coldest_temperature(periods: list) -> dict:
    """Returns the period with the coldest temperature
    :param periods: a list of weather data periods, :return: the period with the coldest temperature"""
    if not periods:
        return {}
    temperatures = [period.get("temperature") for period in periods]
    temp_check2 = list(filter(lambda temp: temp is not None, temperatures))
    if not temp_check2:
        return {}
    min_temp = temperatures.index(min(temp_check2))
    return periods[min_temp]


def average_temperature(periods: list) -> dict[Any, Any] | int:
    """Returns the average temperature over all periods
    :param periods: a list of weather data periods, :return: the rounded average temperature over all periods"""
    if not periods:
        return {}
    temperatures = [period.get("temperature") for period in periods]
    temp_check3 = list(filter(lambda temp: temp is not None, temperatures))
    if not temp_check3:
        return {}
    average_temp = round(sum(temp_check3) / len(temp_check3))
    return average_temp


try:
    if __name__ == '__main__':
        weather_data = import_data()
        warm = warmest_temperature(weather_data)
        cold = coldest_temperature(weather_data)
        avg = average_temperature(weather_data)
        print("The National Weather Service forecast for the next 7 days for Prescott, AZ is:")
        print(f"The warmest temperature is {warm.get('temperature')}F {warm.get('name')}.")
        print(f"The coldest temperature is {cold.get('temperature')}F {cold.get('name')}.")
        print(f"The average temperature is {avg} F.")

except:
    print(OSError)