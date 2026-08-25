# 配合 Katz 书籍一起学习

> 源文件：`配合Katz书籍一起学习.pdf`（PDF 原文保留，本文由 OCR 识别生成）
>
> 配套教材：《Introduction to Modern Cryptography》（Katz & Lindell）。以下问题供阅读时参考。

## Foundation of Crypto

学习路径（按层次递进）：

- **Motivation > Concept**（communication model）level 1 > formalize a complex problem level 2 > ......
- **Level 1 (Application)**：How to use!
- **Level 2 (Security Research)**：How to formalize a problem, define the security model and then prove it!!
- **Level 3 (Crypto Research)**：You should know various foundations of cryptography, various security proof skills. Design basic crypto schemes or protocols!!!

## 以下内容供阅读时参考

### 1. Private-Key Encryption

#### 1.1 Computational Security

- 什么是计算安全？
- 计算安全与完美安全有什么区别？
- 什么样的敌手是 "efficient adversary"？

#### 1.2 Defining Computational Secure Encryption

- 如何理解 private-key encryption scheme 的通信模型？
- 如何形式化描述一个 private-key encryption scheme?
- 什么是 stateful private-key encryption scheme?
- 定义一个安全模型，需要哪两个基本要素？以例子进行说明
- 什么是不可区分性安全？
- 解释定义 3.8 的合理性；定义 3.8 和定义 3.9 你感觉哪个更好？
- Page-56 的四个例子中，选择一个你感兴趣的进行详细阐述。
- 什么是语义安全？
- 语义安全和不可区分性安全有什么区别和联系？你感觉哪个更好？

#### 1.3 Constructing an EAV-secure encryption scheme

- 什么是 PRG?
- 阐述规约证明（proof by reduction）框架，并解释其合理性
- 那么如何证明一个方案是安全的？又如何证明一个方案是不安全的？
- 证明 construction 3.17 的安全性 (Theorem 3.16)

#### 1.4 Stronger Security Notions

- 为什么需要概率加密（Probabilistic encryption）？
- 什么是选择明文攻击？什么是预言机（oracle）？
- 什么是 IND-CPA?
- 你认为 IND-CPA 和 IND-EAV 哪个安全定义更强一点？

#### 1.5 Constructing a CPA-Secure Encryption Schemes

- 什么是 PRFs？什么是 PRPs？
- PRG, PRFs, PRPs 的区别是什么?
- 什么是 Strong pseudorandom permutations？你感觉他有什么用？
- 复习规约证明框架，证明 construction 3.28 的安全性 (Theorem 3.29).

#### 1.6 Modes of Operations and Encryption in Practice

- 为什么需要操作模式？
- 常用的操作模式有哪些？了解其工作原理

#### Exercise

课后习题 3.6 3.10 3.19

### 2. Message Authentication Codes

#### 2.1 Message Integrity

- 什么是保密性？
- 什么是完整性？为什么需要完整性？
- 什么是安全？（一个值得你思考整个研究生阶段的问题）

#### 2.2 Message Authentication Code

- 阐述 MAC 的通信模型。
- 如何形式化描述一个 MAC 方案？
- 如何定义 MAC 方案的安全性？
- 什么是 replay attack？如何解决 replay attack?
- 什么是强不可伪造？为什么需要强不可伪造？

#### 2.3 Constructing Secure Message Authentication Codes

- 复习规约证明框架，证明 construction 4.5 的安全性 (Theorem 4.6).
- 证明 construction 4.7 的安全性 (Theorem 4.8).

#### Exercise

课后习题 4.6

### 3. CCA-Secure and Authenticated Encryption

- 本章和前面几个章节的关系是什么？

#### 3.1 Chosen Ciphertext Attack and CCA-Secure

- 什么是选择密文攻击？为什么选择密文攻击赋予了敌手更强的攻击能力？
- 什么是 IND-CCA?
- 证明 construction 3.28 在 IND-CCA 下是不安全的。
- IND-CCA 比 IND-CPA 更安全？
- 实际应用中，你会让设计的方案满足哪个安全定义？
- 什么是安全？（一个值得你思考整个研究生阶段的问题）

