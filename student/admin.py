from django.contrib import admin
from .models import Student,product,fooditem,Category,Service

# Register your models here.
admin.site.register(Student)
admin.site.register(product)
admin.site.register(fooditem)
admin.site.register(Category)
admin.site.register(Service)