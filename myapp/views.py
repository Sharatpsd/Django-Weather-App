from django.shortcuts import render
import requests
from datetime import datetime


def index(request):
    appid = '9406e9bd7209b42f4be1b62513e67e7e'
    city = ''  # Initially empty

    weather = None

    if request.method == 'POST':
        city = request.POST.get('city')
        URL = 'https://api.openweathermap.org/data/2.5/weather'
        PARAMS = {
            'q': city,
            'appid': appid,
            'units': 'metric'
        }

        r = requests.get(url=URL, params=PARAMS)
        if r.status_code == 200:
            data = r.json()
            weather = {
                'city': data['name'],
                'temperature': data['main']['temp'],
                'description': data['weather'][0]['description'],
                'icon': data['weather'][0]['icon']
            }
        else:
            weather = {
                'city': city,
                'temperature': 'N/A',
                'description': 'City Not Found',
                'icon': '01d'
            }

    now = datetime.now()
    current_time = now.strftime("%Y-%m-%d %I:%M:%S %p")

    context = {
        'weather': weather,
        'current_time': current_time
    }

    return render(request, 'myapp/index.html', context)
