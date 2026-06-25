import requests

city = input(
    "Enter city name: "
)

url = f"https://wttr.in/{city}?format=j1"

response = requests.get(url)

data = response.json()
print(data)

weather = data["current_condition"][0]

print("Temperature:",
      weather["temp_C"], "°C")

print("Humidity:",
      weather["humidity"], "%")

print("Wind Speed:",
      weather["windspeedKmph"],
      "km/h")