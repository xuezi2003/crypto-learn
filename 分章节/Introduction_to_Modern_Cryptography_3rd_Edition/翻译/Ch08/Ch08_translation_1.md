# Chapter 8: Theoretical Constructions of Symmetric-Key Primitives　第八章　对称密钥原语的理论构造

In Chapter 3 we introduced the notion of pseudorandomness and defined some basic cryptographic primitives including pseudorandom generators, functions, and permutations. We further showed in Chapters 3–5 that these primitives can serve as building blocks for all of private-key cryptography. As such, it is of great importance to understand these primitives from a theoretical point of view. In this chapter we formally introduce the concept of one-way functions—functions that are, informally, easy to compute but hard to invert—and show how pseudorandom generators, functions, and permutations can be constructed under the sole assumption that one-way functions exist. $^{1}$ Moreover, we will see that one-way functions are necessary for “non-trivial” private-key cryptography. That is: the existence of one-way functions is equivalent to the existence of all (non-trivial) private-key cryptography. This is one of the major contributions of modern cryptography.

在第 3 章中，我们介绍了伪随机性的概念，并定义了包括伪随机生成器、伪随机函数和伪随机置换在内的一些基本密码学原语。我们还在第 3–5 章进一步证明了这些原语可以作为整个私钥密码学的构建模块。因此，从理论角度理解这些原语至关重要。在本章中，我们正式介绍单向函数的概念——非正式地说，单向函数是易于计算却难以求逆的函数——并展示如何在“单向函数存在”这一唯一假设下构造伪随机生成器、伪随机函数和伪随机置换。$^{1}$ 此外，我们将看到单向函数对“非平凡”私钥密码学而言是必要的。也就是说：单向函数的存在性等价于所有（非平凡）私钥密码学的存在性。这是现代密码学的主要贡献之一。

> $^{1}$ 原书脚注：Although we will for the most part rely on the stronger assumption of one-way permutations in this chapter, it is known that one-way functions suffice.（本章大部分内容将依赖更强的“单向置换存在”假设，但已知单向函数便已足够。）

The constructions we show in this chapter should be viewed as complementary to the constructions of stream ciphers and block ciphers discussed in the previous chapter. The focus of the previous chapter was on how various cryptographic primitives are currently realized in practice, and the intent of that chapter was to introduce some basic approaches and design principles that are used. Somewhat disappointing, though, was the fact that none of the constructions we showed could be proven secure based on any weaker (i.e., more reasonable) assumptions. In contrast, in this chapter we will show constructions that can be proven secure starting from the very mild assumption that one-way functions exist. That assumption is more appealing than assuming, say, that AES is a pseudorandom permutation, both because it is a qualitatively weaker assumption and also because we have a number of candidate, number-theoretic one-way functions that have been studied for many years, even before the advent of cryptography. (See the very beginning of Chapter 7 for further discussion of this point.) The downside, however, is that the constructions we show here are all far less efficient than those of Chapter 7, and thus (currently) have little practical significance. It remains an important challenge for cryptographers to "bridge this gap" and develop provably secure constructions of pseudorandom generators and permutations whose efficiency is comparable to the best available stream ciphers and block ciphers.

本章展示的构造应视为对上一章所讨论的流密码与分组密码构造的补充。上一章的重点是各类密码学原语目前在实践中如何实现，其意图是介绍其中用到的一些基本方法和设计原则。不过令人有些失望的是，我们所展示的构造没有一个能基于更弱（即更合理）的假设证明其安全性。与此相反，本章将展示的构造可以从“单向函数存在”这一极为温和的假设出发证明其安全性。这一假设比假定（比方说）AES 是伪随机置换更具吸引力，原因有二：一方面它在性质上是更弱的假设，另一方面我们已有许多候选的数论单向函数，它们被研究多年，甚至早于密码学的出现。（关于这一点的进一步讨论见第 7 章开头。）然而其缺点在于，本章展示的构造效率都远低于第 7 章的构造，因而（目前）几乎没有实用价值。“弥合这一差距”——开发出效率可与现有最佳流密码和分组密码相媲美的、可证明安全的伪随机生成器与置换构造——仍是密码学家面临的一项重要挑战。

Collision-resistant hash functions. Unlike the previous chapter, here we do not consider collision-resistant hash functions. The reason is that constructions of such hash functions from one-way functions are unknown and, in fact, there is evidence suggesting that such constructions are impossible. We will see a provably secure construction of a collision-resistant hash function—based on a specific, number-theoretic assumption—in Section 9.4.2.

**抗碰撞哈希函数。**

与上一章不同，本章不考虑抗碰撞哈希函数。原因在于，目前还不知道如何从单向函数构造这类哈希函数；事实上，有证据表明这样的构造是不可能的。我们将在 9.4.2 节看到一个可证明安全的抗碰撞哈希函数构造——它基于一个具体的数论假设。

A note regarding this chapter. The material in this chapter is somewhat more advanced than the material in the rest of this book. This material is not used explicitly anywhere else in the book, and so can be skipped if desired. Having said this, we have tried to present the material in such a way that it is understandable (with effort) to an advanced undergraduate or beginning graduate student. We encourage all readers to peruse Sections 8.1 and 8.2, which introduce one-way functions and provide an overview of the rest of this chapter. We believe that familiarity with at least some of the topics covered here is important enough to warrant the effort.

**关于本章的说明。**

本章内容比本书其余部分的内容略显进阶。这些内容在本书其他任何地方都没有被显式使用，因此如愿意可以跳过。尽管如此，我们已尽力以高年级本科生或研究生新生（在付出努力后）能够理解的方式来呈现这些内容。我们鼓励所有读者通读 8.1 节和 8.2 节，它们介绍单向函数并概述本章其余内容。我们认为，熟悉这里讲述的至少部分主题非常重要，值得为此付出努力。

## 8.1 One-Way Functions　单向函数

In this section we formally define one-way functions, and then briefly discuss some candidates that are believed to satisfy this definition. (We will see more examples of conjectured one-way functions in Chapter 9.) We next introduce the notion of hard-core predicates, which can be viewed as encapsulating the hardness of inverting a one-way function and will be used extensively in the constructions that follow in subsequent sections.

在本节中，我们正式定义单向函数，然后简要讨论一些被认为满足这一定义的候选函数。（我们将在第 9 章看到更多猜想为单向函数的例子。）接下来我们介绍难核谓词的概念；它可以视为封装了对单向函数求逆的困难性，并将在后续小节的构造中得到广泛使用。

### 8.1.1 Definitions　定义

A one-way function $f: \{0,1\}^* \to \{0,1\}^*$ is easy to compute, yet hard to invert. The first condition is easy to formalize: we will simply require that $f$ be computable in polynomial time. Since we are ultimately interested in building cryptographic schemes that are hard for a probabilistic polynomial-time adversary to break except with negligible probability, we will formalize the second condition by requiring that it be infeasible for any probabilistic polynomial-time algorithm to invert $f$—that is, to find a preimage of a given value $y$—except with negligible probability. A technical point is that this probability is taken over an experiment in which $y$ is generated by choosing a uniform element $x$ in the domain of $f$ and then setting $y := f(x)$ (rather than choosing $y$ uniformly from the range of $f$). The reason for this should become clear from the constructions we will see in the remainder of the chapter.

单向函数 $f: \{0,1\}^* \to \{0,1\}^*$ 易于计算，却难以求逆。第一个条件很容易形式化：我们只要求 $f$ 可以在多项式时间内计算。由于我们最终感兴趣的是构造这样的密码方案——除可忽略的概率外，概率多项式时间敌手很难攻破它——我们把第二个条件形式化为：任何概率多项式时间算法对 $f$ 求逆——即对给定的值 $y$ 找到原像——成功的概率都是可忽略的。一个技术性的要点是，这一概率是在如下实验中取的：先在 $f$ 的定义域中均匀选取元素 $x$ 并令 $y := f(x)$（而不是从 $f$ 的值域中均匀选取 $y$）。其原因从本章余下部分将看到的构造中可以看得清楚。

Let $f: \{0,1\}^* \to \{0,1\}^*$ be a function. Consider the following experiment defined for any algorithm $\mathcal{A}$ and any value $n$ for the security parameter:

设 $f: \{0,1\}^* \to \{0,1\}^*$ 是一个函数。考虑为任意算法 $\mathcal{A}$ 和安全参数的任意取值 $n$ 定义的如下实验：

The inverting experiment $\mathsf{Invert}_{\mathcal{A}, f}(n)$

求逆实验 $\mathsf{Invert}_{\mathcal{A}, f}(n)$

1. Choose uniform $x \in \{0,1\}^{n}$, and compute $y := f(x)$.

   均匀选取 $x \in \{0,1\}^{n}$，并计算 $y := f(x)$。

2. A is given ${1}^{n}$ and y as input, and outputs $x^{\prime}$.

   将 ${1}^{n}$ 和 $y$ 作为输入交给 $\mathcal{A}$，$\mathcal{A}$ 输出 $x^{\prime}$。

3. The output of the experiment is defined to be 1 if $f(x^{\prime}) = y$, and 0 otherwise.

   若 $f(x^{\prime}) = y$，则实验输出定义为 1；否则为 0。

We stress that $\mathcal{A}$ need not find the original preimage $x$; it suffices for $\mathcal{A}$ to find any value $x^{\prime}$ for which $f(x^{\prime}) = y = f(x)$. The security parameter ${1}^n$ is given to $\mathcal{A}$ in the second step to stress that $\mathcal{A}$ may run in time polynomial in the security parameter $n$, regardless of the length of $y$.

我们强调，$\mathcal{A}$ 无需找出最初的原像 $x$；$\mathcal{A}$ 只要找到任意一个满足 $f(x^{\prime}) = y = f(x)$ 的值 $x^{\prime}$ 即可。第二步把安全参数 ${1}^n$ 交给 $\mathcal{A}$，是为了强调 $\mathcal{A}$ 的运行时间可以是安全参数 $n$ 的多项式，而与 $y$ 的长度无关。

We can now define what it means for a function f to be one-way.

现在我们可以给出“函数 $f$ 是单向的”这一定义。

DEFINITION 8.1 A function $f: \{0,1\}^* \to \{0,1\}^*$ is one-way if the following two conditions hold:

定义 8.1　若函数 $f: \{0,1\}^* \to \{0,1\}^*$ 满足以下两个条件，则称其为单向函数：

1. (Easy to compute:) There exists a polynomial-time algorithm $M_{f}$ computing f; that is, $M_{f}(x) = f(x)$ for all x.

   （易于计算：）存在计算 $f$ 的多项式时间算法 $M_{f}$；即对所有 $x$ 都有 $M_{f}(x) = f(x)$。

2. (Hard to invert:) For every probabilistic polynomial-time algorithm A, there is a negligible function $\mathsf{negl}$ such that

   （难以求逆：）对每个概率多项式时间算法 $\mathcal{A}$，存在可忽略函数 $\mathsf{negl}$ 使得

   $$
   \Pr[\mathsf{Invert}_{\mathcal{A},f}(n)=1]\leq\mathsf{negl}(n).
   $$

Notation. In this chapter we will often make the probability space more explicit by subscripting (part of) it in the probability notation. For example, we can succinctly express the second requirement in the definition above as follows: For every probabilistic polynomial-time algorithm A, there exists a negligible function $\mathsf{negl}$ such that

**记号。**

在本章中，我们常常通过把（部分）概率空间写成概率记号的下标，使概率空间更加明确。例如，上一定义中的第二个要求可以简洁地表述如下：对每个概率多项式时间算法 $\mathcal{A}$，存在可忽略函数 $\mathsf{negl}$ 使得

