from django.shortcuts import render

# Create your views here.
#need to define a view using a function
def home(request):
    import json
    import requests

    api_request = requests.get("http://api.weatherapi.com/v1/current.json?key=8bbd43bbdc5f421e8ce01116212601&q=M9W2Y2")
    try:
        api = json.loads(api_request.content)
    except Exception as e:
        api = "Error..."
    return render(request, 'home.html', {'api':api})

def about(request):
    return render(request, 'about.html', {})