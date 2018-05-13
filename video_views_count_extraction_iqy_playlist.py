#!/usr/bin/python
# -*- coding: UTF-8 -*-

import requests, bs4
import re

response = requests.get('http://www.iqiyi.com/playlist471041502.html')
soup = bs4.BeautifulSoup(response.text, "html.parser")


def show_video_stats(n):
    info = {}
    title = soup.select('.site-piclist_info [target="_blank"]')[n]['title']
    info['title'] = title[15:]
    views_str = soup.select('.site-piclist_info .site-piclist_info_times [data-widget-counter="player"]')[n].get_text()
    info['views'] = convertDigits(views_str)
    
    return info


def convertDigits (views_str, encoding="utf-8"):
    digits = re.search('[0-9]*.?[0-9]', views_str)
    digits = digits.group()                            
    
#   chinese_digits = re.search('万', views_str)    
#    if (chinese_digits is not None):
#        digits = digits * 10000
    return float(digits)




video_stats = []
for n in range(0,35):
    video_stats.append(show_video_stats(n))
    
video_stats = sorted(video_stats, key=lambda k: k['views'], reverse=True) 

rank = 1
for member in video_stats:
    print(rank, member['title'], member['views'])
    rank += 1


