# （非）均匀性：一次探索

> 本文是 [(Non-)uniformity - An Exploration.md](./%28Non-%29uniformity%20-%20An%20Exploration.md) 的中文翻译。
>
> 这是 Zhongming 的工作笔记，它可能需要非常非常长的时间才能完成。:(

# 预备知识

**记号：**

- $\mathcal{P}$, $\mathcal{Q}$ 是两个原语（primitive），P 和 Q 分别是它们的实现。
- B 和 A 分别是针对这两个原语的两个 PPT 敌手。

![图片](./assets/images/7422930762200465410.png)
<!-- 飞书原始链接: https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=ODdlYzkyMDhkZjhmN2Q0NDM2MDVkMmU2NzcwYzlhNzVfYmMyM2RlYTZiZmZiNjY4NjlkMDIwMmFmNWM1NzM0ZDBfSUQ6NzQyMjkzMDc2MjIwMDQ2NTQxMF8xNzg1NDYxODg2OjE3ODU0NjU0ODZfVjM -->

# 概念

**通用构造（General Construction）：**（构造映射 Q）存在一个映射 Q(·)，使得：如果 P 是 $\mathcal{P}$ 的一个高效实现，那么 Q(P) 就是 $\mathcal{Q}$ 的一个高效实现。

**完全黑盒构造（Fully Black-box Construction）：**（黑盒构造 Q）对于实现 $\mathcal{P}$ 的每一个（计算能力无界的）预言机 P，$Q^P$ 都实现 $\mathcal{Q}$。

观察 1：$\mathcal{Q}$ 的完全黑盒构造把 P 当作预言机使用，而通用构造可以访问其代码。

**均匀安全归约（存在性安全）：** 如果存在一个能够攻破 $\mathcal{Q}$ 安全性的预言机 A，那么就存在一个能够攻破 $\mathcal{P}$ 安全性的 B。

**非均匀安全归约（构造性安全）：** 如果存在一个能够攻破 $\mathcal{Q}$ 安全性的 PPT 敌手 A，那么就存在一个能够输出一个实例来攻破 $\mathcal{P}$ 安全性的 B。

观察 2：构造性安全要求归约算法*输出一个困难问题实例的见证（witness）*，而存在性安全只要求该见证存在。这类似于 ZKPoK（零知识知识证明）与 ZKP（零知识证明）之间的区别。

注 1（为什么需要构造性安全？）：构造性安全由 Rogaway 提出，用于解决存在性安全与*无密钥（unkeyed）哈希函数*之间的张力。理想情况下，使用哈希函数的构造应该使用*带密钥的哈希*，或者使用*来自某个函数族*的无密钥哈希；否则，该哈希函数就是非均匀的。对于非均匀哈希，总存在一个高效算法，能够利用硬编码的输入输出一个碰撞。为克服这一局限，构造性安全要求归约算法输出其所用哈希的一个碰撞，而不是仅要求这样的敌手存在。

# 例子

**非均匀构造。**

**非均匀安全归约。**

**均匀与非均匀归约的分离。**

**实现 RO 的不可能性。**

# 参考

- [[MRH03](https://eprint.iacr.org/2003/161),TCC] Indifferentiability, Impossibility Results on Reductions, and Applications to the Random Oracle Methodology
- [[Rogaway06](https://eprint.iacr.org/2006/281),VietCrypt] Formalizing human ignorance: Collision-resistant hashing without the keys
- [BU08,[ASIACRYPT](https://www.iacr.org/archive/asiacrypt2008/53500293/53500293.pdf)] Limits of Constructive Security Proofs
- [CMLP13,[ITCS](https://www.cs.cornell.edu/~rafael/papers/nonuniform-camera.pdf)] On the Power of Non-uniformity in Proofs of Security
