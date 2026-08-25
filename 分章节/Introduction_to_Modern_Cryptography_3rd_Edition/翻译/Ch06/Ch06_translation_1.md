# Chapter 6: Hash Functions and Applications　第六章　哈希函数及其应用

In this chapter we look beyond the problem of secure communication that has occupied us until now, and consider a cryptographic primitive with many applications: cryptographic hash functions. At the most basic level, a hash function $H$ provides a way to deterministically map a long input string to a shorter output string sometimes called a digest. The primary requirement is that it should be infeasible to find a collision in $H$: namely, two inputs that produce the same digest. As we will see, collision-resistant hash functions have numerous uses, including another approach—standardized as HMAC—for domain extension for message authentication codes.

在本章中，我们把目光投向迄今为止一直关注的安全通信问题之外，考察一种有着众多应用的密码学原语：密码学哈希函数。在最基本的层面上，哈希函数 $H$ 提供了一种将长输入串确定性地映射到较短输出串（有时称为摘要，digest）的方法。首要要求是难以找到 $H$ 中的一个碰撞（collision）：即两个产生相同摘要的输入。我们将看到，抗碰撞哈希函数有众多用途，其中包括另一种消息认证码域扩展的方法——已被标准化为 HMAC。

Hash functions can be viewed as lying between the worlds of private- and public-key cryptography. On the one hand, as we will see in Chapter 7, they are (in practice) constructed using symmetric-key techniques. From a theoretical point of view, however, the existence of collision-resistant hash functions appears to be a qualitatively stronger assumption than the existence of other symmetric-key primitives, while at the same time being weaker than what is needed for public-key encryption. Hash functions have important applications in both the private- and public-key settings.

哈希函数可被视为处于私钥密码学与公钥密码学两个世界之间。一方面，正如我们将在第 7 章看到的，它们（在实践中）是使用对称密钥技术构造的。然而从理论角度看，抗碰撞哈希函数的存在性似乎是一个在性质上比其他对称密钥原语的存在性更强的假设，同时又弱于公钥加密所需的假设。哈希函数在私钥和公钥设置下都有重要应用。

Hash functions have become ubiquitous in cryptography, and they are often used in scenarios that require properties much stronger than collision resistance. Indeed, it has become common to model cryptographic hash functions as being “completely unpredictable” (a.k.a., random oracles), and we discuss this model—and the controversy that surrounds it—in Section 6.5. In Section 6.6 we touch on a few applications of random oracles; we will encounter the random-oracle model again in the context of public-key cryptography.

哈希函数在密码学中已变得无处不在，它们常被用于需要远比抗碰撞更强性质的场景。事实上，把密码学哈希函数建模为“完全不可预测的”（又称随机预言机，random oracles）已成为常见做法，我们在 6.5 节讨论这一模型——以及围绕它的争议。在 6.6 节我们触及随机预言机的若干应用；我们还将在公钥密码学的语境中再次遇到随机预言机模型。

## 6.1 Definitions　6.1 定义

Hash functions are simply functions that take inputs of some length and compress them into short, fixed-length outputs. The classic use of (non-cryptographic) hash functions is in data structures, where they can be used to build hash tables that enable $\mathcal{O}(1)$ lookup time when storing a set of elements. Specifically, if the range of the hash function $H$ is of size $N$, then element $x$ is stored in row $H(x)$ of a table of size $N$. To retrieve $x$, it suffices to compute $H(x)$ and probe that row of the table for the elements stored there. A “good” hash function for this purpose is one that yields few collisions, where a collision is a pair of distinct elements $x$ and $x^{\prime}$ for which $H(x)=H(x^{\prime})$; in this case we also say that $x$ and $x^{\prime}$ collide. (When a collision occurs, two elements end up being stored in the same cell, increasing the lookup time.)

哈希函数不过是这样一些函数：它们接受某种长度的输入并将其压缩为短的、固定长度的输出。（非密码学的）哈希函数的经典用途是在数据结构中，它们可用于构建哈希表，使得在存储一组元素时能实现 $\mathcal{O}(1)$ 的查找时间。具体而言，如果哈希函数 $H$ 的值域大小为 $N$，那么元素 $x$ 就存放在大小为 $N$ 的表中第 $H(x)$ 行。要检索 $x$，只需计算 $H(x)$ 并探查表中相应行存放的元素即可。用于此目的的“好”哈希函数是产生很少碰撞的函数，其中碰撞是指一对不同元素 $x$ 和 $x^{\prime}$ 满足 $H(x)=H(x^{\prime})$；此时我们也说 $x$ 和 $x^{\prime}$ 发生碰撞。（当碰撞发生时，两个元素最终被存放在同一格中，增加了查找时间。）

Collision-resistant hash functions are similar in spirit; again, the goal is to avoid collisions. However, there are fundamental differences. For one, the desire to minimize collisions in the setting of data structures becomes a requirement to avoid collisions in the setting of cryptography. Furthermore, in the context of data structures we assume that the set of elements being hashed is chosen independently of H and without any intention to cause collisions. In the context of cryptography, in contrast, we are faced with an adversary who may select elements with the explicit goal of causing collisions. This means that collision-resistant hash functions are much harder to design.

抗碰撞哈希函数与之在精神上是类似的；目标同样是避免碰撞。然而，两者存在根本差异。首先，在数据结构的场景下“尽量减少碰撞”的愿望，在密码学的场景下变成了“避免碰撞”的要求。此外，在数据结构的语境中我们假设被哈希的元素集合是独立于 H 选择的，并且没有任何制造碰撞的意图。相比之下，在密码学的语境中，我们面对的是一个可能以制造碰撞为明确目标来选择元素的敌手。这意味着抗碰撞哈希函数的设计要困难得多。

### 6.1.1 Collision Resistance　6.1.1 抗碰撞性

Informally, a function $H$ is collision resistant if it is infeasible for any probabilistic polynomial-time algorithm to find a collision in $H$. We will only be interested in hash functions whose domain is larger than their range. In this case collisions must exist, but such collisions should be hard to find.

非正式地说，如果一个函数 $H$ 使得任何概率多项式时间算法都难以在其中找到碰撞，则称 $H$ 是抗碰撞的。我们只对定义域大于值域的哈希函数感兴趣。在这种情况下碰撞必然存在，但这样的碰撞应当难以找到。

Formally, we consider keyed hash functions. That is, $H$ is a two-input function that takes as input a key $s$ and a string $x$, and outputs a string $H^s(x) \overset{\mathrm{def}}{=} H(s,x)$. The requirement is that it must be hard to find a collision in $H^s$ for a randomly generated key $s$. We highlight one major difference between keys in this context and the keys we have considered until now: In the present context, the key $s$ is (generally) not kept secret, and collision resistance is required even when the adversary is given $s$. In order to emphasize that the key may not be secret, we superscript the key and write $H^s$ rather than $H_s$.

形式化地，我们考虑带密钥的哈希函数。即 $H$ 是一个双输入函数，以一个密钥 $s$ 和一个串 $x$ 为输入，输出一个串 $H^s(x) \overset{\mathrm{def}}{=} H(s,x)$。要求是对于随机生成的密钥 $s$，在 $H^s$ 中找到碰撞必须是困难的。我们强调此处密钥与我们迄今为止考虑过的密钥之间的一个主要区别：在当前语境中，密钥 $s$（通常）是不保密的，并且即使敌手获得了 $s$ 也要求抗碰撞性。为了强调密钥可能不保密，我们把密钥写成上标形式 $H^s$ 而非 $H_s$。

DEFINITION 6.1 A hash function (with output length $\ell(n)$) is a pair of probabilistic polynomial-time algorithms (Gen, H) satisfying the following:

Gen is a probabilistic algorithm that takes as input a security parameter ${1}^{n}$ and outputs a key s. We assume that n is implicit in s.

**定义 6.1** 哈希函数（输出长度为 $\ell(n)$）是一对概率多项式时间算法 (Gen, H)，满足：

Gen 是一个概率算法，以安全参数 ${1}^{n}$ 为输入并输出一个密钥 s。我们假设 n 隐含在 s 中。

- $H$ is a deterministic algorithm that takes as input a key $s$ and a string $x \in \{0,1\}^*$ and outputs a string $H^s(x) \in \{0,1\}^{\ell(n)}$ (where $n$ is the value of the security parameter implicit in $s$).

  $H$ 是一个确定性算法，以密钥 $s$ 和串 $x \in \{0,1\}^*$ 为输入，输出一个串 $H^s(x) \in \{0,1\}^{\ell(n)}$（其中 $n$ 是隐含在 $s$ 中的安全参数取值）。

If $H^{s}$ is defined only for inputs x of length $\ell^{\prime}(n) > \ell(n)$, then we say that (Gen, H) is a fixed-length hash function for inputs of length $\ell^{\prime}(n)$. In this case, we also call H a compression function.

如果 $H^{s}$ 仅对长度为 $\ell^{\prime}(n) > \ell(n)$ 的输入 $x$ 有定义，则我们称 $(\mathsf{Gen}, H)$ 是输入长度为 $\ell^{\prime}(n)$ 的固定长度哈希函数。在这种情况下，我们也称 H 为压缩函数（compression function）。

In the fixed-length case we require that $\ell^{\prime}$ be greater than $\ell$. This ensures that $H^{s}$ compresses its input. In the general case the function takes as input strings of arbitrary length; thus, it also compresses (albeit only inputs of length greater than $\ell(n)$). Note that without compression, collision resistance is trivial (since one can just take the identity function $H^{s}(x)=x$).

在固定长度的情形下，我们要求 $\ell^{\prime}$ 大于 $\ell$。这保证了 $H^{s}$ 压缩其输入。在一般情形下，该函数接受任意长度的串作为输入；因此它也压缩（尽管只压缩长度大于 $\ell(n)$ 的输入）。注意，如果没有压缩，抗碰撞性是平凡的（因为可以直接取恒等函数 $H^{s}(x)=x$）。

We now proceed to define security. As usual, we first define an experiment for a hash function $\mathcal{H} = (\mathsf{Gen}, H)$, an adversary $\mathcal{A}$, and a security parameter $n$:

我们现在着手定义安全性。与往常一样，我们首先为哈希函数 $\mathcal{H} = (\mathsf{Gen}, H)$、敌手 $\mathcal{A}$ 和安全参数 $n$ 定义一个实验：

The collision-finding experiment $\mathsf{Hash-coll}_{A,\mathcal{H}}(n)$:

寻找碰撞实验 $\mathsf{Hash-coll}_{A,\mathcal{H}}(n)$：

1. A key s is generated by running Gen(1^{n}).

   通过运行 Gen(1^{n}) 生成一个密钥 s。

2. The adversary $\mathcal{A}$ is given s, and outputs $x, x^{\prime}$. (If $\mathcal{H}$ is a fixed-length hash function for inputs of length $\ell^{\prime}(n)$, then we require $x, x^{\prime} \in \{0,1\}^{\ell^{\prime}(n)}.$)

   敌手 $\mathcal{A}$ 获得 s，并输出 $x, x^{\prime}$。（如果 $\mathcal{H}$ 是输入长度为 $\ell^{\prime}(n)$ 的固定长度哈希函数，则要求 $x, x^{\prime} \in \{0,1\}^{\ell^{\prime}(n)}.$）

3. The output of the experiment is defined to be 1 if and only if $x \neq x^{\prime}$ and $H^{s}(x) = H^{s}(x^{\prime})$. In such a case we say that A has found a collision.

   当且仅当 $x \neq x^{\prime}$ 且 $H^{s}(x) = H^{s}(x^{\prime})$ 时，实验的输出定义为 1。在此情形下我们说 A 找到了一个碰撞。

The definition of collision resistance states that no efficient adversary can find a collision in the above experiment except with negligible probability.

抗碰撞性的定义表明，任何高效敌手都至多只能以可忽略的概率在上述实验中找到碰撞。

DEFINITION 6.2 A hash function $\mathcal{H} = (\mathsf{Gen}, H)$ is collision resistant if for all probabilistic polynomial-time adversaries $\mathcal{A}$ there is a negligible function $\mathsf{negl}$ such that

**定义 6.2** 哈希函数 $\mathcal{H} = (\mathsf{Gen}, H)$ 是抗碰撞的，如果对于所有概率多项式时间敌手 $\mathcal{A}$，存在一个可忽略函数 $\mathsf{negl}$ 使得

$$
\Pr\left[\mathsf{Hash-coll}_{\mathcal{A},\mathcal{H}}(n)=1\right]\leq\mathsf{negl}(n).
$$

For simplicity, we sometimes refer to $H$ or $H^s$ as a “collision-resistant hash function,” even though technically we should only say that $\mathcal{H} = (\mathsf{Gen}, H)$ is. This should not cause any confusion.

为简单起见，我们有时把 $H$ 或 $H^s$ 称为“抗碰撞哈希函数”，尽管严格来说我们只应说 $\mathcal{H} = (\mathsf{Gen}, H)$ 是抗碰撞的。这不应当引起任何混淆。

Cryptographic hash functions are designed with the explicit goal of being collision resistant (among other things). We will discuss some design principles for hash functions, along with some commonly used examples, in Chapter 7. In Section 9.4.2 we will see how it is possible to construct hash functions with proven collision resistance based on an assumption about the hardness of a certain number-theoretic problem.

密码学哈希函数在设计时以抗碰撞为明确目标（同时还有其他目标）。我们将在第 7 章讨论哈希函数的一些设计原则以及一些常用示例。在 9.4.2 节我们将看到，基于某个数论问题的困难性假设，如何能够构造出具有可证明抗碰撞性的哈希函数。

Unkeyed hash functions. Cryptographic hash functions used in practice are generally unkeyed and have a fixed output length (by analogy with block ciphers), meaning that the hash function is just a fixed, deterministic function $H : \{0,1\}^* \to \{0,1\}^\ell$. This is problematic from a theoretical standpoint since for any such function there is always a constant-time algorithm that outputs a collision in $H$: the algorithm simply outputs a colliding pair $(x, x^{\prime})$ hardcoded into the algorithm itself. Using keyed hash functions solves this technical issue since it is impossible to hardcode a collision for every possible key using a reasonable amount of memory (and in an asymptotic setting, it would be impossible to hardcode a collision for every value of the security parameter).

无密钥哈希函数。实践中使用的密码学哈希函数通常是无密钥的，并且具有固定的输出长度（与分组密码类比），这意味着哈希函数只是一个固定的确定性函数 $H : \{0,1\}^* \to \{0,1\}^\ell$。从理论角度看这是有问题的，因为对于任何这样的函数，总存在一个能在常数时间内输出 $H$ 中一个碰撞的算法：该算法只需输出一个硬编码在算法之中的碰撞对 $(x, x^{\prime})$。使用带密钥的哈希函数可以解决这一技术问题，因为不可能用合理的内存量为每个可能的密钥都硬编码一个碰撞（而在渐近设置下，为安全参数的每个取值都硬编码一个碰撞是不可能的）。

