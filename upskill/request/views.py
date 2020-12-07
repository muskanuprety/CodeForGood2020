from django.shortcuts import render
from django.http import HttpResponse
from .forms import userform
# Create your views here.

def home(request, *args, **kwargs):

	form = userform(request.POST or None)
	if form.is_valid():
		form.save()
		form = userform()


	context = {
		'form': form
	}

	return render(request, 'home.html',context)




def requestQuote(request, *args, **kwargs):

	return render (request, 'quote.html', {})

def login(request, *args, **kwargs):
	return render( request, 'login.html', {})
	