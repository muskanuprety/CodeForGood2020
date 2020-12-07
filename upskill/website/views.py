from django.shortcuts import render
from django.http import HttpResponse
from .models import Consumer
from .forms import CreateNewList

def base(response):
	return render(response, "website/base.html")

def create(response):

	if response.method=="POST":
		form = CreateNewList(response.POST)

		if form.is_valid():
			c=form.cleaned_data["company"]
			n=form.cleaned_data["reference"]
			e=form.cleaned_data["email"]
			user=Consumer(company=c, reference=n, email=e)
			user.save()

	else:
		form = CreateNewList()

	return render(response,"website/create.html", {"form":form})
