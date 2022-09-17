from django.contrib import admin

# from hostel_app.issues.models import all_issues, student_data

from . import models
# Register your models here.
admin.site.register(models.student_data)
admin.site.register(models.all_issues)