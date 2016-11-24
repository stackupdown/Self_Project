# -*- coding:utf-8 -*- 
import urllib
import urllib2
import re
import cookielib

# Python image processing
import sys
import pytesser
import pytesseract
from PIL import Image


# time counting



# threading

##import thread
##import time
####http://mp.weixin.qq.com/s?src=3&timestamp=1468857319&ver=1&signature=upC1pkfV-rv*ZXMXUf6g2wZAm3leKpyr8News9KIyOcN*f8KV*UXndCX-qGFEP*yYA-n5ilfIggdzcpY3ycJ7FGy-DOOP8EXJL7c5faHeDPrCXGO2SHq1IbwlxLL7z3Za3dK9z9ejkguBc4Ju4RPKQ==
##
##for i in range(10):
##    print 'start ' + str(i) + ' thread'

    
##thread.start_new_thread(save_mark, (i * 100, (i + 1)*100))


class Tool:
    #去除img标签,7位长空格
    removeImg = re.compile('<img.*?>| {7}|')
    #删除超链接标签
    removeAddr = re.compile('<a.*?>|</a>')
    #把换行的标签换为\n
    replaceLine = re.compile('<tr>|<div>|</div>|</p>')
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

from webbrowser import open_new_tab
class Spider:
    def __init__(self, baseurl, name0, name1, phone):
        baseurl = 'http://query.5184.com/query/gk/gk_2016_cj.jsp'
        self.name0 = '0512107753'
        self.name1 = '9806'
        self.phone = '13835866000'
        self.tool = Tool()
        self.file = open('filemark.txt', 'a')

        ## image file
        self.list = []
        self.rand = ''
        self.count = 0
        self.baseURL = baseurl + '?phone=' + self.phone + '&serChecked=on'

##    # def getmainPage(self):
##    #     try:
##    #         baseURL = 'http://query.5184.com/query/gk/gk_2016_cj.htm'
##    #         request = urllib2.Request(baseURL)
##    #         response = urlopener.open(request)
##    #         page = response.read()
##    #         return response.read().decode('utf-8')
##    #     except urllib2.URLError, e:
##    #         if hasattr(e, 'reason'):
##    #             print u'>>Connection failed, reason is ', e.reason
##    #             # return None

    def getRandPicture(self, imgurl):
        request = urllib2.Request('http://query.5184.com/query/image.jsp')
        response = urlopener.open(request)
        if response:
            try:
                data = response.read()
                f = open('ttt0.jpg', 'wb')
                f.write(data)
                f.close()
                return response.read()
            except IOError, e:
                print 'write file failed'
                return None


    def getRand(self):
        try:
            fname = 'ttt0.jpg'
            rand = pytesser.image_file_to_string(fname).strip()
            self.rand = rand
            pattern_check = re.compile('[0-9]{4}', re.S)
            check = re.search(pattern_check, self.rand)
            if check:
                return self.rand
            else:
                return None
        except IOError, e:
            print '>>getRand failed'
            return None

    def post_get_page(self, number, name0, name1):
        url = self.baseURL + '&name0=' + name0 + '&name1=' + name1 + \
              '&rand=' + number
##        url = 'http://query.5184.com/query/gk/gk_2016_cj.jsp?phone=13835866000&serChecked=on&name0=0512107202&name1=9803&rand=0157'

        print url
        request = urllib2.Request(url)
        response = urlopener.open(request)
##        print response.read()
        pattern = re.compile('<tr><td>(.*?)</th><td>(.*?)</th><td>(.*?)</th>', re.S)
        items = re.findall(pattern, response.read())
        if items:
            item = items[0]
            self.count += 1
            f = open('filemark.txt', 'a')
            f.write(u'考号:'.encode('gb2312') + name0 + u' 出生年月:'.encode('gb2312') + name1 + '\r\n')
            f.write(u'姓名:'.encode('gb2312') + item[0] + '\r\n' + item[2])
            k = 0
            for item in items:
                if k == 0:
                    k += 1
                    continue
##                print item[0], ' ', item[1], ' ', item[2]
                f.write(',' + item[2])
            f.write('\r\n' * 2)
            f.close()
            return True
        else:
            return False

    def put_not_found(self, name0):
        self.file.write('Not found: ID = ' + name0 + '\r\n')
        return None
