from django import forms

class CreateNewList(forms.Form):

	company=forms.CharField(label="Company",max_length=250)
	reference=forms.CharField(label="Your name", max_length=250)
	email=forms.CharField(label="Email",max_length=500)
	