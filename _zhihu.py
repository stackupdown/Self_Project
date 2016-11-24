# -*- coding:utf-8 -*- 
import urllib
import urllib2
import re
baseURL = 'https://www.zhihu.com/question/'
question = '49078861'
question = '24099873'
question = '23410067'
question = '24326030'

baseURL = baseURL + question + '?sort=created&page='
pageNum = 1
##%'新闻聚合'

fname = 'iwgc' + '.txt'
fname = 'zhihu_han_' + question + '.txt'
f = open(fname, 'wb')

author = re.compile('<a class="author-link"(.*?\n){3}>(.*?)</a>', re.S)
answerp = re.compile('<div class="zm-editable-content clearfix">\n(.*?)\n(.*?)</div>', re.S)
##author = re.compile('<h3.*?><a href=.*?>(.*?)</a></h3>\r\n\s+<span>(.*?)</span>', re.S)
##item[0] = name
##item[1] = count
removbr = re.compile('<br>')
au_count = 0
f.write(baseURL + '\n\r')

j = 0
for i in range(1, 38):
    print 'page ' + str(i)
    f.write('=' * 15 + 'page ' + str(i) + '=' * 15 + '\r\n')
    rq = urllib2.Request(baseURL + str(i))
    response = urllib2.urlopen(rq)
    con = response.read()
    items = re.findall(author, con)
    answers = re.findall(answerp, con)
    for item in answers:
        j += 1
##        print item[0].decode('utf-8')
##        print item[1].decode('utf-8')
##        print type(answer) ## 只有当re.compile(pattern, )的pattern里面有两个()才能成为tuple,否则是str
        au_count += 1
        print au_count
        f.write('No ' + str(j) + ':')
        f.write('*' * 30 + '\r\n')
        s = re.sub(removbr, '\r\n', item[0])
        f.write(s + '\r\n' * 2)
##        f.write('No' + str(au_count) + ": Name:" + item[0] + '\t')
##        f.write(item[1] + '\r\n')
f.close()
print '=' * 20
print 'write into:' +  fname




##cnblogs
##http://zzk.cnblogs.com/s?t=b&p=1&w=notepad%2B%2B+%E6%AD%A3%E5%88%99%E8%A1%A8%E8%BE%BE%E5%BC%8F+
