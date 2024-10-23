
from django.views.generic import View
from django.http import HttpResponse
from django.shortcuts import render

class HelloWorldView(View):

    def get(self,request,*args,**kwargs):

        return HttpResponse("Hello World")
    
    
class GoodMorningView(View):
    def get(self,request,*args,**kwargs):

        return HttpResponse("Good Morning")
    

class GoodAfternoonVIew(View):
    def get(self,request,*args,**kwargs):
        return HttpResponse("Good Afternoon")    
    
class GoodEveningVIew(View):
    def get(self,request,*args,**kwargs):
        return HttpResponse("Good Evening")  

class GoodNightView(View):
    def get(self,request,*args,**kwargs):
        return HttpResponse("Good Night")  


class SelfIntroView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"selfintro.html")  

class FrameWorkView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"framework.html")      

    
