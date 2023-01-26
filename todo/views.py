from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from .models import Info


# Create your views here.
def index(request):
    data = Info.objects.all()
    context = {'items':data}
    print(data)
    return render(request, 'home.html',context)
    return render(request, 'index.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.create_user(username, email, password)
        user.save()
        return render(request, 'signin.html')
    return render(request, 'signup.html')

def signin(request):
    if  request.user.is_authenticated:
        # data = Info.objects.filter(user = request.user.id)
        data = Info.objects.all()
        print(data)
        return render(request, 'home.html',context = {'items':data})  
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user     = authenticate(request, username=username, password=password)
       
        if user is not None:
            login(request, user)
            # data = Info.objects.filter(user = user.id)
            data = Info.objects.all()
            print(data)
            return render(request, 'home.html',context = {'items':data})
    
        else:
            return render(request, 'signin.html')
   
    return render(request, 'signin.html')

def logout_view(request):
    logout(request)
    return render(request, 'signin.html')

def create(request):
    if  request.user.is_authenticated and request.method == "POST":
        title = request.POST['title']
        description = request.POST['description']

        info = Info(user = request.user, name = title, description = description)
        info.save()

        # data = Info.objects.filter(user = request.user.id)
        # data = Info.objects.all()
        # print(data)
        # return render(request, 'home.html',context = {'items':data})  
    return render(request, 'create.html') 