from datetime import datetime
from rest_framework import serializers
from rest_api.models import Weather
import json

class WeatherCreateSerializer(serializers.Serializer):
    
    date = serializers.CharField()
    lat = serializers.FloatField()
    lon = serializers.FloatField()
    city = serializers.CharField()
    state = serializers.CharField()
    temperatures = serializers.ListField()

    def create(self, validated_data:dict) -> Weather:
        instance = Weather.objects.create(
            date = datetime.strptime(validated_data.get("date"), '%Y-%m-%d'),
            lat = validated_data.get("lat"),
            lon = validated_data.get("lon"),
            city = validated_data.get("city"),
            state = validated_data.get("state"),
            temperatures = json.dumps(validated_data.get("temperatures"))
        )
        instance.save()
        return instance


    

class WeatherListSerializer(serializers.Serializer):
    date = serializers.CharField(required=False)
    city = serializers.CharField(required=False)
    sort = serializers.CharField(required=False)

    def json_serialize(self, list):
        response = []
        for element in list:
            response.append(
                get_instance_response(element)
            )
        return response


    
class WeatherGetSerializer(serializers.Serializer):
    id = serializers.IntegerField()

def get_instance_response(obj):
    return {
        'id': obj.id,
        'date': str(obj.date)[:-9] if len(str(obj.date)) > 10 else str(obj.date),
        'lat': obj.lat,
        'lon': obj.lon,
        'city': obj.city,
        "state": obj.state,
        "temperatures": json.loads(obj.temperatures)
    }