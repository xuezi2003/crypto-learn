# Chapter 10: Algorithms for Factoring and Computing Discrete Logarithms　第 10 章　因子分解与计算离散对数的算法

In the last chapter, we introduced several number-theoretic problems—most prominently, factoring the product of two large primes and computing discrete logarithms in certain groups—that are widely believed to be hard. As defined there, this means there are presumed to be no polynomial-time algorithms for these problems. This asymptotic notion of hardness, however, tells us little about how to set the security parameter—sometimes called the key length, although the terms are not interchangeable—to achieve some desired, concrete level of security in practice. A proper understanding of this issue is extremely important for the real-world deployment of cryptosystems based on these problems. Setting the security parameter too low means a cryptosystem may be vulnerable to attacks more efficient than anticipated; being overly conservative and setting the security parameter too high will give good security, but at the expense of efficiency for the honest users. The relative difficulty of different number-theoretic problems can also play a role in determining which problems to use as the basis for building cryptosystems in the first place.

在上一章中，我们介绍了几个被广泛认为困难的数论问题——其中最突出的是对两个大素数之积进行因子分解，以及在某些群中计算离散对数。按照那里的定义，这意味着假定这些问题不存在多项式时间算法。然而，这种渐近意义上的困难性概念几乎无法告诉我们：应当如何设定安全参数——有时也称作“密钥长度”，尽管这两个术语并不能互换使用——才能在实践中达到某个期望的具体安全级别。正确理解这一问题，对基于这些问题的密码系统在现实世界中的部署极为重要。安全参数设得过低，意味着密码系统可能容易受到比预期更高效的攻击；而过于保守、把安全参数设得过高，虽然能带来良好的安全性，却以牺牲诚实用户的效率为代价。不同数论问题之间的相对难度，也会影响我们在构建密码系统时最初选择以哪些问题为基础。

The fundamental issue, of course, is that a brute-force search may not be the best algorithm for solving a given problem; thus, using key length $n$ does not, in general, give security against attackers running for ${2}^n$ time. This is in contrast to the private-key setting where the best attacks on existing block ciphers have roughly the complexity of brute-force search. As a consequence, the key lengths used in the public-key setting tend to be significantly larger than those used in the private-key setting.

根本问题当然在于：暴力搜索未必是求解给定问题的最佳算法；因此，一般而言，使用长度为 $n$ 的密钥并不能保证抵御运行 ${2}^n$ 时间的攻击者。这与私钥场景形成对照——在那里，针对现有分组密码的最佳攻击复杂度大致相当于暴力搜索。其结果是，公钥场景中使用的密钥长度往往明显大于私钥场景中所用的密钥长度。

To gain a better appreciation of this point, we explore in this chapter several algorithms for factoring and computing discrete logarithms that do not run in polynomial time, but nevertheless perform far better than brute-force search. The goal is merely to give a taste of existing algorithms for these problems, as well as to provide some basic guidance for setting parameters in practice. Our focus is on the high-level ideas, and we consciously do not address many important implementation-level details that would be critical to deal with if these algorithms were to be used in practice. We also concentrate exclusively on classical algorithms here, deferring a discussion about the effect of quantum algorithms to Chapter 14.

为了更好地体会这一点，本章将探讨几种用于因子分解和计算离散对数的算法。它们虽然不是多项式时间算法，性能却远优于暴力搜索。我们的目标只是让读者初步领略求解这些问题的现有算法，并为实践中设置参数提供一些基本指导。我们关注的是主要思想，并有意识地不去讨论许多重要的实现层面的细节——若要在实践中使用这些算法，那些细节将是必须认真处理的关键。此外，这里只专注于经典算法，量子算法的影响留待第 14 章讨论。

The reader may also notice that we only describe algorithms for factoring and computing discrete logarithms, and not algorithms for, say, solving the RSA or decisional Diffie–Hellman problems. Our choice is justified by the facts that the best known algorithms for solving RSA require factoring the modulus, and (in the groups discussed in Sections 9.3.3 and 9.3.4) the best known approaches for solving the decisional Diffie–Hellman problem require computing discrete logarithms.

读者可能还会注意到，我们只描述了因子分解和计算离散对数的算法，而没有给出例如求解 RSA 问题或判定性 Diffie–Hellman 问题的算法。这样选择有如下依据：求解 RSA 问题的已知最佳算法需要对模数进行因子分解，而且（在 9.3.3 节和 9.3.4 节讨论的群中）求解判定性 Diffie–Hellman 问题的已知最佳途径需要计算离散对数。

## 10.1 Algorithms for Factoring　因子分解算法

Throughout this chapter, we assume that $N = pq$ is a product of two distinct primes with $p < q$. We will be most interested in the case when $p$ and $q$ each has the same (known) length $n$, and so $n = \Theta(\log N)$.

在本章中，我们始终假设 $N = pq$ 是两个不同素数的乘积，且 $p < q$。我们最感兴趣的是 $p$ 和 $q$ 具有相同（且已知）长度 $n$ 的情形，此时 $n = \Theta(\log N)$。

We will frequently use the Chinese remainder theorem along with the notation developed in Section 9.1.5. The Chinese remainder theorem states that

我们将频繁使用中国剩余定理以及 9.1.5 节中引入的记号。中国剩余定理断言：

$$
\mathbb{Z}_{N}\simeq\mathbb{Z}_{p}\times\mathbb{Z}_{q}\quad\text{and}\quad\mathbb{Z}_{N}^{*}\simeq\mathbb{Z}_{p}^{*}\times\mathbb{Z}_{q}^{*},
$$

with isomorphism given by $f(x) \stackrel{\mathrm{def}}{=} ([x \bmod p], [x \bmod q])$. The fact that $f$ is an isomorphism means, in particular, that it gives a bijection between elements $x \in \mathbb{Z}_N$ and pairs $(x_p, x_q) \in \mathbb{Z}_p \times \mathbb{Z}_q$. We write $x \leftrightarrow (x_p, x_q)$ to denote this bijection, with $x_p = [x \bmod p]$ and $x_q = [x \bmod q]$.

其同构由 $f(x) \stackrel{\mathrm{def}}{=} ([x \bmod p], [x \bmod q])$ 给出。$f$ 是同构这一事实尤其意味着：它在元素 $x \in \mathbb{Z}_N$ 与数对 $(x_p, x_q) \in \mathbb{Z}_p \times \mathbb{Z}_q$ 之间给出了一个双射。我们用 $x \leftrightarrow (x_p, x_q)$ 表示这个双射，其中 $x_p = [x \bmod p]$，$x_q = [x \bmod q]$。

Recall from Section 9.2 that trial division—a trivial, brute-force factoring method—finds a factor of a given number $N$ in time $\mathcal{O}(N^{1/2} \cdot \mathsf{polylog}(N))$. (This is an exponential-time algorithm, since the size of the input is $\|N\|$, the length of the binary representation of $N$, and $\|N\| = \mathcal{O}(\log N)$.$^{1}$) We show here three factoring algorithms with better performance:

回顾 9.2 节可知，试除法这种平凡的暴力因子分解方法可以在 $\mathcal{O}(N^{1/2} \cdot \mathsf{polylog}(N))$ 时间内找出给定数 $N$ 的一个因子。（这是一个指数时间算法，因为输入的规模是 $\|N\|$，即 $N$ 的二进制表示的长度，而 $\|N\| = \mathcal{O}(\log N)$。$^{1}$）本节介绍三种性能更好的因子分解算法：

- Pollard’s $p-1$ method is effective if $p-1$ has only “small” prime factors.

- 若 $p-1$ 只含“小”素因子，则 Pollard $p-1$ 方法有效。

- Pollard’s rho method applies to arbitrary $N$. (As such, it is called a general-purpose factoring algorithm.) Its running time for $N$ of the form discussed at the beginning of this section is $\mathcal{O}(N^{1/4} \cdot \mathsf{polylog}(N))$. Note this is still exponential in n, the length of N.

- Pollard ρ 方法适用于任意 $N$。（因此它被称为通用型因子分解算法。）对本节开头所讨论形式的 $N$，其运行时间为 $\mathcal{O}(N^{1/4} \cdot \mathsf{polylog}(N))$。注意，它关于 $n$（即 $N$ 的长度）仍是指数级的。

- The quadratic sieve algorithm is a general-purpose factoring algorithm that runs in time sub-exponential in the length of $N$. We give a high-level overview of how this algorithm works, but the details are somewhat complex and beyond the scope of this book.

- 二次筛法是一种通用型因子分解算法，其运行时间关于 $N$ 的长度是亚指数级的。我们将概要介绍该算法的工作原理，但其细节较为复杂，超出了本书的范围。

> $^{1}$ Thus, a running time of $N^{\mathcal{O}(1)} = 2^{\mathcal{O}(\|N\|)}$ is exponential, a running time of $2^{o(\log N)} = 2^{o(\|N\|)}$ is sub-exponential, and a running time of $(\log N)^{\mathcal{O}(1)} = \|N\|^{\mathcal{O}(1)}$ is polynomial.
> $^{1}$ 因此，运行时间 $N^{\mathcal{O}(1)} = 2^{\mathcal{O}(\|N\|)}$ 是指数级的，运行时间 $2^{o(\log N)} = 2^{o(\|N\|)}$ 是亚指数级的，而运行时间 $(\log N)^{\mathcal{O}(1)} = \|N\|^{\mathcal{O}(1)}$ 是多项式级的。

The fastest known general-purpose factoring algorithm is the general number field sieve. Heuristically, this algorithm factors its input $N$ in expected time ${2}^{\mathcal{O}((\log N)^{1/3}\cdot(\log\log N)^{2/3})}$, which is sub-exponential in the length of $N$.

目前已知最快的通用型因子分解算法是一般数域筛法（general number field sieve）。在启发式假设下，该算法能在期望时间 ${2}^{\mathcal{O}((\log N)^{1/3}\cdot(\log\log N)^{2/3})}$ 内分解其输入 $N$，这关于 $N$ 的长度是亚指数级的。

### 10.1.1 Pollard's p-1 Algorithm　Pollard $p-1$ 算法

If $N = pq$ and $p-1$ has only “small” prime factors, Pollard’s $p-1$ algorithm can be used to efficiently factor $N$. The basic idea is simple. Let $B$ be an integer for which $(p-1)\mid B$ and $(q-1)\nmid B$; we defer to below the details of how such a $B$ is computed. Say $B = \gamma \cdot (p-1)$ for some integer $\gamma$. Choose a uniform $x \in \mathbb{Z}_N^*$ and compute $y := [x^B - 1 \bmod N]$. (Note that $y$ can be computed using the efficient exponentiation algorithm from Appendix B.2.3.) Since ${1} \leftrightarrow (1,1)$, we have

若 $N = pq$ 且 $p-1$ 只含“小”素因子，就可以用 Pollard $p-1$ 算法高效地分解 $N$。基本思想很简单。取整数 $B$ 使得 $(p-1)\mid B$ 而 $(q-1)\nmid B$；至于这样的 $B$ 如何计算，见下文。设 $B = \gamma \cdot (p-1)$，其中 $\gamma$ 是某个整数。均匀选取 $x \in \mathbb{Z}_N^*$ 并计算 $y := [x^B - 1 \bmod N]$。（注意，可以利用附录 B.2.3 中的高效取幂算法来计算 $y$。）由于 ${1} \leftrightarrow (1,1)$，我们有

$$
\begin{aligned}
y=[x^{B}-1\bmod N]&\leftrightarrow(x_{p},x_{q})^{B}-(1,1)\\
&=(x_{p}^{B}-1\bmod p,x_{q}^{B}-1\bmod q)\\
&=((x_{p}^{p-1})^{\gamma}-1\bmod p,x_{q}^{B}-1\bmod q)\\
&=(0,[x_{q}^{B}-1\bmod q]),
\end{aligned}
$$

using Theorem 9.14 and the fact that the order of $\mathbb{Z}_p^*$ is $p-1$. We show below that, with high probability, $x_q^B \neq 1 \bmod q$. Assuming this is the case, we have obtained an integer $y \in \mathbb{Z}_N^*$ for which

这里用到定理 9.14 以及 $\mathbb{Z}_p^*$ 的阶为 $p-1$ 这一事实。下面我们将证明，以高概率 $x_q^B \neq 1 \bmod q$ 成立。假设确实如此，我们就得到了一个整数 $y \in \mathbb{Z}_N^*$，满足

$$
y=0\bmod p\quad\text{but}\quad y\neq0\bmod q;
$$

that is, $p \mid y$ but $q \nmid y$. This, in turn, implies that $\gcd(y, N) = p$. Thus, a simple gcd computation (which can be done efficiently as described in Appendix B.1.2) yields a prime factor of $N$.

