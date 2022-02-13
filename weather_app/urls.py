from django.urls import path
from rest_api.views import WheatherViewSet

urlpatterns = [
    path('weather/', WheatherViewSet.as_view({"post": "create"}))
]
