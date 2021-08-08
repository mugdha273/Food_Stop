from MainApp.models import CustOrderSelection, CustOrderStatus, FoodCategory, FoodDetails


class Employee:

    def add_food_category(self, category_name):

        category = FoodCategory(category_name=category_name)
        category.save()
        return category

    def view_categories(self):

        categories = FoodCategory.objects.all()
        print(categories);
        return categories

    def add_food_details(self, category_id, food_name, price):

        food_details = FoodDetails(
            category_id_id=category_id, 
            food_name=food_name, 
            price=price
            )
        food_details.save()
        return food_details

    def view_food_details(self):

        all_food_details = FoodDetails.objects.all()
        print(all_food_details)
        return all_food_details