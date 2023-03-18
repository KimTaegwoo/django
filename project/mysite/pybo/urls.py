# 여기 폴더의 url을 처리한다.

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('1/', views.index),
]

