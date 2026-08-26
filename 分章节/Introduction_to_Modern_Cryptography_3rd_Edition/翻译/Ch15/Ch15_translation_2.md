## 15.4 The Goldwasser–Micali Encryption Scheme　Goldwasser–Micali 加密方案

Before we present the Goldwasser–Micali encryption scheme, we need to develop a better understanding of quadratic residues. We first explore the easier case of quadratic residues modulo a prime $p$, and then look at the slightly more complicated case of quadratic residues modulo a composite $N$.

在介绍 Goldwasser–Micali 加密方案之前，我们需要对二次剩余有更深入的理解。先探讨较简单的情形——模素数 $p$ 的二次剩余，然后再看稍复杂的情形——模合数 $N$ 的二次剩余。

Throughout this section, $p$ and $q$ denote odd primes, and $N = pq$ denotes a product of two distinct, odd primes.

本节中，$p$ 和 $q$ 始终表示奇素数，$N = pq$ 表示两个不同奇素数的乘积。

### 15.4.1 Quadratic Residues Modulo a Prime　模素数二次剩余

In a group $\mathbb{G}$, an element $y \in \mathbb{G}$ is a quadratic residue if there exists an $x \in \mathbb{G}$ with $x^2 = y$. In this case, we call $x$ a square root of $y$. An element that is not a quadratic residue is called a quadratic non-residue. In an abelian group, the set of quadratic residues forms a subgroup.

在群 $\mathbb{G}$ 中，若存在 $x \in \mathbb{G}$ 使得 $x^2 = y$，则称元素 $y \in \mathbb{G}$ 为二次剩余，此时称 $x$ 为 $y$ 的一个平方根。不是二次剩余的元素称为二次非剩余。在阿贝尔群中，全体二次剩余构成一个子群。

In the specific case of $\mathbb{Z}_p^*$, we have that $y$ is a quadratic residue if there exists an $x$ with $x^2 = y \mod p$. We begin with an easy observation.

具体到 $\mathbb{Z}_p^*$ 的情形，$y$ 是二次剩余是指存在 $x$ 使得 $x^2 = y \mod p$。我们从一个简单的观察入手。

PROPOSITION 15.16 Let $p > 2$ be prime. Every quadratic residue in $\mathbb{Z}_{p}^{*}$ has exactly two square roots.

命题 15.16　设 $p > 2$ 为素数。$\mathbb{Z}_{p}^{*}$ 中的每个二次剩余恰好有两个平方根。

PROOF This follows from Theorem 9.66, but we give a direct proof here. Let $y \in \mathbb{Z}_p^*$ be a quadratic residue. Then there exists an $x \in \mathbb{Z}_p^*$ such that $x^2 = y \bmod p$. Clearly, $(-x)^2 = x^2 = y \bmod p$. Furthermore, $-x \neq x \bmod p$: if $-x = x \bmod p$ then ${2}x = 0 \bmod p$, which implies $p \mid 2x$. Since $p$ is prime, this would mean that either $p \mid 2$ (which is impossible since $p > 2$) or $p \mid x$ (which is impossible since ${0} < x < p$). So, $[x \bmod p]$ and $[-x \bmod p]$ are distinct elements of $\mathbb{Z}_p^*$, and $y$ has at least two square roots.

证明　这可由定理 9.66 推出，但这里给出一个直接证明。设 $y \in \mathbb{Z}_p^*$ 是二次剩余，则存在 $x \in \mathbb{Z}_p^*$ 使得 $x^2 = y \bmod p$。显然 $(-x)^2 = x^2 = y \bmod p$。此外 $-x \neq x \bmod p$：若 $-x = x \bmod p$，则 ${2}x = 0 \bmod p$，即 $p \mid 2x$。由于 $p$ 是素数，这意味着要么 $p \mid 2$（不可能，因为 $p > 2$），要么 $p \mid x$（也不可能，因为 ${0} < x < p$）。因此 $[x \bmod p]$ 与 $[-x \bmod p]$ 是 $\mathbb{Z}_p^*$ 中两个不同的元素，$y$ 至少有两个平方根。

Let $x^{\prime} \in \mathbb{Z}_p^*$ be a square root of $y$. Then $x^2 = y = (x^{\prime})^2 \mod p$, implying that $x^2 - (x^{\prime})^2 = 0 \mod p$. Factoring the left-hand side we obtain

设 $x^{\prime} \in \mathbb{Z}_p^*$ 是 $y$ 的一个平方根。则 $x^2 = y = (x^{\prime})^2 \mod p$，从而 $x^2 - (x^{\prime})^2 = 0 \mod p$。对左端作因子分解，得到

$$
(x-x^{\prime})(x+x^{\prime})=0\bmod p,
$$

so that (by Proposition 9.3) either $p \mid (x - x^{\prime})$ or $p \mid (x + x^{\prime})$. In the first case, $x^{\prime} = x \mod p$ and in the second case $x^{\prime} = -x \mod p$, showing that $y$ indeed has only $\left[\pm x \mod p\right]$ as square roots.

于是（由命题 9.3）要么 $p \mid (x - x^{\prime})$，要么 $p \mid (x + x^{\prime})$。前者给出 $x^{\prime} = x \mod p$，后者给出 $x^{\prime} = -x \mod p$，这说明 $y$ 的平方根确实只有 $\left[\pm x \mod p\right]$。

Let $\mathsf{sq}_p : \mathbb{Z}_p^* \to \mathbb{Z}_p^*$ be the function $\mathsf{sq}_p(x) \overset{\mathrm{def}}{=} [x^2 \bmod p]$. The above shows that $\mathsf{sq}_p$ is a two-to-one function when $p > 2$ is prime. This immediately implies that exactly half the elements of $\mathbb{Z}_p^*$ are quadratic residues. We denote the set of quadratic residues modulo $p$ by $\mathcal{QR}_p$, and the set of quadratic non-residues by $\mathcal{QNR}_p$. We have just seen that for $p > 2$ prime

令 $\mathsf{sq}_p : \mathbb{Z}_p^* \to \mathbb{Z}_p^*$ 为函数 $\mathsf{sq}_p(x) \overset{\mathrm{def}}{=} [x^2 \bmod p]$。上述结果表明，当 $p > 2$ 为素数时 $\mathsf{sq}_p$ 是一个二对一函数。这立即说明 $\mathbb{Z}_p^*$ 中恰好一半的元素是二次剩余。记模 $p$ 的二次剩余集合为 $\mathcal{QR}_p$，二次非剩余集合为 $\mathcal{QNR}_p$。刚才已经看到，对素数 $p > 2$ 有

$$
\left|\mathcal{QR}_{p}\right|=\left|\mathcal{QNR}_{p}\right|=\frac{\left|\mathbb{Z}_{p}^{*}\right|}{2}=\frac{p-1}{2}.
$$

Define $\mathcal{J}_p(x)$, the Jacobi symbol of $x$ modulo $p$, as follows. $^4$ Let $p > 2$ be prime, and $x \in \mathbb{Z}_p^*$. Then

如下定义 $x$ 模 $p$ 的雅可比符号 $\mathcal{J}_p(x)$。$^4$ 设 $p > 2$ 为素数，$x \in \mathbb{Z}_p^*$。则

