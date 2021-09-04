# ipv6-ddns

## 查看机器网卡

```bash
ip a
```

## 设置定时执行

```bash
crontab -e
```

每隔10分钟执行1次
```bash
*/10 * * * * /usr/bin/python3 ~/ipv6-ddns/alidns-ddns6.py [域名] [主机记录]
```
