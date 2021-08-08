from MainApp.customer import Customer
import json

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, response
from django.views.decorators.csrf import csrf_exempt


def index(request):
    return HttpResponse("Hello, Welcome to the FoodStop!")


@csrf_exempt
def customer_signup(request):
    
    json_data = json.loads(request.body)
    customer_details = Customer.customer_signup(request, json_data['cust_email'], json_data['password'])
    response = {
        "cust_id": customer_details.id,
        "cust_email": customer_details.cust_email,
        "password": customer_details.password
        }
    return JsonResponse(response)


@csrf_exempt
def customer_login(request, cust_id):

    customer = Customer.customer_login(request, cust_id)
    response = {
        "cust_id": customer.id,
        "cust_email": customer.cust_email
    }
    return JsonResponse(response, safe=False)