from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    studentName= models.CharField(max_length=100)
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
    
class studentprofile(models.Model):
    
    hobbies=(("reading","reading"),("travel","travel"),("music","music"))

    studentId=models.OneToOneField(Student,on_delete=models.CASCADE)
    studentHobbies=models.CharField(max_length=100,choices=hobbies)
    studentAddress=models.CharField(max_length=100)
    studentPhone=models.CharField(max_length=10)
    studentGender=models.CharField(max_length=10)
    studentDOB=models.DateField()

    class Meta:
        db_table="studentprofile"
        
    def __str__(self):
        return self.studentId.studentName
    
class Category(models.Model):
    categoryName=models.CharField(max_length=100)
    categoryDescription=models.TextField()

    class Meta:
        db_table="category"
    def __str__(self):
        return self.categoryName
    
class Service(models.Model):
    serviceName = models.CharField(max_length=100)
    serviceDescription = models.TextField()
    servicePrice = models.IntegerField()
    serviceStatus = models.BooleanField(default=True)
    categoryId = models.ForeignKey(Category,on_delete=models.CASCADE,null=True)
    

    class Meta:
        db_table="service"
    def __str__(self):
        return self.serviceName
    
    class UserProfile(models.Model):
        user_name=models.OneToOneField(User,on_delete=models.CASCADE)
        phone=models.CharField(max_length=15)
        address=models.TextField()

        def __str__(self):
            return self.user_name
        class Meta:
            db_table="UserProfile"
        
class ServiceCategory(models.Model):
    category_name=models.CharField(max_length=100)
    description=models.TextField()

    def __str__(self):
        return self.category_name
    class Meta:
            db_table="ServiceCategory"
        
    

    class ServiceProvider(models.Model):
        user_name=models.OneToOneField(User,on_delete=models.CASCADE)
        Category=models.ForeignKey(Service,on_delete=models.CASCADE,related_name='providers')
        experience=models.ImageField()
        availability=models.BooleanField(default=True)
        verified=models.BooleanField(default=False)

        def __str__(self):
            return self.user_name
        class Meta:
            db_table="ServiceProvider"
        

class UserProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    phone=models.CharField(max_length=100)
    address=models.TextField()

    def __str__(self):
        return self.user.username
    class Meta:
        db_table="UserProfile"

class ServiceCategory(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField()

    def __str__(self):
        return self.name
    class Meta:
        db_table="ServiceCategory"
class Department(models.Model):
    departmentName=models.CharField(max_length=50)
    departmentStatus= models.BooleanField(default=True)
    

    class Meta:
        db_table="department"

    def __str__(self):
        return self.departmentName
class Teacher(models.Model):
    teacherName=models.CharField(max_length=100)
    teacherEmail=models.EmailField(unique=True)
    departmentid=models.ForeignKey(
        Department,on_delete=models.CASCADE
    )

    class Meta :
        db_table="teacher"

    def __str__(self):
        return self.teacherName

class Author(models.Model):
    authorName=models.CharField(max_length=100)
    authorEmail=models.EmailField(unique=True)
    authorStatus=models.BooleanField(default=True)

    class Meta:
        db_table="author"
    def __str__(self):
        return self.authorName
class Book(models.Model):
    bookTitle=models.CharField(max_length=150)
    publishYear=models.IntegerField()
    authors=models.ManyToManyField(Author,related_name="books")

    class Meta:
        db_table="book"
    def __str__(self):
        return self.bookTitle