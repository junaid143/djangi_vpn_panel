
from rest_framework import serializers
from . models import VpnModel


class VpnSerializer(serializers.ModelSerializer):
    class Meta:
        model = VpnModel
        fields = [ 'hostname' , 'countryshort' , 'username' ,'password','config' , 'is_enable']