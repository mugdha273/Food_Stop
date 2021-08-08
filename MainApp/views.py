from MainApp.employee import Employee
from MainApp.utils import get_grand_total, view_order, view_order_total
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

@csrf_exempt
def view_menu(request):

    result = []
    menu = Customer.view_menu(request)
    for m in menu:
        obj = {
            "category_id": m.category_id.id,
            "category_name": m.category_id.category_name,
            "food_id": m.id,
            "food_name": m.food_name,
            "price": m.price
            }
        result.append(obj)
    return JsonResponse(result, safe=False)

@csrf_exempt
def add_food_details(request):

    json_data = json.loads(request.body)
    
    category_id = json_data['category_id_id']
    food_name = json_data['food_name']
    price = json_data['price']
    food_details = Employee.add_food_details(request, category_id, food_name, price)
    response = {
        "category_id": food_details.category_id_id,
        "food_id": food_details.id,
        "food_name": food_details.food_name,
        "food_price": food_details.price
        }
    return JsonResponse(response)

@csrf_exempt
def view_food_details(request):

    food_details = Employee.view_food_details(request)
    result = []
    for i in food_details:
        obj = {
            "category_id": i.category_id_id,
            "food_id": i.id,
            "food_name": i.food_name,
            "food_price": i.price
            }
        result.append(obj)
    return JsonResponse(result, safe=False)

@csrf_exempt
def add_food_category(request):
   
    json_data = json.loads(request.body)
    food_category = Employee.add_food_category(request, json_data['category_name'])
    response = {
        "category_id": food_category.id,
        "category_name": food_category.category_name
        }
    return JsonResponse(response)


@csrf_exempt
def view_food_category(request):

    categories = Employee.view_categories(request)
    result = []
    for i in categories:
        obj = {
            "category_id": i.id,
            "category_name": i.category_name,
            }
        result.append(obj)
    return JsonResponse(result, safe=False)

@csrf_exempt
def place_order(request, cust_id):

    json_data = json.loads(request.body)
    order = Customer.place_order(request, json_data['cust_id'])
    response = {
        "order_id": order.id,
        "cust_id": order.cust_id_id
        }
    return JsonResponse(response)

@csrf_exempt
def add_food_to_order(request, cust_id):

    json_data = json.loads(request.body)
    order_id = json_data["order_id"]
    food_id = json_data["food_id"]
    food_qty = json_data["food_qty"]
    add_food = Customer.add_food_to_order(request, order_id, food_id, food_qty)
    response = {
        "order_id": add_food.order_id_id,
        "food_id": add_food.food_id_id,
        "food_quantity": add_food.food_qty
        }
    return JsonResponse(response)


@csrf_exempt
def remove_food_from_order(request, cust_id):

    json_data = json.loads(request.body)
    order_id = json_data["order_id"]
    food_id = json_data["food_id"]
    Customer.remove_food_from_order(request, order_id, food_id)
    response = {
        "order_id": order_id,
        "food_id": food_id
        }
    return JsonResponse(response)

@csrf_exempt
def checkout(request, cust_id):

    json_data = json.loads(request.body)
    order_id = json_data["order_id"]
    order_status = "Checked out"
    order_address = json_data["order_address"]
    bill_amount = get_grand_total(order_id)
    Customer.checkout(request, order_id, order_status, 
        order_address, bill_amount)
    response = {
        "order_id": order_id,
        "order_status": order_status,
        "order_address": order_address,
        "bill_amount": bill_amount
        }
    return JsonResponse(response)


@csrf_exempt
def cancel_order(request, cust_id):

    json_data = json.loads(request.body)
    order_id = json_data["order_id"]
    order_status = "Cancelled"
    Customer.cancel_order(request, order_id, order_status)
    response = {
        "order_id": order_id,
        "order_status": order_status
        }
    return JsonResponse(response)

@csrf_exempt
def view_order_by_id(request, cust_id):

    json_data = json.loads(request.body)
    order_id = json_data["order_id"]
    view_order_item = view_order(order_id)
    result = []
    for i in view_order_item:
        obj = {
            "food_category": i.food_id.category_id.category_name,
            "food_name": i.food_id.food_name,
            "food_price": i.food_id.price,
            "food_quantity": i.food_qty,
            "total_per_item": (i.food_id.price*i.food_qty)
            }
        result.append(obj)
    return JsonResponse(result, safe=False)

@csrf_exempt
def view_order_total_by_id(request, cust_id):

    json_data = json.loads(request.body)
    order_id = json_data["order_id"]
    view_order = view_order_total(order_id)
    for i in view_order:
        obj = {
            "cust_email": i.cust_id.cust_email,
            "order_id": i.id,
            "grand_total": i.bill_amount
            }
    return JsonResponse(obj)