import argparse
from modules import webget

from modules.webget import download
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="A program that downloads")
    parser.add_argument('url', help='The URL to download from')
    parser.add_argument('--destination', help='The place you want to save the file')
    args=parser.parse_args()

    if args.destination == None:
        destination = args.url.replace('https://', '').strip('.com') + '.dat'
        webget.download(args.url, destination)
    else:
        webget.download(args.url, args.destination)

    