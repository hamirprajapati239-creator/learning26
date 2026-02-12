from. import views
from django.urls import path
urlpatterns = [
        path('employeelist/',views.employeelist,name="employeelist"),
        path('employeeFilter/',views.employeeFilter),
         path('createemployee/',views.createEmployee),
        path('createEmployeeWithForm/',views.createEmployeeWithForm,name="createEmployeeWithForm"),
        path('createCourse/',views.createCourse),
        path("deleteEmployee/<int:id>",views.deleteEmployee,name="deleteEmployee"),
        path("filterEmployee/",views.filterEmployee,name="filterEmployee"),
        path("sortemployees/<int:id>",views.sortemployees,name="sortemployees")
]


