## Part II: Private-Key (Symmetric) Cryptography　第二部分：私钥（对称）密码学

# Chapter 2: Perfectly Secret Encryption　第二章　完美保密加密

In the previous chapter we presented some historical encryption schemes and showed that they can be broken easily. In this chapter, we look at the other extreme and study encryption schemes that are provably secure even against an adversary with unbounded computational power. Such schemes are called perfectly secret. We rigorously define this notion, and explore conditions under which perfect secrecy can be achieved.

在上一章中，我们介绍了一些历史上的加密方案，并展示了它们很容易被攻破。在本章中，我们将转向另一个极端，研究那些即使在面对拥有无界计算能力的敌手时也可证明安全的加密方案。这类方案被称为**完美保密**（perfectly secret）的方案。我们将严格定义这一概念，并探讨能够实现完美保密的条件。

The material in this chapter belongs, in some sense, more to the world of "classical" cryptography than to the world of "modern" cryptography. Besides the fact that all the material introduced here was developed before the revolution in cryptography that took place in the mid-1970s and 1980s, the constructions we study in this chapter rely only on the first and third principles outlined in Section 1.4. That is, precise mathematical definitions are used and rigorous proofs are given, but it will not be necessary to rely on any unproven computational assumptions. It is clearly advantageous to avoid such assumptions; we will see, however, that doing so has inherent limitations. Thus, in addition to serving as a good basis for understanding the principles underlying modern cryptography, the results of this chapter also justify our later adoption of all three of the aforementioned principles.

从某种意义上说，本章内容更属于“经典”密码学而非“现代”密码学的范畴。这不仅因为本章介绍的所有材料都是在 20 世纪 70 年代中期和 80 年代的密码学革命之前发展起来的，而且本章研究的构造也仅依赖于 1.4 节中概述的第一和第三项原则。也就是说，我们使用精确的数学定义并给出严格的证明，但不必依赖任何未经证明的计算假设。避免此类假设显然是有利的；然而，我们将看到这样做有其固有的局限性。因此，除了为理解现代密码学的基本原理提供良好基础之外，本章的结果也为我们之后采用上述全部三项原则提供了理由。

Beginning with this chapter, we will define security and analyze schemes using probabilistic experiments involving randomized algorithms. (We assume familiarity with basic probability theory. The relevant notions are reviewed in Appendix A.3.) A simple example is given by the "experiment" in which the parties who wish to communicate using a private-key encryption scheme generate a random key. Since randomness is so essential, we briefly discuss the issue of generating randomness suitable for cryptographic applications before returning to a discussion of cryptography per se.

从本章开始，我们将使用涉及随机化算法的概率实验来定义安全性并分析方案。（我们假定读者熟悉基本的概率论。相关概念在附录 A.3 中进行了回顾。）举个简单的例子：希望使用私钥加密方案通信的双方生成一个随机密钥，这一过程本身就是一个“实验”。由于随机性如此重要，我们在回到对密码学本身的讨论之前，先简要讨论一下生成适用于密码学应用的随机性的问题。

Generating randomness. Throughout the book, we will assume for simplicity that parties have access to an unlimited supply of independent, unbiased (i.e., uniform) bits. Where do these random bits come from? Since classical computation is deterministic, it is not at all clear how computers can be used to generate random bits. In principle, one could generate a small number of uniform bits by hand, e.g., by flipping a fair coin. But that approach is not very convenient, nor does it scale.

**生成随机性。**

为简单起见，本书假定各方可以无限制地获得独立、无偏（即均匀）的比特。这些随机比特从何而来？由于经典计算是确定性的，如何用计算机生成随机比特并不显而易见。原则上，人们可以手动生成少量均匀比特，例如通过抛掷一枚公平的硬币。但这种方法不太方便，也无法扩展。

Modern random-number generation proceeds in two steps. First, a "pool" of high-entropy data is collected. (For our purposes a formal definition of entropy is not needed, and it suffices to think of entropy as a measure of unpredictability.) Next, this high-entropy data is processed to yield a sequence of nearly independent and unbiased bits. This second step is necessary since high-entropy data is not necessarily uniform.

现代随机数生成分两步进行。首先，收集一个高熵数据的“池”。（就我们的目的而言，不需要熵的形式化定义，把熵视为不可预测性的一种度量即可。）接下来，对这些高熵数据进行处理，以产生一系列近乎独立且无偏的比特。这第二步是必要的，因为高熵数据不一定是均匀的。

For the first step, some source of unpredictable data is needed. This can come from external inputs, for example, delays between network events, hard-disk access times, keystrokes or mouse movements made by the user, and so on. More sophisticated approaches—which, by design, incorporate random-number generation more tightly into the system at the hardware level—can also be used. These rely on physical phenomena such as thermal/shot noise or radioactive decay; for example, certain Intel processors use thermal noise to generate high-entropy data on-chip. Hardware random-number generators of this sort generally produce high-entropy data at a faster rate than techniques relying on external sources.

第一步需要某种不可预测数据的来源。这可以来自外部输入，例如网络事件之间的延迟、硬盘访问时间、用户的击键或鼠标移动等。也可以使用更复杂的方法——这些方法在设计上就将随机数生成更紧密地集成到了系统的硬件层面。这些方法依赖于物理现象，如热噪声/散粒噪声或放射性衰变；例如，某些 Intel 处理器使用热噪声在芯片上生成高熵数据。这类硬件随机数生成器通常比依赖外部来源的技术以更快的速度产生高熵数据。

The processing needed to "smooth" the high-entropy data to obtain (nearly) independent and uniform bits is non-trivial, and is discussed briefly in Section 6.6.4. Here, we consider a simple example to give an idea of what can be done. Imagine that our high-entropy pool contains a sequence of biased bits, where 1 occurs with probability p and 0 occurs with probability 1 - p. (We do assume, however, that the bits are all independent. In practice this assumption is typically not valid and so more-complex processing must be done.) Thousands of such bits have lots of entropy, but are not close to uniform. We can obtain a uniform sequence of bits by taking the original bits in pairs: if we see a 1 followed by a 0 then we output 0, and if we see a 0 followed by a 1 then we output 1. (If we see two 0s or two 1s in a row we output nothing, and simply move on to the next pair.) The probability that any pair results in a 0 is $p \cdot (1 - p)$, which is exactly equal to the probability that any pair results in a 1. (Note that we do not even need to know the value of $p$!) We thus obtain a uniformly distributed output from our initial high-entropy pool.

将高熵数据“平滑”以获得（近乎）独立且均匀的比特并非易事，我们将在 6.6.4 节简要讨论。在此，我们考虑一个简单例子来了解可行的做法。假设我们的高熵池包含一个有偏的比特序列，其中 1 出现的概率为 $p$，0 出现的概率为 $1 - p$。（但我们确实假定了这些比特是独立的。在实践中，这一假设通常不成立，因此必须进行更复杂的处理。）成千上万个这样的比特具有大量的熵，但并不接近均匀。我们可以通过将原始比特成对处理来获得均匀的比特序列：如果看到 1 后面跟着 0，则输出 0；如果看到 0 后面跟着 1，则输出 1。（如果连续看到两个 0 或两个 1，则不输出任何内容，直接处理下一对。）任何一对产生 0 的概率是 $p \cdot (1 - p)$，这恰好等于任何一对产生 1 的概率。（注意，我们甚至不需要知道 $p$ 的值！）于是，我们从初始的高熵池中获得了均匀分布的输出。

Care must be taken in how random bits are produced, and using poor random-number generators can often leave a good cryptosystem vulnerable to attack. One should use a random-number generator that is designed for cryptographic use, rather than a "general-purpose" random-number generator that is generally not suitable for cryptographic applications. In particular, the rand() function in the C stdlib.h library is not cryptographically secure, and using it in cryptographic settings can have disastrous consequences.

产生随机比特时必须格外谨慎，使用差的随机数生成器常常会使一个好的密码系统易于受到攻击。应该使用为密码学用途设计的随机数生成器，而不是那些通常不适合密码学应用的“通用”随机数生成器。特别地，C 语言 stdlib.h 库中的 rand() 函数在密码学上是不安全的，在密码学场景中使用它可能会带来灾难性后果。

## 2.1 Definitions　定义

We begin by recalling and expanding upon the syntax of encryption, as introduced in the previous chapter. An encryption scheme is defined by three algorithms Gen, Enc, and Dec, as well as a specification of a message space $\mathcal{M}$ with $|\mathcal{M}| > 1$.$^1$ The key-generation algorithm Gen is a probabilistic algorithm that outputs a key $k$ chosen according to some distribution. We denote by $\mathcal{K}$ the (finite) key space, i.e., the set of all possible keys that can be output by Gen. The encryption algorithm Enc takes as input a key $k \in \mathcal{K}$ and a message $m \in \mathcal{M}$, and outputs a ciphertext $c$. We now explicitly allow the encryption algorithm to be probabilistic (so $\mathsf{Enc}_k(m)$ might output a different ciphertext when run multiple times), and we write $c \leftarrow \mathsf{Enc}_k(m)$ to denote the possibly probabilistic process by which message $m$ is encrypted using key $k$ to give ciphertext $c$. (Looking ahead, we also sometimes use the notation $x \leftarrow S$ to denote uniform selection of $x$ from a set $S$. In case Enc is deterministic, we may emphasize this by writing $c := \mathsf{Enc}_k(m)$.) We let $\mathcal{C}$ denote the set of all possible ciphertexts that can be output by $\mathsf{Enc}_k(m)$, for all possible choices of $k \in \mathcal{K}$ and $m \in \mathcal{M}$ (and for all random choices of Enc in case it is randomized). The decryption algorithm Dec takes as input a key $k \in \mathcal{K}$ and a ciphertext $c \in \mathcal{C}$ and outputs a message $m \in \mathcal{M}$. We assume perfect correctness, meaning that for all $k \in \mathcal{K}$, $m \in \mathcal{M}$, and any ciphertext $c$ output by $\mathsf{Enc}_k(m)$, it holds that $\mathsf{Dec}_k(c) = m$ with probability 1. Perfect correctness implies that we may assume Dec is deterministic without loss of generality, since $\mathsf{Dec}_k(c)$ must give the same output every time it is run. We will thus write $m := \mathsf{Dec}_k(c)$ to denote the (deterministic) decryption process.

我们首先回顾上一章介绍的加密语法，并在此基础上加以扩展。一个加密方案由三个算法 Gen、Enc 和 Dec 以及一个消息空间 $\mathcal{M}$（$|\mathcal{M}| > 1$）的规范来定义。$^1$ 密钥生成算法 Gen 是一个概率算法，它输出一个按某种分布选取的密钥 $k$。我们用 $\mathcal{K}$ 表示（有限的）密钥空间，即 Gen 可能输出的所有密钥的集合。加密算法 Enc 以密钥 $k \in \mathcal{K}$ 和消息 $m \in \mathcal{M}$ 为输入，输出一个密文 $c$。现在我们明确允许加密算法可以是概率性的（因此 $\mathsf{Enc}_k(m)$ 在多次运行时可能输出不同的密文），并用 $c \leftarrow \mathsf{Enc}_k(m)$ 表示使用密钥 $k$ 对消息 $m$ 进行加密以得到密文 $c$ 这一可能带有随机性的过程。（展望后续，我们有时也使用记号 $x \leftarrow S$ 表示从集合 $S$ 中均匀选取 $x$。如果 Enc 是确定性的，我们会写 $c := \mathsf{Enc}_k(m)$ 来强调这一点。）我们用 $\mathcal{C}$ 表示所有可能密文的集合，即对所有 $k \in \mathcal{K}$、$m \in \mathcal{M}$（以及 Enc 随机化时的全部随机选择），$\mathsf{Enc}_k(m)$ 可能输出的密文全体。解密算法 Dec 以密钥 $k \in \mathcal{K}$ 和密文 $c \in \mathcal{C}$ 为输入，输出一个消息 $m \in \mathcal{M}$。我们假定方案满足完全正确性（perfect correctness），即对于所有 $k \in \mathcal{K}$、$m \in \mathcal{M}$ 以及 $\mathsf{Enc}_k(m)$ 输出的任何密文 $c$，$\mathsf{Dec}_k(c) = m$ 以概率 1 成立。完全正确性意味着我们可以不失一般性地假定 Dec 是确定性的，因为 $\mathsf{Dec}_k(c)$ 每次运行必须给出相同输出。因此我们用 $m := \mathsf{Dec}_k(c)$ 来表示（确定性的）解密过程。

