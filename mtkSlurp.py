#	Nabeel Ansari
#	MET-Lab Research Assistant
#	6/24/2014
#	mtkSlurp.py - Downloads full multi-track sessions from Mixing Secrets additional resources.

import os
import re
import urllib
from HTMLParser import HTMLParser

mtkWebsite = "http://www.multitracks.cambridge-mt.com/"
mp3Website = "http://www.previews.cambridge-mt.com/"
mtkFilePattern = "((?<=" + mtkWebsite + ").*_Full\.zip)"
mp3FilePattern = "((?<=" + mp3Website + ")((.*_Full_Preview\.mp3)|(.*_Remix\.mp3)))"

directory = "ms-mtk-downloads/"
print "Downloading all files to directory: ", directory
if not os.path.exists(directory):
	os.makedirs(directory)
file = open(directory + "/mtkLog.txt", "a")

class mtkDownloader(HTMLParser):
	def handle_starttag(self, tag, attrs):
		if tag == "a" and len(attrs) == 1:
			attr = attrs[0]
			if attr[0] == "href":
				match = re.search("("+mtkFilePattern+"|"+mp3FilePattern+")", attr[1])
				if match is not None:
					fname = match.group(0)
					urllib.urlretrieve(attr[1], directory+"/"+fname)
					print "File downloaded: ", fname 
					file.write("File downloaded: " + fname)
	def handle_endtag(self, tag):
		return
	def handle_data(self, data):
		return

page = urllib.urlopen("http://www.cambridge-mt.com/ms-mtk.htm")
scanner = mtkDownloader()
scanner.feed(page.read())
page.close()
file.close()
