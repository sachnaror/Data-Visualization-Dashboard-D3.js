# data_visualization/urls.py
from django.urls import path

from . import views

urlpatterns = [

    path('data-points/', DataPointList.as_view(), name='data-point-list'),
    path('api/data/', views.DataListView.as_view(), name='data-list'),
]
