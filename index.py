import pandas as pd
from pprint import pprint
import time
import numpy as np

#used to load dictionary from countydict.txt file
import ast

# loads dictionary from countydict.txt file
with open("/Users/nigelmeyer/Desktop/Python/Voter_Data/countydict.txt", "r") as data:
    counties = ast.literal_eval(data.read())

# reads voterstats Excel sheet into a pandas DataFrame
df = pd.read_excel(r"/Users/nigelmeyer/Desktop/Python/Voter_Data/voterstats-20220215-080324.xls")

# splits the 'County' column after the index number into 'Index' and 'County' columns
df[['index', 'County']] = df['County'].str.split(expand=True)

print(df)

def comparecounty(df):
    county1 = input("To compare two counties, pick the first county by typing its name:\n").upper()
    county2 = input("Now select the second county by typing the name:\n").upper()

    try:
        print(df[df['County'].isin([county1, county2])])
        input("Press RETURN to continue.")
    except:
        print("Counties not found.\n")
        time.sleep(2)
        return

def askforcounty(df):

    # this asks the user to select a county to load
    x = input("Which county would you like to examine?\n\nOr type 'Statewide Totals' to receive statewide totals.").upper()

    # This looks for the user's response in the list of available counties
    for county in counties:

        # if the requested county is found, the df will be printed
        try:
        
            # here, the .iloc command inverts the columns and rows
            print(df.iloc[counties[x]])
            input("Press RETURN to continue.")
            return

        except:

            # error message if the requested county is not found
            print("County not found.\n")
            time.sleep(2)
            return
    

# main function
def main(df):

    # loops program
    while True:

        # prints list of available counties
        for county in counties.keys():
            print(county)

        # print(df)
        #df["County"]= df["County"].str.split()
        # print("new dataFrame: \n", df)

        comparecounty(df)

        #askforcounty(df)

if __name__ == "__main__":
    main(df) 