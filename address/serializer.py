from rest_framework import serializers

class ListAddressSubjectionSerializer(serializers.Serializer):

    keyword = serializers.CharField(max_length = 40)
    # number = serializers.CharField(max_length = 40)
    # street = serializers.CharField(max_length = 40)
    # ward = serializers.CharField(max_length = 40)
    # district = serializers.CharField(max_length = 40)


class AddressSerializer(serializers.Serializer):
    city = serializers.CharField(max_length = 40)


class GeoSerializer(serializers.Serializer):
    lat = serializers.FloatField()
    lng = serializers.FloatField()
    # lat = serializers.CharField(max_length = 40)
    # lng = serializers.CharField(max_length = 40)

class LocationIdSerializer(serializers.Serializer):
    location_id = serializers.CharField(max_length = 100)