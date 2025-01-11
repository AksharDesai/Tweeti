from django.shortcuts import render,redirect
from .forms import Tweetform
from .models import Tweet

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.forms import AuthenticationForm

from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def index(request):
    context={}
    tweets = Tweet.objects.all()
    context["tweets"]=tweets
    
    return render(request,'index.html',context)

def create(request):
    context={}
    
    
    if request.method == "POST":
       form = Tweetform(request.POST,request.FILES)
       form.save()
       return redirect('/')
       
    else:
        form = Tweetform()
    
    
    
    context["form"]=form
    return render(request,'create.html',context)

def edit(request,id):
    context={}
    tweet = Tweet.objects.get(id=id)
    if request.method == "POST":
       form = Tweetform(request.POST,request.FILES,instance=tweet)
       form.save()
       return redirect('/')
       
    else:#fills the value from the database
        
        
        form = Tweetform(instance=tweet)
        
    
    context["form"]=form
    context["id"]=id
    
    
    return render(request,'edit.html',context)


def delete(request,id):
    if request.method == "POST":
        tweet = Tweet.objects.get(id=id)
        tweet.delete()
        return redirect('/')
        

def view(request,id):
    context={}
    tweet = Tweet.objects.get(id=id)
    
    context["tweet"]=tweet
    return render(request,"view.html",context)



def User_signup(request):
    context={}
    if request.method == "POST":
       form = UserCreationForm(request.POST)
       if form.is_valid():
             form.save()
             return redirect("login")
        
  
        
    form = UserCreationForm()
    
    
    context["form"]=form    
    return render(request,'signup.html',context)


def User_login(request):
    context={}
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
        
            user = authenticate(username=username,password=password)
        
            if user is not None:
                login(request,user)
                return redirect("index")
            else:
                # Invalid credentials, you could add a message or some error handling
                return render(request, 'login.html', {'form': form, 'error': 'Invalid credentials'})
        
    else:
        
        form =AuthenticationForm()
    context["form"]=form
    return render(request,'login.html',context)


def User_logout(request):
    logout(request)
    return redirect('/')
    


