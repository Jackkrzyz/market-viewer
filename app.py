from dearpygui import dearpygui as dpg
from chart import *
import itertools

dpg.create_context()

tab_counter = itertools.count(1)
open_chart_tabs = set()

def close_window(sender, app_data, user_data):
    tag = user_data
    if tag in open_chart_tabs:
        open_chart_tabs.remove(tag)
    dpg.delete_item(tag)

def open_chart_clicked(sender, app_data, user_data):
    # user_data is a dict with input tag and window tag
    input_tag = user_data["input_tag"]
    window_tag = user_data["window_tag"]
    ticker = dpg.get_value(input_tag)
    try:
        open_chart(ticker)   
    except Exception as e:
        print("Failed to open chart:", e)
    close_window(None, None, window_tag)
def open_chart_tab():
    if open_chart_tabs:
        existing = next(iter(open_chart_tabs))  
        try:
            dpg.focus_item(existing)
            dpg.show_item(existing)
        except Exception:
            pass
        return
    tab_id = next(tab_counter)
    window_tag = f"Open Chart"
    open_chart_tabs.add(window_tag)
    with dpg.window(tag=window_tag, label=f"Open Chart", width=100, height=100, no_resize=True, on_close=close_window, user_data=window_tag):
        dpg.add_text("Ticker:")
        dpg.add_input_text(label="##ticker_input", tag="ticker_input", default_value="BTC")
        dpg.add_button(label="Open", callback=open_chart_clicked, user_data={"input_tag": "ticker_input", "window_tag": window_tag})

def _on_t_down(sender, app_data):
    if dpg.is_key_down(dpg.mvKey_Tab):
        open_chart_tab()

with dpg.handler_registry():
    dpg.add_key_press_handler(key=dpg.mvKey_T, callback=_on_t_down)

with dpg.window(tag="HomePage", label="HomePage", width=400, height=400, no_resize=True):
    dpg.add_text("This is the Home Page.")
    # allow for widgets like watchlists, news, etc. in the future

with dpg.window(tag="WelcomeTab", label="WelcomeTab", width=400, height=400):
    dpg.add_text("Welcome to MarketViewer!")
    dpg.add_text("TAB+T to open a new chart tab")


dpg.create_viewport(title='MarketViewer')
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("HomePage", True)
dpg.start_dearpygui()   
dpg.destroy_context()