## 7.3 Compression Functions and Hash Functions　7.3 压缩函数与哈希函数

Recall from Chapter 6 that the primary security requirement for a cryptographic hash function $H$ is collision resistance: that is, it should be difficult to find a collision in $H$, i.e., distinct inputs $x, x^{\prime}$ such that $H(x) = H(x^{\prime})$. (We drop mention of any key here, since real-world hash functions are generally unkeyed.) If the hash function has $\ell$-bit output length, then the best we can hope for is that it should be infeasible to find a collision using substantially fewer than ${2}^{\ell/2}$ invocations of $H$. (See Section 6.4.1.)

回顾第 6 章可知，密码学哈希函数 $H$ 的主要安全要求是抗碰撞性：即难以在 $H$ 中找到碰撞，也就是说难以找到不同的输入 $x, x^{\prime}$ 使得 $H(x) = H(x^{\prime})$。（这里我们不再提及密钥，因为现实世界中的哈希函数通常是无密钥的。）如果哈希函数的输出长度为 $\ell$ 比特，那么我们最多只能期望：想用远少于 ${2}^{\ell/2}$ 次 $H$ 调用来找到碰撞是不可行的。（参见 6.4.1 节。）

We describe two approaches for constructing collision-resistant hash functions. In Section 7.3.1, we show how to build a compression function (i.e., a fixed-length hash function) from any block cipher. As we have seen in Section 6.2, any such compression function can be extended to a full-fledged hash function using the Merkle–Damgård transform. This approach has been used to design popular hash functions including MD5, SHA-1, and SHA-2.

我们描述构造抗碰撞哈希函数的两种方法。在 7.3.1 节中，我们展示如何从任意分组密码构造压缩函数（即固定长度的哈希函数）。如我们在 6.2 节中所见，任何这样的压缩函数都可以使用 Merkle–Damgård 变换扩展为功能完整的哈希函数。这种方法已被用于设计包括 MD5、SHA-1 和 SHA-2 在内的流行哈希函数。

In Section 7.3.3 we discuss a more recent approach for constructing hash functions based on the so-called sponge construction. This technique is used by the SHA-3 standard.

在 7.3.3 节中，我们讨论一种较新的构造哈希函数的方法，它基于所谓海绵构造（sponge construction）。SHA-3 标准使用了这一技术。

### 7.3.1 Compression Functions from Block Ciphers　7.3.1 从分组密码构造压缩函数

Perhaps surprisingly, it is possible to build a collision-resistant compression function from a block cipher satisfying strong security properties. There are several ways to do this. One of the most common is via the Davies–Meyer construction. Let $F$ be a block cipher with $n$-bit key length and $\ell$-bit block length. The Davies–Meyer construction then defines the compression function $h: \{0,1\}^{n+\ell} \to \{0,1\}^{\ell}$ by $h(k,x) \overset{\mathrm{def}}{=} F_k(x) \oplus x$. (See Figure 7.11.)

也许令人惊讶的是，可以从满足强安全性质的分组密码构造抗碰撞的压缩函数。有多种方法可以做到这一点。最常见的方法之一是通过 Davies–Meyer 构造。设 $F$ 是密钥长度为 $n$ 比特、分组长度为 $\ell$ 比特的分组密码。Davies–Meyer 构造由此定义压缩函数 $h: \{0,1\}^{n+\ell} \to \{0,1\}^{\ell}$ 为 $h(k,x) \overset{\mathrm{def}}{=} F_k(x) \oplus x$。（见图 7.11。）

