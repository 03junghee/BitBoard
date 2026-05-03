from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), # 홈페이지 주소
]