from rest_api.views import WeatherViewSet
from django.urls import path


urlpatterns = [
    path('weather/', WeatherViewSet.as_view({"post": "create", "get": "list"})),
    path('weather/<int:id>/', WeatherViewSet.as_view({"get": "get"}))
]
