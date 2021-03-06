#!/usr/bin/python
import gpod
import os
import shutil
import re

database = gpod.Database('/mnt/ipod')
master = database.get_master()
print 'Id', master.get_id()
print 'Master ', master.get_master()
print 'Order ', master.order

cnt = 0
size = 0
g = 1
for track in database:
	if re.match('.*\.mp3$',track.ipod_filename()):
		cnt+=1
		size += os.path.getsize(track.ipod_filename())
		#print track.artist, track.ipod_filename()
		folder = "./music/{0}/{1}/".format(track['artist'],track['album'])
		if not os.path.exists(folder):
			os.makedirs(folder)
		shutil.copy(track.ipod_filename(), "./music/{0}/{1}/{2}.mp3".format(track['artist'],track['album'],re.sub(r"\/",'_',track['title'])))
		print "copied {0}/{1}/{2}.mp3".format(track['artist'],track['album'],track['title'])
		print "copied",size/1024/1024,"MB so far"
print 'There are', cnt,'songs on the IPOD summing up',size,'bytes.'
