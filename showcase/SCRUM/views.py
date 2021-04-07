from django.shortcuts import render
# from django.http import HttpResponse
# from django.template import loader
from .models import *

# Create your views here.
def index(req):
    # return HttpResponse('hello world')
    # return render(request, 'SCRUM/index.html')
    taskList = Task.objects.all()
    context = {
        'taskList': taskList,
    }
    return render(req, 'SCRUM/index.html', context)