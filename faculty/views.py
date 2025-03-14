from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url="faculty-login")
def facultDashboard(request):
    return render(request,"faculty/dashboard.html")