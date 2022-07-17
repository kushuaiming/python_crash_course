import csv

from matplotlib import pyplot as plt

filename = './csv_data/sitka_weather_2018_full.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    highs =[]
    for row in reader:
        try:
            high = int(row[8])
        except ValueError: # there may be empty data
            pass
        highs.append(high)

fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(highs, c='red')

plt.title('Daily high temperatures, 2018', fontsize=24)
plt.xlabel('', fontsize=16)
plt.ylabel("Temperature(F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()