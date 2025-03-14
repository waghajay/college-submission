from django.db import models
from accounts.models import *

# Create your models here.


class Year(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    year_name = models.CharField(max_length=100)
    

    def __str__(self):
        return f'Year :- {self.year_name} --- Department :- {self.department.department_name}'
    
    
class Division(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    year = models.ForeignKey(Year, on_delete=models.CASCADE)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    division_name = models.CharField(max_length=150)
    
    def __str__(self):
        return f'Department :- {self.department.department_name} -- Year :- {self.year.year_name} -- Division Name :- {self.division_name}'
    
class Subject(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    year = models.ForeignKey(Year, on_delete=models.CASCADE)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE,null=True,blank=True)
    subject_id = models.CharField(max_length=50,unique=True)
    subject_name = models.CharField(max_length=50)
    
    def __str__(self):
        return f"Subject Name :- {self.subject_name} -- Year :- {self.year.year_name}"
    
    