$^1$ If $|\mathcal{M}| = 1$ there is only one message and no point in communicating, let alone encrypting. / 如果 $|\mathcal{M}| = 1$，就只有一条消息，连通信都没有意义了，更谈不上加密。

In the definitions and theorems below, we refer to probability distributions over $\mathcal{K}$, $\mathcal{M}$, and $\mathcal{C}$. The distribution over $\mathcal{K}$ is the one defined by running Gen and taking the output. (It is almost always the case that Gen chooses a key uniformly from $\mathcal{K}$ and, in fact, we may assume this without loss of generality; see Exercise 2.1.) We let $K$ be the random variable denoting the value of the key output by Gen; thus, for any $k \in \mathcal{K}$, $\Pr[K = k]$ denotes the probability that the key output by Gen is equal to $k$. Similarly, we let $M$ be the random variable denoting the message being encrypted, so $\Pr[M = m]$ denotes the probability that the message takes on the value $m \in \mathcal{M}$. The probability distribution of the message is not determined by the encryption scheme itself, but instead reflects the likelihood of different messages being sent by the parties using the scheme, as well as an adversary's uncertainty about what will be sent. As an example, an adversary may know that the message will either be attack today or don't attack. The adversary may even know (by other means) that with probability 0.7 the message will be a command to attack and with probability 0.3 the message will be a command not to attack. In this case, we have $\Pr[M = \text{attack today}] = 0.7$ and $\Pr[M = \text{don't attack}] = 0.3$.

下面定义和定理中涉及 $\mathcal{K}$、$\mathcal{M}$ 和 $\mathcal{C}$ 上的概率分布。$\mathcal{K}$ 上的分布是由运行 Gen 并取其输出定义的。（几乎总是如此：Gen 从 $\mathcal{K}$ 中均匀地选择密钥，事实上我们可以不失一般性地假定如此；见习题 2.1。）令 $K$ 为表示 Gen 输出密钥值的随机变量；因此，对于任意 $k \in \mathcal{K}$，$\Pr[K = k]$ 表示 Gen 输出的密钥等于 $k$ 的概率。类似地，令 $M$ 为表示被加密消息的随机变量，因此 $\Pr[M = m]$ 表示消息取值为 $m \in \mathcal{M}$ 的概率。消息的概率分布并非由加密方案本身决定，而是反映了使用该方案的各方发送不同消息的可能性，以及敌手对于将要发送内容的不确定性。例如，敌手可能知道消息要么是 attack today，要么是 don't attack。敌手甚至可能（通过其他途径）知道消息有 0.7 的概率是攻击命令，0.3 的概率是不攻击的命令。在这种情况下，我们有 $\Pr[M = \text{attack today}] = 0.7$ 和 $\Pr[M = \text{don't attack}] = 0.3$。

K and M are required to be independent, i.e., what is being communicated by the parties must be independent of the key they share. This makes sense, among other reasons, because the distribution over $\mathcal{K}$ is determined by the encryption scheme itself (since it is defined by $\mathsf{Gen}$), while the distribution over $\mathcal{M}$ depends on the context in which the encryption scheme is being used.

要求 $K$ 与 $M$ 相互独立，即各方通信的内容必须独立于他们共享的密钥。这之所以合理，原因之一是 $\mathcal{K}$ 上的分布由加密方案本身决定（由 $\mathsf{Gen}$ 定义），而 $\mathcal{M}$ 上的分布则取决于使用该加密方案的上下文。

Fixing an encryption scheme and a distribution over $\mathcal{M}$ determines a distribution over the space of ciphertexts $\mathcal{C}$ given by choosing a key $k \in \mathcal{K}$ (according to $\mathsf{Gen}$) and a message $m \in \mathcal{M}$ (according to the given distribution), and then computing the ciphertext $c \leftarrow \mathsf{Enc}_k(m)$. We let $C$ be the random variable denoting the resulting ciphertext and so, for $c \in \mathcal{C}$, write $\Pr[C = c]$ to denote the probability that the ciphertext is equal to the fixed value $c$.

固定一个加密方案以及 $\mathcal{M}$ 上的一个分布，就确定了密文空间 $\mathcal{C}$ 上的一个分布：选取一个密钥 $k \in \mathcal{K}$（根据 $\mathsf{Gen}$）和一条消息 $m \in \mathcal{M}$（根据给定分布），然后计算密文 $c \leftarrow \mathsf{Enc}_k(m)$。令 $C$ 为表示所得密文的随机变量，因此对任意 $c \in \mathcal{C}$，用 $\Pr[C = c]$ 表示密文等于该固定值 $c$ 的概率。

**Example 2.1**　**示例 2.1**

We work through a simple example for the shift cipher (cf. Section 1.3). Here, by definition, we have $\mathcal{K} = \{0, \ldots, 25\}$ with $\Pr[K = k] = 1/26$ for each $k \in \mathcal{K}$.

我们以移位密码（参见 1.3 节）为例进行简单计算。根据定义，此处 $\mathcal{K} = \{0, \ldots, 25\}$，且对每个 $k \in \mathcal{K}$，$\Pr[K = k] = 1/26$。

Say we are given the following distribution over $\mathcal{M}$:

假设给定如下的 $\mathcal{M}$ 分布：

$$\Pr[M=\mathtt{a}]=0.7 \quad \text{and} \quad \Pr[M=\mathtt{z}]=0.3.$$

What is the probability that the ciphertext is $\mathtt{B}$? There are only two ways this can occur: either $M = \mathtt{a}$ and $K = 1$, or $M = \mathtt{z}$ and $K = 2$. By independence of $M$ and $K$, we have

密文为 $\mathtt{B}$ 的概率是多少？这只能以两种方式发生：要么 $M = \mathtt{a}$ 且 $K = 1$，要么 $M = \mathtt{z}$ 且 $K = 2$。由 $M$ 和 $K$ 的独立性，我们有

$$\begin{aligned}\Pr[M=\mathtt{a}\land K=1]&=\Pr[M=\mathtt{a}]\cdot\Pr[K=1]\\&=0.7\cdot\left(\frac{1}{26}\right).\end{aligned}$$

Similarly, $\Pr[M = \mathtt{z} \land K = 2] = 0.3 \cdot \left( \frac{1}{26} \right)$. Therefore,

类似地，$\Pr[M = \mathtt{z} \land K = 2] = 0.3 \cdot \left( \frac{1}{26} \right)$。因此，

$$\begin{aligned}\Pr[C=\mathtt{B}]&=\Pr[M=\mathtt{a}\land K=1]+\Pr[M=\mathtt{z}\land K=2]\\&=0.7\cdot\left(\frac{1}{26}\right)+0.3\cdot\left(\frac{1}{26}\right)=1/26.\end{aligned}$$

We can calculate conditional probabilities as well. For example, what is the probability that the message a was encrypted, given that we observe ciphertext B? Using Bayes' Theorem (Theorem A.8) we have

我们也可以计算条件概率。例如，在观察到密文 B 的条件下，消息 a 被加密的概率是多少？利用贝叶斯定理（定理 A.8），我们有

$$\begin{aligned}\Pr[M=\mathtt{a}\mid C=\mathtt{B}]&=\frac{\Pr[C=\mathtt{B}\mid M=\mathtt{a}]\cdot\Pr[M=\mathtt{a}]}{\Pr[C=\mathtt{B}]}\\&=\frac{\Pr[C=\mathtt{B}\mid M=\mathtt{a}]\cdot0.7}{1/26}.\end{aligned}$$

Note that $\Pr[C = \mathtt{B} \mid M = \mathtt{a}] = 1/26$, since if $M = \mathtt{a}$ then the only way $C = \mathtt{B}$ can occur is if $K = 1$ (which occurs with probability ${1}/26$). We conclude that $\Pr[M = \mathtt{a} \mid C = \mathtt{B}] = 0.7$.

注意 $\Pr[C = \mathtt{B} \mid M = \mathtt{a}] = 1/26$，因为如果 $M = \mathtt{a}$，那么 $C = \mathtt{B}$ 发生的唯一方式是 $K = 1$（其发生概率为 ${1}/26$）。我们得出结论：$\Pr[M = \mathtt{a} \mid C = \mathtt{B}] = 0.7$。

**Example 2.2**　**示例 2.2**

Consider the shift cipher again, but with the following distribution over $\mathcal{M}$:

再次考虑移位密码，但使用如下的 $\mathcal{M}$ 分布：

$$\Pr[M=\mathtt{kim}]=0.5,\Pr[M=\mathtt{ann}]=0.2,\Pr[M=\mathtt{boo}]=0.3.$$

What is the probability that $C = \mathtt{DQQ}$? The only way this ciphertext can occur is if $M = \mathtt{ann}$ and $K = 3$, or $M = \mathtt{boo}$ and $K = 2$, which happens with probability $0.2 \cdot 1/26 + 0.3 \cdot 1/26 = 1/52$.

$C = \mathtt{DQQ}$ 的概率是多少？该密文发生的唯一方式是 $M = \mathtt{ann}$ 且 $K = 3$，或 $M = \mathtt{boo}$ 且 $K = 2$，其概率为 $0.2 \cdot 1/26 + 0.3 \cdot 1/26 = 1/52$。

We can also compute the probability that $\mathtt{ann}$ was encrypted, conditioned on observing the ciphertext $\mathtt{DQQ}$? A calculation as above using Bayes' Theorem gives $\Pr[M = \mathtt{ann} \mid C = \mathtt{DQQ}] = 0.4$.

我们也可以计算在观察到密文 $\mathtt{DQQ}$ 的条件下，$\mathtt{ann}$ 被加密的概率。利用贝叶斯定理进行与上面类似的计算，可得 $\Pr[M = \mathtt{ann} \mid C = \mathtt{DQQ}] = 0.4$。

Perfect secrecy. We are now ready to define the notion of perfect secrecy. We imagine an adversary who knows the probability distribution of $M$; that is, the adversary knows the likelihood that different messages will be sent. The adversary also knows the encryption scheme being used. The only thing unknown to the adversary is the key shared by the parties. A message is chosen by one of the honest parties and encrypted, and the resulting ciphertext is transmitted to the other party. The adversary can eavesdrop on the parties' communication, and thus observe this ciphertext. (That is, this is a ciphertext-only attack, where the attacker sees only a single ciphertext.) For a scheme to be perfectly secret, observing this ciphertext should have no effect on the adversary's knowledge regarding the actual message that was sent; in other words, the a posteriori probability that some message $m \in \mathcal{M}$ was sent, conditioned on the ciphertext that was observed, should be no different from the a priori probability that m would be sent. This means that the ciphertext reveals nothing about the underlying plaintext, and the adversary learns absolutely nothing about the plaintext that was encrypted. Formally:

**完美保密。**

我们现在准备定义完美保密的概念。设想一个敌手，他知道 $M$ 的概率分布；也就是说，敌手知道不同消息被发送的可能性。敌手也知道所使用的加密方案。敌手唯一不知道的是通信双方共享的密钥。一条消息由诚实的一方选择并加密，所得密文被传送给另一方。敌手可以窃听双方的通信，从而观察到该密文。（也就是说，这是一种唯密文攻击，攻击者只看到单个密文。）一个方案要称得上完美保密，观察到该密文就不应改变敌手对实际所发消息的认识；换句话说，在观察到密文的条件下，某条消息 $m \in \mathcal{M}$ 被发送的后验概率，应与 $m$ 被发送的先验概率完全相同。这意味着密文不泄露关于底层明文的任何信息，敌手对被加密的明文一无所知。形式化地：

