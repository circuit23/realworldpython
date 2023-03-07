#! python3
# downloadXkcd.py - downloads every XKCD comic

import requests
import os
import bs4

url = 'https://xkcd.com'  # starting URL
os.makedirs('xkcd', exist_ok=True)  # store comics in .\xkcd
while not url.endswith('#'):
    # Download the page
    print(f'Downloading page {url}')
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    # TODO: Find the URL of the comic image
    # TODO: Download the image
    # TODO: Save the image to .\xkcd
    # TODO: Get the Prev button's URL.

print('Done.')
