'''
imports os, shutils, sched, time
# load sweep paths
# load dustbin path
# load ignores

# while true
#   for each path in sweeps
#       list items in sweep
#       for each item in list
#           move item from sweep to dustbin
'''
# imports os, shutils, sched, time
import shutil
from os import listdir, path, mkdir, remove
import schedule
from time import sleep
from datetime import datetime
from json import load
from sys import exit

try:
    file = open('config.json', 'r')
    config = load(file)
    file.close()
    SWEEPS = config["SWEEPS"]
    DUSTBIN = config["DUSTBIN"]
    IGNORES = config["IGNORES"]
    BIN_CONTENTS = []
except FileNotFoundError:
    print("config.json not found. Quitting...")
    exit()


def clean_up():
    '''Try to create DUSTBIN directory, move on if it exists'''
    try:
        BIN_CONTENTS = listdir(DUSTBIN)
    except FileNotFoundError:
        mkdir(DUSTBIN)
        print(">>created", DUSTBIN)
        BIN_CONTENTS = listdir(DUSTBIN)

    print("______________________________________")
    print(str(datetime.now()) + ": working...")
    #   for each path in sweeps
    for dir_path in SWEEPS:
        print("...", dir_path)
        #   list items in sweep
        try:
            contents = listdir(dir_path)
        except FileNotFoundError:
            print("...... contents not found. Moving on...")
        #   for each item in list
        for item in contents:
            print("......", item)
            #   move item from sweep to dustbin
            if item in IGNORES:
                print("......... ignored")
                continue

            try:
                dst = shutil.move(
                    path.join(dir_path, item),
                    DUSTBIN
                )
                BIN_CONTENTS.append(item)
                print("......... Moved to", dst)
            except shutil.Error:
                print(".........", item, "exists in", DUSTBIN)
                remove(path.join(dir_path, item))
                print("......... deleted")
        if not contents:
            print("...... No items to move. Moving on...")
    print("Cleaning complete. Rescheduling...")


# schedule delay(10min)
if __name__ == "__main__":
    print('Pulling rip cord...')

    # Try to create DUSTBIN directory, move on if it exists
    try:
        BIN_CONTENTS = listdir(DUSTBIN)
    except FileNotFoundError:
        mkdir(DUSTBIN)
        print(">>created", DUSTBIN)
        BIN_CONTENTS = listdir(DUSTBIN)

    # schedule program to run every 2 minutes
    schedule.every(2).minutes.do(clean_up)

    # main loop
    while True:
        schedule.run_pending()
        sleep(30)
