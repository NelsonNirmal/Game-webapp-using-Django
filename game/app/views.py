from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import gamesform
from .models import games

def login(request):
  return render(request,'app/login.html')

def check(request):
    name=request.POST['email']
    password=request.POST['password']
    check=games.objects.filter(email=name,password=password).values()
    print(check.exists())
    if check.exists():
        return render(request,'app/frontpage.html')
    else:
        return render(request,'app/login.html')




def signup1(request):
    games=gamesform()
    context={'form':games}
    return render(request,'app/signup.html',context)

def signup(request):
    if request.method=="POST":
        username=request.POST['email']
        password=request.POST['password']
        form=gamesform(request.POST)
        if form.is_valid():
            us=games(email=username,password=password)
            us.save()
    return render(request,'app/login.html')


def xox(request,direct):
    return render(request,'app/X.O.X.HTML')

def rps(request,direct):
    return  render(request,'app/r.p.s.html')

def snake(request,direct):
    return render(request,'app/snake.html')

def pong(request,direct):
    return render(request,'app/pong.html')

def brick(request,direct):
    return render(request,'app/brick.html')

def memory(request,direct):
    return render(request,'app/memory.html')

def mole(request,direct):
    return render(request,'app/mole.html')

def  frogger(request,direct):
    return render(request,'app/frogger.html')

def game_2048(request,direct):
    return render(request,'app/2048.html')

def connect(request,direct):
    return render(request,'app/connect.html')

def mainsweeper(request,direct):
    return render(request,'app/mainsweeper.html')
