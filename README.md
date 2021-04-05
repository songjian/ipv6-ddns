# ipv6-ddns

## 查看机器网卡

```bash
ip a
```

## 设置定时执行

```bash
crontab -e
```

添加
`*/10 * * * * /home/sj/ipv6-ddns/ipv6-ddns.sh enp2s0`
