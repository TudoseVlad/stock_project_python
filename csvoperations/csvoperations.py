import csv
import os
from datetime import datetime
from typing import List, Tuple
from common.common import Info,TIME_LAYOUT

def read_csv(file_path: str) -> Tuple[List[Info], Exception]:
    sol = []
    try:
        with open(file_path, mode='r') as file:
            reader = csv.reader(file)
            data = list(reader)
    except Exception as e:
        print(f"Error opening or reading file {file_path}\n Error: {e}")
        return [], e

    for line in data:
        if len(line) != 3:
            raise ValueError("Invalid data from csv file")
        
        try:
            pret = float(line[2])
        except ValueError as e:
            print(f"Price invalid: {e}")
            return [], e

        try:
            timp = datetime.strptime(line[1], TIME_LAYOUT)
        except ValueError as e:
            print(f"Timestamp invalid: {e}")
            return [], e

        value = Info(timestamp=timp, name=line[0], price=pret)
        sol.append(value)
    
    return sol, None

def write_csv(file_path: str, data: List[Info]) -> Exception:
    try:
        with open(file_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            for info in data:
                record = [
                    info.name,
                    info.timestamp.strftime(TIME_LAYOUT),
                    f"{info.price:.2f}",
                ]
                writer.writerow(record)
    except Exception as e:
        print(f"Error writing record to CSV: {e}")
        return e
    
    return None