from django.urls import path
from accounts.views import *


urlpatterns = [
    path('institute-register', institudeRegister, name='institute-register'),
    path('institute-login',instituteLogin,name="institute-login"),
    
    path('department-register',registerDepartment,name="department-register"),
    path('department-login',loginDepartment,name="department-login"),
    
    path('faculty-register',facultyRegister,name="faculty-register"),
    path('faculty-login',loginFaculty,name="faculty-login"),
    
    
    path('student-register',studentRegister,name="student-register"),
    path('student-login',loginStudent,name="student-login")
]
