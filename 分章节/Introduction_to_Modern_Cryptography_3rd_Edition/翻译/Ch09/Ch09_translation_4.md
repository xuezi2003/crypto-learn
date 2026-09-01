## 9.4 \*Cryptographic Applications　\*密码学应用

We have spent a fair bit of time discussing number theory and group theory, and introducing computational hardness assumptions that are widely believed to hold. Applications of these assumptions will occupy us for the rest of the book, but we provide some brief examples here.

我们已经花了不少篇幅讨论数论与群论，并介绍了被广泛认为成立的若干计算困难性假设。这些假设的应用将占据本书余下的篇幅，这里我们先给出几个简短的例子。

### 9.4.1 One-Way Functions and Permutations　单向函数与单向置换

One-way functions are the minimal cryptographic primitive, and they are both necessary and sufficient for private-key encryption and message authentication codes. A more complete discussion of the role of one-way functions in cryptography appears in Chapter 8; here we only provide a definition of one-way functions and demonstrate that their existence follows from the number-theoretic hardness assumptions we have seen in this chapter.

单向函数是最基本的密码学原语；对于私钥加密和消息认证码而言，它既是必要的又是充分的。关于单向函数在密码学中之作用的更完整讨论见第 8 章；这里我们只给出单向函数的定义，并证明其存在性可以由本章见过的数论困难性假设推出。

Informally, a function $f$ is one-way if it is easy to compute but hard to invert. The following experiment and definition, a restatement of Definition 8.1, formalizes this.

非正式地说，若函数 $f$ 易于计算却难以求逆，就称它是单向的。下面的实验和定义——即定义 8.1 的重述——把这一点形式化了。

The inverting experiment $\mathsf{Invert}_{\mathcal{A},f}(n)$:

求逆实验 $\mathsf{Invert}_{\mathcal{A},f}(n)$：

1. Choose uniform $x \in \{0,1\}^{n}$ and compute $y := f(x)$.

   均匀选取 $x \in \{0,1\}^{n}$，并计算 $y := f(x)$。

2. $\mathcal{A}$ is given $1^{n}$ and $y$ as input, and outputs $x^{\prime}$.

   将 $1^{n}$ 和 $y$ 作为输入交给 $\mathcal{A}$，$\mathcal{A}$ 输出 $x^{\prime}$。

3. The output of the experiment is 1 if and only if $f(x^{\prime}) = y$.

   当且仅当 $f(x^{\prime}) = y$ 时，实验输出为 1。

DEFINITION 9.73 A function $f: \{0,1\}^* \to \{0,1\}^*$ is one-way if the following two conditions hold:

定义 9.73　若函数 $f: \{0,1\}^* \to \{0,1\}^*$ 满足以下两个条件，则称其为单向函数：

1. (Easy to compute:) There is a polynomial-time algorithm that on input $x$ outputs $f(x)$.

   （易于计算：）存在一个多项式时间算法，以 $x$ 为输入，输出 $f(x)$。

2. (Hard to invert:) For all PPT algorithms $\mathcal{A}$ there is a negligible function $\mathsf{negl}$ such that $\Pr[\mathsf{Invert}_{\mathcal{A},f}(n) = 1] \leq \mathsf{negl}(n)$.

   （难以求逆：）对所有 PPT 算法 $\mathcal{A}$，都存在可忽略函数 $\mathsf{negl}$ 使得 $\Pr[\mathsf{Invert}_{\mathcal{A},f}(n) = 1] \leq \mathsf{negl}(n)$。

We now show formally that the factoring assumption implies the existence of a one-way function. Let $\mathsf{Gen}$ be a polynomial-time algorithm that, on input $1^n$, outputs $(N, p, q)$ where $N = pq$ and $p$ and $q$ are $n$-bit primes except with probability negligible in $n$. (We use $\mathsf{Gen}$ rather than $\mathsf{GenModulus}$ here purely for notational convenience.) Since $\mathsf{Gen}$ runs in polynomial time, there is a polynomial upper bound on the number of random bits the algorithm uses. For simplicity, and in order to get the main ideas across, we assume $\mathsf{Gen}$ always uses at most $n$ random bits on input $1^n$. In Algorithm 9.74 we define a function $f_{\mathsf{Gen}}$ that uses its input as the random bits for running $\mathsf{Gen}$. Thus, $f_{\mathsf{Gen}}$ is a deterministic function (as required).

现在我们形式化地证明：因子分解假设蕴含单向函数的存在性。设 $\mathsf{Gen}$ 是一个多项式时间算法，以 $1^n$ 为输入，输出 $(N, p, q)$，其中 $N = pq$，并且除关于 $n$ 可忽略的概率外，$p$ 和 $q$ 都是 $n$ 比特素数。（这里纯粹出于记号上的方便，我们用 $\mathsf{Gen}$ 而不是 $\mathsf{GenModulus}$。）既然 $\mathsf{Gen}$ 在多项式时间内运行，该算法所用的随机比特数就有多项式的上界。为了简单起见、也为了把主要思想讲清楚，我们假定 $\mathsf{Gen}$ 在输入 $1^n$ 下总是至多使用 $n$ 个随机比特。算法 9.74 定义了一个函数 $f_{\mathsf{Gen}}$，它把自己的输入用作运行 $\mathsf{Gen}$ 所需的随机比特。这样，$f_{\mathsf{Gen}}$ 就是确定性函数（正如定义所要求的）。

If the factoring problem is hard relative to $\mathsf{Gen}$ then $f_{\mathsf{Gen}}$ is a one-way function. Certainly $f_{\mathsf{Gen}}$ is easy to compute. As for the hardness of inverting this function, note that the following distributions are identical:

如果因子分解问题相对于 $\mathsf{Gen}$ 是困难的，那么 $f_{\mathsf{Gen}}$ 就是单向函数。$f_{\mathsf{Gen}}$ 当然易于计算；至于对这个函数求逆的困难性，请注意下面两个分布是完全相同的：

1. The modulus $N$ output by $f_{\mathsf{Gen}}(x)$, when $x \in \{0,1\}^n$ is chosen uniformly.

   $f_{\mathsf{Gen}}(x)$ 所输出的模数 $N$，其中 $x \in \{0,1\}^n$ 均匀选取。

2. The modulus $N$ output by (the randomized algorithm) $\mathsf{Gen}(1^{n})$.

   （随机化算法）$\mathsf{Gen}(1^{n})$ 所输出的模数 $N$

