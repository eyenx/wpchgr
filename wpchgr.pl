#!/usr/bin/perl

use v5.14;
use strict;
use warnings;
use LWP::Simple;
use File::Copy;
use MIME::Base64;

#my $URL='http://wallbase.cc/random/all/eqeq/1920x1080/0/100/32';
my $URL="http://wallbase.cc/random?section=wallpapers&q=&res_opt=eqeq&res=1920x1080&thpp=32&purity=100&board=21&aspect=0.00";
my $finder='http://wallbase.cc/wallpaper/';
my $filepath='/tmp/wall.jpg';
my $archive='/media/exthome/img/wallpapers/wallbase/';

# get random first wallpaper
sub randomwall{
my $resp = get($URL);
if ($resp =~ m/<a href="($finder\d*)"/){
	return get($1);}}
# new b64 decoding
sub b64url{
	my $wallurl=randomwall();
	$wallurl =~ m/.*src\=.*\+B\(\'(.*)\'\)\+.*/;
	return decode_base64($1);
}
# w/o decoding
sub jpgurl{
  my $wallurl=randomwall();
  $wallurl =~ m/.*src\=\"(http:\/\/wallpapers.wallbase.cc\/.*)\" class/;
  return $1;
}
# get decoded url, test if jpg and return it - if not jpg redo the process (max of 3 times)
sub wallurl{
  #my $wurl=b64url();
  my $wurl=jpgurl();
	my $count=1;
	until ($wurl =~ /http\:.*wallpaper\-\d*.jpg/ or $count > 3){
		sleep 3;
		++$count;
#		my $wurl=b64url();}
		my $wurl=jpgurl();}
	return $wurl;
}

# get final the image and store it. also put it as wallpaper
sub getimg{
	my $wpurl=wallurl();
	getstore($wpurl,$filepath);
	copy($filepath,$archive.'wallbase-'.substr($wpurl,-10));
	system('export DISPLAY=:0.0 ; feh --bg-scale --no-fehbg '.$filepath);
#	system('sh ~/.fehbg');
}
getimg();
