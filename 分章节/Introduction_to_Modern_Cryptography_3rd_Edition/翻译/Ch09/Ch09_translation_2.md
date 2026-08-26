## 9.2 Primes, Factoring, and RSA　素数、因子分解与 RSA

In this section, we show the first examples of number-theoretic problems that are conjectured to be “hard.” We begin with a discussion of one of the oldest problems: integer factorization or just factoring.

本节给出首批被猜想为“困难的”数论问题的例子。我们从最古老的问题之一谈起：整数因子分解，或简称因子分解。

Given a composite integer $N$, the factoring problem is to find integers $p, q > 1$ such that $pq = N$. Factoring is a classic example of a hard problem, both because it is so simple to describe and since it has been recognized as a hard computational problem for a long time (even before its use in cryptography). The problem can be solved in exponential time $\mathcal{O}(\sqrt{N} \cdot \mathsf{polylog}(N))$ using trial division: that is, by exhaustively checking whether $p$ divides $N$ for $p = 2, \ldots, \lfloor \sqrt{N} \rfloor$. (This method requires $\sqrt{N}$ divisions, each one taking $\mathsf{polylog}(N) = \|N\|^c$ time for some constant $c$.) This always succeeds because although the largest prime factor of $N$ may be as large as $N/2$, the smallest prime factor of $N$ can be at most $\lfloor \sqrt{N} \rfloor$. Although algorithms with better running time are known (see Chapter 10), no polynomial-time algorithm for factoring has been demonstrated despite many years of effort.

给定合数 $N$，因子分解问题就是要找出整数 $p, q > 1$ 使得 $pq = N$。因子分解是困难问题的经典例子：一方面它描述起来极其简单，另一方面人们很早（早在它被用于密码学之前）就认识到这是一个困难的计算问题。用试除法可以在指数时间 $\mathcal{O}(\sqrt{N} \cdot \mathsf{polylog}(N))$ 内求解该问题：也就是对 $p = 2, \ldots, \lfloor \sqrt{N} \rfloor$ 逐一检验 $p$ 是否整除 $N$。（该方法需要 $\sqrt{N}$ 次除法，每次耗时 $\mathsf{polylog}(N) = \|N\|^c$，其中 $c$ 为某个常数。）这种方法总能成功，因为虽然 $N$ 的最大素因子可能大到 $N/2$，但 $N$ 的最小素因子至多是 $\lfloor \sqrt{N} \rfloor$。尽管已知运行时间更优的算法（见第 10 章），但经过多年的努力，仍未有人给出因子分解的多项式时间算法。

Consider the following experiment for a given algorithm $\mathcal{A}$ and parameter $n$:

对给定的算法 $\mathcal{A}$ 和参数 $n$，考虑如下实验：

The weak factoring experiment $\mathsf{w\text{-}Factor}_{\mathcal{A}}(n)$:

弱因子分解实验 $\mathsf{w\text{-}Factor}_{\mathcal{A}}(n)$：

1. Choose two uniform n-bit integers $x_{1}, x_{2}$

   均匀选取两个 $n$ 比特整数 $x_{1}, x_{2}$

2. Compute $N := x_1 \cdot x_2$.

   计算 $N := x_1 \cdot x_2$。

3. $\mathcal{A}$ is given $N$, and outputs $x_{1}^{\prime}, x_{2}^{\prime} > 1$.

   将 $N$ 交给 $\mathcal{A}$，$\mathcal{A}$ 输出 $x_{1}^{\prime}, x_{2}^{\prime} > 1$。

4. The output of the experiment is defined to be 1 if $x_1^{\prime} \cdot x_2^{\prime} = N$, and 0 otherwise.

   若 $x_1^{\prime} \cdot x_2^{\prime} = N$，则实验输出定义为 1；否则为 0。

We have just said that the factoring problem is believed to be hard. Does this mean that

我们刚说过因子分解问题被认为是困难的。这是否意味着

$$
\Pr[\mathsf{w\text{-}Factor}_{\mathcal{A}}(n)=1]\leq\mathsf{negl}(n)
$$

is negligible for every PPT algorithm $\mathcal{A}$? Not at all. For starters, the number $N$ in the above experiment is even with probability ${3}/{4}$ (this occurs when either $x_1$ or $x_2$ is even); it is, of course, easy for $\mathcal{A}$ to factor $N$ in this case. While we can make $\mathcal{A}$'s job more difficult by requiring $\mathcal{A}$ to output integers $x^{\prime}_1, x^{\prime}_2$ of length $n$, it remains the case that $x_1$ or $x_2$ (and hence $N$) might have small prime factors that can still be easily found. For cryptographic applications, we will need to prevent this.

对所有 PPT 算法 $\mathcal{A}$ 都是可忽略的？绝非如此。首先，上述实验中的数 $N$ 以 ${3}/{4}$ 的概率是偶数（当 $x_1$ 或 $x_2$ 为偶数时就会如此）；这种情况下 $\mathcal{A}$ 当然容易分解 $N$。虽然可以通过要求 $\mathcal{A}$ 输出长度为 $n$ 的整数 $x^{\prime}_1, x^{\prime}_2$ 来增加它的难度，但 $x_1$ 或 $x_2$（从而 $N$）仍可能含有容易找到的小素因子。在密码学应用中，我们需要防止这种情况。

As this discussion indicates, the “hardest” numbers to factor are those having only large prime factors. This suggests redefining the above experiment so that $x_{1}, x_{2}$ are random n-bit primes rather than random n-bit integers, and in fact such an experiment will be used when we formally define the factoring assumption in Section 9.2.3. For this experiment to be useful in a cryptographic setting, however, it is necessary to be able to generate random n-bit primes efficiently. This is the topic of the next two sections.

如上所述，“最难”分解的数是那些只有大素因子的数。这提示我们重新定义上述实验，让 $x_{1}, x_{2}$ 是随机的 $n$ 比特素数而非随机的 $n$ 比特整数；事实上，9.2.3 节正式定义因子分解假设时用的正是这样的实验。然而，要让该实验在密码学场景中有用，就必须能够高效地生成随机 $n$ 比特素数。这正是接下来两节的主题。

### 9.2.1 Generating Random Primes　生成随机素数

A natural approach to generating a random n-bit prime is to repeatedly choose random n-bit integers until we find one that is prime; we repeat this at most t times or until we are successful. See Algorithm 9.31 for a high-level description of the process.

生成随机 $n$ 比特素数的一种自然做法是：反复选取随机的 $n$ 比特整数，直到找到一个素数为止；最多重复 $t$ 次，或直到成功为止。该过程的高层描述见算法 9.31。

ALGORITHM 9.31
Generating a random prime – high-level outline

Input: Length $n$; parameter $t$

Output: A uniform $n$-bit prime

for $i = 1$ to $t$:
  $p^{\prime} \leftarrow \{0,1\}^{n-1}$
  $p := 1\|p^{\prime}$
  if $p$ is prime return $p$
return fail

算法 9.31
生成随机素数——高层概要

输入：长度 $n$；参数 $t$

输出：一个均匀的 $n$ 比特素数

对 $i = 1$ 到 $t$ 执行：
  $p^{\prime} \leftarrow \{0,1\}^{n-1}$
  $p := 1\|p^{\prime}$
  若 $p$ 是素数则返回 $p$
返回 fail

Note that the algorithm forces the output to be an integer of length exactly $n$ (rather than length at most $n$) by fixing the high-order bit of $p$ to “1.” Our convention throughout this book is that an “integer of length n” means an integer whose binary representation with most significant bit equal to 1 is exactly n bits long.

注意，该算法通过把 $p$ 的最高位固定为“1”，强制输出恰为 $n$ 位长的整数（而不是至多 $n$ 位长）。本书通篇的约定是：“长度为 $n$ 的整数”指其二进制表示（最高位为 1）恰好为 $n$ 位长的整数。

Given a way to determine whether or not a given integer $p$ is prime, the above algorithm outputs a uniform $n$-bit prime conditioned on the event that it does not output fail. The probability that the algorithm outputs fail depends on $t$, and for our purposes we will want to set $t$ so as to obtain a failure probability that is negligible in $n$. To show that Algorithm 9.31 leads to an efficient (i.e., polynomial-time in $n$) algorithm for generating primes, we need a better understanding of two issues: (1) the probability that a uniform $n$-bit integer is prime and (2) how to efficiently test whether a given integer $p$ is prime. We discuss these issues briefly now, and defer a more in-depth exploration of the second topic to the following section.

有了判定给定整数 $p$ 是否为素数的方法之后，上述算法在“不输出 fail”的条件下输出均匀的 $n$ 比特素数。算法输出 fail 的概率取决于 $t$；就我们的目的而言，要把 $t$ 设成使失败概率关于 $n$ 可忽略。为了说明算法 9.31 能得到一个高效的（即关于 $n$ 多项式时间的）素数生成算法，需要更好地理解两个问题：（1）均匀的 $n$ 比特整数是素数的概率有多大；（2）如何高效地检测给定的整数 $p$ 是否是素数。我们现在简要讨论这两个问题，第二个话题的深入探讨留待下一节。

The distribution of primes. The prime number theorem, an important result in mathematics, gives fairly precise bounds on the fraction of integers of a given length that are prime. We state a corollary (without proof) that suffices for our purposes:

**素数的分布。**

素数定理是数学中的一个重要结果，它对给定长度的整数中素数所占的比例给出了相当精确的界。我们陈述一个（不加证明的）推论，它对我们的目的已经足够：

THEOREM 9.32 For any n > 1, the fraction of n-bit integers that are prime is at least ${1}/{3n}$.

定理 9.32　对任意 $n > 1$，$n$ 比特整数中素数所占的比例至少为 ${1}/{3n}$。

Returning to the approach for generating primes described above, this implies that if we set $t = 3n^2$ then the probability that a prime is not chosen in all $t$ iterations of the algorithm is at most

回到上面描述的素数生成方法，这意味着若取 $t = 3n^2$，则算法在全部 $t$ 次迭代中都未选到素数的概率至多为

$$
\left(1-\frac{1}{3n}\right)^{t}=\left(\left(1-\frac{1}{3n}\right)^{3n}\right)^{n}\leq\left(e^{-1}\right)^{n}=e^{-n}
$$

(using Inequality A.2), which is negligible in $n$. Thus, using $\mathsf{poly}(n)$ iterations we obtain an algorithm for which the probability of outputting fail is negligible in $n$. (Tighter results than Theorem 9.32 are known, and so in practice even fewer iterations are needed.)

（利用不等式 A.2），该概率关于 $n$ 可忽略。于是，用 $\mathsf{poly}(n)$ 次迭代就得到一个输出 fail 的概率关于 $n$ 可忽略的算法。（已有比定理 9.32 更紧的结果，因此实践中所需的迭代次数甚至更少。）

