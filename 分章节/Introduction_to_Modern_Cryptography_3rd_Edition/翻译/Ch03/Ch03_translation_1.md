# Chapter 3: Private-Key Encryption　第三章　私钥加密

In the previous chapter we saw some fundamental limitations of perfect secrecy. In this chapter we begin our study of modern cryptography by introducing the weaker (but sufficient) notion of computational secrecy. We then show how this definition can be used to bypass the impossibility results shown previously for perfect secrecy and, in particular, how a short key (say, 128 bits long) can be used to encrypt many long messages (say, gigabytes in total).

在上一章中，我们看到了完美保密的一些基本局限性。在本章中，我们将通过引入更弱（但足够）的计算保密性（computational secrecy）概念来开始我们对现代密码学的研究。然后，我们将展示如何使用这一定义来绕过之前对完美保密所展示的不可能性结果，特别是如何使用短密钥（比如 128 位）来加密大量长消息（比如总计达数 GB）。

Along the way we will study the fundamental notion of pseudorandomness, which captures the idea that something can "look" completely random even though it is not. This powerful concept underlies much of modern cryptography, and has applications and implications beyond the field as well.

在此过程中，我们将研究伪随机性（pseudorandomness）这一基本概念，它捕捉了某物即使不是完全随机的，也可以“看起来”完全随机的思想。这一强大概念是现代密码学许多内容的基础，并且在密码学领域之外也有应用和影响。

## 3.1 Computational Security　3.1 计算安全性

In Chapter 2 we introduced the notion of perfect secrecy. While perfect secrecy is a worthwhile goal, it is also unnecessarily strong. Perfect secrecy requires that absolutely no information about an encrypted message is leaked, even to an eavesdropper with unlimited computational power. For all practical purposes, however, an encryption scheme would still be considered secure if it leaked information with some tiny probability to eavesdroppers with bounded computational power. For example, a scheme that leaks information with probability at most ${2}^{-60}$ to eavesdroppers investing up to 200 years of computational effort on the fastest available supercomputer (or cluster of computers) would be more than adequate for real-world applications. Computational security definitions take into account computational limits on an attacker, and allow for a small probability that security is violated, in contrast to notions (such as perfect secrecy) that are information-theoretic in nature. Computational security is now the de facto way in which security is defined for almost all cryptographic applications.

在第二章中，我们介绍了完美保密的概念。虽然完美保密是一个有价值的目标，但它也过于强了。完美保密要求即使对拥有无限计算能力的窃听者，也绝不泄露关于加密消息的任何信息。然而，就实际用途而言，如果一个加密方案仅以极小的概率向计算能力有界的窃听者泄露信息，那么它仍然可以被认为是安全的。例如，一个方案以不超过 ${2}^{-60}$ 的概率向投入多达 200 年计算工作量（在最快的超级计算机或计算机集群上）的窃听者泄露信息，这对实际应用来说已经绰绰有余。计算安全性定义考虑了攻击者的计算限制，并允许安全以极小的概率被破坏，这与信息论性质的概念（如完美保密）形成对比。计算安全性现在是几乎所有密码学应用中定义安全性的事实标准。

We stress that although we give up on obtaining perfect secrecy, this does not mean we do away with the rigorous mathematical approach we have been taking so far. Definitions and proofs are still essential; the only difference is that we now consider a weaker (but still meaningful) notion of security.

我们强调，虽然我们放弃追求完美保密，但这并不意味着我们抛弃了迄今为止一直采用的严格数学方法。定义和证明仍然是必不可少的；唯一的区别是我们现在考虑一个更弱（但仍然有意义）的安全性概念。

As discussed, computational security definitions incorporate two relaxations relative to information-theoretic notions of security:

如前所述，相对于信息论的安全性概念，计算安全性定义包含两个放宽条件：

1. Security is only guaranteed against *efficient* adversaries that run for some feasible amount of time. This means that given enough time (or sufficient computational resources) an attacker may be able to violate security. If we can make the resources required to break the scheme larger than those available to any realistic attacker, however, then for all practical purposes the scheme is unbreakable.

   安全性仅针对运行时间为某个可行时长的*高效*敌手得到保证。这意味着给定足够的时间（或足够的计算资源），攻击者可能能够破坏安全。然而，如果我们能使攻破方案所需的资源大于任何现实攻击者可用的资源，那么从实际角度看，该方案是不可攻破的。

2. Adversaries can potentially succeed (i.e., security can potentially fail) with some very small probability. If we can make this probability sufficiently small, we need not worry about it.

   敌手有可能以非常小的概率成功（即安全有可能失效）。如果我们能使这个概率足够小，就无需担心它。

(As we will see, both these relaxations are necessary in order to overcome the limitations of perfect secrecy shown in the last chapter.) To obtain a meaningful theory, we need to precisely define what we mean by the above relaxations. There are two general approaches for doing so: the concrete approach and the asymptotic approach. These are described next.

（正如我们将看到的，这两个放宽条件对于克服上一章所展示的完美保密的局限性都是必要的。）为了获得一个有意义的理论，我们需要精确定义上述放宽条件的含义。有两种通用方法可以做到这一点：具体方法（the concrete approach）和渐近方法（the asymptotic approach）。下面将分别描述。

### 3.1.1 The Concrete Approach　3.1.1 具体方法

The concrete approach to computational security quantifies the security of a cryptographic scheme by explicitly bounding the maximum success probability of a (randomized) adversary running for some specified amount of time or, more precisely, investing some specified amount of computational effort. Thus, a concrete definition of security takes the following form:

计算安全性的具体方法通过明确限定（随机化）敌手在运行指定时间——或更准确地说，投入指定计算量——时的最大成功概率来量化密码方案的安全性。因此，安全性的具体定义采取以下形式：

A scheme is $(t,\varepsilon)$-secure if any adversary running for time at most $t$ succeeds in breaking the scheme with probability at most $\varepsilon$.

一个方案是 $(t,\varepsilon)$-安全的，如果任何运行时间不超过 $t$ 的敌手以最多 $\varepsilon$ 的概率成功攻破该方案。

(Of course, the above serves only as a general template, and for it to make sense we need to define exactly what it means to "break" the scheme in question.) As an example, one might have a scheme with the guarantee that no adversary running for at most 200 years using the fastest available supercomputer can succeed in breaking the scheme with probability better than ${2}^{-60}$. Or, it may be more convenient to measure running time in terms of CPU cycles, and to construct a scheme such that no adversary using at most ${2}^{80}$ cycles can break the scheme with probability better than ${2}^{-60}$.

（当然，上述仅作为一个通用模板，要使其有意义，我们需要精确定义“攻破”所讨论方案的含义。）例如，可以有一个方案保证：没有敌手在使用最快的超级计算机运行最多 200 年后能以优于 ${2}^{-60}$ 的概率成功攻破该方案。或者，更方便的做法是以 CPU 周期来衡量运行时间，并构造一个方案使得没有使用最多 ${2}^{80}$ 个周期的敌手能以优于 ${2}^{-60}$ 的概率攻破方案。

It is instructive to get a feel for the large values of t and the small values of $\varepsilon$ that are typical of modern cryptosystems.

了解现代密码系统中典型的大 $t$ 值和小 $\varepsilon$ 值是很有启发性的。

**Example 3.1**　**示例 3.1**

Modern private-key encryption schemes are generally assumed to give almost optimal security in the following sense: when the key has length $n$—and so the key space has size ${2}^n$—an adversary running for time $t$ (measured in, say, CPU cycles) succeeds in breaking the scheme with probability at most $ct/2^n$ for some fixed constant $c$. (This simply corresponds to a brute-force search of the key space.)

现代私钥加密方案通常被认为在以下意义上提供近乎最优的安全性：当密钥长度为 $n$——因此密钥空间大小为 ${2}^n$——时，运行时间为 $t$（比如以 CPU 周期衡量）的敌手以最多 $ct/2^n$ 的概率成功攻破方案，其中 $c$ 是某个固定常数。（这对应于对密钥空间的穷举搜索。）

Assuming $c = 1$ for simplicity, a key of length $n = 64$ provides adequate security against an adversary using a standard desktop computer. Indeed, on a 4 GHz processor with 16 cores that executes ${4} \times 10^9$ cycles per second per core, ${2}^{64}$ CPU cycles require ${2}^{64}/(4 \times 10^9 \times 16)$ seconds, or about 9 years. (The above numbers are for illustrative purposes only; in practice $c \neq 1$, and several other factors—including the time required for accessing memory—can significantly affect the performance of brute-force attacks.)

为简单起见假定 $c = 1$，长度为 $n = 64$ 的密钥可以提供足够的安全性来对抗使用标准台式计算机的敌手。实际上，在一个每核每秒执行 ${4} \times 10^9$ 个周期的 4 GHz、16 核处理器上，${2}^{64}$ 个 CPU 周期需要 ${2}^{64}/(4 \times 10^9 \times 16)$ 秒，大约 9 年。（以上数字仅为说明目的；在实践中 $c \neq 1$，其他几个因素——包括访问内存所需的时间——会显著影响穷举攻击的性能。）

However, there is no reason to assume that an adversary is limited to a desktop computer, and powerful adversaries are able to carry out computations orders of magnitude faster. Today, the minimum recommended key length is $n = 128$. The difference between ${2}^{64}$ and ${2}^{128}$ is a multiplicative factor of ${2}^{64}$. To get a feeling for how big this is, note that according to physicists' estimates the number of seconds since the Big Bang is on the order of ${2}^{58}$.

然而，没有理由假定敌手仅限于一台台式计算机，强大的敌手能够以快数个数量级的速度执行计算。如今，最小推荐密钥长度为 $n = 128$。${2}^{64}$ 和 ${2}^{128}$ 之间的差异是一个 ${2}^{64}$ 的乘法因子。要感受这个数字有多大，请注意根据物理学家的估计，自大爆炸以来的秒数约为 ${2}^{58}$ 量级。

If the probability that an attacker can successfully recover an encrypted message in one year is at most ${2}^{-60}$, then it is much more likely that the sender and receiver will both be hit by lightning in that time period than that the attacker will recover the message! Something that occurs with probability ${2}^{-60}$ each second is expected to occur roughly once every 10 billion years.

如果一个攻击者在一年内成功恢复加密消息的概率最多为 ${2}^{-60}$，那么在该时间段内发送方和接收方双双被闪电击中的可能性都比攻击者恢复消息的可能性大得多！以概率 ${2}^{-60}$ 每秒发生的事件预计大约每 100 亿年发生一次。

