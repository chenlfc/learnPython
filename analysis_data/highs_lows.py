from matplotlib import pyplot as plt

from conversion_f_c import ConversionForC as cFC
from get_highs_lows import GetHighsAndLows

# 从文件中获取最高气温
# filename = './analysis_data/sitka_weather_07-2014.csv'
# filename = './analysis_data/sitka_weather_2014.csv'
filename = './analysis_data/death_valley_2014.csv'
cfc = cFC()
h_l = GetHighsAndLows(filename)

dates = h_l.dates
f_highs = h_l.highs
f_lows = h_l.lows
highs, lows = [], []

for high in f_highs:
    cfc.temperature = high
    highs.append(cfc.f_to_c())

for low in f_lows:
    cfc.temperature = low
    lows.append(cfc.f_to_c())

# 根据数据绘制图形
fig = plt.figure(dpi=64, figsize=(10, 6))
plt.plot(dates, highs, c='red', alpha=0.5)
plt.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

plt.plot(dates, f_highs, c='green', alpha=0.5)
plt.plot(dates, f_lows, c='orange', alpha=0.5)
plt.fill_between(dates, f_highs, f_lows, facecolor='green', alpha=0.1)

# 设置图形的格式
plt.title(
    "Daily high and low temperatures - 2014\nDeath Valley, CA", fontsize=24)
plt.xlabel('', fontsize=16)

# 用于避免标签重叠，自动倾斜x轴上的日期
fig.autofmt_xdate()

plt.ylabel("Temperature (℃) - red & blue\n(℉) - green & orange", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
