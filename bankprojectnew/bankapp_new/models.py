from django.db import models

# Create your models here.

class District(models.Model):
    name=models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Branch(models.Model):
    district=models.ForeignKey(District,on_delete=models.CASCADE)
    name=models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Account_type(models.Model):
    name= models.CharField(max_length=200)


    def __str__(self):
        return self.name
class Customer(models.Model):
    name=models.CharField(max_length=200)
    dob=models.DateField(null=True,blank=True)
    Gender=models.CharField(max_length=200)
    Phone_no=models.CharField(max_length=200)
    Email_id=models.CharField(max_length=200)
    Address=models.CharField(max_length=200)
    district=models.ForeignKey(District,on_delete=models.SET_NULL,blank=True,null=True)
    branch=models.ForeignKey(Branch,on_delete=models.SET_NULL,blank=True,null=True)
    Account_type=models.ForeignKey(Account_type,on_delete=models.SET_NULL,blank=True,null=True)

    def __str__(self):
        return self.name