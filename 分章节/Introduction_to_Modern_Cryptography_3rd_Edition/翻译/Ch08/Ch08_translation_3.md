## 8.6 Constructing (Strong) Pseudorandom Permutations　（强）伪随机置换的构造

We next show how pseudorandom permutations and strong pseudorandom permutations can be constructed from any pseudorandom function. Recall from Section 3.5.1 that a pseudorandom permutation is a pseudorandom function that is also efficiently invertible, while a strong pseudorandom permutation is additionally hard to distinguish from a random permutation even by an adversary given oracle access to both the permutation and its inverse.

接下来我们展示如何从任意伪随机函数构造伪随机置换与强伪随机置换。回顾 3.5.1 节的内容：伪随机置换是同时还能够高效求逆的伪随机函数，而强伪随机置换更进一步——即使敌手同时获得对该置换及其逆的预言机访问，也难以把它与随机置换区分开。

Feistel networks revisited. A Feistel network, introduced in Section 7.2.2, provides a way of constructing an efficiently invertible permutation from an arbitrary set of functions. A Feistel network operates in a series of rounds. The input to the $i$th round is a string of length ${2}n$, divided into two $n$-bit halves $L_{i-1}$ and $R_{i-1}$ (the “left half” and the “right half,” respectively). The output of the $i$th round is the ${2}n$-bit string $(L_i, R_i)$, where

**再谈 Feistel 网络。**

7.2.2 节介绍过 Feistel 网络，它提供了一种从任意一组函数出发构造可高效求逆的置换的方法。Feistel 网络以一系列轮次运作。第 $i$ 轮的输入是长度 ${2}n$ 的串，被分成两个 $n$ 比特的一半 $L_{i-1}$ 与 $R_{i-1}$（分别为“左半”与“右半”）。第 $i$ 轮的输出是 ${2}n$ 比特串 $(L_i, R_i)$，其中

$$
L_{i}:=R_{i-1}\quad\text{and}\quad R_{i}:=L_{i-1}\oplus f_{i}(R_{i-1})
$$

for some efficiently computable (but not necessarily invertible) function $f_i$ mapping $n$-bit inputs to $n$-bit outputs. We denote by $\mathsf{Feistel}_{f_1,\ldots,f_r}$ the $r$-round Feistel network using functions $f_1,\ldots,f_r$. (That is, $\mathsf{Feistel}_{f_1,\ldots,f_r}(L_0,R_0)$ outputs the ${2}n$-bit string $(L_r,R_r)$.) We saw in Section 7.2.2 that $\mathsf{Feistel}_{f_1,\ldots,f_r}$ is an efficiently invertible permutation regardless of the $\{f_i\}$.

其中 $f_i$ 是某个可高效计算（但不一定可逆）的、把 $n$ 比特输入映射为 $n$ 比特输出的函数。我们把使用函数 $f_1,dots,f_r$ 的 $r$ 轮 Feistel 网络记作 $\mathsf{Feistel}_{f_1,\ldots,f_r}$。（也就是说，$\mathsf{Feistel}_{f_1,\ldots,f_r}(L_0,R_0)$ 输出 ${2}n$ 比特串 $(L_r,R_r)$。）我们在 7.2.2 节已经看到：无论 $\{f_i\}$ 如何取，$\mathsf{Feistel}_{f_1,\ldots,f_r}$ 都是可高效求逆的置换。

We can define a keyed permutation by using a Feistel network in which the $\{f_i\}$ depend on a key. For example, let $F : \{0,1\}^n \times \{0,1\}^n \to \{0,1\}^n$ be a pseudorandom function, and define the keyed permutation $F^{(1)}$ as

我们可以借助 $\{f_i\}$ 依赖于密钥的 Feistel 网络来定义带密钥的置换。例如，设 $F : \{0,1\}^n \times \{0,1\}^n \to \{0,1\}^n$ 是一个伪随机函数，并如下定义带密钥置换 $F^{(1)}$：

$$
F_{k}^{(1)}(x)\stackrel{\mathrm{def}}{=}\mathsf{Feistel}_{F_{k}}(x).
$$

(Note that $F_k^{(1)}$ has an n-bit key and maps 2n-bit inputs to 2n-bit outputs.) Is $F^{(1)}$ pseudorandom? A little thought shows that it is decidedly not. For any key $k \in \{0,1\}^n$, the first n bits of the output of $F_k^{(1)}$ (that is, $L_1$) are equal to the last n bits of the input (i.e., $R_0$), something that occurs with only negligible probability for a random permutation.

（注意 $F_k^{(1)}$ 具有 $n$ 比特的密钥，并把 ${2}n$ 比特输入映射为 ${2}n$ 比特输出。）那么 $F^{(1)}$ 是伪随机的吗？稍加思考便能发现它显然不是。对任意密钥 $k \in \{0,1\}^n$，$F_k^{(1)}$ 输出的前 $n$ 个比特（即 $L_1$）总等于输入的后 $n$ 个比特（即 $R_0$）；而对随机置换而言，这种情况发生的概率只有可忽略的量级。

Trying again, define $F^{(2)} : \{0,1\}^{2n} \times \{0,1\}^{2n} \to \{0,1\}^{2n}$ as follows:

再试一次，如下定义 $F^{(2)} : \{0,1\}^{2n} \times \{0,1\}^{2n} \to \{0,1\}^{2n}$：

$$
F_{k_{1},k_{2}}^{(2)}(x)\stackrel{\mathrm{def}}{=}\mathsf{Feistel}_{F_{k_{1}},F_{k_{2}}}(x). \tag{8.15}
$$

(Note that $k_{1}$ and $k_{2}$ are independent keys.) Unfortunately, $F^{(2)}$ is not pseudorandom either, as you are asked to show in Exercise 8.16.

（注意 $k_{1}$ 与 $k_{2}$ 是相互独立的密钥。）遗憾的是，$F^{(2)}$ 同样不是伪随机的，习题 8.16 将请你证明这一点。

Given this, it may be somewhat surprising that a three-round Feistel network is pseudorandom. Define the keyed permutation $F^{(3)}$, taking a key of length 3n and mapping 2n-bit inputs to 2n-bit outputs, as follows:

有鉴于此，三轮 Feistel 网络竟然是伪随机的，这多少有些出人意料。如下定义带密钥置换 $F^{(3)}$，它取长度为 ${3}n$ 的密钥，把 ${2}n$ 比特输入映射为 ${2}n$ 比特输出：

$$
F_{k_{1},k_{2},k_{3}}^{(3)}(x)\stackrel{\mathrm{def}}{=}\mathsf{Feistel}_{F_{k_{1}},F_{k_{2}},F_{k_{3}}}(x) \tag{8.16}
$$

where, once again, $k_{1}, k_{2}$, and $k_{3}$ are independent. We have:

其中 $k_{1}, k_{2}$ 与 $k_{3}$ 同样相互独立。我们有：

THEOREM 8.22 If F is a pseudorandom function, then $F^{(3)}$ is a pseudorandom permutation.

定理 8.22　若 $F$ 是伪随机函数，则 $F^{(3)}$ 是伪随机置换。

PROOF In the standard way, we can replace the pseudorandom functions used in the construction of $F^{(3)}$ with functions chosen uniformly at random

证明　按标准做法，我们可以把构造 $F^{(3)}$ 时所用的那些伪随机函数替换成均匀随机选取的函数

