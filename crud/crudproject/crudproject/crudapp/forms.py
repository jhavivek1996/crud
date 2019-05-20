from django import forms  
from .models import Employee  

class EmployeeForm(forms.Modelform):  
    class Meta:  
        model = Employee  
        fields = "__all__"  