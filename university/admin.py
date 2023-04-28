from django.contrib import admin

from university.models import Student


# Register your models here.

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    ordering = ["first_name"]
    list_filter = ["first_name", "last_name"]
    list_display = ["first_name", "last_name"]
