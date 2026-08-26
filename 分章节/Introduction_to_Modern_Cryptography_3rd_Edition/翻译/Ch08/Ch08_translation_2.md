## 8.4 Constructing Pseudorandom Generators　伪随机生成器的构造

We first show how to construct pseudorandom generators that stretch their input by a single bit, under the assumption that one-way permutations exist. We then show how to extend this to obtain any polynomial expansion factor.

我们首先在单向置换存在的假设下，展示如何构造把输入扩展单个比特的伪随机生成器；随后展示如何将其推广，以获得任意多项式级的扩展因子。

### 8.4.1 Pseudorandom Generators with Minimal Expansion　具有最小扩展的伪随机生成器

Let $f$ be a one-way permutation with hard-core predicate $\mathsf{hc}$. This means that $\mathsf{hc}(s)$ “looks random” given $f(s)$, when $s$ is uniform. Furthermore, since $f$ is a permutation, $f(s)$ itself is uniformly distributed. (Applying a permutation to a uniformly distributed value yields a uniformly distributed value.) So if $s$ is a uniform $n$-bit string, the $(n+1)$-bit string $f(s)\|\mathsf{hc}(s)$ consists of a uniform $n$-bit string plus an additional bit that looks uniform even conditioned on the initial $n$ bits; in other words, this $(n+1)$-bit string is pseudorandom. Thus, the algorithm $G$ defined by $G(s) = f(s)\|\mathsf{hc}(s)$ is a pseudorandom generator.

设 $f$ 是带难核谓词 $\mathsf{hc}$ 的单向置换。这意味着：当 $s$ 均匀时，在给定 $f(s)$ 的条件下，$\mathsf{hc}(s)$ “看起来是随机的”。此外，由于 $f$ 是置换，$f(s)$ 本身就服从均匀分布。（把置换作用于均匀分布的值，得到的仍是均匀分布的值。）于是，若 $s$ 是均匀的 $n$ 比特串，则 $(n+1)$ 比特串 $f(s)\|\mathsf{hc}(s)$ 由一个均匀的 $n$ 比特串再加一个额外比特组成，而这个额外比特即使在已知前 $n$ 个比特的条件下看起来也是均匀的；换言之，这个 $(n+1)$ 比特串是伪随机的。因此，由 $G(s) = f(s)\|\mathsf{hc}(s)$ 定义的算法 $G$ 就是一个伪随机生成器。

THEOREM 8.18 Let $f$ be a one-way permutation with hard-core predicate $\mathsf{hc}$. Then algorithm $G$ defined by $G(s) = f(s)\|\mathsf{hc}(s)$ is a pseudorandom generator with expansion factor $\ell(n) = n + 1$.

定理 8.18　设 $f$ 是带难核谓词 $\mathsf{hc}$ 的单向置换。那么由 $G(s) = f(s)\|\mathsf{hc}(s)$ 定义的算法 $G$ 是扩展因子为 $\ell(n) = n + 1$ 的伪随机生成器。

PROOF Let $D$ be a probabilistic polynomial-time algorithm. We prove that there is a negligible function $\mathsf{negl}$ such that

证明　设 $D$ 是一个概率多项式时间算法。我们证明：存在可忽略函数 $\mathsf{negl}$，使得

$$
\Pr_{r\leftarrow\{0,1\}^{n+1}}[D(r)=1]-\Pr_{s\leftarrow\{0,1\}^{n}}[D(G(s))=1]\leq\mathsf{negl}(n). \tag{8.2}
$$

A similar argument shows that there is a negligible function $\mathsf{negl}^{\prime}$ for which

用类似的论证可以表明，存在可忽略函数 $\mathsf{negl}^{\prime}$，使得

$$
\Pr_{s\leftarrow\{0,1\}^{n}}[D(G(s))=1]-\Pr_{r\leftarrow\{0,1\}^{n+1}}[D(r)=1]\leq\mathsf{negl}^{\prime}(n), \tag{8.3}
$$

which completes the proof.

这就完成了证明。

Observe first that

首先注意到

$$
\begin{aligned}
\Pr_{r\leftarrow\{0,1\}^{n+1}}[D(r)=1]&=\Pr_{r\leftarrow\{0,1\}^n,r^{\prime}\leftarrow\{0,1\}}[D\left(r\|r^{\prime}\right)=1]\\
&=\Pr_{s\leftarrow\{0,1\}^n,r^{\prime}\leftarrow\{0,1\}}[D\left(f(s)\|r^{\prime}\right)=1]\\
&=\frac{1}{2}\cdot\Pr_{s\leftarrow\{0,1\}^n}[D\left(f(s)\|\mathsf{hc}(s)\right)=1]\\
&\quad+\frac{1}{2}\cdot\Pr_{s\leftarrow\{0,1\}^n}[D\left(f(s)\|\overline{\mathsf{hc}}(s)\right)=1],
\end{aligned}
$$

using the fact that $f$ is a permutation for the second equality, and that a uniform bit $r^{\prime}$ is equal to $\mathsf{hc}(s)$ with probability exactly ${1}/{2}$ for the third equality. Since

其中第二个等号利用了 $f$ 是置换这一事实，第三个等号则利用了均匀比特 $r^{\prime}$ 恰好以 ${1}/{2}$ 的概率等于 $\mathsf{hc}(s)$。由于

$$
\Pr_{s\leftarrow\{0,1\}^{n}}[D(G(s))=1]=\Pr_{s\leftarrow\{0,1\}^{n}}[D\left(f(s)\|\mathsf{hc}(s)\right)=1]
$$

(by definition of $G$), this means that Equation (8.3) is equivalent to

（由 $G$ 的定义），这意味着式 (8.3) 等价于

$$
\frac{1}{2}\cdot\left(\Pr_{s\leftarrow\{0,1\}^{n}}[D\left(f(s)\|\overline{{\mathsf{hc}}}(s)\right)=1]-\Pr_{s\leftarrow\{0,1\}^{n}}[D\left(f(s)\|\mathsf{hc}(s)\right)=1]\right)\leq\mathsf{negl}(n).
$$

Consider the following algorithm $\mathcal{A}$ that is given as input a value $y = f(s)$ and tries to predict the value of $\mathsf{hc}(s)$:

考虑如下算法 $\mathcal{A}$：它以值 $y = f(s)$ 为输入，试图预测 $\mathsf{hc}(s)$ 的值：

1. Choose uniform $r^{\prime} \in \{0,1\}$.

   均匀选取 $r^{\prime} \in \{0,1\}$。

2. Run $D(y\|r^{\prime})$. If D outputs 0, output $r^{\prime}$; otherwise output $\bar{r}^{\prime}$.

   运行 $D(y\|r^{\prime})$。若 D 输出 0，则输出 $r^{\prime}$；否则输出 $\bar{r}^{\prime}$。

Clearly A runs in polynomial time. By definition of A, we have

显然 $A$ 在多项式时间内运行。根据 $A$ 的定义，我们有

$$
\begin{aligned}
&\Pr_{s\leftarrow\{0,1\}^{n}}[\mathcal{A}(f(s))=\mathsf{hc}(s)]\\
&\quad=\frac{1}{2}\cdot\Pr_{s\leftarrow\{0,1\}^{n}}[\mathcal{A}(f(s))=\mathsf{hc}(s)\mid r^{\prime}=\mathsf{hc}(s)]\\
&\quad+\frac{1}{2}\cdot\Pr_{s\leftarrow\{0,1\}^{n}}[\mathcal{A}(f(s))=\mathsf{hc}(s)\mid r^{\prime}\neq\mathsf{hc}(s)]\\
&\quad=\frac{1}{2}\cdot\left(\Pr_{s\leftarrow\{0,1\}^{n}}[D(f(s)\|\mathsf{hc}(s))=0]+\Pr_{s\leftarrow\{0,1\}^{n}}[D(f(s)\|\overline{\mathsf{hc}}(s))=1]\right)\\
&\quad=\frac{1}{2}\cdot\left(\left(1-\Pr_{s\leftarrow\{0,1\}^{n}}[D(f(s)\|\mathsf{hc}(s))=1]\right)+\Pr_{s\leftarrow\{0,1\}^{n}}[D(f(s)\|\overline{\mathsf{hc}}(s))=1]\right)\\
&\quad=\frac{1}{2}+\frac{1}{2}\cdot\left(\Pr_{s\leftarrow\{0,1\}^{n}}[D(f(s)\|\overline{\mathsf{hc}}(s))=1]-\Pr_{s\leftarrow\{0,1\}^{n}}[D\left(f(s)\|\mathsf{hc}(s)\right)=1]\right).
\end{aligned}
$$

