from django.shortcuts import render
import requests

def get_coordinates(zip_code):
    key = 'fiyonYjyfbmVxjmLOGaeLdmscFXiBGYa'
    url = f'http://www.mapquestapi.com/geocoding/v1/address?key={key}&location={zip_code}' 
    response = requests.get(url).json()
    coordinates = response['results'][0]['locations'][0]['latLng']
    return coordinates

def get_grid(lat, lng):
    url = f'https://api.weather.gov/points/{lat},{lng}'
    response = requests.get(url).json()
    return response['properties']['forecast']

def get_forecast(request, zip_code=10001):
    #add validation for zip code
    if request.method == 'POST':
        zip_code = request.POST['zip_code']
    coordinates = get_coordinates(zip_code)
    grid_url = get_grid(coordinates['lat'], coordinates['lng'])
    response = requests.get(grid_url).json()
    return render(request, 'temperature/temperature.html', {'response': response})