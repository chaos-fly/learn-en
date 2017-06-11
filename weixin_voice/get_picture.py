#!/usr/bin/env python
#-*- coding:utf8 -*-

import urllib
import requests
import json
import os

class ImgHelper:
    def __init__(self, keyWord):
        self.name = keyWord
        self.outFile = "imgs/" + keyWord + ".jpg" 
        self.maxRetry = 5

    def getImg(self):
        """ 获取图片url
        """
        print "=====getImg", self.name
        keyword = urllib.quote(self.name)
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
        page_start = 0               # 第一页
        page_num = self.maxRetry     # 数量
        url = 'http://image.baidu.com/search/avatarjson?tn=resultjsonavatarnew&ie=utf-8&word=' 
        url += keyword
        url += '&cg=girl&pn=' + str(page_start) + '&rn=' + str(page_num) + '&itg=0&z=0&fr=&width=&height=&lm=-1&ic=0&s=0&st=-1&gsm=1e0000001e'
        r = requests.get(url, headers=headers)
        ret = json.loads(r.text)
        for i in ret['imgs']:
            if self.saveImg(i['objURL']) == 0:
                break
            

    def saveImg(self, url):
        """ 下载并保存图片
        """
        print "=====saveImg", self.name, url
        try:
            r = requests.get(url, timeout=5)
            if r.status_code == 200:
                with open(self.outFile, 'wb') as fp:
                    fp.write(r.content)
                return 0 
            else:
                print 'Error >> down faild. key:%s url:%s st:%d' % (self.name, url, r.status_code)
        except requests.exceptions.ConnectionError:
            return -1
        return -1

    def covert200x200(self):
        os.system('ffmpeg -i %s -s 200x200 tmp/tmp.jpg' % (self.outFile, ))
        os.system('mv tmp/tmp.jpg %s' % (self.outFile, ))


if __name__ == '__main__':
    for f in os.listdir('audios'):
        if f.find('_') != -1:
            continue
        key = f.split(".")[0]
        print "===========", key
        helper = ImgHelper(key)
        helper.getImg()
        helper.covert200x200()
