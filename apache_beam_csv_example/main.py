
import apache_beam as beam
import json
from csv_maker import CsvMaker
import csv
from io import StringIO
from typing import Dict

def parse_csv(line: str) -> Dict[str, str]:
    reader = csv.DictReader(StringIO(line), fieldnames=["order_id" , "customer" , "amount" , "date"])
    return next(reader)

def format_order(order : str) -> str:
    return f'{order["order_id"]}, {order["customer"]}, {order["amount"]}, {order["date"]}'

def filter_large_orders(order) -> bool:
    return float(order["amount"]) > 4000

if __name__ == "__main__":
    csv_maker = CsvMaker()
    csv_maker.make_csv_file()
    with beam.Pipeline() as pipeline:
        (
            pipeline
            | "Read CSV" >> beam.io.ReadFromText("orders.csv", skip_header_lines=1)
            | "Parse CSV" >> beam.Map(parse_csv)
            | "Filter Order" >> beam.Filter(filter_large_orders)
            | "Format Order for Output" >> beam.Map(format_order)
            | "Write to new CSV" >> beam.io.WriteToText("filtered_orders3", file_name_suffix=".csv", header="order_id, customer, amount, date")
        )