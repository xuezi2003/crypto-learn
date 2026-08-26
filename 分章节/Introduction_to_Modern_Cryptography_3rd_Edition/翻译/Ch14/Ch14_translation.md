# Chapter 14: *Post-Quantum Cryptography*　第 14 章　后量子密码学

So far in this book (cf. Section 3.1.2), we have equated the notion of “efficient adversaries” with adversarial algorithms running in (probabilistic) polynomial-time on a classical computer. Thus, when evaluating the security of our schemes we only considered efficient classical attacks. We did not, however, consider the potential impact of quantum computers—that is, computers that rely in an essential way on the principles of quantum mechanics. As we will see here, quantum algorithms can in some cases be faster than classical algorithms—possibly much faster—and thus quantum computers can have a dramatic impact on the security of cryptosystems.

在本书此前的内容中（参见 3.1.2 节），我们一直把“高效敌手”等同于在经典计算机上以（概率）多项式时间运行的敌手算法。因此，在评估方案的安全性时，我们只考虑了高效的经典攻击。然而，我们并未考虑量子计算机——即以本质方式依赖量子力学原理的计算机——可能带来的影响。正如本章将看到的，量子算法在某些情况下可以比经典算法更快——甚至可能快得多——因此量子计算机能够对密码系统的安全性产生巨大的影响。

While the theoretical impact of quantum computing on cryptography has been recognized since the mid-1990s, its potential impact in practice is currently unclear. As of this writing, no large-scale, general-purpose quantum computer has been built, and the timeframe for developing such a computer is uncertain due to the numerous engineering difficulties involved. Even if such computers are one day built, the true cost in time or money of executing quantum algorithms on those computers (as distinguished from the theoretical analysis of the number of steps those algorithms take in theory) is not well understood. Nevertheless, the current consensus is that there is a strong chance that well-funded attackers (e.g., government agencies) will be able to build quantum computers capable of attacking currently deployed cryptosystems in the next 10-15 years. Assuming this to be the case, we cannot wait 10-15 years to worry about the problem: standardizing and deploying new cryptographic algorithms takes time, and there may be messages encrypted now that must remain secret for more than a decade.

尽管量子计算对密码学的理论影响自 20 世纪 90 年代中期起就已被认识到，但它在实践中的潜在影响目前仍不明朗。截至本书写作之时，尚未有人建造出大规模的通用量子计算机；由于涉及诸多工程难题，研制出这种计算机的时间表也不确定。即便有朝一日真的造出了这样的计算机，在其上执行量子算法所需的真实时间或金钱代价（区别于理论上对这些算法步数的分析）也尚未被充分理解。尽管如此，目前的共识是：资金雄厚的攻击者（例如政府机构）很有可能在未来 10 到 15 年内建造出能够攻击当前已部署密码系统的量子计算机。假设情况果真如此，我们就不能等上 10 到 15 年才开始担忧这个问题：新密码算法的标准化与部署需要时间，而且现在加密的消息中，可能有些必须保密十年以上。

The above concerns have motivated an intense research effort over the past several years aimed at designing, analyzing, and developing “post-quantum” cryptosystems that would remain secure even against (polynomial-time) quantum algorithms. This work accelerated in 2017, when NIST announced an effort to evaluate and (eventually) standardize quantum-resistant public-key schemes. As in the case of the earlier AES and SHA-3 competitions, NIST solicited proposals for public-key encryption schemes and signature schemes from cryptographers around the world, eventually receiving 69 candidates; 26 of those made it to the second round in early 2019. In contrast to the AES and SHA-3 process, NIST is not expected to choose a single “winner” in each category; instead, the idea is to identify multiple schemes judged to be secure. NIST is expected to issue a set of draft standards for such schemes by 2024.

上述担忧推动了过去几年间一场紧锣密鼓的研究工作，其目标是设计、分析并开发即使面对（多项式时间）量子算法也仍能保持安全的“后量子”密码系统。这项工作在 2017 年提速：当年 NIST 宣布启动一项评估（并最终标准化）抗量子公钥方案的工作。与早先的 AES 和 SHA-3 竞赛一样，NIST 向全世界的密码学家征集公钥加密方案和签名方案的提案，最终收到 69 个候选方案；其中 26 个于 2019 年初进入第二轮。与 AES 和 SHA-3 的流程不同，NIST 预计不会在每个类别中选出唯一的“胜出者”；相反，其思路是甄别出多个被判定为安全的方案。NIST 预计将在 2024 年前发布此类方案的一组标准草案。

The goal of this chapter is to describe the impact of quantum algorithms on the schemes used today, and to offer a glimpse of some schemes offering plausible post-quantum security. We do not assume any background in quantum mechanics or quantum computing, and will not present any quantum algorithms in detail. Rather, we explain what existing quantum algorithms can do (without describing in detail how they do it) and otherwise treat them as “black boxes.” The post-quantum cryptosystems we describe are similar to current leading candidates in the NIST post-quantum standardization effort, but we have simplified them for pedagogical purposes.

本章的目标是描述量子算法对当今所用方案的影响，并初步介绍几种有望提供后量子安全性的方案。我们不假定读者具备量子力学或量子计算的背景，也不会详细展示任何量子算法；相反，我们只解释现有量子算法能做什么（而不详述它们是如何做到的），除此之外把它们当作“黑盒”对待。我们描述的后量子密码系统与 NIST 后量子标准化工作中目前的领先候选方案类似，但出于教学目的做了简化。

Post-quantum cryptography vs. quantum cryptography. Quantum cryptography is related to, but distinct from, post-quantum cryptography as we use the term here. Quantum cryptography refers to cryptosystems that are implemented using quantum computers, quantum-mechanical phenomena, and quantum communication channels; for this reason, they would be difficult to deploy widely over the existing Internet. Post-quantum cryptosystems, on the other hand, are entirely classical—but are intended to ensure security even if an attacker has access to a quantum computer.

**后量子密码学与量子密码学。**

量子密码学与本文所说的后量子密码学相关，但二者并不相同。量子密码学指的是利用量子计算机、量子力学现象和量子通信信道实现的密码系统；正因如此，这类系统难以在现有互联网上广泛部署。而后量子密码系统则完全是经典的——但其目标是：即使攻击者拥有量子计算机，也能确保安全性。

Interestingly, quantum cryptosystems can in some cases be proven secure unconditionally (i.e., without any computational assumptions), even against quantum attackers. In contrast, post-quantum cryptosystems—as with the rest of the schemes in this book—rely on assumptions regarding the hardness of certain mathematical problems even for quantum algorithms.

有趣的是，量子密码系统在某些情况下可以被证明是无条件安全的（即不依赖任何计算性假设），即使面对量子攻击者亦然。相比之下，后量子密码系统——与本书中其余的方案一样——依赖于某些数学问题即使对量子算法也依然困难的假设。

## 14.1 Post-Quantum Symmetric-Key Cryptography　后量子对称密钥密码学

We begin by exploring the impact of quantum computers on symmetric-key cryptography. While there are known quantum attacks that can outperform classical attacks in this setting, the net result is only a polynomial speedup and so the overall impact on symmetric-key cryptography is relatively minor.

我们首先考察量子计算机对对称密钥密码学的影响。虽然已知的量子攻击在这一场景下确实能胜过经典攻击，但最终结果只是多项式级别的加速，因此对对称密钥密码学的总体影响相对较小。

### 14.1.1 Grover's Algorithm and Symmetric-Key Lengths　Grover 算法与对称密钥长度

Consider the following abstract problem: Given oracle access to a function $f: D \to \{0,1\}$, find an input $x$ for which $f(x) = 1$. If there is only one such input, chosen uniformly in $D$, then it is not hard to show that any classical algorithm for this problem requires $\mathcal{O}(|D|)$ evaluations of $f$; this effectively corresponds to exhaustive search over the domain $D$ of the function.

考虑如下抽象问题：给定对函数 $f: D \to \{0,1\}$ 的预言机访问，找出一个满足 $f(x) = 1$ 的输入 $x$。如果这样的输入只有一个，且是在 $D$ 中均匀选取的，那么不难证明：求解该问题的任何经典算法都需要对 $f$ 求值 $\mathcal{O}(|D|)$ 次；这实际上就相当于在函数的定义域 $D$ 上进行穷举搜索。

In a surprising result published in 1996, Lov Grover showed that quantum algorithms can do better. Specifically, he gave an algorithm that finds $x$ as above using only $\mathcal{O}(|D|^{1/2})$ evaluations of $f$—a quadratic speedup. It was later shown that this is optimal, i.e., no quantum algorithm can do better.

在 1996 年发表的一项令人惊讶的结果中，Lov Grover 证明了量子算法可以做得更好。具体而言，他给出的算法只需对 $f$ 求值 $\mathcal{O}(|D|^{1/2})$ 次就能找到上述的 $x$——实现了平方级加速。后来人们证明这是最优的，即不存在更快的量子算法。

Let us explore the impact this has on the required key length for symmetric-key cryptosystems. For concreteness, consider the case of a block cipher $F: \{0,1\}^n \times \{0,1\}^\ell \to \{0,1\}^\ell$ for which exhaustive search is the best attack, and an attacker whose goal is to determine the key $k \in \{0,1\}^n$ given a constant number of input/output pairs $\{(x_i, y_i)\}$ with $y_i = F_k(x_i)$. Say we want security against attacks running in time ${2}^\kappa$. Classically, it suffices to set $n = \kappa$ (since exhaustive search for $k$ requires time $\approx 2^n$). But if we define

我们来探讨这一结果对对称密钥密码系统所需密钥长度的影响。具体来说，考虑分组密码 $F: \{0,1\}^n \times \{0,1\}^\ell \to \{0,1\}^\ell$，假设穷举搜索是对它的最佳攻击，而攻击者的目标是：给定常数个满足 $y_i = F_k(x_i)$ 的输入/输出对 $\{(x_i, y_i)\}$，确定密钥 $k \in \{0,1\}^n$。设我们希望抵御运行时间为 ${2}^\kappa$ 的攻击。在经典情形下，取 $n = \kappa$ 即可（因为穷举搜索 $k$ 需要约 $2^n$ 的时间）。但如果定义

$$f(k)=1\Leftrightarrow F_{k}(x_{i})=y_{i}\text{ for all }i,$$

then Grover's algorithm allows an attacker to find the key using $\mathcal{O}(2^{n/2})$ evaluations of $f$, or equivalently $\mathcal{O}(2^{n/2})$ evaluations of $F$. Thus, to achieve the desired level of security we must set $n = 2\kappa$. Summarizing:

那么 Grover 算法使攻击者只需对 $f$ 求值 $\mathcal{O}(2^{n/2})$ 次——等价地，对 $F$ 求值 $\mathcal{O}(2^{n/2})$ 次——就能找到密钥。因此，要达到期望的安全级别，必须取 $n = 2\kappa$。总结如下：

To ensure equivalent security against exhaustive-search attacks in the quantum setting, symmetric-key cryptosystems must use keys that are double the length of keys used in the classical setting.

为确保在量子环境下抵御穷举搜索攻击的安全性达到同等水平，对称密钥密码系统使用的密钥长度必须是经典环境下的两倍。

We stress that the above applies only if exhaustive-search attacks are the best possible; in other cases quantum algorithms may give even larger speedups.

需要强调的是，上述结论仅当穷举搜索攻击是最佳攻击时才成立；在其他情况下，量子算法可能带来更大的加速。

### 14.1.2 Collision-Finding Algorithms and Hash Functions　碰撞查找算法与哈希函数

Consider next the problem of finding a collision in some hash function $H: \{0,1\}^m \to \{0,1\}^n$ (with $m > n$). As we have seen already in Section 6.4.1, this can be done classically via a “birthday attack” using $\mathcal{O}(2^{n/2})$ evaluations of $H$. Is it possible to do better using a quantum algorithm?

接下来考虑在某个哈希函数 $H: \{0,1\}^m \to \{0,1\}^n$（其中 $m > n$）中找碰撞的问题。正如 6.4.1 节已经看到的，在经典情形下可以通过“生日攻击”用 $\mathcal{O}(2^{n/2})$ 次 $H$ 的求值做到这一点。那么，用量子算法是否可能做得更好？

It is indeed possible to do better via clever use of Grover’s algorithm. For simplicity in the analysis we will model $H$ as a random function (as we did in Section 6.4.1); the collision-finding algorithm we describe can be adapted for arbitrary $H$ as well. The approach is as follows. Let $\ell \ll 2^n$ be a parameter that we will set later. Let $C, D$ be disjoint subsets of $\{0,1\}^m$ with $|C| = \ell$ and $|D| = \ell^2$; for example, we can let $C$ be the set of all strings whose first $\log \ell$ bits are all 0 and take $D$ to be the set of all strings whose first ${2}\log \ell$ bits are all 1. For $x_i \in C$, set $y_i := H(x_i)$ using $\ell$ evaluations of $H$; define $C^{\prime} = \{y_i\}$. If $y_i = y_j$ for some $i \neq j$ then a collision has already been found. Otherwise, define the function $f: D \to \{0,1\}$ as

确实可以通过巧妙地运用 Grover 算法做得更好。为了简化分析，我们把 $H$ 建模为随机函数（如同 6.4.1 节中的做法）；下面描述的碰撞查找算法同样可以改造后适用于任意的 $H$。方法如下。设 $\ell \ll 2^n$ 是一个稍后再设定的参数。取 $\{0,1\}^m$ 的两个不相交子集 $C, D$，满足 $|C| = \ell$ 且 $|D| = \ell^2$；例如，可以让 $C$ 是前 $\log \ell$ 个比特全为 0 的所有串组成的集合，并取 $D$ 为前 ${2}\log \ell$ 个比特全为 1 的所有串组成的集合。对每个 $x_i \in C$，用 $\ell$ 次 $H$ 的求值计算 $y_i := H(x_i)$；定义 $C^{\prime} = \{y_i\}$。如果存在 $i \neq j$ 使 $y_i = y_j$，那么就已经找到了一个碰撞。否则，定义函数 $f: D \to \{0,1\}$ 为

$$f(x)=1\Leftrightarrow H(x)\in C^{\prime}.$$

If there is any $x$ with $f(x)=1$, then we can use Grover's algorithm to find such an $x$ using $\mathcal{O}(|D|^{1/2})$ evaluations of $f$, or equivalently $\mathcal{O}(|D|^{1/2})$ evaluations of $H$. The overall number of evaluations of $H$, then, is $\mathcal{O}(\ell+\sqrt{\ell^{2}})=\mathcal{O}(\ell)$.

如果存在使 $f(x)=1$ 的 $x$，就可以用 Grover 算法找到这样一个 $x$，为此需对 $f$ 求值 $\mathcal{O}(|D|^{1/2})$ 次——等价地，对 $H$ 求值 $\mathcal{O}(|D|^{1/2})$ 次。于是，对 $H$ 求值的总次数为 $\mathcal{O}(\ell+\sqrt{\ell^{2}})=\mathcal{O}(\ell)$。

What is the probability that such an $x$ exists? We only run the second stage of the algorithm if all the $\{y_i\}$ are distinct. Since we model $H$ as a random function, for any particular $x \in D$ the probability that $H(x) \in C^{\prime}$ is $\frac{\ell}{2^n}$, and so the probability that the hash of some element of $D$ lies in $C^{\prime}$ is

这样的 $x$ 存在的概率有多大？我们只在所有 $\{y_i\}$ 彼此不同的情况下才运行算法的第二阶段。由于我们把 $H$ 建模为随机函数，对任一特定的 $x \in D$，$H(x) \in C^{\prime}$ 的概率是 $\frac{\ell}{2^n}$，因此 $D$ 中某个元素的哈希值落入 $C^{\prime}$ 的概率为

$${1}-\left(1-\frac{\ell}{2^{n}}\right)^{\ell^{2}}\geq1-e^{-\ell^{3}/2^{n}}$$

(using Proposition A.3). We thus see that taking $\ell = \Theta(2^{n/3})$ gives a constant probability of finding a collision using only $\mathcal{O}(2^{n/3})$ evaluations of $H$.

（利用命题 A.3。）于是我们看到，取 $\ell = \Theta(2^{n/3})$，就能仅用 $\mathcal{O}(2^{n/3})$ 次 $H$ 的求值以常数概率找到一个碰撞。

Consider the impact this has on the required output length of a hash function $H: \{0,1\}^m \to \{0,1\}^n$ in order to achieve some desired level of security. As in the previous section, say we want security (i.e., inability to find collisions) against attackers running in time ${2}^\kappa$, and assume there are no structural weaknesses in $H$ so generic attacks are the best possible. Classically, it suffices to set $n = 2\kappa$ (since a birthday attack would then require time $\mathcal{O}(2^{n/2}) = \mathcal{O}(2^\kappa)$). But achieving the same level of security in the quantum setting requires $n = 3\kappa$. Summarizing:

来看一看这对哈希函数 $H: \{0,1\}^m \to \{0,1\}^n$ 为达到某个期望安全级别所需的输出长度有什么影响。与上一节一样，设我们希望抵御运行时间为 ${2}^\kappa$ 的攻击者（即无法找到碰撞），并假设 $H$ 不存在结构性弱点，因而通用攻击已是最佳攻击。在经典情形下，取 $n = 2\kappa$ 就够了（因为此时生日攻击所需时间为 $\mathcal{O}(2^{n/2}) = \mathcal{O}(2^\kappa)$）。但在量子环境下要达到同样的安全级别，则需要 $n = 3\kappa$。总结如下：

To ensure equivalent security against generic collision-finding attacks in the quantum setting, the output length of a hash function must be 50% larger than the output length in the classical setting.

为确保在量子环境下抵御通用碰撞查找攻击的安全性达到同等水平，哈希函数的输出长度必须比经典环境下的输出长度大 50%。

## 14.2 Shor's Algorithm and its Impact on Cryptography　Shor 算法及其对密码学的影响

In the previous section we have seen quantum algorithms that offer a polynomial speedup as compared to the best classical algorithms for the same problems. These improved algorithms necessitate changes in the underlying parameters of symmetric-key schemes, but do not fundamentally render those schemes insecure. Here, in contrast, we discuss quantum algorithms that result in exponential speedups for solving certain number-theoretic problems—in particular, we show polynomial-time quantum algorithms for factoring and computing discrete logarithms. The existence of such algorithms means that all the public-key schemes we have discussed so far in this book are insecure (at least asymptotically) against a quantum attacker.

