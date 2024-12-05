from django.shortcuts import render
from django.http import HttpResponse
from .models import Member
from django.template import loader

# Create your views here.
def view_td(request):
    return HttpResponse("Hello")

def index(request):
    return render(request, 'index.html')

def member(request):
    mymembers = Member.objects.all().values()
    template = loader.get_template('all_members.html')
    context = {
        'mymembers': mymembers,
        }
    return HttpResponse(template.render(context, request))