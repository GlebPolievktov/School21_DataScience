import sys

def name(name_of_company:str):
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
    if name_of_company not in COMPANIES:
        print("Unknown company")
    else:
        print(STOCKS[COMPANIES[name_of_company]])

if __name__ == "__main__":
    if len(sys.argv[:]) == 2:
        name(sys.argv[1].capitalize())
    else:
        sys.exit(0)
    