也就是说，$p \mid y$ 但 $q \nmid y$。这进而意味着 $\gcd(y, N) = p$。于是，只需一次简单的 gcd 计算（可按附录 B.1.2 所述高效完成），就能得到 $N$ 的一个素因子。

ALGORITHM 10.1
Pollard’s $p-1$ algorithm for factoring

Input: Integer $N$
Output: A nontrivial factor of $N$

$x \leftarrow \mathbb{Z}_N^*$
$y := [x^B - 1 \bmod N]$
// $B$ is as in the text
$p := \gcd(y, N)$
if $p \notin \{1, N\}$ return $p$

算法 10.1
用于因子分解的 Pollard $p-1$ 算法

输入：整数 $N$
输出：$N$ 的一个非平凡因子

$x \leftarrow \mathbb{Z}_N^*$
$y := [x^B - 1 \bmod N]$
// $B$ 如正文中所述
$p := \gcd(y, N)$
若 $p \notin \{1, N\}$ 则返回 $p$

We now argue that the algorithm works with high probability. Because $(q-1)\nmid B$, as long as $x_q \stackrel{\mathrm{def}}{=} [x \bmod q]$ is a generator of $\mathbb{Z}_q^*$ we must have $x_q^B \neq 1 \bmod q$. (This follows from Proposition 9.53.) It remains to analyze the probability that $x_q$ is a generator. Here we rely on some results proved in Appendix B.3.1. Since $q$ is prime, $\mathbb{Z}_q^*$ is a cyclic group of order $q-1$ that has exactly $\phi(q-1)$ generators (cf. Theorem B.16). If $x$ is chosen uniformly from $\mathbb{Z}_N^*$, then $x_q$ is uniformly distributed in $\mathbb{Z}_q^*$. (This is a consequence of the fact that the Chinese remainder theorem gives a bijection between $\mathbb{Z}_N^*$ and $\mathbb{Z}_p^* \times \mathbb{Z}_q^*$). Thus, the probability that $x_q$ is a generator is $\frac{\phi(q-1)}{q-1} = \Omega(1/\log q) = \Omega(1/n)$ (cf. Theorem B.15). Multiple values of $x$ can be chosen to boost the probability of success.

现在我们论证该算法以高概率成功。由于 $(q-1)\nmid B$，只要 $x_q \stackrel{\mathrm{def}}{=} [x \bmod q]$ 是 $\mathbb{Z}_q^*$ 的生成元，就必有 $x_q^B \neq 1 \bmod q$。（这由命题 9.53 可得。）剩下的就是分析 $x_q$ 是生成元的概率。这里我们要用到附录 B.3.1 中证明的一些结果。由于 $q$ 是素数，$\mathbb{Z}_q^*$ 是阶为 $q-1$ 的循环群，恰有 $\phi(q-1)$ 个生成元（参见定理 B.16）。如果 $x$ 从 $\mathbb{Z}_N^*$ 中均匀选取，那么 $x_q$ 在 $\mathbb{Z}_q^*$ 中均匀分布。（这是中国剩余定理给出 $\mathbb{Z}_N^*$ 与 $\mathbb{Z}_p^* \times \mathbb{Z}_q^*$ 之间双射的推论。）因此，$x_q$ 是生成元的概率为 $\frac{\phi(q-1)}{q-1} = \Omega(1/\log q) = \Omega(1/n)$（参见定理 B.15）。可以选取多个不同的 $x$ 来提高成功概率。

We are left with the problem of finding $B$ such that $(p-1)\mid B$ but $(q-1)\nmid B$. One possibility is to choose $B=\prod_{i=1}^{k} p_{i}^{\lfloor n/\log p_{i}\rfloor}$ for some $k$, where $p_{i}$ denotes the $i$th prime (i.e., $p_{1}=2,p_{2}=3,p_{3}=5,\ldots$) and $n$ is the length of $p$. (Note that $p_{i}^{\lfloor n/\log p_{i}\rfloor}$ is the largest power of $p_{i}$ that can possibly divide $p-1$.) If $p-1$ can be written as $\prod_{i=1}^{k} p_{i}^{e_{i}}$ with $e_{i}\geq0$ (that is, if the largest prime factor of $p-1$ is less than $p_{k}$), then it will hold that $(p-1)\mid B$. In contrast, if $q-1$ has any prime factor larger than $p_{k}$, then $(q-1)\nmid B$.

剩下的问题是找出满足 $(p-1)\mid B$ 但 $(q-1)\nmid B$ 的 $B$。一种可能的做法是对某个 $k$ 取 $B=\prod_{i=1}^{k} p_{i}^{\lfloor n/\log p_{i}\rfloor}$，其中 $p_{i}$ 表示第 $i$ 个素数（即 $p_{1}=2,p_{2}=3,p_{3}=5,\ldots$），而 $n$ 是 $p$ 的长度。（注意，$p_{i}^{\lfloor n/\log p_{i}\rfloor}$ 是有可能整除 $p-1$ 的 $p_{i}$ 的最大幂。）如果 $p-1$ 能写成 $\prod_{i=1}^{k} p_{i}^{e_{i}}$（其中 $e_{i}\geq0$），也就是说 $p-1$ 的最大素因子小于 $p_{k}$，那么必有 $(p-1)\mid B$。反之，如果 $q-1$ 有任何大于 $p_{k}$ 的素因子，则 $(q-1)\nmid B$。

Choosing a larger value for $k$ increases $B$ and so increases the running time of the algorithm (which performs a modular exponentiation to the power $B$). A larger value of $k$ also makes it more likely that $(p-1)\mid B$, but at the same time makes it less likely that $(q-1)\nmid B$. It is, of course, possible to run the algorithm repeatedly using multiple choices for $k$.

把 $k$ 取得更大会使 $B$ 增大，从而增加算法的运行时间（算法要做一次以 $B$ 为指数的模幂运算）。较大的 $k$ 使 $(p-1)\mid B$ 更可能成立，但同时也使 $(q-1)\nmid B$ 不太可能成立。当然，也可以对多个不同的 $k$ 反复运行该算法。

Pollard’s $p-1$ algorithm is thwarted if both $p-1$ and $q-1$ have any large prime factors. (More precisely, the algorithm still works but only for $B$ so large that the algorithm becomes impractical.) For this reason, when generating a modulus $N = pq$ for cryptographic applications, $p$ and $q$ are sometimes chosen to be strong primes, namely, with $(p-1)/2$ and $(q-1)/2$ themselves prime. This ensures that both $p-1$ and $q-1$ have a large prime factor, and so the resulting modulus will not be vulnerable to Algorithm 10.1. Selecting $p$ and $q$ in this way is markedly less efficient than choosing $p$ and $q$ as arbitrary primes. Moreover, if $p$ and $q$ are uniform $n$-bit primes, it is unlikely that either $p-1$ or $q-1$ will have only small prime factors and so unlikely that Algorithm 10.1 will apply. Finally, better factoring algorithms are available anyway (as we will see below). For these reasons, the current consensus is that the added computational cost of generating $p$ and $q$ as strong primes does not yield any appreciable security gains.

如果 $p-1$ 与 $q-1$ 都含有大的素因子，Pollard $p-1$ 算法就会受挫。（更准确地说，算法仍然可行，但所需的 $B$ 会大到使算法失去实用性。）正因如此，在为密码学应用生成模数 $N = pq$ 时，有时会把 $p$ 和 $q$ 选为强素数（strong primes），即 $(p-1)/2$ 和 $(q-1)/2$ 本身也是素数。这保证了 $p-1$ 和 $q-1$ 都有大素因子，从而使所得模数不会受到算法 10.1 的威胁。不过，按这种方式选取 $p$ 和 $q$，效率明显低于把它们取为任意素数。而且，如果 $p$ 和 $q$ 是均匀的 $n$ 比特素数，那么 $p-1$ 或 $q-1$ 只含小素因子的可能性很小，因而算法 10.1 能奏效的可能性也很小。最后，本就有更好的因子分解算法可用（我们将在下文看到）。基于这些原因，目前的共识是：把 $p$ 和 $q$ 生成为强素数所增加的计算开销，并不能带来任何可观的安全性收益。

### 10.1.2 Pollard's rho Algorithm　Pollard ρ 算法

In contrast to Algorithm 10.1, which is only effective for certain moduli, Pollard’s rho algorithm can be used to factor an arbitrary integer $N = pq$; in that sense, it is a general-purpose factoring algorithm. Heuristically, the algorithm factors $N$ with constant probability in $\mathcal{O}(N^{1/4} \cdot \mathsf{polylog}(N))$ time; this is still exponential, but a vast improvement over trial division.

与只对某些模数有效的算法 10.1 不同，Pollard ρ 算法可用于分解任意整数 $N = pq$；在这个意义上，它是一种通用型因子分解算法。在启发式假设下，该算法能以常数概率在 $\mathcal{O}(N^{1/4} \cdot \mathsf{polylog}(N))$ 时间内分解 $N$；这仍是指数级的，但比试除法有了巨大改进。

The core idea of the approach is to find distinct values $x, x^{\prime} \in \mathbb{Z}_N^*$ that are equivalent modulo $p$ (i.e., for which $x = x^{\prime}\bmod p$); call such a pair good. Note that for a good pair $x, x^{\prime}$ it holds that $\gcd(x - x^{\prime}, N) = p$ (since $x \neq x^{\prime}\bmod N$), so computing the gcd gives a nontrivial factor of $N$.

该方法的核心思想是找到两个模 $p$ 等价的不同值 $x, x^{\prime} \in \mathbb{Z}_N^*$（即满足 $x = x^{\prime}\bmod p$）；我们把这样的数对称为“好的”。注意，对好的数对 $x, x^{\prime}$ 有 $\gcd(x - x^{\prime}, N) = p$（因为 $x \neq x^{\prime}\bmod N$），所以计算这个 gcd 就能得到 $N$ 的一个非平凡因子。

How can we find a good pair? Say we choose values $x^{(1)}, \ldots, x^{(k)}$ uniformly from $\mathbb{Z}_N^*$, where $k = 2^{n/2} = \mathcal{O}(\sqrt{p})$. Viewing these in their Chinese remainder representation as $(x_p^{(1)}, x_q^{(1)}), \ldots, (x_p^{(k)}, x_q^{(k)})$, we have that each $x_p^{(i)} \stackrel{\mathrm{def}}{=} [x^{(i)} \bmod p]$ is uniform in $\mathbb{Z}_p^*$. (This follows from bijectivity between $\mathbb{Z}_N^*$ and $\mathbb{Z}_p^* \times \mathbb{Z}_q^*$.) Thus, using the birthday bound of Lemma A.15, we see that with high probability there exist distinct $i, j$ with $x_p^{(i)} = x_p^{(j)}$ or, equivalently, $x^{(i)} = x^{(j)}$ mod $p$. Moreover, Lemma A.15 shows that $x^{(i)} \neq x^{(j)}$ except with negligible probability. Thus, with high probability we obtain a good pair $x^{(i)}, x^{(j)}$ that can be used to find a nontrivial factor of $N$, as discussed earlier.

如何找到好的数对呢？假设我们从 $\mathbb{Z}_N^*$ 中均匀选取值 $x^{(1)}, \ldots, x^{(k)}$，其中 $k = 2^{n/2} = \mathcal{O}(\sqrt{p})$。把这些值按中国剩余表示看成 $(x_p^{(1)}, x_q^{(1)}), \ldots, (x_p^{(k)}, x_q^{(k)})$，则每个 $x_p^{(i)} \stackrel{\mathrm{def}}{=} [x^{(i)} \bmod p]$ 在 $\mathbb{Z}_p^*$ 中都是均匀的。（这由 $\mathbb{Z}_N^*$ 与 $\mathbb{Z}_p^* \times \mathbb{Z}_q^*$ 之间的双射性可得。）于是，利用引理 A.15 的生日界可知，以高概率存在不同的 $i, j$ 使得 $x_p^{(i)} = x_p^{(j)}$，等价地，$x^{(i)} = x^{(j)}$ mod $p$。此外，引理 A.15 还表明，除非发生概率可忽略的例外情形，否则 $x^{(i)} \neq x^{(j)}$。这样，以高概率我们能得到一个好的数对 $x^{(i)}, x^{(j)}$，如前所述，可以用它求出 $N$ 的一个非平凡因子。

ALGORITHM 10.2
Pollard’s rho algorithm for factoring

Input: Integer $N$, a product of two $n$-bit primes
Output: A nontrivial factor of $N$
$x \leftarrow \mathbb{Z}_{N}^{*}$, $x^{\prime} := x$
for $i = 1$ to ${2}^{n/2}$:
 $x := F(x)$
 $x^{\prime} := F(F(x^{\prime}))$
 $p := \gcd(x - x^{\prime}, N)$
    if $p \notin \{1, N\}$ return $p$ and stop