![Image](https://lsky.jerryxue.top/i/2026/08/22/6a88f9eb6384a.jpg)

**FIGURE 8.3: A three-round Feistel network, as used to construct a pseudorandom permutation from a pseudorandom function. / 图 8.3：用于从伪随机函数构造伪随机置换的三轮 Feistel 网络**

instead. Pseudorandomness of $F$ implies that this has only a negligible effect on the output of any probabilistic polynomial-time distinguisher interacting with $F^{(3)}$ as an oracle. We leave the details as an exercise.

来代替。$F$ 的伪随机性保证：这一替换对任何与 $F^{(3)}$ 进行预言机交互的概率多项式时间区分器的输出仅有可忽略的影响。细节留作习题。

Let D be a probabilistic polynomial-time distinguisher. In the remainder of the proof, we show the following is negligible:

设 $D$ 是一个概率多项式时间区分器。在证明的余下部分，我们证明下式是可忽略的：

$$
\left|\Pr[D^{\mathsf{Feistel}_{f_{1},f_{2},f_{3}}(\cdot)}(1^{n})=1]-\Pr[D^{\pi(\cdot)}(1^{n})=1]\right|,
$$

where the first probability is taken over uniform and independent choice of $f_1, f_2, f_3$ from $\mathsf{Func}_n$, and the second probability is taken over uniform choice of $\pi$ from $\mathsf{Perm}_{2n}$. Fix some value for the security parameter $n$, and let $q = q(n)$ denote a polynomial upper bound on the number of oracle queries made by $D$. We assume without loss of generality that $D$ never makes the same oracle query twice. Focusing on $D$'s interaction with $\mathsf{Feistel}_{f_1, f_2, f_3}(\cdot)$, let $(L_0^i, R_0^i)$ denote the $i$th query $D$ makes to its oracle, and let $(L_1^i, R_1^i)$, $(L_2^i, R_2^i)$, and $(L_3^i, R_3^i)$ denote the intermediate values after rounds 1, 2, and 3, respectively, that result from that query. (See Figure 8.3.) Note that $D$ chooses $(L_0^i, R_0^i)$ and sees the result $(L_3^i, R_3^i)$, but does not directly observe $(L_1^i, R_1^i)$ or $(L_2^i, R_2^i)$.

其中第一个概率是对从 $\mathsf{Func}_n$ 中独立、均匀选取的 $f_1, f_2, f_3$ 而取，第二个概率是对从 $\mathsf{Perm}_{2n}$ 中均匀选取的 $\pi$ 而取。固定安全参数 $n$ 的某个取值，令 $q = q(n)$ 表示 $D$ 所做预言机查询次数的多项式上界。不失一般性，假设 $D$ 从不会对同一预言机查询发起两次。聚焦 D 与 $\mathsf{Feistel}_{f_1, f_2, f_3}(\cdot)$ 的交互：令 $(L_0^i, R_0^i)$ 表示 $D$ 对其预言机的第 $i$ 次查询，并令 $(L_1^i, R_1^i)$、$(L_2^i, R_2^i)$ 与 $(L_3^i, R_3^i)$ 分别表示由这次查询产生的第 1、2、3 轮之后的中间值。（见图 8.3。）注意：$D$ 自己选择 $(L_0^i, R_0^i)$ 并看到结果 $(L_3^i, R_3^i)$，但它并不直接观察到 $(L_1^i, R_1^i)$ 或 $(L_2^i, R_2^i)$。

We say there is a collision at $R_1$ if $R_1^i = R_1^j$ for some distinct $i, j$. We first prove that a collision at $R_1$ occurs with only negligible probability. Consider any fixed, distinct $i, j$. If $R_0^i = R_0^j$ then $L_0^i \neq L_0^j$, but then

如果对某两个不同的 $i, j$ 有 $R_1^i = R_1^j$，我们就说在 $R_1$ 处发生了一次碰撞。我们首先证明：在 $R_1$ 处发生碰撞的概率是可忽略的。考虑任意固定的一对不同 $i, j$。若 $R_0^i = R_0^j$，则 $L_0^i \neq L_0^j$，于是

$$
R_{1}^{i}=L_{0}^{i}\oplus f_{1}(R_{0}^{i})\neq L_{0}^{j}\oplus f_{1}(R_{0}^{j})=R_{1}^{j}.
$$

If $R_{0}^{i} \neq R_{0}^{j}$ then $f_{1}(R_{0}^{i})$ and $f_{1}(R_{0}^{j})$ are uniform and independent, so

若 $R_{0}^{i} \neq R_{0}^{j}$，则 $f_{1}(R_{0}^{i})$ 与 $f_{1}(R_{0}^{j})$ 均匀且独立，因此

$$
\Pr[R_{1}^{i}=R_{1}^{j}]=\Pr\left[f_{1}(R_{0}^{j})=L_{0}^{i}\oplus f_{1}(R_{0}^{i})\oplus L_{0}^{j}\right]=2^{-n}.
$$

Taking a union bound over all distinct $i,j$ shows that the probability of a collision at $R_1$ is at most $q^2/2^n$.

对所有不同的 $i, j$ 取联合界可知，在 $R_1$ 处发生碰撞的概率至多为 $q^2/2^n$。

Say there is a collision at $R_2$ if $R_2^i = R_2^j$ for some distinct $i, j$. We prove that conditioned on no collision at $R_1$, the probability of a collision at $R_2$ is negligible. The analysis is as above: consider any fixed $i, j$, and note that if there is no collision at $R_1$ then $R_1^i \neq R_1^j$. Thus $f_2(R_1^i)$ and $f_2(R_1^j)$ are uniform and independent, and therefore

如果对某两个不同的 $i, j$ 有 $R_2^i = R_2^j$，我们就说在 $R_2$ 处发生了一次碰撞。我们证明：在 $R_1$ 处没有碰撞的条件下，$R_2$ 处发生碰撞的概率可忽略。分析与上面一样：考虑任意固定的 $i, j$，注意若 $R_1$ 处没有碰撞则 $R_1^i \neq R_1^j$。于是 $f_2(R_1^i)$ 与 $f_2(R_1^j)$ 均匀且独立，因此

$$
\Pr\left[L_{1}^{i}\oplus f_{2}(R_{1}^{i})=L_{1}^{j}\oplus f_{2}(R_{1}^{j})\mid\text{no collision at }R_{1}\right]=2^{-n}.
$$

(Note that $f_{2}$ is independent of $f_{1}$, making the above calculation easy.) Taking a union bound over all distinct i, j gives

（注意 $f_{2}$ 与 $f_{1}$ 相互独立，这让上述计算变得容易。）对所有不同的 $i, j$ 取联合界可得

$$
\Pr[\text{collision at }R_{2}\mid\text{no collision at }R_{1}]\leq q^{2}/2^{n}.
$$

Note that $L_3^i = R_2^i = L_1^i \oplus f_2(R_1^i)$; so, conditioned on there being no collision at $R_1$, the values $L_3^1, \ldots, L_3^q$ are all independent and uniformly distributed in $\{0,1\}^n$. If we additionally condition on the event that there is no collision at $R_2$, then the values $L_3^1, \ldots, L_3^q$ are uniformly distributed among all sequences of $q$ distinct values in $\{0,1\}^n$. Similarly, $R_3^i = L_2^i \oplus f_3(R_2^i)$; thus, conditioned on there being no collision at $R_2$, the values $R_3^1, \ldots, R_3^q$ are all uniformly distributed in $\{0,1\}^n$, independent of each other as well as $L_3^1, \ldots, L_3^q$.

注意 $L_3^i = R_2^i = L_1^i \oplus f_2(R_1^i)$；因此在 $R_1$ 处没有碰撞的条件下，值 $L_3^1, \ldots, L_3^q$ 彼此独立且在 $\{0,1\}^n$ 中均匀分布。如果我们再附加“$R_2$ 处没有碰撞”这一条件，那么值 $L_3^1, \ldots, L_3^q$ 就在 $\{0,1\}^n$ 中所有由 $q$ 个互不相同值构成的序列中均匀分布。类似地，$R_3^i = L_2^i \oplus f_3(R_2^i)$；因此在 $R_2$ 处没有碰撞的条件下，值 $R_3^1, \ldots, R_3^q$ 都在 $\{0,1\}^n$ 中均匀分布，它们彼此独立，并且与 $L_3^1, \ldots, L_3^q$ 也独立。

To summarize: when querying $F^{(3)}$ (with uniform round functions) on a series of $q$ distinct inputs, except with negligible probability the output values $(L_3^1, R_3^1), \ldots, (L_3^q, R_3^q)$ are distributed such that the $\{L_3^i\}$ are uniform and independent, but distinct, $n$-bit values, and the $\{R_3^i\}$ are uniform and independent $n$-bit values. In contrast, when querying a random permutation on a series of $q$ distinct inputs, the output values $(L_3^1, R_3^1), \ldots, (L_3^q, R_3^q)$ are uniform and independent, but distinct, ${2}n$-bit values. It can be shown that the best distinguishing attack for $D$, then, is to guess that it is interacting with a random permutation if $L_3^i = L_3^j$ for some distinct $i, j$. But that event occurs with negligible probability even in that case.

总结一下：用 $F^{(3)}$（轮函数均匀）在一列 $q$ 个互不相同的输入上进行查询时，除可忽略的概率外，输出值 $(L_3^1, R_3^1), \ldots, (L_3^q, R_3^q)$ 的分布满足：$\{L_3^i\}$ 是均匀、独立但互不相同的 $n$ 比特值，而 $\{R_3^i\}$ 是均匀、独立的 $n$ 比特值。相比之下，用随机置换在一列 $q$ 个互不相同的输入上进行查询时，输出值 $(L_3^1, R_3^1), \ldots, (L_3^q, R_3^q)$ 是均匀、独立但互不相同的 ${2}n$ 比特值。可以证明：此时对 $D$ 而言最佳的区分攻击是——当存在不同 $i, j$ 使 $L_3^i = L_3^j$ 时，猜测自己正在与随机置换交互。但即便在这种情况下，该事件发生的概率也是可忽略的。

 $F^{(3)}$ is not a strong pseudorandom permutation, as you are asked to demonstrate in Exercise 8.17. Fortunately, adding a fourth round does yield a strong pseudorandom permutation. The details are given as Construction 8.23.

 $F^{(3)}$ 并不是强伪随机置换，习题 8.17 将请你证明这一点。幸运的是，增加第四轮确实能得到强伪随机置换。具体内容见构造 8.23。

THEOREM 8.24 If F is a pseudorandom function, then Construction 8.23 is a strong pseudorandom permutation that maps 2n-bit inputs to 2n-bit outputs (and uses a 4n-bit key).

定理 8.24　若 $F$ 是伪随机函数，则构造 8.23 是把 ${2}n$ 比特输入映射为 ${2}n$ 比特输出的强伪随机置换（并使用 4n 比特的密钥）。

**CONSTRUCTION 8.23**

**构造 8.23**

Let F be a keyed, length-preserving function. Define the keyed permutation $F^{(4)}$ as follows:

设 $F$ 是一个带密钥的保长度函数。如下定义带密钥置换 $F^{(4)}$：

Inputs: A key $k = (k_1, k_2, k_3, k_4)$ with $|k_i| = n$, and an input $x \in \{0,1\}^{2n}$ parsed as $(L_0, R_0)$ with $|L_0| = |R_0| = n$.

输入：密钥 $k = (k_1, k_2, k_3, k_4)$（其中 $|k_i| = n$），以及输入 $x \in \{0,1\}^{2n}$，将 $x$ 解析为 $(L_0, R_0)$（$|L_0| = |R_0| = n$）。

Computation:

计算：

1. Compute $L_1 := R_0$ and $R_1 := L_0 \oplus F_{k_1}(R_0)$.

   计算 $L_1 := R_0$ 与 $R_1 := L_0 \oplus F_{k_1}(R_0)$。

2. Compute $L_2 := R_1$ and $R_2 := L_1 \oplus F_{k_2}(R_1)$.

   计算 $L_2 := R_1$ 与 $R_2 := L_1 \oplus F_{k_2}(R_1)$。

3. Compute $L_3 := R_2$ and $R_3 := L_2 \oplus F_{k_3}(R_2)$.

   计算 $L_3 := R_2$ 与 $R_3 := L_2 \oplus F_{k_3}(R_2)$。

4. Compute $L_4 := R_3$ and $R_4 := L_3 \oplus F_{k_4}(R_3)$.

   计算 $L_4 := R_3$ 与 $R_4 := L_3 \oplus F_{k_4}(R_3)$。

5. Output $(L_{4}, R_{4})$

   输出 $(L_{4}, R_{4})$

A strong pseudorandom permutation from any pseudorandom function.

从任意伪随机函数构造强伪随机置换。

## 8.7 Assumptions for Private-Key Cryptography　私钥密码学的假设

We have shown that (1) if there exist one-way permutations, then there exist pseudorandom generators; (2) if there exist pseudorandom generators, then there exist pseudorandom functions; and (3) if there exist pseudorandom functions, then there exist (strong) pseudorandom permutations. Although we did not prove it here, it is possible to construct pseudorandom generators from one-way functions. We thus have the following fundamental theorem:

我们已经证明：(1) 若存在单向置换，则存在伪随机生成器；(2) 若存在伪随机生成器，则存在伪随机函数；(3) 若存在伪随机函数，则存在（强）伪随机置换。虽然本书并未在此处证明，但从单向函数出发构造伪随机生成器同样是可能的。于是我们有如下基本定理：

THEOREM 8.25 If one-way functions exist, then so do pseudorandom generators, pseudorandom functions, and strong pseudorandom permutations.

定理 8.25　若单向函数存在，则伪随机生成器、伪随机函数与强伪随机置换也存在。

All the private-key schemes we have studied in Chapters 3–5 can be constructed from pseudorandom generators/functions. We therefore have:

我们在第 3–5 章中研究过的所有私钥方案都可以由伪随机生成器/函数构造出来。因此我们有：

THEOREM 8.26 If one-way functions exist, then so do authenticated encryption schemes and secure message authentication codes.

定理 8.26　若单向函数存在，则认证加密方案与安全的消息认证码也存在。

That is, one-way functions are sufficient for all private-key cryptography. Here, we show that one-way functions are also necessary.

也就是说，单向函数足以支撑全部私钥密码学。在这里，我们要证明单向函数也是必要的。

Pseudorandomness implies one-way functions. We begin by showing that pseudorandom generators imply the existence of one-way functions:

**伪随机性蕴含单向函数。**

我们首先证明：伪随机生成器蕴含单向函数的存在。

PROPOSITION 8.27 If a pseudorandom generator exists, then so do one-way functions.

命题 8.27　若伪随机生成器存在，则单向函数也存在。

PROOF Let $G$ be a pseudorandom generator with expansion factor $\ell(n) = 2n$. (By Theorem 8.19, we know that the existence of a pseudorandom generator implies the existence of one with this expansion factor.) We show that $G$ itself is one-way. Efficient computability is straightforward (since $G$ can be computed in polynomial time). We show that the ability to invert $G$ can be translated into the ability to distinguish the output of $G$ from uniform. Intuitively, this holds because the ability to invert $G$ implies the ability to find the seed used by the generator.

证明　设 $G$ 是扩展因子为 $\ell(n) = 2n$ 的伪随机生成器。（由定理 8.19 可知，伪随机生成器的存在性蕴含具有这一扩展因子的伪随机生成器的存在性。）我们证明 $G$ 本身就是单向的。可高效计算性一目了然（因为 $G$ 可以在多项式时间内计算）。我们要展示的是：对 $G$ 求逆的能力可以转化为区分 $G$ 的输出与均匀串的能力。直观地说，这是因为能对 $G$ 求逆就意味着能找到生成器所用的种子。

Let $\mathcal{A}$ be an arbitrary probabilistic polynomial-time algorithm. We show that $\Pr[\mathsf{Invert}_{\mathcal{A},G}(n)=1]$ is negligible (cf. Definition 8.1). To see this, consider the following PPT distinguisher $D$: on input a string $w\in\{0,1\}^{2n}$, run $\mathcal{A}(w)$ to obtain output $s$. If $G(s)=w$ then output 1; otherwise, output 0.

设 $\mathcal{A}$ 是任意的概率多项式时间算法。我们证明 $\Pr[\mathsf{Invert}_{\mathcal{A},G}(n)=1]$ 可忽略（参见定义 8.1）。为此，考虑如下的 PPT 区分器 $D$：当输入串 $w\in\{0,1\}^{2n}$ 时，运行 $\mathcal{A}(w)$ 得到输出 $s$；若 $G(s)=w$ 则输出 1，否则输出 0。

We now analyze the behavior of $D$. First consider the probability that $D$ outputs 1 when its input string $w$ is uniform. Since there are at most ${2}^n$ values in the range of $G$ (namely, the values $\{G(s)\}_{s\in\{0,1\}^n}$), the probability that $w$ is in the range of $G$ is at most ${2}^n/{2}^{2n} = {2}^{-n}$. When $w$ is not in the range of $G$, it is impossible for $\mathcal{A}$ to compute an inverse of $w$ and thus impossible for $D$ to output 1. We conclude that $\Pr_{w\leftarrow\{0,1\}^{2n}}[D(w) = 1] \leq 2^{-n}$.

现在来分析 $D$ 的行为。先考虑 $D$ 在输入串 $w$ 均匀时输出 1 的概率。由于 $G$ 的值域中至多有 ${2}^n$ 个值（也就是 $\{G(s)\}_{s\in\{0,1\}^n}$ 这些值），$w$ 落在 $G$ 值域中的概率至多为 ${2}^n/{2}^{2n} = {2}^{-n}$。当 $w$ 不在 $G$ 的值域中时，$\mathcal{A}$ 不可能算出 $w$ 的逆，因而 $D$ 也不可能输出 1。我们得出 $\Pr_{w\leftarrow\{0,1\}^{2n}}[D(w) = 1] \leq 2^{-n}$。

On the other hand, if $w = G(s)$ for a seed $s \in \{0,1\}^n$ chosen uniformly at random then, by definition, $\mathcal{A}$ computes a correct inverse (and so $D$ outputs 1) with probability exactly equal to $\Pr[\mathsf{Invert}_{\mathcal{A},G}(n) = 1]$. Thus,

另一方面，若 $w = G(s)$（其中种子 $s \in \{0,1\}^n$ 均匀随机选取），那么根据定义，$\mathcal{A}$ 以恰好等于 $\Pr[\mathsf{Invert}_{\mathcal{A},G}(n) = 1]$ 的概率算出正确的逆（从而 $D$ 输出 1）。于是，

$$
\left|\Pr_{w\leftarrow\{0,1\}^{2n}}[D(w)=1]-\Pr_{s\leftarrow\{0,1\}^{n}}[D(G(s))=1]\right|\geq\Pr[\mathsf{Invert}_{\mathcal{A},G}(n)=1]-2^{-n}.
$$

Since $G$ is a pseudorandom generator, the above must be negligible. Since ${2}^{-n}$ is negligible, this implies that $\Pr[\mathsf{Invert}_{\mathcal{A},G}(n) = 1]$ is negligible as well and so $G$ is one-way.

由于 $G$ 是伪随机生成器，上式必定可忽略。又因 ${2}^{-n}$ 可忽略，这就蕴含 $\Pr[\mathsf{Invert}_{\mathcal{A},G}(n) = 1]$ 也可忽略，故 $G$ 是单向的。

Non-trivial private-key encryption implies one-way functions. Proposition 8.27 does not imply that one-way functions are needed for constructing secure private-key encryption schemes, since it may be possible to construct the latter without relying on a pseudorandom generator. Furthermore, it is possible to construct perfectly secret encryption schemes (see Chapter 2), as long as the plaintext is no longer than the key. Thus, a proof that secure private-key encryption implies one-way functions requires more care.

**非平凡的私钥加密蕴含单向函数。**

命题 8.27 并不意味着构造安全的私钥加密方案必须要有单向函数，因为后者或许可以在不依赖伪随机生成器的情况下构造出来。此外，只要明文不超过密钥的长度，完美保密的加密方案是可以构造出来的（见第 2 章）。因此，要证明“安全的私钥加密蕴含单向函数”，需要更加小心。

PROPOSITION 8.28 If there exists an EAV-secure private-key encryption scheme that encrypts messages twice as long as its key, then a one-way function exists.

命题 8.28　若存在 EAV 安全的私钥加密方案，它能加密长度为其密钥两倍的消息，则单向函数存在。

PROOF Let $\Pi = (\mathsf{Enc}, \mathsf{Dec})$ be a private-key encryption scheme that has indistinguishable encryptions in the presence of an eavesdropper and encrypts messages of length ${2}n$ when the key has length $n$. (We assume for simplicity that the key is chosen uniformly.) Let $\ell(n)$ be a bound on the number of random bits used by $\mathsf{Enc}$. Denote the encryption of a message $m$ using key $k$ and randomness $r$ by $\mathsf{Enc}_k(m; r)$.

证明　设 $\Pi = (\mathsf{Enc}, \mathsf{Dec})$ 是一个在窃听者面前具有不可区分加密性质的私钥加密方案，并且在密钥长度为 $n$ 时能加密长度为 ${2}n$ 的消息。（为简单起见，假设密钥是均匀选取的。）令 $\ell(n)$ 表示 $\mathsf{Enc}$ 所用随机比特数的一个上界。把用密钥 $k$ 与随机数 $r$ 对消息 $m$ 加密的结果记作 $\mathsf{Enc}_k(m; r)$。

Define the following function $f$:

定义如下函数 $f$：

$$
f(k,m,r)\stackrel{\mathrm{def}}{=}\mathsf{Enc}_{k}(m;r)\parallel m,
$$

where $|k|=n$, $|m|=2n$, and $|r|=\ell(n)$. We claim that f is a one-way function. Clearly it can be efficiently computed; we show that it is hard to invert. Letting A be an arbitrary PPT algorithm, we show that $\Pr[\mathsf{Invert}_{\mathcal{A},f}(n)=1]$ is negligible (cf. Definition 8.1).

其中 $|k|=n$，$|m|=2n$，$|r|=\ell(n)$。我们断言 $f$ 是单向函数。显然它可以被高效计算；我们要证明它难以求逆。设 $A$ 是任意的 PPT 算法，我们证明 $\Pr[\mathsf{Invert}_{\mathcal{A},f}(n)=1]$ 可忽略（参见定义 8.1）。

Consider the following probabilistic polynomial-time adversary $\mathcal{A}^{\prime}$ attacking private-key encryption scheme $\Pi$ (i.e., in experiment $\mathsf{PrivK}_{\mathcal{A}^{\prime},\Pi}^{\mathsf{eav}}(n)$):

考虑如下攻击私钥加密方案 Π 的概率多项式时间敌手 $\mathcal{A}^{\prime}$（即在实验 $\mathsf{PrivK}_{\mathcal{A}^{\prime},\Pi}^{\mathsf{eav}}(n)$ 中）：

Adversary $\mathcal{A}^{\prime}(1^{n})$

敌手 $\mathcal{A}^{\prime}(1^{n})$

1. Choose uniform $m_0, m_1 \leftarrow \{0,1\}^{2n}$ and output them. Receive in return a challenge ciphertext $c$.

   均匀选取 $m_0, m_1 \leftarrow \{0,1\}^{2n}$ 并输出它们；作为回应，收到挑战密文 $c$。

2. Run $\mathcal{A}(c \parallel m_0)$ to obtain $(k^{\prime}, m^{\prime}, r^{\prime})$. If $f(k^{\prime}, m^{\prime}, r^{\prime}) = c \parallel m_0$, output 0; else, output 1.

   运行 $\mathcal{A}(c \parallel m_0)$ 得到 $(k^{\prime}, m^{\prime}, r^{\prime})$。若 $f(k^{\prime}, m^{\prime}, r^{\prime}) = c \parallel m_0$，则输出 0；否则输出 1。

We now analyze the behavior of $\mathcal{A}^{\prime}$. When $c$ is an encryption of $m_0$, then $c\|m_0$ is distributed exactly as $f(k, m_0, r)$ for uniform $k, m_0$, and $r$. Therefore, $\mathcal{A}$ outputs a valid inverse of $c\|m_0$ (and hence $\mathcal{A}^{\prime}$ outputs 0) with probability exactly equal to $\Pr[\mathsf{Invert}_{\mathcal{A},f}(n) = 1]$.

现在分析 $\mathcal{A}^{\prime}$ 的行为。当 $c$ 是 $m_0$ 的加密结果时，$c\|m_0$ 恰好服从均匀的 $k$、$m_0$、$r$ 下 $f(k, m_0, r)$ 的分布。因此，$\mathcal{A}$ 以恰好等于 $\Pr[\mathsf{Invert}_{\mathcal{A},f}(n) = 1]$ 的概率输出 $c\|m_0$ 的一个有效逆（从而 $\mathcal{A}^{\prime}$ 输出 0）。

On the other hand, when $c$ is an encryption of $m_1$ then $c$ is independent of $m_0$. For any fixed value of the challenge ciphertext $c$, there are at most ${2}^n$ possible messages (one for each possible key) to which $c$ can correspond. Since $m_0$ is a uniform ${2}n$-bit string, the probability that there exists some key $k$ for which $\mathsf{Dec}_k(c) = m_0$ is at most ${2}^n/{2}^{2n} = {2}^{-n}$. This gives an upper bound on the probability with which $\mathcal{A}$ can possibly output a valid inverse of $c \parallel m_0$ under $f$, and hence an upper bound on the probability with which $\mathcal{A}^{\prime}$ outputs 0 in that case.

另一方面，当 $c$ 是 $m_1$ 的加密结果时，$c$ 与 $m_0$ 相互独立。对挑战密文 $c$ 的任何固定取值，$c$ 所能对应的消息至多有 ${2}^n$ 个（每个可能的密钥对应一个）。由于 m0 是均匀的 ${2}n$ 比特串，存在某个密钥 $k$ 使得 $\mathsf{Dec}_k(c) = m_0$ 的概率至多为 ${2}^n/{2}^{2n} = {2}^{-n}$。这给出了 $A$ 能够在 $f$ 下输出 $c \parallel m_0$ 的有效逆的概率上界，从而也给出了该情形下 $\mathcal{A}^{\prime}$ 输出 0 的概率上界。

Putting the above together, we have:

把上述结果合在一起，我们得到：

$$
\begin{aligned}
&\Pr\left[\mathsf{PrivK}_{\mathcal{A}^{\prime},\Pi}^{\mathsf{eav}}(n)=1\right]\\
&=\frac{1}{2}\cdot\Pr\left[\mathcal{A}^{\prime}\text{ outputs }0\mid b=0\right]+\frac{1}{2}\cdot\Pr\left[\mathcal{A}^{\prime}\text{ outputs }1\mid b=1\right]\\
&\geq\frac{1}{2}\cdot\Pr[\mathsf{Invert}_{\mathcal{A},f}(n)=1]+\frac{1}{2}\cdot\left(1-2^{-n}\right)\\
&=\frac{1}{2}+\frac{1}{2}\cdot\left(\Pr[\mathsf{Invert}_{\mathcal{A},f}(n)=1]-2^{-n}\right).
\end{aligned}
$$

Security of $\Pi$ means that $\Pr\left[\mathsf{PrivK}_{\mathcal{A}^{\prime},\Pi}^{\mathsf{eav}}(n)=1\right]\leq\frac{1}{2}+\mathsf{negl}(n)$ for some negligible function $\mathsf{negl}$. This, in turn, implies that $\Pr[\mathsf{Invert}_{\mathcal{A},f}(n)=1]$ is negligible, completing the proof that $f$ is one-way.

Π 的安全性意味着：对某个可忽略函数 $\mathsf{negl}$ 有 $\Pr\left[\mathsf{PrivK}_{\mathcal{A}^{\prime},\Pi}^{\mathsf{eav}}(n)=1\right]\leq\frac{1}{2}+\mathsf{negl}(n)$。这又蕴含 $\Pr[\mathsf{Invert}_{\mathcal{A},f}(n)=1]$ 可忽略，从而完成了“$f$ 是单向的”这一证明。

Message authentication codes imply one-way functions. It is also true that message authentication codes satisfying Definition 4.2 imply the existence of one-way functions. As in the case of private-key encryption, a proof of this fact is somewhat subtle because unconditional message authentication codes do exist when there is a bound on the number of messages that will be authenticated. (See Section 4.6.) Thus, a proof relies on the fact that Definition 4.2 requires security even when the adversary sees tags for an arbitrary (polynomial) number of messages. The proof is somewhat involved, so we do not give it here.

**消息认证码蕴含单向函数。**

满足定义 4.2 的消息认证码同样蕴含单向函数的存在。与私钥加密的情形一样，这一事实的证明有些微妙，因为当被认证的消息数量有界时，无条件安全的消息认证码确实是存在的。（见 4.6 节。）因此，证明依赖如下事实：定义 4.2 要求即使敌手看到了任意（多项式）多条消息的标签，安全性依然成立。该证明相当繁琐，此处从略。

Discussion. We conclude that the existence of one-way functions is necessary and sufficient for all (non-trivial) private-key cryptography. In other words, one-way functions are a minimal assumption as far as private-key cryptography is concerned. Interestingly, this appears not to be the case for hash functions and public-key encryption, where one-way functions are known to be necessary but are not known (or believed) to be sufficient.

**讨论。**

我们的结论是：对所有（非平凡的）私钥密码学而言，单向函数的存在性既是必要的也是充分的。换句话说，就私钥密码学而言，单向函数是一个最小假设。有趣的是，对哈希函数与公钥加密来说情况似乎并非如此：在这些领域，单向函数已被证明是必要的，但是否充分却不得而知（人们也不相信它充分）。

## 8.8 Computational Indistinguishability　计算不可区分性

The notion of computational indistinguishability is central to the theory of cryptography, and underlies much of what we have seen in Chapter 3 and this chapter. Informally, two probability distributions are computationally indistinguishable if no efficient algorithm can tell them apart (or distinguish them). In more detail, consider two distributions X and Y over strings of some length $\ell$; that is, X and Y each assigns some probability to every string in $\{0,1\}^{\ell}$. When we say that some algorithm D cannot distinguish these two distributions, we mean that D cannot tell whether it is given a string sampled according to distribution X or whether it is given a string sampled according to distribution Y. Put differently, if we imagine D outputting “0” when it believes its input was sampled according to X and outputting “1” if it thinks its input was sampled according to Y, then the probability that D outputs “1” should be roughly the same regardless of whether D is provided with a sample from X or from Y. In other words, we want

计算不可区分性的概念是密码学理论的核心，它支撑着第 3 章以及本章所讲的大部分内容。非正式地说，如果没有任何高效算法能把两个概率分布区分开，那么这两个分布在计算上不可区分。更详细地说，考虑某个长度 ℓ 的串上的两个分布 $X$ 与 $Y$；也就是说，$X$ 与 $Y$ 各自给 $\{0,1\}^{\ell}$ 中的每个串赋予一定的概率。当我们说算法  $D$ 无法区分这两个分布时，意思是 $D$ 分辨不出自己拿到的是按分布 $X$ 抽样的串，还是按分布 $Y$ 抽样的串。换个说法：设想当 $D$ 认为其输入按 $X$ 抽样时输出“0”，认为其输入按 $Y$ 抽样时输出“1”；那么无论提供给 $D$ 的样本来自 $X$ 还是来自 $Y$，$D$ 输出“1”的概率都应当大致相同。换言之，我们希望

$$
\left|\Pr_{s\leftarrow X}[D(s)=1]-\Pr_{s\leftarrow Y}[D(s)=1]\right|
$$

to be small.

尽可能小。

This should be reminiscent of the way we defined pseudorandom generators and, indeed, we will soon formally redefine the notion of a pseudorandom generator using this terminology.

这应当让我们回想起定义伪随机生成器的方式；事实上，我们很快就会用这套术语正式地重新定义伪随机生成器的概念。

The formal definition of computational indistinguishability refers to probability ensembles, which are infinite sequences of probability distributions.

计算不可区分性的形式化定义要用到概率总体（probability ensemble），也就是由概率分布构成的无穷序列。

(This formalism is necessary for a meaningful asymptotic approach.) Although the notion can be generalized, for our purposes we consider probability ensembles in which the underlying distributions are indexed by natural numbers. If for every natural number $n$ we have a distribution $X_n$, then $\mathcal{X} = \{X_n\}_{n \in \mathbb{N}}$ is a probability ensemble. It is often the case that $X_n = Y_{t(n)}$ for some function $t$, in which case we write $\{Y_{t(n)}\}_{n \in \mathbb{N}}$ in place of $\{X_n\}_{n \in \mathbb{N}}$.

（这种形式化对于有意义的渐近处理是必要的。）尽管这一概念可以推广，但出于本书的目的，我们只考虑底层分布以自然数为下标的概率总体。如果对每个自然数 $n$ 都有一个分布 $X_n$，那么 $\mathcal{X} = \{X_n\}_{n \in \mathbb{N}}$ 就是一个概率总体。经常出现 $X_n = Y_{t(n)}$（$t$ 为某个函数）的情况，此时我们就用 $\{Y_{t(n)}\}_{n \in \mathbb{N}}$ 来代替 $\{X_n\}_{n \in \mathbb{N}}$。

We will only be interested in *efficiently* sampleable probability ensembles. An ensemble $\mathcal{X} = \{X_n\}_{n \in \mathbb{N}}$ is efficiently sampleable if there is a probabilistic polynomial-time algorithm $S$ such that the random variables $S(1^n)$ and $X_n$ are identically distributed. That is, algorithm $S$ is an efficient way of sampling $\mathcal{X}$.

我们只关心*可高效*抽样的概率总体。总体 $\mathcal{X} = \{X_n\}_{n \in \mathbb{N}}$ 称为可高效抽样的，如果存在概率多项式时间算法 $S$，使得随机变量 $S(1^n)$ 与 $X_n$ 同分布。也就是说，算法 $S$ 就是抽样 $\mathcal{X}$ 的一种高效方式。

We can now formally define what it means for two ensembles to be computationally indistinguishable.

现在我们可以正式定义两个总体计算不可区分的含义了。

DEFINITION 8.29 Two probability ensembles $\mathcal{X} = \{X_n\}_{n \in \mathbb{N}}$ and $\mathcal{Y} = \{Y_n\}_{n \in \mathbb{N}}$ are computationally indistinguishable, denoted $\mathcal{X} \overset{\mathrm{c}}{=} \mathcal{Y}$, if for every probabilistic polynomial-time distinguisher $D$ there exists a negligible function $\mathsf{negl}$ such that:

定义 8.29　两个概率总体 $\mathcal{X} = \{X_n\}_{n \in \mathbb{N}}$ 与 $\mathcal{Y} = \{Y_n\}_{n \in \mathbb{N}}$ 称为计算不可区分的，记作 $\mathcal{X} \overset{\mathrm{c}}{=} \mathcal{Y}$，如果对每个概率多项式时间区分器 $D$，都存在可忽略函数 $\mathsf{negl}$，使得：

$$
\left|\Pr_{x\leftarrow X_{n}}[D(1^{n},x)=1]-\Pr_{y\leftarrow Y_{n}}[D(1^{n},y)=1]\right|\leq\mathsf{negl}(n).
$$

In the definition, $D$ is given the unary input ${1}^n$ so it can run in time polynomial in $n$. This is important when the outputs of $X_n$ and $Y_n$ may have length less than $n$. As shorthand in probability expressions, we will sometimes write $X$ as a placeholder for a random sample from distribution $X$. That is, we would write $\Pr[D(1^n, X_n) = 1]$ in place of $\Pr_{x \leftarrow X_n}[D(1^n, x) = 1]$.

在该定义中，$D$ 被给了一元输入 ${1}^n$，以便它能以 $n$ 的多项式为运行时间上界。当 $X_n$ 与 $Y_n$ 的输出长度可能小于 n 时，这一点很重要。作为概率表达式中的简写，我们有时会写 $X$ 来代表从分布 $X$ 中抽取的一个随机样本。也就是说，我们会用 $\Pr[D(1^n, X_n) = 1]$ 来代替 $\Pr_{x \leftarrow X_n}[D(1^n, x) = 1]$。

Pseudorandomness and pseudorandom generators. Pseudorandomness is just a special case of computational indistinguishability. For any integer $\ell$, let $U_\ell$ denote the uniform distribution over $\{0,1\}^\ell$. We can define a pseudorandom generator as follows:

**伪随机性与伪随机生成器。**

伪随机性不过是计算不可区分性的一种特例。对任意整数 ℓ，令 $U_\ell$ 表示 $\{0,1\}^\ell$ 上的均匀分布。我们可以如下定义伪随机生成器：

DEFINITION 8.30 Let $\ell(\cdot)$ be a polynomial and let $G$ be a (deterministic) polynomial-time algorithm where for all s it holds that $|G(s)| = \ell(|s|)$. We say that $G$ is a pseudorandom generator if the following two conditions hold:

定义 8.30　设 $\ell(\cdot)$ 是多项式，$G$ 是（确定性）多项式时间算法，且对所有 $s$ 都有 $|G(s)| = \ell(|s|)$。如果下列两个条件成立，我们就称 $G$ 是伪随机生成器：

1. (Expansion.) For every n it holds that $\ell(n) > n$.

   （扩展性。）对每个 $n$ 都有 $\ell(n) > n$。

2. (Pseudorandomness.) The ensemble $\{G(U_n)\}_{n \in \mathbb{N}}$ is computationally indistinguishable from the ensemble $\{U_{\ell(n)}\}_{n \in \mathbb{N}}$.

   （伪随机性。）总体 $\{G(U_n)\}_{n \in \mathbb{N}}$ 与总体 $\{U_{\ell(n)}\}_{n \in \mathbb{N}}$ 计算不可区分。

Many of the other definitions and assumptions in this book can also be cast as special cases or variants of computational indistinguishability.

本书中的许多其他定义与假设同样可以被表述为计算不可区分性的特例或变体。

Multiple samples. An important theorem regarding computational indistinguishability is that polynomial$^{1}$ many samples of (efficiently sampleable) computationally indistinguishable ensembles are also computationally indistinguishable.

**多样本。**

关于计算不可区分性的一个重要定理是：（可高效抽样的）计算不可区分总体的多项式$^{1}$ 个样本放在一起仍然计算不可区分。

THEOREM 8.31 Let $\mathcal{X}$ and $\mathcal{Y}$ be efficiently sampleable probability ensembles that are computationally indistinguishable. Then, for every polynomial $t$, the ensemble $\overline{\mathcal{X}} = \{(X_n^{(1)}, \ldots, X_n^{(t(n))})\}_{n \in \mathbb{N}}$ is computationally indistinguishable from the ensemble $\overline{\mathcal{Y}} = \{(Y_n^{(1)}, \ldots, Y_n^{(t(n))})\}_{n \in \mathbb{N}}$.

定理 8.31　设 $\mathcal{X}$ 与 $\mathcal{Y}$ 是计算不可区分的可高效抽样概率总体。那么，对任意多项式 $t$，总体 $\overline{\mathcal{X}} = \{(X_n^{(1)}, \ldots, X_n^{(t(n))})\}_{n \in \mathbb{N}}$ 与总体 $\overline{\mathcal{Y}} = \{(Y_n^{(1)}, \ldots, Y_n^{(t(n))})\}_{n \in \mathbb{N}}$ 计算不可区分。

For example, let $G$ be a pseudorandom generator with expansion factor ${2}n$, in which case the ensembles $\{G(U_n)\}_{n\in\mathbb{N}}$ and $\{U_{2n}\}_{n\in\mathbb{N}}$ are computationally indistinguishable. In the proof of Theorem 8.21 we showed that for any polynomial $t$ the ensembles

例如，设 $G$ 是扩展因子为 ${2}n$ 的伪随机生成器，此时总体 $\{G(U_n)\}_{n\in\mathbb{N}}$ 与 $\{U_{2n}\}_{n\in\mathbb{N}}$ 计算不可区分。我们在定理 8.21 的证明中已经表明：对任意多项式 $t$，总体

$$
\{(\underbrace{G(U_{n}),\ldots,G(U_{n})}_{t(n)})\}_{n\in\mathbb{N}}\quad\text{and}\quad\{(\underbrace{U_{2n},\ldots,U_{2n}}_{t(n)})\}_{n\in\mathbb{N}}
$$

are also computationally indistinguishable. Theorem 8.31 is proved by a hybrid argument in exactly the same way.

也计算不可区分。定理 8.31 正是以完全相同的混合论证证得的。

## References and Additional Reading　参考文献与延伸阅读

The notion of a one-way function was first proposed by Diffie and Hellman [65] and later formalized by Yao [205]. Hard-core predicates were introduced by Blum and Micali [41], and the fact that there exists a hard-core predicate for every one-way function was proved by Goldreich and Levin [86].

单向函数的概念最早由 Diffie 与 Hellman [65] 提出，后来由 Yao [205] 形式化。难核谓词由 Blum 与 Micali [41] 引入；“每个单向函数都存在难核谓词”这一事实由 Goldreich 与 Levin [86] 证明。

The first construction of pseudorandom generators (under a specific number-theoretic hardness assumption) was given by Blum and Micali [41]. The construction of a pseudorandom generator from any one-way permutation was given by Yao [205], and the result that pseudorandom generators can be constructed from any one-way function was shown by Håstad et al. [93]. Pseudorandom functions were defined and constructed by Goldreich, Goldwasser and Micali [85] and their extension to (strong) pseudorandom permutations was shown by Luby and Rackoff [132]. The fact that one-way functions are a necessary assumption for most of private-key cryptography was shown in [101]. The proof of Proposition 8.28 is from [79].

伪随机生成器的第一个构造（在一个具体的数论困难性假设下）由 Blum 与 Micali [41] 给出。从任意单向置换出发的伪随机生成器构造由 Yao [205] 给出；“伪随机生成器可以从任意单向函数构造出来”这一结果由 Håstad 等人 [93] 证明。伪随机函数由 Goldreich、Goldwasser 与 Micali [85] 定义并构造，它们向（强）伪随机置换的推广由 Luby 与 Rackoff [132] 证明。“单向函数是大部分私钥密码学的必要假设”这一事实发表于 [101]。命题 8.28 的证明出自 [79]。

Our presentation is heavily influenced by Goldreich's book [82], which is highly recommended for those interested in exploring the topics of this chapter in greater detail.

我们的讲述深受 Goldreich 的著作 [82] 的影响；对希望更深入探究本章主题的读者，强烈推荐此书。

## Exercises　习题

8.1 Prove that if there exists a one-way function, then there exists a one-way function $f$ such that $f(0^n) = 0^n$ for every $n$. Note that for infinitely many values $y$, it is easy to compute $f^{-1}(y)$. Why does this not contradict one-wayness?

     8.1 证明：若存在单向函数，则存在单向函数 $f$，使得对每个 $n$ 都有 $f(0^n) = 0^n$。注意：对无穷多个值 $y$ 来说，计算 $f^{-1}(y)$ 是容易的。为什么这不与单向性矛盾？

8.2 Prove that if $f$ is a one-way function, then the function $g$ defined by $g(x_1, x_2) \stackrel{\mathrm{def}}{=} (f(x_1), x_2)$, where $|x_1| = |x_2|$, is also a one-way function. Observe that $g$ reveals half of its input, but is nevertheless one-way.

     8.2 证明：若 $f$ 是单向函数，则由 $g(x_1, x_2) \stackrel{\mathrm{def}}{=} (f(x_1), x_2)$（其中 $|x_1| = |x_2|$）定义的函数 $g$ 也是单向函数。可以看到 $g$ 泄露了自己输入的一半，但它依然是单向的。

8.3 Prove that if there exists a one-way function, then there exists a length-preserving one-way function.

     8.3 证明：若存在单向函数，则存在保长度的单向函数。

Hint: Let $f$ be a one-way function and let $p(\cdot)$ be a polynomial such that $|f(x)| \leq p(|x|)$. (Justify the existence of such a $p$.) Define $f^{\prime}(x) \stackrel{\mathrm{def}}{=} f(x)\|1\|0^{p(|x|)-|f(x)|}$. Further modify $f^{\prime}$ to get a length-preserving function that remains one-way.

     提示：设 $f$ 是单向函数，$p(\cdot)$ 是满足 $|f(x)| \leq p(|x|)$ 的多项式。（请说明这样的 $p$ 为何存在。）定义 $f^{\prime}(x) \stackrel{\mathrm{def}}{=} f(x)\|1\|0^{p(|x|)-|f(x)|}$。再进一步修改 $f^{\prime}$，得到仍保持单向性的保长度函数。

8.4 Let $(Gen, H)$ be a collision-resistant hash function, where H maps strings of length 2n to strings of length n. Prove that the function family $(Gen, Samp, H)$ is one-way (cf. Definition 8.3), where Samp is the trivial algorithm that samples a uniform string of length 2n.

     8.4 设 $(Gen, H)$ 是抗碰撞哈希函数，其中 $H$ 把长度 $2n$ 的串映射为长度 $n$ 的串。证明函数族 $(Gen, Samp, H)$ 是单向的（参见定义 8.3），其中 $Samp$ 是均匀抽取一条长度为 $2n$ 的串的平凡算法。

Hint: Choosing uniform $x \in \{0,1\}^{2n}$ and finding an inverse of $y = H^s(x)$ does not guarantee a collision. But it does yield a collision most of the time...

     提示：均匀选取 $x \in \{0,1\}^{2n}$ 并求出 $y = H^s(x)$ 的一个逆，并不能保证找到碰撞。但在绝大多数时候它确实能产生碰撞……

8.5 Let F be a (length-preserving) pseudorandom permutation.

     8.5 设 $F$ 是（保长度的）伪随机置换。

(a) Show that the function $f(x, y) = F_x(y)$ is not one-way.

     (a) 证明函数 $f(x, y) = F_x(y)$ 不是单向的。

(b) Show that the function $f(y) = F_{0^n}(y)$ (where $n = |y|$) is not one-way.

     (b) 证明函数 $f(y) = F_{0^n}(y)$（其中 $n = |y|$）不是单向的。

(c) Prove that the function $f(x) = F_x(0^n)$ (where $n = |x|$) is one-way.

     (c) 证明函数 $f(x) = F_x(0^n)$（其中 $n = |x|$）是单向的。

8.6 Let $f$ be a length-preserving one-way function, and let $\mathsf{hc}$ be a hard-core predicate of $f$. Define $G$ as $G(x) = f(x)\|\mathsf{hc}(x)$. Is $G$ necessarily a pseudorandom generator? Prove your answer.

     8.6 设 $f$ 是保长度的单向函数，$\mathsf{hc}$ 是 $f$ 的难核谓词。定义 $G(x) = f(x)\|\mathsf{hc}(x)$。$G$ 一定是伪随机生成器吗？请证明你的答案。

8.7 Prove that there exist one-way functions if and only if there exist one-way function families. Discuss why your proof does not carry over to the case of one-way permutations.

     8.7 证明：单向函数存在当且仅当单向函数族存在。并讨论为什么你的证明不能照搬到单向置换的情形。

8.8 Let $f$ be a length-preserving one-way function. Is $g(x) \overset{\mathrm{def}}{=} f(f(x))$ necessarily one-way? What about $g^{\prime}(x) \overset{\mathrm{def}}{=} f(x)\|f(f(x))$?

     8.8 设 $f$ 是保长度的单向函数。$g(x) \overset{\mathrm{def}}{=} f(f(x))$ 一定是单向的吗？那 $g^{\prime}(x) \overset{\mathrm{def}}{=} f(x)\|f(f(x))$ 又如何呢？

8.9 Let $\Pi = (\mathsf{Gen}, \mathsf{Samp}, f)$ be a function family. A function $\mathsf{hc} : \{0,1\}^* \to \{0,1\}$ is a hard-core predicate of $\Pi$ if it is efficiently computable and if for every PPT algorithm $\mathcal{A}$ there is a negligible function $\mathsf{negl}$ such that

     8.9 设 $\Pi = (\mathsf{Gen}, \mathsf{Samp}, f)$ 是函数族。若函数 $\mathsf{hc} : \{0,1\}^* \to \{0,1\}$ 可以高效计算，并且对每个 PPT 算法 $\mathcal{A}$ 都存在可忽略函数 $\mathsf{negl}$ 使得

$$
\Pr_{\substack{I\leftarrow\mathsf{Gen}(1^{n}),x\leftarrow\mathsf{Samp}(I)}}[\mathcal{A}(I,f_{I}(x))=\mathsf{hc}(I,x)]\le\frac{1}{2}+\mathsf{negl}(n).
$$

Prove a version of the Goldreich–Levin theorem for this setting, namely, if a one-way function (resp., permutation) family $\Pi$ exists, then there exists a one-way function (resp., permutation) family $\Pi^{\prime}$ and a hard-core predicate $\mathsf{hc}$ of $\Pi^{\prime}$.

     则称 $\mathsf{hc}$ 为 $\Pi$ 的难核谓词。请针对这一设定证明一个版本的 Goldreich–Levin 定理：即若单向函数（相应地，单向置换）族 $\Pi$ 存在，则存在单向函数（相应地，单向置换）族 $\Pi^{\prime}$ 以及 $\Pi^{\prime}$ 的难核谓词 $\mathsf{hc}$。

8.10 Show a construction of a pseudorandom generator from any one-way permutation family. You may use the result of the previous exercise.

     8.10 给出一个从任意单向置换族构造伪随机生成器的方法。你可以使用上一题的结果。

8.11 This exercise is for students who have taken a course in complexity theory or are otherwise familiar with $\mathcal{NP}$-completeness.

     8.11 本题供修过复杂性理论课程或以其他方式熟悉 $\mathcal{NP}$ 完全性的学生练习。

(a) Show that the existence of one-way functions implies $\mathcal{P} \neq \mathcal{NP}$.

     (a) 证明：单向函数的存在性蕴含 $\mathcal{P} \neq \mathcal{NP}$。

(b) Assume that $\mathcal{P} \neq \mathcal{NP}$. Show that there exists a function $f$ that is: (1) computable in polynomial time, (2) hard to invert in the worst case (i.e., for all probabilistic polynomial-time $\mathcal{A}$, $\Pr_{x\leftarrow\{0,1\}^n}[f(\mathcal{A}(f(x))) = f(x)] \neq 1$), but (3) is not one-way.

     (b) 假设 $\mathcal{P} \neq \mathcal{NP}$。证明存在函数 $f$ 同时满足：(1) 可在多项式时间内计算；(2) 最坏情况下难以求逆（即对一切概率多项式时间的 $\mathcal{A}$，$\Pr_{x\leftarrow\{0,1\}^n}[f(\mathcal{A}(f(x))) = f(x)] \neq 1$）；但 (3) 它却不是单向的。

8.12 For $x \in \{0,1\}^n$ let $x = x_1 \cdots x_n$. Prove that if there exists a one-way function, then there exists a one-way function $f$ such that for every $i$ there is an algorithm $A_i$ such that

     8.12 对 $x \in \{0,1\}^n$，记 $x = x_1 \cdots x_n$。证明：若存在单向函数，则存在单向函数 $f$，使得对每个 $i$ 都存在算法 $A_i$ 满足

$$
\Pr_{x\leftarrow\{0,1\}^{n}}[A_{i}(f(x))=x_{i}]\geq\frac{1}{2}+\frac{1}{2n}.
$$

(This exercise demonstrates that it is not possible to claim that every one-way function hides at least one specific bit of the input.)

     （本题说明：我们不能断言每个单向函数都至少隐藏输入中的某一个特定比特。）

8.13 Show that if an efficiently computable one-to-one function $f$ has a hard-core predicate, then $f$ is one-way.

     8.13 证明：若可高效计算的一一函数 $f$ 具有难核谓词，则 $f$ 是单向的。

8.14 Show that if Construction 8.20 is modified in the natural way so that $F_k(x)$ is defined for every nonempty string x of length at most n, then the construction is no longer a pseudorandom function.

     8.14 证明：若把构造 8.20 以自然的方式加以修改，使 $F_k(x)$ 对每个长度不超过 $n$ 的非空串 $x$ 都有定义，那么该构造便不再是伪随机函数。

8.15 Prove that if there exists a pseudorandom function that, using a key of length n, maps n-bit inputs to single-bit outputs, then there exists a pseudorandom function that maps n-bit inputs to n-bit outputs.

     8.15 证明：若存在这样的伪随机函数——它使用长度为 $n$ 的密钥，把 $n$ 比特输入映射为单比特输出——则存在把 $n$ 比特输入映射为 $n$ 比特输出的伪随机函数。

Hint: Use a key of length $n^{2}$, and prove your construction secure using a hybrid argument.

     提示：使用长度为 $n^{2}$ 的密钥，并用混合论证证明你所给构造的安全性。

8.16 Prove that a two-round Feistel network using pseudorandom round functions (as in Equation (8.15)) is not a pseudorandom permutation.

     8.16 证明：使用伪随机轮函数的两轮 Feistel 网络（如式 (8.15) 那样）不是伪随机置换。

8.17 Prove that a three-round Feistel network using pseudorandom round functions (as in Equation (8.16)) is not a strong pseudorandom permutation.

     8.17 证明：使用伪随机轮函数的三轮 Feistel 网络（如式 (8.16) 那样）不是强伪随机置换。

Hint: This is significantly more difficult than the previous exercise. Use a distinguisher that makes two queries to the permutation and one query to its inverse.

     提示：本题比上一题难得多。使用一个对该置换做两次查询、对其逆做一次查询的区分器。

8.18 Consider the keyed permutation $F^{*}$ defined by

     8.18 考虑如下定义的带密钥置换 $F^{*}$：

$$
F_{k}^{*}(x)\stackrel{\mathrm{def}}{=}\mathsf{Feistel}_{F_{k},F_{k},F_{k}}(x).
$$

(Note that the same key is used in each round.) Show that $F^{*}$ is not a pseudorandom permutation.

     （注意每一轮用的都是同一个密钥。）证明 $F^{*}$ 不是伪随机置换。

8.19 Let $\mathcal{X}, \mathcal{Y}, \mathcal{Z}$ be probability ensembles. Prove that if $\mathcal{X} \overset{\mathrm{c}}{=} \mathcal{Y}$ and $\mathcal{Y} \overset{\mathrm{c}}{=} \mathcal{Z}$, then $\mathcal{X} \overset{\mathrm{c}}{=} \mathcal{Z}$.

     8.19 设 $\mathcal{X}, \mathcal{Y}, \mathcal{Z}$ 是概率总体。证明：若 $\mathcal{X} \overset{\mathrm{c}}{=} \mathcal{Y}$ 且 $\mathcal{Y} \overset{\mathrm{c}}{=} \mathcal{Z}$，则 $\mathcal{X} \overset{\mathrm{c}}{=} \mathcal{Z}$。

8.20 Prove Theorem 8.31.

     8.20 证明定理 8.31。

8.21 Let $\mathcal{X} = \{X_n\}_{n \in \mathbb{N}}$ and $\mathcal{Y} = \{Y_n\}_{n \in \mathbb{N}}$ be computationally indistinguishable probability ensembles. Prove that for any probabilistic polynomial-time algorithm $\mathcal{A}$, the ensembles $\{\mathcal{A}(X_n)\}_{n \in \mathbb{N}}$ and $\{\mathcal{A}(Y_n)\}_{n \in \mathbb{N}}$ are computationally indistinguishable.

     8.21 设 $\mathcal{X} = \{X_n\}_{n \in \mathbb{N}}$ 与 $\mathcal{Y} = \{Y_n\}_{n \in \mathbb{N}}$ 是计算不可区分的概率总体。证明：对任意概率多项式时间算法 $\mathcal{A}$，总体 $\{\mathcal{A}(X_n)\}_{n \in \mathbb{N}}$ 与 $\{\mathcal{A}(Y_n)\}_{n \in \mathbb{N}}$ 计算不可区分。
