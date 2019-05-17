# locWechat
#关注微信公共账号 wxpusher

![](https://i.loli.net/2019/05/09/5cd3c47b19e8d.jpg)

```
左下角获取你的userids

```
#记得修改userids为你的
```
脚本toWechat.py  第8行
userIds='orPQ800sg4nMZkuMKxH01LiFpNxsyvWM149999'
```

#安装beautifulsoup
```
wget https://www.crummy.com/software/BeautifulSoup/bs4/download/4.5/beautifulsoup4-4.5.1.tar.gz

tar xvzf beautifulsoup4-4.5.1.tar.gz
cd beautifulsoup4-4.5.1

python setup.py install
```
or use this way
```
pip install beautifulsoup4
```

#安装request
```
pip install request
```

#下载脚本执行，执行前记得修改userids<br>
**hostloc.com**
```
wget https://raw.githubusercontent.com/bjtest3/locWechat/master/toWechat.py

python toWechat.py
```
**zuanke8.com**
```
wget https://raw.githubusercontent.com/bjtest3/locWechat/master/zkbWechat.py

python zkbWechat.py
```
***脚本跑十几小时就会挂，用这个脚本守护一下***
```
vi listen.sh
chmod +x listen.sh
```
<br>
```
#!/bin/sh
# `默认shell执行需要的内容`

# `环境变量重新生效`
source /etc/profile

# `判断进程是否存在，记得使用grep -v 排除gerp进程`
retDesc=`ps -ef | grep "toWechat" | grep -v grep`
retCode=$?
# `判断是否不为0，不为0就重新启动服务器，为0就说明服务器存在`
if [ ${retCode} -ne 0 ]; 
    then
    echo "`date` restart" >> /root/wechatlisten.log 
    nohup python /root/toWechat.py & 
else
    echo "server on"
fi
```

***加入到定时任务***
```
crontab -e
*/1 * * * * /root/listen.sh
```
