import requests

api_key = "Please, add your personal API key."

municipality = input("Enter the name of the municipality: ")
municipality = municipality.title()

url = f"https://api.openweathermap.org/data/2.5/weather?q={municipality}&appid={api_key}"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    weather_description = data["weather"][0]["description"]
    temp_kelvin = data["main"]["temp"]

    temp_celsius = temp_kelvin - 273.15

    print(f"The current weather in {municipality} is: {weather_description}.\n"
          f"And temperature in {municipality} is {temp_celsius:.1f}°C.")

else:
    print("Sorry, check the name of municipality properly and try again.")



