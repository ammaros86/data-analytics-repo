# Apache Beam CSV Order Filter Example

This project demonstrates a simple Apache Beam pipeline that:

- Reads orders from a CSV file
- Parses the CSV lines into Python dictionaries
- Filters orders where the amount is greater than 4000
- Formats and writes the filtered orders back to a CSV file