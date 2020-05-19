from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.homePage),
    path('maker',views.maker),
    path('masked',views.make),
    path('simple',views.simple),
    path('gallery',views.gallery),
    path('creator',views.creator)
]
