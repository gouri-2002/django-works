from django.shortcuts import render
from django.views.generic import View

class IndexView(View):
    def get(self,request,*args,**kwargs):

        person_data={
            "id":1,
            "age":32,
            "name":"Gouri",
            "location":"tvm",
            "address":"ph3dvhgv",
        }

        return render(request,"index.html",{"person":person_data})
    

class ProjectView(View):
    def get(self,request,*args,**kwargs):

        projects=[
            {"id":1,
             "title":"codehub",
             "description":"project description",
             "front_end":"react","back_end":"django"
             },

             {"id":2,
             "title":"serviceshub",
             "description":"project description",
             "front_end":"angular","back_end":"django"
             },
             {"id":3,
             "title":"linksphere",
             "description":"project description",
             "front_end":"react","back_end":"django"
             }

        ]
        
        return render(request,"project.html",{"projects":projects})
    

class ContactView(View):
    def get(self,request,*args,**kwargs):

        person_email="gouri@gmail.com"
        person_phoneno=9990088770
        person_address="h1meee"
        person_place="kollam"

        return render(request,"contact.html",{"email":person_email,"phoneno":person_phoneno,"address":person_address,"place":person_place})
    

class SkillsView(View):
    def get(self,request,*args,**kwargs):

        skills=["python","java","javascript","react","angular"] 

        return render(request,"skills.html",{"skills":skills}) 
    


class ServicesView(View):
    def get(self,request,*args,**kwargs):

        services=["webapplication development","api development","ui/ux"] 

        return render(request,"services.html",{"services":services}) 


    




        