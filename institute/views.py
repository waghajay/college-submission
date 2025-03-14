from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.contrib.auth.decorators import login_required
from accounts.models import Department

# Create your views here.


@login_required(login_url="institute-login")
def instituteDashboard(request):
    departments = Department.objects.all()
    return render(request,'institute/dashboard.html',{"departments" : departments})


