from. import views
from django.urls import path
urlpatterns = [
        path('employeelist/',views.employeelist),
        path('employeeFilter/',views.employeeFilter),
         path('createemployee/',views.createEmployee),
        path('createEmployeeWithForm/',views.createEmployeeWithForm),
        path('createCourse/',views.createCourse)
]

