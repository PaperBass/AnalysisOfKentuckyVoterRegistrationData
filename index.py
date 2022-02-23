import pandas as pd
from pprint import pprint
import time


while True:

    counties = {'ADAIR':1,
                'ALLEN':2,
                'ANDERSON':3,
                'BALLARD':4,
                'BARREN':5,
                'BATH':6,
                'BELL':7,
                'BOONE':8,
                'BOURBON':9,
                'BOYD':10,
                'BOYLE':11,
                'BRACKEN':12,
                'BREATHITT':13,
                'BRECKINRIDGE':14,
                'BULLITT':15,
                'BUTLER':16,
                'CALDWELL':17,
                'CALLOWAY':18,
                'CAMPBELL':19,
                'CARLISLE':20,
                'CARROLL':21,
                'CARTER':22,
                'CASEY':23,
                'CHRISTIAN':24,
                'CLARK':25,
                'CLAY':26,
                'CLINTON':27,
                'CRITTENDEN':28,
                'CUMBERLAND':29,
                'DAVIESS':30,
                'EDMONSON':31,
                'ELLIOTT':32,
                'ESTILL':33,
                'FAYETTE':34,
                'FLEMING':35,
                'FLOYD':36,
                'FRANKLIN':37,
                'FULTON':38,
                'GALLATIN':39,
                'GARRARD':40,
                'GRANT':41,
                'GRAVES':42,
                'GRAYSON':43,
                'GREEN':44,
                'GREENUP':45,
                'HANCOCK':46,
                'HARDIN':47,
                'HARLAN':48,
                'HARRISON':49,
                'HART':50,
                'HENDERSON':51,
                'HENRY':52,
                'HICKMAN':53,
                'HOPKINS':54,
                'JACKSON':55,
                'JEFFERSON':56,
                'JESSAMINE':57,
                'JOHNSON':58,
                'KENTON':59,
                'KNOTT':60,
                'KNOX':61,
                'LARUE':62,
                'LAUREL':63,
                'LAWRENCE':64,
                'LEE':65,
                'LESLIE':66,
                'LETCHER':67,
                'LEWIS':68,
                'LINCOLN':69,
                'LIVINGSTON':70,
                'LOGAN':71,
                'LYON':72,
                'MCCRACKEN':73,
                'MCCREARY':74,
                'MCLEAN':75,
                'MADISON':76,
                'MAGOFFIN':77,
                'MARION':78,
                'MARSHALL':79,
                'MARTIN':80,
                'MASON':81,
                'MEADE':82,
                'MENIFEE':83,
                'MERCER':84,
                'METCALFE':85,
                'MONROE':86,
                'MONTGOMERY':87,
                'MORGAN':88,
                'MUHLENBERG':89,
                'NELSON':90,
                'NICHOLAS':91,
                'OHIO':92,
                'OLDHAM':93,
                'OWEN':94,
                'OWSLEY':95,
                'PENDLETON':96,
                'PERRY':97,
                'PIKE':98,
                'POWELL':99,
                'PULASKI':100,
                'ROBERTSON':101,
                'ROCKCASTLE':102,
                'ROWAN':103,
                'RUSSELL':104,
                'SCOTT':105,
                'SHELBY':106,
                'SIMPSON':107,
                'SPENCER':108,
                'TAYLOR':109,
                'TODD':110,
                'TRIGG':111,
                'TRIMBLE':112,
                'UNION':113,
                'WARREN':114,
                'WASHINGTON':115,
                'WAYNE':116,
                'WEBSTER':117,
                'WHITLEY':118,
                'WOLFE':119,
                'WOODFORD':120}


                
    for county in counties.keys():
            pprint(county)

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
                        print("An error occured")
        
        askforcounty()
    main()