'''
#!/usr/bin/env python
# -*- coding: utf-8 -*-
@File  :down_pics.py
@Author:wufeitong 公众号「吾非同」
@Date  :2020/9/29
'''
# 批量下载图片
import requests
import re
import os
import time

def create_dirs(search_words):
    # 创建关键词目录
    if not os.path.exists('./{}'.format(search_words)):
        os.mkdir('./{}'.format(search_words))


def save_urls(url):
    # 请求并解析数据
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) \
        Chrome/76.0.3809.100 Safari/537.36'}
    html = requests.get(url,headers=headers).text # 获取响应的文本信息
    urls = re.compile(r'<img width="548" height="365" src="(.*?)"') #正则提取图片的URL列表
    res = re.findall(urls, html)
    return res

def save_pics(search_words,urls):
    # 根据图片的URL地址进行循环下载
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) \
        Chrome/76.0.3809.100 Safari/537.36'}
    for i in urls:
        filename = './{}/'.format(search_words)+i.split('/')[-1]
        try:
            with open(filename,'wb+') as f:
                f.write(requests.get(i,headers=headers).content)# 将请求响应的二进制文件写入文件
            print("图片下载成功")
        except:
            print("图片下载失败")
        time.sleep(5)

if __name__ == '__main__':
    search_words=input("下载图片关键词：")
    search_page=int(input("下载页数："))
    # 按页循环下载
    for page in range(1,search_page+1):
        url = 'http://alana.io/page/{}/?s={}&post_type=download'.format(page,search_words)
        create_dirs(search_words)
        urls = save_urls(url)
        save_pics(search_words,urls)
        time.sleep(2)





