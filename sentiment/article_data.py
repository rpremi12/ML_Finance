# creates article_data class
class article_data:

    # self denotes this object itself
    def __init__(self, title, URL, description, pubDate):
        self.title = title
        self.URL = URL
        self.description = description
        self.pubDate = pubDate
        self.total =1

    # official string representitle_listation to make it look better in console
    #instead of showing where it's stored in memory
    def __repr__(self):
        return "(%s, %s, %s, %s)" \
        % (self.title, \
        self.URL, \
        self.description, \
        self.pubDate)

    # define equality
    # compares objects and see when they're equal
    def __eq__(self, other):
        return type(other) == type(self) \
        and self.URL == other.URL \


