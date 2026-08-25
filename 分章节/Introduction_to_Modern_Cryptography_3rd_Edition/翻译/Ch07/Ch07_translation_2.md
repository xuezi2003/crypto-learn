## 7.2 Block Ciphers　7.2 分组密码

Recall from Section 3.5.1 that a block cipher is an efficient, keyed permutation $F: \{0,1\}^n \times \{0,1\}^\ell \to \{0,1\}^\ell$. This means the function $F_k$ defined by $F_k(x) \overset{\mathrm{def}}{=} F(k,x)$ is a bijection (i.e., a permutation), and moreover $F_k$ and its inverse $F_k^{-1}$ are efficiently computable given $k$. We refer to $n$ as the key length and $\ell$ as the block length of $F$, and here we explicitly allow them to differ. The key length and block length are now fixed constants, whereas in Chapter 3 they were viewed as functions of a security parameter. This puts us in the setting of concrete security rather than asymptotic security. $^{2}$ The concrete-security requirements for block ciphers are quite stringent, and a block cipher is generally only considered "secure" if the best known attack (without preprocessing) has time complexity roughly equivalent to a brute-force search for the key. Thus, if a cipher with key length $n = 256$ can be broken in time ${2}^{128}$, the cipher is (generally) considered insecure even though a ${2}^{128}$-time attack is infeasible. (In contrast, in an asymptotic setting an attack of complexity ${2}^{n/2}$ is not considered efficient since it requires exponential time, and thus a cipher where such an attack is possible might still qualify as a pseudorandom permutation.) This is because in the concrete setting we care about the actual complexity of attacks, and not just their asymptotic behavior. Furthermore, there is a concern that existence of a better-than-brute-force attack may indicate some more fundamental weakness in the design of the cipher.

回顾 3.5.1 节，分组密码是一个高效且带密钥的置换 $F: \{0,1\}^n \times \{0,1\}^\ell \to \{0,1\}^\ell$。这意味着由 $F_k(x) \overset{\mathrm{def}}{=} F(k,x)$ 定义的函数 $F_k$ 是一个双射（即一个置换），而且在给定 $k$ 的情况下 $F_k$ 及其逆 $F_k^{-1}$ 都是高效可计算的。我们将 $n$ 称为 $F$ 的密钥长度，将 $\ell$ 称为 $F$ 的分组长度，这里我们明确允许二者不同。现在密钥长度和分组长度都是固定的常数，而在第 3 章中它们被视为安全参数的函数。这使我们处于具体安全性的设定而非渐近安全性的设定。$^{2}$ 分组密码的具体安全性要求相当严格，通常只有当已知最佳攻击（不含预处理）的时间复杂度大致等同于穷举搜索密钥时，一个分组密码才被认为是“安全的”。因此，如果密钥长度为 $n = 256$ 的密码可以在 ${2}^{128}$ 的时间内被破解，那么该密码（一般而言）被认为是不安全的，即使 ${2}^{128}$ 时间的攻击是不可行的。（相比之下，在渐近设定中，复杂度为 ${2}^{n/2}$ 的攻击不被认为是高效的，因为它需要指数时间，因此存在这种攻击的密码仍然可能符合伪随机置换的条件。）这是因为在具体设定中，我们关心的是攻击的实际复杂度，而不仅仅是其渐近行为。此外，还有一个担忧：如果存在优于穷举的攻击，就可能表明密码设计中有更根本的弱点。

Block ciphers are designed to behave, at a minimum, as (strong) pseudo-random permutations; see Definition 3.27. (Often, block ciphers are designed and assumed to satisfy even stronger security properties, as we discuss in Section 7.3.1.) Modeling block ciphers as pseudorandom permutations allows proofs of security for constructions based on block ciphers, and also makes explicit the necessary requirements of a block cipher. A solid understanding of what block ciphers are supposed to achieve is instrumental in their design. The view that block ciphers should be modeled as pseudorandom permutations has, at least recently, served as a major influence in their design. As an example, the call for proposals for the Advanced Encryption Standard (AES) that we will encounter later in this chapter stated the following evaluation criterion:

分组密码的设计目标至少是要表现得像（强）伪随机置换；见定义 3.27。（通常，分组密码还被设计和假定为满足甚至更强的安全性质，正如我们在 7.3.1 节中讨论的那样。）将分组密码建模为伪随机置换，使得基于分组密码的构造可以进行安全性证明，同时也明确了一个分组密码的必要要求。扎实理解分组密码应当实现什么目标，对分组密码的设计至关重要。将分组密码建模为伪随机置换的观点，至少近年来已成为其设计的主要影响因素。例如，本章后面将要介绍的高级加密标准（AES），其提案征集就陈述了以下评估准则：

The security provided by an algorithm is the most important factor.... Algorithms will be judged on the following factors: ...

一个算法所提供的安全性是最重要的因素⋯⋯算法将根据以下因素来评判：⋯⋯

- The extent to which the algorithm output is indistinguishable from a random permutation ...

  算法输出与随机置换不可区分的程度⋯⋯

Modern block ciphers are suitable for all the constructions using pseudorandom permutations (or pseudorandom functions) we have seen in this book.

现代分组密码适用于本书中所有使用伪随机置换（或伪随机函数）的构造。

Notwithstanding the fact that block ciphers are not, on their own, encryption schemes, the standard terminology for attacks on a block cipher F is:

尽管分组密码本身不是加密方案，但对分组密码 F 的攻击的标准术语是：

- In a known-plaintext attack, the attacker is given pairs of inputs/outputs $\{(x_i, F_k(x_i))\}$ (for an unknown key $k$), with the $\{x_i\}$ outside the attacker's control.

  在已知明文攻击中，攻击者获得输入/输出对 $\{(x_i, F_k(x_i))\}$（对应某个未知密钥 $k$），其中 $\{x_i\}$ 不受攻击者控制。

- In a chosen-plaintext attack, the attacker is given $\{F_k(x_i)\}$ (again, for an unknown key $k$) for a series of inputs $\{x_i\}$ chosen by the attacker.

  在选择明文攻击中，攻击者针对其选择的一系列输入 $\{x_i\}$，获得 $\{F_k(x_i)\}$（同样对应某个未知密钥 $k$）。

- In a chosen-ciphertext attack, the attacker is given $\{F_k(x_i)\}$ for $\{x_i\}$ chosen by the attacker, as well as $\{F_k^{-1}(y_i)\}$ for chosen $\{y_i\}$.

  在选择密文攻击中，攻击者针对其选择的 $\{x_i\}$ 获得 $\{F_k(x_i)\}$，并针对其选择的 $\{y_i\}$ 获得 $\{F_k^{-1}(y_i)\}$。

A cipher secure against chosen-plaintext attacks corresponds to a pseudorandom permutation, while one secure against chosen-ciphertext attacks corresponds to a strong pseudorandom permutation. In addition to attacks distinguishing $F_{k}$ from a uniform permutation, we will also be interested in key-recovery attacks in which the attacker can recover the key $k$ after interacting with $F_{k}$. (This is stronger than being able to distinguish $F_{k}$ from uniform.)

能抵御选择明文攻击的密码对应于伪随机置换，而能抵御选择密文攻击的密码对应于强伪随机置换。除了区分 $F_{k}$ 与均匀置换的攻击之外，我们还将关注密钥恢复攻击，在这种攻击中，攻击者在与 $F_{k}$ 交互后能够恢复密钥 $k$。（这比能够区分 $F_{k}$ 与均匀置换更强。）

### 7.2.1 Substitution-Permutation Networks　7.2.1 代换-置换网络

A secure block cipher (using a random key) must behave like a random permutation. There are ${2}^{\ell}!$ permutations on $\ell$-bit strings, so representing an arbitrary permutation in this case requires $\log({2}^{\ell}!)$ $\approx \ell \cdot 2^{\ell}$ bits. This is impractical for $\ell > 20$ and infeasible for $\ell > 60$. (Looking ahead, modern block ciphers have block lengths $\ell \geq 128$.) The challenge when designing a block cipher is to construct permutations having a concise description (namely, a short key) that behave like random permutations. In particular, just as evaluating a random permutation at two inputs that differ in only a single bit should yield two (almost) independent outputs (they are not completely independent since they cannot be equal), so too changing one bit of the input to $F_k(\cdot)$, where k is uniform and unknown to an attacker, should yield an (almost) independent result. This implies that a one-bit change in the input should "affect" every bit of the output. (Note that this does not mean that all the output bits will be changed—that would be different behavior than one would expect for a random permutation. Rather, we just mean informally that each bit of the output is changed with probability roughly half.) This takes some work to achieve.

一个安全的分组密码（使用随机密钥）必须表现得像一个随机置换。$\ell$ 比特串上有 ${2}^{\ell}!$ 个置换，因此在这种情况下表示任意一个置换需要 $\log({2}^{\ell}!)$ $\approx \ell \cdot 2^{\ell}$ 比特。这对于 $\ell > 20$ 是不切实际的，对于 $\ell > 60$ 是不可行的。（提前说明一下，现代分组密码的分组长度 $\ell \geq 128$。）设计分组密码的挑战在于构造出具有简洁描述（即一个短密钥）、行为却像随机置换的置换。特别地，随机置换在两个仅相差一个比特的输入上的求值结果，应当是（几乎）独立的两个输出（它们不可能完全独立，因为不能相等）。类似地，改变 $F_k(\cdot)$ 输入的一个比特（其中 $k$ 均匀且对攻击者未知）也应当产生（几乎）独立的结果。这意味着输入中一个比特的改变应当“影响”输出的每一个比特。（注意，这并不意味着所有输出比特都会被改变——那样的行为与对随机置换的预期不符。相反，我们只是直观地说明：输出中的每个比特大约以一半的概率被改变。）做到这一点需要下些功夫。

The confusion-diffusion paradigm. In addition to his work on perfect secrecy, Shannon also introduced a basic paradigm for constructing concise, random-looking permutations. The basic idea is to construct a random-looking permutation $F$ with a large block length from many smaller random (or random-looking) permutations $\{f_i\}$ with small block length. Let us see how this works on the most basic level. Say we want $F$ to have a block length of 128 bits. We can define $F$ as follows: the key $k$ for $F$ will specify 16 permutations $f_1, \ldots, f_{16}$ that each have an 8-bit (1-byte) block length. $^3$ Given an input $x \in \{0,1\}^{128}$, we parse it as 16 bytes $x_1 \cdots x_{16}$ and then set

混淆-扩散范式。除了在完美保密性方面的工作外，Shannon 还引入了一个构造简洁、看似随机的置换的基本范式。基本思想是从许多具有小分组长度的较小随机（或看似随机）置换 $\{f_i\}$ 出发，构造一个具有大分组长度的看似随机的置换 $F$。让我们看看这在最基本层面上是如何工作的。假设我们希望 $F$ 的分组长度为 128 比特。我们可以如下定义 $F$：$F$ 的密钥 $k$ 将指定 16 个置换 $f_1, \ldots, f_{16}$，每个置换具有 8 比特（1 字节）的分组长度。$^3$ 给定输入 $x \in \{0,1\}^{128}$，我们将其解析为 16 个字节 $x_1 \cdots x_{16}$，然后令

$$
F_{k}(x)=f_{1}(x_{1})\|\cdots\|f_{16}(x_{16}). \tag{7.1}
$$

These round functions $\{f_{i}\}$ are said to introduce confusion into $F$.

这些轮函数 $\{f_{i}\}$ 被称作向 $F$ 中引入混淆。

$^3$ An arbitrary permutation on 8 bits can be represented using $\log(2^{8}!)$ bits, so the length of the key for F is about $16\cdot\log(2^{8}!)$ bits, or about 3 kbytes. This is much smaller than the $\approx 128\cdot 2^{128}$ bits that would be required to specify an arbitrary permutation on 128 bits. / 8 比特上的任意一个置换可以用 $\log(2^{8}!)$ 比特表示，因此 F 的密钥长度约为 $16\cdot\log(2^{8}!)$ 比特，即约 3 KB。这远小于指定 128 比特上任意置换所需的约 $128\cdot 2^{128}$ 比特。

It should be immediately clear, however, that $F$ as defined above will not be pseudorandom. Specifically, if $x$ and $x^{\prime}$ differ only in their first bit then $F_k(x)$ and $F_k(x^{\prime})$ will differ only in their first byte (regardless of the key $k$). In contrast, for a truly random permutation changing the first bit of the input would be expected to affect all bytes of the output.

然而，立刻可以看出，如上定义的 $F$ 不会是伪随机的。具体来说，如果 $x$ 和 $x^{\prime}$ 仅在第一个比特上不同，那么 $F_k(x)$ 和 $F_k(x^{\prime})$ 将仅在第一个字节上不同（无论密钥 $k$ 是什么）。相比之下，对于一个真正的随机置换，改变输入的第一个比特预计会影响输出的所有字节。

For this reason, a diffusion step is introduced whereby the bits of the output are permuted, or "mixed," using a mixing permutation. This has the effect of spreading a local change (e.g., a change in the first byte) throughout the entire block. In principle the mixing permutation could depend on the key, but in practice it is carefully designed and fixed.

出于这个原因，需要引入一个扩散步骤：用混合置换对输出的比特进行置换，或者说“混合”。这样就能把一个局部变化（例如第一个字节的变化）扩散到整个分组。原则上，混合置换可以依赖于密钥，但在实践中它是经过精心设计并固定的。

The confusion/diffusion steps—together called a round—are repeated multiple times. This helps ensure that changing a single bit of the input will affect all the bits of the output. As an example, a two-round block cipher following this approach would operate as follows. First, confusion is introduced by computing the intermediate result $f_1(x_1) \parallel \cdots \parallel f_{16}(x_{16})$ as in Equation (7.1), where we stress again that the $\{f_i\}$ depend on the key. The bits of the result are then "shuffled," or re-ordered, using a mixing permutation to give $x^{\prime} = x_1^{\prime} \cdots x_{16}^{\prime}$. Then $f_1^{\prime}(x_1^{\prime}) \parallel \cdots \parallel f_{16}^{\prime}(x_{16}^{\prime})$ is computed, using possibly different functions $\{f_i^{\prime}\}$ that again depend on the key, and the bits of the result are again permuted using a mixing permutation to give output $x^{\prime\prime}$.

混淆/扩散步骤——合称为一轮——被重复多次。这有助于确保改变输入的一个比特将影响输出的所有比特。作为一个例子，遵循这种方法的两轮分组密码将按如下方式工作。首先，如式 (7.1) 那样计算中间结果 $f_1(x_1) \parallel \cdots \parallel f_{16}(x_{16})$ 以引入混淆；这里再次强调，$\{f_i\}$ 依赖于密钥。然后使用混合置换将结果的比特“洗牌”或重新排序，得到 $x^{\prime} = x_1^{\prime} \cdots x_{16}^{\prime}$。接着计算 $f_1^{\prime}(x_1^{\prime}) \parallel \cdots \parallel f_{16}^{\prime}(x_{16}^{\prime})$（使用可能不同的、同样依赖于密钥的函数 $\{f_i^{\prime}\}$），然后再用混合置换对结果的比特洗牌，得到输出 $x^{\prime\prime}$。

Substitution-permutation networks. A substitution-permutation network (SPN) can be viewed as a direct implementation of the confusion-diffusion paradigm. The difference is that now the permutations (i.e., the $\{f_i\}, \{f_i^{\prime}\}$) have a particular form rather than being chosen from the set of all possible permutations. Specifically, rather than having (a portion of) the key k specify an arbitrary permutation $f$, we instead fix a public "substitution function" (i.e., permutation) $S$ called an $S$-box, and then let $k$ define the function $f$ given by $f(x) = S(k \oplus x)$. (If $f$ takes 8-bit inputs as before, we have thus reduced the number of possibilities for $f$ from ${2}^8!$ to ${2}^8$.)

代换-置换网络。代换-置换网络（substitution-permutation network，SPN）可以看作是混淆-扩散范式的直接实现。区别在于，现在的置换（即 $\{f_i\}, \{f_i^{\prime}\}$）具有特定的形式，而不是从所有可能的置换集合中选取。具体地，我们不再让密钥 $k$（的一部分）指定任意置换 $f$，而是固定一个公开的“代换函数”（即置换）$S$，称为 S 盒，然后让 $k$ 定义函数 $f$，即 $f(x) = S(k \oplus x)$。（如果 $f$ 像之前那样接受 8 比特输入，我们就将 $f$ 的可能性数量从 ${2}^8!$ 减少到了 ${2}^8$。）

To see how this works concretely, consider an SPN with a 64-bit block length based on a collection of 8-bit (1-byte) S-boxes $S_1, \ldots, S_8$. (See Figure 7.3.) Evaluating the cipher proceeds in a series of rounds, where in each round we apply the following sequence of operations to the 64-bit input x of that round (the input to the first round is just the input to the cipher):

为了具体说明它是如何工作的，考虑一个分组长度为 64 比特、基于一组 8 比特（1 字节）S 盒 $S_1, \ldots, S_8$ 的 SPN。（见图 7.3。）密码的求值分一系列轮次进行，在每一轮中，对该轮的 64 比特输入 $x$ 应用以下操作序列（第一轮的输入就是密码的输入）：

1. Key mixing: Set $x := x \oplus k$, where k is the current-round sub-key;

   密钥混合：令 $x := x \oplus k$，其中 k 是当前轮的子密钥；

2. Substitution: Set $x := S_1(x_1) \Vert \cdots \Vert S_8(x_8)$, where $x_i$ is the ith byte of $x$;

   代换：令 $x := S_1(x_1) \Vert \cdots \Vert S_8(x_8)$，其中 $x_i$ 是 $x$ 的第 i 个字节；

3. Permutation: Permute the bits of x to obtain the output of the round.

   置换：置换 $x$ 的比特，得到该轮的输出。

