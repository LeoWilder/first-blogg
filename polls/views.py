from django.shortcuts import render
from django.http import HttpResponse


def index(renderuest):
	return HttpResponse("Hello, world. You're at the polls index.")
# Create your views here.
