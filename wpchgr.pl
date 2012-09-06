#!/usr/bin/perl

## by gnomeye

use v5.14;
use strict;
use warnings;
use LWP::Simple;
use File::Copy;

# variables
my $URL='http://wallbase.cc/random/all/eqeq/1920x1080/0/100/32';
my $finder='http://wallbase.cc/wallpaper/';
my $filepath='/tmp/wall.jpg';
my $archive='/media/exthome/img/wallpapers/wallbase/';

sub randomwall{
	## get random first wallpaper on site
my $resp = get($URL);
if ($resp =~ m/<a href="($finder\d*)"/){
	return get($1);}}

sub wallurl{
	my $wallresp=randomwall();
	my $count=1; ## try 3 times...
	## test if it is a valid jpg url if not get new randomurl
	until ($wallresp =~ m/<img src="(http:.*wallpaper-\d*.jpg)"/ or $count > 3){
		sleep 3;
		++$count;
		my $wallresp=randomwall();}
	$wallresp =~ m/<img src="(http:.*wallpaper-\d*.jpg)"/;
		return $1;} ## return jpg url

sub getimg{
	my $wpurl=wallurl();
	## get img from web
	getstore($wpurl,$filepath);
	## copy to archive 
	copy($filepath,$archive.'wallbase-'.substr($wpurl,-10));
	## use favorit wpsetter to set wp
	system('export DISPLAY=:0.0 ; feh --bg-scale --no-fehbg '.$filepath);
#	system('sh ~/.fehbg');
}

getimg();
