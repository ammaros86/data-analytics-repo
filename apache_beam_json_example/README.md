# Apache Beam JSON Order Filter Example

This project demonstrates a simple Apache Beam pipeline that:

- Generates a JSON file with random order data (using `JsonMaker`)
- Reads orders from the generated JSON file
- Parses each order and extracts individual products using `FlatMap`
- Filters the extracted products where the order amount is greater than 4500
- Formats and writes the filtered products back to a JSON file (one JSON object per line)