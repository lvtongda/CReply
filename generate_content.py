#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
About: Generate common reply.
Author: XIAO
Date: 2016-08-10
'''

content = open('common_reply.txt')
fp = open('content.html', 'w')
num = -1

for line in content:
    if line.strip():
        num += 1
        line = '<p id="list' + str(num) + '">' + line + '<button class="btn btn-info btn-sm" data-clipboard-target="#list' + str(num) + '">复制</button></p>'
        fp.write(line)

fp.close