If moduli $N$ generated according to the second distribution are hard to factor, then the same holds for moduli $N$ generated according to the first distribution.

如果按第二种分布生成的模数 $N$ 难以分解，那么按第一种分布生成的模数 $N$ 也同样难以分解。

| ALGORITHM 9.74 |
| --- |
| Algorithm computing $f_{\mathsf{Gen}}$ |
| Input: String $x$ of length $n$ |
| Output: Integer $N$ |
| compute $(N,p,q) := \mathsf{Gen}(1^{n}; x)$ |
| // i.e., run $\mathsf{Gen}(1^{n})$ using $x$ as the random tape |
| return $N$ |

| 算法 9.74　计算 $f_{\mathsf{Gen}}$ 的算法 |
| --- |
| 输入：长度为 $n$ 的串 $x$ |
| 输出：整数 $N$ |
| 计算 $(N,p,q) := \mathsf{Gen}(1^{n}; x)$ |
| // 即以 $x$ 作为随机带运行 $\mathsf{Gen}(1^{n})$ |
| 返回 $N$ |

Moreover, given any preimage $x^{\prime}$ of $N$ with respect to $f_{\mathsf{Gen}}$ (i.e., an $x^{\prime}$ for which $f_{\mathsf{Gen}}(x^{\prime}) = N$; note that we do not require $x^{\prime} = x$), it is easy to recover a factor of $N$ by running $\mathsf{Gen}(1^n; x^{\prime})$ to obtain $(N, p, q)$ and outputting the factors $p$ and $q$. Thus, finding a preimage of $N$ with respect to $f_{\mathsf{Gen}}$ is as hard as factoring $N$. One can easily turn this into a formal proof.

此外，给定 $N$ 关于 $f_{\mathsf{Gen}}$ 的任意原像 $x^{\prime}$（即满足 $f_{\mathsf{Gen}}(x^{\prime}) = N$ 的 $x^{\prime}$；注意我们不要求 $x^{\prime} = x$），要恢复出 $N$ 的一个因子也很容易：运行 $\mathsf{Gen}(1^n; x^{\prime})$ 得到 $(N, p, q)$，然后输出因子 $p$ 和 $q$。因此，求 $N$ 关于 $f_{\mathsf{Gen}}$ 的原像与分解 $N$ 一样困难。这一论证很容易转化为形式化的证明。

#### One-Way Permutations　单向置换

We can also use number-theoretic assumptions to construct a family of one-way permutations. We begin with a restatement of Definitions 8.2 and 8.3, specialized to the case of permutations:

我们同样可以利用数论假设来构造一族单向置换。先重述定义 8.2 和定义 8.3，并将其特殊化到置换的情形：

DEFINITION 9.75 A triple $\Pi = (\mathsf{Gen}, \mathsf{Samp}, f)$ of probabilistic polynomial-time algorithms is a family of permutations if the following hold:

定义 9.75　若由概率多项式时间算法构成的三元组 $\Pi = (\mathsf{Gen}, \mathsf{Samp}, f)$ 满足以下条件，则称其为置换族：

1. The parameter-generation algorithm $\mathsf{Gen}$, on input $1^n$, outputs parameters $I$ with $|I| \geq n$. Each value of $I$ defines a set $\mathcal{D}_I$ that constitutes the domain and range of a permutation (i.e., bijection) $f_I: \mathcal{D}_I \to \mathcal{D}_I$.

   参数生成算法 $\mathsf{Gen}$ 以 $1^n$ 为输入，输出满足 $|I| \geq n$ 的参数 $I$。$I$ 的每个取值定义一个集合 $\mathcal{D}_I$，它同时构成置换（即双射）$f_I: \mathcal{D}_I \to \mathcal{D}_I$ 的定义域和值域。

2. The sampling algorithm $\mathsf{Samp}$, on input $I$, outputs a uniformly distributed element of $\mathcal{D}_{I}$.

   采样算法 $\mathsf{Samp}$ 以 $I$ 为输入，输出 $\mathcal{D}_I$ 中均匀分布的一个元素。

3. The deterministic evaluation algorithm $f$, on input $I$ and $x \in \mathcal{D}_I$, outputs an element $y \in \mathcal{D}_I$. We write this as $y := f_I(x)$.

   确定性求值算法 $f$ 以 $I$ 和 $x \in \mathcal{D}_I$ 为输入，输出元素 $y \in \mathcal{D}_I$。记作 $y := f_I(x)$。

Given a family of functions $\Pi$, consider the following experiment for any algorithm $\mathcal{A}$ and parameter $n$:

给定函数族 $\Pi$，考虑针对任意算法 $\mathcal{A}$ 和参数 $n$ 的如下实验：

The inverting experiment $\mathsf{Invert}_{\mathcal{A},\Pi}(n)$:

求逆实验 $\mathsf{Invert}_{\mathcal{A},\Pi}(n)$：

1. $\mathsf{Gen}(1^n)$ is run to obtain $I$, and then $\mathsf{Samp}(I)$ is run to choose a uniform $x \in \mathcal{D}_I$. Finally, $y := f_I(x)$ is computed.

   运行 $\mathsf{Gen}(1^n)$ 得到 $I$，然后运行 $\mathsf{Samp}(I)$ 均匀选取 $x \in \mathcal{D}_I$。最后计算 $y := f_I(x)$。

2. $\mathcal{A}$ is given $I$ and $y$ as input, and outputs $x'$.

   将 $I$ 和 $y$ 作为输入交给 $\mathcal{A}$，$\mathcal{A}$ 输出 $x'$。

3. The output of the experiment is 1 if and only if $f_{I}(x^{\prime}) = y$.

   当且仅当 $f_{I}(x^{\prime}) = y$ 时，实验输出为 1。

DEFINITION 9.76 The family of permutations $\Pi = (\mathsf{Gen}, \mathsf{Samp}, f)$ is one-way if for all probabilistic polynomial-time algorithms $\mathcal{A}$ there exists a negligible function $\mathsf{negl}$ such that

定义 9.76　如果对所有概率多项式时间算法 $\mathcal{A}$ 都存在可忽略函数 $\mathsf{negl}$ 使得

$$
\Pr[\mathsf{Invert}_{\mathcal{A},\Pi}(n)=1]\leq\mathsf{negl}(n).
$$

