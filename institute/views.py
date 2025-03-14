from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.contrib.auth.decorators import login_required
from accounts.models import *

# Create your views here.


@login_required(login_url="institute-login")
def instituteDashboard(request):
    departments = Department.objects.all()
    return render(request,'institute/dashboard.html',{"departments" : departments})



@login_required(login_url="department-login")
def departmentDetails(request,departmen_id):
    
    department = Department.objects.get(id=departmen_id)
    faculties = Faculty.objects.filter(department=department, is_approved=True)
    Students = Student.objects.filter(department=department, is_approved=True)
    
    print(department)
    print(faculties)
    print(Students)
    
    return render(request,'institute/department_details.html',{"department" : department, "faculties" : faculties, "Students" : Students})  