# CSV to JSON Converter

A simple Python utility that converts CSV files into clean, formatted JSON.

## Description

This tool takes a CSV file (such as product data, contacts, or any tabular data) and converts it into a properly formatted JSON file. The script preserves the column headers as keys in the resulting JSON objects and maintains the data structure.

## Features

- Handles UTF-8 encoded CSV files
- Preserves column headers as JSON keys
- Produces nicely formatted JSON with proper indentation
- Simple to use with minimal dependencies (only standard Python libraries)

## Requirements

- Python 3.x

## Usage

1. Clone this repository or download the `csv_to_json.py` file
2. Place your CSV file in the same directory or provide the full path
3. Run the script with your CSV file as input:

```bash
python csv_to_json.py
```

Or modify the script to use your own file paths:

```python
csv_to_json('your_data.csv', 'your_output.json')
```

## Example

### Sample Input (CSV)

```csv
id,name,category,price,in_stock,description
1,Laptop XPS 13,Electronics,1299.99,true,"13-inch ultrabook with Intel Core i7, 16GB RAM, 512GB SSD"
2,Wireless Headphones,Electronics,199.99,true,"Noise-cancelling wireless headphones with 30-hour battery life"
3,Coffee Maker,Home Appliances,89.95,true,"Programmable coffee maker with 12-cup capacity"
4,Running Shoes,Footwear,129.50,false,"Lightweight running shoes with responsive cushioning"
5,Protein Powder,Nutrition,39.99,true,"Whey protein isolate, 2lb container, vanilla flavor"
```

### Sample Output (JSON)

```json
[
    {
        "id": "1",
        "name": "Laptop XPS 13",
        "category": "Electronics",
        "price": "1299.99",
        "in_stock": "true",
        "description": "13-inch ultrabook with Intel Core i7, 16GB RAM, 512GB SSD"
    },
    {
        "id": "2",
        "name": "Wireless Headphones",
        "category": "Electronics",
        "price": "199.99",
        "in_stock": "true",
        "description": "Noise-cancelling wireless headphones with 30-hour battery life"
    },
    {
        "id": "3",
        "name": "Coffee Maker",
        "category": "Home Appliances",
        "price": "89.95",
        "in_stock": "true",
        "description": "Programmable coffee maker with 12-cup capacity"
    },
    {
        "id": "4",
        "name": "Running Shoes",
        "category": "Footwear",
        "price": "129.50",
        "in_stock": "false",
        "description": "Lightweight running shoes with responsive cushioning"
    },
    {
        "id": "5",
        "name": "Protein Powder",
        "category": "Nutrition",
        "price": "39.99",
        "in_stock": "true",
        "description": "Whey protein isolate, 2lb container, vanilla flavor"
    }
]
```

## Customization

You can easily modify the script to:
- Handle different CSV formats
- Apply data transformations during conversion
- Change the output formatting
- Process multiple files in batch

## License

This project is open source and available under the MIT License.

## Contributing

Contributions, issues, and feature requests are welcome!

## Author

Your Name - [Your GitHub Profile](https://github.com/yourusername)
