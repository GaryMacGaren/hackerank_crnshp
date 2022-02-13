from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.request import Request
from rest_framework.response import Response
from rest_api.serializers import WheatherCreateSerializer
from django.core import serializers
import json

class WheatherViewSet(ViewSet):
    permission_classes = []
    
    """ 
    Manage each request related to Wheather
    """

    def create(self, request: Request) -> Response:
        serializer = WheatherCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        obj = serializer.create(request.data)
        response = serializer.get_instance_response(obj)
        # return Response(json.loads(serializers.serialize('json', [obj])), status=status.HTTP_201_CREATED) 
        return Response(response, status=status.HTTP_201_CREATED) 
