import yfinance

class Download():
    
    def __init__(self, data):
        self.data = yfinance.download(tickers = data, period = '1d', interval = '1m')
        self.data.to_csv(f'{data}.csv')
        print('Done')