$$
\Pr_{x\leftarrow\{0,1\}^{n}}\left[\mathcal{A}(1^{n},f(x))\in f^{-1}(f(x))\right]\leq\mathsf{negl}(n).
$$

(Recall that $x \leftarrow \{0,1\}^n$ means that $x$ is chosen uniformly from $\{0,1\}^n$.) The probability above is also taken over the randomness used by $\mathcal{A}$, which here is left implicit.

（回顾一下，$x \leftarrow \{0,1\}^n$ 表示 $x$ 从 $\{0,1\}^n$ 中均匀选取。）上式中的概率还取遍 $\mathcal{A}$ 自身的随机性，这里略去不写。

Successful inversion of one-way functions. A function that is not one-way is not necessarily easy to invert all the time (or even “often”). Rather, the converse of the second condition of Definition 8.1 is that there exists a probabilistic polynomial-time algorithm $\mathcal{A}$ and a non-negligible function $\gamma$ such that $\mathcal{A}$ inverts $f(x)$ with probability at least $\gamma(n)$ (where the probability is taken over uniform choice of $x \in \{0,1\}^n$ and the randomness of $\mathcal{A}$). This means, in turn, that there exists a positive polynomial $p(\cdot)$ such that for
infinitely many values of $n$, algorithm $\mathcal{A}$ inverts $f$ with probability at least ${1}/{p(n)}$. Thus, if there exists an $\mathcal{A}$ that inverts $f$ with probability $n^{-10}$ for all even values of $n$ (but always fails to invert $f$ when $n$ is odd), then $f$ is not one-way—even though $\mathcal{A}$ only succeeds on half the values of $n$, and only succeeds with probability $n^{-10}$ (for values of $n$ where it succeeds at all).

**单向函数的成功求逆。**

不是单向函数，并不意味着它总是容易求逆（甚至不意味着它“经常”容易求逆）。确切地说，定义 8.1 第二个条件的否定是：存在概率多项式时间算法 $\mathcal{A}$ 和非可忽略函数 $\gamma$，使得 $\mathcal{A}$ 以至少 $\gamma(n)$ 的概率对 $f(x)$ 求逆（概率取遍 $x \in \{0,1\}^n$ 的均匀选择和 $\mathcal{A}$ 的随机性）。这又意味着：存在正多项式 $p(\cdot)$，使得对无穷多个 $n$ 的取值，算法 $\mathcal{A}$ 以至少 ${1}/{p(n)}$ 的概率对 $f$ 求逆。因此，若存在算法 $\mathcal{A}$，对所有偶数 $n$ 以 $n^{-10}$ 的概率对 $f$ 求逆（而当 $n$ 为奇数时总是求逆失败），那么 $f$ 就不是单向函数——尽管 $\mathcal{A}$ 只在一半的 $n$ 取值上成功，而且（在其能成功的那些 $n$ 取值上）成功概率也只有 $n^{-10}$。

Exponential-time inversion. Any one-way function can be inverted at any point $y$ in exponential time, by simply trying all values $x \in \{0,1\}^n$ until a value $x$ is found such that $f(x) = y$. Thus, the existence of one-way functions is inherently an assumption about computational complexity and computational hardness. That is, it concerns a problem that can be solved in principle but is assumed to be hard to solve efficiently.

**指数时间求逆。**

任何单向函数在任意点 $y$ 处都可以用指数时间求逆：只需逐一尝试所有 $x \in \{0,1\}^n$，直到找到满足 $f(x) = y$ 的值 $x$。因此，单向函数的存在性本质上是一个关于计算复杂性和计算困难性的假设。也就是说，它关注的是一个原则上可解、但被假定难以高效求解的问题。

One-way permutations. We will often be interested in one-way functions with additional structural properties. We say a function $f$ is length-preserving if $|f(x)| = |x|$ for all $x$. A one-way function that is length-preserving and one-to-one is called a one-way permutation. If $f$ is a one-way permutation, then any value $y$ has a unique preimage $x = f^{-1}(y)$. Nevertheless, it is still hard to find $x$ in polynomial time.

**单向置换。**

我们常常对具有额外结构性质的单向函数感兴趣。若函数 $f$ 对所有 $x$ 都满足 $|f(x)| = |x|$，则称 $f$ 是保长度的。保长度且一一对应的单向函数称为单向置换。若 $f$ 是单向置换，则任意值 $y$ 都有唯一的原像 $x = f^{-1}(y)$。尽管如此，在多项式时间内找到 $x$ 仍然是困难的。

One-way function/permutation families. The above definitions of one-way functions and permutations are convenient in that they consider a single function over an infinite domain and range. However, most candidate one-way functions and permutations do not fit neatly into this framework. Instead, there is an algorithm generating some set of parameters I that define a function $f_I$; one-wayness here means essentially that $f_I$ should be one-way with all but negligible probability over choice of I. Because each value of I defines a different function, we now refer to families of one-way functions (resp., permutations). We give the definition now, and refer the reader to the next section for a concrete example. (See also Section 9.4.1.)

**单向函数/置换族。**

上述单向函数与单向置换的定义很方便，因为它们考虑的是定义在无穷定义域和值域上的单个函数。然而，大多数候选单向函数和单向置换并不能整齐地纳入这一框架。实际上，做法是由一个算法生成某组参数 $I$，由 $I$ 定义函数 $f_I$；这里的单向性实质上是指：除可忽略的概率外，在 $I$ 的随机选取下 $f_I$ 都是单向的。由于 $I$ 的每个取值定义一个不同的函数，我们现在改称单向函数（相应地，单向置换）族。我们在此给出定义，具体例子见下一节。（另见 9.4.1 节。）

DEFINITION 8.2 A tuple $\Pi = (\mathsf{Gen}, \mathsf{Samp}, f)$ of probabilistic polynomial-time algorithms is a function family if the following hold:

定义 8.2　若由概率多项式时间算法构成的三元组 $\Pi = (\mathsf{Gen}, \mathsf{Samp}, f)$ 满足以下条件，则称其为函数族：

1. The parameter-generation algorithm Gen, on input ${1}^n$, outputs parameters $I$ with $|I| \geq n$. Each value of $I$ output by Gen defines sets $\mathcal{D}_I$ and $\mathcal{R}_I$ that constitute the domain and range, respectively, of a function $f_I$.

   参数生成算法 $\mathsf{Gen}$ 以 ${1}^n$ 为输入，输出满足 $|I| \geq n$ 的参数 $I$。$\mathsf{Gen}$ 输出的每个 $I$ 取值定义集合 $\mathcal{D}_I$ 和 $\mathcal{R}_I$，二者分别构成函数 $f_I$ 的定义域和值域。

2. The sampling algorithm Samp, on input I, outputs a uniformly distributed element of $\mathcal{D}_{I}$.

   采样算法 $\mathsf{Samp}$ 以 $I$ 为输入，输出 $\mathcal{D}_{I}$ 中均匀分布的一个元素。

3. The deterministic evaluation algorithm $f$, on input $I$ and $x \in \mathcal{D}_I$, outputs an element $y \in \mathcal{R}_I$. We write this as $y := f_I(x)$.

   确定性求值算法 $f$ 以 $I$ 和 $x \in \mathcal{D}_I$ 为输入，输出元素 $y \in \mathcal{R}_I$。记作 $y := f_I(x)$。

 $\Pi$ is a permutation family if for each value of $I$ output by $\mathsf{Gen}(1^n)$, it holds that $\mathcal{D}_I = \mathcal{R}_I$ and the function $f_I : \mathcal{D}_I \to \mathcal{D}_I$ is a bijection.

 若对 $\mathsf{Gen}(1^n)$ 输出的每个 $I$ 取值，都有 $\mathcal{D}_I = \mathcal{R}_I$ 且函数 $f_I : \mathcal{D}_I \to \mathcal{D}_I$ 是双射，则 $\Pi$ 是置换族。

Let $\Pi$ be a function family. What follows is the natural analogue of the experiment introduced previously.

设 $\Pi$ 是一个函数族。下面给出的是前文所述实验的自然类比。

The inverting experiment $\mathsf{Invert}_{\mathcal{A}, \Pi}(n)$:

求逆实验 $\mathsf{Invert}_{\mathcal{A}, \Pi}(n)$：

1. $\mathsf{Gen}(1^n)$ is run to obtain $I$, and then $\mathsf{Samp}(I)$ is run to obtain a uniform $x \in \mathcal{D}_I$. Finally, $y := f_I(x)$ is computed.

   运行 $\mathsf{Gen}(1^n)$ 得到 $I$，然后运行 $\mathsf{Samp}(I)$ 得到均匀的 $x \in \mathcal{D}_I$。最后计算 $y := f_I(x)$。

2. A is given I and y as input, and outputs x'.

   将 $I$ 和 $y$ 作为输入交给 $\mathcal{A}$，$\mathcal{A}$ 输出 $x^{\prime}$。

3. The output of the experiment is 1 if $f_{I}(x^{\prime}) = y$.

   若 $f_{I}(x^{\prime}) = y$，则实验输出为 1。

DEFINITION 8.3 A function/permutation family $\Pi = (\mathsf{Gen}, \mathsf{Samp}, f)$ is one-way if for all probabilistic polynomial-time algorithms $\mathcal{A}$ there exists a negligible function $\mathsf{negl}$ such that

定义 8.3　若函数/置换族 $\Pi = (\mathsf{Gen}, \mathsf{Samp}, f)$ 满足：对每个概率多项式时间算法 $\mathcal{A}$，都存在可忽略函数 $\mathsf{negl}$ 使得

$$
\Pr[\mathsf{Invert}_{\mathcal{A},\Pi}(n)=1]\leq\mathsf{negl}(n).
$$

Throughout this chapter we work with one-way functions/permutations over an infinite domain (as in Definition 8.1), rather than working with families of one-way functions/permutations. This is primarily for convenience, and does not significantly affect any of the results. (See Exercise 8.7.)

在本章中，我们始终使用定义在无穷定义域上的单向函数/置换（如定义 8.1 所述），而不使用单向函数/置换族。这主要是出于方便，并且不会显著影响任何结果。（见习题 8.7。）

### 8.1.2 Candidate One-Way Functions　候选单向函数

One-way functions are of interest only if they exist. We do not know how to prove they exist unconditionally (this would be a major breakthrough in complexity theory), so we must conjecture or assume their existence. Such a conjecture is based on the fact that several natural computational problems have received much attention, yet still are not known to be solvable by any polynomial-time algorithm. Perhaps the most famous such problem is integer factorization, i.e., finding the prime factors of a large integer. It is easy to multiply two numbers and obtain their product, but difficult to take a number and find its factors. This leads us to define the function $f_{\mathsf{mult}}(x, y) = x \cdot y$. If we do not restrict the lengths of x and y, however, $f_{\mathsf{mult}}$ is easy to invert: with high probability $x \cdot y$ will be even, in which case $(2, xy/2)$ is an inverse. This issue can be addressed by restricting the domain of $f_{\mathsf{mult}}$ to equal-length primes x and y. We return to this idea in Section 9.2.

单向函数只有在其存在时才有研究价值。我们不知道如何无条件地证明它们存在（那将是复杂性理论的重大突破），因此必须猜想或假设其存在。这一猜想基于如下事实：若干自然的计算问题已受到大量关注，但至今仍不知道有任何多项式时间算法能够求解。此类问题中最著名的也许是整数分解，即找出一个大整数的素因子。把两个数相乘得到乘积很容易，但取一个数并找出它的因子却很困难。由此我们定义函数 $f_{\mathsf{mult}}(x, y) = x \cdot y$。然而，如果不限制 $x$ 和 $y$ 的长度，$f_{\mathsf{mult}}$ 是容易求逆的：$x \cdot y$ 以很大概率是偶数，此时 $(2, xy/2)$ 就是一个原像。把 $f_{\mathsf{mult}}$ 的定义域限制为等长的素数 $x$ 和 $y$ 即可解决这一问题。我们将在 9.2 节回到这一想法。

