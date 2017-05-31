# index.py
# Created by: Zied Guesmi
# A program that allow scraping all pages of a web site recursively

from lxml import html
import requests

ENTRY_POINT = ''
VISITED_PAGES = []
HOSTNAME = 'https://www.example.com'
ROUTE = '/index'
URL = HOSTNAME + ROUTE

def main():
    # main


# scrap the page given as parameter and extract all links (<a> tags) and do
#the same for these links.
def get_hyperlinks_from_page(page):
    global URL
    html_page = requests.get(URL + page)
    tree = html.fromstring(html_page.content)
    return tree.xpath('//@href')


def get_all_divs(page):
    global URL
    html_page = requests.get(URL + page)
    tree = html.fromstring(html_page.content)
    return tree.xpath('//div')


def get_div_by_id(page [,id]):
    global URL
    html_page = requests.get(URL + page)
    tree = html.fromstring(html_page.content)
    return tree.xpath('//div[@id=' + id + ']')


def get_div_by_class(page [,class]):
    global URL
    html_page = requests.get(URL + page)
    tree = html.fromstring(html_page.content)
    return tree.xpath('//div[@class=' + class + ']')


# tree.xpath('//div/font/text()')
# def scrap(page):
#     # global secrets
#     global VISITED_PAGES
#     if (len(links) == 0):
#         return
#     else:
#         for page in links:
#             if (page not in visited_pages):
#                 visited_pages.append(page)
#                 scrap(page)
#
# secrets = list(set(secrets))
