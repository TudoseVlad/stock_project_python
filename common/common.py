import os
from datetime import datetime
from operator import attrgetter

class Info:
    def __init__(self, timestamp, name, price):
        self.timestamp = timestamp
        self.name = name
        self.price = price

# Time format and file location
TIME_LAYOUT = "%d-%m-%Y"
OUTPUT_FILE = "data/output.csv"
LOCATION = os.getcwd()

# Sorter class with sorting methods
class Sorter:
    def __init__(self, infos):
        self.infos = infos

    def __len__(self):
        return len(self.infos)

    def __getitem__(self, index):
        return self.infos[index]

    def sort(self):
        self.infos.sort(key=attrgetter('timestamp', 'price', 'name'))

def print_data(data):
    for val in data:
        print(f"Timestamp: {val.timestamp.strftime('%a, %d %b %Y %H:%M:%S')}, Name: {val.name}, Price: {val.price:.2f}")
