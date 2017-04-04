import json
import datetime
from datetime import tzinfo,timedelta

all_title = []
count = {}

class Zone(tzinfo):
    def __init__(self,offset,isdst,name):
        self.offset = offset
        self.isdst = isdst
        self.name = name
    def utcoffset(self, dt):
        return timedelta(hours=self.offset) + self.dst(dt)
    def dst(self, dt):
            return timedelta(hours=1) if self.isdst else timedelta(0)
    def tzname(self,dt):
         return self.name

GMT = Zone(0,False,'GMT')
EST = Zone(-5,False,'EST')

def date_from_webkit(timestamp):
	epoch_start = datetime.datetime(1970,1,1)
	delta = datetime.timedelta(microseconds=int(timestamp))

	_time = epoch_start + delta

	t = _time.replace(tzinfo=GMT)
	est_time = t.astimezone(EST)
	print est_time


with open('BrowserHistory.json') as data_file:
	data = json.load(data_file)

	for item in data['Browser History']:
		url = item['url'].encode('utf-8')
		title = item['title'].encode('utf-8')
		timestamp = item['time_usec']

		epoch_start = datetime.datetime(1970,1,1)
		delta = datetime.timedelta(microseconds=int(timestamp))

		_time = epoch_start + delta
		t = _time.replace(tzinfo=GMT)
		est_time = t.astimezone(EST)

		title = str(est_time)[11:-13] + " " + title

		if "youtube.com" in url:
			all_title.append(title)
			sorted_time = sorted(all_title)

	for title in sorted_time:
		print title