Another candidate one-way function, not relying directly on number theory, is based on the subset-sum problem and is defined by

另一个不直接依赖数论的候选单向函数基于子集求和问题，定义如下

$$
f_{\mathsf{ss}}(x_{1},\ldots,x_{n},J)=\left(x_{1},\ldots,x_{n},\;\left[\textstyle\sum_{j\in J}x_{j}\bmod2^{n}\right]\right),
$$

where each $x_i$ is an $n$-bit string interpreted as an integer, and $J$ is an $n$-bit string interpreted as specifying a subset of $\{1, \ldots, n\}$. Inverting $f_{\mathsf{ss}}$ on an output $(x_1, \ldots, x_n, y)$ requires finding a subset $J^{\prime} \subseteq \{1, \ldots, n\}$ such that

其中每个 $x_i$ 是按整数解释的 $n$ 比特串；$J$ 是指定 $\{1, \ldots, n\}$ 的某个子集的 $n$ 比特串。在输出 $(x_1, \ldots, x_n, y)$ 上对 $f_{\mathsf{ss}}$ 求逆，需要找到子集 $J^{\prime} \subseteq \{1, \ldots, n\}$ 使得

$$
\sum_{j \in J} x_j = y \mod 2^n.
$$

Readers who have studied $\mathcal{NP}$-completeness may recall that this problem is $\mathcal{NP}$-complete. But even $\mathcal{P} \neq \mathcal{NP}$ would not imply that $f_{\mathsf{ss}}$ is one-way: $\mathcal{P} \neq \mathcal{NP}$ would mean that every polynomial-time algorithm fails to solve the subset-sum problem on at least one input, whereas for $f_{\text{ss}}$ to be one-way it is required that every polynomial-time algorithm fails to solve the subset-sum problem (at least for certain parameters) almost always. Thus, our belief that the function above is one-way is based on the lack of known algorithms to solve this problem even with “small” probability on random inputs, and not merely the fact that the problem is $\mathcal{NP}$-complete.

学过 $\mathcal{NP}$ 完全性的读者也许记得，该问题是 $\mathcal{NP}$ 完全的。但即使 $\mathcal{P} \neq \mathcal{NP}$ 也推不出 $f_{\mathsf{ss}}$ 是单向的：$\mathcal{P} \neq \mathcal{NP}$ 只意味着每个多项式时间算法都至少在一个输入上无法求解子集求和问题，而要使 $f_{\text{ss}}$ 是单向的，则要求每个多项式时间算法（至少对某些参数）几乎总是无法求解子集求和问题。因此，我们相信上述函数是单向的，依据是：目前没有已知算法能在随机输入上哪怕以“小”的概率求解该问题，而不仅仅是该问题是 $\mathcal{NP}$ 完全的这一事实。

We conclude by showing a family of permutations that is believed to be one-way. Let $\mathsf{Gen}$ be a probabilistic polynomial-time algorithm that, on input ${1}^n$, outputs an $n$-bit prime $p$ along with a special element $g \in \{2, \ldots, p-1\}$. (The element $g$ should be a generator of $\mathbb{Z}_p^*$; see Section 9.3.3.) Let $\mathsf{Samp}$ be an algorithm that, given $p$ and $g$, outputs a uniform integer $x \in \{1, \ldots, p-1\}$. Finally, define

最后，我们给出一个被认为是单向的置换族。设 $\mathsf{Gen}$ 是一个概率多项式时间算法，以 ${1}^n$ 为输入，输出 $n$ 比特素数 $p$ 以及一个特殊元素 $g \in \{2, \ldots, p-1\}$。（元素 $g$ 应当是 $\mathbb{Z}_p^*$ 的生成元；见 9.3.3 节。）设 $\mathsf{Samp}$ 是如下算法：给定 $p$ 和 $g$，输出均匀的整数 $x \in \{1, \ldots, p-1\}$。最后，定义

$$
f_{p,g}(x)=[g^{x}\bmod p].
$$

(The fact that $f_{p,g}$ can be computed efficiently follows from the results in Appendix B.2.3.) It can be shown that this function is one-to-one, and thus a permutation. The presumed difficulty of inverting this function is based on the conjectured hardness of the discrete-logarithm problem; we will have much more to say about this in Section 9.3.

（$f_{p,g}$ 可以高效计算这一事实可由附录 B.2.3 的结果得到。）可以证明该函数是一一对应的，因而是置换。人们假定对此函数求逆是困难的，其依据是离散对数问题被猜想为困难的；我们将在 9.3 节对此展开更多讨论。

Finally, we remark that very efficient one-way functions can be obtained from practical cryptographic constructions such as SHA-2 or AES under the assumption that they are collision resistant or a pseudorandom permutation, respectively; see Exercises 8.4 and 8.5. (Technically speaking, they cannot satisfy the definition of one-wayness since they have fixed-length input/output and so their asymptotic behavior is undefined. Nevertheless, it is plausible to conjecture that they are one-way in a concrete sense.)

最后我们指出，若分别假设 SHA-2 或 AES 是抗碰撞的或是伪随机置换，则可以从 SHA-2、AES 这类实用的密码学构造得到非常高效的单向函数；见习题 8.4 和习题 8.5。（严格来说，它们无法满足单向性的定义，因为其输入/输出长度固定，渐近行为没有定义。尽管如此，猜想它们在具体意义下是单向的仍是合理的。）

### 8.1.3 Hard-Core Predicates　难核谓词

By definition, a one-way function is hard to invert. Stated differently: given $y = f(x)$, the value $x$ cannot be computed in its entirety by any polynomial-time algorithm (except with negligible probability; we ignore this here). One might get the impression that nothing about $x$ can be determined from $f(x)$ in polynomial time. This is not necessarily the case. Indeed, it is possible for $f(x)$ to “leak” a lot of information about $x$ even if $f$ is one-way. For a trivial example, let $g$ be a one-way function and define $f(x_1, x_2) \overset{\mathrm{def}}{=} (x_1, g(x_2))$, where $|x_1| = |x_2|$. It is easy to show that $f$ is also a one-way function (this is left as an exercise), even though it reveals half its input.

根据定义，单向函数难以求逆。换一种说法：给定 $y = f(x)$，任何多项式时间算法都无法完整计算出 $x$（除可忽略的概率外；这里我们忽略这一点）。人们可能由此产生一种印象：在多项式时间内无法从 $f(x)$ 得知关于 $x$ 的任何信息。情况未必如此。事实上，即使 $f$ 是单向的，$f(x)$ 也可能“泄露”关于 $x$ 的许多信息。举一个平凡的例子：设 $g$ 是单向函数，定义 $f(x_1, x_2) \overset{\mathrm{def}}{=} (x_1, g(x_2))$，其中 $|x_1| = |x_2|$。容易证明 $f$ 也是单向函数（留作习题），尽管它泄露了一半的输入。

For our applications, we will need to identify a specific piece of information about $x$ that is “hidden” by $f(x)$. This motivates the notion of a hard-core predicate. A hard-core predicate $\mathsf{hc} : \{0,1\}^* \to \{0,1\}$ of a function $f$ has the property that $\mathsf{hc}(x)$ is hard to compute with probability significantly better than 1/2 given $f(x)$. (Since hc is a boolean function, it is always possible to compute $\mathsf{hc}(x)$ with probability 1/2 by random guessing.) Formally:

在我们的应用中，需要找出被 $f(x)$ “隐藏”的关于 $x$ 的某一条特定信息。这引出了难核谓词的概念。函数 $f$ 的难核谓词 $\mathsf{hc} : \{0,1\}^* \to \{0,1\}$ 具有如下性质：给定 $f(x)$，以显著优于 1/2 的概率计算 $\mathsf{hc}(x)$ 是困难的。（由于 $\mathsf{hc}$ 是布尔函数，通过随机猜测总能以概率 1/2 计算出 $\mathsf{hc}(x)$。）形式化表述如下：

DEFINITION 8.4 A function $\mathsf{hc} : \{0,1\}^* \to \{0,1\}$ is a hard-core predicate of a function $f$ if $\mathsf{hc}$ can be computed in polynomial time, and for every probabilistic polynomial-time algorithm $\mathcal{A}$ there is a negligible function $\mathsf{negl}$ such that

定义 8.4　若函数 $\mathsf{hc} : \{0,1\}^* \to \{0,1\}$ 可以在多项式时间内计算，且对每个概率多项式时间算法 $\mathcal{A}$，都存在可忽略函数 $\mathsf{negl}$ 使得

$$
\Pr_{x\gets\{0,1\}^{n}}[\mathcal{A}(1^{n},f(x))=\mathsf{hc}(x)]\leq\frac{1}{2}+\mathsf{negl}(n),
$$

where the probability is taken over the uniform choice of x in $\{0,1\}^{n}$ and the randomness of A.

其中概率取遍 $x$ 在 $\{0,1\}^{n}$ 中的均匀选择以及 $\mathcal{A}$ 的随机性。

We stress that $\mathsf{hc}(x)$ is efficiently computable given $x$ (since the function $\mathsf{hc}$ can be computed in polynomial time); the definition requires that $\mathsf{hc}(x)$ is hard to compute given $f(x)$. The above definition does not require f to be one-way; if f is a permutation, however, then it cannot have a hard-core predicate unless it is one-way. (See Exercise 8.13.)

我们强调，给定 $x$ 时 $\mathsf{hc}(x)$ 是可以高效计算的（因为函数 $\mathsf{hc}$ 可以在多项式时间内计算）；该定义要求的是给定 $f(x)$ 时 $\mathsf{hc}(x)$ 难以计算。上述定义并不要求 $f$ 是单向的；然而，若 $f$ 是置换，那么除非它是单向的，否则它不可能拥有难核谓词。（见习题 8.13。）

Simple ideas don’t work. Consider the predicate $\mathsf{hc}(x) \overset{\mathrm{def}}{=} \bigoplus_{i=1}^{n} x_i$ where $x_1, \ldots, x_n$ denote the bits of $x$. One might hope that this is a hard-core predicate of any one-way function $f$: if $f$ cannot be inverted, then $f(x)$ must hide at least one of the bits $x_i$ of its preimage $x$, which would seem to imply that the XOR of all of the bits of $x$ is hard to compute. Despite its appeal, this argument is incorrect. To see this, let $g$ be a one-way function and define $f(x) \overset{\mathrm{def}}{=} (g(x), \bigoplus_{i=1}^{n} x_i)$. It is not hard to show that $f$ is one-way. However, it is clear that $f(x)$ does not hide the value of $\mathsf{hc}(x) = \bigoplus_{i=1}^{n} x_i$ because this is part of its output; therefore, $\mathsf{hc}(x)$ is not a hard-core predicate of $f$. Extending this, one can show that for any fixed predicate $\mathsf{hc}$, there is a one-way function $f$ for which $\mathsf{hc}$ is not a hard-core predicate of $f$.

**简单的想法行不通。**

考虑谓词 $\mathsf{hc}(x) \overset{\mathrm{def}}{=} \bigoplus_{i=1}^{n} x_i$，其中 $x_1, \ldots, x_n$ 表示 $x$ 的各个比特。人们或许希望它是任何单向函数 $f$ 的难核谓词：如果 $f$ 无法被求逆，那么 $f(x)$ 必定至少隐藏其原像 $x$ 的一个比特 $x_i$，而这似乎意味着 $x$ 全部比特的异或难以计算。尽管颇具诱惑力，这一论证是不正确的。为看清这一点，设 $g$ 是单向函数，并定义 $f(x) \overset{\mathrm{def}}{=} (g(x), \bigoplus_{i=1}^{n} x_i)$。不难证明 $f$ 是单向的。然而，显然 $f(x)$ 并不隐藏 $\mathsf{hc}(x) = \bigoplus_{i=1}^{n} x_i$ 的值，因为它就是输出的一部分；因此 $\mathsf{hc}(x)$ 不是 $f$ 的难核谓词。将此推广可以证明：对任何固定的谓词 $\mathsf{hc}$，都存在单向函数 $f$ 使得 $\mathsf{hc}$ 不是 $f$ 的难核谓词。

