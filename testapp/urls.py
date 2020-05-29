from django.contrib import admin
from django.urls import path,include
from .views import testpage
urlpatterns = [
    path('testpage/',testpage)

]