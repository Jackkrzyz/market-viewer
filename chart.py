import subprocess, sys, os

def open_chart(ticker: str):
    print(ticker)
    return 
    has_display = os.name == "nt" or bool(os.environ.get("DISPLAY")) or bool(os.environ.get("WAYLAND_DISPLAY"))
    if has_display:
        subprocess.Popen([
            sys.executable, "-c",
            f"from lightweight_charts import Chart; import pandas as pd; df=pd.read_csv('ohlcv.csv'); c=Chart(toolbox=True); c.set(df); c.show(block=True)"
        ])
        return

    raise RuntimeError("No graphical display detected. No X/Wayland found. On headless Linux use xvfb-run or enable a display.")