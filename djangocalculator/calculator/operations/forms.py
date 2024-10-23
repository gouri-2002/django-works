
from django import forms

class BmiForm(forms.Form):

    height=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control mb-3"}))

    weight=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control mb-3"}))


class EmiForm(forms.Form):
    
    loan_amount = forms.IntegerField(label= 'Loan Amount',widget=forms.NumberInput(attrs={"class":"form-control mb-3"}))
    tenure = forms.IntegerField(label= 'Tenure',widget=forms.NumberInput(attrs={"class":"form-control mb-3"}))
    interest = forms.FloatField(label= 'Interest Rate',widget=forms.NumberInput(attrs={"class":"form-control mb-3"}))   



class BmrForm(forms.Form):

    # <input type="text" class="form-control" name="height">

    height=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control mb-3"}))
    weight=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control mb-3"}))
    age=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control mb-3"}))

    gender_choice=(
        ("male","male"),
        ("female","female")
    )

    gender=forms.ChoiceField(choices=gender_choice,widget=forms.Select(attrs={"class":"form-control form-select mb-3"}))    

    activity_choices=(

        (1.2,"sedentary"),
        (1.375,"lightly active"),
        (1.55,"moderately active"),
        (1.725,"very active"),
        (1.9,"extra active")

    )


    activity=forms.ChoiceField(choices=activity_choices,widget=forms.Select(attrs={"class":"form-control form-select mb-3"}))



class WeightManagementForm(BmrForm):

    mode_choice=(

        ("gain","gain"),
        ("loss","loss")
    )

    mode=forms.ChoiceField(choices=mode_choice,widget=forms.Select(attrs={"class":"form-control mb-3"}))

    duration=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control mb-3"}))

    target_weight=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control mb-3"}))



class MilageForm(forms.Form):

    distance=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control mb-3"}))
    fuel_consumed=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control mb-3"}))


class SignupForm(forms.Form):

    first_name=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control mb-3"}))
    last_name=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control mb-3"}))
    email=forms.CharField(widget=forms.EmailInput(attrs={"class":"form-control mb-3"}))
    password= forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control mb-3"}))
    

class CustomerRegritrationForm(forms.Form):

    first_name=forms.CharField(label="fullname",widget=forms.TextInput(attrs={"class":"form-control mb-3"}))
    last_name=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control mb-3"}))
    address=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control mb-3","rows":5}))
    city=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control mb-3"}))
    pincode=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control mb-3"}))
    phone=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control mb-3"}))
    email=forms.CharField(widget=forms.EmailInput(attrs={"class":"form-control mb-3"}))
    recommendation_choice=(
        ("socialmedia","socialmedia"),
        ("friend","friend"),
        ("onsite","onsite"),
    )
    recommendation=forms.ChoiceField(label="how did you hear about us",choices=recommendation_choice,widget=forms.Select(attrs={"class":"form-control form-select mb-3"}))

    other=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control mb-3"}))

    feedback=forms.CharField(widget=forms.Textarea(attrs={"class":"form-control mb-3","rows":5}))

    suggestions=forms.CharField(widget=forms.Textarea(attrs={"class":"form-control mb-3","rows":5}))
    
    rec_choices=(
        ("yes","yes"),
        ("no","no"),
        ("maybe","maybe"),
    )

    recommendation_option=forms.ChoiceField(choices=rec_choices,widget=forms.RadioSelect)





