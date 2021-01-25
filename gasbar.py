#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import requests
from requests.exceptions import HTTPError

def safe_cast(val, to_type, default=None):
    try:
        return to_type(val)
    except (ValueError, TypeError):
        print("Type error")

def check_gas():
    valid_gas = False
    try:
        api_url = "https://api.etherscan.io/api?module=gastracker&action=gasoracle&apikey=" + token
        response = requests.get(api_url)
        response.raise_for_status()
        # access JSOn content
        jsonResponse = response.json()

        if jsonResponse["message"] == "OK":
            gaslow = safe_cast(jsonResponse["result"]["SafeGasPrice"], int)
            gasavg = safe_cast(jsonResponse["result"]["ProposeGasPrice"], int)
            gashigh = safe_cast(jsonResponse["result"]["FastGasPrice"], int)
        
        if (gaslow <= gasavg <= gashigh) and (gaslow > 0):
            valid_gas = True

    except HTTPError as http_err:
        print('HTTP error')
    except Exception as err:
        print('Other error')

    if valid_gas:
        # adding in nice icon
        gas_icon = "iVBORw0KGgoAAAANSUhEUgAAAD4AAAA7CAYAAAAjDDn3AAAEqUlEQVRoge2a21MaVxzHf4sQFlgQCRdRawTRSKfQjr3YzHTajJlekk4asZm2dqbT+tKnPvc5/U/60mmTmcboQ6xtJ7HTTNKxMW0gRlNviVjUiCIg7ILV7ZytyQi7B5cFlKV8Zxjg/M7l99k957dnzzlQVVVVVbQIHBzLsoLpSZrxRKIxf5KmgWHSwIJwPjFSKZWg02rAoNeFjQaD5SAvdF7g4fUI+zAYglR6q7hOEAB2qxnsNssRUq0ubuW4NnGGbPDH4XV2en6hpM6YjAZwtzmxPjGplCowOZ2OxRPQ6XVv1dUajkhtSxR4gqY9E1Mz/q1/tqW2I1rO5kZ05wX9ujj4A/tHYIr7bTYZ4bOPetA3liGXFGIyra5FDgQaKbSyKpg+8WDmKTRww24Dvv7uCvqWFGREgSeTtJS6JYlJpSFJ057sstvbO7zqCoEX1dXH/fdZ5FC24vEExBMJyZAN9VbBdLfLAaa62gzf0Pi+ODiSnvxrjpdfSrcXBX777gQrFMln5xfgvoAjYnX27ZOCOY+3HgOzqY7nG80w5ktDP64WA15UVy8XaUgy/MF7b1nc7U6eR/l2e1mBwx74464Wni0feNmBwy78s+2tgrYn8OsbUX5Q2iNZgu8nBD80MqrKla0iwZGmpue5oIyzVyw4cJOeWaytosGXV8JYW0WDR6IxrE224LV6qqDysgWvt5nDCkLSixkn2YIbDXpL14teyeWVhTTe6mjmPoel7tdeGQiGln2LoZW8PZB1cNNTut7+vh5vV6cH1Or8FmNkH9V1Gk3Ad+YU8eUX/d6W5kbR5SrmcYYuAJnHXa/o53gu/W/BC4rqpdK1G2OQTm+xdpsF7DYzNDXUDxgoXW8xmytL8NW1CAT/XoZ7UzPcf0qn9Z175yTrcbdLn7FkSRZdfTORhG++vwqXhkbYzWTSV4w6ZTXG7/gn4afRW5eLUVdZgquUKsDNw8fuBGByek76TuWuynKM977bDSSp7l0MrVy++vOvaN/uqQ0RXxm+Bo7mRlUhG4xl29UprXagw+UgPv/k/IWjdbUZtmhsEwXAnIuJ+6nsxzil03516vVXeelLmD02sZJFcGsU2GpayrGsJEayACdJtT87jUmlCqqzOlcvZykIAr9OLEE0wxCyAEcLDpROm5EWzFp1QdvIoaXHWeUyyyB9OzBcoyFJVjZd3Wo2ZfwPr0Xg1vhdFgGjz2/j/nRsM3Ovvt7KP0jV5zvNHe0oywmMkNqcx2Du0WKGZXD4Ovxy83Z6Z3sHsqGRmhps8t9C6ur0eI+ajLz0jWhcENpo0MOJl57HzutlA67VkIGzb74BypqaffOiWX7P6W4wULrzuDyyepx1tDmI/r4eoHQabB50pz/98ByXN1ddBZ2BKZVwZ2CeCJ2w/PPeA/SWBiiSU5SWC2RNdiucePkFUas12MpHb/7OXr8xBkKnnQ5CyDFnyzPw8ftnvGgFtdhNYrv6YULD7uvn7MMgzMwt8KarxRAW/DCh96pUflTn6jyDojyuiUJRtIXVzHpxhuc6XCVpMB+RajW4HM0leZzkfJw9WgwJnmE9CBH/nXW9gFZgDsWBqqqqSr4CgH8BOcG/44Zsca8AAAAASUVORK5CYII="
        printout = "L: " + safe_cast(gaslow, str) + " | " + "A: " + safe_cast(gasavg, str) + " | " + "H: " + safe_cast(gashigh, str)
        printout = "{\"text\":\"" + printout + "\", \"icon_data\": \"" + gas_icon + "\"}"
        print(printout)
    else:
        print("Gas invalid")

token = os.getenv('ETHERSCAN_TOKEN')
check_gas()