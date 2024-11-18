from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('student', 'Student'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    student_id = models.CharField(max_length=20, unique=True)
    full_name = models.CharField(max_length=100)

    def __str__(self):
        return self.full_name

class Marks(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject_math = models.PositiveIntegerField()
    subject_english = models.PositiveIntegerField()
    subject_kiswahili = models.PositiveIntegerField()
    total_marks = models.PositiveIntegerField(blank=True, null=True)
    remarks = models.TextField()

    def save(self, *args, **kwargs):
        self.total_marks = self.subject_math + self.subject_english + self.subject_kiswahili
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Marks for {self.student.full_name}"
