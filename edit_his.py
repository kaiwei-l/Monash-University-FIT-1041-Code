from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import urllib
import csv


def getStatus(url):
    global dateCollector
    html = "https://en.wikipedia.org" + url
    try:
        response = urlopen(html)
        bsObj = BeautifulSoup(response, "html.parser")
        target = bsObj.find("div", {"id": "mw-indicator-pp-default"}).img.attrs['alt']
        print(target)
        dateCollector.append(1)

    except AttributeError:
        print("Unprotected")
        dateCollector.append(0)


def getPages(url):
    global pages
    html = urlopen(url)
    bsObj = BeautifulSoup(
        html, "html.parser")
    try:
        for links in bsObj.find(attrs={'class': 'wikitable sortable'}).findAll("a", href=re.compile("^(/wiki/)((?!:).)*$")):
            pageUrl = links.attrs['href']
            pages.add(pageUrl)
    except AttributeError:
        print("Pages have all been found")


def getEdit(historyUrl):
    global dateCollector
    try:
        historyUrl = "https://en.wikipedia.org" + historyUrl
        html = urlopen(historyUrl)
        bsObj = BeautifulSoup(html, "html.parser")
        try:
            older = bsObj.find("a", {"class": "mw-nextlink"})
            olderUrl = older.attrs['href']

            for edit in bsObj.findAll("a", {"class": "mw-changeslist-date"}):
                editRecord = edit.get_text()
                dateCollector.append(editRecord)
                print(editRecord)

            getEdit(olderUrl)
        except AttributeError:
            for edit in bsObj.findAll("a", {"class": "mw-changeslist-date"}):
                editRecord = edit.get_text()
                dateCollector.append(editRecord)
                print(editRecord)

    except urllib.request.HTTPError:
        pass


pages = set()
main = "https://en.wikipedia.org/wiki/User:West.andrew.g/Popular_pages"
getPages(main)
count = 0

with open('date1.csv', 'a', newline='') as dateFile:
    dateWriter = csv.writer(dateFile)
    for page in pages:
        dateCollector = []
        print("\n" + page)
        count += 1
        print("Number of pages being printed: " + str(count))
        getStatus(page)
        page = page.replace("/wiki/", "")

        dateCollector.append(page)
        historyUrl = "/w/index.php?title=" + page + "&offset=&limit=5000&action=history"
        getEdit(historyUrl)

        dateWriter.writerow(dateCollector)
        dateCollector.clear()   # initialise date collector