DEFINITION 2.3 An encryption scheme (Gen, Enc, Dec) with message space $\mathcal{M}$ is perfectly secret if for every probability distribution for $M$, every message $m \in \mathcal{M}$, and every ciphertext $c \in \mathcal{C}$ for which $\Pr[C = c] > 0$:

定义 2.3 一个具有消息空间 $\mathcal{M}$ 的加密方案 (Gen, Enc, Dec) 是**完美保密**的，如果对于 $M$ 的每一个概率分布、每一条消息 $m \in \mathcal{M}$ 以及每一个满足 $\Pr[C = c] > 0$ 的密文 $c \in \mathcal{C}$，都有

$$\Pr[M=m\mid C=c]=\Pr[M=m].$$

(The requirement that $\Pr[C = c] > 0$ is a technical one needed to prevent conditioning on a zero-probability event.)

（要求 $\Pr[C = c] > 0$ 是一个技术性条件，用于防止对零概率事件进行条件化。）

**Example 2.4**　**示例 2.4**

We show that the shift cipher is not perfectly secret when used with the message space $\mathcal{M}$ consisting of all two-character plaintexts. To do so, we work with Definition 2.3, and show a probability distribution over $\mathcal{M}$ for which, for some message m and ciphertext c,

我们证明当消息空间 $\mathcal{M}$ 由所有双字符明文组成时，移位密码不是完美保密的。为此，我们使用定义 2.3，并展示一个 $\mathcal{M}$ 上的概率分布，使得对于某消息 $m$ 和密文 $c$，有

$$\Pr[M=m\mid C=c]\neq\Pr[M=m].$$

Many such distributions are possible, but we pick a simple one: say the message is either aa or ab, each with half probability. Set $m = ab$ and $c = XX$. Then clearly $\Pr[M = ab \mid C = XX] = 0$, as there is no way that XX can ever result from the encryption of ab. But $\Pr[M = ab] = 1/2$.

很多这样的分布都是可能的，但我们选一个简单的：假设消息要么是 aa 要么是 ab，各以一半概率。设 $m = ab$ 且 $c = XX$。那么显然 $\Pr[M = ab \mid C = XX] = 0$，因为 XX 不可能由 ab 加密得到。但 $\Pr[M = ab] = 1/2$。

We now give an equivalent formulation of perfect secrecy. This formulation defines perfect secrecy by requiring that the distribution of the ciphertext does not depend on the plaintext, i.e., for any two messages $m, m^{\prime} \in \mathcal{M}$ the distribution of the ciphertext when $m$ is encrypted should be identical to the distribution of the ciphertext when $m^{\prime}$ is encrypted. That is, for every $m, m^{\prime} \in \mathcal{M}$, and every $c \in \mathcal{C}$, we have

我们现在给出完美保密的一个等价表述。该表述要求密文的分布不依赖于明文，即对于任意两条消息 $m, m^{\prime} \in \mathcal{M}$，加密 $m$ 时密文的分布应与加密 $m^{\prime}$ 时密文的分布完全相同。也就是说，对于每一个 $m, m^{\prime} \in \mathcal{M}$ 和每一个 $c \in \mathcal{C}$，有

$$
\Pr[\mathsf{Enc}_{K}(m)=c]=\Pr[\mathsf{Enc}_{K}(m^{\prime})=c]\tag{2.1}
$$

(where the probabilities are over choice of K and any randomness of $\mathsf{Enc}$). Note that the above probabilities depend only on the encryption scheme, and make no reference to any underlying distribution on $\mathcal{M}$. The above condition implies that a ciphertext contains no information about the plaintext, and that it is impossible to distinguish an encryption of m from an encryption of $m^{\prime}$, since the distributions of the ciphertext are the same in each case.

（其中概率是相对于 $K$ 的选择以及 $\mathsf{Enc}$ 的任何随机性而言的）。注意上述概率仅依赖于加密方案本身，与 $\mathcal{M}$ 上的分布无关。上述条件意味着密文不包含关于明文的任何信息，并且由于两种情况下密文的分布相同，因此无法区分对 $m$ 的加密和对 $m^{\prime}$ 的加密。

LEMMA 2.5 An encryption scheme (Gen, Enc, Dec) with message space $\mathcal{M}$ is perfectly secret if and only if Equation (2.1) holds for every $m, m^{\prime} \in \mathcal{M}$ and every $c \in \mathcal{C}$.

引理 2.5 一个具有消息空间 $\mathcal{M}$ 的加密方案 (Gen, Enc, Dec) 是完美保密的，当且仅当对于每一个 $m, m^{\prime} \in \mathcal{M}$ 和每一个 $c \in \mathcal{C}$，式 (2.1) 成立。

PROOF The proof is straightforward, but we go through it in detail. The key observation is that for any scheme, any distribution on $\mathcal{M}$, any $m \in \mathcal{M}$ for which $\Pr[M = m] > 0$, and any $c \in \mathcal{C}$, we have

证明 证明十分直接，但我们还是详细展开。关键的观察是，对于任何方案、$\mathcal{M}$ 上的任何分布、任何满足 $\Pr[M = m] > 0$ 的 $m \in \mathcal{M}$ 以及任何 $c \in \mathcal{C}$，我们有

$$\begin{align*}\Pr[C=c\mid M=m]&=\Pr[\mathsf{Enc}_{K}(M)=c\mid M=m]\\&=\Pr[\mathsf{Enc}_{K}(m)=c\mid M=m]\\&=\Pr[\mathsf{Enc}_{K}(m)=c], \tag{2.2}\end{align*}$$

where the first equality is by definition of the random variable $C$, the second is because we are conditioning on the event that $M = m$, and the third is because $K$ is independent of $M$. We also use the fact that for any $c \in \mathcal{C}$ with $\Pr[C = c] > 0$, we have

其中第一个等式来自随机变量 $C$ 的定义，第二个是因为我们以 $M = m$ 为条件，第三个是因为 $K$ 独立于 $M$。我们还用到如下事实：对于任何 $\Pr[C = c] > 0$ 的 $c \in \mathcal{C}$，有

$$
\Pr[M=m\mid C=c]\cdot\Pr[C=c]=\Pr[C=c\mid M=m]\cdot\Pr[M=m].\tag{2.3}
$$

Take the uniform distribution over $\mathcal{M}$. If the scheme is perfectly secret then $\Pr[M = m \mid C = c] = \Pr[M = m]$, and so Equation (2.3) implies that $\Pr[C = c \mid M = m] = \Pr[C = c]$. Since $m$ and $c$ were arbitrary, this shows that for every $m, m^{\prime} \in \mathcal{M}$ and every $c \in \mathcal{C}$,

取 $\mathcal{M}$ 上的均匀分布。如果方案是完美保密的，那么 $\Pr[M = m \mid C = c] = \Pr[M = m]$，因此式 (2.3) 蕴含着 $\Pr[C = c \mid M = m] = \Pr[C = c]$。由于 $m$ 和 $c$ 是任意的，这表明对于每一个 $m, m^{\prime} \in \mathcal{M}$ 和每一个 $c \in \mathcal{C}$，

$$\begin{aligned}\Pr[\mathsf{Enc}_{K}(m)=c]&=\Pr[C=c\mid M=m]\\&=\Pr[C=c]\\&=\Pr[C=c\mid M=m^{\prime}]=\Pr[\mathsf{Enc}_{K}(m^{\prime})=c]\end{aligned}$$

(using Equation (2.2)), proving one direction of the lemma.

（利用式 (2.2)），证明了引理的一个方向。

Conversely, say Equation (2.1) holds for every $m, m^{\prime} \in \mathcal{M}$ and every $c \in \mathcal{C}$. Fix some distribution over $\mathcal{M}$, a message $m \in \mathcal{M}$, and a ciphertext $c \in \mathcal{C}$ with $\Pr[C = c] > 0$. If $\Pr[M = m] = 0$ then we trivially have

反之，假设式 (2.1) 对每一个 $m, m^{\prime} \in \mathcal{M}$ 和每一个 $c \in \mathcal{C}$ 成立。固定 $\mathcal{M}$ 上的某个分布、一条消息 $m \in \mathcal{M}$ 以及一个满足 $\Pr[C = c] > 0$ 的密文 $c \in \mathcal{C}$。如果 $\Pr[M = m] = 0$，那么显然有

$$\Pr[M=m\mid C=c]=\Pr[M=m]=0.$$

So, assume $\Pr[M = m] > 0$. For $c \in \mathcal{C}$, define $p_c \stackrel{\mathrm{def}}{=} \Pr[\mathsf{Enc}_K(m) = c]$. Equations (2.1) and (2.2) imply that $\Pr[C = c \mid M = m^{\prime}] = p_c$ for every $m^{\prime} \in \mathcal{M}$. So,

那么，假定 $\Pr[M = m] > 0$。对于 $c \in \mathcal{C}$，定义 $p_c \stackrel{\mathrm{def}}{=} \Pr[\mathsf{Enc}_K(m) = c]$。式 (2.1) 和 (2.2) 表明对每一个 $m^{\prime} \in \mathcal{M}$ 有 $\Pr[C = c \mid M = m^{\prime}] = p_c$。于是，

$$\begin{align*}\Pr[C=c]&=\sum_{m^{\prime}\in\mathcal{M}}\Pr[C=c\mid M=m^{\prime}]\cdot\Pr[M=m^{\prime}]\\&=\sum_{m^{\prime}\in\mathcal{M}}p_{c}\cdot\Pr[M=m^{\prime}]=p_{c}=\Pr[C=c\mid M=m],\end{align*}$$

where the sum is over $m^{\prime}$ with $\Pr[M = m^{\prime}] > 0$. Equation (2.3) implies that $\Pr[M = m \mid C = c] = \Pr[M = m]$, so the scheme is perfectly secret.

其中求和遍历所有满足 $\Pr[M = m^{\prime}] > 0$ 的 $m^{\prime}$。式 (2.3) 蕴含着 $\Pr[M = m \mid C = c] = \Pr[M = m]$，因此方案是完美保密的。

Perfect (adversarial) indistinguishability. We conclude this section by presenting another equivalent definition of perfect secrecy. This definition is based on an experiment involving an adversary passively observing a ciphertext and then trying to guess which of two possible messages was encrypted. We introduce this notion since it will serve as our starting point for defining computational security in the next chapter; throughout the rest of the book we will often use experiments like this one to define security.

**完美（敌手）不可区分性。**

我们在本节最后给出完美保密的另一个等价定义。该定义基于一个实验：敌手被动地观察一个密文，然后尝试猜测两个可能消息中哪一个被加密了。我们引入这个概念，是因为它将作为我们下一章定义计算安全性的起点；在本书余下部分，我们将经常使用此类实验来定义安全性。

In the present context, we consider the following experiment: An adversary $\mathcal{A}$ first specifies two arbitrary messages $m_0, m_1 \in \mathcal{M}$. Next, a key $k$ is generated using $\mathsf{Gen}$. Then, one of the two messages specified by $\mathcal{A}$ is chosen (each with probability ${1}/2$) and encrypted using $k$; the resulting ciphertext is given to $\mathcal{A}$. Finally, $\mathcal{A}$ outputs a "guess" as to which of the two messages was encrypted; $\mathcal{A}$ succeeds if it guesses correctly. An encryption scheme is perfectly indistinguishable if no adversary $\mathcal{A}$ can succeed with probability better than ${1}/2$. (Note that, for any encryption scheme, $\mathcal{A}$ can succeed with probability ${1}/2$ by outputting a uniform guess; the requirement is simply that no attacker can do any better than this.) We stress that no limitations are placed on the computational power of $\mathcal{A}$.

