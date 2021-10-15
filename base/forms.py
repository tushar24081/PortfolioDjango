from django import forms
from django.forms import ModelForm
from .models import *


class CreatePost(ModelForm):
	class Meta:
		model = Post
		fields = '__all__'
		widgets = {
		'tags': forms.CheckboxSelectMultiple(),
		}

class CommentForm(ModelForm):
	body = forms.CharField(label='', 
                            widget=forms.TextInput(attrs={'placeholder': 'Add a comment...'}))
	user = forms.CharField(label='', 
                            widget=forms.TextInput(attrs={'placeholder': 'Enter Display Name:'}))
	class Meta:	
		model = Comment
		fields = ('body', 'user' )