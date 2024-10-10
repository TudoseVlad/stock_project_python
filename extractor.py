
import os
import random
import sys
from csvoperations.csvoperations import read_csv,write_csv
from common.common import OUTPUT_FILE,print_data
from datetime import datetime
def randomize(data):
    if len(data) < 10:
        return data

    data.sort(key=lambda x: (x.timestamp, x.price, x.name))
    random.seed(datetime.now().timestamp())
    starting_pos = random.randint(0, len(data) - 10)
    return data[starting_pos:starting_pos+10]

def main():
    all_data = []
    if len(sys.argv) < 2:
        raise Exception("No files provided")

    for file in sys.argv[1:]:
        rez, err = read_csv(file)
        if err:
            raise Exception(f"Error encountered: {err}")
        all_data.extend(rez)

    sol = randomize(all_data)
    err = write_csv(OUTPUT_FILE, sol)
    if err:
        raise Exception(f"Error writing CSV: {err}")
    
    print_data(sol)

if __name__ == "__main__":
    main()