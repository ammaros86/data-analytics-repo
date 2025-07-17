import apache_beam as beam
import json
from json_maker import JsonMaker
from typing import Dict, Iterator


def parse_json(line: str) -> Iterator[Dict]:
    order = json.loads(line)
    for product in order["products"]:
        yield{
            "order_id": order["order_id"],
            "customer": order["customer"],
            "amount": order["amount"],
            "date": order["order_date"],
            "product_id": product["product_id"],
            "quantity": product["quantity"],
            "price": product["price"]
        }

def filter_large_orders(order: Dict) -> bool:
    return float(order["amount"]) > 4500

def format_order(order: Dict) -> str:
    return json.dumps(order)

if __name__ == "__main__":
    JsonMaker().make_json_file()
    with beam.Pipeline() as pipeline:(
        pipeline
        | "Read JSON File" >> beam.io.ReadFromText("orders.json")
        | "Parse JSON" >> beam.FlatMap(parse_json)
        | "Filter Order" >> beam.Filter(filter_large_orders)
        | "Write filtered to new JSON File" >> beam.io.WriteToText("filtered_orders", file_name_suffix=".json")
    )