Trivial hard-core predicates. Some functions have “trivial” hard-core predicates. For example, let $f$ be the function that drops the last bit of its input (i.e., $f(x_1\cdots x_n) = x_1\cdots x_{n-1}$). It is hard to determine $x_n$ given $f(x)$ since $x_n$ is independent of the output; thus, $\mathsf{hc}(x) = x_n$ is a hard-core predicate of $f$. However, $f$ is not one-way. When we use hard-core predicates in our constructions, it will become clear why trivial hard-core predicates of this sort are of no use.

**平凡的难核谓词。**

有些函数拥有“平凡的”难核谓词。例如，设 $f$ 是丢弃输入最后一个比特的函数（即 $f(x_1\cdots x_n) = x_1\cdots x_{n-1}$）。给定 $f(x)$ 时难以确定 $x_n$，因为 $x_n$ 与输出无关；因此 $\mathsf{hc}(x) = x_n$ 是 $f$ 的难核谓词。然而 $f$ 不是单向的。当我们在构造中使用难核谓词时，这类平凡的难核谓词为何毫无用处自会一目了然。

## 8.2 From One-Way Functions to Pseudorandomness　从单向函数到伪随机性

In this chapter we show how to construct pseudorandom generators, functions, and permutations from any one-way function/permutation. In this section, we give an overview of these constructions. Details are given in the sections that follow.

在本章中，我们将展示如何从任意单向函数/置换构造伪随机生成器、伪随机函数和伪随机置换。本节给出这些构造的概述，细节将在后续小节中给出。

A hard-core predicate from any one-way function. The first step is to show that a hard-core predicate exists for any one-way function. Actually, it remains open whether this is true; we show something weaker that suffices for our purposes: Namely, we show that given a one-way function f we can construct another one-way function g along with a hard-core predicate of g.

**从任意单向函数得到难核谓词。**

第一步是证明任意单向函数都存在难核谓词。实际上，这是否成立仍是一个公开问题；我们证明一个更弱但足以满足需要的结论：即给定单向函数 $f$，我们可以构造另一个单向函数 $g$ 以及 $g$ 的一个难核谓词。

THEOREM 8.5 (Goldreich–Levin theorem) Assume one-way functions (resp., permutations) exist. Then there exists a one-way function (resp., permutation) g and a hard-core predicate hc of g.

定理 8.5　（Goldreich–Levin 定理）假设单向函数（相应地，单向置换）存在。那么存在单向函数（相应地，单向置换）$g$ 以及 $g$ 的难核谓词 $\mathsf{hc}$。

Let $f$ be a one-way function. Functions $g$ and $\mathsf{gl}$ are constructed as follows:

设 $f$ 是单向函数。函数 $g$ 与 $\mathsf{gl}$ 构造如下：

Set $g(x,r)\stackrel{\mathrm{def}}{=}(f(x),r)$, for $|x|=|r|$, and define

令 $g(x,r)\stackrel{\mathrm{def}}{=}(f(x),r)$，其中 $|x|=|r|$，并定义

$$
\mathsf{gl}(x,r)\stackrel{\mathrm{def}}{=}\bigoplus_{i=1}^{n}x_{i}\cdot r_{i},
$$

where $x_i$ (resp., $r_i$) denotes the $i$th bit of $x$ (resp., $r$). Notice that if $r$ is uniform, then $\mathsf{gl}(x, r)$ outputs the XOR of a random subset of the bits of $x$. (When $r_i = 1$ the bit $x_i$ is included in the XOR, and otherwise it is not.) The Goldreich–Levin theorem thus states that if $f$ is a one-way function then $f(x)$ hides the XOR of a random subset of the bits of $x$.

其中 $x_i$（相应地，$r_i$）表示 $x$（相应地，$r$）的第 $i$ 个比特。注意，若 $r$ 是均匀的，则 $\mathsf{gl}(x, r)$ 输出的是 $x$ 的比特的一个随机子集的异或。（当 $r_i = 1$ 时，比特 $x_i$ 被纳入异或；否则不纳入。）因此，Goldreich–Levin 定理断言：如果 $f$ 是单向函数，那么 $f(x)$ 隐藏了“$x$ 诸比特中随机一个子集的异或值”这一信息。

Pseudorandom generators from one-way permutations. The next step is to show how a hard-core predicate of a one-way permutation can be used to construct a pseudorandom generator. (It is known that a hard-core predicate of a one-way function suffices, but the proof is extremely complicated and well beyond the scope of this book.) Specifically, we show:

**从单向置换得到伪随机生成器。**

下一步是展示如何利用单向置换的难核谓词构造伪随机生成器。（已知单向函数的难核谓词就足够了，但其证明极其复杂，远超本书范围。）具体地，我们证明：

THEOREM 8.6 Let $f$ be a one-way permutation and let $\mathsf{hc}$ be a hard-core predicate of $f$. Then, $G$ defined by $G(s) \stackrel{\mathrm{def}}{=} f(s) \| \mathsf{hc}(s)$ is a pseudorandom generator with expansion factor $\ell(n) = n + 1$.

定理 8.6　设 $f$ 是单向置换，$\mathsf{hc}$ 是 $f$ 的难核谓词。那么，由 $G(s) \stackrel{\mathrm{def}}{=} f(s) \| \mathsf{hc}(s)$ 定义的 $G$ 是扩展因子为 $\ell(n) = n + 1$ 的伪随机生成器。

As intuition for why $G$ is a pseudorandom generator, note first that the initial $n$ bits of $G(s)$ (i.e., the bits of $f(s)$) are uniformly distributed when $s$ is uniformly distributed, since $f$ is a permutation. Next, the fact that $\mathsf{hc}$ is a hard-core predicate of $f$ means that $\mathsf{hc}(s)$ “looks random”—i.e., is *pseudo*-random—even given $f(s)$ (assuming again that $s$ is uniform). Putting these observations together, we see that the entire output of $G$ is *pseudo*-random.

至于 $G$ 为什么是伪随机生成器，直观上首先注意：当 $s$ 均匀分布时，$G(s)$ 的前 $n$ 个比特（即 $f(s)$ 的各比特）也均匀分布，因为 $f$ 是置换。其次，$\mathsf{hc}$ 是 $f$ 的难核谓词意味着：即使给定 $f(s)$（同样假设 $s$ 均匀），$\mathsf{hc}(s)$ 也“看起来随机”——即它是*伪*随机的。把这两个观察合在一起，我们看到 $G$ 的整个输出都是*伪*随机的。

Pseudorandom generators with arbitrary expansion. The existence of a pseudorandom generator that stretches its seed by even a single bit (as we have just seen) is already highly non-trivial. But for applications (e.g., for efficient encryption of large messages as in Section 3.3), we need a pseudorandom generator with much larger expansion. Fortunately, we can obtain any polynomial expansion factor we like:

**具有任意扩展的伪随机生成器。**

伪随机生成器哪怕只把种子扩展一个比特（正如我们刚刚看到的），其存在性本身就已经高度非平凡。但在应用中（例如 3.3 节中对大消息的高效加密），我们需要的是扩展大得多的生成器。幸运的是，我们可以获得任意想要的多项式扩展因子：

THEOREM 8.7 If there exists a pseudorandom generator with expansion factor $\ell(n) = n+1$, then for any polynomial poly there exists a pseudorandom generator with expansion factor $\mathsf{poly}(n)$.

定理 8.7　若存在扩展因子为 $\ell(n) = n+1$ 的伪随机生成器，则对任意多项式 $\mathsf{poly}$，存在扩展因子为 $\mathsf{poly}(n)$ 的伪随机生成器。

We conclude that pseudorandom generators with arbitrary (polynomial) expansion can be constructed from any one-way permutation.

由此我们得出结论：从任意单向置换可以构造具有任意（多项式）扩展的伪随机生成器。

Pseudorandom permutations from pseudorandom generators. Pseudorandom generators suffice for constructing EAV-secure private-key encryption schemes. For CPA-secure private-key encryption (not to mention message authentication codes), however, we relied on pseudorandom functions. The following result shows that the latter can be constructed from the former:

**从伪随机生成器得到伪随机置换。**

伪随机生成器足以构造 EAV 安全的私钥加密方案。然而，对于 CPA 安全的私钥加密（更不用说消息认证码），我们依赖的是伪随机函数。下面的结果表明，后者可以由前者构造出来：

THEOREM 8.8 If there exists a pseudorandom generator with expansion factor $\ell(n) = 2n$, then there exists a pseudorandom function.

定理 8.8　若存在扩展因子为 $\ell(n) = 2n$ 的伪随机生成器，则存在伪随机函数。

In fact, we can do even more:

事实上，我们还能做得更多：

THEOREM 8.9 If there exists a pseudorandom function, then there exists a strong pseudorandom permutation.

定理 8.9　若存在伪随机函数，则存在强伪随机置换。

Combining the above theorems and the results of Chapters 3–5 we have:

把上述定理与第 3–5 章的结果结合起来，我们得到：

COROLLARY 8.10 Assuming the existence of one-way permutations:

推论 8.10　假设单向置换存在：

- There exist pseudorandom generators with any expansion factor, pseudorandom functions, and strong pseudorandom permutations.

  存在具有任意扩展因子的伪随机生成器、伪随机函数和强伪随机置换。

- There exist authenticated encryption schemes and secure message authentication codes.

  存在认证加密方案和安全的消息认证码。

As noted earlier, even one-way functions suffice.

如前所述，即使是单向函数也足够了。

## 8.3 Hard-Core Predicates from One-Way Functions　从单向函数构造难核谓词

In this section, we prove Theorem 8.5 by showing the following:

在本节中，我们通过证明如下结论来证明定理 8.5：

THEOREM 8.11 Let $f$ be a one-way function and define $g(x, r) \stackrel{\mathrm{def}}{=} (f(x), r)$, where $|x| = |r|$, and $\mathsf{gl}(x, r) \stackrel{\mathrm{def}}{=} \bigoplus_{i=1}^{n} x_i \cdot r_i$. Then $\mathsf{gl}$ is a hard-core predicate of $g$.

定理 8.11　设 $f$ 是单向函数，定义 $g(x, r) \stackrel{\mathrm{def}}{=} (f(x), r)$，其中 $|x| = |r|$，并定义 $\mathsf{gl}(x, r) \stackrel{\mathrm{def}}{=} \bigoplus_{i=1}^{n} x_i \cdot r_i$。那么 $\mathsf{gl}$ 是 $g$ 的难核谓词。

Due to the complexity of the proof, we prove three successively stronger results culminating in what is claimed in the theorem.

由于证明较为复杂，我们依次证明三个逐步加强的结果，最终得到该定理所断言的结论。

### 8.3.1 A Simple Case　一个简单情形

We first show that if there exists a polynomial-time adversary $\mathcal{A}$ that always correctly computes $\mathsf{gl}(x, r)$ given $g(x, r) = (f(x), r)$, then it is possible to invert $f$ in polynomial time. (Note that such an $\mathcal{A}$ can only possibly exist if $f$ is one-to-one.) Given the assumption that $f$ is a one-way function, it follows that no such adversary $\mathcal{A}$ exists.

