from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(req):
    return HttpResponse('<h1>My Second App</h1>')

def help(req):
    helpdict = {'help_insert': 'HELP PAGE'}
    return render(req, 'help/help.html',context=helpdict)