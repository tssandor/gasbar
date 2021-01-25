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
        printout = "L: " + safe_cast(gaslow, str) + " | " + "A: " + safe_cast(gasavg, str) + " | " + "H: " + safe_cast(gashigh, str)
        print(printout)
    else:
        print("Gas invalid")

token = os.getenv('ETHERSCAN_TOKEN')
check_gas()