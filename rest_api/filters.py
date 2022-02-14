from rest_api.models import Weather
from django.db.models import Q


def filter_by_date(obj_list, validated_data):
    return obj_list.filter(date=validated_data.get('date'))

def filter_by_city(obj_list, validated_data):
    city_or_cities = validated_data.get('city').split(",")
    if len (city_or_cities) > 1:
        filters = None
        for city in city_or_cities:
            city = city[0].upper() + city[1:]
            if not filters:
                filters = Q(city=city)
            filters = filters | Q(city=city)
        return obj_list.filter(filters)
    else:
        return obj_list.filter(city=city_or_cities)


def sort(obj_list, validated_data):
    sort_way = validated_data.get('sort')
    return obj_list.order_by(sort_way).order_by('id')

def filter_params(validated_data):
    obj_list = Weather.objects.all()
    if validated_data.get("city") != None:
        obj_list = filter_by_city(obj_list, validated_data)
    if validated_data.get("date") != None:
        obj_list = filter_by_date(obj_list, validated_data)
    if validated_data.get('sort') != None:
        obj_list = sort(obj_list, validated_data)

    return obj_list
        