**CONSTRUCTION 9.77**

**构造 9.77**

Let $\mathsf{GenRSA}$ be as before. Define a family of permutations as follows:

设 $\mathsf{GenRSA}$ 如前所述。如下定义一个置换族：

- $\mathsf{Gen}$: on input $1^n$, run $\mathsf{GenRSA}(1^n)$ to obtain $(N, e, d)$ and output $I = \langle N, e \rangle$. Set $\mathcal{D}_I = \mathbb{Z}_N^*$.

  Gen：以 $1^n$ 为输入，运行 $\mathsf{GenRSA}(1^n)$ 得到 $(N, e, d)$，输出 $I = \langle N, e \rangle$，并令 $\mathcal{D}_I = \mathbb{Z}_N^*$。

- $\mathsf{Samp}$: on input $I = \langle N, e \rangle$, choose a uniform element of $\mathbb{Z}_N^*$.

  Samp：以 $I = \langle N, e \rangle$ 为输入，在 $\mathbb{Z}_N^*$ 中均匀选取一个元素。

- $f$: on input $I = \langle N, e \rangle$ and $x \in \mathbb{Z}_N^*$, output $[x^e \bmod N]$.

  $f$：以 $I = \langle N, e \rangle$ 和 $x \in \mathbb{Z}_N^*$ 为输入，输出 $[x^e \bmod N]$。

A family of permutations based on the RSA problem.

基于 RSA 问题的置换族。

Given $\mathsf{GenRSA}$ as in Section 9.2.4, Construction 9.77 defines a family of permutations. It is immediate that if the RSA problem is hard relative to $\mathsf{GenRSA}$ then this family is one-way. It can similarly be shown that hardness of the discrete-logarithm problem in $\mathbb{Z}_p^*$, with $p$ prime, implies the existence of a one-way family of permutations; see Section 8.1.2.

给定 9.2.4 节中的 $\mathsf{GenRSA}$，构造 9.77 就定义了一个置换族。显然，如果 RSA 问题相对于 $\mathsf{GenRSA}$ 是困难的，那么这个族就是单向的。类似地可以证明：$\mathbb{Z}_p^*$（$p$ 为素数）中离散对数问题的困难性蕴含单向置换族的存在性；参见 8.1.2 节。

### 9.4.2 Collision-Resistant Hash Functions　抗碰撞哈希函数

Collision-resistant hash functions were introduced in Section 6.1. Although we have discussed constructions of collision-resistant hash functions used in practice in Section 7.3, we have not yet seen constructions that can be rigorously based on simpler assumptions. We show here a construction based on the discrete-logarithm assumption in prime-order groups. (A construction based on the RSA problem is described in Exercise 9.27.) Although these constructions are less efficient than the hash functions used in practice, they are important since they illustrate the feasibility of achieving collision resistance based on standard and well-studied number-theoretic assumptions.

抗碰撞哈希函数在 6.1 节中引入。尽管我们已在 7.3 节讨论过实践中所用抗碰撞哈希函数的构造，但还没有见到能严格建立在更简单假设之上的构造。这里我们给出一个基于素数阶群中离散对数假设的构造。（基于 RSA 问题的构造见习题 9.27。）这些构造虽然比实践中使用的哈希函数效率低，但十分重要——因为它们表明：基于标准且已被充分研究的数论假设来实现抗碰撞是可行的。

Let $\mathcal{G}$ be a polynomial-time algorithm that, on input $1^n$, outputs a (description of a) cyclic group $\mathbb{G}$, its order $q$ (with $\|q\| = n$), and a generator $g$. Here we also require that $q$ is prime except possibly with negligible probability. We define a fixed-length hash function $(\mathsf{Gen}, H)$ by choosing a uniform $h \in \mathbb{G}$ as part of the key $s$, and defining $H^s(x_1, x_2) = g^{x_1}h^{x_2}$; see Construction 9.78.

设 $\mathcal{G}$ 是一个多项式时间算法，以 $1^n$ 为输入，输出一个循环群 $\mathbb{G}$ 的描述、它的阶 $q$（满足 $\|q\| = n$）以及生成元 $g$。这里我们还要求：除关于 $n$ 可忽略的概率外，$q$ 都是素数。我们如下定义定长哈希函数 $(\mathsf{Gen}, H)$：把均匀选取的一个 $h \in \mathbb{G}$ 作为密钥 $s$ 的一部分，并定义 $H^s(x_1, x_2) = g^{x_1}h^{x_2}$；参见构造 9.78。

Note that Gen and H can be computed in polynomial time. Before continuing with an analysis of the construction, we make some technical remarks:

注意，$\mathsf{Gen}$ 和 $H$ 都可以在多项式时间内计算。在继续分析这个构造之前，我们先作几点技术性说明：

- For a given $s = \langle \mathbb{G}, q, g, h \rangle$ with $n = \|q\|$, the function $H^s$ is described as taking elements of $\mathbb{Z}_q \times \mathbb{Z}_q$ as input. However, $H^s$ can be viewed as taking bit-strings of length $2 \cdot (n-1)$ as input if we parse an input $x \in \{0,1\}^{2(n-1)}$ as two strings $x_1, x_2$, each of length $n-1$, and then view $x_1, x_2$ as elements of $\mathbb{Z}_q$ in the natural way.

  对于给定的 $s = \langle \mathbb{G}, q, g, h \rangle$（其中 $n = \|q\|$），函数 $H^s$ 的描述是取 $\mathbb{Z}_q \times \mathbb{Z}_q$ 中的元素作为输入。不过，如果先把输入 $x \in \{0,1\}^{2(n-1)}$ 解析为两条长度各为 $n-1$ 的串 $x_1, x_2$，再以自然的方式把 $x_1, x_2$ 视为 $\mathbb{Z}_q$ 中的元素，那么 $H^s$ 就可以看作取长度为 $2 \cdot (n-1)$ 的比特串作为输入。

- The output of $H^{s}$ is similarly specified as being an element of $\mathbb{G}$, but we can view this as a bit-string if we fix some representation of $\mathbb{G}$. To satisfy the requirements of Definition 6.2 (which requires the output length to be fixed as a function of $n$) we can pad the output as needed.

  类似地，$H^{s}$ 的输出被规定为 $\mathbb{G}$ 中的元素，但只要固定 $\mathbb{G}$ 的某种表示，就能把它看作比特串。为了满足定义 6.2 的要求（该定义要求输出长度固定为 $n$ 的函数），可以按需对输出进行填充。

