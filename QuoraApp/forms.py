from django import forms
from tinymce.widgets import TinyMCE
from .models import *
from django.forms import ModelForm


class TinyMCEWidget(TinyMCE):
    def use_required_attribute(self, *args):
        return False


class PostForm(forms.ModelForm):
    Answer = forms.CharField(
        widget=TinyMCEWidget(
            attrs={'required': False, 'cols': 30, 'rows': 50}
        )
    )

    class Meta:
        model = Answer
        fields = '__all__'
        

class CreateUserForm(ModelForm):
    class Meta:
        model=Member
        fields=('user','name','email')


class ProfileForm(ModelForm):
    class Meta:
        model = Member
        fields = '__all__'
        exclude = ['user']


class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        exclude = ['member']


class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        exclude = ['member']

class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = '__all__'
        widgets = {
            'description': forms.TextInput(attrs={
                            'class': 'question-text-input',
                            'placeholder': "Start your Question with 'Why', 'What', 'How', etc."
            })
        }

