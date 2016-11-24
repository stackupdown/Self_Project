# -*- coding:utf-8 -*-
##//==================================================================
##[填坑] 有关在多线程中使用Python API
##http://tieba.baidu.com/p/4402015571
import thread
import time

# Define a function for the thread
def print_time(threadName, delay):
   count = 0
   while count < 3:
      time.sleep(delay)
      count += 1
      print "%s: %s" % ( threadName, time.ctime(time.time()) )

# Create two threads as follows
try:
   thread.start_new_thread( print_time, ("Thread-1", 0.5, ) )
   thread.start_new_thread( print_time, ("Thread-2", 0.4, ) )
except:
   print "Error: unable to start thread"



##==================================================================//

##//==================================================================

# -*- coding:utf-8 -*- 
##import time, threading
##
### 新线程执行的代码:
##def loop():
##    print('thread %s is running...' % threading.current_thread().name)
##    n = 0
##    while n < 5:
##        n = n + 1
##        print('thread %s >>> %s' % (threading.current_thread().name, n))
##        time.sleep(1)
##    print('thread %s ended.' % threading.current_thread().name)
##
##print('thread %s is running...' % threading.current_thread().name)
##t = threading.Thread(target=loop, name='LoopThread')
##t.start()
##t.join()
##print('thread %s ended.' % threading.current_thread().name)


##==================================================================//

##//==================================================================

##[python]使用 multiprocessing.dummy 执行多线程任务
##    >>
##from multiprocessing.dummy import  Pool as ThreadPool
##import requests
##import time
##import urllib2, urllib
##def getsource(url, i):
##    request = urllib2.Request(url)
##    html = urllib2.urlopen(request)
##    print html.read()
##
##urls = []
##for i in range(1, 3):
##    newpage = 'http://www.qianfandu.com/major?page='+str(i)
##    urls.append(newpage)
##
##pool = ThreadPool(2)
##time3 = time.time()
##results = pool.map(getsource, urls)
##pool.close()
##pool.join()
##time4 = time.time()
##print u'多线程爬虫： ', (time4-time3)
