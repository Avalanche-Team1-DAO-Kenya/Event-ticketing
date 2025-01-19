from django.urls import path
from . import views

urlpatterns = [
    path('fetch-data/', views.fetch_and_store_data, name='fetch_and_store_data'),
]