上一节中，我们看到某些量子算法相对求解同一问题的最佳经典算法能提供多项式加速。这些改进的算法要求对称密钥方案调整其底层参数，但并不会从根本上使这些方案变得不安全。而本节与此不同，我们要讨论的是对求解某些数论问题带来指数级加速的量子算法——特别地，我们将给出用于因子分解和计算离散对数的多项式时间量子算法。这类算法的存在意味着，本书迄今讨论的所有公钥方案在面对量子攻击者时都是不安全的（至少在渐近意义上如此）。

We begin by discussing an abstract mathematical problem with no explicit connection to cryptography. Let $f : \mathbb{H} \to R$ be a function whose domain $\mathbb{H}$ is an abelian group. (For now, $R$ can be arbitrary.) Assume further that $f$ is periodic, i.e., there is a $\delta \in \mathbb{H}$ (not equal to the identity) called the period such that for all $x \in \mathbb{H}$

我们首先讨论一个与密码学没有直接联系的抽象数学问题。设 $f : \mathbb{H} \to R$ 是一个定义域 $\mathbb{H}$ 为阿贝尔群的函数。（此处 $R$ 可以任意。）进一步假设 $f$ 是周期函数，即存在 $\delta \in \mathbb{H}$（不等于单位元），称为周期，使得对所有 $x \in \mathbb{H}$ 有

$$f(x)=f(x+\delta).$$

(Note that if $\delta$ is a period then so is ${2}\delta$, etc., and so the period is not unique.) The period-finding problem is to find a period, given oracle access to $f$.

（注意，若 $\delta$ 是周期，则 ${2}\delta$ 等也是周期，因此周期并不唯一。）周期查找问题就是：给定对 $f$ 的预言机访问，找出一个周期。

Classically, it is not clear how to solve this problem efficiently; even verifying that a given $\delta$ is a period seems difficult given only oracle access to $f$. In 1994, Peter Shor stunned researchers by showing a polynomial-time quantum algorithm for this problem for certain groups $\mathbb{H}$. His result was subsequently generalized by others to handle larger classes of groups. The details of Shor's algorithm lie outside our scope, but we discuss the cryptographic implications of Shor's algorithm below.

在经典情形下，如何高效求解这个问题并不清楚；即便只验证给定的 $\delta$ 是否为周期，在仅有预言机访问的条件下似乎也很困难。1994 年，Peter Shor 展示了针对某些群 $\mathbb{H}$ 求解该问题的多项式时间量子算法，令研究者们大为震惊。他的结果后来被其他人推广到更大的群类。Shor 算法的细节超出了本书范围，但我们在下文讨论 Shor 算法对密码学的影响。

**Implications for factoring and computing discrete logarithms.**

Period finding is a powerful tool: in particular, it can be used to factor and compute discrete logarithms! All we need to do is carefully choose the function whose period gives us the solution we are looking for.

**对因子分解与计算离散对数的影响。**

周期查找是一个强大的工具：特别地，它可以用来进行因子分解和计算离散对数！我们需要做的只是精心选取函数，使其周期给出我们所寻找的解。

First consider the problem of factoring. Fix a composite number $N$ that is the product of two distinct primes. Taking any $x \in \mathbb{Z}_N^*$, define the function $f_{x,N} : \mathbb{Z} \to \mathbb{Z}_N^*$ by

首先考虑因子分解问题。固定一个由两个不同素数相乘得到的合数 $N$。取任意 $x \in \mathbb{Z}_N^*$，定义函数 $f_{x,N} : \mathbb{Z} \to \mathbb{Z}_N^*$ 为

$$f_{x,N}(r)=[x^{r}\bmod N].$$

The key observation is that this function has period $\phi(N)$ since

关键的观察是：该函数以 $\phi(N)$ 为周期，因为

$$f_{x,N}(r+\phi(N))=[x^{r+\phi(N)}\bmod N]=[x^{r}\cdot x^{\phi(N)}\bmod N]=[x^{r}\bmod N]$$

