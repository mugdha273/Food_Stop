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
