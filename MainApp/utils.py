from MainApp.models import CustOrderSelection, CustOrderStatus

def get_grand_total(order_id):

    grand_total = CustOrderSelection.objects\
        .select_related('food_id')\
        .filter(order_id_id=order_id)
    price_per_food = []
    for i in grand_total:
        d = {
            "quantity": i.food_qty,
            "price": i.food_id.price
            }
        price_per_food.append(d["quantity"]*d["price"])
    bill_amount = sum(price_per_food)
    return bill_amount


def view_order(order_id):

    view = CustOrderSelection.objects\
        .select_related('food_id__category_id')\
        .filter(order_id_id=order_id)
    return view


def view_order_total(order_id):
    """ Employee/Customer can view the grand total of an order """

    view = CustOrderStatus.objects\
        .select_related('cust_id')\
        .filter(id=order_id)
    return view