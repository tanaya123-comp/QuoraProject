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
