import math
import yfinance as yf


def get_data(ticker):
    data = yf.download(ticker, period="9y")
    return data


def get_stock_price(ticker):
    data = get_data(ticker)
    return data


def close_day(data, stocks):
    new_close = data["Close"]
    date = data.head(1).index[0]
    diff = 1 - start_close / new_close
    update = False
    sum = 0
    if diff > 0.05:
        print(f"{date}")
        stocks_sold = math.floor(stocks / 2)
        stocks -= stocks_sold
        update = True
        print(f"Close price has increased {diff + 1}. Sell.")
        sum = stocks_sold * new_close
    elif diff < -0.05:
        stocks_bought = math.floor(max_buy / new_close)
        stocks += stocks_bought
        update = True
        print(f"Close price has decreased {diff + 1}. Buy.")
        sum = -1 * stocks_bought * new_close
    return stocks, new_close, update, sum


if __name__ == "__main__":
    data = get_stock_price("KNEBV.HE")
    stocks = 0
    cash_money = 0
    start_date = data.head(1).index[-1]
    start_close = data["Close"].iloc[-1]
    max_buy = 1000
    print(f"Start date: {start_date}")
    print(f"Start close: {start_close}")
    for index, row in data.iterrows():
        if index > start_date:
            stocks, new_close, update, sum = close_day(row, stocks)
            if update:
                start_close = new_close
                cash_money += sum
                print("********************************************************")
                print(f"Date: {index}")
                print(f"Stocks: {stocks} = {stocks * new_close}")
                print(f"Cash: {cash_money}")
                print(f"Total: {cash_money + stocks * new_close}")
    print("Done")
    exit()
