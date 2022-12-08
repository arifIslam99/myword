#from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Members

# Create your views here.


def index(request):
    #template=loader.get_template('index.html')
    #return HttpResponse("<h2>Welcome Users!</h2>")
    #return HttpResponse(template.render())
    mymembers=Members.objects.all().values()
    # output=""
    # for x in mymembers:
    #     output+=x['name']+"<br>"
    # return HttpResponse(output)
    template=loader.get_template('index.html')
    context={
        'mymembers':mymembers,
    }
    return HttpResponse(template.render(context,request))

def add(request):
    template=loader.get_template('add.html')
    return HttpResponse(template.render({}, request))

def addrecord(request):
    x=request.POST['name']
    y=request.POST['address']
    member=Members(name=x,address=y)
    member.save()
    return HttpResponseRedirect(reverse('index'))

def delete(request, id):
    member=Members.objects.get(id=id)
    member.delete()
    return HttpResponseRedirect(reverse('index'))

def edit(request, id):
    member=Members.objects.get(id=id)
    template=loader.get_template('edit.html')
    context={
        'member':member,
    }
    return HttpResponse(template.render(context,request))

def update(request, id):
    x=request.POST['name']
    y=request.POST['address']
    member=Members.objects.get(id=id)
    member.name=x
    member.address=y
    member.save()
    return HttpResponseRedirect(reverse('index'))

def profile(request):
    template=loader.get_template('profile.html')

    return HttpResponse(template.render())