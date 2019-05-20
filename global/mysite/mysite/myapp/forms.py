from django import forms
from .models import *


class globalform(forms.Form):
	name=forms.CharField(max_length=255)
	roll=forms.CharField(max_length=255)
	date=forms.DateField()
	