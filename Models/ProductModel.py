class ProductModel:

    def __init__(self):
        self.product_db = dict()

    def add_product(self, product_name, product_type, available_quantity, unit_price):
        self.product_db[product_name] = {"product_name": product_name, 
                                         "product_type": product_type, 
                                         "available_quantity": available_quantity, 
                                         "unit_price": unit_price
                                        }
        return True

    def search_product(self, product_name):
        # Search the passed product_name in the dictionary and return the value
        if product_name in self.product_db:
            return self.product_db.get(product_name)
        else:
            return None
    def all_products(self):
        # return all the products available in the dictionary
        return self.product_db