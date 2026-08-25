# How to use TC command (Simplified)

**测试环境：ubuntu20.04**

参考文档：https://netbeez.net/blog/how-to-use-the-linux-traffic-control/

## 查看网卡

这里的目的是查看网卡名称，以便于我们根据不同需求来控制不同的网卡

一般来说，我们自己的电脑会有3张网卡，在命令输入ifconfig查看：

```Bash
jz@jz-YangTianP780-10:~$ ifconfig
eno1: flags=4099<UP,BROADCAST,MULTICAST>  mtu 1500
        ether d8:bb:c1:2e:a1:94  txqueuelen 1000  (以太网)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
        device interrupt 16  memory 0xa1300000-a1320000  

lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
        inet 127.0.0.1  netmask 255.0.0.0
        inet6 ::1  prefixlen 128  scopeid 0x10<host>
        loop  txqueuelen 1000  (本地环回)
        RX packets 264792  bytes 137307435 (137.3 MB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 264792  bytes 137307435 (137.3 MB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

wlp3s0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 192.168.1.60  netmask 255.255.255.0  broadcast 192.168.1.255
        inet6 fe80::c3bb:e8ad:fdd3:ee92  prefixlen 64  scopeid 0x20<link>
        ether 90:0f:0c:30:d6:fb  txqueuelen 1000  (以太网)
        RX packets 1561182  bytes 1021250787 (1.0 GB)
        RX errors 0  dropped 537  overruns 0  frame 0
        TX packets 425179  bytes 193564462 (193.5 MB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
```

其中eno1对应有线网络（如果我们的电脑通过有线的方式组网，则调整这个），wlp3s0对应无线网络（如果我们的电脑通过无线路由器组网，则调整这个），lo对应本地环回网络（如果我们想仅通过1台电脑仿真，则调整这个）。下面我们以lo为例。

## 调整网络延迟

```Bash
tc qdisc add dev lo root netem delay 200ms
```

其中：

- **qdisc:** modify the scheduler (aka queuing discipline)
- **add:** add a new rule
- **dev eth0:** rules will be applied on device eth0
- **root:** modify the outbound traffic scheduler (aka known as the egress qdisc)
- **netem:** use the network to emulate a WAN property
- **delay:** the network property that is modified
- **200ms:** introduce a delay of 200 ms

## 调整带宽

```Bash
tc qdisc add dev lo root tbf rate 1mbit burst 32kbit latency 400ms
# 或者
tc qdisc add dev lo root netem rate 5mbit delay 40ms
```

其中：

- **tbf:** use the token buffer filter to manipulate traffic rates
- **rate:** sustained maximum rate

## 查看已添加的规则

```Bash
tc qdisc show dev lo
```

## 删除规则

```Bash
tc qdisc del dev lo root
```

## 在Docker中开启TC权限

有可能在Docker中，可能会发生我们已经使用了sudo，但是在使用tc命令时仍然提示permission denied。我们可以通过下面的命令来在容器启动时赋予权限。

```Bash
docker run --cap-add=NET_ADMIN --cap-add=NET_RAW -it your/image/name
```