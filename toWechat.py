# encoding=utf8 
#!/usr/bin/python
import requests
from bs4 import BeautifulSoup
import time

#update your userids 
userIds='orPQ800sg4nMZkuMKxH01LiFpNxsyvWM149999'

def getnewesttitle():
    url = 'https://www.hostloc.com/forum.php?mod=forumdisplay&fid=45&filter=author&orderby=dateline'
    headers = {'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.76 Mobile Safari/537.36'}

    requests.adapters.DEFAULT_RETRIES = 5
    s = requests.session() 
    s.keep_alive = False
    r = s.get(url, headers=headers)

    soup = BeautifulSoup(r.text,'html.parser')
    newest = soup.find('span',class_='by')
    
    pid = r.text[r.text.find('tid')+4:r.text.find('tid')+10]
    post_url = "https://www.hostloc.com/thread-{}-1-1.html".format(pid)

    #print post_url
    print ('monitor is runing ,please wait for a monent')

    resultArr = [newest.parent.text,post_url]
    return resultArr

def sendmessage(newesttitle,postUrl): 
    finalUrl = 'http://wxmsg.dingliqc.com/send?msg='+ newesttitle +'&userIds=' + userIds  + '&url=' + postUrl
    
    requests.adapters.DEFAULT_RETRIES = 5
    s = requests.session() 
    s.keep_alive = False
    s.get(finalUrl)       
    
    print('send a new message to wechat')

firstArr = getnewesttitle()
newesttitle = firstArr[0]
sendmessage(firstArr[0],firstArr[1])
while True:
    try:
        time.sleep(30)  
        try:
          newArr = getnewesttitle()
        finally:
          time.sleep(5)  
          pass
        thenexttitle = newArr[0]
        postUrl = newArr[1]
        print('monitoring...')
        print 'old message is ' + newesttitle.encode('utf-8')
        print 'new message is ' + thenexttitle.encode('utf-8')
        print postUrl.encode('utf-8')
        if thenexttitle != newesttitle:
            newesttitle = thenexttitle
            print('find new message ,reading....')           
            sendmessage(thenexttitle,postUrl)
            
            pass
        else:
            pass
    except RuntimeError:
        print(RuntimeError)
    pass     
