import sys

def func():
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
    s = sys.argv[1].replace(' ','').split(',')
    for i in s:
        if not i:
            sys.exit(0)
    for i in s:
        if i.lower().capitalize() in COMPANIES:
            print(f'{i.lower().capitalize()} stock price is {STOCKS[COMPANIES[i.lower().capitalize()]]}')
        elif i.upper() in STOCKS:
            for j in COMPANIES:
                if COMPANIES[j] == i.upper():
                    print(f'{i.upper()} is a ticker symbol for {j}')
        else:
            print(f'{i} is an unknown company or an unknown ticker symbol')
    
    

        
if __name__ == "__main__":
    if len(sys.argv[:]) == 2:
        func()
    else:
        sys.exit(0)

