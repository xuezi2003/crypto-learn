## 4.4 CBC-MAC　4.4 CBC-MAC

Theorems 4.6 and 4.8 show that it is possible to construct a secure message authentication code for arbitrary-length messages from a pseudorandom function with block length n. This demonstrates, in principle, that secure MACs can be constructed from block ciphers. Unfortunately, the resulting construction is extremely inefficient: to compute a tag on a message of length $dn$, the block cipher is evaluated 4d times, and the tag is more than 4dn bits long. Fortunately, far more efficient constructions are available. We begin by exploring one such construction that relies solely on block ciphers.

定理 4.6 和 4.8 表明，可以从分组长度为 n 的伪随机函数构造出适用于任意长度消息的安全消息认证码。这原则上证明了安全的 MAC 可以从分组密码构造出来。不幸的是，由此得到的构造效率极低：对于长度为 $dn$ 的消息，需要计算 4d 次分组密码，且标签长度超过 4dn 比特。幸运的是，我们有更高效的构造。我们首先探讨一种仅依赖分组密码的高效构造。

### 4.4.1 The Basic Construction　4.4.1 基本构造

CBC-MAC was one of the first message authentication codes to be standardized. A basic version of CBC-MAC, secure when authenticating messages of any fixed length, is given as Construction 4.9. (See also Figure 4.1.) We caution that this basic scheme is not secure in the general case when messages of different lengths may be authenticated; see further discussion below.

CBC-MAC 是最早被标准化的消息认证码之一。构造 4.9 给出了 CBC-MAC 的一个基本版本，该版本在认证任意固定长度的消息时是安全的。（另见图 4.1。）我们提醒，当需要认证不同长度的消息时，该基本方案在一般情况下是不安全的；详见后文讨论。

THEOREM 4.10 Let $\ell$ be a polynomial. If $F$ is a pseudorandom function, then Construction 4.9 is a secure MAC for messages of length $\ell(n) \cdot n$.

定理 4.10 设 $\ell$ 是一个多项式。如果 $F$ 是一个伪随机函数，那么构造 4.9 对于长度为 $\ell(n) \cdot n$ 的消息是一个安全的 MAC。

> **CONSTRUCTION 4.9**　**构造 4.9**
>
> Let $F$ be a pseudorandom function, and fix a length function $\ell(n) > 0$. The basic CBC-MAC construction is as follows:
> - Mac: on input a key $k \in \{0,1\}^n$ and a message $m$ of length $\ell(n) \cdot n$, do the following (set $\ell = \ell(n)$ in what follows):
> 1. Parse $m$ as $m = m_1, \ldots, m_\ell$ where each $m_i$ is of length $n$.
> 2. Set $t_0 := 0^n$. Then, for $i = 1$ to $\ell$, set $t_i := F_k(t_{i-1} \oplus m_i)$.
> Output $t_\ell$ as the tag.
> - Vrfy: on input a key $k \in \{0,1\}^n$, a message $m$, and a tag $t$, do: If $m$ is not of length $\ell(n) \cdot n$ then output 0. Otherwise, output 1 if and only if $t \overset{?}{=} \mathsf{Mac}_k(m)$.
>
> **Basic CBC-MAC (for fixed-length messages).**
>
> 设 $F$ 是一个伪随机函数，并固定一个长度函数 $\ell(n) > 0$。基本 CBC-MAC 构造如下：
> - Mac：输入密钥 $k \in \{0,1\}^n$ 和长度为 $\ell(n) \cdot n$ 的消息 $m$，执行以下步骤（下文中设 $\ell = \ell(n)$）：
> 1. 将 $m$ 解析为 $m = m_1, \ldots, m_\ell$，其中每个 $m_i$ 长度为 $n$。
> 2. 设 $t_0 := 0^n$。然后对 $i = 1$ 到 $\ell$，计算 $t_i := F_k(t_{i-1} \oplus m_i)$。
> 输出 $t_\ell$ 作为标签。
> - Vrfy：输入密钥 $k \in \{0,1\}^n$、消息 $m$ 和标签 $t$：如果 $m$ 的长度不是 $\ell(n) \cdot n$，则输出 0。否则，当且仅当 $t \overset{?}{=} \mathsf{Mac}_k(m)$ 时输出 1。
>
> **基本 CBC-MAC（用于固定长度消息）。**

The proof of Theorem 4.10 is fairly complex. In the following section we will prove a more general result from which the above theorem follows.

定理 4.10 的证明相当复杂。在下一节中，我们将证明一个更一般的结论，上述定理将是该结论的一个推论。

Although Construction 4.9 can be extended in the obvious way to handle messages of different lengths, the construction is only secure when the length of the messages being authenticated is fixed and agreed upon in advance by the sender and receiver. (See Exercise 4.13.) The advantage of this construction over Construction 4.5, which also gives a fixed-length MAC, is that basic CBC-MAC can authenticate longer messages. Compared to Construction 4.7, basic CBC-MAC is much more efficient, requiring only $d$ block-cipher evaluations for a message of length $dn$, and with a tag of length $n$.

虽然可以按显而易见的方式扩展构造 4.9 来处理不同长度的消息，但它仅在所认证消息的长度固定且由发送方和接收方预先约定时才是安全的。（见习题 4.13。）与同样提供定长 MAC 的构造 4.5 相比，该构造的优势在于基本 CBC-MAC 能够认证更长的消息。与构造 4.7 相比，基本 CBC-MAC 高效得多，对于长度为 $dn$ 的消息仅需 $d$ 次分组密码计算，且标签长度为 $n$。

CBC-MAC vs. CBC-mode encryption. Basic CBC-MAC is similar to the CBC mode of operation. There are, however, some important differences:

CBC-MAC 与 CBC 模式加密。基本 CBC-MAC 与 CBC 工作模式类似。然而，存在一些重要区别：

1. CBC-mode encryption uses a random IV and this is crucial for security. In contrast, CBC-MAC uses no IV (alternately, it can be viewed as using the fixed value $IV = 0^{n}$) and this is also crucial for security. Specifically, CBC-MAC using a random IV is not secure.

   CBC 模式加密使用随机 IV，这对安全性至关重要。相比之下，CBC-MAC 不使用 IV（或者，可以视为使用固定值 $IV = 0^{n}$），这对安全性也至关重要。特别地，使用随机 IV 的 CBC-MAC 是不安全的。

2. In CBC-mode encryption all intermediate values $t_{i}$ (called $c_{i}$ in the case of CBC-mode encryption) are output by the encryption algorithm as part of the ciphertext, whereas in CBC-MAC only the final block is output as the tag. If CBC-MAC is modified to output all the $\{t_{i}\}$ obtained during the course of the computation then it is no longer secure.

   在 CBC 模式加密中，所有中间值 $t_{i}$（在 CBC 模式加密中称为 $c_{i}$）都由加密算法作为密文的一部分输出，而在 CBC-MAC 中，只有最后一个块作为标签输出。如果修改 CBC-MAC 使其输出计算过程中获得的所有 $\{t_{i}\}$，则它不再安全。