$$
\mathcal{J}_{p}(x)\stackrel{\mathrm{def}}{=}\left\{\begin{matrix}+1 & \text{if } x \text{ is a quadratic residue modulo } p\\ -1 & \text{if } x \text{ is not a quadratic residue modulo } p.\\ \end{matrix}\right.
$$

The notation can be extended in the natural way for any $x$ relatively prime to $p$ by setting $\mathcal{J}_p(x) \overset{\mathrm{def}}{=} \mathcal{J}_p([x \bmod p])$.

对任意与 $p$ 互素的 $x$，可令 $\mathcal{J}_p(x) \overset{\mathrm{def}}{=} \mathcal{J}_p([x \bmod p])$，将该记号自然地推广。

> $^4$ For $p$ prime, $\mathcal{J}_p(x)$ is also sometimes called the Legendre symbol of $x$ and denoted by $L_p(x)$; we have chosen our notation to be consistent with notation introduced later.

> $^4$ 当 $p$ 为素数时，$\mathcal{J}_p(x)$ 有时也称为 $x$ 的勒让德符号，记作 $L_p(x)$；我们选用这里的记号，是为了与后文引入的记号保持一致。

Can we characterize the quadratic residues in $\mathbb{Z}_p^*$? We begin with the fact that $\mathbb{Z}_p^*$ is a cyclic group of order $p-1$ (see Theorem 9.57). Let $g$ be a generator of $\mathbb{Z}_p^*$. This means that

如何刻画 $\mathbb{Z}_p^*$ 中的二次剩余？出发点是这样一个事实：$\mathbb{Z}_p^*$ 是 $p-1$ 阶循环群（见定理 9.57）。设 $g$ 是 $\mathbb{Z}_p^*$ 的生成元。这意味着

$$
\mathbb{Z}_{p}^{*}=\{g^{0},g^{1},g^{2},\ldots,g^{\frac{p-1}{2}-1},g^{\frac{p-1}{2}},g^{\frac{p-1}{2}+1},\ldots,g^{p-2}\}
$$

(recall that $p$ is odd, so $p-1$ is even). Squaring each element in this list and reducing modulo $p-1$ in the exponent (cf. Corollary 9.15) yields a list of all the quadratic residues in $\mathbb{Z}_p^*$:

（回忆 $p$ 是奇数，故 $p-1$ 是偶数。）把该列表中每个元素平方，并在指数上对 $p-1$ 取模（参见推论 9.15），就得到 $\mathbb{Z}_p^*$ 中全部二次剩余的列表：

$$
\mathcal{QR}_{p}=\{g^{0},g^{2},g^{4},\ldots,g^{p-3},g^{0},g^{2},\ldots,g^{p-3}\}.
$$

Each quadratic residue appears twice in this list. Therefore, the quadratic residues in $\mathbb{Z}_p^*$ are exactly those elements that can be written as $g^i$ with $i \in \{0, \ldots, p-2\}$ an even integer.

每个二次剩余在该列表中都出现两次。因此，$\mathbb{Z}_p^*$ 中的二次剩余恰好是那些可以写成 $g^i$（其中 $i \in \{0, \ldots, p-2\}$ 为偶数）的元素。

The above characterization leads to a simple way to compute the Jacobi symbol and thus tell whether an element $x \in \mathbb{Z}_p^*$ is a quadratic residue or not.

上述刻画给出了一种计算雅可比符号的简单方法，从而可以判定元素 $x \in \mathbb{Z}_p^*$ 是否为二次剩余。

PROPOSITION 15.17 Let $p > 2$ be a prime. Then $\mathcal{J}_p(x) = x^{\frac{p-1}{2}} \bmod p$.

命题 15.17　设 $p > 2$ 为素数。则 $\mathcal{J}_p(x) = x^{\frac{p-1}{2}} \bmod p$。

PROOF Let $g$ be an arbitrary generator of $\mathbb{Z}_p^*$. If $x$ is a quadratic residue modulo $p$, our earlier discussion shows that $x = g^i$ for some even integer $i$. Writing $i = 2j$ with $j$ an integer we then have

证明　任取 $\mathbb{Z}_p^*$ 的生成元 $g$。若 $x$ 是模 $p$ 的二次剩余，由前面的讨论可知 $x = g^i$，其中 $i$ 为某个偶数。记 $i = 2j$（$j$ 为整数），则有

$$x^{\frac{p-1}{2}}=\left(g^{2j}\right)^{\frac{p-1}{2}}=g^{(p-1)j}=\left(g^{p-1}\right)^{j}=1^{j}=1\bmod p,$$

and so $x^{\frac{p-1}{2}} = +1 = \mathcal{J}_p(x) \bmod p$ as claimed.

于是 $x^{\frac{p-1}{2}} = +1 = \mathcal{J}_p(x) \bmod p$，即得所证。

On the other hand, if $x$ is not a quadratic residue then $x = g^{i}$ for some odd integer $i$. Writing $i = 2j + 1$ with $j$ an integer, we have

另一方面，若 $x$ 不是二次剩余，则 $x = g^{i}$，其中 $i$ 为某个奇数。记 $i = 2j + 1$（$j$ 为整数），则有

$$x^{\frac{p-1}{2}}=\left(g^{2j+1}\right)^{\frac{p-1}{2}}=\left(g^{2j}\right)^{\frac{p-1}{2}}\cdot g^{\frac{p-1}{2}}=1\cdot g^{\frac{p-1}{2}}=g^{\frac{p-1}{2}}\bmod p.$$

Now,

而

$$\left(g^{\frac{p-1}{2}}\right)^{2}=g^{p-1}=1\bmod p,$$

and so $g^{\frac{p-1}{2}} = \pm1 \bmod p$ since $[\pm1 \bmod p]$ are the two square roots of 1 (cf. Proposition 15.16). Since $g$ is a generator, it has order $p - 1$ and so $g^{\frac{p-1}{2}} \neq 1 \bmod p$. It follows that $x^{\frac{p-1}{2}} = -1 = \mathcal{J}_p(x) \bmod p$.

故 $g^{\frac{p-1}{2}} = \pm1 \bmod p$，因为 $[\pm1 \bmod p]$ 是 1 的两个平方根（参见命题 15.16）。由于 $g$ 是生成元，其阶为 $p - 1$，所以 $g^{\frac{p-1}{2}} \neq 1 \bmod p$。由此可得 $x^{\frac{p-1}{2}} = -1 = \mathcal{J}_p(x) \bmod p$。

Proposition 15.17 directly gives a polynomial-time algorithm (cf. Algorithm 15.18) for testing whether an element $x \in \mathbb{Z}_p^*$ is a quadratic residue.

命题 15.17 直接给出了一个多项式时间算法（参见算法 15.18），用于检验元素 $x \in \mathbb{Z}_p^*$ 是否为二次剩余。

ALGORITHM 15.18
Deciding quadratic residuosity modulo a prime

Input: A prime $p$; an element $x \in \mathbb{Z}_p^*$

Output: $\mathcal{J}_p(x)$ (or, equivalently, whether $x$ is a quadratic residue or quadratic non-residue)

$b := \left[ x^{\frac{p-1}{2}} \mod p \right]$

if $b = 1$ return “quadratic residue”

else return “quadratic non-residue”

算法 15.18
判定模素数的二次剩余性

输入：素数 $p$；元素 $x \in \mathbb{Z}_p^*$

输出：$\mathcal{J}_p(x)$（或等价地，$x$ 是二次剩余还是二次非剩余）

$b := \left[ x^{\frac{p-1}{2}} \mod p \right]$

若 $b = 1$ 则返回“二次剩余”

否则返回“二次非剩余”

We conclude this section by noting a nice multiplicative property of quadratic residues and non-residues modulo p.

本节最后指出模 $p$ 的二次剩余与二次非剩余所具有的一个很好的乘法性质。

PROPOSITION 15.19 Let $p > 2$ be a prime, and $x, y \in \mathbb{Z}_p^*$. Then

命题 15.19　设 $p > 2$ 为素数，$x, y \in \mathbb{Z}_p^*$。则

$$\mathcal{J}_{p}(x y)=\mathcal{J}_{p}(x)\cdot\mathcal{J}_{p}(y).$$

PROOF Using the previous proposition.

证明　利用上一命题，有

 $\mathcal{J}_p(xy) = (xy)^{\frac{p-1}{2}} = x^{\frac{p-1}{2}} \cdot y^{\frac{p-1}{2}} = \mathcal{J}_p(x) \cdot \mathcal{J}_p(y) \mod p.$

Since $\mathcal{J}_{p}(xy), \mathcal{J}_{p}(x), \mathcal{J}_{p}(y) = \pm1$, equality holds over the integers as well.

由于 $\mathcal{J}_{p}(xy), \mathcal{J}_{p}(x), \mathcal{J}_{p}(y) = \pm1$，该等式在整数上也成立。

COROLLARY 15.20 Let $p > 2$ be prime, and say $x, x^{\prime} \in \mathcal{QR}_p$ and $y, y^{\prime} \in \mathcal{QNR}_p$. Then:

推论 15.20　设 $p > 2$ 为素数，且 $x, x^{\prime} \in \mathcal{QR}_p$、$y, y^{\prime} \in \mathcal{QNR}_p$。则：

1. $[xx^{\prime} \bmod p] \in \mathcal{QR}_p$.

   $[xx^{\prime} \bmod p] \in \mathcal{QR}_p$。

2. $[yy^{\prime} \bmod p] \in \mathcal{QR}_p$.

   $[yy^{\prime} \bmod p] \in \mathcal{QR}_p$。

3. $[xy \bmod p] \in \mathcal{QNR}_p$.

   $[xy \bmod p] \in \mathcal{QNR}_p$。

### 15.4.2 Quadratic Residues Modulo a Composite　模合数二次剩余

We now turn our attention to quadratic residues in the group $\mathbb{Z}_N^*$, where $N = pq$. Characterizing the quadratic residues modulo $N$ is easy if we use the results of the previous section in conjunction with the Chinese remainder theorem. Recall that the Chinese remainder theorem says that $\mathbb{Z}_N^* \simeq \mathbb{Z}_p^* \times \mathbb{Z}_q^*$, and we let $y \leftrightarrow (y_p, y_q)$ denote the correspondence guaranteed by the theorem (i.e., $y_p = [y \mod p]$ and $y_q = [y \mod q]$). The key observation is:

现在把目光转向群 $\mathbb{Z}_N^*$ 中的二次剩余，其中 $N = pq$。如果把上一节的结果与中国剩余定理结合起来，刻画模 $N$ 的二次剩余就很容易了。回忆一下，中国剩余定理表明 $\mathbb{Z}_N^* \simeq \mathbb{Z}_p^* \times \mathbb{Z}_q^*$，我们用 $y \leftrightarrow (y_p, y_q)$ 表示该定理所保证的对应关系（即 $y_p = [y \mod p]$、$y_q = [y \mod q]$）。关键的观察是：

PROPOSITION 15.21 Let $N = pq$ with $p, q$ distinct primes, and $y \in \mathbb{Z}_N^*$ with $y \leftrightarrow (y_p, y_q)$. Then $y$ is a quadratic residue modulo $N$ if and only if $y_p$ is a quadratic residue modulo $p$ and $y_q$ is a quadratic residue modulo $q$.

命题 15.21　设 $N = pq$，其中 $p, q$ 为不同的素数，$y \in \mathbb{Z}_N^*$ 且 $y \leftrightarrow (y_p, y_q)$。则 $y$ 是模 $N$ 的二次剩余，当且仅当 $y_p$ 是模 $p$ 的二次剩余且 $y_q$ 是模 $q$ 的二次剩余。

PROOF If $y$ is a quadratic residue modulo $N$ then, by definition, there exists an $x \in \mathbb{Z}_N^*$ such that $x^2 = y \bmod N$. Let $x \leftrightarrow (x_p, x_q)$. Then

证明　若 $y$ 是模 $N$ 的二次剩余，则由定义，存在 $x \in \mathbb{Z}_N^*$ 使得 $x^2 = y \bmod N$。设 $x \leftrightarrow (x_p, x_q)$。则

$$(y_{p},y_{q})\leftrightarrow y=x^{2}\leftrightarrow(x_{p},x_{q})^{2}=([x_{p}^{2}\bmod p],[x_{q}^{2}\bmod q]),$$

where $(x_p, x_q)^2$ is simply the square of the element $(x_p, x_q)$ in the group $\mathbb{Z}_p^* \times \mathbb{Z}_q^*$. We have thus shown that:

其中 $(x_p, x_q)^2$ 就是元素 $(x_p, x_q)$ 在群 $\mathbb{Z}_p^* \times \mathbb{Z}_q^*$ 中的平方。于是我们证明了：

$$y_{p}=x_{p}^{2}\bmod p\quad\text{and}\quad y_{q}=x_{q}^{2}\bmod q \tag{15.4}$$

and $y_{p}, y_{q}$ are quadratic residues (with respect to the appropriate moduli).

即 $y_{p}, y_{q}$ 是（相应模数下的）二次剩余。

Conversely, if $y \leftrightarrow (y_p, y_q)$ and $y_p, y_q$ are quadratic residues modulo $p$ and $q$, respectively, then there exist $x_p \in \mathbb{Z}_p^*$ and $x_q \in \mathbb{Z}_q^*$ such that Equation (15.4) holds. Let $x \in \mathbb{Z}_N^*$ be such that $x \leftrightarrow (x_p, x_q)$. Reversing the above steps shows that $x$ is a square root of $y$ modulo $N$.

反之，若 $y \leftrightarrow (y_p, y_q)$ 且 $y_p, y_q$ 分别是模 $p$ 和模 $q$ 的二次剩余，则存在 $x_p \in \mathbb{Z}_p^*$ 和 $x_q \in \mathbb{Z}_q^*$ 使式 (15.4) 成立。取 $x \in \mathbb{Z}_N^*$ 满足 $x \leftrightarrow (x_p, x_q)$。把上述步骤倒过来走一遍，即可说明 $x$ 是 $y$ 模 $N$ 的平方根。

The above proposition characterizes the quadratic residues modulo $N$. A careful examination of the proof yields another important observation: each quadratic residue $y \in \mathbb{Z}_N^*$ has exactly four square roots. To see this, let $y \leftrightarrow (y_p, y_q)$ be a quadratic residue modulo $N$ and let $x_p, x_q$ be square roots of $y_p$ and $y_q$ modulo $p$ and $q$, respectively. Then the four square roots of $y$ are given by the elements in $\mathbb{Z}_N^*$ corresponding to:

上述命题刻画了模 $N$ 的二次剩余。仔细考察其证明还能得到另一个重要观察：每个二次剩余 $y \in \mathbb{Z}_N^*$ 恰好有四个平方根。为看清这一点，设 $y \leftrightarrow (y_p, y_q)$ 是模 $N$ 的二次剩余，$x_p, x_q$ 分别是 $y_p$ 模 $p$ 和 $y_q$ 模 $q$ 的平方根。那么 $y$ 的四个平方根就是 $\mathbb{Z}_N^*$ 中与以下各组对应的元素：

$$(x_{p},x_{q}),\quad(-x_{p},x_{q}),\quad(x_{p},-x_{q}),\quad(-x_{p},-x_{q}). \tag{15.5}$$

Each of these is a square root of y since

其中每一个都是 y 的平方根，因为

$$\begin{align*}(\pm x_{p},\pm x_{q})^{2}&=\Big([(\pm x_{p})^{2}\bmod p],[(\pm x_{q})^{2}\bmod q]\Big)\\&=([x_{p}^{2}\bmod p],[x_{q}^{2}\bmod q])=(y_{p},y_{q})\leftrightarrow y\end{align*}$$

(where again the notation $(\cdot,\cdot)^2$ refers to squaring in the group $\mathbb{Z}_p \times \mathbb{Z}_q$). The Chinese remainder theorem guarantees that the four elements in Equation (15.5) correspond to distinct elements of $\mathbb{Z}_N^*$, since $x_p$ and $-x_p$ are unique modulo $p$ (and similarly for $x_q$ and $-x_q$ modulo $q$).

（这里记号 $(\cdot,\cdot)^2$ 同样指在群 $\mathbb{Z}_p \times \mathbb{Z}_q$ 中取平方。）中国剩余定理保证式 (15.5) 中的四个元素对应 $\mathbb{Z}_N^*$ 中互不相同的元素，因为 $x_p$ 与 $-x_p$ 在模 $p$ 下互不相同（$x_q$ 与 $-x_q$ 在模 $q$ 下同理）。

**Example 15.22**

**例 15.22**

Consider $\mathbb{Z}_{15}^*$ (the correspondence given by the Chinese remainder theorem is tabulated in Example 9.25). Element 4 is a quadratic residue modulo 15 with square root 2. Since ${2} \leftrightarrow (2,2)$, the other square roots of 4 are given by

考虑 $\mathbb{Z}_{15}^*$（中国剩余定理给出的对应关系已在例 9.25 中列成表）。元素 4 是模 15 的二次剩余，其平方根为 2。由于 ${2} \leftrightarrow (2,2)$，4 的其余平方根为

 $\bullet (2, [-2 \mod 3]) = (2, 1) \leftrightarrow 7;$

 $\bullet (2, [-2 \mod 3]) = (2, 1) \leftrightarrow 7$；

 $\bullet$ ([-2 mod 5], 2) = (3, 2) $\leftrightarrow$ 8; and

 $\bullet$ ([-2 mod 5], 2) = (3, 2) $\leftrightarrow$ 8；

 $\bullet\left([-2\bmod5],[-2\bmod3]\right)=(3,1)\leftrightarrow13.$

 $\bullet\left([-2\bmod5],[-2\bmod3]\right)=(3,1)\leftrightarrow13$。

One can verify that ${7}^{2} = 8^{2} = 13^{2} = 4 \mod 15$.

可以验证 ${7}^{2} = 8^{2} = 13^{2} = 4 \mod 15$。

Let $\mathcal{QR}_N$ denote the set of quadratic residues modulo $N$. Since squaring modulo $N$ is a four-to-one function, we see that exactly 1/4 of the elements of $\mathbb{Z}_N^*$ are quadratic residues. Alternately, we could note that since $y \in \mathbb{Z}_N^*$ is a quadratic residue if and only if $y_p, y_q$ are quadratic residues, there is a one-to-one correspondence between $\mathcal{QR}_N$ and $\mathcal{QR}_p \times \mathcal{QR}_q$. Thus, the fraction of quadratic residues modulo $N$ is,

记 $\mathcal{QR}_N$ 为模 $N$ 的二次剩余集合。由于模 $N$ 取平方是四对一函数，可见 $\mathbb{Z}_N^*$ 中恰好 1/4 的元素是二次剩余。或者也可以这样看：$y \in \mathbb{Z}_N^*$ 是二次剩余当且仅当 $y_p, y_q$ 都是二次剩余，因此 $\mathcal{QR}_N$ 与 $\mathcal{QR}_p \times \mathcal{QR}_q$ 之间存在一一对应。于是，模 $N$ 的二次剩余所占比例为

$$\frac{|\mathcal{QR}_{N}|}{|\mathbb{Z}_{N}^{*}|}=\frac{|\mathcal{QR}_{p}|\cdot|\mathcal{QR}_{q}|}{|\mathbb{Z}_{N}^{*}|}=\frac{\frac{p-1}{2}\cdot\frac{q-1}{2}}{(p-1)(q-1)}=\frac{1}{4},$$

in agreement with the above.

与上面的结论一致。

![Image](https://lsky.jerryxue.top/i/2026/08/25/6a8d87031b82d.jpg)

**FIGURE 15.1: The structure of $\mathbb{Z}_p^*$ and $\mathbb{Z}_N^*$. / 图 15.1：$\mathbb{Z}_p^*$ 与 $\mathbb{Z}_N^*$ 的结构**

In the previous section, we defined the Jacobi symbol $\mathcal{J}_p(x)$ for $p > 2$ prime. We extend the definition to the case of $N$ a product of distinct, odd primes $p$ and $q$ as follows. For any $x$ relatively prime to $N = pq$,

上一节对素数 $p > 2$ 定义了雅可比符号 $\mathcal{J}_p(x)$。现在把该定义推广到 $N$ 为不同奇素数 $p$ 与 $q$ 之积的情形。对任意与 $N = pq$ 互素的 $x$，定义

$$\begin{align*}\mathcal{J}_{N}(x)&\stackrel{\mathrm{def}}{=}\mathcal{J}_{p}(x)\cdot\mathcal{J}_{q}(x)\\&=\mathcal{J}_{p}([x\bmod p])\cdot\mathcal{J}_{q}([x\bmod q]).\end{align*}$$

We define $\mathcal{J}_N^{+1}$ as the set of elements in $\mathbb{Z}_N^*$ having Jacobi symbol +1, and define $\mathcal{J}_N^{-1}$ analogously.

我们把 $\mathbb{Z}_N^*$ 中雅可比符号为 +1 的元素构成的集合记作 $\mathcal{J}_N^{+1}$，并类似地定义 $\mathcal{J}_N^{-1}$。

We know from Proposition 15.21 that if $x$ is a quadratic residue modulo $N$, then $[x \bmod p]$ and $[x \bmod q]$ are quadratic residues modulo $p$ and $q$, respectively; that is, $\mathcal{J}_p(x) = \mathcal{J}_q(x) = +1$. So $\mathcal{J}_N(x) = +1$ and we see that:

由命题 15.21 可知，若 $x$ 是模 $N$ 的二次剩余，则 $[x \bmod p]$ 和 $[x \bmod q]$ 分别是模 $p$ 和模 $q$ 的二次剩余；也就是说 $\mathcal{J}_p(x) = \mathcal{J}_q(x) = +1$。于是 $\mathcal{J}_N(x) = +1$，由此可见：

If $x$ is a quadratic residue modulo $N$, then $\mathcal{J}_{N}(x) = +1$.

若 $x$ 是模 $N$ 的二次剩余，则 $\mathcal{J}_{N}(x) = +1$。

However, $\mathcal{J}_N(x) = +1$ can also occur when $\mathcal{J}_p(x) = \mathcal{J}_q(x) = -1$, that is, when both $[x \bmod p]$ and $[x \bmod q]$ are not quadratic residues modulo $p$ and $q$ (and so $x$ is not a quadratic residue modulo $N$). This turns out to be useful for the Goldwasser–Micali encryption scheme, and we therefore introduce the notation $\mathcal{QNR}_{N}^{+1}$ for the set of elements of this type. That is,

然而，当 $\mathcal{J}_p(x) = \mathcal{J}_q(x) = -1$ 时同样有 $\mathcal{J}_N(x) = +1$，也就是说 $[x \bmod p]$ 和 $[x \bmod q]$ 分别不是模 $p$ 和模 $q$ 的二次剩余（因而 $x$ 也不是模 $N$ 的二次剩余）。这一事实对 Goldwasser–Micali 加密方案很有用，因此我们引入记号 $\mathcal{QNR}_{N}^{+1}$ 来表示这类元素构成的集合。即

$$\begin{array}{r}{\mathcal{QNR}_{N}^{+1}\overset{\mathrm{def}}{=}\left\{x\in\mathbb{Z}_{N}^{*}\Big|\begin{array}{r l}{x\mathrm{~is~not~a~quadratic~residue~modulo~}N,}\\ {\mathrm{but~}\mathcal{J}_{N}(x)=+1}\end{array}\right\}.}\end{array}$$

It is now easy to prove the following (see Figure 15.1):

现在很容易证明以下结论（参见图 15.1）：

PROPOSITION 15.23 Let $N = pq$ with $p, q$ distinct, odd primes. Then:

命题 15.23　设 $N = pq$，其中 $p, q$ 为不同的奇素数。则：

1. Exactly half the elements of $\mathbb{Z}_N^*$ are in $\mathcal{J}_N^{+1}$.

   $\mathbb{Z}_N^*$ 中恰好一半的元素属于 $\mathcal{J}_N^{+1}$。

2. $\mathcal{QR}_{N}$ is contained in $\mathcal{J}_{N}^{+1}$.

   $\mathcal{QR}_{N}$ 包含于 $\mathcal{J}_{N}^{+1}$。

3. Exactly half the elements of $\mathcal{J}_{N}^{+1}$ are in $\mathcal{QR}_{N}$ (the other half are in $\mathcal{QNR}_{N}^{+1}$).

   $\mathcal{J}_{N}^{+1}$ 中恰好一半的元素属于 $\mathcal{QR}_{N}$（另一半属于 $\mathcal{QNR}_{N}^{+1}$）。

PROOF We know that $\mathcal{J}_N(x) = +1$ if either $\mathcal{J}_p(x) = \mathcal{J}_q(x) = +1$ or $\mathcal{J}_p(x) = \mathcal{J}_q(x) = -1$. We also know (from the previous section) that exactly half the elements of $\mathbb{Z}_p^*$ have Jacobi symbol +1, and half have Jacobi symbol -1 (and similarly for $\mathbb{Z}_q^*$). Defining $\mathcal{J}_p^{+1}$, $\mathcal{J}_p^{-1}$, $\mathcal{J}_q^{+1}$, and $\mathcal{J}_q^{-1}$ in the natural way, we thus have

证明　我们知道，当 $\mathcal{J}_p(x) = \mathcal{J}_q(x) = +1$ 或 $\mathcal{J}_p(x) = \mathcal{J}_q(x) = -1$ 时都有 $\mathcal{J}_N(x) = +1$。由上一节又知，$\mathbb{Z}_p^*$ 中恰好一半的元素雅可比符号为 +1，另一半为 -1（$\mathbb{Z}_q^*$ 同理）。按自然的方式定义 $\mathcal{J}_p^{+1}$、$\mathcal{J}_p^{-1}$、$\mathcal{J}_q^{+1}$ 和 $\mathcal{J}_q^{-1}$，于是有

$$\begin{align*}\left|\mathcal{J}_{N}^{+1}\right|&=\left|\mathcal{J}_{p}^{+1}\times\mathcal{J}_{q}^{+1}\right|+\left|\mathcal{J}_{p}^{-1}\times\mathcal{J}_{q}^{-1}\right|\\&=\left|\mathcal{J}_{p}^{+1}\right|\cdot\left|\mathcal{J}_{q}^{+1}\right|+\left|\mathcal{J}_{p}^{-1}\right|\cdot\left|\mathcal{J}_{q}^{-1}\right|\\&=\frac{(p-1)}{2}\frac{(q-1)}{2}+\frac{(p-1)}{2}\frac{(q-1)}{2}=\frac{\phi(N)}{2}.\end{align*}$$

So $|\mathcal{J}_{N}^{+1}| = |\mathbb{Z}_{N}^{*} |/2$, proving that half the elements of $\mathbb{Z}_{N}^{*}$ are in $\mathcal{J}_{N}^{+1}$.

所以 $|\mathcal{J}_{N}^{+1}| = |\mathbb{Z}_{N}^{*} |/2$，这就证明了 $\mathbb{Z}_{N}^{*}$ 中一半的元素属于 $\mathcal{J}_{N}^{+1}$。

We have noted earlier that all quadratic residues modulo $N$ have Jacobi symbol $+1$, showing that $\mathcal{QR}_N \subseteq \mathcal{J}_N^{+1}$.

前面已经指出，模 $N$ 的二次剩余的雅可比符号都是 $+1$，这说明 $\mathcal{QR}_N \subseteq \mathcal{J}_N^{+1}$。

Since $x \in \mathcal{QR}_N$ if and only if $\mathcal{J}_p(x) = \mathcal{J}_q(x) = +1$, we have:

由于 $x \in \mathcal{QR}_N$ 当且仅当 $\mathcal{J}_p(x) = \mathcal{J}_q(x) = +1$，我们有

$$|\mathcal{QR}_{N}|=|\mathcal{J}_{p}^{+1}\times\mathcal{J}_{q}^{+1}|=\frac{(p-1)}{2}\frac{(q-1)}{2}=\frac{\phi(N)}{4},$$

and so $|\mathcal{QR}_N| = |\mathcal{J}_N^{+1}|/2$. Since $\mathcal{QR}_N$ is a subset of $\mathcal{J}_N^{+1}$, this proves that half the elements of $\mathcal{J}_N^{+1}$ are in $\mathcal{QR}_N$.

从而 $|\mathcal{QR}_N| = |\mathcal{J}_N^{+1}|/2$。又因为 $\mathcal{QR}_N$ 是 $\mathcal{J}_N^{+1}$ 的子集，这就证明了 $\mathcal{J}_{N}^{+1}$ 中一半的元素属于 $\mathcal{QR}_N$。

The next two results are analogues of Proposition 15.19 and Corollary 15.20.

接下来两个结果是命题 15.19 和推论 15.20 的对应版本。

PROPOSITION 15.24 Let $N = pq$ be a product of distinct, odd primes, and $x, y \in \mathbb{Z}_N^*$. Then $\mathcal{J}_N(xy) = \mathcal{J}_N(x) \cdot \mathcal{J}_N(y)$.

命题 15.24　设 $N = pq$ 为不同奇素数之积，$x, y \in \mathbb{Z}_N^*$。则 $\mathcal{J}_N(xy) = \mathcal{J}_N(x) \cdot \mathcal{J}_N(y)$。

PROOF Using the definition of $\mathcal{J}_N(\cdot)$ and Proposition 15.19:

证明　利用 $\mathcal{J}_N(\cdot)$ 的定义和命题 15.19：

$$\begin{align*}\mathcal{J}_{N}(xy)=\mathcal{J}_{p}(xy)\cdot\mathcal{J}_{q}(xy)&=\mathcal{J}_{p}(x)\cdot\mathcal{J}_{p}(y)\cdot\mathcal{J}_{q}(x)\cdot\mathcal{J}_{q}(y)\\&=\mathcal{J}_{p}(x)\cdot\mathcal{J}_{q}(x)\cdot\mathcal{J}_{p}(y)\cdot\mathcal{J}_{q}(y)=\mathcal{J}_{N}(x)\cdot\mathcal{J}_{N}(y).\end{align*}$$

COROLLARY 15.25 Let $N = pq$ be a product of distinct, odd primes, and say $x, x^{\prime} \in \mathcal{QR}_N$ and $y, y^{\prime} \in \mathcal{QNR}_N^{+1}$. Then:

推论 15.25　设 $N = pq$ 为不同奇素数之积，且 $x, x^{\prime} \in \mathcal{QR}_N$、$y, y^{\prime} \in \mathcal{QNR}_N^{+1}$。则：

1. $[xx^{\prime} \bmod N] \in \mathcal{QR}_N$.

   $[xx^{\prime} \bmod N] \in \mathcal{QR}_N$。

2. $[yy^{\prime} \bmod N] \in \mathcal{QR}_N$.

   $[yy^{\prime} \bmod N] \in \mathcal{QR}_N$。

3. $[xy \bmod N] \in \mathcal{QNR}_{N}^{+1}$.

   $[xy \bmod N] \in \mathcal{QNR}_{N}^{+1}$。

PROOF We prove the final claim; proofs of the others are similar. Since $x \in \mathcal{QR}_N$, we have $\mathcal{J}_p(x) = \mathcal{J}_q(x) = +1$. Since $y \in \mathcal{QNR}_N^{+1}$, we have $\mathcal{J}_p(y) = \mathcal{J}_q(y) = -1$. Using Proposition 15.19,

证明　我们只证最后一条，其余各条的证明类似。由 $x \in \mathcal{QR}_N$ 知 $\mathcal{J}_p(x) = \mathcal{J}_q(x) = +1$；由 $y \in \mathcal{QNR}_N^{+1}$ 知 $\mathcal{J}_p(y) = \mathcal{J}_q(y) = -1$。利用命题 15.19，有

$$\mathcal{J}_{p}(x y)=\mathcal{J}_{p}(x)\cdot\mathcal{J}_{p}(y)=-1\quad\mathrm{and}\quad\mathcal{J}_{q}(x y)=\mathcal{J}_{q}(x)\cdot\mathcal{J}_{q}(y)=-1,$$

and so $\mathcal{J}_N(xy) = +1$. But $xy$ is not a quadratic residue modulo $N$, since $\mathcal{J}_p(xy) = -1$ and so $[xy \bmod p]$ is not a quadratic residue modulo $p$. We conclude that $xy \in \mathcal{QNR}_{N}^{+1}$.

于是 $\mathcal{J}_N(xy) = +1$。但 $xy$ 不是模 $N$ 的二次剩余，因为 $\mathcal{J}_p(xy) = -1$，即 $[xy \bmod p]$ 不是模 $p$ 的二次剩余。综上，$xy \in \mathcal{QNR}_{N}^{+1}$。

In contrast to Corollary 15.20, it is not true that $y, y^{\prime} \in \mathcal{QNR}_N$ implies $yy^{\prime} \in \mathcal{QR}_N$. (Instead, as indicated in the corollary, this is only guaranteed if $y, y^{\prime} \in \mathcal{QNR}_N^{+1}$.) For example, we could have $\mathcal{J}_p(y) = +1$, $\mathcal{J}_q(y) = -1$ and $\mathcal{J}_p(y^{\prime}) = -1$, $\mathcal{J}_q(y^{\prime}) = +1$, so $\mathcal{J}_p(yy^{\prime}) = \mathcal{J}_q(yy^{\prime}) = -1$ and $yy^{\prime}$ is not a quadratic residue even though $\mathcal{J}_N(yy^{\prime}) = +1$.

与推论 15.20 不同的是，由 $y, y^{\prime} \in \mathcal{QNR}_N$ 并不能推出 $yy^{\prime} \in \mathcal{QR}_N$。（正如推论中所示，只有当 $y, y^{\prime} \in \mathcal{QNR}_N^{+1}$ 时才有此保证。）举例来说，可能有 $\mathcal{J}_p(y) = +1$、$\mathcal{J}_q(y) = -1$ 且 $\mathcal{J}_p(y^{\prime}) = -1$、$\mathcal{J}_q(y^{\prime}) = +1$，于是 $\mathcal{J}_p(yy^{\prime}) = \mathcal{J}_q(yy^{\prime}) = -1$，此时尽管 $\mathcal{J}_N(yy^{\prime}) = +1$，$yy^{\prime}$ 却不是二次剩余。

### 15.4.3 The Quadratic Residuosity Assumption　二次剩余性假设

In Section 15.4.1, we showed an efficient algorithm for deciding whether an input $x$ is a quadratic residue modulo a prime p. Can we adapt the algorithm to work modulo a composite number N? Proposition 15.21 gives an easy solution to this problem provided the factorization of N is known. See Algorithm 15.26.

15.4.1 节给出了一个高效算法，用于判定输入 $x$ 是否为模素数 $p$ 的二次剩余。能否把该算法改造为适用于模合数 $N$ 的情形？在已知 $N$ 的因子分解的前提下，命题 15.21 给出了这一问题的简单解法。见算法 15.26。

ALGORITHM 15.26
Deciding quadratic residuosity modulo a composite
of known factorization

Input: Composite $N = pq$; the factors $p$ and $q$; element $x \in \mathbb{Z}_N^*$,
Output: A decision as to whether $x \in \mathcal{QR}_N$

compute $\mathcal{J}_p(x)$ and $\mathcal{J}_q(x)$

if $\mathcal{J}_p(x) = \mathcal{J}_q(x) = +1$ return “quadratic residue”
else return “quadratic non-residue”

算法 15.26
在因子分解已知时判定模合数的二次剩余性

输入：合数 $N = pq$；因子 $p$ 和 $q$；元素 $x \in \mathbb{Z}_N^*$
输出：判定 $x$ 是否属于 $\mathcal{QR}_N$

计算 $\mathcal{J}_p(x)$ 和 $\mathcal{J}_q(x)$

若 $\mathcal{J}_p(x) = \mathcal{J}_q(x) = +1$ 则返回“二次剩余”
否则返回“二次非剩余”

(As always, we assume the factors of N are distinct odd primes.) A simple modification of the above algorithm allows for computing $\mathcal{J}_{N}(x)$ when the factorization of N is known.

（同往常一样，我们假定 $N$ 的因子是不同的奇素数。）对上述算法作简单修改，即可在已知 $N$ 的因子分解时计算 $\mathcal{J}_{N}(x)$。

When the factorization of $N$ is unknown, however, there is no known polynomial-time algorithm for deciding whether a given $x$ is a quadratic residue modulo $N$ or not. Somewhat surprisingly, a polynomial-time algorithm is known for computing $\mathcal{J}_{N}(x)$ without the factorization of $N$. (Although the algorithm itself is not that complicated, its proof of correctness is beyond the scope of this book and we therefore do not present the algorithm at all. The interested reader can refer to the references listed at the end of this chapter.) This leads to a partial test of quadratic residuosity: if, for a given input x, it holds that $\mathcal{J}_{N}(x) = -1$, then x cannot possibly be a quadratic residue. (See Proposition 15.23.) This test says nothing when $\mathcal{J}_{N}(x) = +1$, and there is no known polynomial-time algorithm for deciding quadratic residuosity in that case (that does better than random guessing).

然而，当 $N$ 的因子分解未知时，目前没有已知的多项式时间算法可以判定给定的 $x$ 是否为模 $N$ 的二次剩余。多少有些令人惊讶的是，已知存在多项式时间算法，可以在不知道 $N$ 的因子分解的情况下计算 $\mathcal{J}_{N}(x)$。（该算法本身并不算复杂，但其正确性证明超出了本书范围，因此我们完全不予介绍。感兴趣的读者可参阅本章末尾列出的文献。）由此可以得到二次剩余性的一个部分判定：对给定的输入 x，若 $\mathcal{J}_{N}(x) = -1$，则 x 绝不可能是二次剩余。（见命题 15.23。）而当 $\mathcal{J}_{N}(x) = +1$ 时，该判定给不出任何结论；在这种情况下，目前没有已知的多项式时间算法能够判定二次剩余性并比随机猜测做得更好。

We now formalize the assumption that this problem is hard. Let GenModulus be a polynomial-time algorithm that, on input ${1}^n$, outputs $(N, p, q)$ where $N = pq$, and $p$ and $q$ are $n$-bit primes except with probability negligible in $n$.

现在把“该问题是困难的”这一假设形式化。设 $\mathsf{GenModulus}$ 是一个多项式时间算法，以 ${1}^n$ 为输入，输出 $(N, p, q)$，其中 $N = pq$，并且除关于 $n$ 可忽略的概率外，$p$ 和 $q$ 都是 $n$ 比特素数。

DEFINITION 15.27 We say deciding quadratic residuosity is hard relative to GenModulus if for all probabilistic polynomial-time algorithms D there exists a negligible function $\mathsf{negl}$ such that

定义 15.27　称判定二次剩余性相对于 $\mathsf{GenModulus}$ 是困难的，如果对所有概率多项式时间算法 $\mathcal{D}$，都存在可忽略函数 $\mathsf{negl}$ 使得

$$\left|\Pr[D(N,\mathsf{qr})=1]-\Pr[D(N,\mathsf{qnr})=1]\right|\leq\mathsf{negl}(n),$$

where in each case the probabilities are taken over the experiment in which $\mathsf{GenModulus}(1^n)$ is run to give $(N, p, q)$, $\mathsf{qr}$ is chosen uniformly from $\mathcal{QR}_N$, and $\mathsf{qnr}$ is chosen uniformly from $\mathcal{QNR}_{N}^{+1}$.

其中两个概率所对应的实验都是：运行 $\mathsf{GenModulus}(1^n)$ 得到 $(N, p, q)$，从 $\mathcal{QR}_N$ 中均匀选取 $\mathsf{qr}$，并从 $\mathcal{QNR}_{N}^{+1}$ 中均匀选取 $\mathsf{qnr}$。

It is crucial in the above that $\mathfrak{qnr}$ is chosen from $\mathcal{QNR}_{N}^{+1}$ rather than $\mathcal{QNR}_{N}$; if $\mathfrak{qnr}$ were chosen from $\mathcal{QNR}_{N}$ then with probability 2/3 it would be the case that $\mathcal{J}_{N}(x) = -1$ and so distinguishing $\mathfrak{qnr}$ from a uniform quadratic residue would be easy. (Recall that $\mathcal{J}_{N}(x)$ can be computed efficiently even without the factorization of $N$.)

上述定义中至关重要的一点是：$\mathfrak{qnr}$ 取自 $\mathcal{QNR}_{N}^{+1}$ 而不是 $\mathcal{QNR}_{N}$；若 $\mathfrak{qnr}$ 取自 $\mathcal{QNR}_{N}$，则以 2/3 的概率会有 $\mathcal{J}_{N}(x) = -1$，此时把 $\mathfrak{qnr}$ 与均匀的二次剩余区分开来就很容易。（回忆一下，即使不知道 $N$ 的因子分解，$\mathcal{J}_{N}(x)$ 也能高效计算。）

The quadratic residuosity assumption is simply the assumption that there exists a GenModulus relative to which deciding quadratic residuosity is hard. It is easy to see that if deciding quadratic residuosity is hard relative to GenModulus, then factoring must be hard relative to GenModulus as well.

二次剩余性假设就是：存在某个 $\mathsf{GenModulus}$，使得判定二次剩余性相对于它是困难的。容易看出，若判定二次剩余性相对于 $\mathsf{GenModulus}$ 是困难的，则因子分解相对于 $\mathsf{GenModulus}$ 也必定是困难的。

### 15.4.4 The Goldwasser–Micali Encryption Scheme　Goldwasser–Micali 加密方案

The preceding section immediately suggests a public-key encryption scheme for single-bit messages based on the quadratic residuosity assumption:

上一节的内容直接提示了一个基于二次剩余性假设、用于加密单比特消息的公钥加密方案：

- The public key is a modulus N, and the private key is its factorization.

  公钥是模数 $N$，私钥是它的因子分解。

- To encrypt a '0,' send a uniform quadratic residue; to encrypt a '1,' send a uniform quadratic non-residue with Jacobi symbol +1.

  加密“0”时，发送一个均匀的二次剩余；加密“1”时，发送一个雅可比符号为 +1 的均匀二次非剩余。

- The receiver can decrypt a ciphertext $c$ with its private key by using the factorization of $N$ to decide whether $c$ is a quadratic residue or not.

  接收方可以用私钥解密：利用 $N$ 的因子分解判定密文 $c$ 是否为二次剩余。

CPA-security of this scheme follows almost trivially from the hardness of the quadratic residuosity problem as formalized in Definition 15.27.

该方案的选择明文安全性几乎可以直接由定义 15.27 所形式化的二次剩余性问题的困难性推出。

One thing missing from the above description is a specification of how the sender, who does not know the factorization of $N$, can choose a uniform element of $\mathcal{QR}_N$ (to encrypt a 0) or a uniform element of $\mathcal{QNR}_{N}^{+1}$ (to encrypt a 1). The first of these is easy, while the second requires some ingenuity.

上面的描述还缺一环：发送方不知道 $N$ 的因子分解，如何选取 $\mathcal{QR}_N$ 中的均匀元素（用于加密 0）或 $\mathcal{QNR}_{N}^{+1}$ 中的均匀元素（用于加密 1）？前者很容易，后者则需要一点技巧。

**Choosing a uniform quadratic residue.**

**选取均匀的二次剩余。**

Choosing a uniform element $y \in \mathcal{QR}_N$ is easy: simply pick a uniform $x \in \mathbb{Z}_N^*$ (see Appendix B.2.5) and set $y := x^2 \bmod N$. Clearly $y \in \mathcal{QR}_N$. The fact that $y$ is uniformly distributed in $\mathcal{QR}_N$ follows from the facts that squaring modulo $N$ is a 4-to-1 function (see Section 15.4.2) and that $x$ is chosen uniformly from $\mathbb{Z}_N^*$. In more detail, fix any $\hat{y} \in \mathcal{QR}_N$ and let us compute the probability that $y = \hat{y}$ after the above procedure. Denote the four square roots of $\hat{y}$ by $\pm\hat{x}, \pm\hat{x}^{\prime}$. Then:

选取均匀元素 $y \in \mathcal{QR}_N$ 很容易：只需均匀选取 $x \in \mathbb{Z}_N^*$（见附录 B.2.5），再令 $y := x^2 \bmod N$。显然 $y \in \mathcal{QR}_N$。$y$ 在 $\mathcal{QR}_N$ 中均匀分布，这一点可由以下两个事实推出：模 $N$ 取平方是四对一函数（见 15.4.2 节），且 $x$ 是从 $\mathbb{Z}_N^*$ 中均匀选取的。更详细地说，任意固定 $\hat{y} \in \mathcal{QR}_N$，计算上述过程输出 $y = \hat{y}$ 的概率。记 $\hat{y}$ 的四个平方根为 $\pm\hat{x}, \pm\hat{x}^{\prime}$。则

$$\begin{aligned}\Pr[y=\hat{y}]&=\Pr[x\text{ is a square root of }\hat{y}]\\&=\Pr\left[x\in\{\pm\hat{x},\pm\hat{x}^{\prime}\}\right]\\&=\frac{4}{\left|\mathbb{Z}_{N}^{*}\right|}=\frac{1}{\left|\mathcal{QR}_{N}\right|}.\end{aligned}$$

Since the above holds for every $\hat{y} \in \mathcal{QR}_N$, we see that $y$ is distributed uniformly in $\mathcal{QR}_N$.

由于上式对每个 $\hat{y} \in \mathcal{QR}_N$ 都成立，可见 $y$ 在 $\mathcal{QR}_N$ 中均匀分布。

**Choosing a uniform element of $\mathcal{QNR}_N^{+1}$.**

**选取 $\mathcal{QNR}_N^{+1}$ 中的均匀元素。**

In general, it is not known how to choose a uniform element of $\mathcal{QNR}_N^{+1}$ if the factorization of $N$ is unknown. What saves us in the present context is that the receiver can help by including certain information in the public key. Specifically, we modify the scheme so that the receiver additionally chooses a uniform $z \in \mathcal{QNR}_N^{+1}$ and includes $z$ as part of its public key. (This is easy for the receiver to do since it knows the factorization of $N$; see Exercise 15.7.) The sender can choose a uniform element $y \in \mathcal{QNR}_N^{+1}$ by choosing a uniform $x \in \mathbb{Z}_N^*$ (as above) and setting $y := [z \cdot x^2 \mod N]$. It follows from Corollary 15.25 that $y \in \mathcal{QNR}_N^{+1}$. We leave it as an exercise to show that $y$ is uniformly distributed in $\mathcal{QNR}_N^{+1}$; we do not use this fact directly in the proof of security given below.

一般而言，在不知道 $N$ 的因子分解时，如何选取 $\mathcal{QNR}_N^{+1}$ 中的均匀元素是未知的。所幸在当前的场景下，接收方可以通过在公钥中附带某些信息来提供帮助。具体来说，我们修改方案，让接收方额外选取一个均匀的 $z \in \mathcal{QNR}_N^{+1}$，并把 $z$ 作为公钥的一部分。（接收方知道 $N$ 的因子分解，做这件事很容易；见习题 15.7。）发送方可以（像上面那样）均匀选取 $x \in \mathbb{Z}_N^*$，再令 $y := [z \cdot x^2 \mod N]$，由此得到元素 $y$，且由推论 15.25 可知 $y \in \mathcal{QNR}_N^{+1}$。$y$ 在 $\mathcal{QNR}_N^{+1}$ 中均匀分布这一点的证明留作习题；下面给出的安全性证明并不直接用到这一事实。

We give a complete description of the Goldwasser–Micali encryption scheme, implementing the above ideas, in Construction 15.28.

构造 15.28 给出了 Goldwasser–Micali 加密方案的完整描述，实现了上述想法。

**CONSTRUCTION 15.28**

**构造 15.28**

Let GenModulus be as usual. Construct a public-key encryption scheme as follows:

设 $\mathsf{GenModulus}$ 同前。如下构造公钥加密方案：

Gen: on input ${1}^n$, run $\mathsf{GenModulus}(1^n)$ to obtain $(N, p, q)$, and choose a uniform $z \in \mathcal{QNR}_{N}^{+1}$. The public key is $pk = \langle N, z \rangle$ and the private key is $sk = \langle p, q \rangle$.

Gen：以 ${1}^n$ 为输入，运行 $\mathsf{GenModulus}(1^n)$ 得到 $(N, p, q)$，并均匀选取 $z \in \mathcal{QNR}_{N}^{+1}$。公钥为 $pk = \langle N, z \rangle$，私钥为 $sk = \langle p, q \rangle$。

- Enc: on input a public key $pk = \langle N, z \rangle$ and a message $m \in \{0,1\}$, choose a uniform $x \in \mathbb{Z}_N^*$ and output the ciphertext

  Enc：以公钥 $pk = \langle N, z \rangle$ 和消息 $m \in \{0,1\}$ 为输入，均匀选取 $x \in \mathbb{Z}_N^*$，输出密文

$$c:=[z^{m}\cdot x^{2}\bmod N].$$

- Dec: on input a private key $sk = \langle p,q\rangle$ and a ciphertext $c$, determine whether $c$ is a quadratic residue modulo $N$ using, e.g., Algorithm 15.26. If yes, output 0; otherwise, output 1.

  Dec：以私钥 $sk = \langle p,q\rangle$ 和密文 $c$ 为输入，（例如用算法 15.26）判定 $c$ 是否为模 $N$ 的二次剩余。若是，输出 0；否则输出 1。

The Goldwasser–Micali encryption scheme.

Goldwasser–Micali 加密方案。

THEOREM 15.29 If the quadratic residuosity problem is hard relative to GenModulus, then the Goldwasser–Micali encryption scheme is CPA-secure.

定理 15.29　若二次剩余性问题相对于 $\mathsf{GenModulus}$ 是困难的，则 Goldwasser–Micali 加密方案是选择明文安全的。

PROOF Let $\Pi$ denote the Goldwasser–Micali encryption scheme. We prove that $\Pi$ has indistinguishable encryptions in the presence of an eavesdropper; by Theorem 12.6 this implies that it is CPA-secure.

证明　记 $\Pi$ 为 Goldwasser–Micali 加密方案。我们证明 $\Pi$ 在窃听者存在时具有不可区分的加密；由定理 12.6，这意味着它是选择明文安全的。

Let A be an arbitrary probabilistic polynomial-time adversary. Consider the following PPT adversary D that attempts to solve the quadratic residuosity problem relative to GenModulus:

设 $\mathcal{A}$ 是任意的概率多项式时间敌手。考虑如下试图求解相对于 $\mathsf{GenModulus}$ 的二次剩余性问题的概率多项式时间敌手 $\mathcal{D}$：

Algorithm D:

算法 $\mathcal{D}$：

The algorithm is given $N$ and $z$ as input, and its goal is to determine if $z \in \mathcal{QR}_N$ or $z \in \mathcal{QNR}_N^{+1}$.

该算法以 $N$ 和 $z$ 为输入，目标是判定 $z \in \mathcal{QR}_N$ 还是 $z \in \mathcal{QNR}_N^{+1}$。

- Set $pk = \langle N, z \rangle$ and run $\mathcal{A}(pk)$ to obtain two single-bit messages $m_0, m_1$.

  令 $pk = \langle N, z \rangle$，运行 $\mathcal{A}(pk)$ 得到两个单比特消息 $m_0, m_1$。

• Choose a uniform bit $b$ and a uniform $x \in \mathbb{Z}_N^*$, and then set $c := [z^{m_b} \cdot x^2 \bmod N]$.

• 均匀选取比特 $b$ 和 $x \in \mathbb{Z}_N^*$，然后令 $c := [z^{m_b} \cdot x^2 \bmod N]$。

• Give the ciphertext c to A, who in turn outputs a bit $b^{\prime}$. If $b^{\prime} = b$, output 1; otherwise, output 0.

• 把密文 c 交给 A，A 输出比特 $b^{\prime}$。若 $b^{\prime} = b$，输出 1；否则输出 0。

Let us analyze the behavior of D. There are two cases to consider:

下面分析 $\mathcal{D}$ 的行为。分两种情形：

Case 1: Say the input to $D$ was generated by running $\mathsf{GenModulus}(1^n)$ to obtain $(N, p, q)$ and then choosing a uniform $z \in \mathcal{QNR}_N^{+1}$. Then $D$ runs $\mathcal{A}$ on a public key constructed exactly as in $\Pi$, and we see that in this case the view of $\mathcal{A}$ when run as a subroutine by $D$ is distributed identically to $\mathcal{A}$'s view in experiment $\mathsf{PubK}_{\mathcal{A},\Pi}^{\mathsf{eav}}(n)$. Since $D$ outputs 1 exactly when the output $b^{\prime}$ of $\mathcal{A}$ is equal to $b$, we have

情形 1：设 $D$ 的输入是这样生成的：运行 $\mathsf{GenModulus}(1^n)$ 得到 $(N, p, q)$，然后均匀选取 $z \in \mathcal{QNR}_N^{+1}$。此时 $D$ 交给 $\mathcal{A}$ 的公钥与 $\Pi$ 中构造的公钥完全一致，因此在这种情形下，$\mathcal{A}$ 作为 $D$ 的子程序运行时的视图，与 $\mathcal{A}$ 在实验 $\mathsf{PubK}_{\mathcal{A},\Pi}^{\mathsf{eav}}(n)$ 中的视图分布完全相同。由于 $D$ 恰在 $\mathcal{A}$ 的输出 $b^{\prime}$ 等于 $b$ 时输出 1，故有

$$\Pr[D(N,\mathsf{qnr})=1]=\Pr[\mathsf{PubK}_{\mathcal{A},\Pi}^{\mathsf{eav}}(n)=1],$$

where qnr represents a uniform element of $\mathcal{QNR}_{N}^{+1}$ as in Definition 15.27.

其中 qnr 如定义 15.27 所述，表示 $\mathcal{QNR}_{N}^{+1}$ 中的均匀元素。

Case 2: Say the input to $D$ was generated by running $\mathsf{GenModulus}(1^n)$ to obtain $(N, p, q)$ and then choosing a uniform $z \in \mathcal{QR}_N$. We claim that the view of $\mathcal{A}$ in this case is independent of the bit $b$. To see this, note that the ciphertext $c$ given to $\mathcal{A}$ is a uniform quadratic residue regardless of whether a 0 or a 1 is encrypted:

情形 2：设 $D$ 的输入是这样生成的：运行 $\mathsf{GenModulus}(1^n)$ 得到 $(N, p, q)$，然后均匀选取 $z \in \mathcal{QR}_N$。我们断言，此时 $\mathcal{A}$ 的视图与比特 $b$ 无关。为看清这一点，注意无论加密的是 0 还是 1，交给 $\mathcal{A}$ 的密文 $c$ 都是均匀的二次剩余：

- When a 0 is encrypted, $c = [x^2 \mod N]$ for a uniform $x \in \mathbb{Z}_N^*$, and so c is a uniform quadratic residue.

  加密 0 时，$c = [x^2 \mod N]$，其中 $x \in \mathbb{Z}_N^*$ 均匀选取，故 c 是均匀的二次剩余。

- When a 1 is encrypted, $c = [z \cdot x^2 \mod N]$ for a uniform $x \in \mathbb{Z}_N^*$. Let $\hat{x} \overset{\mathrm{def}}{=} [x^2 \mod N]$, and note that $\hat{x}$ is a uniformly distributed element of the group $\mathcal{QR}_N$. Since $z \in \mathcal{QR}_N$, we can apply Lemma 12.15 to conclude that $c$ is uniformly distributed in $\mathcal{QR}_N$ as well.

  加密 1 时，$c = [z \cdot x^2 \mod N]$，其中 $x \in \mathbb{Z}_N^*$ 均匀选取。令 $\hat{x} \overset{\mathrm{def}}{=} [x^2 \mod N]$，注意 $\hat{x}$ 是群 $\mathcal{QR}_N$ 中均匀分布的元素。由于 $z \in \mathcal{QR}_N$，应用引理 12.15 可知 $c$ 在 $\mathcal{QR}_N$ 中同样均匀分布。

Since $\mathcal{A}$'s view is independent of b, the probability that $b^{\prime} = b$ in this case is exactly $\frac{1}{2}$. That is,

由于 $\mathcal{A}$ 的视图与 $b$ 无关，此时 $b^{\prime} = b$ 的概率恰好是 $\frac{1}{2}$。即

$$\Pr[D(N,\mathsf{qr})=1]=\frac{1}{2},$$

where $\mathbf{qr}$ represents a uniform element of $\mathcal{QR}_{N}$ as in Definition 15.27.

其中 $\mathbf{qr}$ 如定义 15.27 所述，表示 $\mathcal{QR}_{N}$ 中的均匀元素。

Thus,

于是

$$\left|\Pr[D(N,\mathfrak{q}\mathfrak{r})=1]-\Pr[D(N,\mathfrak{q}\mathfrak{n}\mathfrak{r})=1]\right|=\left|\Pr[\mathsf{PubK}_{\mathcal{A},\Pi}^{\mathsf{eav}}(n)=1]-\tfrac{1}{2}\right|.$$

By the assumption that the quadratic residuosity problem is hard relative to GenModulus, there is a negligible function $\mathsf{negl}$.  Let $\varepsilon(n) \stackrel{\mathrm{def}}{=} \Pr[\mathsf{PubK}_{\mathcal{A},\Pi}^{\mathsf{eav}}(n)=1]$. Then

由二次剩余性问题相对于 $\mathsf{GenModulus}$ 困难的假设，存在可忽略函数 $\mathsf{negl}$ 使得下式成立（其中 $\varepsilon(n) \stackrel{\mathrm{def}}{=} \Pr[\mathsf{PubK}_{\mathcal{A},\Pi}^{\mathsf{eav}}(n)=1]$）：

$$\left|\varepsilon(n)-\tfrac{1}{2}\right|\leq\mathsf{negl}(n);$$

thus, $\varepsilon(n) \leq \frac{1}{2} + \mathsf{negl}(n)$. This completes the proof.

从而 $\varepsilon(n) \leq \frac{1}{2} + \mathsf{negl}(n)$。证毕。

## 15.5 The Rabin Encryption Scheme　Rabin 加密方案

As mentioned at the beginning of this chapter, the Rabin encryption scheme is attractive because its security is equivalent to the assumption that factoring is hard. An analogous result is not known for RSA-based encryption, and the RSA problem may potentially be easier than factoring. (The same is true of the Goldwasser–Micali encryption scheme, and it is possible that deciding quadratic residuosity modulo N is easier than factoring N.)

正如本章开头所提到的，Rabin 加密方案之所以吸引人，是因为它的安全性与因子分解困难假设等价。对基于 RSA 的加密而言，人们并不知道类似的结果，而且 RSA 问题有可能比因子分解更容易。（Goldwasser–Micali 加密方案也是如此：判定模 $N$ 的二次剩余性有可能比分解 $N$ 更容易。）

Interestingly, the Rabin encryption scheme is (superficially, at least) very similar to the RSA encryption scheme yet has the advantage of being based on a potentially weaker assumption. The fact that RSA is more widely used than the former seems to be due more to historical factors than technical ones; we discuss this further at the end of this section.

有趣的是，Rabin 加密方案（至少表面上）与 RSA 加密方案非常相似，却有建立在可能更弱的假设之上的优势。RSA 比前者应用得更广泛，这一事实与其说是出于技术上的原因，不如说是历史因素所致；本节末尾将对此作进一步讨论。

We begin with some preliminaries about computing modular square roots. We then introduce a trapdoor permutation that can be based directly on the assumption that factoring is hard. The Rabin encryption scheme (or, at least, one instantiation of it) is then obtained by applying the results from Section 15.1. Throughout this section, we continue to let $p$ and $q$ denote odd primes, and let $N = pq$ denote a product of two distinct, odd primes.

我们先介绍计算模平方根的预备知识，然后引入一个可以直接建立在因子分解困难假设上的陷门置换，再应用 15.1 节的结果得到 Rabin 加密方案（或者至少是它的一种实例化）。本节中，仍用 $p$ 和 $q$ 表示奇素数，用 $N = pq$ 表示两个不同奇素数的乘积。

### 15.5.1 Computing Modular Square Roots　计算模平方根

The Rabin encryption scheme requires the receiver to compute modular square roots, and so in this section we explore the algorithmic complexity of this problem. We first show an efficient algorithm for computing square roots modulo a prime $p$, and then extend this algorithm to enable computation of square roots modulo a composite $N$ of known factorization. The reader willing to accept the existence of these algorithms on faith can skip to the following section, where we show that computing square roots modulo a composite $N$ with unknown factorization is equivalent to factoring $N$.

Rabin 加密方案要求接收方计算模平方根，因此本节探讨该问题的算法复杂度。我们先给出一个计算模素数 $p$ 平方根的高效算法，然后把它推广到在因子分解已知时计算模合数 $N$ 的平方根。愿意直接承认这些算法存在的读者可以跳到下一节——那里我们将证明：在因子分解未知时，计算模合数 $N$ 的平方根与分解 $N$ 等价。

Let $p$ be an odd prime. Computing square roots modulo $p$ is relatively simple when $p = 3 \mod 4$, but much more involved when $p = 1 \mod 4$. (The easier case is all we need for the Rabin encryption scheme as presented in Section 15.5.3; we include the second case for completeness.) In both cases, we show how to compute one of the square roots of a quadratic residue $a \in \mathbb{Z}_p^*$. Note that if $x$ is one of the square roots of $a$, then $[ -x \bmod p ]$ is the other.

设 $p$ 为奇素数。当 $p = 3 \mod 4$ 时，计算模 $p$ 的平方根相对简单；而当 $p = 1 \mod 4$ 时则要复杂得多。（15.5.3 节给出的 Rabin 加密方案只需要较简单的情形；第二种情形为完整起见也一并介绍。）在两种情形下，我们都展示如何计算二次剩余 $a \in \mathbb{Z}_p^*$ 的一个平方根。注意，若 $x$ 是 $a$ 的一个平方根，则 $[ -x \bmod p ]$ 是另一个。

We tackle the easier case first. Say $p = 3 \mod 4$, meaning we can write $p = 4i + 3$ for some integer $i$. Since $a \in \mathbb{Z}_p^*$ is a quadratic residue, we have $\mathcal{J}_p(a) = 1 = a^{\frac{p-1}{2}} \mod p$ (see Proposition 15.17). Multiplying both sides by $a$ we obtain:

先处理较简单的情形。设 $p = 3 \mod 4$，即存在整数 $i$ 使 $p = 4i + 3$。由于 $a \in \mathbb{Z}_p^*$ 是二次剩余，有 $\mathcal{J}_p(a) = 1 = a^{\frac{p-1}{2}} \mod p$（见命题 15.17）。两边同乘 $a$，得到

$$a=a^{\frac{p-1}{2}+1}=a^{2i+2}=\left(a^{i+1}\right)^{2}\bmod p,$$

and so $a^{i+1} = a^{\frac{p+1}{4}}$ mod $p$ is a square root of $a$. That is, we obtain a square root of $a$ modulo $p$ by simply computing $x := [a^{\frac{p+1}{4}} \mod p]$.

于是 $a^{i+1} = a^{\frac{p+1}{4}}$ mod $p$ 是 $a$ 的一个平方根。也就是说，只需计算 $x := [a^{\frac{p+1}{4}} \mod p]$ 即可得到 $a$ 模 $p$ 的一个平方根。

It is crucial above that $(p+1)/2$ is even because this ensures that $(p+1)/4$ is an integer (this is necessary in order for $a^{\frac{p+1}{4}}$ mod $p$ to be well-defined; recall that the exponent must be an integer). This approach does not succeed when $p=1$ mod 4, in which case $p+1$ is an integer that is not divisible by 4.

上面的推导中，$(p+1)/2$ 为偶数至关重要，因为这保证 $(p+1)/4$ 是整数（这是 $a^{\frac{p+1}{4}}$ mod $p$ 良定义所必需的；回想指数必须为整数这一前提）。当 $p=1$ mod 4 时该方法行不通，因为此时 $p+1$ 是不能被 4 整除的整数。

When $p = 1 \mod 4$ we proceed slightly differently. Motivated by the above approach, we might hope to find an odd integer $r$ for which it holds that $a^r = 1 \mod p$. Then, as above, $a^{r+1} = a \mod p$ and $a^{\frac{r+1}{2}} \mod p$ would be a square root of $a$ with $(r+1)/2$ an integer. Although we will not be able to do this, we can do something just as good: we will find an odd integer $r$ along with an element $b \in \mathbb{Z}_p^*$ and an even integer $r^{\prime}$ such that

当 $p = 1 \mod 4$ 时，我们改用略有不同的方法。受上述方法启发，我们可能希望找到一个奇数 $r$ 使得 $a^r = 1 \mod p$。这样一来，同上，$a^{r+1} = a \mod p$，而 $a^{\frac{r+1}{2}} \mod p$ 将会是 $a$ 的平方根（此时 $(r+1)/2$ 是整数）。虽然这一点做不到，但我们能做一件同样好的事：找到一个奇数 $r$、一个元素 $b \in \mathbb{Z}_p^*$ 和一个偶数 $r^{\prime}$，使得

$$a^{r}\cdot b^{r^{\prime}}=1\bmod p.$$

Then $a^{r+1} \cdot b^{r^{\prime}} = a \bmod p$ and $a^{\frac{r+1}{2}} \cdot b^{\frac{r^{\prime}}{2}} \bmod p$ is a square root of $a$ (with the exponents $(r+1)/2$ and $r^{\prime}/2$ being integers).

于是 $a^{r+1} \cdot b^{r^{\prime}} = a \bmod p$，而 $a^{\frac{r+1}{2}} \cdot b^{\frac{r^{\prime}}{2}} \bmod p$ 就是 $a$ 的平方根（其中指数 $(r+1)/2$ 和 $r^{\prime}/2$ 都是整数）。

We now describe the general approach to finding $r, b$, and $r^{\prime}$ with the stated properties. Let $\frac{p-1}{2} = 2^\ell \cdot m$ where $\ell, m$ are integers with $\ell \geq 1$ and $m$ odd. Since $a$ is a quadratic residue, we know that

现在介绍寻找满足上述性质的 $r, b$ 和 $r^{\prime}$ 的一般方法。记 $\frac{p-1}{2} = 2^\ell \cdot m$，其中 $\ell, m$ 为整数，$\ell \geq 1$ 且 $m$ 为奇数。由于 $a$ 是二次剩余，可知

$$a^{2^{\ell}m}=a^{\frac{p-1}{2}}=1\bmod p. \tag{15.6}$$

This means that $a^{2^{\ell-1}m} \mod p$ is a square root of 1. The square roots of 1 modulo p are $\pm 1 \mod p$, so $a^{2^{\ell-1}m} = \pm 1 \mod p$. If $a^{2^{\ell-1}m} = 1 \mod p$, we are in the same situation as in Equation (15.6) except that the exponent of $a$ is now divisible by a smaller power of 2. This is progress in the right direction: if we can get to the point where the exponent of $a$ is not divisible by any power of 2 (as would be the case here if $\ell = 1$), then the exponent of $a$ is odd and we can compute a square root as discussed earlier. We give an example, and discuss in a moment how to deal with the case when $a^{2^{\ell-1}m} = -1 \bmod p$.

这意味着 $a^{2^{\ell-1}m} \mod p$ 是 1 的一个平方根。1 模 $p$ 的平方根是 $\pm 1 \mod p$，所以 $a^{2^{\ell-1}m} = \pm 1 \mod p$。若 $a^{2^{\ell-1}m} = 1 \mod p$，则所处情形与式 (15.6) 相同，只是 $a$ 的指数现在只能被更小的 2 的幂整除。这是朝正确方向迈出的一步：如果能把 $a$ 的指数约化至不再被任何 2 的幂整除（这里若 $\ell = 1$ 即属此情形），那么 $a$ 的指数就是奇数，就可以按前面讨论的方法计算平方根了。我们先举一个例子，稍后再讨论 $a^{2^{\ell-1}m} = -1 \bmod p$ 的情形如何处理。

**Example 15.30**

**例 15.30**

Take $p = 29$ and $a = 7$. Since ${7}$ is a quadratic residue modulo ${29}$, we have ${7}^{14} \mod 29 = 1$ and we know that ${7}^{7} \mod 29$ is a square root of 1. In fact,

取 $p = 29$、$a = 7$。由于 ${7}$ 是模 ${29}$ 的二次剩余，有 ${7}^{14} \mod 29 = 1$，并且知道 ${7}^{7} \mod 29$ 是 1 的一个平方根。事实上，

$${7}^{7}=1\bmod{29},$$

and the exponent 7 is odd. So ${7}^{(7+1)/2} = 7^4 = 23 \mod 29$ is a square root of 7 modulo 29.

而指数 7 是奇数。所以 ${7}^{(7+1)/2} = 7^4 = 23 \mod 29$ 是 7 模 29 的一个平方根。

To summarize the algorithm so far: we begin with $a^{2^{\ell} m} = 1 \mod p$ and we pull out factors of 2 from the exponent until one of two things happen: either $a^m = 1 \mod p$, or $a^{2^{\ell^{\prime}} m} = -1 \mod p$ for some $\ell^{\prime} < \ell$. In the first case, since $m$ is odd we can immediately compute asquare root of a as in Example 15.30. In the second case, we will “restore” the +1 on the right-hand side of the equation by multiplying each side of the equation by -1 mod p. However, as motivated at the beginning of this discussion, we want to achieve this by multiplying the left-hand side of the equation by some element b raised to an even power. If we have available a quadratic non-residue $b \in \mathbb{Z}_p^*$, this is easy: since $b^{2^{\ell} m} = b^{\frac{p-1}{2}} = -1 \mod p$, we have

总结一下到目前为止的算法：从 $a^{2^{\ell} m} = 1 \mod p$ 出发，不断从指数中剥离因子 2，直到出现两种情形之一：要么 $a^m = 1 \mod p$，要么对某个 $\ell^{\prime} < \ell$ 有 $a^{2^{\ell^{\prime}} m} = -1 \mod p$。第一种情形下，由于 $m$ 是奇数，可以像例 15.30 那样立即算出 $a$ 的平方根。第二种情形下，我们将给等式两边同乘 -1 mod p，把等式右端“恢复”为 +1。不过，正如本讨论开头所说明的，我们希望这一操作通过给等式左端乘以某个元素 $b$ 的偶数次幂来实现。如果手头有一个二次非剩余 $b \in \mathbb{Z}_p^*$，这很容易：由于 $b^{2^{\ell} m} = b^{\frac{p-1}{2}} = -1 \mod p$，于是有

$$a^{2^{\ell^{\prime}}m}\cdot b^{2^{\ell}m}=(-1)(-1)=+1\bmod p.$$

With this we can proceed as before, taking a square root of the left-hand side to reduce the largest power of 2 dividing the exponent of $a$, and multiplying by $b^{2^{\ell} m}$ (as needed) so the right-hand side is always +1. Observe that the exponent of $b$ is always divisible by a larger power of 2 than the exponent of $a$ (and so we can indeed take square roots by dividing by 2 in both exponents). We continue performing these steps until the exponent of $a$ is odd, and can then compute a square root of $a$ as described earlier. Pseudocode for this algorithm, which gives another way of viewing what is going on, is given below in Algorithm 15.31. It can be verified that the algorithm runs in polynomial time given a quadratic non-residue $b$ since the number of iterations of the inner loop is $\ell = \mathcal{O}(\log p)$.

有了它，就可以像之前那样继续：对等式左端开平方，以降低整除 $a$ 的指数的最大 2 的幂，并（按需）乘以 $b^{2^{\ell} m}$，使右端始终保持为 +1。注意，$b$ 的指数始终能被比 $a$ 的指数更大的 2 的幂整除（因此确实可以把两个指数同时除以 2 来开平方）。重复这些步骤，直到 $a$ 的指数变为奇数，然后即可按前述方法计算 $a$ 的平方根。算法 15.31 给出了该算法的伪代码，它提供了理解这一过程的另一种视角。可以验证，在已知二次非剩余 $b$ 的情况下，该算法以多项式时间运行，因为内层循环的迭代次数为 $\ell = \mathcal{O}(\log p)$。

One point we have not yet addressed is how to find $b$ in the first place. In fact, no deterministic polynomial-time algorithm for finding a quadratic non-residue modulo $p$ is known. Fortunately, it is easy to find a quadratic non-residue probabilistically: simply choose uniform elements of $\mathbb{Z}_p^*$ until a
quadratic non-residue is found. This works because exactly half the elements of $\mathbb{Z}_p^*$ are quadratic non-residues, and because a polynomial-time algorithm for deciding quadratic residuosity modulo a prime is known (see Section 15.4.1 for proofs of both these statements). This means that the algorithm we have shown is actually randomized when $p = 1 \mod 4$; a deterministic polynomial-time algorithm for computing square roots in this case is not known.

还有一点尚未解决：一开始如何找到 $b$。事实上，目前并不知道有什么确定性多项式时间算法能找出模 $p$ 的二次非剩余。幸运的是，用概率方法很容易找到二次非剩余：只需不断均匀选取 $\mathbb{Z}_p^*$ 中的元素，直到找到二次非剩余为止。这之所以可行，是因为 $\mathbb{Z}_p^*$ 中恰好一半的元素是二次非剩余，而且已知有判定模素数二次剩余性的多项式时间算法（这两个论断的证明见 15.4.1 节）。这意味着，当 $p = 1 \mod 4$ 时，我们给出的算法实际上是随机化的；在这种情况下，尚不知道有什么计算平方根的确定性多项式时间算法。

ALGORITHM 15.31
Computing square roots modulo a prime

Input: Prime $p$, quadratic residue $a \in \mathbb{Z}_p^*$
Output: A square root of $a$

case $p = 3 \mod 4$:
    return $[a^{\frac{p+1}{4}} \mod p]$
case $p = 1 \mod 4$:
    let $b$ be a quadratic non-residue modulo $p$
        compute $\ell \geq 1$ and odd $m$ with ${2}^{\ell} \cdot m = \frac{p-1}{2}$
 $r := 2^{\ell} \cdot m$, $r^{\prime} := 0$
    for $i = \ell \to 1$ {
        // maintain the invariant $a^r \cdot b^{r^{\prime}} = 1 \mod p$
     $r := r/2$, $r^{\prime} := r^{\prime}/2$
        if $a^r \cdot b^{r^{\prime}} = -1 \mod p$
         $r^{\prime} := r^{\prime} + 2^{\ell} \cdot m$
        }
    // now $r = m$, $r^{\prime}$ is even, and $a^r \cdot b^{r^{\prime}} = 1 \mod p$
    return $[a^{\frac{r+1}{2}} \cdot b^{\frac{r^{\prime}}{2}} \mod p]$

算法 15.31
计算模素数的平方根

输入：素数 $p$，二次剩余 $a \in \mathbb{Z}_p^*$
输出：$a$ 的一个平方根

情形 $p = 3 \mod 4$：
    返回 $[a^{\frac{p+1}{4}} \mod p]$
情形 $p = 1 \mod 4$：
    令 $b$ 为模 $p$ 的二次非剩余
        计算 $\ell \geq 1$ 和奇数 $m$，使得 ${2}^{\ell} \cdot m = \frac{p-1}{2}$
 $r := 2^{\ell} \cdot m$，$r^{\prime} := 0$
    for $i = \ell \to 1$ {
        // 保持循环不变式 $a^r \cdot b^{r^{\prime}} = 1 \mod p$
     $r := r/2$，$r^{\prime} := r^{\prime}/2$
        若 $a^r \cdot b^{r^{\prime}} = -1 \mod p$
         $r^{\prime} := r^{\prime} + 2^{\ell} \cdot m$
        }
    // 此时 $r = m$，$r^{\prime}$ 为偶数，且 $a^r \cdot b^{r^{\prime}} = 1 \mod p$
    返回 $[a^{\frac{r+1}{2}} \cdot b^{\frac{r^{\prime}}{2}} \mod p]$

**Example 15.32**

**例 15.32**

Here we consider the “worst case,” when taking a square root always gives -1. Let $a \in \mathbb{Z}_p^*$ be the element whose square root we are trying to compute; let $b \in \mathbb{Z}_p^*$ be a quadratic non-residue; and let $\frac{p-1}{2} = 2^3 \cdot m$ where $m$ is odd.

这里考虑“最坏情形”，即每次开平方都得到 -1。设 $a \in \mathbb{Z}_p^*$ 是我们要计算平方根的元素；$b \in \mathbb{Z}_p^*$ 是二次非剩余；并设 $\frac{p-1}{2} = 2^3 \cdot m$，其中 $m$ 为奇数。

In the first step, we have $a^{2^{3}m} = 1 \bmod p$. Since $a^{2^{3}m} = \left(a^{2^{2}m}\right)^{2}$ and the square roots of 1 are $\pm1$, this means that $a^{2^{2}m} = \pm1 \bmod p$; assuming the worst case, $a^{2^{2}m} = -1 \bmod p$. So, we multiply by $b^{\frac{p-1}{2}} = b^{2^{3}m} = -1 \bmod p$ to obtain

第一步，有 $a^{2^{3}m} = 1 \bmod p$。由于 $a^{2^{3}m} = \left(a^{2^{2}m}\right)^{2}$，而 1 的平方根是 $\pm1$，这意味着 $a^{2^{2}m} = \pm1 \bmod p$；按最坏情形假设 $a^{2^{2}m} = -1 \bmod p$。于是乘以 $b^{\frac{p-1}{2}} = b^{2^{3}m} = -1 \bmod p$，得到

$$a^{2^{2}m}\cdot b^{2^{3}m}=1\bmod p.$$

In the second step, we observe that $a^{2m} \cdot b^{2^2m}$ is a square root of 1; again assuming the worst case, we thus have $a^{2m} \cdot b^{2^2m} = -1 \mod p$. Multiplying by $b^{2^3m}$ to “correct” this gives

第二步，注意到 $a^{2m} \cdot b^{2^2m}$ 是 1 的一个平方根；仍按最坏情形假设，于是有 $a^{2m} \cdot b^{2^2m} = -1 \mod p$。乘以 $b^{2^3m}$ 来“纠正”它，得到

$$a^{2m}\cdot b^{2^{2}m}\cdot b^{2^{3}m}=1\bmod p.$$

In the third step, taking square roots and assuming the worst case (as above) we obtain $a^m \cdot b^{2m} \cdot b^{2^2m} = -1 \mod p$; multiplying by the “correction factor” $b^{2^3m}$ we get

第三步，开平方并（同上）按最坏情形假设，得到 $a^m \cdot b^{2m} \cdot b^{2^2m} = -1 \mod p$；乘以“纠正因子” $b^{2^3m}$，得到

$$a^{m}\cdot b^{2m}\cdot b^{2^{2}m}\cdot b^{2^{3}m}=1\bmod p.$$

We are now where we want to be. To conclude the algorithm, multiply both sides by a to obtain

现在到达了想要的状态。最后，两边同乘 $a$，得到

$$a^{m+1}\cdot b^{2m+2^{2}m+2^{3}m}=a\bmod p.$$

Since $m$ is odd, $(m+1)/2$ is an integer and $a^{\frac{m+1}{2}} \cdot b^{m+2m+2^2m} \mod p$ is a square root of $a$.

由于 $m$ 是奇数，$(m+1)/2$ 是整数，故 $a^{\frac{m+1}{2}} \cdot b^{m+2m+2^2m} \mod p$ 是 $a$ 的一个平方根。

**Example 15.33**

**例 15.33**

Here we work out a concrete example. Let p = 17, a = 2, and b = 3. Note that here $(p - 1)/2 = 2^3$ and m = 1.

这里完整演算一个具体例子。取 $p = 17$、$a = 2$、$b = 3$。注意此时 $(p - 1)/2 = 2^3$，$m = 1$。

We begin with ${2}^{2^3} = 1 \mod 17$. So ${2}^{2^2}$ should be equal to $\pm1 \mod 17$; by calculation, ${2}^{2^2} = -1 \mod 17$. Multiplying by ${3}^{2^3}$ gives ${2}^{2^2} \cdot 3^{2^3} = 1 \mod 17$. Continuing, we know that ${2}^2 \cdot 3^{2^2}$ is a square root of 1 and so must be equal to $\pm1 \mod 17$; calculation gives ${2}^2 \cdot 3^{2^2} = 1 \mod 17$. So no correction term is needed here.

从 ${2}^{2^3} = 1 \mod 17$ 开始。于是 ${2}^{2^2}$ 应等于 $\pm1 \mod 17$；经计算，${2}^{2^2} = -1 \mod 17$。乘以 ${3}^{2^3}$ 得 ${2}^{2^2} \cdot 3^{2^3} = 1 \mod 17$。继续，可知 ${2}^2 \cdot 3^{2^2}$ 是 1 的平方根，故必等于 $\pm1 \mod 17$；经计算，${2}^2 \cdot 3^{2^2} = 1 \mod 17$。所以这一步不需要纠正项。

Halving the exponents again we find that ${2} \cdot 3^2 = 1 \mod 17$. We are now almost done: multiplying both sides by 2 gives ${2}^2 \cdot 3^2 = 2 \mod 17$, and so ${2} \cdot 3 = 6 \mod 17$ is a square root of 2.

再把指数减半，得到 ${2} \cdot 3^2 = 1 \mod 17$。现在离完成只差一步：两边同乘 2 得 ${2}^2 \cdot 3^2 = 2 \mod 17$，所以 ${2} \cdot 3 = 6 \mod 17$ 是 2 的一个平方根。

#### Computing Square Roots Modulo N　计算模 $N$ 的平方根

It is not hard to see that the algorithm we have shown for computing square roots modulo a prime extends easily to the case of computing square roots modulo a composite $N = pq$ of known factorization. Specifically, let $a \in \mathbb{Z}_N^*$ be a quadratic residue with $a \leftrightarrow (a_p, a_q)$ via the Chinese remainder theorem. Computing the square roots $x_p, x_q$ of $a_p, a_q$ modulo $p$ and $q$, respectively, gives a square root $(x_p, x_q)$ of a (see Section 15.4.2). Given $x_p$ and $x_q$, the representation $x$ corresponding to $(x_p, x_q)$ can be recovered as discussed in Section 9.1.5. That is, to compute a square root of a modulo an integer $N = pq$ of known factorization:

不难看出，上述计算模素数平方根的算法很容易推广到在因子分解已知时计算模合数 $N = pq$ 的平方根。具体来说，设 $a \in \mathbb{Z}_N^*$ 是二次剩余，并在中国剩余定理下有 $a \leftrightarrow (a_p, a_q)$。分别计算 $a_p$ 模 $p$ 的平方根 $x_p$ 和 $a_q$ 模 $q$ 的平方根 $x_q$，就得到 $a$ 的平方根 $(x_p, x_q)$（见 15.4.2 节）。有了 $x_p$ 和 $x_q$ 之后，可按 9.1.5 节讨论的方法恢复与 $(x_p, x_q)$ 对应的表示 $x$。也就是说，要在因子分解已知时计算 $a$ 模整数 $N = pq$ 的平方根：

• Compute $a_p := [a \bmod p]$ and $a_q := [a \bmod q]$.

• 计算 $a_p := [a \bmod p]$ 和 $a_q := [a \bmod q]$。

Using Algorithm 15.31, compute a square root $x_{p}$ of $a_{p}$ modulo p and a square root $x_{q}$ of $a_{q}$ modulo q.

用算法 15.31 计算 $a_{p}$ 模 $p$ 的平方根 $x_{p}$ 和 $a_{q}$ 模 $q$ 的平方根 $x_{q}$。

- Convert from the representation $(x_p, x_q) \in \mathbb{Z}_p^* \times \mathbb{Z}_q^*$ to $x \in \mathbb{Z}_N^*$ with $x \leftrightarrow (x_p, x_q)$. Output $x$, which is a square root of a modulo $N$.

  把表示 $(x_p, x_q) \in \mathbb{Z}_p^* \times \mathbb{Z}_q^*$ 转换为满足 $x \leftrightarrow (x_p, x_q)$ 的 $x \in \mathbb{Z}_N^*$。输出 $x$，它就是 $a$ 模 $N$ 的平方根。

It is easy to modify the algorithm so that it returns all four square roots of a.

很容易修改该算法，使其返回 $a$ 的全部四个平方根。

### 15.5.2 A Trapdoor Permutation Based on Factoring　基于因子分解的陷门置换

We have seen that computing square roots modulo N can be carried out in polynomial time if the factorization of N is known. We show here that, in contrast, computing square roots modulo a composite N of unknown factorization is as hard as factoring N.

我们已经看到，在已知 $N$ 的因子分解时，计算模 $N$ 的平方根可以在多项式时间内完成。这里要证明的是：反过来，在因子分解未知时，计算模合数 $N$ 的平方根与分解 $N$ 一样困难。

More formally, let $\mathsf{GenModulus}$ be a polynomial-time algorithm that, on input ${1}^{n}$, outputs $(N, p, q)$ where $N = pq$ and $p$ and $q$ are $n$-bit primes except with probability negligible in $n$. Consider the following experiment for a given algorithm $\mathcal{A}$ and parameter $n$:

更形式化地说，设 $\mathsf{GenModulus}$ 是一个多项式时间算法，以 ${1}^{n}$ 为输入，输出 $(N, p, q)$，其中 $N = pq$，并且除关于 $n$ 可忽略的概率外，$p$ 和 $q$ 都是 $n$ 比特素数。对给定的算法 $\mathcal{A}$ 和参数 $n$，考虑如下实验：

The square-root computation experiment $\mathsf{SQR}_{\mathcal{A},\mathsf{GenModulus}}(n)$:

平方根计算实验 $\mathsf{SQR}_{\mathcal{A},\mathsf{GenModulus}}(n)$：

1. Run $\mathsf{GenModulus}({1}^{n})$ to obtain output $N, p, q$.

   运行 $\mathsf{GenModulus}({1}^{n})$，得到输出 $N, p, q$。

2. Choose a uniform $y \in \mathcal{QR}_N$.

   均匀选取 $y \in \mathcal{QR}_N$。

3. $\mathcal{A}$ is given $(N,y)$, and outputs $x\in\mathbb{Z}_{N}^{*}$.

   将 $(N,y)$ 交给 $\mathcal{A}$，$\mathcal{A}$ 输出 $x\in\mathbb{Z}_{N}^{*}$。

4. The output of the experiment is defined to be 1 if $x^{2} = y \mod N$, and 0 otherwise.

   若 $x^{2} = y \mod N$，则实验输出定义为 1；否则为 0。

DEFINITION 15.34 We say that computing square roots is hard relative to GenModulus if for all probabilistic polynomial-time algorithms A there exists a negligible function negl such that

定义 15.34　称计算平方根相对于 $\mathsf{GenModulus}$ 是困难的，如果对所有概率多项式时间算法 $\mathcal{A}$，都存在可忽略函数 $\mathsf{negl}$ 使得

$$\Pr[\mathsf{SQR}_{\mathcal{A},\mathsf{GenModulus}}(n)=1]\leq\mathsf{negl}(n).$$

It is easy to see that if computing square roots is hard relative to GenModulus then factoring must be hard relative to GenModulus too: if moduli N output by GenModulus could be factored easily, then it would be easy to compute square roots modulo N by first factoring N and then applying the algorithm discussed in the previous section. Our goal now is to show the converse: that if factoring is hard relative to GenModulus then so is the problem of computing square roots. We emphasize again that an analogous result is not known for the RSA problem or the problem of deciding quadratic residuosity.

容易看出，若计算平方根相对于 $\mathsf{GenModulus}$ 是困难的，则因子分解相对于 $\mathsf{GenModulus}$ 也必定是困难的：如果 $\mathsf{GenModulus}$ 输出的模数 $N$ 可以被轻易分解，那么先分解 $N$、再应用上一节讨论的算法，就能轻易计算模 $N$ 的平方根。我们现在的目标是证明反方向：若因子分解相对于 $\mathsf{GenModulus}$ 是困难的，则计算平方根问题也同样困难。再次强调，对 RSA 问题或判定二次剩余性问题，人们并不知道类似的结果。

The key is the following lemma, which says that two “unrelated” square roots of any element in $\mathbb{Z}_{N}^{*}$ can be used to factor $N$.

关键在于下面的引理：$\mathbb{Z}_{N}^{*}$ 中任一元素的两个“不相关”的平方根可以用来分解 $N$。

LEMMA 15.35 Let $N = pq$ with $p, q$ distinct, odd primes. Given $x, \hat{x}$ such that $x^2 = y = \hat{x}^2 \bmod N$ but $x \neq \pm \hat{x} \bmod N$, it is possible to factor $N$ in time polynomial in $\|N\|$.

引理 15.35　设 $N = pq$，其中 $p, q$ 为不同的奇素数。给定满足 $x^2 = y = \hat{x}^2 \bmod N$ 但 $x \neq \pm \hat{x} \bmod N$ 的 $x, \hat{x}$，就可以在关于 $\|N\|$ 多项式的时间内分解 $N$。

PROOF We claim that either $\gcd(N, x + \hat{x})$ or $\gcd(N, x - \hat{x})$ is equal to one of the prime factors of $N$. Since $\gcd$ computations can be carried out in polynomial time (see Appendix B.1.2), this proves the lemma.

证明　我们断言：$\gcd(N, x + \hat{x})$ 或 $\gcd(N, x - \hat{x})$ 中必有一个等于 $N$ 的某个素因子。由于 $\gcd$ 可以在多项式时间内计算（见附录 B.1.2），这就证明了引理。

If $x^2 = \hat{x}^2 \mod N$ then

若 $x^2 = \hat{x}^2 \mod N$，则

$${0}=x^{2}-\hat{x}^{2}=\left(x-\hat{x}\right)\cdot\left(x+\hat{x}\right)\bmod N,$$

and so $N|(x-\hat{x})(x+\hat{x})$. Then $p|(x-\hat{x})(x+\hat{x})$ and so $p$ divides one of these terms. Say $p|(x+\hat{x})$ (the proof proceeds similarly if $p|(x-\hat{x})$). If $q|(x+\hat{x})$ then $N|(x+\hat{x})$, but this cannot be the case since $x\neq-\hat{x}\bmod N$. So $q\nmid(x+\hat{x})$ and $\gcd(N,x+\hat{x})=p$.

于是 $N|(x-\hat{x})(x+\hat{x})$。进而 $p|(x-\hat{x})(x+\hat{x})$，所以 $p$ 整除这两个因子之一。不妨设 $p|(x+\hat{x})$（若 $p|(x-\hat{x})$，证明完全类似）。若 $q|(x+\hat{x})$，则 $N|(x+\hat{x})$，但这不可能，因为 $x\neq-\hat{x}\bmod N$。所以 $q\nmid(x+\hat{x})$，从而 $\gcd(N,x+\hat{x})=p$。

An alternative way of proving the above is to look at what happens in the Chinese remaindering representation. Say $x \leftrightarrow (x_p, x_q)$. Then, because x and $\hat{x}$ are square roots of the same value y, we know that $\hat{x}$ corresponds to either $(-x_p, x_q)$ or $(x_p, -x_q)$. (It cannot correspond to $(x_p, x_q)$ or $(-x_p, -x_q)$ since the first corresponds to x while the second corresponds to $[-x \bmod N]$, and both possibilities are ruled out by the assumption of the lemma.) Say $\hat{x} \leftrightarrow (-x_p, x_q)$. Then

证明上述结论的另一种方式是考察中国剩余表示下发生的情况。设 $x \leftrightarrow (x_p, x_q)$。由于 x 和 $\hat{x}$ 是同一个值 y 的平方根，可知 $\hat{x}$ 对应 $(-x_p, x_q)$ 或 $(x_p, -x_q)$。（它不可能对应 $(x_p, x_q)$ 或 $(-x_p, -x_q)$，因为前者对应 x，后者对应 $[-x \bmod N]$，而这两种可能都被引理的假设排除了。）不妨设 $\hat{x} \leftrightarrow (-x_p, x_q)$。则

$$[x+\hat{x}\bmod N]\leftrightarrow(x_{p},x_{q})+(-x_{p},x_{q})=(0,[2x_{q}\bmod q]),$$

and we see that $x + \hat{x} = 0 \bmod p$ while $x + \hat{x} \neq 0 \bmod q$. It follows that $\gcd(N, x + \hat{x}) = p$, a factor of N.

可见 $x + \hat{x} = 0 \bmod p$ 而 $x + \hat{x} \neq 0 \bmod q$。由此可得 $\gcd(N, x + \hat{x}) = p$，即 $N$ 的一个因子。

We can now prove the main result of this section.

现在可以证明本节的主要结果。

THEOREM 15.36 If factoring is hard relative to GenModulus, then computing square roots is hard relative to GenModulus.

定理 15.36　若因子分解相对于 $\mathsf{GenModulus}$ 是困难的，则计算平方根相对于 $\mathsf{GenModulus}$ 也是困难的。

PROOF Let A be a probabilistic polynomial-time algorithm computing square roots (as in Definition 15.34). Consider the following probabilistic polynomial-time algorithm $A_{fact}$ for factoring moduli output by GenModulus:

证明　设 $\mathcal{A}$ 是计算平方根的概率多项式时间算法（如定义 15.34 所述）。考虑如下用于分解 $\mathsf{GenModulus}$ 输出的模数的概率多项式时间算法 $A_{fact}$：

Algorithm $A_{fact}$:

算法 $A_{fact}$：

The algorithm is given a modulus $N$ as input.

该算法以模数 $N$ 为输入。

• Choose a uniform $x \in \mathbb{Z}_N^*$ and compute $y := [x^2 \bmod N]$.

• 均匀选取 $x \in \mathbb{Z}_N^*$，计算 $y := [x^2 \bmod N]$。

• Run $\mathcal{A}(N,y)$ to obtain output $\hat{x}$.

• 运行 $\mathcal{A}(N,y)$，得到输出 $\hat{x}$。

• If $\hat{x}^2 = y \bmod N$ and $\hat{x} \neq \pm x \bmod N$, then factor $N$ using Lemma 15.35.

• 若 $\hat{x}^2 = y \bmod N$ 且 $\hat{x} \neq \pm x \bmod N$，则用引理 15.35 分解 $N$。

By Lemma 15.35, we know that $\mathcal{A}_{\mathsf{fact}}$ succeeds in factoring $N$ exactly when $\hat{x} \neq \pm x \bmod N$ and $\hat{x}^2 = y \bmod N$. That is,

由引理 15.35 可知，$\mathcal{A}_{\mathsf{fact}}$ 成功分解 $N$ 当且仅当 $\hat{x} \neq \pm x \bmod N$ 且 $\hat{x}^2 = y \bmod N$。即

$$\begin{aligned}&\Pr[\mathsf{Factor}_{\mathcal{A}_{\mathsf{fact}},\mathsf{GenModulus}}(n)=1]\\ &=\Pr\left[\hat{x}\neq\pm x\bmod N\land\hat{x}^{2}=y\bmod N\right]\\ &=\Pr\left[\hat{x}\neq\pm x\bmod N\mid\hat{x}^{2}=y\bmod N\right]\cdot\Pr\left[\hat{x}^{2}=y\bmod N\right],\\ \end{aligned} \tag{15.7}$$

where the above probabilities all refer to experiment $\mathsf{Factor}_{\mathcal{A}_{\mathsf{fact}}, \mathsf{GenModulus}}(n)$ (see Section 9.2.3 for a description of this experiment). In the experiment, the modulus $N$ given as input to $\mathcal{A}_{\mathsf{fact}}$ is generated by $\mathsf{GenModulus}(1^n)$, and $y$ is a uniform quadratic residue modulo $N$ since $x$ was chosen uniformly from $\mathbb{Z}_N^*$ (see Section 15.4.4). So the view of $\mathcal{A}$ when run as a subroutine by $\mathcal{A}_{\mathsf{fact}}$ is distributed exactly as $\mathcal{A}$'s view in experiment $\mathsf{SQR}_{\mathcal{A}, \mathsf{GenModulus}}(n)$. Therefore,

其中上述概率都对应实验 $\mathsf{Factor}_{\mathcal{A}_{\mathsf{fact}}, \mathsf{GenModulus}}(n)$（该实验的描述见 9.2.3 节）。在该实验中，作为输入交给 $\mathcal{A}_{\mathsf{fact}}$ 的模数 $N$ 由 $\mathsf{GenModulus}(1^n)$ 生成；又因为 $x$ 是从 $\mathbb{Z}_N^*$ 中均匀选取的，$y$ 是模 $N$ 的均匀二次剩余（见 15.4.4 节）。所以，$\mathcal{A}$ 作为 $\mathcal{A}_{\mathsf{fact}}$ 的子程序运行时的视图，与 $\mathcal{A}$ 在实验 $\mathsf{SQR}_{\mathcal{A}, \mathsf{GenModulus}}(n)$ 中的视图分布完全一致。因此，

$$\Pr\left[\hat{x}^{2}=y\bmod N\right]=\Pr\left[\mathsf{SQR}_{\mathcal{A},\mathsf{GenModulus}}(n)=1\right]. \tag{15.8}$$

Conditioned on the value of the quadratic residue $y$ used in experiment $\mathsf{Factor}_{\mathcal{A}_{\mathsf{fact}},\mathsf{GenModulus}}(n)$, the value $x$ is equally likely to be any of the four possible square roots of $y$. This means that from the point of view of algorithm $\mathcal{A}$ (being run as a subroutine by $\mathcal{A}_{\mathsf{fact}}$), $x$ is equally likely to be each of the four square roots of $y$. This in turn means that, conditioned on $\mathcal{A}$ outputting some square root $\hat{x}$ of $y$, the probability that $\hat{x} = \pm x \bmod N$ is exactly ${1}/{2}$. (We stress that we do not make any assumption about how $\hat{x}$ is distributed among the square roots of $y$, and in particular are not assuming here that $\mathcal{A}$ outputs a uniform square root of $y$. Rather we are using the fact that $x$ is uniformly distributed among the square roots of $y$.) That is,

在实验 $\mathsf{Factor}_{\mathcal{A}_{\mathsf{fact}},\mathsf{GenModulus}}(n)$ 中所用的二次剩余 $y$ 取定的条件下，$x$ 等可能地是 $y$ 的四个平方根中的任何一个。这意味着，从算法 $\mathcal{A}$（作为 $\mathcal{A}_{\mathsf{fact}}$ 的子程序运行）的角度看，$x$ 等可能地是 $y$ 的四个平方根中的每一个。这又意味着，在 $\mathcal{A}$ 输出 $y$ 的某个平方根 $\hat{x}$ 的条件下，$\hat{x} = \pm x \bmod N$ 的概率恰好是 ${1}/{2}$。（我们强调，这里对 $\hat{x}$ 在 $y$ 的各平方根之间如何分布不作任何假设，特别地，并不假设 $\mathcal{A}$ 输出 $y$ 的均匀平方根；我们利用的是 $x$ 在 $y$ 的各平方根中均匀分布这一事实。）即

$$\Pr\left[\hat{x}\neq\pm x\bmod N\big|\ \hat{x}^{2}=y\bmod N\right]=\frac{1}{2}. \tag{15.9}$$

Combining Equations (15.7)–(15.9), we see that

联立式 (15.7)–(15.9)，可得

$$\Pr\left[\mathsf{Factor}_{\mathcal{A}_{\mathsf{fact}},\mathsf{GenModulus}}(n)=1\right]=\frac{1}{2}\cdot\Pr\left[\mathsf{SQR}_{\mathcal{A},\mathsf{GenModulus}}(n)=1\right].$$

Since factoring is hard relative to GenModulus, there is a negligible function negl such that

由于因子分解相对于 $\mathsf{GenModulus}$ 是困难的，存在可忽略函数 $\mathsf{negl}$ 使得

$$\begin{array}{r}{\Pr[\mathsf{Factor}_{\mathcal{A}_{\mathsf{fact}},\mathsf{GenModulus}}(n)=1]\leq\mathsf{negl}(n),}\end{array}$$

which implies $\Pr\left[\mathsf{SQR}_{\mathcal{A},\mathsf{GenModulus}}(n)=1\right]\leq2\cdot\mathsf{negl}(n)$. Since $\mathcal{A}$ was arbitrary, this completes the proof.

这蕴含 $\Pr\left[\mathsf{SQR}_{\mathcal{A},\mathsf{GenModulus}}(n)=1\right]\leq2\cdot\mathsf{negl}(n)$。由于 $\mathcal{A}$ 是任意的，证明完毕。

The previous theorem leads directly to a family of one-way functions (see Definition 9.76) based on any GenModulus relative to which factoring is hard:

由上述定理可直接得到一个单向函数族（见定义 9.76），它基于任意使因子分解困难的 $\mathsf{GenModulus}$：

Algorithm Gen, on input ${1}^n$, runs GenModulus( ${1}^n$) to obtain $(N, p, q)$ and outputs $I = N$. The domain $\mathcal{D}_I$ is $\mathbb{Z}_N^*$ and the range $\mathcal{R}_I$ is $\mathcal{QR}_N$.

算法 $\mathsf{Gen}$：以 ${1}^n$ 为输入，运行 $\mathsf{GenModulus}({1}^n)$ 得到 $(N, p, q)$，输出 $I = N$。定义域 $\mathcal{D}_I$ 为 $\mathbb{Z}_N^*$，值域 $\mathcal{R}_I$ 为 $\mathcal{QR}_N$。

Algorithm Samp, on input $N$, chooses a uniform element $x \in \mathbb{Z}_N^*$.

算法 Samp：以 $N$ 为输入，均匀选取元素 $x \in \mathbb{Z}_N^*$。

- Algorithm $f$, on input $N$ and $x \in \mathbb{Z}_N^*$, outputs $[x^2 \bmod N]$.

  算法 $f$：以 $N$ 和 $x \in \mathbb{Z}_N^*$ 为输入，输出 $[x^2 \bmod N]$。

The preceding theorem shows that this family is one-way if factoring is hard relative to GenModulus.

上述定理表明，若因子分解相对于 $\mathsf{GenModulus}$ 是困难的，则该族是单向的。

We can turn this into a family of one-way permutations by using moduli $N$ of a special form and letting $\mathcal{D}_I$ be a subset of $\mathbb{Z}_N^*$. (See Exercise 15.20 for another way to make this a permutation.) Call $N = pq$ a Blum integer if $p$ and $q$ are distinct primes with $p \equiv q \equiv 3 \bmod 4$. The key to building a permutation is the following proposition.

若使用特殊形式的模数 $N$，并把 $\mathcal{D}_I$ 取为 $\mathbb{Z}_N^*$ 的子集，就可以把它变成单向置换族。（另一种使其成为置换的方法见习题 15.20。）若 $N = pq$ 中 $p$ 和 $q$ 是满足 $p \equiv q \equiv 3 \bmod 4$ 的不同素数，则称 $N$ 为 Blum 整数。构造置换的关键在于下面的命题。

PROPOSITION 15.37 Let N be a Blum integer. Then every quadratic residue modulo N has exactly one square root that is also a quadratic residue.

命题 15.37　设 $N$ 为 Blum 整数。则模 $N$ 的每个二次剩余都恰好有一个本身也是二次剩余的平方根。

PROOF Say $N = pq$ with $p \equiv q \equiv 3 \bmod 4$. Using Proposition 15.17, we see that $-1$ is not a quadratic residue modulo $p$ or $q$. This is because for $p = 3 \mod 4$ it holds that $p = 4i + 3$ for some $i$ and so

证明　设 $N = pq$，其中 $p \equiv q \equiv 3 \bmod 4$。利用命题 15.17 可知，$-1$ 不是模 $p$ 或模 $q$ 的二次剩余。这是因为当 $p = 3 \mod 4$ 时，存在某个 $i$ 使 $p = 4i + 3$，于是

$$(-1)^{\frac{p-1}{2}}=(-1)^{2i+1}=-1\bmod p$$

(because ${2}i+1$ is odd). Now let $y \leftrightarrow (y_p, y_q)$ be an arbitrary quadratic residue modulo $N$ with the four square roots

（因为 ${2}i+1$ 是奇数）。现在设 $y \leftrightarrow (y_p, y_q)$ 是模 $N$ 的任意二次剩余，其四个平方根为

$$(x_{p},x_{q}),\quad(-x_{p},x_{q}),\quad(x_{p},-x_{q}),\quad(-x_{p},-x_{q}).$$

We claim that exactly one of these is a quadratic residue modulo $N$. To see this, assume $\mathcal{J}_{p}(x_{p}) = +1$ and $\mathcal{J}_{q}(x_{q}) = -1$ (the proof proceeds similarly in any other case). Using Proposition 15.19, we have

我们断言其中恰好有一个是模 $N$ 的二次剩余。为看清这一点，不妨设 $\mathcal{J}_{p}(x_{p}) = +1$ 且 $\mathcal{J}_{q}(x_{q}) = -1$（其余情形的证明类似）。利用命题 15.19，有

$$\mathcal{J}_{q}(-x_{q})=\mathcal{J}_{q}(-1)\cdot\mathcal{J}_{q}(x_{q})=+1,$$

and so $(x_p, -x_q)$ corresponds to a quadratic residue modulo $N$ (using Proposition 15.21). Similarly, $\mathcal{J}_p(-x_p) = -1$ and so none of the other square roots of $y$ are quadratic residues modulo $N$.

于是 $(x_p, -x_q)$ 对应模 $N$ 的一个二次剩余（利用命题 15.21）。类似地，$\mathcal{J}_p(-x_p) = -1$，故 $y$ 的其余平方根都不是模 $N$ 的二次剩余。

Expressed differently, the above proposition says that when $N$ is a Blum integer, the function $f_N : \mathcal{QR}_N \to \mathcal{QR}_N$ given by $f_N(x) = [x^2 \bmod N]$ is a permutation over $\mathcal{QR}_N$. Modifying the sampling algorithm $\mathsf{Samp}$ above to choose a uniform $x \in \mathcal{QR}_N$ (which, as we have already seen, can be done easily by choosing uniform $r \in \mathbb{Z}_N^*$ and setting $x := [r^2 \bmod N]$) gives a family of one-way permutations. Finally, because square roots modulo $N$ can be computed in polynomial time given the factorization of $N$, a straightforward modification yields a family of trapdoor permutations based on any $\mathsf{GenModulus}$ relative to which factoring is hard. This is sometimes called the $\text{Rabin}$ family of trapdoor permutations. In summary:

换一种说法，上述命题表明：当 $N$ 是 Blum 整数时，由 $f_N(x) = [x^2 \bmod N]$ 给出的函数 $f_N : \mathcal{QR}_N \to \mathcal{QR}_N$ 是 $\mathcal{QR}_N$ 上的一个置换。把上面的采样算法 $\mathsf{Samp}$ 修改为均匀选取 $x \in \mathcal{QR}_N$（前面已经看到，这很容易做到：均匀选取 $r \in \mathbb{Z}_N^*$，再令 $x := [r^2 \bmod N]$），就得到一个单向置换族。最后，由于在已知 $N$ 的因子分解时可以在多项式时间内计算模 $N$ 的平方根，再作一点直接的修改，就得到基于任意使因子分解困难的 $\mathsf{GenModulus}$ 的陷门置换族。它有时称为 $\text{Rabin}$ 陷门置换族。总结如下：

THEOREM 15.38 Let GenModulus be an algorithm that, on input ${1}^{n}$, outputs $(N, p, q)$ where $N = pq$ and $p$ and $q$ are distinct primes (except possibly with negligible probability) with $p \equiv q \equiv 3 \bmod 4$. If factoring is hard relative to GenModulus, then there exists a family of trapdoor permutations.

定理 15.38　设 $\mathsf{GenModulus}$ 是一个算法，以 ${1}^{n}$ 为输入，输出 $(N, p, q)$，其中 $N = pq$，且（除可能以可忽略的概率外）$p$ 和 $q$ 是满足 $p \equiv q \equiv 3 \bmod 4$ 的不同素数。若因子分解相对于 $\mathsf{GenModulus}$ 是困难的，则存在陷门置换族。

### 15.5.3 The Rabin Encryption Scheme　Rabin 加密方案

We can apply the results of Section 15.1.2 to the Rabin trapdoor permutation to obtain a public-key encryption scheme whose security is based on factoring. To do this, we first need to identify a hard-core predicate for this trapdoor permutation. Although we could appeal to Theorem 15.3, which states that a suitable hard-core predicate always exists, it turns out that the least significant bit $\mathsf{lsb}$ is a hard-core predicate for the Rabin trapdoor permutation just as it is for the case of RSA (see Section 12.5.3). Using this as our hard-core predicate, we obtain the scheme of Construction 15.39.

把 15.1.2 节的结果应用到 Rabin 陷门置换上，就可以得到一个安全性基于因子分解的公钥加密方案。为此，首先需要为该陷门置换确定一个难核谓词。虽然可以诉诸定理 15.3——它表明合适的难核谓词总是存在——但事实证明，最低有效位 $\mathsf{lsb}$ 就是 Rabin 陷门置换的难核谓词，正如它在 RSA 情形中一样（见 12.5.3 节）。以它作为难核谓词，便得到构造 15.39 中的方案。

**CONSTRUCTION 15.39**

**构造 15.39**

Let GenModulus be a polynomial-time algorithm that, on input ${1}^{n}$, outputs $(N, p, q)$ where $N = pq$ and $p$ and $q$ are $n$-bit primes (except with probability negligible in $n$) with $p \equiv q \equiv 3 \bmod 4$. Construct a public-key encryption scheme as follows:

设 $\mathsf{GenModulus}$ 是一个多项式时间算法，以 ${1}^{n}$ 为输入，输出 $(N, p, q)$，其中 $N = pq$，并且（除关于 $n$ 可忽略的概率外）$p$ 和 $q$ 是满足 $p \equiv q \equiv 3 \bmod 4$ 的 $n$ 比特素数。如下构造公钥加密方案：

Gen: on input ${1}^{n}$ run GenModulus( ${1}^{n}$) to obtain $(N, p, q)$. The public key is $N$, and the private key is $\langle p, q \rangle$.

Gen：以 ${1}^{n}$ 为输入，运行 $\mathsf{GenModulus}$( ${1}^{n}$) 得到 $(N, p, q)$。公钥为 $N$，私钥为 $\langle p, q \rangle$。

- Enc: on input a public-key $N$ and message $m \in \{0,1\}$, choose a uniform $x \in \mathcal{QR}_N$ subject to the constraint that $\mathsf{lsb}(x) = m$. Output the ciphertext $c := [x^2 \bmod N]$.

  Enc：以公钥 $N$ 和消息 $m \in \{0,1\}$ 为输入，在约束 $\mathsf{lsb}(x) = m$ 下均匀选取 $x \in \mathcal{QR}_N$。输出密文 $c := [x^2 \bmod N]$。

- Dec: on input a private key $\langle p, q \rangle$ and a ciphertext $c$, compute the unique $x \in \mathcal{QR}_N$ such that $x^2 = c \mod N$, and output $\text{lsb}(x)$.

  Dec：以私钥 $\langle p, q \rangle$ 和密文 $c$ 为输入，计算满足 $x^2 = c \mod N$ 的唯一 $x \in \mathcal{QR}_N$，输出 $\text{lsb}(x)$。

The Rabin encryption scheme.

Rabin 加密方案。

Theorems 15.5 and 15.38 imply the following result.

定理 15.5 和定理 15.38 蕴含以下结果。

THEOREM 15.40 If factoring is hard relative to GenModulus, then Construction 15.39 is CPA-secure.

定理 15.40　若因子分解相对于 $\mathsf{GenModulus}$ 是困难的，则构造 15.39 是选择明文安全的。

#### Rabin Encryption vs. RSA Encryption　Rabin 加密与 RSA 加密的比较

It is worthwhile to remark on the similarities and differences between the Rabin and RSA cryptosystems. (The discussion here applies to any cryptographic construction—not necessarily a public-key encryption scheme—based on the Rabin or RSA trapdoor permutations.)

值得对 Rabin 与 RSA 密码体制的异同作一番评述。（这里的讨论适用于任何基于 Rabin 或 RSA 陷门置换的密码构造——不一定是公钥加密方案。）

The RSA and Rabin trapdoor permutations appear quite similar, with squaring in the case of Rabin corresponding to taking $e = 2$ in the case of RSA. (Of course, 2 is not relatively prime to $\phi(N)$ and so Rabin is not a special case of RSA.) In terms of the security offered by each construction, hardness of computing modular square roots is equivalent to hardness of factoring, whereas hardness of solving the RSA problem is not known to be implied by the hardness of factoring. The Rabin trapdoor permutation is thus based on a potentially weaker assumption: it is theoretically possible that someone might develop an efficient algorithm for solving the RSA problem, yet computing square roots will remain hard. Or, someone may develop an algorithm that solves the RSA problem faster than known factoring algorithms. Lemma 15.35 ensures, however, that computing square roots modulo $N$ can never be much faster than the best available algorithm for factoring $N$.

RSA 与 Rabin 陷门置换看起来十分相似：Rabin 中的取平方相当于 RSA 中取 $e = 2$。（当然，2 与 $\phi(N)$ 并不互素，所以 Rabin 并不是 RSA 的特例。）就各构造提供的安全性而言，计算模平方根的困难性与因子分解的困难性等价，而求解 RSA 问题的困难性能否由因子分解的困难性推出，目前尚不清楚。因此，Rabin 陷门置换建立在可能更弱的假设之上：理论上存在这样的可能——有人发明了高效求解 RSA 问题的算法，而计算平方根仍然困难；或者有人发明了比已知因子分解算法更快地求解 RSA 问题的算法。然而，引理 15.35 保证：计算模 $N$ 的平方根绝不可能显著快于目前已知的最佳 $N$ 因子分解算法。

In terms of their efficiency, the RSA and Rabin permutations are essentially the same. Actually, if a large exponent $e$ is used in the case of RSA then computing eth powers (as in RSA) is slightly slower than squaring (as in Rabin). On the other hand, a bit more care is required when working with the Rabin permutation since it is only a permutation over a subset of $\mathbb{Z}_N^*$, in contrast to RSA, which gives a permutation over all of $\mathbb{Z}_N^*$.

就效率而言，RSA 与 Rabin 置换基本相同。实际上，如果 RSA 使用较大的指数 $e$，那么计算 e 次幂（如 RSA）会比取平方（如 Rabin）稍慢一些。另一方面，使用 Rabin 置换时需要多一分小心，因为它只是 $\mathbb{Z}_N^*$ 某个子集上的置换，而 RSA 给出的则是整个 $\mathbb{Z}_N^*$ 上的置换。

A “plain Rabin” encryption scheme, constructed in a manner analogous to plain RSA encryption, is vulnerable to a chosen-ciphertext attack that enables an adversary to learn the entire private key (see Exercise 15.18). Although plain RSA is not CCA-secure either, known chosen-ciphertext attacks on plain RSA are less damaging since they recover the message but not the private key. Perhaps the existence of such an attack on “plain Rabin” influenced cryptographers, early on, to reject the use of Rabin encryption entirely.

以类似于朴素 RSA 加密的方式构造的“朴素 Rabin”加密方案，容易受到一种选择密文攻击，敌手借此可以获知整个私钥（见习题 15.18）。虽然朴素 RSA 也不是选择密文安全的，但已知的针对朴素 RSA 的选择密文攻击危害较小，因为它们只能恢复消息而不能恢复私钥。也许正是因为“朴素 Rabin”存在这样的攻击，密码学界早期便彻底弃用了 Rabin 加密。

In summary, the RSA permutation is much more widely used in practice than the Rabin permutation, but in light of the above this appears to be due more to historical accident than to any compelling technical justification.

总而言之，RSA 置换在实践中比 Rabin 置换应用得广泛得多；但鉴于上述讨论，这似乎更多是出于历史偶然，而非有什么令人信服的技术依据。

## References and Additional Reading　参考文献与扩展阅读

The existence of public-key encryption based on arbitrary trapdoor permutations was shown by Yao [205], and the efficiency improvement discussed at the end of Section 15.1.2 is due to Blum and Goldwasser [40].

基于任意陷门置换的公钥加密的存在性由 Yao [205] 证明；15.1.2 节末尾讨论的效率改进归功于 Blum 和 Goldwasser [40]。

Childs [51] and Shoup [183] provide further coverage of the (computational) number theory used in this chapter. A good description of the algorithm for computing the Jacobi symbol modulo a composite of unknown factorization, along with a proof of correctness, is given in [64].

Childs [51] 和 Shoup [183] 对本章所用的（计算）数论有更深入的介绍。对在因子分解未知时计算模合数雅可比符号的算法，[64] 给出了出色的描述及正确性证明。

The Paillier encryption scheme was introduced in [157]. Shoup [183, Section 7.5] gives a characterization of $\mathbb{Z}_{N^e}^*$ for arbitrary integers $N, e$ (and not just $N = pq$, $e = 2$ as done here).

Paillier 加密方案由 [157] 提出。Shoup [183, 7.5 节] 对任意整数 $N, e$ 给出了 $\mathbb{Z}_{N^e}^*$ 的刻画（而不仅是这里所做的 $N = pq$、$e = 2$）。

The problem of deciding quadratic residuosity modulo a composite of unknown factorization goes back to Gauss [78] and is related to other (conjectured) hard number-theoretic problems. The Goldwasser–Micali encryption scheme [87], introduced in 1982, was the first public-key encryption scheme with a proof of security.

在因子分解未知时判定模合数二次剩余性的问题可追溯到高斯 [78]，并与其他（被猜想为）困难的数论问题相关。1982 年提出的 Goldwasser–Micali 加密方案 [87] 是第一个带有安全性证明的公钥加密方案。

Rabin [166] showed that computing square roots modulo a composite is equivalent to factoring. The results of Section 15.5.2 are due to Blum [39]. Hard-core predicates for the Rabin trapdoor permutation are discussed in [8, 94, 7] and references therein.

Rabin [166] 证明了计算模合数的平方根与因子分解等价。15.5.2 节的结果归功于 Blum [39]。Rabin 陷门置换的难核谓词在 [8, 94, 7] 及其所引文献中有讨论。

## Exercises　习题

15.1 Construct and prove CPA-security for a KEM based on any trapdoor permutation by suitably generalizing Construction 12.34.

     15.1 通过适当推广构造 12.34，基于任意陷门置换构造一个 KEM，并证明其选择明文安全。

15.2 Show that the isomorphism of Proposition 15.6 can be efficiently inverted when the factorization of $N$ is known.

     15.2 证明：在已知 $N$ 的因子分解时，命题 15.6 中的同构可以被高效地求逆。

15.3 Generalize the Paillier encryption scheme so $(1+N)$ is replaced by any $g \in \mathbb{Z}_{N^2}^*$ of order $N$. I.e., the public key now includes $g$, and encryption of $m$ is done by computing the ciphertext $c := [g^m \cdot r^N \mod N^2]$.

     15.3 推广 Paillier 加密方案，把 $(1+N)$ 换成任意阶为 $N$ 的 $g \in \mathbb{Z}_{N^2}^*$。即公钥现在包含 $g$，加密 $m$ 通过计算密文 $c := [g^m \cdot r^N \mod N^2]$ 完成。

(a) Show how decryption can be done.

     (a) 说明如何解密。

(b) Prove CPA-security under the same assumption as in Theorem 15.13.

     (b) 在与定理 15.13 相同的假设下证明其选择明文安全。

15.4 Let $\Psi(N^2)$ denote the set $\{(a,1)\mid a\in\mathbb{Z}_N\}\subset\mathbb{Z}_{N^2}^*$. Show that it is not hard to decide whether a given element $y\in\mathbb{Z}_{N^2}^*$ is in $\Psi(N^2)$.

     15.4 记 $\Psi(N^2)$ 为集合 $\{(a,1)\mid a\in\mathbb{Z}_N\}\subset\mathbb{Z}_{N^2}^*$。证明：判定给定元素 $y\in\mathbb{Z}_{N^2}^*$ 是否属于 $\Psi(N^2)$ 并不困难。

15.5 Let $\mathbb{G}$ be an abelian group. Show that the set of quadratic residues in $\mathbb{G}$ forms a subgroup.

     15.5 设 $\mathbb{G}$ 为阿贝尔群。证明：$\mathbb{G}$ 中全体二次剩余构成一个子群。

15.6 This question concerns the quadratic residues in the additive group $\mathbb{Z}_N$. (An element $y \in \mathbb{Z}_N$ is a quadratic residue if and only if there exists an $x \in \mathbb{Z}_N$ with ${2}x = y \mod N$.)

     15.6 本题关注加法群 $\mathbb{Z}_N$ 中的二次剩余。（元素 $y \in \mathbb{Z}_N$ 是二次剩余，当且仅当存在 $x \in \mathbb{Z}_N$ 使得 ${2}x = y \mod N$。）

(a) Let $p$ be an odd prime. How many elements of $\mathbb{Z}_p$ are quadratic residues?

     (a) 设 $p$ 为奇素数。$\mathbb{Z}_p$ 中有多少个元素是二次剩余？

(b) Let $N = pq$ be a product of two odd primes $p$ and $q$. How many elements of $\mathbb{Z}_N$ are quadratic residues?

     (b) 设 $N = pq$ 为两个奇素数 $p$ 和 $q$ 的乘积。$\mathbb{Z}_N$ 中有多少个元素是二次剩余？

(c) Let $N$ be an even integer. How many elements of $\mathbb{Z}_N$ are quadratic residues?

     (c) 设 $N$ 为偶数。$\mathbb{Z}_N$ 中有多少个元素是二次剩余？

15.7 Let $N = pq$ with $p, q$ distinct, odd primes. Show a PPT algorithm for choosing a uniform element of $\mathcal{QNR}_{N}^{+1}$ when the factorization of $N$ is known. (Your algorithm can have failure probability negligible in $\|N\|$.)

     15.7 设 $N = pq$，其中 $p, q$ 为不同的奇素数。给出一个 PPT 算法，在已知 $N$ 的因子分解时选取 $\mathcal{QNR}_{N}^{+1}$ 中的均匀元素。（你的算法可以具有关于 $\|N\|$ 可忽略的失败概率。）

15.8 Let $N = pq$ with $p, q$ distinct, odd primes. Prove that if $x \in \mathcal{QR}_N$ then $[x^{-1} \bmod N] \in \mathcal{QR}_N$, and if $x \in \mathcal{QNR}_N^{+1}$ then $[x^{-1} \bmod N] \in \mathcal{QNR}_N^{+1}$.

     15.8 设 $N = pq$，其中 $p, q$ 为不同的奇素数。证明：若 $x \in \mathcal{QR}_N$，则 $[x^{-1} \bmod N] \in \mathcal{QR}_N$；若 $x \in \mathcal{QNR}_N^{+1}$，则 $[x^{-1} \bmod N] \in \mathcal{QNR}_N^{+1}$。

15.9 Let $N = pq$ with $p, q$ distinct, odd primes, and fix $z \in \mathcal{QNR}_{N}^{+1}$. Show that choosing uniform $x \in \mathcal{QR}_{N}$ and setting $y := [z \cdot x \mod N]$ gives a $y$ that is uniformly distributed in $\mathcal{QNR}_{N}^{+1}$. That is, for any $\hat{y} \in \mathcal{QNR}_{N}^{+1}$:

     15.9 设 $N = pq$，其中 $p, q$ 为不同的奇素数，并固定 $z \in \mathcal{QNR}_{N}^{+1}$。证明：均匀选取 $x \in \mathcal{QR}_{N}$ 并令 $y := [z \cdot x \mod N]$，得到的 $y$ 在 $\mathcal{QNR}_{N}^{+1}$ 中均匀分布。即对任意 $\hat{y} \in \mathcal{QNR}_{N}^{+1}$ 都有

$$\begin{array}{r}{\Pr[z\cdot x=\hat{y}\bmod N]=1/|\mathcal{QNR}_{N}^{+1}|,}\end{array}$$

where the probability is taken over uniform choice of $x \in \mathcal{QR}_{N}$.

     其中概率基于 $x \in \mathcal{QR}_{N}$ 的均匀选取。

Hint: Use the previous exercise.

     提示：利用上一题。

15.10 Let $N$ be the product of 5 distinct, odd primes. If $y \in \mathbb{Z}_N^*$ is a quadratic residue, how many solutions are there to the equation $x^2 = y \mod N?$

     15.10 设 $N$ 为 5 个不同奇素数的乘积。若 $y \in \mathbb{Z}_N^*$ 是二次剩余，方程 $x^2 = y \mod N$ 有多少个解？

15.11 Show that the Goldwasser–Micali encryption scheme is homomorphic if the message space $\{0,1\}$ is viewed as the group $\mathbb{Z}_2$.

     15.11 证明：若把消息空间 $\{0,1\}$ 视为群 $\mathbb{Z}_2$，则 Goldwasser–Micali 加密方案是同态的。

15.12 Consider the following variation of the Goldwasser–Micali encryption scheme: $\mathsf{GenModulus}(1^n)$ is run to obtain $(N, p, q)$ where $N = pq$ and $p \equiv q \equiv 3 \bmod 4$, (i.e., $N$ is a Blum integer.) The public key is $N$ and the private key is $\langle p, q \rangle$. To encrypt $m \in \{0,1\}$, the sender chooses uniform $x \in \mathbb{Z}_N$ and computes the ciphertext $c := [(-1)^m \cdot x^2 \mod N]$.

     15.12 考虑 Goldwasser–Micali 加密方案的如下变体：运行 $\mathsf{GenModulus}(1^n)$ 得到 $(N, p, q)$，其中 $N = pq$ 且 $p \equiv q \equiv 3 \bmod 4$（即 $N$ 是 Blum 整数）。公钥为 $N$，私钥为 $\langle p, q \rangle$。加密 $m \in \{0,1\}$ 时，发送方均匀选取 $x \in \mathbb{Z}_N$，并计算密文 $c := [(-1)^m \cdot x^2 \mod N]$。

(a) Prove that for $N$ of the stated form, $[-1 \mod N] \in \mathcal{QNR}_{N}^{+1}$.

     (a) 证明：对具有上述形式的 $N$，有 $[-1 \mod N] \in \mathcal{QNR}_{N}^{+1}$。

(b) Prove that the scheme described has indistinguishable encryptions under a chosen-plaintext attack if deciding quadratic residuosity is hard relative to GenModulus.

     (b) 证明：若判定二次剩余性相对于 $\mathsf{GenModulus}$ 是困难的，则所述方案在选择明文攻击下具有不可区分加密。

15.13 Assume deciding quadratic residuosity is hard for GenModulus. Show that this implies the hardness of distinguishing a uniform element of $\mathcal{QR}_N$ from a uniform element of $\mathcal{J}_N^{+1}$.

     15.13 假设判定二次剩余性相对于 $\mathsf{GenModulus}$ 是困难的。证明：这意味着区分 $\mathcal{QR}_N$ 中的均匀元素与 $\mathcal{J}_N^{+1}$ 中的均匀元素也是困难的。

15.14 Show that plain RSA encryption of a message $m$ leaks $\mathcal{J}_N(m)$.

     15.14 证明：对消息 $m$ 的朴素 RSA 加密会泄露 $\mathcal{J}_N(m)$。

15.15 Consider the following variation of the Goldwasser–Micali encryption scheme: $\mathsf{GenModulus}(1^n)$ is run to obtain $(N, p, q)$. The public key is $N$ and the private key is $\langle p, q \rangle$. To encrypt a 0, the sender chooses $n$ uniform elements $c_1, \ldots, c_n \in \mathcal{QR}_N$. To encrypt a 1, the sender chooses $n$ uniform elements $c_1, \ldots, c_n \in \mathcal{J}_N^{+1}$. In each case, the resulting ciphertext is $c^* = \langle c_1, \ldots, c_n \rangle$.

     15.15 考虑 Goldwasser–Micali 加密方案的如下变体：运行 $\mathsf{GenModulus}(1^n)$ 得到 $(N, p, q)$。公钥为 $N$，私钥为 $\langle p, q \rangle$。加密 0 时，发送方选取 $n$ 个均匀的元素 $c_1, \ldots, c_n \in \mathcal{QR}_N$；加密 1 时，发送方选取 $n$ 个均匀的元素 $c_1, \ldots, c_n \in \mathcal{J}_N^{+1}$。无论哪种情形，所得密文均为 $c^* = \langle c_1, \ldots, c_n \rangle$。

(a) Show how the sender can generate a uniform element of $\mathcal{J}_{N}^{+1}$ in polynomial time, where failing with negligible probability.

     (a) 说明发送方如何以多项式时间生成 $\mathcal{J}_{N}^{+1}$ 中的均匀元素，且失败概率可忽略。

(b) Suggest a way for the receiver to decrypt efficiently, although with negligible error probability.

     (b) 给出一种接收方高效解密的方法（但错误概率可忽略）。

(c) Prove that if deciding quadratic residuosity is hard relative to GenModulus, this scheme is CPA-secure.

     (c) 证明：若判定二次剩余性相对于 $\mathsf{GenModulus}$ 是困难的，则该方案是选择明文安全的。

Hint: Use the previous exercise.

     提示：利用上一题。

15.16 Let $\mathcal{G}$ be a polynomial-time algorithm that, on input ${1}^n$, outputs a prime $p$ with $\|p\| = n$ and a generator $g$ of $\mathbb{Z}_p^*$. Prove that the DDH problem is not hard relative to $\mathcal{G}$.

     15.16 设 $\mathcal{G}$ 是一个多项式时间算法，输入 ${1}^n$ 时输出满足 $\|p\| = n$ 的素数 $p$ 和 $\mathbb{Z}_p^*$ 的生成元 g。证明：DDH 问题相对于 $\mathcal{G}$ 并不困难。

Hint: Use the fact that quadratic residuosity can be decided efficiently modulo a prime.

     提示：利用“模素数的二次剩余性可以高效判定”这一事实。

15.17 The discrete logarithm problem is believed to be hard for $\mathcal{G}$ as in the previous exercise. This means that the function (family) $f_{p,g}$ where $f_{p,g}(x) \overset{\mathrm{def}}{=} [g^x \bmod p]$ is one-way. Let $\mathsf{lsb}(x)$ denote the least-significant bit of $x$. Show that $\mathsf{lsb}$ is not a hard-core predicate for $f_{p,g}$.

     15.17 人们相信，如上一题中的 $\mathcal{G}$ 对应的离散对数问题是困难的。这意味着函数（族）$f_{p,g}$（其中 $f_{p,g}(x) \overset{\mathrm{def}}{=} [g^x \bmod p]$）是单向函数。记 $\mathsf{lsb}(x)$ 为 x 的最低有效位。证明：$\mathsf{lsb}$ 不是 $f_{p,g}$ 的难核谓词。

15.18 Consider the plain Rabin encryption scheme in which a message $m \in \mathcal{QR}_N$ is encrypted relative to a public key $N$ (where $N$ is a Blum integer) by computing the ciphertext $c := [m^2 \mod N]$. Show a chosen-ciphertext attack on this scheme that recovers the entire private key.

     15.18 考虑朴素 Rabin 加密方案：以公钥 $N$（$N$ 为 Blum 整数）加密消息 $m \in \mathcal{QR}_N$ 时，计算密文 $c := [m^2 \mod N]$。给出针对该方案的一种选择密文攻击，使其能恢复整个私钥。

15.19 The plain Rabin signature scheme is like the plain RSA signature scheme, except using the Rabin trapdoor permutation. Show an attack on plain Rabin signatures by which the attacker learns the signer's private key.

     15.19 朴素 Rabin 签名方案与朴素 RSA 签名方案类似，只是改用 Rabin 陷门置换。给出一种针对朴素 Rabin 签名的攻击，使攻击者能获知签名者的私钥。

15.20 Let $N$ be a Blum integer.

     15.20 设 $N$ 为 Blum 整数。

(a) Define the set $S \overset{\mathrm{def}}{=} \{x \in \mathbb{Z}_N^* \mid x < N/2 \text{ and } \mathcal{J}_N(x) = +1\}$. Define the function $f_N : S \to \mathbb{Z}_N^*$ by:

$$f_{N}(x)=\left\{\begin{array}{l l}{\left[x^{2}\bmod N\right]}&{\mathrm{~if~}\left[x^{2}\bmod N\right]<N/2}\\ {\left[-x^{2}\bmod N\right]}&{\mathrm{~if~}\left[x^{2}\bmod N\right]>N/2}\end{array}\right.$$

Show that $f_{N}$ is a permutation over S.

     (a) 定义集合 $S \overset{\mathrm{def}}{=} \{x \in \mathbb{Z}_N^* \mid x < N/2 \text{ 且 } \mathcal{J}_N(x) = +1\}$，并如下定义函数 $f_N : S \to \mathbb{Z}_N^*$：

     证明：$f_{N}$ 是 S 上的置换。

(b) Define a family of trapdoor permutations based on factoring using $f_{N}$ as defined above.

     (b) 利用上面定义的 $f_{N}$，构造一个基于因子分解的陷门置换族。

15.21 Let $N$ be a Blum integer. Define the function $\mathsf{half}_N : \mathbb{Z}_N^* \to \{0,1\}$ as

     15.21 设 $N$ 为 Blum 整数。如下定义函数 $\mathsf{half}_N : \mathbb{Z}_N^* \to \{0,1\}$：

$$\mathsf{half}_{N}(x)=\left\{\begin{array}{l l}{-1}&{\mathrm{~if~}x<N/2}\\ {+1}&{\mathrm{~if~}x>N/2}\end{array}\right.$$

Show that the function $f: \mathbb{Z}_N^* \to \mathcal{QR}_N \times \{-1, +1\}^2$ defined as

     证明：如下定义的函数 $f: \mathbb{Z}_N^* \to \mathcal{QR}_N \times \{-1, +1\}^2$

$$f(x)=\left([x^{2}\bmod N],\mathcal{J}_{N}(x),\mathsf{half}_{N}(x)\right)$$

is one-to-one.

     是单射。
