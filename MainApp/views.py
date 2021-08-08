import json

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, response
from django.views.decorators.csrf import csrf_exempt


def index(request):
    return HttpResponse("Hello, Welcome to the FoodStop!")