#### 3.2 Authentication Encryption

- 阐述 AE 的通信模型。
- 如何形式化描述一个 AE 方案？
- 如何定义 AE 方案的安全性？

#### Exercise

阅读 5.3，5.4 节

### 4. Hash Functions and Applications

- 本章和前面几个章节的关系是什么？

#### 4.1 Definitions

- 什么是 hash 函数？它有什么作用？
- 如何定义 cryptographic hash function 的安全性？

#### 4.2 Merkle-Damgård Transform

- 为什么需要 Merkle-Damgård Transform？它有什么作用？
- 复习规约证明框架，证明 construction 6.3 的安全性 (Theorem 6.4).

#### 4.3 Message Authentication Codes using Hash Functions

- 复习规约证明框架，证明 construction 6.5 的安全性 (Theorem 6.6).
- 解释为什么 construction 6.7 是安全的？
- 研究 construction 4.5, 4.7, 6.5, 6.7 的共同点；

#### 4.4 The Random Oracle Model

> Congrats! 恭喜你没有放弃，其实密码学对大家都难。从这里开始，证明开始投机取巧。

> 人话：能坚持到这里已经不容易；接下来（随机预言机模型）的证明会借助理想化假设，不再像之前那么严格。

- 为什么需要 Random Oracle Model?
- Random Oracle Model 是什么?
- Random Oracle Model 在证明中怎么用？
- 追求 Standard model. 那么什么是 standard model?

#### 4.5 Additional Applications

- 为什么这一节的标题有个 "additional"？
- fingerprinting and Deduplication.
- Merkle trees（这个很重要，很实用）
- Password Hashing
- Key-Derivation Function
- Commitment schemes（这个很重要）

#### Exercise

课后习题 6.2，6.11，6.20

### 5. Theoretical Constructions of Symmetric-Key Primitives

- 本章和前面几个章节的关系是什么？
- 前面章节的一些概念，比如 encryption，mac，hash function，对于攻击者来说好像都有一个"难"点。那么这个"难"点是什么呢？是什么本质的东西赋予了这些方案能够在现实中存在？
- **It is the one way functions.**

#### 5.1 - 5.3 One way functions and hard-core bits（基于可计算安全密码学方案构造的最基本单元）

- 什么是单向函数？什么是单向置换？
- 什么是单向函数族？什么是单向置换族？
- 常见的单向函数有哪些？这个和 P, NP 有啥关系吗？
- 什么是 hard-core predicates?（这个是单向函数的最本质的东西）
- 你知道单向函数求逆过程中哪一个 bit 最难吗？
- 存不存在这样一个 bit 的通用构造，使得敌手无论如何都没有足够的计算能力预测这个 bit 的值？
- 如果存在这样一个 bit 的通用构造，那我们是不是可以更多难以预测的 bits (a binary string)?

#### 5.4 Constructing PRG

- 如何利用 hard-core bits 构造 PRG?
- 什么是 hybrid argument？这个概念很重要，以后将会在 paper 中经常看到。
- 如何使用 hybrid argument 证明构造 PRG 的安全性？

#### 5.5 Constructing PRFs

- 如何利用 PRG 构造 PRFs?
- 如何用 hybrid argument 证明构造的 PRFs 是安全的？

#### 5.6 - 5.7 From one way functions to symmetric-key primitives

- 画图表示目前接触到的所有密码学相关的概念之间的关系。即把本章中定理的结论整理在一张图中表示出来。

### 6. Key Management and Public-key revolution

#### 6.1 - 6.2 Key Management

- 对称密码在密钥管理中存在的问题有哪些？
- 在 KDC 框架下，上述问题分别是如何解决的？

#### 6.3 Key Exchange

- 密钥协商机制解决了什么问题？
- Diffie-Hellman 密钥协商机制具体是怎么工作的？
- 如何形式化表述密钥协商机制的安全性？如何证明其安全性？
- DH 密钥协商真的安全吗？可以用于实际生活中吗？

#### 6.4 Public-Key Revolution

