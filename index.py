import pandas as pd
from pprint import pprint
from Voter_Data import counties




if __name__ == "__main__":
    for county in counties.keys():
            print(county)

    def main():
        df = pd.read_excel(r'/Users/nigelmeyer/Desktop/Python/Voter_Data/voterstats-20220215-080324.xls')
        

        def askforcounty():
            x = input("Which county would you like to examine?\n").upper()
            for county in counties.keys():
                if x == county:
                    try:
                        print(df.iloc[counties[x]])
                        input("Press RETURN to continue.")
                        continue
                    except:
                        print("County not found.\n")
        
        askforcounty()