Since $\mathsf{hc}$ is a hard-core predicate of $f$, it follows that there exists a negligible function $\mathsf{negl}$ for which

由于 $\mathsf{hc}$ 是 $f$ 的难核谓词，可知存在可忽略函数 $\mathsf{negl}$，使得

$$
\frac{1}{2}\cdot\left(\Pr_{s\leftarrow\{0,1\}^{n}}[D\left(f(s)\|\overline{{\mathsf{hc}}}(s)\right)=1]-\Pr_{s\leftarrow\{0,1\}^{n}}[D\left(f(s)\|\mathsf{hc}(s)\right)=1]\right)\leq\mathsf{negl}(n),
$$

as desired.

此即所证。

### 8.4.2 Increasing the Expansion Factor　提高扩展因子

We now show that the expansion factor of a pseudorandom generator can be increased by any desired (polynomial) amount. This means that the previous construction, with expansion factor $\ell(n) = n + 1$, suffices for constructing a pseudorandom generator with arbitrary (polynomial) expansion factor.

我们现在证明：伪随机生成器的扩展因子可以提高任意想要的（多项式）量。这意味着前述扩展因子为 $\ell(n) = n + 1$ 的构造，已足以用来构造具有任意（多项式）扩展因子的伪随机生成器。

THEOREM 8.19 If there exists a pseudorandom generator G with expansion factor $n+1$, then for any polynomial poly there exists a pseudorandom generator $\hat{G}$ with expansion factor $\mathsf{poly}(n)$.

定理 8.19　若存在扩展因子为 $n+1$ 的伪随机生成器 G，则对任意多项式 poly，存在扩展因子为 $\mathsf{poly}(n)$ 的伪随机生成器 $\hat{G}$。

PROOF We first consider constructing a pseudorandom generator $\hat{G}$ that outputs $n + 2$ bits. $\hat{G}$ works as follows: Given an initial seed $s \in \{0,1\}^n$, it computes $t_1 := G(s)$ to obtain $n + 1$ pseudorandom bits. The initial $n$ bits of $t_1$ are then used again as a seed for $G$; the resulting $n+1$ bits, concatenated with the final bit of $t_1$, yield the $(n+2)$-bit output. (See Figure 8.1.) The second application of $G$ uses a pseudorandom seed rather than a random one. The proof of security we give next shows that this does not impact the pseudorandomness of the output.

证明　我们先考虑构造一个输出 $n + 2$ 比特的伪随机生成器 $\hat{G}$。$\hat{G}$ 的工作方式如下：给定初始种子 $s \in \{0,1\}^n$，它计算 $t_1 := G(s)$，得到 $n + 1$ 个伪随机比特。然后将 $t_1$ 的前 $n$ 个比特再次用作 $G$ 的种子；把所得的 $n+1$ 个比特与 $t_1$ 的最后一个比特拼接起来，就得到 $(n+2)$ 比特的输出。（见图 8.1。）第二次使用 $G$ 时用的是伪随机的种子，而非随机的种子；下面给出的安全性证明将表明，这并不影响输出的伪随机性。

We now prove that $\hat{G}$ is a pseudorandom generator. Define three sequences of distributions $\{H_n^0\}_{n\in\mathbb{N}}$, $\{H_n^1\}_{n\in\mathbb{N}}$, and $\{H_n^2\}_{n\in\mathbb{N}}$, where each of $H_n^0$, $H_n^1$, and $H_n^2$ is a distribution on strings of length $n+2$. In distribution $H_n^0$, a uniform string $t_0 \in \{0,1\}^n$ is chosen and the output is $t_2 := \hat{G}(t_0)$. In distribution $H_n^1$, a uniform string $t_1 \in \{0,1\}^{n+1}$ is chosen and parsed as $s_1 \|\sigma_1$ (where $s_1$ is the initial $n$ bits of $t_1$ and $\sigma_1$ is the final bit). The output is $t_2 := G(s_1)\|\sigma_1$. In distribution $H_n^2$, the output is a uniform string $t_2 \in \{0,1\}^{n+2}$. We denote by $t_2 \leftarrow H_n^i$ the process of generating an $(n+2)$-bit string $t_2$ according to distribution $H_n^i$.

现在证明 $\hat{G}$ 是伪随机生成器。定义三个分布序列 $\{H_n^0\}_{n\in\mathbb{N}}$、$\{H_n^1\}_{n\in\mathbb{N}}$ 与 $\{H_n^2\}_{n\in\mathbb{N}}$，其中 $H_n^0$、$H_n^1$、$H_n^2$ 都是长度为 $n+2$ 的串上的分布。在分布 $H_n^0$ 中，均匀选取串 $t_0 \in \{0,1\}^n$，输出为 $t_2 := \hat{G}(t_0)$。在分布 $H_n^1$ 中，均匀选取串 $t_1 \in \{0,1\}^{n+1}$ 并把它解析为 $s_1 \|\sigma_1$（其中 $s_1$ 是 $t_1$ 的前 $n$ 个比特，$\sigma_1$ 是最后一个比特），输出为 $t_2 := G(s_1)\|\sigma_1$。在分布 $H_n^2$ 中，输出是均匀的串 $t_2 \in \{0,1\}^{n+2}$。我们把按分布 $H_n^i$ 生成长度为 $n+2$ 的串 $t_2$ 的过程记作 $t_2 \leftarrow H_n^i$。

Fix an arbitrary probabilistic polynomial-time distinguisher $D$. We first claim that there is a negligible function $\mathsf{negl}^{\prime}$ such that

任取一个概率多项式时间区分器 $D$。我们首先断言：存在可忽略函数 $\mathsf{negl}^{\prime}$，使得

$$
\left|\Pr_{t_{2}\leftarrow H_{n}^{0}}[D(t_{2})=1]-\Pr_{t_{2}\leftarrow H_{n}^{1}}[D(t_{2})=1]\right|\leq\mathsf{negl}^{\prime}(n). \tag{8.4}
$$

To see this, consider the polynomial-time distinguisher $D^{\prime}$ that, on input $t_1 \in \{0,1\}^{n+1}$, parses $t_1$ as $s_1\|\sigma_1$ with $|s_1| = n$, computes $t_2 := G(s_1)\|\sigma_1$, and outputs $D(t_2)$. Clearly $D^{\prime}$ runs in polynomial time. Observe that:

为看清这一点，考虑多项式时间区分器 $D^{\prime}$：当输入 $t_1 \in \{0,1\}^{n+1}$ 时，它把 $t_1$ 解析为 $s_1\|\sigma_1$（其中 $|s_1| = n$），计算 $t_2 := G(s_1)\|\sigma_1$，并输出 $D(t_2)$。显然 $D^{\prime}$ 在多项式时间内运行。注意到：

1. If $t_{1}$ is uniform, the distribution on $t_{2}$ generated by $D^{\prime}$ is exactly that of distribution $H_{n}^{1}$. Thus,

   若 $t_{1}$ 均匀，则 $D^{\prime}$ 生成的 $t_{2}$ 恰好服从分布 $H_{n}^{1}$。于是，

   $$
   \Pr_{t_{1}\gets\{0,1\}^{n+1}}[D^{\prime}(t_{1})=1]=\Pr_{t_{2}\gets H_{n}^{1}}[D(t_{2})=1].
   $$

