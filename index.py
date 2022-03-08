
import pandas as pd
from pprint import pprint
import time
from os import sys


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

# asks user to list all the counties they wish to compare and waits for "C" to be input to continue
# this function is called in the printcountychoices() function
def continuouscounty():
    county_list = ''
    while True:
        county = input(
                    "List the counties you would like to see and press enter:\n\
                    Then enter 'C' when you're ready to continue.\n\
                    Enter 'Q' to quit at anytime\n").upper()
        county_list += county + ' '
        if county == 'Q':
            return county_list
        elif county == 'C':
            return county_list      
    


# prints the counties the user has requested
def printcountychoices(df):
    counties = continuouscounty()
    if 'Q' in counties:
            sys.exit(0)
    else:        
        try:
            print(df[df['County'].isin(counties.split()[:-1])])
            input("Press RETURN to continue.")
        except:
            print("Counties not found.\n")
            time.sleep(2)
            return




if __name__ == "__main__":
    main(df) 