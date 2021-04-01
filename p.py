#!/usr/bin/env python3
#coding=utf-8

from alibabacloud_ecs20140526.models import DescribeImagesRequest
from alibabacloud_tea_rpc.models import Config
from alibabacloud_ecs20140526.client import Client

config = Config(
        access_key_id='<ACCESS-KEY-ID>',
        access_key_secret='<ACCESS-KEY-SECRET>',
        region_id='cn-hangzhou'
                    )
client = Client(config)
request = DescribeImagesRequest(image_id='<image-id>')

response = client.describe_images(request)

for image in response.images.image:
    print(image.image_id)
    print(image.image_name)