2. If $t_1 = G(s)$ for uniform $s \in \{0,1\}^n$, the distribution on $t_2$ generated by $D^{\prime}$ is exactly that of distribution $H_n^0$. That is,

   若 $t_1 = G(s)$（其中 $s \in \{0,1\}^n$ 均匀），则 $D^{\prime}$ 生成的 $t_2$ 恰好服从分布 $H_n^0$。也就是说，

   $$
   \Pr_{s\leftarrow\{0,1\}^{n}}[D^{\prime}(G(s))=1]=\Pr_{t_{2}\leftarrow H_{n}^{0}}[D(t_{2})=1].
   $$

Pseudorandomness of $G$ implies that there is a negligible function $\mathsf{negl}^{\prime}$ with

$G$ 的伪随机性蕴含：存在可忽略函数 $\mathsf{negl}^{\prime}$，使得

$$
\left|\Pr_{s\leftarrow\{0,1\}^{n}}[D^{\prime}(G(s))=1]-\Pr_{t_{1}\leftarrow\{0,1\}^{n+1}}[D^{\prime}(t_{1})=1]\right|\leq\mathsf{negl}^{\prime}(n).
$$

Equation (8.4) follows.

由此即得式 (8.4)。

We next claim that there is a negligible function $\mathsf{negl}^{\prime\prime}$ such that

接下来我们断言：存在可忽略函数 $\mathsf{negl}^{\prime\prime}$，使得

$$
\left|\Pr_{t_{2}\leftarrow H_{n}^{1}}[D(t_{2})=1]-\Pr_{t_{2}\leftarrow H_{n}^{2}}[D(t_{2})=1]\right|\leq\mathsf{negl}^{\prime\prime}(n). \tag{8.5}
$$

To see this, consider the polynomial-time distinguisher $D^{\prime\prime}$ that, on input $w \in \{0,1\}^{n+1}$, chooses uniform $\sigma_1 \in \{0,1\}$, sets $t_2 := w\|\sigma_1$, and outputs $D(t_2)$. If $w$ is uniform then so is $t_2$; thus,

为看清这一点，考虑多项式时间区分器 $D^{\prime\prime}$：当输入 $w \in \{0,1\}^{n+1}$ 时，它均匀选取 $\sigma_1 \in \{0,1\}$，令 $t_2 := w\|\sigma_1$，并输出 $D(t_2)$。若 $w$ 均匀，则 $t_2$ 也均匀；于是，

$$
\Pr_{w\leftarrow\{0,1\}^{n+1}}[D^{\prime\prime}(w)=1]=\Pr_{t_{2}\leftarrow H_{n}^{2}}[D(t_{2})=1].
$$

On the other hand, if $w = G(s)$ for uniform $s \in \{0,1\}^n$, then $t_2$ is distributed exactly according to $H_n^1$ and so

另一方面，若 $w = G(s)$（其中 $s \in \{0,1\}^n$ 均匀），则 $t_2$ 恰好服从分布 $H_n^1$，于是

$$
\Pr_{s\leftarrow\{0,1\}^{n}}[D^{\prime\prime}(G(s))=1]=\Pr_{t_{2}\leftarrow H_{n}^{1}}[D(t_{2})=1].
$$

As before, pseudorandomness of G implies Equation (8.5).

与前面一样，$G$ 的伪随机性蕴含式 (8.5)。

Putting everything together, we have

把所有结果合在一起，我们得到

$$
\begin{aligned}
&\left|\Pr_{s\leftarrow\{0,1\}^{n}}[D(\hat{G}(s))=1]-\Pr_{r\leftarrow\{0,1\}^{n+2}}[D(r)=1]\right|\\
&=\left|\Pr_{t_{2}\leftarrow H_{n}^{0}}[D(t_{2})=1]-\Pr_{t_{2}\leftarrow H_{n}^{2}}[D(t_{2})=1]\right|\\
&\leq\left|\Pr_{t_{2}\leftarrow H_{n}^{0}}[D(t_{2})=1]-\Pr_{t_{2}\leftarrow H_{n}^{1}}[D(t_{2})=1]\right|\\
&\quad+\left|\Pr_{t_{2}\leftarrow H_{n}^{1}}[D(t_{2})=1]-\Pr_{t_{2}\leftarrow H_{n}^{2}}[D(t_{2})=1]\right|\\
&\leq\mathsf{negl}^{\prime}(n)+\mathsf{negl}^{\prime \prime}(n). \tag{8.6}
\end{aligned}
$$

using Equations (8.4) and (8.5). Since $D$ was an arbitrary polynomial-time distinguisher, this proves that $\hat{G}$ is a pseudorandom generator.

其中用到式 (8.4) 与式 (8.5)。由于 $D$ 是任意的多项式时间区分器，这就证明了 $\hat{G}$ 是伪随机生成器。