The concrete approach is important in practice, since concrete guarantees are what users of a cryptographic scheme are ultimately interested in. However, precise concrete guarantees are difficult to provide. Furthermore, one must be careful in interpreting concrete-security claims. For example, a claim that no adversary running for 5 years can break a given scheme with probability better than $\varepsilon$ begs the questions: what type of computing power (e.g., desktop PC, supercomputer, network of hundreds of computers) does this assume? Does this take into account expected future advances in computing power (which, by Moore's Law, roughly doubles every 18 months)? Does the estimate assume the use of "off-the-shelf" algorithms, or dedicated hardware optimized for the attack? Furthermore, such a guarantee says little about the success probability of an adversary running for 2 years (other than the fact that it can be at most $\varepsilon$) and says nothing about the success probability of an adversary running for 10 years.

具体方法在实践中很重要，因为具体保证是密码方案用户最终关心的。然而，精确的具体保证难以提供。此外，解释具体安全性声明时必须谨慎。例如，声称没有运行 5 年的敌手能以优于 $\varepsilon$ 的概率攻破给定方案，这引出了以下问题：这假定了何种计算能力（例如，台式 PC、超级计算机、数百台计算机的网络）？是否考虑到了计算能力预期的未来进步（根据摩尔定律，大约每 18 个月翻一番）？该估计是否假定使用“现成”算法，还是针对攻击优化的专用硬件？此外，这样的保证对运行 2 年的敌手的成功概率几乎只字未提（除了最多为 $\varepsilon$ 之外），并且对运行 10 年的敌手的成功概率没有任何说明。

### 3.1.2 The Asymptotic Approach　3.1.2 渐近方法

As partly noted above, there are some technical and theoretical difficulties in using the concrete-security approach. These issues must be dealt with in practice but when describing schemes abstractly (as we do in this book) it is convenient instead to use an asymptotic approach. This approach, rooted in complexity theory, introduces an integer-valued security parameter (denoted by n) that parameterizes both cryptographic schemes as well as all involved parties (i.e., the honest parties as well as the attacker). When honest parties use a scheme (e.g., when they generate a key), they choose some value for the security parameter; for the purposes of this discussion, one can view the security parameter as corresponding to the length of the key. We also view the running time of the adversary, as well as its success probability, as functions of the security parameter rather than as fixed, concrete values. Then:

如上所述，使用具体安全性方法存在一些技术和理论上的困难。在实践中必须处理这些问题，但在抽象地描述方案时（正如本书中所做的那样），使用渐近方法更为方便。这种方法源于复杂性理论，引入了一个整数值的安全参数（记为 $n$），该参数参数化了密码方案以及所有参与方（即诚实方和攻击者）。当诚实方使用方案时（例如，生成密钥时），他们为安全参数选择某个值；就当前讨论而言，可以将安全参数视为对应于密钥的长度。我们还将敌手的运行时间及其成功概率视为安全参数的函数，而不是固定的具体值。于是：

1. We equate "efficient adversaries" with randomized (i.e., probabilistic) algorithms running in time polynomial in n. This means there is some polynomial p such that the adversary runs for time at most $p(n)$ when the security parameter is n. We also require—for real-world efficiency—that honest parties run in polynomial time, although we stress that the adversary may be much more powerful (and run much longer) than the honest parties.

   我们将“高效敌手”等同于运行时间是 $n$ 的多项式的随机化（即概率性）算法。这意味着存在某个多项式 $p$，使得当安全参数为 $n$ 时，敌手的运行时间最多为 $p(n)$。我们还要求——出于实际效率的考虑——诚实方在多项式时间内运行，尽管我们强调敌手可能比诚实方强大得多（并且运行时间长得多）。

2. We equate the notion of "small probabilities of success" with success probabilities smaller than any inverse polynomial in n. (See Definition 3.4.) Such probabilities are called negligible.

   我们将“小的成功概率”的概念等同于小于 $n$ 的任何逆多项式的成功概率。（见定义 3.4。）这样的概率称为可忽略的（negligible）。

Let PPT stand for "probabilistic polynomial-time." A definition of asymptotic security then takes the following general form:

令 PPT 表示“概率多项式时间”（probabilistic polynomial-time）。于是渐近安全性的定义采用以下一般形式：

A scheme is secure if any PPT adversary succeeds in breaking the scheme with at most negligible probability.

一个方案是安全的，如果任何 PPT 敌手最多以可忽略的概率成功攻破该方案。

This notion of security is asymptotic since it depends on a scheme's behavior for sufficiently large values of n. The following example illustrates this.

这种安全性概念是渐近的，因为它依赖于方案在足够大的 n 值下的行为。以下示例说明了这一点。

**Example 3.2**　**示例 3.2**

Say we have a scheme that is asymptotically secure. Then it may be the case that an adversary running for $n^3$ minutes can succeed in "breaking the scheme" with probability ${2}^{40}/{2}^n$ (which is a negligible function of $n$). When $n \leq 40$ this means that an adversary running for ${40}^3$ minutes (about 6 weeks) can break the scheme with probability 1, so such values of $n$ are not very useful. Even for $n = 50$ an adversary running for ${50}^3$ minutes (about 3 months) can break the scheme with probability roughly 1/1000, which may not be acceptable. On the other hand, when $n = 500$ an adversary running for 200 years breaks the scheme only with probability roughly ${2}^{-460}$.

假设我们有一个渐近安全的方案。那么可能出现这样的情况：运行 $n^3$ 分钟的敌手以概率 ${2}^{40}/{2}^n$（这是 $n$ 的一个可忽略函数）成功“攻破方案”。当 $n \leq 40$ 时，这意味着运行 ${40}^3$ 分钟（约 6 周）的敌手可以以概率 1 攻破方案，因此这样的 $n$ 值不是很有用。即使对于 $n = 50$，运行 ${50}^3$ 分钟（约 3 个月）的敌手也能以大约 1/1000 的概率攻破方案，这可能不可接受。另一方面，当 $n = 500$ 时，运行 200 年的敌手仅以大约 ${2}^{-460}$ 的概率攻破方案。

As indicated by the previous example, we can view the security parameter as a mechanism that allows the honest parties to "tune" the security of a scheme to some desired level. (Increasing the security parameter also increases the time required to run the scheme, as well as the length of the key, so the honest parties will want to set the security parameter as small as possible subject to defending against the class of attacks they are concerned about.) Viewing the security parameter as the key length, this corresponds to the fact that the time required for an exhaustive-search attack grows exponentially in the length of the key. The ability to "increase security" by increasing the security parameter has important practical ramifications, since it enables honest parties to defend against increases in computing power. The following example gives a sense of how this might play out in practice.

正如前一示例所示，我们可以将安全参数视为一种允许诚实方将方案安全性“调整”到期望水平的机制。（增加安全参数也会增加运行方案所需的时间以及密钥的长度，因此诚实方希望在防御他们所关心的攻击类型的前提下，将安全参数设置得尽可能小。）将安全参数视为密钥长度，这对应于穷举搜索攻击所需的时间随密钥长度呈指数增长这一事实。通过增加安全参数来“增强安全性”的能力具有重要的实际影响，因为它使诚实方能够防御计算能力的增长。以下示例可以大致说明这种情况在实践中可能如何展开。

**Example 3.3**　**示例 3.3**

Let us see the effect that the availability of faster computers might have on security in practice. Say we have a cryptographic scheme in which the honest parties run for ${10}^6 \cdot n^2$ cycles, and for which an adversary running for ${10}^8 \cdot n^4$ cycles can succeed in "breaking" the scheme with probability at most ${2}^{-n/2}$. (The numbers are intended to make calculations easier, and are not meant to correspond to any existing cryptographic scheme.)

让我们看看更快的计算机的出现可能对实际安全性产生的影响。假设我们有一个密码方案，其中诚实方运行 ${10}^6 \cdot n^2$ 个周期，而运行 ${10}^8 \cdot n^4$ 个周期的敌手最多以 ${2}^{-n/2}$ 的概率成功“攻破”方案。（这些数字旨在使计算更容易，并不对应于任何现有的密码方案。）

Assume all parties are using 2 GHz computers and the honest parties set $n = 80$. Then the honest parties run for ${10}^6 \cdot 6400$ cycles, or 3.2 seconds, and an adversary running for ${10}^8 \cdot (80)^4$ cycles, or roughly 3 weeks, can break the scheme with probability only ${2}^{-40}$.

假设所有方都使用 2 GHz 计算机，诚实方设置 $n = 80$。那么诚实方运行 ${10}^6 \cdot 6400$ 个周期，即 3.2 秒，而运行 ${10}^8 \cdot (80)^4$ 个周期（大约 3 周）的敌手仅以概率 ${2}^{-40}$ 攻破方案。

Say 8 GHz computers become available, and all parties upgrade. Honest parties can increase $n$ to 160 (which requires generating a fresh key) and maintain a running time of 3.2 seconds (i.e., ${10}^6 \cdot 160^2$ cycles at ${8} \cdot 10^9$ cycles/second). In contrast, the adversary now has to run for over 8 million seconds, or more than 13 weeks, to achieve a success probability of ${2}^{-80}$. The effect of a faster computer has been to make the adversary's job harder.

假设 8 GHz 计算机面市，所有方都升级。诚实方可以将 $n$ 增加到 160（这需要生成新密钥）并保持运行时间为 3.2 秒（即，在 ${8} \cdot 10^9$ 周期/秒下运行 ${10}^6 \cdot 160^2$ 个周期）。相比之下，敌手现在需要运行超过 800 万秒，即超过 13 周，才能达到 ${2}^{-80}$ 的成功概率。更快的计算机的效果反而是使敌手的工作更加困难。

Even when using the asymptotic approach it is important to remember that when a cryptosystem is ultimately deployed a concrete security guarantee will be needed. (After all, some value of n must be chosen, and it is important to understand what level of security is being provided.) As the above examples indicate, however, an asymptotic security claim can typically be translated into a concrete security bound for any desired value of n.

即使在使用渐近方法时，重要的是要记住，当密码系统最终部署时，仍需要具体的安全保证。（毕竟，必须选择某个 n 值，了解正在提供何种级别的安全性是重要的。）然而，如上例所示，渐近安全性声明通常可以转化为任何期望 n 值下的具体安全界限。

#### The Asymptotic Approach in Detail　渐近方法详解

We now discuss more formally the notions of "polynomial-time algorithms" and "negligible success probabilities."

现在我们更形式化地讨论“多项式时间算法”和“可忽略的成功概率”的概念。

Efficient algorithms. A function $f$ from the natural numbers to the nonnegative real numbers is polynomially bounded (or simply polynomial) if there is a constant $c$ such that $f(n) < n^c$ for all $n$. An algorithm $A$ runs in polynomial time if there exists a polynomial $p$ such that, for every input $x \in \{0,1\}^*$, the computation of $A(x)$ terminates within at most $p(|x|)$ steps. (Here, $|x|$ denotes the length of the string $x$). As mentioned earlier, we equate efficient adversaries with those whose running time is polynomial in the security parameter $n$. When it is necessary to explicitly indicate this, we provide the security parameter in unary (i.e., the string ${1}^n$ consisting of $n$ ones) as input to an algorithm. An algorithm may take other inputs besides the security parameter—for example, a message to be encrypted—and in that case we allow its running time to be polynomial in the total length of its inputs.

**高效算法。**

如果存在常数 $c$ 使得对于所有 $n$ 有 $f(n) < n^c$，则从自然数到非负实数的函数 $f$ 是多项式有界的（或简称多项式）。如果存在多项式 $p$ 使得对于每个输入 $x \in \{0,1\}^*$，$A(x)$ 的计算在最多 $p(|x|)$ 步内终止，则算法 $A$ 在多项式时间内运行。（这里 $|x|$ 表示串 $x$ 的长度。）如前所述，我们将高效敌手等同于那些运行时间为安全参数 $n$ 的多项式的敌手。当需要明确指示这一点时，我们以一元形式（即由 $n$ 个 1 组成的串 ${1}^n$）向算法提供安全参数。算法可能除了安全参数之外还接收其他输入——例如，要加密的消息——在这种情况下，我们允许其运行时间为输入总长度的多项式。

A technical advantage of working with polynomials is that they obey certain closure properties. In particular, if $p_1, p_2$ are two polynomials, then the function $p(n) = p_1(p_2(n))$ is also polynomial.

使用多项式的一个技术优势是它们满足某些封闭性质。特别地，如果 $p_1, p_2$ 是两个多项式，那么函数 $p(n) = p_1(p_2(n))$ 也是多项式。

By default, we allow all algorithms to be probabilistic (i.e., randomized). Any such algorithm is assumed to have access to a sequence of unbiased, independent random bits. Equivalently, a randomized algorithm is given (in addition to its input) a uniformly distributed random tape of sufficient length whose bits it can use, as needed, throughout its execution.

默认情况下，我们允许所有算法都是概率性的（即随机化的）。任何此类算法都被假定可以访问一系列无偏的独立随机比特。等价地，随机化算法被给予（除了其输入之外）一个长度足够的均匀分布随机带，其比特可以在执行过程中根据需要被使用。

We consider randomized algorithms by default for two reasons. First, randomness is essential to cryptography (e.g., in order to choose random keys and so on) and so honest parties must be probabilistic; given this, it is natural to allow adversaries to be probabilistic as well. Second, randomization is practical and—as far as we know—gives attackers additional power. Since our goal is to model all realistic attacks, we prefer a more liberal definition of efficient computation.

我们默认考虑随机化算法有两个原因。第一，随机性对密码学至关重要（例如，为了选择随机密钥等），因此诚实方必须是概率性的；鉴于此，自然也应允许敌手是概率性的。第二，随机化是实用的，并且——据我们所知——赋予了攻击者额外的能力。由于我们的目标是建模所有现实攻击，我们倾向于采用更宽松的高效计算定义。

Negligible success probability. A negligible function is one that is asymptotically smaller than any inverse polynomial function. Formally:

**可忽略的成功概率。**

可忽略函数是渐近小于任何逆多项式函数的函数。形式化地：

DEFINITION 3.4 A function $f$ from the natural numbers to the nonnegative real numbers is negligible if for every polynomial $p$ there is an $N$ such that for all $n > N$ it holds that $f(n) < \frac{1}{p(n)}$.

定义 3.4 从自然数到非负实数的函数 $f$ 是可忽略的，如果对于每个多项式 $p$，存在一个 $N$ 使得对所有 $n > N$ 都有 $f(n) < \frac{1}{p(n)}$。

The above is equivalently stated as follows: for every polynomial $p$ and all sufficiently large values of $n$ it holds that $f(n) < \frac{1}{p(n)}$. Or, in other words, for all constants $c$ there exists an $N$ such that for all $n > N$ it holds that $f(n) < n^{-c}$. We typically denote an arbitrary negligible function by *negl*.

以上等价地陈述如下：对于每个多项式 $p$ 和所有足够大的 $n$，都有 $f(n) < \frac{1}{p(n)}$。或者换句话说，对于所有常数 $c$，存在一个 $N$ 使得对所有 $n > N$ 都有 $f(n) < n^{-c}$。我们通常用 *negl* 表示任意可忽略函数。

**Example 3.5**　**示例 3.5**

The functions ${2}^{-n}, {2}^{-\sqrt{n}}$, and $n^{-\log n}$ are all negligible. However, they approach zero at very different rates. For example, we can look at the minimum value of n for which each function is smaller than ${1}/{n^5}$:

函数 ${2}^{-n}$、${2}^{-\sqrt{n}}$ 和 $n^{-\log n}$ 都是可忽略的。然而，它们以非常不同的速率趋近于零。例如，我们可以考察每个函数小于 ${1}/{n^5}$ 时的最小 n 值：

1. Solving ${2}^{-n} \lt n^{-5}$ we get $n > 5 \log n$. The smallest integer value of $n > 1$ for which this holds is $n = 23$.

   解 ${2}^{-n} \lt n^{-5}$ 得到 $n > 5 \log n$。满足此条件的最小整数 $n > 1$ 是 $n = 23$。

2. Solving ${2}^{-\sqrt{n}} \lt n^{-5}$ we get $n > 25 \log^{2} n$. The smallest integer value of $n > 1$ for which this holds is $n \approx 3500$.

   解 ${2}^{-\sqrt{n}} \lt n^{-5}$ 得到 $n > 25 \log^{2} n$。满足此条件的最小整数 n > 1 是 $n \approx 3500$。

3. Solving $n^{-\log n} < n^{-5}$ we get $\log n > 5$. The smallest integer value of $n$ for which this holds is $n = 33$.

   解 $n^{-\log n} < n^{-5}$ 得到 $\log n > 5$。满足此条件的最小整数 $n$ 是 $n = 33$。

From the above you may have the impression that $n^{-\log n}$ is smaller than ${2}^{-\sqrt{n}}$. However, this is incorrect; for all $n > 65536$ it holds that ${2}^{-\sqrt{n}} \lt n^{-\log n}$. Nevertheless, this does show that for values of $n$ in the hundreds or thousands, an adversarial success probability of $n^{-\log n}$ is preferable to an adversarial success probability of ${2}^{-\sqrt{n}}$.

从以上你可能会觉得 $n^{-\log n}$ 小于 ${2}^{-\sqrt{n}}$。然而，这是不正确的；对于所有 $n > 65536$，有 ${2}^{-\sqrt{n}} \lt n^{-\log n}$。尽管如此，这确实表明对于数百或数千的 $n$ 值，敌手成功概率为 $n^{-\log n}$ 比敌手成功概率为 ${2}^{-\sqrt{n}}$ 更可取。

A technical advantage of working with negligible success probabilities is that they obey certain closure properties. The following is an easy exercise.

使用可忽略成功概率的一个技术优势是它们满足某些封闭性质。以下是一个简单的练习题。

PROPOSITION 3.6 Let $\mathsf{negl}_1$ and $\mathsf{negl}_2$ be negligible functions. Then,

命题 3.6 设 $\mathsf{negl}_1$ 和 $\mathsf{negl}_2$ 是可忽略函数。那么，

1. The function $\mathsf{negl}_{3}(n) = \mathsf{negl}_{1}(n) + \mathsf{negl}_{2}(n)$ is negligible.

   函数 $\mathsf{negl}_{3}(n) = \mathsf{negl}_{1}(n) + \mathsf{negl}_{2}(n)$ 是可忽略的。

2. For any polynomial $p$, the function $\mathsf{negl}_{4}(n) = p(n) \cdot \mathsf{negl}_{1}(n)$ is negligible.

   对于任何多项式 $p$，函数 $\mathsf{negl}_{4}(n) = p(n) \cdot \mathsf{negl}_{1}(n)$ 是可忽略的。

The second part of the above proposition implies that if a certain event occurs with only negligible probability in some experiment, then the event occurs with negligible probability even if that experiment is repeated polynomially many times. (This relies on the union bound; see Proposition A.7.) For example, the probability that n fair coin flips all come up "heads" is ${2}^{-n}$, which is negligible. This means that even if we repeat the experiment of flipping n coins polynomially many times, the probability that even one of those experiments results in n heads is still negligible.

上述命题的第二部分意味着，如果某个事件在某个实验中仅以可忽略的概率发生，那么即使该实验重复多项式多次，该事件仍然以可忽略的概率发生。（这依赖于联合界（union bound）；见命题 A.7。）例如，$n$ 次公平硬币抛掷全部为“正面”的概率是 ${2}^{-n}$，这是可忽略的。这意味着即使将抛掷 $n$ 枚硬币的实验重复多项式多次，其中任何一个实验产生 $n$ 个正面的概率仍然是可忽略的。

A corollary of the second part of the above proposition is that if a function $g$ is not negligible, then neither is the function $f(n) \overset{\mathrm{def}}{=} g(n)/p(n)$ for any polynomial $p$.

上述命题第二部分的一个推论是，如果函数 $g$ 不是可忽略的，那么对于任何多项式 $p$，函数 $f(n) \overset{\mathrm{def}}{=} g(n)/p(n)$ 也不是可忽略的。

#### Asymptotic Security: A Summary　渐近安全性：总结

Any security definition consists of two components: a definition of what is considered a "break" of the scheme, and a specification of the power of the adversary. The power of the adversary can relate to many issues (e.g., in the case of encryption, whether we assume a ciphertext-only attack or a chosen-plaintext attack). However, when it comes to the computational power of the adversary, we will from now on model the adversary as efficient and thus only consider adversarial strategies that can be implemented in probabilistic polynomial time. (The only exceptions are Section 4.6, where we revisit information-theoretic security, and Chapter 14, where we consider quantum polynomial-time attackers.) Definitions will also be formulated so that a break that occurs with negligible probability is not considered significant. Thus, the general framework of any security definition will be:

任何安全性定义都包含两个组成部分：对什么构成方案“攻破”的定义，以及对敌手能力的说明。敌手的能力可能涉及许多问题（例如，在加密的情况下，我们假定是唯密文攻击还是选择明文攻击）。然而，关于敌手的计算能力，从现在起我们将把敌手建模为高效的，因此只考虑可以在概率多项式时间内实现的敌手策略。（唯一的例外是第 4.6 节，我们在那里重新审视了信息论安全性，以及第 14 章，我们在那里考虑了量子多项式时间攻击者。）定义的表述方式也将确保：以可忽略概率发生的攻破不被视为显著。因此，任何安全性定义的一般框架将是：

A scheme is secure if for every probabilistic polynomial-time adversary A carrying out an attack (of some formally specified type), the probability that A succeeds in the attack (where success is also formally specified) is negligible.

一个方案是安全的，如果对于每个执行（某种形式化指定类型的）攻击的概率多项式时间敌手 $\mathcal{A}$，$\mathcal{A}$ 在攻击中成功（其中成功也是形式化指定的）的概率是可忽略的。

Such a definition is asymptotic because it is possible that for small values of n an adversary can succeed with high probability. In order to see this more clearly, we expand the term "negligible" in the above statement:

这样的定义是渐近的，因为对于小的 n 值，敌手有可能以高概率成功。为了更清楚地看到这一点，我们展开上述陈述中的“可忽略”一词：

A scheme is secure if for every PPT adversary $\mathcal{A}$ carrying out an attack, and every polynomial $p$, there is an integer $N$ such that when $n > N$ the probability that $\mathcal{A}$ succeeds in the attack is less than $\frac{1}{p(n)}$.

一个方案是安全的，如果对于每个执行攻击的 PPT 敌手 $\mathcal{A}$ 和每个多项式 $p$，存在一个整数 $N$，使得当 $n > N$ 时，$\mathcal{A}$ 在攻击中成功的概率小于 $\frac{1}{p(n)}$。

Note that nothing is guaranteed for values $n \leq N$.

注意对于 $n \leq N$ 的值没有任何保证。

#### On the Choices Made in Defining Asymptotic Security　关于定义渐近安全性时所做的选择

In defining the general notion of asymptotic security, we have made two choices: we have identified efficient adversarial strategies with the class of probabilistic polynomial-time algorithms, and have equated small chances of success with negligible probabilities. Both these choices are—to some extent—arbitrary, and one could build a perfectly reasonable theory by defining, say, efficient strategies as those running in time ${2}^{o(n)}$, or small success probabilities as those bounded by ${2}^{-n}$. Nevertheless, we briefly justify the choices we have made (which are the standard ones).

在定义渐近安全性的一般概念时，我们做了两个选择：将高效敌手策略等同于概率多项式时间算法类，并将小的成功概率等同于可忽略概率。这两个选择在某种程度上都是任意的，人们可以通过将高效策略定义为运行时间为 ${2}^{o(n)}$ 的策略，或将小的成功概率定义为受 ${2}^{-n}$ 界定的概率来构建一个完全合理的理论。尽管如此，我们还是简要证明我们所做选择（也是标准选择）的合理性。

Those familiar with complexity theory or algorithms will recognize that the idea of equating efficient computation with (probabilistic) polynomial-time algorithms is not unique to cryptography. One advantage of using (probabilistic) polynomial time as our notion of efficiency is that this frees us from having to specify our model of computation precisely, since the extended Church-Turing thesis states that all "reasonable" models of computation are polynomially equivalent. $^{1}$ Thus, we need not specify whether we use Turing machines, boolean circuits, or random-access machines; we can present algorithms in high-level pseudocode and be confident that if our analysis shows that an algorithm runs in polynomial time, then any reasonable implementation of that algorithm will run in polynomial time.

熟悉复杂性理论或算法的人会认识到，将高效计算等同于（概率）多项式时间算法的想法并非密码学所独有。使用（概率）多项式时间作为我们的效率概念的一个优点是，这使我们不必精确指定我们的计算模型，因为扩展的 Church-Turing 论题指出所有“合理的”计算模型都是多项式等价的。$^{1}$ 因此，我们无需指定是使用图灵机、布尔电路还是随机访问机器；我们可以用高级伪代码呈现算法，并确信如果我们的分析表明算法在多项式时间内运行，那么该算法的任何合理实现都将在多项式时间内运行。

Another advantage of (probabilistic) polynomial-time algorithms is that they satisfy desirable closure properties: in particular, an algorithm that does only polynomial computation and makes polynomially many calls to polynomial-time subroutines will itself run in polynomial time.

（概率）多项式时间算法的另一个优点是它们满足理想的封闭性质：特别地，一个只进行多项式计算并多项式多次调用多项式时间子程序的算法本身也将在多项式时间内运行。

The most important feature of negligible probabilities is the closure property we have already seen in Proposition 3.6(2): a polynomial multiplied by a negligible function is still negligible. This means, in particular, that if a polynomial-time algorithm makes polynomially many calls to some subroutine that "fails" with negligible probability each time it is called, then the probability that any call to that subroutine fails is still negligible.

可忽略概率最重要的特征是我们已经在命题 3.6(2) 中看到的封闭性质：多项式乘以可忽略函数仍然是可忽略的。这特别意味着，如果一个多项式时间算法多项式多次调用某个子程序，而该子程序每次调用时以可忽略概率“失败”，那么对该子程序的任何调用失败的概率仍然是可忽略的。

#### Necessity of the Relaxations　放宽条件的必要性

Computational secrecy introduces two relaxations of perfect secrecy: first, secrecy is guaranteed only against efficient adversaries; second, secrecy may "fail" with small probability. Both these relaxations are essential for achieving practical encryption schemes, and in particular for bypassing the negative results for perfectly secret encryption. We informally discuss why this is the case. Assume we have an encryption scheme where the size of the key space $\mathcal{K}$ is smaller than the size of the message space $\mathcal{M}$. (As shown in the previous chapter, this means the scheme cannot be perfectly secret.) Two attacks apply regardless of how the encryption scheme is constructed:

计算安全性引入了完美保密的两项放宽条件：第一，安全性仅针对高效敌手得到保证；第二，安全性可能以很小的概率“失效”。这两项放宽条件对于实现实用的加密方案都是必不可少的，特别是对于绕过完美保密加密的否定结果。我们非正式地讨论为什么会这样。假设我们有一个加密方案，其中密钥空间 $\mathcal{K}$ 的大小小于消息空间 $\mathcal{M}$ 的大小。（如前一章所示，这意味着该方案不可能是完美保密的。）无论加密方案如何构造，以下两种攻击都适用：

Given a ciphertext $c$, an adversary can decrypt $c$ using all keys $k \in \mathcal{K}$. This gives a list of all the messages to which $c$ can possibly correspond. Since this list cannot contain all of $\mathcal{M}$ (because $|\mathcal{K}| < |\mathcal{M}|$), this attack leaks some information about the message that was encrypted.

给定一个密文 $c$，敌手可以使用所有密钥 $k \in \mathcal{K}$ 解密 $c$。这给出了 $c$ 可能对应的所有消息的列表。由于该列表不能包含 $\mathcal{M}$ 中的所有消息（因为 $|\mathcal{K}| < |\mathcal{M}|$），这种攻击泄露了关于被加密消息的一些信息。

Moreover, say the adversary carries out a known-plaintext attack and learns that ciphertexts $c_1, \ldots, c_\ell$ correspond to the messages $m_1, \ldots, m_\ell$, respectively. The adversary can again try decrypting each of these ciphertexts with all possible keys until it finds a key $k$ for which $\mathsf{Dec}_k(c_i) = m_i$ for all $i$. Later, given a ciphertext $c$ that is the encryption of an unknown message $m$, it is almost surely the case that $\mathsf{Dec}_k(c) = m$.

此外，假设敌手进行已知明文攻击，并得知密文 $c_1, \ldots, c_\ell$ 分别对应于消息 $m_1, \ldots, m_\ell$。敌手可以再次尝试用所有可能的密钥解密每个密文，直到找到一个密钥 $k$，使得对所有 $i$ 有 $\mathsf{Dec}_k(c_i) = m_i$。之后，给定一个未知消息 $m$ 加密所得的密文 $c$，几乎必然有 $\mathsf{Dec}_k(c) = m$。

Brute-force attacks like the above allow an adversary to "succeed" with probability $\approx 1$ in time $\mathcal{O}(|\mathcal{K}|)$.

像上述这样的穷举攻击允许敌手在 $\mathcal{O}(|\mathcal{K}|)$ 时间内以 $\approx 1$ 的概率“成功”。

- Consider again the case where the adversary learns that ciphertexts $c_1, \ldots, c_\ell$ correspond to messages $m_1, \ldots, m_\ell$. The adversary can guess a uniform key $k \in \mathcal{K}$ and check whether $\mathsf{Dec}_k(c_i) = m_i$ for all $i$. If so, then, as above, the attacker can use $k$ to decrypt anything subsequently encrypted by the honest parties.

  再次考虑敌手得知密文 $c_1, \ldots, c_\ell$ 对应于消息 $m_1, \ldots, m_\ell$ 的情况。敌手可以猜测一个均匀密钥 $k \in \mathcal{K}$ 并检查是否对所有 $i$ 有 $\mathsf{Dec}_k(c_i) = m_i$。如果是，那么如上所述，攻击者可以使用 $k$ 解密诚实方随后加密的任何内容。

Here the adversary runs in constant time and "succeeds" with nonzero probability ${1}/{|\mathcal{K}|}$.

此处敌手在常数时间内运行，并以非零概率 ${1}/{|\mathcal{K}|}$ “成功”。

Nevertheless, by setting $|\mathcal{K}|$ large enough we can hope to achieve meaningful secrecy against attackers running in time much less than $|\mathcal{K}|$ (so the attacker does not have sufficient time to carry out a brute-force attack), except possibly with small probability on the order of ${1}/{|\mathcal{K}|}$.

然而，通过将 $|\mathcal{K}|$ 设置得足够大，我们可以希望对运行时间远小于 $|\mathcal{K}|$ 的攻击者（因此攻击者没有足够时间进行穷举攻击）实现有意义的保密性——至多存在 ${1}/{|\mathcal{K}|}$ 量级的小概率例外。

## 3.2 Defining Computationally Secure Encryption　3.2 定义计算安全的加密

Given the background of the previous section, we are ready to present a definition of computational security for private-key encryption. First, we redefine the syntax of private-key encryption; this will be largely the same as the syntax introduced in Chapter 2 except that we now explicitly take into account the security parameter $n$. We also make two other changes: we allow the decryption algorithm to output an error (e.g., in case it is presented with an invalid ciphertext), and let the message space be the set $\{0,1\}^{*}$ of all (finite-length) binary strings by default.

在上一节背景知识的基础上，我们准备给出私钥加密的计算安全性定义。首先，我们重新定义私钥加密的语法；这与第二章引入的语法基本相同，不同之处在于我们现在显式地考虑了安全参数 $n$。我们还做了另外两个改动：我们允许解密算法输出错误（例如，当它遇到无效密文时），并默认将消息空间设为所有（有限长度）二进制串的集合 $\{0,1\}^{*}$。

DEFINITION 3.7 A private-key encryption scheme consists of three probabilistic polynomial-time algorithms (Gen, Enc, Dec) such that:

定义 3.7 一个私钥加密方案由三个概率多项式时间算法 (Gen, Enc, Dec) 组成，满足：

1. The key-generation algorithm Gen takes as input ${1}^n$ (i.e., the security parameter written in unary) and outputs a key $k$; we write $k \leftarrow \mathsf{Gen}(1^n)$ (emphasizing that Gen is a randomized algorithm). We assume without loss of generality that any key $k$ output by $\mathsf{Gen}(1^n)$ satisfies $|k| \geq n$.

   密钥生成算法 Gen 以 ${1}^n$（即一元表示的安全参数）为输入，输出一个密钥 $k$；我们记作 $k \leftarrow \mathsf{Gen}(1^n)$（强调 Gen 是一个随机化算法）。我们不失一般性地假定 $\mathsf{Gen}(1^n)$ 输出的任何密钥 $k$ 满足 $|k| \geq n$。

2. The encryption algorithm Enc takes as input a key k and a plaintext message $m \in \{0,1\}^*$, and outputs a ciphertext c. Since Enc may be randomized, we write this as $c \leftarrow \mathsf{Enc}_k(m)$.

   加密算法 Enc 以密钥 $k$ 和明文消息 $m \in \{0,1\}^*$ 为输入，输出一个密文 $c$。由于 Enc 可能是随机化的，我们记作 $c \leftarrow \mathsf{Enc}_k(m)$。

3. The decryption algorithm Dec takes as input a key k and a ciphertext c, and outputs a message $m \in \{0,1\}^{*}$ or an error. We denote a generic error by the symbol $\bot$.

   解密算法 Dec 以密钥 $k$ 和密文 $c$ 为输入，输出一个消息 $m \in \{0,1\}^{*}$ 或一个错误。我们用符号 $\bot$ 表示一般性错误。

It is required that for every $n$, every key $k$ output by $\mathsf{Gen}(1^n)$, and every $m \in \{0,1\}^*$, it holds that $\mathsf{Dec}_k(\mathsf{Enc}_k(m)) = m$.

要求对于每个 $n$、每个由 $\mathsf{Gen}(1^n)$ 输出的密钥 $k$ 以及每个 $m \in \{0,1\}^*$，都有 $\mathsf{Dec}_k(\mathsf{Enc}_k(m)) = m$。

If (Gen, Enc, Dec) is such that for k output by $\mathsf{Gen}(1^n)$, algorithm $\mathsf{Enc}_k$ is only defined for messages $m \in \{0,1\}^{\ell(n)}$, then we say that (Gen, Enc, Dec) is a fixed-length private-key encryption scheme for messages of length $\ell(n)$.

如果 (Gen, Enc, Dec) 使得对于 $\mathsf{Gen}(1^n)$ 输出的 k，算法 $\mathsf{Enc}_k$ 仅对消息 $m \in \{0,1\}^{\ell(n)}$ 有定义，那么我们称 (Gen, Enc, Dec) 是一个针对长度为 $\ell(n)$ 的消息的定长私钥加密方案。

Almost always, $\mathsf{Gen}(1^n)$ simply outputs a uniform $n$-bit string as the key. When this is the case, we omit $\mathsf{Gen}$ and define a private-key encryption scheme to be a pair of algorithms ( $\mathsf{Enc}, \mathsf{Dec}$). Without significant loss of generality, we assume $\mathsf{Dec}$ is deterministic throughout this book, and so write $m := \mathsf{Dec}_k(c)$.

在绝大多数情况下，$\mathsf{Gen}(1^n)$ 只是简单地输出一个均匀的 $n$ 比特串作为密钥。在这种情况下，我们省略 $\mathsf{Gen}$，将私钥加密方案定义为一对算法 ($\mathsf{Enc}, \mathsf{Dec}$)。在不失一般性的前提下，我们在本书中假定 $\mathsf{Dec}$ 是确定性的，因此写作 $m := \mathsf{Dec}_k(c)$。

The above definition considers stateless schemes, in which each invocation of Enc is independent of all prior invocations (and similarly for Dec). Later in this chapter, we will discuss stateful schemes in which parties may maintain local state that is updated after each invocation of Enc and/or Dec. We assume encryption schemes are stateless (as in the above definition) unless explicitly noted otherwise.

上述定义考虑的是无状态方案，其中 Enc 的每次调用都独立于之前的所有调用（Dec 同理）。在本章后面，我们将讨论有状态方案，其中各方可以维护在 Enc 和/或 Dec 每次调用后更新的本地状态。除非另有明确说明，我们假定加密方案是无状态的（如上述定义所述）。

### 3.2.1 The Basic Definition of Security (EAV-Security)　3.2.1 安全性的基本定义（EAV 安全性）

We begin by presenting the most basic notion of computational security for private-key encryption: security against a ciphertext-only attack where the adversary observes only a single ciphertext or, equivalently, security when a given key is used to encrypt just a single message. We consider stronger definitions of security later.

我们首先介绍私钥加密最基础的计算安全性概念：针对唯密文攻击的安全性，其中敌手仅观察单个密文——等价地，即在给定密钥仅用于加密单条消息时的安全性。我们将在后面考虑更强的安全性定义。

Motivating the definition. As we have already discussed, any definition of security consists of two distinct components: a threat model (i.e., a specification of the assumed power of the adversary) and a security goal (usually specified by describing what constitutes a "break" of the scheme). We begin our definitional treatment by considering the simplest threat model, where there is an eavesdropping adversary who observes the encryption of a single message. This is exactly the threat model we considered in the previous chapter. The only difference here is that, as explained in the previous section, we are now interested only in computationally bounded adversaries that are limited to running in polynomial time.

**定义的动机。**

正如我们已经讨论过的，任何安全性定义都包含两个不同的组成部分：威胁模型（即对假定的敌手能力的说明）和安全目标（通常通过描述什么构成方案的“攻破”来指定）。我们从考虑最简单的威胁模型开始给出安全性定义，其中存在一个观察单条消息加密的窃听敌手。这正是我们在前一章中考虑的威胁模型。这里唯一的区别是，如前一节所述，我们现在只关心计算能力有界、限于多项式时间运行的敌手。

Although we have made two assumptions about the adversary's capabilities (namely, that it eavesdrops on one ciphertext, and that it runs in polynomial time), we make no assumptions whatsoever about the adversary's strategy in trying to decipher the ciphertext it observes. This is crucial for obtaining meaningful notions of security: the definition ensures protection against any computationally bounded eavesdropper, regardless of the algorithm it uses.

虽然我们对敌手的能力做了两个假设（即它窃听一个密文，并且它在多项式时间内运行），但我们不对敌手试图解密它所观察到的密文时所采用的策略做任何假设。这对于获得有意义的安全性概念至关重要：定义确保防御任何计算能力有界的窃听者，无论其使用何种算法。

Correctly defining the security goal for encryption is not trivial, but we have already discussed this issue at length in Section 1.4.1 and in the previous chapter. We therefore just recall that the idea behind the definition is that the adversary should be unable to learn any partial information about the plaintext from the ciphertext. The definition of semantic security (cf. Section 3.2.2) exactly formalizes this notion, and was the first definition of computationally secure encryption to be proposed. Semantic security is complex and difficult to work with. Fortunately, there is an equivalent definition called indistinguishability that is much simpler.

正确定义加密的安全目标并非易事，但我们已经在第 1.4.1 节和前一章中详细讨论了这个问题。因此我们仅回顾，定义背后的思想是敌手应无法从密文中学习到关于明文的任何部分信息。语义安全性（semantic security）的定义（参见 3.2.2 节）精确地形式化了这一概念，并且是第一个被提出的计算安全加密定义。语义安全性复杂且难以处理。幸运的是，存在一个称为不可区分性（indistinguishability）的等价定义，它简单得多。

The definition of indistinguishability is patterned on the alternative definition of perfect secrecy given as Definition 2.6. (This serves as further justification that the definition of indistinguishability is a good one.) Recall that Definition 2.6 considers an experiment $\mathsf{PrivK}_{\mathcal{A},\Pi}^{\mathsf{eav}}$ in which an adversary $\mathcal{A}$ outputs two messages $m_0$ and $m_1$, and is then given an encryption of one of those messages using a randomly generated key. The definition states that a scheme $\Pi$ is secure if no adversary $\mathcal{A}$ can determine which of the messages $m_0, m_1$ was encrypted with probability any different from ${1}/{2}$ (which is the probability that $\mathcal{A}$ is correct if it just makes a random guess).

不可区分性的定义基于定义 2.6 给出的完美保密的替代定义。（这进一步证明了不可区分性定义是一个好定义。）回忆定义 2.6 考虑了一个实验 $\mathsf{PrivK}_{\mathcal{A},\Pi}^{\mathsf{eav}}$，其中敌手 $\mathcal{A}$ 输出两条消息 $m_0$ 和 $m_1$，然后被给予其中一条消息使用随机生成密钥加密的结果。该定义指出，方案 $\Pi$ 是安全的，如果没有敌手 $\mathcal{A}$ 能以任何不同于 ${1}/{2}$ 的概率（即 $\mathcal{A}$ 仅靠随机猜测时的正确概率）确定 $m_0, m_1$ 中哪条消息被加密。

Here, we keep the experiment $\mathsf{PrivK}_{\mathcal{A},\Pi}^{\mathsf{eav}}$ almost exactly the same (except for some technical differences discussed below), but introduce two important modifications in the definition itself:

在这里，我们保持实验 $\mathsf{PrivK}_{\mathcal{A},\Pi}^{\mathsf{eav}}$ 几乎完全相同（除了一些下面讨论的技术性差异），但在定义本身中引入了两个重要修改：

1. We now consider only adversaries running in polynomial time, whereas Definition 2.6 considered even adversaries with unbounded running time.

   我们现在只考虑在多项式时间内运行的敌手，而定义 2.6 甚至考虑运行时间无界的敌手。

2. We now concede that the adversary might determine the encrypted message with probability negligibly better than 1/2.

   我们现在承认敌手可能以仅比 1/2 高一个可忽略量的概率确定被加密的消息。

As discussed extensively in the previous section, the above relaxations constitute the core elements of computational security.

正如前一节广泛讨论的那样，上述放宽条件构成了计算安全性的核心要素。

As for the other differences, the most prominent is that we now parameterize the experiment by a security parameter $n$. The running time of the adversary $\mathcal{A}$, as well as its success probability, are then both viewed as functions of $n$. We write $\mathsf{PrivK}_{\mathcal{A},\Pi}^{\mathsf{eav}}(n)$ to denote the experiment being run with security parameter $n$, and write

至于其他差异，最突出的是我们现在用安全参数 $n$ 对实验进行参数化。敌手 $\mathcal{A}$ 的运行时间及其成功概率都被视为 $n$ 的函数。我们记 $\mathsf{PrivK}_{\mathcal{A},\Pi}^{\mathsf{eav}}(n)$ 表示使用安全参数 $n$ 运行的实验，并记

$$
\Pr[\mathsf{PrivK}_{\mathcal{A},\Pi}^{\mathsf{eav}}(n)=1]\tag{3.1}
$$

to denote the probability that the output of experiment $\mathsf{PrivK}_{\mathcal{A},\Pi}^{\mathsf{eav}}(n)$ is 1. Note that with $\mathcal{A}$, $\Pi$ fixed, the expression in Equation (3.1) is a function of $n$.

表示实验 $\mathsf{PrivK}_{\mathcal{A},\Pi}^{\mathsf{eav}}(n)$ 的输出为 1 的概率。注意在 $\mathcal{A}$、$\Pi$ 固定的情况下，式 (3.1) 中的表达式是 $n$ 的函数。

A second difference is that we now explicitly require the adversary to output two messages $m_0, m_1$ of equal length. (In Definition 2.6 this requirement is implicit if the message space $\mathcal{M}$ only contains messages of some fixed length, as is the case for the one-time pad encryption scheme.) This means that, by default, we do not require a secure encryption scheme to hide the length of the plaintext. We revisit this point at the end of this section; see also Exercises 3.2 and 3.3.

第二个区别是我们现在明确要求敌手输出两条长度相等的消息 $m_0, m_1$。（在定义 2.6 中，如果消息空间 $\mathcal{M}$ 只包含某个固定长度的消息——如一次一密加密方案那样——这一要求是隐含的。）这意味着，默认情况下，我们不要求安全的加密方案隐藏明文的长度。我们将在本节末尾重新讨论这一点；另见习题 3.2 和 3.3。

Indistinguishability in the presence of an eavesdropper. We now give the formal definition, beginning with the experiment outlined above. The experiment is defined for a private-key encryption scheme $\Pi = (\mathsf{Gen}, \mathsf{Enc}, \mathsf{Dec})$, an adversary $\mathcal{A}$, and a value $n$ for the security parameter:

**存在窃听者时的不可区分性。**

我们现在给出形式化定义，从上述概述的实验开始。该实验针对私钥加密方案 $\Pi = (\mathsf{Gen}, \mathsf{Enc}, \mathsf{Dec})$、敌手 $\mathcal{A}$ 和安全参数值 $n$ 定义：

The adversarial indistinguishability experiment PrivK_{A,Π}^{eav}(n):

敌手不可区分性实验 PrivK_{A,Π}^{eav}(n)：

1. The adversary A is given input ${1}^{n}$, and outputs a pair of messages $m_{0}, m_{1}$ with $|m_{0}| = |m_{1}|$.

   敌手 $\mathcal{A}$ 获得输入 ${1}^{n}$，并输出一对消息 $m_{0}, m_{1}$，满足 $|m_{0}| = |m_{1}|$。

2. A key k is generated by running $\mathsf{Gen}(1^n)$, and a uniform bit $b \in \{0,1\}$ is chosen. Ciphertext $c \leftarrow \mathsf{Enc}_k(m_b)$ is computed and given to $\mathcal{A}$. We refer to c as the challenge ciphertext.

   通过运行 $\mathsf{Gen}(1^n)$ 生成密钥 $k$，并选择一个均匀比特 $b \in \{0,1\}$。计算密文 $c \leftarrow \mathsf{Enc}_k(m_b)$ 并交给 $\mathcal{A}$。我们将 $c$ 称为挑战密文。

3. A outputs a bit b'.

   $\mathcal{A}$ 输出一个比特 $b'$。

4. The output of the experiment is defined to be 1 if $b^{\prime} = b$, and 0 otherwise. If $\mathsf{PrivK}_{\mathcal{A},\Pi}^{\mathsf{eav}}(n) = 1$, we say that $\mathcal{A}$ succeeds.

   实验的输出定义为：如果 $b^{\prime} = b$ 则为 1，否则为 0。如果 $\mathsf{PrivK}_{\mathcal{A},\Pi}^{\mathsf{eav}}(n) = 1$，我们说 $\mathcal{A}$ 成功。

There is no limitation on the lengths of $m_0$ and $m_1$, as long as they are the same. (Of course, if $\mathcal{A}$ runs in polynomial time, then $m_0$ and $m_1$ have length polynomial in $n$.) If $\Pi$ is a fixed-length scheme for messages of length $\ell(n)$, the above experiment is modified by requiring $m_0, m_1 \in \{0,1\}^{\ell(n)}$.

对 $m_0$ 和 $m_1$ 的长度没有限制，只要它们相等即可。（当然，如果 $\mathcal{A}$ 在多项式时间内运行，那么 $m_0$ 和 $m_1$ 的长度是 $n$ 的多项式。）如果 $\Pi$ 是针对长度为 $\ell(n)$ 的消息的定长方案，则上述实验修改为要求 $m_0, m_1 \in \{0,1\}^{\ell(n)}$。

The fact that the adversary can only eavesdrop is implicit in the fact that the adversary is given only a (single) ciphertext, and does not have any further interaction with the sender or the receiver. (As we will see later, allowing additional interaction makes the adversary significantly stronger.)

敌手只能窃听这一事实隐含地体现在敌手仅被给予一个（单个）密文，并且与发送方或接收方没有任何进一步交互。（正如我们稍后将看到的，允许额外的交互会使敌手强大得多。）

The definition of indistinguishability states that an encryption scheme is secure if no PPT adversary A succeeds in guessing which message was encrypted in the above experiment with probability significantly better than random guessing (which is correct with probability ${1}/{2}$):

不可区分性的定义指出，一个加密方案是安全的，如果没有 PPT 敌手 $\mathcal{A}$ 能在上述实验中以显著优于随机猜测（其正确概率为 ${1}/{2}$）的概率成功猜出哪条消息被加密：

DEFINITION 3.8 A private-key encryption scheme $\Pi = (\mathrm{Gen}, \mathrm{Enc}, \mathrm{Dec})$ has indistinguishable encryptions in the presence of an eavesdropper, or is EAV-secure, if for all probabilistic polynomial-time adversaries $\mathcal{A}$ there is a negligible function $\mathrm{negl}$ such that, for all $n$,

定义 3.8 私钥加密方案 $\Pi = (\mathrm{Gen}, \mathrm{Enc}, \mathrm{Dec})$ 在窃听者存在的情况下具有不可区分加密（indistinguishable encryptions），或者是 EAV 安全的，如果对于所有概率多项式时间敌手 $\mathcal{A}$，存在一个可忽略函数 $\mathrm{negl}$，使得对所有 $n$ 有

$$
\Pr\left[\mathsf{PrivK}_{\mathcal{A},\Pi}^{\mathsf{eav}}(n)=1\right]\leq\frac{1}{2}+\mathsf{negl}(n).
$$

The probability above is taken over the randomness used by $\mathcal{A}$ and the randomness used in the experiment (for choosing the key and the bit $b$, as well as any randomness used by $\mathsf{Enc}$).

上述概率取遍 $\mathcal{A}$ 使用的随机性以及实验中使用的随机性（用于选择密钥和比特 $b$，以及 $\mathsf{Enc}$ 使用的任何随机性）。

It should be clear that Definition 3.8 is weaker than Definition 2.6, which is equivalent to perfect secrecy. Thus, any perfectly secret encryption scheme is also EAV-secure. Our goal, therefore, is to show that there exist encryption schemes satisfying Definition 3.8 that can circumvent the limitations of perfect secrecy, and in particular for which the key is shorter than the message. (Note that this must be the case if the scheme can handle arbitrary length messages.) That is, we will show schemes that satisfy Definition 3.8 but cannot satisfy Definition 2.6.

应该清楚，定义 3.8 比等价于完美保密的定义 2.6 更弱。因此，任何完美保密的加密方案也是 EAV 安全的。我们的目标是展示存在满足定义 3.8 且能够绕过完美保密局限性的加密方案，特别是密钥比消息短的方案。（注意，如果方案能够处理任意长度的消息，则情况必然如此。）也就是说，我们将展示满足定义 3.8 但不满足定义 2.6 的方案。

An equivalent formulation. Definition 3.8 requires that no PPT adversary can determine which of two messages was encrypted with probability significantly better than 1/2. An equivalent formulation is that every PPT adversary behaves the same whether it observes an encryption of $m_0$ or of $m_1$. Since $\mathcal{A}$ outputs a bit, "behaving the same" means it outputs 1 with almost the same probability in each case. To formalize this, define $\mathsf{PrivK}_{\mathcal{A},\Pi}^{\mathsf{eav}}(n,b)$ as above except that the fixed bit $b \in \{0,1\}$ is used (rather than being chosen at random). Let $\text{out}_{\mathcal{A}}(\mathsf{PrivK}_{\mathcal{A},\Pi}^{\mathsf{eav}}(n,b))$ denote the output bit $b^{\prime}$ of $\mathcal{A}$ in this experiment. The following states that the output distribution of $\mathcal{A}$ is not significantly affected by whether it is running in experiment $\mathsf{PrivK}_{\mathcal{A},\Pi}^{\mathsf{eav}}(n,0)$ or experiment $\mathsf{PrivK}_{\mathcal{A},\Pi}^{\mathsf{eav}}(n,1)$.

**等价表述。**

定义 3.8 要求没有 PPT 敌手能以显著优于 1/2 的概率确定两条消息中哪条被加密。一个等价表述是每个 PPT 敌手在观察到 $m_0$ 的加密或 $m_1$ 的加密时行为相同。由于 $\mathcal{A}$ 输出一个比特，“行为相同”意味着它在每种情况下以几乎相同的概率输出 1。为形式化这一表述，定义 $\mathsf{PrivK}_{\mathcal{A},\Pi}^{\mathsf{eav}}(n,b)$ 与上述相同，只是使用固定的比特 $b \in \{0,1\}$（而不是随机选择）。令 $\text{out}_{\mathcal{A}}(\mathsf{PrivK}_{\mathcal{A},\Pi}^{\mathsf{eav}}(n,b))$ 表示 $\mathcal{A}$ 在此实验中输出的比特 $b^{\prime}$。以下陈述指出 $\mathcal{A}$ 的输出分布不受它是在实验 $\mathsf{PrivK}_{\mathcal{A},\Pi}^{\mathsf{eav}}(n,0)$ 还是实验 $\mathsf{PrivK}_{\mathcal{A},\Pi}^{\mathsf{eav}}(n,1)$ 中运行的显著影响。

DEFINITION 3.9 A private-key encryption scheme $\Pi = (\mathsf{Gen}, \mathsf{Enc}, \mathsf{Dec})$ has indistinguishable encryptions in the presence of an eavesdropper if for all PPT adversaries A there is a negligible function $\mathsf{negl}$ such that

定义 3.9 私钥加密方案 $\Pi = (\mathsf{Gen}, \mathsf{Enc}, \mathsf{Dec})$ 在窃听者存在的情况下具有不可区分加密，如果对于所有 PPT 敌手 $\mathcal{A}$，存在一个可忽略函数 $\mathsf{negl}$，使得

$$
\begin{array}{r l}&{\left|\Pr[\mathsf{out}_{\mathcal{A}}(\mathsf{PrivK}_{\mathcal{A},\Pi}^{\mathsf{eav}}(n,0))=1]-\Pr[\mathsf{out}_{\mathcal{A}}(\mathsf{PrivK}_{\mathcal{A},\Pi}^{\mathsf{eav}}(n,1))=1]\right|\leq\mathsf{negl}(n).}\end{array}
$$

The fact that this is equivalent to Definition 3.8 is left as an exercise.

该定义与定义 3.8 等价这一点的证明留作练习。

#### On Revealing the Plaintext Length　关于泄露明文长度

The default notion of secure encryption does not require the encryption scheme to hide the plaintext length and, in fact, all commonly used encryption schemes reveal the plaintext length (or a close approximation thereof). The main reason for this is that it is impossible to support arbitrary length messages while hiding all information about the plaintext length (cf. Exercise 3.2). In many cases this is inconsequential since the plaintext length is already public or is not sensitive. This is not always the case, however, and sometimes leaking the plaintext length is problematic. As examples:

安全加密的默认概念不要求加密方案隐藏明文长度，事实上，所有常用的加密方案都会泄露明文长度（或其近似值）。其主要原因是不可能在隐藏关于明文长度的所有信息的同时支持任意长度的消息（参见习题 3.2）。在许多情况下这无关紧要，因为明文长度已经是公开的或不敏感。然而，情况并非总是如此，有时泄露明文长度是有问题的。例如：

- Simple numeric/text data: Say the encryption scheme being used reveals the plaintext length exactly. Then encrypted salary information would reveal whether someone makes a 5-figure or a 6-figure salary. Similarly, encryption of "yes"/"no" responses would leak the answer exactly.

  简单的数字/文本数据：假设所使用的加密方案精确地泄露明文长度。那么加密的薪资信息将揭示某人赚取 5 位数还是 6 位数的薪水。类似地，对“是”/“否”回答的加密将精确泄露答案。

- Auto-suggestions: Websites often include an "auto-complete" or "auto-suggestion" functionality by which the website suggests a list of potential words or phrases based on partial information the user has already typed. The size of this list can reveal information about the letters the user has typed so far. (For example, the number of auto-completions returned for "th" is far greater than the number for "zo.")

  自动建议：网站通常包含“自动补全”或“自动建议”功能，网站根据用户已输入的部分信息建议潜在单词或短语的列表。该列表的大小可以揭示用户到目前为止已输入的字母的信息。（例如，为"th"返回的自动补全数量远大于为"zo"返回的数量。）

- Database searches: Consider a user querying a database for all records matching some search term. The number of records returned can reveal a lot of information about what the user was searching for. This can be particularly damaging if the user is searching for medical information and the query reveals information about a disease the user has.

  数据库搜索：考虑用户查询数据库以获取匹配某个搜索词的所有记录。返回的记录数量可以揭示大量关于用户正在搜索的内容的信息。如果用户正在搜索医疗信息，并且查询揭示了用户所患疾病的信息，这可能特别有害。

- Compressed data: If the plaintext is compressed before being encrypted, then information about the plaintext might be revealed even if only fixed-length plaintext is being encrypted. For example, a short compressed plaintext would indicate that the original (uncompressed) plaintext has a lot of redundancy. If an adversary can control a portion of what gets encrypted, this vulnerability can enable an adversary to learn additional information about the rest of the plaintext; it has been shown possible to use an attack of exactly this sort (called the CRIME attack) to reveal secret session cookies from encrypted HTTPS traffic.

  压缩数据：如果明文在加密前被压缩，那么即使只加密定长明文，关于明文的信息也可能被泄露。例如，短的压缩明文表明原始（未压缩）明文具有大量冗余。如果敌手可以控制被加密内容的一部分，这种漏洞可以使敌手学习关于明文其余部分的额外信息；已经证明可以使用这类攻击（称为 CRIME 攻击）从加密的 HTTPS 流量中泄露秘密会话 cookie。

When using encryption one should determine whether leaking the plaintext length is a concern and, if so, take steps to mitigate or prevent such leakage by padding all messages to some pre-determined length before encrypting them.

在使用加密时，应确定泄露明文长度是否值得关注，如果是，则应采取措施，通过在加密之前将所有消息填充到某个预定长度，来减轻或防止此类泄露。

### 3.2.2 \*Semantic Security　\*语义安全性

We motivated the definition of secure encryption by saying that it implies the inability of an adversary to learn any partial information about the plaintext from the ciphertext. At first glance, however, Definition 3.8 looks very different. As we have mentioned, though, that definition is equivalent to a definition called semantic security that formalizes exactly the notion we want.

我们在介绍安全加密的定义时曾说过，它意味着敌手无法从密文中学习到关于明文的任何部分信息。然而，乍看之下，定义 3.8 看起来非常不同。但正如我们提到过的，该定义等价于称为语义安全性（semantic security）的定义，后者精确地形式化了我们想要的概念。

We build up to that definition by first introducing two weaker notions and showing that they are implied by EAV-security.

我们首先引入两个较弱的概念并展示它们可由 EAV 安全性蕴含，从而逐步构建出该定义。

We begin by showing that EAV-security implies that ciphertexts leak no information about individual bits of the plaintext. Formally, we show that if an EAV-secure encryption scheme (Enc, Dec) (recall that if Gen is omitted, the key is a uniform n-bit string) is used to encrypt a uniform message $m \in \{0,1\}^{\ell}$, then for any i it is infeasible for an attacker given the ciphertext to guess the ith bit of m (here denoted by $m^i$) with probability much better than ${1}/{2}$.

我们首先展示 EAV 安全性意味着密文不会泄露关于明文单个比特的信息。形式化地，我们证明如果使用 EAV 安全的加密方案 $(\mathsf{Enc}, \mathsf{Dec})$（回想如果省略 Gen，密钥是均匀的 $n$ 比特串）来加密均匀消息 $m \in \{0,1\}^{\ell}$，那么对于任何 $i$，给定密文的攻击者无法以远优于 ${1}/{2}$ 的概率猜测 $m$ 的第 $i$ 个比特（此处记为 $m^i$）。

THEOREM 3.10 Let $\Pi = (\mathsf{Enc}, \mathsf{Dec})$ be a fixed-length private-key encryption scheme for messages of length $\ell$ that is EAV-secure. Then for all PPT adversaries $\mathcal{A}$ and $i \in \{1, \ldots, \ell\}$, there is a negligible function $\mathsf{negl}$ such that

定理 3.10 设 $\Pi = (\mathsf{Enc}, \mathsf{Dec})$ 是一个针对长度为 $\ell$ 的消息的定长私钥加密方案，且是 EAV 安全的。那么对于所有 PPT 敌手 $\mathcal{A}$ 和 $i \in \{1, \ldots, \ell\}$，存在一个可忽略函数 $\mathsf{negl}$，使得

$$
\Pr\left[\mathcal{A}(1^{n},\mathsf{Enc}_{k}(m))=m^{i}\right]\leq\frac{1}{2}+\mathsf{negl}(n)\tag{3.2}
$$

where the probability is taken over uniform $m \in \{0,1\}^{\ell}$ and $k \in \{0,1\}^{n}$, the randomness of $\mathcal{A}$, and the randomness of $\mathsf{Enc}$.

其中概率取遍均匀的 $m \in \{0,1\}^{\ell}$ 和 $k \in \{0,1\}^{n}$、$\mathcal{A}$ 的随机性以及 $\mathsf{Enc}$ 的随机性。

PROOF The idea behind the proof of this theorem is that if it were possible to determine the $i$th bit of $m$ from $\mathsf{Enc}_k(m)$, then it would also be possible to distinguish between encryptions of messages $m_0$ and $m_1$ whose $i$th bits differ. We formalize this via a proof by reduction, in which we show how to use any efficient adversary $\mathcal{A}$ to construct an efficient adversary $\mathcal{A}^{\prime}$ such that if $\mathcal{A}$ violates Equation (3.2), then $\mathcal{A}^{\prime}$ violates EAV-security of $\Pi$. (See Section 3.3.2 for more discussion of proofs by reduction.) Since $\Pi$ is EAV-secure, this implies that no such $\mathcal{A}$ can exist.

证明 该定理证明背后的思想是，如果可能从 $\mathsf{Enc}_k(m)$ 确定 $m$ 的第 $i$ 个比特，那么也就可能区分第 $i$ 个比特不同的消息 $m_0$ 和 $m_1$ 的加密。我们通过归约证明来形式化这一点，其中我们展示如何使用任何高效敌手 $\mathcal{A}$ 构造一个高效敌手 $\mathcal{A}^{\prime}$，使得如果 $\mathcal{A}$ 违反式 (3.2)，那么 $\mathcal{A}^{\prime}$ 违反 $\Pi$ 的 EAV 安全性。（关于归约证明的更多讨论见 3.3.2 节。）由于 $\Pi$ 是 EAV 安全的，这意味着不存在这样的 $\mathcal{A}$。

Fix an arbitrary PPT adversary $\mathcal{A}$ and $i \in \{1, \ldots, \ell\}$. Let $I_0 \subset \{0,1\}^{\ell}$ be the set of all strings whose $i$th bit is 0, and let $I_1 \subset \{0,1\}^{\ell}$ be the set of all strings whose $i$th bit is 1. We have

固定任意 PPT 敌手 $\mathcal{A}$ 和 $i \in \{1, \ldots, \ell\}$。令 $I_0 \subset \{0,1\}^{\ell}$ 是所有第 $i$ 个比特为 0 的串的集合，令 $I_1 \subset \{0,1\}^{\ell}$ 是所有第 $i$ 个比特为 1 的串的集合。我们有

$$
\begin{aligned}&\Pr\left[\mathcal{A}(1^{n},\mathsf{Enc}_{k}(m))=m^{i}\right]\\ &=\frac{1}{2}\cdot\Pr_{m_{0}\leftarrow I_{0}}\left[\mathcal{A}(1^{n},\mathsf{Enc}_{k}(m_{0}))=0\right]+\frac{1}{2}\cdot\Pr_{m_{1}\leftarrow I_{1}}\left[\mathcal{A}(1^{n},\mathsf{Enc}_{k}(m_{1}))=1\right].\\ \end{aligned}
$$

Construct the following eavesdropping adversary $A^{\prime}$:

构造以下窃听敌手 $A^{\prime}$：

Adversary $A^{\prime}(1^n)$:

敌手 $A^{\prime}(1^n)$：

1. Choose uniform $m_0 \in I_0$ and $m_1 \in I_1$. Output $m_0, m_1$.

   选择均匀的 $m_0 \in I_0$ 和 $m_1 \in I_1$。输出 $m_0, m_1$。

2. Upon observing a ciphertext $c$, invoke $\mathcal{A}(1^n, c)$. If $\mathcal{A}$ outputs 0, output $b^{\prime} = 0$; otherwise, output $b^{\prime} = 1$.

   观察到密文 $c$ 后，调用 $\mathcal{A}(1^n, c)$。如果 $\mathcal{A}$ 输出 0，则输出 $b^{\prime} = 0$；否则，输出 $b^{\prime} = 1$。

Note that $A^{\prime}$ runs in polynomial time since A does.

注意 $A^{\prime}$ 在多项式时间内运行，因为 A 也是如此。

By the definition of experiment $\mathsf{PrivK}_{\mathcal{A}^{\prime},\Pi}^{\mathsf{eav}}(n)$, we have that $\mathcal{A}^{\prime}$ succeeds if and only if $\mathcal{A}$ outputs $b$ upon receiving $\mathsf{Enc}_k(m_b)$. So

根据实验 $\mathsf{PrivK}_{\mathcal{A}^{\prime},\Pi}^{\mathsf{eav}}(n)$ 的定义，$\mathcal{A}^{\prime}$ 成功当且仅当 $\mathcal{A}$ 在接收到 $\mathsf{Enc}_k(m_b)$ 时输出 $b$。所以

$$
\begin{aligned}&\Pr\left[\mathsf{PrivK}_{\mathcal{A}^{\prime},\Pi}^{\mathsf{eav}}(n)=1\right]\\ &=\Pr\left[\mathcal{A}(1^{n},\mathsf{Enc}_{k}(m_{b}))=b\right]\\ &=\frac{1}{2}\cdot\Pr_{m_{0}\leftarrow I_{0}}\left[\mathcal{A}(1^{n},\mathsf{Enc}_{k}(m_{0}))=0\right]+\frac{1}{2}\cdot\Pr_{m_{1}\leftarrow I_{1}}\left[\mathcal{A}(1^{n},\mathsf{Enc}_{k}(m_{1}))=1\right]\\ &=\Pr\left[\mathcal{A}(1^{n},\mathsf{Enc}_{k}(m))=m^{i}\right].\\ \end{aligned}
$$

Since (Enc, Dec) is EAV-secure, there is a negligible function $\mathsf{negl}$ such that $\Pr\left[\mathsf{PrivK}_{\mathcal{A}^{\prime},\Pi}^{\mathsf{eav}}(n)=1\right]\leq\frac{1}{2}+\mathsf{negl}(n)$. We conclude that

由于 (Enc, Dec) 是 EAV 安全的，存在可忽略函数 $\mathsf{negl}$ 使得 $\Pr\left[\mathsf{PrivK}_{\mathcal{A}^{\prime},\Pi}^{\mathsf{eav}}(n)=1\right]\leq\frac{1}{2}+\mathsf{negl}(n)$。我们得出结论

$$
\Pr\left[\mathcal{A}(1^{n},\mathsf{Enc}_{k}(m))=m^{i}\right]\leq\frac{1}{2}+\mathsf{negl}(n),
$$

completing the proof.

证明完成。

We next argue that EAV-security implies that no PPT adversary can learn any function $f$ of the plaintext $m$ from the ciphertext, regardless of the distribution $\mathcal{D}$ of $m$. This requirement is not trivial to define formally, because it needs to distinguish information that the attacker knows about the message due to $\mathcal{D}$ from information the attacker learns about the message from the ciphertext. (For example, if $\mathcal{D}$ is only over messages for which $f$ evaluates to 1, then it is easy for an attacker to determine $f(m)$. But in this case the attacker is not learning $f(m)$ from the ciphertext.) This is taken into account in the definition by requiring that if there exists an adversary who, with some probability, correctly computes $f(m)$ when given $\mathsf{Enc}_k(m)$, then there exists an adversary that can correctly compute $f(m)$ with almost the same probability without being given the ciphertext at all (and knowing only the distribution $\mathcal{D}$ of $m$).

我们接下来论证 EAV 安全性意味着没有 PPT 敌手能从密文中学习明文的任何函数 $f$，无论 $m$ 的分布 $\mathcal{D}$ 如何。这个要求不容易形式化地定义，因为它需要区分攻击者由于 $\mathcal{D}$ 而知道的关于消息的信息与攻击者从密文中学习到的关于消息的信息。（例如，如果 $\mathcal{D}$ 仅限于那些 $f$ 求值为 1 的消息，那么攻击者很容易确定 $f(m)$。但在这种情况下，攻击者并不是从密文中学习 $f(m)$。）这一点在定义中通过以下要求得到考虑：如果存在一个敌手在给定 $\mathsf{Enc}_k(m)$ 时以某种概率正确计算 $f(m)$，那么存在一个敌手在完全未给定密文的情况下（仅知道 $m$ 的分布 $\mathcal{D}$）能够以几乎相同的概率正确计算 $f(m)$。

THEOREM 3.11 Let (Enc, Dec) be a fixed-length private-key encryption scheme for messages of length $\ell$ that is EAV-secure. Then for any PPT algorithm $\mathcal{A}$ there is a PPT algorithm $\mathcal{A}^{\prime}$ such that for any distribution $\mathcal{D}$ over $\{0,1\}^{\ell}$ and any function $f: \{0,1\}^{\ell} \to \{0,1\}$, there is a negligible function $\mathsf{negl}$ such that:

定理 3.11 设 (Enc, Dec) 是一个针对长度为 $\ell$ 的消息的定长私钥加密方案，且是 EAV 安全的。那么对于任何 PPT 算法 $\mathcal{A}$，存在一个 PPT 算法 $\mathcal{A}^{\prime}$，使得对于 $\{0,1\}^{\ell}$ 上的任何分布 $\mathcal{D}$ 和任何函数 $f: \{0,1\}^{\ell} \to \{0,1\}$，存在一个可忽略函数 $\mathsf{negl}$，满足：

$$
\begin{array}{r}{\left|\Pr\left[\mathcal{A}(1^{n},\mathsf{Enc}_{k}(m))=f(m)\right]-\Pr\left[\mathcal{A}^{\prime}(1^{n})=f(m)\right]\right|\leq\mathsf{negl}(n),}\end{array}
$$

where the first probability is taken over choice of $m$ according to $\mathcal{D}$, uniform choice of $k \in \{0,1\}^{n}$, and the randomness of $\mathcal{A}$ and $\mathsf{Enc}$, and the second probability is taken over choice of $m$ according to $\mathcal{D}$ and the randomness of $\mathcal{A}^{\prime}$.

其中第一个概率取遍根据 $\mathcal{D}$ 选择的 $m$、均匀选择的 $k \in \{0,1\}^{n}$ 以及 $\mathcal{A}$ 和 $\mathsf{Enc}$ 的随机性，第二个概率取遍根据 $\mathcal{D}$ 选择的 $m$ 以及 $\mathcal{A}^{\prime}$ 的随机性。

PROOF (Sketch) The fact that (Enc, Dec) is EAV-secure means that, for any $\mathcal{D}$, no PPT adversary can distinguish between $\mathsf{Enc}_k(m)$ for $m$ chosen according to $\mathcal{D}$, and $\mathsf{Enc}_k(1^\ell)$ (i.e., an encryption of the all-1 string). (We leave a proof of this claim to the reader.) Consider now the probability that $\mathcal{A}$ successfully computes $f(m)$ given $\mathsf{Enc}_k(m)$. We claim that $\mathcal{A}$ should successfully compute $f(m)$ given $\mathsf{Enc}_k(1^\ell)$ with almost the same probability; otherwise, $\mathcal{A}$ could be used to distinguish between $\mathsf{Enc}_k(m)$ and $\mathsf{Enc}_{k}(1^\ell)$. The distinguisher is easily constructed: choose $m$ according to $\mathcal{D}$, and output $m_0 = m$, $m_1 = 1^\ell$. When given a ciphertext $c$ that is an encryption of either $m_0$ or $m_1$, invoke $\mathcal{A}(1^n, c)$ and output 0 if and only if $\mathcal{A}$ outputs $f(m)$. If $\mathcal{A}$ outputs $f(m)$ when given an encryption of $m$ with probability that is significantly different from the probability that it outputs $f(m)$ when given an encryption of ${1}^\ell$, then the described distinguisher violates Definition 3.9.

证明（概要） (Enc, Dec) 是 EAV 安全的这一事实意味着，对于任何 $\mathcal{D}$，没有 PPT 敌手能够区分根据 $\mathcal{D}$ 选择的 $m$ 的 $\mathsf{Enc}_k(m)$ 和 $\mathsf{Enc}_k(1^\ell)$（即全 1 串的加密）。（我们将此论断的证明留给读者。）现在考虑 $\mathcal{A}$ 在给定 $\mathsf{Enc}_k(m)$ 时成功计算 $f(m)$ 的概率。我们断言 $\mathcal{A}$ 在给定 $\mathsf{Enc}_k(1^\ell)$ 时应该以几乎相同的概率成功计算 $f(m)$；否则，$\mathcal{A}$ 可被用于区分 $\mathsf{Enc}_k(m)$ 和 $\mathsf{Enc}_{k}(1^\ell)$。该区分器很容易构造：根据 $\mathcal{D}$ 选择 $m$，输出 $m_0 = m$，$m_1 = 1^\ell$。当给定一个加密 $m_0$ 或 $m_1$ 的密文 $c$ 时，调用 $\mathcal{A}(1^n, c)$，当且仅当 $\mathcal{A}$ 输出 $f(m)$ 时输出 0。如果 $\mathcal{A}$ 在给定 $m$ 的加密时输出 $f(m)$ 的概率与在给定 ${1}^\ell$ 的加密时输出 $f(m)$ 的概率显著不同，那么所描述的区分器违反了定义 3.9。

The above suggests the following algorithm $\mathcal{A}^{\prime}$ that does not receive an encryption of $m$, yet computes $f(m)$ almost as well as $\mathcal{A}$ does: $\mathcal{A}^{\prime}(1^n)$ chooses a uniform key $k \in \{0,1\}^n$, invokes $\mathcal{A}$ on $c \leftarrow \mathsf{Enc}_k(1^\ell)$, and outputs whatever $\mathcal{A}$ does. By the above, we have that $\mathcal{A}$ outputs $f(m)$ when run as a subroutine by $\mathcal{A}^{\prime}$ with almost the same probability as when it receives $\mathsf{Enc}_k(m)$. Thus, $\mathcal{A}^{\prime}$ fulfills the property required by the theorem.

上述内容提出了以下算法 $\mathcal{A}^{\prime}$，它不接收 $m$ 的加密，却能几乎像 $\mathcal{A}$ 一样好地计算 $f(m)$：$\mathcal{A}^{\prime}(1^n)$ 选择均匀密钥 $k \in \{0,1\}^n$，在 $c \leftarrow \mathsf{Enc}_k(1^\ell)$ 上调用 $\mathcal{A}$，并输出 $\mathcal{A}$ 的输出。由上述内容，当 $\mathcal{A}$ 被 $\mathcal{A}^{\prime}$ 作为子程序运行时，它输出 $f(m)$ 的概率几乎与接收 $\mathsf{Enc}_k(m)$ 时相同。因此，$\mathcal{A}^{\prime}$ 满足定理所要求的性质。

Semantic security. The full definition of semantic security guarantees considerably more than what is considered in Theorem 3.11. The definition allows arbitrary (efficiently sampleable) distributions over messages, generated by some polynomial-time sampling algorithm Samp. The definition also takes into account arbitrary "external" information $h(m)$ about the message m that may be available to the adversary via other means (e.g., because the message is used for some other purpose as well). It also allows messages of varying lengths, although—as discussed at the end of the previous section—it assumes the message length is revealed.

**语义安全性。**

语义安全性的完整定义所保证的远多于定理 3.11 中所考虑的内容。该定义允许消息上的任意（可高效采样的）分布，由某个多项式时间采样算法 $\mathsf{Samp}$ 生成。该定义还考虑了敌手可能通过其他方式获得的关于消息 $m$ 的任意“外部”信息 $h(m)$（例如，因为消息也用于某些其他目的）。它还允许可变长度的消息，尽管——如上一节末尾所讨论的——它假定消息长度被泄露。

DEFINITION 3.12 A private-key encryption scheme (Enc, Dec) is semantically secure in the presence of an eavesdropper if for every PPT algorithm A there exists a PPT algorithm A' such that for any PPT algorithm Samp and polynomial-time computable functions f and h, the following is negligible:

定义 3.12 私钥加密方案 $(\mathsf{Enc}, \mathsf{Dec})$ 在窃听者存在的情况下是语义安全的，如果对于每个 PPT 算法 $\mathcal{A}$ 存在一个 PPT 算法 $\mathcal{A}'$，使得对于任何 PPT 算法 $\mathsf{Samp}$ 和多项式时间可计算函数 $f$ 和 $h$，以下表达式是可忽略的：

$$
\left|\Pr[\mathcal{A}(1^n,\operatorname{Enc}_k(m),h(m))=f(m)]-\Pr[\mathcal{A}^{\prime}(1^n,|m|,h(m))=f(m)]\right|,
$$

where the first probability is taken over $m$ output by $\mathsf{Samp}(1^n)$, uniform choice of $k \in \{0,1\}^n$, and the randomness of $\mathsf{Enc}$ and $\mathcal{A}$, and the second probability is taken over $m$ output by $\mathsf{Samp}(1^n)$ and the randomness of $\mathcal{A}^{\prime}$.

其中第一个概率取遍由 $\mathsf{Samp}(1^n)$ 输出的 $m$、均匀选择的 $k \in \{0,1\}^n$ 以及 $\mathsf{Enc}$ 和 $\mathcal{A}$ 的随机性，第二个概率取遍由 $\mathsf{Samp}(1^n)$ 输出的 $m$ 以及 $\mathcal{A}^{\prime}$ 的随机性。

The adversary $\mathcal{A}$ is given the ciphertext $\mathsf{Enc}_{k}(m)$ as well as the external information $h(m)$, and attempts to guess the value of $f(m)$. Algorithm $\mathcal{A}^{\prime}$ also attempts to guess the value of $f(m)$, but is given only the length of $m$ and $h(m)$. The security requirement states that $\mathcal{A}^{\prime}$'s probability of correctly guessing $f(m)$ is about the same as that of $\mathcal{A}$. Intuitively, then, this means that the ciphertext $\mathsf{Enc}_k(m)$ does not reveal any information about $f(m)$ except for $|m|$.

敌手 $\mathcal{A}$ 被给予密文 $\mathsf{Enc}_{k}(m)$ 以及外部信息 $h(m)$，并试图猜测 $f(m)$ 的值。算法 $\mathcal{A}^{\prime}$ 也试图猜测 $f(m)$ 的值，但只被给予 $m$ 的长度和 $h(m)$。安全性要求指出 $\mathcal{A}^{\prime}$ 正确猜测 $f(m)$ 的概率与 $\mathcal{A}$ 大致相同。因此，直觉上这意味着密文 $\mathsf{Enc}_k(m)$ 除了 $|m|$ 之外不泄露关于 $f(m)$ 的任何信息。

Definition 3.12 is a very strong and convincing formulation of the security guarantees that should be provided by an encryption scheme. Definition 3.8 is much easier to work with. Fortunately, the definitions are equivalent:

定义 3.12 是一个非常强且有说服力的加密方案应提供的安全保证的表述。定义 3.8 使用起来要容易得多。幸运的是，这两个定义是等价的：

THEOREM 3.13 A private-key encryption scheme has indistinguishable encryptions in the presence of an eavesdropper (i.e., is EAV-secure) if and only if it is semantically secure in the presence of an eavesdropper.

定理 3.13 一个私钥加密方案在窃听者存在的情况下具有不可区分加密（即 EAV 安全的）当且仅当它在窃听者存在的情况下是语义安全的。

Looking ahead, a similar equivalence to a "semantic security"-based definition is known for all the definitions we present in this chapter and Chapter 5. We can therefore use a simpler notion as our working definition, while being assured that it implies the strong guarantees of semantic security.

展望后续，对于本章和第 5 章中给出的所有定义，都存在类似的、与基于“语义安全性”的定义之间的等价性。因此，我们可以使用更简单的概念作为工作定义，同时确信它蕴含了语义安全性的强保证。
