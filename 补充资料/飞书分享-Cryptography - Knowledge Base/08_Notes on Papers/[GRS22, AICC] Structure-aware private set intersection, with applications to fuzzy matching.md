# [GRS22, AICC] Structure-aware private set intersection, with applications to fuzzy matching

**Summary: 这篇文章利用FSS构造了fuzzy structure aware PSI，A输入一个结构化集合（$\ell_\infty$ 球体集合），B输入一个非结构化集合（点集合），协议输出是二者集合中距离在阈值内点。**

这篇文章从Boolean Function Secret Sharing（bFSS）切入，介绍了strong bFSS，其中function是一个指示函数，当方程的输入为集合的值时，输出0，否则输出1。然后这篇文章提出了weak bFSS的概念，允许假阳性和允许输出大于1。然后这篇文章介绍了两个用于构造weak bFSS的技术，一个是spatial hashing，另一个是xor-share技术。

spatial hashing的基本思想是:

1. 将大的输入域划分为较小的网格单元。
2. 识别与输入集合相交的"活动单元",为每个活动单元构造一个组件bFSS。
3. 将所有组件bFSS打包进一个保密的键值存储(OKVS)数据结构中。
4. 在评估时,根据输入点所在的单元,查询OKVS以获得相应的组件bFSS,然后使用它来评估该点。
5. 对于不活动的单元,OKVS会输出随机值,从而产生有界误报率。

整体上,spatial hashing利用网格划分,将大域上的bFSS问题变换到小单元上,后者可以使用非常高效简单的bFSS。同时,OKVS可以隐藏活动单元的信息。这种技术对表示多个球体的并集特别有效。

xor-share的基本思想是:

1. 对每个球体 $i$，在 $d$ 个维度上生成一个加法共享的 ${0}$：$R[i,1] \oplus \ldots \oplus R[i,d] = 0$。
2. 将所有球体在每个维度上投影,得到一组不相交的区间。
3. 对每个维度 $j$，使用区间的并集的bFSS,使得在球体 $i$ 的投影区间上输出 $R[i,j]$。
4. 对任意点 $x$，在每个维度上评估区间并集的bFSS,得到 $y_1, \ldots, y_d$。
5. 如果 $x$ 在某个球体 $i$ 内,则 $\bigoplus_j y_j = \bigoplus_j R[i,j] = 0$。如果不在任何球体内,则 $\bigoplus_j y_j$ 是随机的。
6. 通过这种xor技术,避免了对不同维度的bFSS输出进行连接,降低了与维数的关系从指数级到线性级。

这种技术还使用了我们的spatial hashing方法,但需要保证在相交单元内仍然正确地输出随机共享。

最后作者里利用bFSS构造了PSI，其思路和基于OPRF的PSI类似。基本思路是:

1. 使用弱函数秘密分享(bFSS)表示Alice的结构化输入集合 $A$。
2. Bob随机选择一组比特 $s$，通过OT协议获得 $A$ 的bFSS密钥的一份。
3. Bob使用这份bFSS密钥,对每个元素 $b \in B$ 计算一个PRF值 $F(b)$。
4. Bob发送这组PRF值给Alice。
5. 对于 $a \in A$，因为Alice持有bFSS的另一份密钥,她可以计算 $F(a)$。
6. Alice检查Bob发来的PRF值集合,找出与 $F(a)$ 匹配的,就可以得到 $a \in A \cap B$。

这篇文章比较抽象，有一些地方还没有看懂，需要再看几天。并且这里的fuzzy和apple PSI的fuzzy不是一个概念，这里的fuzzy在于两点之间的距离，而Apple PSI的fuzzy在于匹配的数量，他们的共同点是都使用到了bFSS。
