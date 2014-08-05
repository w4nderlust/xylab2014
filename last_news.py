# This script reads the last piece of news from a feed and outputs it with a json notation
# Usage:
# install pip
#  sudo easy_install pip
# install feedparser
#  sudo pip install feedparser
# run the script
#  python last_news.py "feed_url" > output_file

import sys
import re
import feedparser
from HTMLParser import HTMLParser

class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)

def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()

def main(rss_url):
	d = feedparser.parse(rss_url)
	if d.entries:
		post = d.entries[0]
		print '{'
		if hasattr(post, 'title'):
			print '\t' + '"title":"' + strip_tags(post.title).replace('"', '').strip() + '",'
		if hasattr(post, 'summary'):
			print '\t' + '"summary":"' + re.sub('\s+', ' ', strip_tags(post.summary)).replace('"', '').strip() + '",'
		if hasattr(post, 'content'):
			if len(post.content) > 0:
				print '\t' + '"content":"' + re.sub('\s+', ' ', strip_tags(post.content[0].value)).replace('"', '').strip() + '",'
		if hasattr(post, 'author'):
			print '\t' + '"author":"' + post.author + '",'
		if hasattr(post, 'published'):
			print '\t' + '"published":"' + post.published + '",'
		if hasattr(post, 'image'):
			print '\t' + '"image":"' + post.image + '",'
		print '}'


if __name__ == "__main__":
	if (len(sys.argv) > 0) :
		main(sys.argv[1])
	else:
		print 'Put an RSS Feed url as a parameter.'