**CONSTRUCTION 9.78**

**构造 9.78**

Let $\mathcal{G}$ be as described in the text. Define a fixed-length hash function $(\mathsf{Gen}, H)$ as follows:

设 $\mathcal{G}$ 如正文所述。如下定义定长哈希函数 $(\mathsf{Gen}, H)$：

- $\mathsf{Gen}$: on input $1^n$, run $\mathcal{G}(1^n)$ to obtain $(\mathbb{G}, q, g)$ and then select a uniform $h \in \mathbb{G}$. Output $s := \langle \mathbb{G}, q, g, h \rangle$ as the key.

  Gen：以 $1^n$ 为输入，运行 $\mathcal{G}(1^n)$ 得到 $(\mathbb{G}, q, g)$，然后均匀选取一个 $h \in \mathbb{G}$。输出 $s := \langle \mathbb{G}, q, g, h \rangle$ 作为密钥。

- $H$: given a key $s = \langle \mathbb{G}, q, g, h \rangle$ and input $(x_1, x_2) \in \mathbb{Z}_q \times \mathbb{Z}_q$, output $H^s(x_1, x_2) := g^{x_1} h^{x_2} \in \mathbb{G}$.

  $H$：给定密钥 $s = \langle \mathbb{G}, q, g, h \rangle$ 和输入 $(x_1, x_2) \in \mathbb{Z}_q \times \mathbb{Z}_q$，输出 $H^s(x_1, x_2) := g^{x_1} h^{x_2} \in \mathbb{G}$。

A fixed-length hash function.

一个定长哈希函数。

Given the above, the construction only compresses its input when elements of $\mathbb{G}$ can be represented using fewer than $2n - 2$ bits. A generalization of Construction 9.78 can be used to obtain compression from any $\mathbb{G}$ for which the discrete-logarithm problem is hard, regardless of the number of bits required to represent group elements; see Exercise 9.28.

综上所述，只有当 $\mathbb{G}$ 的元素能用少于 $2n - 2$ 个比特表示时，这一构造才能压缩输入。构造 9.78 的一个推广可以从任何离散对数问题困难的 $\mathbb{G}$ 得到压缩，而不论表示群元素需要多少个比特；参见习题 9.28。

THEOREM 9.79 Say $\mathcal{G}$ outputs prime-order groups, and the discrete-logarithm problem is hard relative to $\mathcal{G}$. Then Construction 9.78 is a fixed-length collision-resistant hash function (subject to the discussion regarding compression, above).

定理 9.79　设 $\mathcal{G}$ 输出的是素数阶群，并且离散对数问题相对于 $\mathcal{G}$ 是困难的。那么构造 9.78 是一个定长抗碰撞哈希函数（以上文关于压缩的讨论为前提）。

PROOF Let $\Pi = (\mathsf{Gen}, H)$ be as in Construction 9.78, and let $\mathcal{A}$ be a probabilistic polynomial-time algorithm with

证明　设 $\Pi = (\mathsf{Gen}, H)$ 如构造 9.78 中所示，并设 $\mathcal{A}$ 是满足下式的概率多项式时间算法：

$$
\varepsilon(n)\stackrel{\mathrm{def}}{=}\Pr[\mathsf{Hash-coll}_{\mathcal{A},\Pi}(n)=1]
$$

(cf. Definition 6.2). We show how $\mathcal{A}$ can be used by an algorithm $\mathcal{A}^{\prime}$ to solve the discrete-logarithm problem with success probability $\varepsilon(n)$:

（参见定义 6.2。）我们来展示：某个算法 $\mathcal{A}^{\prime}$ 可以利用 $\mathcal{A}$，以成功概率 $\varepsilon(n)$ 求解离散对数问题：

Algorithm $\mathcal{A}^{\prime}$:

算法 $\mathcal{A}^{\prime}$：

The algorithm is given $\mathbb{G}, q, g, h$ as input.

该算法以 $\mathbb{G}, q, g, h$ 作为输入。

1. Let $s := \langle \mathbb{G}, q, g, h \rangle$. Run $\mathcal{A}(s)$ and obtain output $x$ and $x^{\prime}$.

   令 $s := \langle \mathbb{G}, q, g, h \rangle$。运行 $\mathcal{A}(s)$，得到输出 $x$ 和 $x^{\prime}$。

2. If $x \neq x^{\prime}$ and $H^s(x) = H^s(x^{\prime})$ then parse $x$ as $(x_1, x_2)$ and parse $x^{\prime}$ as $(x_1^{\prime}, x_2^{\prime})$, where $x_1, x_2, x_1^{\prime}, x_2^{\prime} \in \mathbb{Z}_q$. Use Lemma 9.65 to compute $\log_g h$.

   若 $x \neq x^{\prime}$ 且 $H^s(x) = H^s(x^{\prime})$，则把 $x$ 解析为 $(x_1, x_2)$、把 $x^{\prime}$ 解析为 $(x_1^{\prime}, x_2^{\prime})$，其中 $x_1, x_2, x_1^{\prime}, x_2^{\prime} \in \mathbb{Z}_q$。用引理 9.65 计算 $\log_g h$。

Clearly, $\mathcal{A}^{\prime}$ runs in polynomial time. Furthermore, the input $s$ given to $\mathcal{A}$ when run as a subroutine by $\mathcal{A}^{\prime}$ is distributed exactly as in experiment $\mathsf{Hash-coll}_{\mathcal{A},\Pi}$ for the same value of the security parameter $n$. (The input to $\mathcal{A}^{\prime}$ is generated by running $\mathcal{G}(1^n)$ to obtain $\mathbb{G}, q, g$ and then choosing uniform $h \in \mathbb{G}$. This is exactly how $s$ is generated by $\mathsf{Gen}(1^n)$.) So, with probability exactly $\varepsilon(n)$ there is a collision; i.e., $x \neq x^{\prime}$ and $H^s(x) = H^s(x^{\prime})$. Lemma 9.65 implies that whenever there is a collision, $\mathcal{A}^{\prime}$ returns the correct answer $\log_g h$.

