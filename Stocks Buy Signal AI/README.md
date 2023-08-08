## Purpose:
this tool is only useful when market is freshly opened, it need to current market open price and yesterdays data to give you a buy signal (1 means buy and 0 means don't).

## Usage:
1- download historical data from Yahoo finance.
2- Feed the file to clean_data.py and get data.csv output
```bash
python3 clean_data.py AMZN.csv
```
3- run predict.py and wait for it to do the math and ask for your input, enter the data in following format:
```
YesterdayOpen, YesterdayHigh, YesterdayLow, YesterdayClose, YesterdayAdj Close, YesterdayVolume, Todays Open
```

## Requirments:
```bash
pip install -U scikit-learn pandas
```
