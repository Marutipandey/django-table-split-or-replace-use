# myproject/urls.py

from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name='home'),  # Homepage
    path('create/', views.create_data, name='create_data'),  # Create operation
    path('update/<int:id>/', views.update_data, name='update_data'),  # Update operation
    path('delete/<int:id>/', views.delete_data, name='delete_data'),  # Delete operation
]