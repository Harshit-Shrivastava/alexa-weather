import requests

def find_weather():
    url = 'http://api.openweathermap.org/data/2.5/weather?appid=9a3fa9dc0c5b36d730b1f66e62460b58&units=metric&q=Chicago'
    response =  requests.get(url)
    return response.json()