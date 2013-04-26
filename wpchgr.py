#!/usr/bin/python

## this script downloads a random wallpaper from http://wallbase.net. Standard Resolution = 1920 x 1080 FullHD
## by gnomeye

import subprocess,urllib.request,re,base64

# variables

site = 'http://wallbase.cc/random/all/eqeq/1920x1080/0/100/32'
op = 35
op2 = 11
op3 = 4
finder = 'http://wallbase.cc/wallpaper/'
defdir='/tmp/wall.jpg'
archive='/media/exthome/img/wallpapers/wallbase/'

def getimghtml():
	## read first random url page
	html = urllib.request.urlopen(site)
	pat=re.compile(".*\"(http:\/\/wallbase.cc\/wallpaper\/[0-9]+)\"")
	h=html.read().decode()
	mtch=pat.search(h)
	res=mtch.group(1)
	imghtml=urllib.request.urlopen(res)
	## search for complete jpg url path and decode (base64)
	pat=re.compile(".*src\=.*\+B\(\\\'(.*)\\\'\)\+.*")
	ih=imghtml.read().decode()
	mtch=pat.search(ih)
	res=base64.b64decode(mtch.group(1)).decode()
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
	subprocess.Popen('DISPLAY=:0.0 feh --bg-scale '+defdir,shell=True)

	

def testimghtml():
	text = getimghtml()
	## just test if valid jpg url - if not try again
	while '.jpg' not in text:
		text=getimghtml()
	getit(text)

if __name__ == '__main__':
    testimghtml()
