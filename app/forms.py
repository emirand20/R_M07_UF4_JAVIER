from django.forms import ModelForm
from .models import Teacher
from .models import Student


class TeacherForm(ModelForm):
    class Meta: 
        model = Teacher
        # field = ['id',]
        fields = '__all__'
        
class StudentForm(ModelForm):
    class Meta:
        model = Student
        # field = ['id',]
        fields = '__all__'