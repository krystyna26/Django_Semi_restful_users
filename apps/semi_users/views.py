
from __future__ import unicode_literals
from django.contrib.messages import error
from django.shortcuts import render, HttpResponse, redirect
from .models import User 

def index(request):
    context = {
        "userList": User.objects.all()
        }
    return render(request, "semi_users/index.html", context)



def new(request):
    return render(request,"semi_users/new.html")



def create(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors):
        for field, message in errors.iteritems():
            error(request, message, extra_tags=field)
        return redirect('/users/new')
    User.objects.create(
        first_name=request.POST['first_name'],
        last_name=request.POST['last_name'],
        email=request.POST['email'],
        # created_at=strftime("%H:%M:%S, %B %d, %Y", gmtime()
    )
    return redirect("/users")



def show(request, id):
    userObj = User.objects.get(id = id)
    return render(request, "semi_users/show.html", {"user":userObj})



def edit(request, id):
    userObj = User.objects.get(id = id)
    print "edit"
    return render(request, "semi_users/edit.html", {"user":userObj})



def update(request, id):
    errors = User.objects.basic_validator(request.POST)
    if len(errors):
        for field, message in errors.iteritems():
            error(request, message, extra_tags=field)    
        return redirect('/users/{}/edit'.format(id))

    u = User.objects.get(id=id)
    # instead of a multi-line update, try this:
    # User.objects.filter(id=id).update(your params)
    u.first_name = request.POST['first_name']
    u.last_name = request.POST['last_name']
    u.email = request.POST['email']
    u.save()
    return redirect('/users')



def destroy(request, id):
    dest = User.objects.get(id = id)
    dest.delete()
    return redirect('/users')