显然，$\mathcal{A}^{\prime}$ 在多项式时间内运行。此外，当 $\mathcal{A}$ 作为子程序被 $\mathcal{A}^{\prime}$ 运行时，交给它的输入 $s$ 的分布与实验 $\mathsf{Hash-coll}_{\mathcal{A},\Pi}$ 在同一安全参数取值 $n$ 下的分布完全一致。（$\mathcal{A}^{\prime}$ 的输入是这样生成的：运行 $\mathcal{G}(1^n)$ 得到 $\mathbb{G}, q, g$，然后均匀选取 $h \in \mathbb{G}$；这与 $\mathsf{Gen}(1^n)$ 生成 $s$ 的方式完全相同。）于是，恰好以概率 $\varepsilon(n)$ 出现碰撞，即 $x \neq x^{\prime}$ 且 $H^s(x) = H^s(x^{\prime})$。由引理 9.65 可知，只要出现碰撞，$\mathcal{A}^{\prime}$ 就会返回正确的答案 $\log_g h$。

In summary, $\mathcal{A}^{\prime}$ correctly solves the discrete-logarithm problem with probability exactly $\varepsilon(n)$. Since, by assumption, the discrete-logarithm problem is hard relative to $\mathcal{G}$, we conclude that $\varepsilon(n)$ is negligible.

总而言之，$\mathcal{A}^{\prime}$ 恰好以概率 $\varepsilon(n)$ 正确求解离散对数问题。既然按假设离散对数问题相对于 $\mathcal{G}$ 是困难的，我们就得出结论：$\varepsilon(n)$ 是可忽略的。

## References and Additional Reading　参考文献与延伸阅读

The book by Childs [51] has excellent coverage of the group theory discussed in this chapter (and more), in greater depth but at a similar level of exposition. Shoup [183] gives a more advanced, yet still accessible, treatment of much of this material also, with special focus on algorithmic aspects. Relatively gentle introductions to abstract algebra and group theory that go well beyond what we have space for here are available in the books by Fraleigh [74] and Herstein [97]; the interested reader will have no trouble finding more-advanced algebra texts if they are so inclined.

Childs 的书 [51] 出色地涵盖了本章所讨论的群论（以及更多内容），内容更为深入，但阐述水平与本书相近。Shoup [183] 对其中的许多材料也给出了更高级但仍易读的处理，并且特别关注算法层面的内容。Fraleigh [74] 与 Herstein [97] 的书中提供了较为平易的抽象代数与群论入门介绍，其涵盖范围远超本书篇幅所能容纳的内容；有兴趣的读者如果想更进一步，要找到更高深的代数教材并不困难。

The first efficient primality test was by Solovay and Strassen [190]. The Miller–Rabin test is due to Miller [143] and Rabin [167]. A deterministic primality test was discovered by Agrawal et al. [5]. See Dietzfelbinger [64] for a comprehensive survey of this area.

第一个高效的素性检测由 Solovay 和 Strassen [190] 提出。Miller–Rabin 检测归功于 Miller [143] 与 Rabin [167]。确定性素性检测则由 Agrawal 等人 [5] 发现。关于这一领域的全面综述参见 Dietzfelbinger [64]。

The RSA problem was publicly introduced by Rivest, Shamir, and Adleman [171], although it was revealed in 1997 that Ellis, Cocks, and Williamson, three members of the British intelligence agency GCHQ, had explored similar ideas—without fully recognizing their importance—several years earlier, in a classified setting.

RSA 问题由 Rivest、Shamir 和 Adleman [171] 公开提出；不过 1997 年披露的信息表明，英国情报机构 GCHQ 的三名成员 Ellis、Cocks 和 Williamson 早在数年之前就已在一个保密环境中探索过类似的想法——只是没有充分认识到这些想法的重要性。

The discrete-logarithm and Diffie–Hellman problems were first considered, at least implicitly, by Diffie and Hellman [65] in the group $\mathbb{Z}_p^*$. Current practical guidance for that setting can be found in various standards [15, 150, 151]. Most treatments of elliptic curves require advanced mathematical background; the book by Silverman and Tate [185] is perhaps an exception. As with many books on the subject written for mathematicians, however, that book has little coverage of elliptic curves over finite fields, which is the case most relevant to cryptography. The text by Washington [202], although a bit more advanced, deals heavily (but not exclusively) with the finite-field case. Implementation issues related to elliptic-curve cryptography are covered by Hankerson et al. [91]. Recommended elliptic curves are given by NIST [50].

离散对数问题和 Diffie–Hellman 问题最早（至少是隐含地）由 Diffie 和 Hellman [65] 在群 $\mathbb{Z}_p^*$ 中加以考虑。针对该情形的现行实用指南可参见各种标准 [15, 150, 151]。大多数关于椭圆曲线的论著都要求高深的数学背景；Silverman 和 Tate 的书 [185] 或许是个例外。然而，正如许多为数学家撰写的同类著作一样，这本书对有限域上的椭圆曲线着墨很少，而这恰恰是与密码学最相关的情形。Washington 的教材 [202] 虽然略微进阶一些，但着重（不过并非仅仅）处理有限域的情形。与椭圆曲线密码学相关的实现问题见 Hankerson 等人 [91]。推荐的椭圆曲线由 NIST [50] 给出。

The collision-resistant hash function based on the discrete-logarithm problem is due to Chaum et al. [49], and an earlier construction based on the hardness of factoring is given by Goldwasser et al. [88] (see also Exercise 9.27).

基于离散对数问题的抗碰撞哈希函数归功于 Chaum 等人 [49]；Goldwasser 等人 [88] 则给出了一个更早的、基于因子分解困难性的构造（另见习题 9.27）。

## Exercises　习题

9.1 Let $\mathbb{G}$ be an abelian group. Prove that there is a unique identity in $\mathbb{G}$, and that every element $g \in \mathbb{G}$ has a unique inverse.

9.1 设 $\mathbb{G}$ 是阿贝尔群。证明 $\mathbb{G}$ 中存在唯一的单位元，并且每个元素 $g \in \mathbb{G}$ 都有唯一的逆元。

9.2 Show that Proposition 9.36 does not necessarily hold when $\mathbb{G}$ is infinite.

9.2 证明：当 $\mathbb{G}$ 是无限群时，命题 9.36 不一定成立。

Hint: Consider the set $\{1\} \cup \{2, 4, 6, 8, \ldots\} \subset \mathbb{R}$ under multiplication.

提示：考虑 $\mathbb{R}$ 中在乘法运算下的集合 $\{1\} \cup \{2, 4, 6, 8, \ldots\}$。

