## 12.3 Hybrid Encryption and the KEM/DEM Paradigm　混合加密与 KEM/DEM 范式

Claim 12.7 shows that any CPA-secure public-key encryption scheme for $\ell$-bit messages can be used to obtain a CPA-secure public-key encryption scheme for messages of arbitrary length. Encrypting an arbitrary-length message using this approach requires $\gamma \stackrel{\mathrm{def}}{=} \lceil |m|/\ell \rceil$ invocations of the original encryption scheme, meaning that both the computation and the ciphertext length are increased by a multiplicative factor of $\gamma$ relative to the underlying scheme.

断言 12.7 表明，任何针对 $\ell$ 比特消息的选择明文安全公钥加密方案，都可以用来得到针对任意长度消息的选择明文安全公钥加密方案。但用这种方法加密任意长度的消息需要调用原加密方案 $\gamma \stackrel{\mathrm{def}}{=} \lceil |m|/\ell \rceil$ 次，这意味着相对于底层方案，计算量和密文长度都扩大了 $\gamma$ 倍。

It is possible to do better by using private-key encryption in tandem with public-key encryption. This improves efficiency because private-key encryption is significantly faster than public-key encryption, and improves bandwidth because private-key schemes have lower ciphertext expansion. The resulting combination is called hybrid encryption and is used extensively in practice. The basic idea is to use public-key encryption to obtain a shared key $k$, and then encrypt the message $m$ using a private-key encryption scheme and key k. The receiver uses its long-term (asymmetric) private key to derive k, and then uses private-key decryption (with key k) to recover the original message. We stress that although private-key encryption is used as a component, this is a full-fledged public-key encryption scheme by virtue of the fact that the sender and receiver do not share any secret key in advance.

把私钥加密与公钥加密结合起来使用可以做得更好。这样做之所以能提高效率，是因为私钥加密比公钥加密快得多；之所以能节省带宽，是因为私钥方案的密文扩展更小。这样得到的组合称为混合加密，在实践中被广泛使用。其基本思想是：用公钥加密来得到一个共享密钥 $k$，然后用私钥加密方案和密钥 $k$ 加密消息 $m$。接收方用其长期（非对称）私钥导出 $k$，再用私钥解密（用密钥 $k$）恢复原始消息。我们强调，尽管使用了私钥加密作为组件，但由于发送方与接收方事先并不共享任何秘密密钥，这是一个名副其实的公钥加密方案。

![Image](https://lsky.jerryxue.top/i/2026/08/25/6a8d86dc71b4a.jpg)

**FIGURE 12.1: Hybrid encryption. Enc denotes a public-key encryption scheme, while Enc' is a private-key encryption scheme. / 图 12.1：混合加密。Enc 表示公钥加密方案，Enc′ 表示私钥加密方案**

In a direct implementation of this idea (see Figure 12.1), the sender would share $k$ by (1) choosing a uniform value $k$ and then (2) encrypting $k$ using a public-key encryption scheme. A more direct approach is to use a public-key primitive called a key-encapsulation mechanism (KEM) to accomplish both of these “in one shot.” This is advantageous both from a conceptual point of view and in terms of efficiency, as we will see later.

这一思想的直接实现（见图 12.1）是：发送方通过（1）均匀选取一个值 $k$，然后（2）用公钥加密方案加密 $k$ 来共享 $k$。更直接的做法是使用一种称为密钥封装机制（KEM）的公钥原语，“一次性”完成这两件事。正如我们稍后将看到的，无论从概念上还是从效率上看，这都更有优势。

A KEM has three algorithms similar in spirit to those of a public-key encryption scheme. As before, the key-generation algorithm Gen is used to generate a pair of public and private keys. In place of encryption, we now have an encapsulation algorithm Encaps that takes only a public key as input (and no message), and outputs a ciphertext c along with a key k. A corresponding decapsulation algorithm Decaps is run by the receiver to recover $k$ from the ciphertext $c$ using the private key. Formally:

KEM 包含三个算法，其形式与公钥加密方案类似。与之前一样，密钥生成算法 $\mathsf{Gen}$ 用于生成一对公钥和私钥。现在取代加密算法的是封装算法 $\mathsf{Encaps}$：它只以公钥为输入（没有消息），输出一个密文 $c$ 和一个密钥 $k$。对应的解封装算法 $\mathsf{Decaps}$ 由接收方运行，利用私钥从密文 $c$ 中恢复 $k$。严格地说：

DEFINITION 12.9 A key-encapsulation mechanism (KEM) is a tuple of probabilistic polynomial-time algorithms (Gen, Encaps, Decaps) such that:

定义 12.9　密钥封装机制（KEM）是由概率多项式时间算法构成的三元组 $(\mathsf{Gen}, \mathsf{Encaps}, \mathsf{Decaps})$，满足：

1. The key-generation algorithm Gen takes as input the security parameter ${1}^{n}$ and outputs a public-/private-key pair $(pk, sk)$. We assume $pk$ and $sk$ each has length at least $n$, and that $n$ can be determined from $pk$.

   密钥生成算法 $\mathsf{Gen}$ 以安全参数 ${1}^{n}$ 为输入，输出一个公钥/私钥对 $(pk, sk)$。我们假定 $pk$ 和 $sk$ 的长度都至少为 $n$，并且 $n$ 可以从 $pk$ 中确定。

2. The encapsulation algorithm Encaps takes as input a public key $pk$ (which implicitly defines $n$). It outputs a ciphertext $c$ and a key $k \in \{0,1\}^{\ell(n)}$ where $\ell$ is the key length. We write this as $(c,k) \leftarrow \mathsf{Encaps}_{pk}(1^n)$.

   封装算法 $\mathsf{Encaps}$ 以公钥 $pk$ 为输入（它隐含地确定了 $n$）。它输出一个密文 $c$ 和一个密钥 $k \in \{0,1\}^{\ell(n)}$，其中 $\ell$ 为密钥长度。记作 $(c,k) \leftarrow \mathsf{Encaps}_{pk}(1^n)$。

3. The deterministic decapsulation algorithm Decaps takes as input a private key $sk$ and a ciphertext $c$, and outputs a key $k$ or a special symbol $\perp$ denoting failure. We write this as $k := \mathsf{Decaps}_{sk}(c)$.

   确定性解封装算法 $\mathsf{Decaps}$ 以私钥 $sk$ 和密文 $c$ 为输入，输出一个密钥 $k$，或者一个表示失败的特殊符号 $\perp$。记作 $k := \mathsf{Decaps}_{sk}(c)$。

It is required that all but negligible probability over the randomness of Gen and Encaps, if $\mathsf{Encaps}_{pk}(1^{n})$ outputs $(c,k)$ then $\mathsf{Decaps}_{sk}(c)$ outputs $k$.

要求：除去由 $\mathsf{Gen}$ 与 $\mathsf{Encaps}$ 的随机性引起的可忽略概率外，若 $\mathsf{Encaps}_{pk}(1^{n})$ 输出 $(c,k)$，则 $\mathsf{Decaps}_{sk}(c)$ 输出 $k$。

In the definition we assume for simplicity that Encaps always outputs (a ciphertext $c$ and) a key of some fixed length $\ell(n)$. One could also consider a more general definition in which Encaps takes ${1}^{\ell}$ as an addition

在该定义中，为简单起见，我们假定 $\mathsf{Encaps}$ 总是输出（一个密文 $c$ 和）某个固定长度 $\ell(n)$ 的密钥。也可以考虑一种更一般的定义，其中 $\mathsf{Encaps}$ 额外地以 ${1}^{\ell}$ 为输入

Any public-key encryption scheme trivially gives a KEM by choosing a random key $k$ and encrypting it. As we will see, however, dedicated constructions of KEMs can be more efficient.

任何公钥加密方案都可以通过随机选取一个密钥 $k$ 并加密它而直接得到一个 KEM。然而，正如我们将看到的，专门构造的 KEM 可以更高效。

![Image](https://lsky.jerryxue.top/i/2026/08/25/6a8d86e080fc6.jpg)

**FIGURE 12.2: Hybrid encryption using the KEM/DEM approach. / 图 12.2：采用 KEM/DEM 方法的混合加密**

Using a KEM (with key length $n$), we can implement hybrid encryption as in Figure 12.2. The sender runs $\mathsf{Encaps}_{pk}(1^n)$ to obtain $c$ along with a key $k$; it then uses a private-key encryption scheme to encrypt its message $m$, using $k$ as the key. In this context, the private-key encryption scheme is called a data-encapsulation mechanism (DEM) for obvious reasons. The ciphertext sent to the receiver includes both $c$ and the ciphertext $c^{\prime}$ from the private-key scheme. Construction 12.10 gives a formal specification.

使用（密钥长度为 $n$ 的）KEM，我们可以如图 12.2 所示实现混合加密。发送方运行 $\mathsf{Encaps}_{pk}(1^n)$ 得到 $c$ 和一个密钥 $k$；然后用私钥加密方案、以 $k$ 为密钥加密其消息 $m$。在这一语境中，私钥加密方案由于显而易见的原因被称为数据封装机制（DEM）。发送给接收方的密文包括 $c$ 和来自私钥方案的密文 $c^{\prime}$ 两部分。构造 12.10 给出了形式化的描述。

What is the efficiency of the resulting hybrid encryption scheme $\Pi^{hy}$? For some fixed value of $n$, let $\alpha$ denote the cost of encapsulating an $n$-bit key using Encaps, and let $\beta$ denote the cost (per bit of plaintext) of encryption using Enc'. (The formal specification is given in Construction 12.10.)

由此得到的混合加密方案 $\Pi^{hy}$ 效率如何？对某个固定的 $n$ 值，令 $\alpha$ 表示用 $\mathsf{Encaps}$ 封装一个 $n$ 比特密钥的开销，令 $\beta$ 表示用 $\mathsf{Enc}^{\prime}$ 加密的（每比特明文）开销。（形式化描述见构造 12.10。）

**CONSTRUCTION 12.10**

**构造 12.10**

Let $\Pi = (\mathsf{Gen}, \mathsf{Encaps}, \mathsf{Decaps})$ be a KEM with key length $n$, and let $\Pi' = (\mathsf{Gen}', \mathsf{Enc}', \mathsf{Dec}')$ be a private-key encryption scheme. Construct a public-key encryption scheme $\Pi^{\mathsf{hy}} = (\mathsf{Gen}^{\mathsf{hy}}, \mathsf{Enc}^{\mathsf{hy}}, \mathsf{Dec}^{\mathsf{hy}})$ as follows:

设 $\Pi = (\mathsf{Gen}, \mathsf{Encaps}, \mathsf{Decaps})$ 是密钥长度为 $n$ 的 KEM，$\Pi' = (\mathsf{Gen}', \mathsf{Enc}', \mathsf{Dec}')$ 是私钥加密方案。按如下方式构造公钥加密方案 $\Pi^{\mathsf{hy}} = (\mathsf{Gen}^{\mathsf{hy}}, \mathsf{Enc}^{\mathsf{hy}}, \mathsf{Dec}^{\mathsf{hy}})$：

