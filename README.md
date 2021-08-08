# foodstop
-Quick Demo of frontend and Backend sides of FoodStop: https://drive.google.com/file/d/1Qw5bbqoMSCPiUQYIE5rLxhRxa2xqxpHS/view?usp=sharing

## Steps to follow:
-Instructions for API in backend part

### Employee operations:
1. Add food category (Add category like Snacks, Desserts etc.)

`curl --location --request POST 'http://127.0.0.1:8000/employees/add-food-category' \
--header 'Content-Type: application/json' \
--data-raw '{
    "category_name": "desserts"
}'`  

2.  Retrieve all the added food categories

`curl --location --request GET 'http://127.0.0.1:8000/employees/get-food-categories'`


3. Add food details (name, price) corresponding to categories added

`curl --location --request POST 'http://127.0.0.1:8000/employees/add-food-details' \
--header 'Content-Type: application/json' \
--data-raw '{
    "category_id_id": 1,
    "food_name": "KitKat Shake",
    "price": 200
}
'`

4. Get Food Details

`curl --location --request GET 'http://127.0.0.1:8000/employees/get-food-details'`


### Customer operations:

1. SignUp to FoodStop

`curl --location --request POST 'http://127.0.0.1:8000/customers/signup' \
--header 'Content-Type: application/json' \
--data-raw '{
    "cust_email": "test@gmail.com",
    "password": "test"
}'`

2. Login to FoodStop

`curl --location --request GET 'http://127.0.0.1:8000/customers/1/login'`

3. View Menu
`curl --location --request GET 'http://127.0.0.1:8000/customers/view-menu'`

4. Create Food Order

`curl --location --request POST 'http://127.0.0.1:8000/customers/1/place-order' \
--header 'Content-Type: application/json' \
--data-raw '{"cust_id":1}'` 

5. Add food to Order

`curl --location --request POST 'http://127.0.0.1:8000/customers/1/add-food-to-order' \
--header 'Content-Type: text/plain' \
--data-raw '{
    "order_id": 1,
    "food_id": 1,
    "food_qty":10
}'`

6. Remove food from order

`curl --location --request DELETE 'http://127.0.0.1:8000/customers/1/remove-food-from-order' \
--header 'Content-Type: application/json' \
--data-raw '{"order_id":1, "food_id":1}'`

7. View Order

`curl --location --request GET 'http://127.0.0.1:8000/employees/1/view-order' \
--header 'Content-Type: application/json' \
--data-raw '{"order_id":1}'`

8. Checkout your Order

`curl --location --request PUT 'http://127.0.0.1:8000/customers/1/checkout' \
--header 'Content-Type: application/json' \
--data-raw '{"order_id":1, "order_address":"IIIT Vadodara"}'`

9. View Total Order 

`curl --location --request GET 'http://127.0.0.1:8000/customers/1/view-order-total' \
--header 'Content-Type: application/json' \
--data-raw '{"order_id":1}'`

10. Cancel order

`curl --location --request PUT 'http://127.0.0.1:8000/customers/1/cancel-order' \
--header 'Content-Type: application/json' \
--data-raw '{"order_id":1}'`
