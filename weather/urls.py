from django.urls import path
from .views import *

urlpatterns = [
    path('home/', home),
    path('item/', item),
    path('about/', about),
]