The output of each round is used as input to the next round. After the last round there is a final key-mixing step, and the result is the output of the cipher. (By Kerckhoffs' principle, we assume the S-boxes and the mixing permutation(s) are public and known to any attacker. Without the final key-mixing step, the substitution and permutation steps of the last round would offer no additional security since they do not depend on the key and can be inverted by an attacker.)

每一轮的输出用作下一轮的输入。在最后一轮之后有一个最终的密钥混合步骤，其结果就是密码的输出。（根据 Kerckhoffs 原则，我们假设 S 盒和混合置换是公开的且为任何攻击者所知。没有最终的密钥混合步骤，最后一轮的代换和置换步骤将不提供任何额外的安全性，因为它们不依赖于密钥且可以被攻击者求逆。）

![Image](https://lsky.jerryxue.top/i/2026/08/19/6a85c541132a9.jpg)

**FIGURE 7.3: A single round of a substitution-permutation network.**

**图 7.3：代换-置换网络的单轮。**

Figure 7.4 shows three rounds of an SPN with a 16-bit block length and a different set of 4-bit S-boxes used in each round.

图 7.4 展示了一个 SPN 的三轮：其分组长度为 16 比特，每轮使用一组不同的 4 比特 S 盒。

Different sub-keys (or round keys) are used in each round. The actual key of the block cipher is sometimes called the master key. The round keys are derived from the master key according to a key schedule. The key schedule is often simple and may just use different subsets of the bits of the master key as the various sub-keys, though more complex key schedules can also be defined. An r-round SPN has r rounds of key mixing, S-box substitution, and application of a mixing permutation, followed by a final key-mixing step. (This means that an r-round SPN uses $r + 1$ sub-keys.)

每一轮使用不同的子密钥（或轮密钥）。分组密码的实际密钥有时称为主密钥。轮密钥根据密钥扩展从主密钥派生。密钥扩展通常很简单，可能只是将主密钥的不同比特子集用作各个子密钥，但也可以定义更复杂的密钥扩展。一个 $r$ 轮 SPN 包含 $r$ 轮的密钥混合、S 盒代换和混合置换，最后还有一个最终的密钥混合步骤。（这意味着一个 $r$ 轮 SPN 使用 $r + 1$ 个子密钥。）

Any SPN is invertible (given the key). To see this, it suffices to show that a single round can be inverted; this implies the entire SPN can be inverted by working from the final round back to the beginning. But inverting a single round is easy: the mixing permutation can easily be inverted since it is just a re-ordering of bits. Since the S-boxes are permutations (i.e., one-to-one), these too can be inverted. The result can then be XORed with the appropriate sub-key to obtain the original input. Summarizing:

任何 SPN（给定密钥时）都是可逆的。要明白这一点，只需证明单轮可逆即可；由此，从最后一轮逐轮逆推回开头，整个 SPN 就可逆。而求逆单轮是容易的：混合置换可以容易地求逆，因为它只是比特的重新排序。由于 S 盒是置换（即一一对应的），它们也可以被求逆。然后可以将结果与相应的子密钥异或，得到原始输入。总结如下：

PROPOSITION 7.3 Let F be a keyed function defined by an SPN in which the S-boxes are all permutations. Then regardless of the key schedule and the number of rounds, $F_k$ is a permutation for any k.

命题 7.3 设 $F$ 是一个由 S 盒均为置换的 SPN 定义的带密钥函数。那么无论密钥扩展和轮数如何，对于任意 $k$，$F_k$ 都是一个置换。

![Image](https://lsky.jerryxue.top/i/2026/08/19/6a85c5459fd30.jpg)

**FIGURE 7.4: Three rounds of a substitution-permutation network.**

**图 7.4：代换-置换网络的三轮。**

The number of rounds, along with the exact choices of the S-boxes, mixing permutations, and key schedule, are what ultimately determine whether a given block cipher is trivially breakable or highly secure. We now discuss a basic principle behind the design of the S-boxes and mixing permutations.

轮数，连同 S 盒、混合置换和密钥扩展的确切选择，最终决定了一个给定的分组密码是可以被轻易破解还是高度安全的。我们现在讨论 S 盒和混合置换设计背后的一个基本原则。

The avalanche effect. As noted repeatedly, an important property in any block cipher is that a small change in the input must "affect" every bit of the output. We refer to this as the avalanche effect. One way to induce the avalanche effect in a substitution-permutation network is to ensure that the following two properties hold (and sufficiently many rounds are used):

雪崩效应。正如前面反复指出的，任何分组密码的一个重要性质是：输入的微小变化必须“影响”输出的每一个比特。我们将此称为雪崩效应。在代换-置换网络中引发雪崩效应的一种方法是确保以下两个性质成立（并且使用足够多的轮数）：

1. The S-boxes are designed so that changing a single bit of the input to an S-box changes at least two bits in the output of the S-box.

   S 盒的设计使得改变 S 盒输入的一个比特会改变 S 盒输出中至少两个比特。

2. The mixing permutations are designed so that the bits output by any given S-box affect the input to multiple S-boxes in the next round. For example, in Figure 7.4 the output from $S_{1}$ affects the input to $S_{5}, S_{6}, S_{7}$, and $S_{8}$.

   混合置换的设计使得任何给定 S 盒输出的比特会影响下一轮中多个 S 盒的输入。例如，在图 7.4 中，$S_{1}$ 的输出影响 $S_{5}, S_{6}, S_{7}$ 和 $S_{8}$ 的输入。

To see how this yields the avalanche effect, at least heuristically, assume the S-boxes are all such that changing a single bit of the input to the S-box results in a change in exactly two bits in the output of the S-box, and that the mixing permutations are chosen as required above. For concreteness, assume the S-boxes have 8-bit input/output length, and that the block length of the cipher is 128 bits. Consider now what happens when the block cipher is applied to two inputs that differ in a single bit:

为了看清雪崩效应是如何产生的（至少是启发式地），假设所有 S 盒都是这样的：改变 S 盒输入的一个比特，恰好导致 S 盒输出中两个比特的改变；并且混合置换按上述要求选取。为具体起见，假设 S 盒有 8 比特的输入/输出长度，且密码的分组长度为 128 比特。现在考虑当分组密码被应用于两个仅相差一个比特的输入时会发生什么：

1. After the first round, the intermediate values differ in exactly two bits. This is because XORing the first-round sub-key maintains the 1-bit difference in the intermediate values, and so the inputs to all the S-boxes except one are identical. In the one S-box where the inputs differ, the output of the S-box causes a 2-bit difference. The mixing permutation applied to the results changes the positions of these differences, but maintains a 2-bit difference.

   第一轮之后，中间值恰好有两个比特不同。这是因为与第一轮子密钥异或保持了中间值中的 1 比特差异，因此除一个 S 盒外所有 S 盒的输入都相同。在那个输入不同的 S 盒中，S 盒的输出导致 2 比特差异。对结果应用的混合置换改变了这些差异的位置，但保持了 2 比特差异。

2. The mixing permutation applied at the end of the first round spreads the two bit-positions where the intermediate results differ into two different S-boxes in the second round. This remains true even after the second-round key mixing is done. So, in the second round there are now two S-boxes that receive inputs differing in a single bit. Thus, at the end of the second round the intermediate values differ in 4 bits.

   第一轮末尾应用的混合置换将中间值不同的两个比特位置扩散到第二轮的两个不同 S 盒中。即使在进行第二轮密钥混合之后，这一点仍然成立。因此，第二轮中现在有两个 S 盒的输入相差一个比特。于是，在第二轮结束时中间值有 4 个比特不同。

3. Continuing the same argument, we expect 8 bits of the intermediate value to be affected after the 3rd round, 16 bits to be affected after the 4th round, and all 128 bits to be affected at the end of the 7th round.

   继续同样的论证，我们预计第 3 轮后中间值有 8 个比特受到影响，第 4 轮后有 16 个比特受到影响，第 7 轮结束时所有 128 个比特都受到影响。

The last point is not quite precise and it is certainly possible that there will be fewer differences than expected at the end of some round. (In fact, we want this to be the case because uncorrelated values should not differ in all their bits, either.) This can occur when the mixing permutation maps two bit-positions that differ in some intermediate result to the same S-box in the following round. For this reason, it is customary to use many more than the minimum number of rounds needed. But the above analysis gives a lower bound: if fewer than 7 rounds are used then there must be some set of output bits that are not affected by a single-bit change in the input, implying that it will be possible to distinguish the cipher from a random permutation.

最后一点并不完全精确，而且某些轮次结束时确实有可能出现比预期更少的差异。（事实上，我们希望如此，因为不相关的值也不应在所有比特上都不同。）当混合置换将某个中间结果中不同的两个比特位置映射到下一轮的同一个 S 盒时，就会出现这种情况。出于这个原因，通常使用的轮数会远超所需的最少轮数。但上述分析给出了一个下界：如果使用的轮数少于 7 轮，那么必定存在某组输出比特不受输入中单比特变化的影响，这意味着可以把该密码与一个随机置换区分开来。

One might expect that the "best" way to design S-boxes would be to choose them at random (subject to the restriction that they are permutations). Interestingly, this turns out not to be the case, at least if we want to satisfy the design criteria mentioned earlier. Consider the case of an S-box operating on 4-bit inputs and let x and $x^{\prime}$ be two distinct values. Let $y = S(x)$, and now consider choosing uniform $y^{\prime} \neq y$ as the value of $S(x^{\prime})$. There are 4 strings that differ from y in only 1 bit, and so with probability 4/15 we will choose $y^{\prime}$ that does not differ from y in two or more bits. The problem is compounded when we consider all pairs of inputs that differ in a single bit. We conclude based on this example that, as a general rule, the S-boxes must be designed carefully rather than being chosen at random. Random S-boxes are also not good for defending against attacks like the ones we will show in Section 7.2.6.

人们可能期望，设计 S 盒的“最佳”方式是随机选取它们（前提是它们必须是置换）。有趣的是，事实并非如此，至少如果我们想满足前面提到的设计准则的话。考虑一个对 4 比特输入进行操作的 S 盒，令 $x$ 和 $x^{\prime}$ 是两个不同的值。令 $y = S(x)$，现在考虑选择均匀的 $y^{\prime} \neq y$ 作为 $S(x^{\prime})$ 的值。有 4 个串仅在 1 个比特上与 $y$ 不同，因此以 4/15 的概率我们将选择的 $y^{\prime}$ 与 $y$ 至多相差一个比特。当我们考虑所有仅相差一个比特的输入对时，问题会加剧。基于这个例子我们得出结论：一般来说，S 盒必须精心设计，而不能随机选取。随机 S 盒也不能很好地抵御我们将在 7.2.6 节中展示的那类攻击。

If a block cipher should also be strongly pseudorandom, then the avalanche effect must also apply to its inverse. That is, changing a single bit of the output should affect every bit of the input. For this it is useful if the S-boxes are designed so that changing a single bit of the output of an S-box changes at least two bits of the input to the S-box. Achieving the avalanche effect in both directions is another reason for further increasing the number of rounds.

如果一个分组密码还应当是强伪随机的，那么雪崩效应也必须适用于它的逆。也就是说，改变输出的一个比特应当影响输入的每一个比特。为此，如果 S 盒的设计使得改变 S 盒输出的一个比特会改变 S 盒输入的至少两个比特，那将是有益的。在两个方向上都实现雪崩效应是进一步增加轮数的另一个原因。

#### Attacking Reduced-Round SPNs　攻击减少轮数的 SPN

Experience, along with many years of cryptanalytic effort, indicate that substitution-permutation networks are a good choice for constructing pseudorandom permutations as long as care is taken in the choice of the S-boxes, the mixing permutations, and the key schedule. The Advanced Encryption Standard, described in Section 7.2.5, is similar in structure to a substitution-permutation network as described above, and is widely believed to be a strong pseudorandom permutation.

经验以及多年的密码分析努力表明，只要在 S 盒、混合置换和密钥扩展的选择上谨慎行事，代换-置换网络是构造伪随机置换的一个好选择。7.2.5 节中描述的高级加密标准在结构上类似于上述代换-置换网络，并被广泛认为是一个强伪随机置换。

The strength of a cipher $F$ constructed as an SPN depends heavily on the number of rounds. In order to obtain more insight into substitution-permutation networks, we will demonstrate attacks on SPNs having very few rounds. These attacks are fairly simple, but are worth seeing as they demonstrate conclusively why a large number of rounds is needed.

构造为 SPN 的密码 $F$ 的强度在很大程度上取决于轮数。为了更深入地了解代换-置换网络，我们将展示对轮数极少的 SPN 的攻击。这些攻击相当简单，但值得一看，因为它们确凿地证明了为什么需要大量的轮数。

A trivial case. We first consider a trivial case where $F$ consists of one round and no final key-mixing step. We show that an adversary given only a single input/output pair $(x, y)$ can easily learn the secret key $k$ for which $y = F_k(x)$. The adversary begins with the output value $y$ and then inverts the mixing permutation and the $S$-boxes. It can do this, as noted before, because the full specification of the mixing permutation and the $S$-boxes is public. The intermediate value that the adversary computes is exactly $x \oplus k$ (assuming, without loss of generality, that the master key is used as the sub-key in the only round of the network). Since the adversary also knows the input $x$, it can immediately derive the secret key $k$. This is therefore a complete break.

一个平凡的情形。我们首先考虑一个平凡的情形，其中 $F$ 仅由一轮组成且没有最终的密钥混合步骤。我们证明，一个仅获得单个输入/输出对 $(x, y)$ 的敌手可以容易地学到满足 $y = F_k(x)$ 的秘密密钥 $k$。敌手从输出值 $y$ 开始，然后求逆混合置换和 $S$ 盒。如前所述，它可以做到这一点，因为混合置换和 $S$ 盒的完整规范是公开的。敌手计算出的中间值恰好是 $x \oplus k$（不失一般性地假设主密钥被用作网络唯一一轮的子密钥）。由于敌手也知道输入 $x$，它可以立即推导出秘密密钥 $k$。因此这是一次完全攻破。

Although this is a trivial attack, it demonstrates that in any substitution-permutation network there is no security gained by performing S-box substitution or applying a mixing permutation after the last key-mixing step.

虽然这是一个平凡的攻击，但它表明在任何代换-置换网络中，在最后一个密钥混合步骤之后执行 S 盒代换或应用混合置换不会带来任何安全性。

Attacking a one-round SPN. Now we have one round followed by a key-mixing step. For concreteness, we assume a 64-bit block length and S-boxes with 8-bit (1-byte) input/output length. We assume independent 64-bit sub-keys $k_1$, $k_2$ are used for the two key-mixing steps, and so the master key $k_1\|k_2$ of the SPN is 128 bits long.

攻击一轮 SPN。现在我们有一轮后跟一个密钥混合步骤。为具体起见，我们假设分组长度为 64 比特，S 盒的输入/输出长度为 8 比特（1 字节）。我们假设两个密钥混合步骤使用独立的 64 比特子密钥 $k_1$、$k_2$，因此该 SPN 的主密钥 $k_1\|k_2$ 长 128 比特。

A first observation is that we can extend the attack from the trivial case above to give a key-recovery attack here using much less than ${2}^{128}$ work. The idea is as follows: Given a single input/output pair $(x, y)$ as before, the attacker enumerates over all possible values for the first-round sub-key $k_1$. For each such value, the attacker can compute the first round of the SPN using $k_1$ to get a candidate intermediate value $x^l$. The only second-round sub-key that is consistent with $k_1$ and output $y$ is $k_2 = x^l \oplus y$. Thus, for each possible choice of $k_1$ the attacker derives a unique corresponding $k_2$ for which $k_1 \parallel k_2$ might be the master key. In this way, the attacker obtains (in ${2}^{64}$ time) a list of ${2}^{64}$ possibilities for the master key. These can be narrowed down using additional input/output pairs in roughly ${2}^{64}$ additional time.

第一个观察是，我们可以将上述平凡情形的攻击扩展为这里的密钥恢复攻击，其工作量远小于 ${2}^{128}$。想法如下：如前所述给定单个输入/输出对 $(x, y)$，攻击者枚举第一轮子密钥 $k_1$ 的所有可能值。对于每一个这样的值，攻击者可以使用 $k_1$ 计算 SPN 的第一轮，得到一个候选中间值 $x^l$。唯一与 $k_1$ 和输出 $y$ 一致的第二轮子密钥是 $k_2 = x^l \oplus y$。因此，对于 $k_1$ 的每一种可能选择，攻击者推导出一个唯一的对应 $k_2$，使得 $k_1 \parallel k_2$ 可能是主密钥。以这种方式，攻击者在 ${2}^{64}$ 时间内获得一个包含 ${2}^{64}$ 个主密钥可能性的列表。使用额外的输入/输出对，可以在大约 ${2}^{64}$ 的额外时间内缩小范围。

A better attack is possible by noting that individual bits of the output depend on only part of the sub-keys. Fix some given input/output pair $(x, y)$ as before. Now, the adversary will enumerate over all possible values for the first byte of $k_1$. It can XOR each such value with the first byte of $x$ to obtain a candidate value for the 1-byte input to the first S-box. Evaluating this S-box, the attacker learns a candidate value for the output of that S-box. Since the output of that S-box is XORed with 8 bits of $k_2$ to yield 8 bits of $y$ (where the positions of those bits depend on the mixing permutation but are known to the attacker), this yields a candidate value for 8 bits of $k_2$.

注意到输出的各个比特仅依赖于子密钥的一部分，就可以实施更好的攻击。如前所述固定某个给定的输入/输出对 $(x, y)$。现在，敌手将枚举 $k_1$ 第一个字节的所有可能值。它可以将每个这样的值与 $x$ 的第一个字节异或，得到第一个 S 盒的 1 字节输入的候选值。求值该 S 盒后，攻击者得到该 S 盒输出的候选值。由于该 S 盒的输出与 $k_2$ 的 8 个比特异或以产生 $y$ 的 8 个比特（这些比特的位置取决于混合置换但为攻击者所知），这就给出了 $k_2$ 的 8 个比特的候选值。

To summarize: for each candidate value for the first byte of $k_1$, there is a unique possible corresponding value for some 8 bits of $k_2$. Put differently, this means that for some 16 bits of the master key, the attacker has reduced the number of possible values for those bits from ${2}^{16}$ to ${2}^8$. The attacker can tabulate all those feasible values in ${2}^8$ time. This can be repeated for each byte of $k_1$, giving 8 lists—each containing ${2}^8$ 16-bit values—that together characterize the possible values of the entire master key. In this way, the attacker has reduced the number of possible master keys to $(2^8)^8 = 2^{64}$, as in the earlier attack; the total time to do this, however, is now ${8} \cdot 2^8 = 2^{11}$, a dramatic improvement.

总结：对于 $k_1$ 第一个字节的每个候选值，$k_2$ 的某 8 个比特有唯一可能的对应值。换言之，这意味着对于主密钥的某 16 个比特，攻击者已将这些比特的可能值数量从 ${2}^{16}$ 减少到了 ${2}^8$。攻击者可以在 ${2}^8$ 时间内列出所有这些可行的值。这可以对 $k_1$ 的每个字节重复进行，得到 8 个列表——每个包含 ${2}^8$ 个 16 比特值——它们共同刻画了整个主密钥的可能值。以这种方式，攻击者将可能主密钥的数量减少到了 $(2^8)^8 = 2^{64}$，与之前的攻击一样；然而，这样做的总时间现在是 ${8} \cdot 2^8 = 2^{11}$，这是一个显著的改进。

The attacker can use additional input/output pairs to further reduce the space of possible keys. Importantly, this can be done for each list individually. Consider the list of ${2}^8$ feasible values for some set of 16 bits of the master key. The attacker knows that the correct value from that list must be consistent with any additional input/output pairs the attacker learns, whereas any incorrect value in the list is expected to be consistent with another input/output pair $(x^{\prime}, y^{\prime})$ with probability no better than random. Since a 16-bit value from the list can be used to compute eight bits of the output given the input $x^{\prime}$, an incorrect value will be consistent with the actual output $y^{\prime}$ with probability roughly ${2}^{-8}$. A small number of additional input/output pairs thus suffices to narrow down all the lists to just a single value each, at which point the entire master key is known.

攻击者可以使用额外的输入/输出对来进一步缩小可能的密钥空间。重要的是，这可以针对每个列表单独进行。考虑主密钥的某组 16 个比特的 ${2}^8$ 个可行值的列表。攻击者知道，该列表中的正确值必须与攻击者获得的任何额外输入/输出对一致，而列表中的任何错误值，预计与另一个输入/输出对 $(x^{\prime}, y^{\prime})$ 一致的概率不会高于随机水平。由于列表中的一个 16 比特值可以用来在给定输入 $x^{\prime}$ 时计算输出的八个比特，一个错误值将以大约 ${2}^{-8}$ 的概率与实际输出 $y^{\prime}$ 一致。因此，少量额外的输入/输出对就足以将所有列表各缩小到只有一个值，此时整个主密钥就已知了。

This attack exploits the fact that the effects of different parts of the key can be isolated. Additional rounds are needed to ensure further diffusion, and to make sure that each bit of the key affects all of the bits of the output.

这种攻击利用了这样一个事实：密钥不同部分的效果可以被分离开来。需要额外的轮数来确保进一步的扩散，并确保密钥的每个比特影响输出的所有比特。

Attacking a two-round SPN. It is possible to extend the above ideas to give a better-than-brute-force attack on a two-round SPN using independent sub-keys in each round; we leave this as an exercise. Here we simply note that a two-round SPN will not be a good pseudorandom permutation, since the avalanche effect does not occur after only two rounds. (Of course, this depends on the block length of the cipher and the input/output length of the S-boxes, but with reasonable parameters this will be the case.) An attacker can distinguish a two-round SPN from a uniform permutation if it learns the result of evaluating the SPN on two inputs that differ in a single bit, since some predictable subset of the output bits will not change.

攻击两轮 SPN。可以将上述思想扩展为对每轮使用独立子密钥的两轮 SPN 的优于穷举的攻击；我们将此留作练习。这里我们仅指出，两轮 SPN 不会是一个好的伪随机置换，因为仅经过两轮后雪崩效应不会发生。（当然，这取决于密码的分组长度和 S 盒的输入/输出长度，但在合理的参数下情况确实如此。）如果攻击者获得了 SPN 在两个仅相差一个比特的输入上的求值结果，它就可以区分两轮 SPN 与均匀置换，因为输出的某个可预测子集的比特不会改变。

### 7.2.2 Feistel Networks　7.2.2 Feistel 网络

Feistel networks offer another approach for constructing block ciphers. An advantage of Feistel networks over substitution-permutation networks is that the underlying functions used in a Feistel network—in contrast to the S-boxes used in SPNs—need not be invertible. A Feistel network thus provides a way to construct an invertible function from non-invertible components. This is important because a good block cipher should have "unstructured" behavior (so it looks random), yet requiring all the components of a construction to be invertible inherently introduces structure. Requiring invertibility also introduces an additional constraint on S-boxes, making them harder to design.

Feistel 网络提供了构造分组密码的另一种方法。Feistel 网络相对于代换-置换网络的一个优势在于，Feistel 网络中使用的底层函数——与 SPN 中使用的 S 盒不同——不需要是可逆的。因此，Feistel 网络提供了一种从不可逆组件构造可逆函数的方法。这很重要，因为一个好的分组密码应当具有“无结构”的行为（使其看起来随机），然而，要求构造的所有组件都可逆，这本身就引入了结构。要求可逆性还给 S 盒引入了额外的约束，使其更难设计。

A Feistel network operates in a series of rounds. In each round, a keyed round function is applied in the manner described below. Round functions need not be invertible. They will typically be constructed from components like S-boxes and mixing permutations, but a Feistel network can deal with any round functions irrespective of their design.

Feistel 网络在一系列轮次中运行。在每一轮中，以下面描述的方式应用一个带密钥的轮函数。轮函数不需要是可逆的。它们通常由 S 盒和混合置换等组件构造，但 Feistel 网络可以处理任何轮函数，无论其设计如何。

In a (balanced) Feistel network with $\ell$-bit block length, the $i$th round function $\hat{f}_i$ takes as input a sub-key $k_i$ and an $\ell/2$-bit string and generates an $\ell/2$-bit output. As in the case of SPNs, a master key $k$ is used to derive sub-keys for each round. When some master key is chosen, thereby determining each sub-key $k_i$, we define $f_i : \{0,1\}^{\ell/2} \to \{0,1\}^{\ell/2}$ via $f_i(R) \overset{\mathrm{def}}{=} \hat{f}_i(k_i, R)$. Note that the round functions $\hat{f}_i$ are fixed and publicly known, but the $f_i$ depend on the master key and so are not known to the attacker.

在具有 $\ell$ 比特分组长度的（平衡）Feistel 网络中，第 $i$ 个轮函数 $\hat{f}_i$ 以子密钥 $k_i$ 和 $\ell/2$ 比特串为输入，生成 $\ell/2$ 比特输出。与 SPN 的情况一样，主密钥 $k$ 用于派生每一轮的子密钥。当选定某个主密钥从而确定了每个子密钥 $k_i$ 时，我们通过 $f_i(R) \overset{\mathrm{def}}{=} \hat{f}_i(k_i, R)$ 定义 $f_i : \{0,1\}^{\ell/2} \to \{0,1\}^{\ell/2}$。注意，轮函数 $\hat{f}_i$ 是固定且公开的，但 $f_i$ 依赖于主密钥，因此攻击者并不知道它们。

The $i$th round of a Feistel network operates as follows. The $\ell$-bit input to the round is divided into two halves denoted $L_{i-1}$ and $R_{i-1}$ (the "left" and "right" halves, respectively). The output $(L_i, R_i)$ of the round is

Feistel 网络的第 $i$ 轮按如下方式工作。该轮的 $\ell$ 比特输入被分为两半，分别记为 $L_{i-1}$ 和 $R_{i-1}$（分别为“左”半和“右”半）。该轮的输出 $(L_i, R_i)$ 为

$$
L_{i}:=R_{i-1}\quad\mathrm{and}\quad R_{i}:=L_{i-1}\oplus f_{i}(R_{i-1}).
$$

In an r-round Feistel network, the $\ell$-bit input to the network is parsed as $(L_0, R_0)$, and the output is the $\ell$-bit value $(L_r, R_r)$ obtained after applying all r rounds. A three-round Feistel network is shown in Figure 7.5.

在一个 $r$ 轮 Feistel 网络中，网络的 $\ell$ 比特输入被解析为 $(L_0, R_0)$，输出是应用全部 $r$ 轮后得到的 $\ell$ 比特值 $(L_r, R_r)$。三轮 Feistel 网络如图 7.5 所示。

Inverting a Feistel network. A Feistel network is invertible regardless of the $\{f_i\}$ (and thus regardless of the round functions $\{\hat{f}_i\}$). To show this we need only show that each round of the network can be inverted if the $\{f_i\}$ are known. Given the output $(L_i, R_i)$ of the $i$th round, we can compute $(L_{i-1}, R_{i-1})$ as follows: first set $R_{i-1} := L_i$. Then compute

求逆 Feistel 网络。Feistel 网络无论 $\{f_i\}$ 如何（因此也无论轮函数 $\{\hat{f}_i\}$ 如何）都是可逆的。为了证明这一点，我们只需证明在 $\{f_i\}$ 已知的情况下网络的每一轮都可以被求逆。给定第 $i$ 轮的输出 $(L_i, R_i)$，我们可以按如下方式计算 $(L_{i-1}, R_{i-1})$：首先令 $R_{i-1} := L_i$。然后计算

![Image](https://lsky.jerryxue.top/i/2026/08/19/6a85c5480e91d.jpg)

**FIGURE 7.5: A three-round Feistel network.**

**图 7.5：三轮 Feistel 网络。**

$$
L_{i-1}:=R_{i}\oplus f_{i}(R_{i-1}). \tag{7.2}
$$

This gives the value $(L_{i-1}, R_{i-1})$ that was the input of this round (i.e., it computes the inverse of Equation (7.2)). Note that $f_i$ is evaluated only in the forward direction, so it need not be invertible. We thus have:

这就给出了该轮的输入值 $(L_{i-1}, R_{i-1})$（即它计算了式 (7.2) 的逆）。注意 $f_i$ 仅在正向被求值，因此它不需要是可逆的。于是我们有：

PROPOSITION 7.4 Let F be a keyed function defined by a Feistel network. Then regardless of the key schedule, the round functions $\{\hat{f}_i\}$, and the number of rounds, $F_k$ is a permutation for any k.

命题 7.4 设 $F$ 是一个由 Feistel 网络定义的带密钥函数。那么无论密钥扩展、轮函数 $\{\hat{f}_i\}$ 和轮数如何，对于任意 $k$，$F_k$ 都是一个置换。

#### Attacking Reduced-Round Feistel Networks　攻击减少轮数的 Feistel 网络

As in the case of SPNs, attacks on Feistel networks are possible when the number of rounds is too low. Although it is not possible to show key-recovery attacks without knowing something about the round functions, we show here that one- and two-round Feistel networks can easily be distinguished from random functions. (In Section 8.6 we show that three- and four-round Feistel networks can be proven secure under certain conditions.)

与 SPN 的情况一样，当轮数太少时，对 Feistel 网络的攻击是可能的。虽然在不了解轮函数的情况下无法展示密钥恢复攻击，但我们在这一节展示一轮和两轮 Feistel 网络可以容易地与随机函数区分开来。（在 8.6 节中我们证明，在某些条件下三轮和四轮 Feistel 网络可以被证明是安全的。）

Attacking a one-round Feistel network. If $F$ is a one-round Feistel network then $F_k(L_0, R_0) = (R_0, f_1(R_0) \oplus L_0)$, where $f_1$ depends in some way on $k$. Although the attacker does not know $f_1$ (because it does not know $k$), it is clear that $F_k$ (for a uniform key $k$) is easy to distinguish from a random function since the left half of the output of $F_k$ is always equal to the right half of its input. Formally, consider a distinguisher given access to an oracle $g$ that is either equal to $F_k$ (for uniform $k$) or a random permutation. The distinguisher simply queries $g(0^\ell)$ to obtain an output $y$, and then outputs 1 iff the first half of $y$ is equal to ${0}^{\ell/2}$. When $g$ is $F_k$, the distinguisher outputs 1 with probability 1; when $g$ is a random permutation, however, the value $y$ is uniform and so the distinguisher outputs 1 only with probability ${2}^{-\ell/2}$.

攻击一轮 Feistel 网络。如果 $F$ 是一轮 Feistel 网络，那么 $F_k(L_0, R_0) = (R_0, f_1(R_0) \oplus L_0)$，其中 $f_1$ 以某种方式依赖于 $k$。虽然攻击者不知道 $f_1$（因为它不知道 $k$），显然 $F_k$（对于均匀密钥 $k$）容易与随机函数区分，因为 $F_k$ 输出的左半部分总是等于其输入的右半部分。形式化地说，考虑一个区分器，它被赋予访问预言机 $g$ 的权限，其中 $g$ 要么等于 $F_k$（对于均匀的 $k$），要么是一个随机置换。区分器只需查询 $g(0^\ell)$ 以获得输出 $y$，然后当且仅当 $y$ 的前半部分等于 ${0}^{\ell/2}$ 时输出 1。当 $g$ 是 $F_k$ 时，区分器以概率 1 输出 1；然而当 $g$ 是随机置换时，值 $y$ 是均匀的，因此区分器仅以概率 ${2}^{-\ell/2}$ 输出 1。

Attacking a two-round Feistel network. If F is a two-round Feistel network then

攻击两轮 Feistel 网络。如果 F 是两轮 Feistel 网络，那么

$$
F_{k}(L_{0},R_{0})=\left(f_{1}(R_{0})\oplus L_{0},R_{0}\oplus f_{2}(f_{1}(R_{0})\oplus L_{0})\right),
$$

where $f_1, f_2$ depend in some way on $k$. If the round functions $\hat{f}_1, \hat{f}_2$ are designed properly, then $f_1, f_2$ may indeed look random when $k$ is unknown, in which case the output $F_k(L_0, R_0)$ for a single input may look random. Nevertheless, there are correlations between the outputs of $F_k$ on related inputs that can be used to distinguish $F_k$ from a random permutation. Specifically, consider evaluating $F_k$ on the inputs $(0^{\ell/2}, 0^{\ell/2})$ and $(1^{\ell/2}, 0^{\ell/2})$. If we let

其中 $f_1, f_2$ 以某种方式依赖于 $k$。如果轮函数 $\hat{f}_1, \hat{f}_2$ 设计得当，那么当 $k$ 未知时 $f_1, f_2$ 确实可能看起来是随机的，在这种情况下，单个输入的输出 $F_k(L_0, R_0)$ 可能看起来是随机的。尽管如此，$F_k$ 在相关输入上的输出之间存在相关性，可用于区分 $F_k$ 与随机置换。具体地，考虑在输入 $(0^{\ell/2}, 0^{\ell/2})$ 和 $(1^{\ell/2}, 0^{\ell/2})$ 上求值 $F_k$。如果我们令

$$
(L_{2},R_{2})\stackrel{\mathrm{def}}{=}F_{k}(0^{\ell/2},0^{\ell/2})\mathrm{and}(L_{2}^{\prime},R_{2}^{\prime})\stackrel{\mathrm{def}}{=}F_{k}(1^{\ell/2},0^{\ell/2}),
$$

then a little algebra gives

那么稍作代数运算即可得到

$$
L_{2}\oplus L_{2}^{\prime}=f_{1}(0^{\ell/2})\oplus0^{\ell/2}\oplus f_{1}(0^{\ell/2})\oplus1^{\ell/2}=1^{\ell/2}.
$$

This holds regardless of the key. On the other hand, for a random permutation $f$ the probability that the XOR of the left halves of $f(0^{\ell/2},0^{\ell/2})$ and $f(1^{\ell/2},0^{\ell/2})$ is equal ${1}^{\ell/2}$ is roughly ${2}^{-\ell/2}$.

无论密钥如何这都是成立的。另一方面，对于随机置换 $f$，$f(0^{\ell/2},0^{\ell/2})$ 和 $f(1^{\ell/2},0^{\ell/2})$ 左半部分的异或等于 ${1}^{\ell/2}$ 的概率大约为 ${2}^{-\ell/2}$。

### 7.2.3 DES – The Data Encryption Standard　7.2.3 DES——数据加密标准

The Data Encryption Standard, or DES, was developed in the 1970s by IBM (with help from the National Security Agency) and adopted by the US in 1977 as a Federal Information Processing Standard. DES is of great historical significance. It has undergone intensive scrutiny within the cryptographic community, arguably more than any other cryptographic algorithm in history, and the consensus is that DES is an extremely well-designed cipher. Indeed, even after many years, the best attack on DES in practice is an exhaustive search over all ${2}^{56}$ possible keys. (There are important theoretical attacks on DES requiring less computation; however, those attacks assume certain conditions that seem difficult to realize in practice.) In its basic form, though, DES is no longer considered suitable since a 56-bit key is too short, i.e., brute-force attacks running in time ${2}^{56}$ are feasible today. The 64-bit block length of DES is also too small for modern applications. Nevertheless, DES remains in limited use in the strengthened form of triple-DES, described in Section 7.2.4.

数据加密标准（Data Encryption Standard，DES）是 IBM 在 20 世纪 70 年代（在美国国家安全局的协助下）开发的，并于 1977 年被美国采纳为联邦信息处理标准。DES 具有重大的历史意义。它在密码学界经受了严格的审查——可以说比历史上任何其他密码算法受到的审查都多——而共识是，DES 是一个设计极其精良的密码。事实上，即使经过多年，实践中对 DES 的最佳攻击仍然是对所有 ${2}^{56}$ 个可能密钥的穷举搜索。（存在一些重要的理论攻击，其所需计算量更少；然而，这些攻击假设了某些在实践中似乎难以实现的条件。）不过，在其基本形式下，DES 不再被认为是合适的，因为 56 比特密钥太短，即今天运行时间为 ${2}^{56}$ 的穷举攻击是可行的。DES 的 64 比特分组长度对于现代应用来说也太短。尽管如此，DES 仍以三重 DES（见 7.2.4 节）这种增强形式在有限范围内使用。

In this section, we provide a high-level overview of the main components of DES. We do not provide a full specification, and we have simplified some parts of the design. The reader interested in the low-level details of DES can consult the references at the end of this chapter.

在本节中，我们提供 DES 主要组件的高层概述。我们不提供完整的规范，并且我们简化了设计的某些部分。对 DES 底层细节感兴趣的读者可以参阅本章末尾的参考文献。

#### The Design of DES　DES 的设计

The DES block cipher is a 16-round Feistel network with a block length of 64 bits and a key length of 56 bits. The same round function $\hat{f}$ is used in each of the 16 rounds. The round function takes a 48-bit sub-key and, as expected for a (balanced) Feistel network, a 32-bit input (namely, half a block). The key schedule of DES is used to derive a sequence of 48-bit sub-keys $k_1, \ldots, k_{16}$ from the 56-bit master key. The key schedule of DES is relatively simple, with each sub-key $k_i$ being a permuted subset of 48 bits of the master key. For our purposes, it suffices to note that the 56 bits of the master key are divided into two halves—a "left half" and a "right half"—containing 28 bits each. (This division occurs after an initial permutation is applied to the key, but we ignore this in our description.) The left-most 24 bits of each round sub-key are taken as some subset of the 28 bits in the left half of the master key, and the right-most 24 bits of each round sub-key are taken as some subset of the 28 bits in the right half of the master key. The entire key schedule (including the manner in which the master key is divided into left and right halves, and which bits are used in forming each sub-key $k_i$) is fixed and public, and the only secret is the master key itself.

DES 分组密码是一个 16 轮 Feistel 网络，分组长度为 64 比特，密钥长度为 56 比特。在 16 轮的每一轮中使用相同的轮函数 $\hat{f}$。轮函数接受一个 48 比特子密钥和一个 32 比特输入（即半个分组），这与（平衡）Feistel 网络的预期一致。DES 的密钥扩展用于从 56 比特主密钥派生一系列 48 比特子密钥 $k_1, \ldots, k_{16}$。DES 的密钥扩展相对简单，每个子密钥 $k_i$ 是由主密钥的 48 个比特经置换得到的一个子集。就我们的目的而言，只需注意主密钥的 56 个比特被分成两半——一个“左半部分”和一个“右半部分”——各包含 28 个比特。（这种划分发生在对密钥应用一个初始置换之后，但我们在描述中忽略这一点。）每一轮子密钥的最左边 24 个比特取自主密钥左半部分 28 个比特的某个子集，每一轮子密钥的最右边 24 个比特取自主密钥右半部分 28 个比特的某个子集。整个密钥扩展（包括主密钥被分成左右两半的方式，以及哪些比特用于形成每个子密钥 $k_i$）是固定且公开的，唯一的秘密是主密钥本身。

The DES round function. The DES round function $\hat{f}$—sometimes called the DES mangler function—is constructed using a paradigm we have previously analyzed: it is (basically) a substitution-permutation network! In more detail, computation of $\hat{f}(k_i, R)$ with $k_i \in \{0,1\}^{48}$ and $R \in \{0,1\}^{32}$ proceeds as follows: first, $R$ is expanded to a 48-bit value $R^{\prime}$. This is carried out by simply duplicating half the bits of $R$; we denote this by $R^{\prime} := E(R)$ where $E$ is called the expansion function. Following this, computation proceeds exactly as in our earlier discussion of SPNs: The expanded value $R^{\prime}$ is XORed with $k_i$, which is also 48 bits long, and the resulting value is divided into 8 blocks, each of which is 6 bits long. Each block is passed through a (different) S-box that takes a 6-bit input and yields a 4-bit output; concatenating the output from the 8 S-boxes gives a 32-bit result. A mixing permutation is then applied to the bits of this result to obtain the final output. See Figure 7.6.

DES 轮函数。DES 的轮函数 $\hat{f}$——有时称为 DES 混淆函数（mangler function）——是使用我们之前分析过的一个范式构造的：它（基本上）就是一个代换-置换网络！更详细地说，计算 $\hat{f}(k_i, R)$（其中 $k_i \in \{0,1\}^{48}$ 且 $R \in \{0,1\}^{32}$）的过程如下：首先，$R$ 被扩展为一个 48 比特值 $R^{\prime}$。这是通过简单地复制 $R$ 的一半比特来实现的；我们将其记为 $R^{\prime} := E(R)$，其中 $E$ 称为扩展函数。此后，计算过程与我们之前对 SPN 的讨论完全一样：扩展后的值 $R^{\prime}$ 与 $k_i$（同样长 48 比特）异或，所得结果被分成 8 个块，每个块长 6 比特。每个块经过一个（不同的）S 盒，该 S 盒接受 6 比特输入并产生 4 比特输出；将 8 个 S 盒的输出拼接起来得到一个 32 比特的结果。然后对该结果的比特应用混合置换，得到最终输出。见图 7.6。

One difference as compared to our original discussion of SPNs is that the S-boxes here are not invertible; indeed, they cannot be invertible since their inputs are longer than their outputs. Further discussion regarding the structural details of the S-boxes is given below.

与我们最初对 SPN 的讨论相比，一个区别是这里的 S 盒不是可逆的；事实上，它们不可能是可逆的，因为它们的输入比输出长。关于 S 盒结构细节的进一步讨论见下文。

We stress once again that everything in the above description (including the S-boxes themselves as well as the mixing permutation) is publicly known. The only secret is the master key which is used to derive all the sub-keys.

我们再次强调，上述描述中的一切（包括 S 盒本身以及混合置换）都是公开的。唯一的秘密是用于派生所有子密钥的主密钥。

![Image](https://lsky.jerryxue.top/i/2026/08/19/6a85c54b346b7.jpg)

**FIGURE 7.6: The DES mangler function.**

**图 7.6：DES 混淆函数。**

The S-boxes and the mixing permutation. The eight S-boxes that form the "core" of $\hat{f}$ are a crucial element of the DES construction and were very carefully designed. Studies of DESs have shown that if the S-boxes were slightly modified, DESs would have been much more vulnerable to attack. This should serve as a warning to anyone wishing to design a block cipher: seemingly arbitrary choices are not arbitrary at all, and if not made correctly may render the entire construction insecure.

S 盒和混合置换。构成 $\hat{f}$ “核心”的八个 S 盒是 DES 构造的关键元素，经过了非常精心的设计。对 DES 的研究表明，如果对 S 盒稍作修改，DES 就会变得容易攻击得多。这对任何希望设计分组密码的人都应当是一个警示：看似任意的选择根本不是任意的，如果选择不当可能使整个构造变得不安全。

Recall that each S-box maps a 6-bit input to a 4-bit output. Each S-box can be viewed as a table with 4 rows and 16 columns, where each cell of the table contains a 4-bit entry. A 6-bit input can be viewed as indexing one of the ${2}^6 = 64 = 4 \times 16$ cells of the table in the following way: The first and last input bits are used to choose the table row, and bits 2–5 are used to choose the table column. The 4-bit entry at some position of the table represents the output value for the input associated with that position.

回顾一下，每个 S 盒将 6 比特输入映射到 4 比特输出。每个 S 盒可以看作一个 4 行 16 列的表，表中每个单元格包含一个 4 比特条目。一个 6 比特输入可以按以下方式索引表的 ${2}^6 = 64 = 4 \times 16$ 个单元格之一：第一个和最后一个输入比特用于选择表行，第 2–5 比特用于选择表列。表中某个位置的 4 比特条目表示与该位置相关联的输入所对应的输出值。

The DES S-boxes have the following properties (among others):

DES 的 S 盒具有以下性质（及其他性质）：

1. Each S-box is a 4-to-1 function. (That is, exactly 4 inputs are mapped to each possible output.) This follows from the properties below.

   每个 S 盒是一个 4 对 1 函数。（即，恰好 4 个输入被映射到每个可能的输出。）这可由下面的性质推出。

2. Each row in the table contains each of the 16 possible 4-bit strings exactly once.

   表中的每一行恰好包含 16 个可能的 4 比特串各一次。

3. Changing one bit of any input to an S-box always changes at least two bits of the output.

   改变 S 盒任意输入的一个比特总是至少改变输出的两个比特。

The DES mixing permutation was also designed carefully. In particular it has the property that the four output bits from any S-box affect the input to six S-boxes in the next round. (This is possible because of the expansion function that is applied in the next round before the S-boxes are computed.)

DES 的混合置换也经过了精心设计。特别地，它具有这样的性质：任何 S 盒的四个输出比特会影响下一轮中六个 S 盒的输入。（这是可能的，因为在下一轮计算 S 盒之前会应用扩展函数。）

The DES avalanche effect. The design of the mangler function ensures that DES exhibits a strong avalanche effect. In order to see this, we will trace the difference between the intermediate values in the DES computations of two inputs that differ by just a single bit. Let us denote the two inputs to the cipher by $(L_0, R_0)$ and $(L^{\prime}_0, R^{\prime}_0)$, where we assume that $R_0 = R^{\prime}_0$ and so the single-bit difference occurs in the left half of the inputs (it may help to refer to Equation (7.2) and Figure 7.6 in what follows). After the first round, the intermediate values $(L_1, R_1)$ and $(L^{\prime}_1, R^{\prime}_1)$ still differ by only a single bit, although now this difference is in the right half. In the second round of DES, the right half of each intermediate value is run through $\hat{f}$. Assuming that the bit where $R_1$ and $R^{\prime}_1$ differ is not duplicated in the expansion step, the intermediate values before applying the S-boxes still differ by only a single bit. By property 3 of the S-boxes, the intermediate values after the S-box computation differ in at least two bits. The result is that the intermediate values $(L_2, R_2)$ and $(L^{\prime}_2, R^{\prime}_2)$ differ in three bits: there is a 1-bit difference between $L_2$ and $L^{\prime}_2$ (carried over from the difference between $R_1$ and $R^{\prime}_1$) and a 2-bit difference between $R_2$ and $R^{\prime}_2$.

DES 的雪崩效应。混淆函数的设计确保了 DES 展现出强的雪崩效应。为了看清这一点，我们将追踪两个仅相差一个比特的输入在 DES 计算中中间值之间的差异。我们将密码的两个输入记为 $(L_0, R_0)$ 和 $(L^{\prime}_0, R^{\prime}_0)$，其中我们假设 $R_0 = R^{\prime}_0$，因此单比特差异出现在输入的左半部分（在下面的讨论中，参考式 (7.2) 和图 7.6 可能会有所帮助）。第一轮之后，中间值 $(L_1, R_1)$ 和 $(L^{\prime}_1, R^{\prime}_1)$ 仍然只相差一个比特，尽管现在这个差异在右半部分。在 DES 的第二轮中，每个中间值的右半部分经过 $\hat{f}$ 处理。假设 $R_1$ 和 $R^{\prime}_1$ 不同的那个比特在扩展步骤中没有被复制，那么应用 S 盒之前的中间值仍然只相差一个比特。根据 S 盒的性质 3，S 盒计算之后的中间值至少有两个比特不同。结果是中间值 $(L_2, R_2)$ 和 $(L^{\prime}_2, R^{\prime}_2)$ 有三个比特不同：$L_2$ 和 $L^{\prime}_2$ 之间有 1 比特差异（由 $R_1$ 和 $R^{\prime}_1$ 之间的差异延续而来），$R_2$ 和 $R^{\prime}_2$ 之间有 2 比特差异。

The mixing permutation spreads the two-bit difference between $R_2$ and $R^{\prime}_2$ such that, in the following round, each of the two differing bits is used as input to a different S-box, resulting in a difference of at least 4 bits in the outputs from the S-boxes. (If either or both of the two bits in which $R_2$ and $R^{\prime}_2$ differ are duplicated by $E$, the difference may be even greater.) There is also now a 2-bit difference in the left halves.

混合置换将 $R_2$ 和 $R^{\prime}_2$ 之间的两比特差异扩散，使得在下一轮中，两个不同的比特各自被用作不同 S 盒的输入，导致 S 盒输出中至少有 4 比特的差异。（如果 $R_2$ 和 $R^{\prime}_2$ 不同的两个比特中的一个或两个被 $E$ 复制，差异可能更大。）此时左半部分也有 2 比特差异。

As with a substitution-permutation network, the number of "affected" bits grows exponentially and so after 7 rounds we expect all 32 bits in the right half to be affected, and after 8 rounds we expect all 32 bits in the left half will be affected as well. DES has 16 rounds, and so the avalanche effect occurs very early in the computation. This ensures that the computation of DES on similar inputs yields independent-looking outputs.

与代换-置换网络一样，“受影响”的比特数量呈指数增长，因此经过 7 轮后我们预计右半部分的所有 32 个比特都受到影响，经过 8 轮后我们预计左半部分的所有 32 个比特也将受到影响。DES 有 16 轮，因此雪崩效应在计算的早期就发生了。这确保了 DES 对相似输入的计算产生看似独立的输出。

#### Attacks on Reduced-Round DES　对减少轮数 DES 的攻击

A useful exercise for understanding more about the DES construction and its security is to look at the behavior of DES with only a few rounds. We show attacks on one-, two-, and three-round variants of DES (recall that DES has 16 rounds). DES variants with three rounds or fewer cannot be pseudorandom functions because three rounds are not enough for the avalanche effect to occur. Thus, we will be interested in demonstrating more difficult (and more damaging) key-recovery attacks which compute the key k using only a relatively small number of input/output pairs computed using that key. Some of the attacks are similar to those we have seen in the context of substitution-permutation networks; here, however, we will see how they are applied to a concrete block cipher rather than to an abstract design.

一个有用的练习是观察 DES 在只有少数几轮时的行为，这有助于更好地理解 DES 的构造及其安全性。我们展示对一轮、两轮和三轮 DES 变体的攻击（回顾 DES 有 16 轮）。三轮或更少的 DES 变体不可能是伪随机函数，因为三轮不足以使雪崩效应发生。因此，我们将展示更困难的（且更具破坏性的）密钥恢复攻击，它们仅利用少量由该密钥计算得到的输入/输出对，就能算出密钥 $k$。其中一些攻击与我们在代换-置换网络背景下看到的类似；然而，在这里我们将看到它们如何被应用于一个具体的分组密码而非抽象设计。

The attacks below will be known-plaintext attacks in which the adversary knows some plaintext/ciphertext pairs $\{(x_i, y_i)\}$ computed using some secret key $k$. When we describe the attacks, we will focus on a particular plaintext/ciphertext pair $(x, y)$ and describe the information about the key that the adversary can derive from this pair. Continuing to use the notation developed earlier, we denote the left and right halves of the input $x$ as $L_0$ and $R_0$, respectively, and let $L_i, R_i$ denote the left and right halves of the intermediate result after the $i$th round. Recall that $E$ denotes the DES expansion function, $k_i$ denotes the sub-key used in round $i$, and $f_i(R) = \hat{f}(k_i, R)$ denotes the actual function being applied in the Feistel network in the $i$th round.

下面的攻击将是已知明文攻击，其中敌手知道使用某个秘密密钥 $k$ 计算的一些明文/密文对 $\{(x_i, y_i)\}$。当我们描述这些攻击时，我们将聚焦于一个特定的明文/密文对 $(x, y)$，并描述敌手可以从该对中推导出的关于密钥的信息。继续使用之前发展的记号，我们将输入 $x$ 的左右两半分别记为 $L_0$ 和 $R_0$，并用 $L_i, R_i$ 表示第 $i$ 轮后中间结果的左右两半。回顾 $E$ 表示 DES 的扩展函数，$k_i$ 表示第 $i$ 轮使用的子密钥，$f_i(R) = \hat{f}(k_i, R)$ 表示 Feistel 网络中第 $i$ 轮应用的实际函数。

One-round DES. Say we are given an input/output pair $(x, y)$. In one-round DES, we have $y = (L_1, R_1)$, where $L_1 = R_0$ and $R_1 = L_0 \oplus f_1(R_0)$. We therefore know an input/output pair for $f_1$: specifically, we know that $f_1(R_0) = R_1 \oplus L_0$. By applying the inverse of the mixing permutation to the output $R_1 \oplus L_0$, we obtain the intermediate value consisting of the outputs from all the S-boxes, where the first 4 bits are the output from the first S-box, the next 4 bits are the output from the second S-box, and so on.

一轮 DES。假设我们给定一个输入/输出对 $(x, y)$。在一轮 DES 中，我们有 $y = (L_1, R_1)$，其中 $L_1 = R_0$ 且 $R_1 = L_0 \oplus f_1(R_0)$。因此我们知道 $f_1$ 的一个输入/输出对：具体地，我们知道 $f_1(R_0) = R_1 \oplus L_0$。通过对输出 $R_1 \oplus L_0$ 应用混合置换的逆，我们得到由所有 S 盒输出组成的中间值，其中前 4 个比特是第一个 S 盒的输出，接下来的 4 个比特是第二个 S 盒的输出，依此类推。

Consider the (known) 4-bit output of the first S-box. Since each S-box is a 4-to-1 function, this means there are exactly four possible inputs to this S-box that would result in the given output, and similarly for all the other S-boxes; each such input is 6 bits long. The input to the S-boxes is simply the XOR of $E(R_0)$ with the sub-key $k_1$. Since $R_0$, and hence $E(R_0)$, is known, we can compute a set of four possible values for each 6-bit portion of $k_1$. This means we have reduced the number of possible keys $k_1$ from ${2}^{48}$ to ${4}^{48/6} = 4^8 = 2^{16}$ (since there are four possibilities for each of the eight 6-bit portions of $k_1$). This is already a small number and so we can just try all the possibilities on a different input/output pair $(x^{\prime}, y^{\prime})$ to find the right key. We thus obtain the key using only two known plaintexts in time roughly ${2}^{16}$.

考虑第一个 S 盒的（已知的）4 比特输出。由于每个 S 盒是一个 4 对 1 函数，这意味着恰好有四个输入能让该 S 盒产生给定的输出，其他 S 盒也类似；每个这样的输入长 6 比特。S 盒的输入仅仅是 $E(R_0)$ 与子密钥 $k_1$ 的异或。由于 $R_0$（因而 $E(R_0)$）是已知的，我们可以为 $k_1$ 的每个 6 比特部分计算出一组四个可能的值。这意味着我们已将可能密钥 $k_1$ 的数量从 ${2}^{48}$ 减少到了 ${4}^{48/6} = 4^8 = 2^{16}$（因为 $k_1$ 的八个 6 比特部分各有四种可能性）。这已经是一个小数目，因此我们可以在另一个不同的输入/输出对 $(x^{\prime}, y^{\prime})$ 上尝试所有可能性以找到正确的密钥。于是我们仅使用两个已知明文，在大约 ${2}^{16}$ 的时间内就获得了密钥。

Two-round DES. In two-round DES, the output y is equal to $(L_{2}, R_{2})$ where

两轮 DES。在两轮 DES 中，输出 $y$ 等于 $(L_{2}, R_{2})$，其中

$$
\begin{aligned}&L_{1}=R_{0}\\&R_{1}=L_{0}\oplus f_{1}(R_{0})\\&L_{2}=R_{1}=L_{0}\oplus f_{1}(R_{0})\\&R_{2}=L_{1}\oplus f_{2}(R_{1}).\\ \end{aligned}
$$

$L_{0}, R_{0}, L_{2}$, and $R_{2}$ are known from the given input/output pair $(x, y)$, and thus we also know $L_{1} = R_{0}$ and $R_{1} = L_{2}$. This means that we know the input/output of both $f_{1}$ and $f_{2}$, and so the same method used in the attack on one-round DES can be used here to determine both $k_{1}$ and $k_{2}$ in time roughly ${2}\cdot2^{16}$. This attack works even if $k_1$ and $k_2$ are completely independent keys, although in fact the key schedule of DES ensures that many of the bits of $k_1$ and $k_2$ are equal (which can be used to further speed up the attack).

从给定的输入/输出对 $(x, y)$ 可以知道 $L_{0}, R_{0}, L_{2}$ 和 $R_{2}$，因此我们也知道 $L_{1} = R_{0}$ 和 $R_{1} = L_{2}$。这意味着我们知道 $f_{1}$ 和 $f_{2}$ 的输入/输出，因此攻击一轮 DES 时使用的同样方法可以在这里用来确定 $k_{1}$ 和 $k_{2}$，时间约为 ${2}\cdot2^{16}$。即使 $k_1$ 和 $k_2$ 是完全独立的密钥，这种攻击也能奏效，尽管事实上 DES 的密钥扩展确保了 $k_1$ 和 $k_2$ 的许多比特是相等的（这可以用来进一步加速攻击）。

Three-round DES. Referring to Figure 7.5, the output value $y$ is now equal to $(L_3, R_3)$. Since $L_1 = R_0$ and $R_2 = L_3$, the only unknown values in the figure are $R_1$ and $L_2$ (which are equal).

三轮 DES。参见图 7.5，输出值 $y$ 现在等于 $(L_3, R_3)$。由于 $L_1 = R_0$ 且 $R_2 = L_3$，图中唯一未知的值是 $R_1$ 和 $L_2$（二者相等）。

Now we no longer have the input/output to any round function $f_i$. For example, the output value of $f_2$ is equal to $L_1 \oplus R_2$, where both of these values are known. However, we do not know the value $R_1$ that is input to $f_2$. Similarly, we can determine the inputs to $f_1$ and $f_3$ but not the outputs of those functions. Thus, the attack we used to break one-round and two-round DES will not work here.

现在我们不再拥有任何轮函数 $f_i$ 的输入/输出。例如，$f_2$ 的输出值等于 $L_1 \oplus R_2$，其中这两个值都是已知的。然而，我们不知道作为 $f_2$ 输入的值 $R_1$。类似地，我们可以确定 $f_1$ 和 $f_3$ 的输入，但不能确定这些函数的输出。因此，我们用来破解一轮和两轮 DES 的攻击在这里不再奏效。

Instead of relying on full knowledge of the input and output of one of the round functions, we will use knowledge of a certain relation between the inputs and outputs of $f_1$ and $f_3$. Observe that the output of $f_1$ is equal to $L_0 \oplus R_1 = L_0 \oplus L_2$, and the output of $f_3$ is equal to $L_2 \oplus R_3$. Therefore,

我们不再依赖对某个轮函数输入和输出的完全了解，而是利用 $f_1$ 和 $f_3$ 的输入与输出之间的某个关系。注意 $f_1$ 的输出等于 $L_0 \oplus R_1 = L_0 \oplus L_2$，$f_3$ 的输出等于 $L_2 \oplus R_3$。因此，

$$
f_{1}(R_{0})\oplus f_{3}(R_{2})=(L_{0}\oplus L_{2})\oplus(L_{2}\oplus R_{3})=L_{0}\oplus R_{3},
$$

where both $L_{0}$ and $R_{3}$ are known. That is, the XOR of the outputs of $f_{1}$ and $f_{3}$ is known. Furthermore, the input to $f_{1}$ is $R_{0}$ and the input to $f_{3}$ is $L_{3}$, both of which are known. Summarizing: we can determine the inputs to $f_{1}$ and $f_{3}$, and the XOR of their outputs. We now describe an attack that finds the secret key based on this information.

其中 $L_{0}$ 和 $R_{3}$ 都是已知的。也就是说，$f_{1}$ 和 $f_{3}$ 输出的异或是已知的。此外，$f_{1}$ 的输入是 $R_{0}$，$f_{3}$ 的输入是 $L_{3}$，二者都是已知的。总结：我们可以确定 $f_{1}$ 和 $f_{3}$ 的输入及其输出的异或。我们现在描述一种基于这些信息找出秘密密钥的攻击。

Recall that the key schedule of DES has the property that the master key is divided into a "left half," which we denote by $k_L$, and a "right half" $k_R$, each containing 28 bits. Furthermore, the 24 left-most bits of the sub-key used in each round are taken only from $k_L$, and the 24 right-most bits of each sub-key are taken only from $k_R$. This means that $k_L$ affects only the inputs to the first four S-boxes in any round, while $k_R$ affects only the inputs to the last four S-boxes. Since the mixing permutation is known, we also know which bits of the output of each round function come from each S-box.

回顾 DES 的密钥扩展具有这样的性质：主密钥被分成一个“左半部分”（我们记为 $k_L$）和一个“右半部分” $k_R$，各包含 28 个比特。此外，每一轮使用的子密钥的最左边 24 个比特仅取自 $k_L$，每个子密钥的最右边 24 个比特仅取自 $k_R$。这意味着 $k_L$ 仅影响任何一轮中前四个 S 盒的输入，而 $k_R$ 仅影响后四个 S 盒的输入。由于混合置换是已知的，我们还知道每一轮函数输出中的哪些比特来自哪个 S 盒。

The idea behind the attack is to separately traverse the key space for each half of the master key, giving an attack with complexity roughly ${2} \cdot 2^{28}$ rather than complexity ${2}^{56}$. Such an attack will be possible if we can verify a guess of half the master key, and we now show how this can be done. Say we guess some value for $k_L$, the left half of the master key. We know the input $R_0$ of $f_1$, and so using our guess of $k_L$ we can compute the input to the first four S-boxes. This means that we can compute half the output bits of $f_1$ (the mixing permutation spreads out the bits we know, but since the mixing permutation is known we know exactly which bits those are). Likewise, we can compute the same locations in the output of $f_3$ by using the known input $L_3$ to $f_3$ and the same guess for $k_L$. Finally, we can compute the XOR of these output values and check whether they match the appropriate bits in the known value of the XOR of the outputs of $f_1$ and $f_3$. If they are not equal, then our guess for $k_L$ is incorrect. A correct guess for $k_L$ will always pass this test, and so will not be eliminated, but an incorrect guess is expected to pass this test only with probability roughly ${2}^{-16}$ (since we check equality of 16 bits in two computed values). There are ${2}^{28}$ possible values for $k_L$, so if each incorrect value remains a viable candidate with probability ${2}^{-16}$ then we expect to be left with only ${2}^{28} \cdot 2^{-16} = 2^{12}$ possibilities for $k_L$ after the above.

攻击背后的想法是分别遍历主密钥每一半的密钥空间，从而给出复杂度大约为 ${2} \cdot 2^{28}$ 而非 ${2}^{56}$ 的攻击。如果我们能够验证对主密钥一半的猜测，那么这样的攻击就是可能的，我们现在展示如何做到这一点。假设我们猜测 $k_L$（主密钥的左半部分）的某个值。我们知道 $f_1$ 的输入 $R_0$，因此使用我们对 $k_L$ 的猜测可以计算前四个 S 盒的输入。这意味着我们可以计算 $f_1$ 的一半输出比特（混合置换将我们知道的比特分散开来，但由于混合置换是已知的，我们确切地知道那些比特是哪些）。同样，利用 $f_3$ 的已知输入 $L_3$ 和对 $k_L$ 的同样猜测，我们可以计算 $f_3$ 输出中的相同位置。最后，我们可以计算这些输出值的异或，并检查它们是否与 $f_1$ 和 $f_3$ 输出异或的已知值中的相应比特匹配。如果它们不相等，那么我们对 $k_L$ 的猜测是不正确的。$k_L$ 的正确猜测将总是通过这个测试，因此不会被淘汰，但错误猜测预计仅以大约 ${2}^{-16}$ 的概率通过这个测试（因为我们在两个计算值中检查 16 个比特的相等性）。$k_L$ 有 ${2}^{28}$ 个可能的值，因此如果每个错误值以 ${2}^{-16}$ 的概率保留为可行候选，那么我们预计经过上述过程后 $k_L$ 仅剩 ${2}^{28} \cdot 2^{-16} = 2^{12}$ 种可能性。

By performing the above for each half of the master key, we obtain in time ${2} \cdot 2^{28}$ approximately ${2}^{12}$ candidates for the left half and ${2}^{12}$ candidates for the right half. Since each combination of the left and right halves is possible, we have ${2}^{24}$ candidate keys overall and can run a brute-force search over this set using an additional input/output pair $(x^{\prime}, y^{\prime})$. (An alternative that is more efficient is to simply repeat the previous attack using the ${2}^{12}$ remaining candidates for each half of the key.) The time for the attack is roughly ${2} \cdot 2^{28} + 2^{24} < 2^{30}$, much less than a ${2}^{56}$-time brute-force attack.

通过对主密钥的每一半执行上述过程，我们在 ${2} \cdot 2^{28}$ 时间内获得大约 ${2}^{12}$ 个左半部分候选和 ${2}^{12}$ 个右半部分候选。由于左右两半的每种组合都是可能的，我们总共有 ${2}^{24}$ 个候选密钥，可以使用一个额外的输入/输出对 $(x^{\prime}, y^{\prime})$ 在这个集合上进行穷举搜索。（一种更高效的替代方法是简单地使用每一半密钥剩余的 ${2}^{12}$ 个候选重复之前的攻击。）攻击的时间大约为 ${2} \cdot 2^{28} + 2^{24} < 2^{30}$，远小于 ${2}^{56}$ 时间的穷举攻击。

#### Security of DES　DES 的安全性

After almost 30 years of intensive study, the best known practical attack on DES is still an exhaustive search through its key space. (We discuss some important theoretical attacks in Section 7.2.6. Those attacks require a large number of input/output pairs, which can be difficult to obtain in an attack on any real-world system using DES.) Unfortunately, the 56-bit key length of DES is short enough that an exhaustive search through all ${2}^{56}$ possible keys is now feasible. Already in the late 1970s there were strong objections to using such a short key for DES. Back then the objection was academic, as the computational power needed to search through ${2}^{56}$ keys was generally unavailable. (It has been estimated that in 1977 a computer that could crack DES in one day would cost 20 million to build.) The practicality of a brute-force attack on DES, however, was demonstrated in 1997 when a DES challenge set up by RSA Security was solved by the DESCHALL project using thousands of computers coordinated across the Internet; the computation took 96 days. A second challenge was broken the following year in just 41 days by the distributed.net project. A significant breakthrough came in 1998 when a third challenge was solved in just 56 hours. This impressive feat was achieved via a special-purpose DES-breaking machine called Deep Crack that was built by the Electronic Frontier Foundation at a cost of 250,000. In 1999, a DES challenge was solved in just over 22 hours by a combined effort of Deep Crack and distributed.net. The current state-of-the-art is the DES cracking box by PICO Computing, which uses 48 FPGAs and can find a DES key in approximately 26 hours; see https://crack.sh for further details.

经过近 30 年的深入研究，已知的对 DES 的最佳实际攻击仍然是对其密钥空间的穷举搜索。（我们在 7.2.6 节讨论一些重要的理论攻击。那些攻击需要大量的输入/输出对，而在攻击任何使用 DES 的现实系统时，这些对可能很难获得。）不幸的是，DES 的 56 比特密钥长度足够短，使得对所有 ${2}^{56}$ 个可能密钥的穷举搜索现在是可行的。早在 20 世纪 70 年代末，就有人强烈反对为 DES 使用如此短的密钥。在当时这种反对是学术性的，因为搜索 ${2}^{56}$ 个密钥所需的计算能力通常是无法获得的。（据估计，1977 年一台能在一天内破解 DES 的计算机造价为 2000 万美元。）然而，对 DES 的穷举攻击的可行性在 1997 年得到了证明，当时 RSA Security 设立的一个 DES 挑战由 DESCHALL 项目动用数千台通过互联网协调的计算机解决；计算耗时 96 天。第二年，第二个挑战仅用 41 天就被 distributed.net 项目破解。1998 年取得了重大突破，第三个挑战仅用 56 小时就被解决。这一令人印象深刻的壮举是通过一台名为 Deep Crack 的专用 DES 破解机实现的，该机器由电子前沿基金会（Electronic Frontier Foundation）耗资 25 万美元建造。1999 年，一个 DES 挑战在 Deep Crack 和 distributed.net 的共同努力下仅用 22 个多小时就被解决。目前最先进的是 PICO Computing 的 DES 破解盒，它使用 48 个 FPGA，可以在大约 26 小时内找到一个 DES 密钥；更多细节见 https://crack.sh。

The time/space tradeoffs discussed in Section 6.4.3 show that exhaustive key-search attacks can be accelerated using pre-computation and additional memory. Due to the short key length of DES, time/space tradeoffs can be especially effective. Specifically, using pre-processing it is possible to generate a table a few terabytes large that enables recovery of a DES key with high probability from a single input/output pair using approximately ${2}^{38}$ DES evaluations (which can be computed in under a minute). The bottom line is that the key length of DES is far too short by modern standards, and DES cannot be considered secure for any serious application today.

6.4.3 节中讨论的时间/空间折中表明，穷举密钥搜索攻击可以通过预计算和额外的内存来加速。由于 DES 的密钥长度短，时间/空间折中可以特别有效。具体地，使用预处理可以生成一个几太字节大小的表，从而能以高概率从单个输入/输出对中恢复 DES 密钥（使用大约 ${2}^{38}$ 次 DES 求值，可以在不到一分钟内完成计算）。结论是，按照现代标准，DES 的密钥长度实在太短，DES 不能被认为是当今任何严肃应用的安全之选。

A second cause for concern is the relatively short block length of DES. A short block length is problematic because the concrete security of many constructions based on block ciphers depends on the block length of the cipher—even if the cipher is otherwise "perfect." For example, the proof of CTR mode (cf. Theorem 3.33) shows that plaintext information can be leaked to an attacker if an IV repeats. If CTR mode is instantiated using DES, with a block length of only 64 bits, then security is compromised with high probability after encrypting only $\approx 2^{24}$ messages.

第二个令人担忧的原因是 DES 相对较短的分组长度。短的分组长度是有问题的，因为许多基于分组密码的构造的具体安全性取决于密码的分组长度——即使该密码在其他方面是“完美的”。例如，CTR 模式的证明（参见定理 3.33）表明，如果 IV 重复，明文信息可能泄露给攻击者。如果 CTR 模式使用 DES 实例化（分组长度仅为 64 比特），那么在仅加密 $\approx 2^{24}$ 条消息后，安全性就会以高概率被破坏。

The insecurity of DES has nothing to do with its design per se, but rather is due to its short key length (and, to a lesser extent, its short block length). This is a great tribute to the designers of DES, who seem to have succeeded in constructing an almost "perfect" block cipher otherwise. Since DES itself seems not to have significant structural weaknesses, it makes sense to use DES as a building block for constructing block ciphers with longer keys. We discuss this further in Section 7.2.4.

DES 的不安全性与它的设计本身无关，而是因为它过短的密钥长度（以及在较小程度上，过短的分组长度）。这是对 DES 设计者的极大赞誉，他们似乎在其他方面成功地构造了一个几乎“完美”的分组密码。由于 DES 本身似乎没有显著的结构弱点，将 DES 用作构造具有更长密钥的分组密码的构建模块是合理的。我们在 7.2.4 节中进一步讨论这一点。

The replacement for DES—the Advanced Encryption Standard (AES), covered later in this chapter—was explicitly designed to address concerns regarding the short key length and block length of DES. AES supports 128-, 192-, and 256-bit keys, and has a 128-bit block length.

DES 的替代者——高级加密标准（AES），将在本章后面介绍——其设计目的非常明确：解决对 DES 短密钥长度和短分组长度的担忧。AES 支持 128、192 和 256 比特密钥，并具有 128 比特的分组长度。

### 7.2.4 3DES: Increasing the Key Length of a Block Cipher　7.2.4 3DES：增加分组密码的密钥长度

The main weakness of DES is its short key. It thus makes sense to try to design a block cipher with a larger key length using DES as a building block. Some approaches to doing so are discussed in this section. Although we refer to DES frequently throughout the discussion, and DES is the most prominent block cipher to which these techniques have been applied, everything we say here applies generically to any block cipher.

DES 的主要弱点是其短密钥。因此，尝试以 DES 作为构建模块来设计具有更大密钥长度的分组密码是合理的。本节讨论了这样做的一些方法。虽然我们在整个讨论中频繁提及 DES，且 DES 是应用这些技术的最突出的分组密码，但我们这里所说的一切都同样适用于任何分组密码。

Internal modifications vs. "black-box" constructions. There are two general approaches one could take to constructing another cipher based on DES. The first approach would be to somehow modify the internal structure of DES, while increasing the key length. For example, one could leave the round function untouched and simply use a 128-bit master key with a different key schedule (still choosing a 48-bit sub-key in each round). Or, one could change the S-boxes themselves and use a larger sub-key in each round. The disadvantage of such approaches is that by modifying DES—in even the smallest way—we lose the confidence we have gained in DES by virtue of the fact that it has remained resistant to attack for so many years. Cryptographic constructions are very sensitive; even mild, seemingly insignificant changes can render a construction completely insecure. (In fact, various results to this effect have been shown for DES; e.g., changing the S-boxes or the mixing permutation can make DES much more vulnerable to attack.) Tweaking the internal components of a block cipher is therefore not recommended.

内部修改与“黑盒”构造。基于 DES 构造另一个密码可以采取两种一般方法。第一种方法是以某种方式修改 DES 的内部结构，同时增加密钥长度。例如，可以保持轮函数不变，简单地使用 128 比特主密钥和不同的密钥扩展（在每一轮中仍然选择 48 比特子密钥）。或者，可以改变 S 盒本身并在每一轮使用更大的子密钥。这种方法的缺点在于：即使只对 DES 做最小的修改，我们也会失去对 DES 的信心，而这信心正是它多年来抵御攻击换来的。密码构造非常敏感；即使是微小的、看似无关紧要的改变也可能使构造变得完全不安全。（事实上，针对 DES 已有多种此类结论；例如，改变 S 盒或混合置换会使 DES 更容易受到攻击。）因此，不建议对分组密码的内部组件进行调整。

An alternative approach that does not suffer from the above problem is to use DES as a "black box" and not touch its internal structure at all. In following this approach we treat DES as a "perfect" block cipher with a 56-bit key, and construct a new block cipher that only invokes the original, unmodified DES. Since DES itself is not tampered with, this is a much more prudent approach and is the one we will pursue here.

一种不存在上述问题的替代方法是将 DES 用作“黑盒”，完全不触及它的内部结构。遵循这种方法，我们将 DES 视为具有 56 比特密钥的“完美”分组密码，并构造一个新的分组密码，该密码仅调用原始的、未经修改的 DES。由于 DES 本身没有被篡改，这是一种更加谨慎的方法，也是我们在这里将采用的方法。

#### Double Encryption　双重加密

Let $F$ be a block cipher with an $n$-bit key length and $\ell$-bit block length. Then a new block cipher $F^{\prime}$ with a key of length ${2}n$ can be defined by

设 $F$ 是一个具有 $n$ 比特密钥长度和 $\ell$ 比特分组长度的分组密码。那么可以按如下方式定义一个新的分组密码 $F^{\prime}$，其密钥长度为 ${2}n$：

$$
F^{\prime}_{k_{1},k_{2}}(x)\stackrel{\mathrm{def}}{=}F_{k_{2}}(F_{k_{1}}(x)),
$$

where $k_1$ and $k_2$ are independent keys. If exhaustive key search were the best available attack, this would mean that the best attack would require time ${2}^{2n}$. Unfortunately, we show an attack on $F^{\prime}$ that runs in time roughly ${2}^n$. This means that $F^{\prime}$ is not any more secure against brute-force attacks than $F$, even though $F^{\prime}$ has a key that is twice as long. $^4$

其中 $k_1$ 和 $k_2$ 是独立的密钥。如果穷举密钥搜索是最佳的可用攻击，这意味着最佳攻击将需要 ${2}^{2n}$ 的时间。不幸的是，我们展示一种对 $F^{\prime}$ 的攻击，其运行时间大约为 ${2}^n$。这意味着 $F^{\prime}$ 在抵御穷举攻击方面并不比 $F$ 更安全，尽管 $F^{\prime}$ 的密钥长度是前者的两倍。$^4$

$^4$ This is not quite true since a brute-force attack on F can be carried out in time ${2}^n$ and constant memory, whereas the attack we show on $F^{\prime}$ requires ${2}^n$ time and ${2}^n$ memory. Nevertheless, the attack illustrates that $F^{\prime}$ does not achieve the desired level of security. / 严格来说这并不完全成立：对 F 的穷举攻击可以只用 ${2}^n$ 时间和常数内存完成，而这里对 $F^{\prime}$ 展示的攻击需要 ${2}^n$ 时间和 ${2}^n$ 内存。尽管如此，该攻击表明 $F^{\prime}$ 并未达到所期望的安全水平。

The attack is called a "meet-in-the-middle attack," for reasons that will soon become clear. Say the adversary is given a single input/output pair $(x, y)$, where $y = F^{\prime}_{k_1^*, k_2^*}(x) = F_{k_2^*}(F_{k_1^*}(x))$ for unknown $k_1^*, k_2^*$. The adversary can narrow down the set of possible keys in the following way:

这种攻击被称为“中间相遇攻击”，原因很快就会清楚。假设敌手获得单个输入/输出对 $(x, y)$，其中 $y = F^{\prime}_{k_1^*, k_2^*}(x) = F_{k_2^*}(F_{k_1^*}(x))$，而 $k_1^*, k_2^*$ 未知。敌手可以通过以下方式缩小可能密钥的集合：

1. For each $k_1 \in \{0,1\}^n$, compute $z := F_{k_1}(x)$ and store $(z, k_1)$ in a list $L$.

   对于每个 $k_1 \in \{0,1\}^n$，计算 $z := F_{k_1}(x)$ 并将 $(z, k_1)$ 存储在列表 $L$ 中。

2. For each $k_2 \in \{0,1\}^n$, compute $z := F_{k_2}^{-1}(y)$ and store $(z, k_2)$ in a list $L^{\prime}$.

   对于每个 $k_2 \in \{0,1\}^n$，计算 $z := F_{k_2}^{-1}(y)$ 并将 $(z, k_2)$ 存储在列表 $L^{\prime}$ 中。

3. Call entries $(z_1, k_1) \in L$ and $(z_2, k_2) \in L^{\prime}$ a match if $z_1 = z_2$. For each such match, add $(k_1, k_2)$ to a set $S$. (Matches can be found easily by first sorting the elements in $L$ and $L^{\prime}$ by their first entry.)

   如果 $z_1 = z_2$，则称条目 $(z_1, k_1) \in L$ 和 $(z_2, k_2) \in L^{\prime}$ 为一个匹配。对于每个这样的匹配，将 $(k_1, k_2)$ 添加到集合 $S$ 中。（通过首先将 $L$ 和 $L^{\prime}$ 中的元素按第一项排序，可以容易地找到匹配。）

See Figure 7.7 for a graphical depiction of the attack. The attack requires ${2} \cdot 2^n$ evaluations of $F$, and uses ${2} \cdot (n + \ell) \cdot 2^n$ bits of memory.

攻击的图示见图 7.7。该攻击需要 ${2} \cdot 2^n$ 次 $F$ 的求值，并使用 ${2} \cdot (n + \ell) \cdot 2^n$ 比特的内存。

The set S output by this algorithm contains exactly those values $(k_{1}, k_{2})$ for which

该算法输出的集合 S 恰好包含满足以下条件的那些值 $(k_{1}, k_{2})$：

$$
F_{k_{1}}(x)=F_{k_{2}}^{-1}(y) \tag{7.3}
$$

or, equivalently, for which $y = F_{k_1, k_2}^{\prime}(x)$. In particular, $(k_1^*, k_2^*) \in S$. On the other hand, a pair $(k_1, k_2) \neq (k_1^*, k_2^*)$ is (heuristically) expected to satisfy Equation (7.3) with probability ${2}^{-\ell}$ if we treat $F_{k_1}(x)$ and $F_{k_2}^{-1}(y)$ as uniform $\ell$-bit strings, and so the expected size of S is ${2}^{2n} \cdot 2^{-\ell} = 2^{2n-\ell}$. Using another few input/output pairs, and taking the intersection of the sets that are obtained, the correct $(k_1^*, k_2^*)$ can be identified with very high probability.

或者等价地，满足 $y = F_{k_1, k_2}^{\prime}(x)$。特别地，$(k_1^*, k_2^*) \in S$。另一方面，一对 $(k_1, k_2) \neq (k_1^*, k_2^*)$ （启发式地）预计以概率 ${2}^{-\ell}$ 满足式 (7.3)（如果我们将 $F_{k_1}(x)$ 和 $F_{k_2}^{-1}(y)$ 视为均匀的 $\ell$ 比特串），因此 S 的期望大小为 ${2}^{2n} \cdot 2^{-\ell} = 2^{2n-\ell}$。使用另外几个输入/输出对，并取所得集合的交集，可以以很高的概率识别出正确的 $(k_1^*, k_2^*)$。

![Image](https://lsky.jerryxue.top/i/2026/08/19/6a85c54d67957.jpg)

**FIGURE 7.7: A meet-in-the-middle attack.**

**图 7.7：中间相遇攻击。**

#### Triple Encryption　三重加密

The obvious generalization of the preceding approach is to apply the block cipher three times in succession. Two variants of this approach are common:

上述方法的一个明显推广是连续应用分组密码三次。这种方法的两个常见变体是：

Variant 1: three keys. The most natural thing to do is to choose three independent keys, i.e., to define $F_{k_1,k_2,k_3}^{\prime\prime}(x) \overset{\mathrm{def}}{=} F_{k_3}(F_{k_2}^{-1}(F_{k_1}(x)))$.

变体 1：三密钥。最自然的做法是选择三个独立的密钥，即定义 $F_{k_1,k_2,k_3}^{\prime\prime}(x) \overset{\mathrm{def}}{=} F_{k_3}(F_{k_2}^{-1}(F_{k_1}(x)))$。

Variant 2: two keys. As we explain below, another option is to choose two independent keys and define $F_{k_1,k_2}^{\prime\prime}(x) \overset{\mathrm{def}}{=} F_{k_1}(F_{k_2}^{-1}(F_{k_1}(x)))$.

变体 2：两密钥。正如我们在下面解释的，另一种选择是选择两个独立的密钥并定义 $F_{k_1,k_2}^{\prime\prime}(x) \overset{\mathrm{def}}{=} F_{k_1}(F_{k_2}^{-1}(F_{k_1}(x)))$。

Note that the middle invocation of $F$ is traditionally reversed. If $F$ is a secure cipher this makes no difference as far as security is concerned (since if $F$ is a strong pseudorandom permutation then $F^{-1}$ is too). This is done for backward compatibility: by setting $k_{3} = k_{2} = k_{1}$, the resulting cipher is equivalent to a single invocation of $F$ using the key $k_{1}$.

注意，按照惯例，中间那次对 $F$ 的调用是反向的。如果 $F$ 是一个安全的密码，这对安全性没有影响（因为如果 $F$ 是强伪随机置换，那么 $F^{-1}$ 也是）。这样做是为了向后兼容：通过设置 $k_{3} = k_{2} = k_{1}$，所得密码等价于使用密钥 $k_{1}$ 的单次 $F$ 调用。

Security of the first variant. The key length of the first variant is 3n, and so we might hope that the best attack requires time ${2}^{3n}$. However, the cipher is susceptible to a meet-in-the-middle attack (just as in the case of double encryption) that here requires ${2}^{2n}$ time.

第一个变体的安全性。第一个变体的密钥长度为 3n，因此我们可能希望最佳攻击需要 ${2}^{3n}$ 的时间。然而，该密码容易受到中间相遇攻击（与双重加密的情况一样），这里需要 ${2}^{2n}$ 的时间。

Security of the second variant. The key length of this variant is ${2}n$, and a meet-in-the-middle attack requires time ${2}^{2n}$. Assuming $\ell \geq n$, this is the best known attack when the adversary is given only a few input/output pairs. (There is a known-plaintext attack using ${2}^t$ input/output pairs that runs in time $\approx 2^{n+\ell-t}$. See Exercise 7.16.)

第二个变体的安全性。该变体的密钥长度为 ${2}n$，中间相遇攻击需要 ${2}^{2n}$ 的时间。假设 $\ell \geq n$，这是当敌手仅获得少量输入/输出对时的最佳已知攻击。（有一个使用 ${2}^t$ 个输入/输出对的已知明文攻击，运行时间为 $\approx 2^{n+\ell-t}$。见习题 7.16。）

Triple-DES (3DES). Triple-DES (or 3DES), standardized in 1999, is based on three invocations of DES using two or three keys, as described above. Two-key 3DES (which corresponds to the second variant) is no longer recommended, in part due to the known-plaintext attack mentioned above. Three-key 3DES is still used, though the current recommendation is to phase it out due to its small block length and the fact that it is relatively slow. These drawbacks have led to 3DES to be supplanted in practice by the Advanced Encryption Standard, described in the next section.

三重 DES（3DES）。三重 DES（或 3DES）于 1999 年标准化，基于如上所述的使用两个或三个密钥的三次 DES 调用。两密钥 3DES（对应于第二个变体）不再被推荐，部分原因是上面提到的已知明文攻击。三密钥 3DES 仍在使用，不过由于它的分组长度偏小、速度又相对较慢，目前的建议是逐步淘汰它。这些缺点导致 3DES 在实践中被下一节描述的高级加密标准所取代。

### 7.2.5 AES – The Advanced Encryption Standard　7.2.5 AES——高级加密标准

In January 1997, the United States National Institute of Standards and Technology (NIST) announced that it would hold a competition to select a new block cipher—to be called the Advanced Encryption Standard, or AES—to replace DES. The competition began with an open call for teams to submit candidate block ciphers for evaluation. A total of 15 different algorithms were submitted from all over the world, including contributions from many of the best cryptographers and cryptanalysts. Each team's candidate cipher was intensively analyzed by members of NIST, the public, and (especially) the other teams. Two workshops were held, one in 1998 and one in 1999, to discuss and analyze the various submissions. Following the second workshop, NIST narrowed the field down to 5 "finalists" and the second round of the competition began. A third AES workshop was held in April 2000, inviting additional scrutiny on the five finalists. In October 2000, NIST announced that the winning algorithm was Rijndael (a block cipher designed by the Belgian cryptographers Vincent Rijmen and Joan Daemen), although NIST conceded that any of the 5 finalists would have made an excellent choice. In particular, no serious security vulnerabilities were found in any of the 5 finalists, and the selection of a "winner" was based in part on properties such as efficiency, performance in hardware, flexibility, etc.

1997 年 1 月，美国国家标准与技术研究院（NIST）宣布将举办一场竞赛，以选出一个新的分组密码——称为高级加密标准（Advanced Encryption Standard，AES）——来替代 DES。竞赛伊始，组织方公开征集各团队提交候选分组密码以供评估。共有来自世界各地的 15 种不同算法被提交，包括许多最优秀的密码学家和密码分析家的贡献。每个团队的候选密码都经受了 NIST 成员、公众以及（特别是）其他团队的深入分析。1998 年和 1999 年各举行了一次研讨会，以讨论和分析各种提交方案。在第二次研讨会之后，NIST 将范围缩小到 5 个“入围者”，竞赛的第二轮开始。2000 年 4 月举行了第三次 AES 研讨会，邀请对五个入围者进行额外的审查。2000 年 10 月，NIST 宣布获胜算法为 Rijndael（一种由比利时密码学家 Vincent Rijmen 和 Joan Daemen 设计的分组密码），尽管 NIST 承认五个入围者中的任何一个都会是一个出色的选择。特别地，在五个入围者中都没有发现严重的安全漏洞，“获胜者”的选择部分基于效率、硬件性能、灵活性等性质。

The process of selecting AES was ingenious because any group that submitted an algorithm (and was therefore interested in having its algorithm adopted) had strong motivation to find attacks on the other submissions. This incentivized the world's best cryptanalysts to focus their attention on finding even the slightest weaknesses in the candidate ciphers submitted to the competition. After only a few years each candidate algorithm was already subjected to intensive study, thus increasing confidence in the security of the winner. Of course, the longer AES is used and studied without being broken, the more our confidence in it continues to grow. Today, AES is widely used and no significant security weaknesses have been discovered.

选择 AES 的过程非常巧妙，因为任何提交算法的团队（因此有兴趣让其算法被采纳）都有强烈的动机去寻找对其他提交方案的攻击。这激励了世界上最优秀的密码分析家集中注意力寻找提交给竞赛的候选密码中哪怕是极微小的弱点。仅经过几年时间，每个候选算法都已受到深入研究，从而增加了对获胜者安全性的信心。当然，AES 被使用和研究的时间越长而不被破解，我们对它的信心就越强。如今，AES 被广泛使用，且未发现显著的安全弱点。

The AES construction. We present the high-level structure of AES. As with DES, we will not present a full specification and our description should not be used as a basis for implementation. Our aim is only to provide a general idea of how the algorithm works.

AES 的构造。我们介绍 AES 的高层结构。正如 DES 一样，我们不提供完整的规范，我们的描述不应当作实现的依据。我们的目的只是提供算法如何工作的一般概念。

The AES block cipher has three variants called AES-128, AES-192, and AES-256 that use 128-, 192-, or 256-bit keys, respectively; they all have a 128-bit block length. The length of the key affects the key schedule (i.e., the way sub-keys are derived from the master key) as well as the number of rounds, but does not affect the high-level structure of each round.

AES 分组密码有三个变体，分别称为 AES-128、AES-192 和 AES-256，分别使用 128、192 或 256 比特密钥；它们都具有 128 比特的分组长度。密钥的长度影响密钥扩展（即子密钥从主密钥派生的方式）以及轮数，但不影响每一轮的高层结构。

In contrast to DES, which uses a Feistel structure, AES is essentially a substitution-permutation network. During computation of the AES algorithm, a 4-by-4 array of bytes called the state is modified in a series of rounds. The state is initially set equal to the input to the cipher (note that the input is 128 bits, which is exactly 16 bytes). In each round, the following operations are then applied to the state:

与使用 Feistel 结构的 DES 相比，AES 本质上是一个代换-置换网络。在 AES 算法的计算过程中，一个称为状态的 4×4 字节阵列在一系列轮次中被修改。状态最初被设为密码的输入（注意输入是 128 比特，恰好是 16 字节）。在每一轮中，对状态应用以下操作：

Stage 1 – AddRoundKey: A 128-bit sub-key is derived from the master key, and viewed as a 4-by-4 array of bytes. The state array is updated by XORing it with this sub-key.

阶段 1——AddRoundKey（轮密钥加）：从主密钥派生一个 128 比特子密钥，并将其视为 4×4 字节阵列。状态阵列通过与该子密钥异或来更新。

Stage 2 – SubBytes: In this step, each byte of the state array is replaced by another byte according to a single, fixed lookup table S. This substitution table (or S-box) is a permutation on $\{0,1\}^{8}$.

阶段 2——SubBytes（字节代换）：在这一步中，状态阵列的每个字节根据一个单一的、固定的查找表 S 被另一个字节替换。这个代换表（或 S 盒）是 $\{0,1\}^{8}$ 上的一个置换。

Stage 3 – ShiftRows: Next, the bytes in each row of the state array are shuffled as follows: the first row of the array is untouched, each byte in the second row is shifted one place to the left, the third row is shifted two places to the left, and the fourth row is shifted three places to the left. (All shifts are cyclic so that, e.g., in the second row the first byte becomes the fourth byte.)

阶段 3——ShiftRows（行移位）：接下来，状态阵列每一行中的字节按如下方式洗牌：阵列的第一行保持不变，第二行的每个字节向左移一位，第三行向左移两位，第四行向左移三位。（所有移位都是循环的，因此例如在第二行中第一个字节变成第四个字节。）

Stage 4 – MixColumns: Finally, an invertible linear transformation is applied to the four bytes in each column. This transformation has the property that if two inputs differ in $b>0$ bytes, then the resulting outputs differ in at least ${5}-b$ bytes.

阶段 4——MixColumns（列混淆）：最后，对每一列中的四个字节应用一个可逆线性变换。该变换具有这样的性质：如果两个输入在 $b>0$ 个字节上不同，则所得输出在至少 ${5}-b$ 个字节上不同。

In the final round, MixColumns is replaced with AddRoundKey. This prevents an adversary from simply inverting the last three stages, which do not depend on the key.

在最后一轮中，MixColumns 被 AddRoundKey 替代。这防止了敌手简单地求逆最后三个不依赖于密钥的阶段。

By treating stages 3 and 4 as one step, we see that each round of AES has the structure of a substitution-permutation network: the round sub-key is first XORed with the input to the current round in a key-mixing step; next, an invertible S-box is applied to each byte of the resulting value; finally, the bits of the result are "permuted." The only difference is that, unlike our previous description of substitution-permutation networks, here the final step does not consist of simply shuffling the bits using a mixing permutation, but is instead carried out using a permutation plus an invertible linear transformation. Nevertheless, the net effect—namely, diffusion—is the same. Note that, as we have pointed out previously in our discussion of SPNs, a final key-mixing step is done after the last round.

通过将阶段 3 和 4 视为一个步骤，我们可以看到 AES 的每一轮具有代换-置换网络的结构：轮子密钥首先在密钥混合步骤中与当前轮的输入异或；接着，对所得值的每个字节应用一个可逆 S 盒；最后，结果的比特被“置换”。唯一的区别在于，与我们之前对代换-置换网络的描述不同，这里的最后一步不是简单地使用混合置换来洗牌比特，而是通过一个置换加上一个可逆线性变换来执行。尽管如此，净效果——即扩散——是相同的。注意，正如我们之前在讨论 SPN 时已经指出的，在最后一轮之后会进行一个最终的密钥混合步骤。

The number of rounds depends on the key length. Ten rounds are used for a AES-128, 12 rounds for AES-192, and 14 rounds for a AES-256.

轮数取决于密钥长度。AES-128 使用 10 轮，AES-192 使用 12 轮，AES-256 使用 14 轮。

Security of AES. As we have mentioned, the AES cipher was subject to intense scrutiny during the selection process and has continued to be studied ever since. To date, there are no practical cryptanalytic attacks that are significantly better than an exhaustive search for the key.

AES 的安全性。正如我们所提到的，AES 密码在选择过程中经受了严格的审查，并且此后一直被持续研究。迄今为止，没有比穷举搜索密钥显著更好的实际密码分析攻击。

We conclude that, as of today, AES constitutes an excellent choice for any cryptographic scheme that requires a (strong) pseudorandom permutation. It is free, standardized, efficient, and highly secure.

我们得出结论，截至今天，对于任何需要（强）伪随机置换的密码方案，AES 都是一个出色的选择。它是免费的、标准化的、高效的，且高度安全。

### 7.2.6 \*Differential and Linear Cryptanalysis　7.2.6 \*差分和线性密码分析

Block ciphers are relatively complicated, and as such are difficult to analyze. Nevertheless, one should not be fooled into thinking that a complicated cipher is necessarily difficult to break. On the contrary, it is very hard to construct a secure block cipher, and surprisingly easy to find attacks on most constructions (no matter how complicated they appear). This should serve as a warning that non-experts should not try to construct new ciphers. Given the availability of AES, it is hard to justify using anything else.

分组密码相对复杂，因此难以分析。然而，人们不应被误导而认为一个复杂的密码就一定难以破解。恰恰相反，构造一个安全的分组密码非常困难，而对大多数构造找到攻击却出人意料地容易（无论它们看起来多么复杂）。这应当作为一个警示：非专家不应尝试构造新的密码。既然已有 AES 可用，再使用其他任何算法都难以有正当理由。

In this section we describe two tools that are now a standard part of the cryptanalyst's toolbox. Our goal here is to give a taste of some advanced cryptanalysis, as well as to reinforce the idea that designing a secure block cipher involves careful choice of its components.

在本节中，我们描述两种如今已成为密码分析家标准工具箱一部分的工具。我们这里的目标是让读者体验一些高级密码分析，并强化这样一个观念：设计安全的分组密码需要仔细选择其组件。

Differential cryptanalysis. This technique, which can lead to a chosen-plaintext attack on a block cipher, was first presented in the late 1980s by Biham and Shamir, who used it to attack DES in 1993. The basic idea behind the attack is to tabulate specific differences in the input that lead to specific differences in the output with probability greater than would be expected for a random permutation. Specifically, say the differential $\left(\Delta_x, \Delta_y\right)$ occurs in some keyed permutation $G$ with probability $p$ if for uniform inputs $x_1$ and $x_2$ satisfying $x_1 \oplus x_2 = \Delta_x$, and uniform choice of key $k$, the probability that $G_k(x_1) \oplus G_k(x_2) = \Delta_y$ is $p$. For any fixed $\left(\Delta_x, \Delta_y\right)$ and $x_1, x_2$ satisfying $x_1 \oplus x_2 = \Delta_x$, if we choose a uniform function $f : \{0, 1\}^{\ell} \to \{0, 1\}^{\ell}$, we have $\Pr[f(x_1) \oplus f(x_2) = \Delta_y] = 2^{-\ell}$. In a weak block cipher, however, there may be differentials that occur with significantly higher probability. This can be leveraged to give a full key-recovery attack, as we now show for SPNs.

差分密码分析。这种技术可以导致对分组密码的选择明文攻击，最早由 Biham 和 Shamir 在 20 世纪 80 年代末提出，他们于 1993 年用它来攻击 DES。攻击背后的基本思想是列出这样的输入差分：它们以高于随机置换预期的概率导致特定的输出差分。具体地，称差分 $\left(\Delta_x, \Delta_y\right)$ 在某个带密钥的置换 $G$ 中以概率 $p$ 出现，如果对于满足 $x_1 \oplus x_2 = \Delta_x$ 的均匀输入 $x_1$ 和 $x_2$ 以及均匀选择的密钥 $k$，$G_k(x_1) \oplus G_k(x_2) = \Delta_y$ 的概率为 $p$。对于任意固定的 $\left(\Delta_x, \Delta_y\right)$ 和满足 $x_1 \oplus x_2 = \Delta_x$ 的 $x_1, x_2$，如果我们选择均匀函数 $f : \{0, 1\}^{\ell} \to \{0, 1\}^{\ell}$，则 $\Pr[f(x_1) \oplus f(x_2) = \Delta_y] = 2^{-\ell}$。然而，在一个弱的分组密码中，可能存在以显著更高概率出现的差分。这可以被利用来实施完整的密钥恢复攻击，我们现在对 SPN 展示这一点。

We describe the basic idea, and then work through a concrete example. Let $F$ be an $r$-round SPN with an $\ell$-bit block length, and let $G_k(x)$ denote the intermediate result in the computation of $F_k(x)$ after applying the key-mixing step of the last round. (That is, $G$ excludes the $S$-box substitution and mixing permutation of the last round, as well as the final key-mixing step.) Assume there is a differential $(\Delta_x, \Delta_y)$ in $G$ that occurs with probability $p \gg 2^{-\ell}$. It is possible to exploit this high-probability differential to learn bits of the final sub-key $k_{r+1}$. The high-level idea is as follows: let $\{(x_1^i, x_2^i)\}_{i=1}^L$ be a collection of $L$ pairs of random inputs with differential $\Delta_x$, i.e., with $x_1^i \oplus x_2^i = \Delta_x$ for all $i$. Using a chosen-plaintext attack, obtain $y_1^i = F_k(x_1^i)$ and $y_2^i = F_k(x_2^i)$ for all $i$. Now, for each possible $k_{r+1}^*\in\{0,1\}^\ell$ do: for each pair $y_1^i, y_2^i$, invert the final key-mixing step using $k_{r+1}^*$, and also invert the mixing permutation and $S$-boxes of round $r$ (which do not depend on the master key) to obtain $\tilde{y}_1^i$, $\tilde{y}_2^i$. Note that when $k_{r+1}^* = k_{r+1}$ we have $\tilde{y}_1^i = G_k(x_1^i)$ and $\tilde{y}_2^i = G_k(x_2^i)$, and in that case we expect that a $p$-fraction of the pairs will satisfy $\tilde{y}_1^i \oplus \tilde{y}_2^i = \Delta_y$. On the other hand, when $k^* \neq k_{r+1}$ we heuristically expect only a ${2}^{-\ell}$-fraction of the pairs to yield this differential. By setting $L$ large enough, the correct value of the final sub-key $k_{r+1}$ can be determined.

我们描述基本思想，然后通过一个具体例子来演示。设 $F$ 是一个具有 $\ell$ 比特分组长度的 $r$ 轮 SPN，令 $G_k(x)$ 表示在 $F_k(x)$ 的计算中应用最后一轮密钥混合步骤后的中间结果。（也就是说，$G$ 排除了最后一轮的 $S$ 盒代换和混合置换，以及最终的密钥混合步骤。）假设 $G$ 中存在一个以概率 $p \gg 2^{-\ell}$ 出现的差分 $(\Delta_x, \Delta_y)$。可以利用这个高概率差分来学习最终子密钥 $k_{r+1}$ 的比特。高层想法如下：令 $\{(x_1^i, x_2^i)\}_{i=1}^L$ 为 $L$ 对具有差分 $\Delta_x$ 的随机输入的集合，即对所有 $i$ 有 $x_1^i \oplus x_2^i = \Delta_x$。使用选择明文攻击，对所有 $i$ 获得 $y_1^i = F_k(x_1^i)$ 和 $y_2^i = F_k(x_2^i)$。现在，对每个可能的 $k_{r+1}^*\in\{0,1\}^\ell$ 执行以下操作：对每对 $y_1^i, y_2^i$，使用 $k_{r+1}^*$ 求逆最终的密钥混合步骤，并求逆第 $r$ 轮的混合置换和 $S$ 盒（它们不依赖于主密钥），得到 $\tilde{y}_1^i$、$\tilde{y}_2^i$。注意当 $k_{r+1}^* = k_{r+1}$ 时，我们有 $\tilde{y}_1^i = G_k(x_1^i)$ 和 $\tilde{y}_2^i = G_k(x_2^i)$，此时我们预计有 $p$ 比例的输入对满足 $\tilde{y}_1^i \oplus \tilde{y}_2^i = \Delta_y$。另一方面，当 $k^* \neq k_{r+1}$ 时，我们启发式地预计仅有 ${2}^{-\ell}$ 比例的输入对产生这个差分。通过将 $L$ 设得足够大，就可以确定最终子密钥 $k_{r+1}$ 的正确值。

This works, but requires enumerating over ${2}^{\ell}$ possible values for the final sub-key. We can do better by guessing portions of $k_{r+1}$ at a time. More concretely, assume the S-boxes in $F$ have 1-byte input/output length, and focus on the first byte of $\Delta_y$. It is possible to verify if the differential holds in that byte by guessing only 8 bits of $k_{r+1}$, namely, the 8 bits that correspond (after the round-r mixing permutation) to the output of the first S-box. Thus, proceeding as above, we can learn these 8 bits by enumerating over all possible values for those bits, and seeing which value yields the desired differential in the first byte with the highest probability. Incorrect guesses for those 8 bits yield the expected differential in that byte with (heuristic) probability ${2}^{-8}$, but the correct guess will give the expected differential with probability roughly $p + 2^{-8}$; this is because with probability $p$ the differential holds on the entire block (so in particular for the first byte), and when this is not the case then we can treat the differential in the first byte as random. Note that different differentials may be needed to learn different portions of $k_{r+1}$.

这可行，但需要枚举最终子密钥的 ${2}^{\ell}$ 个可能值。我们可以做得更好，方法是每次猜测 $k_{r+1}$ 的一部分。更具体地，假设 $F$ 中的 S 盒具有 1 字节的输入/输出长度，并关注 $\Delta_y$ 的第一个字节。只需猜测 $k_{r+1}$ 的 8 个比特（即经过第 $r$ 轮混合置换后对应第一个 S 盒输出的那 8 个比特），就可以验证差分是否在该字节上成立。因此，按上述方式进行，我们可以通过枚举这些比特的所有可能值，并观察哪个值以最高概率在第一个字节上产生所需差分，来学得这 8 个比特。对这 8 个比特的错误猜测以（启发式）概率 ${2}^{-8}$ 产生该字节上的预期差分，但正确猜测将以大约 $p + 2^{-8}$ 的概率产生预期差分；这是因为以概率 $p$ 差分在整个块上成立（因此特别地也适用于第一个字节），而当不成立时，我们可以将第一个字节中的差分视为随机的。注意，可能需要不同的差分来学习 $k_{r+1}$ 的不同部分。

In practice, various optimizations are performed to improve the effectiveness of the above test or, more specifically, to increase the gap between the probability that an incorrect guess for (bits of) $k_{r+1}$ yields the differential vs. the probability that a correct guess does. One optimization is to use a low-weight differential in which $\Delta_y$ has many zero bytes. Any pairs $\tilde{y}_1, \tilde{y}_2$ satisfy such a differential have equal values entering many of the S-boxes in round $r$, and so will result in output values $y_1, y_2$ that are equal in the corresponding bit-positions (depending on the final mixing permutation). This means that the attacker can simply discard any pairs $(y_1^i, y_2^i)$ that do not agree in those bit-positions (since the corresponding intermediate values $(\tilde{y}_1, \tilde{y}_2)$ cannot possibly satisfy the differential, for any choice of the final sub-key). This significantly improves the effectiveness of the attack.

在实践中，会执行各种优化来提高上述测试的有效性，或者更具体地说，来增大对 $k_{r+1}$（的比特）的错误猜测产生差分的概率与正确猜测产生差分的概率之间的差距。一种优化是使用低重量差分，其中 $\Delta_y$ 有许多零字节。任何满足这种差分的输入对 $\tilde{y}_1, \tilde{y}_2$，在进入第 $r$ 轮中许多 S 盒时取值都相等，因此会得到在相应比特位置上相等的输出值 $y_1, y_2$（取决于最终的混合置换）。这意味着攻击者可以简单地丢弃那些在这些比特位置上不一致的输入对 $(y_1^i, y_2^i)$（因为对于最终子密钥的任何选择，对应的中间值 $(\tilde{y}_1, \tilde{y}_2)$ 都不可能满足差分）。这显著提高了攻击的有效性。

Once $k_{r+1}$ is known, the attacker can "peel off" the final key-mixing step, as well as the mixing permutation and S-box substitution steps of round $r$ (since these do not depend on the master key), and then apply the same attack—using a different differential—to find the $r$th-round sub-key $k_r$, and so on, until it learns all sub-keys (or, equivalently, the master key). Relations between the sub-keys can be used to improve the efficiency of the attack.

一旦 $k_{r+1}$ 已知，攻击者就可以“剥离”最终的密钥混合步骤，以及第 $r$ 轮的混合置换和 S 盒代换步骤（因为它们不依赖于主密钥），然后使用不同的差分应用同样的攻击来找到第 $r$ 轮子密钥 $k_r$，依此类推，直到它学得所有子密钥（或等价地，主密钥）。子密钥之间的关系可用于提高攻击的效率。

**A worked example. We work through a "toy" example, illustrating also how a good differential can be found. We use a four-round SPN with a block length of 16 bits, based on a single S-box with 4-bit input/output length. The S-box is defined as follows:**

**一个演算示例。我们演算一个“玩具”例子，同时也说明如何找到一个好的差分。我们使用一个 16 比特分组长度、基于单个具有 4 比特输入/输出长度的 S 盒的四轮 SPN。该 S 盒定义如下：**

| Input: 输入 | 0000 | 0001 | 0010 | 0011 | 0100 | 0101 | 0110 | 0111 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Output: 输出 | 0000 | 1011 | 0101 | 0001 | 0110 | 1000 | 1101 | 0100 |
| Input: 输入 | 1000 | 1001 | 1010 | 1011 | 1100 | 1101 | 1110 | 1111 |
| Output: 输出 | 1111 | 0111 | 0010 | 1100 | 1001 | 0011 | 1110 | 1010 |

**The mixing permutation, showing where each of the 16 bits in a block is moved, is:**

**混合置换（展示一个块中的 16 个比特各自被移到了哪里）如下：**

| In: 入 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Out: 出 | 7 | 2 | 3 | 8 | 12 | 5 | 11 | 9 | 10 | 1 | 14 | 13 | 4 | 6 | 16 | 15 |

We first find a differential in the S-box. Let $S(x)$ denote the output of the S-box on input x. Consider the differential $\Delta_x = 1111$. Then, for example, we have $S(0000) \oplus S(1111) = 0000 \oplus 1010 = 1010$ and so in this case a difference of 1111 in the inputs leads to a difference of 1010 in the outputs. Let us see if this relation holds frequently. We have $S(0001) = 1011$ and $S(0001 \oplus 1111) = S(1110) = 1110$, and so here a difference of 1111 in the inputs does not lead to a difference of 1010 in the outputs. However, $S(0100) = 0110$ and $S(0100 \oplus 1111) = S(1011) = 1100$ and so in this case, a difference of 1111 in the inputs yields a difference of 1010 in the outputs. In Figure 7.8 we tabulate results for all possible inputs. We see that half the time a difference of 1111 in the inputs yields a difference of 1010 in the outputs. Thus, (1111, 1010) is a differential in S that occurs with probability ${1}/{2}$.

我们首先在 S 盒中找一个差分。令 $S(x)$ 表示 S 盒在输入 $x$ 上的输出。考虑差分 $\Delta_x = 1111$。那么，例如我们有 $S(0000) \oplus S(1111) = 0000 \oplus 1010 = 1010$，因此在这种情况下输入差异 1111 导致输出差异 1010。让我们看看这个关系是否经常成立。我们有 $S(0001) = 1011$ 且 $S(0001 \oplus 1111) = S(1110) = 1110$，因此这里输入差异 1111 并未导致输出差异 1010。然而，$S(0100) = 0110$ 且 $S(0100 \oplus 1111) = S(1011) = 1100$，因此在这种情况下，输入差异 1111 产生输出差异 1010。在图 7.8 中我们列出了所有可能输入的结果。我们看到，输入差异 1111 在半数情况下产生输出差异 1010。因此，(1111, 1010) 是 S 中以概率 ${1}/{2}$ 出现的一个差分。

| x | S(x) | x ⊕ 1111 | S(x ⊕ 1111) | S(x) ⊕ S(x ⊕ 1111) |
| --- | --- | --- | --- | --- |
| 0000 | 0000 | 1111 | 1010 | 1010 |
| 0001 | 1011 | 1110 | 1110 | 0101 |
| 0010 | 0101 | 1101 | 0011 | 0110 |
| 0011 | 0001 | 1100 | 1001 | 1000 |
| 0100 | 0110 | 1011 | 1100 | 1010 |
| 0101 | 1000 | 1010 | 0010 | 1010 |
| 0110 | 1101 | 1001 | 0111 | 1010 |
| 0111 | 0100 | 1000 | 1111 | 1011 |
| 1000 | 1111 | 0111 | 0100 | 1011 |
| 1001 | 0111 | 0110 | 1101 | 1010 |
| 1010 | 0010 | 0101 | 1000 | 1010 |
| 1011 | 1100 | 0100 | 0110 | 1010 |
| 1100 | 1001 | 0011 | 0001 | 1000 |
| 1101 | 0011 | 0010 | 0101 | 0110 |
| 1110 | 1110 | 0001 | 1011 | 0101 |
| 1111 | 1010 | 0000 | 0000 | 1010 |

**FIGURE 7.8: The effect of the input difference $\Delta_x = 1111$ in our S-box.**

**图 7.8：输入差异 $\Delta_x = 1111$ 在我们的 S 盒中的效果。**

![Image](https://lsky.jerryxue.top/i/2026/08/19/6a85c5506bd3d.jpg)

**FIGURE 7.9: Differentials in our S-box.**

**图 7.9：我们的 S 盒中的差分。**

The same process can be carried out for all ${2}^4$ input differences $\Delta x$ to calculate the probability of every differential. Namely, for each pair $(\Delta_x, \Delta_y)$ we tabulate the number of inputs $x$ for which $S(x) \oplus S(x \oplus \Delta x) = \Delta_y$. We have done this for our example $S$-box in Figure 7.9. (For conciseness we use hexadecimal notation.) The table should be read as follows: entry $(i, j)$ counts how many inputs with difference $i$ map to outputs with difference $j$. Observe, for example, that there are 8 inputs with difference $\mathtt{0xF} = 1111$ that map to output $\mathtt{0xA} = 1010$, as we have shown above. This is the highest-probability differential (apart from the trivial differential $(\mathtt{0x0}, \mathtt{0x0})$). But there are also other differentials of interest: an input difference of $\Delta x = \mathtt{0x4} = 0100$ maps to an output difference of $\Delta_y = \mathtt{0x6} = 0110$ with probability ${6}/16 = 3/8$, and there are several differentials with probability ${4}/16 = 1/4$.

同样的过程可以对所有 ${2}^4$ 个输入差异 $\Delta x$ 进行，以计算每个差分的概率。即，对于每对 $(\Delta_x, \Delta_y)$，我们列出满足 $S(x) \oplus S(x \oplus \Delta x) = \Delta_y$ 的输入 $x$ 的个数。我们在图 7.9 中对我们的示例 $S$ 盒做了这件事。（为简洁起见，我们使用十六进制记号。）该表应按如下方式读取：条目 $(i, j)$ 计数有多少个差异为 $i$ 的输入映射到差异为 $j$ 的输出。例如，观察到有 8 个差异为 $\mathtt{0xF} = 1111$ 的输入映射到输出 $\mathtt{0xA} = 1010$，正如我们上面所示。这是最高概率的差分（除了平凡差分 $(\mathtt{0x0}, \mathtt{0x0})$ 之外）。但还有其他令人感兴趣的差分：输入差异 $\Delta x = \mathtt{0x4} = 0100$ 以概率 ${6}/16 = 3/8$ 映射到输出差异 $\Delta_y = \mathtt{0x6} = 0110$，还有若干概率为 ${4}/16 = 1/4$ 的差分。

We now extend this to find a good differential for the first three rounds of the SPN. Consider evaluating the SPN on two inputs that have a differential of 0000 1100 0000 0000, and tracing the differential between the intermediate values at each step of this evaluation. (Refer to Figure 7.10, which shows the first three rounds of the SPN.) The key-mixing step in the first round does not affect the differential, and so the inputs to the second S-box in the first round have differential 1100. We see from Figure 7.9 that a difference of 0xC = 1100 in the inputs to the S-box yields a difference of 0x8 = 1000 in the outputs of the S-box with probability 1/4. So with probability 1/4 the differential in the output of the 2nd S-box after round 1 is a single bit which is moved by the mixing permutation from the 5th position to the 12th position. (The inputs to the other S-boxes are equal, so their outputs are equal and the differential of the outputs is 0000.) Assuming this to be the case, the input difference to the third S-box in the second round is $\mathtt{0x1} = 0001$ (once again, the key-mixing step in the second round does not affect the differential); using Figure 7.9 we have that with probability ${1}/{4}$ the output difference from that S-box is $\mathtt{0x4} = 0100$. Thus, once again there is just a single output bit that is different, and it is moved from the 10th position to the first position by the mixing permutation. Finally, consulting Figure 7.9 yet again, we see that an input difference of $\mathtt{0x8} = 1000$ to the S-box results in an output difference of $\mathtt{0xF} = 1111$ with probability ${1}/{4}$. The bits in positions 1, 2, 3, and 4 are then moved by the mixing permutation to positions 7, 2, 3, and 8. Note that the key-mixing step in the fourth round does not affect the output differential.

我们现在将此扩展，为 SPN 的前三轮找到一个好的差分。考虑在两个具有差异 0000 1100 0000 0000 的输入上求值该 SPN，并追踪该求值每一步中中间值之间的差分。（参见图 7.10，它展示了该 SPN 的前三轮。）第一轮的密钥混合步骤不影响差分，因此第一轮中第二个 S 盒的输入具有差异 1100。我们从图 7.9 看到，S 盒输入的差异 0xC = 1100 以概率 1/4 产生 S 盒输出的差异 0x8 = 1000。因此以概率 1/4，第 1 轮后第 2 个 S 盒输出中的差分是单个比特，它被混合置换从第 5 个位置移到了第 12 个位置。（其他 S 盒的输入相等，因此它们的输出相等，输出的差分为 0000。）假设情况如此，第二轮中第三个 S 盒的输入差异为 $\mathtt{0x1} = 0001$（同样，第二轮的密钥混合步骤不影响差分）；利用图 7.9，我们得到以概率 ${1}/{4}$ 该 S 盒的输出差异为 $\mathtt{0x4} = 0100$。因此，再次只有一个输出比特不同，它被混合置换从第 10 个位置移到了第一个位置。最后，再次查阅图 7.9，我们看到 S 盒的输入差异 $\mathtt{0x8} = 1000$ 以概率 ${1}/{4}$ 产生输出差异 $\mathtt{0xF} = 1111$。第 1、2、3、4 位置上的比特随后被混合置换分别移到第 7、2、3、8 位置。注意第四轮的密钥混合步骤不影响输出差分。

![Image](https://lsky.jerryxue.top/i/2026/08/19/6a85c55392196.jpg)

**FIGURE 7.10: Tracing differentials through the first three rounds of an SPN that uses the S-box and mixing permutation given in the text.**

**图 7.10：在使用文中给出的 S 盒和混合置换的 SPN 的前三轮中追踪差分。**

Overall, then, we see that an input difference of $\Delta_x = 0000\ 1100\ 0000\ 0000$ yields the output difference $\Delta_y = 0110\ 0011\ 0000\ 0000$ after three rounds with probability at least $\frac{1}{4} \cdot \frac{1}{4} \cdot \frac{1}{4} = \frac{1}{64}$. (This is a lower bound on the probability of the differential, since there may be other differences in the intermediate values that result in the same difference in the outputs. We multiply the probabilities since we assume independence of the sub-keys used in each round.) For a random function, the probability that any given differential occurs is just ${2}^{-16} = 1/65536$. Thus, the differential we have found occurs with probability significantly higher than what would be expected for a random function. Observe also that we have found a low-weight differential.

综上，我们看到输入差异 $\Delta_x = 0000\ 1100\ 0000\ 0000$ 在三轮后以至少 $\frac{1}{4} \cdot \frac{1}{4} \cdot \frac{1}{4} = \frac{1}{64}$ 的概率产生输出差异 $\Delta_y = 0110\ 0011\ 0000\ 0000$。（这是该差分概率的一个下界，因为中间值中可能存在其他差异也导致输出中的相同差异。我们相乘概率是因为假设每轮使用的子密钥是独立的。）对于一个随机函数，任何给定差分出现的概率仅为 ${2}^{-16} = 1/65536$。因此，我们找到的差分以显著高于随机函数所预期的概率出现。还注意到我们找到了一个低重量的差分。

We can use this differential to find 8 bits of the final sub-key $k_5$—namely, the bits at positions 2, 3, 5, 7, 8, 9, 11, and 12. (i.e., the positions that the outputs of the first two S-boxes from the 3rd round get mapped to by the mixing permutation.) As discussed earlier, we begin by letting $\{(x_1^i, x_2^i)\}_{i=1}^L$ be a set of $L$ pairs of random inputs with differential $\Delta_x$. Using a chosen-plaintext attack, we then obtain the values $y_1^i = F_k(x_1^i)$ and $y_2^i = F_k(x_2^i)$ for all $i$. Now, for all possible values of the specified 8 bits of $k_5$, we compute the initial 8 bits of $\tilde{y}_1^i$, $\tilde{y}_2^i$, the intermediate values after the key-mixing step of the 4th round. (We can do this because we only need to invert the two left-most S-boxes of the 4th round in order to derive those 8 bits.) When we guess the correct value for the specified 8 bits of $k_5$, we expect the 8-bit differential 0110 0011 to occur with probability at least 1/64. Heuristically, an incorrect guess yields the expected differential only with probability ${2}^{-8} = 1/256$. By setting $L$ large enough, we can (with high probability) identify the correct value.

我们可以用这个差分来找到最终子密钥 $k_5$ 的 8 个比特——即位置 2、3、5、7、8、9、11 和 12 上的比特。（即第 3 轮前两个 S 盒的输出被混合置换映射到的那些位置。）如前所述，我们首先令 $\{(x_1^i, x_2^i)\}_{i=1}^L$ 为一组 $L$ 对具有差分 $\Delta_x$ 的随机输入。使用选择明文攻击，我们随后对所有 $i$ 获得 $y_1^i = F_k(x_1^i)$ 和 $y_2^i = F_k(x_2^i)$ 的值。现在，对于 $k_5$ 的指定 8 个比特的所有可能值，我们计算 $\tilde{y}_1^i$、$\tilde{y}_2^i$（第 4 轮密钥混合步骤后的中间值）的初始 8 个比特。（我们可以做到这一点，因为只需对第 4 轮最左边的两个 S 盒求逆即可推导出这 8 个比特。）当我们猜对 $k_5$ 的指定 8 个比特的正确值时，我们预计 8 比特差分 0110 0011 以至少 1/64 的概率出现。启发式地，错误猜测仅以概率 ${2}^{-8} = 1/256$ 产生预期差分。通过将 $L$ 设得足够大，我们可以（以高概率）识别出正确的值。

Differential attacks in practice. Differential cryptanalysis is very powerful, and has been used to attack real ciphers. A prominent example is FEAL-8, which was proposed as an alternative to DES in 1987. A differential attack on FEAL-8 was found that requires just 1,000 chosen plaintexts. In 1991, it took less than 2 minutes using this attack to find the entire key. Today, any proposed cipher is tested for resistance to differential cryptanalysis.

实践中的差分攻击。差分密码分析非常强大，已被用于攻击真实的密码。一个突出的例子是 FEAL-8，它于 1987 年作为 DES 的替代方案被提出。人们发现了对 FEAL-8 的差分攻击，只需 1,000 个选择明文。1991 年，使用这种攻击只需不到 2 分钟就能找到整个密钥。如今，任何提出的密码都要经过抗差分密码分析能力的测试。

A differential attack was also the first attack on DES to require less time than a simple brute-force search. While an interesting theoretical result, the attack is not very effective in practice since it requires ${2}^{47}$ chosen plaintexts, and it would be difficult for an attacker to obtain this many chosen plaintext/ciphertext pairs in most real-world applications. Interestingly, small modifications to the S-boxes of DES make the cipher much more vulnerable to differential attacks. Personal testimony of the DES designers (after differential attacks were discovered in the outside world) confirmed that the S-boxes of DES were designed specifically to thwart differential attacks.

差分攻击也是第一个针对 DES 的、所需时间少于简单穷举搜索的攻击。虽然这是一个有趣的理论结果，但该攻击在实践中不是很有效，因为它需要 ${2}^{47}$ 个选择明文，而且在大多数现实应用中，攻击者很难获得如此多的选择明文/密文对。有趣的是，对 DES 的 S 盒做小的修改会使该密码更容易受到差分攻击。DES 设计者的个人证词（在差分攻击被外部世界发现之后）证实，DES 的 S 盒是专门为抵御差分攻击而设计的。

Linear cryptanalysis. Linear cryptanalysis was developed by Matsui in the early 1990s. We will only describe the idea underlying the technique. The basic idea is to consider linear relationships between the input, output, and key that hold with high probability. In more detail, assume an $n$-bit key length and $\ell$-bit block length, and let $I, O \subseteq \{1, \ldots, \ell\}$ and $K \subseteq \{1, \ldots, n\}$. For an $\ell$-bit $x$, let $x_I$ denote the XOR of the bits at the positions indicated by $I$; define $k_K$ similarly for $k \in \{0,1\}^n$. We say that $I, O, K$ have linear bias $\varepsilon$ if, for uniform $x$ and $k$, and $y \overset{\mathrm{def}}{=} F_k(x)$, it holds that

线性密码分析。线性密码分析由 Matsui 在 20 世纪 90 年代初开发。我们只描述该技术背后的思想。基本思想是考虑以高概率成立的输入、输出和密钥之间的线性关系。更详细地，假设 $n$ 比特密钥长度和 $\ell$ 比特分组长度，令 $I, O \subseteq \{1, \ldots, \ell\}$ 和 $K \subseteq \{1, \ldots, n\}$。对于 $\ell$ 比特的 $x$，令 $x_I$ 表示由 $I$ 所指示位置上的比特的异或；类似地对 $k \in \{0,1\}^n$ 定义 $k_K$。我们说 $I, O, K$ 具有线性偏差 $\varepsilon$，如果对于均匀的 $x$ 和 $k$，以及 $y \overset{\mathrm{def}}{=} F_k(x)$，成立

$$
\left|\Pr[x_{I}\oplus y_{O}\oplus k_{K}=0]-\frac{1}{2}\right|=\varepsilon.
$$

If such a bias can be identified, it will clearly be useful for determining bits of the key given a number of plaintext/ciphertext pairs. Besides giving another method for attacking ciphers, an important feature of this attack compared to differential cryptanalysis is that it uses known plaintexts rather than chosen plaintexts. This is very significant, since an encrypted file can provide a huge amount of known plaintext, whereas obtaining encryptions of chosen plaintexts is much more difficult. Matsui showed that DES can be broken using linear cryptanalysis with just ${2}^{43}$ plaintext/ciphertext pairs.

如果能够识别出这样的偏差，它显然将有助于在给定若干明文/密文对的情况下确定密钥的比特。除了提供另一种攻击密码的方法之外，与差分密码分析相比，这种攻击的一个重要特征是它使用已知明文而非选择明文。这非常关键，因为一个加密文件可以提供大量的已知明文，而获得选择明文的加密则困难得多。Matsui 证明 DES 可以使用线性密码分析仅用 ${2}^{43}$ 个明文/密文对来破解。

Impact on block-cipher design. Modern block ciphers are designed and evaluated based, in part, on their resistance to differential and linear cryptanalysis. When constructing a block cipher, designers choose S-boxes and other components so as to minimize differential probabilities and linear biases. It is not possible to eliminate all high-probability differentials in an S-box: any S-box will have some differential that occurs more frequently than others. Still, these deviations can be minimized. Moreover, increasing the number of rounds (and choosing the mixing permutation carefully) can both reduce the differential probabilities as well as make it more difficult for cryptanalysts to find any differentials to exploit.

对分组密码设计的影响。现代分组密码的设计和评估部分基于它们对差分和线性密码分析的抵抗力。在构造分组密码时，设计者选择 S 盒和其他组件以最小化差分概率和线性偏差。不可能消除 S 盒中所有的高概率差分：任何 S 盒都会有一些差分比其他差分出现得更频繁。尽管如此，这些偏差可以被最小化。此外，增加轮数（以及仔细选择混合置换）既可以降低差分概率，也可以使密码分析家更难找到任何可利用的差分。
