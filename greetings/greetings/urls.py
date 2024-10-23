"""
URL configuration for greetings project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from myapp.views import HelloWorldView
from myapp.views import GoodMorningView
from myapp.views import GoodAfternoonVIew
from myapp.views import GoodEveningVIew
from myapp.views import GoodNightView
from myapp.views import SelfIntroView
from myapp.views import FrameWorkView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('HelloWorld/',HelloWorldView.as_view()),
    path('goodmorning/',GoodMorningView.as_view()),
    path('goodafternoon/',GoodAfternoonVIew.as_view()),
    path('goodevening/',GoodEveningVIew.as_view()),
    path('goodnight/',GoodNightView.as_view()),
    path('selfintro/',SelfIntroView.as_view()),
    path('framework/',FrameWorkView.as_view()),
]
