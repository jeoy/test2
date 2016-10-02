
# -*- coding: utf-8 -*-  

import urllib
import urllib2
import re

# import time
 #where2showthis
#处理页面标签类
 

#试着用命令行去同步这个文件
#试着用命令行去同步这个文件2
#试着用命令行去同步这个文件3
#试着用命令行去同步这个文件4
 
 I added some master changed this
 master
 
    #初始化，传入基地址，是否只看楼主的参数
    def __init__(self,baseUrl,seeLZ):
        self.baseURL = baseUrl
        self.seeLZ = '?see_lz='+str(seeLZ)

    def getPageNum(self):
    	page = self.getPage(1)
    	pattern = re.compile('<li class="l_reply_num.*?</span>.*?<span.*?>(.*?)</span>',re.S)
    	result = re.search(pattern,page)
    	if result:
	        #print result.group(1)  #测试输出
	        return result.group(1).strip()
		
	     

    #传入页码，获取该页帖子的代码
    def getPage(self,pageNum):
        try:
            url = self.baseURL+ self.seeLZ + '&pn=' + str(pageNum)
            t1 = time.time()
            request = urllib2.Request(url)
            t2 = time.time()
            response = urllib2.urlopen(request)
            t3 = time.time()
            print response
            print type(response)
            # print response.read()
            # print t2-t1
            print t3 -t2
            a = response.read()
            t4 = time.time()
            print t4 -t3
            # print a


            return a
        except urllib2.URLError, e:
            if hasattr(e,"reason"):
                print u"连接百度贴吧失败,错误原因",e.reason
                return None
 	
	  	
    def getPageT(self):
    	t1 = time.time()
    	page = self.getPage(1)
    	t2 = time.time()
    	pattern = re.compile('<h3 class="core_title_txt.*?>(.*?)</h3>',re.S)
    	t3 = time.time()
    	result = re.search(pattern,page)
    	t4 = time.time()
    	t = t2-t1
    	print t
    	t = t3 - t2
    	print t
    	t = t4 -t3
    	print t
    	if result:
    		return result.group(1).strip()
    	else:
    		return None
    #获取每一层楼的内容,传入页面内容
    def getContent(self,page):
		pattern = re.compile('<div id="post_content_.*?>(.*?)</div>',re.S)
		items = re.findall(pattern,page)
		
		return items
		

tt1 = time.time()
baseURL = 'http://tieba.baidu.com/p/1975955502'
bdtb = BDTB(baseURL,1)
page = bdtb.getPage(1)
t1 = time.time()
fo2 = open("BUG1.txt",'w')
items = bdtb.getContent(page)
t2 = time.time()
t = t2 - t1
print t
remove = Tool()
t1 = time.time()

for item in items:
	a = remove.replace(item)
	fo2.write("\n________________\n")
	fo2.write(a)

t2 = time.time()
t = t1 - tt1
print t


# print remove.replace(a)



# 
# fo2.write(str(a))

# page = fo2.readlines();
 
# bdtb.getPage(1)