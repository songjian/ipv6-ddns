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

client = AcsClient('LTAI4G46AuNBx4X44ohS2wCR', 'Fz0jobmwGq9j1536oVPsgslg7JIKSR', 'cn-hangzhou')
request = DescribeDomainRecordsRequest()
request.set_accept_format('json')
request.set_DomainName(sys.argv[2])
request.set_RRKeyWord(sys.argv[1])
response = client.do_action_with_exception(request)
res = json.loads(str(response, encoding='utf-8'))
#print(str(response, encoding='utf-8'))     
if res['TotalCount'] == 0:
    request = AddDomainRecordRequest()
    request.set_accept_format('json')
    request.set_Type("AAAA")
    request.set_Value(sys.argv[3])
    request.set_RR(sys.argv[1])
    request.set_DomainName(sys.argv[2])
    response = client.do_action_with_exception(request)
elif res['DomainRecords']['Record'][0]['Value'] != sys.argv[3]:
    request = UpdateDomainRecordRequest()
    request.set_accept_format('json')
    request.set_Value(sys.argv[3])
    request.set_Type("AAAA")
    request.set_RR(sys.argv[1])
    request.set_RecordId(res['DomainRecords']['Record'][0]['RecordId'])
    response = client.do_action_with_exception(request)