9.3 Let $\mathbb{G}$ be a finite group, and $g \in \mathbb{G}$. Show that $\langle g \rangle$ is a subgroup of $\mathbb{G}$. Is the set $\{g^0, g^1, \ldots\}$ necessarily a subgroup of $\mathbb{G}$ when $\mathbb{G}$ is infinite?

9.3 设 $\mathbb{G}$ 是有限群，$g \in \mathbb{G}$。证明 $\langle g \rangle$ 是 $\mathbb{G}$ 的子群。当 $\mathbb{G}$ 是无限群时，集合 $\{g^0, g^1, \ldots\}$ 就一定是 $\mathbb{G}$ 的子群吗？

9.4 This question concerns the Euler phi function.

9.4 本题关注欧拉 $\phi$ 函数。

(a) Let $p$ be prime and $e \geq 1$ an integer. Show that $\phi(p^e) = p^{e-1}(p-1)$.

(a) 设 $p$ 为素数，$e \geq 1$ 为整数。证明 $\phi(p^e) = p^{e-1}(p-1)$。

(b) Let $p, q$ be relatively prime. Show that $\phi(pq) = \phi(p) \cdot \phi(q)$. (You may use the Chinese remainder theorem.)

(b) 设 $p, q$ 互素。证明 $\phi(pq) = \phi(p) \cdot \phi(q)$。（可以使用中国剩余定理。）

(c) Prove Theorem 9.19.

(c) 证明定理 9.19。

9.5 Compute the final two (decimal) digits of $3^{1000}$ (by hand).

9.5 手算 $3^{1000}$ 的末两位十进制数字。

Hint: The answer is $[3^{1000} \mod 100]$.

提示：答案是 $[3^{1000} \mod 100]$。

9.6 Compute $[101^{4,800,000,002} \bmod 35]$ (by hand).

9.6 手算 $[101^{4,800,000,002} \bmod 35]$。

9.7 Compute $[46^{51} \mod 55]$ (by hand) using the Chinese remainder theorem.

9.7 使用中国剩余定理计算 $[46^{51} \mod 55]$（手算）。

9.8 Prove that if $\mathbb{G}, \mathbb{H}$ are groups, then $\mathbb{G} \times \mathbb{H}$ is a group.

9.8 证明：若 $\mathbb{G}, \mathbb{H}$ 都是群，则 $\mathbb{G} \times \mathbb{H}$ 也是群。

9.9 Let p, N be integers with p | N. Prove that for any integer X,

9.9 设 $p$、$N$ 是满足 $p \mid N$ 的整数。证明：对任意整数 $X$，

$$
[\left[X\bmod N\right]\bmod p]=[X\bmod p].
$$

Show that, in contrast, $[[X \bmod p] \bmod N]$ need not equal $[X \bmod N]$.

与此相反，请证明 $[[X \bmod p] \bmod N]$ 不一定等于 $[X \bmod N]$。

9.10 This question concerns the group $\mathbb{Z}_{24}$.

9.10 本题关注群 $\mathbb{Z}_{24}$。

(a) List the elements of this group.

(a) 列出这个群的元素。

(b) Is this group cyclic?

(b) 这个群是循环群吗？

(c) Is 18 a generator of this group? What about 5?

(c) 18 是这个群的生成元吗？那 5 呢？

9.11 This question concerns the group $\mathbb{Z}_{21}^{*}$.

9.11 本题关注群 $\mathbb{Z}_{21}^{*}$。

(a) How many elements are in this group? List the elements.

(a) 这个群有多少个元素？请把它们列出来。

(b) What is $\phi(21)$?

(b) $\phi(21)$ 等于多少？

(c) Compute $[11^{-1} \bmod 21]$.

(c) 计算 $[11^{-1} \bmod 21]$。

(d) Compute $[2^{2403} \bmod 21]$ (by hand).

(d) 手算 $[2^{2403} \bmod 21]$。

9.12 This question concerns the group $\mathbb{Z}_{23}^{*}$.

9.12 本题关注群 $\mathbb{Z}_{23}^{*}$。

(a) What is the order of this group?

(a) 这个群的阶是多少？

(b) Compute $[3^{46} \bmod 23]$ (by hand).

(b) 手算 $[3^{46} \bmod 23]$。

(c) Is this group cyclic? Is 2 a generator? What about 5?

(c) 这个群是循环群吗？2 是生成元吗？那 5 呢？

9.13 This question concerns the group $\mathbb{Z}_{55}^{*}$.

9.13 本题关注群 $\mathbb{Z}_{55}^{*}$。

(a) Compute $\phi(55)$.

(a) 计算 $\phi(55)$。

(b) Is exponentiating to the 3rd power a permutation of $\mathbb{Z}_{55}^{*}$?

(b) 在 $\mathbb{Z}_{55}^{*}$ 中取三次幂是一个置换吗？

(c) Compute $[2^{1/3} \bmod 55]$ (i.e., the 3rd root of 2 modulo 55).

(c) 计算 $[2^{1/3} \bmod 55]$（也就是 2 在模 55 下的三次方根）。

(d) Is exponentiating to the 5th power a permutation of $\mathbb{Z}_{55}^{*}$?

(d) 在 $\mathbb{Z}_{55}^{*}$ 中取五次幂是一个置换吗？

9.14 Corollary 9.21 shows that if $N = pq$ for distinct primes $p$ and $q$, and $ed = 1 \bmod \phi(N)$, then for all $x \in \mathbb{Z}_N^*$, we have $(x^e)^d = x \bmod N$. Show that this holds for all $x \in \{0, \ldots, N-1\}$.

9.14 推论 9.21 表明：若 $N = pq$，其中 $p$ 与 $q$ 是不同的素数，且 $ed = 1 \bmod \phi(N)$，则对所有 $x \in \mathbb{Z}_N^*$ 都有 $(x^e)^d = x \bmod N$。证明：这对所有 $x \in \{0, \ldots, N-1\}$ 也成立。

Hint: Use the Chinese remainder theorem.

提示：使用中国剩余定理。

9.15 Complete the details of the proof of the Chinese remainder theorem, showing that $\mathbb{Z}_N^*$ is isomorphic to $\mathbb{Z}_p^* \times \mathbb{Z}_q^*$.

