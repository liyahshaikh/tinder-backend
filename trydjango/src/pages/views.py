from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def home_view(response, *args, **kwargs):
	return render(response, "home.html", {})
def aboutUs_view(response, *args, **kwargs):
	return render(response, "about-us.html", {})