#!/usr/bin/env python3
import requests
import datetime
import time

while True:
    time.sleep(240)
    print(str(datetime.datetime.now()) + ": Calling Azure Function: https://vwsfunction.azurewebsites.net/api/alexapy")
    requests.get("https://vwsfunction.azurewebsites.net/api/alexapy")
    