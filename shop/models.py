from django.db import models

# Create your models here.
class Product(models.Model):
    OPTS_1= (("electronics","ELECTRONICS"),
            ("shoes","SHOES"),
            ("tops","TOPS"), ("trousers","TROUSERS"),
            ("jewellries","JEWELLRIES")
            )
    OPTS_2=  (("men","MEN"),
            ("women","WOMEN"),
            ("all","ALL")
            )       
    name=models.CharField(max_length=100)    
    price=models.IntegerField(max_length=50)    
    description=models.CharField(max_length=200)
    image=models.ImageField(upload_to="shop")
    category1= models.CharField(max_length=100,choices=OPTS_1)
    category2= models.CharField(max_length=100,choices=OPTS_2)

    class UserCheckout(models.Model):
        names=models.CharField(max_length=200)
        phone=models.IntegerField(max_length=200)
        email=models.EmailField(max_length=200)
        address=models.CharField(max_length=200)
        details=models.CharField(max_length=200)
        totalcash=models.IntegerField(max_length=200)
        PAYMENT=  (("cash","CASH"),
            ("transfer","TRANSFER"),
            ("card","CARD")
            )     
        payment=models.CharField(max_length=200,choices=PAYMENT)     