- $\mathsf{Gen}^{\mathsf{hy}}$: on input ${1}^{n}$ run $\mathsf{Gen}({1}^{n})$ and use the public and private keys $(pk, sk)$ that are output.

  $\mathsf{Gen}^{\mathsf{hy}}$：输入 ${1}^{n}$ 时，运行 $\mathsf{Gen}({1}^{n})$，并使用输出的公钥与私钥 $(pk, sk)$。

- $\mathsf{Enc}^{\mathsf{hy}}$: on input a public key pk and a message $m \in \{0,1\}^{*}$ do:

  $\mathsf{Enc}^{\mathsf{hy}}$：输入公钥 $pk$ 和消息 $m \in \{0,1\}^{*}$ 时，执行：

   1. Compute $(c, k) \leftarrow \mathsf{Encaps}_{pk}(1^n)$.

      计算 $(c, k) \leftarrow \mathsf{Encaps}_{pk}(1^n)$。

   2. Compute $c^{\prime} \leftarrow \mathsf{Enc}_{k}^{\prime}(m)$.

      计算 $c^{\prime} \leftarrow \mathsf{Enc}_{k}^{\prime}(m)$。

   3. Output the ciphertext $\langle c, c^{\prime}\rangle$.

      输出密文 $\langle c, c^{\prime}\rangle$。

- $\mathsf{Dec}^{\mathsf{hy}}$: on input a private key sk and a ciphertext $\langle c, c^{\prime}\rangle$ do:

  $\mathsf{Dec}^{\mathsf{hy}}$：输入私钥 $sk$ 和密文 $\langle c, c^{\prime}\rangle$ 时，执行：

   1. Compute $k := \mathsf{Decaps}_{sk}(c)$.

      计算 $k := \mathsf{Decaps}_{sk}(c)$。

   2. Output the message $m := \mathsf{Dec}_{k}^{\prime}(c^{\prime})$.

      输出消息 $m := \mathsf{Dec}_{k}^{\prime}(c^{\prime})$。

Hybrid encryption using the KEM/DEM paradigm.

采用 KEM/DEM 范式的混合加密。

Assume $|m| > n$, which is the interesting case. Then the cost, per bit of plaintext, of encrypting a message $m$ using $\Pi^{hy}$ is

设 $|m| > n$（这才是有意义的情形），那么用 $\Pi^{hy}$ 加密消息 $m$ 时，分摊到每比特明文的加密开销为

$$
\frac{\alpha+\beta\cdot|m|}{|m|}=\frac{\alpha}{|m|}+\beta, \tag{12.8}
$$

which approaches $\beta$ for sufficiently long $m$. In the limit of very long messages, then, the cost per bit incurred by the public-key encryption scheme $\Pi^{hy}$ is the same as the cost per bit of the private-key scheme $\Pi^{\prime}$. Hybrid encryption thus allows us to achieve the functionality of public-key encryption at the efficiency of private-key encryption, at least for sufficiently long messages.

当 $m$ 足够长时，上式趋于 $\beta$。因此在消息极长的极限下，公钥加密方案 $\Pi^{hy}$ 的每比特开销与私钥方案 $\Pi^{\prime}$ 的每比特开销相同。由此可见，至少对足够长的消息，混合加密使我们能够以私钥加密的效率实现公钥加密的功能。

A similar calculation can be used to measure the effect of hybrid encryption on the ciphertext length. For some fixed value of $n$, let $L$ denote the length of the ciphertext output by $\mathsf{Encaps}$, and say the private-key encryption of a message $m$ using $\mathsf{Enc}^{\prime}$ results in a ciphertext of length $n + |m|$ (this can be achieved using one of the modes of encryption discussed in Section 3.6; actually, even ciphertext length $|m|$ is possible since, as we will see, $\Pi^{\prime}$ need not be CPA-secure). Then the total length of a ciphertext in scheme $\Pi^{hy}$ is

类似的计算也可以用来衡量混合加密对密文长度的影响。对某个固定的 $n$ 值，令 $L$ 表示 $\mathsf{Encaps}$ 输出的密文长度，并设用 $\mathsf{Enc}^{\prime}$ 对消息 $m$ 做私钥加密所得密文的长度为 $n + |m|$（用 3.6 节讨论的某种加密模式即可做到；实际上，密文长度甚至可以为 $|m|$，因为正如我们将看到的，$\Pi^{\prime}$ 无需满足选择明文安全）。那么方案 $\Pi^{hy}$ 中密文的总长度为

