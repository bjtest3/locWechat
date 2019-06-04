# encoding=utf8 
#!/usr/bin/python
import js2py
import requests
import re

#pip install js2py
def getcookies():
    url = 'https://www.hostloc.com/forum.php?mod=forumdisplay&fid=45&filter=author&orderby=dateline'
    js=js2py.EvalJs()
    headers = {"Referer": "http://www.baidu.com",'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.76 Mobile Safari/537.36'}

    aesjs=requests.get("https://www.hostloc.com/aes.min.js",headers=headers,timeout=5).text
    print aesjs
    js.execute(aesjs)
    getcookie=requests.get(url).text
    #print getcookie
    getcookie_script=re.findall("<script>(.*?)</script>",getcookie)
    js.execute(getcookie_script[0].split("document")[0])
    data=js.toHex(js.slowAES.decrypt(js.c, 2, js.a, js.b))
    cookie="L7FW="+data 
    print cookie 
    return cookie

#print getcookies()
