#!/usr/bin/python

import sys
import time
import pync
import random
import requests


def main():
    log_status = 0
    while True:
        try:
            headers = {
                'Connection': 'keep-alive',
                'Pragma': 'no-cache',
                'Cache-Control': 'no-cache',
                'Accept': 'application/json, text/javascript, */*; q=0.01',
                'X-Requested-With': 'XMLHttpRequest',
                'Content-Type': 'application/x-www-form-urlencoded',
                'Origin': 'http://192.168.1.1',
                'Referer': 'http://192.168.1.1/index.html',
                'Accept-Language': 'en-US,en;q=0.9,ko;q=0.8,id;q=0.7',
            }

            params = (
                ('rand', random.random()),
            )

            data = {
                'd': '1'
            }

            response = requests.post('http://192.168.1.1/goform/getImgInfo',
                                     headers=headers, params=params, data=data, verify=False)
            json_data = response.json()

            if log_status == json_data['bat_level']:
                time.sleep(60)
                continue

            switcher = {
                1: "Low battery, please plug in the AC adapter!",
                2: "Battery level 25%",
                3: "Battery level 75%",
                4: "Battery full, please disconnect the AC adapter!",
            }

            msg = switcher.get(json_data['bat_level'], "Unknown battery level")
            print(msg)
            pync.notify("{msg}\n(click to see detail)".format(msg=msg), open="http://192.168.1.1/index.html",
                        appIcon="img/{level}.png".format(level=json_data['bat_level']), title='4Gee Wifi Mini')
            log_status = json_data['bat_level']
        except KeyboardInterrupt:
            pync.notify("Watcher closed")
            sys.exit()


if __name__ == "__main__":
    main()