![Image](https://lsky.jerryxue.top/i/2026/08/19/6a85c55612d96.jpg)

**FIGURE 7.11: The Davies–Meyer construction.**

**图 7.11：Davies–Meyer 构造。**

We do not know how to prove collision resistance of $h$ based only on the assumption that $F$ is a strong pseudorandom permutation, and in fact there are reasons to believe such a proof is not possible. We can, however, prove collision resistance if we are willing to model $F$ as an ideal cipher. The ideal-cipher model is a strengthening of the random-oracle model (see Section 6.5), in which we posit that all parties have access to an oracle for a random keyed permutation $F : \{0,1\}^n \times \{0,1\}^\ell \to \{0,1\}^\ell$ as well as its inverse $F^{-1}$ (i.e., $F^{-1}(k,F(k,x)) = x$ for all $k,x$). Another way to think of this is that each key $k \in \{0,1\}^n$ specifies an independent, uniform permutation $F(k,\cdot)$ on $\ell$-bit strings. As in the random-oracle model, the only way to compute $F$ (or $F^{-1}$) is to explicitly query the oracle with $(k,x)$ and receive back $F(k,x)$ (or $F^{-1}(k,x)$). The ideal-cipher model is stronger than the random-permutation model that we encountered briefly in Section 7.1.5.

我们不知道如何仅基于 $F$ 是强伪随机置换的假设来证明 $h$ 的抗碰撞性，事实上有理由相信这样的证明是不可能的。然而，如果我们愿意将 $F$ 建模为理想密码，则可以证明抗碰撞性。理想密码模型（ideal-cipher model）是比随机预言机模型（参见 6.5 节）更强的模型，其中我们假设所有参与方都可以访问一个预言机，该预言机提供带密钥的随机置换 $F : \{0,1\}^n \times \{0,1\}^\ell \to \{0,1\}^\ell$ 及其逆 $F^{-1}$（即对所有 $k,x$ 有 $F^{-1}(k,F(k,x)) = x$）。另一种理解方式是，每个密钥 $k \in \{0,1\}^n$ 指定 $\ell$ 比特串上的一个独立均匀置换 $F(k,\cdot)$。与随机预言机模型一样，计算 $F$（或 $F^{-1}$）的唯一方式是用 $(k,x)$ 显式查询预言机并接收返回的 $F(k,x)$（或 $F^{-1}(k,x)$）。理想密码模型比我们在 7.1.5 节中简要遇到的随机置换模型更强。

Analyzing constructions in the ideal-cipher model comes with all the advantages and disadvantages of working in the random-oracle model, as discussed at length in Section 6.5. We only add here that the ideal-cipher model implies the absence of related-key attacks on $F$, in the sense that the permutations $F(k,\cdot)$ and $F(k^{\prime},\cdot)$ must behave independently even if, for example, $k$ and $k^{\prime}$ differ in only a single bit. In addition, there can be no "weak keys" $k$ (say, the all-0 key) for which $F(k,\cdot)$ is easily distinguishable from random. It also means that $F(k,\cdot)$ should "behave randomly" even when $k$ is known. These requirements are not part of the definition of a (strong) pseudorandom permutation. Moreover, these properties do not necessarily hold for real-world block ciphers, and the reader may note that we have not discussed these properties in any of our analysis of block-cipher constructions. (In fact, DES and triple-DES do not satisfy these properties.) Any block cipher being considered for instantiating an ideal cipher must be evaluated with respect to these more stringent requirements.

在理想密码模型中分析构造，会带来在随机预言机模型中工作的全部优缺点，6.5 节对此有详细讨论。我们在此仅补充，理想密码模型蕴含 $F$ 不存在相关密钥攻击，即置换 $F(k,\cdot)$ 和 $F(k^{\prime},\cdot)$ 必须相互独立，即使 $k$ 和 $k^{\prime}$ 仅相差一个比特。此外，不存在使 $F(k,\cdot)$ 容易与随机置换区分开的“弱密钥” $k$（例如全 0 密钥）。这也意味着即使 $k$ 已知，$F(k,\cdot)$ 也应当“表现得随机”。这些要求不是（强）伪随机置换定义的一部分。而且，这些性质对于现实世界中的分组密码不一定成立，读者可能注意到我们在分组密码构造的分析中并未讨论这些性质。（事实上，DES 和三重 DES 不满足这些性质。）任何被考虑用来实例化理想密码的分组密码，都必须按照这些更严格的要求加以评估。

The following shows that, when F is modeled as an ideal cipher, the Davies–Meyer construction is collision resistant as long as $\ell$ is sufficiently large.

以下结论表明，当 F 被建模为理想密码时，只要 $\ell$ 足够大，Davies–Meyer 构造就是抗碰撞的。

**THEOREM 7.5** If $F$ is modeled as an ideal cipher, then any attacker making $q$ queries to $F$ or $F^{-1}$ can find a collision in the Davies–Meyer construction with probability at most $q^2/2^\ell$.

**定理 7.5** 如果 $F$ 被建模为理想密码，则任何对 $F$ 或 $F^{-1}$ 进行 $q$ 次查询的攻击者，在 Davies–Meyer 构造中找到碰撞的概率至多为 $q^2/2^\ell$。

**PROOF** To be clear, we consider here the probabilistic experiment in which a uniform $F$ is sampled (more precisely, for each $k \in \{0,1\}^n$ the function $F(k, \cdot) : \{0,1\}^\ell \to \{0,1\}^\ell$ is chosen uniformly from the set $\mathsf{Perm}_\ell$ of permutations on $\ell$-bit strings) and then the attacker is given oracle access to $F$ and $F^{-1}$. The attacker then tries to find a colliding pair $(k, x)$, $(k^{\prime}, x^{\prime})$, i.e., for which $F(k, x) \oplus x = F(k^{\prime}, x^{\prime}) \oplus x^{\prime}$. No computational bounds are placed on the attacker other than bounding the number of oracle queries it makes. We assume the attacker never makes the same query more than once, and never queries $F^{-1}(k, y)$ once it has learned that $y = F(k, x)$ (or vice versa). We assume that if the attacker outputs a candidate collision $(k, x)$, $(k^{\prime}, x^{\prime})$ then it has previously made the oracle queries necessary to compute the values $h(k, x)$ and $h(k^{\prime}, x^{\prime})$. All these assumptions are without much loss of generality.

**证明** 明确地说，我们这里考虑如下概率实验：采样一个均匀的 $F$（更精确地说，对每个 $k \in \{0,1\}^n$，函数 $F(k, \cdot) : \{0,1\}^\ell \to \{0,1\}^\ell$ 从 $\ell$ 比特串上的置换集合 $\mathsf{Perm}_\ell$ 中均匀选择），然后给予攻击者对 $F$ 和 $F^{-1}$ 的预言机访问。攻击者然后试图找到一对碰撞 $(k, x)$、$(k^{\prime}, x^{\prime})$，即满足 $F(k, x) \oplus x = F(k^{\prime}, x^{\prime}) \oplus x^{\prime}$。除了限制预言机查询次数外，对攻击者不施加任何计算限制。我们假设攻击者从不对同一查询重复提问，且一旦得知 $y = F(k, x)$ 就不再查询 $F^{-1}(k, y)$（反之亦然）。我们假设如果攻击者输出一个候选碰撞 $(k, x)$、$(k^{\prime}, x^{\prime})$，则它此前已进行了计算 $h(k, x)$ 和 $h(k^{\prime}, x^{\prime})$ 所需的预言机查询。所有这些假设几乎不损失一般性。

Consider the $i$th query the attacker makes to one of its oracles. A query $(k_i, x_i)$ to $F$ reveals only the hash value $h_i \stackrel{\mathrm{def}}{=} h(k_i, x_i) = F(k_i, x_i) \oplus x_i$; similarly, a query $(k_i, y_i)$ to $F^{-1}$ giving the result $x_i = F^{-1}(k_i, y_i)$ yields only the hash value $h_i \stackrel{\mathrm{def}}{=} h(k_i, x_i) = y_i \oplus F^{-1}(k_i, y_i)$. The key observation is that no matter which kind of query the attacker makes, the hash value $h_i$ it learns is almost uniformly distributed (since the result of the oracle query to $F$ or $F^{-1}$ is almost uniformly distributed—with the only deviation from uniform being that $F(k, x)$ cannot be equal to $F(k, x^{\prime})$ for any $x \neq x^{\prime}$). This makes finding a collision hard since the attacker does not obtain a collision unless $h_i = h_j$ for some $i \neq j$.

考虑攻击者对其某个预言机进行的第 $i$ 次查询。对 $F$ 的查询 $(k_i, x_i)$ 仅揭示哈希值 $h_i \stackrel{\mathrm{def}}{=} h(k_i, x_i) = F(k_i, x_i) \oplus x_i$；类似地，对 $F^{-1}$ 的查询 $(k_i, y_i)$ 给出结果 $x_i = F^{-1}(k_i, y_i)$，仅产生哈希值 $h_i \stackrel{\mathrm{def}}{=} h(k_i, x_i) = y_i \oplus F^{-1}(k_i, y_i)$。关键在于，无论攻击者进行哪种查询，它所学到的哈希值 $h_i$ 几乎是均匀分布的（因为对 $F$ 或 $F^{-1}$ 的预言机查询结果几乎是均匀分布的——唯一偏离均匀之处在于，对任何 $x \neq x^{\prime}$，$F(k, x)$ 都不能等于 $F(k, x^{\prime})$）。这使得寻找碰撞变得困难，因为除非存在某个 $i \neq j$ 使 $h_i = h_j$，否则攻击者不会得到碰撞。

In detail: Fix $i, j$ with $i > j$ and consider the probability that $h_i = h_j$. At the time of the $i$th query, the value of $h_j$ is fixed. A collision between $h_i$ and $h_j$ is obtained on the $i$th query only if the attacker queries $(k_i, x_i)$ to $F$ and obtains the result $F(k_i, x_i) = h_j \oplus x_i$, or queries $(k_i, y_i)$ to $F^{-1}$ and obtains the result $F^{-1}(k_i, y_i) = h_j \oplus y_i$. Either event occurs with probability at most ${1}/(2^\ell - (i-1))$ since, for example, $F(k_i, x_i)$ is uniform over $\{0,1\}^\ell$ except that it cannot be equal to any value $F(k_i, x)$ already defined by the attacker's (at most) $i-1$ previous oracle queries using key $k_i$. Assuming $i \leq q < 2^{\ell/2}$ (if not, the theorem is trivially true), the probability that $h_i = h_j$ is at most ${2}/2^\ell$.

具体来说：固定 $i, j$（$i > j$），考虑 $h_i = h_j$ 的概率。在第 $i$ 次查询时，$h_j$ 的值已固定。只有当攻击者查询 $F$ 的 $(k_i, x_i)$ 并获得结果 $F(k_i, x_i) = h_j \oplus x_i$，或查询 $F^{-1}$ 的 $(k_i, y_i)$ 并获得结果 $F^{-1}(k_i, y_i) = h_j \oplus y_i$ 时，才在第 $i$ 次查询获得 $h_i$ 和 $h_j$ 的碰撞。两个事件的概率都至多为 ${1}/(2^\ell - (i-1))$，举例来说，$F(k_i, x_i)$ 在 $\{0,1\}^\ell$ 上均匀分布，只是它不能等于攻击者此前（至多）$i-1$ 次使用密钥 $k_i$ 的预言机查询已确定的任何值 $F(k_i, x)$。假设 $i \leq q < 2^{\ell/2}$（若不满足，定理平凡成立），$h_i = h_j$ 的概率至多为 ${2}/2^\ell$。

Taking a union bound over all $\binom{q}{2} < q^{2}/2$ distinct pairs $i, j$ gives the result stated in the theorem.

对所有 $\binom{q}{2} < q^{2}/2$ 个不同的对 $i, j$ 取联合界，即得定理所述结论。

Davies–Meyer and DES. As we have mentioned above, one must take care when instantiating the Davies–Meyer construction with any concrete block cipher, since the cipher must satisfy additional properties (beyond being a strong pseudorandom permutation) in order for the resulting construction to be secure. In Exercise 7.24 we explore what goes wrong when DES is used in the Davies–Meyer construction.

**Davies–Meyer 与 DES。**

如上所述，用任何具体的分组密码实例化 Davies–Meyer 构造时必须小心，因为该密码必须满足额外的性质（除作为强伪随机置换之外），所得构造才是安全的。在习题 7.24 中，我们探讨当 DES 用于 Davies–Meyer 构造时会出现什么问题。

This should serve as a warning that the proof of security for the Davies–Meyer construction in the ideal-cipher model does not necessarily translate into real-world security when instantiated with a specific cipher. Nevertheless, as we will describe below, this paradigm has been used to construct practical hash functions that have resisted attack (although in those cases the block cipher used was designed specifically for this purpose).

这提醒我们：Davies–Meyer 构造在理想密码模型中的安全性证明，在以具体密码实例化时并不必然转化为现实世界中的安全性。尽管如此，如下文所述，这一范式已被用于构造经受住攻击的实用哈希函数（尽管在那些情况下，所用的分组密码是专门为此目的设计的）。

In conclusion, the Davies–Meyer construction is a useful paradigm for constructing collision-resistant compression functions. However, it should not be applied to block ciphers not designed to behave like an ideal cipher.

总之，Davies–Meyer 构造是构造抗碰撞压缩函数的有用范式。然而，它不应当用于那些并非为表现得像理想密码而设计的分组密码。

### 7.3.2 MD5, SHA-1, and SHA-2　7.3.2 MD5、SHA-1 和 SHA-2

Several prominent and widely used hash functions have been constructed by applying the Davies–Meyer construction to some underlying block cipher to obtain a compression function, and then applying the Merkle–Damgård transform. Examples include the hash functions MD5, SHA-1, and SHA-2, which we discuss next.

几种著名的、广泛使用的哈希函数，都是先对某个底层分组密码应用 Davies–Meyer 构造以获得压缩函数，再应用 Merkle–Damgård 变换构造而成的。例子包括 MD5、SHA-1 和 SHA-2 哈希函数，我们接下来讨论它们。

MD5. MD5 is a hash function with a 128-bit output length. It was designed in 1991 and for some time was believed to be collision resistant. Over a period of several years, various weaknesses began to be found in MD5 but these did not appear to lead to any easy way to find collisions. Shockingly, in 2004 a team of Chinese cryptanalysts presented a new method for finding collisions in MD5 and demonstrated an explicit collision. Since then, the attack has been improved and today collisions in MD5 can be found in under a minute on a desktop PC. In addition, the attacks have been extended so that even "controlled collisions" (e.g., two pdf files) can be found. Due to these attacks, MD5 should not be used anywhere cryptographic security is needed. We mention MD5 only because it is still found in legacy code.

**MD5。**

MD5 是一种输出长度为 128 比特的哈希函数。它于 1991 年设计，一度被认为具有抗碰撞性。在随后数年间，人们陆续发现了 MD5 的各种弱点，但这些弱点似乎并未带来任何寻找碰撞的便捷途径。令人震惊的是，2004 年一个中国密码分析团队提出了一种在 MD5 中寻找碰撞的新方法，并展示了一个显式碰撞。此后，该攻击得到改进，如今在台式 PC 上不到一分钟即可找到 MD5 中的碰撞。此外，攻击还得到进一步扩展，甚至可以找到“受控碰撞”（例如两个 pdf 文件）。由于这些攻击，MD5 不应用于任何需要密码学安全性的场合。我们提及 MD5 仅仅是因为它仍然存在于遗留代码中。

SHA-1. The Secure Hash Algorithms (SHA) refer to a set of cryptographic hash functions standardized by NIST. The hash function SHA-1, standardized in 1995, has a 160-bit output length and was considered secure for many years. Beginning in 2005, theoretical analysis indicated that collisions in SHA-1 could be found using roughly ${2}^{69}$ hash-function evaluations, which is much lower than the ${2}^{80}$ hash-function evaluations that would be needed for a birthday attack. This prompted researchers to recommend migrating away from SHA-1; nevertheless, since even ${2}^{69}$ operations is still significant, an explicit collision in SHA-1 remained out of reach. It was not until 2017 that an improvement in the collision-finding attack, along with tremendous computational resources devoted by Google, enabled researchers to find an explicit collision. The attack required the equivalent of ${2}^{63}$ hash-function evaluations, and took 6,500 CPU years (along with 100 GPU years) to execute on a distributed cluster of machines. As of the time of this writing, more-devastating attacks have been found, and SHA-1 is no longer recommended for use.

**SHA-1。**

安全哈希算法（Secure Hash Algorithms，SHA）是指 NIST 标准化的一组密码学哈希函数。哈希函数 SHA-1 于 1995 年标准化，输出长度为 160 比特，多年来被认为是安全的。从 2005 年开始，理论分析表明使用大约 ${2}^{69}$ 次哈希函数求值即可找到 SHA-1 中的碰撞，这远低于生日攻击所需的 ${2}^{80}$ 次哈希函数求值。这促使研究人员建议弃用 SHA-1；然而，由于 ${2}^{69}$ 次运算本身仍是相当大的计算量，SHA-1 的显式碰撞依然遥不可及。直到 2017 年，碰撞寻找攻击的改进以及 Google 投入的大量计算资源才使研究人员找到了一个显式碰撞。该攻击需要相当于 ${2}^{63}$ 次哈希函数求值，在一个分布式机器集群上执行耗时 6,500 CPU 年（以及 100 GPU 年）。截至撰写本文时，已发现更具破坏性的攻击，SHA-1 不再被推荐使用。

SHA-2. The SHA-2 hash family, introduced in 2001, consists of the two related hash functions SHA-256 and SHA-512 with 256- and 512-bit output lengths, respectively. (The outputs can be truncated if smaller hash values are desired.) These hash functions do not currently appear to have the same weaknesses that led to attacks on SHA-1; moreover, because of their long output lengths, it will remain difficult to find collisions even if small weaknesses are discovered. SHA-2, or the more recent standard SHA-3 (see below), are currently recommended when collision-resistant hashing is needed.

**SHA-2。**

SHA-2 哈希族于 2001 年引入，由两个相关的哈希函数 SHA-256 和 SHA-512 组成，输出长度分别为 256 和 512 比特。（如果需要更小的哈希值，输出可以被截断。）这些哈希函数目前似乎不具有导致 SHA-1 被攻击的同类弱点；此外，由于输出长度很长，即使发现小弱点，寻找碰撞仍将很困难。当需要抗碰撞哈希时，目前推荐使用 SHA-2 或更新的标准 SHA-3（见下文）。

### 7.3.3 The Sponge Construction and SHA-3 (Keccak)　7.3.3 海绵构造与 SHA-3（Keccak）

In the aftermath of the collision attack on MD5 and the theoretical weaknesses found in SHA-1, NIST announced in 2007 a public competition to design a new cryptographic hash function. As in the case of the AES competition from roughly a decade earlier, the competition was completely open and transparent; anyone could submit an algorithm for consideration, and the public was invited to give their opinions on any of the candidates. The 51 first-round candidates were narrowed down to 14 in December 2008, and these were further reduced to five finalists in 2010. These remaining candidates were subject to intense scrutiny by the cryptographic community over the next two years. In October 2012, NIST announced the selection of Keccak as the winner of the competition. The resulting standard SHA-3, released in 2015, supports 224-, 256-, 384-, and 512-bit output lengths.

在 MD5 碰撞攻击和 SHA-1 理论弱点被发现之后，NIST 于 2007 年宣布了一项设计新密码学哈希函数的公开竞赛。与大约十年前的 AES 竞赛一样，该竞赛完全开放和透明；任何人都可以提交算法供考虑，公众也被邀请对任何候选方案发表意见。51 个第一轮候选方案在 2008 年 12 月缩减为 14 个，并在 2010 年进一步缩减为五个入围方案。在接下来的两年中，这些候选方案受到了密码学界的严格审查。2012 年 10 月，NIST 宣布选择 Keccak 作为竞赛的获胜者。由此产生的标准 SHA-3 于 2015 年发布，支持 224、256、384 和 512 比特输出长度。

The structure of Keccak is very different from the structure of SHA-1 and SHA-2, and in particular it does not use the Merkle–Damgård transform. (Interestingly, this may have been one of the reasons it was chosen.) The core primitive of Keccak is an unkeyed permutation $P$ with a large block length of 1600 bits. $P$ is used to build a hash function directly (i.e., without first building a compression function in an intermediate step) via what is known as the sponge construction. The resulting hash function can be proven to be collision resistant if $P$ is modeled as a random permutation. (We have already seen the random-permutation model in Section 7.1.5.) By analogy with the random-oracle and ideal-cipher models, the random-permutation model assumes that all parties are given access to oracles for a uniform permutation $P$ as well as its inverse $P^{-1}$; the only way to compute $P$ or $P^{-1}$ is to explicitly query those oracles. Note that the random-permutation model is weaker than the ideal-cipher model; indeed, we can easily obtain a random permutation $P$ from an ideal cipher $F$ by defining $P(x) \overset{\mathrm{def}}{=} F(0^n, x)$, i.e., by simply fixing the key for $F$ to any constant value.

Keccak 的结构与 SHA-1 和 SHA-2 的结构非常不同，特别是它不使用 Merkle–Damgård 变换。（有趣的是，这可能是它被选中的原因之一。）Keccak 的核心原语是一个无密钥置换 $P$，分组长度高达 1600 比特。借助所谓的海绵构造，$P$ 被直接用于构建哈希函数（即无需先在中间步骤构建压缩函数）。如果 $P$ 被建模为随机置换，可以证明所得哈希函数是抗碰撞的。（我们在 7.1.5 节中已经见过随机置换模型。）类似于随机预言机和理想密码模型，随机置换模型假设所有参与方都可以访问分别给出均匀置换 $P$ 及其逆 $P^{-1}$ 的预言机；计算 $P$ 或 $P^{-1}$ 的唯一方式是显式查询这些预言机。注意，随机置换模型弱于理想密码模型；事实上，从理想密码 $F$ 容易得到随机置换 $P$：定义 $P(x) \overset{\mathrm{def}}{=} F(0^n, x)$，即简单地将 $F$ 的密钥固定为任意常数值。

We now describe the construction. Fix a permutation $P: \{0,1\}^{\ell} \to \{0,1\}^{\ell}$, and let $r,c,v \geq 1$ be such that $r+c=\ell$ and $v\leq\ell$. The sponge construction accepts as input a sequence of $r$-bit blocks $m_1,\ldots,m_t$. (See Figure 7.12.)

我们现在描述该构造。固定置换 $P: \{0,1\}^{\ell} \to \{0,1\}^{\ell}$，令 $r,c,v \geq 1$ 满足 $r+c=\ell$ 且 $v\leq\ell$。海绵构造接受 $r$ 比特块序列 $m_1,\ldots,m_t$ 作为输入。（见图 7.12。）

![Image](https://lsky.jerryxue.top/i/2026/08/19/6a85c5582882f.jpg)

**FIGURE 7.12: The sponge construction. The absorbing phase is to the left of the dashed line, and the squeezing phase is to the right.**

**图 7.12：海绵构造。吸收阶段在虚线左侧，挤出阶段在右侧。**

During its computation, the construction maintains an $\ell$-bit state, initialized to zero. This state is modified in an input-dependent way during an "absorbing phase," and the final state is then used to generate output in a "squeezing phase." (Hence the name "sponge.") When processing the $i$th block during the absorbing phase, the state is updated from $y_{i-1}$ to $y_i$ by XORing $m_i$ with the first $r$ bits of $y_{i-1}$ to obtain an intermediate value $x_i$, and then setting $y_i := P(x_i)$. The final state $y_t$ is then used to generate output in the squeezing phase by repeatedly outputting the initial $v$ bits of the state followed by an application of $P$.

在计算过程中，该构造维护一个 $\ell$ 比特状态，初始化为零。该状态在“吸收阶段”中以依赖于输入的方式被修改，然后最终状态在“挤出阶段”中被用来生成输出。（因此得名“海绵”。）在吸收阶段处理第 $i$ 个块时，状态从 $y_{i-1}$ 更新为 $y_i$，方式是将 $m_i$ 与 $y_{i-1}$ 的前 $r$ 个比特异或得到中间值 $x_i$，然后设 $y_i := P(x_i)$。最终状态 $y_t$ 随后在挤出阶段中用于生成输出：重复地先输出状态的前 $v$ 个比特，再应用一次 $P$。

The sponge construction can be used for many purposes. In Construction 7.6 we provide a formal description of how to use it to build a hash function. That construction includes a parameter $\lambda \geq 1$ that affects how many times the squeezing step is run, and thus determines the output length of the hash. (Namely, the output is a string of length $\lambda \cdot v$.) The construction also incorporates an initial padding step so that the resulting hash function can accept inputs of arbitrary length.

海绵构造可用于多种目的。在构造 7.6 中，我们提供了如何用它构建哈希函数的形式化描述。该构造包含一个参数 $\lambda \geq 1$，它影响挤出步骤运行的次数，从而决定哈希的输出长度。（即输出是长度为 $\lambda \cdot v$ 的串。）该构造还包含一个初始填充步骤，使所得哈希函数可以接受任意长度的输入。

Hash functions following the sponge construction can be shown to satisfy several security properties when P is modeled as a random permutation. Here we prove collision resistance as long as r and c are sufficiently large, assuming for simplicity that $\lambda = 1$ (which is the case for the SHA-3 standard).

当 P 被建模为随机置换时，可以证明遵循海绵构造的哈希函数满足若干安全性质。这里我们在 $r$ 和 $c$ 足够大的条件下证明抗碰撞性，为简单起见假设 $\lambda = 1$（SHA-3 标准即如此）。

> **CONSTRUCTION 7.6**　**构造 7.6**
>
> Fix $P : \{0,1\}^{\ell} \to \{0,1\}^{\ell}$ and constants $r,c,v$ as in the text and $\lambda \geq 1$.
>
> Hash function $H$, on input $\hat{m} \in \{0,1\}^*$, does:
>
> (Padding) Append a 1 to $\hat{m}$, followed by enough zeros so that the length of the resulting string is a multiple of $r$. Parse the resulting string as the sequence of $r$-bit blocks $m_1, \ldots, m_t$.
>
> (Absorbing phase) Set $y_0 := 0^{\ell}$. Then for $i = 1, \ldots, t$ do:
> - $x_i := y_{i-1} \oplus (m_i \| 0^c)$.
> - $y_i := P(x_i)$.
>
> (Squeezing phase) Set $y_1^* := y_t$, and let $h_1$ be the first $v$ bits of $y_1^*$. Then for $i = 2, \ldots, \lambda$ do
> - $y_i^* := P(y_{i-1}^*)$.
> - Let $h_i$ be the first $v$ bits of $y_i^*$.
>
> (Output) Output $h_1 \| \cdots \| h_\lambda$.
>
> A hash function based on the sponge construction.
>
> 固定 $P : \{0,1\}^{\ell} \to \{0,1\}^{\ell}$ 以及如正文所述的常数 $r,c,v$ 和 $\lambda \geq 1$。
>
> 哈希函数 $H$，输入 $\hat{m} \in \{0,1\}^*$，执行：
>
> （填充）向 $\hat{m}$ 追加一个 1，然后追加足够多的零，使所得串的长度为 $r$ 的倍数。将所得串解析为 $r$ 比特块序列 $m_1, \ldots, m_t$。
>
> （吸收阶段）设 $y_0 := 0^{\ell}$。然后对 $i = 1, \ldots, t$ 执行：
> - $x_i := y_{i-1} \oplus (m_i \| 0^c)$。
> - $y_i := P(x_i)$。
>
> （挤出阶段）设 $y_1^* := y_t$，令 $h_1$ 为 $y_1^*$ 的前 $v$ 个比特。然后对 $i = 2, \ldots, \lambda$ 执行
> - $y_i^* := P(y_{i-1}^*)$。
> - 令 $h_i$ 为 $y_i^*$ 的前 $v$ 个比特。
>
> （输出）输出 $h_1 \| \cdots \| h_\lambda$。
>
> 基于海绵构造的哈希函数。

**THEOREM 7.7** Let H denote Construction 7.6 with $\lambda = 1$. If P is modeled as a random permutation, then any attacker making q queries to P or $P^{-1}$ can find a collision in H with probability at most $\frac{q^2}{2^v} + \frac{q \cdot (q+1)}{2^c}$.

**定理 7.7** 令 H 表示 $\lambda = 1$ 时的构造 7.6。如果 P 被建模为随机置换，则任何对 P 或 $P^{-1}$ 进行 $q$ 次查询的攻击者，在 H 中找到碰撞的概率至多为 $\frac{q^2}{2^v} + \frac{q \cdot (q+1)}{2^c}$。

**PROOF** Consider an attacker that is given oracle access to a random permutation $P$ and its inverse $P^{-1}$, and then outputs a pair of distinct messages; let $m_1, \ldots, m_t$ and $m^{\prime}_1, \ldots, m^{\prime}_{t^{\prime}}$ denote the results after padding. (Note that, because of the way padding is done, these padded messages are also distinct.)

**证明** 考虑一个攻击者，它拥有对随机置换 $P$ 及其逆 $P^{-1}$ 的预言机访问权限，然后输出一对不同的消息；令 $m_1, \ldots, m_t$ 和 $m^{\prime}_1, \ldots, m^{\prime}_{t^{\prime}}$ 表示填充后的结果。（注意，由于填充方式的原因，这些填充后的消息也是不同的。）

We assume the attacker never makes the same query to P or $P^{-1}$ more than once, and never queries $P^{-1}(y)$ once it has learned that $y = P(x)$ (and vice versa). We further assume that by the end of its execution the attacker has made the oracle queries necessary to evaluate H on the messages it outputs.

我们假设攻击者从不对 P 或 $P^{-1}$ 重复同一查询，且一旦得知 $y = P(x)$ 就不再查询 $P^{-1}(y)$（反之亦然）。我们进一步假设，攻击者在执行结束时已经进行了所需的预言机查询，从而能在其输出的消息上计算 H。

Define the following three events:

定义以下三个事件：

E1: The attacker makes two distinct queries to P whose results agree on their first v bits.

E1：攻击者对 P 进行两次不同的查询，其结果的前 v 个比特相同。

E2: The attacker makes a query to P or $P^{-1}$ whose result has its last c bits equal to ${0}^{c}$.

E2：攻击者对 P 或 $P^{-1}$ 进行一次查询，其结果的最后 c 个比特等于 ${0}^{c}$。

E3: The attacker makes two distinct queries (to either P or $P^{-1}$) whose results agree on their last c bits.

E3：攻击者进行两次不同的查询（对 P 或 $P^{-1}$），其结果的最后 c 个比特相同。

We show that if the attacker outputs a collision then one of the above events occurs; we complete the proof by bounding the probabilities of these events.

我们证明如果攻击者输出一个碰撞，则上述事件之一必然发生；然后通过界定这些事件的概率来完成证明。

**CLAIM 7.8** If the attacker outputs a collision then E1, E2, or E3 occurs.

**断言 7.8** 如果攻击者输出一个碰撞，则 E1、E2 或 E3 发生。

**PROOF** Consider the execution of Construction 7.6 on the padded message $m_1, \ldots, m_t$. Let $y_0, x_1, y_1, \ldots, x_t, y_t$ be the values of the variables during the course of the execution, so that $y_0 = 0^\ell$ and, for $i \geq 1$, the last $c$ bits of $y_{i-1}$ and $x_i$ are equal and $y_i = P(x_i)$. Define $y^{\prime}_0, x^{\prime}_1, y^{\prime}_1, \ldots, x^{\prime}_{t^{\prime}}, y^{\prime}_{t^{\prime}}$ analogously with respect to the padded message $m^{\prime}_1, \ldots, m^{\prime}_{t^{\prime}}$. If, for some $i$, the attacker queried $P^{-1}(y_i)$ to obtain $x_i$ or queried $P^{-1}(y^{\prime}_i)$ to obtain $x^{\prime}_i$ then we say an inverse query occurred. We consider two cases:

**证明** 考虑构造 7.6 在填充消息 $m_1, \ldots, m_t$ 上的执行。令 $y_0, x_1, y_1, \ldots, x_t, y_t$ 为执行过程中各变量的值，其中 $y_0 = 0^\ell$，且对 $i \geq 1$，$y_{i-1}$ 和 $x_i$ 的最后 $c$ 个比特相等，$y_i = P(x_i)$。对填充消息 $m^{\prime}_1, \ldots, m^{\prime}_{t^{\prime}}$ 类似地定义 $y^{\prime}_0, x^{\prime}_1, y^{\prime}_1, \ldots, x^{\prime}_{t^{\prime}}, y^{\prime}_{t^{\prime}}$。如果对某个 $i$，攻击者查询了 $P^{-1}(y_i)$ 以获得 $x_i$ 或查询了 $P^{-1}(y^{\prime}_i)$ 以获得 $x^{\prime}_i$，则我们说发生了一次逆查询。我们分两种情形：

Case 1: An inverse query occurred. Assume without loss of generality an inverse query occurred for the first padded message. Let $i$ be minimal such that the attacker queried $P^{-1}(y_i)$ to obtain $x_i$. If $i = 1$ then the last $c$ bits of $x_1$ are ${0}^c$ and $\mathbf{E2}$ occurred. Otherwise, the last $c$ bits of $y_{i-1} = P(x_{i-1})$ and $x_i = P^{-1}(y_i)$ are equal and so $\mathbf{E3}$ occurred.

情形 1：发生了逆查询。不失一般性地假设逆查询发生在第一个填充消息上。设 $i$ 是使攻击者查询 $P^{-1}(y_i)$ 获得 $x_i$ 的最小指标。如果 $i = 1$，则 $x_1$ 的最后 $c$ 个比特为 ${0}^c$，$\mathbf{E2}$ 发生。否则，$y_{i-1} = P(x_{i-1})$ 和 $x_i = P^{-1}(y_i)$ 的最后 $c$ 个比特相等，因此 $\mathbf{E3}$ 发生。

Case 2: No inverse query occurred. If $y_t \neq y^{\prime}_{t^{\prime}}$, then the first v bits of $y_t$ and $y^{\prime}_{t^{\prime}}$ are equal (since the attacker output a collision) even though $x_t \neq x^{\prime}_{t^{\prime}}$. Since no inverse query occurred, the attacker must have queried $P(x_t)$ and $P(x^{\prime}_{t^{\prime}})$ and so E1 occurred.

情形 2：没有发生逆查询。如果 $y_t \neq y^{\prime}_{t^{\prime}}$，则尽管 $x_t \neq x^{\prime}_{t^{\prime}}$，$y_t$ 与 $y^{\prime}_{t^{\prime}}$ 的前 v 个比特却相等（因为攻击者输出了一个碰撞）。由于没有逆查询发生，攻击者必定查询了 $P(x_t)$ 和 $P(x^{\prime}_{t^{\prime}})$，因此 E1 发生。

If $y_t = y_{t^{\prime}}^{\prime}$, assume without loss of generality that $t^{\prime} \geq t$. Let $C(z)$ denote the last $c$ bits of an $\ell$-bit string $z$. Take ${0} \leq i \leq t$ maximal such that $(C(y_{t-i}), \ldots, C(y_t)) = (C(y_{t^{\prime}-i}), \ldots, C(y_{t^{\prime}}))$. If $i < t$ then $C(y_{t-i-1}) \neq C(y_{t^{\prime}-i-1})$ and hence $x_{t-i} \neq x_{t^{\prime}-i}$, but

如果 $y_t = y_{t^{\prime}}^{\prime}$，不失一般性地假设 $t^{\prime} \geq t$。令 $C(z)$ 表示 $\ell$ 比特串 $z$ 的最后 $c$ 个比特。取 ${0} \leq i \leq t$ 为使 $(C(y_{t-i}), \ldots, C(y_t)) = (C(y_{t^{\prime}-i}), \ldots, C(y_{t^{\prime}}))$ 成立的最大值。如果 $i < t$，则 $C(y_{t-i-1}) \neq C(y_{t^{\prime}-i-1})$，因而 $x_{t-i} \neq x_{t^{\prime}-i}$，但

$$
C(P(x_{t-i}))=C(y_{t-i})=C(y_{t^{\prime}-i}^{\prime})=C(P(x_{t^{\prime}-i}^{\prime}))
$$

and so $\mathbf{E3}$ occurred. If $i = t$ and $t^{\prime} > t$ then $C(P(x^{\prime}_{t^{\prime}-i})) = C(y^{\prime}_{t^{\prime}-i}) = C(y_0) = 0^c$; thus, $\mathbf{E2}$ occurred. If $i = t$ and $t^{\prime} = t$ then we have $(C(y_0), \ldots, C(y_t)) = (C(y^{\prime}_0), \ldots, C(y^{\prime}_t))$. Let $j$ be minimal such that $m_j \neq m^{\prime}_j$ (such a $j$ must exist since the padded messages are distinct). Then $y_{j-1} = y^{\prime}_{j-1}$, but $x_j \neq x^{\prime}_j$, and yet

因此 $\mathbf{E3}$ 发生。如果 $i = t$ 且 $t^{\prime} > t$，则 $C(P(x^{\prime}_{t^{\prime}-i})) = C(y^{\prime}_{t^{\prime}-i}) = C(y_0) = 0^c$；因此 $\mathbf{E2}$ 发生。如果 $i = t$ 且 $t^{\prime} = t$，则我们有 $(C(y_0), \ldots, C(y_t)) = (C(y^{\prime}_0), \ldots, C(y^{\prime}_t))$。设 $j$ 为使 $m_j \neq m^{\prime}_j$ 的最小指标（这样的 $j$ 必然存在，因为填充后的消息是不同的）。则 $y_{j-1} = y^{\prime}_{j-1}$，但 $x_j \neq x^{\prime}_j$，而

$$
C(P(x_{j}))=C(y_{j})=C(y_{j}^{\prime})=C(P(x_{j}^{\prime}))
$$

and so E3 occurred.

因此 E3 发生。

**CLAIM 7.9** $\Pr[E1 \lor E2 \lor E3] \leq \frac{q^2}{2^v} + \frac{q \cdot (q+1)}{2^c}$.

**断言 7.9** $\Pr[E1 \lor E2 \lor E3] \leq \frac{q^2}{2^v} + \frac{q \cdot (q+1)}{2^c}$。

**PROOF** We bound the probability of each event; a union bound yields the claim. It is easy to see that $\Pr[\mathbf{E2}] \leq q/2^c$. To bound $\Pr[\mathbf{E1}]$ we use an analysis similar to the one used to prove the birthday bound (cf. Appendix A.4). Let $\mathsf{Coll}_{i,j}$ be the event that the results of the $i$th and $j$th queries of the attacker agree on their first $v$ bits. We have $\Pr[\mathsf{Coll}_{i,j}] \leq 2^{\ell - v}/(2^{\ell} - 1) \leq 2 \cdot 2^{-v}$. (Taking into account that $P$ is a random permutation.) So

**证明** 我们界定每个事件的概率；取联合界即得断言。容易看出 $\Pr[\mathbf{E2}] \leq q/2^c$。为界定 $\Pr[\mathbf{E1}]$，我们采用与证明生日界（参见附录 A.4）类似的分析。令 $\mathsf{Coll}_{i,j}$ 为攻击者第 $i$ 次和第 $j$ 次查询的结果在前 $v$ 个比特上一致的事件。我们有 $\Pr[\mathsf{Coll}_{i,j}] \leq 2^{\ell - v}/(2^{\ell} - 1) \leq 2 \cdot 2^{-v}$。（考虑到 $P$ 是随机置换。）所以

$$
\Pr[\mathbf{E}\mathbf{1}]=\Pr\left[\bigvee_{i<j}\mathsf{Coll}_{i,j}\right]\leq\sum_{i<j}\Pr[\mathsf{Coll}_{i,j}]\leq\binom{q}{2}\cdot2\cdot2^{-v}\leq q^{2}/2^{v}.
$$

A similar argument gives $\Pr[\mathbf{E3}] \leq q^2/2^c$.

类似的论证给出 $\Pr[\mathbf{E3}] \leq q^2/2^c$。

This concludes the proof of the theorem.

至此完成定理的证明。

### References and Additional Reading　参考文献与补充阅读

Lidl and Niederreiter [130] give the standard treatment of LFSRs. Additional information on LFSRs in the context of cryptography can be found in the Handbook of Applied Cryptography [137] or the text by Paar and Pelzl [156]. Further details about eSTREAM, as well as a document describing the design of Trivium, can be found at https://www.ecrypt.eu.org/stream.

Lidl 和 Niederreiter [130] 给出了 LFSR 的标准论述。关于 LFSR 在密码学中的更多信息可参见《应用密码学手册》[137] 或 Paar 和 Pelzl 的教材 [156]。关于 eSTREAM 的更多细节以及描述 Trivium 设计的文档可在 https://www.ecrypt.eu.org/stream 找到。

The work of AlFardan et al. [9] surveys recent attacks on RC4. ChaCha20 is due to Bernstein [29], and is described in RFC 8439 [154]. It can be analyzed (in the random-permutation model) as an Even-Mansour cipher [70].

AlFardan 等人 [9] 的工作综述了最近对 RC4 的攻击。ChaCha20 由 Bernstein [29] 提出，并在 RFC 8439 [154] 中描述。它可以在随机置换模型中被分析为 Even-Mansour 密码 [70]。

The confusion-diffusion paradigm and substitution-permutation networks were introduced by Shannon [177] and Feistel [71]. See the thesis of Heys [98] for further information regarding SPN design. A theoretical analysis of block ciphers based on SPNs has recently been given by Cogliati et al. [52]. We remark that SPNs are useful not only for building ciphers, but also for increasing the block length of an existing cipher.

混淆-扩散范式和代换-置换网络由 Shannon [177] 和 Feistel [71] 引入。关于 SPN 设计的更多信息参见 Heys 的论文 [98]。Cogliati 等人 [52] 最近给出了基于 SPN 的分组密码的理论分析。我们指出，SPN 不仅可用于构造密码，还可用于增加现有密码的分组长度。

Feistel networks were first described in 1973 [71]. A theoretical analysis of Feistel networks was given by Luby and Rackoff [132]; see Chapter 8.

Feistel 网络于 1973 年首次被描述 [71]。Luby 和 Rackoff [132] 给出了 Feistel 网络的理论分析；参见第 8 章。

More details on DES, AES, and block-cipher constructions in general can be found in the text by Knudsen and Robshaw [117]. The meet-in-the-middle attack on double encryption is due to Diffie and Hellman [66]. The attack on two-key triple encryption mentioned in the text (and explored in Exercise 7.16) is by Merkle and Hellman [141] and has been developed further [197, 144]. Positive results about double/triple encryption are also known [6, 27].

关于 DES、AES 和分组密码构造的更多细节可参见 Knudsen 和 Robshaw 的教材 [117]。对双重加密的中间相遇攻击由 Diffie 和 Hellman [66] 提出。正文中提到的对双密钥三重加密的攻击（习题 7.16 中探讨）由 Merkle 和 Hellman [141] 提出，并已得到进一步发展 [197, 144]。关于双重/三重加密也有已知的正面结果 [6, 27]。

Work of Bhargavan and Leurent [33] demonstrates real-world security implications of using ciphers (like DES or 3DES) with small block length. See https://sweet32.info for further information.

Bhargavan 和 Leurent [33] 的工作展示了使用小分组长度密码（如 DES 或 3DES）的现实安全影响。更多信息参见 https://sweet32.info。

Differential cryptanalysis was introduced by Biham and Shamir [34], and its application to DES is described in a book by those authors [35]. Coppersmith [53] describes design principles of the DES S-boxes in light of the public discovery of differential cryptanalysis. Linear cryptanalysis was discovered by Matsui [134]. For more information on these advanced cryptanalytic techniques, we refer the reader to the tutorial on differential and linear cryptanalysis by Heys [99] or the book by Knudsen and Robshaw [117].

差分密码分析由 Biham 和 Shamir [34] 引入，两位作者在著作 [35] 中描述了它在 DES 上的应用。鉴于差分密码分析被公开发现，Coppersmith [53] 描述了 DES S 盒的设计原则。线性密码分析由 Matsui [134] 发现。关于这些高级密码分析技术的更多信息，我们推荐读者参考 Heys [99] 的差分和线性密码分析教程或 Knudsen 和 Robshaw 的著作 [117]。

Menezes et al. [137] give further information about MD5 and SHA-1; note, though, that their treatment pre-dates the recent attacks on those hash functions. Various other constructions of compression functions from block ciphers are known [164, 37]. The sponge construction is described and analyzed by Bertoni et al. [32]. For additional details about the SHA-3 competition, see https://csrc.nist.gov/projects/hash-functions/sha-3-project.

Menezes 等人 [137] 给出了关于 MD5 和 SHA-1 的更多信息；但请注意，他们的论述早于最近对这些哈希函数的攻击。从分组密码构造压缩函数的其他各种方法也是已知的 [164, 37]。海绵构造由 Bertoni 等人 [32] 描述和分析。关于 SHA-3 竞赛的更多细节，参见 https://csrc.nist.gov/projects/hash-functions/sha-3-project。

The first explicit collision in SHA-1 was found in 2017 by Stevens et al. [192]; improved attacks, which have serious practical security implications, have been shown even more recently [127, 128].

SHA-1 中的第一个显式碰撞由 Stevens 等人 [192] 于 2017 年找到；更近期还出现了改进的攻击（具有严重的实际安全影响）[127, 128]。

### Exercises　习题

7.1 Consider a degree-6 LFSR where only $c_{5}$ and $c_{0}$ are set to 1.

7.1 考虑一个次数为 6 的 LFSR，其中仅 $c_{5}$ 和 $c_{0}$ 设为 1。

(a) What are the first 10 bits output by this LFSR if it starts in initial state $(s_{5}, s_{4}, s_{3}, s_{2}, s_{1}, s_{0}) = (1, 1, 1, 1, 1, 1)$?

(a) 如果该 LFSR 以初始状态 $(s_{5}, s_{4}, s_{3}, s_{2}, s_{1}, s_{0}) = (1, 1, 1, 1, 1, 1)$ 开始，其输出的前 10 个比特是什么？

(b) Is this LFSR maximum length?

(b) 该 LFSR 是最大长度的吗？

7.2 Consider a degree-7 LFSR where only $c_{6}, c_{1}$, and $c_{0}$ are set to 1.

7.2 考虑一个次数为 7 的 LFSR，其中仅 $c_{6}, c_{1}$ 和 $c_{0}$ 设为 1。

(a) What are the first 10 bits output by this LFSR if it starts in the initial state $(s_6, s_5, s_4, s_3, s_2, s_1, s_0) = (0, 0, 0, 0, 0, 0, 1)$?

(a) 如果该 LFSR 以初始状态 $(s_6, s_5, s_4, s_3, s_2, s_1, s_0) = (0, 0, 0, 0, 0, 0, 1)$ 开始，其输出的前 10 个比特是什么？

(b) Show that this LFSR is not maximum length.

(b) 证明该 LFSR 不是最大长度的。

Hint: Find a nonzero state with a self-loop in the transition graph.

提示：在状态转移图中找到一个具有自环的非零状态。

7.3 Consider a stream cipher constructed from a degree-$n$ LFSR where the output at each clock tick is not $s_0$, but instead $g(s_{n-1}, \ldots, s_0)$ for some nonlinear function $g$. The $n$-bit key of the stream cipher is used as the initial state of the LFSR. Show that this does not result in a secure stream cipher for the following choices of $g$:

7.3 考虑一个由次数为 $n$ 的 LFSR 构造的流密码，其中每个时钟节拍的输出不是 $s_0$，而是某个非线性函数 $g$ 的值 $g(s_{n-1}, \ldots, s_0)$。该流密码的 $n$ 比特密钥用作 LFSR 的初始状态。证明对于下列 $g$ 的取值，这样构造出来的都不是安全的流密码：

(a) $g(s_{n-1}, \ldots, s_0) = s_0 \land s_1$.

(a) $g(s_{n-1}, \ldots, s_0) = s_0 \land s_1$。

(b) $g(s_{n-1}, \ldots, s_0) = s_2 \oplus (s_1 \land s_0)$.

(b) $g(s_{n-1}, \ldots, s_0) = s_2 \oplus (s_1 \land s_0)$。

7.4 Consider a stream cipher constructed from two LFSRs $A$ and $B$ of degrees $n_a$ and $n_b$, respectively, where the output at each clock tick is computed by taking the AND of the outputs of the two LFSRs. The key $k \in \{0,1\}^{n_a+n_b}$ is used to set the initial states of the two LFSRs.

7.4 考虑一个由两个次数分别为 $n_a$ 和 $n_b$ 的 LFSR $A$ 和 $B$ 构造的流密码，其中每个时钟节拍的输出通过取两个 LFSR 输出的 AND 来计算。密钥 $k \in \{0,1\}^{n_a+n_b}$ 用于设置两个 LFSR 的初始状态。

(a) Show that this is never a secure stream cipher.

(a) 证明这样构造的永远不是安全的流密码。

(b) Show that given a long enough output from this stream cipher, it is possible to recover the key in time $\approx 2^{n_a} + 2^{n_b}$.

(b) 证明给定该流密码足够长的输出，可以在 $\approx 2^{n_a} + 2^{n_b}$ 时间内恢复密钥。

7.5 Fix a public, invertible permutation $P$, and define the keyed function $F_k(x) \stackrel{\mathrm{def}}{=} P(\text{const}\|k\|x)$. Show that $F$ is not a pseudorandom function.

7.5 固定一个公开的可逆置换 $P$，定义带密钥函数 $F_k(x) \stackrel{\mathrm{def}}{=} P(\text{const}\|k\|x)$。证明 $F$ 不是伪随机函数。

7.6 Let F be a block cipher with n-bit key length and block length. Say there is a key-recovery attack on F that succeeds with probability 1 using n chosen plaintexts and minimal computational effort. Prove formally that F cannot be a pseudorandom permutation.

7.6 设 $F$ 是密钥长度和分组长度均为 $n$ 比特的分组密码。假设存在一个对 $F$ 的密钥恢复攻击，使用 $n$ 个选择明文以概率 1 成功且只需最小计算量。形式化地证明 $F$ 不可能是伪随机置换。

7.7 In our attack on a one-round SPN, we considered a block length of 64 bits and 8 S-boxes that each take an 8-bit input. Repeat the analysis for the case of 16 S-boxes, each taking a 4-bit input. What is the complexity of the attack now? Repeat the analysis again with a 128-bit block length and 16 S-boxes that each take an 8-bit input.

7.7 在我们对一轮 SPN 的攻击中，我们考虑的是 64 比特分组长度和 8 个各接受 8 比特输入的 S 盒。对 16 个 S 盒、每个接受 4 比特输入的情况重复分析。现在攻击的复杂度是多少？再用 128 比特分组长度和 16 个 S 盒（每个接受 8 比特输入）重复分析。

7.8 Consider a modified SPN that first applies $r$ rounds of key mixing (using independent sub-keys), then carries out $r$ rounds of substitution (using different $S$-boxes in each round), and finally applies $r$ (different) mixing permutations. Show an attack on this construction.

7.8 考虑一个修改的 SPN，它首先应用 $r$ 轮密钥混合（使用独立的子密钥），然后执行 $r$ 轮代换（每轮使用不同的 S 盒），最后应用 $r$ 个（不同的）混合置换。展示对此构造的攻击。

7.9 In this question we assume a two-round SPN with 64-bit block length.

7.9 本题假设一个 64 比特分组长度的两轮 SPN。

(a) Assume independent 64-bit sub-keys are used in each round, so the master key is 192 bits long. Show a key-recovery attack using much less than ${2}^{192}$ time.

(a) 假设每轮使用独立的 64 比特子密钥，因此主密钥长 192 比特。展示一个耗时远少于 ${2}^{192}$ 的密钥恢复攻击。

(b) Assume the first and third sub-keys are equal, and the second sub-key is independent, so the master key is 128 bits long. Show a key-recovery attack using much less than ${2}^{128}$ time.

(b) 假设第一个和第三个子密钥相等，第二个子密钥独立，因此主密钥长 128 比特。展示一个耗时远少于 ${2}^{128}$ 的密钥恢复攻击。

7.10 What is the output of an r-round Feistel network when the input is $(L_{0}, R_{0})$ in each of the following two cases:

7.10 当输入为 $(L_{0}, R_{0})$ 时，$r$ 轮 Feistel 网络在以下两种情况下的输出分别是什么：

(a) Each round function outputs all 0s, regardless of the input.

(a) 每个轮函数无论输入如何都输出全 0。

(b) Each round function is the identity function.

(b) 每个轮函数是恒等函数。

7.11 Let $\mathsf{Feistel}_{f_1,f_2}(\cdot)$ denote a two-round Feistel network using functions $f_1$ and $f_2$ (in that order). Define $\text{swap}(L,R)=(R,L)$.

7.11 令 $\mathsf{Feistel}_{f_1,f_2}(\cdot)$ 表示使用函数 $f_1$ 和 $f_2$（以此顺序）的两轮 Feistel 网络。定义 $\text{swap}(L,R)=(R,L)$。

(a) Show that if

(a) 证明如果

$$
(L_{2},R_{2})=\mathsf{swap}(\mathsf{Feistel}_{f_{1},f_{2}}(L_{0},R_{0}))
$$

then

则

$$
(L_{0},R_{0})=\mathsf{swap}(\mathsf{Feistel}_{f_{2},f_{1}}(L_{2},R_{2})).
$$

(b) Show that if

(b) 证明如果

$$
(L_{16},R_{16})=\mathrm{swap}\left(\mathrm{Feistel}_{f_{15},f_{16}}(\cdots(\mathrm{Feistel}_{f_{1},f_{2}}(L_{0},R_{0}))\cdots)\right)
$$

then

则

$$
(L_{0},R_{0})=\mathsf{swap}\left(\mathsf{Feistel}_{f_{2},f_{1}}(\cdots\mathsf{Feistel}_{f_{16},f_{15}}(L_{16},R_{16})\cdots)\right).
$$

7.12 For this exercise, rely on the description of DES given in this chapter. However, use the fact that in the actual construction of DES the two halves of the output of the final round of the Feistel network are swapped. That is, if the output of the final round of the Feistel network is $(L_{16}, R_{16})$, then the output of DES is $(R_{16}, L_{16})$.

7.12 本题依赖本章给出的 DES 描述。但请利用以下事实：在 DES 的实际构造中，Feistel 网络最后一轮输出的两半被交换。也就是说，如果 Feistel 网络最后一轮的输出是 $(L_{16}, R_{16})$，则 DES 的输出是 $(R_{16}, L_{16})$。

(a) Show that the only difference between computation of $DES_k$ and $DES_k^{-1}$ is the order in which sub-keys are used. (Rely on the previous exercise.)

(a) 证明 $DES_k$ 和 $DES_k^{-1}$ 的计算之间唯一的区别在于子密钥的使用顺序。（依赖前一习题。）

(b) Show that when $k = 0^{56}$ then $DES_k(DES_k(x)) = x$ for all x.

(b) 证明当 $k = 0^{56}$ 时，对所有 x 有 $DES_k(DES_k(x)) = x$。

Hint: Consider the sub-keys generated from this key.

提示：考虑从该密钥生成的子密钥。

(c) Find three other DES keys with the same property. These keys are known as weak keys for DES. (Note: the keys you find will differ from the actual weak keys of DES because of differences in our description of the DES key schedule.)

(c) 找出具有相同性质的另外三个 DES 密钥。这些密钥称为 DES 的弱密钥。（注意：由于我们对 DES 密钥扩展的描述与实际不同，你找到的密钥将与 DES 的实际弱密钥不同。）

(d) Do these 4 weak keys represent a serious vulnerability in the use of triple-DES as a pseudorandom permutation? Explain.

(d) 这 4 个弱密钥是否构成三重 DES 作为伪随机置换使用时的严重漏洞？解释原因。

7.13 (This exercise relies on Exercise 7.12.) Our goal is to show that for any weak key k of DES, it is easy to find an input x such that $DES_k(x) = x$.

7.13 （本习题依赖习题 7.12。）我们的目标是证明对于 DES 的任何弱密钥 $k$，都容易找到输入 $x$ 使得 $DES_k(x) = x$。

(a) Assume we evaluate $DES_{k}$ on input $(L_{0}, R_{0})$, and the intermediate result after 8 rounds of the Feistel network is $(L_{8}, R_{8})$ with $L_{8}=R_{8}$. Show that $(L_{0}, R_{0})=DES_{k}(L_{0}, R_{0})$. (Recall from Exercise 7.12 that DES swaps the two halves of the output of the 16th round of the Feistel network.)

(a) 假设我们在输入 $(L_{0}, R_{0})$ 上计算 $DES_{k}$，Feistel 网络 8 轮后的中间结果为 $(L_{8}, R_{8})$ 且 $L_{8}=R_{8}$。证明 $(L_{0}, R_{0})=DES_{k}(L_{0}, R_{0})$。（回忆习题 7.12：DES 交换 Feistel 网络第 16 轮输出的两半。）

(b) Show how to find an input $(L_{0}, R_{0})$ with the property in part (a).

(b) 展示如何找到具有 (a) 中性质的输入 $(L_{0}, R_{0})$。

7.14 Show that DES has the property that $DES_k(x) = \overline{DES_k}(\bar{x})$ for every key $k$ and input $x$ (where $\bar{x}$ denotes the bitwise complement of $z$). (This is called the complementarity property of DES.) Does this represent a serious vulnerability in the use of triple-DES as a pseudorandom permutation? Explain.

7.14 证明 DES 具有如下性质：对每个密钥 $k$ 和输入 $x$ 有 $DES_k(x) = \overline{DES_k}(\bar{x})$（其中 $\bar{x}$ 表示 $x$ 的按位补）。（这称为 DES 的互补性性质。）这是否构成三重 DES 作为伪随机置换使用时的严重漏洞？解释原因。

7.15 Describe attacks on the following modifications of DES:

7.15 描述对以下 DES 修改的攻击：

(a) Each sub-key is 32 bits long, and the round function simply XORs the sub-key with the input to the round (i.e., $\hat{f}(k, R) = k_i \oplus R$). For this question, the key schedule is unimportant and you can treat the sub-keys $k_i$ as independent keys.

(a) 每个子密钥长 32 比特，轮函数简单地将子密钥与轮输入异或（即 $\hat{f}(k, R) = k_i \oplus R$）。本题中密钥扩展不重要，你可以将子密钥 $k_i$ 视为独立密钥。

(b) Instead of using different sub-keys in every round, the same 48-bit sub-key is used in every round. Show how to distinguish the cipher from a random permutation using two chosen plaintexts and negligible work.

(b) 不在每轮使用不同的子密钥，而是每轮使用相同的 48 比特子密钥。展示如何仅用两个选择明文和可忽略的计算量就把该密码与随机置换区分开来。

Hint: Exercises 7.11 and 7.12 may help...

提示：习题 7.11 和 7.12 可能有帮助……

7.16 This question develops an attack on two-key triple encryption. Let $F$ be a block cipher with $\ell$-bit block length and $n$-bit key length (where $\ell \geq n$), and set $F^{\prime}_{k_1,k_2}(x) \overset{\mathrm{def}}{=} F_{k_1}(F_{k_2}(F_{k_1}(x)))$. Assume an attacker is given $N \ll 2^{\ell}$ input/output pairs $\{(x_i, y_i)\}_{i=1}^N$ where the $\{x_i\}$ are uniform and $y_i = F^{\prime}_{k_1,k_2}(x_i)$ for unknown keys $k_1, k_2$.

7.16 本题构造对双密钥三重加密的攻击。设 $F$ 是分组长度为 $\ell$ 比特、密钥长度为 $n$ 比特的分组密码（其中 $\ell \geq n$），令 $F^{\prime}_{k_1,k_2}(x) \overset{\mathrm{def}}{=} F_{k_1}(F_{k_2}(F_{k_1}(x)))$。假设攻击者获得 $N \ll 2^{\ell}$ 个输入/输出对 $\{(x_i, y_i)\}_{i=1}^N$，其中 $\{x_i\}$ 均匀，$y_i = F^{\prime}_{k_1,k_2}(x_i)$，密钥 $k_1, k_2$ 未知。

(a) Assume the attacker knows $z \in \{0,1\}^{\ell}$ such that $F_{k_1}(x_i) = z$ for some $i$. (The attacker does not know $i$.) Show how the attacker can find $k_1, k_2$ using ${2}^{n+1} + \mathcal{O}(N) \approx 2^{n+1}$ evaluations of $F/F^{-1}$.

(a) 假设攻击者知道 $z \in \{0,1\}^{\ell}$ 使得对某个 $i$ 有 $F_{k_1}(x_i) = z$。（攻击者不知道 $i$。）展示攻击者如何使用 ${2}^{n+1} + \mathcal{O}(N) \approx 2^{n+1}$ 次 $F/F^{-1}$ 求值找到 $k_1, k_2$。

Hint: Start by computing $\{F_{k}(z)\}$ for all possible keys.

提示：先对所有可能的密钥计算 $\{F_{k}(z)\}$。

(b) In general, the attacker does not know $z$ as required for part (a). Show how the attacker can nevertheless learn $k_{1}, k_{2}$ using roughly ${2}^{n+\ell+1}/N$ evaluations of $F/F^{-1}$.

(b) 一般情况下，攻击者不知道 (a) 所需的 $z$。展示攻击者如何仍能利用大约 ${2}^{n+\ell+1}/N$ 次 $F/F^{-1}$ 求值恢复 $k_{1}, k_{2}$。

Hint: What happens if the attacker chooses a random z?

提示：如果攻击者选择一个随机的 z 会怎样？

7.17 Say the key schedule of DES is modified as follows: the left half of the master key is used to derive all the sub-keys in rounds 1–8, while the right half of the master key is used to derive all the sub-keys in rounds 9–16. Show an attack on this modified scheme that recovers the entire key in time roughly ${2}^{28}$.

7.17 假设 DES 的密钥扩展修改如下：主密钥的左半部分用于推导第 1–8 轮的所有子密钥，右半部分用于推导第 9–16 轮的所有子密钥。展示一个在大约 ${2}^{28}$ 时间内恢复完整密钥的攻击。

7.18 Fix arbitrary $G_1, G_2: \{0,1\}^n \to \{0,1\}^{4n}$, and define

7.18 固定任意的 $G_1, G_2: \{0,1\}^n \to \{0,1\}^{4n}$，定义

$$
G(s_{1}||s_{2})=G_{1}(s_{1})\oplus G_{2}(s_{2}).
$$

Show how to distinguish the output of $G$ from random in time $\approx 2^{n+1}$.

展示如何在 $\approx 2^{n+1}$ 时间内将 $G$ 的输出与随机输出区分开。

Hint: Adapt the meet-in-the-middle attack.

提示：对中间相遇攻击加以改造。

7.19 Let $f: \{0,1\}^m \times \{0,1\}^\ell \to \{0,1\}^\ell$ and $g: \{0,1\}^n \times \{0,1\}^\ell \to \{0,1\}^\ell$ be secure block ciphers with $m > n$, and define $F_{k_1,k_2}(x) = f_{k_1}(g_{k_2}(x))$. Show a key-recovery attack on $F$ using time $\mathcal{O}(2^m)$ and space $\mathcal{O}(\ell \cdot 2^n)$.

7.19 设 $f: \{0,1\}^m \times \{0,1\}^\ell \to \{0,1\}^\ell$ 和 $g: \{0,1\}^n \times \{0,1\}^\ell \to \{0,1\}^\ell$ 是安全的分组密码且 $m > n$，定义 $F_{k_1,k_2}(x) = f_{k_1}(g_{k_2}(x))$。展示一个对 $F$ 的密钥恢复攻击，使用 $\mathcal{O}(2^m)$ 时间和 $\mathcal{O}(\ell \cdot 2^n)$ 空间。

7.20 Define $DESY_{k,k^{\prime}}(x) = DES_k(x \oplus k^{\prime})$. The key length of $DESY$ is 120 bits. Show a key-recovery attack on $DESY$ taking $\approx 2^{56}$ time and $\mathcal{O}(1)$ memory.

7.20 定义 $DESY_{k,k^{\prime}}(x) = DES_k(x \oplus k^{\prime})$。$DESY$ 的密钥长度为 120 比特。展示一个耗时 $\approx 2^{56}$、使用 $\mathcal{O}(1)$ 内存的 $DESY$ 密钥恢复攻击。

7.21 Choose random S-boxes and mixing permutations for SPNs of different sizes, and develop differential attacks against them. We recommend trying five-round SPNs with 16-bit and 24-bit block lengths, using S-boxes with 4-bit input/output. Write code to compute the differential tables, and to carry out the attack.

7.21 为不同大小的 SPN 选择随机 S 盒和混合置换，并构造针对它们的差分攻击。我们建议尝试 16 比特和 24 比特分组长度的五轮 SPN，使用 4 比特输入/输出的 S 盒。编写代码计算差分表并执行攻击。

7.22 Implement the time/space tradeoff from Section 6.4.3 for a key-recovery attack on 40-bit DES (e.g., fix the first 16 bits of the key to 0). Calculate the time and memory needed, and empirically estimate the probability of success. Experimentally verify the increase in success probability as the number of tables is increased. (Warning: this is a big project!)

7.22 实现 6.4.3 节中的时间/空间折中，用于对 40 比特 DES 的密钥恢复攻击（例如，将密钥的前 16 比特固定为 0）。计算所需的时间和内存，并实验估计成功概率。实验验证成功概率随表数量增加而提高。（警告：这是一个大项目！）

7.23 For each of the following constructions of a compression function $h$ from a block cipher $F: \{0,1\}^n \times \{0,1\}^n \to \{0,1\}^n$, either show an attack or prove collision resistance in the ideal-cipher model:

7.23 对于以下从分组密码 $F: \{0,1\}^n \times \{0,1\}^n \to \{0,1\}^n$ 构造压缩函数 $h$ 的每种方式，要么展示攻击，要么在理想密码模型中证明抗碰撞性：

(a) $h(k,x) = F_{k}(x)$.

(a) $h(k,x) = F_{k}(x)$。

(b) $h(k,x) = F_{k}(x) \oplus k \oplus x$.

(b) $h(k,x) = F_{k}(x) \oplus k \oplus x$。

(c) $h(k,x) = F_{k}(x) \oplus k$.

(c) $h(k,x) = F_{k}(x) \oplus k$。

7.24 Let $F$ be a block cipher for which it is easy to find fixed points for some key: namely, there is a key $k$ for which it is easy to find inputs $x$ for which $F_k(x) = x$. Find a collision in the Davies–Meyer construction when applied to $F$. (Consider this in light of Exercise 7.13.)

7.24 设 $F$ 是一个对某个密钥容易找到不动点的分组密码：即存在密钥 $k$ 使得容易找到输入 $x$ 满足 $F_k(x) = x$。在将 Davies–Meyer 构造应用于 $F$ 时找到一个碰撞。（结合习题 7.13 考虑。）

7.25 Consider using DES to construct a compression function in the following way: Define $h : \{0,1\}^{112} \to \{0,1\}^{64}$ as $h(x_1, x_2) \overset{\mathrm{def}}{=} DES_{x_1}(DES_{x_2}(0^{64}))$ where $|x_1| = |x_2| = 56$.

7.25 考虑用 DES 如下构造压缩函数：定义 $h : \{0,1\}^{112} \to \{0,1\}^{64}$ 为 $h(x_1, x_2) \overset{\mathrm{def}}{=} DES_{x_1}(DES_{x_2}(0^{64}))$，其中 $|x_1| = |x_2| = 56$。

(a) Write down an explicit collision in h.

(a) 写出 h 中的一个显式碰撞。

Hint: Use Exercise 7.12(a–b).

提示：使用习题 7.12(a–b)。

(b) Show how to find a preimage of an arbitrary value $y$ (that is, $x_1, x_2$ such that $h(x_1 \| x_2) = y$) in roughly ${2}^{56}$ time.

(b) 展示如何在大约 ${2}^{56}$ 时间内找到任意值 $y$ 的原像（即 $x_1, x_2$ 使得 $h(x_1 \| x_2) = y$）。

(c) Show a more clever preimage attack that runs in roughly ${2}^{32}$ time and succeeds with high probability.

(c) 展示一个更巧妙的原像攻击，在大约 ${2}^{32}$ 时间内运行并以高概率成功。

Hint: Rely on the results of Appendix A.4.

提示：依赖附录 A.4 的结果。

7.26 Say $S_1, \ldots, S_8 : \{0,1\}^n \to \{0,1\}^n$ are modeled as random permutations, and say $P : \{0,1\}^{8n} \to \{0,1\}^{8n}$ is constructed by defining

7.26 设 $S_1, \ldots, S_8 : \{0,1\}^n \to \{0,1\}^n$ 被建模为随机置换，$P : \{0,1\}^{8n} \to \{0,1\}^{8n}$ 由以下方式构造

$$
P(x_{1}||\cdots||x_{8})=S_{1}(x_{1})||\cdots||S_{8}(x_{8}).
$$

Show that it is easy to find a collision in Construction 7.6 for $\lambda = 1$ and r = c = v = 4n when using this P.

证明在 $\lambda = 1$ 且 r = c = v = 4n 的构造 7.6 中使用该 P 时，容易找到碰撞。
