# -*- coding:utf-8 -*- 
import urllib
import urllib2
#### url = "https://passport.baidu.com/v2/?login"
##page = 1
####===============use POST way to login====================
##url = "https://passport.baidu.com/v2/?login"
##values = {"username": "kinsco163@163.com", "password": "XXXX"}
##try:
##    data = urllib.urlencode(values)
##    request = urllib2.Request(url, data)
##    response = urllib2.urlopen(request)
##    print response.read()
##except urllib2.URLError, e:
##    if hasattr(e, "code"):
####        print e.code
##        print 233
##    if hasattr(e, "reason"):
##        print 233
####        print e.reason
##
##
####print response
##
####================use GET way to login====================
##print "use GET way : \n"
##data = urllib.urlencode(values)
##url = "http://passport.csdn.net/account/login"
##url = url + "?" + data
##request = urllib2.Request(url)
##response = urllib2.urlopen(request)
####print data
##
####========================================================
##enable_proxy = True
##proxy_handler = urllib2.ProxyHandler({"http":"http://202.116.76.22:8080"})
##null_proxy_handler = urllib2.ProxyHandler({})
##if enable_proxy:
##    opener = urllib2.build_opener(proxy_handler)
##else:
##    opener = urllib2.build_opener(null_proxy_handler)
##urllib2.install_opener(opener)
##url = "https://passport.csdn.net/account/login"
##
####==============DEBUG LOG==================================
##print 'DEBUG LOG:'
####declare: httpHandler, httpsHandler
####return: opener, response
####method: build_opener, install_opener, urlopen
##httpHandler = urllib2.HTTPHandler(debuglevel=1)
##httpsHandler = urllib2.HTTPSHandler(debuglevel=1)
##opener = urllib2.build_opener(httpHandler, httpsHandler)
##urllib2.install_opener(opener)
##response = urllib2.urlopen('http://www.baidu.com')
##
##===============query gaokao grade==========================
##import requests
##import re
##import cookielib
##url="http://www.sneac.com/gkcjcx/2011zcjcx_jg.jsp?wbtreeid=3063"
##user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
##values={'wbzkzh':'0904150001','wbsfzh':'612422199810290027'}
##header={'User-Agent':user_agent,'Connection':'Keep-alive','Referer': 'http://www.sneac.com/gkcxx/cjcx/zcjcx.htm'}
##data=requests.post(url,data=values,headers=header)
###reg=r'<td\s\w+=.\w+.\w+=.+?>(.*?)</td>'
##reg1=r'<td\s\w+=.\w+.+?>(.*?)</td>'
##data2=re.findall(reg1,data.text)
##print("\n".join(data2))
##================google =========================
##
##url = "http://www.baidu.com"
##request = urllib2.Request(url)
##try:
##    response = urllib2.urlopen(request)
##except urllib2.HTTPError, e:
####    print e.code
####    print e.reason
##    print "heheda"
##except urllib2.URLError, e:
##    print "233"
##else:
##    print 'ok'
####
##cookie = cookielib.CookieJar()
##handler = urllib2.HTTPCookieProcessor(cookie)
##opener = urllib2.build_opener(handler)
##response = opener.open("http://www.baidu.com")
##
##i = 1
##for item in cookie:
##    print str(i) + ' Name = ' + item.name
##    print str(i) + ' Value = ' + item.value
##    i = i + 1

