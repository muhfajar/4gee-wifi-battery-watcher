#!/usr/bin/python

import sys
import time
import pync
import random
import requests


def main():
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

            if json_data['bat_level'] <= 1:
                pync.notify("Low battery, please plug in the AC adapter!\n(click to see detail)",
                            open="http://192.168.1.1/index.html")
            time.sleep(60)
        except KeyboardInterrupt:
            pync.notify("Watcher closed")
            sys.exit()


if __name__ == "__main__":
    main()