9.15 补全中国剩余定理证明的细节，证明 $\mathbb{Z}_N^*$ 同构于 $\mathbb{Z}_p^* \times \mathbb{Z}_q^*$。

9.16 This exercise develops an efficient algorithm for testing whether an integer is a perfect power.

9.16 本习题引导读者构造一个高效的算法，用来检验一个整数是否是完全幂。

(a) Show that if $N = \hat{N}^e$ for some integers $\hat{N}, e > 1$ then $e \leq \|N\|$.

(a) 证明：若存在整数 $\hat{N}, e > 1$ 使得 $N = \hat{N}^e$，则 $e \leq \|N\|$。

(b) Given $N$ and $e$ with $2 \leq e \leq \|N\| + 1$, show how to determine in $\mathsf{poly}(\|N\|)$ time whether there exists an integer $\hat{N}$ with $\hat{N}^e = N$.

(b) 给定 $N$ 以及满足 $2 \leq e \leq \|N\| + 1$ 的 $e$，说明如何在 $\mathsf{poly}(\|N\|)$ 时间内判定是否存在整数 $\hat{N}$ 使得 $\hat{N}^e = N$。

Hint: Use binary search.

提示：使用二分搜索。

(c) Given $N$, show how to test in $\mathsf{poly}(\|N\|)$ time whether $N$ is a perfect power.

(c) 给定 $N$，说明如何在 $\mathsf{poly}(\|N\|)$ 时间内检验 $N$ 是否为完全幂。

9.17 Given $N$ and $a \in \mathbb{Z}_N^*$, show how to test in polynomial time whether $a$ is a strong witness that $N$ is composite.

9.17 给定 $N$ 和 $a \in \mathbb{Z}_N^*$，说明如何在多项式时间内检验 $a$ 是否是“$N$ 为合数”的强见证。

9.18 Fix $N, e$ with $\gcd(e, \phi(N)) = 1$, and assume there is an adversary $\mathcal{A}$ running in time $t$ for which

9.18 固定满足 $\gcd(e, \phi(N)) = 1$ 的 $N$ 和 $e$，并假设存在运行时间为 $t$ 的敌手 $\mathcal{A}$ 使得

$$
\Pr\left[\mathcal{A}\left([x^{e}\bmod N]\right)=x\right]=0.01,
$$

where the probability is taken over uniform choice of $x \in \mathbb{Z}_N^*$. Show that it is possible to construct an adversary $\mathcal{A}^{\prime}$ for which

其中概率取遍 $x \in \mathbb{Z}_N^*$ 的均匀选择。证明：可以构造出敌手 $\mathcal{A}^{\prime}$ 使得

$$
\Pr\left[\mathcal{A}^{\prime}\left([x^{e}\bmod N]\right)=x\right]=0.99
$$

for all $x$. The running time $t^{\prime}$ of $\mathcal{A}^{\prime}$ should be polynomial in $t$ and $\|N\|$.

对所有 $x$ 都成立。$\mathcal{A}^{\prime}$ 的运行时间 $t^{\prime}$ 应当是 $t$ 和 $\|N\|$ 的多项式。

Hint: Use the fact that $y^{1/e} \cdot r = (y \cdot r^e)^{1/e} \bmod N$.

提示：利用模 $N$ 下 $y^{1/e} \cdot r = (y \cdot r^e)^{1/e}$ 这一事实。

9.19 Formally define the CDH assumption. Prove that hardness of the CDH problem relative to $\mathcal{G}$ implies hardness of the discrete-logarithm problem relative to $\mathcal{G}$, and that hardness of the DDH problem relative to $\mathcal{G}$ implies hardness of the CDH problem relative to $\mathcal{G}$.

9.19 形式化地定义 CDH 假设。证明：CDH 问题相对于 $\mathcal{G}$ 的困难性蕴含离散对数问题相对于 $\mathcal{G}$ 的困难性，并且 DDH 问题相对于 $\mathcal{G}$ 的困难性蕴含 CDH 问题相对于 $\mathcal{G}$ 的困难性。

9.20 This question concerns the cyclic group $\mathbb{Z}_{47}^*$, in which $g = 5$ is a generator. You may use a calculator.

9.20 本题关注循环群 $\mathbb{Z}_{47}^*$，其中 $g = 5$ 是一个生成元。可以使用计算器。

(a) Let $h_{1} = g^{4}$. What is the value of $h_{1}$?

(a) 设 $h_{1} = g^{4}$。$h_{1}$ 的值是多少？

(b) Let $h_{2}=g^{32}$. What is the value of $h_{2}$?

(b) 设 $h_{2}=g^{32}$。$h_{2}$ 的值是多少？

(c) What is the value of $\mathsf{DH}_{g}(h_{1}, h_{2})$?

(c) $\mathsf{DH}_{g}(h_{1}, h_{2})$ 的值是多少？

9.21 Can the following problem be solved in polynomial time? Given a prime $p$, an integer $e \in \mathbb{Z}_{p-1}^*$, and $y := [g^e \bmod p]$ (where $g$ is a uniform value in $\mathbb{Z}_p^*$), find $g$, i.e., compute $y^{1/e} \bmod p$. If your answer is “yes,” give a polynomial-time algorithm. If your answer is “no,” show a reduction to one of the assumptions introduced in this chapter.

9.21 下面这个问题能在多项式时间内求解吗？给定素数 $p$、整数 $e \in \mathbb{Z}_{p-1}^*$ 以及 $y := [g^e \bmod p]$（其中 $g$ 是 $\mathbb{Z}_p^*$ 中均匀选取的一个值），找出 $g$，即计算 $y^{1/e} \bmod p$。如果你的答案是“能”，请给出一个多项式时间算法；如果答案是“不能”，请给出到本章所引入的某个假设的归约。

9.22 Determine the points on the elliptic curve $E: y^2 = x^3 + 2x + 1$ over $\mathbb{Z}_{11}$. How many points are on this curve?

9.22 确定椭圆曲线 $E: y^2 = x^3 + 2x + 1$ 在 $\mathbb{Z}_{11}$ 上的各个点。这条曲线上共有多少个点？

9.23 Prove the third statement in Proposition 9.70.

9.23 证明命题 9.70 中的第三条陈述。

9.24 When using the twisted Edwards representation, show that the inverse of a point $(x,y)$ is the point $(-x,y)$.

9.24 使用 twisted Edwards 表示时，证明点 $(x,y)$ 的逆元是点 $(-x,y)$。

