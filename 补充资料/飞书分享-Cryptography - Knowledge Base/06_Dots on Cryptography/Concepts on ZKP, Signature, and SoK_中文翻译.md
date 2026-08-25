# ZKP、签名与 SoK 的相关概念

> 本文是 [Concepts on ZKP, Signature, and SoK.md](./Concepts%20on%20ZKP%2C%20Signature%2C%20and%20SoK.md) 的中文翻译。

![图片](./assets/images/7325338658970779676.png)
<!-- 飞书原始链接: https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=YjU2NzAwZDI3Y2Y4ZWVjOTMxMjIwNGRiMWIzZmNhNDRfNDA5ZGQ3NGY5OGMyYmJkMzc0YjIwYzY1YTZmMGU5NDRfSUQ6NzMyNTMzODY1ODk3MDc3OTY3Nl8xNzg1NDYxODgxOjE3ODU0NjU0ODFfVjM -->

本文档试图厘清以下概念之间的关系：

- 数字签名（Digital signature）
- ZKP/NIZK：零知识证明 / 非交互零知识证明
- SoK：知识签名（signature of knowledge）
- 知识证明（Proof of knowledge）
- 论证（Arguments）

## 'proof' 与 'proof of knowledge' 的区别

> [what is the difference between proofs and arguments of knowledge?](https://crypto.stackexchange.com/questions/34757/what-is-the-difference-between-proofs-and-arguments-of-knowledge?rq=1)

一个 'proof' 允许证明者证明某个词（word）*属于*某个语言。

一个 'proof of knowledge' 允许证明者证明他*知道*该语句的一个 NP 见证（witness）。

因此，对于 'proof of knowledge'，存在一个提取器（extractor，具有倒带（rewinding）或改变证明者纸带等额外能力），它可以通过与证明者交互来提取出知识。

### 'proof' 与 'argument' 的区别

> [what is the difference between proofs and arguments of knowledge?](https://crypto.stackexchange.com/questions/34757/what-is-the-difference-between-proofs-and-arguments-of-knowledge?rq=1)
>
> [[ECZ+24](https://eprint.iacr.org/2024/050.pdf),MART] Do You Need a Zero Knowledge Proof?

简而言之，argument（论证）就是"计算可靠的证明（computational sound proofs）"。
argument 只考虑针对 PPT（概率多项式时间）证明者的可靠性（soundness），而 proof 则考虑针对计算能力无界证明者的可靠性。

类似地，还存在 '统计零知识' 与 '计算零知识' 证明，分别对应无界验证者和 PPT 验证者。

#### NIZK 与数字签名之间的关系

> [What is the relationship between a NIZK protocol and a digital signature scheme?](https://crypto.stackexchange.com/questions/62327/what-is-the-relationship-between-a-nizk-protocol-and-a-digital-signature-scheme?rq=1)

强存在性不可伪造（Strong existential unforgeability）：敌手即使在看到多个不同实例下的许多签名之后，也无法伪造签名。

模拟可靠可提取性（Simulation-sound extractability）：证明者即使在看到许多模拟证明之后，也无法伪造证明。

具有模拟可靠可提取性的 NIZK 是否意味着一个知识签名（digital signature of knowledge）？

#### 每个签名都是知识证明吗？

并且，每个 NIZK 都意味着一个知识签名吗？

> [Did digital signatures come from Zero Knowledge Proofs?](https://crypto.stackexchange.com/questions/100454/did-digital-signatures-come-from-zero-knowledge-proofs)
>
> [Is Using Digital Signatures to prove identity a zero knowledge proof?](https://crypto.stackexchange.com/questions/35177/is-using-digital-signatures-to-prove-identity-a-zero-knowledge-proof?rq=1)

## 参考

- [[Tha22](https://people.cs.georgetown.edu/jthaler/ProofsArgsAndZK.pdf), FTPS] Proofs, arguments, and zero-knowledge
