#	Nabeel Ansari
#	MET-Lab Research Assistant
#	6/24/2014
#	mtkSlurp.py - Outputs a list of download URL's for full multi-track sessions from Mixing Secrets additional resources.

import os
import re
import urllib
import urllib2
from HTMLParser import HTMLParser

class mtkDownloader(HTMLParser):
	def __init__(self, outFile):
		self.out = outFile
	def handle_starttag(self, tag, attrs):
		if tag == "a" and len(attrs) == 1:
			attr = attrs[0]
			if attr[0] == "href":
				match = re.search("("+mtkFilePattern+"|"+mp3FilePattern+")", attr[1])
				if match is not None:
					fname = match.group(0)
					if not os.path.isfile(fname): 
						self.out.write(attr[1]+"\n")
	def handle_endtag(self, tag):
		return
	def handle_data(self, data):
		return

mtkWebsite = "http://www.multitracks.cambridge-mt.com/"
mp3Website = "http://www.previews.cambridge-mt.com/"
mtkFilePattern = "((?<=" + mtkWebsite + ").*Full\.zip)"
mp3FilePattern = "((?<=" + mp3Website + ")((.*_Full_Preview\.mp3)|(.*_Remix\.mp3)))"

directory = "./"
print "Writing all files URL's into a file in: ", directory
if not os.path.exists(directory):
	os.makedirs(directory)

file = open(directory + "/mtkDownloadList.txt", "wb")
page = urllib.urlopen("http://www.cambridge-mt.com/ms-mtk.htm")
scanner = mtkDownloader(file)
scanner.feed(page.read())
page.close()
file.close()