我们首先证明：如果存在多项式时间敌手 $\mathcal{A}$，在给定 $g(x, r) = (f(x), r)$ 时总能正确计算 $\mathsf{gl}(x, r)$，那么就可以在多项式时间内对 $f$ 求逆。（注意，只有当 $f$ 一一对应时，这样的 $\mathcal{A}$ 才有可能存在。）结合 $f$ 是单向函数的假设即可得出：这样的敌手 $\mathcal{A}$ 并不存在。

PROPOSITION 8.12 Let $f$ and $\mathsf{gl}$ be as in Theorem 8.11. If there exists a polynomial-time algorithm $\mathcal{A}$ such that $\mathcal{A}(f(x), r) = \mathsf{gl}(x, r)$ for all $n$ and all $x, r \in \{0,1\}^n$, then there exists a polynomial-time algorithm $\mathcal{A}^{\prime}$ such that $\mathcal{A}^{\prime}(1^n, f(x)) = x$ for all $n$ and all $x \in \{0,1\}^n$.

命题 8.12　设 $f$ 与 $\mathsf{gl}$ 如定理 8.11 所述。若存在多项式时间算法 $\mathcal{A}$，使得对所有 $n$ 及所有 $x, r \in \{0,1\}^n$ 都有 $\mathcal{A}(f(x), r) = \mathsf{gl}(x, r)$，则存在多项式时间算法 $\mathcal{A}^{\prime}$，使得对所有 $n$ 及所有 $x \in \{0,1\}^n$ 都有 $\mathcal{A}^{\prime}(1^n, f(x)) = x$。

PROOF We construct $\mathcal{A}^{\prime}$ as follows. $\mathcal{A}^{\prime}(1^n, y)$ computes $x_i := \mathcal{A}(y, e^i)$ for $i = 1, \ldots, n$, where $e^i$ denotes the $n$-bit string with 1 in the $i$th position and 0 everywhere else. Then $\mathcal{A}^{\prime}$ outputs $x = x_1 \cdots x_n$. Clearly $\mathcal{A}^{\prime}$ runs in polynomial time.

证明　我们如下构造 $\mathcal{A}^{\prime}$。$\mathcal{A}^{\prime}(1^n, y)$ 对 $i = 1, \ldots, n$ 计算 $x_i := \mathcal{A}(y, e^i)$，其中 $e^i$ 表示第 $i$ 位为 1、其余各位均为 0 的 $n$ 比特串。然后 $\mathcal{A}^{\prime}$ 输出 $x = x_1 \cdots x_n$。显然 $\mathcal{A}^{\prime}$ 的运行时间是多项式的。

In the execution of $\mathcal{A}^{\prime}(1^n, f(\hat{x}))$, the value $x_i$ computed by $\mathcal{A}^{\prime}$ satisfies

在 $\mathcal{A}^{\prime}(1^n, f(\hat{x}))$ 的执行中，$\mathcal{A}^{\prime}$ 计算出的 $x_i$ 满足

$$
x_{i}=\mathcal{A}(f(\hat{x}),e^{i})=\mathsf{gl}(\hat{x},e^{i})=\bigoplus_{j=1}^{n}\hat{x}_{j}\cdot e_{j}^{i}=\hat{x}_{i}.
$$

Thus, $x_i = \hat{x}_i$ for all $i$ and so $\mathcal{A}^{\prime}$ outputs the correct inverse $x = \hat{x}$.

因此，对所有 $i$ 都有 $x_i = \hat{x}_i$，于是 $\mathcal{A}^{\prime}$ 输出正确的原像 $x = \hat{x}$。

If $f$ is one-way, it is impossible for any probabilistic polynomial-time algorithm to invert $f$ with non-negligible probability. Thus, we conclude that there is no polynomial-time algorithm that always correctly computes $\mathsf{gl}(x, r)$ from $(f(x), r)$. This is a rather weak result that is very far from our ultimate goal of showing that $\mathsf{gl}(x, r)$ cannot be computed with probability significantly better than ${1}/{2}$ given $(f(x), r)$.

若 $f$ 是单向的，则任何概率多项式时间算法都不可能以非可忽略的概率对 $f$ 求逆。因此我们得出结论：不存在总能从 $(f(x), r)$ 正确计算 $\mathsf{gl}(x, r)$ 的多项式时间算法。这是一个相当弱的结果，离我们的最终目标——证明给定 $(f(x), r)$ 时 $\mathsf{gl}(x, r)$ 无法以显著优于 ${1}/{2}$ 的概率计算——还很远。

### 8.3.2 A More Involved Case　一个更复杂的情形

We now show that it is hard for any probabilistic polynomial-time algorithm $\mathcal{A}$ to compute $\mathsf{gl}(x, r)$ from $(f(x), r)$ with probability significantly better than 3/4. We will again show that any such $\mathcal{A}$ would imply the existence of a polynomial-time algorithm $\mathcal{A}^{\prime}$ that inverts $f$ with non-negligible probability. Notice that the strategy in the proof of Proposition 8.12 fails here because it may be that $\mathcal{A}$ never succeeds when $r = e^i$ (although it may succeed, say, on all other values of $r$). Furthermore, in the present case $\mathcal{A}^{\prime}$ does not know if the result $\mathcal{A}(f(x), r)$ is equal to $\mathsf{gl}(x, r)$ or not; the only thing $\mathcal{A}^{\prime}$ knows is that with high probability, algorithm $\mathcal{A}$ is correct. This further complicates the proof.

现在我们证明：任何概率多项式时间算法 $\mathcal{A}$ 都难以从 $(f(x), r)$ 出发以显著优于 3/4 的概率计算 $\mathsf{gl}(x, r)$。我们将再次证明：任何这样的 $\mathcal{A}$ 都会蕴含一个以非可忽略概率对 $f$ 求逆的多项式时间算法 $\mathcal{A}^{\prime}$ 的存在。注意，命题 8.12 证明中的策略在这里行不通，因为 $\mathcal{A}$ 可能在 $r = e^i$ 时从不成功（尽管它可能在其他所有 $r$ 取值上都成功）。此外，在此情形下，$\mathcal{A}^{\prime}$ 无从知道结果 $\mathcal{A}(f(x), r)$ 是否等于 $\mathsf{gl}(x, r)$；$\mathcal{A}^{\prime}$ 唯一知道的是算法 $\mathcal{A}$ 以高概率正确。这使证明进一步复杂化。

PROPOSITION 8.13 Let f and g be as in Theorem 8.11. If there exists a probabilistic polynomial-time algorithm A and a polynomial $p(\cdot)$ such that

命题 8.13　设 $f$ 与 $g$ 如定理 8.11 所述。若存在概率多项式时间算法 $\mathcal{A}$ 和多项式 $p(\cdot)$ 使得

$$
\Pr_{x,r\gets\{0,1\}^{n}}\left[\mathcal{A}(f(x),r)=\mathsf{gl}(x,r)\right]\geq\frac{3}{4}+\frac{1}{p(n)} \tag{8.1}
$$

for infinitely many values of n, then there exists a probabilistic polynomial-time algorithm $A^{\prime}$ such that

对无穷多个 $n$ 的取值成立，那么存在概率多项式时间算法 $A^{\prime}$ 使得

$$
\Pr_{x\leftarrow\{0,1\}^n}\left[\mathcal{A}^{\prime}(1^n,f(x))\in f^{-1}(f(x))\right]\geq\frac{1}{4\cdot p(n)}
$$

for infinitely many values of n.

对无穷多个 $n$ 的取值成立。

PROOF The main observation underlying the proof of this proposition is that for every $r \in \{0,1\}^n$, the values $\mathsf{gl}(x, r \oplus e^i)$ and $\mathsf{gl}(x, r)$ together can be used to compute the $i$th bit of $x$. (Recall that $e^i$ denotes the $n$-bit string with ${0}s$ everywhere except the $i$th position.) This is true because

证明　本命题证明背后的主要观察是：对每个 $r \in \{0,1\}^n$，把值 $\mathsf{gl}(x, r \oplus e^i)$ 与 $\mathsf{gl}(x, r)$ 合在一起即可算出 $x$ 的第 $i$ 个比特。（回顾一下，$e^i$ 表示除第 $i$ 位外处处为 0 的 $n$ 比特串。）这是因为

$$
\begin{aligned}
\mathsf{gl}(x,r)&\oplus\mathsf{gl}(x,r\oplus e^{i})\\
&=\left(\bigoplus_{j=1}^{n}x_{j}\cdot r_{j}\right)\oplus\left(\bigoplus_{j=1}^{n}x_{j}\cdot(r_{j}\oplus e^{i}_{j})\right)=x_{i}\cdot r_{i}\oplus(x_{i}\cdot\bar{r}_{i})=x_{i},
\end{aligned}
$$

where $\bar{r}_i$ is the complement of $r_i$, and the second equality is due to the fact that for $j \neq i$, the value $x_j \cdot r_j$ appears in both sums and so is canceled out.

其中 $\bar{r}_i$ 是 $r_i$ 的补，第二个等号源于这样的事实：当 $j \neq i$ 时，值 $x_j \cdot r_j$ 同时出现在两个和式中，因而相互抵消。

The above demonstrates that if $\mathcal{A}$ answers correctly on both $(f(x), r)$ and $(f(x), r \oplus e^i)$, then $\mathcal{A}^{\prime}$ can correctly compute $x_i$. Unfortunately, $\mathcal{A}^{\prime}$ does not know when $\mathcal{A}$ answers correctly and when it does not; $\mathcal{A}^{\prime}$ knows only that $\mathcal{A}$ answers correctly with “high” probability. For this reason, $\mathcal{A}^{\prime}$ will use multiple random values of $r$, using each one to obtain an estimate of $x_i$, and then take the estimate occurring a majority of the time as its final guess for $x_i$.

上面的式子表明：如果 $\mathcal{A}$ 对 $(f(x), r)$ 和 $(f(x), r \oplus e^i)$ 都回答正确，那么 $\mathcal{A}^{\prime}$ 就能正确算出 $x_i$。遗憾的是，$\mathcal{A}^{\prime}$ 无从知道 $\mathcal{A}$ 何时回答正确、何时不正确；$\mathcal{A}^{\prime}$ 只知道 $\mathcal{A}$ 以“高”概率回答正确。因此，$\mathcal{A}^{\prime}$ 将使用多个随机的 $r$ 取值，用每一个得到 $x_i$ 的一个估计，然后把出现次数占多数的估计作为 $x_i$ 的最终猜测。

As a preliminary step, we show that for many $x$'s the probability that $\mathcal{A}$ answers correctly for both $(f(x), r)$ and $(f(x), r \oplus e^i)$, when $r$ is uniform, is sufficiently high. This allows us to fix $x$ and then focus solely on uniform choice of $r$, which makes the analysis easier.

作为预备步骤，我们证明：对许多 $x$ 而言，当 $r$ 均匀选取时，$\mathcal{A}$ 对 $(f(x), r)$ 和 $(f(x), r \oplus e^i)$ 都回答正确的概率足够高。这使我们能够先固定 $x$，再只专注于 $r$ 的均匀选择，从而简化分析。

CLAIM 8.14 Let n be such that

断言 8.14　设 $n$ 满足

$$
\Pr_{x,r\gets\{0,1\}^{n}}\left[\mathcal{A}(f(x),r)=\mathsf{gl}(x,r)\right]\geq\frac{3}{4}+\frac{1}{p(n)}.
$$

Then there exists a set $S_n \subseteq \{0,1\}^n$ of size at least $\frac{1}{2p(n)} \cdot 2^n$ such that for every $x \in S_n$ it holds that

那么存在大小至少为 $\frac{1}{2p(n)} \cdot 2^n$ 的集合 $S_n \subseteq \{0,1\}^n$，使得对每个 $x \in S_n$ 都有

