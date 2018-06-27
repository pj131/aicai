# --*-- Encoding: UTF-8 --*--
import requests
import urllib
import re
import sys
import os
import json

def req_get_content(url) :
    '''requests url , return list'''
    r=requests.get(url)
#    print(url)
#    print(r.content)
    j=json.loads(r.content)

#    for a in j['result']:
#        print(a)
#    print(j['result']['keyList'])
#    print(j['result']['cupMatchList'])

    l=j['result']['cupMatchList']
    # for a in l:
    #     print(a)
    #     for item in a:
    #         print(item)
    #         for b in item:
    #             print(b)
                # print(b,item[b])
#    return j['list']

    return l
