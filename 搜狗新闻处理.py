# encoding: utf-8
"""
@version:3.6
@author:lamplight
@file:数据处理-txt文中xml处理.py
@time:2017/12/715:21
"""
import os
from xml.dom import minidom
from urllib.parse import urlparse
import codecs

def file_fill():
    file_dir = ".\语料库"
    for root, dirs, files in os.walk(file_dir):
        for f in files:
            tmp_dir = '.\sougou_after2' + '\\' + f #加上标签后的文本
            text_init_dir = file_dir + '\\' +f  #原始文本
            # print(text_init_dir)
            file_source = open(text_init_dir, 'r')
            ok_file = open(tmp_dir, 'a+')
            start = '<docs>\n'
            end = '</docs>'
            line_content = file_source.readlines()
            ok_file.write(start)
            for lines in line_content:
                text = lines.replace('&', '&')
                ok_file.write(text)
            ok_file.write(end)

            file_source.close()
            ok_file.close()

def file_read():
    file_dir = ".\语料库"
    for root, dirs, files in os.walk(file_dir):
        for f in files:
            print(f)
            doc = minidom.parse(file_dir + "\\" + f)
            root = doc.documentElement
            claimtext = root.getElementsByTagName("content")
            claimurl = root.getElementsByTagName("url")
            for index in range(0, len(claimurl)):
                if (claimtext[index].firstChild == None):
                    continue
                url = urlparse(claimurl[index].firstChild.data)
                if dicurl.has_key(url.hostname):
                    if not os.path.exists(path + dicurl[url.hostname]):
                        os.makedirs(path + dicurl[url.hostname])
                    fp_in = file(path + dicurl[url.hostname] + "\%d.txt" %(len(os.listdir(path + dicurl[url.hostname])) + 1),"w")
                    fp_in.write((claimtext[index].firstChild.data).encode('utf-8'))



if __name__ == "__main__":


    file_fill()
    file_read()
    path = ".\sougou_all\\"
    dicurl = {
        'auto.sohu.com': 'qiche', 'it.sohu.com': 'hulianwang', 'health.sohu.com': 'jiankang', \
        'sports.sohu.com': 'tiyu', 'travel.sohu.com': 'lvyou', 'learning.sohu.com': 'jiaoyu', \
        'career.sohu.com': 'zhaopin', 'cul.sohu.com': 'wenhua', 'mil.news.sohu.com': 'junshi', \
        'house.sohu.com': 'fangchan', 'yule.sohu.com': 'yule', 'women.sohu.com': 'shishang', \
        'media.sohu.com': 'chuanmei', 'gongyi.sohu.com': 'gongyi', '2008.sohu.com': 'aoyun', \
        'business.sohu.com': 'shangye'
    }
    file_read(".\sougou_after2")