$$
\Pr_{r\leftarrow\{0,1\}^{n}}[\mathcal{A}(f(x),r)=\mathsf{gl}(x,r)]\geq\frac{3}{4}+\frac{1}{2p(n)}.
$$

PROOF Let $\varepsilon(n) = 1/p(n)$, and define $S_n \subseteq \{0,1\}^n$ to be the set of all $x^{\prime}$s for which

证明　令 $\varepsilon(n) = 1/p(n)$，并把 $S_n \subseteq \{0,1\}^n$ 定义为所有满足下式的 $x$ 构成的集合：

$$
\Pr_{r\leftarrow\{0,1\}^{n}}[\mathcal{A}(f(x),r)=\mathsf{gl}(x,r)]\geq\frac{3}{4}+\frac{\varepsilon(n)}{2}.
$$

We have:

我们有：

$$
\begin{aligned}
\Pr_{x,r\leftarrow\{0,1\}^{n}}\big[\mathcal{A}(f(x),r)=\mathsf{gl}(x,r)\big]&=\frac{1}{2^{n}}\sum_{x\in\{0,1\}^{n}}\Pr_{r\leftarrow\{0,1\}^{n}}\Big[\mathcal{A}(f(x),r)=\mathsf{gl}(x,r)\Big]\\
&=\frac{1}{2^{n}}\sum_{x\in S_{n}}\Pr_{r\leftarrow\{0,1\}^{n}}\Big[\mathcal{A}(f(x),r)=\mathsf{gl}(x,r)\Big]\\
&\quad+\frac{1}{2^{n}}\sum_{x\not\in S_{n}}\Pr_{r\leftarrow\{0,1\}^{n}}\Big[\mathcal{A}(f(x),r)=\mathsf{gl}(x,r)\Big]\\
&\leq\frac{|S_{n}|}{2^{n}}+\frac{1}{2^{n}}\cdot\sum_{x\not\in S_{n}}\left(\frac{3}{4}+\frac{\varepsilon(n)}{2}\right)\\
&\leq\frac{|S_{n}|}{2^{n}}+\left(\frac{3}{4}+\frac{\varepsilon(n)}{2}\right).
\end{aligned}
$$

Since $\frac{3}{4} + \varepsilon(n) \leq \Pr_{x,r \leftarrow \{0,1\}^n}\left[\mathcal{A}(f(x), r) = \mathsf{gl}(x, r)\right]$, straightforward algebra gives $|S_n| \geq \frac{\varepsilon(n)}{2} \cdot 2^n$.

由于 $\frac{3}{4} + \varepsilon(n) \leq \Pr_{x,r \leftarrow \{0,1\}^n}\left[\mathcal{A}(f(x), r) = \mathsf{gl}(x, r)\right]$，简单的代数运算给出 $|S_n| \geq \frac{\varepsilon(n)}{2} \cdot 2^n$。

The following is an easy consequence.

下面的结论是其简单推论。

**CLAIM 8.15** Let n be such that

**断言 8.15**　设 $n$ 满足

$$
\Pr_{x,r\gets\{0,1\}^{n}}\left[\mathcal{A}(f(x),r)=\mathsf{gl}(x,r)\right]\geq\frac{3}{4}+\frac{1}{p(n)}.
$$

Then there exists a set $S_n \subseteq \{0,1\}^n$ of size at least $\frac{1}{2p(n)} \cdot 2^n$ such that for every $x \in S_n$ and every $i$ it holds that

那么存在大小至少为 $\frac{1}{2p(n)} \cdot 2^n$ 的集合 $S_n \subseteq \{0,1\}^n$，使得对每个 $x \in S_n$ 和每个 $i$ 都有

$$
\Pr_{r\leftarrow\{0,1\}^{n}}\left[\mathcal{A}(f(x),r)=\mathsf{gl}(x,r)\wedge\mathcal{A}(f(x),r\oplus e^{i})=\mathsf{gl}(x,r\oplus e^{i})\right]\geq\frac{1}{2}+\frac{1}{p(n)}.
$$

PROOF Let $\varepsilon(n) = 1/p(n)$, and take $S_n$ to be the set guaranteed by the previous claim. Fix any $x \in S_n$. We have:

证明　令 $\varepsilon(n) = 1/p(n)$，并取 $S_n$ 为前一条断言所保证的集合。固定任意 $x \in S_n$。我们有：

$$
\Pr_{r\leftarrow\{0,1\}^{n}}[\mathcal{A}(f(x),r)\neq\mathsf{gl}(x,r)]\leq\frac{1}{4}-\frac{\varepsilon(n)}{2}.
$$

Fix any $i \in \{1, \ldots, n\}$. If $r$ is uniform then so is $r \oplus e^i$; thus

固定任意 $i \in \{1, \ldots, n\}$。若 $r$ 是均匀的，则 $r \oplus e^i$ 也是均匀的；因此

$$
\Pr_{r\leftarrow\{0,1\}^{n}}[\mathcal{A}(f(x),r\oplus e^{i})\neq\mathsf{gl}(x,r\oplus e^{i})]\leq\frac{1}{4}-\frac{\varepsilon(n)}{2}.
$$

We are interested in lower-bounding the probability that $\mathcal{A}$ outputs the correct answer for both $\mathsf{gl}(x, r)$ and $\mathsf{gl}(x, r \oplus e^i)$; equivalently, we want to upper-bound the probability that $\mathcal{A}$ fails to output the correct answer in either of these cases. Note that $r$ and $r \oplus e^i$ are not independent, so we cannot just multiply the probabilities of failure. However, we can apply the union bound (see Proposition A.7) and sum the probabilities of failure. That is, the probability that $\mathcal{A}$ is incorrect on either $\mathsf{gl}(x, r)$ or $\mathsf{gl}(x, r \oplus e^i)$ is at most

我们关心的是给出 $\mathcal{A}$ 对 $\mathsf{gl}(x, r)$ 和 $\mathsf{gl}(x, r \oplus e^i)$ 都输出正确答案的概率的下界；等价地，即给出 $\mathcal{A}$ 在这两种情形的任一情形下未能输出正确答案的概率的上界。注意，$r$ 与 $r \oplus e^i$ 并不独立，所以不能直接将失败概率相乘。不过，我们可以应用联合界（见命题 A.7），把失败概率相加。也就是说，$\mathcal{A}$ 在 $\mathsf{gl}(x, r)$ 或 $\mathsf{gl}(x, r \oplus e^i)$ 上出错的概率至多为

$$
\left(\frac{1}{4}-\frac{\varepsilon(n)}{2}\right)+\left(\frac{1}{4}-\frac{\varepsilon(n)}{2}\right)=\frac{1}{2}-\varepsilon(n),
$$

and so $\mathcal{A}$ is correct on both $\mathsf{gl}(x,r)$ and $\mathsf{gl}(x,r\oplus e^{i})$ with probability at least ${1}/2+\varepsilon(n)$. This proves the claim.

因此，$\mathcal{A}$ 对 $\mathsf{gl}(x,r)$ 和 $\mathsf{gl}(x,r\oplus e^{i})$ 都正确的概率至少为 ${1}/2+\varepsilon(n)$。这就证明了该断言。

For the rest of the proof we set $\varepsilon(n) = 1/p(n)$ and consider only those values of n for which

在证明的其余部分，我们令 $\varepsilon(n) = 1/p(n)$，并且只考虑使下式成立的那些 $n$ 取值：

$$
\Pr_{x,r\gets\{0,1\}^{n}}\left[\mathcal{A}(f(x),r)=\mathsf{gl}(x,r)\right]\geq\frac{3}{4}+\varepsilon(n).
$$

The previous claim states that for an $\varepsilon(n)/2$ fraction of inputs $x$, and any $i$, algorithm $\mathcal{A}$ answers correctly on both $(f(x), r)$ and $(f(x), r \oplus e^i)$ with probability at least ${1}/2 + \varepsilon(n)$ over uniform choice of $r$, and from now on we focus only on such values of $x$. We construct a probabilistic polynomial-time algorithm $\mathcal{A}^{\prime}$ that inverts $f(x)$ with probability at least ${1}/{2}$ when $x \in S_n$. This suffices to prove Proposition 8.13 since then, for infinitely many values of $n$,

前一条断言表明：对占比例 $\varepsilon(n)/2$ 的输入 $x$ 以及任意 $i$，在 $r$ 均匀选取时算法 $\mathcal{A}$ 对 $(f(x), r)$ 和 $(f(x), r \oplus e^i)$ 都回答正确的概率至少为 ${1}/2 + \varepsilon(n)$；从现在起我们只关注这样的 $x$ 取值。我们构造一个概率多项式时间算法 $\mathcal{A}^{\prime}$，当 $x \in S_n$ 时它以至少 ${1}/{2}$ 的概率对 $f(x)$ 求逆。这足以证明命题 8.13，因为这样一来，对无穷多个 $n$ 的取值就有

$$
\begin{aligned}
\Pr_{x\leftarrow\{0,1\}^{n}}&[\mathcal{A}^{\prime}(1^{n},f(x))\in f^{-1}(f(x))]\\
&\geq\Pr_{x\leftarrow\{0,1\}^{n}}[\mathcal{A}^{\prime}(1^{n},f(x))\in f^{-1}(f(x))\mid x\in S_{n}]\cdot\Pr_{x\leftarrow\{0,1\}^{n}}[x\in S_{n}]\\
&\geq\frac{1}{2}\cdot\frac{\varepsilon(n)}{2}=\frac{1}{4p(n)}.
\end{aligned}
$$

Algorithm $\mathcal{A}^{\prime}$, given as input ${1}^{n}$ and y, works as follows:

算法 $\mathcal{A}^{\prime}$ 以 ${1}^{n}$ 和 $y$ 为输入，工作方式如下：

1. For i = 1, ..., n do:

   对 $i = 1, \ldots, n$ 依次执行：

   - Repeatedly choose a uniform $r \in \{0,1\}^n$ and compute $\mathcal{A}(y,r) \oplus \mathcal{A}(y,r \oplus e^i)$ as an “estimate” for the $i$th bit of the preimage of $y$. After doing this sufficiently many times (see below), let $x_i$ be the “estimate” that occurs a majority of the time.

     反复均匀选取 $r \in \{0,1\}^n$，并计算 $\mathcal{A}(y,r) \oplus \mathcal{A}(y,r \oplus e^i)$，作为 $y$ 的原像第 $i$ 个比特的一个“估计”。重复足够多次（见下文）后，令 $x_i$ 为出现次数占多数的那个“估计”。

2. Output $x = x_1 \cdots x_n$.

   输出 $x = x_1 \cdots x_n$。

We sketch an analysis of the probability that $\mathcal{A}^{\prime}$ correctly inverts its given input $y$. (We allow ourselves to be a bit laconic, since a full proof for a more difficult case is given in the following section.) Say $y = f(\hat{x})$ and recall that we assume here that $n$ is such that Equation (8.1) holds and $\hat{x} \in S_n$. Fix some $i$. The previous claim implies that the estimate $\mathcal{A}(y, r) \oplus \mathcal{A}(y, r \oplus e^i)$ is equal to $\mathsf{gl}(\hat{x}, e^i)$ with probability at least $\frac{1}{2} + \varepsilon(n)$ over choice of $r$. By obtaining sufficiently many estimates and letting $x_i$ be the majority value, $\mathcal{A}^{\prime}$ can ensure that $x_i$ is equal to $\mathsf{gl}(\hat{x}, e^i)$ with probability at least ${1} - \frac{1}{2n}$. Since $\varepsilon(n) = 1/p(n)$ for some polynomial $p$, and an independent value of $r$ is used for obtaining each estimate, the Chernoff bound (cf. Proposition A.14) shows that polynomially many estimates suffice.