在当前语境下，我们考虑如下实验：敌手 $\mathcal{A}$ 首先指定两条任意消息 $m_0, m_1 \in \mathcal{M}$。接下来，使用 $\mathsf{Gen}$ 生成一个密钥 $k$。然后，$\mathcal{A}$ 指定的两条消息中被选中一条（各以概率 ${1}/2$），并使用 $k$ 进行加密；所得密文被交给 $\mathcal{A}$。最后，$\mathcal{A}$ 输出一个“猜测”，指明两条消息中哪一条被加密了；如果 $\mathcal{A}$ 猜对了，就认为它成功。一个加密方案称为**完美不可区分**的，如果没有敌手 $\mathcal{A}$ 能以优于 ${1}/2$ 的概率成功。（注意，对于任何加密方案，$\mathcal{A}$ 都可以通过输出均匀猜测以概率 ${1}/2$ 成功；要求只是没有攻击者能比这做得更好。）我们强调，对 $\mathcal{A}$ 的计算能力没有任何限制。

Formally, let $\Pi = (\mathrm{Gen}, \mathrm{Enc}, \mathrm{Dec})$ be an encryption scheme with message space $\mathcal{M}$. Let $\mathcal{A}$ be an adversary, which is formally just a (stateful) algorithm that we may assume is deterministic without loss of generality. We define an experiment $\mathrm{PrivK}_{\mathcal{A},\Pi}^{\mathrm{eav}}$, based on $\mathcal{A}$ and $\Pi$, as follows:

形式化地，设 $\Pi = (\mathrm{Gen}, \mathrm{Enc}, \mathrm{Dec})$ 是一个具有消息空间 $\mathcal{M}$ 的加密方案。设 $\mathcal{A}$ 是一个敌手，它本质上只是一个（有状态的）算法，我们可以不失一般性地假定它是确定性的。我们基于 $\mathcal{A}$ 和 $\Pi$ 定义一个实验 $\mathrm{PrivK}_{\mathcal{A},\Pi}^{\mathrm{eav}}$，如下所示：

The adversarial indistinguishability experiment $\mathsf{PrivK}_{\mathcal{A},\Pi}^{\mathsf{eav}}$:

敌手不可区分性实验 $\mathsf{PrivK}_{\mathcal{A},\Pi}^{\mathsf{eav}}$：

1. The adversary $\mathcal{A}$ outputs a pair of messages $m_0, m_1 \in \mathcal{M}$.

   敌手 $\mathcal{A}$ 输出一对消息 $m_0, m_1 \in \mathcal{M}$。

2. A key k is generated using Gen, and a uniform bit $b \in \{0,1\}$ is chosen. Ciphertext $c \leftarrow \mathsf{Enc}_k(m_b)$ is computed and given to A. We refer to c as the challenge ciphertext.

   使用 $\mathsf{Gen}$ 生成一个密钥 $k$，并选择一个均匀比特 $b \in \{0,1\}$。计算密文 $c \leftarrow \mathsf{Enc}_k(m_b)$ 并交给 $\mathcal{A}$。我们将 $c$ 称为挑战密文。

3. A outputs a bit b'.

   $\mathcal{A}$ 输出一个比特 $b'$。

4. The output of the experiment is defined to be 1 if $b^{\prime} = b$, and 0 otherwise. We write $\mathsf{PrivK}_{\mathcal{A},\Pi}^{\mathsf{eav}} = 1$ if the output of the experiment is 1 and in this case we say that $\mathcal{A}$ succeeds.

   实验的输出定义为：如果 $b^{\prime} = b$ 则为 1，否则为 0。如果实验的输出为 1，则记 $\mathsf{PrivK}_{\mathcal{A},\Pi}^{\mathsf{eav}} = 1$，此时称 $\mathcal{A}$ 成功。

As noted earlier, it is trivial for $\mathcal{A}$ to succeed with probability ${1}/2$ by outputting a random guess. Perfect indistinguishability requires that it is impossible for any $\mathcal{A}$ to do better.

如前所述，$\mathcal{A}$ 通过输出随机猜测以概率 ${1}/2$ 成功是轻而易举的。完美不可区分性要求任何 $\mathcal{A}$ 都不可能做得更好。

DEFINITION 2.6 Encryption scheme $\Pi = (\mathsf{Gen}, \mathsf{Enc}, \mathsf{Dec})$ with message space $\mathcal{M}$ is perfectly indistinguishable if for every $\mathcal{A}$ it holds that

定义 2.6 具有消息空间 $\mathcal{M}$ 的加密方案 $\Pi = (\mathsf{Gen}, \mathsf{Enc}, \mathsf{Dec})$ 是**完美不可区分**的，如果对于每一个 $\mathcal{A}$，都有

$$\Pr\left[\mathsf{PrivK}_{\mathcal{A},\Pi}^{\mathsf{eav}}=1\right]=\frac{1}{2}.$$

The following lemma states that Definition 2.6 is equivalent to Definition 2.3. We leave the proof of the lemma as Exercise 2.6.

下面的引理指出定义 2.6 与定义 2.3 是等价的。我们将该引理的证明留作习题 2.6。

LEMMA 2.7 Encryption scheme $\Pi$ is perfectly secret if and only if it is perfectly indistinguishable.

引理 2.7 加密方案 $\Pi$ 是完美保密的，当且仅当它是完美不可区分的。

**Example 2.8**　**示例 2.8**

We show that the Vigenère cipher is not perfectly indistinguishable, at least for certain parameters. Concretely, let $\Pi$ denote the Vigenère cipher for the message space of two-character strings, and where the period is chosen uniformly in $\{1,2\}$. To show that $\Pi$ is not perfectly indistinguishable, we exhibit an adversary $\mathcal{A}$ for which $\Pr\left[\mathsf{PrivK}_{\mathcal{A},\Pi}^{\mathsf{eav}}=1\right]>\frac{1}{2}$.

我们证明维吉尼亚密码不是完美不可区分的，至少对于某些参数如此。具体地，令 $\Pi$ 表示消息空间为双字符串的维吉尼亚密码，其中周期均匀选取自 $\{1,2\}$。为了证明 $\Pi$ 不是完美不可区分的，我们给出一个敌手 $\mathcal{A}$，使得 $\Pr\left[\mathsf{PrivK}_{\mathcal{A},\Pi}^{\mathsf{eav}}=1\right]>\frac{1}{2}$。

Adversary A does:

敌手 A 的行为如下：

1. Output $m_{0} = aa$ and $m_{1} = ab$.

   输出 $m_{0} = aa$ 和 $m_{1} = ab$。

2. Upon receiving the challenge ciphertext $c = c_1c_2$, do the following: if $c_1 = c_2$ output 0; else output 1.

   在收到挑战密文 $c = c_1c_2$ 后，执行如下操作：如果 $c_1 = c_2$ 则输出 0；否则输出 1。

Computation of $\Pr\left[\mathsf{PrivK}_{\mathcal{A},\Pi}^{\mathsf{eav}}=1\right]$ is tedious but straightforward.

计算 $\Pr\left[\mathsf{PrivK}_{\mathcal{A},\Pi}^{\mathsf{eav}}=1\right]$ 虽然繁琐但方法直截了当。

$$
\begin{aligned}
&\Pr\left[\mathsf{PrivK}_{\mathcal{A},\Pi}^{\mathsf{eav}}=1\right]\\
&=\frac{1}{2}\cdot\Pr\left[\mathsf{PrivK}_{\mathcal{A},\Pi}^{\mathsf{eav}}=1\mid b=0\right]+\frac{1}{2}\cdot\Pr\left[\mathsf{PrivK}_{\mathcal{A},\Pi}^{\mathsf{eav}}=1\mid b=1\right]\\
&=\frac{1}{2}\cdot\Pr[\mathcal{A}\text{ outputs }0\mid b=0]+\frac{1}{2}\cdot\Pr[\mathcal{A}\text{ outputs }1\mid b=1],
\end{aligned} \tag{2.4}
$$

where $b$ is the uniform bit determining which message gets encrypted. As defined, $\mathcal{A}$ outputs 0 if and only if the two characters of the ciphertext $c = c_1 c_2$ are equal. When $b = 0$ (so $m_0 = \mathtt{aa}$ is encrypted) then $c_1 = c_2$ if either (1) a key of period 1 is chosen, or (2) a key of period 2 is chosen and both characters of the key are equal. The former occurs with probability $\frac{1}{2}$, and the latter occurs with probability $\frac{1}{2} \cdot \frac{1}{26}$. So

其中 $b$ 是决定加密哪条消息的均匀比特。根据定义，$\mathcal{A}$ 输出 0 当且仅当密文 $c = c_1 c_2$ 的两个字符相等。当 $b = 0$（即加密 $m_0 = \mathtt{aa}$）时，$c_1 = c_2$ 在以下情况下发生：（1）选择了周期为 1 的密钥，或（2）选择了周期为 2 的密钥且密钥的两个字符相等。前者以概率 $\frac{1}{2}$ 发生，后者以概率 $\frac{1}{2} \cdot \frac{1}{26}$ 发生。因此

$$\Pr[\mathcal{A}\text{ outputs }0\mid b=0]=\frac{1}{2}+\frac{1}{2}\cdot\frac{1}{26}\approx0.52.$$

When $b = 1$ then $c_1 = c_2$ only if a key of period 2 is chosen and the first character of the key is one more than the second character of the key, which happens with probability $\frac{1}{2} \cdot \frac{1}{26}$. So

当 $b = 1$ 时，$c_1 = c_2$ 仅在选择了周期为 2 的密钥且密钥的第一个字符比第二个字符大 1 时发生，其概率为 $\frac{1}{2} \cdot \frac{1}{26}$。因此

$$\Pr[\mathcal{A}\text{ outputs }1\mid b=1]=1-\Pr[\mathcal{A}\text{ outputs }0\mid b=1]=1-\frac{1}{2}\cdot\frac{1}{26}\approx0.98.$$

Plugging into Equation (2.4) then gives

代入式 (2.4) 可得

$$\Pr\left[\mathsf{PrivK}_{\mathcal{A},\Pi}^{\mathsf{eav}}=1\right]=\frac{1}{2}\cdot\left(\frac{1}{2}+\frac{1}{2}\cdot\frac{1}{26}+1-\frac{1}{2}\cdot\frac{1}{26}\right)=0.75>\frac{1}{2},$$

and the scheme is not perfectly indistinguishable.

因此该方案不是完美不可区分的。

## 2.2 The One-Time Pad　一次一密

In 1917, Vernam patented a perfectly secret encryption scheme now called the one-time pad. At the time Vernam proposed the scheme, there was no proof that it was perfectly secret; in fact, the notion of perfect secrecy was not yet defined. Approximately 25 years later, however, Shannon introduced the definition of perfect secrecy and demonstrated that the one-time pad satisfied that definition.

1917 年，Vernam 为一种完美保密的加密方案申请了专利，该方案现在被称为**一次一密**（one-time pad）。在 Vernam 提出该方案时，并没有证明它是完美保密的；事实上，完美保密的概念当时尚未被定义。然而，大约 25 年后，Shannon 引入了完美保密的定义，并证明了一次一密满足该定义。

In describing the scheme we let $a \oplus b$ denote the bitwise exclusive-or (XOR) of two equal-length binary strings $a$ and $b$. (i.e., if $a = a_1 \cdots a_\ell$ and $b = b_1 \cdots b_\ell$ are $\ell$-bit strings, then $a \oplus b$ is the $\ell$-bit string given by $(a_1 \oplus b_1) \cdots (a_\ell \oplus b_\ell)$.) In the one-time pad encryption scheme the key is a uniform string of the same length as the message, and the ciphertext is computed by simply XORing the key and the message; a formal definition is given as Construction 2.9. Before discussing security, we first verify correctness: For every key $k$ and every message $m$ it holds that $\mathsf{Dec}_k(\mathsf{Enc}_k(m)) = k \oplus k \oplus m = m$, and so the one-time pad constitutes a valid encryption scheme.