$$
L+n+\left|m\right|. \tag{12.9}
$$

In contrast, when using block-by-block encryption as in Equation (12.1), and assuming that public-key encryption of an $n$-bit message using $\mathsf{Enc}$ results in a ciphertext of length $L$, encryption of a message $m$ would result in a ciphertext of length $L \cdot \lceil |m|/n \rceil$. The ciphertext length given by Equation (12.9) is a significant improvement for sufficiently long $m$.

相比之下，若像式 (12.1) 那样逐块加密，并假设用 $\mathsf{Enc}$ 对 $n$ 比特消息做公钥加密得到长度为 $L$ 的密文，则加密消息 $m$ 所得的密文长度为 $L \cdot \lceil |m|/n \rceil$。对于足够长的 $m$，式 (12.9) 给出的密文长度是一个显著的改进。

We can use some rough estimates to get a sense for what the above results mean in practice. (We stress that these numbers are only meant to give the reader a feel for the improvement; realistic values would depend on a variety of factors.) A typical value for the length of the key $k$ might be $n = 128$. Furthermore, a “base” public-key encryption scheme might yield 256-bit ciphertexts when encrypting 128-bit messages; assume a KEM has ciphertexts of the same length when encapsulating a 128-bit key. Letting $\alpha$, as before, denote the computational cost of public-key encryption/encapsulation of a 128-bit key, we see that block-by-block encryption as in Equation (12.1) would encrypt a 1 Mb ( $\approx 2^{20}$-bit) message with computational cost $\alpha \cdot \lceil 2^{20}/128 \rceil \approx 8200 \cdot \alpha$ and the ciphertext would be 2 MB long. Compare this to the efficiency of hybrid encryption. Letting $\beta$, as before, denote the per-bit computational cost of private-key encryption, a reasonable approximation is $\beta \approx \alpha/2^{11}$. Using Equation (12.8), we see that the overall computational cost for hybrid encryption for a 1 Mb message is

我们可以通过一些粗略估计来体会上述结果在实践中意味着什么。（我们强调，这些数字只是为了让读者直观感受改进的幅度；实际数值取决于多种因素。）密钥 $k$ 的典型长度可能是 $n = 128$。此外，“基础”公钥加密方案加密 128 比特消息时可能产生 256 比特的密文；假设 KEM 封装 128 比特密钥时密文长度与此相同。与前面一样，令 $\alpha$ 表示对 128 比特密钥做公钥加密/封装的计算开销，可以看到，如式 (12.1) 那样逐块加密一条 1 Mb（$\approx 2^{20}$ 比特）消息的计算开销为 $\alpha \cdot \lceil 2^{20}/128 \rceil \approx 8200 \cdot \alpha$，且密文长达 2 MB。再对比混合加密的效率：与前面一样，令 $\beta$ 表示私钥加密每比特的计算开销，合理的近似为 $\beta \approx \alpha/2^{11}$。由式 (12.8) 可知，混合加密一条 1 Mb 消息的总计算开销为

$$
\alpha+2^{20}\cdot\frac{\alpha}{2^{11}}\approx512\cdot\alpha,
$$

and the ciphertext would be only slightly longer than 1 MB. Thus, hybrid encryption improves the computational efficiency in this case by a factor of 16, and the ciphertext length by a factor of 2.

而密文仅比 1 MB 略长。因此在这一情形下，混合加密把计算效率提高了 16 倍，把密文长度缩短了一半。

It remains to analyze the security of $\Pi^{hy}$. This, of course, depends on the security of its underlying components $\Pi$ and $\Pi^{\prime}$. In the following sections we define notions of CPA-security and CCA-security for KEMs, and show:

剩下的工作是分析 $\Pi^{hy}$ 的安全性。这当然取决于其底层组件 $\Pi$ 和 $\Pi^{\prime}$ 的安全性。接下来几节将定义 KEM 的选择明文安全与选择密文安全概念，并证明：

If $\Pi$ is a CPA-secure KEM and the private-key scheme $\Pi^{\prime}$ is EAV-secure, then $\Pi^{\mathrm{hy}}$ is a CPA-secure public-key encryption scheme. Notice that it suffices for $\Pi^{\prime}$ to satisfy a weaker definition of security—which, recall, does not imply CPA-security in the private-key setting—in order for the hybrid scheme $\Pi^{\mathrm{hy}}$ to be CPA-secure. Intuitively, the reason is that a fresh, uniform key $k$ is chosen each time a new message is encrypted. Since each key $k$ is used only once, security of $\Pi^{\prime}$ for a single encryption suffices for CPA-security of the hybrid scheme $\Pi^{\mathrm{hy}}$. This means that basic private-key encryption using a pseudorandom generator (or stream cipher), as in Construction 3.17, suffices.

若 $\Pi$ 是选择明文安全的 KEM，且私钥方案 $\Pi^{\prime}$ 是 EAV 安全的，则 $\Pi^{\mathrm{hy}}$ 是选择明文安全的公钥加密方案。注意，$\Pi^{\prime}$ 只需满足一个较弱的安全性定义即可——回顾一下，在私钥情形中它并不蕴含选择明文安全——这足以使混合方案 $\Pi^{\mathrm{hy}}$ 达到选择明文安全。直观的原因在于：每次加密新消息时都会选取一个新的均匀密钥 $k$。由于每个密钥 $k$ 只使用一次，$\Pi^{\prime}$ 对单次加密的安全性就足以保证混合方案 $\Pi^{\mathrm{hy}}$ 的选择明文安全。这也意味着，采用伪随机生成器（或流密码）的基础私钥加密（如构造 3.17）就已足够。

If $\Pi$ is a CCA-secure KEM and $\Pi^{\prime}$ is a CCA-secure private-key encryption scheme, then $\Pi^{hy}$ is a CCA-secure public-key encryption scheme.

若 $\Pi$ 是选择密文安全的 KEM，且 $\Pi^{\prime}$ 是选择密文安全的私钥加密方案，则 $\Pi^{hy}$ 是选择密文安全的公钥加密方案。

### 12.3.1 CPA-Security　选择明文安全

For simplicity, we assume in this and the next section a KEM with key length $n$. We define a notion of CPA-security for KEMs by analogy with Definition 12.2. As there, the adversary here eavesdrops on a single ciphertext $c$. Definition 12.2 requires that the attacker is unable to distinguish whether $c$ is an encryption of some message $m_0$ or some other message $m_1$. With a KEM, there is no message, and we require instead that the encapsulated key $k$ is indistinguishable from a uniform key that is independent of the ciphertext c.

为简单起见，本节及下一节均假设 KEM 的密钥长度为 $n$。仿照定义 12.2，我们为 KEM 定义一种选择明文安全的概念。与那里一样，这里的敌手窃听单条密文 $c$。定义 12.2 要求攻击者无法区分 $c$ 是某条消息 $m_0$ 还是另一条消息 $m_1$ 的加密；而对 KEM 来说并不涉及消息，我们改为要求被封装的密钥 $k$ 与一个独立于密文 $c$ 的均匀密钥不可区分。

Let $\Pi = (\mathsf{Gen}, \mathsf{Encaps}, \mathsf{Decaps})$ be a KEM and A an arbitrary adversary.

设 $\Pi = (\mathsf{Gen}, \mathsf{Encaps}, \mathsf{Decaps})$ 为一个 KEM，$\mathcal{A}$ 为任意敌手。

**The CPA indistinguishability experiment $\mathsf{KEM}_{\mathcal{A},\Pi}^{\mathsf{cpa}}(n)$:**

