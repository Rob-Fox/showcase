from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import User as User
from SCRUM.models import Task as Task
from django.contrib import messages
import bcrypt


def index(req):
    req.session['user'] = -1
    return render(req, 'login_reg/index.html')

def registration(req):
    errors = User.objects.registration_validator(req.POST)
    if len(errors):
        for tag, error in errors.items():
            messages.error(req, error, extra_tags=tag)
        return redirect('/')
    else:
        p_word = bcrypt.hashpw(req.POST['password'].encode(), bcrypt.gensalt())
        user = User.objects.create(name=req.POST['name'], username=req.POST['username'], password=p_word)
        user.save()
        print(user)
        req.session['user'] = user.id
        return redirect('/success')

def login(req):
    errors = User.objects.login_validator(req.POST)
    if len(errors):
        for tag, error in errors.items():
            messages.error(req, error, extra_tags=tag)
        return redirect('/')
    else:
        req.session['user'] = User.objects.get(username=req.POST['l_username']).id
        return redirect('/success')

def success(req):
    if req.session['user'] == -1:
        return redirect('/')
    user = User.objects.get(id=req.session['user'])
    taskList = Task.objects.filter(creator=user)
    context={
        'name':user.name,
        'taskList':taskList,
    }
    # return redirect('SCRUM:index', context=context)
    # return render(req, 'SCRUM/index.html', context)
    return redirect('SCRUM:index')