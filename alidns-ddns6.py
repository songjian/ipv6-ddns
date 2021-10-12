#!/usr/bin/env python3
#coding=utf-8

from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.acs_exception.exceptions import ClientException
from aliyunsdkcore.acs_exception.exceptions import ServerException
from aliyunsdkalidns.request.v20150109.AddDomainRecordRequest import AddDomainRecordRequest
from aliyunsdkalidns.request.v20150109.DescribeDomainRecordsRequest import DescribeDomainRecordsRequest
from aliyunsdkalidns.request.v20150109.UpdateDomainRecordRequest import UpdateDomainRecordRequest
import sys
import json
import os

from dotenv import load_dotenv
from os import environ
#print(sys.argv)

load_dotenv(verbose=True)

tmp = os.popen("ip addr show enp2s0 | grep inet6 | grep mngtmpaddr | awk '{ print $2; }' | sed 's/\/.*$//'").readlines()
inet6_addr = tmp[0].strip('\n')
#print(inet6_addr)

ACCESS_KEY_ID = environ.get('ACCESS_KEY_ID')
ACCESS_KEY_SECRET = environ.get('ACCESS_KEY_SECRET')

client = AcsClient(ACCESS_KEY_ID, ACCESS_KEY_SECRET, 'cn-hangzhou')
request = DescribeDomainRecordsRequest()
request.set_accept_format('json')
request.set_DomainName(sys.argv[1])
request.set_RRKeyWord(sys.argv[2])
response = client.do_action_with_exception(request)
res = json.loads(str(response, encoding='utf-8'))
#print(str(response, encoding='utf-8'))     
if res['TotalCount'] == 0:
    request = AddDomainRecordRequest()
    request.set_accept_format('json')
    request.set_Type("AAAA")
    request.set_Value(inet6_addr)
    request.set_RR(sys.argv[2])
    request.set_DomainName(sys.argv[1])
    response = client.do_action_with_exception(request)
elif res['DomainRecords']['Record'][0]['Value'] != inet6_addr:
    request = UpdateDomainRecordRequest()
    request.set_accept_format('json')
    request.set_Value(inet6_addr)
    request.set_Type("AAAA")
    request.set_RR(sys.argv[2])
    request.set_RecordId(res['DomainRecords']['Record'][0]['RecordId'])
    response = client.do_action_with_exception(request)
