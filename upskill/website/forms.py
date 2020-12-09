from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CreateUserForm(UserCreationForm):
	class Meta:
		model=User
		fields=['username','first_name','last_name','email','password1', 'password2']


class CreateNewList(forms.Form):

	company=forms.CharField(label="Company",max_length=250)
	reference=forms.CharField(label="Your name", max_length=250)
	email=forms.CharField(label="Email",max_length=500)
	
class CreateNewList2(forms.Form):

	number_of_requests=forms.IntegerField(label="Number of people you are lookig to train:")
	type_of_programes=forms.CharField(label="Types of courses you are interested in",max_length=100)