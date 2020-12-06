from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request, *args, **kwargs):

	return render(request, 'home.html',{})

def requestQuote(request, *args, **kwargs):

	return render (request, 'quote.html', {})
	