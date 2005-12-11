#!/bin/sh
# location for irssi themes
url='http://www.irssi.org/themefiles/'

# this script must reside inSOURCES dir
set -e
dir=$(dirname "$0")
cd "$dir"
cd ../SOURCES # this makes sure we're in right place
top=$(pwd)

snap=$(date +%Y%m%d)
if [ ! -f irssi-themes-$snap.tar.bz2 ]; then
	tmpd=$(mktemp -d ${TMPDIR:-/tmp}/irssiXXXXXX)
	cd $tmpd
	mkdir irssi-themes-$snap
	cd irssi-themes-$snap
	wget -r -np -l1 -nH --cut-dirs=1 -A theme $url
	rmdir irssi-themes-$snap 2>/dev/null || :
	cd ..
	tar cjf $top/irssi-themes-$snap.tar.bz2 irssi-themes-$snap
	cd $top
	rm -rf $tmpd
fi