for any $r$. Thus, for any $x \in \mathbb{Z}_N^*$ of our choice we can run Shor's algorithm to obtain some period of $f_{x,N}$, i.e., a nonzero integer $k$ such that $x^k = 1 \bmod N$. Theorem 9.50 shows that this enables us to factor $N$ using polynomially many calls to Shor's algorithm and polynomial-time classical computation. (Shor's algorithm in this case runs in time polynomial in the logarithm of the smallest period—which is at most $\phi(N)$—and so this gives a quantum algorithm running in polynomial time overall.)

对任意 $r$ 都成立。于是，对我们选定的任意 $x \in \mathbb{Z}_N^*$，都可以运行 Shor 算法得到 $f_{x,N}$ 的某个周期，即一个满足 $x^k = 1 \bmod N$ 的非零整数 $k$。定理 9.50 表明，这使我们能够通过多项式次调用 Shor 算法加上多项式时间的经典计算来分解 $N$。（此时 Shor 算法的运行时间关于最小周期的对数是多项式的——该最小周期至多为 $\phi(N)$——因此整体上得到一个多项式时间的量子算法。）

Period finding can also be used to compute discrete logarithms. Fix some cyclic group $\mathbb{G}$ of prime order $q$ with generator $g$, and say we are given some element $h \in \mathbb{G}$. Consider the function $f_{g,h} : \mathbb{Z}_q \times \mathbb{Z}_q \to \mathbb{G}$ given by

周期查找也可以用于计算离散对数。固定某个阶为素数 $q$、生成元为 $g$ 的循环群 $\mathbb{G}$，并设给定某元素 $h \in \mathbb{G}$。考虑由下式给出的函数 $f_{g,h} : \mathbb{Z}_q \times \mathbb{Z}_q \to \mathbb{G}$：

$$f(a,b)=g^{a}\cdot h^{-b}.$$

If we let $x = \log_{g} h$, then $f_{g,h}$ has period $(x, 1)$ since

若令 $x = \log_{g} h$，则 $f_{g,h}$ 以 $(x, 1)$ 为周期，因为

$$f_{g,h}(a+x,b+1)=g^{a+x}h^{-b-1}=g^{a}g^{x}h^{-b}h^{-1}=g^{a}h^{-b}$$

for any $a,b$. Moreover, for any period $(x^{\prime},y^{\prime})$ we have $g^{x^{\prime}}h^{-y^{\prime}} = 1 = g^0h^0$. Lemma 9.65 thus shows that we can use any period to compute $\log_g h$ using classical polynomial-time computation. A quantum polynomial-time algorithm for computing $\log_g h$ follows from the fact that the running time of the period-finding algorithm in this case is polynomial in $\log q$.

对任意 $a,b$ 都成立。此外，对任意周期 $(x^{\prime},y^{\prime})$ 有 $g^{x^{\prime}}h^{-y^{\prime}} = 1 = g^0h^0$。于是引理 9.65 表明：我们可以利用任意一个周期，通过经典的多项式时间计算求得 $\log_g h$。由于此时周期查找算法的运行时间关于 $\log q$ 是多项式的，便得到计算 $\log_g h$ 的量子多项式时间算法。

Since the hardness of factoring and computing discrete logarithms underlies all the public-key cryptosystems we have seen so far in the book (and, indeed, all public-key algorithms in wide use today), we conclude that
all public-key cryptosystems we have covered thus far can be broken in polynomial time by a quantum computer.

由于因子分解和计算离散对数的困难性是本书迄今为止介绍的所有公钥密码系统的基础（实际上也是当今广泛使用的所有公钥算法的基础），我们得出结论：
本书涵盖的所有公钥密码系统都能被量子计算机在多项式时间内攻破。

This stark fact highlights the importance of post-quantum cryptography.

这一严酷的事实凸显了后量子密码学的重要性。

## 14.3 Post-Quantum Public-Key Encryption　后量子公钥加密

As noted at the end of the previous section, both the factoring and discrete-logarithm problems become “easy” given a quantum computer. To have any hope of constructing public-key schemes with post-quantum security, then, we need to look for mathematical problems that are computationally hard even for quantum computers. As in the classical case, we generally cannot prove unconditionally that a specific problem is hard for quantum algorithms; all we can do is rely on plausible conjectures about the (quantum) hardness of certain problems. One notable difference from the classical setting is that the problems being considered for post-quantum cryptography have, on the whole, not been studied as long as the factoring and discrete-logarithm problems; thus, in some sense, we have less confidence that they are truly hard.

正如上一节末尾所指出的，一旦有了量子计算机，因子分解问题和离散对数问题都会变得“容易”。因此，若还想构造出具有后量子安全性的公钥方案，就需要寻找即使对量子计算机而言也计算困难的数学问题。与经典情形一样，我们通常无法无条件地证明某个特定问题对量子算法是困难的；我们能做的只是依赖关于某些问题（量子）困难性的合理猜想。与经典场景的一个显著不同在于：总体而言，被考虑用于后量子密码学的那些问题，被研究的时间不像因子分解和离散对数问题那样久；因此，从某种意义上说，我们对它们真正困难的信心要弱一些。

In this section we introduce one computational problem that has received a lot of attention, and is widely believed to be hard even for quantum algorithms. We then show how to construct a public-key encryption scheme based on the assumed hardness of that problem. We stress that our goal here is merely to provide a taste of recent work on post-quantum cryptography; in particular, we describe the scheme somewhat loosely without including every detail. For pedagogical purposes we also focus on a simple encryption scheme without attempting to optimize its efficiency.

本节引入一个备受关注、且被广泛认为即使对量子算法也困难的计算问题，然后展示如何基于对该问题困难性的假设来构造公钥加密方案。我们强调，这里的目标只是让读者初步领略后量子密码学的近期工作；特别地，我们的描述较为粗略，并未涵盖每一个细节。出于教学目的，我们还专注于一个简单的加密方案，而不去优化其效率。

The remainder of this section assumes a very basic knowledge of linear algebra, but can be appreciated even without this background if the reader is willing to accept certain facts on faith.

本节余下部分假定读者具备非常基本的线性代数知识；不过，即使没有这一背景，只要读者愿意直接接受某些事实，也能理解这些内容。

Throughout this section we let $q$ be an odd prime. We let $\lfloor \cdot \rfloor$ denote the standard “floor” function, so $\lfloor x \rfloor$ is the largest integer less than or equal to $x$. In this section we also change our view of $\mathbb{Z}_q$, equating it with the set

在本节中，设 $q$ 为奇素数。记 $\lfloor \cdot \rfloor$ 为标准“下取整”函数，即 $\lfloor x \rfloor$ 是小于等于 $x$ 的最大整数。本节还改变了对 $\mathbb{Z}_q$ 的看法，将其等同于集合

$$\{-\lfloor(q-1)/2\rfloor,\ldots,0,\ldots,\lfloor q/2\rfloor\}$$

(as opposed to $\{0, \ldots, q-1\}$ as we have done until now). This viewpoint is better suited to the present context, where we will say that an element of $\mathbb{Z}_q$ is “small” if it is “close” to 0.

（而不是像此前一直采用的那样等同于 $\{0, \ldots, q-1\}$）。这种视角更适合当前语境：在本节中，只要 $\mathbb{Z}_q$ 中的元素“接近”0，我们就称它是“小的”。

**The LWE assumption.**

Consider the following problem: A matrix $\mathbf{B} \in \mathbb{Z}_q^{m \times n}$ is chosen, along with a vector $^1$ $\mathbf{s} \in \mathbb{Z}_q^n$. We are then given $\mathbf{B}$ and $\mathbf{t} := [\mathbf{B} \cdot \mathbf{s} \bmod q]$ (i.e., all operations are done modulo $q$); the goal is to find any value $\mathbf{s}^{\prime} \in \mathbb{Z}_q^n$ such that $\mathbf{B}\mathbf{s}^{\prime} = \mathbf{t} \bmod q$. This problem is easy and can be solved using standard (efficient) linear-algebraic techniques.

**LWE 假设。**

考虑如下问题：选取矩阵 $\mathbf{B} \in \mathbb{Z}_q^{m \times n}$ 以及向量 $^1$ $\mathbf{s} \in \mathbb{Z}_q^n$。然后给我们的是 $\mathbf{B}$ 与 $\mathbf{t} := [\mathbf{B} \cdot \mathbf{s} \bmod q]$（即所有运算都在模 $q$ 意义下进行）；目标是找出任意一个满足 $\mathbf{B}\mathbf{s}^{\prime} = \mathbf{t} \bmod q$ 的值 $\mathbf{s}^{\prime} \in \mathbb{Z}_q^n$。这个问题是容易的，可以用标准的（高效的）线性代数技术求解。

> $^1$ By default, our vectors are column vectors and so we write, e.g., $\mathbf{s}^T$ (the transpose of $\mathbf{s}$) to denote a row vector.

> $^1$ 默认情况下，我们的向量都是列向量，因此我们写作（例如）$\mathbf{s}^T$（$\mathbf{s}$ 的转置）来表示行向量。

Consider next the following variant of the problem. Choose $\mathbf{B}$ and $\mathbf{s}$ as before, but now also choose a short “error vector” $\mathbf{e} \in \mathbb{Z}_q^m$. (We use the standard Euclidean norm to define the length of vectors. That is, the length of a vector $\mathbf{e} = [e_1, \ldots, e_m]^T$, denoted $\|\mathbf{e}\|$, is simply $\sqrt{\sum_i e_i^2}$. At the moment, we do not quantify what we mean by “short.”) The value $\mathbf{t}$ is now computed as $\mathbf{t} := [\mathbf{B}\mathbf{s} + \mathbf{e} \bmod q]$ and the goal, given $\mathbf{B}$ and $\mathbf{t}$, is to find any $\mathbf{s}^{\prime} \in \mathbb{Z}_q^n$ such that $[\mathbf{t} - \mathbf{B}\mathbf{s}^{\prime} \bmod q]$ is short. For historical reasons, this is called the learning with errors (LWE) problem. When parameters are chosen appropriately, this problem appears to be significantly more difficult than the previous problem (when there are no errors), and efficient algorithms for solving it—even allowing for quantum algorithms—are not known.

接下来考虑上述问题的如下变体。照旧选取 $\mathbf{B}$ 和 $\mathbf{s}$，但现在还要选取一个短的“误差向量” $\mathbf{e} \in \mathbb{Z}_q^m$。（我们用标准欧几里得范数定义向量的长度：向量 $\mathbf{e} = [e_1, \ldots, e_m]^T$ 的长度记作 $\|\mathbf{e}\|$，就是 $\sqrt{\sum_i e_i^2}$。此处暂不量化“短”的确切含义。）此时 $\mathbf{t}$ 按 $\mathbf{t} := [\mathbf{B}\mathbf{s} + \mathbf{e} \bmod q]$ 计算，目标则是：给定 $\mathbf{B}$ 与 $\mathbf{t}$，找出任意一个使 $[\mathbf{t} - \mathbf{B}\mathbf{s}^{\prime} \bmod q]$ 为短的 $\mathbf{s}^{\prime} \in \mathbb{Z}_q^n$。出于历史原因，这被称为带误差学习（learning with errors，LWE）问题。当参数选取适当时，该问题看起来比前一个问题（无误差的情形）困难得多，而且目前不知道求解它的有效算法——即使是量子算法也不例外。

For our purposes it is useful to consider a different version of the above called the decisional LWE problem. Here, roughly speaking, the goal is to distinguish whether $\mathbf{t}$ was generated by the process described above, or whether $\mathbf{t}$ was sampled uniformly from $\mathbb{Z}_q^m$. It is possible to show (for certain settings of the parameters) that this problem is hard if and only if the LWE problem itself is hard.

对我们的目的而言，考虑上述问题的另一个版本——判定性 LWE 问题——是有用的。粗略地说，这里的目标是区分 $\mathbf{t}$ 究竟是由上述过程生成的，还是从 $\mathbb{Z}_q^m$ 中均匀采样的。可以证明（对某些参数设定）：这个问题困难当且仅当 LWE 问题本身困难。

We now formalize the above discussion. Let $m,q$ be deterministic functions of the security parameter $n$ with $m>n$; we leave the dependence on $n$ implicit. Let $\psi$ be an efficient randomized algorithm that takes as input ${1}^n$ and outputs an integer; this $\psi$ represents the distribution on the errors, and we also leave its dependence on $n$ implicit. The following defines what it means for the decisional LWE problem to be (quantum-)hard for some $m,q,\psi$.

现在我们把上述讨论形式化。设 $m,q$ 是安全参数 $n$ 的确定性函数且 $m>n$；我们把对 $n$ 的依赖隐去不写。设 $\psi$ 是一个高效的随机化算法，输入为 ${1}^n$、输出一个整数；这个 $\psi$ 表示误差的分布，我们同样隐去它对 $n$ 的依赖。下面定义：对某组 $m,q,\psi$，所谓判定性 LWE 问题（对量子算法而言）困难，是什么意思。

DEFINITION 14.1 We say the decisional $\text{LWE}_{m,q,\psi}$ problem is quantum-hard if for all quantum polynomial-time algorithms $\mathcal{A}$ there is a negligible function $\mathsf{negl}$ such that

$$\begin{align*}\left|\Pr[\mathbf{B}\leftarrow\mathbb{Z}_{q}^{m\times n};\mathbf{s}\leftarrow\psi^{n};\mathbf{e}\leftarrow\psi^{m}:\mathcal{A}\left(\mathbf{B},[\mathbf{B}\mathbf{s}+\mathbf{e}\bmod q]\right)=1]\right.\\\left.-\Pr[\mathbf{B}\leftarrow\mathbb{Z}_{q}^{m\times n};\mathbf{t}\leftarrow\mathbb{Z}_{q}^{m}:\mathcal{A}(\mathbf{B},\mathbf{t})=1]\right|\leq\mathsf{negl}(n).\end{align*}$$

定义 14.1　若对于所有量子多项式时间算法 $\mathcal{A}$，都存在可忽略函数 $\mathsf{negl}$ 使得上式成立，则称判定性 $\text{LWE}_{m,q,\psi}$ 问题为量子困难的。

(Note that we also choose $\mathbf{s}$ to be short.) Clearly, if the decisional $\text{LWE}_{m,q,\psi}$ problem is hard then so is the decisional $\text{LWE}_{m^{\prime},q,\psi}$ problem for any $m^{\prime} \leq m$. It is only slightly more difficult to show that increasing the length of $\mathbf{s}$ can only make the problem harder. We leave the following as an exercise.

（注意，我们也把 $\mathbf{s}$ 选成短的。）显然，若判定性 $\text{LWE}_{m,q,\psi}$ 问题困难，则对任意 $m^{\prime} \leq m$，判定性 $\text{LWE}_{m^{\prime},q,\psi}$ 问题也困难。要证明增大 $\mathbf{s}$ 的长度只会使问题更难，也只需稍多费些笔墨。我们把下面的结论留作习题。

LEMMA 14.2 If the decisional $\operatorname{LWE}_{m,q,\psi}$ problem is quantum-hard, then for all quantum polynomial-time algorithms $\mathcal{A}$ and all functions $m^{\prime}, \ell$ with $m^{\prime}(n) \leq m(n)$ and $\ell(n) \geq n$ there is a negligible function $\mathsf{negl}$ such that

$$\begin{align*}\left|\Pr[\mathbf{B}\leftarrow\mathbb{Z}_{q}^{m^{\prime}\times\ell};\mathbf{s}\leftarrow\psi^{\ell};\mathbf{e}\leftarrow\psi^{m^{\prime}}:\mathcal{A}\left(\mathbf{B},[\mathbf{B}\mathbf{s}+\mathbf{e}\bmod q]\right)=1]\right.&\\\left.-\Pr[\mathbf{B}\leftarrow\mathbb{Z}_{q}^{m^{\prime}\times\ell};\mathbf{t}\leftarrow\mathbb{Z}_{q}^{m^{\prime}}:\mathcal{A}(\mathbf{B},\mathbf{t})=1]\right|&\leq\mathsf{negl}(n).\end{align*}$$

引理 14.2　若判定性 $\operatorname{LWE}_{m,q,\psi}$ 问题为量子困难，则对所有量子多项式时间算法 $\mathcal{A}$，以及所有满足 $m^{\prime}(n) \leq m(n)$ 与 $\ell(n) \geq n$ 的函数 $m^{\prime}, \ell$，都存在可忽略函数 $\mathsf{negl}$ 使得上式成立。

**LWE-Based encryption.**

We motivate the construction of an encryption scheme from the decisional LWE problem by first describing an insecure key-exchange protocol that can be viewed as a linear-algebraic version of Diffie–Hellman key exchange. Fix $n, q, \psi$, and $m > n$, and consider the following protocol run between two parties Alice and Bob. Alice begins by generating a uniform $\mathbf{B} \in \mathbb{Z}_q^{m \times n}$ and choosing $\mathbf{s} \leftarrow \psi^n$; she then sends $(\mathbf{B}, \mathbf{t}_A := [\mathbf{B} \cdot \mathbf{s} \bmod q])$. Bob chooses $\hat{\mathbf{s}} \leftarrow \psi^m$ and replies with $\mathbf{t}_B^T := [\hat{\mathbf{s}}^T \cdot \mathbf{B} \bmod q]$. Finally, Alice computes $k_A := [\mathbf{t}_B^T \cdot \mathbf{s} \bmod q]$ and Bob computes $k_B := [\hat{\mathbf{s}}^T \cdot \mathbf{t}_A \bmod q]$. Note that

**基于 LWE 的加密。**

为了引出基于判定性 LWE 问题的加密方案的构造，我们先描述一个不安全的密钥交换协议，它可以看作 Diffie–Hellman 密钥交换的线性代数版本。固定 $n, q, \psi$ 与 $m > n$，考虑在两方 Alice 和 Bob 之间运行的如下协议。Alice 先生成均匀的 $\mathbf{B} \in \mathbb{Z}_q^{m \times n}$ 并选取 $\mathbf{s} \leftarrow \psi^n$；然后发送 $(\mathbf{B}, \mathbf{t}_A := [\mathbf{B} \cdot \mathbf{s} \bmod q])$。Bob 选取 $\hat{\mathbf{s}} \leftarrow \psi^m$ 并回复 $\mathbf{t}_B^T := [\hat{\mathbf{s}}^T \cdot \mathbf{B} \bmod q]$。最后，Alice 计算 $k_A := [\mathbf{t}_B^T \cdot \mathbf{s} \bmod q]$，Bob 计算 $k_B := [\hat{\mathbf{s}}^T \cdot \mathbf{t}_A \bmod q]$。注意

$$\boldsymbol{k}_{A}=\mathbf{t}_{B}^{T}\cdot\mathbf{s}=\hat{\mathbf{s}}^{T}\cdot\mathbf{B}\cdot\mathbf{s}=\hat{\mathbf{s}}^{T}\cdot\mathbf{t}_{A}=k_{B}$$

(where all calculations above are done modulo $q$), and so Alice and Bob have agreed on a shared key!

以上所有计算均在模 $q$ 意义下进行；于是 Alice 和 Bob 就商定了一个共享密钥！

Of course, the protocol above is not secure since an eavesdropper can use linear algebra to recover $\mathbf{s}$, $\hat{\mathbf{s}}$, or both, and thus compute the key as well. By judiciously adding noise, however (and under the assumption that the decisional LWE problem is hard), it is possible for Alice and Bob to agree on a key while preventing an adversary from learning it. Adapting the resulting protocol to give an encryption scheme (in the same way the Diffie–Hellman protocol is adapted to give El Gamal encryption), we obtain Construction 14.3.

当然，上述协议并不安全，因为窃听者可以利用线性代数恢复 $\mathbf{s}$、$\hat{\mathbf{s}}$ 或二者，从而也能计算出密钥。然而，通过明智地加入噪声（并在判定性 LWE 问题困难的假设下），Alice 和 Bob 可以商定一个密钥，同时防止敌手得知该密钥。把所得协议改造成加密方案（就像把 Diffie–Hellman 协议改造成 El Gamal 加密那样），便得到构造 14.3。

**CONSTRUCTION 14.3**

Let $m, q, \psi$ be as in the text. Define a public-key encryption scheme as follows:

- Gen: on input ${1}^n$ choose uniform $\mathbf{B} \leftarrow \mathbb{Z}_q^{m \times n}$ as well as $\mathbf{s} \leftarrow \psi^n$ and $\mathbf{e} \leftarrow \psi^m$. Set $\mathbf{t} := [\mathbf{B} \cdot \mathbf{s} + \mathbf{e} \bmod q]$. The public key is $\langle \mathbf{B}, \mathbf{t} \rangle$ and the private key is $\mathbf{s}$.

- Enc: on input a public key $pk = \langle \mathbf{B}, \mathbf{t} \rangle$ and a bit $b$, choose $\hat{\mathbf{s}} \leftarrow \psi^m$ and $\hat{\mathbf{e}} \leftarrow \psi^{n+1}$, and output the ciphertext

$$\mathbf{c}^{T}:=\left[\hat{\mathbf{s}}^{T}\cdot[\mathbf{B}\mid\mathbf{t}]+\hat{\mathbf{e}}^{T}+\underbrace{[0,\ldots,0,b\cdot\lfloor q/2\rfloor]}_{n+1}\mod q\right].$$

- Dec: on input a private key $\mathbf{s}$ and a ciphertext $\mathbf{c}^T$, first compute $k := [\mathbf{c}^T \cdot \begin{bmatrix} -\mathbf{s} \\ 1 \end{bmatrix} \bmod q]$. Then output 1 if $k$ is closer to $\lfloor \frac{q}{2} \rfloor$ than to 0 (see text), and 0 otherwise.

An encryption scheme based on the decisional LWE problem.

**构造 14.3**

设 $m, q, \psi$ 如正文所述。按如下方式定义公钥加密方案：

- Gen：输入 ${1}^n$ 时，均匀选取 $\mathbf{B} \leftarrow \mathbb{Z}_q^{m \times n}$，并选取 $\mathbf{s} \leftarrow \psi^n$ 与 $\mathbf{e} \leftarrow \psi^m$。置 $\mathbf{t} := [\mathbf{B} \cdot \mathbf{s} + \mathbf{e} \bmod q]$。公钥为 $\langle \mathbf{B}, \mathbf{t} \rangle$，私钥为 $\mathbf{s}$。

- Enc：输入公钥 $pk = \langle \mathbf{B}, \mathbf{t} \rangle$ 与比特 $b$ 时，选取 $\hat{\mathbf{s}} \leftarrow \psi^m$ 与 $\hat{\mathbf{e}} \leftarrow \psi^{n+1}$，并输出密文（见上方公式）。

- Dec：输入私钥 $\mathbf{s}$ 与密文 $\mathbf{c}^T$ 时，先计算 $k := [\mathbf{c}^T \cdot \begin{bmatrix} -\mathbf{s} \\ 1 \end{bmatrix} \bmod q]$。若 $k$ 更接近 $\lfloor \frac{q}{2} \rfloor$ 而非 0（见正文），则输出 1；否则输出 0。

基于判定性 LWE 问题的加密方案。

During decryption, “closeness” of $k$ to $\lfloor \frac{q}{2} \rfloor$ is determined by looking at the absolute value of $[k - \lfloor \frac{q}{2} \rfloor \bmod q]$. Here it is important that we use the particular representation of $\mathbb{Z}_q$ described at the beginning of this section.

在解密时，$k$ 与 $\lfloor \frac{q}{2} \rfloor$ 的“接近程度”通过考察 $[k - \lfloor \frac{q}{2} \rfloor \bmod q]$ 的绝对值来判断。这里重要的是使用本节开头描述的那种 $\mathbb{Z}_q$ 的特定表示。

The construction is somewhat complicated, so it is worth stepping through the process of encryption and decryption to verify that the scheme is correct (at least with high probability) when parameters are set appropriately. Let $\mathbf{c}^{T}$ be an honestly generated ciphertext, so

这个构造有些复杂，因此值得逐步走一遍加密和解密的过程，以验证当参数设置适当时方案是正确的（至少以高概率正确）。设 $\mathbf{c}^{T}$ 是一个诚实生成的密文，则

$$\mathbf{c}^{T}=\hat{\mathbf{s}}^{T}\cdot\left[\mathbf{B}\mid\mathbf{t}\right]+\hat{\mathbf{e}}^{T}+\mathbf{b}^{T},$$

where we let $\mathbf{b}^T = [0, \ldots, 0, b \cdot \lfloor \frac{q}{2} \rfloor]$. (By default from now on, all operations are performed modulo $q$.) During decryption, the receiver computes

其中我们令 $\mathbf{b}^T = [0, \ldots, 0, b \cdot \lfloor \frac{q}{2} \rfloor]$。（从现在起，默认所有运算都在模 $q$ 意义下进行。）解密时，接收方计算

$$\begin{aligned}k&=\mathbf{c}^{T}\cdot\begin{bmatrix}-\mathbf{s}\\ 1\end{bmatrix}\\&=(\hat{\mathbf{s}}^{T}\cdot[\mathbf{B}\mid\mathbf{t}]+\hat{\mathbf{e}}^{T}+\mathbf{b}^{T})\cdot\begin{bmatrix}-\mathbf{s}\\ 1\end{bmatrix}\\&=-\hat{\mathbf{s}}^{T}\mathbf{B}\mathbf{s}+\hat{\mathbf{s}}^{T}\mathbf{t}+\hat{\mathbf{e}}^{T}\cdot\begin{bmatrix}-\mathbf{s}\\ 1\end{bmatrix}+b\cdot\lfloor\frac{q}{2}\rfloor\\&=\hat{\mathbf{s}}^{T}\mathbf{e}+\hat{\mathbf{e}}^{T}\cdot\begin{bmatrix}-\mathbf{s}\\ 1\end{bmatrix}+b\cdot\lfloor\frac{q}{2}\rfloor,\end{aligned}$$

using the fact that $\mathbf{t} = \mathbf{B} \cdot \mathbf{s} + \mathbf{e}$. At this point, it is unclear that the receiver recovers the correct bit. However, simple algebra shows that as long as

其中用到 $\mathbf{t} = \mathbf{B} \cdot \mathbf{s} + \mathbf{e}$ 这一事实。至此，接收方是否能恢复出正确的比特尚不明朗。然而，简单的代数运算表明：只要

$$\left|\hat{\mathbf{s}}^{T}\mathbf{e}+\hat{\mathbf{e}}^{T}\cdot\begin{bmatrix}-\mathbf{s}\\ 1\end{bmatrix}\right|<(q-1)/4 \tag{14.1}$$

the receiver will output the same bit $b$ used by the sender. Note that if we let $\hat{\mathbf{s}}^{T} = [\hat{s}_{1}, \ldots, \hat{s}_{m}]$, and similarly for $\mathbf{e}, \hat{\mathbf{e}}$, and $\mathbf{s}$, then we may write Equation (14.1) as

接收方就会输出与发送方所用相同的比特 $b$。注意，若令 $\hat{\mathbf{s}}^{T} = [\hat{s}_{1}, \ldots, \hat{s}_{m}]$，并对 $\mathbf{e}, \hat{\mathbf{e}}, \mathbf{s}$ 采用类似的记号，则可将式 (14.1) 写为

$$\left|\sum_{i=1}^{m}\hat{s}_{i}e_{i}-\sum_{i=1}^{n}\hat{e}_{i}s_{i}+\hat{e}_{n+1}\right|<(q-1)/4,$$

so the left-hand side is a sum of products of integers output by $\psi$. Thus, if the distribution $\psi$ is chosen appropriately—specifically, so that it outputs integers sufficiently small so that Equation (14.1) holds (at least with overwhelming probability)—then correctness of the encryption scheme follows.

因此左端是若干个由 $\psi$ 输出的整数的乘积之和。于是，只要分布 $\psi$ 选取得当——具体而言，使其输出的整数足够小，从而使式 (14.1) 成立（至少以压倒性的概率成立）——加密方案的正确性即得证。

We now prove that Construction 14.3 is CPA-secure $^2$ (even for quantum adversaries) if the decisional $\text{LWE}_{m,q,\psi}$ problem is quantum-hard.

我们现在证明：若判定性 $\text{LWE}_{m,q,\psi}$ 问题为量子困难，则构造 14.3 是选择明文安全的 $^2$（即使面对量子敌手亦然）。

> $^2$ One can easily define a notion of CPA-security for quantum adversaries by simply replacing "probabilistic polynomial-time" with "quantum polynomial-time" in Definition 12.2. In doing so, we continue to assume the adversary has only classical access to the encryption oracle in experiment, i.e., it can only request the encryption of classical messages. It is possible to consider stronger notions of security where the attacker is given quantum access to the encryption oracle; this is beyond the scope of our book.

> $^2$ 只需在定义 12.2 中把“概率多项式时间”替换为“量子多项式时间”，就能轻松定义面向量子敌手的选择明文安全性概念。在此过程中，我们继续假定敌手在实验中对加密预言机只有经典访问，即它只能请求加密经典消息。也可以考虑更强的安全性概念，允许攻击者对加密预言机进行量子访问；这超出了本书的范围。

THEOREM 14.4 If the $\operatorname{LWE}_{m,q,\psi}$ problem is quantum-hard, then Construction 14.3 is CPA-secure (even for quantum adversaries).

定理 14.4　若 $\operatorname{LWE}_{m,q,\psi}$ 问题为量子困难，则构造 14.3 是选择明文安全的（即使面对量子敌手）。

PROOF Let $\Pi$ denote Construction 14.3. We prove that $\Pi$ has indistinguishable encryptions in the presence of an eavesdropper even for quantum adversaries; as in the classical case, this implies that $\Pi$ is CPA-secure even for quantum adversaries).

证明　记 $\Pi$ 为构造 14.3。我们证明：即使面对量子敌手，$\Pi$ 在窃听者存在时也具有不可区分的加密；与经典情形一样，这意味着 $\Pi$ 即使面对量子敌手也是选择明文安全的。

Let $\mathcal{A}$ be a quantum polynomial-time adversary. Consider a modified encryption scheme $\widetilde{\Pi}$ in which key generation is done by choosing $\mathbf{B}$ as before, but where $\mathbf{t}$ is chosen uniformly from $\mathbb{Z}_q^m$. (Encryption is done as in $\Pi$.) Although $\widetilde{\Pi}$ is not actually an encryption scheme (as there is no way for the receiver to decrypt), the experiment $\mathsf{PubK}_{\mathcal{A},\widetilde{\Pi}}^{\mathsf{eav}}(n)$ is still well-defined since that experiment depends only on the key-generation and encryption algorithms.

设 $\mathcal{A}$ 是一个量子多项式时间敌手。考虑修改后的加密方案 $\widetilde{\Pi}$：其密钥生成仍像之前那样选取 $\mathbf{B}$，但 $\mathbf{t}$ 改为从 $\mathbb{Z}_q^m$ 中均匀选取。（加密按 $\Pi$ 的方式进行。）虽然 $\widetilde{\Pi}$ 实际上并不是加密方案（因为接收方无法解密），但实验 $\mathsf{PubK}_{\mathcal{A},\widetilde{\Pi}}^{\mathsf{eav}}(n)$ 仍是良定义的，因为该实验只依赖于密钥生成算法和加密算法。

CLAIM 14.5

$$\begin{array}{r}{\left|\Pr[\mathsf{PubK}_{\mathcal{A},\Pi}^{\mathsf{eav}}(n)=1]-\Pr[\mathsf{PubK}_{\mathcal{A},\widetilde{\Pi}}^{\mathsf{eav}}(n)=1]\right|\text{ is negligible}.}\end{array}$$

断言 14.5

PROOF The proof is by a direct reduction to the decisional LWE problem as specified in Definition 14.1. Consider the following algorithm $D$ that attempts to solve the decisional $LWE_{m,q,\psi}$ problem:

证明　证明直接归约到定义 14.1 所述的判定性 LWE 问题。考虑如下试图求解判定性 $LWE_{m,q,\psi}$ 问题的算法 $D$：

Algorithm D:

The algorithm is given $\mathbf{B} \in \mathbb{Z}_q^{m \times n}$ and $\mathbf{t} \in \mathbb{Z}_q^m$ as input.

算法 D：

该算法以 $\mathbf{B} \in \mathbb{Z}_q^{m \times n}$ 和 $\mathbf{t} \in \mathbb{Z}_q^m$ 作为输入。

- Set $pk := \langle \mathbf{B}, \mathbf{t} \rangle$ and run $\mathcal{A}(pk)$ to obtain $m_0, m_1 \in \{0, 1\}$.

- 置 $pk := \langle \mathbf{B}, \mathbf{t} \rangle$，运行 $\mathcal{A}(pk)$ 得到 $m_0, m_1 \in \{0, 1\}$。

• Choose a uniform bit b, and set

• 均匀选取比特 $b$，并置

