from django.urls import path
from department.views import *

urlpatterns = [
    path('',departmentDashboard,name="department-dashboard"),
]