在描述该方案时，我们用 $a \oplus b$ 表示两个等长二进制串 $a$ 和 $b$ 的按位异或（XOR）。（即，如果 $a = a_1 \cdots a_\ell$ 和 $b = b_1 \cdots b_\ell$ 是 $\ell$ 比特的串，那么 $a \oplus b$ 是由 $(a_1 \oplus b_1) \cdots (a_\ell \oplus b_\ell)$ 给出的 $\ell$ 比特串。）在一次一密加密方案中，密钥是一个与消息等长的均匀串，密文通过简单地将密钥与消息异或来计算；形式化定义如构造 2.9 所示。在讨论安全性之前，我们首先验证正确性：对于每一个密钥 $k$ 和每一条消息 $m$，有 $\mathsf{Dec}_k(\mathsf{Enc}_k(m)) = k \oplus k \oplus m = m$，因此一次一密构成了一个有效的加密方案。

One can easily prove perfect secrecy of the one-time pad using Lemma 2.5 because the ciphertext is uniformly distributed regardless of what message is encrypted. We give a direct proof based on the original definition.

利用引理 2.5 可以轻松证明一次一密的完美保密性，因为无论加密什么消息，密文都是均匀分布的。我们给出一个基于原始定义的直接证明。

> **CONSTRUCTION 2.9**　**构造 2.9**
>
> Fix an integer $\ell > 0$. The message space $\mathcal{M}$, key space $\mathcal{K}$, and ciphertext space $\mathcal{C}$ are all equal to $\{0,1\}^{\ell}$ (the set of all binary strings of length $\ell$).
>
> Gen: the key-generation algorithm chooses a key from $\mathcal{K} = \{0,1\}^{\ell}$ according to the uniform distribution (i.e., each of the ${2}^{\ell}$ strings in the space is chosen as the key with probability exactly ${2}^{-\ell}$).
>
> - Enc: given a key $k \in \{0,1\}^{\ell}$ and a message $m \in \{0,1\}^{\ell}$, the encryption algorithm outputs the ciphertext $c := k \oplus m$.
> - Dec: given a key $k \in \{0,1\}^{\ell}$ and a ciphertext $c \in \{0,1\}^{\ell}$, the decryption algorithm outputs the message $m := k \oplus c$.
>
> 固定一个整数 $\ell > 0$。消息空间 $\mathcal{M}$、密钥空间 $\mathcal{K}$ 和密文空间 $\mathcal{C}$ 都等于 $\{0,1\}^{\ell}$（所有长度为 $\ell$ 的二进制串的集合）。
>
> Gen：密钥生成算法根据均匀分布从 $\mathcal{K} = \{0,1\}^{\ell}$ 中选择一个密钥（即空间中 ${2}^{\ell}$ 个串中的每一个被选为密钥的概率恰好为 ${2}^{-\ell}$）。
>
> - Enc：给定密钥 $k \in \{0,1\}^{\ell}$ 和消息 $m \in \{0,1\}^{\ell}$，加密算法输出密文 $c := k \oplus m$。
> - Dec：给定密钥 $k \in \{0,1\}^{\ell}$ 和密文 $c \in \{0,1\}^{\ell}$，解密算法输出消息 $m := k \oplus c$。
>
> The one-time pad encryption scheme. / 一次一密加密方案。

THEOREM 2.10 The one-time pad encryption scheme is perfectly secret.

定理 2.10 一次一密加密方案是完美保密的。

PROOF We first compute $\Pr[C = c \mid M = m]$ for arbitrary $c \in \mathcal{C}$ and $m \in \mathcal{M}$ with $\Pr[M = m] > 0$. For the one-time pad, we have

证明 我们首先对任意 $c \in \mathcal{C}$ 和满足 $\Pr[M = m] > 0$ 的 $m \in \mathcal{M}$ 计算 $\Pr[C = c \mid M = m]$。对于一次一密，我们有

$$\begin{aligned}\Pr[C=c\mid M=m]&=\Pr[K\oplus m=c\mid M=m]\\&=\Pr[K=m\oplus c\mid M=m]\\&=2^{-\ell},\end{aligned}$$

where the first equality is by definition of the scheme and the fact that we condition on the event $M = m$, and the final equality holds because the key $K$ is a uniform $\ell$-bit string that is independent of $M$. Fix any distribution over $\mathcal{M}$. Using the above result, we see that for any $c \in \mathcal{C}$ we have

其中第一个等式来自方案的定义以及我们以事件 $M = m$ 为条件这一事实，最后一个等式成立是因为密钥 $K$ 是一个独立于 $M$ 的均匀 $\ell$ 比特串。固定 $\mathcal{M}$ 上的任意分布。利用上述结果，我们看到对于任意 $c \in \mathcal{C}$ 有

$$\begin{aligned}\Pr[C=c]&=\sum_{m\in\mathcal{M}}\Pr[C=c\mid M=m]\cdot\Pr[M=m]\\&=2^{-\ell}\cdot\sum_{m\in\mathcal{M}}\Pr[M=m]\\&=2^{-\ell},\\ \end{aligned}$$

where the sum is over $m \in \mathcal{M}$ with $\Pr[M = m] \neq 0$. Bayes' Theorem gives:

其中求和遍历所有满足 $\Pr[M = m] \neq 0$ 的 $m \in \mathcal{M}$。贝叶斯定理给出：

$$\begin{aligned}\Pr[M=m\mid C=c]&=\frac{\Pr[C=c\mid M=m]\cdot\Pr[M=m]}{\Pr[C=c]}\\&=\frac{2^{-\ell}\cdot\Pr[M=m]}{2^{-\ell}}\\&=\Pr[M=m].\end{aligned}$$

We conclude that the one-time pad is perfectly secret.

我们得出结论：一次一密是完美保密的。

The one-time pad was used by several national-intelligence agencies in the mid-20th century to encrypt sensitive traffic. Perhaps most famously, the "red phone" linking the White House and the Kremlin during the Cold War was protected using one-time pad encryption, where the governments of the US and the USSR would exchange extremely long keys using trusted couriers carrying briefcases of paper on which random characters were written.

在 20 世纪中期，多个国家情报机构曾使用一次一密来加密敏感通信。最著名的例子或许是冷战期间连接白宫和克里姆林宫的“红机”电话，它使用一次一密加密进行保护，美国和苏联政府通过可信的信使携带装满随机字符纸张的公文包来交换极长的密钥。

Notwithstanding the above, one-time pad encryption is rarely used nowadays because it has a number of drawbacks. Most prominent is that the key is as long as the message.$^{2}$ This limits the usefulness of the scheme for sending very long messages (as it may be difficult to securely share and store a very long key), and is problematic when the parties cannot predict in advance (an upper bound on) how long the message will be.

尽管如此，一次一密加密如今已很少使用，因为它有许多缺点。最突出的缺点是密钥与消息等长。$^{2}$ 这限制了该方案在发送极长消息时的实用性（因为安全地共享和存储极长的密钥可能很困难），并且在各方无法预先预测消息长度（的上界）时也会产生问题。

$^{2}$ The one-time pad is popularly attributed to Vernam, but the version patented by Vernam did not actually require the key to be as long as the message; the notion of security achieved by that version is not clear.

$^{2}$ 一次一密通常归功于 Vernam，但 Vernam 申请专利的版本实际上并不要求密钥与消息等长；该版本所达到的安全性概念并不明确。

Moreover, the one-time pad—as the name indicates—is only secure if used once (with a given key). Although we did not yet define a notion of secrecy when multiple messages are encrypted, it is easy to see that encrypting more than one message with the same key leaks a lot of information. In particular, say two messages $m, m^{\prime}$ are encrypted using the same (unknown) key $k$. An adversary who obtains $c = m \oplus k$ and $c^{\prime} = m^{\prime} \oplus k$ can compute

此外，一次一密——如其名称所示——只有在（使用给定密钥）使用一次的情况下才是安全的。虽然我们还没有定义加密多条消息时的保密性概念，但很容易看出用同一个密钥加密多条消息会泄露大量信息。特别地，假设两条消息 $m, m^{\prime}$ 使用同一个（未知的）密钥 $k$ 加密。获得 $c = m \oplus k$ 和 $c^{\prime} = m^{\prime} \oplus k$ 的敌手可以计算

$$c\oplus c^{\prime}=(m\oplus k)\oplus(m^{\prime}\oplus k)=m\oplus m^{\prime}$$

and thus learn the XOR of the two messages or, equivalently, exactly where the two messages differ. This attack extends to more than two messages as well, where it enables the attacker to learn the XOR of all pairs of messages. While this may not seem very significant, it is enough to rule out any claims of perfect secrecy for encrypting more than one message using the same key. Moreover, if the messages correspond to natural-language text, then given the XOR of sufficiently many pairs of messages—or even two sufficiently long messages—it is possible to perform frequency analysis (as in the previous chapter, though more complex) and recover the messages themselves. (See Exercise 2.16 for an example.) An interesting historical example of this is given by the VENONA project, as part of which the US and UK were able to decrypt ciphertexts sent by the Soviet Union that were mistakenly encrypted with repeated portions of a one-time pad over several decades.

从而获知两条消息的异或，或者等价地，获知两条消息在哪些位置上不同。这种攻击也扩展到两条以上的消息，使攻击者能够获知所有消息对的异或。虽然这看起来可能无足轻重，但已足以排除如下主张：用同一个密钥加密多条消息仍能实现完美保密。此外，如果消息对应于自然语言文本，那么在获得足够多的消息对的异或——甚至两条足够长的消息——之后，就可以进行频率分析（如上一章所述，但更复杂）并恢复出消息本身。（示例见习题 2.16。）一个有趣的历史案例是 VENONA 项目，在该项目中，美国和英国得以在几十年的时间里解密苏联发送的密文，这些密文在加密时错误地重复使用了一次一密的部分密钥。

## 2.3 Limitations of Perfect Secrecy　完美保密的局限性

We ended the previous section by noting some drawbacks of the one-time pad encryption scheme. Here, we show that these drawbacks are not specific to that scheme, but are instead inherent limitations of perfect secrecy. Specifically, we prove that any perfectly secret encryption scheme must have a key space that is at least as large as the message space. If all keys are the same length, and the message space consists of all strings of some fixed length, this implies that the key is at least as long as the message. In particular, the key length of the one-time pad is optimal. (The other limitation—namely, that a key can be used only once—is also inherent; see Exercise 2.19.)

我们在上一节末尾指出了一次一密加密方案的一些缺点。在此，我们证明这些缺点并非该方案所特有，而是完美保密的固有限制。具体来说，我们证明任何完美保密的加密方案的密钥空间都必须不小于消息空间。如果所有密钥长度相同，且消息空间由某个固定长度的所有串组成，这就意味着密钥至少与消息一样长。特别地，一次一密的密钥长度是最优的。（另一个限制——即密钥只能使用一次——也是固有的；见习题 2.19。）

THEOREM 2.11 If (Gen, Enc, Dec) is a perfectly secret encryption scheme with message space $\mathcal{M}$ and key space $\mathcal{K}$, then $|\mathcal{K}| \geq |\mathcal{M}|$.

定理 2.11 如果 (Gen, Enc, Dec) 是一个具有消息空间 $\mathcal{M}$ 和密钥空间 $\mathcal{K}$ 的完美保密加密方案，那么 $|\mathcal{K}| \geq |\mathcal{M}|$。

PROOF We show that if $|\mathcal{K}| < |\mathcal{M}|$ then the scheme cannot be perfectly secret. Assume $|\mathcal{K}| < |\mathcal{M}|$. Consider the uniform distribution over $\mathcal{M}$ and let $c \in \mathcal{C}$ be a ciphertext that occurs with nonzero probability. Let $\mathcal{M}(c)$ be the set of all possible messages that are possible decryptions of $c$; that is

证明 我们证明如果 $|\mathcal{K}| < |\mathcal{M}|$，那么该方案不可能是完美保密的。假定 $|\mathcal{K}| < |\mathcal{M}|$。考虑 $\mathcal{M}$ 上的均匀分布，并令 $c \in \mathcal{C}$ 是一个以非零概率出现的密文。令 $\mathcal{M}(c)$ 是把密文 $c$ 解密所能得到的全部消息的集合，即