cookiejar = cookielib.CookieJar()
urlopener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookiejar))
urllib2.install_opener(urlopener)
imgurl = 'http://query.5184.com/query/image.jsp'
####
basename0 = '051310'
## 金中051210， 潮阳林百欣051310219X
birth = ['9801', '9802', '9803', '9804', '9805',
         '9806', '9807', '9808', '9809', '9810',
         '9811', '9812', '9701', '9702', '9703',
         '9704', '9705', '9706', '9707', '9708',
         '9709', '9710', '9711', '9712', '9901',
         '9902', '9903', '9904', '9905', '9906',
         '9907', '9908', '9909', '9910', '9911',
         '9912']
birthcount = 36
pattern_info_f = re.compile('.*?', re.S) ## not yet used.


def save_mark(stindex, endindex):
    tk = Spider('', '', '', '')
    if stindex >= endindex:
        return None
    tk.file.write('Start write:' + '\n')
    tk.file.close()
    for i in range(stindex, endindex):
        get = False
        j = 0
        while get is not True and j < birthcount:
            name0 = basename0 + str(i)
            pic = tk.getRandPicture(imgurl)
            rand = tk.getRand()
            name1 = birth[j]
            if rand:
                get = tk.post_get_page(rand, name0, name1)
                ## name0 ID count, name1 from birth[0] to birth[35] in post_get_code
                j += 1
                if j == birthcount:
                    if get == False:
                        tk.put_not_found(name0)
                        print name0 + ' not found'
                    else:
                        continue
            else:
                continue

    print tk.count / 100.0
st = 2200
ed = 2295
try:
    save_mark(st, ed)
except:
    tk.file.close()
    print 'HTTP Error'

####item = tk.getContent(rand)
####f = open('ttt.jpg', 'wb')
####f.close()




##====================================================
##====================================================
##import time
##stt = time.time()
##k = 0
##for i in range(1000):
##    for j in range(10000):
##        k = k + 2
##ent = time.time()
##t = ent - stt
##print 'time: %.5f secs' % (t)
##====================================================





##====================================================
##====================================================
# import pytesseract

# from PIL import Image
# for i in range(10):
    # fname = 'D:\\1005 ProgramFiles\\Python\\ttt' + str(i) + '.jpg'
    # im = Image.open(fname)
    # im = im.convert('L')
    # # 灰度值高的点变为黑色
    # im = im.point(lambda x:255 if x > 128 else x)
    # # 灰度值低的点变为白色
    # im = im.point(lambda x:0 if x < 255 else 255)
    # # 去除边框
    # codes = pytesseract.image_to_string(im, lang="eng", config="-psm 7")
    # print 'The ttt' + str(i) + '.jpg\'s code is ' + str(codes) 


##====================================================




##====================================================
##====================================================
##pic = urllib2.urlopen('http://query.5184.com/query/image.jsp')
##data = pic.read()
##filename = 'ttt.jpg'
##f = open(filename, 'wb')
##f.write(data)
##f.close()
##print data
##====================================================

##====================================================
##====================================================
##(encode方法生成的URL)http://query.5184.com/query/gk/gk_2016_cj.jsp?rand=&serChecked=on&phone=13825866000&name0=0512107753&name1=9806
## 确定POST方法是否能够得到页面回应:(正常url)
##        http://query.5184.com/query/gk/gk_2016_cj.jsp?name0=0512107753&name1=9806&rand=9944&phone=13825866000&serChecked=on
##        说明提交方式只是一个字典而非数组(没有顺序)
##====================================================





##====================================================
##====================================================
##pattern_get_mark = re.compile('<tr><td>(.*?)</th><td>(.*?)</th><td>(.*?)</th>', re.S)
##item[0] = 姓名, item[1] = 科目, item[2] = 分数
##====================================================

##====================================================
##====================================================
##cleanFile()
##    in: newfilepath, filepath
##    function: change the 1st image to the 2nd one, using
##    Image and tesseract
##====================================================

##====================================================
##def cleanFile(filePath, newFilePath):
##    image = Image.open(filePath)
###Set a threshold value for the image, and save
##    image = image.point(lambda x: 0 if x<143 else 255)
##    image.save(newFilePath)
###call tesseract to do OCR on the newly created image
##    subprocess.call(["tesseract", newFilePath, "output"])
###Open and read the resulting data file
##    outputFile = open("output.txt", 'r')
##    print(outputFile.read())
##    outputFile.close()
##    cleanFile("text_2.png", "text_2_clean.png")
##====================================================

##====================================================
##Resources:
##====================================================


##高考准考证号的组成





