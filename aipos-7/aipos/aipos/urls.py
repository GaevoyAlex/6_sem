from django.contrib import admin
from django.urls import path

from myapp.views import get_restaurants, create_restaurant, update_restaurant, delete_restaurant,get_tables,create_table,update_table,delete_table,get_reservations,create_reservation,update_reservation,delete_reservation

urlpatterns = [
    path('admin/', admin.site.urls),

    path('restaurants/', get_restaurants, name='get_restaurants'),
    path('restaurants/create/', create_restaurant, name='create_restaurant'),
    path('restaurants/<int:restaurant_id>/', update_restaurant, name='update_restaurant'),
    path('restaurants/<int:restaurant_id>/delete/', delete_restaurant, name='delete_restaurant'),
        
    path('tables/', get_tables, name='get_tables'), # URL для получения списка всех таблиц
    path('tables/create/', create_table, name='create_table'), # URL для создания новой таблицы
    path('tables/update/<int:table_id>/', update_table, name='update_table'), # URL для обновления существующей таблицы по ее идентификатору
    path('tables/delete/<int:table_id>/', delete_table, name='delete_table'), # URL для удаления существующей таблицы по ее идентификатору

    
    # ... другие URL для ресторанов и таблиц
    path('reservations/', get_reservations, name='get_reservations'), # URL для получения списка всех бронирований
    path('reservations/create/', create_reservation, name='create_reservation'), # URL для создания нового бронирования
    path('reservations/update/<int:reservation_id>/', update_reservation, name='update_reservation'), # URL для обновления существующего бронирования по его идентификатору
    path('reservations/delete/<int:reservation_id>/', delete_reservation, name='delete_reservation'), # URL для удаления существующего бронирования по его идентификатору
]