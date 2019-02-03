# import functions
import urllib.request
import json

# making empty list
article_list = []
headline_list = []
URL_list = []
test_short_descriptor_list = []
test_exact_time_released_list = []

# declaring data
url = "https://api.rss2json.com/v1/api.json\
?rss_url=http%3A%2F%2Fwww.reddit.com%2F.rss\
&api_key=aonvwfrfutzuxjksa4uabvwta72ctveswdfk2hoi\
&order_by=pubDate&order_dir=desc&count=25"
api_key = "aonvwfrfutzuxjksa4uabvwta72ctveswdfk2hoi"
response = urllib.request.urlopen(url)
data = json.loads(response.read());

# creates RSSdata
class RSSdata:

    # self denotes this object itself
    def __init__(self, article_title, headline, URL, short_descriptor, exact_time_released):
        self.article_title = article_title
        self.headline = headline
        self.URL = URL
        self.short_descriptor = short_descriptor
        self.exact_time_released = exact_time_released


    # official string representation to make it look better in console
    #instead of showing where it's stored in memory
    def __repr__(self):
        return "(%s, %s, %s, %s, %s)" \
        % (self.article, \
        self.headline, \
        self.URL, \
        self.short_descriptor, \
        self.exact_time_released)

    # define equality
    # compares objects and see when they're equal
    def __eq__(self, other):
        return type(other) == RSSdata \
        and self.article == other.article \
        and self.headline == other.headline \
        and self.URL == other.URL \
        and self.short_descriptor == other.short_descriptor \
        and self.exact_time_released == other.exact_time_released


    '''

    purpose: generate the lists of each type of data that is needed for the language processing

    f = open("data.txt","r")
    result = f.readline().strip()

    data key for newsapi: 62acetest_article_list5950cb941f2aaa5f96ce645bdf8

    make

    '''

def check_for_company(company_name, list): # eg. check_for_company("Google", reddit_RSS_data.article_title)
    company_name = str(company_name)
    


def main():

    reddit_RSS_data = RSSdata(article_list,\
    headline_list,\
    URL_list,\
    test_short_descriptor_list,\
    test_exact_time_released_list)

    for item in data['items']:
        reddit_RSS_data.article_title.append(item['title'])
        reddit_RSS_data.exact_time_released.append(item['pubDate'])
        reddit_RSS_data.short_descriptor.append(item['description'])
        reddit_RSS_data.URL.append(item['link'])

    print('====== ' + data['status'] + ' ======')

    for index in range(25):
        print("Title: ",reddit_RSS_data.article_title[index])
        print("Time: ",reddit_RSS_data.exact_time_released[index])
        #print(reddit_RSS_data.short_descriptor[index])
        print("URL: ",reddit_RSS_data.URL[index])
        print()


if __name__ == '__main__':
    #main() function above will be called when this file is the top level code.
    main()
