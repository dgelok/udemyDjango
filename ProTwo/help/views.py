from django.shortcuts import render


# Create your views here.
def help(req):
    mydict = {
        'mytag':'<h1>Help Page</h1>'
    }
    return HttpResponse(req,'help/',context=mydict)