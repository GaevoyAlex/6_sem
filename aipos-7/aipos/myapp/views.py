from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from .models import Restaurant, Table, Reservation
from rest_framework.response import Response
import logging

from .serializers import RestaurantSerializer, TableSerializer, ReservationSerializer

logger = logging.getLogger('access')

@csrf_exempt
def get_restaurants(request):
    logger.info('GET request received for restaurants')
    restaurants = Restaurant.objects.all()
    serializer = RestaurantSerializer(restaurants, many=True)
    return JsonResponse(serializer.data, safe=False)

@api_view(['POST']) # добавьте декоратор с разрешенным методом
def create_restaurant(request):
    logger.info('POST request received for creating a restaurant')
    if request.method == 'POST':
        serializer = RestaurantSerializer(data=request.data) # используйте request.data
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        logger.warning('Invalid request: {}'.format(serializer.errors))
        return Response(serializer.errors, status=400)
    else:
        logger.warning('Invalid request method')
        return Response({'error': 'Invalid request method'}, status=400)
@csrf_exempt
def update_restaurant(request, restaurant_id):
    try:
        restaurant = Restaurant.objects.get(id=restaurant_id)
    except Restaurant.DoesNotExist:
        return JsonResponse({'error': 'Restaurant not found'}, status=404)

    if request.method == 'PUT': # добавил проверку метода
        serializer = RestaurantSerializer(restaurant, data=request.data) # изменил request.PUT на request.data
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    else:
        
        return JsonResponse({'error': 'Invalid request method'}, status=400)

@csrf_exempt
def delete_restaurant(request, restaurant_id):
    try:
        restaurant = Restaurant.objects.get(id=restaurant_id)
    except Restaurant.DoesNotExist:
        logger.warning('Restaurant not found')
        return JsonResponse({'error': 'Restaurant not found'}, status=404)
    
    if request.method == 'DELETE':
        restaurant.delete()
        return JsonResponse({'message': 'Restaurant deleted'})
    else:
        logger.warning('Invalid request method')
        return JsonResponse({'error': 'Invalid request method'}, status=400)
    




@api_view(['GET'])
def get_tables(request):
    logger.info('GET request received for tables')
    tables = Table.objects.all() # получите все объекты таблиц из базы данных
    serializer = TableSerializer(tables, many=True) # сериализуйте их в JSON-формат
    return Response(serializer.data, status=200) # отправьте ответ с данными и статусом 200 (OK)

@api_view(['POST'])
def create_table(request):
    logger.info('POST request received for creating a tables')
    if request.method == 'POST':
        serializer = TableSerializer(data=request.data) # десериализуйте данные из JSON-тела запроса
        if serializer.is_valid():
            serializer.save() # сохраните объект таблицы в базу данных
            return Response(serializer.data, status=201)
        logger.warning('Invalid request: {}'.format(serializer.errors)) 
        return Response(serializer.errors, status=400) # отправьте ответ с ошибками и статусом 400 (Bad Request)
    else:
        logger.warning('Invalid request method')
        return Response({'error': 'Invalid request method'}, status=400) # отправьте ответ с ошибкой и статусом 400 (Bad Request)

@api_view(['PUT'])
def update_table(request, table_id):
    try:
        table = Table.objects.get(id=table_id) # получите объект таблицы по его идентификатору из базы данных
    except Table.DoesNotExist:
        return Response({'error': 'Table not found'}, status=404) # отправьте ответ с ошибкой и статусом 404 (Not Found)

    if request.method == 'PUT':
        serializer = TableSerializer(table, data=request.data) # десериализуйте данные из JSON-тела запроса и обновите объект таблицы
        if serializer.is_valid():
            serializer.save() # сохраните объект таблицы в базу данных
            return Response(serializer.data)
        logger.warning('Invalid request: {}'.format(serializer.errors))
        
        return Response(serializer.errors, status=400) # отправьте ответ с ошибками и статусом 400 (Bad Request)
    else:
        return Response({'error': 'Invalid request method'}, status=400) # отправьте ответ с ошибкой и статусом 400 (Bad Request)

@api_view(['DELETE'])
def delete_table(request, table_id):
    try:
        table = Table.objects.get(id=table_id) # получите объект таблицы по его идентификатору из базы данных
    except Table.DoesNotExist:
        return Response({'error': 'Table not found'}, status=404) # отправьте ответ с ошибкой и статусом 404 (Not Found)

    if request.method == 'DELETE':
        table.delete() # удалите объект таблицы из базы данных
        return Response({'message': 'Table deleted'}) # отправьте ответ с сообщением и статусом 200 (OK)
    else:
        return Response({'error': 'Invalid request method'}, status=400) # отправьте ответ с ошибкой и статусом 400 (Bad Request)
    


@api_view(['GET'])
def get_reservations(request):
    logger.info('GET request received for tables')
    reservations = Reservation.objects.all() # получите все объекты бронирований из базы данных
    serializer = ReservationSerializer(reservations, many=True) # сериализуйте их в JSON-формат
    return Response(serializer.data, status=200) # отправьте ответ с данными и статусом 200 (OK)

@api_view(['POST'])
def create_reservation(request):
    if request.method == 'POST':
        serializer = ReservationSerializer(data=request.data) # десериализуйте данные из JSON-тела запроса
        if serializer.is_valid():
            serializer.save() # сохраните объект бронирования в базу данных
            return Response(serializer.data, status=201) # отправьте ответ с данными и статусом 201 (Created)
        logger.warning('Invalid request: {}'.format(serializer.errors)) 
        return Response(serializer.errors, status=400) # отправьте ответ с ошибками и статусом 400 (Bad Request)
    else:
        logger.warning('Invalid request method')
        return Response({'error': 'Invalid request method'}, status=400) # отправьте ответ с ошибкой и статусом 400 (Bad Request)

@api_view(['PUT'])
def update_reservation(request, reservation_id):
    try:
        reservation = Reservation.objects.get(id=reservation_id) # получите объект бронирования по его идентификатору из базы данных
    except Reservation.DoesNotExist:
        return Response({'error': 'Reservation not found'}, status=404) # отправьте ответ с ошибкой и статусом 404 (Not Found)

    if request.method == 'PUT':
        serializer = ReservationSerializer(reservation, data=request.data) # десериализуйте данные из JSON-тела запроса и обновите объект бронирования
        if serializer.is_valid():
            serializer.save() # сохраните объект бронирования в базу данных
            return Response(serializer.data) # отправьте ответ с данными и статусом 200 (OK)
        return Response(serializer.errors, status=400) # отправьте ответ с ошибками и статусом 400 (Bad Request)
    else:
        return Response({'error': 'Invalid request method'}, status=400) # отправьте ответ с ошибкой и статусом 400 (Bad Request)

@api_view(['DELETE'])
def delete_reservation(request, reservation_id):
    try:
        reservation = Reservation.objects.get(id=reservation_id) # получите объект бронирования по его идентификатору из базы данных
    except Reservation.DoesNotExist:
        return Response({'error': 'Reservation not found'}, status=404) # отправьте ответ с ошибкой и статусом 404 (Not Found)

    if request.method == 'DELETE':
        reservation.delete() # удалите объект бронирования из базы данных
        return Response({'message': 'Reservation deleted'}) # отправьте ответ с сообщением и статусом 200 (OK)
    else:
        return Response({'error': 'Invalid request method'}, status=400) # отправьте ответ с ошибкой и статусом 400 (Bad Request)


