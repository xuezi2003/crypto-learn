# The Definitions of Random Oracle Model

RO 作为密码学安全证明的基石之一，广泛存在于各类密码学论文中。然而，尽管都属于 ROM，不同论文中所使用的 RO 却有所不同。这里，我们主要对不同类别的 RO 进行了介绍。

## Definitions

根据 Simulator 对 RO 的控制程度，RO 的定义大致可分为以下三类 [龚征08]：

### Non-programmable（i.e., ideal hash function）

Simulator 无法获知敌手的输入，也不能控制 RO 的输出 (例如 Fiat-shamir transform 中需要将 hash 函数抽象为 RO [CLMQ21])。此时，RO 可视作 hash 函数的理想化。其定义保证了：给定输入，输出为真正均匀随机的值；对于重复输入，RO 保持相同输出值。

### Limited-programmable

> 参考 [FLR+10]，这类 ROM 可进一步细分。

Simulator 可获知敌手的输入，但无法控制 RO 的输出。此时，simulator 类似于对敌手的窃听者，其监控了敌手的所有通信。

### Full-programmable

Simulator 可以完全控制 RO 的执行，对于每一个输入，simulator 可以制定输出的规则 (例如 BLS 签名的证明中，需要对 Hash 函数进行编程)。这类 RO 无法被任何现实 hash 函数替换，因为现实世界中的 hash 函数 (如: MD5, SHA-3) 执行均与输入无关。

## Observations

1. RO 是由 Mihir Bellare 和 Philip Rogaway [BR93] 在尝试为部分密码原语提供安全证明时，所引入的理想化（证明）模型。
2. 目前并没有任何复杂度假设可以涵盖所有 RO 所具有的一切性质。且存在方案只在 ROM 下安全，任何对其构造中 RO 进行实例化的尝试，都会使得其方案安全性受损 [RGH98]。
   - 目前没有实例能够实现 RO 的全部性质意味着 RO is more than an assumption (?) 以 Elgamal 加密为例，其要求不存在任何 PPT 敌手能够攻破 DDH 难题。即，DDH 安全意味着 Elgamal 安全。然而，RO 的假设要求存在一个实例满足其所有特性。
3. 目前没有证据表明在（密码学）协议的安全证明中使用 ROM 意味着存在现实中的攻击。即，目前在 ROM 下的证明能够为密码学研究者们提供足够 (?) 的信心 [KM15]。
   - 需要注意的是，大部分密码学研究者对 Full programmable ROM 下的安全证明缺乏信心，而 Non-pragrammable ROM 下的安全证明已被大部分人所接受。
   - 相反的是，绝大部分理论密码学研究者对任何形式的 ROM 下的证明均缺乏信心，因此构造标准模型下安全的密码学方案一直为密码学研究中的重要方向。

## References

- [龚征08, 博士论文] 随机预言机模型下可证明安全性关键问题研究
- [FLR+10,[ASIACRYPT](https://www.iacr.org/archive/asiacrypt2010/6477305/6477305.pdf)] Random Oracles With(out) Programmability
- [[CLMQ21](https://eprint.iacr.org/2020/915),CRYPTO] Does Fiat-Shamir Require a Cryptographic Hash Function
- [BR93,[CCS](https://cseweb.ucsd.edu/~mihir/papers/ro.pdf)] Random oracles are practical: a paradigm for designing efficient protocols
- [[RGH98](https://eprint.iacr.org/1998/011),Preprint] The Random Oracle Model, revisited
- [[KM15](https://eprint.iacr.org/2015/140),Preprint] The Random Oracle Model: A Twenty-Year Retrospective
- [[CDG+18](https://eprint.iacr.org/2018/165),EUROCRYPT] The Wonderful World of Global Random Oracles

## Useful websites

1. [What is Random Oracle Model and Why is it Controversial?](https://crypto.stackexchange.com/questions/879/what-is-the-random-oracle-model-and-why-is-it-controversial)
2. [Indifferentiability by Matthew Green](https://blog.cryptographyengineering.com/2012/07/17/indifferentiability/)
3. [密码学安全证明中的random oracle模型是在什么情况下被提出来的? - 知乎](https://www.zhihu.com/question/633386619)
4. [究竟什么才是随机预言机(random oracle)呢? - 知乎](https://www.zhihu.com/question/26968119)
