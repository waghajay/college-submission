from django.urls import path
from student.views import studentDashboard


urlpatterns = [
    path('',studentDashboard,name="student-dashboard")
]