9.25 Consider the elliptic-curve group from Example 9.69. (See also Example 9.71.) Compute $(1,0)+(4,3)+(4,3)$ in this group by first converting to projective coordinates and then using Equations (9.4) and (9.5).

9.25 考虑来自例 9.69 的椭圆曲线群。（另见例 9.71。）先转换到射影坐标，再利用式 (9.4) 与式 (9.5)，在该群中计算 $(1,0)+(4,3)+(4,3)$。

9.26 Fix $N$, an element $y \in \mathbb{Z}_N^*$, and $e$ with $\gcd(e, \phi(N)) = 1$. Show that given $w \in \mathbb{Z}_N^*$ and an integer $k$ with $\gcd(k, e) = 1$ and $w^e = y^k \bmod N$, it is possible to efficiently compute $x$ such that $x^e = y \bmod N$.

9.26 固定 $N$、元素 $y \in \mathbb{Z}_N^*$，以及满足 $\gcd(e, \phi(N)) = 1$ 的 $e$。证明：给定 $w \in \mathbb{Z}_N^*$ 和满足 $\gcd(k, e) = 1$ 且 $w^e = y^k \bmod N$ 的整数 $k$，就可以高效计算出满足 $x^e = y \bmod N$ 的 $x$。

Hint: Apply Proposition 9.2 to $k$, $e$, and express $y^{1}$ as a power of $e$.

提示：把命题 9.2 应用于 $k$ 和 $e$，并把 $y^{1}$（即 $y$）表示成某个元素的 $e$ 次幂。

9.27 Let $\mathsf{GenRSA}$ be as in Section 9.2.4. Prove that if the RSA problem is hard relative to $\mathsf{GenRSA}$ then Construction 9.80 is a fixed-length collision-resistant hash function.

9.27 设 $\mathsf{GenRSA}$ 如 9.2.4 节所述。证明：如果 RSA 问题相对于 $\mathsf{GenRSA}$ 是困难的，那么构造 9.80 是一个定长抗碰撞哈希函数。

**CONSTRUCTION 9.80**

**构造 9.80**

Define $(\mathsf{Gen}, H)$ as follows:

如下定义 $(\mathsf{Gen}, H)$：

- $\mathsf{Gen}$: on input $1^n$, run $\mathsf{GenRSA}(1^n)$ to obtain $N, e, d$, and select $y \leftarrow \mathbb{Z}_N^*$. The key is $s := \langle N, e, y \rangle$.

  Gen：以 $1^n$ 为输入，运行 $\mathsf{GenRSA}(1^{n})$ 得到 $N, e, d$，并选取 $y \leftarrow \mathbb{Z}_N^*$。密钥为 $s := \langle N, e, y \rangle$。

- $H$: if $s = \langle N, e, y \rangle$, then $H^s$ maps inputs in $\{0,1\}^{3n}$ to outputs in $\mathbb{Z}_N^*$. Let $f_0^s(x) \stackrel{\mathrm{def}}{=} [x^e \bmod N]$ and $f_1^s(x) \stackrel{\mathrm{def}}{=} [y \cdot x^e \bmod N]$. For a $3n$-bit long string $x = x_1 \cdots x_{3n}$, define

  $H$：若 $s = \langle N, e, y \rangle$，则 $H^s$ 把 $\{0,1\}^{3n}$ 中的输入映射为 $\mathbb{Z}_N^*$ 中的输出。令 $f_0^s(x) \stackrel{\mathrm{def}}{=} [x^e \bmod N]$、$f_1^s(x) \stackrel{\mathrm{def}}{=} [y \cdot x^e \bmod N]$。对于长为 $3n$ 比特的串 $x = x_1 \cdots x_{3n}$，定义

  $$
  H^{s}(x)\stackrel{\mathrm{def}}{=}f_{x_{1}}^{s}\left(f_{x_{2}}^{s}\left(\cdots\left(1\right)\cdots\right)\right).
  $$

9.28 Consider the following generalization of Construction 9.78:

9.28 考虑构造 9.78 的如下推广：

**CONSTRUCTION 9.81**

**构造 9.81**

Define a fixed-length hash function $(\mathsf{Gen}, H)$ as follows:

如下定义定长哈希函数 $(\mathsf{Gen}, H)$：

(a) $\mathsf{Gen}$: on input $1^n$, run $\mathcal{G}(1^n)$ to obtain $(\mathbb{G}, q, h_1)$ and then select $h_2, \ldots, h_t \leftarrow \mathbb{G}$. Output $s := \langle \mathbb{G}, q, (h_1, \ldots, h_t) \rangle$ as the key.

(a) Gen：以 $1^n$ 为输入，运行 $\mathcal{G}(1^n)$ 得到 $(\mathbb{G}, q, h_1)$，然后选取 $h_2, \ldots, h_t \leftarrow \mathbb{G}$。输出 $s := \langle \mathbb{G}, q, (h_1, \ldots, h_t) \rangle$ 作为密钥。

(b) $H$: given a key $s = \langle \mathbb{G}, q, (h_1, \ldots, h_t) \rangle$ and input $(x_1, \ldots, x_t)$ with $x_i \in \mathbb{Z}_q$, output $H^s(x_1, \ldots, x_t) := \prod_i h_i^{x_i}$.

(b) $H$：给定密钥 $s = \langle \mathbb{G}, q, (h_1, \ldots, h_t) \rangle$ 和满足 $x_i \in \mathbb{Z}_q$ 的输入 $(x_1, \ldots, x_t)$，输出 $H^s(x_1, \ldots, x_t) := \prod_i h_i^{x_i}$。

(a) Prove that if the discrete-logarithm problem is hard relative to $\mathcal{G}$ and $q$ is prime, then for any $t = \mathsf{poly}(n)$ this construction is a fixed-length collision-resistant hash function.

(a) 证明：如果离散对数问题相对于 $\mathcal{G}$ 是困难的且 $q$ 是素数，那么对任意 $t = \mathsf{poly}(n)$，这个构造都是一个定长抗碰撞哈希函数。

(b) Discuss how this construction can be used to obtain compression regardless of the number of bits needed to represent elements of $\mathbb{G}$ (as long as it is polynomial in $n$).

(b) 讨论如何用这一构造获得压缩，而不论表示 $\mathbb{G}$ 中元素需要多少个比特（只要它是 $n$ 的多项式）。
