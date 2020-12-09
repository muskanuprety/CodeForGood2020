from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Consumer, Request
from .forms import CreateNewList, CreateNewList2, CreateUserForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

u=None

def base(response):
	return render(response, "website/base.html")

def registerPage(response):
	form = CreateUserForm()
	context= {'form':form}
	if response.method=="POST":
		form = CreateUserForm(response.POST)
		if form.is_valid():
			form.save()
	return render(response,"website/register.html", context)


def LoginView(response):
	form = AutenticationForm()
	context= {'form':form}
	if response.method=="POST":
		form = AutenticationForm(data=response.POST)
		
	return render(response,"website/login.html", context)




def create(response):
	#from website.models import Request

	if response.method=="POST":
		form = CreateNewList(response.POST)

		if form.is_valid():
			c=form.cleaned_data["company"]
			n=form.cleaned_data["reference"]
			e=form.cleaned_data["email"]
			u=Consumer(company=c, reference=n, email=e)
			u.save()
		return HttpResponseRedirect("/create2")

	else:
		form = CreateNewList()

	return render(response,"website/create.html", {"form":form})

def create2(response):
	if response.method=="POST":
		form=CreateNewList2(response.POST)

		if form.is_valid():
			num=form.cleaned_data["number_of_requests"]
			intrests=form.cleaned_data["type_of_programes"]
			request=Request(number_of_requests=num, type_of_programes=intrests)

			request.save()
	else:
		form=CreateNewList2()
			
	return render(response,"website/create2.html", {"form":form})