Testing primality. The problem of efficiently determining whether a given number is prime has a long history. In the 1970s the first efficient algorithms for testing primality were developed. These algorithms were probabilistic and had the following guarantee: if the input $p$ were a prime number, the algorithm would always output “prime.” On the other hand, if $p$ were composite, then the algorithm would almost always output “composite,” but might output the wrong answer (“prime”) with probability negligible in the length of $p$. Put differently, if the algorithm outputs “composite” then $p$ is definitely composite, but if the output is “prime” then it is very likely that $p$ is prime but it is also possible that a mistake has occurred (and $p$ is really composite).

**素性检测。**

高效判定给定数字是否是素数的问题由来已久。20 世纪 70 年代出现了最早的素性检测高效算法。这些算法是概率性的，并有如下保证：若输入 $p$ 是素数，算法一定输出“素数”；反过来，若 $p$ 是合数，算法几乎总是输出“合数”，但可能以关于 $\|p\|$ 可忽略的概率输出错误答案（“素数”）。换种说法：若算法输出“合数”，则 $p$ 必定是合数；但若输出“素数”，则 $p$ 很可能是素数，不过也存在出错的可能（即 $p$ 其实是合数）。

When using a randomized primality test of this sort in Algorithm 9.31 (the prime-generation algorithm shown earlier), the output of the algorithm is a uniform prime of the desired length so long as the algorithm does not output fail and the randomized primality test did not err during the execution of the algorithm. This means that an additional source of error (besides the possibility of outputting fail) is introduced, and the algorithm may now output a composite number by mistake. Since we can ensure that this happens with only negligible probability, this remote possibility is of no practical concern and we can safely ignore it.

把这类随机化素性检测用于算法 9.31（前面给出的素数生成算法）时，只要算法没有输出 fail、且随机化素性检测在执行过程中没有出错，算法输出的就是所需长度的均匀素数。这意味着引入了另一个错误来源（除输出 fail 的可能性之外）：算法现在可能误输出一个合数。由于我们可以确保这种情况只以可忽略的概率发生，这种微小的可能性并无实际影响，可以放心忽略。

A deterministic polynomial-time algorithm for testing primality was demonstrated in a breakthrough result in 2002. That algorithm, although running in polynomial time, is slower than the probabilistic tests mentioned above. For this reason, probabilistic primality tests are still used exclusively in practice for generating large prime numbers.

2002 年的一项突破性成果给出了确定性的多项式时间素性检测算法。该算法虽然运行时间为多项式，却比上述概率性检测慢。因此，实践中生成大素数时仍然只用概率性素性检测。

In Section 9.2.2 we describe and analyze one of the most commonly used probabilistic primality tests: the Miller–Rabin algorithm. This algorithm takes two inputs: an integer $p$ and a parameter $t$ (in unary) that determines the error probability. The Miller–Rabin algorithm runs in time polynomial in $\|p\|$ and $t$, and satisfies:

9.2.2 节将描述并分析最常用的概率性素性检测之一：米勒–拉宾算法。该算法接受两个输入：整数 $p$ 和决定错误概率的参数 $t$（以一进制表示）。米勒–拉宾算法的运行时间关于 $\|p\|$ 和 $t$ 是多项式的，并且满足：

THEOREM 9.33 If p is prime, then the Miller–Rabin test always outputs “prime.” If $p$ is composite, the algorithm outputs “composite” except with probability at most ${2}^{-t}$.

定理 9.33　若 $p$ 是素数，则米勒–拉宾检测总是输出“素数”。若 $p$ 是合数，则以至少 $1 - {2}^{-t}$ 的概率输出“合数”。

Putting it all together. Given the preceding discussion, we can now describe a polynomial-time prime-generation algorithm that, on input n, outputs an n-bit prime except with probability negligible in n; moreover, conditioned on the output $p$ being prime, $p$ is a uniformly distributedn-bit prime. The full procedure is described in Algorithm 9.34.

**综合起来。**

基于以上讨论，现在可以描述一个多项式时间的素数生成算法：输入 $n$，除关于 $n$ 可忽略的概率外，它输出一个 $n$ 比特素数；而且在输出 $p$ 为素数的条件下，$p$ 是均匀分布的 $n$ 比特素数。完整流程见算法 9.34。

ALGORITHM 9.34
Generating a random prime

Input: Length $n$
Output: A uniform $n$-bit prime

for $i = 1$ to ${3}n^2$:
  $p^{\prime} \leftarrow \{0,1\}^{n-1}$
  $p := 1\|p^{\prime}$
  run the Miller-Rabin test on input $p$ and parameter ${1}^n$
  if the output is “prime,” return $p$
return fail

算法 9.34
生成随机素数

输入：长度 $n$
输出：一个均匀的 $n$ 比特素数

对 $i = 1$ 到 ${3}n^2$ 执行：
  $p^{\prime} \leftarrow \{0,1\}^{n-1}$
  $p := 1\|p^{\prime}$
  以输入 $p$ 和参数 ${1}^n$ 运行米勒–拉宾检测
  若输出为“素数”则返回 $p$
返回 fail

Generating primes of a particular form. It is sometimes desirable to generate a random $n$-bit prime $p$ of a particular form, for example, satisfying $p = 3 \bmod 4$ or such that $p = 2q + 1$ where $q$ is also prime ($p$ of the latter type are called strong primes). In this case, appropriate modifications of the prime-generation algorithm shown above can be used. (For example, in order to obtain a prime of the form $p = 2q + 1$, modify the algorithm to generate a random prime $q$, compute $p := 2q + 1$, and then output $p$ if it too is prime.) While these modified algorithms work well in practice, rigorous proofs that they run in polynomial time and fail with only negligible probability are more complex (and, in some cases, rely on unproven number-theoretic conjectures regarding the density of primes of a particular form). A detailed exploration of these issues is beyond the scope of this book, and we will simply assume the existence of appropriate prime-generation algorithms when needed.

**生成特定形式的素数。**

有时我们希望生成具有特定形式的随机 $n$ 比特素数 $p$，例如满足 $p = 3 \bmod 4$，或者使得 $p = 2q + 1$ 且 $q$ 也是素数（后一类 $p$ 称为强素数）。这时可以对上面给出的素数生成算法做适当修改。（例如，为得到形如 $p = 2q + 1$ 的素数，可以修改算法：先生成一个随机素数 $q$，计算 $p := 2q + 1$，若 $p$ 也是素数则输出它。）这些修改后的算法在实践中效果很好，但要严格证明它们在多项式时间内运行且失败概率可忽略则更为复杂（某些情形下还依赖关于特定形式素数密度的、尚未证明的数论猜想）。对这些问题的详细探讨超出了本书范围；需要时我们将直接假定存在合适的素数生成算法。

### 9.2.2 \*Primality Testing　\*素性检测

We now describe the Miller–Rabin primality test and prove Theorem 9.33. (We rely on the material presented in Section 9.1.5.) This material is not used directly in the rest of the book.

本节描述米勒–拉宾素性检测并证明定理 9.33。（要用到 9.1.5 节介绍的内容。）这部分内容在本书其余部分不会被直接用到。

The key to the Miller–Rabin algorithm is to find a property that distinguishes primes and composites. Let $N$ denote the input number to be tested. We start with the following observation: if $N$ is prime then $|\mathbb{Z}_N^*| = N - 1$, and so for any $a \in \{1, \ldots, N-1\}$ we have $a^{N-1} = 1 \mod N$ by Theorem 9.14. This suggests testing whether $N$ is prime by choosing a uniform element $a$ and checking whether $a^{N-1} \overset{?}{=} 1 \mod N$. If $a^{N-1} \neq 1 \mod N$, then $N$ cannot be prime. Conversely, we might hope that if $N$ is not prime then there is a reasonable chance that we will pick $a$ with $a^{N-1} \neq 1 \mod N$, and so by repeating this test many times we can determine whether $N$ is prime or not with high confidence. The above approach is shown as Algorithm 9.35. (Recall that exponentiation modulo $N$ and computation of greatest common divisors can be carried out in polynomial time. Choosing a uniform element of $\{1, \ldots, N-1\}$ can also be done in polynomial time. See Appendix B.2.)

米勒–拉宾算法的关键在于找到一个能区分素数与合数的性质。令 $N$ 表示待检测的输入数。从如下观察入手：若 $N$ 是素数，则 $|\mathbb{Z}_N^*| = N - 1$，于是由定理 9.14，对任意 $a \in \{1, \ldots, N-1\}$ 都有 $a^{N-1} = 1 \mod N$。这提示了如下素性检测思路：均匀选取元素 $a$，检查是否 $a^{N-1} \overset{?}{=} 1 \bmod N$。若 $a^{N-1} \neq 1 \mod N$，则 $N$ 不可能是素数。反过来，我们或许期望：若 $N$ 不是素数，就有相当大的机会选中使 $a^{N-1} \neq 1 \mod N$ 的 $a$；这样，把这个测试重复多次，就能以很高的置信度判断 $N$ 究竟是不是素数。上述思路见算法 9.35。（回忆一下，模 $N$ 幂运算与最大公因子的计算都可在多项式时间内完成；均匀选取 $\{1, \ldots, N-1\}$ 中的元素同样可在多项式时间内完成。见附录 B.2。）

ALGORITHM 9.35
Primality testing – first attempt

Input: Integer $N$ and parameter ${1}^{t}$
Output: A decision as to whether $N$ is prime or composite

for $i = 1$ to $t$:
  $a \leftarrow \{1, \ldots, N-1\}$
    if $a^{N-1} \neq 1 \bmod N$ return “composite”

return “prime”

算法 9.35
素性检测——第一次尝试

输入：整数 $N$ 与参数 ${1}^{t}$
输出：关于 $N$ 是素数还是合数的判定

对 $i = 1$ 到 $t$ 执行：
  $a \leftarrow \{1, \ldots, N-1\}$
  若 $a^{N-1} \neq 1 \bmod N$ 则返回“合数”

返回“素数”

If $N$ is prime the algorithm always outputs “prime.” If $N$ is composite, the algorithm outputs “composite” if in any iteration it finds an $a \in \{1, \ldots, N-1\}$ such that $a^{N-1} \neq 1 \bmod N$. Observe that if $a \notin \mathbb{Z}_N^*$ then $a^{N-1} \neq 1 \bmod N$. (If $\gcd(a, N) \neq 1$ then $\gcd(a^{N-1}, N) \neq 1$ and so $[a^{N-1} \mod N]$ cannot equal 1.) For now, we therefore restrict our attention to $a \in \mathbb{Z}_N^*$. We refer to any such $a$ with $a^{N-1} \neq 1 \bmod N$ as a witness that $N$ is composite, or simply a witness. We might hope that when $N$ is composite there are many witnesses, and thus the algorithm finds such a witness with “high” probability. This intuition is correct provided there is at least one witness. Before proving this, we need two group-theoretic lemmas.

