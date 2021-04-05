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
`*/10 * * * * /home/sj/ipv6-ddns/ipv6-ddns.sh [NetworkCardName] [SubdomainName] [DomainName]`
