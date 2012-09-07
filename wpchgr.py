#!/usr/bin/python

## this script downloads a random wallpaper from http://wallbase.net. Standard Resolution = 1920 x 1080 FullHD
## by gnomeye

import os,sys,time,subprocess,urllib.request,re

# variables

site = 'http://wallbase.cc/random/all/eqeq/1920x1080/0/100/32'
defdir='/tmp/wall.jpg'
archive='/media/exthome/img/wallpapers/wallbase/'

def getimghtml():
	## read first random url page
	html = urllib.request.urlopen(site)
	pat=re.compile(".*\"(http:\/\/wallbase.cc\/wallpaper\/[0-9]+)\"")
	for line in html.readlines():
		line=str(line)
		if pat.match(line):
			mtch=pat.search(line)
			res=mtch.group(1)
			## get first wallpaper url and break loop
			break
	imghtml=urllib.request.urlopen(res)
	## search for complete jpg url path
	pat=re.compile(".*img src\=\"(http.*wallpaper\-[0-9]+\.jpg)\".*")
	for line in imghtml.readlines():
		line=str(line)
		if pat.match(line):
			mtch=pat.search(line)
			res=mtch.group(1)
			break
	return(res)




def getit(url):
	## get img in bytes
	img=urllib.request.urlopen(url)
	imgb=img.read()
	## open archive and write bytes into it
	arch=open(archive+'wallbase-'+url[-10:],'wb')
	arch.write(imgb)
	arch.close()
	## open wallpaper dir (defdir) and write same bytes into it
	wall=open(defdir,'wb')
	wall.write(imgb)
	wall.close()
	## start subprocess with your favorite wpsetter.
	subprocess.Popen('DISPLAY=:0.0 feh --bg-scale --no-fehbg '+defdir,shell=True)

	

def testimghtml():
	text = getimghtml()
	## just test if valid jpg url - if not try again
	while '.jpg' not in text:
		text=getimghtml()
	getit(text)

testimghtml()
