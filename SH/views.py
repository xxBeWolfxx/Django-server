from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import *
from .serializers import *
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.apps import apps
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

    
@api_view(['GET','POST','PUT'])
def ESPSensor_list(request, user_id = 3):
    try:
        user = User.objects.get(pk = user_id)
    except User.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    
    
    if request.method == 'GET':
        espS = user.ESPsensor.all()
        serializer = ESPSensorSerializer(espS, many = True)
        return Response(serializer.data)
        
    elif request.method == 'PUT':
        serializer = ESPSensorSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
@api_view(['GET','DELETE','PUT'])
def ESPSensor_listdetail(request, esp_id):
    try:
        esp = ESPSensor.objects.get(pk = esp_id)
    except ESPSensor.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
    if request.method == 'GET':
        serializer = ESPSensorSerializer(esp)
        return Response(serializer.data)
    
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ESPSensorSerializer(esp, data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        esp.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
    
@api_view(['GET','POST','PUT'])
def ESPOut_list(request, user_id = 3):
    try:
        user = User.objects.get(pk = user_id)
    except User.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        espO = user.ESPoutputs.all()
        serializer = ESPOutSerializer(espO, many = True)
        return Response(serializer.data)
        
    elif request.method == 'PUT':
        serializer = ESPOutSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
@api_view(['GET','DELETE','PUT'])
def ESPOut_listdetail(request, esp_id):
    try:
        esp = ESPOut.objects.get(pk = esp_id)
    except ESPOut.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
    if request.method == 'GET':
        serializer = ESPOutSerializer(esp)
        return Response(serializer.data)
    
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ESPOutSerializer(esp, data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        esp.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
   
   
    
@api_view(['GET','POST','PUT'])
def User_list(request):
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many = True)
        return Response(serializer.data)
        
    elif request.method == 'POST':
        serializer = UserSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','DELETE','PUT'])
def User_listdetail(request, user_id):
    try:
        user = User.objects.get(pk = user_id)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
        
    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)
    
    
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = UserSerializer(user, data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        user.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)


@csrf_exempt
def GetUser(request, login):
    try:
        model=User.objects.get(login = login)    
    except User.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        model.ESPoCount = model.ESPoutputs.all().count()  
        model.ESPsCount = model.ESPsensor.all().count()  
        model.save()
        serializer = UserSerializer(model)
    return JsonResponse(serializer.data)
