# ipv6-ddns

## 查看机器网卡

```bash
ip a
```

## crontab

ip addr show $1 | grep inet6 | grep mngtmpaddr | awk '{ print $2; }' | sed 's/\/.*$//'
