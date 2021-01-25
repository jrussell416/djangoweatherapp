from django.shortcuts import render

# Create your views here.
#need to define a view using a function
def home(request):
    return render(request, 'home.html', {})

def about(request):
    return render(request, 'about.html', {})