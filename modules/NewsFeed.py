# NewsFeed.py
from Cheetah.Template import Template
import file_utils
import json


class Feed:
    def __init__(self, title, url):
        self.title = title
        self.url = url

class NewsFeed:
    def __init__(self, config):
        self.config = config
        self.position = config.get('position')
        feeds = config.get('selected_feeds')
        NYFeed = {}
        NYFeed["title"] = "New York Times"
        NYFeed["url"] = "http://www.nytimes.com/services/xml/rss/nyt/HomePage.xml"
        BBCFeed = {}
        BBCFeed["title"] = "BBC"
        BBCFeed["url"] = "http://feeds.bbci.co.uk/news/video_and_audio/news_front_page/rss.xml?edition=us"
        self.feed_list = []
        if "New York Times" in feeds:
            self.feed_list.append(NYFeed)
        if "BBC" in feeds:
            self.feed_list.append(BBCFeed)



    def to_config(self) -> str:
        templateDef = file_utils.readFile("templates/newsfeed.template")
        template = Template(templateDef)
        template.position = self.position
        template.feeds = json.dumps(self.feed_list)
        return template

    def add_custom_feed(self, config):
        custom_feed_title = config.get('custom_feed')
        custom_feed_url = config.get('custom_feed_url')
        
        custom_feed = {}
        custom_feed["title"] = custom_feed_title
        custom_feed["url"] = custom_feed_url
        self.feed_list.append(custom_feed)

