from django.shortcuts import render,redirect
from django.http import JsonResponse,HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from accounts.models import *
from department.models import *
from django.contrib import messages

# Create your views here.

@login_required(login_url="department-login")
def departmentDashboard(request):
    user = User.objects.get(username=request.user)

    departments = Department.objects.filter(user=user)

    faculties = Faculty.objects.filter(department__in=departments, is_approved=False)
    years = Year.objects.filter(department__in=departments)

    return render(
        request,
        'department/dashboard.html',
        {'departments': departments, 'faculties': faculties,'years':years}
    )


@login_required(login_url="department-login")
def addYear(request):
    if request.method == 'POST':
        user = User.objects.get(username=request.user)
        department = Department.objects.get(user=user)
        year_name = request.POST.get('year')
        
        existing_year = Year.objects.filter(department=department, year_name=year_name).first()
        if existing_year:
            messages.error(request, "Year already exists!")
            return redirect('department-dashboard')

        new_year = Year.objects.create(department=department, year_name=year_name)
        new_year.save()
        messages.success(request, "Year added successfully!")
        return redirect('department-dashboard')

    return JsonResponse({'status': 'error', 'message': 'Invalid request method!'})


@login_required(login_url="department-login")
def approveFaculty(request, faculty_id):
    faculty = Faculty.objects.get(id=faculty_id)
    faculty.is_approved = True
    faculty.save()
    messages.success(request, "Faculty approved successfully!")
    return redirect('department-dashboard')


@login_required(login_url="department-login")
def yearDetails(request, year_id):
    
    user = User.objects.get(username=request.user)
    department = Department.objects.get(user=user)
    faculties = Faculty.objects.filter(department=department, is_approved=True)
    year = Year.objects.get(id=year_id)
    divisions = Division.objects.filter(year=year) 
    
    return render(request,'department/year_details.html',{'year': year, 'faculties': faculties,'department_name':department.department_name,'divisions':divisions}
    )
    
@login_required(login_url="department-login")
def addDivision(request):
    if request.method == "POST":
        division_name = request.POST.get('division_name')
        faculty = request.POST.get('faculty')
        year = request.POST.get('year')
        
        try:
            user = User.objects.get(username=request.user)
            department = Department.objects.get(user=user)
            year_obj = Year.objects.get(id=year)
            faculty_obj = Faculty.objects.get(id=faculty)
            
            if Division.objects.filter(department=department, year=year_obj, division_name=division_name).exists():
                messages.error(request, "Division already exists for this year!")
                return redirect(f'/department/year-details/{year}')
            
            division = Division.objects.create(
                department=department,
                year=year_obj,
                faculty=faculty_obj,
                division_name=division_name
            )
            division.save()
            messages.success(request, "Division added successfully!..")
            return redirect(f'/department/year-details/{year}')

        except Exception as e:
            messages.error(request, f"Error: {e}")
            return redirect(f'/department/year-details/{year}')
    
    return JsonResponse({'status': 'error', 'message': 'Invalid request method!'})



def divisionDetails(request,division_id):
    
    user = User.objects.get(username=request.user)
    division = Division.objects.get(id=division_id)

    return render(request,'department/division_details.html',{'division': division})
    
        