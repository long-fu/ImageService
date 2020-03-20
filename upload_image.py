#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 18:52:59 2020

@author: haoshuai
"""

import requests

def upload_image(image_data):

    url = 'http://0.0.0.0:8000/api/v1/upimg'
    files = {'file': open('/Users/haoshuai/opt/tutorial/full/c2b675f6aca4701ba95878b7b2da2d30ef7471ff.jpg', 'rb')}
    headers={'token': 'SheIsABeautifulGirl'}
    r = requests.post(url, files=files,headers=headers)

    #r = requests.post('http://0.0.0.0:8000/api/v1/upimg',image_data,headers=headers)
    print(r.text)


if __name__ == '__main__':
    file_path = "/Users/haoshuai/opt/tutorial/full/c2b675f6aca4701ba95878b7b2da2d30ef7471ff.jpg"
    try:
        f = open(file_path,'rb')
        data = f.read()
        f.close()
        print("数据大小",len(data))
        upload_image(data)
    except IOError:
        print("读取文件错误");

    
#    image_data =  
    pass
