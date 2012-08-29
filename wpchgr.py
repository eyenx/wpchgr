#!/usr/bin/python

## this script downloads a random wallpaper from http://wallbase.net. Standard Resolution = 1920 x 1080 FullHD

import os,sys,time,subprocess,urllib.request

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
	text = html.read()
	text = str(text)
	pos = text.index(finder)
	wallurl = text[pos:pos+op]
	imghtml = urllib.request.urlopen(wallurl)
	imgtext = imghtml.read()
	imgtext = str(imgtext)
	return(imgtext)

def getit(url):
	subprocess.call(['wget',url,'-O',archive+'wallbase-'+url[-10:]],shell=False)
	subprocess.call(['cp',archive+'wallbase-'+url[-10:],defdir],shell=False)
	subprocess.Popen('DISPLAY=:0.0 feh --bg-scale '+defdir,shell=True)

def testimghtml():
	text = getimghtml()
	while '.jpg' not in text:
		text=getimghtml()
	point=text.index('.jpg')
	stop=text[point-100:point+4].index('http://')
	url=(text[point-100:point+4][stop:])
	getit(url)

testimghtml()
