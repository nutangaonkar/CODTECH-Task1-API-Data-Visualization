import requests
import matplotlib.pyplot as plt

API_KEY = "YOUR_API_KEY"

CITY = "Mumbai"

# API URL (5 day / 3 hour forecast)
url = f"https://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric"


response = requests.get(url)

data = response.json()

dates = []
temperatures = []

# Extract first 10 forecast records
for item in data.get('list', [])[:10]:
    dates.append(item["dt_txt"])          
    temperatures.append(item["main"]["temp"])  


plt.figure(figsize=(10,5))
plt.plot(dates, temperatures, marker="o", linestyle="-", color="b")
plt.xlabel("Date & Time")
plt.ylabel("Temperature (°C)")
plt.title(f"Weather Forecast for {CITY}")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.savefig("output.png")

plt.show()
