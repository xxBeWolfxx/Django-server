from rest_framework import serializers 
from .models import User, ESPSensor, ESPOut

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ['id','name','lastname','email', 'login', 'password', 'ESPoCount', 'ESPsCount']


class ESPSensorSerializer(serializers.ModelSerializer):
	class Meta:
		model = ESPSensor
		fields = ['id', 'name', 'pin', 'valueTemp', 'valueAvgDay', 'valueAvgWeek', 'description']
		
class ESPOutSerializer(serializers.ModelSerializer):
	class Meta:
		model = ESPOut
		fields = ['id', 'name', 'pin', 'status', 'description']
		
		
