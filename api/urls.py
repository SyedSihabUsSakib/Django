from home.views import index, people, color
from django.urls import path

urlpatterns = [
    path('index/', index),
    path('people/', people),
    path('color/', color)
]
