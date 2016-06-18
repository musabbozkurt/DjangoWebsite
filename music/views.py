from django.http import HttpResponse
from .models import Album

def index(request):
    return HttpResponse("<h1> album list</h1>")