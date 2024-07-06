from django.urls import path
from . import views

urlpatterns = [
   
    path('', views.timeanddate_list, name='timeanddate_list'),  # List TimeAndDate
    path('timeanddate/new/', views.timeanddate_create, name='timeanddate_create'),  # Create TimeAndDate
    path('set_timezone/', views.set_user_timezone, name='set_user_timezone'),

]
