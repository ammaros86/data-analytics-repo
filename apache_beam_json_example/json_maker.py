import json
import random
from datetime import datetime, timedelta

class JsonMaker():
    def __init__(self):
        self.companies = ["CompanyA", "CompanyB", "CompanyC", "CompanyD", "CompanyE", "CompanyF", "CompanyG"]
        self.prdoucts_ids = ["Product1", "Product2", "Product3"]

    def make_json_file(self):
        with open("orders.json", "w", newline="") as json_file:
            start_date = datetime(2025, 1, 1)
            for order_id in range (1, 1001):
                customer = random.choice(self.companies)
                amount = random.randint(100, 5000)
                order_date = start_date + timedelta(days=random.randint(0, 30))
 
                products = []
                for _ in range (random.randint(1, 4)):
                    product = {
                        "product_id": random.choice(self.prdoucts_ids),
                        "quantity": random.randint(1, 100),
                        "price": random.randint(5, 5000)
                    }
                    products.append(product)
                order = {
                    "order_id": order_id,
                    "customer": customer,
                    "amount": amount,
                    "order_date": order_date.strftime("%Y-%m-%d"),
                    "products":products
                }
                json_file.write(json.dumps(order)+ "\n")
 