#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 18:44:56 2020

@author: haoshuai
"""

from sanic import Sanic
from sanic.response import json, text, file
import os, sys
import hashlib

app = Sanic()
# 图片存储目录
baseDir = sys.path[0] + '/image/'
# 校验 Token 写死就成，反正自己用的嘛
token = 'SheIsABeautifulGirl'
# 允许的域名列表
allowHost = [
            'localhost',
            'ilovethisword',
            'i.fengcss.com',
            'blog.csdn.net'
        ]

# 成功返回方法
def ok(data):
    if type(data) == list:
        return json({"data": {"list": data}, "status": 0})
    else:
        return json({"data": data, "status": 0})
# 失败返回方法
def fail(data):
    return json({"data": data, "status": 1})

# 获取图片后缀名
def getSuffix(filename):
    tempArr = filename.split('.')
    suffix = tempArr[-1]
    fileType = ['jpg', 'jpeg', 'gif', 'png']
    if len(tempArr) < 2:
        return 'error name'
    elif suffix not in fileType:
        return 'error type'
    else:
        return suffix

# 检查请求地址是否授权
def checkHost(host):
    for i in allowHost:
        if i in host:
            return True
    return False

# 上传图片文件接口
@app.route('/api/v1/upimg', methods=['POST'])
async def upimg(request):
    # 判断用户是否具有上传权限
    if request.headers.get('token') != token:
         return fail('您没有使用本服务的权限')
    image = request.files.get('file').body
    # 判断文件是否支持
    imageName = request.files.get('file').name
    imageSuffix = getSuffix(imageName)
    if 'error' in imageSuffix:
        return fail(imageSuffix)
    # 组织图片存储路径
    m1 = hashlib.md5()
    m1.update(image)
    md5Name = m1.hexdigest()

    # 用 md5 的前两位来建文件夹，防止单个文件夹下图片过多，又或者根目录下建立太多的文件夹
    saveDir = baseDir + md5Name[0:2] + '/'
    savePath = saveDir + md5Name[2:] + '.' + imageSuffix
    resPath = '/' + md5Name[0:2] + '/' + md5Name[2:] + '.' + imageSuffix

    # 如果文件夹不存在，就创建文件夹
    if not os.path.exists(saveDir):
        os.makedirs(saveDir)

    # 将文件写入到硬盘
    tempFile = open(savePath, 'wb')
    tempFile.write(image)
    tempFile.close()

    # 给客户端返回结果
    return ok({"path": resPath})

# 请求图片接口
@app.route('/', methods=['GET'])
async def img(request):
    # 判断是否为网站请求，否则就加上自定义的字符串（允许本地访问）
    host = request.headers.get('referer') or 'ilovethisword'
    # 判断请求接口是否带参数，否则加上自定义字符串（没有这个文件夹，返回404）
    args = request.args.get('path') or 'ilovemywife'
    # 拼接文件地址
    path = baseDir + args
    # 如果不在允许列表，则展示 401 图片
    if not checkHost(host):
        path = baseDir + '/7b/e49a54f761da42174d6121fa13e0b3.png'
    # 如果文件不存在，则展示 404 图片
    if not os.path.exists(path):
        path = baseDir + '/b4/74335c3944f42275e3caa13930a9b9.png'
    # 返回文件
    return await file(path)
# 启动服务
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