我们概述 $\mathcal{A}^{\prime}$ 正确求逆其所给输入 $y$ 的概率的分析。（这里我们写得简略一些，因为下一节会对更困难的情形给出完整证明。）设 $y = f(\hat{x})$，并回顾我们在这里假设 $n$ 使得式 (8.1) 成立且 $\hat{x} \in S_n$。固定某个 $i$。前一条断言蕴含：在 $r$ 的选取下，估计值 $\mathcal{A}(y, r) \oplus \mathcal{A}(y, r \oplus e^i)$ 等于 $\mathsf{gl}(\hat{x}, e^i)$ 的概率至少为 $\frac{1}{2} + \varepsilon(n)$。只要获得足够多的估计并令 $x_i$ 为其中的多数值，$\mathcal{A}^{\prime}$ 就能确保 $x_i$ 等于 $\mathsf{gl}(\hat{x}, e^i)$ 的概率至少为 ${1} - \frac{1}{2n}$。由于 $\varepsilon(n) = 1/p(n)$（$p$ 为某个多项式），且每获得一个估计都使用独立的 $r$ 取值，Chernoff 界（参见命题 A.14）表明多项式数量的估计就足够了。

Summarizing, we have that for each $i$ the value $x_i$ computed by $\mathcal{A}^{\prime}$ is incorrect with probability at most $\frac{1}{2n}$. A union bound thus shows that $\mathcal{A}^{\prime}$ is incorrect for some $i$ with probability at most $n \cdot \frac{1}{2n} = \frac{1}{2}$. That is, $\mathcal{A}^{\prime}$ is correct for all $i$—and thus correctly inverts $y$—with probability at least ${1} - \frac{1}{2} = \frac{1}{2}$. This completes the proof of Proposition 8.13.

总结起来：对每个 $i$，$\mathcal{A}^{\prime}$ 算出的 $x_i$ 出错的概率至多为 $\frac{1}{2n}$。于是由联合界可知，$\mathcal{A}^{\prime}$ 对某个 $i$ 出错的概率至多为 $n \cdot \frac{1}{2n} = \frac{1}{2}$。也就是说，$\mathcal{A}^{\prime}$ 对所有 $i$ 都正确——从而正确求逆 $y$——的概率至少为 ${1} - \frac{1}{2} = \frac{1}{2}$。至此命题 8.13 证毕。

A corollary of Proposition 8.13 is that if $f$ is a one-way function, then for any polynomial-time algorithm $\mathcal{A}$ the probability that $\mathcal{A}$ correctly guesses $\mathsf{gl}(x,r)$ when given $(f(x),r)$ is at most negligibly more than ${3}/{4}$.

命题 8.13 的一个推论是：如果 $f$ 是单向函数，那么对任何多项式时间算法 $\mathcal{A}$，在给定 $(f(x),r)$ 时 $\mathcal{A}$ 正确猜出 $\mathsf{gl}(x,r)$ 的概率至多比 ${3}/{4}$ 高出可忽略的量。

### 8.3.3 The Full Proof　完整证明

We assume familiarity with the simplified proofs in the previous sections, and build on the ideas developed there. We rely on some terminology and standard results from probability theory discussed in Appendix A.3.

我们假定读者已熟悉前几小节中的简化证明，并在那里发展出的思想之上展开。我们还会用到附录 A.3 中讨论的一些概率论术语和标准结果。

PROPOSITION 8.16 Let f and g be as in Theorem 8.11. If there exists a probabilistic polynomial-time algorithm A and a polynomial $p(\cdot)$ such that

命题 8.16　设 $f$ 与 $g$ 如定理 8.11 所述。若存在概率多项式时间算法 $\mathcal{A}$ 和多项式 $p(\cdot)$ 使得

$$
\Pr_{x,r\leftarrow\{0,1\}^n}\left[\mathcal{A}(f(x),r)=\mathsf{gl}(x,r)\right]\geq\frac{1}{2}+\frac{1}{p(n)}
$$

for infinitely many values of n, then there exists a probabilistic polynomial-time algorithm $\mathcal{A}^{\prime}$ and a polynomial $p^{\prime}(\cdot)$ such that

对无穷多个 $n$ 的取值成立，那么存在概率多项式时间算法 $\mathcal{A}^{\prime}$ 和多项式 $p^{\prime}(\cdot)$ 使得

$$
\Pr_{x\leftarrow\{0,1\}^n}\left[\mathcal{A}^{\prime}(1^n,f(x))\in f^{-1}(f(x))\right]\geq\frac{1}{p^{\prime}(n)}
$$

for infinitely many values of n.

对无穷多个 $n$ 的取值成立。

PROOF Once again we set $\varepsilon(n) = 1/p(n)$ and consider only those values of $n$ for which $\Pr_{x,r \leftarrow \{0,1\}^n}\left[\mathcal{A}(f(x), r) = \mathsf{gl}(x, r)\right] \geq \frac{1}{2} + \frac{1}{p(n)}$. The following is analogous to Claim 8.14 and is proved in the same way.

证明　我们再次令 $\varepsilon(n) = 1/p(n)$，并且只考虑使 $\Pr_{x,r \leftarrow \{0,1\}^n}\left[\mathcal{A}(f(x), r) = \mathsf{gl}(x, r)\right] \geq \frac{1}{2} + \frac{1}{p(n)}$ 成立的那些 $n$ 取值。下面的结论与断言 8.14 类似，可用同样的方式证明。

**CLAIM 8.17** Let n be such that

**断言 8.17**　设 $n$ 满足

$$
\Pr_{x,r\leftarrow\{0,1\}^{n}}\left[\mathcal{A}(f(x),r)=\mathsf{gl}(x,r)\right]\geq\frac{1}{2}+\varepsilon(n).
$$

Then there exists a set $S_n \subseteq \{0,1\}^n$ of size at least $\frac{\varepsilon(n)}{2} \cdot 2^n$ such that for every $x \in S_n$ it holds that

那么存在大小至少为 $\frac{\varepsilon(n)}{2} \cdot 2^n$ 的集合 $S_n \subseteq \{0,1\}^n$，使得对每个 $x \in S_n$ 都有

$$
\Pr_{r\leftarrow\{0,1\}^{n}}[\mathcal{A}(f(x),r)=\mathsf{gl}(x,r)]\geq\frac{1}{2}+\frac{\varepsilon(n)}{2}.
$$

If we start by trying to prove an analogue of Claim 8.15, the best we can claim here is that when $x \in S_n$ we have

如果我们一开始就试图证明断言 8.15 的类似结论，这里所能断言的最好结果是：当 $x \in S_n$ 时有

$$
\Pr_{r\leftarrow\{0,1\}^{n}}\left[\mathcal{A}(f(x),r)=\mathsf{gl}(x,r)\wedge\mathcal{A}(f(x),r\oplus e^{i})=\mathsf{gl}(x,r\oplus e^{i})\right]\geq\varepsilon(n)
$$

for any $i$. Thus, if we try to use $\mathcal{A}(f(x), r) \oplus \mathcal{A}(f(x), r \oplus e^i)$ as an estimate for $x_i$, all we can claim is that this estimate will be correct with probability at least $\varepsilon(n)$, which may not be any better than taking a random guess! We cannot claim that flipping the result gives a good estimate, either.

对任意 $i$ 成立。于是，如果我们试图用 $\mathcal{A}(f(x), r) \oplus \mathcal{A}(f(x), r \oplus e^i)$ 作为 $x_i$ 的估计，所能断言的只是这个估计以至少 $\varepsilon(n)$ 的概率正确，而这可能并不比随机猜测更好！我们也无法断言把结果取反就是一个好估计。

Instead, we design $\mathcal{A}^{\prime}$ so that it computes $\mathsf{gl}(x,r)$ and $\mathsf{gl}(x,r\oplus e^i)$ by invoking $\mathcal{A}$ only once. We do this by having $\mathcal{A}^{\prime}$ run $\mathcal{A}(f(x),r\oplus e^i)$, and then simply “guessing” the value $\mathsf{gl}(x,r)$ itself. The naive way to do this would be to choose the $r$'s independently, as before, and to have $\mathcal{A}^{\prime}$ make an independent guess of $\mathsf{gl}(x,r)$ for each value of $r$. But then the probability that all such guesses are correct—which, as we will see, is necessary if $\mathcal{A}^{\prime}$ is to output the correct inverse—would be negligible because polynomials many $r$'s are used.

相反，我们这样设计 $\mathcal{A}^{\prime}$：只调用 $\mathcal{A}$ 一次就同时算出 $\mathsf{gl}(x,r)$ 和 $\mathsf{gl}(x,r\oplus e^i)$。做法是让 $\mathcal{A}^{\prime}$ 运行 $\mathcal{A}(f(x),r\oplus e^i)$，然后直接“猜测” $\mathsf{gl}(x,r)$ 本身的值。朴素的做法是像之前那样独立地选取各个 $r$，并让 $\mathcal{A}^{\prime}$ 对每个 $r$ 取值独立地猜测 $\mathsf{gl}(x,r)$。但这样一来，所有猜测全部正确的概率——正如我们将看到的，若 $\mathcal{A}^{\prime}$ 要输出正确的原像，这是必需的——将会是可忽略的，因为要用到多项式个 $r$ 取值。

The crucial observation of the present proof is that $\mathcal{A}^{\prime}$ can generate the $r^{\prime}$s in a pairwise-independent manner and make its guesses in a particular way so that with non-negligible probability all its guesses are correct. Specifically, in order to generate $m$ values of $r$, we have $\mathcal{A}^{\prime}$ select $\ell = \lceil \log(m+1) \rceil$ independent and uniformly distributed strings $s^1, \ldots, s^\ell \in \{0,1\}^n$. Then, for every nonempty subset $I \subseteq \{1, \ldots, \ell\}$, we set $r^I := \oplus_{i \in I} s^i$. Since there are ${2}^\ell - 1$ nonempty subsets, this defines a collection of ${2}^{\lceil \log(m+1) \rceil} - 1 \geq m$ strings. Each such string is uniformly distributed. The strings are not independent, but they are pairwise independent. To see this, notice that for every two subsets $I \neq J$ there is an index $j \in I \cup J$ such that $j \notin I \cap J$. Without loss of generality, assume $j \notin I$. Then the value of $s^j$ is uniform and independent of the value of $r^I$. Since $s^j$ is included in the XOR that defines $r^J$, this implies that $r^J$ is uniform and independent of $r^I$ as well.

本证明的关键观察是：$\mathcal{A}^{\prime}$ 可以按两两独立的方式生成各个 $r$，并以特定方式作出猜测，使得所有猜测以非可忽略的概率全部正确。具体地，为了生成 $m$ 个 $r$ 取值，让 $\mathcal{A}^{\prime}$ 选取 $\ell = \lceil \log(m+1) \rceil$ 个独立且均匀分布的串 $s^1, \ldots, s^\ell \in \{0,1\}^n$。然后，对每个非空子集 $I \subseteq \{1, \ldots, \ell\}$，令 $r^I := \oplus_{i \in I} s^i$。由于非空子集共有 ${2}^\ell - 1$ 个，这就定义了由 ${2}^{\lceil \log(m+1) \rceil} - 1 \geq m$ 个串组成的集合。每个这样的串都是均匀分布的。这些串并不独立，但两两独立。为说明这一点，注意对任意两个子集 $I \neq J$，存在下标 $j \in I \cup J$ 使得 $j \notin I \cap J$。不失一般性，设 $j \notin I$。此时 $s^j$ 的值是均匀的，且与 $r^I$ 的值独立。由于 $s^j$ 出现在定义 $r^J$ 的异或之中，这意味着 $r^J$ 也是均匀的，且与 $r^I$ 独立。

