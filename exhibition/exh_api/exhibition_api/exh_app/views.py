from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.response import Response
from .models import Creator, Event, User
from exhibition_api.serialize import CreatorSerializer, EventSerializer, UserSerializer
from django.contrib.auth import authenticate
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response


@csrf_exempt
def get_creator(request):
    
    creator = Creator.objects.all()
    serializer = CreatorSerializer(creator, many=True)
    return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def get_eventsr(request):
    
    creator = Event.objects.all()
    serializer = EventSerializer(creator, many=True)
    return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def get_user(request):
    
    creator = User.objects.all()
    serializer = UserSerializer(creator, many=True)
    return JsonResponse(serializer.data, safe=False)

@api_view(['POST']) # добавьте декоратор с разрешенным методом
def create_user(request):
    
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data) # используйте request.data
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        
        return Response(serializer.errors, status=400)
    else:
        
        return Response({'error': 'Invalid request method'}, status=400)


@api_view(['POST']) # добавьте декоратор с разрешенным методом
def create_creator(request):
    
    if request.method == 'POST':
        serializer = CreatorSerializer(data=request.data) # используйте request.data
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        
        return Response(serializer.errors, status=400)
    else:
        
        return Response({'error': 'Invalid request method'}, status=400)
    
@api_view(['POST'])
def auth_creator(request):
    
    if request.method == 'POST':
        # получаем логин и пароль из запроса
        login = request.data.get('login')
        password = request.data.get('password')
        # пытаемся аутентифицировать пользователя
        user = authenticate(username=login, password=password)
        # если пользователь существует, возвращаем статус 200
        if user is not None:
            return Response({'message': 'User exists'}, status=200)
        # если нет, возвращаем ошибку
        else:
            return Response({'error': 'Invalid login or password'}, status=400)
    else:
        
        return Response({'error': 'Invalid request method'}, status=400)


@api_view(['POST']) # добавьте декоратор с разрешенным методом
def create_event(request):
   
    if request.method == 'POST':
        serializer = EventSerializer(data=request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        
        return Response(serializer.errors, status=400)
    else:
        
        return Response({'error': 'Invalid request method'}, status=400)