from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(req):
    return HttpResponse('hello world')
    # return render(request, 'SCRUM/index.html')