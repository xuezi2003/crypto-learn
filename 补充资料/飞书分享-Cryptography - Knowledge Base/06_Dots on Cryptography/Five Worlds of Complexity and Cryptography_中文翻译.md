# 复杂性与密码学的五个世界

> 本文是 [Five Worlds of Complexity and Cryptography.md](./Five%20Worlds%20of%20Complexity%20and%20Cryptography.md) 的中文翻译。

1995 年，Impagliazzo 在 SCT 会议上发表了 [A Personal View of Average-Case Complexity（平均情形复杂度之我见）](https://dx.doi.org/10.1109/SCT.1995.514853)。在该文中，他描述了五个可能的世界及其对计算机科学的影响。而大多数计算机科学家认为，我们正生活在 Cryptomania（密码狂热世界）或 Minicrypt（微型密码世界）之中。

![图片](./assets/images/7357274645139095580.png)
<!-- 飞书原始链接: https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=YzVkYjcwYjNhNWYwYjc3MWQzYTNhNDg5MWJlN2I0NmNfNmFjN2Y3Y2E4YmNmNDBmMmEyNjRjZmY4NDMwZDQ2YThfSUQ6NzM1NzI3NDY0NTEzOTA5NTU4MF8xNzg1NDYxODgwOjE3ODU0NjU0ODBfVjM -->

**基于格（lattice）的密码学处于哪个世界？**

[Lattice-based Cryptography: SIS & LWE from Chris Peikert @GeTech](https://web.eecs.umich.edu/~cpeikert/pubs/slides-abit2.pdf)

![图片](./assets/images/7357274958600814620.png)
<!-- 飞书原始链接: https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=MGIwYzM3YzBkYmU4OWVhMjBkYzUyYjVhYmJjYzkxYmFfMmVhMDFmNzE2ZmE3NDA0MDY3ZTgyYzFkNWQzYWE3NTFfSUQ6NzM1NzI3NDk1ODYwMDgxNDYyMF8xNzg1NDYxODgwOjE3ODU0NjU0ODBfVjM -->

**Minicrypt 存在吗？**

[Deng17,EUROCRYPT] Magic Adversaries Versus Individual Reduction: Science Wins Either Way（魔法敌手 vs. 个体归约：科学终将胜出）一文中证明了以下两个结论仅有一个成立：

1. Feige-Shamir 协议具有并发安全性
2. 可以将公钥加密建立在抽象的单向函数之上（即 Minicrypt 不存在）

## 有用的链接

- [P, NP, PSPACE and BQP](https://medium.com/arnaldo-gunzi-quantum/p-np-pspace-and-bqp-44d42a842c6a)
- [Complexity Meets Quantum](https://climberpi.github.io/)
