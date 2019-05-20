from django import forms
from .models import *

class gameform(forms.ModelForm):
	class Meta:
		model= game
		fields = "__all__"