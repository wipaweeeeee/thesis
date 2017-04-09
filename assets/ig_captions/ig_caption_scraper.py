import urllib
import json
import sys

handle = sys.argv[1]
base_url = "https://www.instagram.com/"
url = base_url + handle + "/media/"

def grab_caption(url):
	raw = urllib.urlopen(url).read()
	data = json.loads(raw)
	last_item = len(data["items"])
	last_url = data["items"][last_item - 1]["id"]

	for caption in data["items"]:
		try:
			print (caption["caption"]["text"]).encode('utf-8')
		except:
			pass

	if data["more_available"]:
		next_url = "https://www.instagram.com/" + handle + "/media/?max_id=" + last_url
		grab_caption(next_url)

grab_caption(url)
