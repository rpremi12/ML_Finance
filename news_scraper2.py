from article_data import *
from sentiment.sentiment import sent
from RSS_feed_scraper import *

from newsapi import NewsApiClient
import json
import csv
import os
import math
from time import gmtime, strftime, localtime
import sys

# string -> float
# description -> score

def add_article(art1, titl, desc ):
    return article_data(art1.title + titl, art1.URL, art1.description+desc, art1.pubDate, art1.total +1 )

def tot_sent(art1):
    return (0.4* art1.title + 0.6 * art1.description ) / art1.total


def scrape(q=None, language=None, country=None, category=None, sources=None, from_param=None, to=None, pageSize=None,
           page=None, long=False, h_balance=0.5):
    newsapi = NewsApiClient(api_key='2d4d70291f5548bb8c6776f5ddeefd25')

    everything = newsapi.get_everything(q=q, language=language,  sort_by= "popularity", sources=sources,
                                        page_size=20, page=page, from_param="2019-01-29", to=to)

    # to = '%4d-%02d-%02dT%02d:%02d:%02d' % (year, month, day, hour, minute, second)
    # from_param = '%4d-%02d-%02dT%02d:%02d:%02d' % (year, month, yesterday, hour, minute, second)

    every_parsed = json.dumps(everything, ensure_ascii=False)
    every_data = everything['articles']

    # print(strftime("%Y-%m-%dT%H:%M:%S" , (localtime()-86400)))
    csv_name = "CSVs/" + q + "-" + str((strftime("%Y-%m-%d-%H:%M:%S", localtime()))) + ".csv"

    every_data_file = open(csv_name, "w")

    csvwriter = csv.writer(every_data_file)

    count = 0

    total = 0
    smallest_date = 99999999
    articles = dict()
    print("loading sentiment")
    for i in every_data:

        if count == 0:
            header = list(i.keys())

            lst2 = ["sentiment"]
            header.extend(lst2)

            csvwriter.writerow(header)

            count += 1

        total += 1

        t_score =sent(i['title'])
        d_score = sent(i['description'])
        t_url = (i['url'])
        time_score= (i['publishedAt'])
        key = int(time_score[:10].replace("-",""))
        #print(key)

        if smallest_date > key:
            smallest_date = key
        #print(smallest_date)

        if(articles.get(key) == None):
            articles[key] = article_data(t_score, t_url, d_score, time_score)
        else:
            articles[key] = add_article(articles[key], t_score, d_score)

    total_score = 0
    for art in sorted(articles):
        total_score = tot_sent(articles[art])
        total+=1
    news_score = total_score /total

    '''
    article_list = generate_list_of_articles(RSS_data_list)

    filtered_list = check_for_company(q.lower(), article_list)

    total_score = 0
    total =0

    for art in sorted(articles):
        total_score = tot_sent(articles[art])
        total+=1
    # print(type(str(article_list[0])))
    rss_score = (total_score / total)
    print( total_score, rss_score)
    '''

    every_data_file.close()
    return (news_score )

def main():
    test = scrape("Tesla", category="business", language="en")

if __name__ == "__main__":
    main()
