from django.forms import ModelForm

from university.models import Student


class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ["first_name", "last_name"]
