#!/usr/bin/env python3

import requests

def scrape():
    link_list = []
    r = requests.get("https://ditkalamazoo.squarespace.com/shows")
    for line in r.text.split('\n'):
        if 'href="http://www.google.com/calendar/event?action=TEMPLATE' in line:
            link_list.append(line)
    return link_list

def apply(INIT_LIST):
    #at this point, we just need to hit the links in the list


if __name__ == "__main__":
    print(scrape())
