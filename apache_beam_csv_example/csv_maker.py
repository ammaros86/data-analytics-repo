import csv
import random
from datetime import datetime, timedelta

class CsvMaker():
    def __init__(self):
        self.companies = ["CompanyA", "CompanyB", "CompanyC", "CompanyD", "CompanyE", "CompanyF", "CompanyG"]

    def make_csv_file(self):
        with open("orders.csv", "w", newline="") as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(["order_id", "customer", "amount", "date"])
            start_date = datetime(2025, 1, 1)
            for order_id in range (1, 1001):
                customer = random.choice(self.companies)
                amount = random.randint(100, 5000)
                order_date = start_date + timedelta(days=random.randint(0, 30))
                writer.writerow([order_id, customer, amount, order_date.strftime("%Y-%m-%d")])