import requests
import csv


api_key = '35cdebf5bc920462942567197ecae141'


cities = ['London', 'Paris', 'New York', 'Tokyo', 'Mumbai', 'Delhi', 'Sydney', 'Berlin', 'Rome', 'Cape Town']


url = 'http://api.openweathermap.org/data/2.5/weather'


csv_file = '/weather_data.csv'


with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
   
    writer = csv.writer(file)
    
  
    writer.writerow(['City', 'Weather Description', 'Temperature (°C)', 'Humidity (%)', 'Wind Speed (m/s)'])
    
   
    for city in cities:
     
        full_url = f'{url}?q={city}&appid={api_key}&units=metric'
        
   
        response = requests.get(full_url)
        
       
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()
           
            weather = data['weather'][0]['description']
            temperature = data['main']['temp']
            humidity = data['main']['humidity']
            wind_speed = data['wind']['speed']
            
           
            writer.writerow([city, weather, temperature, humidity, wind_speed])
        else:
            print(f"Failed to retrieve data for {city}. Status code: {response.status_code}")

print(f"Weather data saved to {csv_file}")
