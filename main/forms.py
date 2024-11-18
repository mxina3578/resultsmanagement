from django import forms
from .models import Student, Marks, User


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['user', 'student_id', 'full_name']

class MarksForm(forms.ModelForm):
    class Meta:
        model = Marks
        fields = ['student', 'subject_math', 'subject_english', 'subject_kiswahili', 'remarks']
        widgets = {
            'remarks': forms.Textarea(attrs={'rows': 3}),
        }



