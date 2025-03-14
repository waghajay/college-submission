from django.urls import path
from institute.views import *

urlpatterns = [
    path('',instituteDashboard,name="institute-dashboard"),
    path('department/<int:departmen_id>/',departmentDetails,name="department-details"),
]
