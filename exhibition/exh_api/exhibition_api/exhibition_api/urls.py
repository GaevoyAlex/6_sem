from django.urls import path
from django.contrib import admin
from exh_app.views import (
    create_creator,
    create_event,
    auth_creator,
    get_creator,
    create_user,
    get_eventsr,
    get_user
    
)


urlpatterns = [
    path('admin/', admin.site.urls),

    path('creator/', create_creator, name='create_creator'),
    path('user/create/', create_user, name='get_creator'),
    path('creator/auth/', auth_creator, name='auth_creator'),
    path('event/', create_event, name='create_event'),
    path('creator/get/', get_creator, name='get_creator'),
    path('event/get/', get_eventsr, name='get_creator'),
    path('user/get/', get_user, name='get_creator'),



]