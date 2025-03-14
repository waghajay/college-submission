from django.urls import path
from department.views import *

urlpatterns = [
    path('',departmentDashboard,name="department-dashboard"),
    path('add-year/',addYear,name="add-year"),
    path('approve-faculty/<int:faculty_id>/',approveFaculty,name="approve-faculty"),
    path('year-details/<int:year_id>/',yearDetails,name="year-details"),
    path('add-division/',addDivision,name="add-division"),
    path('division-details/<int:division_id>/',divisionDetails,name='division-details')
]