Notwithstanding the above, the (unkeyed) cryptographic hash functions used in the real world are collision resistant for all practical purposes since colliding pairs are unknown (and computationally difficult to find) even though they must exist. Proofs of security for a scheme based on a collision-resistant hash function are still meaningful even when an unkeyed hash function $H$ is used, as long as the proof shows that any efficient adversary “breaking” the primitive can be used to efficiently find a collision in $H$. (All the proofs in this book satisfy that condition.) In this case, the interpretation of the security proof is that if an adversary can break the scheme, then it can be used to find an explicit collision, something that is believed to be difficult.

尽管如此，现实世界中使用的（无密钥）密码学哈希函数在一切实际意义上都是抗碰撞的，因为碰撞对是未知的（并且在计算上难以找到），尽管它们必然存在。即使使用无密钥哈希函数 $H$，基于抗碰撞哈希函数的方案的安全性证明仍然有意义，只要该证明表明任何“攻破”该原语的高效敌手都可被用来高效地找到 $H$ 中的一个碰撞。（本书中的所有证明都满足该条件。）在这种情况下，安全性证明的解释是：如果敌手能攻破该方案，那么它就可被用来找到一个显式的碰撞，而这被认为是困难的。

In this chapter and throughout the rest of the book, we consider keyed hash functions when formally proving results that rely on collision resistance, but generally assume unkeyed hash functions otherwise.

在本章及本书余下部分，当形式化证明依赖抗碰撞性的结果时，我们考虑带密钥的哈希函数；但在其他情况下通常假设是无密钥哈希函数。

### 6.1.2 Weaker Notions of Security　6.1.2 更弱的安全性概念

For some applications, security requirements weaker than collision resistance suffice. Security notions that are sometimes considered include:

对于某些应用，比抗碰撞性更弱的安全性要求就足够了。有时会考虑的安全性概念包括：

Second-preimage resistance: Informally, a hash function is said to be second-preimage resistant if given s and a uniform x it is infeasible for a PPT adversary to find $x^{\prime} \neq x$ such that $H^s(x^{\prime}) = H^s(x)$.

第二原像抗性（second-preimage resistance）：非正式地说，如果给定 $s$ 和均匀随机选取的 $x$，PPT 敌手难以找到 $x^{\prime} \neq x$ 使得 $H^s(x^{\prime}) = H^s(x)$，则称该哈希函数是第二原像抗性的。

Preimage resistance: Informally, a hash function is preimage resistant if given $s$ and $y = H^{s}(x)$ for a uniform $x$, it is infeasible for a PPT adversary to find a value $x^{\prime}$ (whether equal to $x$ or not) with $H^{s}(x^{\prime}) = y$. (Looking ahead to Chapter 8, this basically means that $H^{s}$ is one-way.)

原像抗性（preimage resistance）：非正式地说，如果对于均匀的 $x$，给定 $s$ 和 $y = H^{s}(x)$，PPT 敌手难以找到一个值 $x^{\prime}$（无论是否等于 $x$）满足 $H^{s}(x^{\prime}) = y$，则称该哈希函数是原像抗性的。（展望第 8 章，这基本上意味着 $H^{s}$ 是单向的。）

It is immediate that any hash function that is collision resistant is also second-preimage resistant. It is also true that if a hash function is second-preimage resistant then it is preimage resistant. We do not formally define the above notions or prove these implications, since they are not used in the rest of the book. You are asked to formalize the above in Exercise 6.1.

显然，任何抗碰撞的哈希函数也是第二原像抗性的。类似地，若一个哈希函数具有第二原像抗性，则它也具有原像抗性。我们不形式化定义上述概念或证明这些蕴含关系，因为本书余下部分不会用到它们。习题 6.1 要求你将上述内容形式化。

## 6.2 The Merkle–Damgård Transform　6.2 Merkle–Damgård 变换

Many applications require "full-fledged" collision-resistant hash functions that can handle very long inputs, or even inputs of arbitrary length. But it is much easier to construct fixed-length hash functions (i.e., compression functions) that only accept "short" inputs—something we will return to in Section 7.3. Fortunately, the Merkle–Damgård transform allows us to convert the latter to the former. This approach for domain extension of hash functions has been used frequently in practice, including for the hash function MD5 and the SHA hash family (cf. Section 7.3). The Merkle–Damgård transform is also interesting from a theoretical point of view since it implies that compressing by a single bit is as easy (or as hard) as compressing by an arbitrary amount.

许多应用需要能够处理很长输入、甚至任意长度输入的“完备”抗碰撞哈希函数。但是构造只接受“短”输入的固定长度哈希函数（即压缩函数）要容易得多——我们将在 7.3 节回到这一点。幸运的是，Merkle–Damgård 变换允许我们把后者转换为前者。这种哈希函数的域扩展方法在实践中被频繁使用，包括用于哈希函数 MD5 和 SHA 哈希族（参见 7.3 节）。Merkle–Damgård 变换在理论上也很有趣，因为它蕴含：压缩一比特与压缩任意多比特一样容易（或一样困难）。

For concreteness, assume the compression function (Gen, h) takes inputs of length $n + n^{\prime} \geq 2n$, and generates outputs of length $n$. (The construction can be generalized for other input/output lengths, as long as $h$ compresses.) Applying the Merkle–Damgård transform, defined in Construction 6.3 and depicted in Figure 6.1, yields a hash function (Gen, $H$) that maps inputs of arbitrary length to outputs of length $n$.

为具体起见，假设压缩函数 (Gen, h) 接受长度为 $n + n^{\prime} \geq 2n$ 的输入，并生成长度为 $n$ 的输出。（只要 $h$ 是压缩的，该构造可推广到其他输入/输出长度。）应用构造 6.3 中定义并如图 6.1 所描绘的 Merkle–Damgård 变换，得到一个将任意长度输入映射为长度为 $n$ 的输出的哈希函数 (Gen, $H$)。

> **CONSTRUCTION 6.3**　**构造 6.3**
>
> Let $(\mathsf{Gen}, h)$ be a compression function for inputs of length $n + n^{\prime} \geq 2n$ with output length $n$. *Fix* $\ell \leq n^{\prime}$ and $IV \in \{0,1\}^n$. *Construct hash function* $(\mathsf{Gen}, H)$ as follows:
>
> Gen: remains unchanged.
>
> - $H$: on input a key $s$ and a string $x \in \{0,1\}^*$ of length $L < 2^\ell$, do:
>
> 1. Append a 1 to x, followed by enough zeros so that the length of the resulting string is $\ell$ less than a multiple of $n^{\prime}$. Then append L, encoded as an $\ell$-bit string. Parse the resulting string as the sequence of $n^{\prime}$-bit blocks $x_1, \ldots, x_B$.
>
> 2. Set $z_{0} := IV$.
>
> 3. For $i = 1, \ldots, B$, compute $z_i := h^s(z_{i-1} | x_i)$.
>
> 4. Output $z_{B}$
>
> 设 $(\mathsf{Gen}, h)$ 是输入长度为 $n + n^{\prime} \geq 2n$、输出长度为 $n$ 的压缩函数。*取定* $\ell \leq n^{\prime}$ 和 $IV \in \{0,1\}^n$。*如下构造哈希函数* $(\mathsf{Gen}, H)$：
>
> Gen：保持不变。
>
> - $H$：输入密钥 $s$ 和长度为 $L < 2^\ell$ 的串 $x \in \{0,1\}^*$，执行：
>
> 1. 向 x 追加一个 1，随后追加足够多的零，使得所得串的长度比 $n^{\prime}$ 的整数倍少 $\ell$。然后追加 L（编码为 $\ell$ 比特串）。将所得串解析为 $n^{\prime}$ 比特块序列 $x_1, \ldots, x_B$。
>
> 2. 置 $z_{0} := IV$。
>
> 3. 对 $i = 1, \ldots, B$，计算 $z_i := h^s(z_{i-1} | x_i)$。
>
> 4. 输出 $z_{B}$
>
> **The Merkle–Damgård transform.**
>
> **Merkle–Damgård 变换。**

THEOREM 6.4 If (Gen, h) is collision resistant, then so is (Gen, H).

**定理 6.4** 如果 (Gen, h) 是抗碰撞的，那么 (Gen, H) 也是抗碰撞的。

PROOF We show that for any $s$, a collision in $H^s$ yields a collision in $h^s$. Let $x$ and $x^{\prime}$ be two different strings of length $L$ and $L^{\prime}$, respectively, such that $H^s(x) = H^s(x^{\prime})$. Let $x_1, \ldots, x_B$ be the $B$ blocks of the padded $x$, and let $x^{\prime}_1, \ldots, x^{\prime}_{B^{\prime}}$ be the $B^{\prime}$ blocks of the padded $x^{\prime}$. Let $z_0, z_1, \ldots, z_B$ (resp., $z^{\prime}_0, z^{\prime}_1, \ldots, z^{\prime}_{B^{\prime}}$) be the intermediate results during computation of $H^s(x)$ (resp., $H^s(x^{\prime})$). There are two cases to consider:

**证明** 我们证明对任意 $s$，$H^s$ 中的一个碰撞会产生 $h^s$ 中的一个碰撞。设 $x$ 和 $x^{\prime}$ 是长度分别为 $L$ 和 $L^{\prime}$ 的两个不同串，满足 $H^s(x) = H^s(x^{\prime})$。设 $x_1, \ldots, x_B$ 是填充后 $x$ 的 $B$ 个块，设 $x^{\prime}_1, \ldots, x^{\prime}_{B^{\prime}}$ 是填充后 $x^{\prime}$ 的 $B^{\prime}$ 个块。设 $z_0, z_1, \ldots, z_B$（对应地 $z^{\prime}_0, z^{\prime}_1, \ldots, z^{\prime}_{B^{\prime}}$）是计算 $H^s(x)$（对应地 $H^s(x^{\prime})$）期间的中间结果。需要考虑两种情形：

Case 1: $L \neq L^{\prime}$. In this case, the last step of the computation of $H^{s}(x)$ is $z_{B} := h^{s}(z_{B-1} \| x_{B})$, and the last step of the computation of $H^{s}(x^{\prime})$ is $z_{B^{\prime}}^{\prime} := h^{s}(z_{B^{\prime}-1}^{\prime} \| x_{B^{\prime}}^{\prime})$. Since $H^{s}(x) = H^{s}(x^{\prime})$ we have $h^{s}(z_{B-1} \| x_{B}) = h^{s}(z_{B^{\prime}-1}^{\prime} \| x_{B^{\prime}}^{\prime})$. However, $L \neq L^{\prime}$ and so $x_{B} \neq x_{B^{\prime}}$. (Recall that the last $\ell$ bits of $x_{B}$ encode $L$, and the last $\ell$ bits of $x_{B^{\prime}}^{\prime}$ encode $L^{\prime}$.) Thus, $z_{B-1} \| x_{B}$ and $z_{B^{\prime}-1}^{\prime} \| x_{B^{\prime}}^{\prime}$ are a collision with respect to $h^{s}$.

情形 1：$L \neq L^{\prime}$。在此情形下，计算 $H^{s}(x)$ 的最后一步是 $z_{B} := h^{s}(z_{B-1} \| x_{B})$，计算 $H^{s}(x^{\prime})$ 的最后一步是 $z_{B^{\prime}}^{\prime} := h^{s}(z_{B^{\prime}-1}^{\prime} \| x_{B^{\prime}}^{\prime})$。由于 $H^{s}(x) = H^{s}(x^{\prime})$，我们有 $h^{s}(z_{B-1} \| x_{B}) = h^{s}(z_{B^{\prime}-1}^{\prime} \| x_{B^{\prime}}^{\prime})$。然而 $L \neq L^{\prime}$，故 $x_{B} \neq x_{B^{\prime}}$。（回忆 $x_{B}$ 的最后 $\ell$ 个比特编码 $L$，$x_{B^{\prime}}^{\prime}$ 的最后 $\ell$ 个比特编码 $L^{\prime}$。）因此，$z_{B-1} \| x_{B}$ 和 $z_{B^{\prime}-1}^{\prime} \| x_{B^{\prime}}^{\prime}$ 是关于 $h^{s}$ 的一个碰撞。