## ====================Cookie====================
##gradeUrl = 'http://jwxt.sdu.edu.cn:7890/pls/wwwbks/bkscjcx.curscopre'
###请求访问成绩查询网址
##result = opener.open(gradeUrl)
##print result.read()
##
##filename = "cook.txt"
##cookie = cookielib.MozillaCookieJar(filename)
##urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
##postdata = urllib.urlencode({
##        'stuid': '2012',
##        'pwd': '2333'
##        })
##loginurl = 'http://jwxt.sdu.edu.cn:7890/pls'
##result = opener.open(loginurl, postdata)
##cookie.save(ignore_discard = True, ignore_expires = True)
##
##================================================
##import cookielib
##filename = 'cookie.txt'
###声明一个MozillaCookieJar对象实例来保存cookie，之后写入文件
##cookie = cookielib.MozillaCookieJar(filename)
###cookie->handler->opener->response
###通过handler来构建opener; HTTPCookieProcessor return a handler of cookie
##opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
###创建一个请求，原理同urllib2的urlopen
##response = opener.open("http://www.baidu.com")
###保存cookie到文件
##cookie.save(ignore_discard=True, ignore_expires=True)
##
###创建MozillaCookieJar实例对象
####cookie = cookielib.MozillaCookieJar()
#####从文件中读取cookie内容到变量
####cookie.load('cookie.txt', ignore_discard=True, ignore_expires=True)
#####创建请求的request
##req = urllib2.Request("http://www.baidu.com")
###利用urllib2的build_opener方法创建一个opener
##opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
##response = opener.open(req)
####print response.read()
##import cookielib
####cookie->opener->gradeurl,+result
###声明一个MozillaCookieJar对象实例来保存cookie，之后写入文件
##cookie = cookielib.MozillaCookieJar(filename)
##opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
##postdata = urllib.urlencode({
##            'stuid':'201200131012',
##            'pwd':'23342321'
##        })
###登录教务系统的URL
##loginUrl = 'http://jwxt.sdu.edu.cn:7890/pls/wwwbks/bks_login2.login'
###模拟登录，并把cookie保存到变量
##result = opener.open(loginUrl,postdata)
###保存cookie到cookie.txt中
####cookie.save(ignore_discard=True, ignore_expires=True)
###利用cookie请求访问另一个网址，此网址是成绩查询网址
##gradeUrl = 'http://jwxt.sdu.edu.cn:7890/pls/wwwbks/bkscjcx.curscopre'
###请求访问成绩查询网址
##print 'loginUrl:' + loginUrl
##print 'result:' + str(result)
##result = opener.open(gradeUrl)
##print result.read()


##================Scrap Qiushi Wiki using regular expression========================
####'Mozilla/4.0(compatible; MSIE 5.5; Windows NT)'
##import urllib
##import urllib2
##import re
##
##page = 1
##url = 'http://www.qiushibaike.com/hot/page/' + str(page)
##user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
##headers = { 'User-Agent' : user_agent }
##try:
##    request = urllib2.Request(url,headers = headers)
##    response = urllib2.urlopen(request)
##    content = response.read().decode('utf-8')
##    pattern = re.compile('<div.*?author">.*?<a.*?<img.*?>(.*?)</a>.*?<div.*?'+
##                         'content">(.*?)<!--(.*?)-->.*?</div>(.*?)<div class="stats.*?class="number">(.*?)</i>',re.S)
##    items = re.findall(pattern,content)
##    print "hahad"
##    for item in items:
##        haveImg = re.search("img",item[3])
##        if not haveImg:
##            print item[0],item[1],item[2],item[4]
##except urllib2.URLError, e:
##    if hasattr(e,"code"):
##        print e.code
##    if hasattr(e,"reason"):
##        print e.reason

####====start of regular ex===========
##tests = '+20 21.3 22 $0.1 $0 1.2'
##pattern = re.compile('[-+]?[0-9]+(\.[0-9]+)?')
##items = re.findall(pattern, tests)
##for item in items:
##    print item
####=====end of regular ex=============

#============using scraper to scrap Tieba =================
## http://tieba.baidu.com/p/3138733512，参数部分是 ?see_lz=1&pn=13138733512
import re

#处理页面标签类
class Tool:
    #去除img标签,7位长空格
    removeImg = re.compile('<img.*?>| {7}|')
    #删除超链接标签
    removeAddr = re.compile('<a.*?>|</a>', re.M)
    #把换行的标签换为\n
    replaceLine = re.compile('<tr(.*?)>|<div(.*?)>|</div>|</p>', re.M)
    #将表格制表<td>替换为\t
    replaceTD= re.compile('<td>')
    #把段落开头换为\n加空两格
    replacePara = re.compile('<p.*?>')
    #将换行符或双换行符替换为\n
    replaceBR = re.compile('<br><br>|<br>')
    #将其余标签剔除
    removeExtraTag = re.compile('<.*?>')
    def replace(self,x):
        x = re.sub(self.removeImg,"",x)
        x = re.sub(self.removeAddr,"",x)
        x = re.sub(self.replaceLine,"\n",x)
        x = re.sub(self.replaceTD,"\t",x)
        x = re.sub(self.replacePara,"\n    ",x)
        x = re.sub(self.replaceBR,"\n",x)
        x = re.sub(self.removeExtraTag,"",x)
        #strip()将前后多余内容删除
        return x.strip()


