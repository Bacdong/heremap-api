"""map URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from address.task import convert_address_to_geo
from address.task import request_autocomplete_suggestion
from address.task import convert_geo_to_address
from address.task import convert_geo_to_location_id

urlpatterns = [
    path('admin/', admin.site.urls),
    path('frontapi/map/get-geo-from-address', 
        convert_address_to_geo, name = "convert-address"),

    path('frontapi/map/get-address-subjection', 
        request_autocomplete_suggestion, name = 'get-subjection'),

    path('frontapi/map/get-address-from-geo',
        convert_geo_to_address, name = 'convert-geo'),
        
    path('frontapi/map/get-geo-from-location-id',
        convert_geo_to_location_id, name = 'get-geo-from-location-id'),
]
