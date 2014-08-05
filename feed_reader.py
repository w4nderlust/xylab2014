# This scripts takes a list of RSS feeds and 2 strings
# and outputs two lists of sentences inside the news from the feeds
# that contains the strings
# Usage:
# install pip
#  sudo easy_install pip
# install feedparser
#  sudo pip install feedparser
# run the script
#  python feed_reader.py > output_file

import sys
import re
import feedparser
from HTMLParser import HTMLParser

feeds = [
	"http://feeds.arstechnica.com/arstechnica/everything",
	"http://rss.slashdot.org/Slashdot/slashdot",
	]

string_1 = "crypto"
string_2 = "google"

sentence_finder = re.compile(r'([A-Z][^\.!?]*[\.!?])\s+', re.M)

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

def main(rss_urls):
	sentences_1 = []
	sentences_2 = []
	for rss_url in rss_urls:
		d = feedparser.parse(rss_url)
		if d.entries:
			for post in d.entries:
				if hasattr(post, 'title'):
					titolo = strip_tags(post.title)
					sentences = sentence_finder.findall(titolo)
					for sentence in sentences:
						print sentence
						if string_1.lower() in sentence.lower():
							sentences_1.append(sentence)
						if string_2.lower() in sentence.lower():
							sentences_2.append(sentence)
				if hasattr(post, 'summary'):
					riassunto = re.sub('\s+', ' ', strip_tags(post.summary)).strip()
					sentences = sentence_finder.findall(riassunto)
					for sentence in sentences:
						if string_1.lower() in sentence.lower():
							sentences_1.append(sentence)
						if string_2.lower() in sentence.lower():
							sentences_2.append(sentence)
				if hasattr(post, 'content'):
					if len(post.content) > 0:
						articolo = re.sub('\s+', ' ', strip_tags(post.content[0].value)).strip()
						sentences = sentence_finder.findall(articolo)
						for sentence in sentences:
							if string_1.lower() in sentence.lower():
								sentences_1.append(sentence)
							if string_2.lower() in sentence.lower():
								sentences_2.append(sentence)
	print string_1 + ":"
	for sentence in sentences_1:
		print sentence
	print ""
	print string_2 + ":"
	for sentence in sentences_2:
		print sentence

if __name__ == "__main__":
	main(feeds)