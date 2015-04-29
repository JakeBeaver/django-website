from django import forms
from models import posts

class PostingForm(forms.ModelForm):
	class Meta:
		model = posts
		fields = ('body',)