- 为什么需要对称密码体制？
- 为什么需要非对称密码体制？
- 非对称密码体制中，分别是如何实现私密性和完整性的？
- 阅读《密码学新方向》

#### Exercise

课后习题 11.3

### 7. Public-Key Encryption

#### 7.1 - 7.2 Public-Key Encryption and its definition

- 对称加密方案和非对称加密方案的区别与联系？
- 非对称加密方案的通信模型？
- 如何形式化定义非对称加密方案？
- 如何形式化定义非对称加密方案的安全模型？
- 为什么非对称加密方案中，CPA 安全和 EAV 安全是等价的？
- 非对称加密可以实现完美安全吗？对称加密方案可以实现完美安全吗？
- 确定性加密安全吗？
- 一个 CPA 安全的非对称加密方案，使用多次是否安全？请证明这个结论。
- 非对称加密方案下，如何形式化定义 CCA 安全？
- 实际生活中，为什么需要 CCA 安全？

#### 7.3 Hybrid Encryption

- 为什么需要混合加密？
- 什么是密钥封装机制？
- 讨论混合加密的安全性。(CPA, then CCA)

#### 7.4 - 7.5 Constructions

- El Gamal 加密是如何工作的？讨论其安全性
- El Gamal-like KEM 是如何工作的？讨论其安全性（可选）
- DHIES/ECIES 是如何工作的？讨论其安全性（可选）
- RSA 加密方案是如何工作的？讨论其安全性
- RSA-OAEP 加密方案是如何工作的？讨论其安全性（可选）
- 讨论 El Gamal 和 RSA 方案的同态性。
- 综合比较上述方案，画表比较
- 同态 v.s. CCA 安全两者有啥关系？

#### Exercise

- 阅读 A practical public key cryptosystem provably secure against adaptive chosen ciphertext attack.
- 课后习题 12.1

### 8. Digital Signature Scheme

#### 8.1 - 8.2 Digital Signature and its definition

- 数字签名和手写签名对比
- 数字签名和消息认证对比
- 数字签名和公钥加密的关系
- 数字签名方案的通信模型？
- 如何形式化描述一个数字签名方案？
- 如何形式化定义数字签名方案的安全性？

#### 8.3 The hash-and-Sign Paradigm

- The hash-and-Sign Paradigm 是如何工作的？讨论其安全性

#### 8.4 - 8.5 Constructions

- Plain RSA 签名如何工作的？讨论其安全性
- RSA-FDH 签名是如何工作的？讨论其安全性
- DSA/ECDSA 是如何工作的？讨论其安全性

#### 8.6 Certificates, PKI, and TLS

- 什么是 Certificates？什么是 PKI?
- 阐述 PKI 的工作方式
- 如何撤销用户的 certificate？阅读 [Crypto1998] Fast Digital Identity Revocation
- TLS 解决的问题是什么？
- 阐述 TLS 的工作方式。

#### Exercise

- 阅读 A practical public key cryptosystem provably secure against adaptive chosen ciphertext attack.
- 课后习题 13.5

### 9. Advanced Topics

#### 9.1 Trapdoor permutations and its application

- 什么是 trapdoor permutation?
- trapdoor permutation 如何构造 PKE? 讨论其安全性

#### 9.2 Paillier Encryption（重要）

- Paillier Encryption 是如何工作的？
- 讨论其正确性，安全性，以及同态性

#### 9.3 Secret Sharing（重要）

- 为什么需要 Secret Sharing (SS)？
- Shamir's SS 是如何工作的？讨论其安全性
- 为什么需要 VSS？什么是 VSS？VSS 是如何工作的？讨论其安全性
- 什么是 Threshold Encryption?
- SS 是如何应用在 Threshold Encryption 中的？

## Paper Training

- [AsiaCrypt2001] Short Signatures from the Weil Pairing
- [Crypto2001] Identity-Based Encryption from the Weil Pairing
- [EuroCrypt2004] Public Key Encryption with Keyword Search
- [EuroCrypt2005] Fuzzy identity-based encryption
- [Crypto2012] Multiparty Computation from Somewhat Homomorphic Encryption

## Security Reduction Training

Fuchun Guo《Introduction to security reduction》.
