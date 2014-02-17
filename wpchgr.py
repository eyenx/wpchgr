#!/usr/bin/python

## this script downloads a random wallpaper from http://wallbase.net. Standard Resolution = 1920 x 1080 FullHD
## by gnomeye

import subprocess,urllib.request,re,base64

# variables

#site = 'http://wallbase.cc/random/all/eqeq/1920x1080/0/100/32'
site="http://wallbase.cc/random?section=wallpapers&q=&res_opt=eqeq&res=1920x1080&thpp=32&purity=100&board=21&aspect=0.00"
finder = 'http://wallbase.cc/wallpaper/'
defdir='/tmp/wall.jpg'
archive='/media/exthome/img/wallpapers/wallbase/'

def getimghtml():
	## read first random url page
  reqsite=urllib.request.Request(site)
  html = urllib.request.urlopen(reqsite)
  pat=re.compile(".*\"(http:\/\/wallbase.cc\/wallpaper\/[0-9]+)\"")
  h=html.read().decode()
  mtch=pat.search(h)
  res=mtch.group(1)
  reqres=urllib.request.Request(res)
  imghtml=urllib.request.urlopen(reqres)
	## search for complete jpg url path and decode (base64)
  #pat=re.compile(".*src\=.*\+B\(\\\'(.*)\\\'\)\+.*") ## no more b64
  pat=re.compile(".*src\=\"(http:\/\/wallpapers.wallbase.cc\/.*)\" class")
  ih=imghtml.read().decode()
  mtch=pat.search(ih)
  #res=base64.b64decode(mtch.group(1)).decode()
  res=mtch.group(1)
  return(res)




def getit(url):
	## get img in bytes
  requrl=urllib.request.Request(url)
  img=urllib.request.urlopen(requrl)
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



if __name__ == '__main__':
	text = getimghtml()
	## just test if valid jpg url - if not try again
	while '.jpg' not in text:
		text=getimghtml()
	getit(text)
