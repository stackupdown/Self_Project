#http://www.dytt8.net/
html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""
import bs4
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'lxml')
##soup = BeautifulSoup(open('index.html'))
##print soup.prettify()
## print the first level of contents
##print soup.title
##print soup.head
##
##
#### print a, p,(itself), dict of soup
##print soup.a.name
##print soup.name
##print soup.p.attrs
##soup.p.attrs = {'class':['gg'], 'name': 'godie'}
##print soup.p.attrs
##if type(soup.a.string) == bs4.element.Comment:
##    print soup.a.string
## print contents
i = 0
for child in soup.descendants:
    print '-----' * 10
    print child