若 $N$ 是素数，算法总输出“素数”。若 $N$ 是合数，则只要任何一次迭代找到满足 $a^{N-1} \neq 1 \bmod N$ 的 $a \in \{1, \ldots, N-1\}$，算法就输出“合数”。可以观察到：若 $a \notin \mathbb{Z}_N^*$，则必有 $a^{N-1} \neq 1 \bmod N$。（若 $\gcd(a, N) \neq 1$，则 $\gcd(a^{N-1}, N) \neq 1$，故 $[a^{N-1} \mod N]$ 不可能等于 1。）因此我们暂时只关注 $a \in \mathbb{Z}_N^*$ 的情形。凡是满足 $a^{N-1} \neq 1 \bmod N$ 的 $a$，我们都称为“$N$ 是合数的见证”，或简称见证。我们或许期望：当 $N$ 是合数时见证有很多，从而算法能以“高”概率找到这样一个见证。只要至少存在一个见证，这一直觉就是正确的。在证明这一点之前，需要两条群论引理。

PROPOSITION 9.36 Let $\mathbb{G}$ be a finite group, and $\mathbb{H} \subseteq \mathbb{G}$. Assume $\mathbb{H}$ is nonempty, and for all $a, b \in \mathbb{H}$ we have $ab \in \mathbb{H}$. Then $\mathbb{H}$ is a subgroup of $\mathbb{G}$.

命题 9.36　设 $\mathbb{G}$ 是有限群，且 $\mathbb{H} \subseteq \mathbb{G}$。假设 $\mathbb{H}$ 非空，并且对所有 $a, b \in \mathbb{H}$ 都有 $ab \in \mathbb{H}$。那么 $\mathbb{H}$ 是 $\mathbb{G}$ 的子群。

PROOF We need to verify that $\mathbb{H}$ satisfies all the conditions of Definition 9.9. By assumption, $\mathbb{H}$ is closed under the group operation. Associativity in $\mathbb{H}$ is inherited automatically from $\mathbb{G}$. Let $m = |\mathbb{G}|$ (here is where we use the fact that $\mathbb{G}$ is finite), and consider an arbitrary element $a \in \mathbb{H}$. Closure of $\mathbb{H}$ means that $\mathbb{H}$ contains $a^{m-1} = a^{-1}$ as well as $a^m = 1$. Thus, $\mathbb{H}$ contains the inverse of each of its elements, as well as the identity.

证明　我们需要验证 $\mathbb{H}$ 满足定义 9.9 的所有条件。由假设，$\mathbb{H}$ 对群运算封闭。$\mathbb{H}$ 中的结合律自动从 $\mathbb{G}$ 继承。令 $m = |\mathbb{G}|$（这里正是用到 $\mathbb{G}$ 有限这一事实的地方），并任取元素 $a \in \mathbb{H}$。$\mathbb{H}$ 的封闭性意味着 $\mathbb{H}$ 包含 $a^{m-1} = a^{-1}$ 以及 $a^m = 1$。于是，$\mathbb{H}$ 包含其中每个元素的逆元，也包含单位元。

LEMMA 9.37 Let $\mathbb{H}$ be a strict subgroup of a finite group $\mathbb{G}$ (i.e., $\mathbb{H} \neq \mathbb{G}$). Then $|\mathbb{H}| \leq |\mathbb{G}|/2$.

引理 9.37　设 $\mathbb{H}$ 是有限群 $\mathbb{G}$ 的真子群（即 $\mathbb{H} \neq \mathbb{G}$）。那么 $|\mathbb{H}| \leq |\mathbb{G}|/2$。

PROOF Let $\bar{h}$ be an element of $\mathbb{G}$ that is not in $\mathbb{H}$; since $\mathbb{H} \neq \mathbb{G}$, we know such an $\bar{h}$ exists. Consider the set $\bar{\mathbb{H}} \overset{\mathrm{def}}{=}\{\bar{h}h \mid h \in \mathbb{H}\}$. We show that (1) $|\bar{\mathbb{H}}| = |\mathbb{H}|$, and (2) every element of $\bar{\mathbb{H}}$ lies outside of $\mathbb{H}$; i.e., the intersection of $\mathbb{H}$ and $\bar{\mathbb{H}}$ is empty. Since both $\mathbb{H}$ and $\bar{\mathbb{H}}$ are subsets of $\mathbb{G}$, these imply $|\mathbb{G}| \geq |\mathbb{H}| + |\bar{\mathbb{H}}| = 2|\mathbb{H}|$, proving the lemma.

证明　取 $\bar{h}$ 为 $\mathbb{G}$ 中不属于 $\mathbb{H}$ 的元素；由于 $\mathbb{H} \neq \mathbb{G}$，这样的 $\bar{h}$ 必然存在。考虑集合 $\bar{\mathbb{H}} \overset{\mathrm{def}}{=}\{\bar{h}h \mid h \in \mathbb{H}\}$。我们证明：(1) $|\bar{\mathbb{H}}| = |\mathbb{H}|$；(2) $\bar{\mathbb{H}}$ 的每个元素都在 $\mathbb{H}$ 之外，也就是说 $\mathbb{H}$ 与 $\bar{\mathbb{H}}$ 的交集为空。由于 $\mathbb{H}$ 与 $\bar{\mathbb{H}}$ 都是 $\mathbb{G}$ 的子集，这两点蕴含 $|\mathbb{G}| \geq |\mathbb{H}| + |\bar{\mathbb{H}}| = 2|\mathbb{H}|$，引理得证。

For any $h_1, h_2 \in \mathbb{H}$, if $\bar{h}h_1 = \bar{h}h_2$ then, multiplying by $\bar{h}^{-1}$ on each side, we have $h_1 = h_2$. This shows that every distinct element $h \in \mathbb{H}$ corresponds to a distinct element $\bar{h}h \in \bar{\mathbb{H}}$, proving (1).

对任意 $h_1, h_2 \in \mathbb{H}$，若 $\bar{h}h_1 = \bar{h}h_2$，则两边同乘 $\bar{h}^{-1}$ 得 $h_1 = h_2$。这说明 $\mathbb{H}$ 中每个不同的元素 $h$ 都对应 $\bar{\mathbb{H}}$ 中一个不同的元素 $\bar{h}h$，(1) 得证。

Assume toward a contradiction that $\bar{h}h \in \mathbb{H}$ for some $h$. This means $\bar{h}h = h^{\prime}$ for some $h^{\prime} \in \mathbb{H}$, and so $\bar{h} = h^{\prime}h^{-1}$. Now, $h^{\prime}h^{-1} \in \mathbb{H}$ since $\mathbb{H}$ is a subgroup and $h^{\prime}, h^{-1} \in \mathbb{H}$. But this means that $\bar{h} \in \mathbb{H}$, in contradiction to the way $\bar{h}$ was chosen. This proves (2) and completes the proof of the lemma.

反设对某个 $h$ 有 $\bar{h}h \in \mathbb{H}$。这意味着存在 $h^{\prime} \in \mathbb{H}$ 使得 $\bar{h}h = h^{\prime}$，于是 $\bar{h} = h^{\prime}h^{-1}$。由于 $\mathbb{H}$ 是子群且 $h^{\prime}, h^{-1} \in \mathbb{H}$，故 $h^{\prime}h^{-1} \in \mathbb{H}$。但这意味着 $\bar{h} \in \mathbb{H}$，与 $\bar{h}$ 的取法矛盾。(2) 得证，引理证毕。

The following theorem will enable us to analyze the algorithm given earlier.

下面的定理使我们能够分析前面给出的算法。

THEOREM 9.38 Fix $N$. Say there exists a witness that $N$ is composite. Then at least half the elements of $\mathbb{Z}_N^*$ are witnesses that $N$ is composite.

定理 9.38　固定 $N$。设存在“$N$ 是合数”的见证。那么 $\mathbb{Z}_N^*$ 中至少一半的元素都是“$N$ 是合数”的见证。

PROOF Let $\mathsf{Bad}$ be the set of elements in $\mathbb{Z}_N^*$ that are not witnesses; that is, $a \in \mathsf{Bad}$ means $a^{N-1} = 1 \mod N$. Clearly, ${1} \in \mathsf{Bad}$. If $a, b \in \mathsf{Bad}$, then $(ab)^{N-1} = a^{N-1} \cdot b^{N-1} = 1 \cdot 1 = 1 \mod N$ and hence $ab \in \mathsf{Bad}$. By Lemma 9.36, we conclude that $\mathsf{Bad}$ is a subgroup of $\mathbb{Z}_N^*$. Since (by assumption) there is at least one witness, $\mathsf{Bad}$ is a strict subgroup of $\mathbb{Z}_N^*$. Lemma 9.37 then shows that $|\mathsf{Bad}| \leq |\mathbb{Z}_N^*|/2$, showing that at least half the elements of $\mathbb{Z}_N^*$ are not in $\mathsf{Bad}$ (and hence are witnesses).

证明　令 $\mathsf{Bad}$ 为 $\mathbb{Z}_N^*$ 中不是见证的元素构成的集合；也就是说，$a \in \mathsf{Bad}$ 意味着 $a^{N-1} = 1 \mod N$。显然 ${1} \in \mathsf{Bad}$。若 $a, b \in \mathsf{Bad}$，则 $(ab)^{N-1} = a^{N-1} \cdot b^{N-1} = 1 \cdot 1 = 1 \mod N$，故 $ab \in \mathsf{Bad}$。由引理 9.36 可知 $\mathsf{Bad}$ 是 $\mathbb{Z}_N^*$ 的子群。由于（由假设）至少存在一个见证，$\mathsf{Bad}$ 是 $\mathbb{Z}_N^*$ 的真子群。再由引理 9.37 得 $|\mathsf{Bad}| \leq |\mathbb{Z}_N^*|/2$，这表明 $\mathbb{Z}_N^*$ 中至少一半的元素不在 $\mathsf{Bad}$ 中（因而都是见证）。

Let $N$ be composite. If there exists a witness that $N$ is composite, then there are at least $|\mathbb{Z}_N^*|/2$ witnesses. The probability that we find either a witness or an element not in $\mathbb{Z}_N^*$ in any given iteration of the algorithm is thus at least ${1}/{2}$, and so the probability that the algorithm does not find a witness in any of the $t$ iterations (and hence the probability that the algorithm mistakenly outputs “prime”) is at most ${2}^{-t}$.

设 $N$ 是合数。若存在“$N$ 是合数”的见证，则见证至少有 $|\mathbb{Z}_N^*|/2$ 个。于是，算法在任意一次迭代中找到见证或找到不属于 $\mathbb{Z}_N^*$ 的元素的概率至少为 ${1}/{2}$；从而算法在全部 $t$ 次迭代中都找不到见证的概率（也就是算法误输出“素数”的概率）至多为 ${2}^{-t}$。

The above, unfortunately, does not give a complete solution since there are infinitely many composite numbers $N$ that do not have any witnesses that they are composite! Such values $N$ are known as Carmichael numbers; a detailed discussion is beyond the scope of this book.

遗憾的是，上面的讨论并未给出完整的解决方案，因为有无限多个合数 $N$ 根本没有任何能表明其为合数的见证！这样的 $N$ 值被称为 Carmichael 数；详细的讨论超出了本书范围。

