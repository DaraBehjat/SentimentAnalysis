
import feedparser

# Input RSS URL for specfic news source 
python_reuters_rss_url = "http://feeds.reuters.com/reuters/companyNews" 

# Input RSS feed name for specific news source
feed = feedparser.parse( python_reuters_rss_url )

entries_feed = feed['entries']


def create_link_list(t):
	"""Function that creates a list of links from RSS feed.
	
	t: list

	returns: list of 25 most recent links given by RSS feed. 
	"""
	link_list = []
	for i in range(len(t)):
		temp_d = entries_feed[i]
	
		summary = temp_d['links']
		summary_d = summary[0]

		link = summary_d['href']
		link_list.append(link)
	
	return link_list
	
links = create_link_list(entries_feed)

print links

