from django.db import models



class Employee(models.Model):

    name=models.CharField(max_length=100)
    age=models.PositiveIntegerField()
    gender=models.CharField(max_length=100)
    department=models.CharField(max_length=200)
    phone=models.CharField(max_length=12)
    salary=models.PositiveIntegerField()
    address=models.TextField()
    qualification=models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.name 





class Movie(models.Model):

    title=models.CharField(max_length=200)
    genre=models.CharField(max_length=200)
    run_time=models.PositiveIntegerField()
    language=models.CharField(max_length=200)
    year=models.PositiveIntegerField()
    director=models.CharField(max_length=200)

    def __str__(self):
        return self.title
    

class Cars(models.Model):

    brand=models.CharField(max_length=20)
    varient=models.CharField(max_length=20)
    
    fuel_options=(
        ("petrol","petrol"),
        ("CNG","CNG"),
        ("EV","EV"),
        ("diesel","diesel"),
    )

    fuel_type=models.CharField(max_length=20,choices=fuel_options,default="petrol")

    transmission_options=(
        ("automatic","automatic"),
        ("manual","manual"),
    )

    transmission_type=models.CharField(max_length=20,choices=transmission_options,default="manual")

    color=models.CharField(max_length=20)
    price=models.PositiveIntegerField()
    mileage=models.IntegerField()

    def __str__(self):
        return self.brand
    
    
    




    
    

