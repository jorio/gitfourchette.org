#! /bin/bash

set -e

newbook="$1"
oldbook="${1%.pdf}_OLD.pdf"
url="$2"

wget -q -O "$oldbook" "$url"
ls -l "$oldbook" "$newbook"

set +e  # let diff return non-zero

diff <(pdftotext "$oldbook" -) <(pdftotext "$newbook" -)
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
