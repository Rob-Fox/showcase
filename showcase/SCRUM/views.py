from django.shortcuts import render, redirect
# from django.http import HttpResponse
# from django.template import loader
from .models import *
from login_reg.models import User

# Create your views here.
# def index(req, *arg_data, **kwarg_data):
def index(req):
    if req.session.get('user') == None:
        return redirect('login_reg:index') 
    context = {
        'taskList': Task.objects.filter(creator=User.objects.get(id=req.session['user']))
    }
    # return HttpResponse('hello world')
    # return render(request, 'SCRUM/index.html')
    # taskList = Task.objects.all()
    # context = {
    #     'taskList': taskList,
    # }
    return render(req, 'SCRUM/index.html', context)