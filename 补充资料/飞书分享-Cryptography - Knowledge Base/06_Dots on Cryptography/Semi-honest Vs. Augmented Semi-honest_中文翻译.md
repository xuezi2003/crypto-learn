# 半诚实（Semi-honest）vs. 增强半诚实（Augmented Semi-honest）

> 本文是 [Semi-honest Vs. Augmented Semi-honest.md](./Semi-honest%20Vs.%20Augmented%20Semi-honest.md) 的中文翻译。

**摘要：** 在增强半诚实模型中，被敌手控制的参与方被允许在计算开始前修改自己的输入。

为简单起见，我们只考虑两方计算。

## 定义

### 基于模拟的安全性（Simulation-based security）

[How To Simulate It – A Tutorial on the Simulation Proof Technique](https://eprint.iacr.org/2016/046)

> 直觉上，一个协议是安全的，如果参与协议的一方能够计算出的任何东西，都可以仅基于其输入和输出计算得出。这根据模拟范式（simulation paradigm）来形式化。粗略地说，我们要求协议执行中一方的视图（view）仅给定其输入和输出即可被模拟。这就意味着参与方从协议执行本身什么也学不到，正如所期望的那样。

![画板](<./assets/whiteboard_QLEmws1K.jpg>)
<!-- 飞书画板 token: QLEmws1Kzh2iXabdLWmcg6ldnTb -->

### 半诚实（静态）

**敌手的能力：** 敌手将腐化（corrupt）两方中的一方，并诚实地遵循协议规范执行。但敌手会试图通过内部消息学习超出理想功能所允许的信息。

**安全性的形式化定义：** 一方在协议（真实）执行中的视图，可以仅给定其输入和输出（理想）不可区分地被模拟。

![图片](./assets/images/7431454770516754435.png)
<!-- 飞书原始链接: https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=YjM0MTFlMWExMTVjN2RkODMyMTBmYWY0ZjMwMGI4YWJfZTZlYWY2OWUxYTI0ODFiNTk5NzRiNDlkMzM1ZmQwZGFfSUQ6NzQzMTQ1NDc3MDUxNjc1NDQzNV8xNzg1NDYxODg5OjE3ODU0NjU0ODlfVjM -->

### 增强半诚实

**敌手的能力：** 与半诚实模型中的行为相同，但敌手可以在协议执行前修改被腐化方的输入。

## 半诚实 / 增强半诚实 / 恶意（Malicious）

如果一个协议被证明可抵御恶意敌手，那么它在半诚实敌手面前未必被证明是安全的。

直觉上，在恶意设置中敌手能够修改输入，这比半诚实设置中的敌手更强大。

如果一个协议被证明可抵御恶意敌手，那么它可以被证明在增强半诚实敌手面前是安全的。

直觉上，增强半诚实敌手是忠实遵循协议的恶意敌手的一种特例。

详细例子请参考 [Efficient secure two party computation](https://link.springer.com/book/10.1007/978-3-642-14303-8) 的第 2.3.3 节。

![画板](<./assets/whiteboard_ShPswvKg.jpg>)
<!-- 飞书画板 token: ShPswvKgth6ZDdbP23CciwQMnPc -->

## 参考

- [Efficient secure two party computation](https://link.springer.com/book/10.1007/978-3-642-14303-8)：第 2.2 章
- [Foundation of cryptography](https://theswissbay.ch/pdf/Gentoomen%20Library/Security/Oded_Goldreich-Foundations_of_Cryptography__Volume_2%2C_Basic_Applications%282009%29.pdf#page=332.29)：定义 7.4.24
