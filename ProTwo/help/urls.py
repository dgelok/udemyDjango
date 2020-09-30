from django.conf.urls import url
from help import views

urlpatterns = [ 
    url(r'help', views.index, name="index"),
]