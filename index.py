
import pandas as pd
from pprint import pprint
import time
from os import sys
import matplotlib.pyplot as plt


# imports countydict.txt file
import ast

# loads dictionary from countydict.txt file
with open("/Users/nigelmeyer/Desktop/Python/Voter_Data/countydict.txt", "r") as data:
    counties = ast.literal_eval(data.read())

# reads voterstats Excel sheet into a pandas DataFrame
df = pd.read_excel(r"/Users/nigelmeyer/Desktop/Python/Voter_Data/voterstats-20220215-080324.xls")

# splits the 'County' column after the index number into 'Index' and 'County' columns
df[['index', 'County']] = df['County'].str.split(expand=True)


# main function
def main(df):

    # loops program
    while True:

        # prints list of available counties
        for county in counties.keys():
            print(county)
        
        print('\n')

        printcountychoices(df)




    
    


# prints the counties the user has requested
def printcountychoices(df):
    chosen_counties = continuouscounty()
    if 'Q' in chosen_counties:
            sys.exit(0)
    else:        
        try:
            print(df[df['County'].isin(chosen_counties.split()[:-1])])
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
                    Enter 'Q' to quit at anytime\n").upper()
        county_list += choice + ' '
        if choice == 'Q':
            return county_list
        elif choice == 'C':
            return county_list  

def print_bar_graph(df, chosen_counties):
    
    # x = chosen_counties.split()[:-1]
    # y = df.columns[2:4]

    chosen_plot = df[df['County'].isin(chosen_counties.split()[:-1])]
    ax = chosen_plot.plot(kind='bar')
    # ax = df[['Rep','Dem']].plot(x='County', kind='bar', title ="V comp", figsize=(15, 10), legend=True, fontsize=12)
    ax.set_xlabel("County", fontsize=12)
    ax.set_ylabel("Registered", fontsize=12)
    plt.show()

    # print(type(x))
    # print(x)
    # print(type(y))
    # print(y)
    # plt.bar(x,y)
    # plt.xlabel("Counties")
    # plt.ylabel("Number of Registered Voters")
    # plt.title("Number of Democrats and Republicans in each county")
    


if __name__ == "__main__":
    main(df) 