算法 10.2
用于因子分解的 Pollard ρ 算法

输入：整数 $N$，为两个 $n$ 比特素数之积
输出：$N$ 的一个非平凡因子
$x \leftarrow \mathbb{Z}_{N}^{*}$，$x^{\prime} := x$
对 $i = 1$ 到 ${2}^{n/2}$ 执行：
 $x := F(x)$
 $x^{\prime} := F(F(x^{\prime}))$
 $p := \gcd(x - x^{\prime}, N)$
    若 $p \notin \{1, N\}$ 则返回 $p$ 并停止

We can generate $k = \mathcal{O}(\sqrt{p})$ uniform elements of $\mathbb{Z}_N^*$ in $\mathcal{O}(\sqrt{p}) = \mathcal{O}(N^{1/4})$ time. Testing all pairs of elements in order to identify a good pair, however, would require $\binom{k}{2} = \mathcal{O}(k^2) = \mathcal{O}(p) = \mathcal{O}(N^{1/2})$ time! (Note that since $p$ is unknown we cannot simply compute $x_p^{(1)}, \ldots, x_p^{(k)}$ explicitly and then sort the $x_p^{(i)}$ to find a good pair. Instead, for all distinct pairs $i, j$ we must compute $\gcd(x^{(i)} - x^{(j)}, N)$ to see whether this gives a nontrivial factor of $N$.) Without further optimizations, this will be no better than trial division.

我们可以在 $\mathcal{O}(\sqrt{p}) = \mathcal{O}(N^{1/4})$ 时间内生成 $\mathbb{Z}_N^*$ 的 $k = \mathcal{O}(\sqrt{p})$ 个均匀元素。然而，为了找出一个好的数对而测试所有元素对，将需要 $\binom{k}{2} = \mathcal{O}(k^2) = \mathcal{O}(p) = \mathcal{O}(N^{1/2})$ 的时间！（注意，由于 $p$ 未知，我们不能直接显式计算 $x_p^{(1)}, \ldots, x_p^{(k)}$，再通过对 $x_p^{(i)}$ 排序来找到好的数对；相反，对所有不同的下标对 $i, j$ 都必须计算 $\gcd(x^{(i)} - x^{(j)}, N)$，看它是否给出 $N$ 的非平凡因子。）不做进一步优化的话，这种做法并不比试除法更好。

Pollard’s idea was to use a technique we have seen in Section 6.4.2 in the context of small-space birthday attacks. Specifically, we compute the sequence $x^{(1)}, x^{(2)}, \ldots$ by letting each value be a function of the one before it, i.e., we fix some function $F: \mathbb{Z}_N^* \to \mathbb{Z}_N^*$, choose a uniform $x^{(0)} = x \in \mathbb{Z}_N^*$, and then set $x^{(i)} := F(x^{(i-1)})$ for $i = 1, \ldots, k$. We require $F$ to have the property that if $x = x^{\prime}$ mod $p$, then $F(x) = F(x^{\prime}) \bmod p$; this ensures that once equivalence modulo $p$ occurs, it persists. (A standard choice is $F(x) = [x^2 + 1 \bmod N]$, but any polynomial modulo $N$ will have this property.) If we heuristically model $F$ as a random function, then with high probability there is a good pair in the first $k$ elements of this sequence. Proceeding roughly as in Algorithm 6.9 from Section 6.4.2, we can detect a good pair (if there is one) using only $\mathcal{O}(k)$ gcd computations; see Algorithm 10.2.

Pollard 的想法是使用我们在 6.4.2 节讨论小空间生日攻击时见过的一种技术。具体而言，我们让序列 $x^{(1)}, x^{(2)}, \ldots$ 中的每个值都是前一个值的函数：固定某个函数 $F: \mathbb{Z}_N^* \to \mathbb{Z}_N^*$，均匀选取 $x^{(0)} = x \in \mathbb{Z}_N^*$，然后对 $i = 1, \ldots, k$ 令 $x^{(i)} := F(x^{(i-1)})$。我们要求 $F$ 具有如下性质：若 $x = x^{\prime}$ mod $p$，则 $F(x) = F(x^{\prime}) \bmod p$；这就保证了模 $p$ 的等价一旦出现就会一直保持下去。（标准选择是 $F(x) = [x^2 + 1 \bmod N]$，但任何模 $N$ 的多项式都具有这一性质。）如果我们启发式地把 $F$ 建模为随机函数，那么该序列的前 $k$ 个元素中以高概率存在好的数对。按照与 6.4.2 节算法 6.9 大致相同的步骤，只需 $\mathcal{O}(k)$ 次 gcd 计算就能检测出好的数对（如果存在）；见算法 10.2。

### 10.1.3 The Quadratic Sieve Algorithm　二次筛法

Pollard’s rho algorithm is better than trial division, but still runs in exponential time. The quadratic sieve algorithm runs in sub-exponential time. It was the fastest known factoring algorithm until the early 1990s and remains the factoring algorithm of choice for numbers up to about 300 bits long. We describe the general principles of the algorithm but caution the reader that several important details are omitted.

Pollard ρ 算法优于试除法，但运行时间仍是指数级的。二次筛法的运行时间则是亚指数级的。直到 20 世纪 90 年代初，它一直是已知最快的因子分解算法；至今，对于长度不超过约 300 比特的数，它仍是首选的因子分解算法。我们将描述该算法的一般原理，但要提醒读者，若干重要细节被省略了。

An element $z \in \mathbb{Z}_N^*$ is a quadratic residue modulo $N$ if there is an $x \in \mathbb{Z}_N^*$ such that $x^2 = z \bmod N$; in this case, we say that $x$ is a square root of $z$. The following observations serve as our starting point:

若存在 $x \in \mathbb{Z}_N^*$ 使得 $x^2 = z \bmod N$，则称元素 $z \in \mathbb{Z}_N^*$ 是模 $N$ 的二次剩余；此时我们称 $x$ 是 $z$ 的一个平方根。以下两条观察是我们的出发点：

If $N$ is a product of two distinct, odd primes, then every quadratic residue modulo $N$ has exactly four square roots. (See Section 15.4.2.)

如果 $N$ 是两个不同奇素数之积，那么每个模 $N$ 的二次剩余恰有四个平方根。（参见 15.4.2 节。）

Given $x, y$ with $x^2 = y^2 \bmod N$ and $x \neq \pm y \bmod N$, it is possible to compute a nontrivial factor of $N$ in polynomial time. This is by virtue of the fact that $x^2 = y^2 \bmod N$ implies

给定 $x, y$，如果 $x^2 = y^2 \bmod N$ 且 $x \neq \pm y \bmod N$，就能在多项式时间内计算出 $N$ 的一个非平凡因子。这是因为 $x^2 = y^2 \bmod N$ 蕴含

$$
0=x^{2}-y^{2}=(x-y)(x+y)\bmod N,
$$

and so $N\mid(x-y)(x+y)$. However, $N\nmid(x-y)$ and $N\nmid(x+y)$ because $x\neq\pm y\bmod N$. So it must be the case that $\gcd(x-y,N)$ is equal to one of the prime factors of $N$. (See also Lemma 15.35.)

所以 $N\mid(x-y)(x+y)$。但是，由于 $x\neq\pm y\bmod N$，有 $N\nmid(x-y)$ 且 $N\nmid(x+y)$。因此 $\gcd(x-y,N)$ 必定等于 $N$ 的素因子之一。（另见引理 15.35。）

The quadratic sieve algorithm tries to generate $x, y$ with $x^2 = y^2 \bmod N$ and $x \neq \pm y \bmod N$. A naive way of doing this—which forms the basis of an older factoring algorithm due to Fermat—is to choose an $x \in \mathbb{Z}_N^*,$ compute $q := [x^2 \bmod N]$, and then check whether $q$ is a square over the integers (i.e., without reduction modulo $N$). If so, then $q = y^2$ for some integer $y$ and so $x^2 = y^2 \bmod N$. Unfortunately, the probability that $[x^2 \bmod N]$ is a square is so low that this process must be repeated exponentially many times.

二次筛法试图生成满足 $x^2 = y^2 \bmod N$ 且 $x \neq \pm y \bmod N$ 的 $x, y$。一种朴素的做法是：选取 $x \in \mathbb{Z}_N^*$，计算 $q := [x^2 \bmod N]$，然后检查 $q$ 是否为整数上的平方（即不做模 $N$ 归约）。如果是，则存在整数 $y$ 使 $q = y^2$，从而 $x^2 = y^2 \bmod N$。这种做法构成了费马更早提出的因子分解算法的基础。遗憾的是，$[x^2 \bmod N]$ 是平方的概率太低，以至于上述过程必须重复指数级多次。

A significant improvement is obtained by generating a sequence of values $q_1 := [x_1^2 \bmod N], \ldots$ and identifying a subset of those values whose product is a square over the integers. In the quadratic sieve algorithm this is accomplished using the following two steps:

一个重大改进是：生成一列值 $q_1 := [x_1^2 \bmod N], \ldots$，并从中识别出乘积为整数平方的一个子集。在二次筛法中，这通过以下两步来完成：

Step 1. Fix some bound $B$. Say an integer is $B$-smooth if all its prime factors are less than or equal to $B$. In the first phase of the algorithm, we search for integers of the form $q_i = [x_i^2 \bmod N]$ that are $B$-smooth and factor them. (Although factoring is hard, finding and factoring $B$-smooth numbers is feasible when $B$ is small enough.) These $\{x_i\}$ are chosen by successively trying $x = \sqrt{N} + 1$, $\sqrt{N} + 2, \ldots$; this ensures a nontrivial reduction modulo $N$ (since $x > \sqrt{N}$) and has the advantage that $q \stackrel{\mathrm{def}}{=} [x^2 \bmod N] = x^2 - N$ is “small” so that $q$ is more likely to be $B$-smooth.

第 1 步。固定某个界 $B$。如果一个整数的所有素因子都小于等于 $B$，就称它是 $B$ 光滑的（$B$-smooth）。在算法的第一阶段，我们寻找形如 $q_i = [x_i^2 \bmod N]$ 的 $B$ 光滑整数，并对它们作因子分解。（虽然因子分解是困难的，但当 $B$ 足够小时，寻找并分解 $B$ 光滑数是可行的。）这些 $\{x_i\}$ 通过依次尝试 $x = \sqrt{N} + 1$, $\sqrt{N} + 2, \ldots$ 来选取；这保证了模 $N$ 的归约是非平凡的（因为 $x > \sqrt{N}$），而且有一个好处：$q \stackrel{\mathrm{def}}{=} [x^2 \bmod N] = x^2 - N$ 是“小的”，因而 $q$ 更可能是 $B$ 光滑的。

Let $\{p_1, \ldots, p_k\}$ be the set of prime numbers less than or equal to $B$. Once we have found and factored the $B$-smooth $\{q_i\}$ as described above, we have a set of equations of the form:

令 $\{p_1, \ldots, p_k\}$ 为小于等于 $B$ 的素数构成的集合。一旦像上面那样找到并分解了 $B$ 光滑的 $\{q_i\}$，我们就得到一组形如下式的方程：

$$
q_{1}=[x_{1}^{2}\bmod N]=\prod_{i=1}^{k}p_{i}^{e_{1,i}} \tag{10.1}
$$

$$
\vdots
$$

$$
q_{\ell}=[x_{\ell}^{2}\bmod N]=\prod_{i=1}^{k}p_{i}^{e_{\ell,i}}.
$$

(Note that the above equations are over the integers.)

（注意上述方程是在整数上成立的。）

Step 2. We next want to find some subset of the $\{q_i\}$ whose product is a square. If we multiply some subset $S$ of the $\{q_i\}$, we see that the result

第 2 步。接下来要找出 $\{q_i\}$ 的某个乘积为平方数的子集。如果把 $\{q_i\}$ 的某个子集 $S$ 相乘，可以看到所得结果

$$
z=\prod_{j\in S}q_{j}=\prod_{i=1}^{k}p_{i}^{\sum_{j\in S}e_{j,i}}
$$

is a square if and only if the exponent of each prime $p_i$ is even. This suggests that we care about the exponents $\{e_{j,i}\}$ in Equation (10.1) only modulo 2; moreover, we can use linear algebra to find a subset of the $\{q_i\}$ whose “exponent vectors” sum to the 0-vector modulo 2.