Happily, a refinement of the above test can be shown to work for all $N$. Let $N-1=2^r u$, where $u$ is odd and $r\geq1$. (It is easy to compute $r$ and $u$ given $N$. Also, restricting to $r\geq1$ means that $N$ is odd, but testing primality is easy when $N$ is even!) The algorithm shown previously tests only whether $a^{N-1}=a^{2^r u}=1$ mod $N$. A more refined algorithm looks at the sequence of $r+1$ values $a^u$, $a^{2u}$, $\ldots$, $a^{2^r u}$ (all modulo $N$). Each term in this sequence is the square of the preceding term; thus, if some value is equal to $\pm1$ then all subsequent values will be equal to ${1}$.

所幸可以证明，上述测试的一个改进版本对所有 $N$ 都有效。令 $N-1=2^r u$，其中 $u$ 是奇数，$r\geq1$。（给定 $N$ 容易算出 $r$ 和 $u$。另外，限定 $r\geq1$ 意味着 $N$ 是奇数，而当 $N$ 是偶数时素性检测本来就容易！）前面给出的算法只检验是否有 $a^{N-1}=a^{2^r u}=1$ mod $N$；改进后的算法则考察由 $r+1$ 个值构成的序列 $a^u$, $a^{2u}$, $\ldots$, $a^{2^r u}$（全部模 $N$）。序列中每一项都是前一项的平方；因此，只要某个值等于 $\pm1$，其后的所有值都将等于 ${1}$。

Say that $a \in \mathbb{Z}_N^*$ is a strong witness that $N$ is composite (or simply a strong witness) if (1) $a^u \neq \pm 1 \bmod N$ and (2) $a^{2^iu} \neq -1 \bmod N$ for all $i \in \{1, \ldots, r-1\}$. Note that when an element $a$ is not a strong witness then the sequence $(a^u, a^{2u}, \ldots, a^{2^r u})$ (all taken modulo $N$) takes one of the following forms:

若 $a \in \mathbb{Z}_N^*$ 满足：(1) $a^u \neq \pm 1 \bmod N$；(2) 对所有 $i \in \{1, \ldots, r-1\}$ 都有 $a^{2^iu} \neq -1 \bmod N$——则称 $a$ 是“$N$ 是合数”的强见证，或简称强见证。注意，当元素 $a$ 不是强见证时，序列 $(a^u, a^{2u}, \ldots, a^{2^r u})$（全部模 $N$）必取下列形式之一：

$$
\left(\pm1,1,\ldots,1\right)\text{ or }\left(\star,\ldots,\star,-1,1,\ldots,1\right),
$$

where $\star$ is an arbitrary term. If a is not a strong witness then we have $a^{2^{r-1}u} = \pm 1 \bmod N$ and

其中 $\star$ 表示任意项。若 $a$ 不是强见证，则 $a^{2^{r-1}u} = \pm 1 \bmod N$，且

$$
a^{N-1}=a^{2^{r}u}=\left(a^{2^{r-1}u}\right)^{2}=1\bmod N,
$$

and so $a$ is not a witness that $N$ is composite, either. Put differently, if $a$ is a witness then it is also a strong witness and so there can only possibly be more strong witnesses than witnesses.

因此 $a$ 也不是“$N$ 是合数”的见证。换句话说，若 $a$ 是见证，则它同时也是强见证，所以强见证只可能比见证更多。

We first show that if $N$ is prime then there does not exist a strong witness that $N$ is composite. In doing so, we rely on the following easy lemma (which is a special case of Proposition 15.16 proved subsequently in Chapter 15):

我们先证明：若 $N$ 是素数，则不存在“$N$ 是合数”的强见证。这要用到下面这条简单的引理（它是第 15 章稍后证明的命题 15.16 的特例）：

LEMMA 9.39 Say $x \in \mathbb{Z}_N^*$ is a square root of 1 modulo $N$ if $x^2 = 1 \bmod N$. If $N$ is an odd prime then the only square roots of 1 modulo $N$ are $[\pm 1 \bmod N]$.

引理 9.39　若 $x \in \mathbb{Z}_N^*$ 满足 $x^2 = 1 \bmod N$，则称 $x$ 是 1 模 $N$ 的平方根。若 $N$ 是奇素数，则 1 模 $N$ 的平方根只有 $[\pm 1 \bmod N]$。

PROOF Say $x^2 = 1 \bmod N$ with $x \in \{1, \ldots, N-1\}$. Then ${0} = x^2 - 1 = (x+1)(x-1) \bmod N$, implying that $N \mid (x+1)$ or $N \mid (x-1)$ by Proposition 9.3. This can only possibly occur if $x = [\pm 1 \bmod N]$.

证明　设 $x^2 = 1 \bmod N$ 且 $x \in \{1, \ldots, N-1\}$。那么 ${0} = x^2 - 1 = (x+1)(x-1) \bmod N$，由命题 9.3 这意味着 $N \mid (x+1)$ 或 $N \mid (x-1)$。这只可能在 $x = [\pm 1 \bmod N]$ 时发生。

Let $N$ be an odd prime and fix arbitrary $a \in \mathbb{Z}_N^*$. Let $i \geq 0$ be the minimum value for which $a^{2^{i}u} = 1 \bmod N$; since $a^{2^{r}u} = a^{N-1} = 1 \bmod N$ we know that some such $i \leq r$ exists. If $i = 0$ then $a^u = 1 \bmod N$ and $a$ is not a strong witness. Otherwise,

设 $N$ 是奇素数，固定任意 $a \in \mathbb{Z}_N^*$。令 $i \geq 0$ 为使 $a^{2^{i}u} = 1 \bmod N$ 成立的最小值；由于 $a^{2^{r}u} = a^{N-1} = 1 \bmod N$，可知这样的 $i \leq r$ 必然存在。若 $i = 0$，则 $a^u = 1 \bmod N$，$a$ 不是强见证。否则，

$$
\left(a^{2^{i-1}u}\right)^{2}=a^{2^{i}u}=1\bmod N
$$

and $a^{2^{i-1}u}$ is a square root of 1. If $N$ is an odd prime, the only square roots of 1 are $\pm1$; by choice of $i$, however, $a^{2^{i-1}u} \neq 1 \bmod N$. So $a^{2^{i-1}u} = -1 \bmod N$, and $a$ is not a strong witness. We conclude that when $N$ is an odd prime there is no strong witness that $N$ is composite.

且 $a^{2^{i-1}u}$ 是 1 的平方根。若 $N$ 是奇素数，则 1 的平方根只有 $\pm1$；但由 $i$ 的取法，$a^{2^{i-1}u} \neq 1 \bmod N$。于是 $a^{2^{i-1}u} = -1 \bmod N$，故 $a$ 不是强见证。我们得出结论：当 $N$ 是奇素数时，不存在“$N$ 是合数”的强见证。

A composite integer $N$ is a prime power if $N = p^{r}$ for some prime $p$ and integer $r \geq 1$. We now show that every odd, composite $N$ that is not a prime power has many strong witnesses.

若合数 $N$ 满足 $N = p^{r}$（$p$ 为某素数，$r \geq 1$ 为整数），则称 $N$ 是素数幂。下面我们证明：每个非素数幂的奇合数 $N$ 都有许多强见证。

THEOREM 9.40 Let $N$ be an odd number that is not a prime power. Then at least half the elements of $\mathbb{Z}_N^*$ are strong witnesses that $N$ is composite.

定理 9.40　设 $N$ 是非素数幂的奇数。那么 $\mathbb{Z}_N^*$ 中至少一半的元素是“$N$ 是合数”的强见证。

PROOF Let $\mathsf{Bad} \subseteq \mathbb{Z}_N^*$ denote the set of elements that are not strong witnesses. We define a set $\mathsf{Bad}^{\prime}$ and show that: (1) $\mathsf{Bad}$ is a subset of $\mathsf{Bad}^{\prime}$, and (2) $\mathsf{Bad}^{\prime}$ is a strict subgroup of $\mathbb{Z}_N^*$. This suffices because by combining (2) and Lemma 9.37 we have that $|\mathsf{Bad}^{\prime}| \leq |\mathbb{Z}_N^*|/2$. Furthermore, by (1) it holds that $\mathsf{Bad} \subseteq \mathsf{Bad}^{\prime}$, and so $|\mathsf{Bad}| \leq |\mathsf{Bad}^{\prime}| \leq |\mathbb{Z}_N^*|/2$ as in Theorem 9.38. Thus, at least half the elements of $\mathbb{Z}_N^*$ are strong witnesses. (We stress that we do not claim that $\mathsf{Bad}$ is a subgroup of $\mathbb{Z}_N^*$.)

证明　令 $\mathsf{Bad} \subseteq \mathbb{Z}_N^*$ 为不是强见证的元素构成的集合。我们定义集合 $\mathsf{Bad}^{\prime}$，并证明：(1) $\mathsf{Bad}$ 是 $\mathsf{Bad}^{\prime}$ 的子集；(2) $\mathsf{Bad}^{\prime}$ 是 $\mathbb{Z}_N^*$ 的真子群。这就足够了：把 (2) 与引理 9.37 结合可得 $|\mathsf{Bad}^{\prime}| \leq |\mathbb{Z}_N^*|/2$；再加上 (1) 给出的 $\mathsf{Bad} \subseteq \mathsf{Bad}^{\prime}$，便有 $|\mathsf{Bad}| \leq |\mathsf{Bad}^{\prime}| \leq |\mathbb{Z}_N^*|/2$，论证与定理 9.38 相同。因此 $\mathbb{Z}_N^*$ 中至少一半的元素是强见证。（我们强调，并不声称 $\mathsf{Bad}$ 本身是 $\mathbb{Z}_N^*$ 的子群。）

Note first that $-1 \in \mathsf{Bad}$ since $(-1)^u = -1 \mod N$ (recall $u$ is odd). Let $i \in \{0, \ldots, r-1\}$ be the largest integer for which there exists an $a \in \mathsf{Bad}$ with $a^{2^i u} = -1 \mod N$; alternatively, $i$ is the largest integer for which there exists an $a \in \mathsf{Bad}$ with

首先注意 $-1 \in \mathsf{Bad}$，因为 $(-1)^u = -1 \mod N$（回忆 $u$ 是奇数）。令 $i \in \{0, \ldots, r-1\}$ 为最大的整数，使得存在 $a \in \mathsf{Bad}$ 满足 $a^{2^i u} = -1 \bmod N$；换言之，$i$ 是最大的整数，使得存在 $a \in \mathsf{Bad}$ 满足

$$
(a^{u},a^{2u},\ldots,a^{2^{r}u})=(\underbrace{\star,\ldots,\star,-1}_{i+1\text{ terms}},1,\ldots,1).
$$

Since $-1 \in \mathsf{Bad}$ and $(-1)^{2^0 u} = -1 \bmod N$, some such $i$ exists.

由于 $-1 \in \mathsf{Bad}$ 且 $(-1)^{2^0 u} = -1 \bmod N$，这样的 $i$ 必然存在。

Fix i as above, and define

按上述方式固定 $i$，并定义