We now have the following two important observations:

现在我们有如下两个重要观察：

1. Given $\mathsf{gl}(x, s^1), \ldots, \mathsf{gl}(x, s^\ell)$, it is possible to compute $\mathsf{gl}(x, r^I)$ for every subset $I \subseteq \{1, \ldots, \ell\}$. This is because

   给定 $\mathsf{gl}(x, s^1), \ldots, \mathsf{gl}(x, s^\ell)$，就能对每个子集 $I \subseteq \{1, \ldots, \ell\}$ 计算 $\mathsf{gl}(x, r^I)$。这是因为

   $$
   \mathsf{gl}(x,r^{I})=\mathsf{gl}(x,\oplus_{i\in I}s^{i})=\oplus_{i\in I}\mathsf{gl}(x,s^{i}).
   $$

2. If $\mathcal{A}^{\prime}$ simply guesses the values of $\mathsf{gl}(x, s^{1}), \ldots, \mathsf{gl}(x, s^{\ell})$ by choosing a uniform bit for each, then all these guesses will be correct with probability ${1}/2^{\ell}$. If $m$ is polynomial in the security parameter $n$, then ${1}/2^{\ell}$ is not negligible, and so with non-negligible probability $\mathcal{A}^{\prime}$ correctly guesses all the values $\mathsf{gl}(x, s^{1}), \ldots, \mathsf{gl}(x, s^{\ell})$.

   如果 $\mathcal{A}^{\prime}$ 只是为每个值选取一个均匀比特来猜测 $\mathsf{gl}(x, s^{1}), \ldots, \mathsf{gl}(x, s^{\ell})$ 的值，那么所有这些猜测以概率 ${1}/2^{\ell}$ 全部正确。若 $m$ 是安全参数 $n$ 的多项式，则 ${1}/2^{\ell}$ 不是可忽略的，因此 $\mathcal{A}^{\prime}$ 以非可忽略的概率正确猜出所有值 $\mathsf{gl}(x, s^{1}), \ldots, \mathsf{gl}(x, s^{\ell})$。

Combining the above yields a way of obtaining $m = \mathsf{poly}(n)$ uniform and pairwise-independent strings $\{r^I\}$ along with correct values for $\{\mathsf{gl}(x, r^I)\}$ with non-negligible probability. These values can then be used to compute $x_i$ in the same way as in the proof of Proposition 8.13. Details follow.

把上面两点结合起来，就得到一种以非可忽略概率获得 $m = \mathsf{poly}(n)$ 个均匀且两两独立的串 $\{r^I\}$ 以及 $\{\mathsf{gl}(x, r^I)\}$ 的正确值的方法。随后可以按命题 8.13 证明中的同样方式，用这些值计算 $x_i$。细节如下。

The inversion algorithm $A^{\prime}$. We now provide a full description of an algorithm $A^{\prime}$ that receives inputs ${1}^n$, $y$ and tries to compute an inverse of $y$. The algorithm proceeds as follows:

**求逆算法 $A^{\prime}$。**

现在我们完整描述算法 $A^{\prime}$：它接收输入 ${1}^n$、$y$，并尝试计算 $y$ 的一个原像。该算法流程如下：

1. Compute $\ell:=\lceil\log(2n/\varepsilon(n)^{2}+1)\rceil$.

   计算 $\ell:=\lceil\log(2n/\varepsilon(n)^{2}+1)\rceil$。

2. Choose uniform, independent $s^1, \ldots, s^\ell \in \{0,1\}^n$ and $\sigma^1, \ldots, \sigma^\ell \in \{0,1\}$.

   均匀、独立地选取 $s^1, \ldots, s^\ell \in \{0,1\}^n$ 和 $\sigma^1, \ldots, \sigma^\ell \in \{0,1\}$。

3. For every nonempty subset $I \subseteq \{1, \ldots, \ell\}$, compute $r^I := \oplus_{i \in I} s^i$ and $\sigma^I := \oplus_{i \in I} \sigma^i$.

   对每个非空子集 $I \subseteq \{1, \ldots, \ell\}$，计算 $r^I := \oplus_{i \in I} s^i$ 和 $\sigma^I := \oplus_{i \in I} \sigma^i$。

4. For i = 1, ..., n do:

   对 $i = 1, \ldots, n$ 依次执行：

   (a) For every nonempty subset $I \subseteq \{1, \ldots, \ell\}$, set

   (a) 对每个非空子集 $I \subseteq \{1, \ldots, \ell\}$，令

   $$
   x_{i}^{I}:=\sigma^{I}\oplus\mathcal{A}(y,r^{I}\oplus e^{i}).
   $$

   (b) Set $x_i := \text{majority}_I\{x_i^I\}$ (i.e., take the bit that appeared a majority of the time in the previous step).

   (b) 令 $x_i := \text{majority}_I\{x_i^I\}$（即取上一步中出现次数占多数的比特）。

5. Output $x = x_1 \cdots x_n$.

   输出 $x = x_1 \cdots x_n$。

It remains to compute the probability that $\mathcal{A}^{\prime}$ outputs $x \in f^{-1}(y)$. As in the proof of Proposition 8.13, we focus only on $n$ as in Claim 8.17 and assume $y = f(\hat{x})$ for some $\hat{x} \in S_n$. Each $\sigma^i$ represents a “guess” for the value of $\mathsf{gl}(\hat{x}, s^i)$. As noted earlier, with non-negligible probability all these guesses are correct; we show that conditioned on this event, $\mathcal{A}^{\prime}$ outputs $x = \hat{x}$ with probability at least ${1}/{2}$.

剩下要计算的是 $\mathcal{A}^{\prime}$ 输出 $x \in f^{-1}(y)$ 的概率。与命题 8.13 的证明一样，我们只关注断言 8.17 中的那些 $n$，并假设 $y = f(\hat{x})$，其中 $\hat{x} \in S_n$。每个 $\sigma^i$ 表示对 $\mathsf{gl}(\hat{x}, s^i)$ 值的一个“猜测”。如前所述，所有这些猜测以非可忽略的概率全部正确；我们将证明，在该事件发生的条件下，$\mathcal{A}^{\prime}$ 以至少 ${1}/{2}$ 的概率输出 $x = \hat{x}$。

Assume $\sigma^i = \mathsf{gl}(\hat{x}, s^i)$ for all $i$. Then $\sigma^I = \mathsf{gl}(\hat{x}, r^I)$ for all $I$. Fix an index $i \in \{1, \ldots, n\}$ and consider the probability that $\mathcal{A}^{\prime}$ obtains the correct value $x_i = \hat{x}_i$. For any nonempty $I$ we have $\mathcal{A}(y, r^I \oplus e^i) = \mathsf{gl}(\hat{x}, r^I \oplus e^i)$ with probability at least $\frac{1}{2} + \varepsilon(n)/2$ over choice of $r$; this follows because $\hat{x} \in S_n$
and $r^I \oplus e^i$ is uniformly distributed. Thus, for any nonempty subset $I$ we have $\Pr[x_i^I = \hat{x}_i] \geq \frac{1}{2} + \varepsilon(n)/2$. Moreover, the $\{x_i^I\}_{I \subseteq \{1, \ldots, \ell\}}$ are pairwise independent because the $\{r^I\}_{I \subseteq \{1, \ldots, \ell\}}$ (and hence the $\{r^I \oplus e^i\}_{I \subseteq \{1, \ldots, \ell\}}$) are pairwise independent. Since $x_i$ is defined to be the value that occurs a majority of the time among the $\{x_i^I\}_{I \subseteq \{1, \ldots, \ell\}}$, we can apply Proposition A.13 to obtain

假设对所有 $i$ 都有 $\sigma^i = \mathsf{gl}(\hat{x}, s^i)$。那么对所有 $I$ 都有 $\sigma^I = \mathsf{gl}(\hat{x}, r^I)$。固定下标 $i \in \{1, \ldots, n\}$，考虑 $\mathcal{A}^{\prime}$ 得到正确值 $x_i = \hat{x}_i$ 的概率。对任意非空 $I$，在 $r$ 的选取下 $\mathcal{A}(y, r^I \oplus e^i) = \mathsf{gl}(\hat{x}, r^I \oplus e^i)$ 的概率至少为 $\frac{1}{2} + \varepsilon(n)/2$；这是因为 $\hat{x} \in S_n$ 且 $r^I \oplus e^i$ 均匀分布。于是，对任意非空子集 $I$ 都有 $\Pr[x_i^I = \hat{x}_i] \geq \frac{1}{2} + \varepsilon(n)/2$。此外，$\{x_i^I\}_{I \subseteq \{1, \ldots, \ell\}}$ 两两独立，因为 $\{r^I\}_{I \subseteq \{1, \ldots, \ell\}}$（从而 $\{r^I \oplus e^i\}_{I \subseteq \{1, \ldots, \ell\}}$）两两独立。由于 $x_i$ 定义为 $\{x_i^I\}_{I \subseteq \{1, \ldots, \ell\}}$ 中出现次数占多数的值，我们可以应用命题 A.13 得到

$$
\begin{aligned}
\Pr[x_{i}\neq\hat{x}_{i}]&\leq\frac{1}{4\cdot(\varepsilon(n)/2)^{2}\cdot(2^{\ell}-1)}\\
&\leq\frac{1}{4\cdot(\varepsilon(n)/2)^{2}\cdot(2n/\varepsilon(n)^{2})}\\
&=\frac{1}{2n}.
\end{aligned}
$$

The above holds for all $i$, so by applying a union bound we see that the probability that $x_i \neq \hat{x}_i$ for some $i$ is at most ${1}/{2}$. That is, $x_i = \hat{x}_i$ for all $i$ (and hence $x = \hat{x}$) with probability at least ${1}/{2}$.

上式对所有 $i$ 都成立，于是应用联合界可知：存在某个 $i$ 使 $x_i \neq \hat{x}_i$ 的概率至多为 ${1}/{2}$。也就是说，对所有 $i$ 都有 $x_i = \hat{x}_i$（从而 $x = \hat{x}$）的概率至少为 ${1}/{2}$。

Putting everything together: Let $n$ be as in Claim 8.17 and $y = f(\hat{x})$. With probability at least $\varepsilon(n)/2$ we have $\hat{x} \in S_n$. All the guesses $\sigma^i$ are correct with probability at least

**综合以上：**

设 $n$ 如断言 8.17 所述，且 $y = f(\hat{x})$。$\hat{x} \in S_n$ 以至少 $\varepsilon(n)/2$ 的概率成立。所有猜测 $\sigma^i$ 都正确的概率至少为

$$
\frac{1}{2^{\ell}}\geq\frac{1}{2\cdot(2n/\varepsilon(n)^{2}+1)}>\frac{\varepsilon(n)^{2}}{5n}
$$

for $n$ sufficiently large. Conditioned on both the above, $\mathcal{A}^{\prime}$ outputs $x = \hat{x}$ with probability at least ${1}/{2}$. The overall probability with which $\mathcal{A}^{\prime}$ inverts its input is thus at least $\varepsilon(n)^{3}/20n = 1/(20np(n)^{3})$ for infinitely many $n$. Since ${20}np(n)^{3}$ is polynomial in $n$, this proves Proposition 8.16.

当 $n$ 足够大时上式成立。在以上两个事件同时发生的条件下，$\mathcal{A}^{\prime}$ 以至少 ${1}/{2}$ 的概率输出 $x = \hat{x}$。因此，对无穷多个 $n$，$\mathcal{A}^{\prime}$ 对其输入求逆的总概率至少为 $\varepsilon(n)^{3}/20n = 1/(20np(n)^{3})$。由于 ${20}np(n)^{3}$ 是 $n$ 的多项式，这就证明了命题 8.16。
