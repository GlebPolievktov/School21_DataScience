import sys

def name(name_of_ticket:str):
    COMPANIES = {
        'Apple': 'AAPL',
        'Microsoft': 'MSFT',
        'Netflix': 'NFLX',
        'Tesla': 'TSLA',
        'Nokia': 'NOK'
    }

    STOCKS = {
        'AAPL': 287.73,
        'MSFT': 173.79,
        'NFLX': 416.90,
        'TSLA': 724.88,
        'NOK': 3.37
    }
    if name_of_ticket not in STOCKS.keys():
        print("Unknown ticker")
    else:
        for i in COMPANIES:
            if COMPANIES[i] == name_of_ticket:
                print(i,STOCKS[name_of_ticket])
            
    
if __name__ == "__main__":
    if len(sys.argv[:]) == 2:
        name(sys.argv[1].upper())
    else:
        sys.exit(0)