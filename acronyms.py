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

def write_in_output(path, line_number, res):
    data = None
    with open(f'{path}/acronyms.csv', 'r') as f:
        reader = csv.reader(f)
        data = list(reader)

    line_to_modify = data[line_number]
    if len(line_to_modify) == 2:
        line_to_modify.pop()
    line_to_modify.append(res)

    # Write the modified data back to the CSV file
    with open('acronyms.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(data)
    return

def get_csv_tlas(path):
    tlas = []
    positions = []
    with open(f"{path}/acronyms.csv") as file:
        info = csv.reader(file, delimiter=',')
        i = 0
        for row in info:
            if len(row) == 1:
                tlas.append(row[0])
                positions.append(i)
            i += 1

    return tlas, positions

def check_acronyms():
    path = "/Users/michal/Documents/playground/acronyms"
    current_tlas, positions = get_csv_tlas(path)
    i = -1
    res = None

    while(i < len(current_tlas)):
        i += 1
        print(current_tlas[i])
        while(True):
            res = input() # 'y', 'n' or 'b'
            if res == 'y' or res == 'n' or res == 'b':
                break
            else:
                print("only use 'y', 'n' or 'b' as responses")
        
        if res == 'b':
            if i == 0:
                i -= 1
            else:
                i -= 2
            os.system('clear')
            continue
        write_in_output(path, positions[i], res)
        os.system('clear')
    print("CONGRATULATIONS!! You've submitted data for all TLAs.\nSee the visualization section in the README to visualize your data.")
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

# create_acronyms()
check_acronyms()