是平方数当且仅当每个素数 $p_i$ 的指数都是偶数。这提示我们：对式 (10.1) 中的指数 $\{e_{j,i}\}$，只需关心其模 2 的值即可；此外，还可以利用线性代数找出 $\{q_i\}$ 的一个子集，使其“指数向量”之和模 2 为零向量。

In more detail: if we reduce the exponents in Equation (10.1) modulo 2, we obtain the 0/1-matrix $\Gamma$ given by

更详细地说：把式 (10.1) 中的指数模 2 归约，就得到如下 0/1 矩阵 $\Gamma$：

$$
\left(\begin{matrix}\gamma_{1,1} & \gamma_{1,2} & \cdots & \gamma_{1,k}\\ \vdots & \vdots & \ddots & \vdots\\ \gamma_{\ell,1} & \gamma_{\ell,2} & \cdots & \gamma_{\ell,k}\\ \end{matrix}\right)\stackrel{\mathrm{def}}{=}\left(\begin{matrix}{[e_{1,1}\bmod2]}&{[e_{1,2}\bmod2]}&\cdots&{[e_{1,k}\bmod2]}\\ {\vdots}&{\vdots}&{\ddots}&{\vdots}\\ {[e_{\ell,1}\bmod2]}&{[e_{\ell,2}\bmod2]}&\cdots&{[e_{\ell,k}\bmod2]}\\ \end{matrix}\right).
$$

If $\ell = k + 1$, then $\Gamma$ has more rows than columns and there must be some nonempty subset $S$ of the rows that sum to the 0-vector modulo 2. Such a subset can be found efficiently using linear algebra. Then:

如果 $\ell = k + 1$，则 $\Gamma$ 的行数多于列数，因而必定存在某个非空的行子集 $S$，其和模 2 为零向量。利用线性代数可以高效地找出这样的子集。于是：

$$
z\stackrel{\mathrm{def}}{=}\prod_{j\in S}q_{j}=\prod_{i=1}^{k}p_{i}^{\sum_{j\in S}e_{j,i}}=\left(\prod_{i=1}^{k}p_{i}^{\left(\sum_{j\in S}e_{j,i}\right)/2}\right)^{2},
$$

using the fact that all the $\left\{\sum_{j\in S} e_{j,i}\right\}$ are even. Since

这里用到所有 $\left\{\sum_{j\in S} e_{j,i}\right\}$ 都是偶数这一事实。由于

$$
z=\prod_{j\in S}q_{j}=\prod_{j\in S}x_{j}^{2}=\left(\prod_{j\in S}x_{j}\right)^{2}\bmod N,
$$

we have obtained two square roots (modulo $N$) of $z$. Although there is no guarantee that these square roots will enable factorization of $N$ (for reasons discussed at the beginning of this section), heuristically they do with constant probability. By taking $\ell > k + 1$ we can obtain multiple subsets $S$ with the desired property and try to factor $N$ using each possibility.

我们就得到了 $z$ 的两个（模 $N$ 意义下的）平方根。虽然无法保证这些平方根一定能分解 $N$（原因见本节开头的讨论），但在启发式假设下，它们能以常数概率做到这一点。取 $\ell > k + 1$ 可以得到多个具有所需性质的子集 $S$，并对每种可能分别尝试分解 $N$。

**Example 10.3**　**例 10.3**

Take $N = 377753$. We have ${6647} = [620^{2} \bmod N]$, and we can factor ${6647}$ (over the integers, without any modular reduction) as

取 $N = 377753$。我们有 ${6647} = [620^{2} \bmod N]$，并且可以在整数上（不做任何模归约）把 ${6647}$ 分解为：

$$
\left[620^{2}\bmod N\right]=6647=17^{2}\cdot23.
$$

Similarly,

类似地，

$$
\left[621^{2}\bmod N\right]=2^{4}\cdot17\cdot29
$$

$$
\left[645^{2}\bmod N\right]=2^{7}\cdot13\cdot23
$$

$$
\left[655^{2}\bmod N\right]=2^{3}\cdot13\cdot17\cdot29.
$$

Letting our subset S include all four of the above equations, we see that

令子集 S 包含上述全部四个等式，可以看到

$$
\begin{aligned}
620^{2}\cdot621^{2}\cdot645^{2}\cdot655^{2}&=2^{14}\cdot13^{2}\cdot17^{4}\cdot23^{2}\cdot29^{2}\bmod N\\
\Rightarrow\left[620\cdot621\cdot645\cdot655\bmod N\right]^{2}&=\left[2^{7}\cdot13\cdot17^{2}\cdot23\cdot29\bmod N\right]^{2}\bmod N\\
\Rightarrow127194^{2}&=45335^{2}\bmod N,
\end{aligned}
$$

with ${127194} \neq \pm45335 \bmod N$. Computing $\gcd(127194 - 45335, 377753) = 751$ yields a nontrivial factor of $N$.

且 ${127194} \neq \pm45335 \bmod N$。计算 $\gcd(127194 - 45335, 377753) = 751$ 就得到 $N$ 的一个非平凡因子。

Running time. Choosing a larger value of $B$ makes it more likely that a uniform value $q = [x^2 \bmod N]$ is $B$-smooth; on the other hand, it means we will have to work harder to identify and factor $B$-smooth numbers, and we will have to find more of them (since we require $\ell > k$, where $k$ is the number of primes less than or equal to $B$). It also means that the matrix $\Gamma$ will be larger, and so the linear-algebraic step will be slower. Choosing the optimal value of $B$ gives an algorithm that (heuristically, at least) factors $N$ in time ${2}^{\mathcal{O}(\sqrt{\log N \cdot \log\log N})}$. (In fact, the constant term in the exponent can be determined quite precisely.) The important point for our purposes is that this is sub-exponential in the length of $N$.

**运行时间。** 把 $B$ 取得更大会使均匀选取的值 $q = [x^2 \bmod N]$ 是 $B$ 光滑的可能性更高；但另一方面，这也意味着识别并分解 $B$ 光滑数要花更多功夫，而且需要找到更多这样的数（因为我们要求 $\ell > k$，其中 $k$ 是小于等于 $B$ 的素数个数）。同时矩阵 $\Gamma$ 也更大，线性代数那一步因此会更慢。选取最优的 $B$ 值，得到的算法（至少在启发式假设下如此）能在时间 ${2}^{\mathcal{O}(\sqrt{\log N \cdot \log\log N})}$ 内分解 $N$。（事实上，指数中的常数项可以被相当精确地确定。）对我们的目的而言，关键在于它关于 $N$ 的长度是亚指数级的。

## 10.2 Algorithms for Computing Discrete Logarithms　计算离散对数的算法

Let $\mathbb{G}$ be a cyclic group of known order $q$. An instance of the discrete-logarithm problem in $\mathbb{G}$ specifies a generator $g \in \mathbb{G}$ and an element $h \in \mathbb{G}$; the goal is to find $x \in \mathbb{Z}_q$ such that $g^x = h$. (See Section 9.3.2.) The solution $x$ is called the discrete logarithm of $h$ with respect to $g$. A trivial brute-force search for $x$ can be done in time $\mathcal{O}(q)$, and so we are interested in algorithms whose running time is better than this.

设 $\mathbb{G}$ 是一个循环群，其阶 $q$ 已知。$\mathbb{G}$ 上离散对数问题的一个实例指定生成元 $g \in \mathbb{G}$ 和元素 $h \in \mathbb{G}$；目标是找到满足 $g^x = h$ 的 $x \in \mathbb{Z}_q$。（参见 9.3.2 节。）解 $x$ 称为 $h$ 关于 $g$ 的离散对数。对 $x$ 做平凡的暴力搜索可以在 $\mathcal{O}(q)$ 时间内完成，因此我们关心的是运行时间优于此的算法。

Algorithms for solving the discrete-logarithm problem fall into two categories: those that are generic and apply to any group $\mathbb{G}$, and those that are tailored to work for some specific class of groups. We begin in this section by discussing three generic algorithms:

求解离散对数问题的算法分为两类：一类是泛型（generic）的，适用于任何群 $\mathbb{G}$；另一类则是针对某类特定群量身定制的。本节先讨论三种泛型算法：

- When the group order $q$ is not prime and a (partial or full) factorization of $q$ is known, the Pohlig–Hellman algorithm reduces the problem of finding discrete logarithms in $\mathbb{G}$ to that of finding discrete logarithms in subgroups of $\mathbb{G}$. When the complete factorization of $q$ is known, the effect is to reduce the complexity of computing discrete logarithms in a group of order $q$ to the complexity of computing discrete logarithms in a group of order $q^{\prime}$, where $q^{\prime}$ is the largest prime dividing $q$. This explains the preference for using prime-order groups (cf. Section 9.3.2).

- 当群的阶 $q$ 不是素数且已知 $q$ 的（部分或完整）因子分解时，Pohlig–Hellman 算法把在 $\mathbb{G}$ 中求离散对数的问题归约为在 $\mathbb{G}$ 的子群中求离散对数的问题。当 $q$ 的完全因子分解已知时，其效果是把在阶为 $q$ 的群中计算离散对数的复杂度归约为在阶为 $q^{\prime}$ 的群中计算离散对数的复杂度，其中 $q^{\prime}$ 是整除 $q$ 的最大素数。这解释了人们为何偏爱使用素数阶群（参见 9.3.2 节）。

- The baby-step/giant-step method, due to Shanks, computes the discrete logarithm in a group of order $q$ using $\mathcal{O}(\sqrt{q})$ group operations. It also requires $\mathcal{O}(\sqrt{q})$ memory.

- 由 Shanks 提出的大步小步方法使用 $\mathcal{O}(\sqrt{q})$ 次群运算计算阶为 $q$ 的群中的离散对数。它还需要 $\mathcal{O}(\sqrt{q})$ 的内存。

- Pollard’s rho algorithm also computes discrete logarithms with $\mathcal{O}(\sqrt{q})$ group operations, but using constant memory. It can be viewed as exploiting the connection between the discrete-logarithm problem and collision-resistant hashing that we have seen in Section 9.4.2.

- Pollard ρ 算法同样用 $\mathcal{O}(\sqrt{q})$ 次群运算计算离散对数，但只使用常数内存。它可以视为利用了我们在 9.4.2 节中看到过的离散对数问题与抗碰撞哈希之间的联系。

It can be shown that the time complexity of the latter two algorithms is optimal as far as generic algorithms are concerned. Thus, to have any hope of doing better we must look at algorithms for specific groups that exploit the binary representation of elements in those groups, i.e., the way group elements are encoded as bit-strings. This point bears some discussion. From a mathematical point of view, any two cyclic groups of the same order are isomorphic, meaning that the groups are identical up to a “renaming” of the group elements. From a computational/algorithmic point of view, however, this “renaming” can have a significant impact. For example, consider the cyclic group $\mathbb{Z}_q$ of integers $\{0, \ldots, q-1\}$ under addition modulo $q$. Computing discrete logarithms in this group is trivial: Say we are given $g, h \in \mathbb{Z}_q$ with $g$ a generator, and we want to find $x$ such that $x \cdot g = h \bmod q$. We must have $\gcd(g, q) = 1$ (cf. Theorem B.16) and so $g$ has a multiplicative inverse $g^{-1}$ modulo $q$. Moreover, $g^{-1}$ can be computed efficiently, as described in Appendix B.2.2. But then $x = h \cdot g^{-1} \bmod q$ is the desired solution. Note that, formally, $x$ here denotes an integer and not a group element—after all, the group operation is addition, not multiplication. Nevertheless, in solving the discrete-logarithm problem in $\mathbb{Z}_q$ we can make use of the fact that another operation (namely, multiplication) can be defined on the elements of that group. The main takeaway point is that the group representation matters.

可以证明，就泛型算法而言，后两种算法的时间复杂度已是最优的。因此，要想有任何机会做得更好，就必须研究针对特定群的算法，利用这些群中元素的二进制表示，也就是群元素被编码为比特串的方式。这一点值得稍作讨论。从数学角度看，任意两个同阶的循环群都同构，也就是说，这些群仅在群元素的“重命名”意义下才有所不同。但从计算/算法的角度看，这种“重命名”可能产生重大影响。例如，考虑整数 $\{0, \ldots, q-1\}$ 在模 $q$ 加法下构成的循环群 $\mathbb{Z}_q$。在这个群里计算离散对数是平凡的：设给定 $g, h \in \mathbb{Z}_q$，其中 $g$ 是生成元，要找满足 $x \cdot g = h \bmod q$ 的 $x$。必有 $\gcd(g, q) = 1$（参见定理 B.16），故 $g$ 在模 $q$ 下有乘法逆元 $g^{-1}$；而且如附录 B.2.2 所述，$g^{-1}$ 可以高效计算。于是 $x = h \cdot g^{-1} \bmod q$ 就是所求解。注意，严格来说这里的 $x$ 表示一个整数而非群元素——毕竟这个群的运算是加法而非乘法。尽管如此，在求解 $\mathbb{Z}_q$ 中的离散对数问题时，我们可以利用这样一个事实：该群的元素上还能定义另一种运算（即乘法）。主要结论是：群的表示很重要。

