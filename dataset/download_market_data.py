import datetime
import pandas as pd
import yfinance as yf


def download_market_data(stock=['GOOG'], start='2021-01-01', end=datetime.date.today()):
    start = pd.to_datetime(start)
    data = yf.download(stock, start=start, end=end)
    return data


if __name__ == '__main__':

    stocks = ['AMD', 'GOOG']
    start_date = '2021-01-01'
    end_date = datetime.date.today()

    for stock in stocks:
        data = download_market_data(stock=stock, start=start_date, end=end_date)
        data.to_csv(f"{stock}_{start_date.replace('-', '')}_{end_date.strftime('%Y%m%d')}.csv")
        print(data)
