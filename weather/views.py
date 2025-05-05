import requests
from django.shortcuts import render
from django.conf import settings
# Create your views here.

def weather_home(request):
    weather_data=None

    if request.method=='POST':
        city=request.POST['city']
        api_key='apijskdn'
        url=f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
        response=requests.get(url)
        if response.status_code==200:
            weather_data=response.json()
        else:
            weather_data=None
    return render(request,'weather/home.html',{'weather_data':weather_data})
