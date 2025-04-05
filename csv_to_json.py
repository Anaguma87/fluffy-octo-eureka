import csv
import json

def csv_to_json(csv_file_path, json_file_path):
    data = []
    with open(csv_file_path, encoding='utf-8') as csvf:
        reader = csv.DictReader(csvf)
        for row in reader:
            data.append(row)

    with open(json_file_path, 'w', encoding='utf-8') as jsonf:
        json.dump(data, jsonf, indent=4)

# Example usage
if __name__ == "__main__":
    csv_to_json('sample_data.csv', 'output.json')
    print("Conversion completed successfully!")
