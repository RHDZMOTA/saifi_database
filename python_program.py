# -*- coding: utf-8 -*-

'''
Authors and contributers:
>> Rodrigo Hernandez Mota
>> [ add ]
'''

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from load import load_data

print('Initializing...')

def quit():
    print('Okay, thanks for using.')
    os._exit(1)

def show_tabl():
    members, roles, status, eyecolor, members_status, members_roles, physical_charact = load_data()
    print('==================== show_tabl ==================== init')
    print('Showing data tables...')
    print('>> members  \n',  members)
    print('>> roles    \n',    roles)
    print('>> status   \n',   status)
    print('>> eyecolor \n', eyecolor)
    print('>> members_status   \n',   members_status)
    print('>> members_roles    \n',    members_roles)
    print('>> physical_charact \n', physical_charact)
    print('\n')
    # add a general table... 
    print('>> general table: \n')
    print('\n')
    print('==================== show_tabl ==================== end')
    print('Returning to main menu... \n')

def proc_tabl():
    members, roles, status, eyecolor, members_status, members_roles, physical_charact = load_data()
    print('==================== proc_tabl ==================== init')
    # add... 
    print('\n')
    print('==================== proc_tabl ==================== end')
    print('Returning to main menu... \n')

'''
Global variable: OPTIONS
Contains the data for the main menu.
Relates an option (given by the user) with the description and a function.
'''
OPTIONS = {"0":dict( desc = "Quit", func = quit),
           "1":dict( desc = "Explore database (show raw tables)", func = show_tabl),
           "2":dict( desc = "Explore database (processed tables)", func = proc_tabl)}
print("Done. \n")

def main():
    print("Loading main menu...")
    print("Note: remember to avoid the use of special characters. \n")
    while True:
        print("\n::::MAIN MENU::::::::::::::::::::::::")
        print("\nPlease choose an option:")
        for key in sorted(OPTIONS.keys()):
            print("\t", key,OPTIONS[key]["desc"])
        inp = input("\nSelection: ")
        print("\n")
        if not inp in OPTIONS.keys():
            print("Invalid selection")
        else:
            OPTIONS[inp]["func"]()

main()



'''
More resources:
- menu building http://stackoverflow.com/questions/23034126/assign-multiple-inputs-into-one-if-else-statement-python
- append pandas dataframe to csv http://stackoverflow.com/questions/17530542/how-to-add-pandas-data-to-an-existing-csv-file
- manipulate dataframes http://pandas.pydata.org/pandas-docs/stable/merging.html
'''