![Image](https://lsky.jerryxue.top/i/2026/08/22/6a88f9e9e502d.jpg)

**FIGURE 8.1: Increasing the expansion of a pseudorandom generator. / 图 8.1：提高伪随机生成器的扩展**

The general case. The same idea as above can be iteratively applied to generate as many pseudorandom bits as desired. Formally, say we wish to construct a pseudorandom generator $\hat{G}$ with expansion factor $n + p(n)$, for some polynomial $p$. On input $s \in \{0,1\}^n$, algorithm $\hat{G}$ does (cf. Figure 8.1):

**一般情形。**

上面的同一思想可以迭代应用，以生成任意所需数量的伪随机比特。形式化地说，假设我们希望构造扩展因子为 $n + p(n)$ 的伪随机生成器 $\hat{G}$，其中 $p$ 是某个多项式。在输入 $s \in \{0,1\}^n$ 上，算法 $\hat{G}$ 执行（参见图 8.1）：

1. Set $t_0 := s$. For $i = 1, \ldots, p(n)$ do:

   令 $t_0 := s$。对 $i = 1, \ldots, p(n)$ 执行：

   (a) Let $s_{i-1}$ be the first $n$ bits of $t_{i-1}$, and let $\sigma_{i-1}$ denote the remaining $i-1$ bits. (When $i=1$, $s_0=t_0$ and $\sigma_0$ is the empty string.)

   (a) 令 $s_{i-1}$ 为 $t_{i-1}$ 的前 $n$ 个比特，$\sigma_{i-1}$ 表示其余的 $i-1$ 个比特。（当 $i=1$ 时，$s_0=t_0$ 且 $\sigma_0$ 为空串。）

   (b) Set $t_i := G(s_{i-1}) \|\sigma_{i-1}$.

   (b) 令 $t_i := G(s_{i-1}) \|\sigma_{i-1}$。

2. Output $t_{p(n)}$

   输出 $t_{p(n)}$

We show that $\hat{G}$ is a pseudorandom generator. The proof uses a common technique known as a hybrid argument. (Actually, even the case of $p(n) = 2$, above, used a simple hybrid argument.) The main difference with respect to the previous proof is a technical one. Previously, we could define and explicitly work with three sequences of distributions $\{H_n^0\}, \{H_n^1\}$, and $\{H_n^2\}$. Here that is not possible since the number of distributions to consider grows with $n$.

我们证明 $\hat{G}$ 是伪随机生成器。该证明使用一种称为混合论证（hybrid argument）的常见技术。（实际上，就连上面 $p(n) = 2$ 的情形也已经用了一个简单的混合论证。）与前一证明相比，主要差别是技术性的。此前，我们可以定义三个分布序列 $\{H_n^0\}$、$\{H_n^1\}$ 和 $\{H_n^2\}$ 并显式地处理它们；而在这里无法这样做，因为要考虑的分布数量会随 $n$ 增长。

For any $n$ and ${0} \leq j \leq p(n)$, let $H_n^j$ be the distribution on strings of length $n+p(n)$ defined as follows: choose uniform $t_j \in \{0,1\}^{n+j}$, then run $\hat{G}$ starting from iteration $j+1$ and output $t_{p(n)}$. (When $j=p(n)$ this means we simply choose uniform $t_{p(n)} \in \{0,1\}^{n+p(n)}$ and output it.) The crucial observation is that $H_n^0$ corresponds to outputting $\hat{G}(s)$ for uniform $s \in \{0,1\}^n$, while $H_n^{p(n)}$ corresponds to outputting a uniform $(n+p(n))$-bit string. Fixing any polynomial-time distinguisher $D$, this means that

对任意 $n$ 以及 ${0} \leq j \leq p(n)$，令 $H_n^j$ 为长度 $n+p(n)$ 的串上如下定义的分布：均匀选取 $t_j \in \{0,1\}^{n+j}$，然后从第 $j+1$ 次迭代开始运行 $\hat{G}$ 并输出 $t_{p(n)}$。（当 $j=p(n)$ 时，这意味着我们直接均匀选取 $t_{p(n)} \in \{0,1\}^{n+p(n)}$ 并输出它。）关键的观察是：$H_n^0$ 对应于对均匀的 $s \in \{0,1\}^n$ 输出 $\hat{G}(s)$，而 $H_n^{p(n)}$ 对应于输出均匀的 $(n+p(n))$ 比特串。固定任意多项式时间区分器 D，这就意味着

$$
\begin{aligned}
&\left|\Pr_{s\leftarrow\{0,1\}^{n}}[D(\hat{G}(s))=1]-\Pr_{r\leftarrow\{0,1\}^{n+p(n)}}[D(r)=1]\right|\\
&=\left|\Pr_{t\leftarrow H^{0}_{n}}[D(t)=1]-\Pr_{t\leftarrow H^{p(n)}_{n}}[D(t)=1]\right|. \tag{8.7}
\end{aligned}
$$

We prove the above is negligible, hence $\hat{G}$ is a pseudorandom generator.

我们证明上式可忽略，从而 $\hat{G}$ 是伪随机生成器。

Fix $D$ as above, and consider the distinguisher $D^{\prime}$ that does the following when given a string $w \in \{0,1\}^{n+1}$ as input:

固定如上的 D，考虑区分器 $D^{\prime}$：当给定串 $w \in \{0,1\}^{n+1}$ 作为输入时，它执行如下操作：

1. Choose uniform $j \in \{1, \ldots, p(n)\}$.

   均匀选取 $j \in \{1, \ldots, p(n)\}$。

2. Choose uniform $\sigma^{\prime}_j \in \{0,1\}^{j-1}$. (When $j = 1$ then $\sigma^{\prime}_j$ is the empty string.)

   均匀选取 $\sigma^{\prime}_j \in \{0,1\}^{j-1}$。（当 $j = 1$ 时，$\sigma^{\prime}_j$ 为空串。）

3. Set $t_j := w\|\sigma_j^{\prime}$. Then run $\hat{G}$ starting from iteration $j + 1$ to compute $t_{p(n)} \in \{0,1\}^{n+p(n)}$. Output $D(t_{p(n)})$.

   令 $t_j := w\|\sigma_j^{\prime}$。然后从第 $j + 1$ 次迭代开始运行 $\hat{G}$，计算出 $t_{p(n)} \in \{0,1\}^{n+p(n)}$，并输出 $D(t_{p(n)})$。

Clearly $D^{\prime}$ runs in polynomial time. Analyzing the behavior of $D^{\prime}$ is more complicated than before, although the underlying ideas are the same. Fix $n$ and say $D^{\prime}$ chooses $j = j^{*}$. If $w$ is uniform, then $t_{j^{*}}$ is uniform and so the distribution on $t \overset{\mathrm{def}}{=} t_{p(n)}$ is exactly that of distribution $H_{n}^{j^{*}}$. That is,

显然 $D^{\prime}$ 在多项式时间内运行。尽管背后的想法相同，但对 $D^{\prime}$ 行为的分析要比之前复杂一些。固定 $n$，设 $D^{\prime}$ 选中的是 $j = j^{*}$。若 $w$ 均匀，则 $t_{j^{*}}$ 均匀，于是 $t \overset{\mathrm{def}}{=} t_{p(n)}$ 恰好服从分布 $H_{n}^{j^{*}}$。也就是说，

$$
\Pr_{w\gets\{0,1\}^{n+1}}[D^{\prime}(w)=1\mid j=j^{*}]=\Pr_{t\gets H_{n}^{j^{*}}}[D(t)=1].
$$

Since each value for j is chosen with equal probability,

由于 $j$ 的每个取值都以相等的概率被选中，

$$
\begin{aligned}
\Pr_{w\leftarrow\{0,1\}^{n+1}}[D^{\prime}(w)=1]&=\frac{1}{p(n)}\cdot\sum_{j^{*}=1}^{p(n)}\Pr_{w\leftarrow\{0,1\}^{n+1}}[D^{\prime}(w)=1\mid j=j^{*}]\\
&=\frac{1}{p(n)}\cdot\sum_{j^{*}=1}^{p(n)}\Pr_{t\leftarrow H_{n}^{j^{*}}}[D(t)=1]. \tag{8.8}
\end{aligned}
$$

On the other hand, say $D^{\prime}$ chooses $j = j^*$ and $w = G(s)$ for uniform $s \in \{0,1\}^n$. Defining $t_{j^*-1} = s\|\sigma_{j^*}^{\prime}$, we see that $t_{j^*-1}$ is uniform and so the experiment involving $D^{\prime}$ is equivalent to running $\hat{G}$ from iteration $j^*$ to compute $t_{p(n)}$. That is, the distribution on $t \overset{\mathrm{def}}{=} t_{p(n)}$ is now exactly that of distribution $H_n^{j^*-1}$, and so

另一方面，设 $D^{\prime}$ 选中的是 $j = j^*$，且 $w = G(s)$（其中 $s \in \{0,1\}^n$ 均匀）。定义 $t_{j^*-1} = s\|\sigma_{j^*}^{\prime}$，可以看到 $t_{j^*-1}$ 均匀，于是涉及 $D^{\prime}$ 的实验就等价于从第 $j^*$ 次迭代开始运行 $\hat{G}$ 来计算 $t_{p(n)}$。也就是说，此时 $t \overset{\mathrm{def}}{=} t_{p(n)}$ 恰好服从分布 $H_n^{j^*-1}$，于是

$$
\Pr_{s\leftarrow\{0,1\}^{n}}[D^{\prime}(G(s))=1\mid j=j^{*}]=\Pr_{t\leftarrow H_{n}^{j^{*}-1}}[D(t)=1].
$$

Therefore,

因此，

$$
\begin{aligned}
\Pr_{s\leftarrow\{0,1\}^{n}}[D^{\prime}(G(s))=1]&=\frac{1}{p(n)}\cdot\sum_{j^{*}=1}^{p(n)}\Pr_{s\leftarrow\{0,1\}^{n}}[D^{\prime}(G(s))=1\mid j=j^{*}]\\
&=\frac{1}{p(n)}\cdot\sum_{j^{*}=1}^{p(n)}\Pr_{t\leftarrow H_{n}^{j^{*}-1}}[D(t)=1]\\
&=\frac{1}{p(n)}\cdot\sum_{j^{*}=0}^{p(n)-1}\Pr_{t\leftarrow H_{n}^{j^{*}}}[D(t)=1]. \tag{8.9}
\end{aligned}
$$

We can now analyze how well $D^{\prime}$ distinguishes outputs of G from random:

现在我们可以分析 $D^{\prime}$ 区分 $G$ 的输出与随机串的能力了：

$$
\begin{aligned}
&\left|\Pr_{s\leftarrow\{0,1\}^{n}}[D^{\prime}(G(s))=1]-\Pr_{w\leftarrow\{0,1\}^{n+1}}[D^{\prime}(w)=1]\right|\\
&=\frac{1}{p(n)}\cdot\left|\sum_{j^{*}=0}^{p(n)-1}\Pr_{t\leftarrow H_{n}^{j^{*}}}[D(t)=1]-\sum_{j^{*}=1}^{p(n)}\Pr_{t\leftarrow H_{n}^{j^{*}}}[D(t)=1]\right|\\
&=\frac{1}{p(n)}\cdot\left|\Pr_{t\leftarrow H_{n}^{0}}[D(t)=1]-\Pr_{t\leftarrow H_{n}^{p(n)}}[D(t)=1]\right|, \tag{8.10}
\end{aligned}
$$

relying on Equations (8.8) and (8.9) for the first equality. (The second equality holds because the same terms are included in each sum, except for the first term of the left sum and the last term of the right sum.) Since $G$ is a pseudorandom generator, the term on the left-hand side of Equation (8.10) is negligible; because $p$ is polynomial, this implies that Equation (8.7) is negligible, completing the proof that $\hat{G}$ is a pseudorandom generator.

其中第一个等号用了式 (8.8) 与式 (8.9)。（第二个等号成立是因为两个和式所含各项相同，只是左和式的第一项与右和式的最后一项除外。）由于 G 是伪随机生成器，式 (8.10) 左边的项是可忽略的；又因为 $p$ 是多项式，这就蕴含式 (8.7) 可忽略，从而完成了 $\hat{G}$ 是伪随机生成器的证明。

Putting it all together. Let $f$ be a one-way permutation. Taking the pseudorandom generator with expansion factor $n+1$ from Theorem 8.18, and increasing the expansion factor to $n+\ell$ using the approach from the proof of Theorem 8.19, we obtain the following pseudorandom generator $\hat{G}$:

**综合起来。**

设 $f$ 是单向置换。取定理 8.18 中扩展因子为 $n+1$ 的伪随机生成器，再按定理 8.19 证明中的方法把扩展因子提高到 $n+\ell$，我们就得到如下的伪随机生成器 $\hat{G}$：

$$
\hat{G}(s)=f^{(\ell)}(s)\parallel\mathsf{hc}(f^{(\ell-1)}(s))\parallel\cdots\parallel\mathsf{hc}(s),
$$

where $f^{(i)}$ refers to i-fold iteration of f. Note that $\hat{G}$ uses $\ell$ evaluations of f, and generates one pseudorandom bit per evaluation using the hard-core predicate hc.

其中 $f^{(i)}$ 表示 $f$ 的 $i$ 次迭代。注意，$\hat{G}$ 共对 $f$ 求 $\ell$ 次值，每次求值都用难核谓词 hc 生成一个伪随机比特。

Connection to stream ciphers. Recall from Section 3.6.1 that a stream cipher (without an IV) is defined by algorithms (Init, Next), where Init takes a seed $s \in \{0,1\}^n$ and returns initial state st, and Next takes as input the current state st and outputs a bit $\sigma$ and updated state st'. The construction $\hat{G}$ from the preceding proof fits nicely into this paradigm: take Init to be the trivial algorithm that outputs st = s, and define Next(st) to compute $G(st)$, parse the result as $st^{\prime}\|\sigma$ with $|st^{\prime}| = n$, and output the bit $\sigma$ and updated state st'. (If we use this stream cipher to generate $p(n)$ output bits starting from seed s, then we get exactly the final $p(n)$ bits of $\hat{G}(s)$ in reverse order.) The preceding proof shows that this yields a pseudorandom generator.

**与流密码的联系。**

回顾 3.6.1 节的内容：流密码（不带 IV）由算法对 (Init, Next) 定义，其中 Init 以种子 $s \in \{0,1\}^n$ 为输入并返回初始状态 st，Next 以当前状态 st 为输入，输出一个比特 $\sigma$ 和更新后的状态 st'。上面证明中的构造 $\hat{G}$ 恰好契合这一范式：取 Init 为输出 $st = s$ 的平凡算法，并定义 Next(st) 计算 $G(st)$，把结果解析为 $st^{\prime}\|\sigma$（其中 $|st^{\prime}| = n$），输出比特 $\sigma$ 与更新后的状态 st'。（如果我们用这个流密码从种子 $s$ 开始生成 $p(n)$ 个输出比特，那么得到的就是 $\hat{G}(s)$ 的最后 $p(n)$ 个比特的逆序。）前面的证明表明，这样得到的是一个伪随机生成器。

Hybrid arguments. A hybrid argument is a basic tool for proving indistinguishability when a primitive is (or several different primitives are) applied multiple times. Somewhat informally, the technique works by defining a series of intermediate “hybrid distributions” that bridge between two “extreme distributions” that we wish to prove indistinguishable. (In the proof above, these extreme distributions correspond to the output of $\hat{G}$ and a random string.) To apply the proof technique, three conditions should hold: First, the extreme distributions should match the original cases of interest. (In the proof above, $H_n^0$ was equal to the distribution induced by $\hat{G}$, while $H_n^{p(n)}$ was the uniform distribution.) Second, it must be possible to translate the capability of distinguishing consecutive hybrid distributions into breaking some underlying assumption. (Intuitively, we showed that distinguishing $H_n^i$ from $H_n^{i+1}$ was equivalent to distinguishing the output of $G$ from random.) Finally, the number of hybrid distributions should be polynomial. See also Theorem 8.31.

**混合论证。**

当某个原语（或若干不同的原语）被多次使用时，混合论证是证明不可区分性的基本工具。大致来说，这一技术的做法是定义一系列中间的“混合分布”，在我们希望证明不可区分的两个“极端分布”之间架起桥梁。（在上面的证明中，这两个极端分布分别对应于 $\hat{G}$ 的输出和一个随机串。）要运用这一证明技术，应满足三个条件：其一，极端分布应当与所关心的原始情形一致。（在上面的证明中，$H_n^0$ 等于 $\hat{G}$ 诱导的分布，而 $H_n^{p(n)}$ 是均匀分布。）其二，必须能够把区分相邻混合分布的能力转化为打破某个底层假设。（直观地说，我们证明了区分 $H_n^i$ 与 $H_n^{i+1}$ 等价于区分 $G$ 的输出与随机串。）其三，混合分布的数量应当是多项式的。另见定理 8.31。

## 8.5 Constructing Pseudorandom Functions　伪随机函数的构造

We now show how to construct a pseudorandom function from any (length-doubling) pseudorandom generator. Recall that a pseudorandom function is an efficiently computable, keyed function $F$ that is indistinguishable from a truly random function in the sense described in Section 3.5.1. For simplicity, we restrict our attention here to the case where $F$ is length preserving, meaning that for $k \in \{0,1\}^n$ the function $F_k$ maps $n$-bit inputs to $n$-bit outputs.

我们现在展示如何从任意（长度加倍的）伪随机生成器构造伪随机函数。回顾一下，伪随机函数是一个可高效计算的带密钥函数 $F$，在 3.5.1 节所述的意义下它与真随机函数不可区分。为简单起见，这里我们只考虑 $F$ 保持长度的情形，也就是说，对 $k \in \{0,1\}^n$，函数 $F_k$ 把 n 比特输入映射为 n 比特输出。

A length-preserving pseudorandom function can be viewed, informally, as a pseudorandom generator with expansion factor $n \cdot 2^n$; given such a pseudorandom generator $G$ we could define $F_k(i)$ (for ${0} \leq i < 2^n$) to be the $i$th $n$-bit block of $G(k)$. One reason this does not work is that $F$ must be efficiently computable; there are exponentially many blocks, and we need a way to compute the $i$th block without having to compute all other blocks. We show how to do this by computing “blocks” of the output by walking down a binary tree. We exemplify the idea by first showing a pseudorandom function taking 2-bit inputs.

保长度的伪随机函数可以非正式地看作扩展因子为 $n \cdot 2^n$ 的伪随机生成器：给定这样的伪随机生成器 $G$，我们可以把 $F_k(i)$（${0} \leq i < 2^n$）定义为 $G(k)$ 的第 $i$ 个 $n$ 比特块。这种做法行不通的一个原因在于：$F$ 必须能够高效计算；块的数目是指数多的，我们需要一种办法，不必算出其他所有块就能算出第 $i$ 块。我们将通过沿一棵二叉树向下行走、逐步算出输出的各个“块”来做到这一点。我们先以一个接受 2 比特输入的伪随机函数为例来展示这一想法。

Let $G$ be a pseudorandom generator with expansion factor ${2}n$. If we use $G$ as in the proof of Theorem 8.19 we can obtain a pseudorandom generator $\hat{G}$ with expansion factor ${4}n$ that uses three invocations of $G$. (We produce $n$ additional pseudorandom bits each time $G$ is applied.) If we define $F_{k}^{\prime}(i)$ (where ${0} \leq i < 4$ and $i$ is encoded as a 2-bit binary string) to be the $i$th block of $\hat{G}(k)$, then computation of $F_{k}^{\prime}(0)$ would require computing $\hat{G}$ in its entirety and hence three invocations of $G$. We show how to construct a pseudorandom function $F$ using only two invocations of $G$ on any input.

设 $G$ 是扩展因子为 ${2}n$ 的伪随机生成器。如果像定理 8.19 的证明中那样使用 $G$，我们可以得到扩展因子为 ${4}n$、调用三次 $G$ 的伪随机生成器 $\hat{G}$。（每应用一次 $G$ 就多产生 $n$ 个伪随机比特。）如果我们把 $F_{k}^{\prime}(i)$（其中 ${0} \leq i < 4$，且 $i$ 编码为 2 比特二进制串）定义为 $\hat{G}(k)$ 的第 $i$ 块，那么计算 $F_{k}^{\prime}(0)$ 就需要完整计算 $\hat{G}$，也就是要调用三次 $G$。我们将展示如何构造一个在任何输入上都只需调用两次 $G$ 的伪随机函数 $F$。

Let $G_0$ and $G_1$ be functions denoting the first and second halves of the output of $G$; i.e., $G(k) = G_0(k) \parallel G_1(k)$ where $|G_0(k)| = |G_1(k)| = |k|$. Define $F$ as follows:

设 $G_0$ 与 $G_1$ 分别表示 $G$ 输出的前一半与后一半这两个函数；也就是说，$G(k) = G_0(k) \parallel G_1(k)$，其中 $|G_0(k)| = |G_1(k)| = |k|$。如下定义 F：

$$
F_{k}(00)=G_{0}(G_{0}(k))\qquad F_{k}(10)=G_{0}(G_{1}(k))
$$

$$
F_{k}(01)=G_{1}(G_{0}(k))\qquad F_{k}(11)=G_{1}(G_{1}(k)).
$$

We claim that the four strings above are indistinguishable from four uniform, independent n-bit strings. (This suffices to prove that $F$ is pseudorandom.) Intuitively, this is because $G_0(k)\|G_1(k) = G(k)$ is pseudorandom and hence indistinguishable from a uniform ${2}n$-bit string $k_0\|k_1$. But then

我们断言：上面四个串与四个均匀且独立的 $n$ 比特串不可区分。（这足以证明 $F$ 是伪随机的。）直观上说，这是因为 $G_0(k)\|G_1(k) = G(k)$ 是伪随机的，因而与均匀的 ${2}n$ 比特串 $k_0\|k_1$ 不可区分。但是这样一来，

$$
G_{0}(G_{0}(k))\parallel G_{1}(G_{0}(k))\parallel G_{0}(G_{1}(k))\parallel G_{1}(G_{1}(k))
$$

is indistinguishable from

就与

$$
G_{0}(k_{0})\parallel G_{1}(k_{0})\parallel G_{0}(k_{1})\parallel G_{1}(k_{1})=G(k_{0})\parallel G(k_{1}).
$$

Since $G$ is a pseudorandom generator, the above is indistinguishable from a uniform 4n-bit string. (A formal proof uses a hybrid argument.)

不可区分。由于 $G$ 是伪随机生成器，上面的串又与均匀的 4n 比特串不可区分。（形式化的证明需要用到混合论证。）

Generalizing this idea, we can obtain a pseudorandom function on n-bit inputs by defining

推广这一想法，我们可以通过定义

$$
F_{k}(x)=G_{x_{n}}(\cdots G_{x_{1}}(k)\cdots),
$$

where $x = x_1 \cdots x_n$; see Construction 8.20. The intuition for why this function is pseudorandom is the same as before, but the formal proof is complicated by the fact that there are now exponentially many inputs to consider.

得到 $n$ 比特输入上的伪随机函数，其中 $x = x_1 \cdots x_n$；见构造 8.20。这个函数为什么是伪随机的，其直觉与之前相同，但形式化证明变得复杂，原因在于现在需要考虑的输入有指数多个。

**CONSTRUCTION 8.20**

**构造 8.20**

Let $G$ be a pseudorandom generator with expansion factor $\ell(n) = 2n$, and define $G_0, G_1$ as in the text. For $k \in \{0,1\}^n$, define the function $F_k : \{0,1\}^n \to \{0,1\}^n$ as:

设 $G$ 是扩展因子为 $\ell(n) = 2n$ 的伪随机生成器，并如正文中所做的那样定义 $G_0, G_1$。对 $k \in \{0,1\}^n$，如下定义函数 $F_k : \{0,1\}^n \to \{0,1\}^n$：

$$
F_{k}(x_{1}x_{2}\cdots x_{n})=G_{x_{n}}\left(\cdots\left(G_{x_{2}}(G_{x_{1}}(k))\right)\right.\cdots).
$$

A pseudorandom function from a pseudorandom generator.

从伪随机生成器构造伪随机函数。

It is useful to view this construction as defining, for each key $k \in \{0,1\}^n$, a complete binary tree of depth $n$ in which each node contains an $n$-bit value. (See Figure 8.2, where $n = 3$.) The root has value $k$, and every non-leaf node with value $v$ has left child with value $G_0(v)$ and right child with value $G_1(v)$. The result $F_k(x)$ for $x = x_1 \cdots x_n$ is defined to be the value on the leaf node reached by traversing the tree according to the bits of $x$, where $x_i = 0$ means “go left” and $x_i = 1$ means “go right.” (The function is only defined for inputs of length $n$, and thus only values at the leaves are ever output.) The size of the tree is exponential in $n$. Nevertheless, to compute $F_k(x)$ the entire tree need not be constructed or stored; only $n$ evaluations of $G$ are needed.

不妨把这一构造看作：对每个密钥 $k \in \{0,1\}^n$，它定义了一棵深度为 $n$ 的完全二叉树，树中每个结点含有一个 $n$ 比特的值。（见图 8.2，其中 $n = 3$。）根的值为 $k$；每个值为 $v$ 的非叶结点，其左孩子的值为 $G_0(v)$，右孩子的值为 $G_1(v)$。对 $x = x_1 \cdots x_n$，结果 $F_k(x)$ 定义为按照 $x$ 的各比特遍历这棵树所到达的叶结点上的值：$x_i = 0$ 表示“向左走”，$x_i = 1$ 表示“向右走”。（该函数只对长度为 $n$ 的输入有定义，因而会被输出的只有叶结点上的值。）树的规模关于 $n$ 是指数级的。尽管如此，计算 $F_k(x)$ 既不需要构造也不需要存储整棵树，只需要对 $G$ 求 $n$ 次值即可。

![Image](https://lsky.jerryxue.top/i/2026/08/22/6a88f9eaa31fb.jpg)

**FIGURE 8.2: Constructing a pseudorandom function. / 图 8.2：构造一个伪随机函数**

THEOREM 8.21 If G is a pseudorandom generator with expansion factor $\ell(n) = 2n$, then Construction 8.20 is a pseudorandom function.

定理 8.21　若 $G$ 是扩展因子为 $\ell(n) = 2n$ 的伪随机生成器，则构造 8.20 是一个伪随机函数。

PROOF We first show that for any polynomial $t$ it is infeasible to distinguish $t(n)$ uniform ${2}n$-bit strings from $t(n)$ pseudorandom strings; i.e., for any polynomial $t$ and any PPT algorithm $A$, the following is negligible:

证明　我们首先证明：对任意多项式 $t$，区分 $t(n)$ 个均匀的 ${2}n$ 比特串与 $t(n)$ 个伪随机串是不可行的；也就是说，对任意多项式 $t$ 与任意概率多项式时间算法 $\mathcal{A}$，下式是可忽略的：

$$
\left|\Pr\left[A\left(r_{1}\|\cdots\|r_{t(n)}\right)=1\right]-\Pr\left[A\left(G(s_{1})\|\cdots\|G(s_{t(n)})\right)=1\right]\right|, \tag{8.11}
$$

where the first probability is over uniform choice of $r_1, \ldots, r_{t(n)} \in \{0,1\}^{2n}$, and the second probability is over uniform choice of $s_1, \ldots, s_{t(n)} \in \{0,1\}^n$.

其中第一个概率取遍均匀选取的 $r_1, \ldots, r_{t(n)} \in \{0,1\}^{2n}$，第二个概率取遍均匀选取的 $s_1, \ldots, s_{t(n)} \in \{0,1\}^n$。

The proof is by a hybrid argument. Fix a polynomial t and a PPT algorithm A, and consider the following algorithm $A^{\prime}:$

证明采用混合论证。固定多项式 $t$ 与概率多项式时间算法 $\mathcal{A}$，考虑如下算法 $A^{\prime}:$

Distinguisher A':

区分器 A'：

 $A^{\prime}$ is given as input a string $w \in \{0,1\}^{2n}$.

 $A^{\prime}$ 的输入是一个串 $w \in \{0,1\}^{2n}$。

1. Choose uniform $j \in \{1, \ldots, t(n)\}$.

   均匀选取 $j \in \{1, \ldots, t(n)\}$。

2. Choose uniform, independent values $r_1, \ldots, r_{j-1} \in \{0,1\}^{2n}$ and $s_{j+1}, \ldots, s_{t(n)} \in \{0,1\}^n$.

   均匀且独立地选取 $r_1, \ldots, r_{j-1} \in \{0,1\}^{2n}$ 以及 $s_{j+1}, \ldots, s_{t(n)} \in \{0,1\}^n$。

3. Output $A\left(r_{1}\|\cdots\|r_{j-1}\|w\|G(s_{j+1})\|\cdots\|G(s_{t(n)})\right)$.

   输出 $A\left(r_{1}\|\cdots\|r_{j-1}\|w\|G(s_{j+1})\|\cdots\|G(s_{t(n)})\right)$。

For any $n$ and ${0} \leq i \leq t(n)$, let $G_n^i$ denote the distribution on strings of length ${2}n \cdot t(n)$ in which the first $i$ “blocks” of length ${2}n$ are uniform and the remaining $t(n) - i$ blocks are pseudorandom. Note that $G_n^{t(n)}$ corresponds to the distribution in which all $t(n)$ blocks are uniform, while $G_n^0$ corresponds to the distribution in which all $t(n)$ blocks are pseudorandom. That is,

对任意 $n$ 与 ${0} \leq i \leq t(n)$，令 $G_n^i$ 表示长度 ${2}n \cdot t(n)$ 的串上的如下分布：其中前 $i$ 个长度为 ${2}n$ 的“块”是均匀的，其余 $t(n) - i$ 个块是伪随机的。注意：$G_n^{t(n)}$ 对应于全部 $t(n)$ 个块都均匀的分布，而 $G_n^0$ 对应于全部 $t(n)$ 个块都是伪随机的分布。也就是说，

$$
\begin{aligned}
&\left|\Pr_{y\leftarrow G_{n}^{t(n)}}[A(y)=1]-\Pr_{y\leftarrow G_{n}^{0}}[A(y)=1]\right|\\
&=\left|\Pr[A(r_{1},\ldots,r_{t(n)})=1]-\Pr[A(G(s_{1}),\ldots,G(s_{t(n)}))=1]\right|. \tag{8.12}
\end{aligned}
$$

Say $A^{\prime}$ chooses $j = j^{*}$. If its input $w$ is a uniform ${2}n$-bit string, then $A$ is run on an input distributed according to $G_{n}^{j^{*}}$. If, on the other hand, $w = G(s)$ for uniform $s$, then $A$ is run on an input distributed according to $G_{n}^{j^{*}-1}$. This means that

设 $A^{\prime}$ 选中的是 $j = j^{*}$。若其输入 $w$ 是均匀的 ${2}n$ 比特串，则 $A$ 的输入服从分布 $G_{n}^{j^{*}}$。反之，若 $w = G(s)$（其中 $s$ 均匀），则 $A$ 的输入服从分布 $G_{n}^{j^{*}-1}$。这意味着

$$
\Pr_{r\leftarrow\{0,1\}^{2n}}[A^{\prime}(r)=1]=\frac{1}{t(n)}\cdot\sum_{j=1}^{t(n)}\Pr_{y\leftarrow G_{n}^{j}}[A(y)=1]
$$

and

以及

$$
\Pr_{s\leftarrow\{0,1\}^{n}}[A^{\prime}(G(s))=1]=\frac{1}{t(n)}\cdot\sum_{j=0}^{t(n)-1}\Pr_{y\leftarrow G_{n}^{j}}[A(y)=1].
$$

Therefore,

因此，

$$
\begin{aligned}
&\left|\Pr_{r\leftarrow\{0,1\}^{2n}}[A^{\prime}(r)=1]-\Pr_{s\leftarrow\{0,1\}^{n}}[A^{\prime}(G(s))=1]\right|\\
&=\frac{1}{t(n)}\cdot\left|\Pr_{y\leftarrow G_{n}^{t(n)}}[A(y)=1]-\Pr_{y\leftarrow G_{n}^{0}}[A(y)=1]\right|.
\end{aligned}
$$

Since $G$ is a pseudorandom generator and $A^{\prime}$ runs in polynomial time, we know that the left-hand side of Equation (8.12) must be negligible; because $t(n)$ is polynomial, this implies that the left-hand side of Equation (8.11) is negligible as well.

由于 $G$ 是伪随机生成器且 $A^{\prime}$ 在多项式时间内运行，我们知道式 (8.12) 的左边必定可忽略；又因为 $t(n)$ 是多项式，这就蕴含式 (8.11) 的左边也可忽略。

Turning to the crux of the proof, we now show that $F$ as in Construction 8.20 is a pseudorandom function. Let $D$ be an arbitrary PPT distinguisher that is given ${1}^n$ as input. We show that $D$ cannot distinguish between the case when it is given oracle access to a function that is equal to $F_k$ for a uniform $k$, or a function chosen uniformly from $\mathsf{Func}_n$. (See Section 3.5.1.) To do so, we use another hybrid argument. Here, we define distributions over $n$-bit values at the leaves of a complete binary tree of depth $n$. By associating each leaf of these binary trees with an $n$-bit input as in Construction 8.20, we can equivalently view these as distributions over functions mapping $n$-bit inputs to $n$-bit outputs. For any $n$ and ${0} \leq i \leq n$, let $H_n^i$ be the following distribution over the values at the leaves of a binary tree of depth $n$: first choose values for the nodes at level $i$ independently and uniformly from $\{0,1\}^n$. Then for every node at level $i$ or below with value $k$, its left child is given value $G_0(k)$ and its right child is given value $G_1(k)$. Note that $H_n^n$ corresponds to the distribution in which all values at the leaves are chosen uniformly and independently, and thus corresponds to choosing a uniform function from $\mathsf{Func}_n$, whereas $H_n^0$ corresponds to choosing a uniform key $k$ in Construction 8.20 since in that case only the value at the root (at level 0) is chosen uniformly. That is,

现在转到证明的核心部分：我们证明构造 8.20 中的 $F$ 是伪随机函数。设 $D$ 是任意的概率多项式时间区分器，其输入为 ${1}^n$。我们将证明：$D$ 无法区分以下两种情形——它获得的是对一个函数的预言机访问，该函数等于均匀的 $k$ 所对应的 $F_k$；或者该函数是从 $\mathsf{Func}_n$ 中均匀选出的。（见 3.5.1 节。）为此，我们再使用一次混合论证。这里，我们在深度为 $n$ 的完全二叉树的叶结点上定义 $n$ 比特值的分布。按照构造 8.20 的方式把这些二叉树的每个叶与一个 $n$ 比特输入相对应之后，我们可以等价地把它们视为“把 $n$ 比特输入映射到 $n$ 比特输出的函数”上的分布。对任意 $n$ 与 ${0} \leq i \leq n$，令 $H_n^i$ 为深度 $n$ 的二叉树叶结点值上的如下分布：首先从 $\{0,1\}^n$ 中独立、均匀地为第 $i$ 层的各结点取值；然后，对第 $i$ 层及以下每个值为 $k$ 的结点，令其左孩子取值 $G_0(k)$、右孩子取值 $G_1(k)$。注意：$H_n^n$ 对应于叶上所有值都独立均匀选取的分布，因而对应于从 $\mathsf{Func}_n$ 中均匀选出一个函数；而 $H_n^0$ 对应于在构造 8.20 中均匀选取密钥 $k$，因为此时只有根（第 0 层）的值是均匀选取的。也就是说，

$$
\begin{aligned}
&\left|\Pr_{k\leftarrow\{0,1\}^{n}}[D^{F_{k}(\cdot)}(1^{n})=1]-\Pr_{f\leftarrow\mathsf{Func}_{n}}[D^{f(\cdot)}(1^{n})=1]\right|\\
&=\left|\Pr_{f\leftarrow H^{0}_{n}}[D^{f(\cdot)}(1^{n})=1]-\Pr_{f\leftarrow H^{n}_{n}}[D^{f(\cdot)}(1^{n})=1]\right|. \tag{8.13}
\end{aligned}
$$

We show that Equation (8.13) is negligible, completing the proof.

我们证明式 (8.13) 可忽略，从而完成证明。

Let $t = t(n)$ be a polynomial upper bound on the number of queries D makes to its oracle on input ${1}^n$. Define a distinguisher A that tries to distinguish $t(n)$ uniform 2n-bit strings from $t(n)$ pseudorandom strings, as follows:

设 $t = t(n)$ 是 $D$ 在输入 ${1}^n$ 下对其预言机所做的查询次数的多项式上界。如下定义一个试图区分 $t(n)$ 个均匀的 2n 比特串与 $t(n)$ 个伪随机串的区分器 A：

**Distinguisher A:**

**区分器 A：**

A is given as input a ${2}n \cdot t(n)$-bit string $w_1 \parallel \cdots \parallel w_{t(n)}$.

$A$ 的输入是一个 ${2}n \cdot t(n)$ 比特的串 $w_1 \parallel \cdots \parallel w_{t(n)}$。

1. Choose uniform $j \in \{0, \ldots, n-1\}$. In what follows, $A$ (implicitly) maintains a binary tree of depth $n$ with $n$-bit values at (a subset of) the internal nodes at depth $j+1$ and below.

   均匀选取 $j \in \{0, \ldots, n-1\}$。在下文中，$A$（隐式地）维护一棵深度为 $n$ 的二叉树，在深度 $j+1$ 及以下的内部结点（的一个子集）上带有 $n$ 比特的值。

2. Run $D(1^n)$. When $D$ makes oracle query $x = x_1 \cdots x_n$, look at the prefix $x_1 \cdots x_j$. There are two cases:

   运行 $D(1^n)$。当 $D$ 进行预言机查询 $x = x_1 \cdots x_n$ 时，查看前缀 $x_1 \cdots x_j$。分两种情形：

If $D$ has never made a query with this prefix before, then use $x_1 \cdots x_j$ to reach a node $v$ on the $j$th level of the tree. Take the next unused ${2}n$-bit string $w$ and set the value of the left child of node $v$ to the first half of $w$, and the value of the right child of $v$ to the second half of $w$.

若 D 此前从未以这个前缀做过查询，则沿 $x_1 \cdots x_j$ 走到树的第 $j$ 层的结点 $v$。取下一个尚未使用的 ${2}n$ 比特串 $w$，把结点 $v$ 的左孩子的值置为 $w$ 的前一半，把 $v$ 的右孩子的值置为 $w$ 的后一半。

If $D$ has made a query with prefix $x_{1}\cdots x_{j}$ before, then node $x_{1}\cdots x_{j+1}$ has already been assigned a value.

若 $D$ 此前曾以前缀 $x_{1}\cdots x_{j}$ 做过查询，则结点 $x_{1}\cdots x_{j+1}$ 已经被赋过值。

Using the value at node $x_1 \cdots x_{j+1}$, compute the value at the leaf corresponding to $x_1 \cdots x_n$ as in Construction 8.20, and return this value to $D$.

利用结点 $x_1 \cdots x_{j+1}$ 上的值，按照构造 8.20 的方式计算出与 $x_1 \cdots x_n$ 相对应的叶结点上的值，并把该值返回给 D。

3. When execution of D is done, output the bit returned by D.

   当 D 执行结束后，输出 $D$ 返回的那个比特。

A runs in polynomial time. It is important here that A does not need to store the entire binary tree of exponential size. Instead, it “fills in” the values of at most ${2}t(n)$ nodes in the tree.

$A$ 在多项式时间内运行。这里的要点是：$A$ 不必存储整棵规模为指数级的二叉树，而只需“填入”树中至多 ${2}t(n)$ 个结点的值。

Say A chooses $j = j^{*}$. Observe that:

设 $A$ 选中的是 $j = j^{*}$。注意到：

1. If $A$'s input is a uniform ${2}n \cdot t(n)$-bit string, then the answers it gives to $D$ are distributed exactly as if $D$ were interacting with a function chosen from distribution $H_n^{j^{*}+1}$. This holds because the values of the nodes at level $j^{*}+1$ of the tree are uniform and independent.

   若 A 的输入是均匀的 ${2}n \cdot t(n)$ 比特串，则 $A$ 给予 $D$ 的回答所服从的分布，恰好就如同 $D$ 在与一个从分布 $H_n^{j^{*}+1}$ 中选出的函数进行交互。这是因为树中第 $j^{*}+1$ 层结点的值是独立且均匀的。

2. If $A$'s input consists of $t(n)$ pseudorandom strings—i.e., $w_i = G(s_i)$ for uniform seed $s_i$—then the answers it gives to $D$ are distributed exactly as if $D$ were interacting with a function chosen from distribution $H_n^{j^*}$. This holds because the values of the nodes at level $j^*$ of the tree (namely, the $\{s_i\}$) are uniform and independent. (The $\{s_i\}$ are unknown to $A$, but that makes no difference.)

   若 A 的输入由 $t(n)$ 个伪随机串组成——即 $w_i = G(s_i)$（其中种子 $s_i$ 均匀）——则 $A$ 给予 $D$ 的回答所服从的分布，恰好就如同 $D$ 在与一个从分布 $H_n^{j^*}$ 中选出的函数进行交互。这是因为树中第 $j^*$ 层结点的值（也就是 $\{s_i\}$）是均匀且独立的。（$A$ 并不知道 $\{s_i\}$，但这没有任何影响。）

Proceeding as before, one can show that

与前面一样地进行论证，可以证明

$$
\begin{aligned}
&\left|\Pr\left[A\left(r_{1}\|\cdots\|r_{t(n)}\right)=1\right]-\Pr\left[A\left(G(s_{1})\|\cdots\|G(s_{t(n)})\right)=1\right]\right|\\
&=\frac{1}{n}\cdot\left|\Pr_{f\leftarrow H^{0}_{n}}\lbrack D^{f(\cdot)}(1^{n})=1\rbrack-\Pr_{f\leftarrow H^{n}_{n}}\lbrack D^{f(\cdot)}(1^{n})=1\rbrack\right|. \tag{8.14}
\end{aligned}
$$

We have shown earlier that Equation (8.14) must be negligible. The above thus implies that Equation (8.13) must be negligible as well.

我们在前面已经证明式 (8.14) 必定可忽略。于是上式蕴含：式 (8.13) 也必定可忽略。