#百度贴吧爬虫类
class BDTB:

    #初始化，传入基地址，是否只看楼主的参数
    def __init__(self,baseUrl,seeLZ,floorTag):
        #base链接地址
        self.baseURL = baseUrl
        #是否只看楼主
        self.seeLZ = '?see_lz='+str(seeLZ)
        #HTML标签剔除工具类对象
        self.tool = Tool()
        #全局file变量，文件写入操作对象
        self.file = None
        #楼层标号，初始为1
        self.floor = 1
        #默认的标题，如果没有成功获取到标题的话则会用这个标题
        self.defaultTitle = u"百度贴吧"
        #是否写入楼分隔符的标记
        self.floorTag = floorTag
        self.title = ''

    #传入页码，获取该页帖子的代码
    def getPage(self,pageNum):
        try:
            #构建URL
            url = self.baseURL+ self.seeLZ + '&pn=' + str(pageNum)
            request = urllib2.Request(url)
            response = urllib2.urlopen(request)
            #返回UTF-8格式编码内容
            # print u'\r\nget page: 我是页面'
            return response.read().decode('utf-8')
        #无法连接，报错
        except urllib2.URLError, e:
            if hasattr(e,"reason"):
                print u"连接百度贴吧失败,错误原因",e.reason
                return None

    #获取帖子标题
    def getTitle(self,page):
        #得到标题的正则表达式
        pattern = re.compile('<h[1-3] class="core_title_txt.*?>(.*?)</h[1-3]>',re.S)
        result = re.search(pattern,page)
        if result:
            #如果存在，则返回标题
            # print u'\r\nTitle :我是标题'
            return result.group(1).strip()
        else:
            return None

    #获取帖子一共有多少页
    def getPageNum(self,page):
        ##debug for number
        #获取帖子页数的正则表达式
        pattern = re.compile('<li class="l_reply_num.*?</span>.*?<span.*?>(.*?)</span>',re.S)
        result = re.search(pattern,page)
        if result:
            # print u'\r\nget page num 我是页号'
            return result.group(1).strip()
        else:
            return None

    #获取每一层楼的内容,传入页面内容
    def getContent(self,page):
        #匹配所有楼层的内容
        pattern = re.compile('<div id="post_content_.*?>(.*?)</div>',re.S)
        items = re.findall(pattern,page)
        contents = []
        for item in items:
            #将文本进行去除标签处理，同时在前后加入换行符
            content = "\n"+self.tool.replace(item)+"\n"
            contents.append(content.encode('utf-8'))
        # print 'get content 我是内容'
        return contents

    def setFileTitle(self,title):
        #如果标题不是为None，即成功获取到标题
        if title is not None:
            self.title = title + ".txt"
            self.file = open(title + ".txt","w+")
        else:
            self.title = self.defaultTitle + ".txt"
            self.file = open(self.defaultTitle + ".txt","w+")

    def writeData(self,contents):
        #向文件写入每一楼的信息
        for item in contents:
            if self.floorTag == 1:
                #楼之间的分隔符
                floorLine = "\n" + str(self.floor) + u"-----------------------------------------------------------------------------------------\n"
                self.file.write(floorLine)
            self.file.write(item)
            self.floor += 1

    def start(self):
        indexPage = self.getPage(1)
##        print indexPage
        pageNum = self.getPageNum(indexPage)
        title = self.getTitle(indexPage)
        self.setFileTitle(title)
        if pageNum == None:
            print "URL已失效，请重试"
            return
        try:
            print "该帖子共有" + str(pageNum) + "页"
            for i in range(1,int(pageNum)+1):
                print "正在写入第" + str(i) + "页数据"
                page = self.getPage(i)
                contents = self.getContent(page)
                self.writeData(contents)
        #出现写入异常
        except IOError,e:
            print "写入异常，原因" + e.message
        finally:
            print u"写入任务完成"

##3138733512 ,4656381000, 4662226770（中山大学）
print u"请输入帖子代号"
baseURL = 'http://tieba.baidu.com/p/' + str(raw_input(u'http://tieba.baidu.com/p/')).strip()
##seeLZ = raw_input("是否只获取楼主发言，是输入1，否输入0\n")
##floorTag = raw_input("是否写入楼层信息，是输入1，否输入0\n")
seeLZ = 0
floorTag = 1
su = u'哈哈'
bdtb = BDTB(baseURL,seeLZ,floorTag)
bdtb.start()
print 'write to file:' + bdtb.title
bdtb.file.close()
### pycharm Bug:
### http://stackoverflow.com/questions/37010146/how-to-properly-use-a-web-link-as-a-raw-input-in-python/37010347#37010347

##===========self test=========
### -*- coding:utf-8 -*-
##print u"请输入帖子代号"
##print "请输入帖子代号"
##print u"帖子代号".encode('utf-8')##甯栧瓙浠ｅ彿
##print u"帖子代号".encode('gbk')
##print "帖子代号"                 ##甯栧瓙浠ｅ彿
##print u'帖子代号'.encode('gb2312')
##print u"鍝堝搱".encode('utf-8')
