from django.shortcuts import render
from django.http import HttpResponse

from .forms import CreateNewList

def base(response):
	return render(response, "website/base.html")

def create(response):
	form = CreateNewList()
	return render(response,"website/create.html", {"form":form})