Turning to groups with cryptographic significance, in Section 10.3 we focus our attention on (subgroups of) $\mathbb{Z}_p^*$ for $p$ prime. (See Section 9.3.3.) As a nontrivial example of an algorithm that is not generic, we give a high-level overview of the index calculus algorithm for solving the discrete-logarithm problem in such groups in sub-exponential time. Currently, the best known algorithm for this class of groups is the general number field sieve, $^2$ which heuristically runs in time ${2}^{\mathcal{O}((\log p)^{1/3} \cdot (\log \log p)^{2/3})}$. Sub-exponential algorithms for computing discrete logarithms in multiplicative subgroups of arbitrary finite fields are also known, but these are beyond our scope.

转向具有密码学意义的群：10.3 节将把注意力集中在素数 $p$ 对应的 $\mathbb{Z}_p^*$（及其子群）上。（参见 9.3.3 节。）作为非泛型算法的一个不平凡的例子，我们将概要介绍指标计算法，它能以亚指数时间求解此类群中的离散对数问题。目前，这类群上已知最好的算法是一般数域筛法，$^2$ 在启发式假设下，其运行时间为 ${2}^{\mathcal{O}((\log p)^{1/3} \cdot (\log \log p)^{2/3})}$。在任意有限域的乘法子群中计算离散对数的亚指数算法同样存在，但这超出了本书的范围。

> $^2$ The algorithm is related to the general number field sieve for factoring.

> $^2$ 该算法与用于因子分解的一般数域筛法相关联。

Importantly, no sub-exponential algorithms are known for computing discrete logarithms in general elliptic-curve groups. This explains why smaller parameters can be used (at the same level of security) when working in elliptic-curve groups than when working in $\mathbb{Z}_p^*$, resulting in more-efficient cryptosystems in the former case.

重要的是，就一般的椭圆曲线群而言，目前尚无已知的计算离散对数的亚指数算法。这解释了为什么在椭圆曲线群中工作时可以使用比在 $\mathbb{Z}_p^*$ 中更小的参数（达到相同的安全级别），从而使前一种情形下的密码系统更加高效。

### 10.2.1 The Pohlig–Hellman Algorithm　Pohlig–Hellman 算法

The Pohlig–Hellman algorithm can be used to speed up the computation of discrete logarithms in a group $\mathbb{G}$ when any nontrivial factors of the group order $q$ are known. Recall that the order of an element $g$, which we denote here by $\operatorname{ord}(g)$, is the smallest positive integer $i$ for which $g^i = 1$. We will need the following lemma:

只要已知 $q$（群 $\mathbb{G}$ 的阶）的某些非平凡因子，就可以用 Pohlig–Hellman 算法加速群 $\mathbb{G}$ 中离散对数的计算。回顾一下，元素 $g$ 的阶（这里记作 $\operatorname{ord}(g)$）是使 $g^i = 1$ 成立的最小正整数 $i$。我们需要下面的引理：

LEMMA 10.4 Let $\operatorname{ord}(g) = q$, and say $p \mid q$. Then $\operatorname{ord}(g^p) = q/p$.

引理 10.4　设 $\operatorname{ord}(g) = q$，再设 $p \mid q$。则 $\operatorname{ord}(g^p) = q/p$。

PROOF Since $(g^p)^{q/p} = g^q = 1$, the order of $g^p$ is at most $q/p$. Let $i > 0$ be such that $(g^p)^i = 1$. Then $g^{pi} = 1$ and, since $q$ is the order of $g$, we must have $pi \geq q$ or equivalently $i \geq q/p$. The order of $g^p$ is thus exactly $q/p$.

证明　由于 $(g^p)^{q/p} = g^q = 1$，故 $g^p$ 的阶至多为 $q/p$。设 $i > 0$ 满足 $(g^p)^i = 1$，则 $g^{pi} = 1$；又由于 $q$ 是 $g$ 的阶，必有 $pi \geq q$，等价地 $i \geq q/p$。因此 $g^p$ 的阶恰好为 $q/p$。

We will also use a generalization of the Chinese remainder theorem: if $q = \prod_{i=1}^{k} q_{i}$ and $\gcd(q_{i}, q_{j}) = 1$ for all $i \neq j$ then

我们还要用到中国剩余定理的一个推广：如果 $q = \prod_{i=1}^{k} q_{i}$ 且对所有 $i \neq j$ 有 $\gcd(q_{i}, q_{j}) = 1$，那么

$$
\mathbb{Z}_{q}\simeq\mathbb{Z}_{q_{1}}\times\cdots\times\mathbb{Z}_{q_{k}}\quad\text{and}\quad\mathbb{Z}_{q}^{*}\simeq\mathbb{Z}_{q_{1}}^{*}\times\cdots\times\mathbb{Z}_{q_{k}}^{*}.
$$

(This can be proved by induction on $k$, using the basic Chinese remainder theorem for $k = 2$.) Moreover, by an extension of the algorithm in Section 9.1.5 it is possible to convert efficiently between the representation of an element as an element of $\mathbb{Z}_q$ and its representation as an element of $\mathbb{Z}_{q_1} \times \cdots \times \mathbb{Z}_{q_k}$ when the factorization $q = \prod_{i=1}^k q_i$ is known.

（对 $k$ 作归纳、并以 $k = 2$ 的基本中国剩余定理为基础，即可证明上式。）此外，将 9.1.5 节的算法加以推广后可知：当因子分解 $q = \prod_{i=1}^k q_i$ 已知时，可以在“元素的 $\mathbb{Z}_q$ 表示”与其“$\mathbb{Z}_{q_1} \times \cdots \times \mathbb{Z}_{q_k}$ 表示”之间高效转换。

We now describe the Pohlig–Hellman algorithm. We are given a generator $g$ and an element $h$ and wish to find $x$ such that $g^x = h$. Say a factorization $q = \prod_{i=1}^{k} q_i$ is known with the $\{q_i\}$ pairwise relatively prime. (This need not be the complete prime factorization of $q$.) We know that

现在描述 Pohlig–Hellman 算法。给定生成元 $g$ 和元素 $h$，希望找到满足 $g^x = h$ 的 $x$。设已知因子分解 $q = \prod_{i=1}^{k} q_i$，其中 $\{q_i\}$ 两两互素。（这不必是 $q$ 的完全素因子分解。）我们知道

$$
\left(g^{q/q_{i}}\right)^{x}=(g^{x})^{q/q_{i}}=h^{q/q_{i}}\quad\text{for }i=1,\ldots,k. \tag{10.2}
$$

Letting $g_i \stackrel{\mathrm{def}}{=} g^{q/q_i}$ and $h_i \stackrel{\mathrm{def}}{=} h^{q/q_i}$, we thus have $k$ instances of a discrete-logarithm problem in $k$ smaller groups. Specifically, each problem $g_i^x = h_i$ is in a subgroup of size $\operatorname{ord}(g_i) = q_i$ (by Lemma 10.4). We can solve each of the $k$ resulting instances using any algorithm for solving the discrete-logarithm problem. Solving these instances gives a set of answers $\{x_i\}_{i=1}^k$, with $x_i \in \mathbb{Z}_{q_i}$, for which $g_i^{x_i} = h_i = g_i^x$. Proposition 9.54 implies that $x = x_i \bmod q_i$ for all $i$. By the generalized Chinese remainder theorem discussed earlier, the constraints

令 $g_i \stackrel{\mathrm{def}}{=} g^{q/q_i}$，$h_i \stackrel{\mathrm{def}}{=} h^{q/q_i}$，于是就得到了 $k$ 个较小群中的 $k$ 个离散对数问题实例。具体来说，每个问题 $g_i^x = h_i$ 都位于大小为 $\operatorname{ord}(g_i) = q_i$ 的子群中（由引理 10.4）。可以用任何求解离散对数问题的算法来解这 $k$ 个实例。求解这些实例得到一组答案 $\{x_i\}_{i=1}^k$（$x_i \in \mathbb{Z}_{q_i}$），满足 $g_i^{x_i} = h_i = g_i^x$。由命题 9.54 可知，对所有 $i$ 有 $x = x_i \bmod q_i$。根据前面讨论的广义中国剩余定理，约束条件

$$
x=x_{1}\bmod q_{1}
$$

$$
\vdots
$$

$$
x=x_{k}\bmod q_{k}
$$

uniquely determine $x$ modulo $q$, and so the desired solution $x$ can be efficiently reconstructed from the $\{x_i\}$.

唯一地确定了模 $q$ 意义下的 $x$，因此可以从 $\{x_i\}$ 高效重构出所求解 $x$。

**Example 10.5**　**例 10.5**

Consider the problem of computing discrete logarithms in $\mathbb{Z}_{31}^*$, a group of order $q = 30 = 5 \cdot 3 \cdot 2$. Say $g = 3$ and $h = 26 = g^x$ with $x$ unknown. We have:

考虑在 $\mathbb{Z}_{31}^*$（一个阶为 $q = 30 = 5 \cdot 3 \cdot 2$ 的群）中计算离散对数的问题。设 $g = 3$，$h = 26 = g^x$，其中 $x$ 未知。我们有：

$$
(g^{30/5})^{x}=h^{30/5}\quad\Rightarrow\quad(3^{6})^{x}=26^{6}\quad\Rightarrow\quad16^{x}=1
$$

$$
(g^{30/3})^{x}=h^{30/3}\quad\Rightarrow\quad(3^{10})^{x}=26^{10}\Rightarrow\quad25^{x}=5
$$

$$
(g^{30/2})^{x}=h^{30/2}\quad\Rightarrow\quad(3^{15})^{x}=26^{15}\Rightarrow30^{x}=30.
$$

(All the above equations are modulo 31.) We have $\operatorname{ord}(16) = 5$, $\operatorname{ord}(25) = 3$, and $\operatorname{ord}(30) = 2$. Solving each equation, we obtain

（以上所有方程均在模 31 意义下。）我们有 $\operatorname{ord}(16) = 5$、$\operatorname{ord}(25) = 3$ 以及 $\operatorname{ord}(30) = 2$。解各个方程可得

$$
x=0\bmod 5,\ x=2\bmod 3,\ \text{and}\ x=1\bmod 2,
$$

and so $x = 5 \bmod 30$. Indeed, ${3}^{5} = 26 \bmod 31$.

从而 $x = 5 \bmod 30$。的确，${3}^{5} = 26 \bmod 31$。

If $q$ has (known) prime factorization $q = \prod_{i=1}^{k} p_{i}^{e_{i}}$ then, by using the Pohlig–Hellman algorithm, the time to compute discrete logarithms in a group of order $q$ is dominated by the computation of a discrete logarithm in a subgroup of size $\max_{i}\{p_{i}^{e_{i}}\}$. This can be further reduced to computation of a discrete logarithm in a subgroup of size $\max_{i}\{p_{i}\}$; see Exercise 10.5.

如果已知 $q$ 的素因子分解 $q = \prod_{i=1}^{k} p_{i}^{e_{i}}$，那么使用 Pohlig–Hellman 算法时，在阶为 $q$ 的群中计算离散对数的时间主要由在大小为 $\max_{i}\{p_{i}^{e_{i}}\}$ 的子群中计算一次离散对数所决定。这还可以进一步归约为在大小为 $\max_{i}\{p_{i}\}$ 的子群中计算离散对数；见习题 10.5。

### 10.2.2 The Baby-Step/Giant-Step Algorithm　大步小步算法

The baby-step/giant-step algorithm computes discrete logarithms in a group of order $q$ using $\mathcal{O}(\sqrt{q})$ group operations. The idea is simple. Given a generator $g \in \mathbb{G}$, we can imagine the powers of $g$ as forming a cycle

大步小步算法使用 $\mathcal{O}(\sqrt{q})$ 次群运算计算阶为 $q$ 的群中的离散对数。想法很简单。给定生成元 $g \in \mathbb{G}$，不妨把 $g$ 的各次幂想象成一个循环

$$
1=g^{0},~g^{1},~g^{2},~\ldots,~g^{q-2},~g^{q-1},~g^{q}=1.
$$

We know that $h$ must lie somewhere in this cycle. Computing all the points in this cycle to find $h$ would take $\Omega(q)$ time. Instead, we “mark off” the cycle at intervals of size $t \stackrel{\mathrm{def}}{=} \lfloor \sqrt{q} \rfloor$; more precisely, we compute and store the $\lfloor q/t \rfloor + 1 = \mathcal{O}(\sqrt{q})$ elements

