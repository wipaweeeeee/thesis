import json
from datetime import datetime,tzinfo,timedelta

all_time = []

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

with open('watch-history.json') as data_file:
	data = json.load(data_file)

	for item in data:
		title = item['snippet']['title'].encode('utf-8')
		time = item['snippet']['publishedAt'].encode('utf-8')[11:-5]
		t = datetime.strptime(time,'%H:%M:%S')
		t = t.replace(tzinfo=GMT)

		time_transpose = str(t.astimezone(EST))[11:-6] + " " + title
		# print time_transpose

		all_time.append(time_transpose)
		sorted_time = sorted(all_time)

	for item in sorted_time:
		print item