**选择明文不可区分实验 $\mathsf{KEM}_{\mathcal{A},\Pi}^{\mathsf{cpa}}(n)$：**

1. $\mathsf{Gen}({1}^n)$ is run to obtain keys $(pk, sk)$. Then $\mathsf{Encaps}_{pk}(1^n)$ is run to generate $(c, k)$ with $k \in \{0,1\}^n$.

   运行 $\mathsf{Gen}({1}^n)$ 得到密钥 $(pk, sk)$。然后运行 $\mathsf{Encaps}_{pk}(1^n)$ 生成 $(c, k)$，其中 $k \in \{0,1\}^n$。

2. A uniform bit $b \in \{0,1\}$ is chosen. If $b = 0$ set $\hat{k} := k$. If $b = 1$ then choose a uniform $\hat{k} \in \{0,1\}^n$.

   均匀选取一个比特 $b \in \{0,1\}$。若 $b = 0$，置 $\hat{k} := k$；若 $b = 1$，则均匀选取 $\hat{k} \in \{0,1\}^n$。

3. Give $(pk,c,\hat{k})$ to $\mathcal{A}$, who outputs a bit $b^{\prime}$. The output of the experiment is defined to be 1 if $b^{\prime}=b$, and 0 otherwise.

   将 $(pk,c,\hat{k})$ 交给 $\mathcal{A}$，$\mathcal{A}$ 输出一个比特 $b^{\prime}$。若 $b^{\prime}=b$，则实验输出定义为 1；否则为 0。

In the experiment, $\mathcal{A}$ is given the ciphertext $c$ and either the actual key $k$ corresponding to $c$, or an independent, uniform key. The KEM is CPA-secure if no efficient adversary can distinguish between these possibilities.

在该实验中，$\mathcal{A}$ 得到密文 $c$，以及与 $c$ 对应的真实密钥 $k$ 或一个独立的均匀密钥。如果没有高效敌手能区分这两种情况，就称该 KEM 是选择明文安全的。

DEFINITION 12.11 A key-encapsulation mechanism $\Pi$ is CPA-secure if for all probabilistic polynomial-time adversaries $\mathcal{A}$ there exists a negligible function $\mathsf{negl}$ such that

定义 12.11　称密钥封装机制 $\Pi$ 是选择明文安全的，如果对所有概率多项式时间敌手 $\mathcal{A}$，都存在可忽略函数 $\mathsf{negl}$ 使得

$$
\Pr[\mathsf{KEM}_{\mathcal{A},\Pi}^{\mathsf{cpa}}(n)=1]\leq\frac{1}{2}+\mathsf{negl}(n).
$$

In the remainder of this section we prove the following theorem:

本节余下部分证明如下定理：

THEOREM 12.12 If $\Pi$ is a CPA-secure KEM and $\Pi^{\prime}$ is an EAV-secure private-key encryption scheme, then $\Pi^{hy}$ as in Construction 12.10 is a CPA-secure public-key encryption scheme.

定理 12.12　若 $\Pi$ 是选择明文安全的 KEM，且 $\Pi^{\prime}$ 是 EAV 安全的私钥加密方案，则构造 12.10 中的 $\Pi^{hy}$ 是选择明文安全的公钥加密方案。

Before proving the theorem formally, we give some intuition. Let the notation “ $X \overset{c}{\equiv} Y$” mean that no polynomial-time adversary can distinguish between two distributions $X$ and $Y$. (This concept is treated more formally in Section 8.8, although we do not rely on that section here.) For example, let $\mathsf{Encaps}_{pk}^{(1)}(1^n)$ (resp., $\mathsf{Encaps}_{pk}^{(2)}(1^n)$) denote the ciphertext (resp., key) output by $\mathsf{Encaps}$. The fact that $\Pi$ is CPA-secure means that

在正式证明定理之前，先给出一些直观解释。记号 “$X \overset{c}{\equiv} Y$” 表示没有多项式时间敌手能够区分两个分布 $X$ 和 $Y$。（这一概念在 8.8 节中有更正式的处理，不过这里并不依赖那一节。）例如，令 $\mathsf{Encaps}_{pk}^{(1)}(1^n)$（相应地，$\mathsf{Encaps}_{pk}^{(2)}(1^n)$）表示 $\mathsf{Encaps}$ 输出的密文（相应地，密钥）。$\Pi$ 是选择明文安全的意味着

$$
\left(pk,\mathsf{Encaps}_{pk}(1^{n})\right)\stackrel{\mathrm{c}}{=}\left(pk,\mathsf{Encaps}_{pk}^{(1)}(1^{n}),k^{\prime}\right),
$$

where $pk$ is generated by $\mathsf{Gen}(1^n)$ and $k^{\prime}$ is chosen independently and uniformly from $\{0,1\}^n$. Similarly, the fact that $\Pi^{\prime}$ is EAV-secure means that for any $m_0, m_1$ output by $\mathcal{A}$ we have $\mathsf{Enc}_k^{\prime}(m_0) \stackrel{\mathrm{c}}{\equiv} \mathsf{Enc}_k^{\prime}(m_1)$ if $k$ is chosen uniformly at random.

其中 $pk$ 由 $\mathsf{Gen}(1^n)$ 生成，$k^{\prime}$ 是从 $\{0,1\}^n$ 中独立、均匀选取的。类似地，$\Pi^{\prime}$ 是 EAV 安全的意味着：对 $\mathcal{A}$ 输出的任意 $m_0, m_1$，只要 $k$ 是均匀随机选取的，就有 $\mathsf{Enc}_k^{\prime}(m_0) \stackrel{\mathrm{c}}{\equiv} \mathsf{Enc}_k^{\prime}(m_1)$。

$$
\begin{array}{l}
\left(pk,\mathsf{Encaps}_{pk}^{(1)}(1^{n}),\mathsf{Enc}_{k}^{\prime}(m_{0})\right)\xleftarrow{\text{(by security of }\Pi\text{)}}\left(pk,\mathsf{Encaps}_{pk}^{(1)}(1^{n}),\mathsf{Enc}_{k}^{\prime}(m_{1})\right)\\
\text{(by transitivity)}\\
\left(pk,\mathsf{Encaps}_{pk}^{(1)}(1^{n}),\mathsf{Enc}_{k^{\prime}}^{\prime}(m_{0})\right)\xleftarrow{\text{(by security of }\Pi^{\prime}\text{)}}\left(pk,\mathsf{Encaps}_{pk}^{(1)}(1^{n}),\mathsf{Enc}_{k^{\prime}}^{\prime}(m_{1})\right)
\end{array}
$$

**FIGURE 12.3: High-level structure of the proof of Theorem 12.12 (the arrows represent indistinguishability). / 图 12.3：定理 12.12 证明的高层结构（箭头表示不可区分性）**

In order to prove CPA-security of $\Pi^{hy}$ we need to show that

为了证明 $\Pi^{hy}$ 的选择明文安全，我们需要证明

$$
\left(pk,\mathsf{Encaps}_{pk}^{(1)}(1^{n}),\mathsf{Enc}_{k}^{\prime}(m_{0})\right)\stackrel{\mathrm{c}}{=}\left(pk,\mathsf{Encaps}_{pk}^{(1)}(1^{n}),\mathsf{Enc}_{k}^{\prime}(m_{1})\right) \tag{12.10}
$$

for $m_0, m_1$ output by a PPT adversary $\mathcal{A}$, where $k = \mathsf{Encaps}_{pk}^{(2)}(1^n)$. (Equation (12.10) shows that $\Pi^{\mathrm{hy}}$ has indistinguishable encryptions in the presence of an eavesdropper; by Proposition 12.3 this implies that $\Pi^{\mathrm{hy}}$ is CPA-secure.)

