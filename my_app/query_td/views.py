from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def view_td(request):
    return HttpResponse("Hello")

def index(request):
    return render(request, 'index.html')