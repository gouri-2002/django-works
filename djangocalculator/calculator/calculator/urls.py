"""
URL configuration for calculator project.

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
from operations.views import AdditionView
from operations.views import SubstractionView
from operations.views import MultiplicationView
from operations.views import CubeView
from operations.views import BmiView
from operations.views import EmiView,BmrView,WeightManagementView,MilageView,SignupView,CustomerRegistrationView,IndexView




urlpatterns = [
    path('admin/', admin.site.urls),
    path('add/',AdditionView.as_view(),name="addition"),
    path('subb/',SubstractionView.as_view(),name="subtration"),
    path('multi/',MultiplicationView.as_view()),
    path('cube/',CubeView.as_view()),
    path('bmi/',BmiView.as_view()),
    path('emi/',EmiView.as_view()),
    path('bmr/',BmrView.as_view()),
    path('weight_management/',WeightManagementView.as_view()),
    path('milage/',MilageView.as_view()),
    path('signup/',SignupView.as_view()),
    path('registration/',CustomerRegistrationView.as_view()),
    path("",IndexView.as_view())
]
