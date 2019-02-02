from eventregistry import *

# creates RSSdata
class RSSdata:

    # self denotes this object itself
    def __init__(self, article, headline, short_descriptor, exact_time_released, view_count):
        self.article = article
        self.headline = headline
        self.short_descriptor = short_descriptor
        self.exact_time_released = exact_time_released
        self.view_count = view_count


    # official string representation to make it look better in console
    #instead of showing where it's stored in memory
    def __repr__(self):
        return "(%s, %s, %s, %s, %s)" \
        % (self.article, \
        self.headline, \
        self.short_descriptor, \
        self.exact_time_released, \
        self.view_count)

    # define equality
    # compares objects and see when they're equal
    def __eq__(self, other):
        return type(other) == RSSdata \
        and self.article == other.article \
        and self.headline == other.headline \
        and self.short_descriptor == other.short_descriptor \
        and self.exact_time_released == other.exact_time_released \
        and self.view_count == other.view_count \

def generate_numbers(x):
    return x

def scrape_data(data_type, data_list, size_of_list):
    '''
    Arg: data_type, data_list, size_of_list
    data_type = which type of data is going to be stored, eg. article names or date released
    data_list = the list where the data is going to be stored
    size_of_list  = the amount of each type of data that is being stored

    purpose: generate the lists of each type of data that is needed for the language processing


    use this to get data from websites:

    curl -v "https://streamdata.motwin.net/https://api.rss2json.com/v1/api.json?rss_url=https%3A%2F%2Ftechcrunch.com%2Ffeed%2F&streamId={your_feedly_stream_id}&X-Sd-Token={your_streamdata_token}"

    command = "curl -d " + '"text='+desc + '" http://text-processing.com/api/sentiment/ >  data.txt'
    os.system(command)
    print(command)

    f = open("data.txt","r")
    result = f.readline().strip()

    https://proxy.streamdata.io/http://stockmarket.streamdata.io/prices/

    https://api.rss2json.com/v1/api.json?rss_url=https%3A%2F%2Fnews.ycombinator.com%2Frss
    https://rss2json.com/docs
    https://rss2json.com/rss-to-json-api-python-example

    data key for newsapi: 62ace5950cb941f2aaa5f96ce645bdf8
    '''

    for index in range(size_of_list):
        data_list.append(generate_numbers(index))
    return data_list


def main():
    test_article_list = []
    test_headline_list = []
    test_short_descriptor_list = []
    test_exact_time_released_list = []
    test_view_count_list = []

    article = "some keywords"

    testRSSdata = RSSdata(test_article_list, test_headline_list, test_short_descriptor_list, test_exact_time_released_list, test_view_count_list)

    testRSSdata.article = scrape_data(article, test_article_list, 20)

    import requests

    url = ('https://newsapi.org/v2/everything?'
           'q=Apple&'
           'from=2019-02-02&'
           'sortBy=popularity&'
           'apiKey=62ace5950cb941f2aaa5f96ce645bdf8')

    response = requests.get(url)

    print(r.json)

if __name__ == '__main__':
    #main() function above will be called when this file is the top level code.
    main()
