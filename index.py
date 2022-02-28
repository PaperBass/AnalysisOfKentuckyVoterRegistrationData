import pandas as pd
from pprint import pprint
import time

#used to load dictionary from countydict.txt file
import ast

# loads dictionary from countydict.txt file
with open("/Users/nigelmeyer/Desktop/Python/Voter_Data/countydict.txt", "r") as data:
    counties = ast.literal_eval(data.read())

# loops program
while True:
    # prints list of available counties
    for county in counties.keys():
        print(county)

    # main function
    def main():
        # reads voterstats Excel sheet into a pandas DataFrame
        df = pd.read_excel(r"/Users/nigelmeyer/Desktop/Python/Voter_Data/voterstats-20220215-080324.xls")
        
        # this asks the user to select a county to load
        def askforcounty():
            x = input("Which county would you like to examine?\n").upper()
            print(x)

            # This looks for the user's response in the list of available counties
            for county in counties.keys():

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
        askforcounty()
    main() 