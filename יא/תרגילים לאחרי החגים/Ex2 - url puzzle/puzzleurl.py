# import os
# import re
import sys
# import urllib.request as req

"""Logpuzzle exercise
Given an apache logfile, find the puzzle urls and download the images.

Here's what a puzzle url looks like:
10.254.254.58 - - [06/Aug/2007:00:10:05 -0700] "GET /edu/python/images/puzzle/a-baaa.jpg HTTP/1.0" 200 2309 "-" "googlebot-mscrawl-moma (enterprise; bar-XYZ; foo123@google.com,foo123@google.com,foo123@google.com,foo123@google.com)"
"""


def read_urls_and_build_html(filename):
    """
    Returns a list of the puzzle urls from the given log file,
    extracting the hostname from the filename itself.
    Screens out duplicate urls and returns the urls sorted into
    increasing order.
    """
    # +++your code here+++


def main():

    args = sys.argv[1:]

    if not args:
        print('log file is missing...')
        print('usage: python puzzleurl.py logfile ')
        input()
        sys.exit(1)

    img_urls = read_urls_and_html_build(args[0])

    for x in img_urls:
        print(x)

  
if __name__ == '__main__':
    main()
