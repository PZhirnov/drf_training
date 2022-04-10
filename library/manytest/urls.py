from django.urls import path, include
from manytest.views import test


urlpatterns = [
    path('', test, name='test'),
]


