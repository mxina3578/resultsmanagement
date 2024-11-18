from django.contrib import admin
from .models import User, Student, Marks

from main.models import User


# admin.site.register(User)


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'student_id')


@admin.register(Marks)
class MarksAdmin(admin.ModelAdmin):
    list_display = ('student', 'subject_math', 'subject_english', 'subject_kiswahili', 'total_marks')
    readonly_fields = ('total_marks',)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass
