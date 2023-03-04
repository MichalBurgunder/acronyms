import random
import math
import os
import csv

def save_as_csv(path, tlas):
    with open(f"{path}/acronyms.csv", "wt") as fw:
        writer = csv.writer(fw)
        for tla in tlas:
            writer.writerow([str(tla)])
    return

def delete_from_source(path):
    
    return

def write_in_output(path, line_number, res):
    data = None
    with open(f'{path}/acronyms.csv', 'r') as f:
        reader = csv.reader(f)
        data = list(reader)

    line_to_modify = data[line_number]
    line_to_modify.append(res)

    # Write the modified data back to the CSV file
    with open('acronyms.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(data)
    return

def get_csv_tlas(path):
    tlas = []
    offset = 0
    with open(f"{path}/acronyms.csv") as file:
        info = csv.reader(file, delimiter=',')
        for row in info:
            if len(row) == 1:
                tlas.append(row[0])
            else:
                offset += 1

    return tlas, offset

def check_acronyms():
    path = "/Users/michal/Documents/playground/acronyms"
    current_tlas, offset = get_csv_tlas(path)
    
    for i in range(0, len(current_tlas)):
        print(current_tlas[i])
        while(True):
            res = input() # 'y' or 'n'
            if res == 'y' or res == 'n':
                print("only use 'y' or 'n' as responses")
                break
        write_in_output(path, offset + i, res)
        os.system('clear')
    return 

# one time run function
def create_acronyms():
    path = "/Users/michal/Documents/playground/acronyms"
    l = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    tlas = []
    
    for i in range(0, len(l)):
        for j in range(0, len(l)):
            for k in range(0, len(l)):
                tlas.append(f"{l[i]}{l[j]}{l[k]}")
    
    final_tlas = []
    while(0 < len(tlas)):
        pos = math.floor(random.random() * len(tlas))
        final_tlas.append(tlas[pos])
        del tlas[pos]
        
    save_as_csv(path, final_tlas)
    return 

# write_in_output("/Users/michal/Documents/playground/acronyms", 2, "lala")
# create_acronyms()


check_acronyms()