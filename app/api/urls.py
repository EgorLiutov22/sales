from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from . import views

urlpatterns = [
    path('customer/', views.CustomerViewSet.as_view({'get': 'list'})),
    # path('api/', include('api.urls', namespace='api'))
]