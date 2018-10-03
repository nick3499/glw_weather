#!/usr/bin/python3
'''Scrape Web page for personal weather station data using:.
- `urllib3` for requests
- `bs4` for HTML parsing
- `terminaltables` for ASCII table format
Created this script for testing purposes and personal use.
ISC License (ISC) https://opensource.org/licenses/ISC
Copyright © nick3499@github
'''
import urllib3
from bs4 import BeautifulSoup
from terminaltables import AsciiTable

http = urllib3.PoolManager()
req = http.request("GET", "http://www.weatherlink.com/user/gooselakewx/index.php?view=summary&headers=0")
if req.status == 200:
    blob = req.data
else:
    print("Check req.status")
soup = BeautifulSoup(blob, "html.parser")

# Intro
print('Personal weather station data (scraped from Davis® Weatherlink)\n \
\033[32mPWS name:\033[0m', soup.find('td', {'class': 'summary_station_name'}).string, \
'\n', soup.find('td', {'class': 'summary_timestamp'}).string, \
'\n', soup.select("td:nth-of-type(98)")[0].string)

main_data = [
['OBSERVATION', '', '', '', '', '', '', ''],
# Temperature
['\033[32mTEMPERATURE:\033[0m', \
f'{soup.select("td:nth-of-type(14)")[0].string}', \
'\033[32mH\033[0m', f'{soup.select("td:nth-of-type(15)")[0].string}', f'{soup.select("td:nth-of-type(16)")[0].string}', \
'\033[32mL\033[0m', f'{soup.select("td:nth-of-type(17)")[0].string}', f'{soup.select("td:nth-of-type(18)")[0].string}'],
# Humidity
['\033[32mHUMIDITY:\033[0m', \
f'{soup.select("td:nth-of-type(20)")[0].string}', \
'\033[32mH\033[0m', f'{soup.select("td:nth-of-type(21)")[0].string}', f'{soup.select("td:nth-of-type(22)")[0].string}', \
'\033[32mL\033[0m', f'{soup.select("td:nth-of-type(23)")[0].string}', f'{soup.select("td:nth-of-type(24)")[0].string}'],
# Heat index
['\033[32mHEAT INDEX:\033[0m', \
f'{soup.select("td:nth-of-type(40)")[0].string}', \
'\033[32mH\033[0m', f'{soup.select("td:nth-of-type(41)")[0].string}', f'{soup.select("td:nth-of-type(42)")[0].string}', '', ''],
# Wind Chill
['\033[32mWIND CHILL:\033[0m', \
f'{soup.select("td:nth-of-type(46)")[0].string}', \
'', '', '', \
'\033[32mL\033[0m', f'{soup.select("td:nth-of-type(49)")[0].string}', f'{soup.select("td:nth-of-type(50)")[0].string}'],
# Dew point
['\033[32mDEW POINT:\033[0m', \
f'{soup.select("td:nth-of-type(52)")[0].string}', \
'\033[32mH\033[0m', f'{soup.select("td:nth-of-type(53)")[0].string}', f'{soup.select("td:nth-of-type(54)")[0].string}', \
'\033[32mL\033[0m', f'{soup.select("td:nth-of-type(55)")[0].string}', f'{soup.select("td:nth-of-type(56)")[0].string}'],
# Barometer
['\033[32mBAROMETER:\033[0m', \
f'{soup.select("td:nth-of-type(59)")[0].string} {soup.select("td:nth-of-type(65)")[0].string}', \
'\033[32mH\033[0m', f'{soup.select("td:nth-of-type(60)")[0].string}', f'{soup.select("td:nth-of-type(61)")[0].string}', \
'\033[32mL\033[0m', f'{soup.select("td:nth-of-type(62)")[0].string}', f'{soup.select("td:nth-of-type(63)")[0].string}'],
# Wind speed Direction
['\033[32mWIND SPEED:\033[0m', \
f'{soup.select("td:nth-of-type(72)")[0].string} — {soup.select("td:nth-of-type(78)")[0].string}', \
'\033[32mH\033[0m', f'{soup.select("td:nth-of-type(73)")[0].string}', f'{soup.select("td:nth-of-type(74)")[0].string}'],
# Solar Radiation
['\033[32mSOLAR RADIATION:\033[0m', \
f'{soup.select("td:nth-of-type(85)")[0].string}', \
'\033[32mH\033[0m', f'{soup.select("td:nth-of-type(86)")[0].string}', f'{soup.select("td:nth-of-type(87)")[0].string}'],
# UV Radiation
['\033[32mUV RADIATION:\033[0m', \
f'{soup.select("td:nth-of-type(91)")[0].string}', \
'\033[32mH\033[0m', f'{soup.select("td:nth-of-type(92)")[0].string}', f'{soup.select("td:nth-of-type(93)")[0].string}']
]

rainfall = [
['\033[32mRAINFALL:\033[0m', \
f'\033[32m Rain/hr:\033[0m {soup.select("td:nth-of-type(130)")[0].string}', \
f'\033[32mtoday:\033[0m {soup.select("td:nth-of-type(131)")[0].string}', \
f'\033[32mstorm:\033[0m {soup.select("td:nth-of-type(132)")[0].string}', \
f'\033[32mmonth:\033[0m {soup.select("td:nth-of-type(133)")[0].string}', \
f'\033[32myear:\033[0m {soup.select("td:nth-of-type(134)")[0].string}']
]

soil = [
['\033[32mSOIL TEMPERATURE:\033[0m', \
f'\033[32mST 1:\033[0m {soup.select("td:nth-of-type(155)")[0].string}', \
f'\033[32mST 2:\033[0m {soup.select("td:nth-of-type(161)")[0].string}', \
f'\033[32mST 3:\033[0m {soup.select("td:nth-of-type(167)")[0].string}', \
f'\033[32mST 4:\033[0m {soup.select("td:nth-of-type(173)")[0].string}']
]

table = AsciiTable(main_data)
r_table = AsciiTable(rainfall)
s_table = AsciiTable(soil)

print(table.table)
print(r_table.table)
try:
    print(s_table.table)
except IndexError:
    print("Soil temperature data is unavailable.")
