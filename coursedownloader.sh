#!/bin/bash 
php codecourse download:course responsive-css-sticky-footer
echo
echo -n '************************************************************'
echo
echo 'processing.... next course'
sleep 5s
echo
php codecourse download:course regular-expressions-basics
echo
echo -n '************************************************************'
echo
echo 'processing.... next course'
sleep 5s
echo
php codecourse download:course git-and-github
echo
echo -n '************************************************************'
echo
echo 'processing.... next course'
sleep 5s
echo
php codecourse download:course html5-input-types
echo
echo -n '************************************************************'
echo
echo 'processing.... next course'
sleep 5s
echo
echo -n press Enter or cmd to exit 
read terminate