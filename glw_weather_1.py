#!/usr/bin/python3
'''Scrape Web page for personal weather station data using:
- `urllib3` for requests
- `bs4` for HTML parsing
Created this script for testing purposes and personal use.
ISC License (ISC) https://opensource.org/licenses/ISC
Copyright © nick3499@github
'''
import urllib3
from bs4 import BeautifulSoup

http = urllib3.PoolManager()
req = http.request("GET", "http://www.weatherlink.com/user/gooselakewx/index.php?view=summary&headers=0")
if req.status == 200:
    blob = req.data
else:
    print("Check req.status")
soup = BeautifulSoup(blob, "html.parser")

# Intro
print("Personal weather station data (scraped from Davis® Weatherlink)\n \
\033[32mPWS name:\033[0m", soup.find("td", {"class": "summary_station_name"}).string, \
"\n", soup.find("td", {"class": "summary_timestamp"}).string)
# Temperature
print("\033[36mTemperature:\033[0m", soup.select("td:nth-of-type(14)")[0].string,
"\n\033[36m       High:\033[0m", soup.select("td:nth-of-type(15)")[0].string,
"\033[36mat\033[0m", soup.select("td:nth-of-type(16)")[0].string, "\033[31m|\033[0m",
"\033[36mLow:\033[0m", soup.select("td:nth-of-type(17)")[0].string,
"\033[36mat\033[0m", soup.select("td:nth-of-type(18)")[0].string)
# Humidity
print("\033[32m   Humidity:\033[0m", soup.select("td:nth-of-type(20)")[0].string,
"\n\033[32m       High:\033[0m", soup.select("td:nth-of-type(21)")[0].string,
"\033[32mat\033[0m", soup.select("td:nth-of-type(22)")[0].string, "\033[31m|\033[0m",
"\033[32mLow:\033[0m", soup.select("td:nth-of-type(23)")[0].string,
"\033[32mat\033[0m", soup.select("td:nth-of-type(24)")[0].string)
# Heat index
print("\033[36m Heat index:\033[0m", soup.select("td:nth-of-type(40)")[0].string,
"\n\033[36m       High:\033[0m", soup.select("td:nth-of-type(41)")[0].string,
"\033[36mat\033[0m", soup.select("td:nth-of-type(42)")[0].string)
# Wind Chill
print("\033[32m Wind chill:\033[0m", soup.select("td:nth-of-type(46)")[0].string,
"\n\033[32m        Low:\033[0m", soup.select("td:nth-of-type(49)")[0].string,
"\033[32mat\033[0m", soup.select("td:nth-of-type(50)")[0].string)
# Dew point
print("\033[36m  Dew point:\033[0m", soup.select("td:nth-of-type(14)")[0].string,
"\n\033[36m       High:\033[0m", soup.select("td:nth-of-type(15)")[0].string,
"\033[36mat\033[0m", soup.select("td:nth-of-type(16)")[0].string, "\033[31m|\033[0m",
"\033[36mLow:\033[0m", soup.select("td:nth-of-type(17)")[0].string,
"\033[36mat\033[0m", soup.select("td:nth-of-type(18)")[0].string)
# Barometer + Trend
print("\033[32m  Barometer:\033[0m", soup.select("td:nth-of-type(59)")[0].string,
"\n\033[32m       High:\033[0m", soup.select("td:nth-of-type(60)")[0].string,
"\033[32mat\033[0m", soup.select("td:nth-of-type(61)")[0].string, "\033[31m|\033[0m",
"\033[32mLow:\033[0m", soup.select("td:nth-of-type(62)")[0].string,
"\033[32mat\033[0m", soup.select("td:nth-of-type(63)")[0].string, "\033[31m|\033[0m",
"\033[32mTrend:\033[0m", soup.select("td:nth-of-type(65)")[0].string)
# Wind speed + Direction
print("\033[36m Wind speed:\033[0m", soup.select("td:nth-of-type(72)")[0].string,
"\n\033[36m       High:\033[0m", soup.select("td:nth-of-type(73)")[0].string,
"\033[36mat\033[0m", soup.select("td:nth-of-type(74)")[0].string,
"\n\033[36m  Direction:\033[0m", soup.select("td:nth-of-type(78)")[0].string)
# Solar Radiation
print("\033[32m  Solar rad:\033[0m", soup.select("td:nth-of-type(85)")[0].string,
"\n\033[32m       High:\033[0m", soup.select("td:nth-of-type(86)")[0].string,
"\033[32mat\033[0m", soup.select("td:nth-of-type(87)")[0].string)
# UV Radiation
print("\033[36m     UV rad:\033[0m", soup.select("td:nth-of-type(91)")[0].string,
"\n\033[36m       High:\033[0m", soup.select("td:nth-of-type(92)")[0].string,
"\033[36mat\033[0m", soup.select("td:nth-of-type(93)")[0].string)
# 12 hr forecast
print("\033[32m12hr forecast:\033[0m", soup.select("td:nth-of-type(98)")[0].string)
# Rain
print("\033[36m Rain rates:\033[0m",
"\n\033[36m    Rain/hr:\033[0m", soup.select("td:nth-of-type(130)")[0].string, "\033[31m|\033[0m",
"\033[36mtoday:\033[0m", soup.select("td:nth-of-type(131)")[0].string, "\033[31m|\033[0m",
"\033[36mstorm:\033[0m", soup.select("td:nth-of-type(132)")[0].string, "\033[31m|\033[0m",
"\033[36mmonth:\033[0m", soup.select("td:nth-of-type(133)")[0].string, "\033[31m|\033[0m",
"\033[36myear:\033[0m", soup.select("td:nth-of-type(134)")[0].string)
print("\033[36mSoil Temperature:\033[0m",
"\n\033[32m     Temp 1:\033[0m", soup.select("td:nth-of-type(155)")[0].string, "\033[31m|\033[0m",
"\033[32mTemp 2:\033[0m", soup.select("td:nth-of-type(161)")[0].string, "\033[31m|\033[0m",
"\033[32mTemp 3:\033[0m", soup.select("td:nth-of-type(167)")[0].string, "\033[31m|\033[0m",
"\033[32mTemp 4:\033[0m", soup.select("td:nth-of-type(173)")[0].string)
