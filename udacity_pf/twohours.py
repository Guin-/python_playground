# Wait 2 hours
# Open browser with url
# repeat


import time
import webbrowser

breakcount = 0
print ("This program started" + time.ctime())
while breakcount <=2:
	time.sleep(7200) 
	webbrowser.open("www.youtube.com")
	breakcount += 1

