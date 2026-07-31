#! /bin/bash

set -e

newbook="$1"
oldbook="${1%.pdf}_OLD.pdf"
url="$2"
skiplines=8  # ignore changes in date or version on the title page

wget -q -O "$oldbook" "$url"
ls -l "$oldbook" "$newbook"

set +e  # let diff return non-zero

diff <(pdftotext "$oldbook" - | tail -n +$skiplines) \
     <(pdftotext "$newbook" - | tail -n +$skiplines)
diffresult=$?

set -e

if [ $diffresult -eq 0 ]
then
    echo "Keeping old book PDF (similar enough to ours)"
    mv -v "$oldbook" "$newbook"
else
    echo "Keeping new book PDF (our contents have diverged from live version)"
    rm -v "$oldbook"
fi