对 PPT 敌手 $\mathcal{A}$ 输出的 $m_0, m_1$ 成立，其中 $k = \mathsf{Encaps}_{pk}^{(2)}(1^n)$。（式 (12.10) 表明 $\Pi^{\mathrm{hy}}$ 在窃听者存在下具有不可区分的加密；由命题 12.3，这蕴含 $\Pi^{\mathrm{hy}}$ 是选择明文安全的。）

The proof proceeds in three steps. (See Figure 12.3.) First we prove that

证明分三步进行。（见图 12.3。）首先证明

$$
\left(pk,\mathsf{Encaps}_{pk}^{(1)}(1^{n}),\mathsf{Enc}_{k}^{\prime}(m_{0})\right)\stackrel{\mathrm{c}}{=}\left(pk,\mathsf{Encaps}_{pk}^{(1)}(1^{n}),\mathsf{Enc}_{k^{\prime}}^{\prime}(m_{0})\right), \tag{12.11}
$$

where on the left $k$ is output by $\mathsf{Encaps}_{pk}^{(2)}(1^n)$, and on the right $k^{\prime}$ is an independent, uniform key. This follows via a fairly straightforward reduction, since CPA-security of $\Pi$ means exactly that $\mathsf{Encaps}_{pk}^{(2)}(1^n)$ cannot be distinguished from a uniform key $k^{\prime}$ even given $pk$ and $\mathsf{Encaps}_{pk}^{(1)}(1^n)$.

其中左边的 $k$ 由 $\mathsf{Encaps}_{pk}^{(2)}(1^n)$ 输出，右边的 $k^{\prime}$ 是一个独立的均匀密钥。这一步通过一个相当直接的归约即可得到，因为 $\Pi$ 的选择明文安全恰好说明：即使给定 $pk$ 和 $\mathsf{Encaps}_{pk}^{(1)}(1^n)$，$\mathsf{Encaps}_{pk}^{(2)}(1^n)$ 也无法与均匀密钥 $k^{\prime}$ 区分。

Next, we prove that

接下来证明

$$
\left(pk,\mathsf{Encaps}_{pk}^{(1)}(1^{n}),\mathsf{Enc}_{k^{\prime}}^{\prime}(m_{0})\right)\stackrel{\mathrm{c}}{=}\left(pk,\mathsf{Encaps}_{pk}^{(1)}(1^{n}),\mathsf{Enc}_{k^{\prime}}^{\prime}(m_{1})\right). \tag{12.12}
$$

Here the difference is between encrypting $m_0$ or $m_1$ using $\Pi^{\prime}$ and a uniform, independent key $k^{\prime}$. Equation (12.12) follows since $\Pi^{\prime}$ is EAV-secure.

这里比较的是用 $\Pi^{\prime}$ 和一个均匀、独立的密钥 $k^{\prime}$ 分别加密 $m_0$ 与 $m_1$ 的差别。由于 $\Pi^{\prime}$ 是 EAV 安全的，式 (12.12) 成立。

Exactly as in the case of Equation (12.11), we can also show that

与式 (12.11) 的情形完全一样，我们还可以证明

$$
\left(pk,\mathsf{Encaps}_{pk}^{(1)}(1^{n}),\mathsf{Enc}_{k}^{\prime}(m_{1})\right)\stackrel{\mathrm{c}}{=}\left(pk,\mathsf{Encaps}_{pk}^{(1)}(1^{n}),\mathsf{Enc}_{k^{\prime}}^{\prime}(m_{1})\right), \tag{12.13}
$$

(where, again, on the left $k$ is output by $\mathsf{Encaps}_{pk}^{(2)}(1^n)$) using CPA-security of $\Pi$. Equations (12.11)–(12.13) imply, by transitivity, the desired result of Equation (12.10). (Transitivity will be implicit in the proof we give below.)

（同样，左边的 $k$ 由 $\mathsf{Encaps}_{pk}^{(2)}(1^n)$ 输出），这用到的是 $\Pi$ 的选择明文安全。由传递性，式 (12.11)–(12.13) 蕴含所需的式 (12.10)。（传递性在我们下面给出的证明中将隐式地用到。）

We now present the full proof.

下面给出完整证明。

PROOF (of Theorem 12.12) We prove that $\Pi^{hy}$ has indistinguishable encryptions in the presence of an eavesdropper; by Proposition 12.3, this implies it is CPA-secure.

证明（定理 12.12）　我们证明 $\Pi^{hy}$ 在窃听者存在下具有不可区分的加密；由命题 12.3，这蕴含它是选择明文安全的。

Fix an arbitrary PPT adversary $\mathcal{A}^{\mathsf{hy}}$, and consider experiment $\mathsf{PubK}_{\mathcal{A}^{\mathsf{hy}},\Pi^{\mathsf{hy}}}^{\mathsf{eav}}(n)$. Our goal is to prove that there is a negligible function $\mathsf{negl}$ such that

固定任意的 PPT 敌手 $\mathcal{A}^{\mathsf{hy}}$，考虑实验 $\mathsf{PubK}_{\mathcal{A}^{\mathsf{hy}},\Pi^{\mathsf{hy}}}^{\mathsf{eav}}(n)$。我们的目标是证明存在可忽略函数 $\mathsf{negl}$，使得

$$
\Pr[\mathsf{PubK}_{\mathcal{A}^{\mathsf{hy}},\Pi^{\mathsf{hy}}}^{\mathsf{eav}}(n)=1]\leq\frac{1}{2}+\mathsf{negl}(n).
$$

By definition of the experiment, we have

根据实验的定义，有

$$
\begin{aligned}
\Pr&[\mathsf{PubK}_{\mathcal{A}^{\mathsf{hy}},\Pi^{\mathsf{hy}}}^{\mathsf{eav}}(n)=1]\\
&=\frac{1}{2}\cdot\Pr[\mathcal{A}^{\mathsf{hy}}(pk,\mathsf{Encaps}_{pk}^{(1)}(1^{n}),\mathsf{Enc}_{k}^{\prime}(m_{0}))=0]\\
&\quad+\frac{1}{2}\cdot\Pr[\mathcal{A}^{\mathsf{hy}}(pk,\mathsf{Encaps}_{pk}^{(1)}(1^{n}),\mathsf{Enc}_{k}^{\prime}(m_{1}))=1],
\end{aligned} \tag{12.14}
$$

where in each case $k$ equals $\mathsf{Encaps}_{pk}^{(2)}(1^n)$. Consider the following PPT adversary $\mathcal{A}_1$ attacking $\Pi$.

其中每种情况下 $k$ 都等于 $\mathsf{Encaps}_{pk}^{(2)}(1^n)$。考虑如下攻击 $\Pi$ 的 PPT 敌手 $\mathcal{A}_1$。

Adversary $A_{1}$

敌手 $\mathcal{A}_1$

1. $A_1$ is given $(pk, c, \hat{k})$.

   $\mathcal{A}_1$ 获得 $(pk, c, \hat{k})$。

2. $\mathcal{A}_1$ runs $\mathcal{A}^{\mathsf{hy}}(pk)$ to obtain two messages $m_0, m_1$. Then $\mathcal{A}_1$ computes $c^{\prime} \leftarrow \mathsf{Enc}_{k}^{\prime}(m_0)$, gives ciphertext $\langle c, c^{\prime} \rangle$ to $\mathcal{A}^{\mathsf{hy}}$, and outputs the bit $b^{\prime}$ that $\mathcal{A}^{\mathsf{hy}}$ outputs.

   $\mathcal{A}_1$ 运行 $\mathcal{A}^{\mathsf{hy}}(pk)$ 得到两条消息 $m_0, m_1$。然后 $\mathcal{A}_1$ 计算 $c^{\prime} \leftarrow \mathsf{Enc}_{k}^{\prime}(m_0)$，把密文 $\langle c, c^{\prime} \rangle$ 交给 $\mathcal{A}^{\mathsf{hy}}$，并输出 $\mathcal{A}^{\mathsf{hy}}$ 输出的比特 $b^{\prime}$。

