# encoding=utf8 
#!/usr/bin/python
import requests
from bs4 import BeautifulSoup
import time
from fake_useragent import UserAgent
import urllib2
import cookielib
import getLocCooKie

userIds='orPQ800sg4nMZkuMKxH01LiFpNxsyvWM148v64'

cookiestr = getLocCooKie.getcookies()
#req = urllib2.Request('https://www.hostloc.com/forum.php?mod=forumdisplay&fid=45&filter=author&orderby=dateline',
#  headers = {"Referer": "http://www.baidu.com",
#    "User-Agent": ua.random
#})
#html = urllib2.urlopen(url = req, timeout = 10).read()


#print 'aaaaaa' + html
def getcookies():
    url = 'https://www.hostloc.com/forum.php?mod=forumdisplay&fid=45&filter=author&orderby=dateline'
    cj = cookielib.CookieJar();
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj));
    urllib2.install_opener(opener);
    resp = urllib2.urlopen(url);
    cookiestr = ''
    for cookie in cj:
        cookiestr = cookiestr + cookie.name + '=' + cookie.value + ';'
        #print cookie.name + '=' + cookie.value;
    print cookiestr
    return cookiestr + 'L7FW=d5d738a47ddb2a78ddb4ce3421bdedb2'
def getnewesttitle2():
    ub = UserAgent()
    useragent = ub.random
    
    url = 'https://www.hostloc.com/forum.php?mod=forumdisplay&fid=45&filter=author&orderby=dateline'
    #headers = {"Referer": "http://www.baidu.com",'user-agent':ua.random}
    #cookiestr = 'hkCM_2132_forum_lastvisit=D_45_1559556616;hkCM_2132_lastact=1559556616%09forum.php%09forumdisplay;hkCM_2132_lastvisit=1559553016;hkCM_2132_saltkey=T944U51f;hkCM_2132_sid=VpB29Z;hkCM_2132_st_t=0%7C1559556616%7C7c8bb3e469e57cba3fe85b5a611cb06c;hkCM_2132_visitedfid=45;'
    #cookiestr = 'hkCM_2132_saltkey=PbbSrztz; hkCM_2132_lastvisit=1559528181; L7FW=ddc7d358eacabd48205e5b675a32e8b8; hkCM_2132_auth=7493XPtMDME6u3z5mt74BTT%2BMQtY14Y0Thd%2Bt1kbVgPZoPZi9jGqNH92xXJ8fMpRexJtkNpqCeSltnpHDdFDW%2FBa1A; hkCM_2132_lastcheckfeed=33410%7C1559531798; hkCM_2132_connect_is_bind=0; hkCM_2132_nofavfid=1; hkCM_2132_visitedfid=45; hkCM_2132_smile=1D1; hkCM_2132_home_diymode=1; hkCM_2132_ulastactivity=6eccDcOLmol8Cs0%2F4lKVoHmcummeuik8a94L1%2F5SnWyPgAyLV4pl; hkCM_2132_viewid=tid_554024; hkCM_2132_sid=pRFyEn; hkCM_2132_lip=112.224.70.56%2C1559548905; hkCM_2132_sendmail=1; hkCM_2132_st_t=33410%7C1559549193%7C5e956c1f6b015aded0bd3ac5ac297004; hkCM_2132_forum_lastvisit=D_45_1559549193; hkCM_2132_noticeTitle=1; hkCM_2132_st_p=33410%7C1559549221%7C706100ad6ad419e5b925b9636a00276c; hkCM_2132_lastact=1559549390%09misc.php%09patch'
    cookiestr = 'L7FW=d5d738a47ddb2a78ddb4ce3421bdedb2'
    req = urllib2.Request(url,headers= {"Referer": "http://www.baidu.com",'Cookie': cookiestr,"User-Agent": useragent})
    r = urllib2.urlopen(url = req, timeout = 10).read()
    
    print useragent
 
    soup = BeautifulSoup(r,'html.parser')
    
    #print soup
    newest = soup.find('th',class_='new')
    newtitle = newest.text.replace('New','').replace(unicode('预览',"utf-8"),'').strip()
    #print newtitle
    #print newest
    #print newest.text.strip()
    tidstr = newest.__str__()
    
    pid = tidstr[tidstr.find('tid')+4:tidstr.find('tid')+10]
    post_url = "https://www.hostloc.com/thread-{}-1-1.html".format(pid)

    #print post_url
    print ('monitor is runing ,please wait for a monent')

    resultArr = [newtitle,post_url]
    return resultArr

def getnewesttitle():
    
    url = 'https://www.hostloc.com/forum.php?mod=forumdisplay&fid=45&filter=author&orderby=dateline'
    headers = {"Referer": "http://www.baidu.com",'Cookie': cookiestr,'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.76 Mobile Safari/537.36'}
    
    #headers = {'user-agent':UserAgent().random}
    
    requests.adapters.DEFAULT_RETRIES = 5
    s = requests.session() 
    s.keep_alive = False
    r = s.get(url, headers=headers)

    #print r.text
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
