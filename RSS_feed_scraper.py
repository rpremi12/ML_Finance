# import functions
import urllib.request
import json
import re
from article_data import *

# declaring data
RSS_data_list = ["https://api.rss2json.com/v1/api.json?rss_url=https%3A%2F%2Fwww.reddit.com%2Fr%2Ffinance%2F.rss&api_key=aonvwfrfutzuxjksa4uabvwta72ctveswdfk2hoi&count=100", "https://api.rss2json.com/v1/api.json?rss_url=http%3A%2F%2Fwww.wsj.com%2Fxml%2Frss%2F3_7014.xml&api_key=aonvwfrfutzuxjksa4uabvwta72ctveswdfk2hoi&count=100", "https://api.rss2json.com/v1/api.json?rss_url=http%3A%2F%2Fwww.wsj.com%2Fxml%2Frss%2F3_7031.xml&api_key=aonvwfrfutzuxjksa4uabvwta72ctveswdfk2hoi&count=100", "https://api.rss2json.com/v1/api.json?rss_url=http%3A%2F%2Fwww.wsj.com%2Fxml%2Frss%2F3_7455.xml&api_key=aonvwfrfutzuxjksa4uabvwta72ctveswdfk2hoi&count=100", "https://api.rss2json.com/v1/api.json?rss_url=https%3A%2F%2Fwww.reddit.com%2Fr%2Fwallstreetbets%2F.rss&api_key=aonvwfrfutzuxjksa4uabvwta72ctveswdfk2hoi&count=100", "https://api.rss2json.com/v1/api.json?rss_url=http%3A%2F%2Frss.cnn.com%2Frss%2Fmoney_topstories.rss&api_key=aonvwfrfutzuxjksa4uabvwta72ctveswdfk2hoi&count=100", "https://api.rss2json.com/v1/api.json?rss_url=http%3A%2F%2Frss.nytimes.com%2Fservices%2Fxml%2Frss%2Fnyt%2FBusiness.xml&api_key=aonvwfrfutzuxjksa4uabvwta72ctveswdfk2hoi&count=100", "https://api.rss2json.com/v1/api.json?rss_url=http%3A%2F%2Ffeeds.reuters.com%2Freuters%2FbusinessNews&api_key=aonvwfrfutzuxjksa4uabvwta72ctveswdfk2hoi&count=100", "https://api.rss2json.com/v1/api.json?rss_url=http%3A%2F%2Ffeeds.reuters.com%2Freuters%2FcompanyNews&api_key=aonvwfrfutzuxjksa4uabvwta72ctveswdfk2hoi&count=100", "https://api.rss2json.com/v1/api.json?rss_url=http%3A%2F%2Ffeeds.reuters.com%2Fnews%2Fwealth&api_key=aonvwfrfutzuxjksa4uabvwta72ctveswdfk2hoi&count=100", "https://api.rss2json.com/v1/api.json?rss_url=http%3A%2F%2Ffeeds.reuters.com%2Freuters%2FtopNews&api_key=aonvwfrfutzuxjksa4uabvwta72ctveswdfk2hoi&count=100", "https://api.rss2json.com/v1/api.json?rss_url=http%3A%2F%2Ffeeds.reuters.com%2FReuters%2FdomesticNews&api_key=aonvwfrfutzuxjksa4uabvwta72ctveswdfk2hoi&count=100", "https://api.rss2json.com/v1/api.json?rss_url=http%3A%2F%2Ffeeds.marketwatch.com%2Fmarketwatch%2Frealtimeheadlines%2F&api_key=aonvwfrfutzuxjksa4uabvwta72ctveswdfk2hoi&count=100", "https://api.rss2json.com/v1/api.json?rss_url=http%3A%2F%2Ffeeds.marketwatch.com%2Fmarketwatch%2Fmarketpulse%2F&api_key=aonvwfrfutzuxjksa4uabvwta72ctveswdfk2hoi&count=100", "https://api.rss2json.com/v1/api.json?rss_url=http%3A%2F%2Ffeeds.marketwatch.com%2Fmarketwatch%2Fbulletins&api_key=aonvwfrfutzuxjksa4uabvwta72ctveswdfk2hoi&count=100", "https://api.rss2json.com/v1/api.json?rss_url=https%3A%2F%2Fengagedscholarship.csuohio.edu%2Frobinhood%2Frecent.rss&api_key=aonvwfrfutzuxjksa4uabvwta72ctveswdfk2hoi&count=100"]


def generate_list_of_articles(RSS_to_json_url):

    articles = []

    for i in RSS_to_json_url:


        response = urllib.request.urlopen(i)
        data = json.loads(response.read());

        print('====== ' + data['status'], "for one RSS feed" + ' ======')

        for item in data['items']:

            # note: you can create objects anywhere like in functions without having to initalize them first
            articles.append(article_data(item['title'],\
            item['link'],\
            item['description'],\
            item['pubDate']))

    return articles

def check_for_company(keyword, unfiltered_list):
    final_list = []
    old_list = unfiltered_list
    new_list = [x for x in old_list if re.search(keyword, str(x).lower())]
    for item in new_list:
        final_list.append(item)

    return final_list

def main():
    test = input("Enter company name: ")

    article_list = generate_list_of_articles(RSS_data_list)

    filtered_list = check_for_company(test.lower(), article_list)

    #print(type(str(article_list[0])))
    print(filtered_list)
    print("number of articles found: ", len(filtered_list))

    '''
    final_list = []
    old_list = ['abc123', 'def456', 'ghi789', '123abc1231312', 'abc12312123']
    new_list = [x for x in old_list if re.search('abc', x)]
    for item in new_list:
        final_list.append(item)
    print(final_list)
    '''

if __name__ == '__main__':
    #main() function above will be called when this file is the top level code.
    main()
