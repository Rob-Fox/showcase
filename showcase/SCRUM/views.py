from django.shortcuts import render, redirect
# from django.http import HttpResponse
# from django.template import loader
from .models import *
from login_reg.models import User

# Create your views here.
# def index(req, *arg_data, **kwarg_data):
def index(req):
    if req.session.get('user') == None or req.session.get('user') == -1:
        return redirect('login_reg:index') 
    context = {
        'projectList': Project.objects.filter(head=User.objects.get(id=req.session['user'])),
        'participating': Project.objects.filter(members=req.session['user']),
    }
    return render(req, 'SCRUM/index.html', context)

def project(req, id):
    print('hello')
    if req.session.get('user') == None or req.session.get('user') == -1:
        return redirect('login_reg:index')
    project = Project.objects.get(id=id)
    context = {
        'project': project,
        'taskList': project.task_set.all(),
        'teamMembers': project.members,
        
    }
    return render(req, 'SCRUM/project.html', context)
    # return render(req, 'SCRUM/project.html', context={})
