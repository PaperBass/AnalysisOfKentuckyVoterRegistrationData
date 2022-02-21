import pandas as pd



while True:
    def main():
        df = pd.read_excel (r'/Users/nigelmeyer/Desktop/Python/Voter_Data/voterstats-20220215-080324.xls')

        # pparties = pd.read_excel('/Users/nigelmeyer/Desktop/Python/Voter_Data/voterstats-20220215-080324.xls', index_col=0).values.tolist()

        # print(pparties)

        x = input("What do you want to see? Press 'R' for Republican, 'D' for Democrat.").upper()
        print(x)


        if x == 'R':
            print(df[['County', 'Precinct count', 'Rep']])
        elif x == 'D':
            print(df[['County', 'Precinct count', 'Dem']])
    main()