Consider the behavior of $\mathcal{A}_1$ when attacking $\Pi$ in experiment $\mathsf{KEM}_{\mathcal{A}_1,\Pi}^{\mathsf{cpa}}(n)$. When $b=0$ in that experiment, then $\mathcal{A}_1$ is given $(pk,c,\hat{k})$ where $c$ and $\hat{k}$ were both output by $\mathsf{Encaps}_{pk}(1^n)$. This means that $\mathcal{A}^{\mathsf{hy}}$ is given a ciphertext of the form $\langle c,c^{\prime}\rangle=\langle c,\mathsf{Enc}_{k}^{\prime}(m_0)\rangle$, where $k$ is the key encapsulated by $c$. So,

考虑 $\mathcal{A}_1$ 在实验 $\mathsf{KEM}_{\mathcal{A}_1,\Pi}^{\mathsf{cpa}}(n)$ 中攻击 $\Pi$ 时的行为。当该实验中 $b=0$ 时，$\mathcal{A}_1$ 得到 $(pk,c,\hat{k})$，其中 $c$ 和 $\hat{k}$ 都是由 $\mathsf{Encaps}_{pk}(1^n)$ 输出的。这意味着 $\mathcal{A}^{\mathsf{hy}}$ 得到的密文形如 $\langle c,c^{\prime}\rangle=\langle c,\mathsf{Enc}_{k}^{\prime}(m_0)\rangle$，其中 $k$ 是被 $c$ 封装的密钥。于是，

$$
\Pr[\mathcal{A}_{1}\text{ outputs }0\mid b=0]=\Pr[\mathcal{A}^{\mathsf{hy}}(pk,\mathsf{Encaps}_{pk}^{(1)}(1^{n}),\mathsf{Enc}_{k}^{\prime}(m_{0}))=0].
$$

On the other hand, when $b = 1$ in experiment $\mathsf{KEM}_{\mathcal{A}_1,\Pi}^{\mathsf{cpa}}(n)$ then $\mathcal{A}_1$ is given $(pk, c, \hat{k})$ with $\hat{k}$ uniform and independent of $c$. If we denote such a key by $k^{\prime},$ this means $\mathcal{A}^{\mathsf{hy}}$ is given a ciphertext of the form $\langle c, \mathsf{Enc}_{k^{\prime}}^{\prime}(m_0) \rangle$, and

另一方面，当实验 $\mathsf{KEM}_{\mathcal{A}_1,\Pi}^{\mathsf{cpa}}(n)$ 中 $b = 1$ 时，$\mathcal{A}_1$ 得到 $(pk, c, \hat{k})$，其中 $\hat{k}$ 均匀且独立于 $c$。若把这个密钥记作 $k^{\prime}$，则意味着 $\mathcal{A}^{\mathsf{hy}}$ 得到的密文形如 $\langle c, \mathsf{Enc}_{k^{\prime}}^{\prime}(m_0) \rangle$，于是

$$
\Pr[\mathcal{A}_{1}\text{ outputs }1\mid b=1]=\Pr[\mathcal{A}^{\mathsf{hy}}(pk,\mathsf{Encaps}_{pk}^{(1)}(1^{n}),\mathsf{Enc}_{k^{\prime}}^{\prime}(m_{0}))=1].
$$

Since $\Pi$ is a CPA-secure KEM, there is a negligible function $\mathsf{negl}_1$ such that

由于 $\Pi$ 是选择明文安全的 KEM，存在可忽略函数 $\mathsf{negl}_1$ 使得

$$
\begin{aligned}
\frac{1}{2}+\mathsf{negl}_{1}(n)&\geq\Pr[\mathsf{KEM}_{\mathcal{A}_{1},\Pi}^{\mathsf{cpa}}(n)=1]\\
&=\frac{1}{2}\cdot\Pr[\mathcal{A}_{1}\text{ outputs }0\mid b=0]+\frac{1}{2}\cdot\Pr[\mathcal{A}_{1}\text{ outputs }1\mid b=1]\\
&=\frac{1}{2}\cdot\Pr[\mathcal{A}^{\mathsf{hy}}(pk,\mathsf{Encaps}_{pk}^{(1)}(1^{n}),\mathsf{Enc}_{k}^{\prime}(m_{0}))=0]\\
&\quad+\frac{1}{2}\cdot\Pr[\mathcal{A}^{\mathsf{hy}}(pk,\mathsf{Encaps}_{pk}^{(1)}(1^{n}),\mathsf{Enc}_{k^{\prime}}^{\prime}(m_{0}))=1]
\end{aligned} \tag{12.15}
$$

where $k$ is equal to $\mathsf{Encaps}_{pk}^{(2)}(1^{n})$ and $k^{\prime}$ is a uniform and independent key.

其中 $k$ 等于 $\mathsf{Encaps}_{pk}^{(2)}(1^{n})$，而 $k^{\prime}$ 是一个均匀且独立的密钥。

Next, consider the following PPT adversary $\mathcal{A}^{\prime}$ that eavesdrops on a message encrypted using the private-key scheme $\Pi^{\prime}$.

接下来考虑如下的 PPT 敌手 $\mathcal{A}^{\prime}$，它窃听用私钥方案 $\Pi^{\prime}$ 加密的消息。

Adversary A':

敌手 $\mathcal{A}^{\prime}$：

1. $\mathcal{A}^{\prime}(1^n)$ runs $\mathsf{Gen}(1^n)$ on its own to generate keys $(pk, sk)$. It also computes $c \leftarrow \mathsf{Encaps}_{pk}^{(1)}(1^n)$.

   $\mathcal{A}^{\prime}(1^n)$ 自己运行 $\mathsf{Gen}(1^n)$ 生成密钥 $(pk, sk)$。它还计算 $c \leftarrow \mathsf{Encaps}_{pk}^{(1)}(1^n)$。

2. $\mathcal{A}^{\prime}$ runs $\mathcal{A}^{\mathsf{hy}}(pk)$ to obtain two messages $m_0, m_1$. These are output by $\mathcal{A}^{\prime}$, and it is given in return a ciphertext $c^{\prime}$.

   $\mathcal{A}^{\prime}$ 运行 $\mathcal{A}^{\mathsf{hy}}(pk)$ 得到两条消息 $m_0, m_1$。这两条消息由 $\mathcal{A}^{\prime}$ 输出，作为回应它会收到一个密文 $c^{\prime}$。

3. $\mathcal{A}^{\prime}$ gives the ciphertext $\langle c, c^{\prime} \rangle$ to $\mathcal{A}^{\mathsf{hy}}$, and outputs the bit $b^{\prime}$ that $\mathcal{A}^{\mathsf{hy}}$ outputs.

   $\mathcal{A}^{\prime}$ 把密文 $\langle c, c^{\prime} \rangle$ 交给 $\mathcal{A}^{\mathsf{hy}}$，并输出 $\mathcal{A}^{\mathsf{hy}}$ 输出的比特 $b^{\prime}$。

When $b = 0$ in experiment $\mathsf{PrivK}_{\mathcal{A}^{\prime},\Pi^{\prime}}^{\mathsf{eav}}(n)$, adversary $\mathcal{A}^{\prime}$ is given a ciphertext $c^{\prime}$ which is an encryption of $m_0$ using a key $k^{\prime}$ that is uniform and independent of anything else. So $\mathcal{A}^{\mathsf{hy}}$ is given a ciphertext of the form $\langle c, \mathsf{Enc}_{k^{\prime}}^{\prime}(m_0)\rangle$ where $k^{\prime}$ is uniform and independent of $c$, and

