#Deploy to mmm
echo "Uploading files"
scp -r * pi@mm:/home/pi/setup
echo "Done"