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


def generate_data(x, RSS_to_json_url):

    url = RSS_to_json_url

    response = urllib.request.urlopen(url)
    data = json.loads(response.read());

    print('====== ' + data['status'] + ' ======')

    for item in data['items']:
        x.title.append(item['title'])
        x.URL.append(item['link'])
        x.description.append(item['description'])
        x.pubDate.append(item['pubDate'])


def check_for_company(company_name, list):
    filtered_list = [x for x in list if re.search(company_name, x)]
    for item in new_list:
        print(item)

def main():

    # creating object that stores the data from RSS feeds
    RSS_data = article_data(title_list,\
    URL_list,\
    description_list,\
    pubDate_list)


    for rss_url in RSS_data_list:
        generate_data(RSS_data, rss_url)


    #x = check_for_company("finance", RSS_data.title)
    print("title :", RSS_data.title)
    print("number of titles: ", len(RSS_data.title))

    #check_for_company(x, RSS_data.description)

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
