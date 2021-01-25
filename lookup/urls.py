from django.urls import path
#need to import views (the "." indicates that we are improting from the directory we are already in)
from . import views

urlpatterns = [
    #everytime a new webpage is created in our app, the page path goes here
    path('', views.home, name ="home"),
    path('about.html', views.about, name="about"),
]