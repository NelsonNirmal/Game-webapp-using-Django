"""game URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [
    path("signup/",views.signup1),
    path("insertuser/",views.signup,name='home'),
    path("",views.login,name='login'),
    path("check/",views.check),
    path('<str:direct>/xox/', views.xox),
    path('<str:direct>/rps/', views.rps),
    path('<str:direct>/snake/', views.snake),
    path('<str:direct>/pong/', views.pong),
    path('<str:direct>/brick/',views.brick),
    path('<str:direct>/memory/',views.memory),
    path('<str:direct>/mole/',views.mole),
    path('<str:direct>/frogger/',views.frogger),
    path('<str:direct>/2048/',views.game_2048),
    path('<str:direct>/connect/',views.connect),
    path('<str:direct>/mainsweeper/',views.mainsweeper)


]
