#!/usr/bin/env python3
#coding=utf-8

# from cgi import print_form
from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.acs_exception.exceptions import ClientException
from aliyunsdkcore.acs_exception.exceptions import ServerException
from aliyunsdkalidns.request.v20150109.AddDomainRecordRequest import AddDomainRecordRequest
from aliyunsdkalidns.request.v20150109.DescribeDomainRecordsRequest import DescribeDomainRecordsRequest
from aliyunsdkalidns.request.v20150109.UpdateDomainRecordRequest import UpdateDomainRecordRequest
import sys
import json
import os
import requests
import yaml

# 读取配置
dir_path = os.path.split(os.path.realpath(__file__))[0]
yaml_path = os.path.join(dir_path, "../config.yaml")
with open(yaml_path) as f:
    yaml_data = yaml.load(f, Loader=yaml.FullLoader)

conf = yaml_data['alidns']
alidns_key = conf['key']
alidns_secret = conf['secret']
domains = conf['domains']

# 获取公网 ip
r = requests.get('http://ipinfo.io/ip')
ip = r.text

# 检查参数
if not alidns_key or not alidns_secret or not domains or not ip:
    sys.exit()

client = AcsClient(alidns_key, alidns_secret, 'cn-hangzhou')
for record in domains:
    for rr in record['RR']:
        domain_name = record['DomainName']
        request = DescribeDomainRecordsRequest()
        request.set_accept_format('json')
        request.set_DomainName(domain_name)
        request.set_RRKeyWord(rr)
        response = client.do_action_with_exception(request)
        res = json.loads(str(response, encoding='utf-8'))
        # print(str(response, encoding='utf-8'))

        if res['TotalCount'] == 0:
            request = AddDomainRecordRequest()
            request.set_accept_format('json')
            request.set_Type("A")
            request.set_Value(ip)
            request.set_RR(rr)
            request.set_DomainName(domain_name)
            response = client.do_action_with_exception(request)
        elif res['DomainRecords']['Record'][0]['Value'] != ip:
            request = UpdateDomainRecordRequest()
            request.set_accept_format('json')
            request.set_Value(ip)
            request.set_Type("A")
            request.set_RR(rr)
            request.set_RecordId(res['DomainRecords']['Record'][0]['RecordId'])
            response = client.do_action_with_exception(request)