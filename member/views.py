# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member

def members(request):
    mymember = Member.objects.all().values()
    template = loader.get_template('all_member.html')
    context = {'mymember' : mymember}
    return HttpResponse(template.render(context,request))


def login(request):
    return HttpResponse("Welcome to login")
