from rest_framework import serializers
from .models import *

class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
     model=Passenger
     fields=['firstname','lastname','travelpoints']