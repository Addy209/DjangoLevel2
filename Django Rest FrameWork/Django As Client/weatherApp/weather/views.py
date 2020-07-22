from django.shortcuts import render, redirect
from django.views.generic import View
import requests
from django.http import JsonResponse, HttpResponse
from rest_framework.decorators import api_view

# Create your views here.
class Weather(View):
    template_name='weather/index.html'
    url="http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=9b352047f591ab042b23201b4f2f9e74"
    city="Mumbai"
    def get(self, request):
        resp=requests.request("GET",self.url.format(self.city)).json()
        
        city_weather={
            'city':resp['name'],
            'temp':resp['main']['temp'],
            'desc':resp['weather'][0]['description'],
            'icon':resp['weather'][0]['icon']
        }
        context={'city_weather':city_weather}
        print(city_weather)


        return render(request,self.template_name)

@api_view(['GET'])
def test(request):
    # url='https://restcountries.eu/rest/v2/name/{}'
    # country=request.POST['country']
    # resp=requests.request('GET',url.format(country)).json()
    print("Here")
    # print(resp)
    return JsonResponse({'name':"this is data"},status=200)