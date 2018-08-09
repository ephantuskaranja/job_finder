from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Jobs, Profile






class addJobForm(forms.ModelForm):
    
    class Meta:
        model = Jobs
        exclude = ['created_at', 'user']
        fields = ('company', 'skill', 'location', 'salary', 'job_type', 'contact', 'description', )