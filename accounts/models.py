from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    role = (
        ('institute','institute'),
        ('department','department'),
        ('faculty', "faculty"),
        ('student', "student"),
    )
    user =models.ForeignKey(User,on_delete=models.CASCADE)
    role = models.CharField(max_length=30,choices=role,null=True,blank=True)
    
    def __str__(self):
        return f'User: {self.user.username} Role: {self.role}'
    
    
class Department(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    department_name = models.CharField(max_length=50)
    department_email = models.EmailField(max_length=254)
    
    def __str__(self):
        return f'Department Name :- {self.department_name} --- HOD Name :- {self.department_email}'
    
    
class Faculty(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    department = models.ForeignKey(Department,on_delete=models.CASCADE)
    faculty_name = models.CharField(max_length=100)
    faculty_email = models.EmailField(max_length=254)
    is_approved = models.BooleanField(default=False)
    
    def __str__(self):
        return f' Faculty name :- {self.faculty_name} --- Department  :- {self.department.department_name} --- Email :- {self.faculty_email}'
    
    
    
class Student(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    department = models.ForeignKey(Department,on_delete=models.CASCADE)
    student_name = models.CharField(max_length=100)
    student_email = models.EmailField(max_length=254)
    is_approved = models.BooleanField(default=False)
    
    def __str__(self):
        return f' Student name :- {self.student_name} --- Department  :- {self.department.department_name} --- Email :- {self.student_email}'
    
    
    
    