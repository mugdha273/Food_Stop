from MainApp.models import CustOrderSelection, CustOrderStatus, CustomerDetails, FoodDetails


class Customer:  

    def customer_signup(self, cust_email, password):

        signup = CustomerDetails(
            cust_email=cust_email, 
            password=password
            )
        signup.save()
        return signup

    def customer_login(self, cust_id):

        login = CustomerDetails.objects.get(pk=cust_id)
        return login

    def view_menu(self):

        menu = FoodDetails.objects\
            .select_related('category_id').all()
        return menu

    def place_order(self, cust_id): 
        """ Generate order id """

        order_id = CustOrderStatus(cust_id_id=cust_id)
        order_id.save()
        return order_id

    def add_food_to_order(self, order_id, food_id, food_qty): 
        """ Add food items """

        add_food = CustOrderSelection(
            order_id_id=order_id, 
            food_id_id=food_id, 
            food_qty=food_qty
            )
        add_food.save()
        return add_food

    def remove_food_from_order(self, order_id, food_id):
        """ Remove food items """

        remove_food = CustOrderSelection.objects\
            .filter(order_id_id=order_id)\
            .filter(food_id_id=food_id).delete()
        return remove_food

    def checkout(self, order_id, order_status, order_address, bill_amount):
        """ Customer can checkout/confirm order """

        checkout_update = CustOrderStatus.objects\
            .filter(id=order_id)\
            .update(
                order_status=order_status, 
                order_address=order_address, 
                bill_amount=bill_amount
                )
        return checkout_update

    def cancel_order(self, order_id, order_status):
        """ Cancel order """

        update_order = CustOrderStatus.objects\
            .filter(id=order_id)\
            .update(order_status=order_status)
        return update_order
