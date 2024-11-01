import wget
import os
import logging
from time import sleep


def download(wget_uri, destination_file):
    i = 0
    max_attempts = 3
    while i < max_attempts:
        i += 1
        try:

            wget.download(wget_uri, str(destination_file))
            if os.path.exists(destination_file):
                return destination_file
            else:
                return ""
        except:
            logging.info(f"Download from cloud failed. Attempt {i} of {max_attempts}")
            sleep(0.05)
            continue

if __name__ == '__main__':
    lines = []
    with open('download_wget.txt', 'r') as file:
        lines = file.readlines()
    for url in lines:
        print('Downloading: ', url)
        dest = 'models/' + url.split('/')[-1].replace('\n', '')
        download(url, dest)

