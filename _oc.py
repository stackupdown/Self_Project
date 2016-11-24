# -*- coding:utf-8 -*-
import sys
import pytesser
import pytesseract
import urllib
import urllib2
import re
import cookielib


from PIL import Image
fname = 'ttt0.jpg'
def tocodes(fname):
    codes = pytesser.image_file_to_string(fname).strip()
    print 'The ttt' + str(i) + '.jpg\'s code is ' + codes
    return codes
def getpage(url):
    re1 = urllib2.request(url)
    page = urlopener.open(re1)
    try:
        f = open('.txt', 'wb+')
    except IOError, e:
        print 'f open error'
    if page:
        print page
    else:
        print 'Error get page'
    if f and page:
        return page
def getCode(fname):
    try:
        rand = pytesser.image_file_to_string(fname).strip()
        pattern_check = re.compile('[0-9]{4}', re.S)
        check = re.search(pattern

##
##import pytesseract
##import urllib
##import urllib2
##import re
##import cookielib
##
##
##from PIL import Image
##import subprocess
##for i in range(10):
##    fname = 'D:\\1005 ProgramFiles\\Python\\ttt' + str(i) + '.jpg'
##    im = Image.open(fname)
##    im = im.convert('L')
##    # 灰度值高的点变为黑色
##    im = im.point(lambda x:255 if x > 128 else x)
##    # 灰度值低的点变为白色
##    im = im.point(lambda x:0 if x < 255 else 255)
##    # 去除边框
##    codes = pytesseract.image_to_string(im)
##    print 'The ttt' + str(i) + '.jpg\'s code is ' + str(codes)






##from urllib.request import urlretrieve
##from urllib.request import urlopen
##from bs4 import BeautifulSoup
##import subprocess
##import requests
##from PIL import Image
##from PIL import ImageOps
##def cleanImage(imagePath):
##image = Image.open(imagePath)
##image = image.point(lambda x: 0 if x<143 else 255)
##borderImage = ImageOps.expand(image,border=20,fill='white')
##borderImage.save(imagePath)
##html = urlopen("http://www.pythonscraping.com/humans-only")
##bsObj = BeautifulSoup(html)
###Gather prepopulated form values
##imageLocation = bsObj.find("img", {"title": "Image CAPTCHA"})["src"]
##formBuildId = bsObj.find("input", {"name":"form_build_id"})["value"]
##captchaSid = bsObj.find("input", {"name":"captcha_sid"})["value"]
##captchaToken = bsObj.find("input", {"name":"captcha_token"})["value"]
##captchaUrl = "http://pythonscraping.com"+imageLocation
##urlretrieve(captchaUrl, "captcha.jpg")
##cleanImage("captcha.jpg")
##p = subprocess.Popen(["tesseract", "captcha.jpg", "captcha"], stdout=
##subprocess.PIPE,stderr=subprocess.PIPE)
##p.wait()
##f = open("captcha.txt", "r")
##
###Clean any whitespace characters
##captchaResponse = f.read().replace(" ", "").replace("\n", "")
##print("Captcha solution attempt: "+captchaResponse)
##
##if len(captchaResponse) == 5:
##    params = {"captcha_token":captchaToken, "captcha_sid":captchaSid,
##    "form_id":"comment_node_page_form", "form_build_id": formBuildId,
##    "captcha_response":captchaResponse, "name":"Ryan Mitchell",
##    "subject": "I come to seek the Grail",
##    "comment_body[und][0][value]":
##    "...and I am definitely not a bot"}
##    r = requests.post("http://www.pythonscraping.com/comment/reply/10",
##    data=params)
##    responseObj = BeautifulSoup(r.text)
##if responseObj.find("div", {"class":"messages"}) is not None:
##    print(responseObj.find("div", {"class":"messages"}).get_text())
##else:
##    print("There was a problem reading the CAPTCHA correctly!"