当实验 $\mathsf{PrivK}_{\mathcal{A}^{\prime},\Pi^{\prime}}^{\mathsf{eav}}(n)$ 中 $b = 0$ 时，敌手 $\mathcal{A}^{\prime}$ 得到的密文 $c^{\prime}$ 是用某个均匀且独立于其他一切的密钥 $k^{\prime}$ 对 $m_0$ 加密的结果。于是 $\mathcal{A}^{\mathsf{hy}}$ 得到形如 $\langle c, \mathsf{Enc}_{k^{\prime}}^{\prime}(m_0)\rangle$ 的密文，其中 $k^{\prime}$ 均匀且独立于 $c$，故

$$
\Pr[\mathcal{A}^{\prime}\text{ outputs }0\mid b=0]=\Pr[\mathcal{A}^{\mathsf{hy}}(pk,\mathsf{Encaps}_{pk}^{(1)}(1^{n}),\mathsf{Enc}_{k^{\prime}}^{\prime}(m_{0}))=0].
$$

On the other hand, when $b = 1$ in experiment $\mathsf{PrivK}_{\mathcal{A}^{\prime},\Pi^{\prime}}^{\mathsf{eav}}(n)$, then $\mathcal{A}^{\prime}$ is given an encryption of $m_1$ using a uniform, independent key $k^{\prime}$. This means $\mathcal{A}^{\mathsf{hy}}$ is given a ciphertext of the form $\langle c, \mathsf{Enc}_{k^{\prime}}^{\prime}(m_1)\rangle$ and so

另一方面，当实验 $\mathsf{PrivK}_{\mathcal{A}^{\prime},\Pi^{\prime}}^{\mathsf{eav}}(n)$ 中 $b = 1$ 时，$\mathcal{A}^{\prime}$ 得到的是用一个均匀、独立的密钥 $k^{\prime}$ 对 $m_1$ 加密的结果。这意味着 $\mathcal{A}^{\mathsf{hy}}$ 得到形如 $\langle c, \mathsf{Enc}_{k^{\prime}}^{\prime}(m_1)\rangle$ 的密文，因此

$$
\Pr[\mathcal{A}^{\prime}\text{ outputs }1\mid b=1]=\Pr[\mathcal{A}^{\mathsf{hy}}(pk,\mathsf{Encaps}_{pk}^{(1)}(1^{n}),\mathsf{Enc}_{k^{\prime}}^{\prime}(m_{1}))=1].
$$

Since $\Pi^{\prime}$ is EAV-secure, there is a negligible function $\mathsf{negl}^{\prime}$ such that

由于 $\Pi^{\prime}$ 是 EAV 安全的，存在可忽略函数 $\mathsf{negl}^{\prime}$ 使得

$$
\begin{aligned}
\frac{1}{2}+\mathsf{negl}^{\prime}(n)&\geq\Pr[\mathsf{PrivK}_{\mathcal{A}^{\prime},\Pi^{\prime}}^{\mathsf{eav}}(n)=1]\\
&=\frac{1}{2}\cdot\Pr[\mathcal{A}^{\prime}\text{ outputs }0\mid b=0]+\frac{1}{2}\cdot\Pr[\mathcal{A}^{\prime}\text{ outputs }1\mid b=1]\\
&=\frac{1}{2}\cdot\Pr[\mathcal{A}^{\mathsf{hy}}(pk,\mathsf{Encaps}_{pk}^{(1)}(1^{n}),\mathsf{Enc}_{k^{\prime}}^{\prime}(m_{0}))=0]\\
&\quad+\frac{1}{2}\cdot\Pr[\mathcal{A}^{\mathsf{hy}}(pk,\mathsf{Encaps}_{pk}^{(1)}(1^{n}),\mathsf{Enc}_{k^{\prime}}^{\prime}(m_{1}))=1].
\end{aligned} \tag{12.16}
$$

Proceeding exactly as we did to prove Equation (12.15), one can show there is a negligible function $\mathsf{negl}_2$ such that

完全按照证明式 (12.15) 时所做的那样进行，可以证明存在可忽略函数 $\mathsf{negl}_2$ 使得

$$
\begin{aligned}
\frac{1}{2}+\mathsf{negl}_{2}(n)&\geq\Pr[\mathsf{KEM}_{\mathcal{A}_{2},\Pi}^{\mathsf{cpa}}(n)=1]\\
&=\frac{1}{2}\cdot\Pr[\mathcal{A}_{2}\text{ outputs }0\mid b=0]+\frac{1}{2}\cdot\Pr[\mathcal{A}_{2}\text{ outputs }1\mid b=1]\\
&=\frac{1}{2}\cdot\Pr[\mathcal{A}^{\mathsf{hy}}(pk,\mathsf{Encaps}_{pk}^{(1)}(1^{n}),\mathsf{Enc}_{k}^{\prime}(m_{1}))=1]\\
&\quad+\frac{1}{2}\cdot\Pr[\mathcal{A}^{\mathsf{hy}}(pk,\mathsf{Encaps}_{pk}^{(1)}(1^{n}),\mathsf{Enc}_{k^{\prime}}^{\prime}(m_{1}))=0].
\end{aligned} \tag{12.17}
$$

Summing Equations (12.15)–(12.17) and using the fact that the sum of three negligible functions is negligible, we see there exists a negligible function $\mathsf{negl}$ such that

将式 (12.15)–(12.17) 相加，并利用三个可忽略函数之和仍是可忽略函数这一事实，可知存在可忽略函数 $\mathsf{negl}$ 使得

$$
\begin{aligned}
\frac{3}{2}&+\mathsf{negl}(n)\geq\\
\frac{1}{2}&\cdot\Big(\Pr[\mathcal{A}^{\mathsf{hy}}(pk,c,\mathsf{Enc}_{k}^{\prime}(m_{0}))=0]+\Pr[\mathcal{A}^{\mathsf{hy}}(pk,c,\mathsf{Enc}_{k^{\prime}}^{\prime}(m_{0}))=1]\\
&+\Pr[\mathcal{A}^{\mathsf{hy}}(pk,c,\mathsf{Enc}_{k^{\prime}}^{\prime}(m_{0}))=0]+\Pr[\mathcal{A}^{\mathsf{hy}}(pk,c,\mathsf{Enc}_{k^{\prime}}^{\prime}(m_{1}))=1]\\
&+\Pr[\mathcal{A}^{\mathsf{hy}}(pk,c,\mathsf{Enc}_{k}^{\prime}(m_{1}))=1]+\Pr[\mathcal{A}^{\mathsf{hy}}(pk,c,\mathsf{Enc}_{k^{\prime}}^{\prime}(m_{1}))=0]\Big),
\end{aligned}
$$

where $c = \mathsf{Encaps}_{pk}^{(1)}(1^n)$ in all the above. Note that

其中上述所有式子中都有 $c = \mathsf{Encaps}_{pk}^{(1)}(1^n)$。注意到

$$
\Pr[\mathcal{A}^{\mathsf{hy}}(pk,c,\mathsf{Enc}_{k^{\prime}}^{\prime}(m_{0}))=1]+\Pr[\mathcal{A}^{\mathsf{hy}}(pk,c,\mathsf{Enc}_{k^{\prime}}^{\prime}(m_{0}))=0]=1,
$$

since the probabilities of complementary events always sum to 1. Similarly,

因为互补事件的概率之和总是为 1。类似地，

