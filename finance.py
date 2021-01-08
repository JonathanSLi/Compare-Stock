import yfinance as yf
from pandas_datareader import data as pdr
import matplotlib.pyplot as plt
from datetime import datetime


f = open("companies.txt", "r")
o = open("companiesInfo.txt", "w")


companies = f.read().split()
d = {1: "forwardPE", 2: "dividendRate", 3: "pegRatio", 4: "enterpriseValue", 5: "fullTimeEmployees",
6: "regularMarketPrice", 7: "totalAssets", 8: "threeYearAverageReturn", 9: "fiftyTwoWeekHigh", 10: "twoHundredDayAverage",
11: "regularMarketDayHigh"}

print("which fields would you like (separate by spaces, i.e. 1 3 5): ")
print("1. forwardPE")
print("2. dividendRate")
print("3. pegRatio (5 year exp)")
print("4. enterpriseValue")
print("5. fullTimeEmployees")
print("6. regularMarketPrice")
print("7. totalAssets")
print("8. threeYearAverageReturn")
print("9. fiftyTwoWeekHigh")
print("10. twoHundredDayAverage")
print("11. regularMarketDayHigh")

fields = input().split() 
if fields[0] == "X":
    print("EXITING...")
else:
    s = "COMPANIES"
    spaces = (25-len(s)) * " "
    s += spaces
    for field in fields:
        f = d[int(field)].upper()
        s += f
        spaces = (25-len(f)) * " "
        s += spaces
    o.write(s + '\n')
    print("loading...")
    for comp in companies:
        c = yf.Ticker(comp)
        s = c.info['shortName']
        spaces = (25-len(s)) * " "
        s += spaces
        for f in fields:
            info = str(c.info[d[int(f)]])
            spaces = (25-len(info)) * " "
            s += info + spaces
        o.write(s + '\n')
print("finished and loaded to file!")
        

