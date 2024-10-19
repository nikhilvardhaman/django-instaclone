from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    fav_color = request.GET["fav_color"]

    message = "I don't have anything to say about your fav color"

    if fav_color == "blue":
        message = 'sky is blue'
    elif fav_color == "yellow":
        message = 'sun is yellow'

    return HttpResponse(message)

