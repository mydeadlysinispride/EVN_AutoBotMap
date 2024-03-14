import pandas as pd

class LocationDataProcessor:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_data(self):
        data = pd.read_csv(self.file_path)
        return data

    def process_data(self, data):
        # Add your data processing logic here
        processed_data = []
        for row in data:
            # Process each row of data
            processed_row = []
            for item in row:
                # Process each item in the row
                processed_item = str(item).upper()  # Example: Convert item to uppercase
                processed_row.append(processed_item)
            processed_data.append(processed_row)
        return processed_data

# Usage example
file_path = './location.csv'
processor = LocationDataProcessor(file_path)
data = processor.read_data()
processed_data = processor.process_data(data)
print(processed_data)