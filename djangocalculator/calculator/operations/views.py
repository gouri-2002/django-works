from django import forms
from django.shortcuts import render
from django.views.generic import View
from operations.forms import BmiForm
from operations.forms import EmiForm,BmrForm,WeightManagementForm,MilageForm,SignupForm,CustomerRegritrationForm





class AdditionView(View):
    template_name="Addition.html"


    def get(self,request,*args,**kwargs):

        return render(request,self.template_name)
    
    def post(self,request,*args,**kwargs):
        n1=request.POST.get("num1")
        n2=request.POST.get("num2")

        result=int(n1)+int(n2)
        print(result)

        return render(request,self.template_name,{"result":result})
    



class SubstractionView(View):
    template_name="sub.html"


    def get(self,request,*args,**kwargs):

        return render(request,self.template_name)
    
    def post(self,request,*args,**kwargs):
        n1=request.POST.get("num1")
        n2=request.POST.get("num2")

        result=int(n1)-int(n2)
        print(result)

        return render(request,self.template_name,{"result":result})
    
    # multiplication
    # division 
    # cube



class MultiplicationView(View):
    template_name="multi.html"


    def get(self,request,*args,**kwargs):

        return render(request,self.template_name)
    
    def post(self,request,*args,**kwargs):
        n1=request.POST.get("num1")
        n2=request.POST.get("num2")

        result=int(n1)*int(n2)
        print(result)

        return render(request,self.template_name,{"result":result})    
    



class CubeView(View):
    template_name="cube.html"


    def get(self,request,*args,**kwargs):

        return render(request,self.template_name)
    
    def post(self,request,*args,**kwargs):
        n=request.POST.get("num")
        result=int(n)*3
        print(result)

        return render(request,self.template_name,{"result":result})    
    




    #BMI





class BmiView(View):

    template_name="bmi.html"

    def get(self,request,*args,**kwargs):

        form_instance=BmiForm()

        return render(request,self.template_name,{"form":form_instance})
    
    def post(self,request,*args,**kwargs):

        # extract data

        form_data=request.POST

        form_instance=BmiForm(form_data)

        # check valid or invalid

        if form_instance.is_valid():

            Height=form_instance.cleaned_data.get("height")
            weight=form_instance.cleaned_data.get("weight")

            bmi=weight/(Height/100)**2

            print(form_instance.cleaned_data)

            print("valid")

            return render(request,self.template_name,{"form":form_instance,"result":bmi})





    
# emi

class EmiView(View):
    
    template = "emi.html"
    
    def get(self, request, *args, **kwargs):
        
        emi_form=EmiForm()
        
        return render(request, self.template, {'form':emi_form})
    
    def post(self, request, *args, **kwargs):
        
        emi_form=EmiForm()
        form_data = request.POST
        
        amount = int(form_data.get('loan_amount'))
        tenure = int(form_data.get('tenure'))
        interest = float(form_data.get('loan_amount'))
        
        X = (1 + interest)**tenure
        emi = (amount * interest * X)/(X - 1)
        
        return render(request, self.template, {'form':emi_form, 'result':emi})
    



# BMRRRR



def calculate_bmr(height,weight,age,gender):

    if gender=="male":

        bmr=10*weight+6.25*height-5*age+5

    else:
         
        bmr=10*weight+6.25*height-5*age-161

    return bmr   

def daily_calorie_intake(bmr,activity):
    return float(activity)*bmr


        

class BmrView(View):

    template_name="bmr.html"

    def get(self,request,*args,**kwargs):

        form_instance=BmrForm()

        return render(request,self.template_name,{"form":form_instance})
    
    def post(self,request,*args,**kwargs):

        form_data=request.POST

        form_instance=BmrForm(form_data)

        if form_instance.is_valid():

            data=form_instance.cleaned_data

            height=data.get("height")
            weight=data.get("weight")
            age=data.get("age")
            gender=data.get("gender")
            activity=data.get("activity")

            print(height,weight,age,gender,activity)

            bmr=calculate_bmr(height,weight,age,gender)

            calorie=daily_calorie_intake(bmr,activity)

            print(calorie)


            return render(request,self.template_name,{"form":form_instance})  



# WEIGHT_MANAGEMENT

        
def calculate_bmr(height,weight,age,gender):

    if gender=="male":

       bmr=10*weight+6.25*height-5*age+5

    else:
         
        bmr=10*weight+6.25*height-5*age-161

    return bmr   
def daily_calorie_intake(bmr,activity):
    return float(activity)*bmr    



class WeightManagementView(View):

    template_name="weight_management.html"

    form_class=WeightManagementForm

    def get(self,request,*args,**kwargs):

        form_instance=self.form_class()

        return render(request,self.template_name,{"form":form_instance})
    
    def post(self,request,*args,**kwargs):

        form_data=request.POST

        form_instance=self.form_class(form_data)

        if form_instance.is_valid():

            data=form_instance.cleaned_data

            height=data.get("height")
            weight=data.get("weight")
            age=data.get("age")
            gender=data.get("gender")
            activity=data.get("activity")
            mode=data.get("mode")
            duration=data.get("duration")
            target_weight=data.get("target_weight")

            print(height,weight,age,gender,activity,mode,duration,target_weight)

            bmr=calculate_bmr(height,weight,age,gender)

            calorie=daily_calorie_intake(bmr,activity)

            target_calorie=target_weight*7700

            days=duration*7

            daily_target_calorie=target_calorie/days

            total_calorie=0

            if mode=="gain":
                total_calorie=calorie+daily_target_calorie
            else:
                total_calorie=calorie-daily_target_calorie 


            result=f"calorie to maintain current weight={round(calorie)}"
            result2=f"total daily calorie to {mode} in {target_weight}kg in{days}days={round(total_calorie)}"


            return render(request,self.template_name,{"form":form_instance,"result":result,"result2":result2})  



# milage
# distance
# fuel_consumed
# milage=distance_traveled/fuel_consumed


    
class MilageView(View):

    template_name="milage.html"

    form_class=MilageForm

    def get(self,request,*args,**kwargs):

        form_instance=self.form_class()

        return render(request,self.template_name,{"form":form_instance})
    
    def post(self,request,*args,**kwargs):

        form_data=request.POST

        form_instance=self.form_class(form_data)

        if form_instance.is_valid():

            data=form_instance.cleaned_data

            distance=data.get("distance")

            fuel_consumed=data.get("fuel_consumed")

            milage=distance/fuel_consumed

            return render(request,self.template_name,{"form":form_instance,"result":milage})
        

# perentage calculator
 
# amount
# percentage

# o/p
# amout=200
# percentage=25
#result=50


# degree_calsius to fh conversion

# fahrenheit to drgree_calsius

# leap_yr view


#signup FORM....


class SignupView(View):
    template_name="signup.html"
    form_class=SignupForm

    def get(self,request,*args,**kwargs):

        form_instance=self.form_class()
        return render(request,self.template_name,{"form":form_instance})
    

# NEW CUSTOMER REGISTRATION FORM    

class CustomerRegistrationView(View):
    template_name="customer.html"
    form_class=CustomerRegritrationForm
    
    def get(self,request,*args,**kwargs):

        form_instance=self.form_class()
        return render(request,self.template_name,{"form":form_instance})
    
class IndexView(View):
    template_name="index.html"
    def get(self,request,*args,**kwargs):
        
        return render(request,self.template_name)



        







