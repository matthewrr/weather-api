from django.shortcuts import render
import json, requests

def get_grid(lat, long):
    url = f'https://api.weather.gov/points/{lat},{long}'
    response = requests.get(url).json()
    return response['properties']['forecast']

def get_forecast(request):
    lat, long = 48, -117
    if request.method == 'POST':
        zip_code = request.POST['zip_code']
    grid_url = get_grid(lat, long)
    response = requests.get(grid_url).json()
    return render(request, 'temperature/temperature.html', {'response': response})