$$\mathbf{c}^{T}:=\left[\hat{\mathbf{s}}^{T}\cdot\left[\mathbf{B}\mid\mathbf{t}\right]+\hat{\mathbf{e}}^{T}+\left[0,\ldots,0,m_{b}\cdot\lfloor\frac{q}{2}\rfloor\right]\bmod q\right].$$

• Give the ciphertext $\mathbf{c}^T$ to $\mathcal{A}$ and obtain an output bit $b^{\prime}$. If $b^{\prime} = b$, output 1; otherwise, output 0.

• 把密文 $\mathbf{c}^T$ 交给 $\mathcal{A}$，得到输出比特 $b^{\prime}$。若 $b^{\prime} = b$ 则输出 1；否则输出 0。

Note that $D$ is a quantum polynomial-time algorithm since $\mathcal{A}$ is.

注意，由于 $\mathcal{A}$ 是量子多项式时间算法，$D$ 也是。

It is immediate that

立即可得

$$\begin{align*}\Pr[\mathbf{B}\gets\mathbb{Z}_{q}^{m\times n};\mathbf{s}\gets\psi^{n};\mathbf{e}\gets\psi^{m}:D\left(\mathbf{B},[\mathbf{B}\mathbf{s}+\mathbf{e}\bmod q]\right)=1]\\=\Pr[\mathsf{PubK}_{\mathcal{A},\Pi}^{\mathtt{eav}}(n)=1]\end{align*}$$

and

以及

$$\begin{array}{r}{\Pr[\mathbf{B}\gets\mathbb{Z}_{q}^{m\times n};\mathbf{t}\gets\mathbb{Z}_{q}^{m}:D(\mathbf{B},\mathbf{t})=1]=\Pr[\mathsf{PubK}_{\mathcal{A},\widetilde{\Pi}}^{\mathsf{eav}}(n)=1].}\end{array}$$

Quantum hardness of the $\mathrm{LWE}_{m,q,\psi}$ problem implies the claim.

$\mathrm{LWE}_{m,q,\psi}$ 问题的量子困难性蕴含了该断言。

Consider now a second modified encryption scheme $\widetilde{\Pi}^{\prime}$ in which key generation is done as in $\widetilde{\Pi}$, but encryption of a bit $b$ is done by choosing a uniform $\hat{\mathbf{t}} \in \mathbb{Z}_q^{n+1}$ and outputting the ciphertext

现在考虑第二个修改后的加密方案 $\widetilde{\Pi}^{\prime}$：其密钥生成与 $\widetilde{\Pi}$ 相同，但对比特 $b$ 的加密改为均匀选取 $\hat{\mathbf{t}} \in \mathbb{Z}_q^{n+1}$ 并输出密文

$$\mathbf{c}^{T}:=\hat{\mathbf{t}}^{T}+[0,\ldots,0,b\cdot\lfloor\frac{q}{2}\rfloor].$$

CLAIM 14.6

 $\left|\Pr[\mathsf{PubK}_{\mathcal{A},\widetilde{\Pi}}^{\mathsf{eav}}(n)=1]-\Pr[\mathsf{PubK}_{\mathcal{A},\widetilde{\Pi}^{\prime}}^{\mathsf{eav}}(n)=1]\right|$ is negligible.

断言 14.6　$\left|\Pr[\mathsf{PubK}_{\mathcal{A},\widetilde{\Pi}}^{\mathsf{eav}}(n)=1]-\Pr[\mathsf{PubK}_{\mathcal{A},\widetilde{\Pi}^{\prime}}^{\mathsf{eav}}(n)=1]\right|$ 可忽略。

PROOF We begin by rewriting the way encryption is done in $\Pi$. Fixing some public key $\langle \mathbf{B}, \mathbf{t} \rangle$, define $\hat{\mathbf{B}} = [\mathbf{B} \mid \mathbf{t}]^T \in \mathbb{Z}_q^{(n+1) \times m}$. Encrypting a bit $b$ in $\tilde{\Pi}$ is then equivalent to choosing $\hat{\mathbf{s}} \leftarrow \psi^m$ and $\hat{\mathbf{e}} \leftarrow \psi^{n+1}$, computing $\hat{\mathbf{t}} := \hat{\mathbf{B}}\hat{\mathbf{s}} + \hat{\mathbf{e}}$, and then outputting the ciphertext

证明　我们首先改写 $\Pi$ 中加密的方式。固定某个公钥 $\langle \mathbf{B}, \mathbf{t} \rangle$，定义 $\hat{\mathbf{B}} = [\mathbf{B} \mid \mathbf{t}]^T \in \mathbb{Z}_q^{(n+1) \times m}$。于是，在 $\tilde{\Pi}$ 中加密比特 $b$ 等价于：选取 $\hat{\mathbf{s}} \leftarrow \psi^m$ 与 $\hat{\mathbf{e}} \leftarrow \psi^{n+1}$，计算 $\hat{\mathbf{t}} := \hat{\mathbf{B}}\hat{\mathbf{s}} + \hat{\mathbf{e}}$，然后输出密文（见上方公式）。

The crucial observation is that $\hat{\mathbf{t}}$ is computed exactly as in the decisional LWE assumption, though with different parameters (namely, $\hat{\mathbf{B}} \in \mathbb{Z}_q^{(n+1) \times m}$ instead of $\mathbf{B} \in \mathbb{Z}_q^{m \times n}$). However, since $m > n$, and hence also $n + 1 \leq m$, Lemma 14.2 shows that the decisional LWE problem is hard for this setting of the parameters as well. The claim can thus be proved similarly to the previous claim.

关键的观察在于：$\hat{\mathbf{t}}$ 的计算方式与判定性 LWE 假设中的方式完全相同，只是参数不同（即用 $\hat{\mathbf{B}} \in \mathbb{Z}_q^{(n+1) \times m}$ 代替 $\mathbf{B} \in \mathbb{Z}_q^{m \times n}$）。但由于 $m > n$、从而也有 $n + 1 \leq m$，引理 14.2 表明判定性 LWE 问题在这一参数设定下同样是困难的。于是可以仿照上一条断言来证明本断言。

CLAIM 14.7 $\Pr[\mathsf{PubK}_{\mathcal{A},\widetilde{\Pi}^{\prime}}^{\mathsf{eav}}(n)=1]=\frac{1}{2}.$

断言 14.7　$\Pr[\mathsf{PubK}_{\mathcal{A},\widetilde{\Pi}^{\prime}}^{\mathsf{eav}}(n)=1]=\frac{1}{2}.$

PROOF This follows from the fact that, in $\widetilde{\Pi}^{\prime}$, the “message vector” $[0, \ldots, 0, b \cdot \lfloor \frac{q}{2} \rfloor]$ is added to a uniform vector $\hat{\mathbf{t}}^T \in \mathbb{Z}_q^{n+1}$ modulo $q$.

证明　这源于如下事实：在 $\widetilde{\Pi}^{\prime}$ 中，“消息向量” $[0, \ldots, 0, b \cdot \lfloor \frac{q}{2} \rfloor]$ 在模 $q$ 意义下被加到均匀向量 $\hat{\mathbf{t}}^T \in \mathbb{Z}_q^{n+1}$ 上。

The preceding three claims prove the theorem.

上述三条断言共同证明了定理。

## 14.4 Post-Quantum Signatures　后量子签名

Security of all the signature schemes presented in Chapter 13 required either the hardness of factoring or the hardness of computing discrete logarithms. As we have discussed, constructions from alternate assumptions are needed if we want security in a post-quantum world. While it is possible to construct signature schemes from the LWE assumption introduced in the previous section, such schemes are complex and we explore a different approach here.

第 13 章给出的所有签名方案，其安全性要么要求因子分解的困难性，要么要求离散对数计算的困难性。如前所述，如果我们想要在后量子世界中保持安全，就需要基于其他假设的构造。虽然可以从上一节引入的 LWE 假设出发构造签名方案，但这类方案很复杂；本节我们探索另一种途径。

Somewhat surprisingly, and in contrast to the case of public-key encryption, it is possible to construct signature schemes based on hash functions, a symmetric-key primitive. Since existing cryptographic hash functions such as SHA-3 are believed to be secure even against quantum algorithms (subject to the increase in parameters discussed in Section 14.1), this provides a promising approach to constructing post-quantum signatures.

有些出人意料的是——与公钥加密的情形相反——人们可以基于哈希函数（一种对称密钥原语）构造签名方案。由于现有的密码学哈希函数（如 SHA-3）被认为即使面对量子算法也是安全的（前提是按 14.1 节讨论的那样增大参数），这为构造后量子签名提供了一条有希望的途径。

Signatures based on hash functions are interesting for several other reasons, as well. First, it is amazing (and perhaps counterintuitive) that signatures can be constructed without any number-theoretic assumptions, unlike public-key encryption schemes. Moreover, as we will see, the ideas developed here can be used to construct signature schemes from the minimal assumption that one-way functions exist. It is also worth noting that the schemes we present here do not rely on random oracles, as opposed to all the constructions we saw in Chapter 13. Finally, signatures based on hash functions can be more efficient than those relying on number-theoretic assumptions.

基于哈希函数的签名之所以有趣，还有其他几个原因。首先，与公钥加密方案不同，签名居然可以在没有任何数论假设的前提下构造出来，这一点令人惊叹（也许还有些反直觉）。其次，正如我们将看到的，这里发展的思想可用于在“单向函数存在”这一最小假设下构造签名方案。同样值得注意的是，与第 13 章看到的所有构造不同，这里给出的方案不依赖随机预言机。最后，基于哈希函数的签名可能比依赖数论假设的签名更高效。

In the rest of this section, we no longer mention quantum attacks explicitly. However, all security claims hold against such attacks so long as the hash function used is quantum-secure (in the appropriate sense).

在本节余下部分，我们不再明确提及量子攻击。不过，只要所用哈希函数是量子安全的（在适当的意义下），所有安全性论断对这类攻击同样成立。

### 14.4.1 Lamport's Signature Scheme　Lamport 签名方案

We initiate our study of signature schemes based on hash functions by considering the relatively weak notion of one-time signature schemes. Informally, such schemes are “secure” as long as a given private key is used to sign only a single message. Schemes satisfying this notion of security may be appropriate for some applications, and also serve as useful building blocks for achieving stronger notions of security, as we will see in the following section.

我们从相对较弱的一次性签名方案概念入手，开始研究基于哈希函数的签名方案。非正式地说，只要给定的私钥只用来签署一条消息，这类方案就是“安全”的。满足这种安全概念的方案可能适用于某些应用，而且正如下一节将看到的，它们还是实现更强安全概念的有用构建模块。

Let $\Pi = (\mathsf{Gen}, \mathsf{Sign}, \mathsf{Vrfy})$ be a signature scheme, and consider the following experiment for an adversary $\mathcal{A}$ and parameter $n$:

设 $\Pi = (\mathsf{Gen}, \mathsf{Sign}, \mathsf{Vrfy})$ 是一个签名方案，并考虑针对敌手 $\mathcal{A}$ 和参数 $n$ 的如下实验：

The one-time signature experiment $\mathsf{Sig-forge}_{\mathcal{A},\Pi}^{1\text{-time}}(n)$:

一次性签名实验 $\mathsf{Sig-forge}_{\mathcal{A},\Pi}^{1\text{-time}}(n)$：

1. Gen ${1}^{n}$ is run to obtain keys $(pk, sk)$.

1. 运行 Gen ${1}^{n}$ 得到密钥 $(pk, sk)$。

2. Adversary $\mathcal{A}$ is given $pk$ and asks a single query $m^{\prime}$ to its oracle $\mathsf{Sign}_{sk}(\cdot)$. $\mathcal{A}$ then outputs $(m,\sigma)$ with $m \neq m^{\prime}$.

2. 敌手 $\mathcal{A}$ 得到 $pk$，并向其预言机 $\mathsf{Sign}_{sk}(\cdot)$ 发起一次查询 $m^{\prime}$。随后 $\mathcal{A}$ 输出满足 $m \neq m^{\prime}$ 的 $(m,\sigma)$。

3. The output of the experiment is defined to be 1 if and only if $\operatorname{Vrfy}_{pk}(m,\sigma)=1$.

3. 当且仅当 $\operatorname{Vrfy}_{pk}(m,\sigma)=1$ 时，实验的输出定义为 1。

DEFINITION 14.8 Signature scheme $\Pi = (\mathrm{Gen}, \mathrm{Sign}, \mathrm{Vrfy})$ is existentially unforgeable under a single-message attack, or is a one-time signature scheme, if for all probabilistic polynomial-time adversaries $\mathcal{A}$, there exists a negligible function $\mathrm{negl}$ such that:

$$\Pr\left[\mathsf{Sig-forge}_{\mathcal{A},\Pi}^{1-\mathsf{time}}(n)=1\right]\leq\mathsf{negl}(n).$$

定义 14.8　若对于所有概率多项式时间敌手 $\mathcal{A}$，都存在可忽略函数 $\mathrm{negl}$ 使得上式成立，则称签名方案 $\Pi = (\mathrm{Gen}, \mathrm{Sign}, \mathrm{Vrfy})$ 在单消息攻击下是存在性不可伪造的，或称其为一次性签名方案。

Leslie Lamport gave a construction of a one-time signature scheme in 1979. We illustrate the idea for the case of signing 3-bit messages. Let $H$ be a cryptographic hash function. A private key consists of six uniform values $x_{1,0}$, $x_{1,1}$, $x_{2,0}$, $x_{2,1}$, $x_{3,0}$, $x_{3,1} \in \{0,1\}^n$, and the corresponding public key contains the results obtained by applying H to each of these elements. These keys can be visualized as two-dimensional arrays:

Leslie Lamport 于 1979 年给出了一个一次性签名方案的构造。我们以签署 3 比特消息的情形为例说明其思想。设 $H$ 是一个密码学哈希函数。私钥由六个均匀选取的值 $x_{1,0}$、$x_{1,1}$、$x_{2,0}$、$x_{2,1}$、$x_{3,0}$、$x_{3,1} \in \{0,1\}^n$ 组成，对应的公钥则包含对每个元素应用 H 所得的结果。这些密钥可以形象地表示为二维数组：

$$\begin{array}{l}p k=\left(\begin{matrix}y_{1,0}&y_{2,0}&y_{3,0}\\ y_{1,1}&y_{2,1}&y_{3,1}\end{matrix}\right)\quad s k=\left(\begin{matrix}x_{1,0}&x_{2,0}&x_{3,0}\\ x_{1,1}&x_{2,1}&x_{3,1}\end{matrix}\right).\end{array}$$

To sign a message $m = m_1 m_2 m_3$ (where $m_i \in \{0, 1\}$), the signer releases the appropriate preimage $x_{i,m_i}$ for each bit of the message; the signature $\sigma$ consists of the three values $(x_{1,m_1}, x_{2,m_2}, x_{3,m_3})$. Verification is carried out in the natural way: presented with the candidate signature $(x_1, x_2, x_3)$ on the message $m = m_1 m_2 m_3$, accept if and only if $H(x_i) \overset{?}{=} y_{i,m_i}$ for ${1} \leq i \leq 3$. This is shown graphically in Figure 14.1, and the general case—for messages of any length $\ell$—is described formally in Construction 14.9.

要签署消息 $m = m_1 m_2 m_3$（其中 $m_i \in \{0, 1\}$），签名者为消息的每个比特公开相应的原像 $x_{i,m_i}$；签名 $\sigma$ 由三个值 $(x_{1,m_1}, x_{2,m_2}, x_{3,m_3})$ 组成。验证按自然的方式进行：给定消息 $m = m_1 m_2 m_3$ 上的候选签名 $(x_1, x_2, x_3)$，当且仅当对所有 ${1} \leq i \leq 3$ 都有 $H(x_i) \overset{?}{=} y_{i,m_i}$ 时才接受。图 14.1 给出了图形化展示；一般情形——即任意长度 $\ell$ 的消息——则在构造 14.9 中正式描述。

