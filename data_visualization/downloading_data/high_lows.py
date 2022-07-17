import csv
from datetime import datetime

from matplotlib import pyplot as plt

filename = './csv_data/sitka_weather_2018_full.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, highs, lows =[], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[2], '%Y-%m-%d')
            high = int(row[8])
            low = int(row[9])
        except ValueError: # there may be empty data
            pass
        lows.append(low)
        highs.append(high)
        dates.append(current_date)

fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red')
plt.plot(dates, lows, c='blue')

plt.title('Daily high and low temperatures, 2018', fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature(F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()