$$
\mathsf{Bad}^{\prime}\stackrel{\mathrm{def}}{=}\{a\mid a^{2^{i}u}=\pm1\bmod N\}.
$$

We now prove what we claimed above.

下面证明前面声称的两点。

CLAIM 9.41 Bad $\subseteq$ Bad'.

断言 9.41　$\mathsf{Bad} \subseteq \mathsf{Bad}^{\prime}$。

Let $a \in \mathsf{Bad}$. Then either $a^u = 1 \bmod N$ or $a^{2^j u} = -1 \bmod N$ for some $j \in \{0, \ldots, r-1\}$. In the first case, $a^{2^i u} = (a^u)^{2^i} = 1 \bmod N$ and so $a \in \mathsf{Bad}^{\prime}$. In the second case, we have $j \leq i$ by choice of $i$. If $j = i$ then clearly $a \in \mathsf{Bad}^{\prime}$. If $j < i$ then $a^{2^i u} = (a^{2^j u})^{2^{i-j}} = 1 \bmod N$ and $a \in \mathsf{Bad}^{\prime}$. Since $a$ was arbitrary, this shows $\mathsf{Bad} \subseteq \mathsf{Bad}^{\prime}$.

设 $a \in \mathsf{Bad}$。那么要么 $a^u = 1 \bmod N$，要么对某个 $j \in \{0, \ldots, r-1\}$ 有 $a^{2^j u} = -1 \bmod N$。第一种情形下，$a^{2^i u} = (a^u)^{2^i} = 1 \bmod N$，故 $a \in \mathsf{Bad}^{\prime}$。第二种情形下，由 $i$ 的取法知 $j \leq i$。若 $j = i$，显然 $a \in \mathsf{Bad}^{\prime}$；若 $j < i$，则 $a^{2^i u} = (a^{2^j u})^{2^{i-j}} = 1 \bmod N$，仍有 $a \in \mathsf{Bad}^{\prime}$。由 $a$ 的任意性，$\mathsf{Bad} \subseteq \mathsf{Bad}^{\prime}$ 得证。

CLAIM 9.42 Bad' is a subgroup of $\mathbb{Z}_{N}^{*}$.

断言 9.42　$\mathsf{Bad}^{\prime}$ 是 $\mathbb{Z}_{N}^{*}$ 的子群。

Clearly ${1} \in \mathsf{Bad}^{\prime}$. Furthermore, if $a, b \in \mathsf{Bad}^{\prime}$ then

显然 ${1} \in \mathsf{Bad}^{\prime}$。再者，若 $a, b \in \mathsf{Bad}^{\prime}$，则

$$
(ab)^{2^{i}u}=a^{2^{i}u}b^{2^{i}u}=(\pm1)(\pm1)=\pm1\bmod N
$$

and so $ab \in \mathsf{Bad}^{\prime}$. By Lemma 9.36, $\mathsf{Bad}^{\prime}$ is a subgroup.

于是 $ab \in \mathsf{Bad}^{\prime}$。由引理 9.36，$\mathsf{Bad}^{\prime}$ 是子群。

CLAIM 9.43 Bad' is a strict subgroup of $\mathbb{Z}_{N}^{*}$.

断言 9.43　$\mathsf{Bad}^{\prime}$ 是 $\mathbb{Z}_{N}^{*}$ 的真子群。

If $N$ is an odd, composite integer that is not a prime power, then $N$ can be written as $N = N_1 N_2$ with $N_1, N_2 > 1$ odd and $\gcd(N_1, N_2) = 1$. Appealing to the Chinese remainder theorem, let $a \leftrightarrow (a_1, a_2)$ denote the representation of $a \in \mathbb{Z}_N^*$ as an element of $\mathbb{Z}_{N_1}^* \times \mathbb{Z}_{N_2}^*$; that is, $a_1 = [a \bmod N_1]$ and $a_2 = [a \bmod N_2]$. Take $a \in \mathsf{Bad}^{\prime}$ such that $a^{2^i u} = -1 \bmod N$ (such as an $a$ must exist by the way we defined $i$), and say $a \leftrightarrow (a_1, a_2)$. Since $-1 \leftrightarrow (-1, -1)$ we have

若 $N$ 是非素数幂的奇合数，则 $N$ 可以写成 $N = N_1 N_2$，其中 $N_1, N_2 > 1$ 为奇数且 $\gcd(N_1, N_2) = 1$。借助中国剩余定理，用 $a \leftrightarrow (a_1, a_2)$ 表示 $a \in \mathbb{Z}_N^*$ 作为 $\mathbb{Z}_{N_1}^* \times \mathbb{Z}_{N_2}^*$ 中元素的表示；也就是说，$a_1 = [a \bmod N_1]$，$a_2 = [a \bmod N_2]$。取 $a \in \mathsf{Bad}^{\prime}$ 使得 $a^{2^i u} = -1 \bmod N$（由 $i$ 的定义方式可知这样的 $a$ 必然存在），并设 $a \leftrightarrow (a_1, a_2)$。由于 $-1 \leftrightarrow (-1, -1)$，有

$$
(a_{1},a_{2})^{2^{i}u}=(a_{1}^{2^{i}u},a_{2}^{2^{i}u})=(-1,-1),
$$

and so

于是

$$
a_{1}^{2^{i}u}=-1\bmod N_{1}\quad\text{and}\quad a_{2}^{2^{i}u}=-1\bmod N_{2}.
$$

Consider the element $b \in \mathbb{Z}_N^*$ with $b \leftrightarrow (a_1, 1)$. Then

考虑满足 $b \leftrightarrow (a_1, 1)$ 的元素 $b \in \mathbb{Z}_N^*$。那么

$$
b^{2^{i}u}\leftrightarrow(a_{1},1)^{2^{i}u}=([a_{1}^{2^{i}u}\bmod N_{1}],\;1)=(-1,1)\not\leftrightarrow\pm1.
$$

That is, $b^{2^i u} \neq \pm1 \bmod N$ and so we have found an element $b \notin \mathsf{Bad}^{\prime}$. This proves that $\mathsf{Bad}^{\prime}$ is a strict subgroup of $\mathbb{Z}_N^*$ and so, by Lemma 9.37, the size of $\mathsf{Bad}^{\prime}$ (and thus the size of $\mathsf{Bad}$) is at most half the size of $\mathbb{Z}_N^*$.

也就是说，$b^{2^i u} \neq \pm1 \bmod N$，于是我们找到了元素 $b \notin \mathsf{Bad}^{\prime}$。这就证明了 $\mathsf{Bad}^{\prime}$ 是 $\mathbb{Z}_N^*$ 的真子群；从而由引理 9.37，$\mathsf{Bad}^{\prime}$ 的大小（因而 $\mathsf{Bad}$ 的大小）至多是 $\mathbb{Z}_N^*$ 大小的一半。

An integer $N$ is a perfect power if $N = \tilde{N}^e$ for integers $\tilde{N}$ and $e \geq 2$ (here it is not required for $\tilde{N}$ to be prime, although of course any prime power is also a perfect power). Algorithm 9.44 gives the Miller–Rabin primality test. Exercises 9.16 and 9.17 ask you to show that testing whether $N$ is a perfect power, and testing whether a particular $a$ is a strong witness, can be done in polynomial time. Given these results, the algorithm clearly runs in time polynomial in $\|N\|$ and $t$. We can now complete the proof of Theorem 9.33:

若整数 $N$ 满足 $N = \tilde{N}^e$（$\tilde{N}$ 与 $e \geq 2$ 为整数），则称 $N$ 是完全幂（这里不要求 $\tilde{N}$ 是素数，当然任何素数幂同时也是完全幂）。算法 9.44 给出了米勒–拉宾素性检测。习题 9.16 与习题 9.17 请读者证明：检测 $N$ 是否是完全幂，以及检测某个特定的 $a$ 是否是强见证，都可以在多项式时间内完成。有了这些结果，该算法显然以关于 $\|N\|$ 和 $t$ 的多项式时间运行。现在可以补全定理 9.33 的证明了：

ALGORITHM 9.44
The Miller–Rabin primality test

Input: Integer $N > 2$ and parameter ${1}^{t}$
Output: A decision as to whether $N$ is prime or composite

if $N$ is even, return “composite”
if $N$ is a perfect power, return “composite”
compute $r \geq 1$ and $u$ odd such that $N - 1 = 2^{r}u$
for $j = 1$ to $t$:
  $a \leftarrow \{1, \ldots, N - 1\}$
  if $a^{u} \neq \pm 1 \bmod N$ and $a^{2^{i}u} \neq -1 \bmod N$ for $i \in \{1, \ldots, r-1\}$
    return “composite”
return “prime”

算法 9.44
米勒–拉宾素性检测

输入：整数 $N > 2$ 与参数 ${1}^{t}$
输出：关于 $N$ 是素数还是合数的判定

若 $N$ 是偶数，返回“合数”
若 $N$ 是完全幂，返回“合数”
计算 $r \geq 1$ 和奇数 $u$ 使得 $N - 1 = 2^{r}u$
对 $j = 1$ 到 $t$ 执行：
  $a \leftarrow \{1, \ldots, N - 1\}$
  若 $a^{u} \neq \pm 1 \bmod N$ 且对所有 $i \in \{1, \ldots, r-1\}$ 有 $a^{2^{i}u} \neq -1 \bmod N$
    返回“合数”
返回“素数”

PROOF If $N$ is an odd prime, there are no strong witnesses and so the Miller–Rabin algorithm always outputs “prime.” If $N$ is even or a prime power, the algorithm always outputs “composite.” The interesting case is when $N$ is an odd, composite integer that is not a prime power. Consider any iteration of the inner loop. Note first that if $a \notin \mathbb{Z}_N^*$ then $a^u \neq \pm 1 \bmod N$ and $a^{2^i u} \neq -1 \bmod N$ for $i \in \{1, \ldots, r-1\}$. The probability of finding either a strong witness or an element not in $\mathbb{Z}_N^*$ is at least ${1}/{2}$ (invoking Theorem 9.40). Thus, the probability that the algorithm never outputs “composite” in any of the $t$ iterations is at most ${2}^{-t}$.

证明　若 $N$ 是奇素数，则不存在强见证，故米勒–拉宾算法总输出“素数”。若 $N$ 是偶数或素数幂，算法总输出“合数”。有趣的情形是 $N$ 为非素数幂的奇合数。考虑内层循环的任意一次迭代。首先注意：若 $a \notin \mathbb{Z}_N^*$，则 $a^u \neq \pm 1 \bmod N$ 且对所有 $i \in \{1, \ldots, r-1\}$ 有 $a^{2^i u} \neq -1 \bmod N$。找到强见证或找到不属于 $\mathbb{Z}_N^*$ 的元素的概率至少为 ${1}/{2}$（引用定理 9.40）。因此，算法在全部 $t$ 次迭代中都从不输出“合数”的概率至多为 ${2}^{-t}$。

### 9.2.3 The Factoring Assumption　因子分解假设

