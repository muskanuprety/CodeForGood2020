from django import forms
from .models import requestUser

class userform(forms.ModelForm):
	class Meta:
		model = requestUser
		fields = [

			'fname',
			'lname'
			'email',
			'company'
			'dob'
			]
			