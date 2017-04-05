#coding: utf-8

from django.shortcuts import render_to_response
from django.http import HttpResponse
import hashlib
import logging

logger = logging.getLogger('django')


def test(req):
    """用于公众平台验证服务器可用性"""
    if req.method == 'GET':
        timestamp = req.GET.get('timestamp','None')
        nonce = req.GET.get('nonce','None')
        signature = req.GET.get('signature','None')
        logger.info(signature)
        token = 'yinzhixin'
        templist = sorted([timestamp,nonce,token])    #字典排序  
        tempstr = ''.join(templist)         #排序后合并为字符串
        encryptstr = hashlib.sha1(tempstr).hexdigest()      #对字符串哈希加密
        logger.info("Encrypt:%s" %encryptstr)
        if signature == encryptstr:
            echostr = req.GET.get('echostr','None')
        else:
            echostr = "false"
        return HttpResponse(echostr)


def take_message(req):
    """接收普通消息接口"""
    return HttpResponse("success!")