$$\mathcal{M}(c)\overset{\operatorname{def}}{=}\{m\mid m=\mathsf{Dec}_{k}(c)\mathrm{for~some}k\in\mathcal{K}\}.$$

Clearly $|\mathcal{M}(c)| \leq |\mathcal{K}|$. (Recall that we may assume Dec is deterministic.) If $|\mathcal{K}| < |\mathcal{M}|$, there is some $m^{\prime} \in \mathcal{M}$ such that $m^{\prime} \notin \mathcal{M}(c)$. But then

显然 $|\mathcal{M}(c)| \leq |\mathcal{K}|$。（回忆一下，我们可以假定 Dec 是确定性的。）如果 $|\mathcal{K}| < |\mathcal{M}|$，存在某个 $m^{\prime} \in \mathcal{M}$ 使得 $m^{\prime} \notin \mathcal{M}(c)$。但此时

$$\Pr[M=m^{\prime}\mid C=c]=0\neq\Pr[M=m^{\prime}],$$

and so the scheme is not perfectly secret.

因此该方案不是完美保密的。

Perfect secrecy with shorter keys? The above theorem shows an inherent limitation of schemes that achieve perfect secrecy. Even so, individuals occasionally claim they have developed a radically new encryption scheme that is "unbreakable" and achieves the security of the one-time pad without using keys as long as what is being encrypted. The above proof demonstrates that such claims cannot be true; anyone making such claims either knows very little about cryptography or is blatantly lying.

**用更短的密钥实现完美保密？**

上述定理展示了实现完美保密的方案的固有限制。即便如此，偶尔仍有人声称他们开发了一种全新的、“不可攻破”的加密方案，无需使用与待加密内容等长的密钥便能实现一次一密的安全性。上述证明表明，这样的说法不可能是真的；任何做出这种声明的人要么对密码学知之甚少，要么就是在公然撒谎。

## 2.4 \*Shannon's Theorem　香农定理

In his work on perfect secrecy, Shannon also provided a characterization of perfectly secret encryption schemes. This characterization says that, under certain conditions, the key-generation algorithm Gen must choose the key uniformly from the set of all possible keys (as in the one-time pad); moreover, for every message m and ciphertext c there is a unique key mapping m to c (again, as in the one-time pad). Beyond being interesting in its own right, this theorem is a useful tool for proving (or disproving) perfect secrecy of schemes. We discuss this further after the proof.

Shannon 在其关于完美保密的工作中，还给出了完美保密加密方案的一个刻画。该刻画表明，在某些条件下，密钥生成算法 Gen 必须从所有可能密钥的集合中均匀地选择密钥（如同一次一密那样）；此外，对于每一条消息 $m$ 和每一个密文 $c$，存在唯一的密钥将 $m$ 映射到 $c$（同样，如同一次一密那样）。除了其自身的理论意义外，该定理也是证明（或反驳）方案完美保密性的有用工具。我们在证明之后进一步讨论这一点。

The theorem as stated here assumes $|\mathcal{M}| = |\mathcal{K}| = |\mathcal{C}|$, meaning that the sets of plaintexts, keys, and ciphertexts all have the same size. We have already seen that for perfect secrecy we must have $|\mathcal{K}| \geq |\mathcal{M}|$. It is easy to see that correct decryption requires $|\mathcal{C}| \geq |\mathcal{M}|$. Therefore, in some sense, perfectly secret encryption schemes with $|\mathcal{M}| = |\mathcal{K}| = |\mathcal{C}|$ are "optimal."

这里陈述的定理假定 $|\mathcal{M}| = |\mathcal{K}| = |\mathcal{C}|$，即明文、密钥和密文的集合都具有相同的大小。我们已经看到，对于完美保密必须有 $|\mathcal{K}| \geq |\mathcal{M}|$。容易看出，正确的解密要求 $|\mathcal{C}| \geq |\mathcal{M}|$。因此，从某种意义上说，满足 $|\mathcal{M}| = |\mathcal{K}| = |\mathcal{C}|$ 的完美保密加密方案是“最优的”。

