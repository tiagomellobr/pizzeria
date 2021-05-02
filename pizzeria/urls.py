from django.urls import path, include
from order import urls

urlpatterns = [
    path('', include(urls)),
]
