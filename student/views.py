from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url="student-login")
def studentDashboard(request):
    return render(request,'student/dashboard.html')