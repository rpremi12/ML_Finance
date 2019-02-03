# import functions
import urllib.request
import json
import re

# making empty list
title_list = []
URL_list = []
description_list = []
pubDate_list = []

# declaring data
RSS_data_list = ["https://api.rss2json.com/v1/api.json?rss_url=https%3A%2F%2Fwww.reddit.com%2Fr%2Ffinance%2F.rss&api_key=aonvwfrfutzuxjksa4uabvwta72ctveswdfk2hoi&count=100", "https://api.rss2json.com/v1/api.json?rss_url=http%3A%2F%2Fwww.wsj.com%2Fxml%2Frss%2F3_7014.xml&api_key=aonvwfrfutzuxjksa4uabvwta72ctveswdfk2hoi&count=100", "https://api.rss2json.com/v1/api.json?rss_url=http%3A%2F%2Fwww.wsj.com%2Fxml%2Frss%2F3_7031.xml&api_key=aonvwfrfutzuxjksa4uabvwta72ctveswdfk2hoi&count=100", "https://api.rss2json.com/v1/api.json?rss_url=http%3A%2F%2Fwww.wsj.com%2Fxml%2Frss%2F3_7455.xml&api_key=aonvwfrfutzuxjksa4uabvwta72ctveswdfk2hoi&count=100" ]

# creates RSSdata
class article_data:

    # self denotes this object itself
    def __init__(self, title, URL, description, pubDate):
        self.title = title
        self.URL = URL
        self.description = description
        self.pubDate = pubDate


    # official string representation to make it look better in console
    #instead of showing where it's stored in memory
    def __repr__(selshort_descriptorf):
        return "(%s, %s, %s, %s)" \
        % (self.title, \
        self.URL, \
        self.description, \
        self.pubDate)

    # define equality
    # compares objects and see when they're equal
    def __eq__(self, other):
        return type(other) == RSSdata \
        and self.title == other.title \
        and self.URL == other.URL \
        and self.description == other.description \
        and self.pubDate == other.pubDate

def generate_data(RSS_URL):

    url = RSS_URL

    response = urllib.request.urlopen(url)
    data = json.loads(response.read());

    print('====== ' + data['status'] + ' ======')

    for item in data['items']:
        RSS_data.title.append(item['title'])
        RSS_data.URL.append(item['link'])
        RSS_data.description.append(item['description'])
        RSS_data.pubDate.append(item['pubDate'])


def check_for_company(company_name, list): # eg. check_for_company("Google", reddit_RSS_data.artishort_descriptorcle_title)
    new_list = [x for x in list if re.search(company_name, x)]
    for item in new_list:
        print(item)

def main():

    RSS_data = article_data(title_list,\
    URL_list,\
    description_list,\
    pubDate_list)

    for data in RSS_data_list:
        generate_data(data)

    x = "finance"
    check_for_company(x, RSS_data.title)
    check_for_company(x, RSS_data.description)


    '''
    for index in range(25):
        print("Title: ",reddit_RSS_data.article_title[index])
        print("Time: ",reddit_RSS_data.exact_time_released[index])
        #print(http://www.wsj.com/public/page/rss_news_and_feeds.htmlreddit_RSS_data.short_descriptor[index])
        print("URL: ",reddit_RSS_data.URL[index])
        print()
    '''



if __name__ == '__main__':
    #main() function above will be called when this file is the top level code.
    main()
