#!/usr/bin/env sh

set -e

radius=20

infile="$1"
outfile="$2"
tempfile1="/tmp/$(basename "$infile" .png)-1.png"
tempfile2="/tmp/$(basename "$infile" .png)-2.png"
tempfile3="/tmp/$(basename "$infile" .png)-3.png"

[ -z "$infile" ] && exit 1
[ -z "$outfile" ] && exit 1

w=$(magick identify -format "%w" "$infile")
h=$(magick identify -format "%h" "$infile")
echo $w,$h

magick "$infile" \
  \( +clone  -alpha extract \
    -draw "fill black polygon 0,0 0,$radius $radius,0 fill white circle $radius,$radius $radius,0" \
    \( +clone -flip \) -compose Multiply -composite \
    \( +clone -flop \) -compose Multiply -composite \
  \) -alpha off -compose CopyOpacity -composite \
  "$tempfile1"

magick "$tempfile1" \
  -fill transparent -stroke '#808080' -strokewidth 1 \
  -draw "roundrectangle 0,0   $(($w-1)),$(($h-1))   $radius,$radius" \
  "$tempfile2"

magick "$tempfile2" \
  \( +clone  -background black  -shadow 40x12-0+10 \) +swap \
  -background none -layers merge  +repage  "$tempfile3"

#pngcrush -ow "$outfile"
pngquant --nofs - <"$tempfile3" >"$outfile"
