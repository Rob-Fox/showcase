from django.urls import path
from . import views

app_name = 'SCRUM'

urlpatterns = [
    path('', views.index, name='index'),
    # path('/project/', views.project, name='project'),
    path('/project/<int:id>',views.project,name='project'),
]