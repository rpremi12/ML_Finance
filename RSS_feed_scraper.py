# import functions
import urllib.request
import json
import re
from article_data import *

# declaring data
RSS_data_list = ["https://api.rss2json.com/v1/api.json?rss_url=https%3A%2F%2Fwww.reddit.com%2Fr%2Ffinance%2F.rss&api_key=aonvwfrfutzuxjksa4uabvwta72ctveswdfk2hoi&count=100", "https://api.rss2json.com/v1/api.json?rss_url=http%3A%2F%2Fwww.wsj.com%2Fxml%2Frss%2F3_7014.xml&api_key=aonvwfrfutzuxjksa4uabvwta72ctveswdfk2hoi&count=100", "https://api.rss2json.com/v1/api.json?rss_url=http%3A%2F%2Fwww.wsj.com%2Fxml%2Frss%2F3_7031.xml&api_key=aonvwfrfutzuxjksa4uabvwta72ctveswdfk2hoi&count=100", "https://api.rss2json.com/v1/api.json?rss_url=http%3A%2F%2Fwww.wsj.com%2Fxml%2Frss%2F3_7455.xml&api_key=aonvwfrfutzuxjksa4uabvwta72ctveswdfk2hoi&count=100" ]


def generate_list_of_articles(RSS_to_json_url):

    articles = []

    for i in RSS_to_json_url:


        response = urllib.request.urlopen(i)
        data = json.loads(response.read());

        print('====== ' + data['status'] + ' ======')

        for item in data['items']:

            # note: you can create objects anywhere like in functions without having to initalize them first
            articles.append(article_data(item['title'],\
            item['link'],\
            item['description'],\
            item['pubDate']))

    return articles

def check_for_company(company_name, list):
    filtered_articles = []
    filtered_list = [x for x in list if re.search(company_name, x)]

    for item in new_list:
        filtered_articles.append(item)

def main():

    article_list = generate_list_of_articles(RSS_data_list)
    print(article_list)
    print("number of articles: ", len(article_list))


if __name__ == '__main__':
    #main() function above will be called when this file is the top level code.
    main()