THEOREM 2.12 (Shannon's theorem) Let (Gen, Enc, Dec) be an encryption scheme with message space $\mathcal{M}$, for which $|\mathcal{M}| = |\mathcal{K}| = |\mathcal{C}|$. The scheme is perfectly secret if and only if:

定理 2.12（香农定理） 设 (Gen, Enc, Dec) 是一个具有消息空间 $\mathcal{M}$ 的加密方案，且 $|\mathcal{M}| = |\mathcal{K}| = |\mathcal{C}|$。该方案是完美保密的当且仅当：

1. Every key $k \in \mathcal{K}$ is chosen with (equal) probability ${1}/|\mathcal{K}|$ by Gen.

   每个密钥 $k \in \mathcal{K}$ 被 Gen 以（相等的）概率 ${1}/|\mathcal{K}|$ 选取。

2. For every $m \in \mathcal{M}$ and every $c \in \mathcal{C}$, there is a unique key $k \in \mathcal{K}$ such that $\mathsf{Enc}_k(m)$ outputs $c$.

   对于每一个 $m \in \mathcal{M}$ 和每一个 $c \in \mathcal{C}$，存在唯一的密钥 $k \in \mathcal{K}$ 使得 $\mathsf{Enc}_k(m)$ 输出 $c$。

PROOF The intuition behind the proof is as follows. To see that the stated conditions imply perfect secrecy, note that condition 2 means that any ciphertext $c$ could be the result of encrypting any possible plaintext $m$, because there is some key $k$ mapping $m$ to $c$. Since there is a unique such key, and each key is chosen with equal probability, perfect secrecy follows as for the one-time pad. For the other direction, perfect secrecy immediately implies that for every $m$ and $c$ there is at least one key mapping $m$ to $c$. The fact that $|\mathcal{M}| = |\mathcal{K}| = |\mathcal{C}|$ means, moreover, that for every $m$ and $c$ there is exactly one such key. Given this, each key must be chosen with equal probability or else perfect secrecy would fail to hold. A formal proof follows.

证明 证明的直观思路如下。要看出所述条件蕴含完美保密，注意到条件 2 意味着任何密文 $c$ 都可能是加密任意明文 $m$ 的结果，因为总存在某个密钥 $k$ 将 $m$ 映射到 $c$。由于这样的密钥唯一，且每个密钥被等概率选取，因此与一次一密同理可得完美保密。对于另一个方向，由完美保密立即可知：对每个 $m$ 和 $c$，至少存在一个把 $m$ 映射到 $c$ 的密钥。而 $|\mathcal{M}| = |\mathcal{K}| = |\mathcal{C}|$ 进一步意味着每个 $m$ 和 $c$ 恰好对应一个这样的密钥。由此，每个密钥必须被等概率选取，否则完美保密将不成立。下面给出形式化证明。

We assume for simplicity that $\mathsf{Enc}$ is deterministic. (One can show that this is without loss of generality here.) We first prove that if the encryption scheme satisfies conditions 1 and 2, then it is perfectly secret. The proof is essentially the same as the proof of perfect secrecy for the one-time pad, so we will be relatively brief. Fix arbitrary $c \in \mathcal{C}$ and $m \in \mathcal{M}$. Let $k$ be the unique key, guaranteed by condition 2, for which $\mathsf{Enc}_k(m) = c$. Then,

为简单起见，我们假定 $\mathsf{Enc}$ 是确定性的。（可以证明在此不失一般性。）我们首先证明，如果加密方案满足条件 1 和 2，那么它是完美保密的。该证明本质上与一次一密的完美保密证明相同，因此我们会写得相对简略。固定任意 $c \in \mathcal{C}$ 和 $m \in \mathcal{M}$。令 $k$ 为条件 2 所保证的唯一密钥，使得 $\mathsf{Enc}_k(m) = c$。于是，

$$\Pr[\mathsf{Enc}_{K}(m)=c]=\Pr[K=k]=1/|\mathcal{K}|,$$

where the final equality holds by condition 1. Since this holds for arbitrary m and c, Lemma 2.5 implies that the scheme is perfectly secret.

其中最后一个等式由条件 1 保证。由于这对任意的 m 和 c 成立，引理 2.5 表明该方案是完美保密的。

For the second direction, assume the encryption scheme is perfectly secret; we show that conditions 1 and 2 hold. Fix arbitrary $c \in \mathcal{C}$. There must be some message $m^*$ for which $\Pr[\mathsf{Enc}_K(m^*) = c] \neq 0$. Lemma 2.5 then implies that $\Pr[\mathsf{Enc}_K(m) = c] \neq 0$ for every $m \in \mathcal{M}$. In other words, if we let $\mathcal{M} = \{m_1, m_2, \ldots\}$, then for each $m_i \in \mathcal{M}$ we have a nonempty set of keys $\mathcal{K}_i \subset \mathcal{K}$ such that $\mathsf{Enc}_k(m_i) = c$ if and only if $k \in \mathcal{K}_i$. Moreover, when $i \neq j$ then $\mathcal{K}_i$ and $\mathcal{K}_j$ must be disjoint or else correctness fails to hold. Since $|\mathcal{K}| = |\mathcal{M}|$, we see that each $\mathcal{K}_i$ contains only a single key $k_i$, as required by condition 2. Now, Lemma 2.5 shows that for any $m_i, m_j \in \mathcal{M}$ we have

对于第二个方向，假定加密方案是完美保密的；我们证明条件 1 和 2 成立。固定任意 $c \in \mathcal{C}$。必存在某条消息 $m^*$ 使得 $\Pr[\mathsf{Enc}_K(m^*) = c] \neq 0$。引理 2.5 进而表明，对于每一个 $m \in \mathcal{M}$，有 $\Pr[\mathsf{Enc}_K(m) = c] \neq 0$。换句话说，如果我们令 $\mathcal{M} = \{m_1, m_2, \ldots\}$，那么对于每个 $m_i \in \mathcal{M}$，存在一个非空的密钥集合 $\mathcal{K}_i \subset \mathcal{K}$，使得 $\mathsf{Enc}_k(m_i) = c$ 当且仅当 $k \in \mathcal{K}_i$。此外，当 $i \neq j$ 时，$\mathcal{K}_i$ 和 $\mathcal{K}_j$ 必须互不相交，否则正确性将不成立。由于 $|\mathcal{K}| = |\mathcal{M}|$，我们看到每个 $\mathcal{K}_i$ 仅包含单个密钥 $k_i$，正如条件 2 所要求的那样。现在，引理 2.5 表明对于任意 $m_i, m_j \in \mathcal{M}$，有

$$\Pr[K=k_{i}]=\Pr[\mathsf{Enc}_{K}(m_{i})=c]=\Pr[\mathsf{Enc}_{K}(m_{j})=c]=\Pr[K=k_{j}].$$

Since this holds for all ${1} \leq i, j \leq |\mathcal{M}| = |\mathcal{K}|$, and $k_i \neq k_j$ for $i \neq j$, this means each key is chosen with probability ${1}/|\mathcal{K}|$, as required by condition 1.

由于这对所有 ${1} \leq i, j \leq |\mathcal{M}| = |\mathcal{K}|$ 成立，且当 $i \neq j$ 时 $k_i \neq k_j$，这意味着每个密钥以概率 ${1}/|\mathcal{K}|$ 被选取，正如条件 1 所要求的那样。

Shannon's theorem is useful for deciding whether a given scheme is perfectly secret. Condition 1 is easy to check, and condition 2 can be demonstrated (or contradicted) without having to compute any probabilities (in contrast to working with Definition 2.3 directly). As an example, perfect secrecy of the one-time pad is trivial to prove using Shannon's theorem. We stress, however, that the theorem only applies when $|\mathcal{M}| = |\mathcal{K}| = |\mathcal{C}|$.

香农定理在判断给定方案是否为完美保密时很有用。条件 1 容易检查，条件 2 无需计算任何概率便可得到验证（或反驳）——这与直接使用定义 2.3 形成对比。例如，使用香农定理证明一次一密的完美保密性是轻而易举的。然而，我们强调，该定理仅适用于 $|\mathcal{M}| = |\mathcal{K}| = |\mathcal{C}|$ 的情况。

### References and Additional Reading　参考文献与延伸阅读

The one-time pad is popularly credited to Vernam [200], who filed a patent on it, but recent historical research [28] shows that it was invented some 35 years earlier. Analysis of the one-time pad had to await the groundbreaking work of Shannon [177], who introduced the notion of perfect secrecy.

一次一密通常归功于 Vernam [200]，他为此申请了专利，但最近的历史研究 [28] 表明，它在 Vernam 申请专利约 35 年前就已被发明。对一次一密的分析有待于 Shannon [177] 的开创性工作，他引入了完美保密的概念。

In this chapter we studied perfectly secret encryption. Some other cryptographic problems can also be solved with "perfect" security. A notable example is the problem of message authentication where the aim is to prevent an adversary from (undetectably) modifying a message sent from one party to another. We study this problem in depth in Chapter 4, discussing "perfectly secure" message authentication in Section 4.6.

在本章中，我们研究了完美保密加密。其他一些密码学问题也可以用“完美”安全性来解决。一个显著的例子是消息认证问题，其目标是防止敌手（不可检测地）修改从一方发送给另一方的消息。我们将在第 4 章深入研究这个问题，并在 4.6 节讨论“完美安全”的消息认证。

### Exercises　习题

2.1 Prove that, by redefining the key space, we may assume that the key-generation algorithm Gen chooses a uniform key from the key space, without changing $\Pr[C = c \mid M = m]$ for any m, c.
Hint: Define the key space to be the set of all possible random bits used by the randomized algorithm Gen.

2.1 证明：通过重新定义密钥空间，我们可以假设密钥生成算法 Gen 从密钥空间中均匀选取密钥，而不改变任意 $m, c$ 的 $\Pr[C = c \mid M = m]$。
提示：将密钥空间定义为随机化算法 Gen 所使用的所有可能随机比特的集合。

2.2 Prove that, by redefining the key space as well as the encryption algorithm, we may assume that encryption is deterministic without changing $\Pr[C = c \mid M = m]$ for any m, c.

2.2 证明：通过重新定义密钥空间与加密算法，我们可以假设加密是确定性的，而不改变任意 $m, c$ 的 $\Pr[C = c \mid M = m]$。

2.3 Prove or refute: An encryption scheme with message space $\mathcal{M}$ is perfectly secret if and only if for every probability distribution on $\mathcal{M}$ and every $c_0, c_1 \in \mathcal{C}$ we have $\Pr[C = c_0] = \Pr[C = c_1]$.

2.3 证明或反驳：消息空间为 $\mathcal{M}$ 的加密方案是完美保密的，当且仅当对于 $\mathcal{M}$ 上的每个概率分布以及每个 $c_0, c_1 \in \mathcal{C}$，都有 $\Pr[C = c_0] = \Pr[C = c_1]$。

2.4 Prove or refute: For every perfectly secret encryption scheme it holds that for every distribution on the message space $\mathcal{M}$, every $m, m^{\prime} \in \mathcal{M}$, and every $c \in \mathcal{C}$:

$$
\Pr[M=m\mid C=c]=\Pr[M=m^{\prime}\mid C=c].
$$

2.4 证明或反驳：对于每个完美保密的加密方案，对消息空间 $\mathcal{M}$ 上的每个分布、每一对 $m, m^{\prime} \in \mathcal{M}$ 以及每个 $c \in \mathcal{C}$：

$$
\Pr[M=m\mid C=c]=\Pr[M=m^{\prime}\mid C=c].
$$

2.5 Prove that in Definition 2.6 we may assume $\mathcal{A}$ is deterministic without loss of generality.

2.5 证明在定义 2.6 中可以不失一般性地假设 $\mathcal{A}$ 是确定性的。

2.6 Prove Lemma 2.7.

2.6 证明引理 2.7。

2.7 What is the ciphertext that results when the plaintext 0x012345 (written in hex) is encrypted using the one-time pad with key 0xFFEEDD?

2.7 当使用密钥为 0xFFEEDD 的一次一密对明文 0x012345（以十六进制表示）进行加密时，得到的密文是什么？

2.8 For each of the following encryption schemes, state whether the scheme is perfectly secret. Justify your answer in each case.

(a) The message space is $\mathcal{M} = \{0, \ldots, 4\}$, and Gen chooses a uniform key from the key space $\mathcal{K} = \{0, \ldots, 5\}$. $\mathsf{Enc}_k(m)$ returns $[m + k \bmod 5]$, and $\mathsf{Dec}_k(c)$ returns $[c - k \bmod 5]$.

(b) The message space is $\mathcal{M} = \{m \in \{0,1\}^{\ell} \mid \text{the last bit of } m \text{ is } 0\}$. Gen chooses a uniform key from $\{0,1\}^{\ell-1}$. $\mathsf{Enc}_k(m)$ returns cipher-text $m \oplus (k\|0)$, and $\mathsf{Dec}_k(c)$ returns $c \oplus (k\|0)$.

2.8 对下列每个加密方案，判断该方案是否完美保密，并说明理由。

(a) 消息空间为 $\mathcal{M} = \{0, \ldots, 4\}$，Gen 从密钥空间 $\mathcal{K} = \{0, \ldots, 5\}$ 中均匀选取密钥。$\mathsf{Enc}_k(m)$ 返回 $[m + k \bmod 5]$，$\mathsf{Dec}_k(c)$ 返回 $[c - k \bmod 5]$。

(b) 消息空间为 $\mathcal{M} = \{m \in \{0,1\}^{\ell} \mid m \text{ 的最后一位是 } 0\}$。Gen 从 $\{0,1\}^{\ell-1}$ 中均匀选取密钥。$\mathsf{Enc}_k(m)$ 返回密文 $m \oplus (k\|0)$，$\mathsf{Dec}_k(c)$ 返回 $c \oplus (k\|0)$。

2.9 In each of the following schemes, $\mathsf{Enc}_k(m) = [m+k \mod 3]$. State in each case whether the scheme is perfectly secret, and justify your answers.

(a) The message space is $\mathcal{M} = \{0,1\}$, and Gen chooses a uniform key from the key space $\mathcal{K} = \{0,1\}$.

(b) The message space is $\mathcal{M} = \{0,1,2\}$, and Gen chooses a uniform key from the key space $\mathcal{K} = \{0,1,2\}$.

(c) The message space is $\mathcal{M} = \{0,1\}$, and Gen chooses a uniform key from the key space $\mathcal{K} = \{0,1,2\}$.

2.9 在下列每个方案中，$\mathsf{Enc}_k(m) = [m+k \bmod 3]$。分别判断该方案是否完美保密，并说明理由。

(a) 消息空间为 $\mathcal{M} = \{0,1\}$，Gen 从密钥空间 $\mathcal{K} = \{0,1\}$ 中均匀选取密钥。

(b) 消息空间为 $\mathcal{M} = \{0,1,2\}$，Gen 从密钥空间 $\mathcal{K} = \{0,1,2\}$ 中均匀选取密钥。

(c) 消息空间为 $\mathcal{M} = \{0,1\}$，Gen 从密钥空间 $\mathcal{K} = \{0,1,2\}$ 中均匀选取密钥。

2.10 The following questions concern the message space $\mathcal{M} = \{0,1\}^{\leq\ell}$, the set of all nonempty binary strings of length at most $\ell$.

(a) Consider the encryption scheme in which Gen chooses a uniform key from $\mathcal{K} = \{0,1\}^{\ell}$, and $\mathsf{Enc}_k(m)$ outputs $k_{|m|} \oplus m$, where $k_t$ denotes the first $t$ bits of $k$. Show that this scheme is not perfectly secret for message space $\mathcal{M}$.

(b) Design a perfectly secret encryption scheme for message space M.

2.10 以下问题涉及消息空间 $\mathcal{M} = \{0,1\}^{\leq\ell}$，即长度至多为 $\ell$ 的所有非空二进制串的集合。

(a) 考虑如下加密方案：Gen 从 $\mathcal{K} = \{0,1\}^{\ell}$ 中均匀选取密钥，$\mathsf{Enc}_k(m)$ 输出 $k_{|m|} \oplus m$，其中 $k_t$ 表示 $k$ 的前 $t$ 位。证明该方案对消息空间 $\mathcal{M}$ 不是完美保密的。

(b) 为消息空间 $\mathcal{M}$ 设计一个完美保密的加密方案。

2.11 When using the one-time pad with the key $k = 0^\ell$, we have $\mathsf{Enc}_k(m) = k \oplus m = m$ and the message is sent in the clear! It has therefore been suggested to modify the one-time pad by only encrypting with $k \neq 0^\ell$ (i.e., to have *Gen* choose $k$ uniformly from the set of *nonzero* keys of length $\ell$). Is this modified scheme still perfectly secret? Explain.

2.11 当使用密钥 $k = 0^\ell$ 的一次一密时，我们有 $\mathsf{Enc}_k(m) = k \oplus m = m$，消息被明文发送！因此有人建议修改一次一密，只用 $k \neq 0^\ell$ 的密钥加密（即让 *Gen* 从长度为 $\ell$ 的*非零*密钥集合中均匀选取 $k$）。这个修改后的方案仍然是完美保密的吗？请解释。

2.12 Let $\Pi$ denote the Vigenère cipher where the message space consists of all 3-character strings (over the English alphabet), and the period $t$ is fixed to 2 (and so the key is a uniform string of length 2). Define $\mathcal{A}$ as follows: $\mathcal{A}$ outputs $m_0 = \mathtt{aaa}$ and $m_1 = \mathtt{aab}$. When given a ciphertext $c$, it outputs 0 if the first character of $c$ is the same as the third character of $c$, and outputs 1 otherwise. Compute $\Pr[\mathrm{PrivK}_{\mathcal{A},\Pi}^{\mathtt{eav}}=1]$.

2.12 设 $\Pi$ 表示维吉尼亚密码，其消息空间由（英文字母表上的）所有 3 字符串组成，周期 $t$ 固定为 2（因此密钥是长度为 2 的均匀字符串）。定义 $\mathcal{A}$ 如下：$\mathcal{A}$ 输出 $m_0 = \mathtt{aaa}$ 和 $m_1 = \mathtt{aab}$。当收到密文 $c$ 时，若 $c$ 的第一个字符与第三个字符相同则输出 0，否则输出 1。计算 $\Pr[\mathrm{PrivK}_{\mathcal{A},\Pi}^{\mathtt{eav}}=1]$。

2.13 Let $\Pi$ denote the Vigenère cipher where the message space consists of all 3-character strings (over the English alphabet), and the key is generated by first choosing the period $t$ uniformly from $\{1,2,3\}$ and then letting the key be a uniform string of length $t$.

(a) Define $\mathcal{A}$ as follows: $\mathcal{A}$ outputs $m_0 = \mathtt{aab}$ and $m_1 = \mathtt{abb}$. When given a ciphertext $c$, it outputs 0 if the first character of $c$ is the same as the second character of $c$, and outputs 1 otherwise. Compute $\Pr[\mathrm{PrivK}_{\mathcal{A},\Pi}^{\mathrm{eav}}=1]$.

(b) Construct and analyze an adversary $\mathcal{A}^{\prime}$ for which $\Pr[\mathrm{PrivK}_{\mathcal{A}^{\prime},\Pi}^{\mathrm{eav}}=1]$ is greater than your answer from part (a).

2.13 设 $\Pi$ 表示维吉尼亚密码，其消息空间由（英文字母表上的）所有 3 字符串组成，密钥的生成方式是先从 $\{1,2,3\}$ 中均匀选取周期 $t$，再取长度为 $t$ 的均匀字符串作为密钥。

(a) 定义 $\mathcal{A}$ 如下：$\mathcal{A}$ 输出 $m_0 = \mathtt{aab}$ 和 $m_1 = \mathtt{abb}$。当收到密文 $c$ 时，若 $c$ 的第一个字符与第二个字符相同则输出 0，否则输出 1。计算 $\Pr[\mathrm{PrivK}_{\mathcal{A},\Pi}^{\mathrm{eav}}=1]$。

(b) 构造并分析一个敌手 $\mathcal{A}^{\prime}$，使其 $\Pr[\mathrm{PrivK}_{\mathcal{A}^{\prime},\Pi}^{\mathrm{eav}}=1]$ 大于 (a) 中得到的答案。

2.14 In this exercise, we look at different conditions under which the shift, mono-alphabetic substitution, and Vigenère ciphers are perfectly secret:

(a) Prove that if only a single character is encrypted, then the shift cipher is perfectly secret.

(b) What is the largest message space $\mathcal{M}$ for which the mono-alphabetic substitution cipher provides perfect secrecy?

(c) Prove that the Vigenère cipher using (fixed) period t is perfectly secret when used to encrypt messages of length t.

Reconcile this with the attacks shown in the previous chapter.

2.14 在本习题中，我们考察移位密码、单表替换密码和维吉尼亚密码在哪些不同条件下是完美保密的：

(a) 证明如果只加密单个字符，那么移位密码是完美保密的。

(b) 单表替换密码能提供完美保密的最大消息空间 $\mathcal{M}$ 是什么？

(c) 证明使用固定周期 $t$ 的维吉尼亚密码在加密长度为 $t$ 的消息时是完美保密的。

并解释这一结果为何与上一章给出的攻击并不矛盾。

2.15 Give a direct proof that a scheme satisfying Definition 2.6 must have $|\mathcal{K}| \geq |\mathcal{M}|$. Specifically, let $\Pi$ be an arbitrary encryption scheme with $|\mathcal{K}| < |\mathcal{M}|$. Show an $\mathcal{A}$ for which $\Pr\left[\operatorname{PrivK}_{\mathcal{A},\Pi}^{\mathsf{eav}} = 1\right] > \frac{1}{2}$.
Hint: It may be easier to let A be randomized.

2.15 给出一个直接证明：满足定义 2.6 的方案必定有 $|\mathcal{K}| \geq |\mathcal{M}|$。具体地，设 $\Pi$ 是任意一个满足 $|\mathcal{K}| < |\mathcal{M}|$ 的加密方案。给出一个 $\mathcal{A}$ 使得 $\Pr\left[\operatorname{PrivK}_{\mathcal{A},\Pi}^{\mathsf{eav}} = 1\right] > \frac{1}{2}$。
提示：让 A 是随机化的，构造起来可能更容易。

2.16 The following questions concern multiple encryptions of single-character ASCII plaintexts with the one-time pad using the same 8-bit key. You may assume that the plaintexts are either (upper- or lower-case) English letters or the space character.

(a) Say you see the ciphertexts 1011 0111 and 1110 0111. What can you deduce about the plaintext characters these correspond to?

(b) Say you see the three ciphertexts 0110 0110, 0011 0010, and 0010 0011. What can you deduce about the plaintext characters these correspond to?

Hint: Focus on the second bit of the ciphertexts.

2.16 以下问题涉及用同一个 8 比特密钥的一次一密对单字符 ASCII 明文进行多次加密。可以假设明文字符是（大写或小写）英文字母或空格。

(a) 假设你看到密文 1011 0111 和 1110 0111。关于它们对应的明文字符你能推断出什么？

(b) 假设你看到三个密文 0110 0110、0011 0010 和 0010 0011。关于它们对应的明文字符你能推断出什么？

提示：关注密文的第二位。

2.17 Assume we require only that an encryption scheme (Gen, Enc, Dec) with message space $\mathcal{M}$ satisfy the following: For all $m \in \mathcal{M}$, we have $\Pr[\mathsf{Dec}_K(\mathsf{Enc}_K(m)) = m] \geq 2^{-t}$. (This probability is taken over choice of the key as well as any randomness used during encryption/decryption.) Show that perfect secrecy can be achieved with $|\mathcal{K}| < |\mathcal{M}|$ when $t \geq 1$. Prove a lower bound on the size of $\mathcal{K}$ in terms of $t$.

2.17 假设我们只要求消息空间为 $\mathcal{M}$ 的加密方案 (Gen, Enc, Dec) 满足：对所有 $m \in \mathcal{M}$，有 $\Pr[\mathsf{Dec}_K(\mathsf{Enc}_K(m)) = m] \geq 2^{-t}$。（该概率是对密钥的选取以及加密/解密过程中使用的任何随机性而言的。）证明当 $t \geq 1$ 时，可以在 $|\mathcal{K}| < |\mathcal{M}|$ 的情况下达到完美保密，并证明 $|\mathcal{K}|$ 关于 $t$ 的一个下界。

2.18 Let $\varepsilon > 0$ be a constant. Say an encryption scheme is $\varepsilon$-perfectly secret if for every adversary A it holds that

$$
\Pr\left[\mathsf{PrivK}_{\mathcal{A},\Pi}^{\mathsf{eav}}=1\right]\leq\frac{1}{2}+\varepsilon.
$$

(Compare to Definition 2.6.) Consider a variant of the one-time pad where $\mathcal{M} = \{0,1\}^{\ell}$ and the key is chosen uniformly from an arbitrary set $\mathcal{K} \subseteq \{0,1\}^{\ell}$ with $|\mathcal{K}| = (1 - \varepsilon) \cdot 2^{\ell}$; encryption and decryption are otherwise the same.

(a) Prove that this scheme is $\varepsilon$-perfectly secret.

(b) Prove that this scheme is $\left(\frac{\varepsilon}{2(1-\varepsilon)}\right)$-perfectly secret when $\varepsilon \leq 1/2$. (Note that $\frac{\varepsilon}{2(1-\varepsilon)} \leq \varepsilon$ here, so this is an improvement over part (a).)

(c) Prove that any deterministic scheme that is $\varepsilon$-perfectly secret must have $|\mathcal{K}| \geq (1 - 2\varepsilon) \cdot |\mathcal{M}|$. (Note: It is an open question to prove a tight lower bound that also holds for randomized schemes.)

2.18 设 $\varepsilon > 0$ 为常数。称一个加密方案是 $\varepsilon$-完美保密的，如果对每个敌手 A 都有

$$
\Pr\left[\mathsf{PrivK}_{\mathcal{A},\Pi}^{\mathsf{eav}}=1\right]\leq\frac{1}{2}+\varepsilon.
$$

（与定义 2.6 比较。）考虑一次一密的一个变体：$\mathcal{M} = \{0,1\}^{\ell}$，密钥从任意集合 $\mathcal{K} \subseteq \{0,1\}^{\ell}$（其中 $|\mathcal{K}| = (1 - \varepsilon) \cdot 2^{\ell}$）中均匀选取；其余加密与解密方式不变。

(a) 证明该方案是 $\varepsilon$-完美保密的。

(b) 证明当 $\varepsilon \leq 1/2$ 时，该方案是 $\left(\frac{\varepsilon}{2(1-\varepsilon)}\right)$-完美保密的。（注意此处 $\frac{\varepsilon}{2(1-\varepsilon)} \leq \varepsilon$，因此这是对 (a) 的改进。）

(c) 证明任何确定性且 $\varepsilon$-完美保密的方案必有 $|\mathcal{K}| \geq (1 - 2\varepsilon) \cdot |\mathcal{M}|$。（注：证明一个对随机化方案也成立的紧下界是一个开放问题。）

2.19 In this problem we consider definitions of perfect secrecy for the encryption of two messages (using the same key). Here we consider distributions on pairs of messages from the message space $\mathcal{M}$; we let $M_1, M_2$ be random variables denoting the first and second message, respectively. (These random variables are not assumed to be independent.) We generate a (single) key $k$, sample a pair of messages $(m_1, m_2)$ according to the given distribution, and then compute ciphertexts $c_1 \leftarrow \mathsf{Enc}_k(m_1)$ and $c_2 \leftarrow \mathsf{Enc}_k(m_2)$; this induces a distribution on pairs of ciphertexts and we let $C_1, C_2$ be the corresponding random variables.

(a) Say encryption scheme (Gen, Enc, Dec) is perfectly secret for two messages if for all distributions on $\mathcal{M} \times \mathcal{M}$, all $m_1, m_2 \in \mathcal{M}$, and all ciphertexts $c_1, c_2 \in \mathcal{C}$ with $\Pr[C_1 = c_1 \land C_2 = c_2] > 0$:

$$
\begin{aligned}\Pr\left[M_{1}=m_{1}\wedge M_{2}=m_{2}\mid C_{1}=c_{1}\wedge C_{2}=c_{2}\right]\\=\Pr[M_{1}=m_{1}\wedge M_{2}=m_{2}].\end{aligned}
$$

Prove that no encryption scheme can satisfy this definition.

Hint: Take $c_1 = c_2$.

(b) Say encryption scheme (Gen, Enc, Dec) is perfectly secret for two distinct messages if for all distributions on $\mathcal{M} \times \mathcal{M}$ where the first and second messages are guaranteed to be different (i.e., distributions on pairs of distinct messages), all $m_1, m_2 \in \mathcal{M}$, and all $c_1, c_2 \in \mathcal{C}$ with $\Pr[C_1 = c_1 \land C_2 = c_2] > 0$:

$$
\begin{aligned}\Pr[M_{1}=m_{1}\land M_{2}=m_{2}\mid C_{1}=c_{1}\land C_{2}=c_{2}]\\=\Pr[M_{1}=m_{1}\land M_{2}=m_{2}].\end{aligned}
$$

Show an encryption scheme that provably satisfies this definition.

Hint: The encryption scheme you propose need not be efficient, although an efficient solution is possible.

2.19 在本题中我们考虑对两条消息（使用同一密钥）加密的完美保密定义。这里考虑消息空间 $\mathcal{M}$ 上消息对的分布；令 $M_1, M_2$ 分别表示第一条和第二条消息的随机变量（不假设这些随机变量相互独立）。我们生成一个（单个）密钥 $k$，按给定分布采样一对消息 $(m_1, m_2)$，然后计算密文 $c_1 \leftarrow \mathsf{Enc}_k(m_1)$ 与 $c_2 \leftarrow \mathsf{Enc}_k(m_2)$；这在密文对上诱导出一个分布，令 $C_1, C_2$ 为相应的随机变量。

(a) 称加密方案 (Gen, Enc, Dec) 对两条消息完美保密，如果对 $\mathcal{M} \times \mathcal{M}$ 上的所有分布、所有 $m_1, m_2 \in \mathcal{M}$ 以及所有满足 $\Pr[C_1 = c_1 \land C_2 = c_2] > 0$ 的密文 $c_1, c_2 \in \mathcal{C}$：

$$
\begin{aligned}\Pr\left[M_{1}=m_{1}\wedge M_{2}=m_{2}\mid C_{1}=c_{1}\wedge C_{2}=c_{2}\right]\\=\Pr[M_{1}=m_{1}\wedge M_{2}=m_{2}].\end{aligned}
$$

证明没有加密方案能够满足此定义。

提示：取 $c_1 = c_2$。

(b) 称加密方案 (Gen, Enc, Dec) 对两条不同消息完美保密，如果对 $\mathcal{M} \times \mathcal{M}$ 上保证第一条与第二条消息不同的所有分布（即不同消息对的分布）、所有 $m_1, m_2 \in \mathcal{M}$ 以及所有满足 $\Pr[C_1 = c_1 \land C_2 = c_2] > 0$ 的 $c_1, c_2 \in \mathcal{C}$：

$$
\begin{aligned}\Pr[M_{1}=m_{1}\land M_{2}=m_{2}\mid C_{1}=c_{1}\land C_{2}=c_{2}]\\=\Pr[M_{1}=m_{1}\land M_{2}=m_{2}].\end{aligned}
$$

给出一个可证明满足此定义的加密方案。

提示：所提出的加密方案不必高效，尽管也存在高效的解法。
