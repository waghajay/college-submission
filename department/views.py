from django.shortcuts import render,render
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url="department-login")
def departmentDashboard(request):
    return render(request, 'department/dashboard.html')
