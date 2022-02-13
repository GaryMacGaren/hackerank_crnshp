from datetime import datetime
from rest_framework import serializers
from rest_api.models import Wheather
import json

class WheatherCreateSerializer(serializers.Serializer):
    
    date = serializers.CharField()
    lat = serializers.FloatField()
    lon = serializers.FloatField()
    city = serializers.CharField()
    state = serializers.CharField()
    temperatures = serializers.ListField()

    def create(self, validated_data:dict) -> Wheather:
        instance = Wheather.objects.create(
            date = datetime.strptime(validated_data.get("date"), '%Y-%m-%d'),
            lat = validated_data.get("lat"),
            lon = validated_data.get("lon"),
            city = validated_data.get("city"),
            state = validated_data.get("state"),
            temperatures = json.dumps(validated_data.get("temperatures"))
        )
        instance.save()
        return instance

    def get_instance_response(self, obj):
        return {
            'id': obj.id,
            'date': str(obj.date)[:-9],
            'lat': obj.lat,
            'lon': obj.lon,
            'city': obj.city,
            "state": obj.state,
            "temperatures": json.loads(obj.temperatures)
        }
    