Let GenModulus be a polynomial-time algorithm that, on input ${1}^n$, outputs $(N, p, q)$ where $N = pq$, and $p$ and $q$ are $n$-bit primes except with probability negligible in $n$. (The natural way to do this is to generate two uniform $n$-bit primes, as discussed previously, and then multiply them to obtain $N$.) Then consider the following experiment for a given algorithm $\mathcal{A}$ and parameter $n$:

设 $\mathsf{GenModulus}$ 是一个多项式时间算法：以 ${1}^n$ 为输入，输出 $(N, p, q)$，其中 $N = pq$，且除关于 $n$ 可忽略的概率外，$p$ 和 $q$ 都是 $n$ 比特素数。（自然的实现方式是按前文讨论的方法生成两个均匀的 $n$ 比特素数，然后相乘得到 $N$。）对给定的算法 $\mathcal{A}$ 和参数 $n$，考虑如下实验：

The factoring experiment $\mathsf{Factor}_{\mathcal{A},\mathsf{GenModulus}}(n)$:

因子分解实验 $\mathsf{Factor}_{\mathcal{A},\mathsf{GenModulus}}(n)$：

1. Run $\mathsf{GenModulus}(1^{n})$ to obtain (N, p, q).

   运行 $\mathsf{GenModulus}(1^{n})$ 得到 $(N, p, q)$。

2. A is given N, and outputs $p^{\prime}, q^{\prime} > 1$.

   将 $N$ 交给 $\mathcal{A}$，$\mathcal{A}$ 输出 $p^{\prime}, q^{\prime} > 1$。

3. The output of the experiment is defined to be 1 if $p^{\prime} \cdot q^{\prime} = N$, and 0 otherwise.

   若 $p^{\prime} \cdot q^{\prime} = N$，则实验输出定义为 1；否则为 0。

Note that if the output of the experiment is 1 then $\{p^{\prime}, q^{\prime}\} = \{p, q\}$, unless $p$ or $q$ are composite (which happens with only negligible probability).

注意，若实验输出为 1，则 $\{p^{\prime}, q^{\prime}\} = \{p, q\}$，除非 $p$ 或 $q$ 是合数（这只以可忽略的概率发生）。

We now formally define the factoring assumption:

现在正式定义因子分解假设：

DEFINITION 9.45 Factoring is hard relative to GenModulus if for all probabilistic polynomial-time algorithms A there exists a negligible function $\mathsf{negl}$ such that

定义 9.45　称因子分解相对于 $\mathsf{GenModulus}$ 是困难的，如果对每个概率多项式时间算法 $\mathcal{A}$，都存在可忽略函数 $\mathsf{negl}$ 使得

$$
\Pr[\mathsf{Factor}_{\mathcal{A},\mathsf{GenModulus}}(n)=1]\leq\mathsf{negl}(n).
$$

The factoring assumption is the assumption that there exists a GenModulus relative to which factoring is hard.

因子分解假设是指：存在某个 $\mathsf{GenModulus}$，使得因子分解相对于它是困难的。

### 9.2.4 The RSA Assumption　RSA 假设

The factoring problem has been studied for hundreds of years without an efficient algorithm being found. Although the factoring assumption does give a one-way function (see Section 9.4.1), it unfortunately does not directly yield practical cryptosystems. (In Section 15.5.2, however, we show how to construct efficient cryptosystems based on a problem whose hardness is equivalent to that of factoring.) This has motivated a search for other problems whose difficulty is related to the hardness of factoring. The best known of these is a problem introduced in 1978 by Rivest, Shamir, and Adleman and now called the RSA problem in their honor.

因子分解问题已被研究了数百年，却始终没有找到高效算法。虽然因子分解假设确实给出一个单向函数（见 9.4.1 节），但可惜它并不能直接导出实用的密码体制。（不过在 15.5.2 节，我们将展示如何基于一个困难性与因子分解等价的问题来构造高效的密码体制。）这促使人们去寻找其他困难性与因子分解相关联的问题。其中最著名的，是 Rivest、Shamir 和 Adleman 于 1978 年提出的问题——如今为纪念他们而称为 RSA 问题。

Given a modulus $N$ and an integer $e > 2$ relatively prime to $\phi(N)$, Corollary 9.22 shows that exponentiation to the $e$th power modulo $N$ is a permutation. We can therefore define $[y^{1/e} \mod N]$ (for any $y \in \mathbb{Z}_N^*$) as the unique element of $\mathbb{Z}_N^*$ that yields $y$ when raised to the $e$th power modulo $N$; that is, $x = y^{1/e} \mod N$ if and only if $x^e = y \mod N$. The RSA problem, informally, is to compute $[y^{1/e} \mod N]$ for a modulus $N$ of unknown factorization.

给定模数 $N$ 和与 $\phi(N)$ 互素的整数 $e > 2$，推论 9.22 表明模 $N$ 的 $e$ 次幂运算是置换。因此我们可以把 $[y^{1/e} \bmod N]$（对任意 $y \in \mathbb{Z}_N^*$）定义为 $\mathbb{Z}_N^*$ 中唯一的那个元素，它在模 $N$ 下取 $e$ 次幂便得到 $y$；也就是说，$x = y^{1/e} \mod N$ 当且仅当 $x^e = y \mod N$。非正式地说，RSA 问题就是要对因子分解未知的模数 $N$ 计算 $[y^{1/e} \bmod N]$。

Formally, let $\mathsf{GenRSA}$ be a probabilistic polynomial-time algorithm that, on input ${1}^n$, outputs a modulus $N$ that is the product of two $n$-bit primes, as well as integers $e, d > 0$ with $\gcd(e, \phi(N)) = 1$ and $ed = 1 \bmod \phi(N)$. (Such a $d$ exists since $e$ is invertible modulo $\phi(N)$. The purpose of $d$ will become clear later.) The algorithm may fail with probability negligible in $n$. Consider the following experiment for a given algorithm $\mathcal{A}$ and security parameter $n$:

形式化地，设 $\mathsf{GenRSA}$ 是一个概率多项式时间算法：以 ${1}^n$ 为输入，输出一个模数 $N$（为两个 $n$ 比特素数的乘积），以及整数 $e, d > 0$，满足 $\gcd(e, \phi(N)) = 1$ 且 $ed = 1 \bmod \phi(N)$。（这样的 $d$ 必然存在，因为 $e$ 模 $\phi(N)$ 可逆。$d$ 的用途稍后便会清楚。）该算法允许以关于 $n$ 可忽略的概率失败。对给定的算法 $\mathcal{A}$ 和安全参数 $n$，考虑如下实验：

The RSA experiment $\mathsf{RSA\text{-}inv}_{\mathcal{A},\mathsf{GenRSA}}(n)$:

RSA 实验 $\mathsf{RSA\text{-}inv}_{\mathcal{A},\mathsf{GenRSA}}(n)$：

1. Run $\mathsf{GenRSA}({1}^{n})$ to obtain $(N,e,d)$.

   运行 $\mathsf{GenRSA}({1}^{n})$ 得到 $(N,e,d)$。

2. Choose a uniform $y \in \mathbb{Z}_N^*$.

   均匀选取 $y \in \mathbb{Z}_N^*$。

3. $\mathcal{A}$ is given $N, e, y$, and outputs $x \in \mathbb{Z}_N^*$.

   将 $N, e, y$ 交给 $\mathcal{A}$，$\mathcal{A}$ 输出 $x \in \mathbb{Z}_N^*$。

4. The output of the experiment is defined to be 1 if $x^{e} = y \mod N$, and 0 otherwise.

   若 $x^{e} = y \mod N$，则实验输出定义为 1；否则为 0。

DEFINITION 9.46 The RSA problem is hard relative to GenRSA if for all probabilistic polynomial-time algorithms $\mathcal{A}$ there exists a negligible function $\mathsf{negl}$ such that $\Pr[\mathsf{RSA\text{-}inv}_{\mathcal{A},\mathsf{GenRSA}}(n) = 1] \leq \mathsf{negl}(n)$.

定义 9.46　称 RSA 问题相对于 $\mathsf{GenRSA}$ 是困难的，如果对每个概率多项式时间算法 $\mathcal{A}$，都存在可忽略函数 $\mathsf{negl}$ 使得 $\Pr[\mathsf{RSA\text{-}inv}_{\mathcal{A},\mathsf{GenRSA}}(n) = 1] \leq \mathsf{negl}(n)$。

The RSA assumption is that there exists a GenRSA algorithm relative to which the RSA problem is hard. A suitable GenRSA algorithm can be constructed from any algorithm GenModulus that generates a composite modulus along with its factorization. A high-level outline is provided as Algorithm 9.47, where the only thing left unspecified is how exactly e is chosen. In fact, the RSA problem is believed to be hard for any e that is relatively prime to $\phi(N)$. We discuss some typical choices of e below.

RSA 假设是指：存在某个 $\mathsf{GenRSA}$ 算法，使得 RSA 问题相对于它是困难的。合适的 $\mathsf{GenRSA}$ 算法可以从任何生成复合模数及其分解的算法 $\mathsf{GenModulus}$ 构造出来。高层概要见算法 9.47，其中唯一未指明的是 $e$ 究竟如何选取。事实上，对任何与 $\phi(N)$ 互素的 $e$，人们都相信 RSA 问题是困难的。下面讨论几种典型的 $e$ 的取法。

ALGORITHM 9.47

GenRSA – high-level outline

Input: Security parameter ${1}^{n}$

Output: N, e, d as described in the text

$(N,p,q)\gets\mathsf{GenModulus}(1^{n})$

$\phi(N):=(p-1)(q-1)$

choose $e > 1$ such that $\gcd(e, \phi(N)) = 1$

compute $d := [e^{-1} \bmod \phi(N)]$

return N, e, d

算法 9.47

GenRSA——高层概要

输入：安全参数 ${1}^{n}$

输出：正文所述的 $N$、$e$、$d$

$(N,p,q)\gets\mathsf{GenModulus}(1^{n})$

$\phi(N):=(p-1)(q-1)$

选取 $e > 1$ 使得 $\gcd(e, \phi(N)) = 1$

计算 $d := [e^{-1} \bmod \phi(N)]$

返回 $N$、$e$、$d$

**Example 9.48**　**例 9.48**

Say $\mathsf{GenModulus}$ outputs $(N, p, q) = (143, 11, 13)$. Then $\phi(N) = 120$. Next, we need to choose an $e$ that is relatively prime to $\phi(N)$; say we take $e = 7$. The next step is to compute $d$ such that $d = [e^{-1} \mod \phi(N)]$. This can be done as shown in Appendix B.2.2 to obtain $d = 103$. (One can check that ${7} \cdot 103 = 721 = 1 \mod 120$.) Our $\mathsf{GenRSA}$ algorithm in this case thus outputs $(N, e, d) = (143, 7, 103)$.