$$
\Pr[\mathcal{A}^{\mathsf{hy}}(pk,c,\mathsf{Enc}_{k^{\prime}}^{\prime}(m_{1}))=1]+\Pr[\mathcal{A}^{\mathsf{hy}}(pk,c,\mathsf{Enc}_{k^{\prime}}^{\prime}(m_{1}))=0]=1.
$$

Therefore,

因此，

$$
\begin{aligned}
&\frac{1}{2}+\mathsf{negl}(n)\\
&\geq\frac{1}{2}\cdot\Big(\Pr[\mathcal{A}^{\mathsf{hy}}(pk,c,\mathsf{Enc}_{k}^{\prime}(m_{0}))=0]+\Pr[\mathcal{A}^{\mathsf{hy}}(pk,c,\mathsf{Enc}_{k}^{\prime}(m_{1}))=1]\Big)\\
&=\Pr[\mathsf{PubK}_{\mathcal{A}^{\mathsf{hy}},\Pi^{\mathsf{hy}}}^{\mathsf{eav}}(n)=1]
\end{aligned}
$$

(using Equation (12.14) for the last equality), proving the theorem.

（最后一个等号用了式 (12.14)），定理得证。

### 12.3.2 CCA-Security　选择密文安全

If the private-key encryption scheme $\Pi^{\prime}$ is not itself secure against chosen-ciphertext attacks, then (regardless of the KEM used) neither is the resulting hybrid encryption scheme $\Pi^{hy}$. As a simple, illustrative example, say we take Construction 3.17 as our private-key encryption scheme. Then, leaving the KEM unspecified, encryption of a message $m$ by $\Pi^{hy}$ is done by computing $(c, k) \leftarrow \mathsf{Encaps}_{pk}(1^n)$ and then outputting the ciphertext

如果私钥加密方案 $\Pi^{\prime}$ 自身不能抵抗选择密文攻击，那么（无论使用哪种 KEM）由此得到的混合加密方案 $\Pi^{hy}$ 同样不能。举一个简单的说明性例子：取构造 3.17 作为私钥加密方案。此时暂不指定 KEM，$\Pi^{hy}$ 对消息 $m$ 的加密方式是先计算 $(c, k) \leftarrow \mathsf{Encaps}_{pk}(1^n)$，然后输出密文

$$
\langle c,G(k)\oplus m\rangle,
$$

where $G$ is a pseudorandom generator. Given a ciphertext $\langle c, c^{\prime} \rangle$, an attacker can simply flip the last bit of $c^{\prime}$ to obtain a modified ciphertext that is a valid encryption of $m$ with its last bit flipped.

其中 $G$ 是伪随机生成器。给定密文 $\langle c, c^{\prime} \rangle$，攻击者只需翻转 $c^{\prime}$ 的最后一比特，就能得到一个修改后的密文，它是把 $m$ 的最后一比特翻转后所得消息的有效加密。

The natural way to fix this is to use a CCA-secure private-key encryption scheme. But this is clearly not enough if the KEM is susceptible to chosen-ciphertext attacks. Since we have not yet defined this notion, we do so now.

解决这一问题的自然办法是使用选择密文安全的私钥加密方案。但如果 KEM 本身容易受到选择密文攻击，这显然还不够。由于我们尚未定义这一概念，现在就来定义。

As in Definition 12.11, we require that an adversary given a ciphertext $c$ cannot distinguish the key $k$ encapsulated by that ciphertext from a uniform and independent key $k^{\prime}$. Now, however, we additionally allow the attacker to request decapsulation of ciphertexts of its choice (as long as they are different from the challenge ciphertext).

与定义 12.11 一样，我们要求敌手在给定密文 $c$ 后，无法区分该密文封装的密钥 $k$ 与一个均匀且独立的密钥 $k^{\prime}$。但现在我们还额外允许攻击者请求对其自行选择的密文进行解封装（只要这些密文不同于挑战密文）。

Formally, let $\mathcal{A}$ be an adversary and let $\Pi = (\mathsf{Gen}, \mathsf{Encaps}, \mathsf{Decaps})$ be a KEM with key length $n$, and consider the following experiment:

严格地说，设 $\mathcal{A}$ 为敌手，$\Pi = (\mathsf{Gen}, \mathsf{Encaps}, \mathsf{Decaps})$ 为密钥长度为 $n$ 的 KEM，考虑如下实验：

**The CCA indistinguishability experiment $\mathsf{KEM}_{\mathcal{A},\Pi}^{\mathsf{cca}}(n)$:**

**选择密文不可区分实验 $\mathsf{KEM}_{\mathcal{A},\Pi}^{\mathsf{cca}}(n)$：**

1. $\mathsf{Gen}(1^n)$ is run to obtain keys $(pk, sk)$. Then $\mathsf{Encaps}_{pk}(1^n)$ is run to generate $(c, k)$ with $k \in \{0,1\}^n$.

   运行 $\mathsf{Gen}(1^n)$ 得到密钥 $(pk, sk)$。然后运行 $\mathsf{Encaps}_{pk}(1^n)$ 生成 $(c, k)$，其中 $k \in \{0,1\}^n$。

2. Choose a uniform bit $b \in \{0,1\}$. If $b = 0$ set $\hat{k} := k$. If $b = 1$ then choose a uniform $\hat{k} \in \{0,1\}^n$.

   均匀选取一个比特 $b \in \{0,1\}$。若 $b = 0$，置 $\hat{k} := k$；若 $b = 1$，则均匀选取 $\hat{k} \in \{0,1\}^n$。

3. $\mathcal{A}$ is given ($pk$, $c$, $\hat{k}$) and access to an oracle $\mathsf{Decaps}_{sk}(\cdot)$, but may not request decapsulation of $c$ itself.

   $\mathcal{A}$ 获得 ($pk$, $c$, $\hat{k}$)，并可访问预言机 $\mathsf{Decaps}_{sk}(\cdot)$，但不得请求对 $c$ 本身解封装。

4. $\mathcal{A}$ outputs a bit $b'$. The output of the experiment is defined to be 1 if $b^{\prime} = b$, and 0 otherwise.

   $\mathcal{A}$ 输出一个比特 $b'$。若 $b^{\prime} = b$，则实验输出定义为 1；否则为 0。

DEFINITION 12.13 A key-encapsulation mechanism $\Pi$ is CCA-secure if for all probabilistic polynomial-time adversaries $\mathcal{A}$ there is a negligible function $\mathsf{negl}$ such that

定义 12.13　称密钥封装机制 $\Pi$ 是选择密文安全的，如果对所有概率多项式时间敌手 $\mathcal{A}$，都存在可忽略函数 $\mathsf{negl}$ 使得

$$
\Pr[\mathsf{KEM}_{\mathcal{A},\Pi}^{\mathsf{cca}}(n)=1]\leq\frac{1}{2}+\mathsf{negl}(n).
$$

Using a CCA-secure KEM in combination with a CCA-secure private-key encryption scheme results in a CCA-secure public-key encryption scheme.

将选择密文安全的 KEM 与选择密文安全的私钥加密方案结合使用，即可得到选择密文安全的公钥加密方案。

THEOREM 12.14 If $\Pi$ is a CCA-secure KEM and $\Pi^{\prime}$ is a CCA-secure private-key encryption scheme, then $\Pi^{hy}$ as in Construction 12.10 is a CCA-secure public-key encryption scheme.

定理 12.14　若 $\Pi$ 是选择密文安全的 KEM，且 $\Pi^{\prime}$ 是选择密文安全的私钥加密方案，则构造 12.10 中的 $\Pi^{hy}$ 是选择密文安全的公钥加密方案。

A proof is obtained by suitable modification of the proof of Theorem 12.12.

对定理 12.12 的证明作适当修改，即可得到本定理的证明。