![Image](https://lsky.jerryxue.top/i/2026/08/25/6a8d86f4f0bdd.jpg)

**FIGURE 14.1: The Lamport scheme used to sign the message m = 011. / 图 14.1：用于签署消息 m = 011 的 Lamport 方案。**

**CONSTRUCTION 14.9**

Let $H: \{0,1\}^* \to \{0,1\}^n$ be a function. Construct a signature scheme for messages of length $\ell = \ell(n)$ as follows:

- Gen: on input ${1}^n$, proceed as follows for $i \in \{1, \ldots, \ell\}$:
  1. Choose uniform $x_{i,0}, x_{i,1} \in \{0,1\}^n$.
  2. Compute $y_{i,0} := H(x_{i,0})$ and $y_{i,1} := H(x_{i,1})$.

The public key $pk$ and the private key $sk$ are

$$pk = \begin{pmatrix} y_{1,0} & y_{2,0} & \cdots & y_{\ell,0} \\ y_{1,1} & y_{2,1} & \cdots & y_{\ell,1} \end{pmatrix} \quad sk = \begin{pmatrix} x_{1,0} & x_{2,0} & \cdots & x_{\ell,0} \\ x_{1,1} & x_{2,1} & \cdots & x_{\ell,1} \end{pmatrix}.$$

- Sign: on input a private key $sk$ as above and a message $m \in \{0,1\}^\ell$ with $m = m_1 \cdots m_\ell$, output the signature $(x_{1,m_1}, \ldots, x_{\ell,m_\ell})$.

- Vrfy: on input a public key $pk$ as above, a message $m \in \{0,1\}^\ell$ with $m = m_1 \cdots m_\ell$, and a signature $\sigma = (x_1, \ldots, x_\ell)$, output 1 if and only if $H(x_i) = y_{i,m_i}$ for all ${1} \leq i \leq \ell$.

The Lamport signature scheme.

**构造 14.9**

设 $H: \{0,1\}^* \to \{0,1\}^n$ 是一个函数。按如下方式构造用于长度为 $\ell = \ell(n)$ 的消息的签名方案：

- Gen：输入 ${1}^n$ 时，对每个 $i \in \{1, \ldots, \ell\}$ 按如下步骤进行：
  1. 均匀选取 $x_{i,0}, x_{i,1} \in \{0,1\}^n$。
  2. 计算 $y_{i,0} := H(x_{i,0})$ 与 $y_{i,1} := H(x_{i,1})$。

公钥 $pk$ 与私钥 $sk$ 为（见上方公式）。

- Sign：输入如上的私钥 $sk$ 与满足 $m = m_1 \cdots m_\ell$ 的消息 $m \in \{0,1\}^\ell$ 时，输出签名 $(x_{1,m_1}, \ldots, x_{\ell,m_\ell})$。

- Vrfy：输入如上的公钥 $pk$、满足 $m = m_1 \cdots m_\ell$ 的消息 $m \in \{0,1\}^\ell$ 以及签名 $\sigma = (x_1, \ldots, x_\ell)$ 时，当且仅当对所有 ${1} \leq i \leq \ell$ 都有 $H(x_i) = y_{i,m_i}$ 时输出 1。

Lamport 签名方案。

After observing a signature on a message, an attacker who wishes to forge a signature on any other message must find a preimage of one of the three “unused” elements in the public key. If $H$ is one-way (see Definition 9.73), then finding any such preimage is computationally difficult.

在观察到一条消息上的签名之后，想伪造其他消息签名的攻击者必须找出公钥中三个“未用”元素之一的原像。若 $H$ 是单向的（见定义 9.73），则找到任何这样的原像在计算上都是困难的。

THEOREM 14.10 Let $\ell$ be any polynomial. If H is a one-way function, then Construction 14.9 is a one-time signature scheme.

定理 14.10　设 $\ell$ 是任意多项式。若 H 是单向函数，则构造 14.9 是一个一次性签名方案。

PROOF Let $\ell = \ell(n)$ throughout. As noted above, the key observation is this: say an attacker $\mathcal{A}$ requests a signature on a message $m^{\prime}$, and consider any other message $m \neq m^{\prime}$. There must be at least one position $i^* \in \{1, \ldots, \ell\}$ on which $m$ and $m^{\prime}$ differ. Say $m_{i^*} = b \neq m^{\prime}_{i^*}$. Then forging a signature on $m$ requires, at least, finding a preimage (under $H$) of element $y_{i^*,b^*}$ of the public key. Since $H$ is one-way, this is infeasible. We now formalize this intuition.

证明　以下恒设 $\ell = \ell(n)$。如上所述，关键的观察是：设攻击者 $\mathcal{A}$ 请求了消息 $m^{\prime}$ 上的签名，考虑任意其他消息 $m \neq m^{\prime}$，则必存在至少一个位置 $i^* \in \{1, \ldots, \ell\}$ 使 $m$ 与 $m^{\prime}$ 不同。设 $m_{i^*} = b \neq m^{\prime}_{i^*}$。那么要在 $m$ 上伪造签名，至少需要找出公钥中元素 $y_{i^*,b^*}$ 在 H 下的原像。由于 H 是单向的，这是不可行的。下面我们把这一直觉形式化。

Let $\Pi$ denote the Lamport scheme, and let $\mathcal{A}$ be a probabilistic polynomial-time adversary. In a particular execution of $\mathsf{Sig-forge}^{1\text{-time}}_{\mathcal{A},\Pi}(n)$, let $m^{\prime}$ denote the message whose signature is requested by $\mathcal{A}$ (we assume without loss of generality that $\mathcal{A}$ always requests a signature on a message), and let $(m, \sigma)$ be the final output of $\mathcal{A}$. We say that $\mathcal{A}$ outputs a forgery at $(i,b)$ if $\mathsf{Vrfy}_{pk}(m,\sigma)=1$ and furthermore $m_{i}\neq m_{i}^{\prime}$ (i.e., messages $m$ and $m^{\prime}$ differ on their $i$th position) and $m_{i}=b\neq m_{i}^{\prime}$. Note that whenever $\mathcal{A}$ outputs a forgery, it outputs a forgery at some $(i,b)$.

记 $\Pi$ 为 Lamport 方案，设 $\mathcal{A}$ 是概率多项式时间敌手。在 $\mathsf{Sig-forge}^{1\text{-time}}_{\mathcal{A},\Pi}(n)$ 的某次执行中，记 $m^{\prime}$ 为 $\mathcal{A}$ 请求签名的消息（不失一般性，假设 $\mathcal{A}$ 总会请求对某个消息的签名），并设 $(m, \sigma)$ 为 $\mathcal{A}$ 的最终输出。若 $\mathsf{Vrfy}_{pk}(m,\sigma)=1$，并且 $m_{i}\neq m_{i}^{\prime}$（即消息 $m$ 与 $m^{\prime}$ 在第 $i$ 位不同）且 $m_{i}=b\neq m_{i}^{\prime}$，则称 $\mathcal{A}$ 在 $(i,b)$ 处输出伪造。注意，每当 $\mathcal{A}$ 输出伪造时，它总是在某个 $(i,b)$ 处输出伪造。

Consider the following PPT algorithm I attempting to invert H:

考虑如下试图对 H 求逆的概率多项式时间算法 I：

**Algorithm I:**

The algorithm is given ${1}^{n}$ and y as input.

**算法 I：**

该算法以 ${1}^{n}$ 和 y 作为输入。

1. Choose uniform $i^* \in \{1, \ldots, \ell\}$ and $b^* \in \{0, 1\}$. Set $y_{i^*, b^*} := y$.

1. 均匀选取 $i^* \in \{1, \ldots, \ell\}$ 与 $b^* \in \{0, 1\}$。置 $y_{i^*, b^*} := y$。

2. For all $i \in \{1, \ldots, \ell\}$ and $b \in \{0,1\}$ with $(i,b) \neq (i^{*},b^{*})$:

2. 对所有满足 $(i,b) \neq (i^{*},b^{*})$ 的 $i \in \{1, \ldots, \ell\}$ 与 $b \in \{0,1\}$：

• Choose uniform $x_{i,b} \in \{0,1\}^{n}$ and set $y_{i,b} := H(x_{i,b})$.

• 均匀选取 $x_{i,b} \in \{0,1\}^{n}$，并置 $y_{i,b} := H(x_{i,b})$。

3. Run $\mathcal{A}$ on input $pk$: $\begin{pmatrix} y_{1,0} & y_{2,0} & \cdots & y_{\ell,0} \\ y_{1,1} & y_{2,1} & \cdots & y_{\ell,1} \end{pmatrix}$.

3. 以公钥 $pk$（即矩阵 $\begin{pmatrix} y_{1,0} & y_{2,0} & \cdots & y_{\ell,0} \\ y_{1,1} & y_{2,1} & \cdots & y_{\ell,1} \end{pmatrix}$）为输入运行 $\mathcal{A}$。

4. When $\mathcal{A}$ requests a signature on the message $m^{\prime}$:

4. 当 $\mathcal{A}$ 请求消息 $m^{\prime}$ 上的签名时：

• If $m^{\prime}_{i^*} = b^{*}$, then $\mathcal{I}$ aborts the execution.

• 若 $m^{\prime}_{i^*} = b^{*}$，则 $\mathcal{I}$ 中止执行。

• Otherwise, $\mathcal{I}$ returns the signature $\sigma = (x_{1,m^{\prime}_1}, \ldots, x_{\ell,m^{\prime}_\ell})$.

• 否则，$\mathcal{I}$ 返回签名 $\sigma = (x_{1,m^{\prime}_1}, \ldots, x_{\ell,m^{\prime}_\ell})$。

5. When $\mathcal{A}$ outputs $(m,\sigma)$ with $\sigma=(x_{1},\ldots,x_{\ell})$:

5. 当 $\mathcal{A}$ 输出满足 $\sigma=(x_{1},\ldots,x_{\ell})$ 的 $(m,\sigma)$ 时：

• If $\mathcal{A}$ outputs a forgery at $(i^{*}, b^{*})$, then output $x_{i^{*}}$.

• 若 $\mathcal{A}$ 在 $(i^{*}, b^{*})$ 处输出伪造，则输出 $x_{i^{*}}$。

Whenever $\mathcal{A}$ outputs a forgery at $(i^*, b^*)$, algorithm $\mathcal{I}$ succeeds in inverting its given input $y$. We are interested in the probability that this occurs when the input to $\mathcal{I}$ is generated by choosing uniform $x \in \{0,1\}^n$ and setting $y := H(x)$ (cf. Definition 9.73). Imagine a “mental experiment” in which $\mathcal{I}$ is given $x$ at the outset, sets $x_{i^{*},b^{*}} := x$, and then always returns a signature to $\mathcal{A}$ in step ${4}$ (i.e., even if $m_{i^{*}} = b^{*}$). The view of $\mathcal{A}$ when run as a subroutine by $\mathcal{I}$ in this mental experiment is distributed identically to the view of $\mathcal{A}$ in experiment $\mathsf{Sig-forge}_{\mathcal{A},\Pi}^{1\text{-time}}(n)$. Because $(i^{*}, b^{*})$ was chosen uniformly at the beginning of the experiment, and the view of $\mathcal{A}$ is independent of this choice, the probability that $\mathcal{A}$ outputs a forgery at $(i^{*}, b^{*})$, conditioned on the fact that $\mathcal{A}$ outputs a forgery at all, is at least ${1}/2\ell$. (The easiest way to see this is to simply consider deferring the choice of $(i^{*}, b^{*})$ to the end of the experiment.) We conclude that, in this mental experiment, the probability that $\mathcal{A}$ outputs a forgery at $(i^{*}, b^{*})$ is at least $\frac{1}{2\ell} \cdot \Pr[\mathsf{Sig-forge}_{\mathcal{A},\Pi}^{1\text{-time}}(n) = 1]$.

每当 $\mathcal{A}$ 在 $(i^*, b^*)$ 处输出伪造时，算法 $\mathcal{I}$ 就成功地对给定的输入 $y$ 求了逆。我们关心的是：当 $\mathcal{I}$ 的输入按“均匀选取 $x \in \{0,1\}^n$ 并置 $y := H(x)$”（参见定义 9.73）生成时，这一事件发生的概率。设想一个“思想实验”：一开始就把 $x$ 交给 $\mathcal{I}$，令其置 $x_{i^{*},b^{*}} := x$，然后在第 ${4}$ 步总是向 $\mathcal{A}$ 返回一个签名（也就是说，即使 $m_{i^{*}} = b^{*}$ 也照样返回）。在这个思想实验中，作为子程序被 $\mathcal{I}$ 运行时 $\mathcal{A}$ 的视图，与实验 $\mathsf{Sig-forge}_{\mathcal{A},\Pi}^{1\text{-time}}(n)$ 中 $\mathcal{A}$ 的视图分布完全相同。由于 $(i^{*}, b^{*})$ 是在实验开始时均匀选取的，而 $\mathcal{A}$ 的视图与该选择无关，因此，在 $\mathcal{A}$ 输出伪造的前提下，它在 $(i^{*}, b^{*})$ 处输出伪造的条件概率至少为 ${1}/2\ell$。（最简单的理解方式是：干脆把 $(i^{*}, b^{*})$ 的选择推迟到实验结束时再做。）于是我们得出结论：在这个思想实验中，$\mathcal{A}$ 在 $(i^{*}, b^{*})$ 处输出伪造的概率至少为 $\frac{1}{2\ell} \cdot \Pr[\mathsf{Sig-forge}_{\mathcal{A},\Pi}^{1\text{-time}}(n) = 1]$。

Returning to the real experiment involving $\mathcal{I}$ as initially described, the key point is that the probability that $\mathcal{A}$ outputs a forgery at $(i^*, b^*)$ is unchanged. This is because the mental experiment and the real experiment coincide if $\mathcal{A}$ outputs a forgery at $(i^*, b^*)$. That is, the experiments only differ if $m_{i^*}^{\prime} = b^*$, but if this happens then it is impossible (by definition) for $\mathcal{A}$ to subsequently output a forgery at $(i^*, b^*)$. So the probability that $\mathcal{A}$ outputs a forgery at $(i^*, b^*)$ is still at least $\frac{1}{2\ell} \cdot \Pr[\mathsf{Sig-forge}_{\mathcal{A},\Pi}^{1-time}(n) = 1]$. In other words,

回到最初描述的涉及 $\mathcal{I}$ 的真实实验，关键点在于：$\mathcal{A}$ 在 $(i^*, b^*)$ 处输出伪造的概率没有改变。这是因为只要 $\mathcal{A}$ 在 $(i^*, b^*)$ 处输出了伪造，思想实验与真实实验就完全一致。换句话说，两个实验仅在 $m_{i^*}^{\prime} = b^*$ 时才会有差别，而一旦发生这种情况，按定义 $\mathcal{A}$ 就不可能随后在 $(i^*, b^*)$ 处输出伪造。所以，$\mathcal{A}$ 在 $(i^*, b^*)$ 处输出伪造的概率仍然至少为 $\frac{1}{2\ell} \cdot \Pr[\mathsf{Sig-forge}_{\mathcal{A},\Pi}^{1-time}(n) = 1]$。换言之，

$$\Pr[\mathsf{Invert}_{\mathcal{I},H}(n)=1]\geq\frac{1}{2\ell}\cdot\Pr[\mathsf{Sig-forge}_{\mathcal{A},\Pi}^{1-\mathsf{time}}(n)=1].$$

Because H is a one-way function, there is a negligible function $\mathsf{negl}$ such that

$$\mathsf{negl}(n)\geq\Pr[\mathsf{Invert}_{\mathcal{I},H}(n)=1].$$

Since $\ell$ is polynomial this implies that $\Pr[\mathsf{Sig-forge}_{\mathcal{A},\Pi}^{1-\text{time}}(n)=1]$ is negligible, completing the proof.

由于 H 是单向函数，存在可忽略函数 $\mathsf{negl}$ 使得上式成立。又因 $\ell$ 是多项式，这意味着 $\Pr[\mathsf{Sig-forge}_{\mathcal{A},\Pi}^{1-\text{time}}(n)=1]$ 可忽略，证明完成。

COROLLARY 14.11 If one-way functions exist, then for any polynomial $\ell$ there is a one-time signature scheme for messages of length $\ell$.

推论 14.11　若单向函数存在，则对任意多项式 $\ell$，存在适用于长度为 $\ell$ 的消息的一次性签名方案。

### 14.4.2 Chain-Based Signatures　基于链的签名

Being able to sign only a single message with a given private key is obviously a significant drawback. We show here an approach based on collision-resistant hash functions that allows a signer to sign arbitrarily many messages, at the expense of maintaining state that must be updated after each signature is generated. In Section 14.4.3 we discuss a more efficient variant of this approach (that still requires state), and then describe how that construction can be made stateless. The result shows that full-fledged signature schemes satisfying Definition 13.2 can be constructed from collision-resistant hash functions.

用给定的私钥只能签署一条消息，这显然是一个重大缺陷。本节给出一种基于抗碰撞哈希函数的方法，允许签名者签署任意多条消息，代价是必须维护一份状态，并在每次生成签名后加以更新。14.4.3 节将讨论这种方法的一个更高效变体（它仍需要状态），随后说明如何把该构造改造为无状态的。结果将表明：完整的、满足定义 13.2 的签名方案可以由抗碰撞哈希函数构造出来。

We first define signature schemes that allow the signer to maintain state that is updated after every signature is produced.

我们首先定义允许签名者维护状态的签名方案；该状态在每产生一个签名后都会更新。

DEFINITION 14.12 A stateful signature scheme is a tuple of probabilistic polynomial-time algorithms (Gen, Sign, Vrfy) satisfying the following:

1. The key-generation algorithm Gen takes as input a security parameter ${1}^{n}$ and outputs $(pk, sk, s_{0})$. These are called the public key, private key, and initial state, respectively. We assume $pk$ and $sk$ each has length at least $n$, and that $n$ can be determined from $pk$, $sk$.

2. The signing algorithm Sign takes as input a private key $sk$, a value $s_{i-1}$, and a message $m \in \{0,1\}^{*}$. It outputs a signature $\sigma$ and a value $s_i$.

3. The deterministic verification algorithm Vrfy takes as input a public key $pk$, a message $m$, and a signature $\sigma$. It outputs a bit $b$.

定义 14.12　有状态签名方案是满足如下条件的一组概率多项式时间算法 (Gen, Sign, Vrfy)：

1. 密钥生成算法 Gen 以安全参数 ${1}^{n}$ 为输入，输出 $(pk, sk, s_{0})$。三者分别称为公钥、私钥和初始状态。我们假设 $pk$ 与 $sk$ 的长度都不小于 $n$，且可以从 $pk$、$sk$ 确定 $n$。

2. 签名算法 Sign 以私钥 $sk$、值 $s_{i-1}$ 和消息 $m \in \{0,1\}^{*}$ 为输入，输出一个签名 $\sigma$ 和一个值 $s_i$。

3. 确定性验证算法 Vrfy 以公钥 $pk$、消息 $m$ 和签名 $\sigma$ 为输入，输出一个比特 $b$。

We require that for every $n$, every $(pk, sk, s_0)$ output by $\mathsf{Gen}(1^n)$, and any messages $m_1, \ldots, m_t \in \{0,1\}^*$, if we iteratively compute $(\sigma_i, s_i) \leftarrow \mathsf{Sign}_{sk, s_{i-1}}(m_i)$ for $i = 1, \ldots, t$, then for every $i \in \{1, \ldots, t\}$, it holds that $\mathsf{Vrfy}_{\text{pk}}(m_i, \sigma_i) = 1$.

我们要求：对每个 $n$、$\mathsf{Gen}(1^n)$ 输出的每组 $(pk, sk, s_0)$ 以及任意消息 $m_1, \ldots, m_t \in \{0,1\}^*$，若对 $i = 1, \ldots, t$ 迭代计算 $(\sigma_i, s_i) \leftarrow \mathsf{Sign}_{sk, s_{i-1}}(m_i)$，则对每个 $i \in \{1, \ldots, t\}$ 都有 $\mathsf{Vrfy}_{\text{pk}}(m_i, \sigma_i) = 1$。

We emphasize that the verifier does not need to know the signer's state in order to verify a signature; in fact, in some schemes the state must be kept secret by the signer in order for security to hold. Signature schemes that do not maintain state (as in Definition 13.1) are called stateless to distinguish them from stateful schemes. Clearly, stateless schemes are preferable (although stateful schemes can still potentially be useful). We introduce stateful signatures as a stepping stone to an eventual stateless construction.

我们要强调：验证者无需知道签名者的状态即可验证签名；事实上，在某些方案中，为了保持安全性，状态反而必须由签名者保密。不维护状态的签名方案（如定义 13.1 那样）称为无状态方案，以区别于有状态方案。显然，无状态方案更受青睐（尽管有状态方案仍可能有其用处）。引入有状态签名，是把它作为通往最终无状态构造的垫脚石。

Security for stateful signatures schemes is exactly analogous to Definition 13.2, with the only subtleties being that the signing oracle returns only the signature (and not the state), and that the signing oracle updates the state each time it is invoked.

有状态签名方案的安全性完全类似于定义 13.2，仅有两处细微差别：签名预言机只返回签名（而不返回状态），并且签名预言机每次被调用时都会更新状态。

For any polynomial $t = t(n)$, we can easily construct a stateful “t-time-secure” signature scheme. (The definition of security here would be the obvious generalization of Definition 14.8.) We can do this by simply letting the public key (resp., private key) consist of $t$ independently generated public keys (resp., private keys) for any one-time signature scheme; i.e., set $pk := \langle pk_1, \ldots, pk_t \rangle$ and $sk := \langle sk_1, \ldots, sk_t \rangle$ where each $(pk_i, sk_i)$ is an independently generated key-pair for some one-time signature scheme. The state is a counter $i$ initially set to 1. To sign a message $m$ using the private key $sk$ and current state $i \leq t$, compute $\sigma \leftarrow \mathsf{Sign}_{sk_i}(m)$ (that is, generate a signature on $m$ using the private key $sk_i$) and output $(\sigma, i)$; the state is updated to $i := i + 1$. Since the state starts at 1, this means the $i$th message is signed using $sk_i$. Verification of a signature $(\sigma, i)$ on a message $m$ is done by checking whether $\sigma$ is a valid signature on $m$ with respect to $pk_i$. This scheme is secure if used to sign $t$ messages since each private key of the underlying one-time scheme is used to sign only a single message.

对任意多项式 $t = t(n)$，都可以轻松构造出一个有状态的“t 次安全”签名方案。（这里的安全定义应是定义 14.8 的显而易见的推广。）做法很简单：让公钥（相应地，私钥）由某个一次性签名方案的 $t$ 个独立生成的公钥（相应地，私钥）组成；即置 $pk := \langle pk_1, \ldots, pk_t \rangle$ 与 $sk := \langle sk_1, \ldots, sk_t \rangle$，其中每个 $(pk_i, sk_i)$ 都是某个一次性签名方案独立生成的密钥对。状态是一个计数器 $i$，初始置为 1。要用私钥 $sk$ 和当前状态 $i \leq t$ 签署消息 $m$，计算 $\sigma \leftarrow \mathsf{Sign}_{sk_i}(m)$（即用私钥 $sk_i$ 生成 $m$ 上的签名），并输出 $(\sigma, i)$；随后状态更新为 $i := i + 1$。由于状态从 1 开始，这意味着第 $i$ 条消息是用 $sk_i$ 签署的。验证消息 $m$ 上的签名 $(\sigma, i)$ 时，只需检查 $\sigma$ 是否是 $m$ 关于 $pk_i$ 的有效签名。该方案若用于签署 $t$ 条消息则是安全的，因为底层一次性方案的每个私钥都只用于签署一条消息。

As described, signatures have constant length (i.e., independent of $t$), but the public key has length linear in $t$. It is possible to trade off the length of the public key and signatures by having the signer compute a Merkle tree $h := \mathcal{MT}(pk_1, \ldots, pk_t)$ (see Section 6.6.2) over the $t$ underlying public keys from the one-time scheme. That is, the public key will now be $\langle t, h \rangle$, and the signature on the $i$th message will include $(\sigma, i)$, as before, along with the $i$th value $pk_i$ and a proof $\pi_i$ that this is the correct value corresponding to $h$. (Verification is done in the natural way.) The public key now has constant size, and the signature length grows only logarithmically with $t$.

如上所述，签名的长度是常数（即与 $t$ 无关），但公钥的长度关于 $t$ 是线性的。可以让签名者在来自一次性方案的 $t$ 个底层公钥之上计算一棵 Merkle 树 $h := \mathcal{MT}(pk_1, \ldots, pk_t)$（见 6.6.2 节），从而在公钥长度与签名长度之间进行权衡。也就是说，此时公钥为 $\langle t, h \rangle$，第 $i$ 条消息上的签名除了像之前一样包含 $(\sigma, i)$ 外，还包括第 $i$ 个值 $pk_i$ 以及证明它是 $h$ 所对应的正确值的证据 $\pi_i$。（验证按自然的方式进行。）这样公钥就是常数大小，而签名长度仅随 $t$ 对数增长。

Since $t$ can be an arbitrary polynomial, why don't the previous schemes give us the solution we are looking for? The main drawback is that they require the upper bound $t$ on the number of messages that can be signed to be fixed in advance, at the time of key generation. This is a potentially severe limitation since once the upper bound is reached a new public key would have to be generated and distributed. We would prefer instead to have a single, fixed public key that can be used to sign an unbounded number of messages.

既然 $t$ 可以是任意多项式，为什么前面的方案仍没有给出我们想要的解呢？主要缺点在于：它们要求可签消息数的上界 $t$ 在密钥生成时就预先固定。这可能是一个严重的限制，因为一旦达到上界，就必须重新生成并分发新的公钥。我们更希望有一个单一的、固定的公钥，能够用来签署数量无上限的消息。

Let $\Pi = (\mathrm{Gen}, \mathrm{Sign}, \mathrm{Vrfy})$ be a one-time signature scheme. In the scheme we have just described (ignoring the Merkle-tree optimization), the signer runs $t$ invocations of $\mathrm{Gen}$ to obtain public keys $pk_1, \ldots, pk_t$, and includes each of these in its actual public key $pk$. The signer is then restricted to signing at most $t$ messages. We can do better by using a “chain-based” scheme in which the signer generates additional public keys on-the-fly, as needed.

设 $\Pi = (\mathrm{Gen}, \mathrm{Sign}, \mathrm{Vrfy})$ 是一次性签名方案。在上面刚描述的方案中（暂不考虑 Merkle 树优化），签名者运行 $t$ 次 $\mathrm{Gen}$ 得到公钥 $pk_1, \ldots, pk_t$，并把它们全部纳入其实际公钥 $pk$ 中。于是签名者最多只能签署 $t$ 条消息。我们可以做得更好：使用一种“基于链的”方案，签名者按需即时生成新的公钥。

In the chain-based scheme, the public key consists of just a single public key $pk_1$ generated using $\mathsf{Gen}$, and the private key is just the associated private key $sk_1$. To sign the first message $m_1$, the signer first generates a new key-pair $(pk_2, sk_2)$ using $\mathsf{Gen}$, and then signs both $m_1$ and $pk_2$ using $sk_1$ to obtain $\sigma_1 \leftarrow \mathsf{Sign}_{sk_1}(m_1\|pk_2)$. The signature that is output includes both $pk_2$ and $\sigma_1$, and the signer adds $(m_1, pk_2, sk_2, \sigma_1)$ to its current state. In general, when it comes time to sign the ith message the signer will have stored $\{(m_j, pk_{j+1}, sk_{j+1}, \sigma_j)\}_{j=1}^i$ as part of its state. To sign the ith message $m_i$, the signer first generates a new key-pair $(pk_{i+1}, sk_{i+1})$ using $\mathsf{Gen}$, and then signs $m_i$ and $pk_{i+1}$ using $sk_i$ to obtain a signature $\sigma_i \leftarrow \mathsf{Sign}_{sk_i}(m_i\|pk_{i+1})$. The actual signature that is output includes $pk_{i+1}$, $\sigma_i$, and also the values $\{m_j, pk_{j+1}, \sigma_j\}_{j=1}^{i-1}$. The signer then adds $(m_i, pk_{i+1}, sk_{i+1}, \sigma_i)$ to its state. See Figure 14.2 for a graphical depiction of this process.

在基于链的方案中，公钥仅由用 $\mathsf{Gen}$ 生成的一个公钥 $pk_1$ 组成，私钥就是相应的私钥 $sk_1$。要签署第一条消息 $m_1$，签名者先用 $\mathsf{Gen}$ 生成新密钥对 $(pk_2, sk_2)$，然后用 $sk_1$ 同时签署 $m_1$ 与 $pk_2$，得到 $\sigma_1 \leftarrow \mathsf{Sign}_{sk_1}(m_1\|pk_2)$。输出的签名同时包含 $pk_2$ 和 $\sigma_1$，签名者把 $(m_1, pk_2, sk_2, \sigma_1)$ 加入其当前状态。一般地，到要签署第 $i$ 条消息时，签名者的状态中已存有 $\{(m_j, pk_{j+1}, sk_{j+1}, \sigma_j)\}_{j=1}^i$。要签署第 $i$ 条消息 $m_i$，签名者先用 $\mathsf{Gen}$ 生成新密钥对 $(pk_{i+1}, sk_{i+1})$，再用 $sk_i$ 签署 $m_i$ 与 $pk_{i+1}$，得到签名 $\sigma_i \leftarrow \mathsf{Sign}_{sk_i}(m_i\|pk_{i+1})$。实际输出的签名包括 $pk_{i+1}$、$\sigma_i$ 以及值 $\{m_j, pk_{j+1}, \sigma_j\}_{j=1}^{i-1}$。随后签名者把 $(m_i, pk_{i+1}, sk_{i+1}, \sigma_i)$ 加入状态。该过程的图形化描述见图 14.2。

To verify a signature $(pk_{i+1}, \sigma_i, \{m_j, pk_{j+1}, \sigma_j\}_{j=1}^{i-1})$ on a message $m = m_i$ with respect to public key $pk_1$, the receiver verifies each link between a public key $pk_j$ and the next public key $pk_{j+1}$ in the chain, as well as the link between the last public key $pk_i$ and $m$. That is, verification outputs 1 if and only if $\mathsf{Vrfy}_{pk_j}(m_j \| pk_{j+1}, \sigma_j) \overset{?}{=} 1$ for all $j \in \{1, \ldots, i\}$. (Refer to Figure 14.2.)

要在公钥 $pk_1$ 下验证消息 $m = m_i$ 上的签名 $(pk_{i+1}, \sigma_i, \{m_j, pk_{j+1}, \sigma_j\}_{j=1}^{i-1})$，接收方需要验证链中相邻两个公钥 $pk_j$ 与 $pk_{j+1}$ 之间的每一环，以及最后一个公钥 $pk_i$ 与 $m$ 之间的那一环。也就是说，当且仅当对所有 $j \in \{1, \ldots, i\}$ 都有 $\mathsf{Vrfy}_{pk_j}(m_j \| pk_{j+1}, \sigma_j) \overset{?}{=} 1$ 时，验证输出 1。（参见图 14.2。）

It is not hard to be convinced—at least on an intuitive level—that this signature scheme is existentially unforgeable under an adaptive chosen-message attack (regardless of how many messages are signed). Informally, this is once again due to the fact that each key-pair $(pk_i, sk_i)$ is used to sign only a single “message,” where in this case the “message” is actually a message/public-key pair $m_i\|pk_{i+1}$. Since we will prove security of a more efficient scheme in the next section, we do not prove security for the chain-based scheme here.

至少在直观层面上，不难相信这个签名方案在自适应选择消息攻击下是存在性不可伪造的（无论签署了多少条消息）。非正式地说，这仍旧是因为每个密钥对 $(pk_i, sk_i)$ 都只用于签署单个“消息”，只不过这里的“消息”实际上是消息/公钥对 $m_i\|pk_{i+1}$。由于下一节将证明一个更高效方案的安全性，这里不再为基于链的方案证明安全性。

![Image](https://lsky.jerryxue.top/i/2026/08/25/6a8d86f9675cf.jpg)

**FIGURE 14.2: Chain-based signatures: the situation before and after signing the third message $m_{3}$. / 图 14.2：基于链的签名：签署第三条消息 $m_{3}$ 前后的情形。**

In the chain-based scheme, each public key $pk_i$ is used to sign both a message and another public key. Thus, it is essential that the underlying one-time signature scheme $\Pi$ is capable of signing messages longer than the public key. The Lamport scheme presented in Section 14.4.1 does not have this property. However, if we apply the hash-and-sign paradigm from Section 13.3 to the Lamport scheme, we do obtain a one-time signature scheme that can sign messages of arbitrary length. (Although Theorem 13.4 was stated only with regard to signature schemes satisfying Definition 13.2, it is not hard to see that an identical proof works for one-time signature schemes.) Because this result is crucial for the next section, we state it formally. (Note that the existence of collision-resistant hash functions implies the existence of one-way functions; see Exercise 8.4.)

在基于链的方案中，每个公钥 $pk_i$ 既用于签署一条消息，又用于签署另一个公钥。因此，底层的一次性签名方案 $\Pi$ 必须能够签署比公钥更长的消息，这一点至关重要。14.4.1 节介绍的 Lamport 方案并不具备这一性质。但如果把 13.3 节的哈希-签名范式应用于 Lamport 方案，就能得到一个可以签署任意长度消息的一次性签名方案。（虽然定理 13.4 只是针对满足定义 13.2 的签名方案陈述的，但不难看出完全相同的证明对一次性签名方案同样适用。）由于这一结果对下一节至关重要，我们正式叙述如下。（注意，抗碰撞哈希函数的存在蕴含单向函数的存在；见习题 8.4。）

LEMMA 14.13 If collision-resistant hash functions exist, then there exists a one-time signature scheme (for messages of arbitrary length).

引理 14.13　若抗碰撞哈希函数存在，则存在一次性签名方案（适用于任意长度的消息）。

The chain-based signature scheme is a stateful signature scheme that is existentially unforgeable under an adaptive chosen-message attack. It has a number of disadvantages, though. For one, there is no immediate way to eliminate the state (recall that our ultimate goal is a stateless scheme satisfying Definition 13.2). It is also not very efficient, in that the signature length, size of the state, and verification time are all linear in the number of messages that have been signed. Finally, each signature reveals all previously signed messages, and this may be undesirable in some contexts.

基于链的签名方案是有状态的签名方案，在自适应选择消息攻击下存在性不可伪造。但它有一些缺点。其一，没有办法直接消除状态（回顾一下，我们的终极目标是满足定义 13.2 的无状态方案）。其二，它的效率不高：签名长度、状态大小和验证时间都与已签消息的数量呈线性关系。其三，每个签名都会暴露之前签署过的所有消息，这在某些场景下可能不符合需求。

![Image](https://lsky.jerryxue.top/i/2026/08/25/6a8d86ff4827c.jpg)

**FIGURE 14.3: Tree-based signatures (conceptually). / 图 14.3：基于树的签名（概念示意）。**

### 14.4.3 Tree-Based Signatures　基于树的签名

The signer in the chain-based scheme of the previous section can be viewed as maintaining a tree of degree 1, rooted at the public key $pk_1$, and with depth equal to the number of messages signed so far (cf. Figure 14.2). A natural way to improve efficiency is to use a binary tree in which each node has degree 2. As before, a signature will correspond to a “signed” path in the tree from a leaf to the root; as long as the tree has polynomial depth (even if it has exponential size!), verification can be done in polynomial time.

上一节基于链的方案中的签名者，可以看成是在维护一棵度为 1 的树：树根为公钥 $pk_1$，深度等于目前已签的消息数（参见图 14.2）。提高效率的一个自然方法，是改用每个节点度数均为 2 的二叉树。与之前一样，一个签名对应树中从某个叶子到根的一条“被签署”路径；只要树的深度是多项式的（即使其规模是指数级的！），验证就可以在多项式时间内完成。

Concretely, to sign messages of length $n$ we will work with a binary tree of depth $n$ having ${2}^n$ leaves. As before, the signer will add nodes to the tree “on-the-fly,” as needed. In contrast to the chain-based scheme, however, only leaves (and not internal nodes) will be used for signing messages. Each leaf of the tree will correspond to one of the possible messages of length $n$.

具体来说，为了签署长度为 $n$ 的消息，我们将使用一棵深度为 $n$、有 ${2}^n$ 个叶子的二叉树。与之前一样，签名者会按需“动态地”向树中添加节点。但与基于链的方案不同的是，这里只有叶子（而非内部节点）被用于签署消息。树的每个叶子对应一条长度为 $n$ 的可能消息。

In more detail, we imagine a binary tree of depth $n$ where the root is labeled by $\varepsilon$ (i.e., the empty string), and a node that is labeled with the binary string $w$ (of length less than $n$) has left-child labeled $w0$ and right-child labeled $w1$. This tree is never constructed in its entirety (note that it has exponential size), but is instead built up by the signer as needed.

更详细地说，我们设想一棵深度为 $n$ 的二叉树：根标记为 $\varepsilon$（即空串），而标记为二元串 $w$（长度小于 $n$）的节点，其左孩子标记为 $w0$、右孩子标记为 $w1$。这棵树从不被整体构建（注意它有指数级的规模），而是由签名者按需逐步搭建。

For every node $w$, we associate a pair of keys $pk_w$, $sk_w$ for a one-time signature scheme $\Pi$. The public key of the root, $pk_\varepsilon$, is the actual public key of the signer. To sign a message $m \in \{0,1\}^n$, the signer does the following:

对每个节点 $w$，我们关联一次性签名方案 $\Pi$ 的一对密钥 $pk_w$, $sk_w$。根的公钥 $pk_\varepsilon$ 就是签名者实际的公钥。要签署消息 $m \in \{0,1\}^n$，签名者执行以下步骤：

1. It first generates keys (as needed) for all nodes on the path from the root to the leaf labeled m. (Some of these public keys may have been generated in the process of signing previous messages, and in that case are not generated again.)

1. 它首先（按需）为从根到标记为 m 的叶子的路径上的所有节点生成密钥。（其中一些公钥可能在签署之前的消息时已经生成；若是这样，就不再重新生成。）

2. Next, it “certifies” the path from the root to the leaf labeled $m$ by computing a signature on $pk_{w0} \| pk_{w1}$, using private key $sk_{w}$, for each string w that is a proper prefix of m.

2. 接着，对每个作为 $m$ 的真前缀的串 $w$，它用私钥 $sk_{w}$ 计算 $pk_{w0} \| pk_{w1}$ 上的签名，从而“认证”从根到标记为 $m$ 的叶子的路径。

3. Finally, it “certifies” $m$ itself by computing a signature on $m$ using the private key $sk_{m}$.

3. 最后，它用私钥 $sk_{m}$ 计算 $m$ 上的签名，从而“认证” $m$ 本身。

The final signature on $m$ consists of the signature on $m$ with respect to $pk_{m}$, as well as all the information needed to verify the path from the leaf labeled $m$ to the root; see Figure 14.3. Additionally, the signer updates its state by storing all the keys generated as part of the above signing process. A formal description of this scheme is given as Construction 14.14.

$m$ 上的最终签名由两部分组成：关于 $pk_{m}$ 的 $m$ 上的签名，以及验证从标记为 $m$ 的叶子到根的路径所需的全部信息；见图 14.3。此外，签名者会把上述签名过程中生成的所有密钥存储起来，以此更新自己的状态。该方案的形式化描述见构造 14.14。

**CONSTRUCTION 14.14**

Let $\Pi = (\mathsf{Gen}, \mathsf{Sign}, \mathsf{Vrfy})$ be a signature scheme. For a binary string $m$, let $m|_{i} \stackrel{\mathrm{def}}{=} m_{1} \cdots m_{i}$ denote the i-bit prefix of $m$ (with $m|_{0} \stackrel{\mathrm{def}}{=} \varepsilon$, the empty string). Construct the scheme $\Pi^* = (\mathsf{Gen}^*, \mathsf{Sign}^*, \mathsf{Vrfy}^*)$ as follows:
- $\mathsf{Gen}^*$: on input ${1}^n$, compute $(pk_{\varepsilon}, sk_{\varepsilon}) \leftarrow \mathsf{Gen}(1^n)$ and output the public key $pk_{\varepsilon}$. The private key and initial state are $sk_{\varepsilon}$.
- $\mathsf{Sign}^*$: on input a message $m \in \{0,1\}^n$, carry out the following.
1. For $i = 0$ to $n - 1$:
   - If $pk_{m|i,0}, pk_{m|i,1}$, and $\sigma_{m|i}$ are not in the state, compute $(pk_{m|i,0}, sk_{m|i,0}) \leftarrow \mathsf{Gen}(1^n)$, $(pk_{m|i,1}, sk_{m|i,1}) \leftarrow \mathsf{Gen}(1^n)$, and $\sigma_{m|i} \leftarrow \mathsf{Sign}_{sk_{m|i}}(pk_{m|i,0} \parallel pk_{m|i,1})$. In addition, add all of these values to the state.
2. If $\sigma_m$ is not yet included in the state, compute $\sigma_m \leftarrow \mathsf{Sign}_{sk_m}(m)$ and store it as part of the state.
3. Output the signature $\left(\{\sigma_{m|i}, pk_{m|i,0}, pk_{m|i,1}\}_{i=0}^{n-1}, \sigma_m\right)$.
- $\mathsf{Vrfy}^*$: on input a public key $pk_{\varepsilon}$, message $m$, and signature $\left(\{\sigma_{m|i}, pk_{m|i,0}, pk_{m|i,1}\}_{i=0}^{n-1}, \sigma_m\right)$, output 1 if and only if:
1. $\mathsf{Vrfy}_{pk_{m|i}}(pk_{m|i,0} \parallel pk_{m|i,1}, \sigma_{m|i}) \stackrel{?}{=} 1$ for all $i \in \{0, \ldots, n-1\}$.
2. $\mathsf{Vrfy}_{pk_m}(m, \sigma_m) \stackrel{?}{=} 1$.

A “tree-based” signature scheme.

**构造 14.14**

设 $\Pi = (\mathsf{Gen}, \mathsf{Sign}, \mathsf{Vrfy})$ 是一个签名方案。对二元串 $m$，记 $m|_{i} \stackrel{\mathrm{def}}{=} m_{1} \cdots m_{i}$ 为 $m$ 的 $i$ 比特前缀（并令 $m|_{0} \stackrel{\mathrm{def}}{=} \varepsilon$，即空串）。按如下方式构造方案 $\Pi^* = (\mathsf{Gen}^*, \mathsf{Sign}^*, \mathsf{Vrfy}^*)$：
- $\mathsf{Gen}^*$：输入 ${1}^n$ 时，计算 $(pk_{\varepsilon}, sk_{\varepsilon}) \leftarrow \mathsf{Gen}(1^n)$ 并输出公钥 $pk_{\varepsilon}$。私钥与初始状态为 $sk_{\varepsilon}$。
- $\mathsf{Sign}^*$：输入消息 $m \in \{0,1\}^n$ 时，执行以下步骤。
1. 对 $i = 0$ 到 $n - 1$：
   - 若状态中没有 $pk_{m|i,0}$、$pk_{m|i,1}$ 与 $\sigma_{m|i}$，则计算 $(pk_{m|i,0}, sk_{m|i,0}) \leftarrow \mathsf{Gen}(1^n)$、$(pk_{m|i,1}, sk_{m|i,1}) \leftarrow \mathsf{Gen}(1^n)$ 以及 $\sigma_{m|i} \leftarrow \mathsf{Sign}_{sk_{m|i}}(pk_{m|i,0} \parallel pk_{m|i,1})$，并把所有这些值加入状态。
2. 若 $\sigma_m$ 尚未包含在状态中，则计算 $\sigma_m \leftarrow \mathsf{Sign}_{sk_m}(m)$ 并将其存入状态。
3. 输出签名 $\left(\{\sigma_{m|i}, pk_{m|i,0}, pk_{m|i,1}\}_{i=0}^{n-1}, \sigma_m\right)$。
- $\mathsf{Vrfy}^*$：输入公钥 $pk_{\varepsilon}$、消息 $m$ 与签名 $\left(\{\sigma_{m|i}, pk_{m|i,0}, pk_{m|i,1}\}_{i=0}^{n-1}, \sigma_m\right)$ 时，当且仅当下列条件成立时输出 1：
1. 对所有 $i \in \{0, \ldots, n-1\}$ 有 $\mathsf{Vrfy}_{pk_{m|i}}(pk_{m|i,0} \parallel pk_{m|i,1}, \sigma_{m|i}) \stackrel{?}{=} 1$。
2. $\mathsf{Vrfy}_{pk_m}(m, \sigma_m) \stackrel{?}{=} 1$。

“基于树的”签名方案。

Notice that each of the underlying keys in this scheme is used to sign only a single “message.” Each key associated with an internal node signs a pair of public keys, and a key at a leaf is used to sign only a single message. Since each key is used to sign a pair of other keys, we again need the one-time signature scheme $\Pi$ to be capable of signing messages longer than the public key. Lemma 14.13 shows that such schemes can be constructed based on collision-resistant hash functions.

注意，该方案中每个底层密钥都只用于签署单个“消息”。与内部节点关联的每个密钥签署一对公钥，而叶子处的密钥只用于签署一条消息。由于每个密钥都用于签署另外一对密钥，我们再次需要一次性签名方案 $\Pi$ 能够签署比公钥长的消息。引理 14.13 表明，这类方案可以基于抗碰撞哈希函数来构造。

Before proving security of this tree-based approach, note that it improves on the chain-based scheme in a number of respects. It still allows for signing an unbounded number of messages. (Although there are only ${2}^n$ leaves, the message space contains only ${2}^n$ messages. In any case, ${2}^n$ is eventually larger than any polynomial function of $n$.) In terms of efficiency, the signature length and verification time are now proportional to the message length $n$ but are independent of the number of messages signed. The scheme is still stateful, but we will see how this can be avoided after we prove the following result.

在证明这种基于树的方法的安全性之前，先指出它在多方面优于基于链的方案。它仍然允许签署数量无上限的消息。（虽然只有 ${2}^n$ 个叶子，但消息空间本就只含 ${2}^n$ 条消息。无论如何，${2}^n$ 最终总会超过 $n$ 的任何多项式函数。）在效率方面，签名长度和验证时间现在正比于消息长度 $n$，而与已签消息的数量无关。该方案仍是有状态的，但在证明下面的结果之后我们会看到如何避免这一点。

THEOREM 14.15 Let $\Pi$ be a one-time signature scheme. Then Construction 14.14 is a secure signature scheme.

定理 14.15　设 $\Pi$ 是一次性签名方案，则构造 14.14 是一个安全签名方案。

PROOF Let $\Pi^{*}$ denote Construction 14.14. Let $\mathcal{A}^{*}$ be a probabilistic polynomial time adversary, let $\ell^{*}=\ell^{*}(n)$ be a (polynomial) upper bound on the number of signing queries made by $\mathcal{A}^{*}$, and set $\ell=\ell(n)\stackrel{\mathrm{def}}{=}2n\ell^{*}(n)+1$. Note that $\ell$ upper bounds the number of public keys from $\Pi$ that are needed to generate $\ell^{*}$ signatures using $\Pi^{*}$. This is because each signature in $\Pi^{*}$ requires at most ${2}n$ new keys from $\Pi$ (in the worst case), and one additional key from $\Pi$ is used as the actual public key $pk_{\varepsilon}$.

证明　记 $\Pi^{*}$ 为构造 14.14。设 $\mathcal{A}^{*}$ 是概率多项式时间敌手，$\ell^{*}=\ell^{*}(n)$ 是 $\mathcal{A}^{*}$ 发起签名查询次数的（多项式）上界，并置 $\ell=\ell(n)\stackrel{\mathrm{def}}{=}2n\ell^{*}(n)+1$。注意，$\ell$ 是用 $\Pi^{*}$ 生成 $\ell^{*}$ 个签名所需的来自 $\Pi$ 的公钥数的上界。这是因为 $\Pi^{*}$ 中每个签名（最坏情况下）至多需要 ${2}n$ 个新的 $\Pi$ 密钥，另外还有一个来自 $\Pi$ 的密钥被用作实际的公钥 $pk_{\varepsilon}$。

Consider the following PPT adversary $\mathcal{A}$ attacking the one-time signature scheme $\Pi$:

考虑如下攻击一次性签名方案 $\Pi$ 的概率多项式时间敌手 $\mathcal{A}$：

Adversary $\mathcal{A}$:

$\mathcal{A}$ is given as input a public key $pk$ (the security parameter $n$ is implicit).

敌手 $\mathcal{A}$：

$\mathcal{A}$ 得到公钥 $pk$ 作为输入（安全参数 $n$ 是隐含的）。

- Choose a uniform index $i^* \in \{1, \ldots, \ell\}$. Construct a list $pk^1, \ldots, pk^\ell$ of keys as follows:

- 均匀选取指标 $i^* \in \{1, \ldots, \ell\}$。按下述方式构造密钥列表 $pk^1, \ldots, pk^\ell$：

- Set $pk^{i^{*}} := pk$.

- 置 $pk^{i^{*}} := pk$。

- For $i \neq i^{*}$, compute $(pk^{i}, sk^{i}) \leftarrow \mathrm{Gen}(1^{n})$.

- 对 $i \neq i^{*}$，计算 $(pk^{i}, sk^{i}) \leftarrow \mathrm{Gen}(1^{n})$。

- Run $\mathcal{A}^*$ on input public key $pk_\varepsilon = pk^1$. When $\mathcal{A}^*$ requests a signature on a message $m$ do:

- 以公钥 $pk_\varepsilon = pk^1$ 为输入运行 $\mathcal{A}^*$。当 $\mathcal{A}^*$ 请求消息 $m$ 上的签名时，执行：

1. For $i = 0$ to $n - 1$:

1. 对 $i = 0$ 到 $n - 1$：

– If the values $pk_{m|i,0}, pk_{m|i,1}$, and $\sigma_{m|i}$ have not yet been defined, then set $pk_{m|i,0}$ and $pk_{m|i,1}$ equal to the next two unused public keys $pk^j$ and $pk^{j+1}$, and compute a signature $\sigma_{m|i}$ on $pk_{m|i,0} \parallel pk_{m|i,1}$ with respect to $pk_{m|i}$.^3

– 若值 $pk_{m|i,0}$、$pk_{m|i,1}$ 与 $\sigma_{m|i}$ 此前尚未定义，则把 $pk_{m|i,0}$ 和 $pk_{m|i,1}$ 设为接下来的两个尚未使用的公钥 $pk^j$ 与 $pk^{j+1}$，并以 $pk_{m|i}$ 为公钥计算 $pk_{m|i,0} \parallel pk_{m|i,1}$ 上的签名 $\sigma_{m|i}$。^3

> $^3$ If $i \neq i^*$ then $\mathcal{A}$ can compute a signature with respect to $pk_i$ by itself. $\mathcal{A}$ can also obtain a (single) signature with respect to $pk_{i^*}$ by making the appropriate query to its signing oracle. This is what is meant here.

> $^3$ 若 $i \neq i^*$，则 $\mathcal{A}$ 可以自己计算关于 $pk_i$ 的签名。$\mathcal{A}$ 也可以通过向其签名预言机发起适当的查询，获得关于 $pk_{i^*}$ 的（唯一一个）签名。这就是这句话的含义。

2. If $\sigma_{m}$ is not yet defined, compute a signature $\sigma_{m}$ on $m$ with respect to $pk_{m}$ (see footnote 3).

2. 若 $\sigma_{m}$ 尚未定义，则以 $pk_{m}$ 为公钥计算 $m$ 上的签名 $\sigma_{m}$（见脚注 3）。

3. Give $\left\{\sigma_{m|i}, pk_{m|i,0}, pk_{m|i,1}\right\}_{i=0}^{n-1}, \sigma_{m}$ to $\mathcal{A}^{*}$.

3. 把 $\left\{\sigma_{m|i}, pk_{m|i,0}, pk_{m|i,1}\right\}_{i=0}^{n-1}, \sigma_{m}$ 交给 $\mathcal{A}^{*}$。

- Say $\mathcal{A}^*$ outputs a message $m$ (for which it had not previously requested a signature) and a signature $\left(\{\sigma_{m|i}^{\prime}, pk_{m|i,0}^{\prime}, pk_{m|i,1}^{\prime}\}_{i=0}^{n-1}, \sigma_{m}^{\prime}\right)$. If this is a valid signature on $m$, then:

- 设 $\mathcal{A}^*$ 输出消息 $m$（此前未曾为其请求过签名）及签名 $\left(\{\sigma_{m|i}^{\prime}, pk_{m|i,0}^{\prime}, pk_{m|i,1}^{\prime}\}_{i=0}^{n-1}, \sigma_{m}^{\prime}\right)$。若这是 $m$ 上的有效签名，则：

Case 1: Say there exists a $j \in \{0, \ldots, n-1\}$ for which $pk_{m|j,0}^{\prime} \neq pk_{m|j,0}$ or $pk_{m|j,1}^{\prime} \neq pk_{m|j,1}$; this includes the case when $pk_{m|j,0}$ or $pk_{m|j,1}$ were never defined by $\mathcal{A}$. Take the minimal such $j$, and let $i$ be such that $pk^i = pk_{m|j} = pk_{m|j}^{\prime}$ (such an $i$ exists by the minimality of $j$). If $i = i^*$, output $(pk_{m|j,0}^{\prime} \| pk_{m|j,1}^{\prime}, \sigma_{m|j}^{\prime})$.

情形 1：设存在 $j \in \{0, \ldots, n-1\}$ 使得 $pk_{m|j,0}^{\prime} \neq pk_{m|j,0}$ 或 $pk_{m|j,1}^{\prime} \neq pk_{m|j,1}$；这也包括 $pk_{m|j,0}$ 或 $pk_{m|j,1}$ 从未被 $\mathcal{A}$ 定义过的情形。取最小的这样的 $j$，并设 $i$ 满足 $pk^i = pk_{m|j} = pk_{m|j}^{\prime}$（由 $j$ 的最小性可知这样的 $i$ 存在）。若 $i = i^*$，则输出 $(pk_{m|j,0}^{\prime} \| pk_{m|j,1}^{\prime}, \sigma_{m|j}^{\prime})$。

Case 2: If case 1 does not hold, then $pk^{\prime}_{m} = pk_{m}$. Let i be such that $pk^{i} = pk_{m}$. If $i = i^{*}$, output $(m, \sigma^{\prime}_{m})$.

情形 2：若情形 1 不成立，则 $pk^{\prime}_{m} = pk_{m}$。设 $i$ 满足 $pk^{i} = pk_{m}$。若 $i = i^{*}$，则输出 $(m, \sigma^{\prime}_{m})$。

In experiment $\mathsf{Sig-forge}_{\mathcal{A},\Pi}^{1\text{-time}}(n)$, the view of $\mathcal{A}^*$ being run as a subroutine by $\mathcal{A}$ is distributed identically to the view of $\mathcal{A}^*$ in experiment $\mathsf{Sig-forge}_{\mathcal{A}^*,\Pi^*}(n)$.$^4$ Thus, the probability that $\mathcal{A}^*$ outputs a forgery is exactly $\delta(n)$ when it is run as a subroutine by $\mathcal{A}$ in this experiment. Given that $\mathcal{A}^*$ outputs a forgery, consider each of the two possible cases described above:

在实验 $\mathsf{Sig-forge}_{\mathcal{A},\Pi}^{1\text{-time}}(n)$ 中，作为子程序被 $\mathcal{A}$ 运行的 $\mathcal{A}^*$ 的视图，与其在实验 $\mathsf{Sig-forge}_{\mathcal{A}^*,\Pi^*}(n)$ 中的视图分布完全相同。$^4$ 因此，在该实验中作为 $\mathcal{A}$ 的子程序运行时，$\mathcal{A}^*$ 输出伪造的概率恰为 $\delta(n)$。在 $\mathcal{A}^*$ 输出伪造的前提下，分别考虑上面描述的两种可能情形：

Case 1: Since $i^*$ is uniform and independent of the view of $\mathcal{A}^*$, the probability that $i = i^*$ is exactly ${1}/\ell$. If $i = i^*$ then $\mathcal{A}$ requested a signature on the message $pk_{m|j,0}\|pk_{m|j,1}$ with respect to the public key $pk = pk^{i^*} = pk_{m|j}$ that it was given (and requested no other signatures). Moreover,

$$pk_{m|j,0}^{\prime}\|pk_{m|j,1}^{\prime}\neq pk_{m|j,0}\|pk_{m|j,1}$$

and yet $\sigma_{m|j}^{\prime}$ is a valid signature on $pk_{m|j,0}^{\prime}\|pk_{m|j,1}^{\prime}$ with respect to $pk$. Thus, $\mathcal{A}$ outputs a forgery in this case.

情形 1：由于 $i^*$ 是均匀的且独立于 $\mathcal{A}^*$ 的视图，$i = i^*$ 的概率恰为 ${1}/\ell$。若 $i = i^*$，则 $\mathcal{A}$ 曾用它所得到的公钥 $pk = pk^{i^*} = pk_{m|j}$ 请求过消息 $pk_{m|j,0}\|pk_{m|j,1}$ 上的签名（且未请求过其他任何签名）。而且，

$$pk_{m|j,0}^{\prime}\|pk_{m|j,1}^{\prime}\neq pk_{m|j,0}\|pk_{m|j,1}$$

但同时 $\sigma_{m|j}^{\prime}$ 却是 $pk_{m|j,0}^{\prime}\|pk_{m|j,1}^{\prime}$ 关于 $pk$ 的有效签名。因此在这种情形下 $\mathcal{A}$ 输出了伪造。

Case 2: Again, since $i^*$ was chosen uniformly at random and is independent of the view of $\mathcal{A}^*$, the probability that $i = i^*$ is exactly ${1}/\ell$. If $i = i^*$, then $\mathcal{A}$ did not request any signatures with respect to the public key $pk = pk^i = pk_m$ and yet $\sigma^{\prime}_m$ is a valid signature on $m$ with respect to $pk$.

情形 2：同理，由于 $i^*$ 是均匀随机选取的且独立于 $\mathcal{A}^*$ 的视图，$i = i^*$ 的概率恰为 ${1}/\ell$。若 $i = i^*$，则 $\mathcal{A}$ 从未以公钥 $pk = pk^i = pk_m$ 请求过任何签名，而 $\sigma^{\prime}_m$ 却是 $m$ 关于 $pk$ 的有效签名。

We see that, conditioned on $\mathcal{A}^*$ outputting a forgery, $\mathcal{A}$ outputs a forgery with probability exactly ${1}/\ell$. This means that

我们看到，在 $\mathcal{A}^*$ 输出伪造的前提下，$\mathcal{A}$ 输出伪造的概率恰为 ${1}/\ell$。这意味着

$$\begin{array}{r}{\Pr[\mathsf{Sig-forge}_{\mathcal{A},\Pi}^{1\mathrm{-time}}(n)=1]=\Pr[\mathsf{Sig-forge}_{\mathcal{A}^{*},\Pi^{*}}(n)=1]/\ell(n).}\end{array}$$

Because $\Pi$ is a one-time signature scheme, there is a negligible function $\mathsf{negl}$ for which

$$\begin{array}{r}{\Pr[\mathsf{Sig-forge}_{\mathcal{A},\Pi}^{1-\mathsf{time}}(n)=1]\leq\mathsf{negl}(n).}\end{array}$$

Since $\ell$ is polynomial, this means $\Pr[\mathsf{Sig-forge}_{\mathcal{A}^*, \Pi^*}(n) = 1]$ is negligible.

由于 $\Pi$ 是一次性签名方案，存在可忽略函数 $\mathsf{negl}$ 使得上式成立。又因 $\ell$ 是多项式，这意味着 $\Pr[\mathsf{Sig-forge}_{\mathcal{A}^*, \Pi^*}(n) = 1]$ 可忽略。

> $^4$ As we have mentioned, $\mathcal{A}$ never "runs out" of public keys. A signing query of $\mathcal{A}^*$ uses ${2}n$ public keys; thus, even if new public keys were required to answer every signing query of $\mathcal{A}^*$ (which will in general not be the case), only ${2}n\ell^*(n)$ public keys would be needed by $\mathcal{A}$ in addition to the "root" public key $pk_\varepsilon$.

> $^4$ 如前所述，$\mathcal{A}$ 永远不会“用完”公钥。$\mathcal{A}^*$ 的一次签名查询要用掉 ${2}n$ 个公钥；因此，即使回答 $\mathcal{A}^*$ 的每次签名查询都需要全新的公钥（一般并非如此），除“根”公钥 $pk_\varepsilon$ 之外，$\mathcal{A}$ 也只需要再备 ${2}n\ell^*(n)$ 个公钥。

#### A Stateless Solution　无状态解决方案

As described, the signer generates state on-the-fly as needed. However, we can imagine having the signer generate the necessary information for all the nodes in the entire tree in advance, at the time of key generation. (That is, at the time of key generation the signer could generate the keys $\{(pk_w, sk_w)\}$ and the signatures $\{\sigma_w\}$ for all binary strings $w$ of length at most $n$.) If key generation were done in this way, the signer would not have to update its state at all; these values could all be stored as part of a (huge) private key, and we would obtain a stateless scheme. The problem with this approach, of course, is that generating all these values would require exponential time, and storing them all would require exponential memory.

如前所述，签名者是按需动态生成状态的。但我们也可以设想：让签名者在密钥生成时就预先为整棵树的所有节点生成必要信息。（也就是说，在密钥生成时，签名者可以为长度不超过 $n$ 的所有二元串 $w$ 生成密钥 $\{(pk_w, sk_w)\}$ 与签名 $\{\sigma_w\}$。）若密钥生成按这种方式进行，签名者就根本不必更新状态；这些值可以全部存进一个（庞大的）私钥里，从而得到无状态方案。当然，这种做法的问题在于：生成所有这些值需要指数时间，而全部存储它们需要指数级内存。

An alternative is to store some randomness that can be used to generate the values $\{(pk_w, sk_w)\}$ and $\{\sigma_w\}$, as needed, rather than storing the values themselves. That is, the signer could store a random string $r_w$ for each $w$, and whenever the values $pk_w$, $sk_w$ are needed the signer can compute $(pk_w, sk_w) := \mathsf{Gen}(1^n; r_w)$, where this denotes the generation of a length-$n$ key using random coins $r_w$. Similarly, if the signing procedure is probabilistic, the signer can store $r^{\prime}_w$ and then set $\sigma_w := \mathsf{Sign}_{sk_w}(pk_{w0}||pk_{w1}; r^{\prime}_w)$ (assuming here that $|w| < n$). Generating and storing sufficiently many random strings, however, still requires exponential time and memory.

另一种做法是不存储这些值本身，而是存储一些随机性，以便在需要时生成值 $\{(pk_w, sk_w)\}$ 和 $\{\sigma_w\}$。也就是说，签名者可以为每个 $w$ 存储一个随机串 $r_w$，每当需要值 $pk_w$、$sk_w$ 时，就计算 $(pk_w, sk_w) := \mathsf{Gen}(1^n; r_w)$，这里表示利用随机带 $r_w$ 生成长度为 $n$ 的密钥。类似地，若签名过程是概率性的，签名者可以存储 $r^{\prime}_w$，然后置 $\sigma_w := \mathsf{Sign}_{sk_w}(pk_{w0}||pk_{w1}; r^{\prime}_w)$（此处假设 $|w| < n$）。然而，生成并存储足够多的随机串仍需要指数级的时间和内存。

A simple modification of this alternative gives a polynomial-time solution. Instead of storing random $r_w$ and $r^{\prime}_w$ as suggested above, the signer can store two keys $k, k^{\prime}$ for a pseudorandom function $F$. When needed, the values $pk_w, sk_w$ can now be generated by the following two-step process:

对这个替代做法稍作修改就能得到多项式时间的解决方案。签名者不再按上面的建议存储随机的 $r_w$ 和 $r^{\prime}_w$，而是存储伪随机函数 $F$ 的两个密钥 $k, k^{\prime}$。需要时，值 $pk_w, sk_w$ 现在可以通过如下两步生成：

1. Compute $r_w := F_k(w)$^5.

1. 计算 $r_w := F_k(w)$^5。

> $^5$ We assume that the output length of F is sufficiently long, and that w is padded to some fixed-length string in a one-to-one fashion. We ignore these technicalities here.

> $^5$ 我们假设 F 的输出长度足够长，且 w 被以一一对应的方式填充为某个定长串。此处忽略这些技术细节。

2. Compute $(pk_{w}, sk_{w}) := \mathrm{Gen}(1^{n}; r_{w})$ (as before).

2. 计算 $(pk_{w}, sk_{w}) := \mathrm{Gen}(1^{n}; r_{w})$（同前）。

In addition, the key $k^{\prime}$ is used to generate the value $r^{\prime}_w$ that is used to compute the signature $\sigma_w$. This gives a stateless scheme in which key generation (as well as signing and verifying) can be done in polynomial time. Intuitively, this is secure because storing a random function is equivalent to storing all the $r_w$ and $r^{\prime}_w$ values that are needed, and storing a pseudorandom function is “just as good.” We leave it as an exercise to give a formal proof that this modified scheme remains secure.

此外，密钥 $k^{\prime}$ 用于生成值 $r^{\prime}_w$，后者用来计算签名 $\sigma_w$。这样就得到了一个无状态方案，其密钥生成（以及签名与验证）都可以在多项式时间内完成。直观上，这是安全的，因为存储一个随机函数等价于存储所需的全部 $r_w$ 与 $r^{\prime}_w$ 值，而存储伪随机函数“效果一样好”。至于该修改后的方案仍保持安全性的形式化证明，我们留作习题。

Since the existence of collision-resistant hash functions implies the existence of one-way functions (cf. Exercise 8.4), and the latter implies the existence of pseudorandom functions (see Chapter 8), we have:

由于抗碰撞哈希函数的存在蕴含单向函数的存在（参见习题 8.4），而后者又蕴含伪随机函数的存在（见第 8 章），我们有：

THEOREM 14.16 If collision-resistant hash functions exist, then there exists a (stateless) secure signature scheme.

定理 14.16　若抗碰撞哈希函数存在，则存在（无状态的）安全签名方案。

We remark that it is possible to construct signature schemes satisfying Definition 13.2 from the (minimal) assumption that one-way functions exist; a proof of this result is beyond the scope of this book.

我们附带说明：从“单向函数存在”这一（最小）假设出发，构造满足定义 13.2 的签名方案也是可能的；该结果的证明超出本书范围。

## References and Additional Reading　参考文献与延伸阅读

Quantum computing is covered in the text by Nielsen and Chuang [153], which also describes Grover's algorithm [90] and Shor's algorithm [178]. The collision-finding algorithm in Section 14.1.2 is due to Brassard et al. [46].

Nielsen 与 Chuang 的著作 [153] 讲述量子计算，其中也介绍了 Grover 算法 [90] 与 Shor 算法 [178]。14.1.2 节的碰撞查找算法归功于 Brassard 等人 [46]。

For details of the NIST post-quantum cryptography standardization effort, see https://csrc.nist.gov/projects/post-quantum-cryptography. The LWE problem originated in the work of Regev [169]. Several of the candidate public-key encryption schemes submitted to NIST can be viewed as following the approach of the LWE-based scheme presented here (which is also due to Regev [169]), with the most similar being Frodo (see https://frodokem.org).

关于 NIST 后量子密码标准化工作的详情，参见 https://csrc.nist.gov/projects/post-quantum-cryptography。LWE 问题源自 Regev [169] 的工作。提交给 NIST 的若干候选公钥加密方案可以视为遵循这里所介绍的基于 LWE 的方案（该方案同样归功于 Regev [169]）的思路，其中与它最相似的是 Frodo（见 https://frodokem.org）。

Lamport’s signature scheme was published in 1979 [124], although it was already described by Diffie and Hellman [65]. A tree-based construction similar in spirit to Construction 14.14 was suggested by Merkle [138, 139], and a tree-based approach was also used in other schemes [88]. Goldreich [81] suggested a way to make the Goldwasser–Micali–Rivest scheme [88] stateless, and we have adapted his ideas in Section 14.4.3. Naor and Yung [146] showed that one-way permutations suffice for constructing one-time signatures that can sign messages of arbitrary length, and this was improved by Rompel [174], who showed that one-way functions are sufficient. (See also [110].) As we have seen in Section 14.4.3, one-time signatures of this sort can be used to construct secure signature schemes, implying that one-way functions suffice for the existence of (stateless) secure signatures. SPHINCS+ (see https://sphincs.org) is a hash-based signature scheme submitted to the NIST post-quantum cryptography standardization effort.

Lamport 签名方案发表于 1979 年 [124]，不过 Diffie 与 Hellman [65] 早已描述过它。Merkle [138, 139] 提出了在精神上与构造 14.14 类似的基于树的构造，其他一些方案 [88] 也采用了基于树的方法。Goldreich [81] 提出了使 Goldwasser–Micali–Rivest 方案 [88] 无状态的方法，14.4.3 节采纳并改编了他的想法。Naor 与 Yung [146] 证明单向置换足以构造能签署任意长度消息的一次性签名；Rompel [174] 将此结果改进为只需单向函数。（另见 [110]。）正如 14.4.3 节所见，这类一次性签名可用来构造安全签名方案，这意味着单向函数足以保证（无状态）安全签名的存在性。SPHINCS+（见 https://sphincs.org）是提交给 NIST 后量子密码标准化工作的一种基于哈希的签名方案。

## Exercises　习题

14.1 Prove Lemma 14.2.

习题 14.1　证明引理 14.2。

14.2 Prove that the existence of a one-time signature scheme for 1-bit messages implies the existence of one-way functions.

习题 14.2　证明：1 比特消息上的一次性签名方案的存在蕴含单向函数的存在。

14.3 Let $f$ be a one-way permutation. Consider the following signature scheme for messages in the set $\{1, \ldots, \ell\}$:

习题 14.3　设 $f$ 是单向置换。考虑用于集合 $\{1, \ldots, \ell\}$ 中消息的如下签名方案：

- To generate keys, choose uniform $x \in \{0,1\}^n$ and set $y := f^{(\ell)}(x)$ (where $f^{(i)}(\cdot)$ refers to $i$-fold iteration of $f$, and $f^{(0)}(x) \overset{\mathrm{def}}{=} x$). The public key is $y$ and the private key is $x$.

- 生成密钥时，均匀选取 $x \in \{0,1\}^n$ 并置 $y := f^{(\ell)}(x)$（其中 $f^{(i)}(\cdot)$ 表示对 $f$ 迭代 $i$ 次，且 $f^{(0)}(x) \overset{\mathrm{def}}{=} x$）。公钥为 $y$，私钥为 $x$。

- To sign message $i \in \{1, \ldots, \ell\}$, output $f^{(\ell-i)}(x)$.

- 要签署消息 $i \in \{1, \ldots, \ell\}$，输出 $f^{(\ell-i)}(x)$。

- To verify signature $\sigma$ on message $i$ with respect to public key $y$, check whether $y \overset{?}{=} f^{(i)}(\sigma)$.

- 要验证消息 $i$ 上关于公钥 $y$ 的签名 $\sigma$，检查是否成立 $y \overset{?}{=} f^{(i)}(\sigma)$。

(a) Show that the above is not a one-time signature scheme. Given a signature on a message $i$, for what messages $j$ can an adversary output a forgery?

(a) 证明上述方案不是一次性签名方案。给定消息 $i$ 上的一个签名，敌手能对哪些消息 $j$ 输出伪造？

(b) Prove that no PPT adversary given a signature on $i$ can output a forgery on any message $j > i$ except with negligible probability.

(b) 证明：得到消息 $i$ 上签名的任何 PPT 敌手，除可忽略的概率外，都无法对任何消息 $j > i$ 输出伪造。

(c) Suggest how to modify the scheme so as to obtain a one-time signature scheme.

(c) 提出修改该方案的办法，使其成为一次性签名方案。

Hint: Include two values $y, y^{\prime}$ in the public key.

提示：在公钥中加入两个值 $y, y^{\prime}$。

14.4 A strong one-time signature scheme satisfies the following (informally): given a signature $\sigma^{\prime}$ on a message $m^{\prime}$, it is infeasible to output $(m, \sigma) \neq (m^{\prime}, \sigma^{\prime})$ for which $\sigma$ is a valid signature on $m$ (note that $m = m^{\prime}$ is allowed).

习题 14.4　强一次性签名方案（非正式地）满足如下性质：给定消息 $m^{\prime}$ 上的签名 $\sigma^{\prime}$，难以输出满足“$\sigma$ 是 $m$ 上有效签名”的 $(m, \sigma) \neq (m^{\prime}, \sigma^{\prime})$（注意允许 $m = m^{\prime}$）。

(a) Give a formal definition of strong one-time signatures.

(a) 给出强一次性签名的形式化定义。

(b) Assuming the existence of one-way functions, show a one-way function for which Lamport's scheme is not a strong one-time signature scheme.

(b) 在单向函数存在的前提下，给出一个单向函数，使 Lamport 方案相对于它不是强一次性签名方案。

(c) Construct a strong one-time signature scheme based on any assumption used in this book.

(c) 基于本书用过的任一假设构造强一次性签名方案。

Hint: Use a particular one-way function in Lamport's scheme.

提示：在 Lamport 方案中使用某个特定的单向函数。

14.5 Show an adversary attacking the Lamport scheme who obtains signatures on two messages of its choice and can then forge signatures on any message it likes.

习题 14.5　给出一个攻击 Lamport 方案的敌手：它获得自选的两条消息上的签名，随后便能伪造任意它想要的消息上的签名。

14.6 The Lamport scheme uses ${2}\ell$ values in the public key to sign messages of length $\ell$. Consider the variant in which the private key contains ${2}\ell$ values $x_1, \ldots, x_{2\ell}$ and the public key contains the values $y_1, \ldots, y_{2\ell}$ with $y_i := f(x_i)$. A message $m \in \{0,1\}^{\ell}$ is mapped in a one-to-one fashion to a subset $S_m \subset \{1, \ldots, 2\ell\}$ of size $\ell$. To sign $m$, the signer reveals $\{x_i\}_{i \in S_m}$. Prove that this gives a one-time signature scheme. What is the maximum message length $\ell^{\prime}$ that this scheme supports?

习题 14.6　Lamport 方案在公钥中使用 ${2}\ell$ 个值来签署长度为 $\ell$ 的消息。考虑如下变体：私钥包含 ${2}\ell$ 个值 $x_1, \ldots, x_{2\ell}$，公钥包含值 $y_1, \ldots, y_{2\ell}$，其中 $y_i := f(x_i)$。每条消息 $m \in \{0,1\}^{\ell}$ 被一一映射到一个大小为 $\ell$ 的子集 $S_m \subset \{1, \ldots, 2\ell\}$。签署 $m$ 时，签名者公开 $\{x_i\}_{i \in S_m}$。证明这构成一个一次性签名方案。该方案支持的最大消息长度 $\ell^{\prime}$ 是多少？

14.7 At the end of Section 14.4.3, we show how a pseudorandom function can be used to make Construction 14.14 stateless. Does a similar approach work for the chain-based scheme described in Section 14.4.2? If so, sketch a construction and proof. If not, explain why and modify the scheme to obtain a stateless variant.

习题 14.7　在 14.4.3 节末尾，我们展示了如何利用伪随机函数把构造 14.14 变为无状态的。类似的方法对 14.4.2 节描述的基于链的方案可行吗？若可行，简述构造与证明；若不可行，解释原因，并修改该方案以得到无状态的变体。

14.8 Prove Theorem 14.16.

习题 14.8　证明定理 14.16。
