from django.urls import path
from . import views

app_name = 'login_reg'

urlpatterns = [
    path('', views.index, name='index'),
    path('reg', views.registration, name='registration'),
    path('success', views.success, name='success'),
    path('login', views.login, name='login'),
]