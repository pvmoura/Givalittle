from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render_to_response
from django.contrib import auth
from givalittle.giftsdb import models
from django.core.context_processors import csrf
import datetime

def give(request):
	return render_to_response("give.html")

def home(request):
	return HttpResponse("thanks for registering!")

def test(request):
	return render_to_response("main.html")

def get(request):
	return render_to_response("get.html")
