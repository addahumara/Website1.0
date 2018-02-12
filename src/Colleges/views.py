from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.from django.core.mail import send_mail
from django.conf import settings
from .models import SignUp

def index(request):
	return HttpResponse("Hello, world. You are at college index")

def home(request):
	return render(request, "home.html", { })

def nits(request):
	return render(request, "nits.html", { })

def iits(request):
	return render(request, "iits.html", { })

def about(request):
	return render(request, "about.html", { })

def contact(request):
	return render(request, "contact.html",{ })