import requests
import json
from django.db.models import Count
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.utils import json
from .models import APIKey
from random import randint
from .serializer import AddressSerializer
from .serializer import ListAddressSubjectionSerializer
from .serializer import GeoSerializer
from .serializer import LocationIdSerializer


def random_key():
    self = APIKey.objects
    count = self.aggregate(count=Count('id'))['count']
    random_index = randint(0, count - 1)

    return self.all()[random_index]


apikey = random_key()


@api_view(['POST', ])
def request_autocomplete_suggestion(request):
    if request.method == 'POST':
        my_data = ListAddressSubjectionSerializer(data = request.data)

        if not my_data.is_valid():
            return Response({
                'message': 'Address is not found, try again!',
                'success': False,
                'status_code': 400,
            }, status = status.HTTP_400_BAD_REQUEST, )
        
        this = my_data.data

        # num = this['number']
        # street = this['street']
        # ward = this['ward']
        # district = this['district']
        keyword = this['keyword']

        # query = num + '+' + street + '+' + ward + '+' + district + '+' + city

        url = 'https://autocomplete.geocoder.ls.hereapi.com/6.2/suggest.json'
        key = '?apiKey=%s' % (apikey, )
        query = '&query=%s' % (keyword, )
        # endpoint = '&beginHighlight=<b>&endHighlight=</b>'

        api_url = url + key + query
        
        print(api_url)

        res = requests.get(api_url)
        data = res.json()

        if not data:
            return Response({
                'message': 'Address not found!',
                'success': False,
                'status_code': 400,
            }, status = status.HTTP_400_BAD_REQUEST, )
        else:
            return Response({
                'message': 'Successful!',
                'success': True,
                'status_code': 200,
                'data': data,
            }, status = status.HTTP_200_OK, )

    else:
        return Response({
            'message': 'Method not supported!',
            'status_code': 405,
            'success': False,
        }, status = status.HTTP_405_METHOD_NOT_ALLOWED, )


@api_view(['POST', ])
def convert_address_to_geo(request):
    if request.method == 'POST':
        my_data = AddressSerializer(data = request.data)

        if not my_data.is_valid():
            return Response({
                'message': 'Address is not found, try again!',
                'success': False,
                'status_code': 400,
            }, status = status.HTTP_400_BAD_REQUEST, )

        # num = my_data.data['number'] 
        # street = my_data.data['street'] 
        # ward = my_data.data['ward'] 
        # district = my_data.data['district'] 
        city = my_data.data['city']
    
        # keyword = '%s %s %s %s %s' % (num, street, ward, district, city, )
        keyword = '%s' % (city, )

        print(keyword)

        api_url = 'https://geocode.search.hereapi.com/v1/geocode?q=%s&apiKey=%s' % (keyword, apikey, )
        
        res = requests.get(api_url)
        data = res.json()

        if not data:
            return Response({
                'message': 'Address not found!',
                'success': False,
                'status_code': 400,
            }, status = status.HTTP_400_BAD_REQUEST, )
        else:
            # print(data)
            items = data['items']

            for item in items:
                title = item['title']
                position = item['position']
                lat = position.get('lat')
                lng = position.get('lng')

            return Response({
                'message': 'Succesful',
                'success': True,
                'status_code': 200,
                'data': ({
                    'title': title,
                    'lat': lat,
                    'lng': lng,
                })
            }, status = status.HTTP_200_OK, )
    else:
        return Response({
            'message': 'Method not supported!',
            'status_code': 405,
            'success': False,
        }, status = status.HTTP_405_METHOD_NOT_ALLOWED, )


@api_view(['POST', ])
def convert_geo_to_address(request):

    if request.method == 'POST':

        my_data = GeoSerializer(data = request.data)

        if not my_data.is_valid():
            return Response({
                'message': 'Address is not found, try again!',
                'success': False,
                'status_code': 400,
            }, status = status.HTTP_400_BAD_REQUEST, )

        this = my_data.data
        lat = this['lat']
        lng = this['lng']
        
        url = 'https://discover.search.hereapi.com/v1/discover'
        location = '?at=%s,%s' % (lat, lng)
        query = '&q=petrol+station'
        limit = '&limit=5'
        language = '&lang=en-US'
        key = '&apiKey=%s' % (apikey, )

        api_url = url + location + query + limit + language + key

        res = requests.get(api_url)
        data = res.json()

        if not data:
            return Response({
                'message': 'Address not found!',
                'success': False,
                'status_code': 400,
            }, status = status.HTTP_400_BAD_REQUEST, )
        else:
            return Response({
                'message': 'Successful!',
                'success': True,
                'status_code': 200,
                'data': data
            }, status = status.HTTP_200_OK)

    else:
        return Response({
            'message': 'Method not supported!',
            'status_code': 405,
            'success': False,
        }, status = status.HTTP_405_METHOD_NOT_ALLOWED, )


@api_view(['POST', ])
def convert_geo_to_location_id(request):

    if request.method == 'POST':

        my_data = LocationIdSerializer(data = request.data)

        if not my_data.is_valid():
            return Response({
                'message': 'Address is not found, try again!',
                'success': False,
                'status_code': 400,
            }, status = status.HTTP_400_BAD_REQUEST, )

        location_id = my_data.data['location_id']

        url = 'https://geocoder.ls.hereapi.com/6.2/geocode.json'
        key = '?apiKey=%s' % (apikey, )
        location = '&locationid=%s' % (location_id, )

        api_url = url + key + location

        res = requests.get(api_url)
        data = res.json()

        if not data:
            return Response({
                'message': 'Address not found!',
                'success': False,
                'status_code': 400,
            }, status = status.HTTP_400_BAD_REQUEST, )
        else:
            return Response({
                'message': 'Successful!',
                'success': True,
                'status_code': 200,
                'data': data
            }, status = status.HTTP_200_OK)

    else:
        return Response({
            'message': 'Method not supported!',
            'status_code': 405,
            'success': False,
        }, status = status.HTTP_405_METHOD_NOT_ALLOWED, )