![Image](https://lsky.jerryxue.top/i/2026/08/22/6a88f9e64f963.jpg)

**FIGURE 6.1: The Merkle–Damgård transform.**

**图 6.1：Merkle–Damgård 变换。**

Case 2: $L = L^{\prime}$. This means that $B = B^{\prime}$. Let $I_i \stackrel{\mathrm{def}}{=} z_{i-1} \| x_i \mathrm{denote~the~i~th~input~to~} h^s$ during computation of $H^s(x)$, and define $I_{B+1} \stackrel{\mathrm{def}}{=} z_B$. Define $I^{\prime}_1, \ldots, I^{\prime}_{B+1}$ analogously with respect to $x^{\prime}$. Let $N$ be the largest index for which $I_N \neq I^{\prime}_N$. Since $|x| = |x^{\prime}|$ but $x \neq x^{\prime}$, there is an $i$ with $x_i \neq x^{\prime}_i$ and so such an $N$ certainly exists. Because

情形 2：$L = L^{\prime}$。这意味着 $B = B^{\prime}$。令 $I_i \stackrel{\mathrm{def}}{=} z_{i-1} \| x_i$ 表示计算 $H^s(x)$ 期间对 $h^s$ 的第 i 个输入，并定义 $I_{B+1} \stackrel{\mathrm{def}}{=} z_B$。关于 $x^{\prime}$ 类似地定义 $I^{\prime}_1, \ldots, I^{\prime}_{B+1}$。设 $N$ 是满足 $I_N \neq I^{\prime}_N$ 的最大指标。由于 $|x| = |x^{\prime}|$ 但 $x \neq x^{\prime}$，存在某个 $i$ 使 $x_i \neq x^{\prime}_i$，因此这样的 $N$ 必然存在。因为

$$
I_{B+1}=z_{B}=H^{s}(x)=H^{s}(x^{\prime})=z_{B}^{\prime}=I_{B+1}^{\prime},
$$

we have $N \leq B$. By maximality of $N$, we have $I_{N+1} = I_{N+1}^{\prime}$ and in particular $z_N = z_N^{\prime}.$ But this means that $I_N, I^{\prime}_N$ collide under $h^s$.

我们有 $N \leq B$。由 $N$ 的最大性，我们有 $I_{N+1} = I_{N+1}^{\prime}$，特别地 $z_N = z_N^{\prime}$。但这意味着 $I_N, I^{\prime}_N$ 在 $h^s$ 下碰撞。

We leave it as an exercise to turn the above into a proof by reduction.

将上述内容转化为一个归约证明，留作练习。

## 6.3 Message Authentication Using Hash Functions　6.3 使用哈希函数的消息认证

We have already seen several constructions of message authentication codes for arbitrary-length messages. In this section we will see another approach that relies on collision-resistant hash functions. We then discuss a standardized and widely used scheme called HMAC that can be viewed as a specific instantiation of this approach.

我们已经见过几种用于任意长度消息的消息认证码构造。在本节中我们将看到另一种依赖抗碰撞哈希函数的方法。然后我们讨论一种称为 HMAC 的标准化且广泛使用的方案，它可以被看作这一方法的一种具体实例化。

### 6.3.1 Hash-and-MAC　6.3.1 哈希后认证

Collision-resistant hash functions can naturally be used for domain extension of message authentication codes. Say we have a fixed-length MAC for $\ell(n)$-bit messages, and a collision-resistant hash function with $\ell(n)$-bit output length. Then we can authenticate an arbitrary-length message $m$ by using the MAC to authenticate the hash of $m$. (See Construction 6.5.) Intuitively, this is secure because the MAC ensures that the attacker cannot authenticate any new hash value, while collision resistance ensures that the attacker will be unable to find any new message that hashes to a previously used hash value.

抗碰撞哈希函数自然地可用于消息认证码的域扩展。假设我们有一个用于 $\ell(n)$ 比特消息的固定长度 MAC，以及一个输出长度为 $\ell(n)$ 比特的抗碰撞哈希函数。那么我们可以通过用 MAC 认证 $m$ 的哈希值来认证任意长度的消息 $m$。（见构造 6.5。）直观上，这是安全的，因为 MAC 保证了攻击者无法认证任何新的哈希值，而抗碰撞性保证了攻击者无法找到任何哈希到先前所用哈希值的新消息。

> **CONSTRUCTION 6.5**　**构造 6.5**
>
> Let $\Pi = (\mathrm{Mac}, \mathrm{Vrfy})$ be a MAC for messages of length $\ell(n)$, and let $\mathcal{H} = (\mathrm{Gen}_{H}, H)$ be a hash function with output length $\ell(n)$. Construct a MAC $\Pi^{\prime} = (\mathrm{Gen}^{\prime}, \mathrm{Mac}^{\prime}, \mathrm{Vrfy}^{\prime})$ for arbitrary-length messages as follows:
>
> Gen': on input ${1}^n$, choose uniform $k \in \{0,1\}^n$ and run $\mathsf{Gen}_H(1^n)$ to obtain $s$; output the key $(k,s)$.
>
> - Mac': on input a key $(k, s)$ and a message $m \in \{0,1\}^*$, output $t \leftarrow \mathsf{Mac}_k(H^s(m))$.
>
> - $\operatorname{Vrfy}^{\prime}$: on input a key $(k,s)$, a message $m \in \{0,1\}^*$, and a tag $t$, output 1 if and only if $\operatorname{Vrfy}_k(H^s(m),t) \overset{?}{=} 1$.
>
> 设 $\Pi = (\mathrm{Mac}, \mathrm{Vrfy})$ 是用于长度为 $\ell(n)$ 的消息的 MAC，设 $\mathcal{H} = (\mathrm{Gen}_{H}, H)$ 是输出长度为 $\ell(n)$ 的哈希函数。如下构造用于任意长度消息的 MAC $\Pi^{\prime} = (\mathrm{Gen}^{\prime}, \mathrm{Mac}^{\prime}, \mathrm{Vrfy}^{\prime})$：
>
> Gen'：输入 ${1}^n$，选择均匀的 $k \in \{0,1\}^n$ 并运行 $\mathsf{Gen}_H(1^n)$ 得到 $s$；输出密钥 $(k,s)$。
>
> - Mac'：输入密钥 $(k, s)$ 和消息 $m \in \{0,1\}^*$，输出 $t \leftarrow \mathsf{Mac}_k(H^s(m))$。
>
> - $\operatorname{Vrfy}^{\prime}$：输入密钥 $(k,s)$、消息 $m \in \{0,1\}^*$ 和标签 $t$，当且仅当 $\operatorname{Vrfy}_k(H^s(m),t) \overset{?}{=} 1$ 时输出 1。
>
> The hash-and-MAC paradigm.
>
> 哈希后认证（hash-and-MAC）范式。

A bit more formally, say a sender uses Construction 6.5 to authenticate some set of messages $Q$, and an attacker $\mathcal{A}$ is then able to forge a valid tag on a new message $m^* \notin Q$. There are two possibilities:

更形式化地说，假设发送方使用构造 6.5 认证了某个消息集合 $Q$，随后攻击者 $\mathcal{A}$ 能够在新消息 $m^* \notin Q$ 上伪造一个有效标签。有两种可能：

Case 1: there is a message $m \in \mathcal{Q}$ such that $H^s(m^*) = H^s(m)$. Then $\mathcal{A}$ has found a collision in $H^s$, contradicting collision resistance of $(\mathrm{Gen}_H, H)$.

情形 1：存在消息 $m \in \mathcal{Q}$ 使得 $H^s(m^*) = H^s(m)$。那么 $\mathcal{A}$ 在 $H^s$ 中找到了一个碰撞，这与 $(\mathrm{Gen}_H, H)$ 的抗碰撞性矛盾。

Case 2: for every message $m \in \mathcal{Q}$ it holds that $H^s(m^*) \neq H^s(m)$. Let $H^s(\mathcal{Q}) \stackrel{\mathrm{def}}{=} \{H^s(m) \mid m \in \mathcal{Q}\}$. Then $H^s(m^*) \notin H^s(\mathcal{Q})$. In this case, $\mathcal{A}$ has forged a valid tag on the “new message” $h^* = H^s(m^*)$ with respect to the (fixed-length) message authentication code $\Pi$. This contradicts the assumption that $\Pi$ is a secure MAC.

情形 2：对每个消息 $m \in \mathcal{Q}$ 都有 $H^s(m^*) \neq H^s(m)$。令 $H^s(\mathcal{Q}) \stackrel{\mathrm{def}}{=} \{H^s(m) \mid m \in \mathcal{Q}\}$。则 $H^s(m^*) \notin H^s(\mathcal{Q})$。在此情形下，$\mathcal{A}$ 相对于（固定长度的）消息认证码 $\Pi$ 在“新消息” $h^* = H^s(m^*)$ 上伪造了一个有效标签。这与 $\Pi$ 是安全 MAC 的假设矛盾。

We now turn the above into a formal proof.

我们现在把上述内容转化为形式化证明。

THEOREM 6.6 If $\Pi$ is a secure MAC for messages of length $\ell(n)$ and H is collision resistant, then Construction 6.5 is a secure MAC (for arbitrary-length messages).

**定理 6.6** 如果 $\Pi$ 是用于长度为 $\ell(n)$ 的消息的安全 MAC，且 H 是抗碰撞的，那么构造 6.5 是（用于任意长度消息的）安全 MAC。

PROOF Let $\Pi^{\prime}$ denote Construction 6.5, and let $\mathcal{A}^{\prime}$ be a PPT adversary attacking $\Pi^{\prime}$. In an execution of experiment $\mathsf{Mac-forge}_{\mathcal{A}^{\prime},\Pi^{\prime}}(n)$, let $(k,s)$ denote the key (of $\Pi^{\prime}$), let $\mathcal{Q}$ denote the set of messages whose tags were requested by $\mathcal{A}^{\prime}$, and let $(m^*,t)$ be the final output of $\mathcal{A}^{\prime}$. We assume without loss of generality that $m^*\notin\mathcal{Q}$. Define $\mathsf{coll}$ to be the event that, in experiment $\mathsf{Mac-forge}_{\mathcal{A}^{\prime},\Pi^{\prime}}(n)$, there is an $m\in\mathcal{Q}$ for which $H^s(m^*)=H^s(m)$. We have

**证明** 令 $\Pi^{\prime}$ 表示构造 6.5，令 $\mathcal{A}^{\prime}$ 是攻击 $\Pi^{\prime}$ 的 PPT 敌手。在实验 $\mathsf{Mac-forge}_{\mathcal{A}^{\prime},\Pi^{\prime}}(n)$ 的一次执行中，令 $(k,s)$ 表示（$\Pi^{\prime}$ 的）密钥，令 $\mathcal{Q}$ 表示 $\mathcal{A}^{\prime}$ 请求过标签的消息集合，令 $(m^*,t)$ 为 $\mathcal{A}^{\prime}$ 的最终输出。我们不失一般性地假设 $m^*\notin\mathcal{Q}$。定义 $\mathsf{coll}$ 为实验 $\mathsf{Mac-forge}_{\mathcal{A}^{\prime},\Pi^{\prime}}(n)$ 中存在 $m\in\mathcal{Q}$ 使得 $H^s(m^*)=H^s(m)$ 这一事件。我们有

$$
\begin{aligned}&\Pr[\mathsf{Mac-forge}_{\mathcal{A}^{\prime},\Pi^{\prime}}(n)=1]\\ &=\Pr[\mathsf{Mac-forge}_{\mathcal{A}^{\prime},\Pi^{\prime}}(n)=1\land\mathsf{coll}]+\Pr[\mathsf{Mac-forge}_{\mathcal{A}^{\prime},\Pi^{\prime}}(n)=1\land\overline{\mathsf{coll}}]\\ &\leq\Pr[\mathsf{coll}]+\Pr[\mathsf{Mac-forge}_{\mathcal{A}^{\prime},\Pi^{\prime}}(n)=1\land\overline{\mathsf{coll}}].\\ \end{aligned}
$$

We show that both terms in Equation (6.1) are negligible, thus completing the proof. Intuitively, the first term is negligible by collision resistance of $\mathcal{H}$, and the second term is negligible by security of $\Pi$.

我们证明式 (6.1) 中的两项都是可忽略的，从而完成证明。直观上，第一项由 $\mathcal{H}$ 的抗碰撞性可知是可忽略的，第二项由 $\Pi$ 的安全性可知是可忽略的。

Consider the following algorithm C for finding a collision in H:

考虑以下在 H 中寻找碰撞的算法 C：

Algorithm C:

算法 C：

The algorithm is given input s (with n implicit).

该算法获得输入 s（其中 n 是隐含的）。

- Choose uniform $k \in \{0,1\}^{n}$.

- Run $\mathcal{A}^{\prime}(1^n)$. When $\mathcal{A}^{\prime}$ requests a tag on the $i$th message $m_i \in \{0,1\}^*$, compute $t_i \leftarrow \mathsf{Mac}_k(H^s(m_i))$ and give $t_i$ to $\mathcal{A}^{\prime}$.

- When $\mathcal{A}^{\prime}$ outputs $(m^*, t)$, then if there exists an $i$ for which $H^s(m^*) = H^s(m_i)$, output $(m^*, m_i)$.

- 选择均匀的 $k \in \{0,1\}^{n}$。

- 运行 $\mathcal{A}^{\prime}(1^n)$。当 $\mathcal{A}^{\prime}$ 请求第 $i$ 个消息 $m_i \in \{0,1\}^*$ 的标签时，计算 $t_i \leftarrow \mathsf{Mac}_k(H^s(m_i))$ 并将 $t_i$ 给 $\mathcal{A}^{\prime}$。

- 当 $\mathcal{A}^{\prime}$ 输出 $(m^*, t)$ 时，如果存在某个 $i$ 使得 $H^s(m^*) = H^s(m_i)$，则输出 $(m^*, m_i)$。

It is clear that $\mathcal{C}$ runs in polynomial time. Let us analyze its behavior. When the input to $\mathcal{C}$ is generated by running $\mathsf{Gen}_H(1^n)$ to obtain $s$, the view of $\mathcal{A}^{\prime}$ when run as a subroutine by $\mathcal{C}$ is distributed identically to the view of $\mathcal{A}^{\prime}$ in experiment $\mathsf{Mac-forge}_{\mathcal{A}^{\prime},\Pi^{\prime}}(n)$. Thus, the probability that $\mathsf{coll}$ occurs is the same in both cases. Since $\mathcal{C}$ outputs a collision when $\mathsf{coll}$ occurs, we have

显然 $\mathcal{C}$ 在多项式时间内运行。让我们分析其行为。当 $\mathcal{C}$ 的输入是由运行 $\mathsf{Gen}_H(1^n)$ 得到的 $s$ 时，$\mathcal{A}^{\prime}$ 作为 $\mathcal{C}$ 的子程序运行时的视图与 $\mathcal{A}^{\prime}$ 在实验 $\mathsf{Mac-forge}_{\mathcal{A}^{\prime},\Pi^{\prime}}(n)$ 中的视图分布相同。因此 $\mathsf{coll}$ 发生的概率在两种情形下相同。由于 $\mathcal{C}$ 在 $\mathsf{coll}$ 发生时输出一个碰撞，我们有

$$
\Pr[\mathsf{Hash-coll}_{\mathcal{C},\mathcal{H}}(n)=1]=\Pr[\mathsf{coll}].
$$

Collision resistance of H thus implies that Pr[coll] is negligible.

因此 H 的抗碰撞性蕴含 Pr[coll] 是可忽略的。

We now proceed to prove that the second term in Equation (6.1) is negligible. Consider the following adversary $\mathcal{A}$ attacking $\Pi$ in $\mathsf{Mac-forge}_{\mathcal{A}, \Pi}(n)$:

我们现在着手证明式 (6.1) 中的第二项是可忽略的。考虑以下在 $\mathsf{Mac-forge}_{\mathcal{A}, \Pi}(n)$ 中攻击 $\Pi$ 的敌手 $\mathcal{A}$：

Adversary A:

敌手 A：

The adversary is given ${1}^{n}$ and access to an oracle $\mathrm{Mac}_{k}(\cdot)$.

该敌手获得 ${1}^{n}$ 并可访问预言机 $\mathrm{Mac}_{k}(\cdot)$。

- Compute $\mathsf{Gen}_{H}(1^{n})$ to obtain s.

- Run $\mathcal{A}^{\prime}(1^n)$. When $\mathcal{A}^{\prime}$ requests a tag on the $i$th message $m_i \in \{0,1\}^*$, then: (1) compute $h_i := H^s(m_i)$; (2) obtain a tag $t_i$ on $h_i$ from the MAC oracle; and (3) give $t_i$ to $\mathcal{A}^{\prime}$.

- When $\mathcal{A}^{\prime}$ outputs $(m^*, t)$, set $h^* := H^s(m^*)$ and then output $(h^*, t)$.

- 计算 $\mathsf{Gen}_{H}(1^{n})$ 得到 s。

- 运行 $\mathcal{A}^{\prime}(1^n)$。当 $\mathcal{A}^{\prime}$ 请求第 $i$ 个消息 $m_i \in \{0,1\}^*$ 的标签时，则：(1) 计算 $h_i := H^s(m_i)$；(2) 从 MAC 预言机获得 $h_i$ 上的标签 $t_i$；(3) 将 $t_i$ 给 $\mathcal{A}^{\prime}$。

- 当 $\mathcal{A}^{\prime}$ 输出 $(m^*, t)$ 时，置 $h^* := H^s(m^*)$，然后输出 $(h^*, t)$。

$\mathcal{A}$ runs in polynomial time. If $\mathcal{A}^{\prime}$ outputs $(m^*, t)$ with $\mathsf{Vrfy}_k(H^s(m^*), t) = 1$, and $\mathsf{coll}$ did not occur, then $\mathcal{A}$ outputs a valid forgery. (In that case $t$ is a valid tag on $h^* = H^s(m^*)$ in scheme $\Pi$ with respect to $k$. The fact that $\mathsf{coll}$ did not occur means that $h^*$ was never asked by $\mathcal{A}$ to its own MAC oracle and so this is indeed a forgery.) Moreover, the view of $\mathcal{A}^{\prime}$ when run as a subroutine by $\mathcal{A}$ in experiment $\mathsf{Mac-forge}_{\mathcal{A},\Pi}(n)$ is distributed identically to the view of $\mathcal{A}^{\prime}$ in experiment $\mathsf{Mac-forge}_{\mathcal{A}^{\prime},\Pi^{\prime}}(n)$. We conclude that

$\mathcal{A}$ 在多项式时间内运行。如果 $\mathcal{A}^{\prime}$ 输出 $(m^*, t)$ 满足 $\mathsf{Vrfy}_k(H^s(m^*), t) = 1$，且 $\mathsf{coll}$ 未发生，则 $\mathcal{A}$ 输出一个有效伪造。（在该情形下 $t$ 是方案 $\Pi$ 中相对于 $k$ 在 $h^* = H^s(m^*)$ 上的有效标签。$\mathsf{coll}$ 未发生这一事实意味着 $\mathcal{A}$ 从未向其自身的 MAC 预言机查询过 $h^*$，因此这确实是一个伪造。）此外，$\mathcal{A}^{\prime}$ 在实验 $\mathsf{Mac-forge}_{\mathcal{A},\Pi}(n)$ 中作为 $\mathcal{A}$ 的子程序运行时的视图，与 $\mathcal{A}^{\prime}$ 在实验 $\mathsf{Mac-forge}_{\mathcal{A}^{\prime},\Pi^{\prime}}(n)$ 中的视图分布相同。我们得出

$$
\Pr[\mathsf{Mac-forge}_{\mathcal{A},\Pi}(n)=1]=\Pr[\mathsf{Mac-forge}_{\mathcal{A}^{\prime},\Pi^{\prime}}(n)=1\land\overline{{\mathsf{coll}}}],
$$

and security of $\Pi$ implies that the former probability is negligible. This concludes the proof of the theorem.

而 $\Pi$ 的安全性蕴含前一个概率是可忽略的。至此完成定理的证明。

### 6.3.2 HMAC　6.3.2 HMAC

In principle, the hash-and-MAC approach from the previous section could be instantiated by combining an arbitrary collision-resistant hash function with the fixed-length MAC of Construction 4.5. This way of realizing the hash-and-MAC approach has at least two drawbacks in practice. First, it requires implementing two cryptographic primitives: a hash function and a block cipher. (Recall that Construction 4.5 is based on a block cipher, and supports messages of length equal to the block length of the cipher.) This can be a problem, e.g., in constrained devices, where it is desirable to keep the size of the code implementing a cryptographic scheme as small as possible. A more fundamental difficulty is that there is often a mismatch between the output length of hash functions and the block length of block ciphers. (This is in part due to a difference between the parameters needed to achieve security for a block cipher vs. a hash function, as will be explored in the next section.) For example, the block cipher AES has a 128-bit block length, whereas modern hash functions have output lengths of at least 256 bits—and a 128-bit output length would be far too short to ensure meaningful collision resistance.

原则上，上一节的哈希后认证方法可以通过将任意的抗碰撞哈希函数与构造 4.5 的固定长度 MAC 组合来实例化。以这种方式实现哈希后认证方法在实践中至少有两个缺点。首先，它需要实现两个密码学原语：一个哈希函数和一个分组密码。（回忆构造 4.5 基于分组密码，并支持长度等于该密码分组长度的消息。）这可能是个问题，例如在受限设备中，我们希望实现密码学方案的代码规模尽可能小。一个更根本的困难是，哈希函数的输出长度与分组密码的分组长度常常不匹配。（这部分是由于分组密码与哈希函数各自实现安全性所需的参数不同，下一节将探讨这一点。）例如，分组密码 AES 的分组长度为 128 比特，而现代哈希函数的输出长度至少为 256 比特——128 比特的输出长度对于确保有意义的抗碰撞性来说太短了。

> **CONSTRUCTION 6.7**　**构造 6.7**
>
> Let $(\mathsf{Gen}_H, H)$ be a hash function constructed by applying the Merkle–Damgård transform to a compression function $(\mathsf{Gen}_H, h)$ that takes inputs of length $n + n^{\prime} > 2n + \log n + 2$ and generates output of length $n$. Fix distinct constants $\text{opad}, \text{ipad} \in \{0,1\}^{n^{\prime}}$. Define a MAC as follows:
>
> Gen: on input ${1}^n$, run $\mathsf{Gen}_H(1^n)$ to obtain a key $s$. Also choose uniform $k \in \{0,1\}^{n^{\prime}}$. Output the key $(s,k)$.
>
> Mac: on input a key $(s,k)$ and a message $m \in \{0,1\}^{*}$, output
>
> $$
> t:=H^{s}\Big((k\oplus\mathsf{opad})\parallel H^{s}\big((k\oplus\mathsf{ipad})\parallel m\big)\Big).
> $$
>
> - $\mathsf{Vrfy}$: on input a key $(s,k)$, a message $m \in \{0,1\}^*$, and a tag $t$, output 1 if and only if $t \stackrel{?}{=} H^s\left((k \oplus \text{opad}) \parallel H^s\left((k \oplus \text{ipad}) \parallel m\right)\right)$.
>
> 设 $(\mathsf{Gen}_H, H)$ 是通过对压缩函数 $(\mathsf{Gen}_H, h)$（该压缩函数接受长度为 $n + n^{\prime} > 2n + \log n + 2$ 的输入并生成长度为 $n$ 的输出）应用 Merkle–Damgård 变换而构造的哈希函数。取定不同的常数 $\text{opad}, \text{ipad} \in \{0,1\}^{n^{\prime}}$。定义 MAC 如下：
>
> Gen：输入 ${1}^n$，运行 $\mathsf{Gen}_H(1^n)$ 得到密钥 $s$。同时选择均匀的 $k \in \{0,1\}^{n^{\prime}}$。输出密钥 $(s,k)$。
>
> Mac：输入密钥 $(s,k)$ 和消息 $m \in \{0,1\}^{*}$，输出
>
> $$
> t:=H^{s}\Big((k\oplus\mathsf{opad})\parallel H^{s}\big((k\oplus\mathsf{ipad})\parallel m\big)\Big).
> $$
>
> - $\mathsf{Vrfy}$：输入密钥 $(s,k)$、消息 $m \in \{0,1\}^*$ 和标签 $t$，当且仅当 $t \stackrel{?}{=} H^s\left((k \oplus \text{opad}) \parallel H^s\left((k \oplus \text{ipad}) \parallel m\right)\right)$ 时输出 1。
>
> **HMAC.**
>
> **HMAC。**

The above concerns motivated the design of HMAC, a message authentication code for arbitrary-length messages that can be based on any hash function $(\mathsf{Gen}_{H}, H)$ constructed using the Merkle–Damgård transform applied to a compression function $(\mathsf{Gen}_{H}, h)$. See Construction 6.7 for a high-level overview that abstracts out the underlying compression function, and Figure 6.2 for a graphical depiction that makes the compression function explicit.

上述顾虑促成了 HMAC 的设计，它是一种用于任意长度消息的消息认证码，可基于任何通过对压缩函数 $(\mathsf{Gen}_{H}, h)$ 应用 Merkle–Damgård 变换而构造的哈希函数 $(\mathsf{Gen}_{H}, H)$。构造 6.7 给出了抽象掉底层压缩函数的高层概览，图 6.2 给出了使压缩函数显式化的图形描绘。

Referring to Figure 6.2, we see that computation of HMAC on a message $m = m_1, m_2, \ldots$ using key k can be separated into an “inner” hash evaluation and an “outer” hash evaluation.

参见图 6.2，我们看到使用密钥 $k$ 对消息 $m = m_1, m_2, \ldots$ 计算 HMAC 可以分为“内层”哈希求值和“外层”哈希求值。

![Image](https://lsky.jerryxue.top/i/2026/08/22/6a88f9e708ec5.jpg)

**FIGURE 6.2: HMAC, pictorially.** The inner hash evaluation involves computing $\hat{m} := H^s((k \oplus \text{ipad})\|m)$, where $\text{ipad}$ is some fixed constant. As per the definition of the Merkle–Damgård transform, the input to $H^s$—which, in this case, is the string $(k \oplus \text{ipad})\|m$—is padded as part of the hash computation; this padding is left implicit in Figure 6.2. The outer hash evaluation involves computation of the tag $t := H^s((k \oplus \text{opad})\| \hat{m})$, where $\text{opad}$ is another fixed constant; note that $k$, $\text{ipad}$, and $\text{opad}$ are all exactly $n^{\prime}$ bits long. Once again, padding is applied to the $(n^{\prime} + n)$-bit input string $(k \oplus \text{opad})\|\hat{m}$ as part of the hash computation; parameters are set such that the padded string is exactly two blocks long. That is, if we let $k_{out} \overset{\mathrm{def}}{=} h^s(IV\|(k \oplus \text{opad}))$ as in the figure, then $t = h^s(k_{out} \|\hat{m}^*)$, where $\hat{m}^*$ is the second block after padding.

**图 6.2：HMAC 的示意图。** 内层哈希求值涉及计算 $\hat{m} := H^s((k \oplus \text{ipad})\|m)$，其中 $\text{ipad}$ 是某个固定常数。按照 Merkle–Damgård 变换的定义，$H^s$ 的输入——在此情形下是串 $(k \oplus \text{ipad})\|m$——作为哈希计算的一部分被填充；该填充在图 6.2 中是隐含的。外层哈希求值涉及计算标签 $t := H^s((k \oplus \text{opad})\| \hat{m})$，其中 $\text{opad}$ 是另一个固定常数；注意 $k$、$\text{ipad}$ 和 $\text{opad}$ 都恰好长 $n^{\prime}$ 比特。同样地，作为哈希计算的一部分，要对 $(n^{\prime} + n)$ 比特的输入串 $(k \oplus \text{opad})\|\hat{m}$ 进行填充；参数的设置使得填充后的串恰好由两个块组成。也就是说，如果如图所示令 $k_{out} \overset{\mathrm{def}}{=} h^s(IV\|(k \oplus \text{opad}))$，则 $t = h^s(k_{out} \|\hat{m}^*)$，其中 $\hat{m}^*$ 是填充后的第二个块。

Given this perspective, we see that HMAC can be viewed as an instantiation of the hash-and-MAC paradigm from the previous section, where the inner computation corresponds to hashing the message $m$ to an $n^{\prime}$-bit string $\hat{m}^*$ (including the padding), and the outer computation corresponds to computing a fixed-length message authentication code on $\hat{m}^*$. Formally, let $\widetilde{\Pi}^s = (\widetilde{\mathsf{Gen}}^s, \widetilde{\mathsf{Mac}}^s, \widetilde{\mathsf{Vrfy}}^s)$ be the message authentication code in which $\widetilde{\mathsf{Mac}}^{s}_{k_{out}}(\hat{m}^*) = h^s(k_{out} \| \hat{m}^*)$ (We view $s$ here as a fixed, public value.) Intuitively, then, if $(\mathsf{Gen}_H, h)$ is collision resistant and $\widetilde{\Pi}^s$ is secure, HMAC is secure. As a technical matter, though, since the key $k_{out}$ used by the MAC $\widetilde{\Pi}^s$ is derived from an underlying key $k$ that is also used in the inner hash evaluation, we need one additional assumption regarding the “computational independence” of $k_{in} \overset{\mathrm{def}}{=} h^s(IV \| (k \oplus \text{ipad}))$ and $k_{out}$. Specifically, define

从这个角度看，我们看到 HMAC 可被视为上一节哈希后认证范式的一种实例化，其中内层计算对应于把消息 $m$ 哈希为一个 $n^{\prime}$ 比特串 $\hat{m}^*$（包括填充），外层计算对应于在 $\hat{m}^*$ 上计算固定长度的消息认证码。形式化地，令 $\widetilde{\Pi}^s = (\widetilde{\mathsf{Gen}}^s, \widetilde{\mathsf{Mac}}^s, \widetilde{\mathsf{Vrfy}}^s)$ 是这样的消息认证码：$\widetilde{\mathsf{Mac}}^{s}_{k_{out}}(\hat{m}^*) = h^s(k_{out} \| \hat{m}^*)$（我们在此把 $s$ 视为一个固定的、公开的值。）那么直观上，如果 $(\mathsf{Gen}_H, h)$ 是抗碰撞的且 $\widetilde{\Pi}^s$ 是安全的，则 HMAC 是安全的。但作为一个技术细节，由于 MAC $\widetilde{\Pi}^s$ 所用的密钥 $k_{out}$ 派生自同样用于内层哈希求值的底层密钥 $k$，我们需要一个关于 $k_{in} \overset{\mathrm{def}}{=} h^s(IV \| (k \oplus \text{ipad}))$ 与 $k_{out}$ 之间“计算独立性”的额外假设。具体地，定义

$$
G^{s}(k)\stackrel{\mathrm{def}}{=}h^{s}\left(IV\|(k\oplus\mathsf{ipad})\right)\|h^{s}\left(IV\|(k\oplus\mathsf{opad})\right)=k_{in}\|k_{out}.
$$

Then it is possible to prove:

那么可以证明：

THEOREM 6.8 Assume $G^{s}$ is a pseudorandom generator, $\widetilde{\Pi}^{s}$ is a secure fixed-length MAC for messages of length $n^{\prime}$, and $(\mathsf{Gen}_{H}, h)$ is collision resistant. Then HMAC is a secure MAC (for arbitrary-length messages).

**定理 6.8** 假设 $G^{s}$ 是伪随机生成器，$\widetilde{\Pi}^{s}$ 是用于长度为 $n^{\prime}$ 的消息的安全固定长度 MAC，且 $(\mathsf{Gen}_{H}, h)$ 是抗碰撞的。则 HMAC 是（用于任意长度消息的）安全 MAC。

(We require the first two assumptions in the theorem to hold for all s. Even if $G^{s}$ is not expanding, it is still meaningful to speak of its output as being pseudorandom.) Because of the way the compression function h is typically designed (see Section 7.3.1), the first two assumptions are reasonable.

（我们要求该定理的前两个假设对所有 s 成立。即使 $G^{s}$ 不具扩展性，说它的输出是伪随机的仍然是有意义的。）考虑到压缩函数 h 的典型设计方式（见 7.3.1 节），前两个假设是合理的。

The roles of ipad and opad. One might wonder why it is necessary to incorporate $k_{in}$ (or k itself) in the “inner” computation at all. In particular, for the hash-and-MAC approach all that is required is for the inner computation to be collision resistant, which does not require any secret key. The reason for including a secret key as part of the inner computation is that this allows security of HMAC to be based on the assumption that $(\mathsf{Gen}_H, H)$ is weakly collision resistant, where (informally) this refers to an experiment in which an attacker needs to find collisions in a secretly keyed hash function. This is a weaker condition than collision resistance, and hence is potentially easier to satisfy. The defensive design strategy of HMAC paid off when it was discovered that the hash function MD5 (see Section 7.3.2) used in HMAC–MD5 was not collision resistant. The attacks on MD5 did not violate weak collision resistance, and so HMAC–MD5 was not broken even though MD5 was. (Despite this, HMAC–MD5 should no longer be used now that weaknesses in MD5 are known.) This gave developers time to replace MD5 in HMAC implementations, without immediate fear of attack.

ipad 和 opad 的作用。人们可能想知道为什么有必要在“内层”计算中纳入 $k_{in}$（或 k 本身）。特别地，对于哈希后认证方法，只要求内层计算是抗碰撞的即可，而这并不需要任何秘密密钥。在内层计算中包含秘密密钥，是为了使 HMAC 的安全性可以基于 $(\mathsf{Gen}_H, H)$ 是弱抗碰撞的这一假设，其中（非正式地）指的是这样一个实验：攻击者需要在带秘密密钥的哈希函数中找到碰撞。这是比抗碰撞性更弱的条件，因此可能更容易满足。当发现 HMAC-MD5 中使用的哈希函数 MD5（见 7.3.2 节）并不抗碰撞时，HMAC 的这种防御性设计策略发挥了作用。对 MD5 的攻击并未违反弱抗碰撞性，因此即便 MD5 被攻破，HMAC-MD5 也未被攻破。（尽管如此，既然 MD5 的弱点现已知晓，HMAC-MD5 不应再被使用。）这为开发者争取了替换 HMAC 实现中 MD5 的时间，而无需立即担忧攻击。

Ideally, independent keys $k_{in}$, $k_{out}$ should have been used in the inner and outer computations. To reduce the key length of HMAC, a single key k is used to derive $k_{in}$ and $k_{out}$ using ipad and opad. (Moreover, in practice it is typical for the length of k to be much shorter than $n^{\prime}$—in which case k is simply padded with 0s before being XORed with ipad and opad.) If we assume that $G^{s}$ (as defined above) is a pseudorandom generator for any s, then $k_{in}$ and $k_{out}$ can be treated as independent, uniform keys when k is uniform.

理想情况下，内层和外层计算应当使用独立的密钥 $k_{in}$、$k_{out}$。为了缩短 HMAC 的密钥长度，使用单一密钥 $k$ 借助 ipad 和 opad 来派生 $k_{in}$ 和 $k_{out}$。（此外，实践中 k 的长度通常比 $n^{\prime}$ 短得多——此时 k 在与 ipad 和 opad 异或之前简单地用 0 填充。）如果我们假设 $G^{s}$（如上定义）对任意 s 都是伪随机生成器，那么当 k 均匀时，$k_{in}$ 和 $k_{out}$ 可被视为独立的均匀密钥。

## 6.4 Generic Attacks on Hash Functions　6.4 针对哈希函数的通用攻击

In the context of the symmetric-key primitives we have studied so far (block ciphers, private-key encryption schemes, etc.), we noted that any scheme using an $n$-bit secret key is vulnerable to a brute-force attack in which an attacker enumerates all ${2}^n$ possible keys until it finds the right one. (Of course, this does not apply to information-theoretic schemes.) Put differently, if we want to achieve security against attackers running in time ${2}^n$ then we need to use secret keys that are at least $n$ bits long.

在我们迄今研究的对称密钥原语（分组密码、私钥加密方案等）的语境中，我们注意到任何使用 $n$ 比特秘密密钥的方案都容易受到蛮力攻击，即攻击者枚举所有 ${2}^n$ 个可能的密钥直到找到正确的那一个。（当然，这不适用于信息论方案。）换言之，如果我们想要获得针对运行时间为 ${2}^n$ 的攻击者的安全性，就需要使用至少 $n$ 比特长的秘密密钥。

What can we say about the security of hash functions against brute-force attacks? We show here that a birthday attack allows an attacker to find a collision in any hash function having an $\ell$-bit output length in time ${2}^{\ell/2}$. Thus, if we want to ensure collision resistance against attackers running in time ${2}^n$ we need to use hash functions whose output is at least ${2}n$ bits long—twice the length of secret keys providing comparable security guarantees.

关于哈希函数抗蛮力攻击的安全性，我们能说什么呢？我们在此表明，生日攻击（birthday attack）使攻击者能够在 ${2}^{\ell/2}$ 的时间内找到任何输出长度为 $\ell$ 比特的哈希函数中的一个碰撞。因此，如果我们想确保针对运行时间为 ${2}^n$ 的攻击者的抗碰撞性，就需要使用输出至少 ${2}n$ 比特长的哈希函数——是提供相当安全性保证的秘密密钥长度的两倍。

While on the topic of generic attacks (i.e., attacks that apply to arbitrary hash functions), we also consider attacks on preimage resistance, where the attacker's goal is to find an input x that hashes to a given value y. Here the question is complicated by the attacker's ability to use preprocessing and a large amount of storage to speed up the attack. This has important ramifications in practice when hashing users' passwords, something we touch on in Section 6.6.3.

在讨论通用攻击（即适用于任意哈希函数的攻击）这一主题时，我们还考虑针对原像抗性的攻击，其中攻击者的目标是找到一个哈希到给定值 $y$ 的输入 $x$。这里，问题之所以复杂，是因为攻击者能够利用预处理和大量存储来加速攻击。这在实践中对用户口令的哈希有重要影响，我们在 6.6.3 节涉及这一点。

### 6.4.1 Birthday Attacks for Finding Collisions　6.4.1 寻找碰撞的生日攻击

Let $H : \{0,1\}^* \to \{0,1\}^\ell$ be a hash function. For any such $H$, there is always a trivial collision-finding attack running in time $\mathcal{O}(2^\ell)$: simply evaluate $H$ on $q = 2^\ell + 1$ distinct inputs; by the pigeonhole principle, two of the outputs must be equal. Is this the best possible attack?

设 $H : \{0,1\}^* \to \{0,1\}^\ell$ 是一个哈希函数。对于任何这样的 $H$，总存在一个平凡的、运行时间为 $\mathcal{O}(2^\ell)$ 的找碰撞攻击：只需在 $q = 2^\ell + 1$ 个不同输入上对 $H$ 求值；由鸽巢原理，必有两个输出相等。这是否已是最好的攻击？

Let us generalize the above algorithm by taking $q$ as a parameter. Say we choose $q$ uniform (distinct) inputs $x_1, \ldots, x_q$, compute $y_i := H(x_i)$ for all $i$, and check whether any of the $\{y_i\}$ are equal. As noted, if $q > 2^\ell$ then there is certainly a collision. When $q \leq 2^\ell$ we can no longer guarantee a collision, but there is clearly some nonzero probability that a collision occurs. It is somewhat difficult to analyze this probability when $H$ is arbitrary, and so we instead consider the idealized case where $H$ is treated as a random function. (It can be shown that this is the worst case, and collisions occur with higher probability if $H$ deviates from random.) That is, for each $i$ we assume that the value $y_i = H(x_i)$ is uniformly distributed in $\{0,1\}^\ell$ and independent of all the other values $\{y_j\}_{j\neq i}$ (recall all the $\{x_i\}$ are distinct). We have thus reduced our problem to the following: if we generate uniform $y_1, \ldots, y_q \in \{0,1\}^\ell$, what is the probability that there exist distinct $i, j$ with $y_i = y_j?$

让我们通过把 $q$ 作为参数来推广上述算法。假设我们选择 $q$ 个均匀的（不同的）输入 $x_1, \ldots, x_q$，对所有 $i$ 计算 $y_i := H(x_i)$，并检查是否有任何 $\{y_i\}$ 相等。如前所述，如果 $q > 2^\ell$ 则必然存在碰撞。当 $q \leq 2^\ell$ 时我们不能再保证存在碰撞，但显然存在碰撞发生的某个非零概率。当 $H$ 任意时，分析这一概率有些困难，因此我们转而考虑把 $H$ 视为随机函数的理想化情形。（可以证明这是最坏情形：如果 $H$ 偏离随机，则碰撞以更高概率发生。）即对每个 $i$，我们假设值 $y_i = H(x_i)$ 均匀分布于 $\{0,1\}^\ell$ 且与所有其他值 $\{y_j\}_{j\neq i}$ 独立（回忆所有 $\{x_i\}$ 是不同的）。这样我们就把问题归结为：如果我们生成均匀的 $y_1, \ldots, y_q \in \{0,1\}^\ell$，存在不同 $i, j$ 使得 $y_i = y_j$ 的概率是多少？

This question has been extensively studied, and is related to the so-called birthday problem discussed in detail in Appendix A.4; for this reason the collision-finding algorithm described above is one of a class of algorithms called birthday attacks. The birthday problem is this: if $q$ people are in a room, what is the probability that some two of them share a birthday? (Assume birthdays are uniformly and independently distributed among the 365 days of a non-leap year.) This is analogous to our problem: if $y_i$ is the birthday of person $i$, then we have uniform and independent $y_1,\ldots,y_q\in\{1,\ldots,365\}$, and matching birthdays correspond to distinct $i,j$ with $y_i=y_j$ (i.e., matching birthdays correspond to collisions).

这个问题已被广泛研究，并与附录 A.4 中详细讨论的所谓生日问题相关；出于这一原因，上述找碰撞的算法属于一类称为生日攻击的算法。生日问题是这样：如果房间里有 $q$ 个人，其中某两个人生日相同的概率是多少？（假设生日在非闰年的 365 天中均匀且独立地分布。）这与我们的问题类似：如果 $y_i$ 是第 $i$ 个人的生日，那么我们有均匀且独立的 $y_1,\ldots,y_q\in\{1,\ldots,365\}$，而生日匹配对应于不同的 $i,j$ 满足 $y_i=y_j$（即生日匹配对应于碰撞）。

In Appendix A.4 we show that when $y_1, \ldots, y_q$ are uniform in $\{1, \ldots, N\}$, then if $q = \Theta(N^{1/2})$ the probability of a collision is roughly ${1}/{2}$. (In the case of birthdays, once there are only 23 people the probability that some two of them have the same birthday is roughly 51%!) In our setting, this means that when the hash function $H$ has output length $\ell$ (and so has range of size $N = 2^{\ell}$), evaluating $H$ on $q = \Theta(2^{\ell/2})$ inputs yields a collision with probability roughly 1/2. From a concrete-security perspective, this implies that for a hash function $H$ to be collision resistant against attackers running in time ${2}^n$ it is required that $H$ have output at least ${2}n$ bits long. Taking specific parameters: if we want finding collisions to be as difficult as an exhaustive search over 128-bit keys, then we need the output length of the hash function to be at least 256 bits. (We stress that having output this long is only a necessary condition, not a sufficient one.)

在附录 A.4 中我们证明，当 $y_1, \ldots, y_q$ 在 $\{1, \ldots, N\}$ 上均匀分布时，如果 $q = \Theta(N^{1/2})$，则碰撞的概率大约为 ${1}/{2}$。（在生日的例子中，只要有 23 个人，其中某两个人生日相同的概率就大约为 51%！）在我们的设置中，这意味着当哈希函数 $H$ 的输出长度为 $\ell$（因而值域大小为 $N = 2^{\ell}$）时，在 $q = \Theta(2^{\ell/2})$ 个输入上对 $H$ 求值将以大约 1/2 的概率产生碰撞。从具体安全性的角度看，这蕴含：要使哈希函数 $H$ 对运行时间为 ${2}^n$ 的攻击者抗碰撞，$H$ 的输出必须至少长 ${2}n$ 比特。取具体参数：如果我们希望寻找碰撞与对 128 比特密钥的穷举搜索一样困难，那么哈希函数的输出长度需要至少为 256 比特。（我们强调，输出这么长只是一个必要条件，而非充分条件。）

Finding meaningful collisions. The birthday attack just described gives a collision that is not necessarily very useful, since the colliding inputs are random. But the same idea can be used to find “meaningful” collisions as well. Assume Alice wishes to find two messages $x$ and $x^{\prime}$ such that $H(x) = H(x^{\prime})$, and furthermore $x$ should be a letter from her employer explaining why she was fired from work, while $x^{\prime}$ should be a flattering letter of recommendation. (This might allow Alice to forge a tag on a letter of recommendation if the hash-and-MAC approach is being used by her employer to authenticate messages.) Note that the birthday attack only requires the hash inputs $x_1, \ldots, x_q$ to be distinct; they do not need to be random. Alice can carry out a birthday attack by generating $q = \Theta(2^{\ell/2})$ messages of the first type and $q$ messages of the second type, and then looking for collisions between messages of the two types. A small change to the analysis from Appendix A.4 shows that this gives a collision between messages of different types with probability roughly ${1}/{2}$. A little thought shows that it is easy to write the same message in many different ways. For example, consider the following:

寻找有意义的碰撞。刚才描述的生日攻击给出的碰撞不一定很有用，因为碰撞的输入是随机的。但同样的思想也可用于寻找“有意义的”碰撞。假设 Alice 希望找到两条消息 $x$ 和 $x^{\prime}$ 使得 $H(x) = H(x^{\prime})$，并且进一步要求 $x$ 是她雇主解释她为何被解雇的信，而 $x^{\prime}$ 是一封赞誉的推荐信。（如果她的雇主使用哈希后认证方法来认证消息，这可能使 Alice 能够伪造推荐信上的标签。）注意，生日攻击只要求哈希输入 $x_1, \ldots, x_q$ 是不同的；它们不必是随机的。Alice 可以通过生成 $q = \Theta(2^{\ell/2})$ 条第一种类型的消息和 $q$ 条第二种类型的消息，然后在两种类型的消息之间寻找碰撞来实施生日攻击。对附录 A.4 的分析作小修改即可表明，这以大约 ${1}/{2}$ 的概率给出不同类型消息之间的碰撞。稍加思考可知，用许多不同方式写出同一条消息是容易的。例如，考虑下面这句话：

It is hard/difficult/challenging/impossible to imagine/believe that we will find/locate/hire another employee/person having similar abilities/skills/character as Alice. She has done a great/super job.

很难/困难/有挑战性/不可能 想象/相信 我们会 找到/定位/雇到 另一位像 Alice 那样具有类似能力/技能/品格的 员工/个人。她做了一份 出色/超级 的工作。

Any combination of the italicized words is possible, and expresses the same idea. Thus, the sentence can be written in ${4}\cdot2\cdot3\cdot2\cdot3\cdot2=288$ different ways. This is just one sentence and so it is actually easy to generate a message that can be rewritten in ${2}^{64}$ different ways—all that is needed are 64 words with one synonym each. Alice can prepare ${2}^{\ell/2}$ letters explaining why she was fired and another ${2}^{\ell/2}$ letters of recommendation; with good probability, a collision between the two types of letters will be found.

任何斜体词的组合都是可能的，并且表达相同的意思。因此，该句子可以以 ${4}\cdot2\cdot3\cdot2\cdot3\cdot2=288$ 种不同方式写出。这只是一句话，因此实际上很容易生成一条可以以 ${2}^{64}$ 种不同方式改写的消息——所需的只是 64 个各有一个同义词的词。Alice 可以准备 ${2}^{\ell/2}$ 封解释她为何被解雇的信和另外 ${2}^{\ell/2}$ 封推荐信；以很大的概率，将在两种类型的信之间找到碰撞。

### 6.4.2 Small-Space Birthday Attacks　6.4.2 小空间生日攻击

The birthday attacks described above require a large amount of memory; specifically, they require the attacker to store all $\Theta(q) = \Theta(2^{\ell/2})$ values $\{y_i\}$, because the attacker does not know in advance which pair of values will yield a collision. This is a significant drawback because memory is, in general, a scarcer resource than time: one can always let a computation run as long as needed, whereas if a program requires more memory than is available then that program will simply halt. Furthermore, memory accesses are typically orders of magnitude slower than executing arithmetic instructions.

上述生日攻击需要大量内存；具体而言，它们要求攻击者存储所有 $\Theta(q) = \Theta(2^{\ell/2})$ 个值 $\{y_i\}$，因为攻击者事先不知道哪一对值会产生碰撞。这是一个显著的缺点，因为内存通常是比时间更稀缺的资源：人们总可以让计算运行任意长的时间，但如果一个程序需要的内存超过可用内存，则该程序将直接停机。此外，内存访问通常比执行算术指令慢几个数量级。

We show here a better birthday attack with drastically reduced memory requirements. In fact, it has similar time complexity and success probability as before, but uses only a constant amount of memory. The attack begins by choosing a uniform value $x_0$ and then computing $x_i := H(x_{i-1})$ and $x_{2i} := H(H(x_{2(i-1)}))$ for $i = 1, 2, \ldots$ (Note that $x_i = H^{(i)}(x_0)$ for all $i$, where $H^{(i)}$ refers to $i$-fold iteration of $H$.) In each step the values $x_i$ and $x_{2i}$ are compared; if they are equal then there is a collision somewhere in the sequence $x_0, x_1, \ldots, x_{2i-1}$. (The values $x_{i-1}$ and $x_{2i-1}$ might not be a collision because they may themselves be equal.) The algorithm then finds the least value of $j$ for which $x_j = x_{j+i}$, and outputs $x_{j-1}, x_{j+i-1}$ as a collision. This attack, described formally as Algorithm 6.9 and analyzed below, only requires storage of two hash values in each iteration.

我们在此给出一个内存需求大幅降低的更好的生日攻击。事实上，它具有与之前类似的时间复杂度和成功概率，但只使用常数大小的内存。该攻击首先选择一个均匀值 $x_0$，然后对 $i = 1, 2, \ldots$ 计算 $x_i := H(x_{i-1})$ 和 $x_{2i} := H(H(x_{2(i-1)}))$（注意对所有 $i$ 有 $x_i = H^{(i)}(x_0)$，其中 $H^{(i)}$ 指 $H$ 的 $i$ 重迭代）。在每一步中比较 $x_i$ 和 $x_{2i}$；如果它们相等，则在序列 $x_0, x_1, \ldots, x_{2i-1}$ 中某处存在碰撞。（$x_{i-1}$ 和 $x_{2i-1}$ 可能不是碰撞，因为它们本身可能相等。）然后算法找到使 $x_j = x_{j+i}$ 成立的最小的 $j$，并输出 $x_{j-1}, x_{j+i-1}$ 作为碰撞。这一攻击的形式化描述见算法 6.9，下文将对其进行分析；它每次迭代只需存储两个哈希值。

ALGORITHM 6.9
A small-space birthday attack

算法 6.9
一种小空间生日攻击

Output: Distinct $x, x^{\prime}$ with $H(x) = H(x^{\prime})$
$x_0 \leftarrow \{0,1\}^{\ell+1}$
$x^{\prime} := x := x_0$
for $i = 1,2,\ldots$ do:
 $x := H(x)$
 $x^{\prime} := H(H(x^{\prime}))$ // now $x = H^{(i)}(x_0)$ and $x^{\prime} = H^{(2i)}(x_0)$
        if $x = x^{\prime}$ break
$x^{\prime} := x$, $x := x_0$
for $j = 1$ to $i$:
    if $H(x) = H(x^{\prime})$ return $x, x^{\prime}$ and halt
    else $x := H(x)$, $x^{\prime} := H(x^{\prime})$
    // now $x = H^{(j)}(x_0)$ and $x^{\prime} = H^{(j+i)}(x_0)$

输出：不同的 $x, x^{\prime}$ 满足 $H(x) = H(x^{\prime})$
$x_0 \leftarrow \{0,1\}^{\ell+1}$
$x^{\prime} := x := x_0$
对 $i = 1,2,\ldots$ 执行：
 $x := H(x)$
 $x^{\prime} := H(H(x^{\prime}))$ // 现在 $x = H^{(i)}(x_0)$，$x^{\prime} = H^{(2i)}(x_0)$
        若 $x = x^{\prime}$ 则跳出
$x^{\prime} := x$，$x := x_0$
对 $j = 1$ 到 $i$ 执行：
    若 $H(x) = H(x^{\prime})$ 则返回 $x, x^{\prime}$ 并停机
    否则 $x := H(x)$，$x^{\prime} := H(x^{\prime})$
    // 现在 $x = H^{(j)}(x_0)$，$x^{\prime} = H^{(j+i)}(x_0)$

How many iterations of the first loop do we expect before $x = x^{\prime}$? Consider the sequence of values $x_1, x_2, \ldots$, where $x_i = H^{(i)}(x_0)$ as before. If we model $H$ as a random function, then each $x_i$ is uniform and independent of $x_1, \ldots, x_{i-1}$ as long as no repeat has yet occurred in this sequence. Thus, we expect a repeat to occur with probability ${1}/{2}$ in the first $q = \Theta(2^{\ell/2})$ elements of the sequence. When there is a repeat in the first $q$ elements, the algorithm finds a repeat in at most $q$ iterations of the first loop:

在出现 $x = x^{\prime}$ 之前，我们预期第一个循环要迭代多少次？考虑值序列 $x_1, x_2, \ldots$，其中 $x_i = H^{(i)}(x_0)$ 如前。如果我们把 $H$ 建模为随机函数，那么只要该序列中尚未发生重复，每个 $x_i$ 都是均匀的且独立于 $x_1, \ldots, x_{i-1}$。因此，我们预期该序列的前 $q = \Theta(2^{\ell/2})$ 个元素中以 ${1}/{2}$ 的概率出现重复。当前 $q$ 个元素中存在重复时，算法至多经过第一个循环的 $q$ 次迭代就能找到一个重复：

CLAIM 6.10 Let $x_1, \ldots, x_q$ be a sequence of values with $x_m = H(x_{m-1})$. If $x_I = x_J$ with ${1} \leq I < J \leq q$, then there is an $i < J$ such that $x_i = x_{2i}$.

**断言 6.10** 设 $x_1, \ldots, x_q$ 是满足 $x_m = H(x_{m-1})$ 的值序列。如果 $x_I = x_J$ 且 ${1} \leq I < J \leq q$，则存在 $i < J$ 使得 $x_i = x_{2i}$。

PROOF The sequence $x_I, x_{I+1}, \ldots$ repeats with period $\Delta \stackrel{\mathrm{def}}{=} J-I$. That is, for all $i \geq I$ and $k \geq 0$ it holds that $x_i = x_{i+k \cdot \Delta}$. Let $i$ be the smallest multiple of $\Delta$ that is also greater than or equal to $I$. We have $i < J$ since the sequence of $\Delta$ values $I, I+1, \ldots, I+(\Delta-1) = J-1$ contains a multiple of $\Delta$. Since $i \geq I$ and ${2}i-i=i$ is a multiple of $\Delta$, it follows that $x_i = x_{2i}$.

**证明** 序列 $x_I, x_{I+1}, \ldots$ 以周期 $\Delta \stackrel{\mathrm{def}}{=} J-I$ 重复。即对所有 $i \geq I$ 和 $k \geq 0$ 有 $x_i = x_{i+k \cdot \Delta}$。设 $i$ 是大于等于 $I$ 的最小的 $\Delta$ 的倍数。我们有 $i < J$，因为由 $\Delta$ 个值 $I, I+1, \ldots, I+(\Delta-1) = J-1$ 组成的序列包含 $\Delta$ 的一个倍数。由于 $i \geq I$ 且 ${2}i-i=i$ 是 $\Delta$ 的倍数，可得 $x_i = x_{2i}$。

Thus, if there is a repeated value in the sequence $x_1, \ldots, x_q$, there is some $i < q$ for which $x_i = x_{2i}$. But then in iteration $i$ of Algorithm 6.9, we have $x = x^{\prime}$ and the algorithm breaks out of the first loop. At that point in the algorithm, we know that $x_i = x_{2i}$. The algorithm then sets $x^{\prime} := x = x_i$ and $x := x_0$, and proceeds to find the smallest $j > 0$ for which $x_j = x_{j+i}$. (Note $x_0 \neq x_i$ because $|x_0| = \ell + 1$.) It outputs $x_{j-1}, x_{j+i-1}$ as a collision.

因此，如果序列 $x_1, \ldots, x_q$ 中存在重复值，则存在某个 $i < q$ 使得 $x_i = x_{2i}$。那么在算法 6.9 的第 $i$ 次迭代中，我们有 $x = x^{\prime}$，算法跳出第一个循环。此时我们知道 $x_i = x_{2i}$。算法随后置 $x^{\prime} := x = x_i$ 且 $x := x_0$，并着手找到使 $x_j = x_{j+i}$ 成立的最小 $j > 0$。（注意 $x_0 \neq x_i$，因为 $|x_0| = \ell + 1$。）它输出 $x_{j-1}, x_{j+i-1}$ 作为碰撞。

Finding meaningful collisions. The algorithm just described may not seem amenable to finding meaningful collisions since it has no control over the $\{x_i\}$ values used. Nevertheless, we show that finding meaningful collisions is still possible. The trick is to find a collision in the right function!

寻找有意义的碰撞。刚才描述的算法似乎不利于寻找有意义的碰撞，因为它无法控制所用的 $\{x_i\}$ 值。尽管如此，我们表明寻找有意义的碰撞仍然是可能的。诀窍在于在正确的函数中找到碰撞！

Assume, as before, that Alice wants to find a collision between messages of two different “types,” e.g., a letter explaining why she was fired and a flattering letter of recommendation. Alice writes each message so there are $\ell-1$ interchangeable words in each; i.e., there are ${2}^{\ell-1}$ messages of each type. Define the function $g: \{0,1\}^{\ell} \to \{0,1\}^{*}$ such that the first bit of the input selects between messages of type 0 or type 1, and the remaining bits select between options for the interchangeable words in messages of the appropriate type. For example, if $\ell = 4$ we could consider the sentences:

与之前一样，假设 Alice 想要在两种不同“类型”的消息之间找到碰撞，例如一封解释她为何被解雇的信和一封赞誉的推荐信。Alice 这样写每条消息，使得每条消息中有 $\ell-1$ 个可互换的词；即每种类型有 ${2}^{\ell-1}$ 条消息。定义函数 $g: \{0,1\}^{\ell} \to \{0,1\}^{*}$，使得输入的第一比特在类型 0 或类型 1 的消息之间选择，剩余比特在相应类型消息的可互换词的选项之间选择。例如，如果 $\ell = 4$，我们可以考虑以下句子：

type 0: Alice is a good/great and honest/trustworthy worker/employee.

type 1: Alice is a bad/lousy and annoying/irritating worker/employee.

类型 0：Alice 是一个 好/很棒的 且 诚实/值得信赖的 员工/雇员。

类型 1：Alice 是一个 差/糟糕的 且 烦人/恼人的 员工/雇员。

The function g is then defined on 4-bit inputs, where the first bit determines the sentence type and the final three bits determine the words in the sentence. That is:

函数 $g$ 定义在 4 比特输入上，其中第一比特确定句子类型，最后三个比特确定句子中的词。即：

$$
g(0000)=Alice\;is\;a\;good\;and\;honest\;worker.
$$

$$
g(1101)=Alice\;is\;a\;lousy\;and\;annoying\;employee.
$$

Finally, define $f : \{0,1\}^{\ell} \to \{0,1\}^{\ell}$ by $f(x) \overset{\mathrm{def}}{=} H(g(x))$. Alice can find a collision in $f$ using a variant of the small-space birthday attack shown earlier. Note that any collision $x, x^{\prime}$ in $f$ yields two messages $g(x), g(x^{\prime})$ that collide under $H$. If $x, x^{\prime}$ is a random collision then we expect that with probability ${1}/{2}$ the colliding messages $g(x), g(x^{\prime})$ will be of different types (since $x$ and $x^{\prime}$ will differ in their first bit with probability ${1}/{2}$). If the colliding messages are not of different types, the process can be repeated.

最后，由 $f(x) \overset{\mathrm{def}}{=} H(g(x))$ 定义 $f : \{0,1\}^{\ell} \to \{0,1\}^{\ell}$。Alice 可以使用前面所示小空间生日攻击的一个变体在 $f$ 中找到碰撞。注意 $f$ 中的任何碰撞 $x, x^{\prime}$ 都给出两条在 $H$ 下碰撞的消息 $g(x), g(x^{\prime})$。如果 $x, x^{\prime}$ 是一个随机碰撞，我们预期碰撞消息 $g(x), g(x^{\prime})$ 以 ${1}/{2}$ 的概率属于不同类型（因为 $x$ 和 $x^{\prime}$ 将以 ${1}/{2}$ 的概率在第一比特上不同）。如果碰撞的消息不属于不同类型，则可以重复该过程。

### 6.4.3 \*Time/Space Tradeoffs for Inverting Hash Functions　6.4.3 \*反转哈希函数的时间/空间折中

In this section we consider the question of preimage resistance, i.e., we are interested in algorithms for the problem of function inversion. Here, we have a hash function $H: \{0,1\}^* \to \{0,1\}^{\ell}$; an adversary is given $y = H(x)$ and its goal is to find any $x^{\prime}$ such that $H(x^{\prime}) = y$. (We call such an $x^{\prime}$ a preimage of $y$.) We begin by assuming that $x \in \{0,1\}^{\ell}$ for simplicity (and so view the domain of $H$ as $\{0,1\}^{\ell}$), and consider the more general case at the end.

在本节中，我们考虑原像抗性的问题，即我们对函数求逆问题的算法感兴趣。这里，我们有一个哈希函数 $H: \{0,1\}^* \to \{0,1\}^{\ell}$；敌手获得 $y = H(x)$，其目标是找到任意 $x^{\prime}$ 使得 $H(x^{\prime}) = y$。（我们称这样的 $x^{\prime}$ 为 $y$ 的一个原像。）为简单起见，我们首先假设 $x \in \{0,1\}^{\ell}$（因而把 $H$ 的定义域视为 $\{0,1\}^{\ell}$），并在末尾考虑更一般的情形。

Finding a preimage of $y = H(x)$ can be done in time $\Theta(2^{\ell})$ via exhaustive search over the domain of $H$, and this is optimal when $H$ is modeled as a random function. However, it ignores the possibility of preprocessing. That is, it may be possible for an algorithm to perform a significant amount of work in an “off-line” preprocessing phase before $y$ is known, and then to find a preimage $x^{\prime}$ in an “on-line” phase after being given $y$, using significantly less than $\Theta(2^{\ell})$ computation. This can be a worthwhile tradeoff if work can be invested in advance, or if the algorithm will be used to find preimages of multiple values (since the same preprocessing can be used for all of them).

通过对 $H$ 的定义域进行穷举搜索，可以在 $\Theta(2^{\ell})$ 时间内找到 $y = H(x)$ 的一个原像，并且当 $H$ 被建模为随机函数时这是最优的。然而，它忽略了预处理的可能性。即，一个算法可能在 $y$ 已知之前的“离线”预处理阶段执行大量工作，然后在得到 $y$ 之后的“在线”阶段找到原像 $x^{\prime}$，所用的计算量显著少于 $\Theta(2^{\ell})$。如果工作可以提前投入，或者该算法将被用于寻找多个值的原像（因为相同的预处理可用于所有这些值），那么这样的折中可能是值得的。

In fact, it is trivial to use preprocessing to improve the on-line time of function inversion. All we need to do is evaluate $H$ on every point in $\{0,1\}^{\ell}$ during the preprocessing phase, and store all the pairs $\{(x,H(x))\}$ in a table, sorted by their second entry. Upon receiving a point $y$, a preimage of $y$ can be found easily by using binary search to find a pair in the table with second entry $y$. The drawback here is that we need to allocate memory for storing ${2}^{\ell}$ pairs, which can be prohibitive—if not impossible—for large $\ell$.

事实上，使用预处理来改善函数求逆的在线时间是平凡的。我们要做的只是在预处理阶段对 $\{0,1\}^{\ell}$ 中的每个点求值 $H$，并将所有对 $\{(x,H(x))\}$ 存储在一张按第二项排序的表中。收到点 $y$ 后，通过二分搜索在表中找到第二项为 $y$ 的一对，即可容易地找到 $y$ 的一个原像。其缺点是我们需要分配内存来存储 ${2}^{\ell}$ 对，这对于大的 $\ell$ 可能是令人望而却步的——甚至是不可能的。

Exhaustive search uses constant memory and $\Theta(2^\ell)$ on-line time, while the attack just described stores $\Theta(2^\ell)$ points in memory but enables inversion in essentially constant on-line time. We now show an approach that allows an attacker to trade off time and memory and interpolate between these extremes. Specifically, we show how to store $\mathcal{O}(2^{2\ell/3})$ values and find preimages in time $\mathcal{O}(2^{2\ell/3})$; other trade-offs are also possible.

穷举搜索使用常数内存和 $\Theta(2^\ell)$ 的在线时间，而刚才描述的攻击在内存中存储 $\Theta(2^\ell)$ 个点，但使得求逆基本上在常数在线时间内完成。我们现在给出一种允许攻击者折中时间和内存并在这些极端之间插值的方法。具体而言，我们展示如何存储 $\mathcal{O}(2^{2\ell/3})$ 个值并在 $\mathcal{O}(2^{2\ell/3})$ 时间内找到原像；其他折中方案也是可能的。

A warmup. We begin by considering the simple case where the function $H$ defines a cycle, meaning that $x, H(x), H(H(x)), \ldots$ covers all of $\{0,1\}^{\ell}$ for any starting point $x$. (Note that most functions do not define a cycle, but we assume this in order to demonstrate the idea in a very simple case.) For clarity, let $N = 2^{\ell}$ denote the size of the domain and range.

热身。我们首先考虑简单情形：函数 $H$ 定义一个圈，即对任意起始点 $x$，$x, H(x), H(H(x)), \ldots$ 覆盖全部 $\{0,1\}^{\ell}$。（注意大多数函数并不定义圈，但我们作此假设以便在非常简单的情形中演示这一思想。）为清楚起见，令 $N = 2^{\ell}$ 表示定义域和值域的大小。

In the preprocessing phase, the attacker simply exhausts the entire cycle, beginning at an arbitrary starting point $x_0$ and computing $x_1 := H(x_0)$, $x_2 := H(H(x_0))$, up to $x_N = H^{(N)}(x_0)$, where $H^{(i)}$ refers to i-fold evaluation of $H$. Let $x_i \overset{\mathrm{def}}{=} H^{(i)}(x_0)$. We imagine partitioning the cycle into $\sqrt{N}$ segments of length $\sqrt{N}$ each, and having the attacker store the points at the beginning and end of each such segment. That is, the attacker stores in a table pairs of the form $(x_{i \cdot \sqrt{N}}, x_{(i+1) \cdot \sqrt{N}})$, for $i = 0$ to $\sqrt{N} - 1$, sorted by the second component of each pair. The resulting table contains $\mathcal{O}(\sqrt{N})$ points.

在预处理阶段，攻击者只需穷尽整个圈，从任意起始点 $x_0$ 开始，计算 $x_1 := H(x_0)$、$x_2 := H(H(x_0))$，直到 $x_N = H^{(N)}(x_0)$，其中 $H^{(i)}$ 指 $H$ 的 $i$ 重求值。令 $x_i \overset{\mathrm{def}}{=} H^{(i)}(x_0)$。我们想象把圈划分为 $\sqrt{N}$ 个长度各为 $\sqrt{N}$ 的段，并让攻击者存储每个段的起点和终点。即，攻击者在表中存储形如 $(x_{i \cdot \sqrt{N}}, x_{(i+1) \cdot \sqrt{N}})$ 的对，其中 $i$ 从 ${0}$ 到 $\sqrt{N} - 1$，并按每对的第二分量排序。所得的表包含 $\mathcal{O}(\sqrt{N})$ 个点。

When the attacker is given a point y to invert in the on-line phase, it checks which of $y$, $H(y)$, $H^{(2)}(y)$, ..., corresponds to the endpoint of a segment. (Each check just involves a table lookup on the second component of the stored pairs.) Since $y$ lies in some segment, this is guaranteed to find an endpoint within $\sqrt{N}$ steps. Once an endpoint $x = x_{(i+1)\cdot\sqrt{N}}$ is identified, the attacker takes the starting point $x^{\prime} = x_{i\cdot\sqrt{N}}$ of the corresponding segment and computes $H(x^{\prime})$, $H^{(2)}(x^{\prime})$, ..., until $y$ is reached; this immediately gives the desired preimage. This takes at most $\sqrt{N}$ additional evaluations of $H$.

在线阶段中，当攻击者获得一个要反转的点 y 时，它检查 $y$、$H(y)$、$H^{(2)}(y)$、⋯⋯ 中哪一个对应于某段的终点。（每次检查只需对所存对的第二分量进行一次表查找。）由于 $y$ 位于某个段中，这保证在 $\sqrt{N}$ 步内找到一个终点。一旦识别出终点 $x = x_{(i+1)\cdot\sqrt{N}}$，攻击者取相应段的起点 $x^{\prime} = x_{i\cdot\sqrt{N}}$，并计算 $H(x^{\prime})$、$H^{(2)}(x^{\prime})$、⋯⋯，直到到达 $y$；这立即给出所需的原像。这最多需要 $\sqrt{N}$ 次额外的 $H$ 求值。

In summary, this attack stores $\mathcal{O}(\sqrt{N}) = \mathcal{O}(2^{\ell/2})$ points and finds preimages with probability 1 using $\mathcal{O}(\sqrt{N}) = \mathcal{O}(2^{\ell/2})$ on-line hash computations.

总之，该攻击存储 $\mathcal{O}(\sqrt{N}) = \mathcal{O}(2^{\ell/2})$ 个点，并使用 $\mathcal{O}(\sqrt{N}) = \mathcal{O}(2^{\ell/2})$ 次在线哈希计算以概率 1 找到原像。

Hellman’s time/space tradeoff. Martin Hellman introduced a more general time/space tradeoff applicable to an arbitrary function $H$ (though the analysis treats $H$ as a random function). Hellman’s attack still stores the starting point and endpoint of several segments, but in this case the segments are “independent” rather than being part of one large cycle. In more detail: let $s, t$ be parameters we will set later. The attacker first chooses $s$ uniform starting points $SP_1, \ldots, SP_s \in \{0, 1\}^\ell$. For each such point $SP_i$, it computes a corresponding endpoint $EP_i := H^{(t)}(SP_i)$ using $t$-fold application of $H$. (See Figure 6.3.) The attacker then stores the values $\{(SP_i, EP_i)\}_{i=1}^{s}$ in a table, sorted by the second entry (i.e., the endpoint) of each pair.

Hellman 的时间/空间折中。Martin Hellman 引入了一种适用于任意函数 $H$ 的更一般的时间/空间折中（尽管分析时把 $H$ 视为随机函数）。Hellman 的攻击仍然存储若干段的起点和终点，但在此情形下这些段是“独立的”，而非一个大的圈的一部分。更详细地说：设 $s, t$ 为我们稍后将设定的参数。攻击者首先选择 $s$ 个均匀的起始点 $SP_1, \ldots, SP_s \in \{0, 1\}^\ell$。对每个这样的点 $SP_i$，它使用 $H$ 的 $t$ 重应用计算相应的终点 $EP_i := H^{(t)}(SP_i)$。（见图 6.3。）攻击者然后将值 $\{(SP_i, EP_i)\}_{i=1}^{s}$ 存储在一张按每对的第二项（即终点）排序的表中。

![Image](https://lsky.jerryxue.top/i/2026/08/22/6a88f9e7bcb54.jpg)

**FIGURE 6.3: Table generation. Only the $(SP_{i}, EP_{i})$ pairs are stored.**

**图 6.3：表的生成。只存储 $(SP_{i}, EP_{i})$ 对。**

Upon receiving a value $y$ to invert, the attack proceeds as in the simple case discussed earlier. Specifically, it checks if any of $y$, $H(y)$, ..., $H^{(t-1)}(y)$ is equal to the endpoint of some segment (stopping as soon as the first such match is found). It is possible that none of these values is equal to an endpoint (as we discuss below). However, if $H^{(j)}(y) = EP_i = H^{(t)}(SP_i)$ for some $i,j$, then the attacker computes $H^{(t-j-1)}(SP_i)$ and checks whether this is a preimage of $y$. The entire process requires at most $t$ evaluations of $H$.

收到要反转的值 $y$ 后，该攻击与前面讨论的简单情形一样进行。具体而言，它检查 $y$、$H(y)$、⋯⋯、$H^{(t-1)}(y)$ 中是否有等于某段终点的值（一旦找到第一个这样的匹配就停止）。这些值中可能没有一个等于终点（如下文所讨论）。然而，如果对某个 $i,j$ 有 $H^{(j)}(y) = EP_i = H^{(t)}(SP_i)$，则攻击者计算 $H^{(t-j-1)}(SP_i)$ 并检查它是否为 $y$ 的一个原像。整个过程最多需要 $t$ 次 $H$ 求值。

This seems to work, but there are several subtleties we have ignored. First, it may happen that none of $y$, $H(y)$, ..., $H^{(t-1)}(y)$ is the endpoint of a segment. This can happen if $y$ is not in the collection of at most $s \cdot t$ values (not counting the starting points) obtained during the initial process of generating the table. We can set $s \cdot t \geq N$ in an attempt to include every $\ell$-bit string in the table, but this does not solve the problem since there can be collisions in the table itself—in fact, for $s \cdot t \geq N^{1/2}$ our previous analysis of the birthday problem tells us that collisions are likely—which will reduce the number of distinct points in the collection of values. A second problem, which arises even if $y$ is in the table, is that even if we find a matching endpoint, and so $H^{(j)}(y) = EP_i = H^{(t)}(SP_i)$ for some $i,j$, this does not guarantee that $H^{(t-j-1)}(SP_i)$ is a preimage of $y$. The issue here is that the segment $y$, $H(y)$, ..., $H^{(t-1)}(y)$ might collide with the $i$th segment even though $y$ itself is not in that segment; see Figure 6.4. (Even if $y$ lies in some segment, the first matching endpoint may not be in that segment.) We call this a false positive. One might think this is unlikely to occur if $H$ is collision resistant; again, however, we are dealing with a situation where more than $\sqrt{N}$ points are involved and so collisions actually become likely.

这似乎可行，但我们忽略了若干微妙之处。首先，$y$、$H(y)$、⋯⋯、$H^{(t-1)}(y)$ 中可能没有一个是某段的终点。如果 $y$ 不在最初生成表的过程中获得的至多 $s \cdot t$ 个值（不含起始点）的集合中，就会发生这种情况。我们可以设定 $s \cdot t \geq N$ 以试图把每个 $\ell$ 比特串都包含在表中，但这并不能解决问题，因为表本身可能存在碰撞——事实上，当 $s \cdot t \geq N^{1/2}$ 时，我们先前对生日问题的分析告诉我们碰撞很可能发生——这将减少该值集合中不同点的数目。第二个问题（即使 $y$ 在表中也可能出现）是，即使我们找到一个匹配的终点，从而对某个 $i,j$ 有 $H^{(j)}(y) = EP_i = H^{(t)}(SP_i)$，这也不能保证 $H^{(t-j-1)}(SP_i)$ 是 $y$ 的原像。这里的问题在于，段 $y$、$H(y)$、⋯⋯、$H^{(t-1)}(y)$ 可能与第 $i$ 段碰撞，即便 $y$ 本身不在该段中；见图 6.4。（即使 $y$ 位于某段中，第一个匹配的终点也可能不在该段中。）我们称之为假阳性（false positive）。人们可能认为如果 $H$ 抗碰撞则这不太可能发生；然而同样地，我们所处理的情况涉及超过 $\sqrt{N}$ 个点，因此碰撞实际上很可能发生。

![Image](https://lsky.jerryxue.top/i/2026/08/22/6a88f9e874d5a.jpg)

**FIGURE 6.4: Colliding in the on-line phase.**

**图 6.4：在线阶段的碰撞。**

The problem of false positives can be addressed by modifying the algorithm so that it always computes the entire sequence $y$, $H(y)$, ..., $H^{(t-1)}(y)$, and checks whether $H^{(t-j-1)}(SP_i)$ is a preimage of $y$ for every $i,j$ such that $H^{(j)}(y) = EP_i$. This is guaranteed to find a preimage as long as $y$ is in the collection of values (not including the starting points) generated during preprocessing. A concern now is that the running time of the algorithm might increase, since each false positive incurs an additional $\mathcal{O}(t)$ hash evaluations. One can show that the expected number of false positives is $\mathcal{O}(st^2/N)$. (There are at most $t$ values in the sequence $y$, $H(y)$, ..., $H^{(t-1)}(y)$ and at most $st$ distinct points in the table. Treating $H$ as a random function, the probability that a given point in the sequence equals some point in the table is ${1}/N$.

假阳性问题可以通过修改算法来解决，使其总是计算整个序列 $y$、$H(y)$、⋯⋯、$H^{(t-1)}(y)$，并对满足 $H^{(j)}(y) = EP_i$ 的每个 $i,j$ 检查 $H^{(t-j-1)}(SP_i)$ 是否为 $y$ 的原像。只要 $y$ 在预处理期间生成的值集合（不含起始点）中，这就保证能找到一个原像。现在的一个担忧是算法的运行时间可能增加，因为每个假阳性都会带来额外的 $\mathcal{O}(t)$ 次哈希求值。可以证明假阳性的期望数目为 $\mathcal{O}(st^2/N)$。（序列 $y$、$H(y)$、⋯⋯、$H^{(t-1)}(y)$ 中至多有 $t$ 个值，而表中至多有 $st$ 个不同的点。把 $H$ 视为随机函数，序列中某个给定点等于表中某个点的概率为 ${1}/N$。

The expected number of false positives is thus at most $t \cdot st \cdot 1/N = st^2/N$.) So, as long as $st^2 \approx N$, which we will ensure for other reasons below, the expected number of false positives is constant and dealing with false positives is expected to require only $\mathcal{O}(t)$ additional hash computations in total.

因此假阳性的期望数目至多为 $t \cdot st \cdot 1/N = st^2/N$。）所以，只要 $st^2 \approx N$（我们将在下文出于其他原因确保这一点），假阳性的期望数目就是常数，处理假阳性预计总共只需 $\mathcal{O}(t)$ 次额外的哈希计算。

Given the above modification, the probability of inverting $y = H(x)$ is at least the probability that x is in the collection of points (not including the endpoints) generated during preprocessing. We now lower bound this probability, taken over the randomness of the preprocessing stage as well as uniform choice of x, treating H as a random function in the analysis. We first compute the expected number of distinct points in the table. Consider what happens when the ith row of the table is generated. The starting point $SP_i$ is uniform and there are at most $(i-1) \cdot t$ distinct points (not including the endpoints) in the table already, so the probability that $SP_i$ is “new” (i.e., not equal to any previous value) is at least ${1} - (i-1) \cdot t/N$. What is the probability that $H(SP_i)$ is new? If $SP_i$ is not new, then almost surely neither is $H(SP_i)$. On the other hand, if $SP_i$ is new then $H(SP_i)$ is uniform (because we treat H as a random function) and so is new with probability at least ${1} - ((i-1) \cdot t + 1)/N$. (We now have the additional point $SP_i$.) Thus, the probability that $H(SP_i)$ is new is at least

经过上述修改后，反转 $y = H(x)$ 的概率至少是 x 在预处理期间生成的点集合（不含终点）中的概率。我们现在在预处理阶段的随机性以及 x 的均匀选择上对该概率给出下界，分析中把 H 视为随机函数。我们首先计算表中不同点的期望数目。考虑生成表的第 i 行时的情况。起始点 $SP_i$ 是均匀的，而表中已有至多 $(i-1) \cdot t$ 个不同的点（不含终点），所以 $SP_i$ 是“新”的（即不等于任何先前的值）概率至少为 ${1} - (i-1) \cdot t/N$。$H(SP_i)$ 是新点的概率是多少？如果 $SP_i$ 不是新的，那么几乎可以肯定 $H(SP_i)$ 也不是。另一方面，如果 $SP_i$ 是新的，那么 $H(SP_i)$ 是均匀的（因为我们把 H 视为随机函数），因而是新点的概率至少为 ${1} - ((i-1) \cdot t + 1)/N$。（我们现在有了额外的点 $SP_i$。）因此 $H(SP_i)$ 是新点的概率至少为

$$
\begin{aligned}\Pr\left[SP_{i}\text{is new}\right]&\cdot\Pr\left[H(SP_{i})\text{is new}\mid SP_{i}\text{is new}\right]\\&\geq\left(1-\frac{(i-1)\cdot t}{N}\right)\cdot\left(1-\frac{(i-1)\cdot t+1}{N}\right)\\&>\left(1-\frac{(i-1)\cdot t+1}{N}\right)^{2}.\end{aligned}
$$

Continuing in this way, the probability that $H^{(t-1)}(SP_{i})$ is new is at least

依此类推，$H^{(t-1)}(SP_{i})$ 是新点的概率至少为

$$
\left(1-\frac{i\cdot t}{N}\right)^{t}=\left[\left(1-\frac{i\cdot t}{N}\right)^{\frac{N}{i\cdot t}}\right]^{\frac{i\cdot t^{2}}{N}}\approx e^{-i t^{2}/N}.
$$

The thing to notice here is that when $it^2 \leq N/2$, this probability is at least ${1}/{2}$; on the other hand, once $it^2 > N$ the probability is relatively small. Considering the last row, when $i = s$, this means that we will not gain much additional coverage if $st^2 > N$. A good setting of the parameters is thus $st^2 = N/2$. Assuming this, the expected number of distinct points in the table is

这里需要注意的是，当 $it^2 \leq N/2$ 时，该概率至少为 ${1}/{2}$；另一方面，一旦 $it^2 > N$，该概率就相对较小。考虑最后一行即 $i = s$ 时，这意味着如果 $st^2 > N$，我们将不会获得太多额外的覆盖。因此参数的一个好的设置是 $st^2 = N/2$。在此假设下，表中不同点的期望数目为

$$
\sum_{i=1}^{s}\sum_{j=0}^{t-1}\Pr\left[H^{(j)}(SP_{i})is new\right]\geq\sum_{i=1}^{s}\sum_{j=0}^{t-1}\frac{1}{2}=\frac{st}{2}.
$$

The probability that x is “covered” is then at least $\frac{st}{2N} = \frac{1}{4t}$.

那么 x 被“覆盖”的概率至少为 $\frac{st}{2N} = \frac{1}{4t}$。

This gives a weak time/space tradeoff, in which we can use more space s (and consequently less time t) while increasing the probability of inverting y. But we can do even better by generating $T = 4t$ “independent” tables. (This increases both the space and time by at most a factor of $T$.) As long as we can treat the probabilities of $x$ being in each of these tables as independent, the probability that at least one of these tables contains $x$ is

这给出一个弱的时间/空间折中，其中我们可以使用更多的空间 s（相应地更少的时间 t），同时增加反转 y 的概率。但我们还可以通过生成 $T = 4t$ 张“独立的”表来做得更好。（这使空间和时间都至多增大为原来的 $T$ 倍。）只要我们能将 x 在每张表中的概率视为独立的，至少一张表包含 x 的概率为

$$
{1}-\Pr[\mathrm{no~table~contains~}x]=1-\left(1-\frac{1}{4t}\right)^{4t}\approx1-e^{-1}=0.63.
$$

The only remaining question is how to generate an independent table. (Note that generating a table exactly as before is the same as adding $s$ additional rows to our original table, which we have already seen does not help.) We can do this for the $i$th such table by applying some function $f_i$ after every evaluation of $H$, where $f_1, \ldots, f_T$ are all distinct. (A good choice might be to set $f_i(x) = x \oplus c_i$ for some fixed constant $c_i$ that is different for each table.) Let $H_i \stackrel{\mathrm{def}}{=} f_i \circ H$, i.e., $H_i(x) = f_i(H(x))$. Then for the $i$th table we again choose $s$ random starting points, but for each such point we now compute $H_i(SP), H_i^{(2)}(SP)$, and so on. Upon receiving a value $y = H(x)$ to invert, the attacker first computes $y^{\prime} = f_i(y)$ and then checks which of $y^{\prime}, H_i(y^{\prime})$, ..., $H_i^{(t-1)}(y^{\prime})$ corresponds to an endpoint in the $i$th table; this is repeated for $i = 1, \ldots, T$. (We omit further details.) While it is difficult to argue independence formally, this approach leads to good results in practice.

唯一剩下的问题是如何生成独立的表。（注意，完全像之前那样生成一张表，等同于向我们原来的表添加 $s$ 行，而我们已经看到这无济于事。）对于第 $i$ 张这样的表，我们可以通过在每次求值 $H$ 之后应用某个函数 $f_i$ 来实现，其中 $f_1, \ldots, f_T$ 互不相同。（一个好的选择可能是设 $f_i(x) = x \oplus c_i$，其中 $c_i$ 是某个固定的、每张表各不相同的常数。）令 $H_i \stackrel{\mathrm{def}}{=} f_i \circ H$，即 $H_i(x) = f_i(H(x))$。那么对第 $i$ 张表，我们再次选择 $s$ 个随机起始点，但对每个这样的点我们现在计算 $H_i(SP), H_i^{(2)}(SP)$ 等等。收到要反转的值 $y = H(x)$ 时，攻击者首先计算 $y^{\prime} = f_i(y)$，然后检查 $y^{\prime}, H_i(y^{\prime})$, ..., $H_i^{(t-1)}(y^{\prime})$ 中哪一个对应第 $i$ 张表中的一个终点；这对 $i = 1, \ldots, T$ 重复。（我们省略进一步的细节。）虽然难以形式化地论证独立性，但这种方法在实践中效果良好。

Choosing parameters. Summarizing the above, we see that as long as $st^2 = N/2$ we have an algorithm that stores $\mathcal{O}(s\cdot T) = \mathcal{O}(s\cdot t) = \mathcal{O}(N/t)$ points during a preprocessing phase, and can then invert $y$ with constant probability in time $\mathcal{O}(t\cdot T) = \mathcal{O}(t^2)$. One setting of the parameters is $t = N^{1/3} = 2^{\ell/3}$, in which case we have an algorithm storing $\mathcal{O}(2^{2\ell/3})$ points that finds a preimage with constant probability using $\mathcal{O}(2^{2\ell/3})$ hash computations. If $\ell = 80$, this is feasible in practice.

选择参数。综上所述，我们看到只要 $st^2 = N/2$，就有一个在预处理阶段存储 $\mathcal{O}(s\cdot T) = \mathcal{O}(s\cdot t) = \mathcal{O}(N/t)$ 个点的算法，然后可以以常数概率在 $\mathcal{O}(t\cdot T) = \mathcal{O}(t^2)$ 时间内反转 $y$。参数的一种设置是 $t = N^{1/3} = 2^{\ell/3}$，在此情形下我们有一个存储 $\mathcal{O}(2^{2\ell/3})$ 个点、使用 $\mathcal{O}(2^{2\ell/3})$ 次哈希计算以常数概率找到原像的算法。如果 $\ell = 80$，这在实践中是可行的。

Handling different domain and range. Consider the more general case where the original preimage $x$ is chosen from a domain $D$ that is different from the range $\{0,1\}^{\ell}$. This situation is quite common. One example is in the context of password cracking (see Section 6.6.3), where an attacker is given $H(pw)$ for a password $pw$ composed of ASCII characters. (Not every bit-string corresponds to ASCII.) While it may be possible to artificially expand the domain, this will not be useful in general: In typical applications we would like to recover a preimage in $D$, but if the domain is artificially expanded then the algorithm above is likely to find a preimage that lies outside of $D$.

处理不同的定义域和值域。考虑更一般的情形：原始原像 $x$ 选自一个与值域 $\{0,1\}^{\ell}$ 不同的定义域 $D$。这种情况相当常见。一个例子是口令破解的语境（见 6.6.3 节），其中攻击者获得由 ASCII 字符组成的口令 $pw$ 的 $H(pw)$。（并非每个比特串都对应 ASCII。）虽然可能人为地扩展定义域，但这在一般情况下并无用处：在典型应用中我们希望恢复 $D$ 中的原像，但如果定义域被人为扩展，则上述算法很可能找到一个位于 $D$ 之外的原像。

We can address this by applying a function $f_i$, as before, between each evaluation of $H$, though now we choose $f_i$ mapping $\{0,1\}^\ell$ to $D$. This ensures that, when constructing the table, the values $f_i(H(SP)),(f_i\circ H)^{(2)}(SP),\ldots$ all lie in the desired domain $D$.

我们可以通过在每次求值 $H$ 之间应用一个函数 $f_i$（如前所述）来解决这个问题，不过现在我们选择将 $\{0,1\}^\ell$ 映射到 $D$ 的 $f_i$。这确保了在构造表时，值 $f_i(H(SP)),(f_i\circ H)^{(2)}(SP),\ldots$ 全部位于所需的定义域 $D$ 中。

Application to key-recovery attacks. Time/space tradeoffs can lead to attacks on cryptographic primitives other than hash functions. A canonical example—in fact, the application originally considered by Hellman—is a key-recovery attack on an arbitrary block cipher $F$. Define $H(k) \overset{\mathrm{def}}{=} F_k(m)$ where $m$ is some arbitrary input that is used for building the table. If an attacker can subsequently obtain $F_k(m)$ for an unknown key $k$—either via a chosen-plaintext attack or by choosing $m$ such that $F_k(m)$ is likely to be obtained in a known-plaintext attack—then by inverting $H$ the attacker learns (a candidate value for) $k$. Note that it is possible for the key length of $F$ to differ from its block length, but in this case we can use the technique just described for handling $H$ with different domain and range.

对密钥恢复攻击的应用。时间/空间折中可导致针对除哈希函数以外的密码学原语的攻击。一个典型的例子——事实上也是 Hellman 最初考虑的应用——是对任意分组密码 $F$ 的密钥恢复攻击。定义 $H(k) \overset{\mathrm{def}}{=} F_k(m)$，其中 $m$ 是某个用于构建表的任意输入。如果攻击者随后能获得未知密钥 $k$ 下的 $F_k(m)$——要么通过选择明文攻击，要么通过选择 $m$ 使得 $F_k(m)$ 很可能在已知明文攻击中被获得——那么通过反转 $H$，攻击者就学到了 $k$（的一个候选值）。注意 $F$ 的密钥长度可能与其分组长度不同，但在这种情况下我们可以使用刚才描述的、用于处理具有不同定义域和值域的 $H$ 的技术。