设 $\mathsf{GenModulus}$ 输出 $(N, p, q) = (143, 11, 13)$，则 $\phi(N) = 120$。接下来需要选取与 $\phi(N)$ 互素的 $e$；不妨取 $e = 7$。下一步是计算 $d$ 使得 $d = [e^{-1} \mod \phi(N)]$。按附录 B.2.2 所示的方法可求得 $d = 103$。（可以验证 ${7} \cdot 103 = 721 = 1 \mod 120$。）此时我们的 $\mathsf{GenRSA}$ 算法就输出 $(N, e, d) = (143, 7, 103)$。

As an example of the RSA problem relative to these parameters, take y = 64 and so the problem is to compute the 7th root of 64 modulo 143 without knowledge of d or the factorization of N.

作为这组参数下 RSA 问题的一个例子，取 $y = 64$，于是问题变成：在不知道 $d$ 或 $N$ 的分解的情况下，计算 64 模 143 的 7 次方根。

Computing $e$th roots modulo $N$ becomes easy if $d$, $\phi(N)$, or the factorization of $N$ is known. (As we show in the next section, any of these can be used to efficiently compute the others.) This follows from Corollary 9.22, which shows that $[y^d \bmod N]$ is the $e$th root of $y$ modulo $N$. This asymmetry—namely, that the RSA problem appears to be hard when $d$ or the factorization of $N$ is unknown, but becomes easy when $d$ is known—serves as the basis for applications of the RSA problem to public-key cryptography.

一旦知道 $d$、$\phi(N)$ 或者 $N$ 的分解，计算模 $N$ 的 $e$ 次方根就变容易了。（下一节将证明，这三者中任何一个都可以用来高效地算出其余两个。）这由推论 9.22 直接得出：$[y^d \bmod N]$ 正是 $y$ 模 $N$ 的 $e$ 次方根。这种不对称性——未知 $d$ 或 $N$ 的分解时 RSA 问题看似困难，而知道 $d$ 后就变得容易——正是 RSA 问题在公钥密码学中各种应用的基础。

**Example 9.49**　**例 9.49**

Continuing the previous example, we can compute the 7th root of 64 modulo 143 using the value $d = 103$; the answer is ${25} = 64^d = 64^{103} \mod 143$. We can verify that this is the correct solution since ${25}^e = 25^7 = 64 \mod 143$.

延续上一个例子，利用值 $d = 103$ 可以算出 64 模 143 的 7 次方根；答案是 ${25} = 64^d = 64^{103} \mod 143$。可以验证这是正确的解，因为 ${25}^e = 25^7 = 64 \mod 143$。

On the choice of $e$. There does not appear to be any difference in the hardness of the RSA problem for different exponents $e$ and, as such, different methods have been suggested for selecting it. One popular choice is to set $e = 3$, since then computing $e$th powers modulo $N$ requires only two multiplications (see Appendix B.2.3). If $e$ is to be set equal to 3, then $p$ and $q$ must be chosen with $p, q \neq 1 \mod 3$ so that $\gcd(e, \phi(N)) = 1$. For similar reasons, another popular choice is $e = 2^{16} + 1 = 65537$, a prime number with low Hamming weight (in Appendix B.2.3, we explain why such exponents are preferable). As compared to choosing $e = 3$, this makes exponentiation slightly more expensive but reduces the constraints on $p$ and $q$, and avoids some “low-exponent attacks” (described at the end of Section 12.5.1) that can result from poorly implemented cryptosystems based on the RSA problem.

**关于 $e$ 的选取。**

不同指数 $e$ 下 RSA 问题的困难性似乎看不出差别，因此人们提出了多种选取 $e$ 的方法。一种流行的做法是取 $e = 3$，因为这样计算模 $N$ 的 $e$ 次幂只需要两次乘法（见附录 B.2.3）。若要把 $e$ 取为 3，则必须选择满足 $p, q \neq 1 \mod 3$ 的 $p$ 和 $q$，以保证 $\gcd(e, \phi(N)) = 1$。出于类似的理由，另一种流行的取法是 $e = 2^{16} + 1 = 65537$，这是一个低汉明重量的素数（附录 B.2.3 解释了为什么这样的指数更可取）。与取 $e = 3$ 相比，这使幂运算的代价略高一些，但对 $p$ 和 $q$ 的约束更少，并且能避免某些“低指数攻击”（见 12.5.1 节末尾的描述）——这类攻击可能出现在基于 RSA 问题但实现不当的密码体制中。

Note that choosing $d$ small (that is, changing GenRSA to choose small $d$ and then compute $e := [d^{-1} \bmod \phi(N)]$) is a bad idea. If $d$ lies in a very small range then a brute-force search for $d$ can be carried out (and, as noted, once $d$ is known the RSA problem can be solved easily). Even if $d$ is chosen so that $d \approx N^{1/4}$, and so brute-force attacks are ruled out, there are known algorithms that can be used to recover $d$ from $N$ and $e$ in this case. For similar reasons, choosing $d$ with low Hamming weight is also not recommended.

注意，把 $d$ 选得很小（也就是修改 $\mathsf{GenRSA}$，让它先选小的 $d$，再计算 $e := [d^{-1} \bmod \phi(N)]$）是个坏主意。若 $d$ 落在很小的范围内，就可以对 $d$ 进行暴力搜索（而且如前所述，一旦知道 $d$，RSA 问题就容易求解了）。即便把 $d$ 选成 $d \approx N^{1/4}$ 从而排除暴力攻击，这种情形下也存在已知的算法能从 $N$ 和 $e$ 恢复出 $d$。出于类似的原因，也不建议选取低汉明重量的 $d$。

### 9.2.5 \*Relating the Factoring and RSA Assumptions　\*因子分解假设与 RSA 假设的关系

Say GenRSA is constructed as in Algorithm 9.47. If $N$ can be factored, then we can compute $\phi(N)$ and use this to compute $d := [e^{-1} \bmod \phi(N)]$ for any given $e$ (using Algorithm B.11). So for the RSA problem to be hard relative to GenRSA, the factoring problem must be hard relative to GenModulus. Put differently, the RSA problem cannot be more difficult than factoring; hardness of factoring (relative to GenModulus) can only potentially be a weaker assumption than hardness of the RSA problem (relative to GenRSA).

设 $\mathsf{GenRSA}$ 按算法 9.47 构造。若 $N$ 能够被分解，则可以算出 $\phi(N)$，进而用它对任意给定的 $e$ 计算 $d := [e^{-1} \bmod \phi(N)]$（使用算法 B.11）。所以，要使 RSA 问题相对于 $\mathsf{GenRSA}$ 是困难的，因子分解问题就必须相对于 $\mathsf{GenModulus}$ 是困难的。换个说法：RSA 问题不可能比因子分解更难；因子分解的困难性（相对于 $\mathsf{GenModulus}$）只可能是比 RSA 问题的困难性（相对于 $\mathsf{GenRSA}$）更弱的假设。

What about the other direction? That is, is hardness of the RSA problem implied by hardness of factoring? That remains an open question. The best we can show is that computing an RSA private key from an RSA public key (i.e., computing $d$ from $N$ and $e$) is as hard as factoring. We start by proving a slightly more powerful result.

那反方向呢？也就是说，RSA 问题的困难性能否由因子分解的困难性推出？这仍是公开问题。我们能给出的最好结论是：从 RSA 公钥计算 RSA 私钥（即由 $N$ 和 $e$ 计算 $d$）与因子分解一样难。我们先证明一个稍微更强的结果。

THEOREM 9.50 Fix $N$, and assume there is a subroutine that, given $x \in \mathbb{Z}_N^*$, outputs an integer $k > 0$ with $x^k = 1 \mod N$. Then there is an algorithm that finds a factor of $N$ in time $\mathsf{poly}(\|N\|)$ (counting each call to the subroutine as one step), except with probability negligible in $\|N\|$.

定理 9.50　固定 $N$，并假设存在一个子程序：给定 $x \in \mathbb{Z}_N^*$，输出满足 $x^k = 1 \mod N$ 的整数 $k > 0$。那么存在一个算法能在时间 $\mathsf{poly}(\|N\|)$ 内找到 $N$ 的一个因子（每次调用子程序记为一步），除关于 $\|N\|$ 可忽略的概率外成立。

PROOF For simplicity (and because it is most relevant to cryptography) we focus on factoring $N$ that are a product of two distinct, odd primes $p$ and $q$. We use the Chinese remainder theorem (Section 9.1.5), and rely on Proposition 9.36 and Lemma 9.37 as well as the following facts (which follow from more-general results proved in Sections 15.4.2 and 15.5.2):

证明　为简单起见（也因为这与密码学的关联最密切），我们专注于分解形如两个不同奇素数 $p$ 与 $q$ 之积的 $N$。我们要用到中国剩余定理（9.1.5 节）、命题 9.36 与引理 9.37，以及以下事实（它们可由 15.4.2 节和 15.5.2 节证明的更一般的结果推出）：

For $N$ of the above form, 1 has exactly four square roots modulo $N$. Two of these are the “trivial” square roots $\left[\pm1 \bmod N\right]$, and two of these are “nontrivial” square roots. In the Chinese remainder representation, the nontrivial square roots are $(1, -1)$ and $(-1, 1)$.

对上述形式的 $N$，1 模 $N$ 恰好有四个平方根。其中两个是“平凡”平方根 $\left[\pm1 \bmod N\right]$，另外两个是“非平凡”平方根。在中国剩余表示下，非平凡平方根是 $(1, -1)$ 和 $(-1, 1)$。

- Any nontrivial square root of 1 can be used to (efficiently) compute a factor of N. This is by virtue of the fact that $y^{2}=1 \bmod N$ implies

  任何 1 的非平凡平方根都可以用来（高效地）计算 $N$ 的一个因子。理由如下：$y^{2}=1 \bmod N$ 蕴含

$$
{0}=y^{2}-1=(y-1)(y+1)\bmod N,
$$

and so $N|(y-1)(y+1)$. However, $N\nmid(y-1)$ and $N\nmid(y+1)$ because $y\neq\pm1$ mod $N$. So it must be the case that $\gcd(y-1,N)$ is equal to one of the prime factors of $N$.

于是 $N|(y-1)(y+1)$。但由于 $y\neq\pm1$ mod $N$，有 $N\nmid(y-1)$ 且 $N\nmid(y+1)$。所以必然有：$\gcd(y-1,N)$ 等于 $N$ 的某个素因子。

We use the following strategy to factor $N$: repeatedly choose a uniform $x \in \mathbb{Z}_N^*$, compute $k > 0$ with $x^k = 1 \bmod N$ (using the assumed subroutine for doing so), write $k = 2^s \cdot v$ for $v$ an odd integer, and compute the sequence

我们采用如下策略分解 $N$：反复均匀选取 $x \in \mathbb{Z}_N^*$，计算满足 $x^k = 1 \bmod N$ 的 $k > 0$（使用假设存在的子程序来完成），把 $k$ 写成 $k = 2^s \cdot v$（其中 $v$ 为奇整数），并计算序列

$$
x^{v},~x^{2v},~\ldots,~x^{2^{s}v}
$$

