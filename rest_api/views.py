from urllib import response
from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.request import Request
from rest_framework.response import Response
from rest_api.serializers import WeatherCreateSerializer, WeatherGetSerializer, WeatherListSerializer, get_instance_response
from django.shortcuts import get_object_or_404
from rest_api.models import Weather
from rest_api.filters import filter_params

class WeatherViewSet(ViewSet):
    permission_classes = []
    
    """ 
    Manage each request related to Wheather
    """

    def create(self, request: Request) -> Response:
        serializer = WeatherCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        obj = serializer.create(request.data)
        response = get_instance_response(obj)
        return Response(response, status=status.HTTP_201_CREATED)

    def list(self, request: Request) -> Response:
        serializer = WeatherListSerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)
        list = filter_params(request.query_params)
        response = serializer.json_serialize(list)
        return Response(response, status=status.HTTP_200_OK)

    def get(self, request: Request, *args, **kwargs) -> Response:
        serializer = WeatherGetSerializer(data=kwargs)
        serializer.is_valid(raise_exception=True)
        obj = get_object_or_404(Weather, id=kwargs.get('id'))
        response = get_instance_response(obj)
        return Response(response, status=status.HTTP_200_OK)

