from django.urls import path
from institute.views import instituteDashboard

urlpatterns = [
    path('',instituteDashboard,name="institute-dashboard")
]
