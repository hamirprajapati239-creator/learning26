from django.shortcuts import render,HttpResponse
from .models import Employee
from.forms import EmployeeForm,CourseForm
from django.shortcuts import redirect


def employeelist(request):

    employee= Employee.objects.all().values()
    
    print(employee)
    return render(request,'employee/employeelist.html',{'employee':employee})

def employeeFilter(request):
     #where select  from employee where name = "raj"
    employee=Employee.objects.filter(name='raj').values()
     #selet  from employee where post = "Developer"
    employee2= Employee.objects.filter(post='Developer').values()
    #select  from employee where name = "raj" and post = "Developer"
    employee3 =Employee.objects.filter(name="raja",post="Developer").values()
     #select  from employee where name = "raj" or post = "Developer"


    employee4 = Employee.objects.filter(age__gt=23).values()
    employee5 = Employee.objects.filter(age__gte=23).values()


    employee6=Employee.objects.filter(post__exact="Developer").values()
    employee7=Employee.objects.filter(post__iexact="developer").values()

    employee8= Employee.objects.filter(name__contains="r").values()
    employee9= Employee.objects.filter(name__icontains="R").values()

    employee10=Employee.objects.filter(name__startswith="R").values()
    employee11= Employee.objects.filter(name__endswith="R").values()
    employee12=Employee.objects.filter(name__istartswith="R").values()
    employee13=Employee.objects.filter(name__iendswith="R").values()


    employee14= Employee.objects.filter(name__in=["raj","jay"]).values()
    employee15= Employee.objects.filter(age__range=[24,30]).values()

    employee16= Employee.objects.order_by('age').values()
    employee17=Employee.objects.order_by("-age").values()

    employee18 = Employee.objects.order_by("-salary").values() 

    print("query 1",employee)
    print("query 2",employee2)
    print("query 3",employee3)
    print("query 4",employee4)
    print("query 5",employee5)
    print("query 6",employee6)   
    print("query 7",employee7) 
    print("query 8",employee8) 
    print("query 9",employee9) 
    print("query 10",employee10) 
    print("query 11",employee11) 
    print("query 12",employee12) 
    print("query 13",employee13) 
    print("query 14",employee14) 
    print("query 15",employee15) 
    print("query 16",employee16) 
    print("query 17",employee17)
    print("query18",employee18)
    return render(request, 'employee/employeeFilter.html')
    
def createEmployee(request):
    Employee.objects.create(name="ajay",age=23,salary=2300,post="HR",join_date="2022-01-01")
    return HttpResponse("Employee Created")

def createEmployeeWithForm(request):
    print(request.method)
    if request.method =="POST":
        form = EmployeeForm(request.POST)
        form.save()
        return redirect("employeelist")
    else:
        form=EmployeeForm()
        return render(request,"employee/createEmployeeWithForm.html",{"form":form})

def createCourse(request):
    if request.method == "POST":
        form=CourseForm(request.POST)
        form.save()
        return HttpResponse("Course creted..")
    else :
        form=CourseForm()
        return render(request,"employee/createCourse.html",{"form":form})

def deleteEmployee(request,id):

    print("id from url =",id)
    Employee.objects.filter(id=id).delete()

    return redirect("employeelist")

def filterEmployee(request):
    print("filter employee called")
    employee =Employee.objects.filter(age__gte=25).values()
    print("filter employee =",employee)

    return render(request,"employee/employeelist.html",{"employee":employee})

def sortemployees(request,id):
    if id == 1:
        employee = Employee.objects.all().order_by('age').values()
    elif id == 2:
        employee = Employee.objects.all().order_by('-age').values()
    else :
        employee = Employee.objects.all().values()
 
    return render(request,'employee/employeelist.html',{'employee': employee})
    