from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.contrib.auth.models import User
from accounts.models import Profile,Department,Faculty,Student
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

# Create your views here.

def institudeRegister(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        
        if User.objects.filter(email=email).exists():
           messages.error(request, "Email address does not exist.")
           return redirect('institute-register')
        else:
            user = User.objects.create_user(username=email,email=email,password=password)
            profile = Profile.objects.create(user=user,role='institute')
            profile.save()
            user.save()
            return redirect('institute-login')
        
    return render(request, 'accounts/institute/register.html')


def instituteLogin(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        user = User.objects.filter(email=email).first()
        if user is None:
            messages.error(request, "Email address does not exist.")
            return redirect('institute-login')
        
        user = authenticate(username=email, password=password)
        
        if user is None:
            messages.error(request, "Incorrect password.")
            return redirect('institute-login')
        
        check_institute = Profile.objects.filter(user=user).first()
        if check_institute.role != 'institute':
            messages.error(request, "You are not an institute.")
            return redirect('institute-login')
        
        login(request, user)
        return redirect('institute-dashboard')
        
    return render(request, 'accounts/institute/login.html')



def registerDepartment(request):
    if request.method == "POST":
        department_name = request.POST.get('department-name')
        department_email = request.POST.get('department-email')
        department_password = request.POST.get('department-password')

        # Check if department already exists
        check_department = Department.objects.filter(department_email=department_email).first()
        if check_department is not None:
            messages.error(request, "Department Email already exists")
            return redirect('department-register')

        # Create User, Department, and Profile
        user = User.objects.create_user(username=department_email, email=department_email, password=department_password)
        Department.objects.create(user=user, department_name=department_name, department_email=department_email)
        Profile.objects.create(user=user, role="department")

        messages.success(request, "Department registered successfully!")
        return redirect('institute-dashboard')

    return redirect('department-register')


def loginDepartment(request):
    if request.method == "POST":
        department_email = request.POST.get('department-email')
        department_password = request.POST.get('department-password')

        user = authenticate(username=department_email, password=department_password)

        if user is None:
            messages.error(request, "Invalid email or password.")
            return redirect('department-login')

        profile = Profile.objects.filter(user=user).first()
        if profile is None or profile.role != 'department':
            messages.error(request, "You are not a department.")
            return redirect('department-login')

        login(request, user)
        messages.success(request, "Welcome to the department dashboard!")
        return redirect('department-dashboard')

    return render(request, 'accounts/department/login.html')


def facultyRegister(request):
    if request.method == "POST":
        faculty_name = request.POST.get('faculty_name')
        faculty_email = request.POST.get('faculty_email')
        department = request.POST.get('department')
        password = request.POST.get('password')

        check_faculty = Faculty.objects.filter(faculty_email=faculty_email).first()
        if check_faculty is not None:
            messages.error(request, "Faculty Email already exists")
            return redirect('faculty-register')

        user = User.objects.create_user(username=faculty_email, email=faculty_email, password=password)
        Profile.objects.create(user=user, role="faculty")

        try:
            department_obj = Department.objects.get(id=department)
        except Department.DoesNotExist:
            messages.error(request, "Selected department does not exist!")
            return redirect('faculty-register')

        Faculty.objects.create(
            user=user,
            department=department_obj,
            faculty_name=faculty_name,
            faculty_email=faculty_email
        )

        messages.success(request, "Faculty registered successfully!")
        return redirect('faculty-login')

    departments = Department.objects.all()
    return render(request, "accounts/faculty/register.html", {'departments': departments})



def loginFaculty(request):
    if request.method == "POST":
        faculty_email = request.POST.get('faculty-email')
        faculty_password = request.POST.get('faculty-password')

        user = authenticate(username=faculty_email, password=faculty_password)

        if user is None:
            messages.error(request, "Invalid email or password.")
            return redirect('faculty-login')

        profile = Profile.objects.filter(user=user).first()
        if profile is None or profile.role != 'faculty':
            messages.error(request, "You are not a Faculty.")
            return redirect('faculty-login')

        faculty = Faculty.objects.filter(user=user).first()
        if faculty and not faculty.is_approved:
            messages.error(request, "The higher authority has not approved you yet...")
            return redirect('faculty-login')

        login(request, user)
        messages.success(request, "Welcome to the Faculty dashboard!")
        return redirect('faculty-dashboard')

    return render(request, 'accounts/faculty/login.html')




def studentRegister(request):
    if request.method == "POST":
        student_name = request.POST.get('student_name')
        student_email = request.POST.get('student_email')
        department = request.POST.get('department')
        password = request.POST.get('password')

        check_student = Student.objects.filter(student_email=student_email).first()
        if check_student is not None:
            messages.error(request, "Student Email already exists")
            return redirect('student-register')

        user = User.objects.create_user(username=student_email, email=student_email, password=password)
        Profile.objects.create(user=user, role="student")

        try:
            department_obj = Department.objects.get(id=department)
        except Department.DoesNotExist:
            messages.error(request, "Selected department does not exist!")
            return redirect('student-register')

        Student.objects.create(
            user=user,
            department=department_obj,
            student_name=student_name,
            student_email=student_email
        )

        messages.success(request, "Student registered successfully!")
        return redirect('student-login')

    departments = Department.objects.all()
    return render(request, "accounts/student/register.html", {'departments': departments})    
        
        
def loginStudent(request):
    if request.method == "POST":
        student_email = request.POST.get('student-email')
        student_password = request.POST.get('student-password')

        user = authenticate(username=student_email, password=student_password)

        if user is None:
            messages.error(request, "Invalid email or password.")
            return redirect('student-login')

        profile = Profile.objects.filter(user=user).first()
        if profile is None or profile.role != 'student':
            messages.error(request, "You are not a Student.")
            return redirect('student-login')
        
        
        student = Student.objects.filter(user=user).first()
        if student and not student.is_approved:
            messages.error(request, "The higher authority has not approved you yet...")
            return redirect('student-login')
        
        
        login(request, user)
        messages.success(request, "Welcome to the Student dashboard!")
        return redirect('student-dashboard')

    return render(request, 'accounts/student/login.html')
        
        
        