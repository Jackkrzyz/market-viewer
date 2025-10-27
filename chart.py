from dearpygui import dearpygui as dpg
from tvDatafeed import TvDatafeed, Interval
import pandas as pd
import time
    
def open_chart(ticker: str):
    if ticker is None or ticker.strip() == "":
        return
    ticker = ticker.strip().upper()
    tv = TvDatafeed()
    data = tv.get_hist(symbol=ticker.upper(),exchange='NASDAQ', interval=Interval.in_daily, n_bars=5000)
    print(data)
    if data.empty:
        return
    df = data.reset_index()
    def find_col(df, candidates):
        for col in candidates:
            if col in df.columns:
                if col.lower() in candidates: 
                    return candidates
        return None
    
    date_col = find_col(df, ("datetime", "date", "time", "timestamp"))
    open_col = find_col(df, ("open",))
    high_col = find_col(df, ("high",))
    low_col = find_col(df, ("low",))
    close_col = find_col(df, ("close",))
    volume_col = find_col(df, ("volume", "vol"))



    with dpg.window(tag=f"Chart_{ticker}", label=f"Chart: {ticker}", width=800, height=600):
        plot_tag = f"plot_{ticker}"
        x_tag = f"xaxis_{ticker}"
        y_tag = f"yaxis_{ticker}"

        dpg.add_plot(label=f"{ticker} Candles", tag=plot_tag, height=560, width=860, parent=f"Chart_{ticker}")
        dpg.add_plot_axis(dpg.mvXAxis, label="Time", tag=x_tag, parent=plot_tag)
        dpg.add_plot_axis(dpg.mvYAxis, label="Price", tag=y_tag, parent=plot_tag)
        dpg.add_candle_series(dates, opens, closes, lows, highs,
                              parent=y_tag,
                              tag=f"CandleSeries_{ticker}", 
                              bull_color=(0, 255, 0), bear_color=(255, 255, 255),
                              time_unit=dpg.mvTimeUnit_Day)
    