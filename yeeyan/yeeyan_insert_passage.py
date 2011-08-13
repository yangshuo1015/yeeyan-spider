#!/usr/bin/python
#coding=utf-8
import urllib2
import sqlite3
import lxml.html as H

db_path = 'yeeyan.db'
file_path = 'error_url.txt'

def pase_jx(doc):
    title = doc.xpath('//head/title/text()')[0].split('|')[1].strip()
    div = doc.xpath('//div[@class="jxar_author"]')[0]
    author = div.xpath('.//a/text()')[0]
    release_time = div.xpath('//p[@class="jxa_info"]/span[1]/text()')[0]
    try:
        excerpt = doc.xpath('//p[@class="jxa_intro"]/text()')[0]
    except Exception:
        excerpt = ""
    category = doc.xpath('//p[@class="jxa_map"]/text()')[1].split()[1]
    content_html = doc.xpath('//div[@class="jxa_content"]')[0].text_content()
    jx = True
    return title,author,release_time,excerpt,category,content_html,jx

def pase_passage(doc):
    title = doc.xpath('//head/title/text()')[0].split('|')[1].strip()
    div = doc.xpath('//div[@class="user_info"]')[0]
    author = div.xpath('.//h2/a/text()')[0]
    excerpt_l = div.xpath('//p[@class="excerpt"]/text()')
    if excerpt_l:
        excerpt = excerpt_l[0]
    else:
        excerpt = ""
    release_time = doc.xpath('.//p/text()')[0].strip()[1:-7]
    try:
        category = doc.xpath('//div[@class="crumb"]/a/text()')[1]
    except Exception:
        category = doc.xpath('//div[@class="crumb"]/a/text()')[0]
    content_html = doc.xpath('//div[@id="conBox"]')[0].text_content()
    jx = False
    return title,author,release_time,excerpt,category,content_html,jx

def getInfo(url):
    req = urllib2.Request(url)
    s = urllib2.urlopen(req).read()
    doc = H.document_fromstring(s)
    if doc.xpath('//div[@id="jx_head"]'):
        title,author,release_time,excerpt,category,content_html,jx=pase_jx(doc)
    else:
        title,author,release_time,excerpt,category,content_html,jx=pase_passage(doc)
    cur = con.cursor()
    cur.execute('insert into yeeyan values(?,?,?,?,?,?,?,?)',(url,title,author,release_time,excerpt,category,content_html,jx))
    con.commit()
    print "插入%s成功"%url
    cur.close()

if __name__=='__main__':
    con = sqlite3.connect(db_path)
    f = open(file_path)
    for url in f:
        getInfo(url.strip())
    con.close()

