from django.shortcuts import render,render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from accounts.models import Department,Faculty

# Create your views here.

@login_required(login_url="department-login")
def departmentDashboard(request):
    # Get logged-in user
    user = User.objects.get(username=request.user)

    # Fetch all departments linked to this user
    departments = Department.objects.filter(user=user)

    # ✅ Handle multiple departments with __in lookup
    faculties = Faculty.objects.filter(department__in=departments, is_approved=False)

    # ✅ Pass data to the template
    return render(
        request,
        'department/dashboard.html',
        {'departments': departments, 'faculties': faculties}
    )

