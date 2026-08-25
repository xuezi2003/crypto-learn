# [BBM+21, Apple] The Apple PSI System

**Summary: 提出了针对iCloud中CSAM检测的Fuzzy Threshold PSI with Associated Data (ftPSI-AD).**

这篇文章使用的PSI本质上是基于DH的，其对比的是图像的哈希：

- Associated data指的是图像的关联信息，比如灰度值之类的，以便于后期的人工审核；
- Threshold指的是，当client的match数量超过阈值时，server才可以解密出相应的associated data，否则server只能得到random id组成的集合，这些random id是和图像独立的；
- Fuzzy指的是，当client的match数量没有超过阈值时，server不知道具体有多少的match，其实现方式是使用到了detectable hash function (DHF) 和一个由client拥有的保密且随机的集合S实现。在执行PSI协议时，client会对每一个random id生成一个voucher，如果id不来自S的话，那就生成一个正常的voucher（包含DHF生成的随机数），否则生成一个fuzzy voucher（包含真随机数）；当正常的voucher达到阈值时，可通过检测算法检测出来，否则会检测失败。

其余部分大多是很长的复杂构造和安全证明，这里就不放上来了。

在阅读的时候，我发现DHF的功能和之前看到过的OKVS和OPPRF有点相似，都是在一串随机数中找到刻意生成（不知道描述合不合理）的随机数，于是思考了一下这里的DHF是否可以替换成OKVS或OPPRF，结果是不可以的。从这里使用DHF的目的来说，使用DHF主要是防止在match没达到阈值的时候服务器获取到match数量信息，在这种情况下，DHF会直接检测失败，而OPPRF或OKVS仍然可以找出具体的match个数，所以并不符合这个fuzzy的要求。