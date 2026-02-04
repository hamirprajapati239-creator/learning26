from django.db import models

class Student(models.Model):
    StudentName= models.CharField(max_length=100)
    studentAge=models.IntegerField()
    studentcity=models.CharField(max_length=40)
    studentEmail=models.EmailField(null=True)

    class Meta:
        db_table = "student"

class product(models.Model):
    productName=models.CharField(max_length=100)
    productPrice=models.IntegerField()
    productDescription=models.TextField()
    productstock=models.PositiveBigIntegerField()
    productColor = models.CharField(max_length=20,null=True)
    productStatus = models.BooleanField(default=True)
    
    
    class Meta:
        db_table = "product"

class fooditem(models.Model):
    foodName = models.CharField(max_length=100)
    foodPrice = models.IntegerField()
    foodDescription = models.TextField()
    foodStock = models.PositiveBigIntegerField()
    foodCategory = models.CharField(max_length=20, null=True)
    foodStatus = models.BooleanField(default=True)

    class Meta:
        db_table = "fooditem"
