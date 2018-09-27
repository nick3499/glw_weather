# glw_weather
## Python 3: Scrape Weather Data from HTML: urllib3, BeautifulSoup, terminaltables

Two versions of a scraping script for tabulated weather data from a Davis® Weatherlink Web page. So, if that Web page HTML changes, the script can easily break. The scripts have been created for testing and personal use. The following modules have been imported into one or both scripts:

- `urllib3` module for server requests, including `PoolManager`
- `BeautifulSoup` class from `bs4` module
- `AsciiTable` class from `terminaltables` module

### Variables

- `http = urllib3.PoolManager()`: `urllib3`'s `PoolManager()` handles arbitrary server requests.
- `req = http.request("GET", "http://www.weatherlink.com/user/gooselakewx/index.php?view=summary&headers=0")`: the `GET` reqeust.

```
if req.status == 200:
    blob = req.data
else:
    print("Check req.status")
```

- the conditional statement above checks for `OK` connection status, or status `200`.
- `soup = BeautifulSoup(blob, "html.parser")`: for parsing HTML for text from elements. in this repo, most of which were `<td>` elements from tabular data.
- `f'{soup.select("td:nth-of-type(14)")[0].string}'`: in this _f-string_, the `select()` function is used to target a specific `<td>` element for its text `.string`.

```
table = AsciiTable(main_data)
r_table = AsciiTable(rainfall)
s_table = AsciiTable(soil)

print(table.table)
print(r_table.table)
print(s_table.table)
```

in the variables defined above, `AsciiTable()` class gets the data arrays and formats them into the three tables shown below:

![glw2]

[glw2]: https://github.com/nick3499/glw_weather/blob/master/glw_weather_2.png "Scraping Script v.2"
