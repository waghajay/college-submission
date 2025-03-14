from django.contrib import admin
from accounts.models import Profile,Department,Faculty,Student

# Register your models here.


admin.site.register(Profile)
admin.site.register(Department)
admin.site.register(Faculty)
admin.site.register(Student)