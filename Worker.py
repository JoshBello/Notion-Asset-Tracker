from datetime import datetime, timedelta
import yfinance as yf
from notion.client import *
from notion.block import *
from forex_python.converter import CurrencyRates

#  Replace Values
token_v2 =
page_url =
table_url =

client = NotionClient(token_v2=token_v2, start_monitoring=False)
page = client.get_block(page_url)
table = client.get_collection_view(table_url)

#  To Allow For Weekends and Holidays:
#  5 Days Are Read and Most Recent Taken
now = datetime.now()
end_date = now.strftime('%Y-%m-%d')
start_date = (datetime.now() - timedelta(days=5)).strftime('%Y-%m-%d')

c = CurrencyRates()


def most_recent_close(ticker, currency):
    data = yf.download(ticker, start=start_date, end=end_date)
    close = data['Close'].tolist()
    close = c.convert(currency[:3], 'GBP', close[-1])

    if currency.endswith('X'):
        close = close / 100

    return round(close, 3)

#  Database is Read
#  Values Caculated and Written
def update_table():
    updated_count, updated_total = 0, 0
    for count, row in enumerate(table.collection.get_rows()):
        ticker, currency, options, inital, value = row.Ticker, row.Currency, row.Options, row.Initial, row.Value

        close = most_recent_close(ticker, currency)
        perc_change = ((close / inital) - 1)
        value = close * options

        row.Close = close
        row.Percent = round(perc_change, 3)
        row.Value = value

        updated_count += 1

    updated_total = count + 1

    return updated_count, updated_total

#  Page Description Updated
#  Time and Date
#  Updates out of Total 
def update_desc():
    current_date_time = (datetime.now()).strftime("%H:%M - %d/%m/%y")
    updated_count, updated_total = update_table()
    page.description = '{}\n{} of {} Updated'.format(
        current_date_time, updated_count, updated_total)


def run(*args):
    update_desc()
    print(args)


run()
