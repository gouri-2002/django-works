from django.shortcuts import render

from django.views.generic import View

from crm.forms import CarsForm

class CarsView(View):

    template_name="cars.html"
    form_class=CarsForm

    def get(self,request,*args,**kwargs):

        form_instance=self.form_class()

        return render(request,self.template_name,{"form":form_instance})




