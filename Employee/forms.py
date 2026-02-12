from django import forms 
from.models import Employee,Course


class EmployeeForm(forms.ModelForm):
    class Meta:
        model=Employee
        fields='_all_'\
        
class CourseForm(forms.Modelform):
    class Meta:
        model = Course
        fields= '_all_'

