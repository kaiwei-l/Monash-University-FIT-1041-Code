from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import json
import urllib
import csv

MAX_DEPTH = 5  # max depth that this code goes

def getView(newArticle, url, wide_lst):
    try:
        page = urlopen(url)
        string = page.read().decode('utf-8')
        jsonObj = json.loads(string)

        lst = [0] * 12
        for i in range(len(jsonObj.get("items")) - 1):  # sum daily view into year view
            time = jsonObj.get("items")[i].get("timestamp")
            year = time[0] + time[1] + time[2] + time[3]
            if year == '2015':
                if time[4] == '0':
                    index = int(time[5]) - 8
                else:
                    index = int(time[4] + time[5]) - 8
            else:
                if time[4] == '0':
                    index = 4 + int(time[5])
                else:
                    index = 4 + int(time[4] + time[5])

            lst[index] = lst[index] + jsonObj.get("items")[i].get("views")

        # print the date list in a readable format
        for i in range(0, 5):
            if lst[i] != 0:
                print("year: 2015 " + " Month: " + str(i + 8) + " page view: " + str(lst[i]))
        for j in range(5, 12):
            if lst[j] != 0:
                print("year: 2016 " + " Month: " + str(j - 4) + " page view: " + str(lst[j]))

        lst.insert(0, newArticle)  # insert classification information
        for i in range(len(wide_lst) - 1, -1, -1):
            lst.insert(0, wide_lst[i])

        with open('page_view_2.csv', 'a', newline='') as viewFile:
            viewWriter = csv.writer(viewFile)
            viewWriter.writerow(lst)

    except urllib.request.HTTPError:
        print("HTTP ERROR")
        pass


def pageGen(cateUrl, depth, cate_name):
    global pages
    global catesCollection
    global width
    cate = "https://en.wikipedia.org" + cateUrl
    try:
        htmlCate = urlopen(cate)
        cateObj = BeautifulSoup(htmlCate, "html.parser")
        try:
            c = cateObj.h1.get_text()
            print('\n-------Category---------')
            print(c)
            try:
                if depth == 0:
                    pass
                else:
                    # copy info in width into temporary list wide_lst
                    width[depth - 1] += 1  # add classification by one
                    wide_lst = []
                    for i in range(depth):
                        wide_lst.append(width[i])

                    while len(wide_lst) != 5:
                        wide_lst.append(0)

                    wide_lst.insert(depth - 1, cate_name)

                # process articles in each category page
                for articles in cateObj.find("div", {"id": "mw-pages"}).findAll("a", href=re.compile(
                        "^(/wiki/)((?!:).)*$")):
                    newArticle = articles.attrs['href']
                    if newArticle not in pages:
                        pages.add(newArticle)
                        print("\n\npages: " + str(newArticle))
                        print("Page depth: " + str(depth))
                        print("Page width: " + str(width[0]))
                        print("Pages being processed: " + str(len(pages)))
                        newArticle = newArticle.replace("/wiki/", "")
                        viewUrl = "http://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/en.wikipedia" \
                                  "/all-access/all-agents/" + newArticle + "/daily/2015080100/2016080100"
                        getView(newArticle, viewUrl, wide_lst)

            except AttributeError:
                print("there is no page under this category")

            if (depth + 1) > MAX_DEPTH:  # check depth
                return

            # go to category at the next depth
            for links in cateObj.find("div", {"id": "mw-subcategories"}).findAll("a", href=re.compile(
                    "^(/wiki/Category:).")):
                subCate = links.attrs['href']
                if subCate not in catesCollection:
                    catesCollection.add(subCate)
                    pageGen(subCate, depth + 1, str(subCate.replace("/wiki/Category:", "")))

        except AttributeError:      # no more subcategories, function returns
            print("this category has no subcategory")

    except urllib.request.HTTPError:
        print("HTTP Error")


pages = set()  # contains the page being visited
catesCollection = set()  # contains the categories being visited
mainCate = "/wiki/Category:Fundamental_categories"
width = [0, 0, 0, 0, 0]  # this list records the current class of each depth
pageGen(mainCate, 0, "foundation")