我们知道 $h$ 必定位于这个循环中的某处。通过计算循环中的所有点来寻找 $h$ 需要 $\Omega(q)$ 时间。作为替代，我们以间隔大小 $t \stackrel{\mathrm{def}}{=} \lfloor \sqrt{q} \rfloor$ 在循环上做“标记”；更精确地说，计算并存储 $\lfloor q/t \rfloor + 1 = \mathcal{O}(\sqrt{q})$ 个元素

$$
g^{0},g^{t},g^{2t},\ldots,g^{\lfloor q/t\rfloor\cdot t}.
$$

(These are the “giant steps.”) Note that the gap between any consecutive “marks” (wrapping around at the end) is at most $t$. Furthermore, we know that $h = g^{x}$ lies in one of these gaps. Thus, if we take “baby steps” and compute the $t$ elements

（这些就是“大步”。）注意，任意相邻两个“标记”之间的间隔（在末端回绕）至多为 $t$。而且，我们知道 $h = g^{x}$ 必落在某个间隔之中。于是，如果我们再走“小步”，计算出 $t$ 个元素

$$
h\cdot g^{1},\cdots,h\cdot g^{t},
$$

each of which corresponds to a “shift” of $h$, we know that one of these values will be equal to one of the marked points. Say we find $h \cdot g^i = g^{k \cdot t}$. We can then easily compute $\log_g h := [(kt - i) \bmod q]$. Pseudocode for this algorithm follows.

其中每个值都对应 $h$ 的一个“平移”，那么这些值中必有一个等于某个标记点。设我们找到 $h \cdot g^i = g^{k \cdot t}$，便能很容易地算出 $\log_g h := [(kt - i) \bmod q]$。该算法的伪代码如下。

ALGORITHM 10.6
The baby-step/giant-step algorithm

Input: Elements $g, h \in \mathbb{G}$; the order $q$ of $\mathbb{G}$
Output: $\log_{g} h$
$t := \lfloor \sqrt{q} \rfloor$
for $i = 0$ to $\lfloor q/t \rfloor$:
    compute $g_{i} := g^{i \cdot t}$
sort the pairs $(i, g_{i})$ by their second component
for $i = 1$ to $t$:
    compute $h_{i} := h \cdot g^{i}$
    if $h_{i} = g_{k}$ for some $k$, return $\left[(kt - i) \bmod q\right]$

算法 10.6
大步小步算法

输入：元素 $g, h \in \mathbb{G}$；$\mathbb{G}$ 的阶 $q$
输出：$\log_{g} h$
$t := \lfloor \sqrt{q} \rfloor$
对 $i = 0$ 到 $\lfloor q/t \rfloor$ 执行：
    计算 $g_{i} := g^{i \cdot t}$
将数对 $(i, g_{i})$ 按第二分量排序
对 $i = 1$ 到 $t$ 执行：
    计算 $h_{i} := h \cdot g^{i}$
    若存在 $k$ 使 $h_{i} = g_{k}$，则返回 $\left[(kt - i) \bmod q\right]$

The algorithm requires $\mathcal{O}(\sqrt{q})$ exponentiations/multiplications in $\mathbb{G}$. (In fact, after computing $g_1 = g^t$, each subsequent value $g_i$ can be computed using a single multiplication as $g_i := g_{i-1} \cdot g_1$. Similarly, each $h_i$ can be computed as $h_i := h_{i-1} \cdot g$.) Sorting the $\mathcal{O}(\sqrt{q})$ pairs $\{(i, g_i)\}$ takes time $\mathcal{O}(\sqrt{q} \cdot \log q)$, and we can then use binary search to check if each $h_i$ is equal to some $g_k$ in time $\mathcal{O}(\log q)$. The overall algorithm thus runs in time $\mathcal{O}(\sqrt{q} \cdot \mathsf{polylog}(q))$.

该算法需要 $\mathcal{O}(\sqrt{q})$ 次 $\mathbb{G}$ 中的取幂/乘法。（实际上，算出 $g_1 = g^t$ 之后，每个后续值 $g_i$ 都只需一次乘法即可得到：$g_i := g_{i-1} \cdot g_1$。类似地，每个 $h_i$ 可由 $h_i := h_{i-1} \cdot g$ 算出。）对 $\mathcal{O}(\sqrt{q})$ 个数对 $\{(i, g_i)\}$ 排序耗时 $\mathcal{O}(\sqrt{q} \cdot \log q)$；随后可用二分查找在 $\mathcal{O}(\log q)$ 时间内检查每个 $h_i$ 是否等于某个 $g_k$。整个算法因此以 $\mathcal{O}(\sqrt{q} \cdot \mathsf{polylog}(q))$ 时间运行。

**Example 10.7**　**例 10.7**

We show an application of the algorithm in the cyclic group $\mathbb{Z}_{29}^{*}$ of order $q = 29 - 1 = 28$. Take $g = 2$ and $h = 17$. We set $t = 5$ and compute:

我们在阶为 $q = 29 - 1 = 28$ 的循环群 $\mathbb{Z}_{29}^{*}$ 中演示该算法的一个应用。取 $g = 2$，$h = 17$。设 $t = 5$ 并计算：

$$
2^{0}=1,\ 2^{5}=3,\ 2^{10}=9,\ 2^{15}=27,\ 2^{20}=23,\ 2^{25}=11.
$$

(It should be understood that all operations are in $\mathbb{Z}_{29}^*$.) Then compute:

（应理解为所有运算都在 $\mathbb{Z}_{29}^*$ 中进行。）再计算：

$$
17\cdot2^{1}=5,\quad17\cdot2^{2}=10,\quad17\cdot2^{3}=20,\quad17\cdot2^{4}=11,
$$

and notice that ${17} \cdot 2^{4} = 11 = 2^{25}$. We thus have $\log_{2} 17 = 25 - 4 = 21$.

并注意到 ${17} \cdot 2^{4} = 11 = 2^{25}$。于是我们得到 $\log_{2} 17 = 25 - 4 = 21$。

### 10.2.3 Discrete Logarithms from Collisions　由碰撞求离散对数

A drawback of the baby-step/giant-step algorithm is that it uses a large amount of memory, as it requires storage of $\mathcal{O}(\sqrt{q})$ points. We can obtain an algorithm that uses constant memory—and has the same asymptotic running time—by exploiting the connection between the discrete-logarithm problem and collision-resistant hashing shown in Section 9.4.2, and recalling the small-space birthday attack for finding collisions from Section 6.4.2.

大步小步算法的一个缺点是内存用量很大，因为它需要存储 $\mathcal{O}(\sqrt{q})$ 个点。利用 9.4.2 节展示的离散对数问题与抗碰撞哈希之间的联系，并结合 6.4.2 节用于找碰撞的小空间生日攻击，我们可以得到一个只用常数内存、且渐近运行时间相同的算法。

We describe the high-level idea. Fix a generator $g \in \mathbb{G}$ and an element $h$. If we define the hash function $H_{g,h} : \mathbb{Z}_q \times \mathbb{Z}_q \to \mathbb{G}$ by $H_{g,h}(x_1, x_2) = g^{x_1}h^{x_2}$, then finding a collision in $H_{g,h}$ implies the ability to compute $\log_g h$ (cf. Lemma 9.65 and Theorem 9.79). We have thus reduced the problem of computing $\log_g h$ to that of finding a collision in a hash function, something we know how to do in time $\mathcal{O}(\sqrt{|\mathbb{G}|}) = \mathcal{O}(\sqrt{q})$ using a birthday attack! Moreover, a small-space birthday attack will give a collision in the same time and constant space.

我们来描述其高层想法。固定生成元 $g \in \mathbb{G}$ 和元素 $h$。如果定义哈希函数 $H_{g,h} : \mathbb{Z}_q \times \mathbb{Z}_q \to \mathbb{G}$ 为 $H_{g,h}(x_1, x_2) = g^{x_1}h^{x_2}$，那么在 $H_{g,h}$ 中找到一个碰撞就意味着有能力计算 $\log_g h$（参见引理 9.65 与定理 9.79）。于是，我们把计算 $\log_g h$ 的问题归约为在哈希函数中找碰撞的问题——而借助生日攻击，我们知道如何在 $\mathcal{O}(\sqrt{|\mathbb{G}|}) = \mathcal{O}(\sqrt{q})$ 时间内做到这一点！而且，小空间生日攻击还能在同样的时间和常数空间内给出一个碰撞。

It only remains to address a few technical details. One is that the small-space birthday attack described in Section 6.4.2 assumes that the range of the hash function is a subset of its domain; that is not the case here, and in fact (depending on the representation being used for elements of $\mathbb{G}$) it could even be that $H_{g,h}$ is not compressing. A second issue is that the analysis in Section 6.4.2 treated the hash function as a random function, whereas $H_{g,h}$ has a significant amount of algebraic structure.

剩下只需处理几个技术细节。其一，6.4.2 节描述的小空间生日攻击假定哈希函数的值域是其定义域的子集；这里并非如此，而且（取决于 $\mathbb{G}$ 中元素所用的表示）$H_{g,h}$ 甚至可能不是压缩的。其二，6.4.2 节的分析把哈希函数当作随机函数处理，而 $H_{g,h}$ 具有相当丰富的代数结构。

Pollard’s rho algorithm provides one way to deal with these issues. We describe a different algorithm that can be viewed as a more direct implementation of the above ideas. (In practice, Pollard’s algorithm would be more efficient, although both algorithms use only $\mathcal{O}(\sqrt{q})$ group operations.) Let $F : \mathbb{G} \to \mathbb{Z}_q \times \mathbb{Z}_q$ denote a cryptographic hash function obtained by, e.g., a suitable modification of SHA-2. Define $H : \mathbb{G} \to \mathbb{G}$ by $H(k) \stackrel{\mathrm{def}}{=} H_{g,h}(F(k))$. We can use Algorithm 6.9, with natural modifications, to find a collision in $H$ using an expected $\mathcal{O}(\sqrt{|\mathbb{G}|}) = \mathcal{O}(\sqrt{q})$ evaluations of $H$ (and constant memory). With overwhelming probability, this yields a collision in $H_{g,h}$. You are asked to flesh out the details in Exercise 10.7.

Pollard ρ 算法提供了应对这些问题的一种途径。我们在这里描述另一个算法，它可以看作上述思想的更直接实现。（实践中 Pollard 算法会更高效一些，不过两种算法都只用 $\mathcal{O}(\sqrt{q})$ 次群运算。）令 $F : \mathbb{G} \to \mathbb{Z}_q \times \mathbb{Z}_q$ 表示一个密码学哈希函数，例如由 SHA-2 经适当改造得到。定义 $H : \mathbb{G} \to \mathbb{G}$ 为 $H(k) \stackrel{\mathrm{def}}{=} H_{g,h}(F(k))$。对算法 6.9 稍作自然修改，就可以用期望 $\mathcal{O}(\sqrt{|\mathbb{G}|}) = \mathcal{O}(\sqrt{q})$ 次 $H$ 求值（以及常数内存）找到 $H$ 的一个碰撞。这会以压倒性的概率给出 $H_{g,h}$ 中的一个碰撞。习题 10.7 将请你补全其中的细节。

It is interesting to observe here a certain duality: the proof that hardness of the discrete-logarithm implies a collision-resistant hash function leads to a better algorithm for solving the discrete-logarithm problem! A little reflection should convince us that this is not surprising: a proof by reduction demonstrates that an attack on some construction (in this case, finding collisions in the hash function) directly yields an attack on the underlying assumption (here, the hardness of the discrete-logarithm problem), which is exactly the property exploited by the above algorithm.

这里可以看到一种有趣的对偶性：证明“离散对数的困难性蕴含抗碰撞哈希函数”竟然带来了求解离散对数问题的更好算法！稍加思考便可知这并不奇怪：归约证明表明，对某个构造的攻击（此处即在哈希函数中找碰撞）可以直接转化为对底层假设的攻击（此处即离散对数问题的困难性），而这正是上述算法所利用的性质。

## 10.3 Index Calculus　指标计算法

We conclude with a brief look at the (non-generic) index calculus algorithm for computing discrete logarithms in the cyclic group $\mathbb{Z}_p^*$ (for $p$ prime). In contrast to the preceding (generic) algorithms, this approach has running time sub-exponential in the size of the group. The algorithm bears some resemblance to the quadratic sieve algorithm introduced in Section 10.1.3, and we assume readers are familiar with the discussion there. As in that case, we discuss the main ideas of the index calculus method but leave a detailed analysis outside the scope of our treatment. Also, some simplifications are introduced to clarify the presentation.

