import pandas as pd
import sys

if len(sys.argv) > 1:
    file_name = sys.argv[1]
else:
    file_name = 'data.csv'

vectors = []

file = pd.read_csv(file_name)
file.drop('Date', inplace=True, axis=1)

next_day_open = file['Open'].tolist()
next_day_open.pop(0)
next_day_open.append(next_day_open[-1])
file['Topen'] = next_day_open  # tomorrow's open price

adj_close = file['Adj Close'].tolist()

for i in range(0, len(adj_close)):
    if i == 0:
        vectors.append(0)
        continue
    vectors.append(int(float(adj_close[i]) > float(adj_close[i-1])))

file['Buy'] = vectors

file.to_csv('data.csv', index=False)
