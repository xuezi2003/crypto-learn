# OKVS based on Garbled Cuckoo Table

In this document, we discuss GCT-based OKVS. In OKVS, we have two algorithms:

$D\leftarrow \text{Encode}(I,R),y\leftarrow \text{Decode}(D,x)$, where $I=\{(x_1,y_1),\ldots,(x_n, y_n)\}$.

## 2-Hash GCT

[[PRTY20, EUROCRYPT](https://eprint.iacr.org/2020/193.pdf)] PSI from PaXoS: Fast, Malicious Private Set Intersection

**Start-Point:** The encoding size of the garbled bloom filter is *large (*encoding rate: $O(1/\lambda)$ *)*, but its encoding time is *linear*. We want a linear time encoding OKVS with a smaller encoding rate ($O(1/(2+\epsilon))$).

**High-level idea:** There are two hash functions $h_1, h_2$. For simplicity, we can view $D$ as a cuckoo table where $D[h_1(x)]\oplus D[h_2(x)]=y$.

Firstly, we can construct a cuckoo graph whose vertices represent the positions in $D$, edges represent the elements meant to be inserted. If this graph happened to be a tree, then $D$ can be constructed through tree traversal. For example, we can set $D[1]$ as the root, and set $D[1]=r$. If we use BFS to traverse the tree, then the computation order is $D[2]=x_1\oplus D[1],D[3]=x_2\oplus D[1],D[4]=x_3\oplus D[2],D[5]=x_4\oplus D[2],D[6]=x_5\oplus D[3], D[7]=x_6\oplus D[3].$

![画板](<./assets/whiteboard_D9XPw5bE.jpg>)
<!-- 飞书画板 token: D9XPw5bE9hGAdCbdNZmcGE4zncd -->

However, for $D$ with size $n=O(m)$, this graph is unlikely to be acyclic, so the above method does not work. We need to find 2-core of the graph (which is shown the black lines). The 2-core of the graph is solved by linear equations. The other part is solved by the above methods.

![图片](./assets/images/7454175237589352452.png)
<!-- 飞书原始链接: https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=M2ZlYWFkZTBiYWI2NjVhNTkzMTcxZWZmMmEwZDg3NzVfZDUzZTJhYTY3NjVlMzk3ZjI3MjU5MGE3OWE0ODM3MmJfSUQ6NzQ1NDE3NTIzNzU4OTM1MjQ1Ml8xNzg1NDYxODkxOjE3ODU0NjU0OTFfVjM -->

**How to add a new edge?**

- In the 2-core: computation complexity scales with the entire set. (recompute the solution of linear equations and all of the subtrees)
- Not in the 2-core: computation complexity scales with the updated set. (retraverse one of the subtrees)

## 3-Hash GCT