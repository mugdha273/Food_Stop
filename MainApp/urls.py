from django.urls import path

from . import views

urlpatterns = [
    path("", views.index),
    path("employees/add-food-category", views.add_food_category, name="add_food_category"),
    path("employees/get-food-categories", views.view_food_category, name="view_food_category"),
    path("employees/add-food-details", views.add_food_details, name="add_food_details"),
    path("employees/get-food-details", views.view_food_details, name="get_food_details"),
    path("customers/signup", views.customer_signup, name="signup"),
    path("customers/<int:cust_id>/login", views.customer_login, name="login"),
    path("customers/<int:cust_id>/place-order", views.place_order, name="place_order"),
    path("customers/<int:cust_id>/add-food-to-order", views.add_food_to_order, name="add_food"),
    path("customers/<int:cust_id>/remove-food-from-order", views.remove_food_from_order, name="remove_food"),
    path("customers/<int:cust_id>/checkout", views.checkout, name="checkout"),
    path("customers/<int:cust_id>/cancel-order", views.cancel_order, name="cancel_order"),
    path("employees/<int:cust_id>/view-order", views.view_order_by_id, name="view_order"),
    path("customers/view-menu", views.view_menu, name="menu"),
    path("customers/<int:cust_id>/view-order", views.view_order_by_id, name="view_order"),
    path("customers/<int:cust_id>/view-order-total", views.view_order_total_by_id, name="view_order_total")
]