最后，我们简要考察在循环群 $\mathbb{Z}_p^*$（$p$ 为素数）中计算离散对数的（非泛型）指标计算法。与前述（泛型）算法不同，这种方法的运行时间关于群的规模是亚指数级的。该算法与 10.1.3 节介绍的二次筛法有几分相似，我们假定读者已熟悉那一节的讨论。与那里一样，我们只讨论指标计算法的主要思想，详细分析不在本书的讨论范围之内。此外，为使叙述清晰，还引入了一些简化。

As in the quadratic sieve algorithm, the index calculus method uses a two-step process. Importantly, the first step requires knowledge only of the modulus $p$ and the base $g$ and so it can be run as a preprocessing step before h—the value whose discrete logarithm we wish to compute—is known. For the same reason, it suffices to run the first step only once in order to solve multiple instances of the discrete-logarithm problem (as long as all those instances share the same $p$ and $g$).

与二次筛法一样，指标计算法分两步进行。重要的一点是：第一步只需要知道模数 $p$ 和底数 $g$，因此可以作为预处理步骤，在 $h$——我们想计算其离散对数的那个值——已知之前先行执行。出于同样的原因，要求解离散对数问题的多个实例，第一步只需运行一次即可（只要那些实例共用相同的 $p$ 和 $g$）。

Step 1. Fix some bound $B$, and let $\{p_1, \ldots, p_k\}$ be the set of prime numbers less than or equal to $B$. In this step, we find $\ell \geq k$ distinct values $x_1, \ldots, x_\ell \in \mathbb{Z}_{p-1}$ for which $g_i \stackrel{\mathrm{def}}{=} [g^{x_i} \bmod p]$ is $B$-smooth. This is done by simply choosing uniform $\{x_i\}$ until suitable values are found.

第 1 步。固定某个界 $B$，令 $\{p_1, \ldots, p_k\}$ 为小于等于 $B$ 的素数构成的集合。在这一步中，我们寻找 $\ell \geq k$ 个不同的值 $x_1, \ldots, x_\ell \in \mathbb{Z}_{p-1}$，使得 $g_i \stackrel{\mathrm{def}}{=} [g^{x_i} \bmod p]$ 是 $B$ 光滑的。做法很简单：不断均匀选取 $\{x_i\}$，直到找到合适的值为止。

Factoring the resulting B-smooth numbers, we have the $\ell$ equations:

对所得的 $B$ 光滑数作因子分解，便得到如下 $\ell$ 个方程：

$$
\begin{aligned}
g^{x_1}&=\prod_{i=1}^k p_{i}^{e_{1,i}}\bmod p\\
&\vdots\\
g^{x_\ell}&=\prod_{i=1}^k p_{i}^{e_{\ell,i}}\bmod p.
\end{aligned}
$$

Taking discrete logarithms, we can transform these into the linear equations

对上述等式两边取离散对数，可将它们化为线性方程

$$
\begin{aligned}
x_{1}&=\sum_{i=1}^{k}e_{1,i}\cdot\log_{g}p_{i}\bmod(p-1)\\
&\vdots\\
x_{\ell}&=\sum_{i=1}^{k}e_{\ell,i}\cdot\log_{g}p_{i}\bmod(p-1).
\end{aligned} \tag{10.3}
$$

Note that the $\{x_i\}$ and the $\{e_{i,j}\}$ are known, while the $\{\log_g p_i\}$ are unknown.

注意，$\{x_i\}$ 和 $\{e_{i,j}\}$ 是已知的，而 $\{\log_g p_i\}$ 是未知的。

Step 2. Now we are given an element $h$ and want to compute $\log_g h$. Here, we find a value $x \in \mathbb{Z}_{p-1}$ for which $[g^x \cdot h \bmod p]$ is $B$-smooth. (Once again, this is done simply by choosing $x$ uniformly.) Say

第 2 步。现在给定元素 $h$，要计算 $\log_g h$。此时，我们找一个值 $x \in \mathbb{Z}_{p-1}$，使得 $[g^x \cdot h \bmod p]$ 是 $B$ 光滑的。（同样，这只需均匀选取 $x$ 即可完成。）设

$$
\begin{aligned}
g^{x}\cdot h&=\prod_{i=1}^{k}p_{i}^{e_{i}}\bmod p\\
\Rightarrow x+\log_{g}h&=\sum_{i=1}^{k}e_{i}\cdot\log_{g}p_{i}\bmod(p-1),
\end{aligned} \tag{10.4}
$$

where $x$ and the $\{e_i\}$ are known. Combined with Equation (10.3), we have $\ell + 1 \geq k + 1$ linear equations in the $k+1$ unknowns $\{\log_g p_i\}_{i=1}^k$ and $\log_g h$. Using linear-algebraic$^3$ methods (and assuming the system of equations is not under-defined), we can solve for each of the unknowns and in particular obtain the desired solution $\log_g h$.

其中 $x$ 和 $\{e_i\}$ 已知。结合式 (10.3)，我们就得到关于 $k+1$ 个未知量 $\{\log_g p_i\}_{i=1}^k$ 与 $\log_g h$ 的 $\ell + 1 \geq k + 1$ 个线性方程。利用线性代数方法$^3$（并假定该方程组不是欠定的），可以解出每个未知量，特别是得到所求解 $\log_g h$。

> $^3$ Technically, things are slightly more complicated here since the linear equations are all modulo $p-1$, which is not prime. Nevertheless, there exist techniques for dealing with this.

> $^3$ 严格来说，这里的情况略微复杂一些，因为这些线性方程都是模 $p-1$ 的，而 $p-1$ 不是素数。不过，已有处理这一问题的相关技术。

**Example 10.8**　**例 10.8**

Let $p = 101$, $g = 3$, and $h = 87$. We have $[3^{10} \bmod 101] = 65 = 5 \cdot 13$. Similarly, $[3^{12} \bmod 101] = 80 = 2^{4} \cdot 5$ and $[3^{14} \bmod 101] = 13$. We thus have the linear equations

取 $p = 101$，$g = 3$，$h = 87$。我们有 $[3^{10} \bmod 101] = 65 = 5 \cdot 13$。类似地，$[3^{12} \bmod 101] = 80 = 2^{4} \cdot 5$，而 $[3^{14} \bmod 101] = 13$。于是得到线性方程

$$
\begin{aligned}
10&=\log_{3}5+\log_{3}13\mod100\\
12&=4\cdot\log_{3}2+\log_{3}5\mod100\\
14&=\log_{3}13\mod100.
\end{aligned}
$$

We also have ${3}^{5} \cdot 87 = 32 = 2^{5} \bmod 101$, or

我们还有 ${3}^{5} \cdot 87 = 32 = 2^{5} \bmod 101$，即

$$
5+\log_{3}87=5\cdot\log_{3}2\mod100.
$$

Adding the second and third equations and subtracting the first, we derive ${4} \cdot \log_3 2 = 16 \bmod 100$. This doesn’t determine $\log_3 2$ uniquely (since 4 is not invertible modulo 100), but it does tell us that $\log_3 2 = 4, 29, 54$, or 79 (cf. Exercise 10.3). Trying all possibilities gives $\log_3 2 = 29$. Plugging this into Equation (10.4) gives $\log_3 87 = 40$.

把第二个和第三个方程相加、再减去第一个方程，我们推导出 ${4} \cdot \log_3 2 = 16 \bmod 100$。这不能唯一确定 $\log_3 2$（因为 4 在模 100 下不可逆），但它告诉我们 $\log_3 2 = 4, 29, 54$ 或 79（参见习题 10.3）。逐一尝试各种可能性可知 $\log_3 2 = 29$。把它代入式 (10.4) 就得到 $\log_3 87 = 40$。

Running time. Choosing a larger value of $B$ makes it more likely that a uniform value in $\mathbb{Z}_p^*$ is $B$-smooth; however, it means we will have to work harder to identify and factor $B$-smooth numbers, and we will have to find more of them. Because the system of equations will be larger, solving the system will take longer. Choosing the optimal value of $B$ gives an algorithm that (heuristically, at least) computes discrete logarithms in $\mathbb{Z}_p^*$ in time ${2}^{\mathcal{O}(\sqrt{\log p \cdot \log\log p})}$. The important point for our purposes is that this is sub-exponential in the length of $p$.

**运行时间。** 把 $B$ 取得更大会使 $\mathbb{Z}_p^*$ 中均匀选取的值是 $B$ 光滑的可能性更高；然而，这也意味着识别并分解 $B$ 光滑数要花更多功夫，而且需要找到更多这样的数。由于方程组更大，求解所需时间也更长。选取最优的 $B$ 值，得到的算法（至少在启发式假设下如此）能在时间 ${2}^{\mathcal{O}(\sqrt{\log p \cdot \log\log p})}$ 内计算 $\mathbb{Z}_p^*$ 中的离散对数。对我们的目的而言，关键在于它关于 $p$ 的长度是亚指数级的。

## 10.4 Recommended Key Lengths　推荐密钥长度

Understanding the best available algorithms for solving various cryptographic problems is essential for determining the appropriate key length for achieving a desired level of security. Figure 10.1 summarizes the key lengths currently recommended by the US National Institute of Standards and Technology $^{4}$ (NIST) [14]. The “effective key length” is a value $n$ such that the best known algorithm for solving a problem takes time roughly ${2}^n$, i.e., the computational difficulty of solving a problem is approximately equivalent to that of performing a brute-force search against a symmetric-key scheme with an $n$-bit key, or the time to find collisions in a hash function with a ${2}n$-bit output length. NIST deems a 112-bit effective key length acceptable for security until the year 2030, but recommends 128-bit or higher key lengths for applications where security is required beyond then.

要确定达到期望安全级别所需的合适密钥长度，就必须理解求解各类密码学问题的现有最佳算法。图 10.1 总结了美国国家标准与技术研究院 $^{4}$（NIST）[14] 目前推荐的密钥长度。“有效密钥长度”是指这样的值 $n$：求解该问题的已知最佳算法所需时间约为 ${2}^n$；也就是说，求解该问题的计算难度，大致等同于对一个密钥为 $n$ 比特的对称密钥方案执行暴力搜索的难度，或等同于在输出长度为 ${2}n$ 比特的哈希函数中找碰撞所需的时间。NIST 认为，到 2030 年之前，112 比特的有效密钥长度是可以接受的安全水平；而对于需要在 2030 年之后仍保证安全的应用，则推荐使用 128 比特或更高的密钥长度。

> $^{4}$ Other groups have made their own recommendations; see http://keylength.com.
> $^{4}$ 其他机构也给出了各自的推荐参数；参见 http://keylength.com。

Given what we have learned in this chapter, it is instructive to look more closely at some of the numbers in the table. One thing to notice is that elliptic-curve groups can be used to realize any given level of security with smaller parameters than for RSA or subgroups of $\mathbb{Z}_p^*$. This is simply because no subexponential algorithms are known for solving the discrete-logarithm problem in elliptic-curve groups (when chosen appropriately). Achieving $n$-bit security, however, requires an elliptic-curve group whose order $q$ is ${2}n$-bits long. This is a consequence of the generic algorithms we have seen in this chapter, which solve the discrete-logarithm problem (in any group) in time $\mathcal{O}(\sqrt{q})$.

结合本章所学，仔细审视表中的某些数字颇有启发。需要注意的一点是：椭圆曲线群能够以比 RSA 或 $\mathbb{Z}_p^*$ 的子群更小的参数实现任意给定的安全级别。原因很简单：在椭圆曲线群中（适当选取时）求解离散对数问题尚无已知的亚指数算法。然而，要达到 $n$ 比特的安全性，需要一个阶 $q$ 的长度为 ${2}n$ 比特的椭圆曲线群。这正是本章所见泛型算法带来的结果：它们能以 $\mathcal{O}(\sqrt{q})$ 时间求解（任何群中的）离散对数问题。

Turning to the case of $\mathbb{Z}_p^*$ we see that here, too, a ${2}n$-bit value of $q$ is needed for $n$-bit security (for the same reason). The length of $p$, however, must be significantly larger, because non-generic algorithms like the index calculus method or the number field sieve can be used to compute discrete logarithms in $\mathbb{Z}_p^*$ in time sub-exponential in the length of $p$. That is, $p$ and $q$ are chosen such that the running time of the number field sieve, which depends on the length of $p$, and the running time of a generic algorithm, which depends on the length of $q$, are approximately equal and both around ${2}^n$. The practical ramifications of this are that, for any desired security level, elliptic-curve cryptosystems can use significantly smaller parameters (and thus give better efficiency for honest users) than cryptosystems based on subgroups of $\mathbb{Z}_p^*$. (See Figure 10.1.)

