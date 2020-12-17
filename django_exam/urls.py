from exam_test import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('insert/', views.index),
    path('', views.xiala_all),
    path('score/<random_li>/', views.score,name ='score' ),


]
