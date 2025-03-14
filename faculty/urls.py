from django.urls import path
from faculty.views import facultDashboard

urlpatterns = [
    path('',facultDashboard,name="faculty-dashboard")
]