再看 $\mathbb{Z}_p^*$ 的情形：出于同样的原因，这里同样需要长度为 ${2}n$ 比特的 $q$ 才能达到 $n$ 比特安全性。但 $p$ 的长度必须显著更大，因为指标计算法或数域筛法这类非泛型算法可以用来在 $\mathbb{Z}_p^*$ 中以关于 $p$ 的长度亚指数的时间计算离散对数。也就是说，$p$ 和 $q$ 的选取应使得：数域筛法的运行时间（取决于 $p$ 的长度）与泛型算法的运行时间（取决于 $q$ 的长度）近似相等，且都在 ${2}^n$ 左右。其实际影响是：对任意期望的安全级别，椭圆曲线密码系统都可以使用比基于 $\mathbb{Z}_p^*$ 子群的密码系统小得多的参数（从而给诚实用户带来更好的效率）。（参见图 10.1。）

| Effective Key Length | RSA (modulus $N$) | Discrete Logarithm, subgroup of $\mathbb{Z}_p^*$ | Discrete Logarithm, elliptic-curve group (order $q$) |
|---|---|---|---|
| 112 | 2048 | p: 2048, q: 224 | 224 |
| 128 | 3072 | p: 3072, q: 256 | 256 |
| 192 | 7680 | p: 7680, q: 384 | 384 |
| 256 | 15360 | p: 15360, q: 512 | 512 |

| 有效密钥长度 | RSA（模数 $N$） | 离散对数，$\mathbb{Z}_p^*$ 的子群 | 离散对数，椭圆曲线群（阶 $q$） |
|---|---|---|---|
| 112 | 2048 | p: 2048, q: 224 | 224 |
| 128 | 3072 | p: 3072, q: 256 | 256 |
| 192 | 7680 | p: 7680, q: 384 | 384 |
| 256 | 15360 | p: 15360, q: 512 | 512 |

**FIGURE 10.1: All values are in bits, e.g., for a 112-bit effective key length in the RSA setting, a 2048-bit modulus $N$ should be used. / 图 10.1：所有数值均以比特为单位。例如，在 RSA 场景下要达到 112 比特的有效密钥长度，应使用 2048 比特的模数 $N$。**

## References and Additional Reading　参考文献与延伸阅读

Pollard’s p-1 algorithm was published in 1974 [160], and his rho method for factoring was described the following year [161]. The quadratic sieve algorithm is due to Pomerance [163], based on earlier ideas of Dixon [67].

Pollard $p-1$ 算法发表于 1974 年 [160]，他提出的用于因子分解的 ρ 方法于次年发表 [161]。二次筛法由 Pomerance [163] 提出，其基础是 Dixon [67] 更早的想法。

The Pohlig–Hellman algorithm was published in 1978 [159]. The baby-step/giant-step algorithm is due to Shanks [176]. Pollard’s paper introducing the rho algorithm for computing discrete logarithms [162] also includes his famous “kangaroo” algorithm for the same problem. A nice feature of the kangaroo method is that it is more flexible; in particular, it can be used to compute discrete logarithms known to lie in a given interval $[a, b]$ using $\mathcal{O}(\sqrt{b - a})$ steps. (Although the baby-step/giant-step algorithm can also be adapted for that case—see Exercise 10.6—the kangaroo algorithm stores only a constant number of group elements.) Lower bounds on the running time of generic algorithms for computing discrete logarithms, which asymptotically match the running times of the algorithms described in this chapter, were given by Nechaev [152] and Shoup [179].

Pohlig–Hellman 算法发表于 1978 年 [159]。大步小步算法由 Shanks 提出 [176]。Pollard 引入用于计算离散对数的 ρ 算法的论文 [162] 中，还包含了他解决同一问题的著名“袋鼠”（kangaroo）算法。袋鼠方法的一个优点是更为灵活；特别是，当已知离散对数位于给定区间 $[a, b]$ 内时，可以用 $\mathcal{O}(\sqrt{b - a})$ 步将其计算出来。（虽然大步小步算法经过调整也能处理这种情况——见习题 10.6——但袋鼠算法只存储常数个群元素。）关于泛型离散对数算法运行时间的下界由 Nechaev [152] 和 Shoup [179] 给出，这些下界在渐近意义上与本章所述算法的运行时间吻合。

The index calculus algorithm as we have described it is by Adleman [4]. The texts by Wagstaff [201], Shoup [183], Crandall and Pomerance [59], Joux [105], and Galbraith [76] provide further information on algorithms for factoring and computing discrete logarithms in finite fields, including descriptions of the (general) number field sieve. The current state-of-the-art for factoring and computing discrete logarithms in $\mathbb{Z}_p^*$ for large $p$ is surveyed in a recent article by Boudot et al. [45].

我们上面所描述的这一版本的指标计算法归功于 Adleman [4]。Wagstaff [201]、Shoup [183]、Crandall 与 Pomerance [59]、Joux [105] 以及 Galbraith [76] 的著作提供了关于因子分解与有限域中离散对数计算的更多资料，其中包括（一般）数域筛法的描述。关于大 $p$ 情形下 $\mathbb{Z}_p^*$ 中因子分解与离散对数计算的最新研究现状，可见 Boudot 等人 [45] 最近的一篇综述文章。

Recently, improved algorithms for solving the discrete-logarithm problem in finite fields of small characteristic [12] or even any fixed characteristic [116] have been announced. It seems prudent to avoid using such groups for cryptographic applications.

近来，人们宣布了改进的算法，可用于求解小特征 [12] 乃至任意固定特征 [116] 的有限域中的离散对数问题。谨慎起见，似乎应避免将此类群用于密码学应用。

Lenstra and Verheul [126] provide a comprehensive discussion, somewhat dated but still relevant, of how known algorithms for factoring and computing discrete logarithms affect the choice of cryptographic parameters in practice.

Lenstra 与 Verheul [126] 全面讨论了已知的因子分解与离散对数计算算法如何影响实践中密码参数的选择；这一讨论虽略显过时，但仍有参考价值。

## Exercises　习题

10.1 In order to speed up the key-generation algorithm for RSA, it has been suggested to generate a large prime number by generating many small random primes, multiplying them together, and adding one (of course, then checking that the result is prime). What do you think of the security implications of this method?

习题 10.1　为了加速 RSA 的密钥生成算法，有人建议这样生成一个大素数：先生成许多小的随机素数，把它们相乘，再加一（当然，随后要检查所得结果是否为素数）。你如何评价这种方法对安全性的影响？

10.2 In an execution of Algorithm 10.2, define $x^{(i)} \stackrel{\mathrm{def}}{=} F^{(i)}(x)$. Show that if, in a given execution, there exist $i, j \leq 2^{n/2}$ such that $x^{(i)} \neq x^{(j)}$ but $x^{(i)} = x^{(j)} \bmod p$, then that execution of the algorithm outputs $p$ with overwhelming probability. (The analysis is a little different from the analysis of Algorithm 6.9, since the algorithms—and their goals—are slightly different.)

习题 10.2　在算法 10.2 的一次执行中，定义 $x^{(i)} \stackrel{\mathrm{def}}{=} F^{(i)}(x)$。证明：如果在某次执行中存在 $i, j \leq 2^{n/2}$ 使得 $x^{(i)} \neq x^{(j)}$ 但 $x^{(i)} = x^{(j)} \bmod p$，那么该次执行会以压倒性的概率输出 $p$。（这里的分析与对算法 6.9 的分析略有不同，因为两个算法——以及它们的目标——稍有差别。）

10.3 (a) Show that if $ab = c \bmod N$ and $\gcd(b, N) = d$, then:

习题 10.3　(a) 证明：如果 $ab = c \bmod N$ 且 $\gcd(b, N) = d$，那么：

i. $d \mid c;$

i. $d \mid c$；

ii. $a \cdot (b/d) = (c/d) \bmod (N/d)$; and

ii. $a \cdot (b/d) = (c/d) \bmod (N/d)$；以及

iii. $\gcd(b/d, N/d) = 1$

iii. $\gcd(b/d, N/d) = 1$

(b) Describe how to use the above to compute $\log_g h$ in $\mathbb{Z}_N$ even when $g$ is not a generator of $\mathbb{Z}_N$ (but $h \in \langle g \rangle$).

(b) 描述如何利用上述结论计算 $\mathbb{Z}_N$ 中的 $\log_g h$——即使 $g$ 不是 $\mathbb{Z}_N$ 的生成元（只要 $h \in \langle g \rangle$）。

10.4 Here we consider how to solve the discrete-logarithm problem in a cyclic group $\mathbb{G}$ of order $q = p^e$ using $\mathcal{O}(e\sqrt{p})$ group operations. We are given as input a generator $g$ and an element $h$, and want to compute $x = \log_g h$.

习题 10.4　本题考虑如何在阶为 $q = p^e$ 的循环群 $\mathbb{G}$ 中，用 $\mathcal{O}(e\sqrt{p})$ 次群运算求解离散对数问题。输入为生成元 $g$ 和元素 $h$，要计算 $x = \log_g h$。

(a) Show how to compute $[x \bmod p]$ using $\mathcal{O}(\sqrt{p})$ group operations.

(a) 证明如何用 $\mathcal{O}(\sqrt{p})$ 次群运算计算 $[x \bmod p]$。

Hint: Solve the equation

提示：求解方程

$$
\left(g^{p^{e-1}}\right)^{x_{0}}=h^{p^{e-1}}
$$

and use the same ideas as in the Pohlig–Hellman algorithm.

并使用与 Pohlig–Hellman 算法相同的思路。

(b) Say $x = x_0 + x_1 \cdot p + \cdots + x_{e-1} \cdot p^{e-1}$ with ${0} \leq x_i < p$. (i.e., write $x$ in base $p$). In the previous step we determined $x_0$. Show how to compute a value $h_1$ such that $(g^p)^{x_1 + x_2 \cdot p + \cdots + x_{e-1} \cdot p^{e-2}} = h_1$.

(b) 设 $x = x_0 + x_1 \cdot p + \cdots + x_{e-1} \cdot p^{e-1}$，其中 ${0} \leq x_i < p$（即把 $x$ 写成 $p$ 进制）。在上一步中我们已经确定了 $x_0$。证明如何计算一个值 $h_1$，使得 $(g^p)^{x_1 + x_2 \cdot p + \cdots + x_{e-1} \cdot p^{e-2}} = h_1$。

(c) Show a recursive algorithm computing the discrete logarithm $x$ in the claimed running time.

(c) 给出一个递归算法，在所声称的运行时间内计算出离散对数 $x$。

10.5 Let $q$ have prime factorization $q = \prod_{i=1}^{k} p_{i}^{e_{i}}$. Using the result from the previous problem, show a modification of the Pohlig–Hellman algorithm that solves the discrete-logarithm problem in a group of order $q$ using $\mathcal{O}\left(\sum_{i=1}^{k} e_{i} \sqrt{p_{i}}\right)$ group operations.

习题 10.5　设 $q$ 的素因子分解为 $q = \prod_{i=1}^{k} p_{i}^{e_{i}}$。利用上一题的结果，给出 Pohlig–Hellman 算法的一种修改版本，使其能用 $\mathcal{O}\left(\sum_{i=1}^{k} e_{i} \sqrt{p_{i}}\right)$ 次群运算求解阶为 $q$ 的群中的离散对数问题。

10.6 Let $\mathbb{G}$ be a cyclic group of order $q$, with generator $g$. Let $h \in \mathbb{G}$ be given, where it is known that $h = g^x$ for $x \in [a, b]$ (and $a, b$ are known). Show how to modify the baby-step/giant-step algorithm to compute $\log_g h$ using $\mathcal{O}(\sqrt{b - a})$ group operations.

习题 10.6　设 $\mathbb{G}$ 是阶为 $q$ 的循环群，生成元为 $g$。给定 $h \in \mathbb{G}$，已知 $h = g^x$，其中 $x \in [a, b]$（且 $a, b$ 已知）。证明如何修改大步小步算法，用 $\mathcal{O}(\sqrt{b - a})$ 次群运算计算 $\log_g h$。

10.7 Based on the ideas described in Section 10.2.3, give pseudocode for a generic algorithm that computes discrete logarithms in a group of order $q$ using $\mathcal{O}(\sqrt{q})$ group operations and $\mathcal{O}(1)$ memory. Also give a heuristic analysis of the probability with which your algorithm succeeds.

习题 10.7　根据 10.2.3 节描述的思想，给出一个泛型算法的伪代码：它在阶为 $q$ 的群中，用 $\mathcal{O}(\sqrt{q})$ 次群运算和 $\mathcal{O}(1)$ 内存计算离散对数。并对你给出的算法成功的概率作启发式分析。