![Image](https://lsky.jerryxue.top/i/2026/08/22/6a88f9e4e1893.jpg)

**FIGURE 4.1: Basic CBC-MAC (for fixed-length messages).**

**图 4.1：基本 CBC-MAC（用于固定长度消息）。**

In Exercise 4.14 you are asked to verify that the modifications of CBC-MAC discussed above are insecure. These examples illustrate the fact that harmless-looking modifications to cryptographic constructions can render them insecure. One should always implement a cryptographic construction exactly as specified and not introduce any variations (unless the variations themselves can be proven secure). Furthermore, it is essential to understand the details of an implementation being used. In many cases cryptographic libraries provide the programmer with a "CBC function," but do not distinguish between the use of this function for encryption or message authentication.

在习题 4.14 中，要求你验证上述对 CBC-MAC 的修改是不安全的。这些例子说明，对密码学构造看似无害的修改可能使其变得不安全。人们应该严格按照规范实现密码学构造，而不引入任何变体（除非这些变体本身可以被证明是安全的）。此外，理解所用实现的细节至关重要。在许多情况下，密码学库为程序员提供了“CBC 函数”，但并不区分该函数是用于加密还是消息认证。

Secure CBC-MAC for arbitrary-length messages. We briefly describe two ways Construction 4.9 can be modified, in a provably secure manner, to handle arbitrary-length messages. (Here for simplicity we assume that all messages being authenticated have length a multiple of n, and that Vrfy rejects any message whose length is not a multiple of n. In the following section we treat the more general case where messages can have arbitrary length.)

用于任意长度消息的安全 CBC-MAC。我们简要描述两种修改构造 4.9 的方法，使其能够以可证明安全的方式处理任意长度的消息。（为简单起见，这里我们假设所有被认证的消息长度均为 n 的倍数，且 Vrfy 拒绝任何长度不是 n 的倍数的消息。在下一节中，我们将处理消息可以有任意长度的更一般情况。）

1. Prepend the message $m$ with its length $|m|$ (encoded as an $n$-bit string), and then compute basic CBC-MAC on the result; see Figure 4.2. Security of this variant follows from the results proved in the next section.

   在消息 $m$ 前面加上其长度 $|m|$（编码为 $n$ 比特串），然后对结果计算基本 CBC-MAC；见图 4.2。该变体的安全性可由下一节证明的结果推出。

Note that appending $|m|$ to the end of the message and then computing basic CBC-MAC is not secure.

注意，将 $|m|$ 附加到消息末尾然后计算基本 CBC-MAC 是不安全的。

![Image](https://lsky.jerryxue.top/i/2026/08/22/6a88f9e59c2b9.jpg)

**FIGURE 4.2: A version of CBC-MAC secure for authenticating arbitrary-length messages.**

**图 4.2：一种安全认证任意长度消息的 CBC-MAC 版本。**

2. Change the scheme so that key generation chooses two independent, uniform keys $k_1 \in \{0,1\}^n$ and $k_2 \in \{0,1\}^n$. Then to authenticate a message $m$, first compute the basic CBC-MAC of $m$ using $k_1$ and let $t$ be the result; output the tag $\hat{t} := F_{k_2}(t)$.

   修改方案，使密钥生成选择两个独立、均匀的密钥 $k_1 \in \{0,1\}^n$ 和 $k_2 \in \{0,1\}^n$。然后，认证消息 $m$ 时，首先使用 $k_1$ 计算 $m$ 的基本 CBC-MAC，令 $t$ 为结果；输出标签 $\hat{t} := F_{k_2}(t)$。

The second option has the advantage of not needing to know the message length in advance (i.e., when beginning to compute the tag). However, it has the drawback of using two keys for $F$. Note that, at the expense of two additional applications of $F$, it is possible to store a single key $k$ and then derive the keys $k_{1} := F_{k}(1)$ and $k_{2} := F_{k}(2)$ at the beginning of the computation. Despite this, in practice, the operation of initializing a block cipher with a new key is considered relatively expensive, and so this option is not always desirable.

第二种选项的优点是不需要预先知道消息长度（即在开始计算标签时）。然而，它的缺点是需要为 $F$ 使用两个密钥。注意，以额外应用两次 $F$ 为代价，可以只存储一个密钥 $k$，然后在计算开始时派生密钥 $k_{1} := F_{k}(1)$ 和 $k_{2} := F_{k}(2)$。尽管如此，在实践中，用新密钥初始化分组密码的操作被认为是相对昂贵的，因此该选项并非总是理想的。

### 4.4.2 \*Proof of Security　4.4.2 \*安全性证明

In this section we prove security of different variants of CBC-MAC. We begin by summarizing the results, and then give the details of the proof. The proof in this section is quite involved, and is intended for advanced readers.

在本节中，我们证明 CBC-MAC 不同变体的安全性。我们首先总结结果，然后给出证明的细节。本节中的证明相当复杂，面向高级读者。

Throughout this section, fix a keyed function $F$ that, for security parameter $n$, maps $n$-bit keys and $n$-bit inputs to $n$-bit outputs. We define a keyed function CBC that, for security parameter $n$, maps $n$-bit keys and inputs in $\left(\{0,1\}^{n}\right)^{+}$ (i.e., nonempty strings whose length is a multiple of $n$) to $n$-bit outputs. This function is defined as

在本节中，固定一个带密钥的函数 $F$，对于安全参数 $n$，它将 $n$ 比特密钥和 $n$ 比特输入映射到 $n$ 比特输出。我们定义一个带密钥的函数 CBC，对于安全参数 $n$，它将 $n$ 比特密钥和 $\left(\{0,1\}^{n}\right)^{+}$ 中的输入（即长度是 $n$ 的倍数的非空串）映射到 $n$ 比特输出。该函数定义为

$$\mathsf{CBC}_{k}(x_{1},\ldots,x_{\ell})\stackrel{\mathrm{def}}{=}F_{k}\left(F_{k}\left(\cdots F_{k}\left(F_{k}(x_{1})\oplus x_{2}\right)\oplus\cdots\right)\oplus x_{\ell}\right),$$

where $|x_1| = \cdots = |x_\ell| = n$. (We leave $\mathsf{CBC}_k$ undefined on the empty string.) Note that CBC is computed in the same way as basic CBC-MAC, although here we explicitly allow inputs of different lengths.

其中 $|x_1| = \cdots = |x_\ell| = n$。（我们对 $\mathsf{CBC}_k$ 在空串上不予定义。）注意，CBC 的计算方式与基本 CBC-MAC 相同，尽管这里我们明确允许不同长度的输入。

A set of strings $P \subset (\{0,1\}^n)^*$ is prefix-free if it does not contain the empty string, and no string $X \in P$ is a prefix of any other string $X^{\prime} \in P$. We show:

一组串 $P \subset (\{0,1\}^n)^*$ 称为**无前缀的**（prefix-free），如果它不包含空串，并且没有串 $X \in P$ 是任何其他串 $X^{\prime} \in P$ 的前缀。我们将证明：

THEOREM 4.11 If F is a pseudorandom function, then CBC is a pseudorandom function as long as the set of inputs on which it is queried is prefix-free. Formally, for any PPT distinguisher D that queries its oracle on a prefix-free set of inputs, there is a negligible function $\mathsf{negl}$ such that

定理 4.11 如果 F 是一个伪随机函数，那么只要对 CBC 查询的输入集合是无前缀的，CBC 就是一个伪随机函数。形式化地，对于任何向其预言机查询的输入构成无前缀集合的 PPT 区分器 D，存在一个可忽略函数 $\mathsf{negl}$，使得

$$\begin{array}{r}\left|\Pr[D^{\mathsf{CBC}_{k}(\cdot)}(1^{n})=1]-\Pr[D^{f(\cdot)}(1^{n})=1]\right|\leq\mathsf{negl}(n),\end{array}$$

where $k$ is chosen uniformly from $\{0,1\}^{n}$ and $f$ is chosen uniformly from the set of functions mapping $(\{0,1\}^n)^*$ to $\{0,1\}^{n}$ (i.e., the value of $f$ at each input is uniform and independent of the values of $f$ at all other inputs).

其中 $k$ 均匀选自 $\{0,1\}^{n}$，$f$ 均匀选自将 $(\{0,1\}^n)^*$ 映射到 $\{0,1\}^{n}$ 的函数集合（即 $f$ 在每个输入上的值是均匀的，且独立于 $f$ 在所有其他输入上的值）。

Thus, we can convert a pseudorandom function $F$ for fixed-length inputs into a pseudorandom function CBC for arbitrary-length inputs (subject to a constraint on which inputs can be queried). To use this for message authentication, we adapt the idea of Construction 4.5 as follows: to authenticate a message $m$, first apply some encoding function $encode$ to obtain a string $encode(m) \in (\{0,1\}^n)^+$; then output the tag $\mathsf{CBC}_k(\mathsf{encode}(m))$. For this to be secure, the encoding needs to be $prefix$-free, namely, to have the property that for any distinct (allowed) messages $m_1, m_2$, the string $\mathsf{encode}(m_1)$ is not a prefix of $\mathsf{encode}(m_2)$. This implies that for any set of (allowed) messages $\{m_1, \ldots\}$, the set of encoded messages $\{encode(m_1), \ldots\}$ is prefix-free.

因此，我们可以将针对固定长度输入的伪随机函数 $F$ 转换为适用于任意长度输入的伪随机函数 CBC（需要对可查询的输入满足一定的约束）。为了将其用于消息认证，我们调整构造 4.5 的思想如下：为认证消息 $m$，首先应用某个编码函数 $encode$ 以获得串 $encode(m) \in (\{0,1\}^n)^+$；然后输出标签 $\mathsf{CBC}_k(\mathsf{encode}(m))$。为了使其安全，编码需要是**无前缀的**（prefix-free），即对于任意不同的（允许的）消息 $m_1, m_2$，串 $\mathsf{encode}(m_1)$ 不是 $\mathsf{encode}(m_2)$ 的前缀。这意味着对于任意（允许的）消息集合 $\{m_1, \ldots\}$，编码后的消息集合 $\{encode(m_1), \ldots\}$ 是无前缀的。

We now examine two concrete applications of this idea:

我们现在考察该思想的两个具体应用：

- Fix $\ell$, and let the set of allowed messages be $\{0,1\}^{\ell(n)\cdot n}$. Then we can take the trivial encoding $\mathsf{encode}(m) = m$, which is prefix-free since a string cannot be a prefix of a different string of the same length. This is exactly basic CBC-MAC, and what we have said above implies that basic CBC-MAC is secure for messages of any fixed length (cf. Theorem 4.10).

  固定 $\ell$，令允许的消息集合为 $\{0,1\}^{\ell(n)\cdot n}$。那么我们可以采用平凡编码 $\mathsf{encode}(m) = m$，这是无前缀的，因为一个串不能是另一个长度相同的不同串的前缀。这恰好是基本 CBC-MAC，并且我们上面的论述表明基本 CBC-MAC 对于任何固定长度的消息是安全的（参见定理 4.10）。

- One way of handling arbitrary-length messages (technically, messages of length less than ${2}^n$) is to encode a string $m \in \{0,1\}^*$ by prepending its length $|m|$ (encoded as an n-bit string), and then appending as many 0s as needed to make the length of the resulting string a multiple of $n$. (This is essentially what is shown in Figure 4.2.) This encoding is prefix-free, and we therefore obtain a secure MAC for arbitrary-length messages.

  处理任意长度消息（技术上，长度小于 ${2}^n$ 的消息）的一种方法是将串 $m \in \{0,1\}^*$ 编码为：在其前面加上长度 $|m|$（编码为 n 比特串），然后根据需要附加尽可能多的 0，使所得串的长度为 $n$ 的倍数。（这本质上就是图 4.2 所示的方法。）该编码是无前缀的，因此我们获得了适用于任意长度消息的安全 MAC。

The rest of this section is devoted to a proof of Theorem 4.11. In proving the theorem, we analyze CBC when it is "keyed" with a random function g rather than a random key k for some underlying pseudorandom function F. That is, we consider the keyed function $CBC_{g}$ defined as

本节的其余部分专门用于证明定理 4.11。在证明该定理时，我们分析的是以随机函数 $g$ 而非以某个底层伪随机函数 $F$ 的随机密钥 $k$ 为“密钥”的 CBC。也就是说，我们考虑带密钥的函数 $CBC_{g}$，定义为

$$\mathsf{CBC}_{g}(x_{1},\ldots,x_{\ell})\stackrel{\mathrm{def}}{=}g\left(g\left(\cdots g(g(x_{1})\oplus x_{2}\right)\oplus\cdots\right)\oplus x_{\ell}$$

where, for security parameter $n$, the function $g$ maps $n$-bit inputs to $n$-bit outputs, and $|x_1| = \cdots = |x_\ell| = n$. Note that $\mathsf{CBC}_g$ as defined here is not efficient (since the representation of $g$ requires space exponential in $n$); nevertheless, it is still a well-defined, keyed function.

其中，对于安全参数 $n$，函数 $g$ 将 $n$ 比特输入映射到 $n$ 比特输出，且 $|x_1| = \cdots = |x_\ell| = n$。注意，此处定义的 $\mathsf{CBC}_g$ 不是高效的（因为表示 $g$ 需要关于 $n$ 指数级的空间）；尽管如此，它仍然是一个定义良好的带密钥函数。

We show that if $g$ is chosen uniformly from $\mathsf{Func}_n$, then $\mathsf{CBC}_g$ is indistinguishable from a random function mapping $(\{0,1\}^n)^*$ to $n$-bit strings, as long as a prefix-free set of inputs is queried. More precisely:

我们证明，如果 $g$ 均匀选自 $\mathsf{Func}_n$，那么只要查询的是无前缀的输入集合，$\mathsf{CBC}_g$ 与将 $(\{0,1\}^n)^*$ 映射到 $n$ 比特串的随机函数是不可区分的。更精确地说：

THEOREM 4.12 Fix any $n \geq 1$. For any distinguisher $D$ that queries its oracle on a prefix-free set of $q$ inputs, where the longest such input contains $\ell$ blocks, it holds that:

定理 4.12 固定任意 $n \geq 1$。对于任何对其预言机查询 $q$ 个输入（构成无前缀集合）的区分器 $D$，其中最长的输入包含 $\ell$ 个块，有：

$$\left|\Pr[D^{\mathsf{CBC}_{g}(\cdot)}(1^{n})=1]-\Pr[D^{f(\cdot)}(1^{n})=1]\right|\leq\frac{q^{2}\ell^{2}}{2^{n}},$$

where $g$ is chosen uniformly from $\mathsf{Func}_n$, and $f$ is chosen uniformly from the set of functions mapping $(\{0,1\}^n)^*$ to $\{0,1\}^n$.

其中 $g$ 均匀选自 $\mathsf{Func}_n$，$f$ 均匀选自将 $(\{0,1\}^n)^*$ 映射到 $\{0,1\}^n$ 的函数集合。

(The theorem is unconditional, and does not impose any constraints on the running time of $D$. Thus we may take $D$ to be deterministic.) The above implies Theorem 4.11 using standard techniques that we have already seen. In particular, for any $D$ running in polynomial time $q(n)$ and $\ell(n)$ are polynomial and so $q(n)^{2}\ell(n)^{2}/2^{n}$ is negligible.

（该定理是无条件的，不对 $D$ 的运行时间施加任何限制。因此我们可以取 $D$ 为确定性的。）上述结论利用我们已经见过的标准技术即可推出定理 4.11。特别地，对于任何在多项式时间内运行的 $D$，$q(n)$ 和 $\ell(n)$ 是多项式，因此 $q(n)^{2}\ell(n)^{2}/2^{n}$ 是可忽略的。

PROOF (of Theorem 4.12) Fix some $n \geq 1$. The proof proceeds in two steps: We first define a notion of smoothness and prove that CBC is smooth; we then show that smoothness implies the claim.

证明（定理 4.12）固定某个 $n \geq 1$。证明分两步进行：我们首先定义光滑性（smoothness）的概念，并证明 CBC 是光滑的；然后证明光滑性蕴含该结论。

Let $P = \{X_1, \ldots, X_q\}$ be a prefix-free set of $q$ inputs, where each $X_i$ is in $(\{0,1\}^n)^*$ and the longest string in $P$ contains $\ell$ blocks (i.e., each $X_i \in P$ contains at most $\ell$ blocks of length $n$). Note that for any $t_1, \ldots, t_q \in \{0,1\}^n$ it holds that $\Pr[\forall i: f(X_i) = t_i] = 2^{-nq}$, where the probability is over uniform choice of the function $f$ from the set of functions mapping $(\{0,1\}^n)^*$ to $\{0,1\}^n$. We say that CBC is $(q, \ell, \delta)$-smooth if for every prefix-free set $P = \{X_1, \ldots, X_q\}$ as above and every $t_1, \ldots, t_q \in \{0,1\}^n$, it holds that

令 $P = \{X_1, \ldots, X_q\}$ 是一个由 $q$ 个输入组成的无前缀集合，其中每个 $X_i \in (\{0,1\}^n)^*$，且 $P$ 中最长的串包含 $\ell$ 个块（即每个 $X_i \in P$ 最多包含 $\ell$ 个长度为 $n$ 的块）。注意，对于任意 $t_1, \ldots, t_q \in \{0,1\}^n$，有 $\Pr[\forall i: f(X_i) = t_i] = 2^{-nq}$，其中概率取自函数 $f$ 从将 $(\{0,1\}^n)^*$ 映射到 $\{0,1\}^n$ 的函数集合中的均匀选择。如果对于每个如上所示的无前缀集合 $P = \{X_1, \ldots, X_q\}$ 以及每个 $t_1, \ldots, t_q \in \{0,1\}^n$，都有

$$\Pr\left[\forall i:{\mathsf{CBC}}_{g}(X_{i})=t_{i}\right]\geq(1-\delta)\cdot2^{-n q},$$

where the probability is over uniform choice of $g \in \mathrm{Func}_{n}$.

其中概率取自 $g \in \mathrm{Func}_{n}$ 的均匀选择，则称 CBC 是 $(q, \ell, \delta)$-光滑的。

In words, CBC is $(q,\ell,\delta)$-smooth if for every fixed set of input/output pairs $\{(X_i,t_i)\}$, where the $\{X_i\}$ form a prefix-free set and each contain at most $\ell$ blocks, the probability that $\mathsf{CBC}_g(X_i)=t_i$ for all $i$ (where $g$ is a random function from $\{0,1\}^n$ to $\{0,1\}^n$) is at least ${1}-\delta$ times the probability that $f(X_i)=t_i$ for all $i$ (where $f$ is a random function from $(\{0,1\}^n)^\ast$ to $\{0,1\}^n$).

换言之，CBC 是 $(q,\ell,\delta)$-光滑的，如果对于每个固定的输入/输出对集合 $\{(X_i,t_i)\}$，其中 $\{X_i\}$ 构成无前缀集合且每个最多包含 $\ell$ 个块，对所有 $i$ 有 $\mathsf{CBC}_g(X_i)=t_i$ 的概率（其中 $g$ 是从 $\{0,1\}^n$ 到 $\{0,1\}^n$ 的随机函数）至少是对所有 $i$ 有 $f(X_i)=t_i$ 的概率（其中 $f$ 是从 $(\{0,1\}^n)^\ast$ 到 $\{0,1\}^n$ 的随机函数）的 ${1}-\delta$ 倍。

CLAIM 4.13 CBC is $(q,\ell,\delta)$-smooth, for $\delta=q^{2}\ell^{2}/2^{n}$.

断言 4.13 CBC 是 $(q,\ell,\delta)$-光滑的，其中 $\delta=q^{2}\ell^{2}/2^{n}$。

PROOF Fix $P$ as above. For $X \in P$, with $X = x_1, \ldots$ and $x_i \in \{0,1\}^n$, let $\mathcal{C}_g(X)$ denote the ordered list of inputs on which $g$ is evaluated during the computation of $\mathsf{CBC}_g(X)$; i.e., if $X \in (\{0,1\}^n)^m$ then

证明 固定如上所示的 $P$。对于 $X \in P$，设 $X = x_1, \ldots$ 且 $x_i \in \{0,1\}^n$，令 $\mathcal{C}_g(X)$ 表示在计算 $\mathsf{CBC}_g(X)$ 期间对 $g$ 进行评估的输入的有序列表；即，如果 $X \in (\{0,1\}^n)^m$，则

$$\mathcal{C}_{g}(X)\stackrel{\mathrm{def}}{=}\left(x_{1},~\mathsf{CBC}_{g}(x_{1})\oplus x_{2},~\ldots,~\mathsf{CBC}_{g}(x_{1},\ldots,x_{m-1})\oplus x_{m}\right).$$

For $X \in (\{0,1\}^n)^m$ and $X^{\prime} \in (\{0,1\}^n)^m$, with $\mathcal{C}_g(X) = (I_1, \ldots, I_m)$ and $\mathcal{C}_g(X^{\prime}) = (I^{\prime}_1, \ldots, I^{\prime}_m)$, say there is a non-trivial collision in $X$ if $I_i = I_j$ for some $i \neq j$, and say there is a non-trivial collision between $X$ and $X^{\prime}$ if $I_i = I^{\prime}_j$ but $(x_1, \ldots, x_i) \neq (x^{\prime}_1, \ldots, x^{\prime}_j)$. We say there is a non-trivial collision in $P$ if there is a non-trivial collision in some $X \in P$ or between some pair of strings $X, X^{\prime} \in P$. Let $\mathsf{Coll}$ be the event that there is a non-trivial collision in $P$.

对于 $X \in (\{0,1\}^n)^m$ 和 $X^{\prime} \in (\{0,1\}^n)^m$，设 $\mathcal{C}_g(X) = (I_1, \ldots, I_m)$ 和 $\mathcal{C}_g(X^{\prime}) = (I^{\prime}_1, \ldots, I^{\prime}_m)$，如果存在 $i \neq j$ 使得 $I_i = I_j$，则称 $X$ 中存在**非平凡碰撞**（non-trivial collision）；如果 $I_i = I^{\prime}_j$ 但 $(x_1, \ldots, x_i) \neq (x^{\prime}_1, \ldots, x^{\prime}_j)$，则称 $X$ 与 $X^{\prime}$ 之间存在非平凡碰撞。如果某个 $X \in P$ 中存在非平凡碰撞，或者某对串 $X, X^{\prime} \in P$ 之间存在非平凡碰撞，则称 $P$ 中存在非平凡碰撞。令 $\mathsf{Coll}$ 表示 $P$ 中存在非平凡碰撞的事件。

We prove the claim in two steps. First, we show that conditioned on the event that $\mathsf{Coll}$ does not occur, the probability that $\mathsf{CBC}_g(X_i) = t_i$ for all $i$ is exactly ${2}^{-nq}$. Next, we show that $\Pr[\mathsf{Coll}] < \delta = q^2 \ell^2/2^n$.

我们分两步证明这个断言。首先，我们证明在 $\mathsf{Coll}$ 不发生的事件条件下，对所有 $i$ 有 $\mathsf{CBC}_g(X_i) = t_i$ 的概率恰好是 ${2}^{-nq}$。接下来，我们证明 $\Pr[\mathsf{Coll}] < \delta = q^2 \ell^2/2^n$。

Consider choosing a uniform $g$ by choosing, one-by-one, uniform values for the outputs of $g$ on different inputs. Determining whether there is a non-trivial collision between two strings $X, X^{\prime} \in P$ can be done by first choosing the values of $g(I_{1})$ and $g(I_{1}^{\prime})$ (if $I_{1}^{\prime} = I_{1}$, these values are the same), then choosing values for $g(I_{2})$ and $g(I_{2}^{\prime})$ (note that $I_{2} = g(I_{1}) \oplus x_{2}$ and $I_{2}^{\prime} = g(I_{1}^{\prime}) \oplus x_{2}^{\prime}$ are defined once $g(I_{1}), g(I_{1}^{\prime})$ have been fixed), and continuing in this way until we choose values for $g(I_{m-1})$ and $g(I_{m^{\prime}-1})$. Observe that the values of $g(I_{m}), g(I_{m^{\prime}})$ need not be chosen in order to determine whether there is a non-trivial collision between $X$ and $X^{\prime}$. Similarly, the value of $g(I_{m})$ need not be chosen in order to determine whether there is a non-trivial collision in $X$. Thus, it is possible to determine whether $\mathsf{Coll}$ occurs by choosing the values of $g$ on all but the final entries of each of $\mathcal{C}_{g}(X_{1}), \ldots, \mathcal{C}_{g}(X_{q})$.

考虑通过逐个为 $g$ 在不同输入上的输出选择均匀值的方式来选择一个均匀的 $g$。确定两个串 $X, X^{\prime} \in P$ 之间是否存在非平凡碰撞，可以通过先选择 $g(I_{1})$ 和 $g(I_{1}^{\prime})$ 的值（如果 $I_{1}^{\prime} = I_{1}$，则这些值相同），然后选择 $g(I_{2})$ 和 $g(I_{2}^{\prime})$ 的值（注意，一旦 $g(I_{1}), g(I_{1}^{\prime})$ 被固定，$I_{2} = g(I_{1}) \oplus x_{2}$ 和 $I_{2}^{\prime} = g(I_{1}^{\prime}) \oplus x_{2}^{\prime}$ 就被定义了），并以此类推，直到我们选择 $g(I_{m-1})$ 和 $g(I_{m^{\prime}-1})$ 的值。观察到，为了确定 $X$ 和 $X^{\prime}$ 之间是否存在非平凡碰撞，不需要选择 $g(I_{m}), g(I_{m^{\prime}})$ 的值。类似地，为了确定 $X$ 中是否存在非平凡碰撞，不需要选择 $g(I_{m})$ 的值。因此，可以通过选择 $g$ 在 $\mathcal{C}_{g}(X_{1}), \ldots, \mathcal{C}_{g}(X_{q})$ 中除每个列表的最后一个条目之外的所有输入上的值，来确定 $\mathsf{Coll}$ 是否发生。

Assume $\mathsf{Coll}$ has not occurred after fixing the values of $g$ on various inputs as described above. Consider the final entries in each of $\mathcal{C}_g(X_1), \ldots, \mathcal{C}_g(X_q)$. These entries are all distinct (this is immediate from the fact that $\mathsf{Coll}$ has not occurred), and we claim that the value of $g$ on each of those points has not yet been fixed. Indeed, the only way the value of $g$ could already be fixed on any of those points is if the final entry $I_m$ of some $\mathcal{C}_g(X)$ is equal to a non-final entry $I_j$ of some $\mathcal{C}_g(X^{\prime})$. But since $\mathsf{Coll}$ has not occurred, this can only happen if $X \neq X^{\prime}$ and $(x^{\prime}_1, \ldots, x^{\prime}_j) = (x_1, \ldots, x_m)$. But then $X$ would be a prefix of $X^{\prime}$, contradicting the assumption that $P$ is prefix-free.

假设在如上所述固定了 $g$ 在各种输入上的值后，$\mathsf{Coll}$ 尚未发生。考虑 $\mathcal{C}_g(X_1), \ldots, \mathcal{C}_g(X_q)$ 中每个列表的最后一个条目。这些条目都是不同的（这直接来自 $\mathsf{Coll}$ 尚未发生的事实），并且我们断言 $g$ 在这些点上的值尚未被固定。事实上，$g$ 的值在这些点中的任何一个上已经被固定的唯一方式是，某个 $\mathcal{C}_g(X)$ 的最后一个条目 $I_m$ 等于某个 $\mathcal{C}_g(X^{\prime})$ 的非最后一个条目 $I_j$。但由于 $\mathsf{Coll}$ 尚未发生，这只能在 $X \neq X^{\prime}$ 且 $(x^{\prime}_1, \ldots, x^{\prime}_j) = (x_1, \ldots, x_m)$ 时发生。但那样 $X$ 将是 $X^{\prime}$ 的前缀，与 $P$ 是无前缀集合的假设矛盾。

Since $g$ is a random function, the above means that $\mathrm{CBC}_g(X_1), \ldots, \mathrm{CBC}_g(X_q)$ are uniform and independent of each other as well as all the other values of $g$ that have already been fixed. (This is because $\mathrm{CBC}_g(X_i)$ is the value of $g$ when evaluated at the final entry of $C_g(X_i)$, an input value which is different from all the other inputs at which $g$ has already been fixed.) Thus, for any $t_1, \ldots, t_q \in \{0,1\}^n$ we have:

由于 $g$ 是一个随机函数，上述意味着 $\mathrm{CBC}_g(X_1), \ldots, \mathrm{CBC}_g(X_q)$ 是均匀的，并且相互独立，同时也独立于所有其他已经固定的 $g$ 的值。（这是因为 $\mathrm{CBC}_g(X_i)$ 是 $g$ 在 $C_g(X_i)$ 的最后一个条目上评估的值，而该输入值与 $g$ 已经被固定的所有其他输入都不同。）因此，对于任意 $t_1, \ldots, t_q \in \{0,1\}^n$，我们有：

$$\Pr\left[\forall i:{\mathsf{CBC}}_{g}(X_{i})=t_{i}\mid\overline{{\mathsf{Coll}}}\right]=2^{-n q}.\tag{4.5}$$

We next show that $\mathsf{Coll}$ occurs with high probability by upper-bounding $\Pr[\mathsf{Coll}]$. For distinct $X_i, X_j \in P$, let $\mathsf{Coll}_{i,j}$ be the event that there is a non-trivial collision in $X_i$ or in $X_j$, or a non-trivial collision between $X_i$ and $X_j$. We have $\mathsf{Coll} = \bigvee_{i,j} \mathsf{Coll}_{i,j}$ and so a union bound gives

接下来我们通过给出 $\Pr[\mathsf{Coll}]$ 的上界来证明 $\overline{\mathsf{Coll}}$（即不发生碰撞）以高概率发生。（译者注：原文为"Coll occurs with high probability"，但下文给出的上界 $\delta = q^2\ell^2/2^n$ 表明 Coll 发生概率其实很低，此处原文疑为 $\overline{\mathsf{Coll}}$ occurs with high probability 之误。）对于不同的 $X_i, X_j \in P$，令 $\mathsf{Coll}_{i,j}$ 表示 $X_i$ 或 $X_j$ 中存在非平凡碰撞，或 $X_i$ 与 $X_j$ 之间存在非平凡碰撞的事件。我们有 $\mathsf{Coll} = \bigvee_{i,j} \mathsf{Coll}_{i,j}$，因此使用联合界（union bound）可得

$$\Pr[\mathsf{Coll}]\leq\sum_{i,j:i<j}\Pr[\mathsf{Coll}_{i,j}]<\frac{q^{2}}{2}\cdot\operatorname*{max}_{i<j}\left\{\Pr[\mathsf{Coll}_{i,j}]\right\}.\tag{4.6}$$

Fixing distinct $X = X_i$ and $X^{\prime} = X_j$ in $P$, we now bound $\max_{i < j} \{\Pr[\mathsf{Coll}_{i,j}]\}$. It is clear that the probability is maximized when $X$ and $X^{\prime}$ are both as long as possible, and thus we assume they are each $\ell$ blocks long. Let $X = (x_1, \ldots, x_\ell)$ and $X^{\prime} = (x^{\prime}_1, \ldots, x^{\prime}_\ell)$, and let $t$ be the largest integer such that $(x_1, \ldots, x_t) = (x^{\prime}_1, \ldots, x^{\prime}_t)$. (Note that $t < \ell$ or else $X = X^{\prime}$.) We assume $t > 0$, but the analysis below can be easily modified, giving the same result, if $t = 0$. We continue to let $I_1, I_2, \ldots$ (resp., $I^{\prime}_1, I^{\prime}_2, \ldots$) denote the inputs to $g$ during the course of computing $\mathsf{CBC}_g(X)$ (resp., $\mathsf{CBC}_g(X^{\prime}))$; note that $(I_1^{\prime}, \ldots, I_t^{\prime}) = (I_1, \ldots, I_t)$. Consider choosing $g$ by choosing uniform values for the outputs of $g$, one-by-one. We do this in ${2}\ell - t - 2$ steps as follows:

固定 $P$ 中不同的 $X = X_i$ 和 $X^{\prime} = X_j$，我们现在给出 $\max_{i < j} \{\Pr[\mathsf{Coll}_{i,j}]\}$ 的上界。显然，当 $X$ 和 $X^{\prime}$ 都尽可能长时概率最大，因此我们假设它们各为 $\ell$ 个块长。设 $X = (x_1, \ldots, x_\ell)$ 和 $X^{\prime} = (x^{\prime}_1, \ldots, x^{\prime}_\ell)$，并令 $t$ 是满足 $(x_1, \ldots, x_t) = (x^{\prime}_1, \ldots, x^{\prime}_t)$ 的最大整数。（注意 $t < \ell$，否则 $X = X^{\prime}$。）我们假设 $t > 0$，但如果 $t = 0$，下面的分析也可以很容易地修改，得到相同的结果。我们继续用 $I_1, I_2, \ldots$（相应地，$I^{\prime}_1, I^{\prime}_2, \ldots$）表示在计算 $\mathsf{CBC}_g(X)$（相应地，$\mathsf{CBC}_g(X^{\prime})$）过程中 $g$ 的输入；注意 $(I_1^{\prime}, \ldots, I_t^{\prime}) = (I_1, \ldots, I_t)$。考虑通过逐个为 $g$ 的输出选择均匀值的方式来选择 $g$。我们按如下步骤进行，共 ${2}\ell - t - 2$ 步：

Steps 1 through $t-1$ (if $t>1$): In each step $i$, choose a uniform value for $g(I_i)$, thus defining $I_{i+1}$ and $I^{\prime}_{i+1}$ (which are equal).

第 1 步到第 $t-1$ 步（如果 $t>1$）：在第 $i$ 步，为 $g(I_i)$ 选择一个均匀值，从而定义 $I_{i+1}$ 和 $I^{\prime}_{i+1}$（两者相等）。

Step t: Choose a uniform value for $g(I_t)$, thus defining $I_{t+1}$ and $I^{\prime}_{t+1}$.

第 t 步：为 $g(I_t)$ 选择一个均匀值，从而定义 $I_{t+1}$ 和 $I^{\prime}_{t+1}$。

Steps $t+1$ to $\ell-1$ (if $t<\ell-1$): Choose, in turn, uniform values for each of $g(I_{t+1})$, $g(I_{t+2})$, ..., $g(I_{\ell-1})$, thus defining $I_{t+2}$, $I_{t+3}$, ..., $I_{\ell}$.

第 $t+1$ 步到第 $\ell-1$ 步（如果 $t<\ell-1$）：依次为 $g(I_{t+1})$、$g(I_{t+2})$、……、$g(I_{\ell-1})$ 各选择一个均匀值，从而定义 $I_{t+2}$、$I_{t+3}$、……、$I_{\ell}$。

Steps $\ell$ to ${2}\ell - t - 2$ (if $t < \ell - 1$): Choose, in turn, uniform values for each of $g(I^{\prime}_{t+1})$, $g(I^{\prime}_{t+2})$, ..., $g(I^{\prime}_{\ell-1})$, thus defining $I^{\prime}_{t+2}$, $I^{\prime}_{t+3}$, ..., $I^{\prime}_{\ell}$.

第 $\ell$ 步到第 ${2}\ell - t - 2$ 步（如果 $t < \ell - 1$）：依次为 $g(I^{\prime}_{t+1})$、$g(I^{\prime}_{t+2})$、……、$g(I^{\prime}_{\ell-1})$ 各选择一个均匀值，从而定义 $I^{\prime}_{t+2}$、$I^{\prime}_{t+3}$、……、$I^{\prime}_{\ell}$。

Let $\mathsf{Coll}(k)$ be the event that a non-trivial collision occurs by step $k$. Then

令 $\mathsf{Coll}(k)$ 表示到第 $k$ 步为止发生非平凡碰撞的事件。那么

$$
\begin{aligned}
\Pr[\mathsf{Coll}_{i,j}]=&\Pr\big[\bigvee_{k}\mathsf{Coll}(k)\big]\\
\leq&\Pr[\mathsf{Coll}(1)]+\sum_{k=2}^{2\ell-t-2}\Pr[\mathsf{Coll}(k)|\overline{\mathsf{Coll}(k-1)}],
\end{aligned} \tag{4.7}
$$

using Proposition A.9. For $k < t$, we claim $\Pr[\mathsf{Coll}(k) \mid \overline{\mathsf{Coll}}(k-1)] = k/2^n$; indeed, if no non-trivial collision has occurred by step $k-1$, the value of $g(I_k)$ is chosen uniformly in step $k$; a non-trivial collision occurs only if it happens that $I_{k+1} = g(I_k) \oplus x_{k+1}$ is equal to one of $\{I_1, \ldots, I_k\}$ (which are all distinct, since $\mathsf{Coll}(k-1)$ has not occurred). By similar reasoning, we have $\Pr[\mathsf{Coll}(t) \mid \overline{\mathsf{Coll}}(t-1)] \leq 2t/2^n$ (here there are two values $I_{t+1}, I_{t+1}^{\prime}$, to consider; note that they cannot be equal to each other). Finally, arguing as before, for $k > t$ we have $\Pr[\mathsf{Coll}(k) \mid \overline{\mathsf{Coll}}(k-1)] = (k+1)/2^n$. Using Equation (4.7), we thus have

利用命题 A.9。对于 $k < t$，我们断言 $\Pr[\mathsf{Coll}(k) \mid \overline{\mathsf{Coll}}(k-1)] = k/2^n$；确实，如果到第 $k-1$ 步为止没有发生非平凡碰撞，则 $g(I_k)$ 的值在第 $k$ 步被均匀选择；非平凡碰撞仅当 $I_{k+1} = g(I_k) \oplus x_{k+1}$ 等于 $\{I_1, \ldots, I_k\}$ 中的某一个时发生（由于 $\mathsf{Coll}(k-1)$ 尚未发生，所有这些值互不相同）。通过类似的推理，我们有 $\Pr[\mathsf{Coll}(t) \mid \overline{\mathsf{Coll}}(t-1)] \leq 2t/2^n$（这里需要考虑两个值 $I_{t+1}, I_{t+1}^{\prime}$；注意它们彼此不可能相等）。最后，与之前类似的论证，对于 $k > t$，我们有 $\Pr[\mathsf{Coll}(k) \mid \overline{\mathsf{Coll}}(k-1)] = (k+1)/2^n$。利用式 (4.7)，我们有

$$\begin{align*}\Pr[\mathsf{Coll}_{i,j}]&\leq2^{-n}\cdot\left(\sum_{k=1}^{t-1}k+2t+\sum_{k=t+1}^{2\ell-t-2}(k+1)\right)\\&=2^{-n}\cdot\sum_{k=2}^{2\ell-t-1}k<\ 2\ell^{2}\cdot2^{-n}.\end{align*}$$

From Equation (4.6) we get $\Pr[\mathsf{Coll}] < q^2\ell^2 \cdot 2^{-n} = \delta$. Finally, using Equation (4.5) we see that

从式 (4.6) 我们得到 $\Pr[\mathsf{Coll}] < q^2\ell^2 \cdot 2^{-n} = \delta$。最后，利用式 (4.5) 我们得到

$$\begin{align*}\Pr\left[\forall i:\mathsf{CBC}_{g}(X_{i})=t_{i}\right]&\geq\Pr\left[\forall i:\mathsf{CBC}_{g}(X_{i})=t_{i}\mid\overline{\mathsf{Coll}}\right]\cdot\Pr[\overline{\mathsf{Coll}}]\\&=2^{-nq}\cdot\Pr[\overline{\mathsf{Coll}}]\geq(1-\delta)\cdot2^{-nq},\end{align*}$$

as claimed.

断言得证。

We now show that smoothness implies the theorem. Assume without loss of generality that $D$ always makes $q$ (distinct) queries, each containing at most $\ell$ blocks. $D$ may choose its queries adaptively (i.e., depending on the answers to previous queries), but the set of $D$'s queries must be prefix-free.

我们现在证明光滑性蕴含该定理。不失一般性，假设 $D$ 总是发出 $q$ 个（互不相同的）查询，每个查询最多包含 $\ell$ 个块。$D$ 可以自适应地选择其查询（即取决于之前查询的答案），但 $D$ 的查询集合必须是无前缀的。

For distinct $X_1, \ldots, X_q \in (\{0,1\}^n)^*$ and arbitrary $t_1, \ldots, t_q \in \{0,1\}^n$, define $\alpha(X_1, \ldots, X_q; t_1, \ldots, t_q)$ to be 1 if and only if $D$ outputs 1 when making queries $X_1, \ldots, X_q$ and getting responses $t_1, \ldots, t_q$. (If, say, $D$ does not make query $X_1$ as its first query, then $\alpha(X_1, \ldots, \ldots) = 0$) Letting $\bar{X} = (X_1, \ldots, X_q)$ and $\bar{t} = (t_1, \ldots, t_q)$, we then have

对于不同的 $X_1, \ldots, X_q \in (\{0,1\}^n)^*$ 和任意的 $t_1, \ldots, t_q \in \{0,1\}^n$，定义 $\alpha(X_1, \ldots, X_q; t_1, \ldots, t_q)$ 为 1 当且仅当 $D$ 在发出查询 $X_1, \ldots, X_q$ 并获得响应 $t_1, \ldots, t_q$ 时输出 1。（例如，如果 $D$ 没有以 $X_1$ 作为其第一个查询，则 $\alpha(X_1, \ldots, \ldots) = 0$）令 $\bar{X} = (X_1, \ldots, X_q)$ 和 $\bar{t} = (t_1, \ldots, t_q)$，那么

$$\begin{align*}\Pr[D^{\mathsf{CBC}_{g}(\cdot)}(1^{n})=1]&=\sum_{\bar{X}\ \mathrm{prefix-free};\ \bar{t}}\alpha(\bar{X},\bar{t})\cdot\Pr[\forall i:\mathsf{CBC}_{g}(X_{i})=t_{i}]\\&\geq\sum_{\bar{X}\ \mathrm{prefix-free};\ \bar{t}}\alpha(\bar{X},\bar{t})\cdot(1-\delta)\cdot\Pr[\forall i:f(X_{i})=t_{i}]\\&=(1-\delta)\cdot\Pr[D^{f(\cdot)}(1^{n})=1]\end{align*}$$

where, above, g is chosen uniformly from $\mathsf{Func}_n$, and f is chosen uniformly from the set of functions mapping $(\{0,1\}^n)^*$ to $\{0,1\}^n$. This implies

其中，上式中 g 均匀选自 $\mathsf{Func}_n$，f 均匀选自将 $(\{0,1\}^n)^*$ 映射到 $\{0,1\}^n$ 的函数集合。这意味着

$$\Pr[D^{f(\cdot)}(1^{n})=1]-\Pr[D^{\mathsf{CBC}_{g}(\cdot)}(1^{n})=1]\leq\delta\cdot\Pr[D^{f(\cdot)}(1^{n})=1]\leq\delta.$$

A symmetric argument for when D outputs 0 completes the proof.

对 D 输出 0 的情况进行对称的论证即可完成证明。

## 4.5 GMAC and Poly1305　4.5 GMAC 与 Poly1305

One drawback of CBC-MAC is that it requires a number of cryptographic operations (specifically, block-cipher evaluations) linear in the length of the message being authenticated. We show here two (related) constructions of secure MACs that can be much more efficient. These MACs have been adopted by several internet standards.

CBC-MAC 的一个缺点是其需要的密码学操作（具体地，分组密码评估）次数与被认证消息的长度成线性关系。我们在此给出两个（相关的）安全 MAC 构造，它们可以更加高效。这些 MAC 已被多个互联网标准采纳。

We present a general paradigm for building secure MACs in Section 4.5.1, and then look at two concrete instantiations of that paradigm—GMAC and Poly1305—in Section 4.5.2.

我们在 4.5.1 节介绍构建安全 MAC 的通用范式，然后在 4.5.2 节考察该范式的两个具体实例——GMAC 和 Poly1305。

### 4.5.1 MACs from Difference-Universal Functions　4.5.1 基于差分通用函数的 MAC

In this section we show a general approach for constructing MACs based on a combinatorial object called a difference-universal function. The paradigm we describe here is inspired by a construction of an information-theoretic MAC that we show in Section 4.6.2; nevertheless, our treatment is self contained and does not directly rely on any results from that section.

在本节中，我们展示一种基于称为**差分通用函数**（difference-universal function）的组合对象来构造 MAC 的通用方法。这里描述的范式受到我们在 4.6.2 节中展示的信息论 MAC 构造的启发；尽管如此，我们的论述是自包含的，不直接依赖于该节的任何结果。

Let $h$ be a keyed function that, for security parameter $n$, maps keys in $\mathcal{K}_n$ and inputs in $\mathcal{M}_n$ to outputs in $\mathcal{T}_n$. (We require also that $h$ is efficiently computable, and that elements in $\{\mathcal{K}_n\}, \{\mathcal{M}_n\}$, and $\{\mathcal{T}_n\}$ can be sampled efficiently, but for simplicity we omit this from the definition.) As usual, we write $h_k(m)$ instead of $h(k, m)$. We assume that $\mathcal{T}_n$ is a group for each $n$. (The reader unfamiliar with the notion of a group can refer to Section 9.1; in this section, nothing beyond the definition of a group is needed.) We now define what it means for $h$ to be difference universal.

设 $h$ 是一个带密钥的函数，对于安全参数 $n$，它将 $\mathcal{K}_n$ 中的密钥和 $\mathcal{M}_n$ 中的输入映射到 $\mathcal{T}_n$ 中的输出。（我们还要求 $h$ 是高效可计算的，且 $\{\mathcal{K}_n\}$、$\{\mathcal{M}_n\}$ 和 $\{\mathcal{T}_n\}$ 中的元素可以被高效采样，但为简单起见，我们在定义中省略了这一点。）通常，我们写作 $h_k(m)$ 而不是 $h(k, m)$。我们假设 $\mathcal{T}_n$ 对每个 $n$ 都是一个群。（不熟悉群概念的读者可以参考 9.1 节；在本节中，不需要任何超出群定义的知识。）我们现在定义 $h$ 为差分通用的确切含义。

DEFINITION 4.14 A keyed function $h$ as above is $\varepsilon(n)$-difference universal if for all $n$, any distinct $m, m^{\prime} \in \mathcal{M}_n$, and any $\Delta \in \mathcal{T}_n$ it holds that

定义 4.14 如上所示的带密钥函数 $h$ 是 **$\varepsilon(n)$-差分通用**的，如果对于所有 $n$、任何不同的 $m, m^{\prime} \in \mathcal{M}_n$ 以及任何 $\Delta \in \mathcal{T}_n$，有

$$\Pr\left[h_{k}(m)-h_{k}(m^{\prime})=\Delta\right]\leq\varepsilon(n),$$

where the probability is taken over uniform choice of $k \in \mathcal{K}_n$.

其中概率取自 $k \in \mathcal{K}_n$ 的均匀选择。

Note that we must have $\varepsilon(n) \geq 1/|\mathcal{T}_n|$. Difference-universal functions with $\varepsilon(n)$ negligible can be constructed without any assumptions. For now we simply assume their existence (though a simple example is given in Section 4.6.2), and defer further discussion to the next section.

注意我们必须有 $\varepsilon(n) \geq 1/|\mathcal{T}_n|$。具有可忽略 $\varepsilon(n)$ 的差分通用函数可以在没有任何假设的情况下构造。目前我们仅假定它们存在（尽管在 4.6.2 节中给出了一个简单例子），并将进一步讨论推迟到下一节。

In Construction 4.15 we show how to use a difference-universal function $h$ in conjunction with a pseudorandom function $F$ to construct a message authentication code. Roughly, the shared key consists of a key $k_h$ for $h$ as well as a key $k_F$ for $F$; a tag on a message $m \in \mathcal{M}_n$ is computed by choosing a uniform value $r \in \{0,1\}^n$ and masking $h_{k_h}(m)$ using $F_{k_F}(r)$. In the construction we assume for simplicity that for security parameter $n$ the keyed function $F$ maps $n$-bit keys and $n$-bit inputs to elements of $\mathcal{T}_n$.

在构造 4.15 中，我们展示如何将差分通用函数 $h$ 与伪随机函数 $F$ 结合使用来构造消息认证码。粗略地说，共享密钥由 $h$ 的密钥 $k_h$ 和 $F$ 的密钥 $k_F$ 组成；消息 $m \in \mathcal{M}_n$ 上的标签通过选择一个均匀值 $r \in \{0,1\}^n$ 并使用 $F_{k_F}(r)$ 掩盖 $h_{k_h}(m)$ 来计算。在该构造中，为简单起见，我们假设对于安全参数 $n$，带密钥的函数 $F$ 将 $n$ 比特密钥和 $n$ 比特输入映射到 $\mathcal{T}_n$ 中的元素。

Interestingly, this is the first (and only) example we will see of a randomized MAC. For this reason, we explicitly consider strong security.

有趣的是，这是我们将看到的第一个（也是唯一一个）随机化 MAC 的例子。因此，我们明确考虑强安全性。

THEOREM 4.16 Let $h$ be an $\varepsilon(n)$-difference-universal function for a negligible function $\varepsilon$, and let $F$ be a pseudorandom function. Then Construction 4.15 is a strongly secure MAC for messages in $\{\mathcal{M}_n\}$.

定理 4.16 设 $h$ 是一个 $\varepsilon(n)$-差分通用函数，其中 $\varepsilon$ 是可忽略函数，并设 $F$ 是一个伪随机函数。那么构造 4.15 对于 $\{\mathcal{M}_n\}$ 中的消息是一个强安全的 MAC。

> **CONSTRUCTION 4.15**　**构造 4.15**
>
> Let $h, F$ be as in the text. Define a MAC for messages in $\{\mathcal{M}_n\}$ as follows:
> Gen: on input ${1}^n$, choose uniform $k_h \in \mathcal{K}_n$ and $k_F \in \{0,1\}^n$; output the key $(k_h, k_F)$.
> - Mac: on input a key $(k_h, k_F)$ and a message $m \in \mathcal{M}_n$, choose a uniform $r \in \{0,1\}^n$ and output the tag $t := \langle r, h_{k_h}(m) + F_{k_F}(r) \rangle$.
> - $\mathsf{Vrfy}$: on input a key $(k_h, k_F)$, a message $m \in \mathcal{M}_n$, and a tag $t = \langle r, s \rangle$, output 1 if and only if $s \overset{?}{=} h_{k_h}(m) + F_{k_F}(r)$.
>
> 设 $h, F$ 如前文所述。为 $\{\mathcal{M}_n\}$ 中的消息定义 MAC 如下：
> Gen：输入 ${1}^n$，选择均匀的 $k_h \in \mathcal{K}_n$ 和 $k_F \in \{0,1\}^n$；输出密钥 $(k_h, k_F)$。
> - Mac：输入密钥 $(k_h, k_F)$ 和消息 $m \in \mathcal{M}_n$，选择一个均匀的 $r \in \{0,1\}^n$，并输出标签 $t := \langle r, h_{k_h}(m) + F_{k_F}(r) \rangle$。
> - $\mathsf{Vrfy}$：输入密钥 $(k_h, k_F)$、消息 $m \in \mathcal{M}_n$ 和标签 $t = \langle r, s \rangle$，当且仅当 $s \overset{?}{=} h_{k_h}(m) + F_{k_F}(r)$ 时输出 1。
>
> A MAC based on a difference-universal function.
> 基于差分通用函数的 MAC。

PROOF Let $\mathcal{A}$ be a PPT adversary, let $q = q(n)$ be a polynomial upper bound on the number of queries $\mathcal{A}$ makes to its Mac oracle, and let $\Pi$ denote Construction 4.15. As usual, we first define a scheme $\widetilde{\Pi}$ that is the same as $\Pi$ except that it uses a truly random function $f$ with the appropriate domain and range in place of $F_{k_F}$. As in previous proofs involving pseudorandom functions, one can show that there is a negligible function $\mathsf{negl}$ such that

证明 设 $\mathcal{A}$ 是一个 PPT 敌手，令 $q = q(n)$ 是 $\mathcal{A}$ 对其 Mac 预言机查询次数的多项式上界，并令 $\Pi$ 表示构造 4.15。与往常一样，我们首先定义一个方案 $\widetilde{\Pi}$，它与 $\Pi$ 相同，只是使用一个具有适当定义域和值域的真正随机函数 $f$ 来代替 $F_{k_F}$。与之前涉及伪随机函数的证明一样，可以证明存在一个可忽略函数 $\mathsf{negl}$，使得

$$\left|\Pr\left[\mathsf{Mac-sforge}_{\mathcal{A},\widetilde{\Pi}}(n)=1\right]-\Pr\left[\mathsf{Mac-sforge}_{\mathcal{A},\Pi}(n)=1\right]\right|\leq\mathsf{negl}(n).$$

In the remainder of the proof, we analyze $\widetilde{\Pi}$.

在证明的剩余部分，我们分析 $\widetilde{\Pi}$。

Let repeat denote the event that the same random value $r$ is used to answer two different oracle queries in $\mathsf{Mac-sforge}_{\mathcal{A},\widetilde{\Pi}}(n)$, and let new-r denote the event that $\mathcal{A}$ outputs $(m, \langle r, s \rangle)$ where $r$ was not used to answer any oracle query. We have

令 repeat 表示在 $\mathsf{Mac-sforge}_{\mathcal{A},\widetilde{\Pi}}(n)$ 中，同一个随机值 $r$ 被用于回答两个不同预言机查询的事件，并令 new-r 表示 $\mathcal{A}$ 输出 $(m, \langle r, s \rangle)$ 且 $r$ 未被用于回答任何预言机查询的事件。我们有

$$\begin{aligned}\Pr\left[\mathsf{Mac-sforge}_{\mathcal{A},\widetilde{\Pi}}(n)=1\right]\leq\Pr[\mathsf{repeat}]+\Pr\left[\mathsf{Mac-sforge}_{\mathcal{A},\widetilde{\Pi}}(n)=1\land\mathsf{new-r}\right]\\+\Pr\left[\mathsf{Mac-sforge}_{\mathcal{A},\widetilde{\Pi}}(n)=1\land\overline{\mathsf{repeat}}\land\overline{\mathsf{new-r}}\right].\end{aligned}$$

Bounding the first two terms of this sum is easy. Using Lemma A.15, we have $\Pr[\mathsf{repeat}] \leq q^2/2^{n+1}$. Next, observe that if $\mathcal{A}$ outputs $(m, \langle r, s \rangle)$ where $r$ was not used to answer any oracle query, then the value $f(r)$ is uniform in $\mathcal{T}_n$ and independent of $\mathcal{A}$'s view, and so the probability that $\langle r, s \rangle$ is a valid tag for $m$ (i.e., the probability that $s = h_{k_h}(m) + f(r)$) is ${1}/{|\mathcal{T}_n|} \leq \varepsilon(n)$. It follows that $\Pr[\mathsf{Mac-sforge}_{\mathcal{A},\widetilde{\Pi}}(n) = 1 \land \mathsf{new-r}] \leq \varepsilon(n)$.

对该和式的前两项进行界定是容易的。利用引理 A.15，我们有 $\Pr[\mathsf{repeat}] \leq q^2/2^{n+1}$。接下来，观察到如果 $\mathcal{A}$ 输出 $(m, \langle r, s \rangle)$ 且 $r$ 未被用于回答任何预言机查询，那么值 $f(r)$ 在 $\mathcal{T}_n$ 中均匀分布且独立于 $\mathcal{A}$ 的视图，因此 $\langle r, s \rangle$ 是 $m$ 的有效标签的概率（即 $s = h_{k_h}(m) + f(r)$ 的概率）为 ${1}/{|\mathcal{T}_n|} \leq \varepsilon(n)$。由此可得 $\Pr[\mathsf{Mac-sforge}_{\mathcal{A},\widetilde{\Pi}}(n) = 1 \land \mathsf{new-r}] \leq \varepsilon(n)$。

To complete the proof, we show that

为完成证明，我们证明

$$\Pr\left[\mathsf{Mac-sforge}_{\mathcal{A},\widetilde{\Pi}}(n)=1\land\overline{\mathsf{repeat}}\land\overline{\mathsf{new-r}}\right]\leq\varepsilon(n).$$

Here we rely on the fact that $h$ is $\varepsilon$-difference universal. Consider an execution of experiment Mac-sforge in which neither repeat nor new-r occurs. Let $m_1, \ldots, m_q$ be the messages queried by $\mathcal{A}$ to its oracle, let $\langle r_1, s_1 \rangle, \ldots, \langle r_q, s_q \rangle$ be the responses, and let $(m, \langle r, s \rangle)$ be the final output of $\mathcal{A}$. Since repeat did not occur the $\{r_i\}$ are distinct; since new-r did not occur we therefore have $r = r_i$ for some unique $i$. Moreover, we may assume $m \neq m_i$ as otherwise there is no way $\mathcal{A}$'s output can be a valid forgery.

这里我们依赖于 $h$ 是 $\varepsilon$-差分通用的事实。考虑一次 Mac-sforge 实验的执行，其中 repeat 和 new-r 都未发生。令 $m_1, \ldots, m_q$ 是 $\mathcal{A}$ 向其预言机查询的消息，令 $\langle r_1, s_1 \rangle, \ldots, \langle r_q, s_q \rangle$ 为响应，并令 $(m, \langle r, s \rangle)$ 为 $\mathcal{A}$ 的最终输出。由于 repeat 未发生，$\{r_i\}$ 互不相同；由于 new-r 未发生，因此存在唯一的 $i$ 使得 $r = r_i$。此外，我们可以假设 $m \neq m_i$，否则 $\mathcal{A}$ 的输出不可能是一个有效伪造。

The crucial observations are:

关键的观察是：

1. Since the $\{r_i\}$ are all distinct, the values $\{f(r_i)\}$ are all uniform and independent. Those values thus serve to perfectly hide any information about $k_h$ from $\mathcal{A}$ (by analogy with the one-time pad). Formally, this means that $k_h$ is independent of $A$'s view in experiment $\mathsf{Mac-sforge}_{\mathcal{A},\widetilde{\Pi}}(n)$.

   由于 $\{r_i\}$ 互不相同，值 $\{f(r_i)\}$ 都是均匀且独立的。因此这些值能够向 $\mathcal{A}$ 完美隐藏关于 $k_h$ 的任何信息（类似于一次一密）。形式化地，这意味着在实验 $\mathsf{Mac-sforge}_{\mathcal{A},\widetilde{\Pi}}(n)$ 中，$k_h$ 独立于 $A$ 的视图。

2. A's output is a valid forgery if and only if $h_{k_h}(m) - h_{k_h}(m_i) = s - s_i$.

   A 的输出是一个有效伪造当且仅当 $h_{k_h}(m) - h_{k_h}(m_i) = s - s_i$。

Letting $\Delta = s - s_i$, the above imply that

令 $\Delta = s - s_i$，上述事实意味着

$$\begin{aligned}\Pr\left[\mathsf{Mac-sforge}_{\mathcal{A},\widetilde{\Pi}}(n)=1\land\overline{\mathsf{repeat}}\land\overline{\mathsf{new-r}}\right]&\leq\Pr_{k\leftarrow\mathcal{K}_{n}}[h_{k_{h}}(m)-h_{k_{h}}(m_{i})=\Delta]\\&\leq\varepsilon(n).\end{aligned}$$

Putting everything together, we conclude that

综合以上所有结果，我们得出结论

$$\begin{array}{r}{\Pr\left[\mathsf{Mac-sforge}_{\mathcal{A},\widetilde{\Pi}}(n)=1\right]\leq2\cdot\varepsilon(n)+\frac{q^{2}}{2^{n+1}},}\end{array}$$

completing the proof.

证明完成。

Nonce-based MACs. The only property of r used in the proof above is that r is unique across all tags (i.e., that repeat not occur). Thus, one can also prove security for Construction 4.15 in a nonce-based setting similar to what was formalized (for private-key encryption) in Section 3.6.4.

基于 nonce 的 MAC。上述证明中用到的 r 的唯一性质是它在所有标签中唯一（即 repeat 不发生）。因此，也可以在类似于 3.6.4 节中（为私钥加密）形式化的基于 nonce 的设置中证明构造 4.15 的安全性。

### 4.5.2 Instantiations　4.5.2 实例化

There is a clever and efficient way to instantiate the difference-universal function required by Construction 4.15 using polynomials over a finite field. (The reader unfamiliar with finite fields may consult Section A.5. The only results we require are that a finite field $\mathbb{F}_q$ containing $q$ elements exists for any prime power $q$, and that a nonzero polynomial of degree $\ell$ over a finite field has at most $\ell$ roots.) Different realizations of that approach are, in turn, used by the standardized schemes GMAC and Poly1305.

有一种巧妙且高效的方式，利用有限域上的多项式来实例化构造 4.15 所需的差分通用函数。（不熟悉有限域的读者可以参考 A.5 节。我们只需要两个结论：对于任何素幂 $q$，存在包含 $q$ 个元素的有限域 $\mathbb{F}_q$；有限域上的非零 $\ell$ 次多项式最多有 $\ell$ 个根。）该方法的不同具体实现分别被标准化方案 GMAC 和 Poly1305 所采用。

For simplicity of exposition in this section (and because it matches current standards) we omit the security parameter and focus on a concrete setting.

为简化本节的论述（并且因为这符合当前标准），我们省略安全参数，专注于具体设定。

**An $\varepsilon$-difference-universal function.**

Fix a finite field $\mathbb{F}$. The idea is to let the key $k \in \mathcal{K}$ be a point in $\mathbb{F}$ and to view $m \in \mathcal{M}$ as a polynomial (of bounded degree) over $\mathbb{F}$; evaluating $h_k(m)$ then corresponds to evaluating $m$ at the point $k$.

一个 $\varepsilon$-差分通用函数。固定一个有限域 $\mathbb{F}$。其思想是让密钥 $k \in \mathcal{K}$ 是 $\mathbb{F}$ 中的一个点，并将 $m \in \mathcal{M}$ 视为 $\mathbb{F}$ 上的一个（有界次数的）多项式；那么计算 $h_k(m)$ 就相当于在点 $k$ 处求 $m$ 的值。

Formally, fix a constant $\ell$ and let $\mathcal{M} = \mathbb{F}^{<\ell}$, i.e., $\mathcal{M}$ consists of vectors over $\mathbb{F}$ containing fewer than $\ell$ entries. For any $m = (m_1, \ldots, m_{\ell^{\prime}-1}) \in \mathcal{M}$, where $\ell^{\prime} \leq \ell$, let $m_{\ell^{\prime}} \in \mathbb{F}$ be an encoding of the length of $m$ (i.e., $\ell^{\prime} - 1$), and define the polynomial

形式化地，固定一个常数 $\ell$，令 $\mathcal{M} = \mathbb{F}^{<\ell}$，即 $\mathcal{M}$ 由少于 $\ell$ 个分量的 $\mathbb{F}$ 上的向量组成。对于任意 $m = (m_1, \ldots, m_{\ell^{\prime}-1}) \in \mathcal{M}$，其中 $\ell^{\prime} \leq \ell$，令 $m_{\ell^{\prime}} \in \mathbb{F}$ 是 $m$ 的长度（即 $\ell^{\prime} - 1$）的编码，并定义多项式

$$m(X)\stackrel{\mathrm{def}}{=}m_{1}\cdot X^{\ell^{\prime}}+m_{2}\cdot X^{\ell^{\prime}-1}+\cdots+m_{\ell^{\prime}}\cdot X.$$

Finally, define the keyed function $h: \mathbb{F} \times \mathbb{F}^{<\ell} \to \mathbb{F}$ as

最后，定义带密钥的函数 $h: \mathbb{F} \times \mathbb{F}^{<\ell} \to \mathbb{F}$ 为

$$h_{k}(m)=m(k).$$

THEOREM 4.17 The function $h$ above is $\ell/|\mathbb{F}|$-difference universal.

定理 4.17 上述函数 $h$ 是 $\ell/|\mathbb{F}|$-差分通用的。

PROOF Fix distinct $m, m^{\prime} \in \mathbb{F}^{<\ell}$ and $\Delta \in \mathbb{F}$. Define the polynomial

证明 固定不同的 $m, m^{\prime} \in \mathbb{F}^{<\ell}$ 和 $\Delta \in \mathbb{F}$。定义多项式

$$P(X)\stackrel{\mathrm{def}}{=}m(X)-m^{\prime}(X)-\Delta.$$

P is a nonzero polynomial of degree at most $\ell$. (If the lengths of $m$ and $m^{\prime}$ are equal then that fact that P is nonzero is immediate; otherwise, $m(X)$ and $m^{\prime}(X)$ differ in their coefficients of the linear term.) So

P 是一个次数不超过 $\ell$ 的非零多项式。（如果 $m$ 和 $m^{\prime}$ 的长度相等，则 P 非零是显然的；否则，$m(X)$ 和 $m^{\prime}(X)$ 在线性项的系数上不同。）因此

$$\Pr_{k\in\mathbb{F}}[h_{k}(m)-h_{k}(m^{\prime})=\Delta]=\Pr_{k\in\mathbb{F}}[P(k)=0]\leq\ell/|\mathbb{F}|,$$

where the final inequality is because $P$ has at most $\ell$ roots.

其中最后一个不等式是因为 $P$ 最多有 $\ell$ 个根。

Efficiency. The function h is extremely efficient in several respects. First, the key can be much shorter than the input. Second h can be evaluated quickly using Horner's rule. That is, to evaluate

效率。函数 h 在多个方面非常高效。首先，密钥可以比输入短得多。其次，可以使用 Horner 规则快速计算 h。即，为计算

$$m_{1}\cdot k^{\ell^{\prime}}+\cdots+m_{\ell^{\prime}}\cdot k$$

set $y_0 := 0$ and then, for $i = 1$ to $\ell^{\prime},$ set $y_i := (y_{i-1} + m_i) \cdot k$; output $y_{\ell^{\prime}}$. This requires only $\ell^{\prime} \leq \ell$ field multiplications and $O(1)$ memory, even if entries of $m$ arrive in a streaming fashion and the length of $m$ is not known in advance.

设 $y_0 := 0$，然后对 $i = 1$ 到 $\ell^{\prime}$，计算 $y_i := (y_{i-1} + m_i) \cdot k$；输出 $y_{\ell^{\prime}}$。这仅需要 $\ell^{\prime} \leq \ell$ 次域乘法和 $O(1)$ 内存，即使 $m$ 的条目以流式方式到达且 $m$ 的长度事先未知。

GMAC. The GMAC message authentication code is just $^{3}$ Construction 4.15 using a block cipher $F$ with a 128-bit block length and the polynomial-based difference-universal function just described over the field $\mathbb{F} = \mathbb{F}_{2^{128}}$ with ${2}^{128}$ elements. Field elements are 128-bit strings; addition corresponds to bit-wise XOR, and multiplication can be done very efficiently using hardware-level instructions available in many modern processors.

GMAC。GMAC 消息认证码正是 $^{3}$ 构造 4.15，它使用分组长度为 128 比特的分组密码 $F$ 以及刚刚描述的、基于有限域 $\mathbb{F} = \mathbb{F}_{2^{128}}$（有 ${2}^{128}$ 个元素）的多项式差分通用函数。域元素是 128 比特串；加法对应按位 XOR，乘法可以利用许多现代处理器中可用的硬件级指令非常高效地完成。

$^{3}$ The GMAC standard does not correspond exactly to the construction described here; in particular, it supports messages whose length is not a multiple of 128.

$^{3}$ GMAC 标准与这里描述的构造并不完全对应；特别地，它支持长度不是 128 的倍数的消息。

Poly1305. The Poly1305 message authentication code is $^{4}$ defined similarly, but uses the field $\mathbb{F} = \mathbb{F}_p = \{0, \ldots, p-1\}$ where the prime $p = 2^{130} - 5$ was chosen for efficient implementation. Field operations here correspond to addition and multiplication modulo $p$. Observe that now there is a mismatch between the output of $F$ (which is a 128-bit string) and the output of $h$ (which lies in the range $\{0, \ldots, p-1\}$); to address this, the final tag is computed as

Poly1305。Poly1305 消息认证码 $^{4}$ 的定义类似，但使用域 $\mathbb{F} = \mathbb{F}_p = \{0, \ldots, p-1\}$，其中素数 $p = 2^{130} - 5$ 是为高效实现而选择的。这里的域运算对应于模 $p$ 的加法和乘法。观察到 $F$ 的输出（128 比特串）与 $h$ 的输出（位于范围 $\{0, \ldots, p-1\}$）之间存在不匹配；为解决这个问题，最终的标签计算为

$$\left\langle r,[h_{k_{h}}(m)+F_{k_{F}}(r)\bmod2^{128}]\right\rangle.$$

This small difference from Construction 4.15 can be accounted for in the security proof.

这个与构造 4.15 的微小差异可以在安全性证明中得到说明。

$^{4}$ Again, we are omitting some details from the actual standard.

$^{4}$ 同样，我们再次省略了实际标准中的一些细节。

**Comparison to CBC-MAC.**

Besides the fact that MACs based on Construction 4.15 can be more efficient than CBC-MAC, such MACs can also obtain a better concrete-security bound. Specifically, consider a setting in which $q$ messages, each of length $\ell$, are authenticated, and treat the block cipher $F$ as a random function. The proof of security for CBC-MAC given in Section 4.4.2 guarantees that an attacker's probability of outputting a valid forgery is at most $q^2 \cdot \ell^2/2^n$, though this can be improved to $\mathcal{O}(q^2 \cdot \ell/2^n)$ for small $\ell$. In contrast, the security bounds obtained for the MACs described in this section show that an attacker's forgery probability is $\mathcal{O}((q^2 + \ell)/2^n)$, a significant improvement. Concretely, take $n = 128$, $q = 2^{40}$, and $\ell = 2^{20}$. CBC-MAC gives a security bound of approximately ${2}^{-8}$, whereas GMAC and Poly1305 have security bounds of approximately ${2}^{-48}$. The latter can be further improved in the nonce-based setting.

与 CBC-MAC 的比较。除了基于构造 4.15 的 MAC 可以比 CBC-MAC 更高效之外，这类 MAC 还可以获得更好的具体安全性界（concrete-security bound）。具体来说，考虑一个场景，其中 $q$ 条消息（每条长度为 $\ell$）被认证，并将分组密码 $F$ 视为随机函数。4.4.2 节中给出的 CBC-MAC 安全性证明保证攻击者输出有效伪造的概率最多为 $q^2 \cdot \ell^2/2^n$，尽管对于较小的 $\ell$，这可以改善为 $\mathcal{O}(q^2 \cdot \ell/2^n)$。相比之下，本节描述的 MAC 获得的安全性界表明攻击者的伪造概率为 $\mathcal{O}((q^2 + \ell)/2^n)$，这是一个显著的改进。具体地说，取 $n = 128$，$q = 2^{40}$，$\ell = 2^{20}$。CBC-MAC 的安全性界大约为 ${2}^{-8}$，而 GMAC 和 Poly1305 的安全性界大约为 ${2}^{-48}$。后者在基于 nonce 的设置中可以进一步改进。

We remark further that in all cases the actual concrete-security bound includes a term that depends on an adversary's advantage in distinguishing the block cipher from a pseudorandom function. This term grows larger as the number of block-cipher evaluations increases. MACs based on Construction 4.15 have the advantage here as well in that they only evaluate the block cipher $q$ times, as opposed to $q \cdot \ell$ times for CBC-MAC.

我们进一步指出，在所有情况下，实际的具体安全性界都包含一项，该项取决于敌手在区分分组密码与伪随机函数上的优势。该项随着分组密码评估次数的增加而增大。基于构造 4.15 的 MAC 在这方面也有优势，因为它们仅评估 $q$ 次分组密码，而 CBC-MAC 需要 $q \cdot \ell$ 次。

## 4.6 \*Information-Theoretic MACs　4.6 \*信息论 MAC

Until now we have explored message authentication codes with computational security, i.e., where we assume bounds on the attacker's running time. But inspired by the results of Chapter 2, it is natural to ask whether message authentication in the presence of an unbounded adversary is possible. In this section, we show conditions under which information-theoretic (as opposed to computational) security is attainable.

到目前为止，我们探讨的是具有计算安全性的消息认证码，即我们假设攻击者的运行时间有界。但受到第 2 章结果的启发，自然会问：在存在无界敌手的情况下，消息认证是否可能？在本节中，我们展示信息论（而非计算）安全性可以实现的条件。

A first observation is that it is impossible to achieve "perfect" security in this context. Namely, we cannot hope to have a message authentication code for which the probability that an adversary outputs a valid tag on a previously unauthenticated message is 0. The reason is that an adversary can simply guess a valid tag $t$ on any message, and this guess will be correct with probability (at least) ${1}/{|\mathcal{T}|}$ (where $\mathcal{T}$ denotes the space of possible tags). Similarly, an attacker can always guess the key and generate a tag that is correct with probability ${1}/{|\mathcal{K}|}$ (where $\mathcal{K}$ denotes the space of possible keys).

第一个观察是，在这种语境下不可能达到“完美”安全性。也就是说，我们不能期望存在一个消息认证码，使得敌手在先前未认证的消息上输出有效标签的概率为 0。原因是敌手可以简单地猜测任何消息上的有效标签 $t$，该猜测正确的概率（至少）为 ${1}/{|\mathcal{T}|}$（其中 $\mathcal{T}$ 表示可能的标签空间）。类似地，攻击者总可以猜测密钥并以概率 ${1}/{|\mathcal{K}|}$（其中 $\mathcal{K}$ 表示可能的密钥空间）生成正确的标签。

The above examples tell us what we can hope to achieve: a MAC where the probability of forgery is at most $\max\{1/|\mathcal{T}|,1/|\mathcal{K}|\}$, even for unbounded adversaries. We will see that this is achievable, but only under restrictions on how many messages are authenticated by the honest parties.

上述例子告诉我们能够期望达到的目标：即使对于无界敌手，伪造概率最多为 $\max\{1/|\mathcal{T}|,1/|\mathcal{K}|\}$ 的 MAC。我们将看到这是可以实现的，但仅限于对诚实方认证的消息数量施加限制的情况。

We first define information-theoretic security for message authentication codes. A starting point is to take experiment $\mathsf{Mac-forge}_{\mathcal{A},\Pi}(n)$ that is used to computationally secure MACs (cf. Definition 4.2), but drop the security parameter $n$ and require simply that $\Pr[\mathrm{Mac-forge}_{\mathcal{A},\Pi}=1]$ be "small" for all adversaries $\mathcal{A}$ (and not just adversaries running in polynomial time). As mentioned above (and as will be proved formally in Section 4.6.3), however, such a definition is impossible to achieve unless we place some bound on the number of messages authenticated by the honest parties. We look here at the most basic setting, where the honest parties authenticate just a single message. We refer to this as one-time message authentication. The following experiment modifies $\mathrm{Mac-forge}_{\mathcal{A},\Pi}(n)$ following the above discussion:

我们首先为消息认证码定义信息论安全性。一个起点是采用用于计算安全 MAC 的实验 $\mathsf{Mac-forge}_{\mathcal{A},\Pi}(n)$（参见定义 4.2），但去掉安全参数 $n$，仅要求对所有敌手 $\mathcal{A}$（而不只是在多项式时间内运行的敌手）而言，$\Pr[\mathrm{Mac-forge}_{\mathcal{A},\Pi}=1]$ 是“小的”。然而，如上所述（并将在 4.6.3 节中正式证明），除非我们对诚实方认证的消息数量施加某种限制，否则这样的定义是不可能实现的。我们在这里考察最基本的设置，即诚实方仅认证一条消息。我们称之为**一次消息认证**（one-time message authentication）。以下实验根据上述讨论修改了 $\mathrm{Mac-forge}_{\mathcal{A},\Pi}(n)$：

The one-time message authentication experiment $\mathsf{Mac-forge}_{\mathcal{A},\Pi}^{1-time}$:

一次消息认证实验 $\mathsf{Mac-forge}_{\mathcal{A},\Pi}^{1-time}$：

1. A key k is generated by running Gen.

   通过运行 $\mathsf{Gen}$ 生成密钥 $k$。

2. The adversary $\mathcal{A}$ outputs a message $m^{\prime}$, and is given in return a tag $t^{\prime} \leftarrow \mathsf{Mac}_k(m^{\prime})$.

   敌手 $\mathcal{A}$ 输出一条消息 $m^{\prime}$，并得到返回的标签 $t^{\prime} \leftarrow \mathsf{Mac}_k(m^{\prime})$。

3. A outputs $(m, t)$.

   A 输出 $(m, t)$。

4. The output of the experiment is defined to be 1 if and only if $(1) \mathsf{Vrfy}_{k}(m, t) = 1$ and $(2) m \neq m^{\prime}$.

   实验的输出定义为 1 当且仅当 (1) $\mathsf{Vrfy}_{k}(m, t) = 1$ 且 (2) $m \neq m^{\prime}$。

DEFINITION 4.18 $\Pi = (\mathsf{Gen}, \mathsf{Mac}, \mathsf{Vrfy})$ is an $\varepsilon$-secure one-time MAC if for all (even unbounded) adversaries $\mathcal{A}$:

定义 4.18 $\Pi = (\mathsf{Gen}, \mathsf{Mac}, \mathsf{Vrfy})$ 是一个 **$\varepsilon$-安全的一次 MAC**，如果对于所有（甚至无界的）敌手 $\mathcal{A}$：

$$\Pr\left[\mathsf{Mac-forge}_{\mathcal{A},\Pi}^{1-time}=1\right]\leq\varepsilon.$$

### 4.6.1 One-Time MACs from Strongly Universal Functions　4.6.1 基于强通用函数的一次 MAC

In this section we show how to construct a one-time MAC based on any strongly universal function. We then show a simple construction of the latter.

在本节中，我们展示如何基于任意**强通用函数**（strongly universal function）构造一次 MAC。然后给出后者的一个简单构造。

Let $h: \mathcal{K} \times \mathcal{M} \to \mathcal{T}$ be a keyed function whose first input is a key $k \in \mathcal{K}$ and whose second input is taken from some domain $\mathcal{M}$; the output is in some set $\mathcal{T}$. As usual, we write $h_k(m)$ instead of $h(k, m)$. Then $h$ is strongly universal (or pairwise independent) if for any two distinct inputs $m, m^{\prime}$ the values $h_k(m)$ and $h_k(m^{\prime})$ are uniformly and independently distributed in $\mathcal{T}$ when $k$ is a uniform key. This is equivalent to saying that the probability that $h_k(m), h_k(m^{\prime})$ take on any particular values $t, t^{\prime}$ is exactly ${1}/{|\mathcal{T}|^2}$. That is:

设 $h: \mathcal{K} \times \mathcal{M} \to \mathcal{T}$ 是一个带密钥的函数，其第一个输入是密钥 $k \in \mathcal{K}$，第二个输入取自某个域 $\mathcal{M}$；输出在某个集合 $\mathcal{T}$ 中。通常，我们写作 $h_k(m)$ 代替 $h(k, m)$。那么，$h$ 是**强通用**（strongly universal，或称**两两独立**，pairwise independent）的，如果对于任意两个不同的输入 $m, m^{\prime}$，当 $k$ 是均匀密钥时，值 $h_k(m)$ 和 $h_k(m^{\prime})$ 在 $\mathcal{T}$ 中均匀且独立分布。这等价于说 $h_k(m), h_k(m^{\prime})$ 取任何特定值 $t, t^{\prime}$ 的概率恰好是 ${1}/{|\mathcal{T}|^2}$。即：

DEFINITION 4.19 $A$ function $h: \mathcal{K} \times \mathcal{M} \to \mathcal{T}$ is strongly universal if for all distinct $m, m^{\prime} \in \mathcal{M}$ and all (not necessarily distinct) $t, t^{\prime} \in \mathcal{T}$ it holds that

定义 4.19 函数 $h: \mathcal{K} \times \mathcal{M} \to \mathcal{T}$ 是**强通用**的，如果对于所有不同的 $m, m^{\prime} \in \mathcal{M}$ 和所有（不一定不同的）$t, t^{\prime} \in \mathcal{T}$，有

$$\Pr\left[h_{k}(m)=t\wedge h_{k}(m^{\prime})=t^{\prime}\right]=\frac{1}{|\mathcal{T}|^{2}},$$

where the probability is taken over uniform choice of $k \in \mathcal{K}$.

其中概率取自 $k \in \mathcal{K}$ 的均匀选择。

The above should motivate the construction of a one-time message authentication code from any strongly universal function $h$. The tag t on a message m is obtained by computing $h_k(m)$, where the key k is uniform; see Construction 4.20. Intuitively, even after an adversary observes the tag $t^{\prime} = h_k(m^{\prime})$ for any message $m^{\prime}$, the correct tag $h_k(m)$ for any other message m is still uniformly distributed in $\mathcal{T}$ from the adversary's point of view. Thus, the adversary can do nothing more than blindly guess the tag, and this guess will be correct only with probability ${1}/{|\mathcal{T}|}$.

上述讨论应该能够启发如何从任意强通用函数 $h$ 构造一次消息认证码。消息 $m$ 上的标签 $t$ 通过计算 $h_k(m)$ 得到，其中密钥 $k$ 是均匀的；见构造 4.20。直观上，即使敌手观察到任何消息 $m^{\prime}$ 的标签 $t^{\prime} = h_k(m^{\prime})$，从敌手的角度来看，任何其他消息 m 的正确标签 $h_k(m)$ 仍然在 $\mathcal{T}$ 中均匀分布。因此，敌手只能盲目猜测标签，且该猜测正确的概率仅为 ${1}/{|\mathcal{T}|}$。

> **CONSTRUCTION 4.20**　**构造 4.20**
>
> Let $h: \mathcal{K} \times \mathcal{M} \to \mathcal{T}$ be a strongly universal function. Define a MAC for messages in $\mathcal{M}$ as follows:
> Gen: choose uniform $k \in \mathcal{K}$ and output it as the key.
> - Mac: on input a key $k \in \mathcal{K}$ and a message $m \in \mathcal{M}$, output the tag $t := h_k(m)$.
> - $\mathsf{Vrfy}$: on input a key $k \in \mathcal{K}$, a message $m \in \mathcal{M}$, and a tag $t \in \mathcal{T}$, output 1 if and only if $t \overset{?}{=} h_k(m)$. (If $m \notin \mathcal{M}$, then output 0.)
>
> 设 $h: \mathcal{K} \times \mathcal{M} \to \mathcal{T}$ 是一个强通用函数。为 $\mathcal{M}$ 中的消息定义 MAC 如下：
> Gen：选择均匀的 $k \in \mathcal{K}$ 并将其作为密钥输出。
> - Mac：输入密钥 $k \in \mathcal{K}$ 和消息 $m \in \mathcal{M}$，输出标签 $t := h_k(m)$。
> - $\mathsf{Vrfy}$：输入密钥 $k \in \mathcal{K}$、消息 $m \in \mathcal{M}$ 和标签 $t \in \mathcal{T}$，当且仅当 $t \overset{?}{=} h_k(m)$ 时输出 1。（如果 $m \notin \mathcal{M}$，则输出 0。）
>
> A one-time MAC from any strongly universal function.
> 基于任意强通用函数的一次 MAC。

The above construction can be viewed as analogous to Construction 4.5. This is because a strongly universal function $h$ behaves like a random function as long as it is evaluated at most twice.

上述构造可以看作类似于构造 4.5。这是因为强通用函数 $h$ 在被评估最多两次时表现得像一个随机函数。

THEOREM 4.21 Let $h : \mathcal{K} \times \mathcal{M} \to \mathcal{T}$ be a strongly universal function. Then Construction 4.20 is a ${1}/{|\mathcal{T}|}$-secure one-time MAC for messages in $\mathcal{M}$.

定理 4.21 设 $h : \mathcal{K} \times \mathcal{M} \to \mathcal{T}$ 是一个强通用函数。那么构造 4.20 对于 $\mathcal{M}$ 中的消息是一个 ${1}/{|\mathcal{T}|}$-安全的一次 MAC。

PROOF Let $\mathcal{A}$ be an adversary and let $\Pi$ denote Construction 4.20. Since $\mathcal{A}$ may be all-powerful, we may assume $\mathcal{A}$ is deterministic. So the message $m^{\prime}$ on which $\mathcal{A}$ requests a tag at the outset of the experiment is fixed. Furthermore, the pair $(m,t)$ that $\mathcal{A}$ outputs at the end of the experiment is a deterministic function of the tag $t^{\prime}$ on $m^{\prime}$ that $\mathcal{A}$ receives. We thus have

证明 设 $\mathcal{A}$ 是一个敌手，$\Pi$ 表示构造 4.20。由于 $\mathcal{A}$ 可能是全能的，我们可以假设 $\mathcal{A}$ 是确定性的。因此 $\mathcal{A}$ 在实验开始时请求标签的消息 $m^{\prime}$ 是固定的。此外，$\mathcal{A}$ 在实验结束时输出的数对 $(m,t)$ 是它收到的 $m^{\prime}$ 上标签 $t^{\prime}$ 的一个确定性函数。因此我们有

$$\begin{aligned}\Pr\left[\mathsf{Mac-forge}_{\mathcal{A},\Pi}^{1-time}=1\right]&=\sum_{t^{\prime}\in\mathcal{T}}\Pr\left[\mathsf{Mac-forge}_{\mathcal{A},\Pi}^{1-time}=1~\land~h_{k}(m^{\prime})=t^{\prime}\right]\\&=\sum_{\substack{t^{\prime}\in\mathcal{T}\\ (m,t):=\mathcal{A}(t^{\prime})}}\Pr\left[h_{k}(m)=t~\land~h_{k}(m^{\prime})=t^{\prime}\right]\\&=\sum_{\substack{t^{\prime}\in\mathcal{T}\\ (m,t):=\mathcal{A}(t^{\prime})}}\frac{1}{|\mathcal{T}|^{2}}~=~\frac{1}{|\mathcal{T}|}.\\ \end{aligned}$$

This proves the theorem.

这就证明了该定理。

It remains to construct a strongly universal function. We assume some basic knowledge about arithmetic modulo a prime number; readers may refer to Sections 9.1.1 and 9.1.2 for necessary background. (Alternatively, everything we say generalizes to an arbitrary finite field, and the interested reader may consult Section A.5.) Fix a prime $p$, and let $\mathbb{Z}_p \overset{\mathrm{def}}{=}\{0,\ldots,p-1\}$. We take as our message space $\mathcal{M}=\mathbb{Z}_p$; the space of possible tags will be $\mathcal{T}=\mathbb{Z}_p$. A key $(a,b)$ consists of a pair of elements from $\mathbb{Z}_p$; thus, $\mathcal{K}=\mathbb{Z}_p\times\mathbb{Z}_p$. Define $h$ as

接下来需要构造一个强通用函数。我们假设读者具备关于素数模算术的基本知识；读者可以参考 9.1.1 和 9.1.2 节了解必要的背景知识。（或者，我们说的所有内容都可以推广到任意有限域，感兴趣的读者可以参考 A.5 节。）固定一个素数 $p$，令 $\mathbb{Z}_p \overset{\mathrm{def}}{=}\{0,\ldots,p-1\}$。我们取消息空间为 $\mathcal{M}=\mathbb{Z}_p$；可能的标签空间为 $\mathcal{T}=\mathbb{Z}_p$。密钥 $(a,b)$ 由 $\mathbb{Z}_p$ 中的一对元素组成；因此 $\mathcal{K}=\mathbb{Z}_p\times\mathbb{Z}_p$。定义 $h$ 为

$$h_{a,b}(m)\stackrel{\mathrm{def}}{=}[a\cdot m+b\bmod p],$$

where the notation [X mod p] refers to the result of reducing X modulo p.

其中记号 [X mod p] 表示将 X 模 p 约化的结果。

THEOREM 4.22 For any prime p, the function h defined above is strongly universal.

定理 4.22 对于任何素数 p，上述定义的函数 h 是强通用的。

PROOF Fix any distinct $m, m^{\prime} \in \mathbb{Z}_p$ and any $t, t^{\prime} \in \mathbb{Z}_p$. For which keys $(a, b)$ does it hold that both $h_{a,b}(m) = t$ and $h_{a,b}(m^{\prime}) = t^{\prime}$? This holds only if

证明 固定任意不同的 $m, m^{\prime} \in \mathbb{Z}_p$ 和任意 $t, t^{\prime} \in \mathbb{Z}_p$。对于哪些密钥 $(a, b)$ 同时满足 $h_{a,b}(m) = t$ 和 $h_{a,b}(m^{\prime}) = t^{\prime}$？这只在以下条件下才成立：

$$a\cdot m+b=t\bmod p\quad \text{and} \quad a\cdot m^{\prime}+b=t^{\prime}\bmod p.$$

We thus have two linear equations in the two unknowns $a,b$. These two equations are both satisfied exactly when $a = [(t - t^{\prime}) \cdot (m - m^{\prime})^{-1} \mod p]$ and $b = [t - a \cdot m \mod p]$; note that $[(m - m^{\prime})^{-1} \mod p]$ exists because $m \neq m^{\prime}$ and so $m - m^{\prime} \neq 0 \mod p$. Restated, this means that for any $m,m^{\prime},t,t^{\prime}$ as above there is a unique key $(a,b)$ with $h_{a,b}(m) = t$ and $h_{a,b}(m^{\prime}) = t^{\prime}$. We conclude that the probability (over uniform choice of the key) that $h_{a,b}(m) = t$ and $h_{a,b}(m^{\prime}) = t^{\prime}$ is exactly ${1}/{|\mathcal{K}|} = 1/|\mathcal{T}|^2$ as required.

因此我们有两个关于两个未知数 $a,b$ 的线性方程。这两个方程同时成立当且仅当 $a = [(t - t^{\prime}) \cdot (m - m^{\prime})^{-1} \mod p]$ 且 $b = [t - a \cdot m \mod p]$；注意 $[(m - m^{\prime})^{-1} \mod p]$ 存在是因为 $m \neq m^{\prime}$，进而 $m - m^{\prime} \neq 0 \mod p$。换句话说，这意味着对于任何如上所述的 $m,m^{\prime},t,t^{\prime}$，存在唯一的密钥 $(a,b)$ 满足 $h_{a,b}(m) = t$ 和 $h_{a,b}(m^{\prime}) = t^{\prime}$。我们得出结论：$h_{a,b}(m) = t$ 和 $h_{a,b}(m^{\prime}) = t^{\prime}$ 的概率（对密钥的均匀选择）恰好是 ${1}/{|\mathcal{K}|} = 1/|\mathcal{T}|^2$，如所要求的那样。

Parameters of Construction 4.20. We briefly discuss the parameters of Construction 4.20 when instantiated with the strongly universal function described above. The construction is a ${1}/{|\mathcal{T}|}$-secure one-time MAC, so is optimal as far as the level of security achieved vs. the number of tags.

构造 4.20 的参数。我们简要讨论用上述强通用函数实例化时构造 4.20 的参数。该构造是一个 ${1}/{|\mathcal{T}|}$-安全的一次 MAC，因此在所达到的安全级别与标签数量方面是最优的。

Let $\mathcal{M} = \mathbb{Z}_p$ be some message space for which we want to construct a one-time MAC. Construction 4.20 gives a ${1}/{|\mathcal{M}|}$-secure one-time MAC with keys that are (roughly) twice the message length. The reader may notice two problems here, at opposite ends of the spectrum: First, if $|\mathcal{M}|$ is small then a ${1}/{|\mathcal{M}|}$ probability of forgery may be unacceptably large. On the flip side, if $|\mathcal{M}|$ is large then a ${1}/{|\mathcal{M}|}$ probability of forgery may be overkill; one might be willing to accept a (somewhat) larger probability of forgery if that level of security can be achieved with shorter tags. The first problem (when $|\mathcal{M}|$ is small) is easy to deal with by simply embedding $\mathcal{M}$ into a larger message space $\mathcal{M}^{\prime}$ by, e.g., padding messages with 0s. The second problem can be addressed as well by using Construction 4.20 and then truncating the tag. We omit details, and refer instead to the references at the end of this chapter.

设 $\mathcal{M} = \mathbb{Z}_p$ 是我们要为其构造一次 MAC 的消息空间。构造 4.20 给出了一个 ${1}/{|\mathcal{M}|}$-安全的一次 MAC，其密钥（大约）是消息长度的两倍。读者可能会注意到两个极端的问题：首先，如果 $|\mathcal{M}|$ 很小，那么 ${1}/{|\mathcal{M}|}$ 的伪造概率可能大到不可接受。另一方面，如果 $|\mathcal{M}|$ 很大，那么 ${1}/{|\mathcal{M}|}$ 的伪造概率可能过于严格；如果可以用更短的标签实现某种安全级别，人们可能愿意容忍（稍微）更大的伪造概率。第一个问题（当 $|\mathcal{M}|$ 很小时）很容易解决，只需将 $\mathcal{M}$ 嵌入到更大的消息空间 $\mathcal{M}^{\prime}$ 中，例如通过在消息后填充 0。第二个问题也可以通过使用构造 4.20 然后截断标签来解决。我们省略细节，而是参考本章末尾的参考文献。

### 4.6.2 One-Time MACs from Difference-Universal Functions　4.6.2 基于差分通用函数的一次 MAC

Here we explore a second construction of one-time MACs. In contrast to the construction given in the previous section, this approach can have shorter keys and better computational efficiency. Perhaps more importantly, it can be adapted to give a computationally secure scheme (for authenticating polynomially many messages), as shown in Section 4.5.

这里我们探索一次 MAC 的第二种构造。与前节给出的构造相比，这种方法可以有更短的密钥和更好的计算效率。也许更重要的是，它可以经过调整而得到一个计算安全的方案（用于认证多项式多条消息），如 4.5 节所示。

We begin by defining a difference-universal function. (In contrast to Definition 4.14, here we give a concrete version of the definition.) We assume familiarity with the notion of a group (cf. Section 9.1), but in this section nothing beyond the definition of a group is needed.

我们首先定义差分通用函数。（与定义 4.14 不同，这里我们给出该定义的具体版本。）我们假设读者熟悉群的概念（参见 9.1 节），但在本节中不需要任何超出群定义的知识。

DEFINITION 4.23 Let $\mathcal{T}$ be a group. $A$ function $h: \mathcal{K} \times \mathcal{M} \to \mathcal{T}$ is $\varepsilon$-difference universal if for all distinct $m, m^{\prime} \in \mathcal{M}$ and all $\Delta \in \mathcal{T}$ it holds that

定义 4.23 设 $\mathcal{T}$ 是一个群。函数 $h: \mathcal{K} \times \mathcal{M} \to \mathcal{T}$ 是 **$\varepsilon$-差分通用**的，如果对于所有不同的 $m, m^{\prime} \in \mathcal{M}$ 和所有 $\Delta \in \mathcal{T}$，有

$$\Pr\left[h_{k}(m)-h_{k}(m^{\prime})=\Delta\right]\leq\varepsilon,$$

where the probability is taken over uniform choice of $k \in \mathcal{K}$.

其中概率取自 $k \in \mathcal{K}$ 的均匀选择。

Being difference universal is weaker than being strongly universal; in particular, any $h : \mathcal{K} \times \mathcal{M} \to \mathcal{T}$ that is strongly universal is also ${1}/{|\mathcal{T}|}$-difference universal, but the converse is not true. To see this, fix a prime $p$, let $\mathcal{K} = \mathcal{M} = \mathcal{T} = \mathbb{Z}_p$, and define $h$ as

差分通用比强通用更弱；特别地，任何强通用的 $h : \mathcal{K} \times \mathcal{M} \to \mathcal{T}$ 也是 ${1}/{|\mathcal{T}|}$-差分通用的，但反之不成立。为了说明这一点，固定一个素数 $p$，设 $\mathcal{K} = \mathcal{M} = \mathcal{T} = \mathbb{Z}_p$，并定义 $h$ 为

$$h_{k}(m)=[k\cdot m\bmod p].$$

It is easy to see that $h$ is not strongly universal (since $h_{k}(0) = 0$ for all $k$), but for any distinct $m, m^{\prime}$ and any $\Delta$ we have

很容易看出 $h$ 不是强通用的（因为对所有 $k$ 有 $h_{k}(0) = 0$），但对于任何不同的 $m, m^{\prime}$ 和任何 $\Delta$，我们有

$$\begin{align*}\Pr[h_{k}(m)-h_{k}(m^{\prime})=\Delta]&=\Pr[k\cdot(m-m^{\prime})=\Delta\bmod p]\\&=\Pr[k=\Delta\cdot(m-m^{\prime})^{-1}\bmod p]=1/p,\end{align*}$$

showing that $h$ is ${1}/{|\mathcal{T}|}$-difference universal. (In Section 4.5 we show a construction of an $\varepsilon$-difference-universal function with $|\mathcal{K}| \ll |\mathcal{M}|.)$

这表明 $h$ 是 ${1}/{|\mathcal{T}|}$-差分通用的。（在 4.5 节中，我们展示了一个 $\varepsilon$-差分通用函数的构造，其中 $|\mathcal{K}| \ll |\mathcal{M}|$。）

Construction 4.24 shows how a difference-universal function $h: \mathcal{K} \times \mathcal{M} \to \mathcal{T}$ can be used to construct a one-time MAC. The shared key now consists of both a key $k \in \mathcal{K}$ for $h$ as well as a uniform $r \in \mathcal{T}$ that will be used as a one-time pad. To authenticate a message $m \in \mathcal{M}$, the sender first computes $h_k(m)$ and then "masks" that value using $r$. (Note the similarity to Construction 4.15, which uses a block cipher to generate masks for polynomially many messages.) As intuition for the security of this scheme, note that even after observing the tag $t^{\prime} = h_k(m^{\prime}) + r$ for a message $m^{\prime}$, an adversary learns nothing about $h_k(m^{\prime})$. Moreover, if the attacker outputs a tag $t$ on another message $m$, this is a successful forgery only if $t = h_k(m) + r$, i.e., if

构造 4.24 展示了如何使用差分通用函数 $h: \mathcal{K} \times \mathcal{M} \to \mathcal{T}$ 来构造一次 MAC。共享密钥现在由两部分组成：$h$ 的密钥 $k \in \mathcal{K}$ 以及用作一次一密的均匀值 $r \in \mathcal{T}$。为认证消息 $m \in \mathcal{M}$，发送方首先计算 $h_k(m)$，然后使用 $r$ “掩盖”该值。（注意这与构造 4.15 的相似性，后者使用分组密码为多项式多条消息生成掩盖值。）关于该方案安全性的直觉是，即使敌手观察到消息 $m^{\prime}$ 的标签 $t^{\prime} = h_k(m^{\prime}) + r$，也无法了解关于 $h_k(m^{\prime})$ 的任何信息。此外，如果攻击者在另一条消息 $m$ 上输出标签 $t$，这只有在 $t = h_k(m) + r$ 时才是成功的伪造，即

$$t-t^{\prime}=h_{k}(m)-h_{k}(m^{\prime}).$$

> **CONSTRUCTION 4.24**　**构造 4.24**
>
> Let $h : \mathcal{K} \times \mathcal{M} \to \mathcal{T}$ be a difference-universal function. Define a MAC for messages in $\mathcal{M}$ as follows:
>
> Gen: choose uniform $k \in \mathcal{K}$ and $r \in \mathcal{T}$; output the key $(k, r)$.
> Mac: on input a key $(k, r)$ and a message $m \in \mathcal{M}$, output the tag $t := h_k(m) + r$. (Addition here is done in the group $\mathcal{T}$.)
> - Vrfy: on input a key $(k, r)$, a message $m \in \mathcal{M}$, and a tag $t \in \mathcal{T}$, output 1 if and only if $t \overset{?}{=} h_k(m) + r$.
>
> 设 $h : \mathcal{K} \times \mathcal{M} \to \mathcal{T}$ 是一个差分通用函数。为 $\mathcal{M}$ 中的消息定义 MAC 如下：
>
> Gen：选择均匀的 $k \in \mathcal{K}$ 和 $r \in \mathcal{T}$；输出密钥 $(k, r)$。
> Mac：输入密钥 $(k, r)$ 和消息 $m \in \mathcal{M}$，输出标签 $t := h_k(m) + r$。（这里的加法在群 $\mathcal{T}$ 中进行。）
> - Vrfy：输入密钥 $(k, r)$、消息 $m \in \mathcal{M}$ 和标签 $t \in \mathcal{T}$，当且仅当 $t \overset{?}{=} h_k(m) + r$ 时输出 1。
>
> A one-time MAC from any difference-universal function.
> 基于任意差分通用函数的一次 MAC。

If $h$ is $\varepsilon$-difference universal then the probability of the above (taken over choice of $k$) is at most $\varepsilon$.

如果 $h$ 是 $\varepsilon$-差分通用的，那么上述概率（取自 $k$ 的均匀选择）最多为 $\varepsilon$。

THEOREM 4.25 Let h be an $\varepsilon$-difference-universal function. Then Construction 4.24 is an $\varepsilon$-secure one-time MAC for messages in M.

定理 4.25 设 h 是一个 $\varepsilon$-差分通用函数。那么构造 4.24 对于 M 中的消息是一个 $\varepsilon$-安全的一次 MAC。

PROOF Let $\Pi$ denote Construction 4.24. The proof is similar to that of Theorem 4.21. As in that proof, fix an adversary $\mathcal{A}$ and let $m^{\prime}$ be the message whose tag is requested by $\mathcal{A}$ at the outset of the experiment. The message/tag pair output by $\mathcal{A}$ is then a deterministic function of the tag $t^{\prime}$ on $m^{\prime}$. So

证明 设 $\Pi$ 表示构造 4.24。该证明与定理 4.21 的证明类似。如该证明一样，固定一个敌手 $\mathcal{A}$，并令 $m^{\prime}$ 为 $\mathcal{A}$ 在实验开始时请求标签的消息。$\mathcal{A}$ 输出的消息/标签对是 $m^{\prime}$ 上标签 $t^{\prime}$ 的一个确定性函数。因此

$$\Pr\left[\mathsf{Mac-forge}_{\mathcal{A},\Pi}^{1-\mathsf{time}}=1\right]=\sum_{\stackrel{t^{\prime}\in\mathcal{T}}{(m,t):=\mathcal{A}(t^{\prime})}}\Pr\left[h_{k}(m)+r=t\land h_{k}(m^{\prime})+r=t^{\prime}\right].$$

Now, for any $m \neq m^{\prime}$ and $t, t^{\prime}$ we have $h_k(m) + r = t$ and $h_k(m^{\prime}) + r = t^{\prime}$ if and only if $h_k(m) + r = t$ and $h_k(m) - h_k(m^{\prime}) = t - t^{\prime} \stackrel{\mathrm{def}}{=} \Delta$. Thus,

现在，对于任意 $m \neq m^{\prime}$ 和 $t, t^{\prime}$，$h_k(m) + r = t$ 且 $h_k(m^{\prime}) + r = t^{\prime}$ 当且仅当 $h_k(m) + r = t$ 且 $h_k(m) - h_k(m^{\prime}) = t - t^{\prime} \stackrel{\mathrm{def}}{=} \Delta$。因此，

$$\begin{aligned}&\Pr\Big[h_{k}(m)+r=t\land h_{k}(m^{\prime})+r=t^{\prime}\Big]\\&=\Pr\Big[h_{k}(m)+r=t\land h_{k}(m)-h_{k}(m^{\prime})=\Delta\Big]\\&=\Pr\Big[r=t-h_{k}(m)\mid h_{k}(m)-h_{k}(m^{\prime})=\Delta\Big]\cdot\Pr\Big[h_{k}(m)-h_{k}(m^{\prime})=\Delta\Big]\\&=\left(\frac{1}{|\mathcal{T}|}\right)\cdot\varepsilon,\end{aligned}$$

using the facts that $h$ is $\varepsilon$-difference universal and that $r$ is uniform and independent of $k$. The theorem follows.

这里利用了 $h$ 是 $\varepsilon$-差分通用的、以及 $r$ 均匀且独立于 $k$ 这两个事实。定理得证。

### 4.6.3 Limitations on Information-Theoretic MACs　4.6.3 信息论 MAC 的局限性

Here we explore limitations on information-theoretic message authentication, showing that any $\varepsilon$-secure one-time MAC must have keys of length at least ${1}/{\varepsilon^2}$. An extension of the proof shows that any $\varepsilon$-secure $\ell$-time MAC (where security is defined by modifying Definition 4.19 to allow the attacker to request tags on $\ell$ messages) requires keys of length at least ${1}/{\varepsilon^{(\ell+1)}}$. A corollary is that no MAC can provide information-theoretic security for authenticating an unbounded number of messages.

这里我们探讨信息论消息认证的局限性，证明任何 $\varepsilon$-安全的一次 MAC 必须具有长度至少为 ${1}/{\varepsilon^2}$ 的密钥。该证明的推广表明，任何 $\varepsilon$-安全的 $\ell$ 次 MAC（其中安全性通过修改定义 4.19 以允许攻击者请求 $\ell$ 条消息上的标签来定义）需要长度至少为 ${1}/{\varepsilon^{(\ell+1)}}$ 的密钥。一个推论是，没有 MAC 能为认证无限多条消息提供信息论安全性。

In the following, we assume the message space contains at least two messages; if not, there is no point in communicating, let alone authenticating.

在下文中，我们假设消息空间至少包含两条消息；否则通信没有意义，更不用说认证了。

THEOREM 4.26 Let $\Pi = (\mathsf{Gen}, \mathsf{Mac}, \mathsf{Vrfy})$ be an $\varepsilon$-secure one-time MAC with key space $\mathcal{K}$. Then $|\mathcal{K}| \geq \varepsilon^{-2}$.

定理 4.26 设 $\Pi = (\mathsf{Gen}, \mathsf{Mac}, \mathsf{Vrfy})$ 是一个具有密钥空间 $\mathcal{K}$ 的 $\varepsilon$-安全的一次 MAC。那么 $|\mathcal{K}| \geq \varepsilon^{-2}$。

PROOF Fix distinct messages $m_0, m_1$. The intuition is that there must be at least $\varepsilon^{-1}$ possibilities for the tag of $m_0$ (or else the adversary could guess it with probability better than $\varepsilon$); furthermore, even conditioned on the value of the tag for $m_0$, there must be $\varepsilon^{-1}$ possibilities for the tag of $m_1$ (or else the adversary could forge a tag on $m_1$ with probability better than $\varepsilon$). Since each key defines tags for $m_0$ and $m_1$, this means there must be at least $\varepsilon^{-1} \times \varepsilon^{-1} = \varepsilon^{-2}$ keys. We make this formal below.

证明 固定不同的消息 $m_0, m_1$。直观上看，$m_0$ 的标签必须至少有 $\varepsilon^{-1}$ 种可能（否则敌手可以以优于 $\varepsilon$ 的概率猜中它）；此外，即使以 $m_0$ 的标签值为条件，$m_1$ 的标签也必须至少有 $\varepsilon^{-1}$ 种可能（否则敌手可以以优于 $\varepsilon$ 的概率伪造 $m_1$ 上的标签）。由于每个密钥定义了 $m_0$ 和 $m_1$ 的标签，这意味着必须至少有 $\varepsilon^{-1} \times \varepsilon^{-1} = \varepsilon^{-2}$ 个密钥。我们下面将给出形式化证明。

Let $\mathcal{K}$ denote the key space (i.e., the set of all possible keys that can be output by Gen). For any possible tag $t_0$, let $\mathcal{K}(t_0)$ denote the set of keys for which $t_0$ is a valid tag on $m_0$; i.e.,

令 $\mathcal{K}$ 表示密钥空间（即 Gen 可能输出的所有密钥的集合）。对于任何可能的标签 $t_0$，令 $\mathcal{K}(t_0)$ 表示使得 $t_0$ 是 $m_0$ 上的有效标签的密钥集合；即

$$\mathcal{K}(t_{0})\overset{\operatorname{def}}{=}\{k\mid\mathsf{Vrfy}_{k}(m_{0},t_{0})=1\}.$$

For any $t_0$ we must have $|\mathcal{K}(t_0)| \leq \varepsilon \cdot |\mathcal{K}|$. Otherwise the adversary could simply output $(m_0, t_0)$ as its forgery; this would be a valid forgery with probability at least $|\mathcal{K}(t_0)|/|\mathcal{K}| > \varepsilon$, contradicting the claimed security.

对于任何 $t_0$，我们必须有 $|\mathcal{K}(t_0)| \leq \varepsilon \cdot |\mathcal{K}|$。否则敌手可以简单地输出 $(m_0, t_0)$ 作为其伪造；这将以至少 $|\mathcal{K}(t_0)|/|\mathcal{K}| > \varepsilon$ 的概率成为一个有效伪造，与声称的安全性矛盾。

Consider now the adversary $\mathcal{A}$ who requests a tag on $m_0$, receives in return a tag $t_0$, chooses a uniform key $k \in \mathcal{K}(t_0)$, and outputs $(m_1, \mathsf{Mac}_k(m_1))$ as its forgery. The probability that $\mathcal{A}$ outputs a valid forgery is at least

现在考虑敌手 $\mathcal{A}$，它请求 $m_0$ 上的标签，收到标签 $t_0$，选择一个均匀的密钥 $k \in \mathcal{K}(t_0)$，并输出 $(m_1, \mathsf{Mac}_k(m_1))$ 作为其伪造。$\mathcal{A}$ 输出有效伪造的概率至少为

$$\begin{align*}\sum_{t_{0}}\Pr[\mathsf{Mac}_{k}(m_{0})=t_{0}]\cdot\frac{1}{|\mathcal{K}(t_{0})|}&\geq\sum_{t_{0}}\Pr[\mathsf{Mac}_{k}(m_{0})=t_{0}]\cdot\frac{1}{\varepsilon\cdot|\mathcal{K}|}\\&=\frac{1}{\varepsilon\cdot|\mathcal{K}|}.\end{align*}$$

By the claimed security of the scheme, the probability that the adversary can output a valid forgery is at most $\varepsilon$. Thus, we must have $|\mathcal{K}| \geq \varepsilon^{-2}$.

根据该方案声称的安全性，敌手输出有效伪造的概率最多为 $\varepsilon$。因此，我们必须有 $|\mathcal{K}| \geq \varepsilon^{-2}$。

As a corollary, a ${2}^{-n}$-secure one-time MAC for which all keys have the same length must have keys of length at least 2n.

作为推论，一个 ${2}^{-n}$-安全的一次 MAC，如果所有密钥长度相同，则密钥长度至少为 2n。

### References and Additional Reading　参考文献与延伸阅读

The definition of security for message authentication codes was adapted by Bellare et al. [20] from the definition of security for digital signatures [88] (see Chapter 13). Later work of Bellare et al. [19] highlighted the importance of the definitional variant where verification queries are allowed.

消息认证码的安全性定义由 Bellare 等人 [20] 从数字签名 [88] 的安全性定义改编而来（见第 13 章）。Bellare 等人 [19] 的后续工作强调了允许验证查询的定义变体的重要性。

The paradigm of using pseudorandom functions for message authentication (as in Construction 4.5) was introduced by Goldreich et al. [84]. Construction 4.7 is due to Goldreich [83].

使用伪随机函数进行消息认证的范式（如构造 4.5 所示）由 Goldreich 等人 [84] 引入。构造 4.7 归功于 Goldreich [83]。

CBC-MAC was standardized in the early 1980s [102, 11]. Basic CBC-MAC was proven secure (for authenticating fixed-length messages) by Bellare et al. [20]. Bernstein [30] gives a more direct proof that we have adapted in Section 4.4.2. An improved bound on the security of basic CBC-MAC, which also directly takes into account reliance on a pseudorandom permutation rather than a pseudorandom function, was given by Bellare et al. [23].

CBC-MAC 在 20 世纪 80 年代早期被标准化 [102, 11]。基本 CBC-MAC 由 Bellare 等人 [20] 证明了安全性（用于认证固定长度消息）。Bernstein [30] 给出了一个更直接的证明，我们在 4.4.2 节中采用了该证明。Bellare 等人 [23] 给出了基本 CBC-MAC 安全性的一个改进界，该界也直接考虑了对伪随机置换（而非伪随机函数）的依赖。

As noted in this chapter, basic CBC-MAC is insecure when used to authenticate messages of different lengths. One way to fix this is to prepend the length to the message. Alternate approaches were explored by Petrank and Rackoff [158], Black and Rogaway [36], and Iwata and Kurosawa [103]; these led to a new proposed standard called CMAC [191].

如本章所述，基本 CBC-MAC 在用于认证不同长度的消息时是不安全的。修复此问题的一种方法是在消息前加上长度。Petrank 和 Rackoff [158]、Black 和 Rogaway [36] 以及 Iwata 和 Kurosawa [103] 探索了其他方法；这些工作导致了称为 CMAC [191] 的新提议标准。

GMAC was introduced as part of the GCM authenticated encryption scheme by McGrew and Viega [136], based on work of Kohno et al. [119]. Poly1305 is due to Bernstein [31].

GMAC 由 McGrew 和 Viega [136] 作为 GCM 认证加密方案的一部分引入，基于 Kohno 等人 [119] 的工作。Poly1305 归功于 Bernstein [31]。

Information-theoretic MACs were first studied by Gilbert et al. [80]. Carter and Wegman [48, 203] introduced the notion of strongly universal functions, and noted their application to one-time message authentication. They also showed how to reduce the key length for this task by using an almost strongly universal function. Construction 4.24 is based on an idea of Wegman and Carter [203], though difference-universal functions were not introduced until several years later [120, 121]. (Note that difference-universal functions are called XOR-universal or almost $\Delta$-universal in the literature.) The reader interested in learning more about information-theoretic MACs is referred to the paper by Stinson [193], the survey by Simmons [187], or the first edition of Stinson's textbook [194, Chapter 10].

信息论 MAC 最早由 Gilbert 等人 [80] 研究。Carter 和 Wegman [48, 203] 引入了强通用函数的概念，并注意到它们在一次消息认证中的应用。他们还展示了如何通过使用几乎强通用函数来减少此任务的密钥长度。构造 4.24 基于 Wegman 和 Carter [203] 的思想，尽管差分通用函数直到几年后才被引入 [120, 121]。（注意，差分通用函数在文献中被称为 XOR-通用（XOR-universal）或几乎 $\Delta$-通用（almost $\Delta$-universal）。）有兴趣了解更多信息论 MAC 的读者可以参考 Stinson [193] 的论文、Simmons [187] 的综述或 Stinson 教科书的第一版 [194, 第 10 章]。

### Exercises　习题

4.1 Consider an extension of the definition of secure message authentication where the adversary is provided with both a Mac and a Vrfy oracle.

4.1 考虑安全消息认证定义的一个扩展，其中敌手被同时提供 Mac 和 Vrfy 预言机。

(a) Provide a formal definition of security for this case.

(a) 给出这种情况下安全性的形式化定义。

(b) Assume $\Pi$ is a deterministic MAC using canonical verification that satisfies Definition 4.2. Prove that $\Pi$ also satisfies your definition from part (a).

(b) 假设 $\Pi$ 是使用规范验证的确定性 MAC，满足定义 4.2。证明 $\Pi$ 也满足你在 (a) 部分中的定义。

4.2 Assume secure MACs exist. Give a construction of a MAC that is secure with respect to Definition 4.2 but that is not secure when the adversary is additionally given access to a Vrfy oracle (cf. the previous exercise).

4.2 假设安全的 MAC 存在。给出一个 MAC 的构造，它相对于定义 4.2 是安全的，但当敌手额外被授予对 Vrfy 预言机的访问权限时是不安全的（参见前一习题）。

4.3 Prove Proposition 4.4.

4.3 证明命题 4.4。

4.4 Assume secure MACs exist. Prove that there exists a MAC that is secure (Definition 4.2) but is not strongly secure (Definition 4.3).

4.4 假设安全的 MAC 存在。证明存在一个 MAC，它是安全的（定义 4.2）但不是强安全的（定义 4.3）。

4.5 Consider the following MAC for messages of length $\ell(n) = 2n - 2$ using a pseudorandom function $F$: On input a message $m_0\|m_1$ (with $|m_0| = |m_1| = n - 1$) and key $k \in \{0,1\}^n$, algorithm Mac outputs $t = F_k(0\|m_0)\|F_k(1\|m_1)$. Algorithm Vrfy is defined in the natural way. Is this MAC secure? Prove your answer.

4.5 考虑以下使用伪随机函数 $F$ 的 MAC，用于长度为 $\ell(n) = 2n - 2$ 的消息：输入消息 $m_0\|m_1$（其中 $|m_0| = |m_1| = n - 1$）和密钥 $k \in \{0,1\}^n$，算法 Mac 输出 $t = F_k(0\|m_0)\|F_k(1\|m_1)$。算法 Vrfy 以自然方式定义。该 MAC 安全吗？证明你的答案。

4.6 Let $F$ be a pseudorandom function. Show that each of the following MACs is insecure, even if used to authenticate fixed-length messages. (In each case $\mathsf{Gen}$ outputs a uniform $k \in \{0,1\}^{n}$; we let $\langle i\rangle$ denote an $n/2$-bit encoding of the integer $i$.)

4.6 设 $F$ 是一个伪随机函数。证明以下每个 MAC 都是不安全的，即使用于认证固定长度的消息。（在每种情况下 $\mathsf{Gen}$ 输出一个均匀的 $k \in \{0,1\}^{n}$；令 $\langle i\rangle$ 表示整数 $i$ 的 $n/2$ 比特编码。）

(a) To authenticate a message $m = m_1, \ldots, m_\ell$, where $m_i \in \{0,1\}^n$, compute $t := F_k(m_1) \oplus \cdots \oplus F_k(m_\ell)$.

(a) 为认证消息 $m = m_1, \ldots, m_\ell$，其中 $m_i \in \{0,1\}^n$，计算 $t := F_k(m_1) \oplus \cdots \oplus F_k(m_\ell)$。

(b) To authenticate a message $m = m_1, \ldots, m_\ell$, where $m_i \in \{0,1\}^{n/2}$, compute $t := F_k(\langle 1\rangle\|m_1) \oplus \cdots \oplus F_k(\langle \ell\rangle\|m_\ell)$.

(b) 为认证消息 $m = m_1, \ldots, m_\ell$，其中 $m_i \in \{0,1\}^{n/2}$，计算 $t := F_k(\langle 1\rangle\|m_1) \oplus \cdots \oplus F_k(\langle \ell\rangle\|m_\ell)$。

(c) To authenticate a message $m = m_1, \ldots, m_\ell$, where $m_i \in \{0,1\}^{n/2}$, choose uniform $r \in \{0,1\}^n$, compute

(c) 为认证消息 $m = m_1, \ldots, m_\ell$，其中 $m_i \in \{0,1\}^{n/2}$，选择均匀的 $r \in \{0,1\}^n$，计算

$$t:=F_{k}(r)\oplus F_{k}(\langle1\rangle\|m_{1})\oplus\cdots\oplus F_{k}(\langle\ell\rangle\|m_{\ell}),$$

and let the tag be $\langle r,t\rangle$.

并令标签为 $\langle r,t\rangle$。

4.7 Let $F$ be a pseudorandom function. Show that the following MAC for messages of length ${2}n$ is insecure: $\mathsf{Gen}$ outputs a uniform $k \in \{0,1\}^n$. To authenticate a message $m_1\|m_2$ with $|m_1|=|m_2|=n$, compute the $\text{tag} F_k(m_1)\|F_k(F_k(m_2))$.

4.7 设 $F$ 是一个伪随机函数。证明以下用于长度为 ${2}n$ 的消息的 MAC 是不安全的：$\mathsf{Gen}$ 输出一个均匀的 $k \in \{0,1\}^n$。为认证消息 $m_1\|m_2$（其中 $|m_1|=|m_2|=n$），计算标签 $F_k(m_1)\|F_k(F_k(m_2))$。

4.8 Given any deterministic MAC (Mac, Vrfy), we may view Mac as a keyed function. In both Constructions 4.5 and 4.9, Mac is a pseudorandom function. Give a construction of a secure, deterministic MAC in which Mac is not a pseudorandom function.

4.8 给定任何确定性 MAC (Mac, Vrfy)，我们可以将 Mac 视为一个带密钥的函数。在构造 4.5 和 4.9 中，Mac 都是一个伪随机函数。给出一个安全的确定性 MAC 构造，其中 Mac 不是一个伪随机函数。

4.9 Is Construction 4.5 necessarily secure when instantiated using a weak pseudorandom function (cf. Exercise 3.28)? Explain.

4.9 当使用弱伪随机函数（参见习题 3.28）实例化时，构造 4.5 是否一定是安全的？解释原因。

4.10 Prove that Construction 4.7 is a secure MAC even when the adversary is additionally given access to a Vrfy oracle (cf. Exercise 4.1), assuming $\Pi^{\prime}$ is a secure MAC that uses canonical verification.

4.10 证明即使敌手额外被授予对 Vrfy 预言机的访问权限（参见习题 4.1），构造 4.7 仍然是一个安全的 MAC，假设 $\Pi^{\prime}$ 是使用规范验证的安全 MAC。

4.11 Prove that Construction 4.7 is strongly secure if $\Pi^{\prime}$ is strongly secure.

4.11 证明如果 $\Pi^{\prime}$ 是强安全的，那么构造 4.7 是强安全的。

4.12 Prove that Construction 4.7 is secure if it is changed as follows: Set $t_i := F_k(r\|b\|i\|m_i)$ where $b$ is a single bit such that $b = 0$ in all blocks but the last one, and $b = 1$ in the last block. (Assume for simplicity that the length of any message being authenticated is always an integer multiple of $n/2 - 1$). What is the advantage of this modification?

4.12 证明如果构造 4.7 被如下修改，它仍然是安全的：设 $t_i := F_k(r\|b\|i\|m_i)$，其中 $b$ 是一个单比特，使得除了最后一个块外 $b = 0$，最后一个块中 $b = 1$。（为简单起见，假设被认证的任何消息的长度始终是 $n/2 - 1$ 的整数倍。）这种修改有什么优势？

4.13 We explore what happens when the basic CBC-MAC construction is used with messages of different lengths.

4.13 我们探讨当基本 CBC-MAC 构造用于不同长度的消息时会发生什么。

(a) Say the sender and receiver do not agree on the message length in advance (and so $\operatorname{Vrfy}_{k}(m,t)=1$ iff $t\stackrel{?}{=}\operatorname{Mac}_{k}(m)$, regardless of the length of $m$), but the sender is careful to only authenticate messages of length 2n. Show that an adversary can forge a valid tag on a message of length 4n.

(a) 假设发送方和接收方没有预先约定消息长度（因此 $\operatorname{Vrfy}_{k}(m,t)=1$ 当且仅当 $t\stackrel{?}{=}\operatorname{Mac}_{k}(m)$，无论 $m$ 的长度如何），但发送方小心地只认证长度为 2n 的消息。证明敌手可以伪造一条长度为 4n 的消息上的有效标签。

(b) Say the receiver only accepts 3-block messages (so $\operatorname{Vrfy}_{k}(m,t)=1$ only if m has length 3n and $t\stackrel{?}{=} \operatorname{Mac}_{k}(m)$), but the sender authenticates messages of any length a multiple of n. Show that an adversary can forge a valid tag on a new message.

(b) 假设接收方只接受 3 块消息（因此 $\operatorname{Vrfy}_{k}(m,t)=1$ 仅当 m 的长度为 3n 且 $t\stackrel{?}{=} \operatorname{Mac}_{k}(m)$），但发送方认证任意长度为 n 的倍数的消息。证明敌手可以伪造一条新消息上的有效标签。

4.14 Prove that the following modifications of basic CBC-MAC do not yield a secure MAC (even for fixed-length messages):

4.14 证明以下对基本 CBC-MAC 的修改不能产生安全的 MAC（即使对于固定长度的消息）：

(a) Mac outputs all blocks $t_1, \ldots, t_\ell$, rather than just $t_\ell$. (Verification only checks whether $t_\ell$ is correct.)

(a) Mac 输出所有块 $t_1, \ldots, t_\ell$，而不仅仅是 $t_\ell$。（验证仅检查 $t_\ell$ 是否正确。）

(b) A random initial block is used each time a message is authenticated. That is, change Construction 4.9 by choosing uniform $t_0 \in \{0,1\}^n$, computing $t_\ell$ as before, and then outputting the tag $\langle t_0,t_\ell\rangle$; verification is done in the natural way.

(b) 每次认证消息时使用一个随机的初始块。即，修改构造 4.9：选择均匀的 $t_0 \in \{0,1\}^n$，如前计算 $t_\ell$，然后输出标签 $\langle t_0,t_\ell\rangle$；验证以自然方式进行。

4.15 Show that appending the message length to the end of the message before applying basic CBC-MAC does not result in a secure MAC for arbitrary-length messages.

4.15 证明在应用基本 CBC-MAC 之前将消息长度附加到消息末尾，不能得到适用于任意长度消息的安全 MAC。

4.16 Define a version of CBC-MAC for messages of length at most $\ell \cdot 2^n$ as follows: given a message $m$, pad it with 0s so that it has length exactly $\ell \cdot 2^n$; apply basic CBC-MAC to the result. Is this secure?

4.16 定义 CBC-MAC 的一个版本，用于长度最多为 $\ell \cdot 2^n$ 的消息如下：给定消息 $m$，用 0 填充使其长度恰好为 $\ell \cdot 2^n$；对结果应用基本 CBC-MAC。这安全吗？

4.17 Consider the following encoding that handles messages whose length is less than $n \cdot 2^n$: We encode a string $m \in \{0,1\}^*$ by first appending as many 0s as needed to make the length of the resulting string $\hat{m}$ a nonzero multiple of $n$. Then we prepend the number of blocks in $\hat{m}$ (equivalently, prepend the integer $|\hat{m}|/n$), encoded as an n-bit string. Show that this encoding is not prefix-free.

4.17 考虑以下处理长度小于 $n \cdot 2^n$ 的消息的编码：我们对串 $m \in \{0,1\}^*$ 的编码方式是，先给它附加尽可能多的 0，使所得串 $\hat{m}$ 的长度成为 $n$ 的非零倍数。然后我们在前面加上 $\hat{m}$ 的块数（等价地，加上整数 $|\hat{m}|/n$），编码为 n 比特串。证明该编码不是无前缀的。

4.18 Prove that the encoding for arbitrary-length messages described in Section 4.4.2 is prefix-free.

4.18 证明 4.4.2 节中描述的用于任意长度消息的编码是无前缀的。

4.19 Prove that the following modification of basic CBC-MAC gives a secure MAC for arbitrary-length messages if $F$ is a pseudorandom function. (Assume all messages have length a multiple of the block length.) $\mathsf{Mac}_k(m)$ first computes $k_\ell := F_k(\ell)$, where $\ell$ is the length of $m$. The tag is then computed using basic CBC-MAC with key $k_\ell$.

4.19 证明如果 $F$ 是一个伪随机函数，以下对基本 CBC-MAC 的修改可以得到一个适用于任意长度消息的安全 MAC。（假设所有消息的长度都是块长度的倍数。）$\mathsf{Mac}_k(m)$ 首先计算 $k_\ell := F_k(\ell)$，其中 $\ell$ 是 $m$ 的长度。然后使用密钥 $k_\ell$ 通过基本 CBC-MAC 计算标签。

4.20 Let F be a keyed function that is a secure (deterministic) MAC for messages of length n. (Note that F need not be a pseudorandom function.) Show that basic CBC-MAC is not necessarily a secure MAC (even for fixed-length messages) when instantiated with F.

4.20 设 F 是一个带密钥的函数，它是长度为 n 的消息的安全（确定性）MAC。（注意 F 不一定是伪随机函数。）证明当使用 F 实例化时，基本 CBC-MAC 不一定是安全的 MAC（即使对于固定长度的消息）。

4.21 Assume the same nonce r is used to authenticate two different messages in GMAC or Poly1305. Show how to construct a forgery in that case, with high probability. Hint: You may assume only single-block messages are authenticated.

4.21 假设在 GMAC 或 Poly1305 中使用相同的 nonce r 来认证两条不同的消息。说明在这种情况下如何以高概率构造一个伪造。提示：你可以假设只认证单块消息。

4.22 Prove or disprove whether the following functions are $\ell/|\mathbb{F}|$-difference universal. In each case assume $\mathcal{K} = \mathbb{F}$ and $\mathcal{M} = \mathbb{F}^{<\ell}$, and for a message $m = (m_1, \ldots, m_{\ell^{\prime} - 1})$ let $m_{\ell^{\prime}} \in \mathbb{F}$ be an encoding of $\ell^{\prime} - 1$.

4.22 证明或反驳以下函数是否为 $\ell/|\mathbb{F}|$-差分通用的。在每种情况下假设 $\mathcal{K} = \mathbb{F}$ 和 $\mathcal{M} = \mathbb{F}^{<\ell}$，对于消息 $m = (m_1, \ldots, m_{\ell^{\prime} - 1})$，令 $m_{\ell^{\prime}} \in \mathbb{F}$ 是 $\ell^{\prime} - 1$ 的编码。

(a) $h_{k}^{\prime}(m) = m^{\prime}(k)$, where

(a) $h_{k}^{\prime}(m) = m^{\prime}(k)$，其中

$$m^{\prime}(X)\stackrel{\mathrm{def}}{=}m_{1}\cdot X^{\ell}+m_{2}\cdot X^{\ell-1}+\cdots+m_{\ell^{\prime}}\cdot X^{\ell-\ell^{\prime}+1}.$$

(b) $h_{k}^{\prime\prime}(m) = m^{\prime\prime}(k)$, where

(b) $h_{k}^{\prime\prime}(m) = m^{\prime\prime}(k)$，其中

$$m^{\prime \prime}(X)\stackrel{\mathrm{def}}{=}m_{1}\cdot X^{\ell^{\prime}-1}+m_{2}\cdot X^{\ell^{\prime}-2}+\cdots+m_{\ell^{\prime}}.$$

(c) $h_{k}^{\prime\prime\prime}(m) = m^{\prime\prime\prime}(k)$, where

(c) $h_{k}^{\prime\prime\prime}(m) = m^{\prime\prime\prime}(k)$，其中

$$m^{\prime\prime\prime}(X)\stackrel{\mathrm{def}}{=}m_{1}\cdot X+m_{2}\cdot X^{2}+\cdots+m_{\ell^{\prime}}\cdot X^{\ell^{\prime}}.$$

4.23 Show that the polynomial-based difference-universal function from Section 4.5.2 is not strongly universal.

4.23 证明 4.5.2 节中基于多项式的差分通用函数不是强通用的。

4.24 Fix $\ell > 0$ and a prime $p$. Let $\mathcal{K} = \mathbb{Z}_{p}^{\ell+1}$, $\mathcal{M} = \mathbb{Z}_{p}^{\ell}$, and $\mathcal{T} = \mathbb{Z}_{p}$. Define $h: \mathcal{K} \times \mathcal{M} \to \mathcal{T}$ as

4.24 固定 $\ell > 0$ 和一个素数 $p$。设 $\mathcal{K} = \mathbb{Z}_{p}^{\ell+1}$，$\mathcal{M} = \mathbb{Z}_{p}^{\ell}$，$\mathcal{T} = \mathbb{Z}_{p}$。定义 $h: \mathcal{K} \times \mathcal{M} \to \mathcal{T}$ 为

$$\begin{array}{r}{h_{k_{0},k_{1},\ldots,k_{\ell}}(m_{1},\ldots,m_{\ell})=\left[k_{0}+\sum_{i}k_{i}m_{i}\bmod p\right].}\end{array}$$

Prove that h is strongly universal.

证明 h 是强通用的。

4.25 Fix $\ell, n > 0$. Let $\mathcal{K} = \{0,1\}^{\ell \times n} \times \{0,1\}^{\ell}$ (interpreted as a boolean $\ell \times n$ matrix and an $\ell$-dimensional vector), let $\mathcal{M} = \{0,1\}^n$, and let $\mathcal{T} = \{0,1\}^{\ell}$. Define $h: \mathcal{K} \times \mathcal{M} \to \mathcal{T}$ as $h_{K,v}(m) = K \cdot m \oplus v$, where all operations are performed modulo 2. Prove that $h$ is strongly universal.

4.25 固定 $\ell, n > 0$。设 $\mathcal{K} = \{0,1\}^{\ell \times n} \times \{0,1\}^{\ell}$（解释为一个布尔 $\ell \times n$ 矩阵和一个 $\ell$ 维向量），$\mathcal{M} = \{0,1\}^n$，$\mathcal{T} = \{0,1\}^{\ell}$。定义 $h: \mathcal{K} \times \mathcal{M} \to \mathcal{T}$ 为 $h_{K,v}(m) = K \cdot m \oplus v$，其中所有运算模 2 进行。证明 $h$ 是强通用的。

4.26 A Toeplitz matrix $K$ is a matrix in which $K_{i,j}=K_{i-1,j-1}$ when $i,j>1$; i.e., the values along any diagonal are equal. So an $\ell\times n$ Toeplitz matrix has the form

4.26 Toeplitz 矩阵 $K$ 是满足当 $i,j>1$ 时 $K_{i,j}=K_{i-1,j-1}$ 的矩阵；即沿任何对角线的值相等。因此一个 $\ell\times n$ Toeplitz 矩阵具有以下形式

$$\left[\begin{matrix}{K_{n}}&{K_{n-1}}&{K_{n-2}}&{\cdots K_{1}}\\ {K_{n+1}}&{K_{n}}&{K_{n-1}}&{\cdots K_{2}}\\ {K_{n+2}}&{K_{n+1}}&{K_{n}}&{\cdots K_{3}}\\ {\vdots}&{\vdots}&{\vdots}&{\vdots}\\ {K_{n+\ell-1}K_{n+\ell-2}K_{n+\ell-3}\cdots K_{\ell}}\\ \end{matrix}\right].$$

Let $\mathcal{K} = T^{\ell \times n} \times \{0,1\}^{\ell}$ (where $T^{\ell \times n}$ denotes the set of $\ell \times n$ Toeplitz matrices), and let $\mathcal{M} = \{0,1\}^n$. Define $h : \mathcal{K} \times \mathcal{M} \to \{0,1\}^{\ell}$ as $h_{K,v}(m) = K \cdot m \oplus v$, where all operations are performed modulo 2. Prove that $h$ is strongly universal. What is the advantage here as compared to the construction in the previous exercise?

设 $\mathcal{K} = T^{\ell \times n} \times \{0,1\}^{\ell}$（其中 $T^{\ell \times n}$ 表示 $\ell \times n$ Toeplitz 矩阵的集合），$\mathcal{M} = \{0,1\}^n$。定义 $h : \mathcal{K} \times \mathcal{M} \to \{0,1\}^{\ell}$ 为 $h_{K,v}(m) = K \cdot m \oplus v$，其中所有运算模 2 进行。证明 $h$ 是强通用的。与前一习题中的构造相比，这里有什么优势？

4.27 Define an appropriate notion of a $\varepsilon$-secure two-time MAC, and give a construction that meets your definition.

4.27 定义 $\varepsilon$-安全的两次 MAC 的适当概念，并给出满足你定义的构造。
