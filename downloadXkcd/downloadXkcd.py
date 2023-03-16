#! python3
# downloadXkcd.py - downloads every XKCD comic

import os

import bs4
import requests

url = 'https://xkcd.com'  # starting URL
os.makedirs('xkcd', exist_ok=True)  # store comics in .\xkcd
while not url.endswith('#'):
    # Download the page
    print(f'Downloading page {url}...')
    res = requests.get(url, verify=False)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    # Find the URL of the comic image
    comicElem = soup.select('#comic img')
    if not comicElem:
        print('Could not find comic image.')
    else:
        comicUrl = 'https:' + comicElem[0].get('src')

        # Download the image
        print(f'Downloading image {comicUrl}...')
        res = requests.get(comicUrl, verify=False)
        res.raise_for_status()

        # Save the image to .\xkcd
        with open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb') as imageFile:
            for chunk in res.iter_content(100_000):
                imageFile.write(chunk)

    # Get the Prev button's URL.
    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'https://xkcd.com' + prevLink.get('href')

print('Done.')
