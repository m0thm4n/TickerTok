from pandas_datareader.quandl import QuandlReader
from .config import api_key

def get_close_data(tickers):
    """
    Arguments:
    ----------
    ticker - (str or list) stock ticker to retrieve
             using pandas_datareader.quandl

    Returns:
    --------
    all_tickers - dict(None or pd.DataFrames)
        key: ticker
        value: None if ticker dne or dataframe of close prices
    """
    if not type(tickers) is list \
       and type(tickers) is str:
            tickers = [tickers]
    
    all_tickers = dict()
    for tick in tickers:
        try:
            data = QuandlReader(tick, api_key=api_key).read()
            data.sort_values(by="Close", ascending=False)
            all_tickers[tick] = dict.fromkeys(['close', 'date'])
            all_tickers[tick]['date'] = [d.strftime("%Y-%m-%d") for d in data.index.tolist()]
            all_tickers[tick]['close'] = list(data['Close'])
        except:
            all_tickers[tick] = None
            print(f"ticker {tick} not valid")
        
    return all_tickers
