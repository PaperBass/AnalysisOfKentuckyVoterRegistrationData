
import pandas as pd
from pprint import pprint
import time
from os import sys
import matplotlib.pyplot as plt


# imports countydict.txt file
import ast

# loads dictionary from countydict.txt file
with open("Voter_Data/countydict.txt", "r") as data:
    counties = ast.literal_eval(data.read())

# load dictionary of demographics from demographics.txt
with open("Voter_Data/demographicsdict.txt", "r") as demos:
    demographics = ast.literal_eval(demos.read())

# reads voterstats Excel sheet into a pandas DataFrame
df = pd.read_excel(r"/Users/nigelmeyer/Desktop/Python/Voter_Data/voterstats-20220215-080324.xls")

# splits the 'County' column after the index number into 'Index' and 'County' columns
df[['index', 'County']] = df['County'].str.split(expand=True)

# makes column names all lowercase
df.columns = map(str.lower, df.columns)

# prints the counties the user has requested
def printcountychoices(df):
    chosen_counties = continuouscounty()
    if 'Q' in chosen_counties:
            sys.exit(0)
    else:        
        try:
            print(df[df['county'].isin(chosen_counties.split()[:-1])])
            print_bar_graph(df, chosen_counties)
            input("Press RETURN to continue.")
        except:
            print("Counties not found.\n")
            time.sleep(2)
            return

# asks user to list all the counties they wish to compare and waits for "C" to be input to continue
# this function is called in the printcountychoices() function
def continuouscounty():
    county_list = ''
    while True:
        choice = input(
                    "List the counties you would like to see and press enter:\n\
                    Then enter 'C' when you're ready to continue.\n\
                    Enter 'Q' to quit at anytime\n\n").upper()
        county_list += choice + ' '
        if choice == 'Q':
            return county_list
        elif choice == 'C':
            return county_list  


def demo_y_axis():

    print("\n\n")
    for demographic in demographics:
        print(demographic)
    chosen_y_axis = input("\nChoose which demographics you want to compare.\n\n").lower()
    return chosen_y_axis.split()

def print_bar_graph(df, chosen_counties):
    
    chosen_plot = df[df['county'].isin(chosen_counties.split()[:-1])]
    y_axis = demo_y_axis()
    print(chosen_counties)
    ax = chosen_plot.plot(y=y_axis, kind='bar')
    ax.set_xlabel("County", fontsize=12)
    ax.set_ylabel("Number of Registered", fontsize=12)
    for p in ax.patches:
        ax.annotate(int(p.get_height()), (p.get_x() * 1.005, p.get_height() * 1.005))
   

    plt.show()

# main function
def main(df):

    # loops program
    while True:

        # prints list of available counties
        for county in counties.keys():
            print(county)
        
        print('\n')

        printcountychoices(df)

if __name__ == "__main__":
    main(df) 