from django.urls import path
from . import views

app_name = 'SCRUM'

urlpatterns = [
    path('', views.index, name='index'),
]