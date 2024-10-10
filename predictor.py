from csvoperations.csvoperations import read_csv
from common.common import print_data,Info,OUTPUT_FILE
from datetime import timedelta

def find_max(data):
    sol = 0
    max_price = data[0].price
    for i in range(1, len(data)):
        if max_price < data[i].price:
            max_price = data[i].price
            sol = i
    return sol

def find_2nd_max(data):
    index = find_max(data)
    max_price = data[0].price * -1  
    name = ""
    for val in data:
        if max_price < val.price and val.price != data[index].price:
            name = val.name
            max_price = val.price
    return name, max_price

def simple_predict(data):
    timestamp = data[-1].timestamp
    nprice = data[-1].price
    name, n1price = find_2nd_max(data)

    n2price = n1price + (nprice - n1price) / 2
    n3price = n2price + (n1price - n2price) / 4
    
    sol = [
        Info(timestamp + timedelta(days=1), name, n1price),
        Info(timestamp + timedelta(days=2), name, n2price),
        Info(timestamp + timedelta(days=3), name, n3price),
    ]
    return sol

def main():
    try:
        sol, err = read_csv(OUTPUT_FILE)
        if err:
            raise Exception(err)
        predicted = simple_predict(sol)
        sol.extend(predicted)

        print_data(sol)
    
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
