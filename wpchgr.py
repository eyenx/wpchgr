#!/usr/bin/python

## this script downloads a random wallpaper from http://wallbase.net. Standard Resolution = 1920 x 1080 FullHD

import os,sys,time,subprocess,urllib.request,re

# variables

site = 'http://wallbase.cc/random/all/eqeq/1920x1080/0/100/32'
op = 35
op2 = 11
op3 = 4
finder = 'http://wallbase.cc/wallpaper/'
defdir='/tmp/wall.jpg'
archive='/media/exthome/img/wallpapers/wallbase/'

def getimghtml():
	html = urllib.request.urlopen(site)
	pat=re.compile(".*\"(http:\/\/wallbase.cc\/wallpaper\/[0-9]+)\"")
	for line in html.readlines():
		line=str(line)
		if pat.match(line):
			mtch=pat.search(line)
			res=mtch.group(1)
			break
	imghtml=urllib.request.urlopen(res)
	pat=re.compile(".*img src\=\"(http.*wallpaper\-[0-9]+\.jpg)\".*")
	for line in imghtml.readlines():
		line=str(line)
		if pat.match(line):
			mtch=pat.search(line)
			res=mtch.group(1)
			break
	return(res)




def getit(url):
	img=urllib.request.urlopen(url)
	arch=open(archive+'wallbase-'+url[-10:],'wb')
	arch.write(img.read())
	arch.close()
	arch=open(archive+'wallbase-'+url[-10:],'rb')
	wall=open(defdir,'wb')
	wall.write(arch.read())
	wall.close()
	arch.close()
	subprocess.Popen('DISPLAY=:0.0 feh --bg-scale '+defdir,shell=True)

	

def testimghtml():
	text = getimghtml()
	while '.jpg' not in text:
		text=getimghtml()
	getit(text)

testimghtml()