modulo $N$. Each term in this sequence is the square of the preceding term, and the final term is 1. Let $j$ be largest with $y \stackrel{\mathrm{def}}{=} [x^{2^{j}v} \bmod N] \neq 1$. (If there is no such $j$, then start again by choosing another $x$.) By choice of $j$, we have $y^{2}=1\bmod N$. If $y\neq-1\bmod N$ we have found a nontrivial square root of $N$, and can then factor $N$ as discussed earlier. All the above can be done in polynomial time, and so it only remains to determine the probability, over choice of $x$, that $y$ exists and is a nontrivial square root of $N$.

（各项均模 $N$。）序列中每一项都是前一项的平方，最后一项为 1。令 $j$ 为最大的下标使得 $y \stackrel{\mathrm{def}}{=} [x^{2^{j}v} \bmod N] \neq 1$。（若不存在这样的 $j$，则重新选取另一个 $x$ 从头再来。）由 $j$ 的取法可知 $y^{2}=1\bmod N$。若 $y\neq-1\bmod N$，我们就找到了 $N$ 的一个非平凡平方根，随后便可像前面讨论的那样分解 $N$。以上步骤都能在多项式时间内完成，剩下的只是要确定：在 $x$ 的随机选取下，“$y$ 存在且是 $N$ 的非平凡平方根”的概率。

We first observe that the probability that the sequence constructed above contains a nontrivial square root of 1 indeed depends only on $x$, and not on $k$. To see this, fix $x$ and let $\lambda$ be the smallest positive integer for which $x^{\lambda} = 1 \mod N$. Write $\lambda = 2^{\alpha} \cdot \beta$ with $\beta$ odd, and assume there is a $j \geq 0$ for which $[x^{2^{j} \beta} \mod N]$ is a nontrivial square root of 1. Without loss of generality, assume $x^{2^{j} \beta} \leftrightarrow (-1, 1)$. Now take any $k > 0$ for which $x^k = 1 \mod N$, and write $k = 2^s \cdot v$ as before. Since $k$ must be a multiple of $\lambda$, we have $v = \beta \cdot \gamma$ for some odd $\gamma$. But then $x^{2^{j} v} = x^{2^{j} \beta \gamma} \leftrightarrow (-1, 1)^{\gamma} = (-1, 1)$, and so $[x^{2^{j} v} \mod N]$ is a nontrivial square root of $N$. A similar argument shows that the implication goes in the other direction as well.

我们首先观察到，上面构造的序列包含 1 的非平凡平方根的概率确实只取决于 $x$，而与 $k$ 无关。为看清这一点，固定 $x$，令 $\lambda$ 为使 $x^{\lambda} = 1 \mod N$ 的最小正整数。把 $\lambda$ 写成 $\lambda = 2^{\alpha} \cdot \beta$（其中 $\beta$ 为奇数），并假设存在 $j \geq 0$ 使得 $[x^{2^{j} \beta} \mod N]$ 是 1 的非平凡平方根。不失一般性，设 $x^{2^{j} \beta} \leftrightarrow (-1, 1)$。现在任取满足 $x^k = 1 \mod N$ 的 $k > 0$，并照旧把 $k$ 写成 $k = 2^s \cdot v$。由于 $k$ 必是 $\lambda$ 的倍数，故有 $v = \beta \cdot \gamma$，其中 $\gamma$ 为奇数。于是 $x^{2^{j} v} = x^{2^{j} \beta \gamma} \leftrightarrow (-1, 1)^{\gamma} = (-1, 1)$，从而 $[x^{2^{j} v} \mod N]$ 是 $N$ 的非平凡平方根。类似的论证也可说明该蕴含关系在另一方向同样成立。

Let $\phi(N) = 2^r \cdot u$ with $u$ odd. We know that $x^{\phi(N)} = x^{2^r u} = 1 \bmod N$ for all $x \in \mathbb{Z}_N^*$. Let $i \in \{0, \ldots, r-1\}$ be the largest integer for which there exists an $x \in \mathbb{Z}_N^*$ such that $x^{2^i u} \neq 1 \bmod N$. (Since $u$ is odd $(-1)^u = -1 \neq 1 \bmod N$, and so the definition is not vacuous.) Then for all $x \in \mathbb{Z}_N^*$, we have $x^{2^{i+1} u} = 1 \bmod N$ and so $[x^{2^i u} \bmod N]$ is a square root of 1. Define

令 $\phi(N) = 2^r \cdot u$，其中 $u$ 为奇数。对任意 $x \in \mathbb{Z}_N^*$，都有 $x^{\phi(N)} = x^{2^r u} = 1 \bmod N$。令 $i \in \{0, \ldots, r-1\}$ 为最大的整数，使得存在 $x \in \mathbb{Z}_N^*$ 满足 $x^{2^i u} \neq 1 \bmod N$。（由于 $u$ 是奇数，有 $(-1)^u = -1 \neq 1 \bmod N$，所以这一定义并非虚设。）那么对所有 $x \in \mathbb{Z}_N^*$ 都有 $x^{2^{i+1} u} = 1 \bmod N$，故 $[x^{2^i u} \bmod N]$ 是 1 的平方根。定义

$$
\mathsf{Bad}\stackrel{\mathrm{def}}{=}\{x\mid x^{2^{i}u}=\pm1\bmod N\}.
$$

By the argument above, we know that if our algorithm chooses $x \notin \mathsf{Bad}$ then it finds a nontrivial square root of 1. We show that $\mathsf{Bad}$ is a strict subgroup of $\mathbb{Z}_N^*$; by Lemma 9.37, this implies $|\mathsf{Bad}| \leq |\mathbb{Z}_N^*|/2$. This means that $x \notin \mathsf{Bad}$ (and the algorithm factors $N$) with probability at least ${1}/{2}$ in each iteration. Using sufficiently many iterations gives the result of the theorem.

由上面的论证可知，若算法选到的 $x \notin \mathsf{Bad}$，它就能找到 1 的非平凡平方根。我们来证明 $\mathsf{Bad}$ 是 $\mathbb{Z}_N^*$ 的真子群；由引理 9.37，这意味着 $|\mathsf{Bad}| \leq |\mathbb{Z}_N^*|/2$。也就是说，每一次迭代中 $x \notin \mathsf{Bad}$（从而算法成功分解 $N$）的概率至少为 ${1}/{2}$。迭代足够多次即得定理结论。

We now prove that Bad is a strict subgroup of $\mathbb{Z}_N^*$. If $x, x^{\prime} \in \mathsf{Bad}$ then

现在证明 $\mathsf{Bad}$ 是 $\mathbb{Z}_N^*$ 的真子群。若 $x, x^{\prime} \in \mathsf{Bad}$，则

$$
(x x^{\prime})^{2^{i}u}=x^{2^{i}u}(x^{\prime})^{2^{i}u}=(\pm1)\cdot(\pm1)=\pm1\bmod N,
$$

and so $xx^{\prime} \in \mathsf{Bad}$ and $\mathsf{Bad}$ is a subgroup. To see that $\mathsf{Bad}$ is a strict subgroup, let $x \in \mathbb{Z}_N^*$ be such that $x^{2^iu} \neq 1 \mod N$ (such as an $x$ must exist by our definition of $i$). If $x^{2^iu} \neq -1 \mod N$, then $x \notin \mathsf{Bad}$ and we are done. Otherwise, let $x \leftrightarrow (x_p, x_q)$ be the Chinese remainder representation of $x$. Since $x^{2^iu} = -1 \mod N$, we know that

故 $xx^{\prime} \in \mathsf{Bad}$，$\mathsf{Bad}$ 是子群。为说明 $\mathsf{Bad}$ 还是真子群，取 $x \in \mathbb{Z}_N^*$ 使 $x^{2^iu} \neq 1 \mod N$（由我们对 $i$ 的定义可知这样的 $x$ 必然存在）。若 $x^{2^iu} \neq -1 \mod N$，则 $x \notin \mathsf{Bad}$，证毕。否则，设 $x \leftrightarrow (x_p, x_q)$ 为 $x$ 的中国剩余表示。由于 $x^{2^iu} = -1 \mod N$，可知

$$
(x_{p},x_{q})^{2^{i}u}=(x_{p}^{2^{i}u},x_{q}^{2^{i}u})=(-1,-1)\leftrightarrow-1.
$$

But then the element corresponding to $(x_{p},1)$ is not in Bad since

但这样一来，与 $(x_{p},1)$ 对应的元素就不在 $\mathsf{Bad}$ 中，因为

$$
(x_{p},1)^{2^{i}u}=(x_{p}^{2^{i}u},1)=(-1,1)\not\leftrightarrow\pm1.
$$

This completes the proof.

证明完毕。

COROLLARY 9.51 There is a probabilistic polynomial-time algorithm that, given as input an integer $N$ and integers $e,d$ with $ed=1\bmod\phi(N)$, factors $N$ except with probability negligible in $\|N\|$.

推论 9.51　存在一个概率多项式时间算法：给定整数 $N$ 以及满足 $ed=1\bmod\phi(N)$ 的整数 $e,d$ 作为输入，除关于 $\|N\|$ 可忽略的概率外，它能分解 $N$。

PROOF Let $k = ed - 1 > 0$ and note that $\phi(N) | k$. Since $x^k = 1 \bmod N$ for all $x \in \mathbb{Z}_N^*$ (cf. Corollary 9.21), we can trivially implement the subroutine needed by the previous theorem by always outputting $k$.

证明　令 $k = ed - 1 > 0$，并注意 $\phi(N) | k$。由于对所有 $x \in \mathbb{Z}_N^*$ 都有 $x^k = 1 \bmod N$（参见推论 9.21），只需总是输出 $k$，便能轻而易举地实现上一条定理所需的子程序。

Assuming factoring is hard, the above result rules out the possibility of efficiently solving the RSA problem by first computing $d$ from $N$ and $e$. However, it does not rule out the possibility that there might be some completely different way of attacking the RSA problem that does not involve (or imply) factoring $N$. Thus, based on our current knowledge, the RSA assumption is stronger than the factoring assumption—that is, it may be that the RSA problem can be solved in polynomial time even though factoring cannot. Nevertheless, when GenRSA is constructed based on GenModulus as in Algorithm 9.47, the prevailing conjecture is that the RSA problem is hard relative to GenRSA whenever factoring is hard relative to GenModulus.

在假设因子分解是困难的前提下，上述结果排除了“先由 $N$ 和 $e$ 算出 $d$、进而高效求解 RSA 问题”的可能性。但它并没有排除另一种可能：也许存在某种完全不同的攻击 RSA 问题的途径，既不涉及也不蕴含分解 $N$。因此，就现有的知识而言，RSA 假设强于因子分解假设——也就是说，有可能 RSA 问题可以在多项式时间内求解，而因子分解却不能。不过，当 $\mathsf{GenRSA}$ 像算法 9.47 那样基于 $\mathsf{GenModulus}$ 构造时，主流的猜想是：只要因子分解相对于 $\mathsf{GenModulus}$ 是困难的，RSA 问题相对于 $\mathsf{GenRSA}$ 就是困难的。
