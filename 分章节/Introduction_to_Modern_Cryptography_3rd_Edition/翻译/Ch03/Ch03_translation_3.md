## 3.5 Constructing a CPA-Secure Encryption Scheme　3.5 构造 CPA 安全加密方案

Before constructing encryption schemes secure against chosen-plaintext attacks, we first introduce the important notion of pseudorandom functions.

在构造能够抵抗选择明文攻击的加密方案之前，我们首先引入伪随机函数这一重要概念。

### 3.5.1 Pseudorandom Functions and Permutations　3.5.1 伪随机函数与伪随机置换

Pseudorandom functions (PRFs) generalize the notion of pseudorandom generators. Now, instead of considering "random-looking" strings we consider "random-looking" functions. As in our earlier discussion of pseudo-randomness, it does not make much sense to say that any fixed function $f: \{0,1\}^* \to \{0,1\}^*$ is pseudorandom (in the same way it makes little sense to say that any fixed function is random). Instead, we must consider the pseudorandomness of a distribution on functions. Such a distribution is induced naturally by considering keyed functions, defined next.

伪随机函数（PRF）推广了伪随机生成器的概念。现在，我们不再考虑“看似随机”的字符串，而是考虑“看似随机”的函数。正如我们之前关于伪随机性的讨论，说某个固定函数 $f: \{0,1\}^* \to \{0,1\}^*$ 是伪随机的意义不大（正如说某个固定函数是随机的一样没有意义）。相反，我们必须考虑函数分布的伪随机性。这种分布自然地由带密钥的函数（keyed function）所导出，下面就来定义它。

A keyed function $F: \{0,1\}^* \times \{0,1\}^* \to \{0,1\}^*$ is a two-input function, where the first input is called the key and typically denoted by $k$. We say $F$ is efficient if there is a polynomial-time algorithm that computes $F(k,x)$ given $k$ and $x$. (We will only be interested in efficient keyed functions.) The security parameter $n$ dictates the key length, input length, and output length. That is, we associate with $F$ three functions $\ell_{key}, \ell_{in}$, and $\ell_{out}$; for any key $k \in \{0,1\}^{\ell_{key}(n)}$, the function $F_k$ is only defined for inputs $x \in \{0,1\}^{\ell_{in}(n)}$, in which case $F_k(x) \in \{0,1\}^{\ell_{out}(n)}$. Unless stated otherwise, we assume for simplicity that $F$ is length preserving, meaning $\ell_{key}(n) = \ell_{in}(n) = \ell_{out}(n) = n$. (Note, however, that this is only to reduce notational clutter, and it is not uncommon to have pseudorandom functions that are not length preserving.) Let $\mathsf{Func}_n$ denote the set of all functions mapping $n$-bit strings to $n$-bit strings.

一个带密钥的函数 $F: \{0,1\}^* \times \{0,1\}^* \to \{0,1\}^*$ 是一个双输入函数，其中第一个输入称为密钥，通常记为 $k$。如果存在一个多项式时间算法在给定 $k$ 和 $x$ 时能计算 $F(k,x)$，我们就说 $F$ 是高效的。（我们只关心高效的带密钥函数。）安全参数 $n$ 决定了密钥长度、输入长度和输出长度。也就是说，我们为 $F$ 关联三个函数 $\ell_{key}$、$\ell_{in}$ 和 $\ell_{out}$；对于任意密钥 $k \in \{0,1\}^{\ell_{key}(n)}$，函数 $F_k$ 只对输入 $x \in \{0,1\}^{\ell_{in}(n)}$ 有定义，此时 $F_k(x) \in \{0,1\}^{\ell_{out}(n)}$。除非另有说明，为简单起见，我们假定 $F$ 是长度保持的（length preserving），即 $\ell_{key}(n) = \ell_{in}(n) = \ell_{out}(n) = n$。（但请注意，这只是为了减少符号上的杂乱，存在非长度保持的伪随机函数也并不罕见。）令 $\mathsf{Func}_n$ 表示所有将 $n$ 比特串映射到 $n$ 比特串的函数的集合。

In typical usage a key $k \in \{0,1\}^n$ is chosen and fixed, and we are then interested in the single-input function $F_k : \{0,1\}^n \to \{0,1\}^n$ defined by $F_k(x) \stackrel{\mathrm{def}}{=} F(k,x)$ mapping $n$-bit input strings to $n$-bit output strings. A keyed function $F$ thus induces a distribution on functions in $\mathsf{Func}_n$, where the distribution is given by choosing a uniform key $k \in \{0,1\}^n$ and then considering the resulting single-input function $F_k$. We call $F$ pseudorandom if the function $F_k$ (for a uniform key $k$) is indistinguishable from a function chosen uniformly at random from the set $\mathsf{Func}_n$ of all functions having the same domain and range; that is, if no efficient adversary can distinguish—in a sense we more carefully define below—whether it is interacting with $F_k$ (for uniform $k$) or $f$ (where $f$ is chosen uniformly from $\mathsf{Func}_n$).

在典型用法中，选择一个密钥 $k \in \{0,1\}^n$ 并固定下来，然后我们关心的是由 $F_k(x) \stackrel{\mathrm{def}}{=} F(k,x)$ 定义的单输入函数 $F_k : \{0,1\}^n \to \{0,1\}^n$，它将 $n$ 比特输入串映射到 $n$ 比特输出串。因此，一个带密钥的函数 $F$ 在 $\mathsf{Func}_n$ 上诱导了一个分布，该分布通过选择均匀密钥 $k \in \{0,1\}^n$ 然后考虑所得的单输入函数 $F_k$ 得到。如果函数 $F_k$（对于均匀密钥 $k$）与从集合 $\mathsf{Func}_n$（所有具有相同定义域和值域的函数）中均匀随机选取的函数不可区分，我们就称 $F$ 是伪随机的；也就是说，没有高效敌手能够区分（按照我们下面将更仔细定义的意义）它是在与 $F_k$（对于均匀 $k$）交互还是在与 $f$（其中 $f$ 从 $\mathsf{Func}_n$ 中均匀选取）交互。

Since choosing a uniform function is less intuitive than choosing a uniform string, it is worth spending a bit more time on this idea. The set $\mathsf{Func}_n$ is finite, and selecting a uniform function mapping $n$-bit strings to $n$-bit strings simply means choosing a function uniformly from this set. How large is $\mathsf{Func}_n$? A function $f$ is specified by giving its value on each point in its domain. We can view any function (over a finite domain) as a large look-up table that stores $f(x)$ in the row of the table labeled by $x$. For $f \in \mathsf{Func}_n$, the look-up table for $f$ has ${2}^n$ rows (one for each string in the domain $\{0,1\}^n$), with each row containing an $n$-bit string (since the range of $f$ is $\{0,1\}^n$). Concatenating all the entries of this table, we see that any function in $\mathsf{Func}_n$ can be represented by a string of length ${2}^n \cdot n$. Moreover, this correspondence is one-to-one, as each string of length ${2}^n \cdot n$ (i.e., each table containing ${2}^n$ entries of length $n$) defines a unique function in $\mathsf{Func}_n$.

由于选择均匀函数不如选择均匀字符串那么直观，因此值得花更多时间来讨论这一想法。集合 $\mathsf{Func}_n$ 是有限的，选择一个将 $n$ 比特串映射到 $n$ 比特串的均匀函数，就是简单地从该集合中均匀地选取一个函数。$\mathsf{Func}_n$ 有多大？一个函数 $f$ 由其定义域中每个点上的值来指定。我们可以将任何（有限定义域上的）函数视为一个大型查找表，在由 $x$ 标记的表行中存储 $f(x)$。对于 $f \in \mathsf{Func}_n$，$f$ 的查找表有 ${2}^n$ 行（定义域 $\{0,1\}^n$ 中每个串对应一行），每行包含一个 $n$ 比特串（因为 $f$ 的值域是 $\{0,1\}^n$）。将该表的所有条目连接起来，我们看到 $\mathsf{Func}_n$ 中的任何函数都可以用长度为 ${2}^n \cdot n$ 的串表示。此外，这种对应是一一对应的，因为每个长度为 ${2}^n \cdot n$ 的串（即包含 ${2}^n$ 个长度为 $n$ 的条目的表）都定义了 $\mathsf{Func}_n$ 中的一个唯一函数。

Thus, the size of $\mathsf{Func}_n$ is exactly the number of strings of length $n \cdot 2^n$, i.e., $|\mathsf{Func}_n| = 2^{n \cdot 2^n}$.

因此，$\mathsf{Func}_n$ 的大小正好等于长度为 $n \cdot 2^n$ 的串的数量，即 $|\mathsf{Func}_n| = 2^{n \cdot 2^n}$。

Viewing a function as a look-up table provides another useful way to think about selecting a uniform function $f \in \mathsf{Func}_n$: It is exactly equivalent to choosing each row in the look-up table of $f$ uniformly. This means, in particular, that the values $f(x)$ and $f(y)$, for any two inputs $x \neq y$, are uniform and independent. We can view this look-up table as being populated by uniform entries in advance, before $f$ is evaluated on any input, or we can view entries of the table as being chosen uniformly "on-the-fly," as needed, whenever $f$ is evaluated on a new input on which it was never evaluated before.

将函数视为查找表提供了另一种有用的方式来思考如何选择均匀函数 $f \in \mathsf{Func}_n$：它完全等价于均匀地选择 $f$ 查找表中的每一行。这特别意味着，对于任意两个不同的输入 $x \neq y$，值 $f(x)$ 和 $f(y)$ 是均匀且独立的。我们可以将这张查找表视为在 $f$ 对任何输入求值之前就已预先填好均匀条目的表，也可以将表中的条目视为按需“即时”均匀选取的——即每当 $f$ 在一个之前从未求值过的新输入上被求值时才选取。

A pseudorandom function is a keyed function $F$ such that $F_k$ (for uniform $k \in \{0,1\}^n$) is indistinguishable from $f$ (for uniform $f \in \mathsf{Func}_n$). The former is chosen from a distribution over (at most) ${2}^n$ distinct functions, whereas the latter is chosen from all ${2}^{n\cdot2^n}$ functions in $\mathsf{Func}_n$. Despite this, the "behavior" of those functions must look the same to any polynomial-time distinguisher.

伪随机函数是这样一种带密钥的函数 $F$，使得 $F_k$（对于均匀的 $k \in \{0,1\}^n$）与 $f$（对于均匀的 $f \in \mathsf{Func}_n$）不可区分。前者是从（至多）${2}^n$ 个不同函数的分布中选取的，而后者是从 $\mathsf{Func}_n$ 中全部 ${2}^{n\cdot2^n}$ 个函数中选取的。尽管如此，这些函数的“行为”在任何多项式时间区分器看来必须是一样的。

A first attempt at formalizing the notion of a pseudorandom function would be to proceed as in Definition 3.14. That is, we could require that every polynomial-time distinguisher $D$ that receives a description of $F_k$ outputs 1 with "almost" the same probability as when it receives a description of a random function $f$. However, this definition is inappropriate since the description of a random function has exponential length (given by its look-up table of length $n \cdot 2^n$), while $D$ is limited to running in polynomial time. So, $D$ would not even have sufficient time to examine its entire input.

形式化伪随机函数概念的一种初步尝试是按照定义 3.14 的方式进行。也就是说，我们可以要求每个收到 $F_k$ 描述的多项式时间区分器 $D$ 输出 1 的概率与它收到随机函数 $f$ 描述时输出 1 的概率“几乎”相同。然而，这个定义是不合适的，因为随机函数的描述具有指数长度（由其长度为 $n \cdot 2^n$ 的查找表给出），而 $D$ 限于在多项式时间内运行。因此，$D$ 甚至没有足够的时间来检查其整个输入。

Instead, we allow $D$ to probe the input/output behavior of the function by giving $D$ access to an oracle $\mathcal{O}$ which is either equal to $F_k$ or $f$. The distinguisher $D$ may query its oracle at any point $x$, in response to which the oracle returns $\mathcal{O}(x)$. We treat the oracle as a black box in the same way as when we provided the adversary with oracle access to the encryption algorithm in the definition of a chosen-plaintext attack. Here, however, the oracle computes a deterministic function and so returns the same result if queried twice on the same input. $D$ may interact freely with its oracle, choosing its queries adaptively based on all previous outputs. Since $D$ runs in polynomial time, however, it can ask only polynomially many queries.

相反，我们允许 $D$ 访问一个预言机 $\mathcal{O}$（它要么等于 $F_k$，要么等于 $f$），以此来探测函数的输入/输出行为。区分器 $D$ 可以在任何点 $x$ 上查询其预言机，预言机返回 $\mathcal{O}(x)$ 作为响应。我们像在选择明文攻击定义中给予敌手对加密算法的预言机访问一样，将预言机视为黑盒。但在这里，预言机计算的是一个确定性函数，因此在同一输入上查询两次会返回相同的结果。$D$ 可以自由地与其预言机交互，根据所有先前的输出自适应地选择其查询。然而，由于 $D$ 在多项式时间内运行，它只能进行多项式次数的查询。

We now present the formal definition. (The definition assumes F is length preserving for simplicity.)

我们现在给出形式化定义。（为简单起见，该定义假定 F 是长度保持的。）

DEFINITION 3.24 An efficient, length preserving, keyed function $F : \{0,1\}^* \times \{0,1\}^* \to \{0,1\}^*$ is a pseudorandom function if for all probabilistic polynomial-time distinguishers $D$, there is a negligible function $\mathsf{negl}$ such that:

定义 3.24 一个高效的、长度保持的带密钥函数 $F : \{0,1\}^* \times \{0,1\}^* \to \{0,1\}^*$ 是一个**伪随机函数**（pseudorandom function），如果对于所有概率多项式时间区分器 $D$，存在一个可忽略函数 $\mathsf{negl}$，使得：

$$\left|\Pr[D^{F_{k}(\cdot)}(1^{n})=1]-\Pr[D^{f(\cdot)}(1^{n})=1]\right|\leq\mathsf{negl}(n),$$

where the first probability is taken over uniform choice of $k \in \{0,1\}^n$ and the randomness of $D$, and the second probability is taken over uniform choice of $f \in \mathsf{Func}_n$ and the randomness of $D$.

其中第一个概率取自均匀选择 $k \in \{0,1\}^n$ 和 $D$ 的随机性，第二个概率取自均匀选择 $f \in \mathsf{Func}_n$ 和 $D$ 的随机性。

We stress that $D$ is not given the key $k$ (in the same way that $D$ is not given the seed when defining a pseudorandom generator). It is meaningless to require that $F_k$ "look random" if $k$ is known, since given $k$ it is trivial to distinguish an oracle for $F_k$ from an oracle for $f$. (All the distinguisher has to do is query the oracle at any point $x$ to obtain the answer $y$, and compare this to the result $y^{\prime} := F_k(x)$ that it computes itself using the known value $k$. An oracle for $F_k$ will return $y = y^{\prime}$, while an oracle for a random function will return $y = y^{\prime}$ only with probability ${2}^{-n}$.) This means that if $k$ is revealed, any claims about pseudorandomness no longer hold.

我们强调，$D$ 并不知道密钥 $k$（就像在定义伪随机生成器时 $D$ 不知道种子一样）。如果 $k$ 已知，要求 $F_k$“看起来随机”是没有意义的，因为在已知 $k$ 的情况下，区分 $F_k$ 的预言机和 $f$ 的预言机是微不足道的。（区分器只需在某个点 $x$ 上查询预言机得到答案 $y$，然后将此结果与它自己使用已知的 $k$ 计算出的 $y^{\prime} := F_k(x)$ 进行比较。$F_k$ 的预言机会返回 $y = y^{\prime}$，而随机函数的预言机仅以 ${2}^{-n}$ 的概率返回 $y = y^{\prime}$。）这意味着如果 $k$ 被泄露，任何关于伪随机性的声明都不再成立。

**Example 3.25**　**示例 3.25**

We can gain familiarity with the definition by considering an insecure example. Define the keyed, length preserving function $F$ by $F(k,x) = k \oplus x$. For any input $x$, the value of $F_k(x)$ is uniformly distributed (when $k$ is uniform). Nevertheless, $F$ is not pseudorandom since its values on any two points are correlated. Consider the distinguisher $D$ that queries its oracle $\mathcal{O}$ on distinct points $x_1, x_2$ to obtain values $y_1 = \mathcal{O}(x_1)$ and $y_2 = \mathcal{O}(x_2)$, and outputs 1 if and only if $y_1 \oplus y_2 = x_1 \oplus x_2$. If $\mathcal{O} = F_k$, for any $k$, then $D$ outputs 1. On the other hand, if $\mathcal{O} = f$ for $f$ chosen uniformly from $\mathsf{Func}_n$, then

我们可以通过考虑一个不安全的例子来熟悉这个定义。定义带密钥的、长度保持的函数 $F$ 为 $F(k,x) = k \oplus x$。对于任何输入 $x$，$F_k(x)$ 的值是均匀分布的（当 $k$ 均匀时）。然而，$F$ 不是伪随机的，因为它在任意两个点上的值是相关的。考虑区分器 $D$，它在不同的点 $x_1, x_2$ 上查询其预言机 $\mathcal{O}$，得到值 $y_1 = \mathcal{O}(x_1)$ 和 $y_2 = \mathcal{O}(x_2)$，当且仅当 $y_1 \oplus y_2 = x_1 \oplus x_2$ 时输出 1。如果 $\mathcal{O} = F_k$（对于任何 $k$），那么 $D$ 输出 1。另一方面，如果 $\mathcal{O} = f$，其中 $f$ 从 $\mathsf{Func}_n$ 中均匀选取，那么

$$\Pr[f(x_{1})\oplus f(x_{2})=x_{1}\oplus x_{2}]=\Pr[f(x_{2})=x_{1}\oplus x_{2}\oplus f(x_{1})]=2^{-n},$$

since $f(x_2)$ is uniform and independent of $x_1, x_2$, and $f(x_1)$. We thus have $\Pr[D^{F_k(\cdot)}(1^n) = 1] = 1$ and $\Pr[D^{f(\cdot)}(1^n) = 1] = 2^{-n}$, and the difference between these two is not negligible.

由于 $f(x_2)$ 是均匀的且与 $x_1, x_2$ 和 $f(x_1)$ 独立，因此我们有 $\Pr[D^{F_k(\cdot)}(1^n) = 1] = 1$ 和 $\Pr[D^{f(\cdot)}(1^n) = 1] = 2^{-n}$，两者之间的差不是可忽略的。

Pseudorandom functions and pseudorandom generators. As one might expect, there is a close relationship between pseudorandom functions and pseudorandom generators. It is fairly easy to construct a pseudorandom generator $G$ from a pseudorandom function $F$ by simply evaluating $F$ on a series of distinct inputs; e.g., we can define $G(s) \overset{\mathrm{def}}{=} F_s(1)\|F_s(2)\|\cdots\|F_s(\ell)$ for any desired $\ell$ (where $\|\cdot\|$ denotes concatenation). If $F_s$ were replaced by a uniform function $f$, the output of $G$ would be uniform; when using $F$, the output is pseudorandom. You are asked to prove this formally in Exercise 3.16.

伪随机函数与伪随机生成器。正如人们所料，伪随机函数和伪随机生成器之间存在密切关系。只需在一系列不同的输入上对 $F$ 求值，就可以很容易地从伪随机函数 $F$ 构造出伪随机生成器 $G$；例如，对于任意期望的 $\ell$，我们可以定义 $G(s) \overset{\mathrm{def}}{=} F_s(1)\|F_s(2)\|\cdots\|F_s(\ell)$（其中 $\|\cdot\|$ 表示连接）。如果将 $F_s$ 替换为均匀函数 $f$，那么 $G$ 的输出将是均匀的；当使用 $F$ 时，输出是伪随机的。习题 3.16 要求你形式化地证明这一点。

Considering the other direction, a pseudorandom generator $G$ immediately gives a pseudorandom function $F$ with small input length. Specifically, say $G$ has expansion factor $\ell(n) = n \cdot 2^{t(n)}$. We can define the keyed function $F: \{0,1\}^n \times \{0,1\}^{t(n)} \to \{0,1\}^n$ as follows: to compute $F_k(i)$, first compute $G(k)$ and interpret the result as a look-up table with ${2}^{t(n)}$ rows each containing $n$ bits; output the $i$th row. (We leave the proof that $F$ is pseudorandom to the reader.) Note, however, that $F$ is efficient only if $t(n) = \mathcal{O}(\log n)$. It is possible, though more difficult, to construct pseudorandom functions with large input length from pseudorandom generators; see Section 8.5. Since pseudorandom generators can be constructed based on certain mathematical problems conjectured to be hard, we conclude that pseudorandom functions (for long inputs) can be constructed based on those same problems. The fact that pseudorandom functions can be based on hard mathematical problems represents one of the amazing contributions of modern cryptography.

反过来考虑，一个伪随机生成器 $G$ 立即给出一个具有小输入长度的伪随机函数 $F$。具体来说，设 $G$ 的扩展因子为 $\ell(n) = n \cdot 2^{t(n)}$。我们可以如下定义带密钥的函数 $F: \{0,1\}^n \times \{0,1\}^{t(n)} \to \{0,1\}^n$：要计算 $F_k(i)$，首先计算 $G(k)$ 并将结果解释为一个具有 ${2}^{t(n)}$ 行、每行包含 $n$ 比特的查找表；输出第 $i$ 行。（我们将 $F$ 是伪随机的证明留给读者。）但请注意，$F$ 只有在 $t(n) = \mathcal{O}(\log n)$ 时才是高效的。从伪随机生成器构造具有大输入长度的伪随机函数是可能的，尽管更为困难；见 8.5 节。由于伪随机生成器可以基于某些被猜测为困难的数学问题来构造，我们得出结论：伪随机函数（对于长输入）也可以基于同样的问题来构造。伪随机函数可以基于困难的数学问题来构造，这一事实是现代密码学令人惊叹的贡献之一。

#### Pseudorandom Permutations　伪随机置换

Let $\mathsf{Perm}_n \subset \mathsf{Func}_n$ be the set of all permutations (i.e., bijections) on $\{0,1\}^n$. Viewing any $f \in \mathsf{Perm}_n$ as a look-up table as before, we now have the added constraint that the entries in any two distinct rows must be different. We have ${2}^n$ different choices for the entry in the first row of the table; once we fix that entry, we are left with only ${2}^n - 1$ choices for the second row, and so on. We thus see that the size of $\mathsf{Perm}_n$ is $(2^n)!$.

令 $\mathsf{Perm}_n \subset \mathsf{Func}_n$ 为 $\{0,1\}^n$ 上所有置换（即双射）的集合。像之前一样将任意 $f \in \mathsf{Perm}_n$ 视为查找表，我们现在有了额外的约束：任意两个不同行中的条目必须不同。对于表的第一行的条目，我们有 ${2}^n$ 种不同的选择；一旦固定了该条目，第二行只有 ${2}^n - 1$ 种选择，以此类推。因此我们看到 $\mathsf{Perm}_n$ 的大小为 $(2^n)!$。

Let $F$ be a keyed function where, for the moment, $\ell_{key}$, $\ell_{in}$, and $\ell_{out}$ can be arbitrary. We call $F$ a keyed permutation if $\ell_{in} = \ell_{out}$, and furthermore for all $k \in \{0,1\}^{\ell_{key}(n)}$ the function $F_k : \{0,1\}^{\ell_{in}(n)} \to \{0,1\}^{\ell_{in}(n)}$ is one-to-one (i.e., $F_k$ is a permutation). We call $\ell_{in}$ the block length of $F$ in this case. A keyed permutation is efficient if there is a polynomial-time algorithm for computing $F_k(x)$ given $k$ and $x$, as well as a polynomial-time algorithm for computing $F_k^{-1}(y)$ given $k$ and $y$. That is, $F_k$ should be both efficiently computable and efficiently invertible given $k$. As before, unless stated otherwise we assume $F$ is length preserving for simplicity and so $\ell_{key}(n) = \ell_{in}(n) = n$.

令 $F$ 为一个带密钥的函数，暂时令 $\ell_{key}$、$\ell_{in}$ 和 $\ell_{out}$ 可以是任意的。如果 $\ell_{in} = \ell_{out}$，并且对于所有 $k \in \{0,1\}^{\ell_{key}(n)}$，函数 $F_k : \{0,1\}^{\ell_{in}(n)} \to \{0,1\}^{\ell_{in}(n)}$ 是一一对应的（即 $F_k$ 是一个置换），我们就称 $F$ 为一个带密钥的置换（keyed permutation）。此时我们称 $\ell_{in}$ 为 $F$ 的分组长度（block length）。一个带密钥的置换是高效的，如果存在多项式时间算法在给定 $k$ 和 $x$ 时计算 $F_k(x)$，以及存在多项式时间算法在给定 $k$ 和 $y$ 时计算 $F_k^{-1}(y)$。也就是说，$F_k$ 在给定 $k$ 时既应能高效计算，也应能高效求逆。与之前一样，除非另有说明，为简单起见我们假定 $F$ 是长度保持的，因此 $\ell_{key}(n) = \ell_{in}(n) = n$。

The definition of what it means for an efficient, keyed permutation $F$ to be a pseudorandom permutation is exactly analogous to Definition 3.24, with the only difference being that now we require $F_k$ to be indistinguishable from a uniform permutation rather than a uniform function. That is, we require that no efficient algorithm can distinguish between access to $F_k$ (for uniform key $k$) and access to $f$ (for uniform $f \in \mathsf{Perm}_n$). We remark that whenever the block length is sufficiently long (as is usually the case in practice), a random permutation is indistinguishable from a random function with the same domain and range; thus, we can equally well define a pseudorandom permutation by requiring that no efficient algorithm can distinguish between access to $F_k$ (for uniform key $k$) and access to $f$ (for uniform $f \in \mathsf{Func}_n$). This is a consequence of the following proposition, proven formally in Appendix A.4.

高效的带密钥置换 $F$ 成为伪随机置换的条件与定义 3.24 完全类似，唯一的区别在于现在我们要求 $F_k$ 与均匀置换（而不是均匀函数）不可区分。也就是说，我们要求没有高效算法能够区分对 $F_k$（对于均匀密钥 $k$）的访问和对 $f$（对于均匀 $f \in \mathsf{Perm}_n$）的访问。我们指出，只要分组长度足够长（正如实践中通常的情况），随机置换与具有相同定义域和值域的随机函数是不可区分的；因此，我们同样可以通过要求没有高效算法能够区分对 $F_k$（对于均匀密钥 $k$）的访问和对 $f$（对于均匀 $f \in \mathsf{Func}_n$）的访问来定义伪随机置换。这是以下命题的推论，其形式化证明见附录 A.4。

PROPOSITION 3.26 If $F$ is a pseudorandom permutation for which $\ell_{in}(n) \geq n$, then $F$ is also a pseudorandom function.

命题 3.26 如果 $F$ 是一个满足 $\ell_{in}(n) \geq n$ 的伪随机置换，那么 $F$ 也是一个伪随机函数。

While the above is true asymptotically, concrete security may be impacted when a pseudorandom permutation is viewed as a pseudorandom function.

虽然上述结论在渐近意义上是成立的，但当将伪随机置换视为伪随机函数时，具体安全性可能会受到影响。

Strong pseudorandom permutations. If $F$ is a keyed permutation then cryptographic schemes based on $F$ might require the honest parties to compute the inverse $F_k^{-1}$ in addition to computing $F_k$ itself. This potentially introduces new security concerns. In particular, it may now be necessary to impose the stronger requirement that $F_k$ be indistinguishable from a uniform permutation even if the distinguisher is additionally given oracle access to the inverse of the permutation. If F has this property, we call it a strong pseudorandom permutation.

强伪随机置换。如果 $F$ 是一个带密钥的置换，那么基于 $F$ 的密码方案可能要求诚实方除了计算 $F_k$ 本身之外还要计算其逆 $F_k^{-1}$。这潜在地引入了新的安全问题。特别地，现在可能需要施加更强的要求：即使区分器额外获得了对置换逆的预言机访问，$F_k$ 也必须与均匀置换不可区分。如果 $F$ 具有这一性质，我们称之为**强伪随机置换**（strong pseudorandom permutation）。

DEFINITION 3.27 Let $F : \{0,1\}^* \times \{0,1\}^* \to \{0,1\}^*$ be an efficient, length preserving, keyed permutation. F is a strong pseudorandom permutation if for all probabilistic polynomial-time distinguishers D, there exists a negligible function $\mathsf{negl}$ such that:

定义 3.27 令 $F : \{0,1\}^* \times \{0,1\}^* \to \{0,1\}^*$ 为一个高效的、长度保持的带密钥置换。如果对于所有概率多项式时间区分器 D，存在一个可忽略函数 $\mathsf{negl}$ 使得下式成立，则称 $F$ 是一个**强伪随机置换**：

$$\begin{array}{r}\left|\Pr[D^{F_{k}(\cdot),F_{k}^{-1}(\cdot)}(1^{n})=1]-\Pr[D^{f(\cdot),f^{-1}(\cdot)}(1^{n})=1]\right|\leq\mathsf{negl}(n),\end{array}$$

where the first probability is taken over uniform choice of $k \in \{0,1\}^n$ and the randomness of $D$, and the second probability is taken over uniform choice of $f \in \mathsf{Perm}_n$ and the randomness of $D$.

其中第一个概率取自均匀选择 $k \in \{0,1\}^n$ 和 $D$ 的随机性，第二个概率取自均匀选择 $f \in \mathsf{Perm}_n$ 和 $D$ 的随机性。

Of course, any strong pseudorandom permutation is also a pseudorandom permutation. However, the converse is not true.

当然，任何强伪随机置换也是伪随机置换。但反之则不成立。

### 3.5.2 CPA-Security from a Pseudorandom Function　3.5.2 基于伪随机函数的 CPA 安全

We focus here on constructing a CPA-secure fixed-length encryption scheme. By what we have said at the end of Section 3.4.3, this implies the existence of a CPA-secure encryption scheme for arbitrary-length messages. In Section 3.6 we will discuss more efficient ways of encrypting messages of arbitrary length.

我们这里专注于构造一个 CPA 安全的定长加密方案。根据我们在 3.4.3 节末尾所述，这意味着存在一个适用于任意长度消息的 CPA 安全加密方案。在 3.6 节中，我们将讨论更高效的任意长度消息加密方式。

A naive attempt at constructing an encryption scheme from a pseudorandom permutation is to define $\mathsf{Enc}_k(m) = F_k(m)$. Although we expect that this "reveals no information about $m$" (since, if $f$ is a uniform permutation, then $f(m)$ is a uniform $n$-bit string for any $m$), this method of encryption is deterministic and so cannot possibly be CPA-secure since encrypting the same plaintext twice will yield the same ciphertext.

一个朴素的尝试是从伪随机置换构造加密方案：定义 $\mathsf{Enc}_k(m) = F_k(m)$。尽管我们期望这“不泄露关于 $m$ 的信息”（因为如果 $f$ 是均匀置换，那么对任意 $m$，$f(m)$ 是一个均匀的 $n$ 比特串），但这种加密方法是确定性的，因此不可能 CPA 安全，因为两次加密同一明文会产生相同密文。

Our CPA-secure construction uses randomized encryption. Specifically, we encrypt by applying a pseudorandom function to a random value $r \in \{0,1\}^n$ and XORing the output with the plaintext; the ciphertext includes both the result as well as $r$ (to enable the receiver to decrypt). See Figure 3.3 and Construction 3.28. Encryption can again be viewed as XORing a pseudorandom pad with the plaintext (just like in the "pseudo-" one-time pad), with the major difference being the fact that here a fresh pseudorandom pad—that depends on $r$—is used each time a message is encrypted. (The pseudorandom pad is only "fresh" if the pseudorandom function is applied to a "fresh" value $r$ on which it has never been evaluated before. The proof below shows that with overwhelming probability this is always the case.)

我们的 CPA 安全构造使用随机化加密。具体来说，我们通过将伪随机函数应用于一个随机值 $r \in \{0,1\}^n$，并将输出与明文进行异或来加密；密文既包含结果也包含 $r$（以使接收方能够解密）。见图 3.3 和构造 3.28。加密同样可以被视为将伪随机填充与明文进行异或（就像“伪”一次一密一样），主要区别在于这里每次加密消息时都使用了一个依赖于 $r$ 的新鲜伪随机填充。（只有在伪随机函数被应用于一个之前从未求值过的“新鲜”值 $r$ 时，伪随机填充才是“新鲜”的。下面的证明表明，这种情况以压倒性概率发生。）

Note that for any key $k$, every message $m$ has ${2}^n$ corresponding ciphertexts. Nevertheless, the receiver is able to decrypt correctly. (Check for yourself that decryption always returns the correct result!) This scheme also has the property that the ciphertext is longer than the plaintext. This is the first encryption scheme we have seen that has either of these properties.

注意，对于任何密钥 $k$，每条消息 $m$ 都有 ${2}^n$ 个对应的密文。尽管如此，接收方能够正确解密。（请自行验证解密总是返回正确结果！）该方案还具有密文比明文长的性质。这是我们见到的第一个具有这两种性质中任何一种的加密方案。

![Image](https://lsky.jerryxue.top/i/2026/08/22/6a88f9de81baf.jpg)

**FIGURE 3.3: Encryption with a pseudorandom function.**

**图 3.3：使用伪随机函数的加密。**

Before turning to the proof that the above construction is CPA-secure, we highlight a common template that is used by most proofs of security (even outside the context of encryption) for constructions based on pseudorandom functions. The first step of such proofs is to consider a hypothetical version of the construction in which the pseudorandom function is replaced with a random function. It is then argued—using a proof by reduction—that this modification does not significantly affect the attacker's success probability. We are then left with analyzing a scheme that uses a completely random function. The rest of the proof typically relies on probabilistic analysis and does not rely on any computational assumptions. We will utilize this proof template several times in this and the next two chapters.

在着手证明上述构造是 CPA 安全的之前，我们先着重介绍一个常见的证明模板——大多数针对基于伪随机函数的构造的安全性证明（甚至在加密之外的场合）都采用它。此类证明的第一步是考虑构造的一个假设版本，其中伪随机函数被替换为随机函数。然后——通过归约证明——论证这一修改不会显著影响攻击者的成功概率。于是我们只需要分析一个使用完全随机函数的方案。证明的其余部分通常依赖于概率分析，而不依赖于任何计算假设。在本章及接下来的两章中，我们将多次使用这一证明模板。

> **CONSTRUCTION 3.28**　**构造 3.28**
>
> Let F be a pseudorandom function. Define a fixed-length, private-key encryption scheme for messages of length n as follows:
>
> Gen: on input ${1}^n$, choose uniform $k \in \{0,1\}^n$ and output it.
>
> - Enc: on input a key $k \in \{0,1\}^n$ and a message $m \in \{0,1\}^n$, choose uniform $r \in \{0,1\}^n$ and output the ciphertext
>
> $c:=\langle r,\mathcal{F}_{k}(r)\oplus m\rangle.$
>
> - Dec: on input a key $k \in \{0,1\}^n$ and a ciphertext $c = \langle r,s \rangle$, output the message
>
> $$m:=F_{k}(r)\oplus s.$$
>
> 令 $F$ 为一个伪随机函数。定义如下的定长私钥加密方案，用于长度为 $n$ 的消息：
>
> Gen：输入 ${1}^n$，选择均匀的 $k \in \{0,1\}^n$ 并输出。
>
> - Enc：输入密钥 $k \in \{0,1\}^n$ 和消息 $m \in \{0,1\}^n$，选择均匀的 $r \in \{0,1\}^n$ 并输出密文
>
> $c:=\langle r,\mathcal{F}_{k}(r)\oplus m\rangle.$
>
> - Dec：输入密钥 $k \in \{0,1\}^n$ 和密文 $c = \langle r,s \rangle$，输出消息
>
> $$m:=F_{k}(r)\oplus s.$$
>
> A CPA-secure encryption scheme from any pseudorandom function.
>
> 基于任意伪随机函数的 CPA 安全加密方案。

THEOREM 3.29 If F is a pseudorandom function, then Construction 3.28 is a CPA-secure, fixed-length private-key encryption scheme for messages of length n.

定理 3.29 如果 $F$ 是一个伪随机函数，那么构造 3.28 是一个 CPA 安全的定长私钥加密方案，用于长度为 $n$ 的消息。

PROOF Let $\widetilde{\Pi} = (\widetilde{\mathsf{Gen}}, \widetilde{\mathsf{Enc}}, \widetilde{\mathsf{Dec}})$ be an encryption scheme that is exactly the same as $\Pi = (\mathsf{Gen}, \mathsf{Enc}, \mathsf{Dec})$ from Construction 3.28, except that a truly random function $f$ is used in place of $F_k$. That is, $\widetilde{\mathsf{Gen}}(1^n)$ chooses a uniform function $f \in \mathsf{Func}_n$, and $\widetilde{\mathsf{Enc}}$ encrypts just like $\mathsf{Enc}$ except that $f$ is used instead of $F_k$. (This modified encryption scheme is not efficient. But we can still define it as a hypothetical encryption scheme for the sake of the proof.)

证明 令 $\widetilde{\Pi} = (\widetilde{\mathsf{Gen}}, \widetilde{\mathsf{Enc}}, \widetilde{\mathsf{Dec}})$ 为一个与构造 3.28 中的 $\Pi = (\mathsf{Gen}, \mathsf{Enc}, \mathsf{Dec})$ 完全相同的加密方案，唯一区别在于使用了一个真正的随机函数 $f$ 来代替 $F_k$。也就是说，$\widetilde{\mathsf{Gen}}(1^n)$ 选择一个均匀函数 $f \in \mathsf{Func}_n$，而 $\widetilde{\mathsf{Enc}}$ 的加密方式与 $\mathsf{Enc}$ 完全相同，只是用 $f$ 代替了 $F_k$。（这个修改后的加密方案不是高效的。但为了证明的目的，我们仍然可以将其定义为一个假设的加密方案。）

Fix an arbitrary PPT adversary $\mathcal{A}$, and let $q(n)$ be an upper bound on the number of queries that $\mathcal{A}(1^n)$ makes to its encryption oracle. (Note that $q$ must be upper-bounded by some polynomial.) As the first step of the proof, we show that there is a negligible function $\mathsf{negl}$ such that

固定一个任意的 PPT 敌手 $\mathcal{A}$，令 $q(n)$ 为 $\mathcal{A}(1^n)$ 对其加密预言机进行查询的次数上界。（注意 $q$ 必须被某个多项式所界定。）作为证明的第一步，我们证明存在一个可忽略函数 $\mathsf{negl}$ 使得

$$
\left|\Pr\left[\mathsf{PrivK}_{\mathcal{A},\Pi}^{\mathsf{cpa}}(n)=1\right]-\Pr\left[\mathsf{PrivK}_{\mathcal{A},\widetilde{\Pi}}^{\mathsf{cpa}}(n)=1\right]\right|\leq\mathsf{negl}(n).\tag{3.9}
$$

We prove this by reduction. We use $\mathcal{A}$ to construct a distinguisher $D$ for the pseudorandom function $F$. The distinguisher $D$ is given oracle access to a function $\mathcal{O}$, and its goal is to determine whether $\mathcal{O}$ is "pseudorandom" (i.e., equal to $F_k$ for uniform $k \in \{0,1\}^n$) or "random" (i.e., equal to $f$ for uniform $f \in \mathsf{Func}_n$). To do this, $D$ simulates experiment $\mathsf{PrivK}^{cpa}$ for $\mathcal{A}$ in the manner described below, and observes whether $\mathcal{A}$ succeeds or not. If $\mathcal{A}$ succeeds then $D$ guesses that its oracle must be a pseudorandom function, whereas if $\mathcal{A}$ does not succeed then $D$ guesses that its oracle must be a random function. In detail:

我们通过归约来证明这一点。我们使用 $\mathcal{A}$ 来构造一个针对伪随机函数 $F$ 的区分器 $D$。区分器 $D$ 被赋予对函数 $\mathcal{O}$ 的预言机访问，其目标是判断 $\mathcal{O}$ 是“伪随机的”（即等于 $F_k$，其中 $k$ 均匀取自 $\{0,1\}^n$）还是“随机的”（即等于 $f$，其中 $f$ 均匀取自 $\mathsf{Func}_n$）。为此，$D$ 以下述方式为 $\mathcal{A}$ 模拟实验 $\mathsf{PrivK}^{cpa}$，并观察 $\mathcal{A}$ 是否成功。如果 $\mathcal{A}$ 成功，则 $D$ 猜测其预言机一定是伪随机函数；而如果 $\mathcal{A}$ 不成功，则 $D$ 猜测其预言机一定是随机函数。具体如下：

> **Distinguisher D:**　**区分器 D：**
>
> D is given input ${1}^n$ and access to an oracle $\mathcal{O}:\{0,1\}^n\to\{0,1\}^n$.
> 1. Run $\mathcal{A}(1^n)$. Whenever $\mathcal{A}$ queries its encryption oracle on a message $m \in \{0,1\}^n$, answer this query in the following way:
> (a) Choose uniform $r \in \{0,1\}^{n}$.
> (b) Query $\mathcal{O}(r)$ and obtain response $y$.
> (c) Return the ciphertext $\langle r, y \oplus m \rangle$ to $\mathcal{A}$.
> 2. When $\mathcal{A}$ outputs messages $m_0, m_1 \in \{0,1\}^n$, choose a uniform bit $b \in \{0,1\}$ and then:
> (a) Choose uniform $r \in \{0,1\}^{n}$.
> (b) Query $\mathcal{O}(r)$ and obtain response $y$.
> (c) Return the challenge ciphertext $\langle r, y \oplus m_b \rangle$.
> 3. Continue answering encryption-oracle queries of A as before until A outputs a bit $b^{\prime}$. Output 1 if $b^{\prime} = b$, and 0 otherwise.
>
> D 被给予输入 ${1}^n$ 并具有对预言机 $\mathcal{O}:\{0,1\}^n\to\{0,1\}^n$ 的访问。
> 1. 运行 $\mathcal{A}(1^n)$。每当 $\mathcal{A}$ 在消息 $m \in \{0,1\}^n$ 上查询其加密预言机时，按以下方式回答该查询：
> (a) 选择均匀的 $r \in \{0,1\}^{n}$。
> (b) 查询 $\mathcal{O}(r)$ 并获得响应 $y$。
> (c) 将密文 $\langle r, y \oplus m \rangle$ 返回给 $\mathcal{A}$。
> 2. 当 $\mathcal{A}$ 输出消息 $m_0, m_1 \in \{0,1\}^n$ 时，选择一个均匀比特 $b \in \{0,1\}$，然后：
> (a) 选择均匀的 $r \in \{0,1\}^{n}$。
> (b) 查询 $\mathcal{O}(r)$ 并获得响应 $y$。
> (c) 返回挑战密文 $\langle r, y \oplus m_b \rangle$。
> 3. 继续像之前一样回答 A 的加密预言机查询，直到 A 输出一个比特 $b^{\prime}$。如果 $b^{\prime} = b$ 则输出 1，否则输出 0。
>
> D runs in polynomial time since A does. The key points are as follows:
>
> D 在多项式时间内运行，因为 A 也是如此。关键点如下：

1. If $D$'s oracle is a pseudorandom function, then the view of $\mathcal{A}$ when run as a subroutine by $D$ is distributed identically to the view of $\mathcal{A}$ in experiment $\mathsf{PrivK}_{\mathcal{A},\Pi}^{\mathsf{cpa}}(n)$. This is because, in this case, a uniform key $k$ is chosen and then every encryption is carried out by choosing a uniform $r$, computing $y := F_k(r)$, and setting the ciphertext equal to $\langle r, y \oplus m \rangle$, exactly as in Construction 3.28. Thus,

   如果 $D$ 的预言机是伪随机函数，那么 $\mathcal{A}$ 作为 $D$ 的子程序运行时所看到的视图与 $\mathcal{A}$ 在实验 $\mathsf{PrivK}_{\mathcal{A},\Pi}^{\mathsf{cpa}}(n)$ 中的视图分布完全相同。这是因为在这种情况下，选择了一个均匀密钥 $k$，然后每次加密都通过选择均匀的 $r$、计算 $y := F_k(r)$、并将密文设为 $\langle r, y \oplus m \rangle$ 来执行，与构造 3.28 完全一致。因此，

$$\begin{array}{r}{\Pr_{k\leftarrow\{0,1\}^{n}}\left[D^{F_{k}(\cdot)}(1^{n})=1\right]=\Pr\left[\mathsf{PrivK}_{\mathcal{A},\Pi}^{\mathsf{cpa}}(n)=1\right],} \tag{3.10}\end{array}$$

where we emphasize on the left-hand side that k is chosen uniformly.

其中我们在左侧强调 $k$ 是均匀选择的。

2. If $D$'s oracle is a random function, then the view of $\mathcal{A}$ when run as a subroutine by $D$ is distributed identically to the view of $\mathcal{A}$ in experiment $\mathsf{PrivK}_{\mathcal{A},\tilde{\Pi}}^{\mathsf{cpa}}(n)$. This can be seen exactly as above, with the only difference being that a uniform function $f \in \mathsf{Func}_n$ is used instead of $F_k$. Thus,

   如果 $D$ 的预言机是随机函数，那么 $\mathcal{A}$ 作为 $D$ 的子程序运行时所看到的视图与 $\mathcal{A}$ 在实验 $\mathsf{PrivK}_{\mathcal{A},\tilde{\Pi}}^{\mathsf{cpa}}(n)$ 中的视图分布完全相同。其理由与上述完全类似，唯一的区别在于使用了一个均匀函数 $f \in \mathsf{Func}_n$ 代替了 $F_k$。因此，

$$\begin{array}{r}{\Pr_{f\leftarrow\mathsf{Func}_{n}}\left[D^{f(\cdot)}(1^{n})=1\right]=\Pr\left[\mathsf{PrivK}_{\mathcal{A},\widetilde{\Pi}}^{\mathsf{cpa}}(n)=1\right],} \tag{3.11}\end{array}$$

where f is chosen uniformly from $\mathsf{Func}_{n}$ on the left-hand side.

其中左侧的 $f$ 是从 $\mathsf{Func}_n$ 中均匀选择的。

By the assumption that F is a pseudorandom function (and since D is efficient), there exists a negligible function $\mathsf{negl}$ for which

根据 F 是伪随机函数的假设（且 D 是高效的），存在一个可忽略函数 $\mathsf{negl}$ 使得

$$\left|\Pr\left[D^{F_{k}(\cdot)}(1^{n})=1\right]-\Pr\left[D^{f(\cdot)}(1^{n})=1\right]\right|\leq\mathsf{negl}(n).$$

Combining the above with Equations (3.10) and (3.11) gives Equation (3.9). For the second part of the proof, we show that

将上面的式子与式 (3.10) 和 (3.11) 结合即得式 (3.9)。对于证明的第二部分，我们证明

$$
\Pr\left[\mathsf{PrivK}_{\mathcal{A},\widetilde{\Pi}}^{\mathsf{cpa}}(n)=1\right]\leq\frac{1}{2}+\frac{q(n)}{2^{n}}.\tag{3.12}
$$

(Recall that $q(n)$ is a bound on the number of encryption queries made by $\mathcal{A}$.) The above holds even if we place no computational restrictions on $\mathcal{A}$. To see this, observe that every time a message $m$ is encrypted in $\mathsf{PrivK}_{\mathcal{A},\widetilde{\Pi}}^{\mathsf{cpa}}(n)$ (either by the encryption oracle or when the challenge ciphertext is computed), a uniform $r \in \{0,1\}^{n}$ is chosen and the ciphertext is set equal to $\langle r, f(r) \oplus m \rangle$. Let $r^*$ denote the random string used when generating the challenge ciphertext $\langle r^*, f(r^*) \oplus m_b \rangle$. There are two possibilities:

（回顾 $q(n)$ 是 $\mathcal{A}$ 进行的加密查询次数的上界。）即使我们对 $\mathcal{A}$ 不施加任何计算限制，上述不等式也成立。为看清这一点，注意在 $\mathsf{PrivK}_{\mathcal{A},\widetilde{\Pi}}^{\mathsf{cpa}}(n)$ 中每次加密消息 $m$ 时（无论是通过加密预言机还是计算挑战密文时），都会选择一个均匀的 $r \in \{0,1\}^{n}$，并将密文设为 $\langle r, f(r) \oplus m \rangle$。令 $r^*$ 表示生成挑战密文 $\langle r^*, f(r^*) \oplus m_b \rangle$ 时使用的随机串。有两种可能性：

1. The value $r^*$ is never used when answering any of $\mathcal{A}$'s encryption-oracle queries: In this case, $\mathcal{A}$ learns nothing about $f(r^*)$ from its interaction with the encryption oracle (since $f$ is a truly random function). This means that, from the perspective of $\mathcal{A}$, the value $f(r^*)$ that is XORed with $m_b$ is uniformly distributed and independent of the rest of the experiment, and so the probability that $\mathcal{A}$ outputs $b^{\prime} = b$ in this case is exactly ${1}/{2}$ (as in the case of the one-time pad).

   值 $r^*$ 从未用于回答 $\mathcal{A}$ 的任何加密预言机查询：在这种情况下，$\mathcal{A}$ 从与加密预言机的交互中学不到关于 $f(r^*)$ 的任何信息（因为 $f$ 是一个真正的随机函数）。这意味着，从 $\mathcal{A}$ 的角度看，与 $m_b$ 进行异或的值 $f(r^*)$ 是均匀分布的，并且与实验的其余部分独立，因此在这种情况下 $\mathcal{A}$ 输出 $b^{\prime} = b$ 的概率恰好是 ${1}/{2}$（与一次一密的情况一样）。

2. The value $r^*$ is used when answering at least one of $\mathcal{A}$'s encryption-oracle queries: In this case, $\mathcal{A}$ may easily determine whether $m_0$ or $m_1$ was encrypted. This is so because if the encryption oracle ever returns a ciphertext $\langle r^*, s \rangle$ in response to a request to encrypt the message $m$, the adversary learns that $f(r^*) = s \oplus m$.

   值 $r^*$ 被用于回答 $\mathcal{A}$ 的至少一个加密预言机查询：在这种情况下，$\mathcal{A}$ 可以轻松地确定 $m_0$ 还是 $m_1$ 被加密了。这是因为，如果加密预言机曾经在响应加密消息 $m$ 的请求时返回过密文 $\langle r^*, s \rangle$，那么敌手就知道 $f(r^*) = s \oplus m$。

However, since $\mathcal{A}$ makes at most $q(n)$ queries to its encryption oracle (and thus at most $q(n)$ values of $r$ are used when answering $\mathcal{A}$'s encryption-oracle queries), and since $r^*$ is chosen uniformly from $\{0,1\}^{n}$, the probability of this event is at most $q(n)/2^{n}$.

然而，由于 $\mathcal{A}$ 最多向其加密预言机进行 $q(n)$ 次查询（因此在回答 $\mathcal{A}$ 的加密预言机查询时最多使用 $q(n)$ 个 $r$ 值），并且由于 $r^*$ 是从 $\{0,1\}^{n}$ 中均匀选择的，该事件的概率至多为 $q(n)/2^{n}$。

Let repeat denote the event that $r^*$ is used by the encryption oracle when answering at least one of $\mathcal{A}$'s queries. As just discussed, the probability of repeat is at most $q(n)/2^n$, and the probability that $\mathcal{A}$ succeeds in $\mathsf{PrivK}_{\mathcal{A},\tilde{\Pi}}^{\mathsf{cpa}}$ if repeat does not occur is exactly ${1}/{2}$. Therefore:

令 repeat 表示 $r^*$ 被加密预言机用于回答 $\mathcal{A}$ 的至少一个查询的事件。正如刚才所讨论的，repeat 的概率至多为 $q(n)/2^n$，并且如果 repeat 不发生，$\mathcal{A}$ 在 $\mathsf{PrivK}_{\mathcal{A},\tilde{\Pi}}^{\mathsf{cpa}}$ 中成功的概率恰好为 ${1}/{2}$。因此：

$$\begin{aligned}\Pr&[\mathsf{PrivK}_{\mathcal{A},\widetilde{\Pi}}^{\mathsf{cpa}}(n)=1]\\ &\quad=\Pr[\mathsf{PrivK}_{\mathcal{A},\widetilde{\Pi}}^{\mathsf{cpa}}(n)=1\land repeat]+\Pr[\mathsf{PrivK}_{\mathcal{A},\widetilde{\Pi}}^{\mathsf{cpa}}(n)=1\land\overline{\mathsf{repeat}}]\\ &\quad\leq\Pr[\mathsf{repeat}]+\Pr[\mathsf{PrivK}_{\mathcal{A},\widetilde{\Pi}}^{\mathsf{cpa}}(n)=1\mid\overline{\mathsf{repeat}}]\leq\frac{q(n)}{2^{n}}+\frac{1}{2}.\end{aligned}$$

Combining the above with Equation (3.9), we see that there is a negligible function $\mathsf{negl}$ such that $\Pr[\mathsf{PrivK}_{\mathcal{A},\Pi}^{\mathsf{cpa}}(n) = 1] \leq \frac{1}{2} + \frac{q(n)}{2^n} + \mathsf{negl}(n)$. Since $q$ is polynomial, $\frac{q(n)}{2^n}$ is negligible. In addition, the sum of two negligible functions is negligible, and thus there exists a negligible function $\mathsf{negl}^{\prime}$ such that $\Pr[\mathsf{PrivK}_{\mathcal{A},\Pi}^{\mathsf{cpa}}(n) = 1] \leq \frac{1}{2} + \mathsf{negl}^{\prime}(n)$.

将上述结果与式 (3.9) 结合，我们看到存在一个可忽略函数 $\mathsf{negl}$ 使得 $\Pr[\mathsf{PrivK}_{\mathcal{A},\Pi}^{\mathsf{cpa}}(n) = 1] \leq \frac{1}{2} + \frac{q(n)}{2^n} + \mathsf{negl}(n)$。由于 $q$ 是多项式，$\frac{q(n)}{2^n}$ 是可忽略的。此外，两个可忽略函数之和仍然是可忽略的，因此存在一个可忽略函数 $\mathsf{negl}^{\prime}$ 使得 $\Pr[\mathsf{PrivK}_{\mathcal{A},\Pi}^{\mathsf{cpa}}(n) = 1] \leq \frac{1}{2} + \mathsf{negl}^{\prime}(n)$。

Concrete security. The above proof shows that

具体安全性。上述证明表明

$$\Pr[\mathsf{PrivK}_{\mathcal{A},\Pi}^{\mathsf{cpa}}(n)=1]\leq\frac{1}{2}+\frac{q(n)}{2^{n}}+\mathsf{negl}(n)$$

for some negligible function $\mathsf{negl}$. The final term depends on the security of $F$ as a pseudorandom function; it is a bound on the distinguishing advantage of algorithm $D$ (which has roughly the same running time as the adversary $\mathcal{A}$). The term $q(n)/2^n$ represents a bound on the probability that the value $r^*$ used to encrypt the challenge ciphertext was used to encrypt some other message, and depends on the number of encryption-oracle queries the attacker makes.

其中 $\mathsf{negl}$ 是某个可忽略函数。最后一项取决于 $F$ 作为伪随机函数的安全性；它是算法 $D$（其运行时间大致与敌手 $\mathcal{A}$ 相同）区分优势的一个界。项 $q(n)/2^n$ 表示用于加密挑战密文的值 $r^*$ 曾被用于加密其他消息的概率的一个界，依赖于攻击者进行的加密预言机查询次数。

## 3.6 Modes of Operation and Encryption in Practice　3.6 工作模式与实践中的加密

The encryption schemes described in Sections 3.3.3 and 3.5.2 (namely, Constructions 3.17 and 3.28) have a number of drawbacks that make them ill-suited for practical applications. For starters, Construction 3.17 is only EAV-secure. In addition, both constructions are defined only for the encryption of fixed-length messages. While Construction 3.28 could be used to encrypt arbitrary-length messages using the approach discussed at the end of Section 3.4.3, this would result in a scheme in which the ciphertext length is a constant multiple of the plaintext length, which is rather inefficient. In this section, we show how to overcome these drawbacks.

3.3.3 节和 3.5.2 节中描述的加密方案（即构造 3.17 和 3.28）存在一些缺点，使其不适合实际应用。首先，构造 3.17 仅满足 EAV 安全。此外，这两个构造仅针对定长消息的加密而定义。虽然使用 3.4.3 节末尾讨论的方法可以将构造 3.28 用于加密任意长度消息，但这会导致密文长度为明文长度的常数倍，相当低效。在本节中，我们将展示如何克服这些缺点。

While we are dealing with practical considerations, we also begin to discuss how the underlying building blocks of secure encryption schemes—namely, pseudorandom generators and pseudorandom permutations—are instantiated in the real world using stream ciphers and block ciphers, respectively. Our goal here is mainly to introduce the appropriate terminology and syntax; we defer an in-depth discussion of how stream ciphers and block ciphers are designed, and some popular candidates for those primitives, to Chapter 7.

在考虑实际问题的同时，我们也将开始讨论安全加密方案的基本构件——即伪随机生成器和伪随机置换——在现实世界中如何分别通过流密码（stream cipher）和分组密码（block cipher）来实例化。我们这里的目标主要是引入适当的术语和语法；关于流密码和分组密码的设计细节以及这些原语的一些流行候选方案，我们将推迟到第 7 章深入讨论。

### 3.6.1 Stream Ciphers　3.6.1 流密码

A pseudorandom generator $G$ as in Definition 3.14 is rather inflexible since its output length is fixed. This makes $G$ a poor fit for adapting Construction 3.17 to handle arbitrary-length messages. Specifically, say $G$ has expansion factor $\ell$. We cannot easily use $G$ to encrypt messages of length $\ell^{\prime} > \ell$ using a single $n$-bit key. And, although we can encrypt messages of length $\ell^{\prime} < \ell$ by truncating the output of $G$, doing so is wasteful since it involves generating $\ell$ pseudorandom bits and then discarding $\ell - \ell^{\prime}$ of them.

定义 3.14 中的伪随机生成器 $G$ 相当不灵活，因为其输出长度是固定的。这使得 $G$ 不太适合用于改造构造 3.17 以处理任意长度消息。具体来说，设 $G$ 的扩展因子为 $\ell$。我们不能轻易地使用 $G$ 以单个 $n$ 比特密钥来加密长度 $\ell^{\prime} > \ell$ 的消息。而且，虽然我们可以通过截断 $G$ 的输出来加密长度 $\ell^{\prime} < \ell$ 的消息，但这样做很浪费，因为它需要生成 $\ell$ 个伪随机比特，然后丢弃其中的 $\ell - \ell^{\prime}$ 个。

Stream ciphers, used in practice to instantiate pseudorandom generators, provide greater flexibility. The output bits of a stream cipher are produced gradually and on demand, so that an application can request exactly as many pseudorandom bits as it needs. This extends their usefulness (since there is no upper bound on the number of bits that can be generated) and improves efficiency (since no extraneous pseudorandom bits are generated).

实践中用于实例化伪随机生成器的流密码提供了更大的灵活性。流密码的输出比特是逐步按需生成的，因此应用程序可以请求恰好所需的伪随机比特数。这扩展了它们的实用性（因为可生成的比特数没有上界）并提高了效率（因为不会生成多余的伪随机比特）。

Formally, a stream cipher is a pair of deterministic algorithms (Init, Next) where:

形式化地，一个流密码是一对确定性算法 (Init, Next)，其中：

- Init takes as input a seed s and an optional initialization vector IV, and outputs some initial state st.

  Init 以种子 s 和一个可选的初始化向量 IV 为输入，输出某个初始状态 st。

- Next takes as input a current state st and outputs a bit$^3$ y along with updated state st'.

  Next 以当前状态 st 为输入，输出一个比特$^3$ y 以及更新后的状态 st'。

$^3$ In practice, Next might output a byte or even a larger number of random bits, rather than just outputting a single bit at a time. We assume it outputs a bit for simplicity here. / 实践中，Next 可能一次输出一个字节甚至更多随机比特，而不是每次只输出单个比特；为简单起见，这里假设它输出一个比特。

Starting from some initial state $\mathbf{st}_{0}$, we can generate any desired number of bits by repeatedly calling Next as many times as needed. As shorthand for this, we define an algorithm GetBits that takes as input an initial state $\mathbf{st}_{0}$ and a desired output length ${1}^{\ell}$ (specified in unary, since GetBits runs in time linear in $\ell$) and then does:

从某个初始状态 $\mathbf{st}_{0}$ 开始，我们可以通过根据需要重复调用 Next 任意多次来生成任意数量的比特。作为简写，我们定义一个算法 GetBits，它输入初始状态 $\mathbf{st}_{0}$ 和期望的输出长度 ${1}^{\ell}$（用一元表示法指定，因为 GetBits 的运行时间与 $\ell$ 成线性关系），然后执行：

1. For $i = 1$ to $\ell$, compute $(y_i, \mathrm{st}_i) := \mathrm{Next}(\mathrm{st}_{i-1})$.

   对于 $i = 1$ 到 $\ell$，计算 $(y_i, \mathrm{st}_i) := \mathrm{Next}(\mathrm{st}_{i-1})$。

2. Return the $\ell$-bit string $y = y_1 \cdots y_\ell$ as well as the final state $st_\ell$.

   返回 $\ell$ 比特串 $y = y_1 \cdots y_\ell$ 以及最终状态 $st_\ell$。

We let $\mathsf{GetBits}_{1}$ be the algorithm that runs GetBits and only returns its initial output (namely, the $\ell$-bit string y).

我们令 GetBits $_1$ 为运行 GetBits 但只返回其第一个输出（即 $\ell$ 比特串 y）的算法。

A secure stream cipher without an $IV$ is just a pseudorandom generator with a more flexible interface. That is, we require that when we run $\mathsf{Init}$ on a uniform seed $s$ to obtain $\text{st}_0$, and then generate any (polynomial) number of bits using $\mathsf{GetBits}_1$, the resulting output is pseudorandom. Formally, given a stream cipher $(\mathsf{Init}, \text{Next})$ and a parameter $\ell = \ell(n) > n$, we may define the deterministic function $G^\ell$ as

没有 $IV$ 的安全流密码只是一个具有更灵活接口的伪随机生成器。也就是说，我们要求当我们在均匀种子 $s$ 上运行 $\mathsf{Init}$ 得到 $\text{st}_0$，然后使用 $\mathsf{GetBits}_1$ 生成任意（多项式）数量的比特时，得到的输出是伪随机的。形式化地，给定一个流密码 $(\mathsf{Init}, \text{Next})$ 和一个参数 $\ell = \ell(n) > n$，我们可以定义确定性函数 $G^\ell$ 为

$$G^{\ell}(s)\overset{\operatorname{def}}{=}\mathsf{GetBits}_{1}(\mathsf{Init}(s),1^{\ell}).$$

Then the stream cipher is secure if $G^{\ell}$ is a pseudorandom generator for any polynomial $\ell$.

那么，如果对于任何多项式 $\ell$，$G^{\ell}$ 都是一个伪随机生成器，该流密码就是安全的。

Security for a stream cipher that does take an IV can be defined in multiple ways. We define security in this case to be akin to that of a pseudorandom function. Specifically, here we consider the setting where a uniform seed s is chosen and then $\mathsf{Init}(s, \cdot)$ is run repeatedly using different values for the IV; the requirement is that running $\mathsf{GetBits}_1$ using the different initial states should produce output streams that appear independently uniform. Formally, given a stream cipher ($\mathsf{Init}, \text{Next}$) (where $\mathsf{Init}$ takes an n-bit IV) and a parameter $\ell = \ell(n)$, we may define the keyed function $F^\ell : \{0,1\}^n \times \{0,1\}^n \to \{0,1\}^\ell$ as

对于确实接受 IV 的流密码，其安全性可以有多种定义方式。我们将这种情况下的安全性定义为与伪随机函数类似。具体而言，这里我们考虑以下设定：选择一个均匀种子 s，然后使用不同的 IV 值重复运行 $\mathsf{Init}(s, \cdot)$；要求是：使用不同的初始状态运行 $\mathsf{GetBits}_1$ 所产生的输出流应当表现为相互独立且均匀。形式化地，给定一个流密码 ($\mathsf{Init}, \text{Next}$)（其中 $\mathsf{Init}$ 接受一个 n 比特的 IV）和一个参数 $\ell = \ell(n)$，我们可以定义带密钥的函数 $F^\ell : \{0,1\}^n \times \{0,1\}^n \to \{0,1\}^\ell$ 为

$$F_{s}^{\ell}(IV)\overset{\operatorname{def}}{=}\mathsf{GetBits}_{1}(\mathsf{Init}(s,IV),1^{\ell}).$$

Then the stream cipher is secure if $F^{\ell}$ is a pseudorandom function for any polynomial $\ell$.

那么，如果对于任何多项式 $\ell$，$F^{\ell}$ 都是一个伪随机函数，该流密码就是安全的。

Practical stream ciphers typically do not support arbitrary values of $n$ (which determines the length of the seed and the $IV$), but instead work only for some fixed values of $n$. Concrete-security definitions are thus more appropriate than the asymptotic definitions given above.

实际的流密码通常不支持任意的 $n$ 值（它决定了种子和 $IV$ 的长度），而仅适用于某些固定的 $n$ 值。因此，具体安全性定义比上面给出的渐近定义更为合适。

Constructing stream ciphers from pseudorandom functions. A pseudorandom function F can be used to construct a stream cipher (Init, Next) that takes an IV. (This is very similar to the construction of pseudorandom generators from pseudorandom functions discussed briefly in Section 3.5.1.) The basic idea is to use the seed s for the stream cipher as a key for F, and to evaluate $F_s$ on a sequence of consecutive inputs starting from a value determined by IV. Concretely, if we set the length of the initialization vector to 3n/4, then the output of the stream cipher will be

从伪随机函数构造流密码。伪随机函数 F 可用于构造接受 IV 的流密码 (Init, Next)。（这与 3.5.1 节中简要讨论的从伪随机函数构造伪随机生成器非常相似。）基本思想是将流密码的种子 s 用作 F 的密钥，并在从 IV 确定的值开始的一系列连续输入上求值 $F_s$。具体来说，如果我们将初始化向量的长度设为 3n/4，那么流密码的输出将是

$$F_{s}(IV\|\langle 0\rangle),F_{s}(IV\|\langle 1\rangle),\ldots$$

(see Construction 3.30), where $\langle i \rangle$ denotes the binary encoding of integer $i$ as an $n/4$-bit string. Informally, this will be secure (assuming $F$ is a pseudorandom function) as long as no more than ${2}^{n/4}$ output blocks are generated for any $IV$, since in that case $F_s$ is evaluated at distinct inputs when the stream cipher is used with different $IVs$.

（见构造 3.30），其中 $\langle i \rangle$ 表示整数 $i$ 的二进制编码，编码为 $n/4$ 比特串。非正式地说，只要对任何 $IV$ 生成的输出块不超过 ${2}^{n/4}$ 个，这就是安全的（假设 $F$ 是伪随机函数），因为在这种情况下，当流密码使用不同的 $IV$ 时，$F_s$ 会在不同的输入上被求值。

> **CONSTRUCTION 3.30**　**构造 3.30**
>
> Let F be a pseudorandom function. Define a stream cipher (Init, Next) as follows, where Init accepts a 3n/4-bit initialization vector and Next outputs n bits in each call:
>
> - Init: on input $s \in \{0,1\}^n$ and $IV \in \{0,1\}^{3n/4}$, output $st = (s, IV, 0)$.
> - Next: on input st = (s, IV, i), output y := $F_s(IV \parallel \langle i \rangle)$ and updated state st' = (s, IV, i+1).
>
> 令 F 为一个伪随机函数。定义如下的流密码 (Init, Next)，其中 Init 接受一个 3n/4 比特的初始化向量，每次调用 Next 输出 n 比特：
>
> - Init：输入 $s \in \{0,1\}^n$ 和 $IV \in \{0,1\}^{3n/4}$，输出 $st = (s, IV, 0)$。
> - Next：输入 st = (s, IV, i)，输出 y := $F_s(IV \parallel \langle i \rangle)$ 和更新后的状态 st' = (s, IV, i+1)。
>
> A stream cipher from a pseudorandom function.
>
> 基于伪随机函数的流密码。

Although stream ciphers can be constructed from pseudorandom functions in this way, dedicated constructions of stream ciphers used in practice typically have better performance, especially in resource-constrained environments.

虽然流密码可以通过这种方式从伪随机函数构造而来，但实践中使用的专用流密码构造通常具有更好的性能，尤其是在资源受限的环境中。

### 3.6.2 Stream-Cipher Modes of Operation　3.6.2 流密码工作模式

We discuss two modes of operation for encrypting arbitrary-length messages using a stream cipher (Init, Next): synchronized mode and unsynchronized mode.

我们讨论使用流密码 (Init, Next) 加密任意长度消息的两种工作模式：同步模式（synchronized mode）和非同步模式（unsynchronized mode）。

Synchronized mode. Stream ciphers are often used to encrypt an online communication session between two parties. In that case, a fresh key k is generated by the parties (e.g., using methods described in Chapter 11) and then that key is used to encrypt the messages sent during the session. Assuming that the communication between the parties is such that all messages arrive in order and no messages are lost (as is the case, e.g., when communicating over TCP), the two parties are synchronized and the following method can be used to encrypt a series of messages from a sender S to a receiver R:

同步模式。流密码通常用于加密两方之间的在线通信会话。在这种情况下，双方生成一个新密钥 $k$（例如，使用第 11 章中描述的方法），然后使用该密钥加密会话期间发送的消息。假设双方之间的通信满足所有消息按顺序到达且没有消息丢失（例如通过 TCP 通信时的情况），则两方是同步的，可以使用以下方法加密从发送方 $S$ 到接收方 $R$ 的一系列消息：

1. Both parties call $\mathsf{Init}(k)$ to obtain the same initial state $\text{st}_{0}$.

   双方调用 $\mathsf{Init}(k)$ 以获得相同的初始状态 $\text{st}_{0}$。

2. Let $\mathbf{st}_S$ be the current state of $S$. If $S$ wants to encrypt a message $m$, it computes $(y, \mathbf{st}_S^{\prime}) := \mathsf{GetBits}(\mathbf{st}_S, 1^{|m|})$, sends $c := m \oplus y$ to the receiver, and updates its local state to $\mathbf{st}_S^{\prime}$.

   令 $\mathbf{st}_S$ 为 $S$ 的当前状态。如果 $S$ 想要加密消息 $m$，它计算 $(y, \mathbf{st}_S^{\prime}) := \mathsf{GetBits}(\mathbf{st}_S, 1^{|m|})$，将 $c := m \oplus y$ 发送给接收方，并将其本地状态更新为 $\mathbf{st}_S^{\prime}$。

3. Let $\mathbf{st}_R$ be the current state of $R$. When $R$ receives a ciphertext $c$ from the sender, it computes $(y, \mathbf{st}_R^{\prime}) := \mathsf{GetBits}(\mathbf{st}_R, 1^{|c|})$, outputs the message $m := c \oplus y$, and updates its own local state to $\mathbf{st}_R^{\prime}$.

   令 $\mathbf{st}_R$ 为 $R$ 的当前状态。当 $R$ 从发送方收到密文 $c$ 时，它计算 $(y, \mathbf{st}_R^{\prime}) := \mathsf{GetBits}(\mathbf{st}_R, 1^{|c|})$，输出消息 $m := c \oplus y$，并将其本地状态更新为 $\mathbf{st}_R^{\prime}$。

In the above description, the same party always acts as a sender. But by sharing a second key the parties can support bidirectional communication.

在上述描述中，同一方始终作为发送方。但通过共享第二个密钥，双方可以支持双向通信。

Let $\ell$ denote the total combined length of all messages encrypted during the course of a session. Conceptually, synchronized mode encryption can be viewed as a counterpart to Construction 3.17 where (1) $\ell$ need not be fixed in advance, and (2) the entire "message" need not be encrypted at once.

令 $\ell$ 表示会话期间加密的所有消息的总长度。概念上，同步模式加密可以看作是构造 3.17 的对应形式，其中 (1) $\ell$ 无须预先固定，(2) 整个“消息”无须一次性加密完毕。

The above is an example of stateful encryption where the sender and receiver are required to maintain state between the encryption/decryption of different messages. One can define an appropriate notion of CPA-security suitable for stateful encryption, and prove that the above scheme meets that definition if the underlying stream cipher is secure.

上述是一个有状态加密（stateful encryption）的例子，其中发送方和接收方需要在不同消息的加密/解密之间维护状态。可以为有状态加密定义一个适当的 CPA 安全概念，并证明如果底层流密码是安全的，上述方案满足该定义。

Observe that for synchronized mode, the stream cipher does not need to use an IV. Note also that there is no ciphertext expansion, since the total communication from the sender to the receiver is exactly equal to the total length of the messages being encrypted.

注意，对于同步模式，流密码不需要使用 IV。还要注意，没有密文扩展，因为从发送方到接收方的总通信量恰好等于被加密消息的总长度。

Unsynchronized mode. When a stream cipher does take an IV, it can be used to construct a stateless encryption scheme that is exactly analogous to Construction 3.28; see Construction 3.31. CPA-security of this scheme follows as in the proof of Theorem 3.29. We stress that the main advantage here is that the encryption scheme directly handles arbitrary-length messages.

非同步模式。当流密码确实接受 IV 时，它可以用于构造一个与构造 3.28 完全类似的无状态加密方案；见构造 3.31。该方案的 CPA 安全性可仿照定理 3.29 的证明证得。我们强调，这里的主要优势在于加密方案直接处理任意长度的消息。

> **CONSTRUCTION 3.31**　**构造 3.31**
>
> Let (Init, Next) be a stream cipher that takes an n-bit IV. Define a private-key encryption scheme for arbitrary-length messages as follows:
>
> - Gen: on input ${1}^n$, choose a uniform $k \in \{0,1\}^n$ and output it.
> - Enc: on input a key $k \in \{0,1\}^n$ and a message $m \in \{0,1\}^*$, choose uniform $IV \in \{0,1\}^n$, and output the ciphertext $\langle IV, \mathsf{GetBits}_1(\mathsf{Init}(k, IV), 1^{|m|}) \oplus m \rangle$.
> - Dec: on input a key $k \in \{0,1\}^n$ and a ciphertext $\langle IV, c \rangle$, output the message $m := \mathsf{GetBits}_1(\mathsf{Init}(k, IV), 1^{|c|}) \oplus c$.
>
> 令 (Init, Next) 为一个接受 n 比特 IV 的流密码。定义如下的私钥加密方案，用于任意长度消息：
>
> - Gen：输入 ${1}^n$，选择一个均匀的 $k \in \{0,1\}^n$ 并输出。
> - Enc：输入密钥 $k \in \{0,1\}^n$ 和消息 $m \in \{0,1\}^*$，选择均匀的 $IV \in \{0,1\}^n$，输出密文 $\langle IV, \mathsf{GetBits}_1(\mathsf{Init}(k, IV), 1^{|m|}) \oplus m \rangle$。
> - Dec：输入密钥 $k \in \{0,1\}^n$ 和密文 $\langle IV, c \rangle$，输出消息 $m := \mathsf{GetBits}_1(\mathsf{Init}(k, IV), 1^{|c|}) \oplus c$。
>
> Unsynchronized mode encryption from a stream cipher that takes an IV.
>
> 基于接受 IV 的流密码的非同步模式加密。

### 3.6.3 Block Ciphers and Block-Cipher Modes of Operation　3.6.3 分组密码与分组密码工作模式

A block cipher is simply another name for a (strong) pseudorandom permutation. That is, a block cipher $F : \{0,1\}^n \times \{0,1\}^\ell \to \{0,1\}^\ell$ is a keyed function such that, for all $k$, the function $F_k$ defined by $F_k(x) \overset{\mathrm{def}}{=} F(k,x)$ is a bijection (i.e., a permutation). Recall that $n$ is the key length of $F$, and $\ell$ is its block length. The main distinction between block ciphers and pseudo-random permutations is that the former typically only support a specific set of key/block lengths, and in particular do not support arbitrary-length keys. For simplicity, we will assume in this section that $\ell = n$.

分组密码就是（强）伪随机置换的另一个名称。也就是说，分组密码 $F : \{0,1\}^n \times \{0,1\}^\ell \to \{0,1\}^\ell$ 是一个带密钥的函数，使得对所有 $k$，由 $F_k(x) \overset{\mathrm{def}}{=} F(k,x)$ 定义的函数 $F_k$ 是一个双射（即一个置换）。回顾 $n$ 是 $F$ 的密钥长度，$\ell$ 是其分组长度。分组密码与伪随机置换之间的主要区别在于，前者通常只支持特定的密钥/分组长度集合，特别是不支持任意长度的密钥。为简单起见，我们在本节中将假定 $\ell = n$。

As shown earlier (cf. Construction 3.30), a block cipher can be used to construct a stream cipher that accepts an $IV$; this means we can use any block cipher $F$ to implement the stream-cipher modes of operation discussed in Section 3.6.2. Several other block-cipher modes of operation are also possible; here, we present four of the most common ones and discuss their security. In our discussion, we assume for simplicity that all messages $m$ being encrypted have length a multiple of $n$ (the block length of $F$), and write $m = m_1, m_2, \ldots, m_\ell$ where each $m_i \in \{0, 1\}^n$ represents a block of the plaintext. (Messages whose length is not a multiple of $n$ can be unambiguously padded to have length a multiple of $n$ by appending a 1 followed by sufficiently many 0s, and so this assumption is without much loss of generality.)

如前所示（参见构造 3.30），分组密码可用于构造接受 $IV$ 的流密码；这意味着我们可以使用任何分组密码 $F$ 来实现 3.6.2 节中讨论的流密码工作模式。其他几种分组密码工作模式也是可能的；在此，我们介绍四种最常见的模式并讨论它们的安全性。在讨论中，为简单起见，我们假定所有被加密的消息 $m$ 的长度都是 $n$（$F$ 的分组长度）的倍数，并写作 $m = m_1, m_2, \ldots, m_\ell$，其中每个 $m_i \in \{0, 1\}^n$ 代表明文的一个分组。（长度不是 $n$ 的倍数的消息可以通过附加一个 1 后跟足够多的 0 来无歧义地填充为 $n$ 的倍数长度，因此这一假设几乎不失一般性。）

Electronic Code Book (ECB) mode. This is a naive mode of operation in which the ciphertext is obtained by direct application of the block cipher to each plaintext block. That is, $c := F_k(m_1), F_k(m_2), \ldots, F_k(m_\ell)$; see Figure 3.4. Decryption is done in the obvious way, using the fact that $F_k^{-1}$ is efficiently computable.

电子密码本（ECB）模式。这是一种朴素的工作模式，其中密文通过将分组密码直接应用于每个明文分组而得到。即 $c := F_k(m_1), F_k(m_2), \ldots, F_k(m_\ell)$；见图 3.4。解密以明显的方式进行，利用了 $F_k^{-1}$ 可高效计算这一事实。

![Image](https://lsky.jerryxue.top/i/2026/08/22/6a88f9dfe2c85.jpg)

**FIGURE 3.4: Electronic Code Book (ECB) mode.**

**图 3.4：电子密码本（ECB）模式。**

ECB mode is deterministic and therefore cannot be CPA-secure. Worse, ECB-mode encryption is not even EAV-secure. This is because if a block is repeated in the plaintext, it will result in a repeating block in the ciphertext. Thus, for example, it is easy to distinguish the encryption of a plaintext that consists of two identical blocks from the encryption of a plaintext that consists of two different blocks. This is not just a theoretical problem. Consider encrypting an image in which small groups of pixels correspond to a plaintext block. Encrypting using ECB mode may reveal a significant amount of information about patterns in the image, something that should not happen when using a secure encryption scheme. (Figure 3.5 demonstrates this.) For these reasons, ECB mode should never be used.

ECB 模式是确定性的，因此不可能是 CPA 安全的。更糟的是，ECB 模式甚至不是 EAV 安全的。这是因为如果明文中的某个分组重复出现，将导致密文中相应分组的重复。因此，例如，很容易区分由两个相同分组组成的明文的加密和由两个不同分组组成的明文的加密。这不仅仅是一个理论问题。考虑加密一幅图像，其中小的像素组对应一个明文分组。使用 ECB 模式加密可能会泄露图像模式的大量信息，而使用安全加密方案时不应发生这种情况。（图 3.5 演示了这一点。）由于这些原因，ECB 模式绝不应当被使用。

![Image](https://lsky.jerryxue.top/i/2026/08/22/6a88f9e0c0c45.jpg)

**FIGURE 3.5: An illustration of the dangers of using ECB mode. The middle figure is an encryption of the image on the left using ECB mode; the figure on the right is an encryption of the same image using a secure mode. (Taken from http://en.wikipedia.org and derived from images created by Larry Ewing (lewing@isc.tamu.edu) using The GIMP.)**

**图 3.5：使用 ECB 模式危险性的图示。中间图是使用 ECB 模式对左侧图像的加密；右侧图是使用安全模式对同一图像的加密。（取自 http://en.wikipedia.org，源自 Larry Ewing (lewing@isc.tamu.edu) 使用 The GIMP 创建的图像。）**

Cipher Block Chaining (CBC) mode. To encrypt here, a uniform initialization vector $(IV)$ of length $n$ is first chosen as the initial ciphertext block. Then, ciphertext blocks are generated by applying the block cipher to the XOR of the current plaintext block and the previous ciphertext block. That is, set $c_0 := IV$ and then, for $i = 1$ to $\ell$, set $c_i := F_k(c_{i-1} \oplus m_i)$. The final ciphertext is $c_0, c_1, \ldots, c_\ell$. (See Figure 3.6.) Decryption of a ciphertext $c_0, \ldots, c_\ell$ is done by computing $m_i := F_k^{-1}(c_i) \oplus c_{i-1}$ for $i = 1, \ldots, \ell$. Note that the $IV$ is included in the ciphertext (and so the ciphertext is $n$ bits longer than the plaintext); this is crucial so decryption can be done.

密码分组链接（CBC）模式。在 CBC 模式中加密时，首先选择一个长度为 $n$ 的均匀初始化向量 $(IV)$ 作为初始密文分组。然后，通过将分组密码应用于当前明文分组与前一个密文分组的异或来生成密文分组。即，设 $c_0 := IV$，然后对于 $i = 1$ 到 $\ell$，设 $c_i := F_k(c_{i-1} \oplus m_i)$。最终的密文为 $c_0, c_1, \ldots, c_\ell$。（见图 3.6。）对密文 $c_0, \ldots, c_\ell$ 的解密通过对于 $i = 1, \ldots, \ell$ 计算 $m_i := F_k^{-1}(c_i) \oplus c_{i-1}$ 来完成。注意 $IV$ 被包含在密文中（因此密文比明文长 $n$ 比特）；这对于能够解密至关重要。

CBC encryption is randomized, and it is possible to show:

CBC 加密是随机化的，并且可以证明：

THEOREM 3.32 If F is a pseudorandom permutation, then CBC mode is CPA-secure.

定理 3.32 如果 F 是一个伪随机置换，那么 CBC 模式是 CPA 安全的。

The main drawback of CBC mode is that encryption must be carried out sequentially because the previous ciphertext block $c_{i-1}$ is needed in order to process the next plaintext block $m_i$. Thus, if parallel processing is available, CBC-mode encryption may not be the most efficient choice.

CBC 模式的主要缺点是加密必须顺序进行，因为处理下一个明文分组 $m_i$ 时需要前一个密文分组 $c_{i-1}$。因此，如果并行处理可用，CBC 模式加密可能不是最高效的选择。

![Image](https://lsky.jerryxue.top/i/2026/08/22/6a88f9e183fb4.jpg)

**FIGURE 3.6: Cipher Block Chaining (CBC) mode.**

**图 3.6：密码分组链接（CBC）模式。**

There is a stateful variant of CBC-mode encryption—called chained CBC mode—in which the last block of the previous ciphertext is used as the IV when encrypting the next message. This reduces the bandwidth, as a new IV need not be sent each time. See Figure 3.7, where an initial message $m_1, m_2, m_3$ is encrypted using a uniform IV, and then subsequently a second message $m_4, m_5$ is encrypted using the final ciphertext block of the previous ciphertext (i.e., $c_3$) as the IV. (In contrast, encryption using standard CBC mode would generate a fresh, random IV when encrypting the second message.) Chained CBC mode was used in SSL 3.0 and TLS 1.0.

CBC 模式加密有一个有状态变体——称为链式 CBC 模式（chained CBC mode）——其中前一个密文的最后一个分组被用作加密下一条消息时的 IV。这减少了带宽，因为每次无需发送新的 IV。见图 3.7，其中初始消息 $m_1, m_2, m_3$ 使用均匀 IV 加密，然后第二条消息 $m_4, m_5$ 使用前一个密文的最后一个密文分组（即 $c_3$）作为 IV 进行加密。（相比之下，使用标准 CBC 模式加密会在加密第二条消息时生成一个新的随机 IV。）链式 CBC 模式曾在 SSL 3.0 和 TLS 1.0 中使用。

![Image](https://lsky.jerryxue.top/i/2026/08/22/6a88f9e27d98b.jpg)

**FIGURE 3.7: Chained CBC mode.**

**图 3.7：链式 CBC 模式。**

It may appear that chained CBC mode is as secure as CBC mode, since the chained-CBC encryption of $m_1, m_2, m_3$ followed by encryption of $m_4, m_5$ yields the same ciphertext blocks as CBC-mode encryption of the (single) message $m_1, m_2, m_3, m_4, m_5$. Nevertheless, chained CBC mode is vulnerable to a chosen-plaintext attack. The basis of the attack is that the adversary knows in advance the "initialization vector" $c_3$ that will be used for the second encrypted message. We describe the attack informally, based on Figure 3.7. Assume the attacker knows that $m_1 \in \{m_1^0, m_1^1\}$, and observes the first ciphertext $IV, c_1, c_2, c_3$. The attacker then requests an encryption of a second message $m_4, m_5$ with $m_4 = IV \oplus m_1^0 \oplus c_3$, and observes a second ciphertext $c_4, c_5$. One can verify that $m_1 = m_1^0$ if and only if $c_4 = c_1$, and so the attacker learns $m_1$. This example serves as a warning against making any modifications to cryptographic schemes, even if those modifications seem benign.

链式 CBC 模式看起来可能与 CBC 模式一样安全，因为 $m_1, m_2, m_3$ 的链式 CBC 加密后再加密 $m_4, m_5$ 产生的密文分组与对（单一）消息 $m_1, m_2, m_3, m_4, m_5$ 进行 CBC 模式加密产生的密文分组相同。然而，链式 CBC 模式容易受到选择明文攻击。该攻击的基础是敌手预先知道加密第二条消息时将使用的“初始化向量” $c_3$。我们基于图 3.7 非正式地描述该攻击。假设攻击者知道 $m_1 \in \{m_1^0, m_1^1\}$，并观察到第一个密文 $IV, c_1, c_2, c_3$。然后攻击者请求加密第二条消息 $m_4, m_5$，其中 $m_4 = IV \oplus m_1^0 \oplus c_3$，并观察到第二个密文 $c_4, c_5$。可以验证，$m_1 = m_1^0$ 当且仅当 $c_4 = c_1$，因此攻击者得知 $m_1$。这个例子警告我们不要对密码方案做任何修改，即使这些修改看起来是良性的。

Output Feedback (OFB) mode. The third mode we present can be viewed as an unsynchronized stream-cipher mode, where the stream cipher is constructed in a specific way from the underlying block cipher. We describe the mode directly. To encrypt a message $m$, first a uniform $IV \in \{0,1\}^n$ is chosen. Then, a pseudorandom stream is generated from IV in the following way:

输出反馈（OFB）模式。我们介绍的第三种模式可以看作是非同步流密码模式，其中流密码以特定方式从底层分组密码构造而来。我们直接描述该模式。要加密消息 $m$，首先选择一个均匀的 $IV \in \{0,1\}^n$。然后，从 IV 以如下方式生成伪随机流：

![Image](https://lsky.jerryxue.top/i/2026/08/22/6a88f9e387f93.jpg)

**FIGURE 3.8: Output Feedback (OFB) mode.**

**图 3.8：输出反馈（OFB）模式。**

Define $y_0 := IV$, and set the $i$th block $y_i$ of the stream to be $y_i := F_k(y_{i-1})$. Each block of the plaintext is then encrypted by XORing it with the appropriate block of the stream; that is, $c_i := y_i \oplus m_i$. (See Figure 3.8.) As in CBC mode, the $IV$ is included as part of the ciphertext to enable decryption. However, in contrast to CBC mode, here it is not required that $F$ be invertible. (In fact, it need not even be a permutation.) Furthermore, as in stream-cipher modes of operation, here it is not necessary for the plaintext length to be a multiple of the block length $n$; instead, the generated stream can be truncated to exactly the plaintext length. Another advantage of OFB mode is that its stateful variant (in which the final value $y_\ell$ is used as the IV for encrypting the next message, and is not sent) is secure. This stateful variant is equivalent to a synchronized stream-cipher mode, with the stream cipher constructed from the block cipher in a specific way.

定义 $y_0 := IV$，并将流的第 $i$ 个分组 $y_i$ 设为 $y_i := F_k(y_{i-1})$。然后，通过将每个明文分组与流的相应分组进行异或来加密；即 $c_i := y_i \oplus m_i$。（见图 3.8。）与 CBC 模式一样，$IV$ 作为密文的一部分包含在内以支持解密。然而，与 CBC 模式不同的是，这里不要求 $F$ 可逆。（实际上，它甚至不必是置换。）此外，与流密码工作模式一样，这里不要求明文长度是分组长度 $n$ 的倍数；相反，生成的流可以被截断到恰好等于明文长度。OFB 模式的另一个优点是其有状态变体（其中最终值 $y_\ell$ 被用作加密下一条消息的 IV，且不被发送）是安全的。这种有状态变体等价于同步流密码模式，其中流密码以特定方式从分组密码构造而来。

OFB mode can be shown to be CPA-secure if $F$ is a pseudorandom function. Although encryption must be carried out sequentially, this mode has the advantage relative to CBC mode that the bulk of the computation (namely, computation of the pseudorandom stream) can be done independently of the actual message to be encrypted. That is, it is possible to generate a pseudorandom stream ahead of time using preprocessing, after which encryption of the plaintext (once it is known) is incredibly fast.

如果 $F$ 是伪随机函数，则可以证明 OFB 模式是 CPA 安全的。虽然加密必须顺序进行，但与 CBC 模式相比，该模式的优势在于大部分计算（即伪随机流的计算）可以与待加密的实际消息无关地进行。也就是说，可以使用预处理提前生成伪随机流，之后（一旦知道明文）对明文的加密将非常快。

Counter (CTR) mode. Counter mode can also be viewed as an unsynchronized stream-cipher mode, where the stream cipher is constructed from the block cipher in a way that is analogous to Construction 3.30. We give a self-contained description here. To encrypt a message with $\ell < 2^{n/4}$ blocks using CTR mode, a uniform $IV \in \{0,1\}^{3n/4}$ is first chosen. Then, a pseudorandom stream is generated by computing $y_i := F_k(IV \parallel \langle i\rangle)$ for $i = 1,2,\ldots$, where the counter $i$ is encoded as an $n/4$-bit string. (The lengths of the IV and the counter are somewhat arbitrary, as long as they sum to $n$. A longer IV leads to better concrete security—cf. the proof of Theorem 3.33—but reduces the maximum length of messages that can be encrypted.) The $i$th ciphertext block is computed as $c_i := y_i \oplus m_i$.

计数器（CTR）模式。计数器模式也可以视为非同步流密码模式，其中流密码以类似于构造 3.30 的方式从分组密码构造而来。我们在此给出一个自包含的描述。要使用 CTR 模式加密一个具有 $\ell < 2^{n/4}$ 个分组的消息，首先选择一个均匀的 $IV \in \{0,1\}^{3n/4}$。然后，对于 $i = 1,2,\ldots$ 计算 $y_i := F_k(IV \parallel \langle i\rangle)$ 来生成伪随机流，其中计数器 $i$ 被编码为 $n/4$ 比特串。（IV 和计数器的长度在一定程度上是任意的，只要它们的和为 $n$。更长的 IV 带来更好的具体安全性——参见定理 3.33 的证明——但会降低可加密消息的最大长度。）第 $i$ 个密文分组计算为 $c_i := y_i \oplus m_i$。

![Image](https://lsky.jerryxue.top/i/2026/08/22/6a88f9e43e155.jpg)

**FIGURE 3.9: Counter (CTR) mode.**

**图 3.9：计数器（CTR）模式。**

As in CBC and OFB modes, the IV is included as part of the ciphertext to enable decryption; see Figure 3.9. Note again that decryption does not require $F$ to be invertible, or even a permutation. As with OFB mode—another "stream-cipher" mode—the generated stream can be truncated to exactly the plaintext length, and preprocessing can be used to generate the pseudorandom stream before the message is known.

与 CBC 和 OFB 模式一样，IV 作为密文的一部分包含在内以支持解密；见图 3.9。再次注意，解密不要求 $F$ 可逆，甚至不要求它是置换。与 OFB 模式（另一种“流密码”模式）一样，生成的流可以被截断到恰好等于明文长度，并且可以使用预处理在消息已知之前生成伪随机流。

In contrast to all the secure modes discussed previously, CTR mode has the advantage that encryption and decryption can be fully parallelized, since all the blocks of the pseudorandom stream can be computed independently of each other. It is also possible to recover the $i$th block of the plaintext from the ciphertext using only a single evaluation of $F$. These features make CTR mode an attractive choice in practice.

与之前讨论的所有安全模式相比，CTR 模式具有加解密可以完全并行化的优势，因为伪随机流的所有分组可以彼此独立地计算。还可以仅使用一次 $F$ 的求值从密文中恢复明文的第 $i$ 个分组。这些特性使 CTR 模式在实践中成为有吸引力的选择。

We provide a proof that CTR mode is CPA-secure, since the proof of security in this case is relatively straightforward. We directly prove CPA-security for multiple encryptions (cf. Definition 3.22), rather than relying on Theorem 3.23, since the proof is equally simple and a direct proof yields a better concrete-security bound.

我们提供 CTR 模式是 CPA 安全的证明，因为这种情况下的安全证明相对直接。我们直接证明多重加密的 CPA 安全性（参见定义 3.22），而不是依赖定理 3.23，因为证明同样简单，且直接证明能给出更好的具体安全性界。

THEOREM 3.33 If F is a pseudorandom function, then CTR mode is CPA-secure for multiple encryptions.

定理 3.33 如果 F 是一个伪随机函数，那么 CTR 模式对于多重加密是 CPA 安全的。

PROOF We follow the same template as in the proof of Theorem 3.29: We first replace F with a random function and then analyze the resulting scheme.

证明 我们遵循与定理 3.29 证明中相同的模板：首先将 F 替换为随机函数，然后分析所得方案。

Fix an arbitrary PPT adversary $\mathcal{A}$, and let $q(n)$ be a polynomial upper-bound on the number of queries made by $\mathcal{A}(1^n)$ to its left-or-right oracle. We assume for simplicity that the messages $\mathcal{A}$ submits to its oracle always contain fewer than ${2}^{n/4}$ blocks. (This must be true for large enough $n$ since $\mathcal{A}$ runs in polynomial time.) Let $\Pi = (\mathsf{Gen}, \mathsf{Enc}, \mathsf{Dec})$ be the CTR-mode encryption scheme, and let $\widetilde{\Pi} = (\widetilde{\mathsf{Gen}}, \widetilde{\mathsf{Enc}}, \widetilde{\mathsf{Dec}})$ be the encryption scheme identical to $\Pi$ except that a random function is used in place of $F_k$. That is, $\widetilde{\mathsf{Gen}}(1^n)$ chooses a uniform function $f \in \mathsf{Func}_n$, and $\widetilde{\mathsf{Enc}}$ encrypts just like $\mathsf{Enc}$ except that $f$ is used instead of $F_k$. (Once again, neither $\widetilde{\mathsf{Gen}}$ nor $\widetilde{\mathsf{Enc}}$ is efficient but this does not matter for the purposes of defining an experiment involving $\widetilde{\Pi}$.)

固定一个任意 PPT 敌手 $\mathcal{A}$，令 $q(n)$ 为 $\mathcal{A}(1^n)$ 向其左右预言机进行的查询次数的多项式上界。为简单起见，我们假定 $\mathcal{A}$ 提交给其预言机的消息总是少于 ${2}^{n/4}$ 个分组。（对于足够大的 $n$ 这必须成立，因为 $\mathcal{A}$ 在多项式时间内运行。）令 $\Pi = (\mathsf{Gen}, \mathsf{Enc}, \mathsf{Dec})$ 为 CTR 模式加密方案，并令 $\widetilde{\Pi} = (\widetilde{\mathsf{Gen}}, \widetilde{\mathsf{Enc}}, \widetilde{\mathsf{Dec}})$ 为与 $\Pi$ 完全相同的加密方案，只是使用随机函数代替了 $F_k$。也就是说，$\widetilde{\mathsf{Gen}}(1^n)$ 选择一个均匀函数 $f \in \mathsf{Func}_n$，而 $\widetilde{\mathsf{Enc}}$ 的加密方式与 $\mathsf{Enc}$ 完全相同，只是使用 $f$ 代替了 $F_k$。（再次强调，$\widetilde{\mathsf{Gen}}$ 和 $\widetilde{\mathsf{Enc}}$ 都不是高效的，但这对于定义涉及 $\widetilde{\Pi}$ 的实验来说无关紧要。）

As the first step of the proof, we claim that there is a negligible function $\mathsf{negl}$ such that

作为证明的第一步，我们断言存在一个可忽略函数 $\mathsf{negl}$ 使得

$$\begin{array}{r l}&{\left|\Pr\left[\mathsf{Priv}\mathsf{K}_{\mathcal{A},\Pi}^{\mathsf{LR-cpa}}(n)=1\right]-\Pr\left[\mathsf{Priv}\mathsf{K}_{\mathcal{A},\widetilde{\Pi}}^{\mathsf{LR-cpa}}(n)=1\right]\right|\leq\mathsf{negl}(n).} \tag{3.13}\end{array}$$

This is proved by reduction to the pseudorandomness of $F$ in a way similar to the analogous step in the proof of Theorem 3.29, and so we omit the details.

这可以通过归约到 $F$ 的伪随机性来证明，方法与定理 3.29 证明中的对应步骤类似，因此我们省略细节。

We next claim that

接下来我们断言

$$
\Pr\left[\mathsf{PrivK}_{\mathcal{A},\widetilde{\Pi}}^{\mathsf{LR-cpa}}(n)=1\right]\leq\frac{1}{2}+\frac{q(n)^{2}}{2^{3n/4+1}}.\tag{3.14}
$$

Combined with Equation (3.13) this means that

结合式 (3.13)，这意味着

$$
\Pr\left[\mathsf{PrivK}_{\mathcal{A},\Pi}^{\mathsf{LR-cpa}}(n)=1\right]\leq\frac{1}{2}+\frac{q(n)^{2}}{2^{3n/4+1}}+\mathsf{negl}(n).\tag{3.15}
$$

Since $q$ is polynomial, $\frac{q(n)^{2}}{2^{3n/4+1}}$ is negligible and so this completes the proof.

由于 $q$ 是多项式，$\frac{q(n)^{2}}{2^{3n/4+1}}$ 是可忽略的，因此这就完成了证明。

To prove Equation (3.14), recall that a uniform $IV$ is chosen for each of $\mathcal{A}$'s queries to its left-or-right oracle. Let $IV_i$ be the $IV$ used to answer the $i$th oracle query. There are two possibilities:

为了证明式 (3.14)，回顾对于 $\mathcal{A}$ 向左右预言机的每次查询，都会选择一个均匀的 $IV$。令 $IV_i$ 为用于回答第 $i$ 次预言机查询的 $IV$。有两种可能性：

1. Each IV is distinct, i.e., $IV_i \neq IV_j$ for all $i \neq j$: The key observation is that in this case all the inputs to the random function f, across the entire experiment, are distinct. (If all IVs chosen are distinct, then the inputs to f when answering different oracle queries must be distinct; inputs to f when answering any particular oracle query are distinct from each other because of the counter.) Thus, the outputs of all the invocations of f are independent, uniform bit-strings. It follows that the ciphertexts returned by the left-or-right oracle are independent of the bit b determining which message is encrypted (by analogy with the one-time pad; see also the proof of Theorem 3.29). We conclude that the probability that $\mathcal{A}$ outputs $b^{\prime} = b$ in this case is exactly ${1}/{2}$.

   每个 IV 互不相同，即对所有 $i \neq j$ 有 $IV_i \neq IV_j$：关键的观察是，在这种情况下，整个实验中随机函数 $f$ 的所有输入都是不同的。（如果选择的所有 IV 都互不相同，那么回答不同预言机查询时输入到 $f$ 的值必定不同；回答任何特定预言机查询时输入到 $f$ 的值因计数器的存在而互不相同。）因此，$f$ 所有调用的输出都是独立、均匀的比特串。由此可知，左右预言机返回的密文与决定加密哪条消息的比特 b 无关（类似于一次一密；另见定理 3.29 的证明）。我们得出结论，在这种情况下 $\mathcal{A}$ 输出 $b^{\prime} = b$ 的概率恰好为 ${1}/{2}$。

2. Some IV is used more than once, i.e., $IV_i = IV_j$ for some $i \neq j$: In this case, $\mathcal{A}$ can easily determine whether b = 0 or b = 1. However, this event occurs with only negligible probability. Specifically, since $\mathcal{A}$ makes at most $q(n)$ queries to its oracle and each IV is chosen uniformly from $\{0,1\}^{3n/4}$, the probability of this event is at most $\frac{q(n)^2}{2^{3n/4+1}}$ (using Lemma A.15).

   某个 IV 被使用超过一次，即存在 $i \neq j$ 使得 $IV_i = IV_j$：在这种情况下，$\mathcal{A}$ 可以轻松确定 b = 0 还是 b = 1。然而，该事件仅以可忽略的概率发生。具体来说，由于 $\mathcal{A}$ 最多向其预言机进行 $q(n)$ 次查询，且每个 IV 从 $\{0,1\}^{3n/4}$ 中均匀选择，该事件的概率至多为 $\frac{q(n)^2}{2^{3n/4+1}}$（使用引理 A.15）。

Let repeat denote the event that some $IV$ is used more than once. As just discussed, the probability that $\mathcal{A}$ succeeds in $\mathsf{PrivK}_{\mathcal{A},\tilde{\Pi}}^{\mathsf{LR-cpa}}$ if repeat does not occur is exactly 1/2, and $\Pr[\mathsf{repeat}] \leq \frac{q(n)^2}{2^{3n/4+1}}$. Therefore:

令 repeat 表示某个 $IV$ 被使用超过一次的事件。正如刚才所讨论的，如果 repeat 不发生，$\mathcal{A}$ 在 $\mathsf{PrivK}_{\mathcal{A},\tilde{\Pi}}^{\mathsf{LR-cpa}}$ 中成功的概率恰好为 1/2，且 $\Pr[\mathsf{repeat}] \leq \frac{q(n)^2}{2^{3n/4+1}}$。因此：

$$\begin{aligned}&\Pr[\mathsf{PrivK}_{\mathcal{A},\widetilde{\Pi}}^{\mathsf{LR-cpa}}(n)=1]\\ &=\Pr[\mathsf{PrivK}_{\mathcal{A},\widetilde{\Pi}}^{\mathsf{LR-cpa}}(n)=1\land\overline{\mathsf{repeat}}]+\Pr[\mathsf{PrivK}_{\mathcal{A},\widetilde{\Pi}}^{\mathsf{LR-cpa}}(n)=1\land\mathsf{repeat}]\\ &\leq\Pr[\mathsf{PrivK}_{\mathcal{A},\widetilde{\Pi}}^{\mathsf{LR-cpa}}(n)=1\mid\overline{\mathsf{repeat}}]+\Pr[\mathsf{repeat}]\leq\frac{1}{2}+\frac{q(n)^{2}}{2^{3n/4+1}},\end{aligned}$$

proving Equation (3.14).

这就证明了式 (3.14)。

#### Practical Considerations　实际考虑

We conclude this section with a brief discussion of some issues that arise in practice when using block-cipher modes of operation.

在本节最后，我们简要讨论在使用分组密码工作模式时实践中出现的一些问题。

Block length and concrete security. CBC, OFB, and CTR modes all use a uniform IV. This has the effect of randomizing the encryption process, and ensures that (with high probability) the underlying block cipher is always evaluated on fresh (i.e., new) inputs. This is important because, as we have noted in the proofs of Theorem 3.29 and Theorem 3.33, if an input to the block cipher is repeated an adversary may learn information about a message.

分组长度与具体安全性。CBC、OFB 和 CTR 模式都使用均匀的 IV。这具有随机化加密过程的效果，并确保（以高概率）底层分组密码总是在新鲜的（即新的）输入上被求值。这一点很重要，因为正如我们在定理 3.29 和定理 3.33 的证明中指出的，如果分组密码的输入重复，敌手可能了解到关于某条消息的信息。

The block length of a block cipher thus has a significant impact on the concrete security of encryption schemes based on that cipher. Consider, e.g., CTR mode, whose concrete security when using a block cipher F with block length n is given by Equation (3.15). Since the IV is a uniform string of length 3n/4, we expect an IV to repeat after encrypting $q(n) \approx 2^{3n/8}$ messages (cf. Lemma A.15). If n is too short, then the resulting concrete-security bound will be too weak for practical applications. Concretely, if n = 64 then after encrypting $q = 2^{24} \approx 17,000,000$ messages a repeated IV is expected to occur. Although this may seem like a lot, encrypting that many messages using a single key is commonplace nowadays.

因此，分组密码的分组长度对基于该密码的加密方案的具体安全性有显著影响。例如，考虑 CTR 模式，当使用分组长度为 n 的分组密码 F 时，其具体安全性由式 (3.15) 给出。由于 IV 是长度为 3n/4 的均匀串，我们预计在加密 $q(n) \approx 2^{3n/8}$ 条消息后会出现 IV 重复（参见引理 A.15）。如果 n 太短，所得具体安全性界对于实际应用来说将太弱。具体来说，如果 n = 64，那么在加密 $q = 2^{24} \approx 17,000,000$ 条消息后，预计会发生 IV 重复。虽然这看起来很多，但现在使用单个密钥加密那么多消息是很常见的。

The security bound may be weak even when $n$ is large. For example, say $n = 128$ (which is the case for AES, a widely used block cipher we introduce in Chapter 7) and we want to use CTR mode while ensuring that an $IV$ repeats with probability at most ${2}^{-32}$. Solving $q^2/2^{3n/4+1} \leq 2^{-32}$ shows that we can safely encrypt only at most $q \approx 2^{32}$ messages.

即使当 $n$ 很大时，安全性界也可能较弱。例如，假设 $n = 128$（这是 AES 的情况，AES 是我们在第 7 章中介绍的一种广泛使用的分组密码），并且我们希望使用 CTR 模式，同时确保 $IV$ 重复的概率不超过 ${2}^{-32}$。求解 $q^2/2^{3n/4+1} \leq 2^{-32}$ 表明，我们只能安全地加密至多 $q \approx 2^{32}$ 条消息。

We remark further that the proof of security for CTR mode given above assumes $F$ is a pseudorandom function, but in practice $F$ would be instantiated by a block cipher that is a pseudorandom permutation. Although every pseudorandom permutation $F$ (with sufficiently large block length $n$) is also a pseudorandom function (cf. Proposition 3.26), using a pseudorandom permutation incurs a concrete-security loss of roughly $b^{2}/2^{n}$ where $b$ denotes the number of invocations of $F$ overall—e.g., in the case of CTR mode, $b$ would be the total number of plaintext blocks encrypted. Thus, when $b$ is large (even if $q$ is small), the concrete security of CTR mode when using a block cipher may be unacceptably low.

我们进一步指出，上面给出的 CTR 模式的安全性证明假定 $F$ 是一个伪随机函数，但在实践中 $F$ 将由一个作为伪随机置换的分组密码来实例化。尽管每个伪随机置换 $F$（具有足够大的分组长度 $n$）也是一个伪随机函数（参见命题 3.26），但使用伪随机置换会带来大约 $b^{2}/2^{n}$ 的具体安全性损失，其中 $b$ 表示 $F$ 总的调用次数——例如，在 CTR 模式的情况下，$b$ 将是加密的明文分组总数。因此，当 $b$ 很大时（即使 $q$ 很小），使用分组密码的 CTR 模式的具体安全性可能低到不可接受。

IV misuse. In our description and discussion of the various (secure) modes, we have assumed a uniform IV of the appropriate length is chosen each time a message encrypted. What happens when this assumption fails, e.g., due to poor randomness generation or a mistaken implementation? The answer depends on the way the assumption fails, as well as the mode being used.

IV 误用。在我们对各种（安全）模式的描述和讨论中，我们假定每次加密消息时都会选择一个适当长度的均匀 IV。当这个假设不成立时（例如由于随机性生成不佳或实现出错）会发生什么？答案取决于假设不成立的方式以及所使用的模式。

We first look at what happens if an IV repeats. For the "stream-cipher modes" (OFB and CTR), a repeated IV can be catastrophic: it implies that the entire pseudorandom stream (that is XORed with the plaintext) is repeated, which means that by XORing the two ciphertexts using the same IV the attacker learns the XOR of the underlying plaintexts (something we have seen previously is problematic). With CBC mode, however, one expects in practice that although some information is leaked when an IV repeats, the inputs to the block cipher in the two encryptions using the same IV will "diverge" after only a few plaintext blocks, and so the attacker will get no information about the plaintext blocks after that point.

我们首先来看 IV 重复时会发生什么。对于“流密码模式”（OFB 和 CTR），重复的 IV 可能是灾难性的：这意味着整个伪随机流（与明文异或的流）被重复，因此通过异或使用同一 IV 的两个密文，攻击者可以获得底层明文的异或（我们之前已经看到这是有问题的）。然而，对于 CBC 模式，在实践中可以预期，尽管 IV 重复时会泄露一些信息，但在两次使用相同 IV 的加密中，分组密码的输入在仅仅几个明文分组之后就会“发散”，因此攻击者在那之后不会获得关于明文分组的信息。

Next, consider what happens if a scheme does not choose a uniform IV (even if we assume an IV never repeats); as an extreme case, imagine the IV is chosen in such a way that the attacker can predict it in advance—say, the IV is a monotonically increasing counter. CTR mode remains secure in this case, as the proof of security only requires that an IV never repeats. CBC mode, on the other hand, is no longer secure, as we have already discussed in the context of chained CBC mode.

接下来，考虑如果一个方案不选择均匀的 IV 会发生什么（即使我们假设 IV 从不重复）；作为极端情况，想象 IV 以攻击者可以提前预测的方式选择——比如，IV 是一个单调递增的计数器。CTR 模式在这种情况下仍然是安全的，因为安全性证明只要求 IV 从不重复。另一方面，CBC 模式不再安全，正如我们在链式 CBC 模式的上下文中已经讨论的那样。

One way to address potential IV misuse is to use nonce-based encryption, discussed in the following section.

解决潜在 IV 误用的一种方法是使用基于 nonce 的加密，下一节将讨论这一点。

Message tampering. In many texts, modes of operation are also compared based on how well they protect against adversarial modification of the ciphertext. We do not include such a comparison here because the issue of message integrity or message authentication must be dealt with separately from secrecy, and we do so in the next chapter. None of the above modes achieves message integrity in the sense we will define there.

消息篡改。在许多教材中，工作模式也根据它们对抗敌手篡改密文的能力进行比较。我们在这里不包含这样的比较，因为消息完整性或消息认证的问题必须与保密性分开处理，我们将在下一章中处理。上述模式都没有达到我们将在那里定义的意义上的消息完整性。

With regard to the behavior of different modes in the presence of "benign" (i.e., non-adversarial) transmission errors, see Exercises 3.29 and 3.30. In general such errors can be addressed using standard non-cryptographic techniques (e.g., error correction or re-transmission).

关于不同模式在“良性”（即非敌意）传输错误下的行为，见习题 3.29 和 3.30。通常这类错误可以使用标准的非密码学技术（如纠错或重传）来处理。

### 3.6.4 \*Nonce-Based Encryption　3.6.4 \*基于 nonce 的加密

We have so far considered one particular syntax for private-key encryption—namely, Definition 3.7. Here we look at an alternate way of formalizing private-key encryption that is useful in some contexts. Specifically, we consider the notion of `nonce-based` (private-key) `encryption`, where the encryption and decryption algorithms additionally accept a `nonce` as input. (A "nonce" refers to a value that is supposed to be used once, and never repeated.) The syntax of `nonce-based` encryption does not specify where the `nonce` comes from; in practice, the nonce is provided by some higher-level application that must ensure that the same nonce is never used to encrypt more than once—e.g., the nonce may be a counter, or the current time.

到目前为止，我们只考虑了一种特定的私钥加密语法——即定义 3.7。现在我们来看另一种在某些上下文中有用的形式化私钥加密的方式。具体来说，我们考虑**基于 nonce 的（私钥）加密**（nonce-based encryption）的概念，其中加密和解密算法额外接受一个 **nonce** 作为输入。（"nonce"指的是一个只能使用一次、永不重复的值。）基于 nonce 的加密的语法不指定 `nonce` 来自何处；在实践中，nonce 由某个更高级别的应用程序提供，该应用程序必须确保同一个 nonce 永远不会被用于加密超过一次——例如，nonce 可以是一个计数器，或者当前时间。

DEFINITION 3.34 A nonce-based (private-key) encryption scheme consists of probabilistic polynomial-time algorithms (Gen, Enc, Dec) such that:

定义 3.34 一个基于 nonce 的（私钥）加密方案由概率多项式时间算法 (Gen, Enc, Dec) 组成，满足：

1. Gen takes as input ${1}^n$ and outputs a key k with $|k| \geq n$.

   Gen 输入 ${1}^n$，输出一个密钥 $k$，满足 $|k| \geq n$。

2. Enc takes as input a key k, a nonce nonce $\in \{0,1\}^*$, and a message $m \in \{0,1\}^*$, and outputs a ciphertext c.

   Enc 输入密钥 $k$、nonce $\in \{0,1\}^*$ 和消息 $m \in \{0,1\}^*$，输出密文 $c$。

3. Dec takes as input a key $k$, a nonce nonce $\in \{0,1\}^*$, and a ciphertext $c$, and outputs a message $m \in \{0,1\}^*$ or $\perp$.

   Dec 输入密钥 $k$、nonce $\in \{0,1\}^*$ 和密文 $c$，输出消息 $m \in \{0,1\}^*$ 或 $\perp$。

We require that for every $n$, every $k$ output by $\mathsf{Gen}(1^n)$, every $\text{nonce} \in \{0,1\}^*$, and every $m \in \{0,1\}^*$, it holds that $\mathsf{Dec}_k(\text{nonce}, \mathsf{Enc}_k(\text{nonce}, m)) = m$.

我们要求对每个 $n$、每个由 $\mathsf{Gen}(1^n)$ 输出的 $k$、每个 $\text{nonce} \in \{0,1\}^*$ 以及每个 $m \in \{0,1\}^*$，都有 $\mathsf{Dec}_k(\text{nonce}, \mathsf{Enc}_k(\text{nonce}, m)) = m$。

Some nonce-based encryption schemes only support nonces of a specific length; all the definitions we discuss can be adapted easily to that case.

一些基于 nonce 的加密方案只支持特定长度的 nonce；我们讨论的所有定义都可以很容易地适用于这种情况。

Security for nonce-based encryption can be defined by suitably adapting any of the definitions we have seen before; for concreteness, we adapt the notion of CPA-security for multiple encryptions (Definition 3.22). The experiment we consider here is conceptually the same as the one considered in that earlier definition, and in particular we again provide the attacker with access to a "left-or-right" oracle that accepts two messages and encrypts either the "left" or "right" message. The difference here is that we also allow the attacker to specify the nonce used during encryption, subject to the constraint that the attacker may never repeat a nonce.

基于 nonce 的加密的安全性可以通过适当改造我们之前见过的任何一个定义来定义；为具体起见，我们对多重加密的 CPA 安全概念（定义 3.22）加以改造。我们这里考虑的实验在概念上与之前那个定义中所考虑的实验相同，特别是我们再次向攻击者提供对“左右”预言机的访问，该预言机接受两条消息并加密“左”消息或“右”消息。这里的区别在于，我们还允许攻击者指定加密时使用的 nonce，约束条件是攻击者不得重复使用 nonce。

In the following experiment, the left-or-right oracle $\mathsf{LR}_{k,b}(\cdot,\cdot,\cdot)$ takes three inputs; $\mathsf{LR}_{k,b}(\mathsf{nonce}, m_0, m_1)$ computes $c \leftarrow \mathsf{Enc}_k(\mathsf{nonce}, m_b)$ and returns $c$. For any nonce-based encryption scheme $\Pi$, adversary $\mathcal{A}$, and security parameter $n$ we define the following experiment:

在下面的实验中，左右预言机 $\mathsf{LR}_{k,b}(\cdot,\cdot,\cdot)$ 接受三个输入；$\mathsf{LR}_{k,b}(\mathsf{nonce}, m_0, m_1)$ 计算 $c \leftarrow \mathsf{Enc}_k(\mathsf{nonce}, m_b)$ 并返回 $c$。对于任何基于 nonce 的加密方案 $\Pi$、敌手 $\mathcal{A}$ 和安全参数 $n$，我们定义以下实验：

The nonce-based LR-oracle experiment $\mathsf{PrivK}_{\mathcal{A},\Pi}^{\mathsf{LR-ncpa}}(n)$:

基于 nonce 的 LR 预言机实验 $\mathsf{PrivK}_{\mathcal{A},\Pi}^{\mathsf{LR-ncpa}}(n)$：

1. A key k is generated by running $\mathsf{Gen}(1^{n})$.

   通过运行 $\mathsf{Gen}(1^{n})$ 生成密钥 $k$。

2. A uniform bit $b \in \{0,1\}$ is chosen.

   选择一个均匀比特 $b \in \{0,1\}$。

3. The adversary $\mathcal{A}$ is given ${1}^n$ and oracle access to $\mathsf{LR}_{k,b}(\cdot,\cdot,\cdot)$. The adversary is not allowed to repeat the first input in any of its queries to the oracle.

   敌手 $\mathcal{A}$ 获得 ${1}^n$ 和对 $\mathsf{LR}_{k,b}(\cdot,\cdot,\cdot)$ 的预言机访问。敌手不得在其对预言机的任何查询中重复第一个输入。

4. The adversary A outputs a bit b'.

   敌手 $\mathcal{A}$ 输出一个比特 $b'$。

5. The output of the experiment is defined to be 1 if $b^{\prime} = b$, in which case we say that A succeeds.

   如果 $b^{\prime} = b$，实验输出定义为 1，此时我们说 A 成功。

The definition of security is the same as usual, except that it now refers to the above experiment.

安全性的定义与通常相同，只是现在它指的是上述实验。

DEFINITION 3.35 A nonce-based private-key encryption scheme $\Pi$ is CPA-secure for multiple encryptions if for all probabilistic polynomial-time adversaries A there is a negligible function $\mathsf{negl}$ such that

定义 3.35 一个基于 nonce 的私钥加密方案 $\Pi$ 称为对于多重加密是 CPA 安全的，如果对所有概率多项式时间敌手 A，存在一个可忽略函数 $\mathsf{negl}$ 使得

$$\Pr\left[\mathsf{PrivK}_{\mathcal{A},\Pi}^{\mathsf{LR-ncpa}}(n)=1\right]\leq\frac{1}{2}+\mathsf{negl}(n),$$

where the probability is taken over the randomness used by $\mathcal{A}$ and the randomness used in the experiment.

其中概率取自 $\mathcal{A}$ 使用的随机性和实验中使用的随机性。

Because "CPA-security" and "CPA-security for multiple encryptions" are equivalent definitions (since an analogue of Theorem 3.23 can be shown for nonce-based encryption as well), we refer simply to CPA-security for brevity.

由于“CPA 安全性”和“多重加密的 CPA 安全性”是等价的定义（因为定理 3.23 的类似结论也可以对基于 nonce 的加密证明），为简洁起见，我们简称为 CPA 安全。

CPA-secure nonce-based encryption. It is easy to modify CTR mode to obtain a CPA-secure nonce-based encryption scheme: when encrypting, the IV is now set equal to the nonce that is provided as input, rather than being chosen uniformly. CPA-security can be shown exactly as in the proof of Theorem 3.33, using the fact that in this context repeat cannot occur (since the adversary is disallowed from repeating a nonce). Indeed, the concrete-security bound obtained here is better than what is obtained in the proof of Theorem 3.33 precisely because here repeat cannot occur. Of course, this is predicated on the assumption that the application using the encryption scheme ensures that nonces never repeat.

CPA 安全的基于 nonce 的加密。只需对 CTR 模式稍作修改，即可得到 CPA 安全的基于 nonce 的加密方案：加密时，IV 不再均匀随机选取，而是直接设置为作为输入提供的 nonce。CPA 安全性可以完全按照定理 3.33 证明中的方式证得，利用的是在这种情况下重复不可能发生（因为禁止敌手重复使用 nonce）这一事实。事实上，这里得到的具体安全性界之所以优于定理 3.33 证明中得到的界，正是因为这里重复不可能发生。当然，这依赖于使用该加密方案的应用程序确保 nonce 永不重复这一前提。

We see that a nonce-based encryption scheme can be CPA-secure even though it is deterministic. This does not contradict Theorem 3.20, since here we are considering an alternate syntax for encryption.

我们看到，基于 nonce 的加密方案即使是确定性的也可以是 CPA 安全的。这与定理 3.20 并不矛盾，因为这里我们考虑的是加密的另一种语法。

Advantages of nonce-based encryption. One may wonder what is gained by using nonce-based encryption, in particular since any nonce-based encryption scheme can be converted to a "standard" encryption scheme by simply choosing the nonce at random. There are several answers to this question.

基于 nonce 的加密的优势。人们可能会好奇使用基于 nonce 的加密有什么好处，特别是因为任何基于 nonce 的加密方案都可以通过简单地随机选取 nonce 来转换为“标准”加密方案。这个问题有几个答案。

First of all, CPA-secure nonce-based encryption is useful in settings where generating high-quality randomness is expensive or impossible. It may be much easier in such cases to use a counter as a nonce rather than to generate a nonce uniformly.

首先，CPA 安全的基于 nonce 的加密在生成高质量随机性成本高昂或不可能的环境中很有用。在这种情况下，使用计数器作为 nonce 可能比均匀生成 nonce 容易得多。

Somewhat similarly, there may be settings where using a short nonce is appropriate, e.g., when only very few messages will be encrypted. In such scenarios, choosing the nonce uniformly may result in a repeated nonce with probability that is unacceptably high.

类似地，可能存在使用短 nonce 合适的场景，例如当只有很少的消息需要加密时。在这种情况下，均匀选择 nonce 可能导致 nonce 重复的概率高到不可接受。

Finally, we have already observed that tighter concrete-security bounds can sometimes be obtained by enforcing non-repeating nonces rather than by choosing a uniform nonce.

最后，我们已经观察到，通过强制 nonce 不重复而不是选择均匀的 nonce，有时可以获得更紧的具体安全性界。

### References and Additional Reading　参考文献与补充阅读

The modern computational approach to cryptography was initiated in a groundbreaking paper by Goldwasser and Micali [87]. That paper introduced the notion of semantic security, and showed how that goal could be achieved in the setting of public-key encryption (see Chapters 11 and 12). The paper also proposed the notion of indistinguishability (cf. Definition 3.8), and showed that it implies semantic security. The converse was shown later [142]. Goldreich's book [83] contains further discussion of semantic security.

现代密码学中的计算性方法始于 Goldwasser 和 Micali 的一篇开创性论文 [87]。该论文引入了语义安全（semantic security）的概念，并展示了如何在公钥加密环境中实现这一目标（见第 11 章和第 12 章）。该论文还提出了不可区分性（indistinguishability）的概念（参见定义 3.8），并证明了它蕴含语义安全。反向蕴含是后来才被证明的 [142]。Goldreich 的著作 [83] 包含了对语义安全的进一步讨论。

Blum and Micali [41] introduced the notion of pseudorandom generators and proved their existence based on a specific, number-theoretic assumption. In the same work, they also pointed out the connection between pseudorandom generators and private-key encryption as in Construction 3.17. The definition of pseudorandom generators given by Blum and Micali is different from the definition we use in this book (Definition 3.14); the latter definition originates in the work of Yao [205], who showed equivalence of the two formulations. Yao also showed constructions of pseudorandom generators based on general assumptions; we explore this topic in Chapter 8.

Blum 和 Micali [41] 引入了伪随机生成器的概念，并基于特定的数论假设证明了它们的存在性。在同一工作中，他们还指出了伪随机生成器与构造 3.17 中私钥加密之间的联系。Blum 和 Micali 给出的伪随机生成器定义不同于本书使用的定义（定义 3.14）；后一定义源于 Yao [205] 的工作，Yao 证明了这两种表述的等价性。Yao 还展示了基于一般假设的伪随机生成器构造；我们在第 8 章中探讨这个主题。

Formal definitions of security against chosen-plaintext attacks were given by Luby [131] and Bellare et al. [17]. See the work of Katz and Yung [112] for other notions of security for private-key encryption.

针对选择明文攻击的安全性的形式化定义由 Luby [131] 和 Bellare 等人 [17] 给出。关于私钥加密的其他安全概念，见 Katz 和 Yung [112] 的工作。

Pseudorandom functions were defined and constructed by Goldreich et al. [85], and their application to encryption was demonstrated in subsequent work by the same authors [84]. Pseudorandom permutations and strong pseudorandom permutations were studied by Luby and Rackoff [132]. These ideas are covered in Chapter 8. Stream ciphers and block ciphers had been used for many years before they began to be studied in the theoretical sense initiated by the above works. Practical constructions of stream ciphers and block ciphers are studied in Chapter 7.

伪随机函数由 Goldreich 等人 [85] 定义和构造，其在加密中的应用由同一批作者在后续工作 [84] 中展示。伪随机置换和强伪随机置换由 Luby 和 Rackoff [132] 研究。这些思想将在第 8 章中介绍。在上述工作所开启的理论研究出现之前，流密码和分组密码已被使用多年。流密码和分组密码的实际构造将在第 7 章中研究。

The ECB, CBC, and OFB modes of operation (as well as CFB, a mode of operation not covered here) were standardized along with the DES block cipher [148]. CTR mode was standardized by NIST in 2001. CBC and CTR modes were proven CPA-secure by Bellare et al. [17]. The attack on chained CBC was first described by Rogaway (unpublished), and was used to attack SSL/TLS in the so-called "BEAST attack" by Duong and Rizzo. Nonce-based encryption was first explicitly highlighted by Rogaway [172].

ECB、CBC 和 OFB 工作模式（以及 CFB，一种这里未涵盖的工作模式）与 DES 分组密码 [148] 一起被标准化。CTR 模式由 NIST 于 2001 年标准化。CBC 和 CTR 模式由 Bellare 等人 [17] 证明是 CPA 安全的。对链式 CBC 的攻击首次由 Rogaway 描述（未发表），并后来由 Duong 和 Rizzo 在所谓的“BEAST 攻击”中用于攻击 SSL/TLS。基于 nonce 的加密首次由 Rogaway [172] 明确强调。

### Exercises　习题

3.1 Prove Proposition 3.6.

3.1 证明命题 3.6。

3.2 Prove that Definition 3.8 cannot be satisfied if $\Pi$ can encrypt arbitrary-length messages and the adversary is not restricted to outputting equal-length messages in experiment $\mathsf{PrivK}_{\mathcal{A},\Pi}^{\mathsf{eav}}$.

3.2 证明如果 $\Pi$ 可以加密任意长度消息，且敌手在实验 $\mathsf{PrivK}_{\mathcal{A},\Pi}^{\mathsf{eav}}$ 中不受限于输出等长消息，则定义 3.8 无法满足。

Hint: Let $q(n)$ be a polynomial upper-bound on the length of the cipher-text when $\Pi$ is used to encrypt a single bit. Then consider an adversary who outputs $m_0 \in \{0,1\}$ and a uniform $m_1 \in \{0,1\}^{q(n)+2}$.

提示：令 $q(n)$ 为使用 $\Pi$ 加密单个比特时密文长度的多项式上界。然后考虑一个输出 $m_0 \in \{0,1\}$ 和均匀的 $m_1 \in \{0,1\}^{q(n)+2}$ 的敌手。

3.3 Say $\Pi = (\mathrm{Gen}, \mathrm{Enc}, \mathrm{Dec})$ is such that for $k \in \{0,1\}^n$, algorithm $\mathrm{Enc}_k$ is only defined for messages of length at most $\ell(n)$ (for some polynomial $\ell$). Construct a scheme satisfying Definition 3.8 even when the adversary is not restricted to outputting equal-length messages in $\mathrm{PrivK}_{\mathcal{A},\Pi}^{\mathrm{eav}}$

3.3 设 $\Pi = (\mathrm{Gen}, \mathrm{Enc}, \mathrm{Dec})$ 使得对于 $k \in \{0,1\}^n$，算法 $\mathrm{Enc}_k$ 仅对长度不超过 $\ell(n)$ 的消息有定义（对于某个多项式 $\ell$）。构造一个满足定义 3.8 的方案，即使敌手在 $\mathrm{PrivK}_{\mathcal{A},\Pi}^{\mathrm{eav}}$ 中不受限于输出等长消息。

3.4 Prove the equivalence of Definition 3.8 and Definition 3.9.

3.4 证明定义 3.8 和定义 3.9 的等价性。

3.5 Define $G(s) \stackrel{\mathrm{def}}{=} s\|s$ (where "$\|$" denotes concatenation). Describe and analyze an attack showing that $G$ is not a pseudorandom generator.

3.5 定义 $G(s) \stackrel{\mathrm{def}}{=} s\|s$（其中"$\|$"表示连接）。描述并分析一个攻击，证明 $G$ 不是伪随机生成器。

3.6 Let G be a pseudorandom generator. In each of the following cases, say whether $G^{\prime}$ is necessarily a pseudorandom generator. If yes, give a proof; if not, show a counterexample.

3.6 设 G 是一个伪随机生成器。在以下每种情况下，判断 $G^{\prime}$ 是否必然是一个伪随机生成器。如果是，给出证明；如果不是，给出反例。

(a) Define $G^{\prime}(s) \stackrel{\mathrm{def}}{=} G(\bar{s})$, where $\bar{s}$ is the complement of s.

(a) 定义 $G^{\prime}(s) \stackrel{\mathrm{def}}{=} G(\bar{s})$，其中 $\bar{s}$ 是 s 的补。

(b) Define $G^{\prime}(s) \stackrel{\mathrm{def}}{=} \overline{G(s)}.$

(b) 定义 $G^{\prime}(s) \stackrel{\mathrm{def}}{=} \overline{G(s)}.$

(c) Define $G^{\prime}(s) \stackrel{\mathrm{def}}{=} G(0^{|s|}\|s)$.

(c) 定义 $G^{\prime}(s) \stackrel{\mathrm{def}}{=} G(0^{|s|}\|s)$。

(d) Define $G^{\prime}(s) \stackrel{\mathrm{def}}{=} G(s) \parallel G(s+1)$.

(d) 定义 $G^{\prime}(s) \stackrel{\mathrm{def}}{=} G(s) \parallel G(s+1)$。

3.7 Let $|G(s)| = \ell(|s|)$ for some $\ell$. Consider the following experiment:

3.7 设对某个 $\ell$ 有 $|G(s)| = \ell(|s|)$。考虑以下实验：

The PRG indistinguishability experiment PRG_{A,G}(n):

PRG 不可区分性实验 PRG_{A,G}(n)：

(a) A uniform bit $b \in \{0,1\}$ is chosen. If b = 0 then choose a uniform $r \in \{0,1\}^{\ell(n)}$; if b = 1 then choose a uniform $s \in \{0,1\}^{n}$ and set $r := G(s)$.

(a) 选择一个均匀比特 $b \in \{0,1\}$。如果 b = 0，则选择一个均匀的 $r \in \{0,1\}^{\ell(n)}$；如果 b = 1，则选择一个均匀的 $s \in \{0,1\}^{n}$ 并设 $r := G(s)$。

(b) The adversary A is given r, and outputs a bit b'.

(b) 敌手 $\mathcal{A}$ 获得 $r$，并输出一个比特 $b'$。

(c) The output of the experiment is defined to be 1 if $b^{\prime} = b$, and 0 otherwise.

(c) 如果 $b^{\prime} = b$，实验输出定义为 1，否则为 0。

Provide a definition of a pseudorandom generator based on this experiment, and prove that your definition is equivalent to Definition 3.14. (That is, show that $G$ satisfies your definition if and only if it satisfies Definition 3.14.)

基于此实验给出伪随机生成器的定义，并证明你的定义与定义 3.14 等价。（即证明 $G$ 满足你的定义当且仅当它满足定义 3.14。）

3.8 Prove the converse of Theorem 3.16. Namely, show that if G is not a pseudorandom generator then Construction 3.17 does not have indistinguishable encryptions in the presence of an eavesdropper.

3.8 证明定理 3.16 的逆命题。即证明如果 G 不是伪随机生成器，那么构造 3.17 在窃听者存在的情况下不具有不可区分加密。

3.9 Consider a notion of indistinguishable encryption for multiple distinct messages, i.e., where a scheme need not hide whether the same message is encrypted twice.

3.9 考虑一种针对多个不同消息的不可区分加密概念，即方案不需要隐藏同一消息是否被加密两次。

(a) Modify Definition 3.18 to obtain a suitable definition of the above.

(a) 修改定义 3.18 以获得上述概念的适当定义。

(b) Show that Construction 3.17 does not satisfy your definition.

(b) 证明构造 3.17 不满足你的定义。

(c) Give a construction of a deterministic (stateless) encryption scheme that satisfies your definition.

(c) 给出一个满足你的定义的确定性（无状态）加密方案的构造。

3.10 Prove unconditionally the existence of a pseudorandom function $F : \{0,1\}^* \times \{0,1\}^* \to \{0,1\}$ with $\ell_{key}(n) = n$ and $\ell_{in}(n) = \log n$.

3.10 无条件证明存在一个伪随机函数 $F : \{0,1\}^* \times \{0,1\}^* \to \{0,1\}$，其中 $\ell_{key}(n) = n$ 且 $\ell_{in}(n) = \log n$。

Hint: Implement a uniform function with logarithmic input length.

提示：实现一个具有对数输入长度的均匀函数。

3.11 Let $F$ be a length preserving pseudorandom function. For the following constructions of a keyed function $F^{\prime}: \{0,1\}^n \times \{0,1\}^{n-1} \to \{0,1\}^{2n}$, state whether $F^{\prime}$ is a pseudorandom function. If yes, prove it; if not, show an attack.

3.11 设 $F$ 是一个长度保持的伪随机函数。对于以下带密钥函数 $F^{\prime}: \{0,1\}^n \times \{0,1\}^{n-1} \to \{0,1\}^{2n}$ 的构造，判断 $F^{\prime}$ 是否是伪随机函数。如果是，给出证明；如果不是，给出攻击。

$$\mathrm{(a)}F^{\prime}_{k}(x)\stackrel{\mathrm{def}}{=}F_{k}(0\|x)\parallel F_{k}(0\|x).$$

(b) $F^{\prime}_k(x) \stackrel{\mathrm{def}}{=} F_k(0\|x)\|F_k(1\|x).$

$$\mathrm{(c)}F^{\prime}_{k}(x)\stackrel{\mathrm{def}}{=}F_{k}(0\|x)\parallel F_{k}(x\|0).$$

(d) $F^{\prime}_k(x) \stackrel{\mathrm{def}}{=} F_k(0\|x) \| F_k(x\|1).$

3.12 Assuming the existence of pseudorandom functions, prove that there is an encryption scheme that has indistinguishable multiple encryptions in the presence of an eavesdropper (i.e., satisfies Definition 3.18), but is not CPA-secure (i.e., does not satisfy Definition 3.21).

3.12 假设伪随机函数存在，证明存在一个加密方案，它在窃听者存在的情况下具有不可区分的多次加密（即满足定义 3.18），但不是 CPA 安全的（即不满足定义 3.21）。

Hint: The scheme need not be "natural." You will need to use the fact that in a chosen-plaintext attack the adversary can choose its queries to the encryption oracle adaptively.

提示：该方案不必是“自然的”。你需要利用在选择明文攻击中敌手可以自适应地选择其对加密预言机的查询这一事实。

3.13 Let F be a keyed function and consider the following experiment:

3.13 设 F 是一个带密钥的函数，考虑以下实验：

**The PRF indistinguishability experiment PRF_{A,F}(n):**

**PRF 不可区分性实验 PRF_{A,F}(n)：**

(a) A uniform $b \in \{0,1\}$ is chosen. If b = 0, choose uniform $f \in \mathsf{Func}_n$; if b = 1, choose uniform $k \in \{0,1\}^n$.

(a) 选择一个均匀的 $b \in \{0,1\}$。如果 b = 0，选择均匀的 $f \in \mathsf{Func}_n$；如果 b = 1，选择均匀的 $k \in \{0,1\}^n$。

(b) $\mathcal{A}$ is given ${1}^{n}$ as input. If $b = 0$ then $\mathcal{A}$ is given access to $f(\cdot)$. If $b = 1$ then $\mathcal{A}$ is given access to $F_{k}(\cdot)$.

(b) $\mathcal{A}$ 获得输入 ${1}^{n}$。如果 $b = 0$，则 $\mathcal{A}$ 获得对 $f(\cdot)$ 的访问。如果 $b = 1$，则 $\mathcal{A}$ 获得对 $F_{k}(\cdot)$ 的访问。

(c) A outputs a bit b'.

(c) $\mathcal{A}$ 输出一个比特 $b'$。

(d) The output of the experiment is defined to be 1 if $b^{\prime} = b$, and 0 otherwise.

(d) 如果 $b^{\prime} = b$，实验输出定义为 1，否则为 0。

Define pseudorandom functions using this experiment, and prove that your definition is equivalent to Definition 3.24.

使用此实验定义伪随机函数，并证明你的定义与定义 3.24 等价。

3.14 Define the keyed function $F$ as $F_k(x) \stackrel{\mathrm{def}}{=} k \& x$, where "&" denotes bitwise AND. Describe and analyze an attack showing that $F$ is not a pseudorandom function.

3.14 定义带密钥的函数 $F$ 为 $F_k(x) \stackrel{\mathrm{def}}{=} k \& x$，其中"&"表示按位与。描述并分析一个攻击，证明 $F$ 不是伪随机函数。

3.15 Consider the following keyed function $F$: For security parameter $n$, the key is an $n \times n$ boolean matrix $A$ and an $n$-bit boolean vector $b$. Define $F_{A,b} : \{0,1\}^{n} \to \{0,1\}^{n}$ by $F_{A,b}(x) \stackrel{\mathrm{def}}{=} Ax + b$, where all operations are done modulo 2. Show that $F$ is not a pseudorandom function.

3.15 考虑以下带密钥的函数 $F$：对于安全参数 $n$，密钥是一个 $n \times n$ 布尔矩阵 $A$ 和一个 $n$ 比特布尔向量 $b$。定义 $F_{A,b} : \{0,1\}^{n} \to \{0,1\}^{n}$ 为 $F_{A,b}(x) \stackrel{\mathrm{def}}{=} Ax + b$，其中所有运算在模 2 下进行。证明 $F$ 不是伪随机函数。

3.16 Prove that if $F$ is a length preserving pseudorandom function, then $G(s) \overset{\mathrm{def}}{=} F_s(\langle 1 \rangle) \| F_s(\langle 2 \rangle) \| \cdots \| F_s(\langle \ell \rangle)$, where $\langle i \rangle$ is the $n$-bit encoding of $i$, is a pseudorandom generator with expansion factor $\ell \cdot n$.

3.16 证明如果 $F$ 是一个长度保持的伪随机函数，那么 $G(s) \overset{\mathrm{def}}{=} F_s(\langle 1 \rangle) \| F_s(\langle 2 \rangle) \| \cdots \| F_s(\langle \ell \rangle)$（其中 $\langle i \rangle$ 是 $i$ 的 $n$ 比特编码）是一个扩展因子为 $\ell \cdot n$ 的伪随机生成器。

3.17 Assume pseudorandom permutations exist. Show that there exists a keyed function $F$ that is a pseudorandom permutation but is not a strong pseudorandom permutation.

3.17 假设伪随机置换存在。证明存在一个带密钥的函数 $F$ 是伪随机置换但不是强伪随机置换。

Hint: Construct $F$ such that $F_k(k) = 0^{|k|}$.

提示：构造 $F$ 使得 $F_k(k) = 0^{|k|}$。

3.18 Define a notion of perfect secrecy against chosen-plaintext attacks by adapting Definition 3.21. Show that the definition cannot be achieved.

3.18 通过修改定义 3.21 来定义针对选择明文攻击的完美保密概念。证明该定义无法实现。

3.19 Let $F$ be a pseudorandom permutation, and define a fixed-length encryption scheme (Enc, Dec) as follows: On input a key $k \in \{0,1\}^n$ and message $m \in \{0,1\}^{n/2}$, algorithm $\mathsf{Enc}$ chooses a uniform string $r \in \{0,1\}^{n/2}$ and computes $c := F_k(r\|m)$.

3.19 设 $F$ 是一个伪随机置换，定义如下的定长加密方案 (Enc, Dec)：输入密钥 $k \in \{0,1\}^n$ 和消息 $m \in \{0,1\}^{n/2}$，算法 $\mathsf{Enc}$ 选择一个均匀串 $r \in \{0,1\}^{n/2}$ 并计算 $c := F_k(r\|m)$。

Show how to decrypt, and prove that this scheme is CPA-secure for messages of length $n/2$.

说明如何解密，并证明该方案对于长度为 $n/2$ 的消息是 CPA 安全的。

3.20 Let $F$ be a length preserving pseudorandom function and $G$ be a pseudorandom generator with expansion factor $\ell(n) = n+1$. For each of the following encryption schemes, state whether the scheme is EAV-secure and whether it is CPA-secure. (In each case, the shared key is a uniform $k \in \{0,1\}^n$.) Explain your answer in each case.

3.20 设 $F$ 是一个长度保持的伪随机函数，$G$ 是一个扩展因子为 $\ell(n) = n+1$ 的伪随机生成器。对于以下每个加密方案，说明该方案是否是 EAV 安全的以及是否是 CPA 安全的。（在每种情况下，共享密钥是一个均匀的 $k \in \{0,1\}^n$。）对每种情况解释你的答案。

(a) To encrypt $m \in \{0,1\}^{n+1}$, choose uniform $r \in \{0,1\}^n$ and output the ciphertext $\langle r, G(r) \oplus m \rangle$.

(a) 要加密 $m \in \{0,1\}^{n+1}$，选择均匀的 $r \in \{0,1\}^n$ 并输出密文 $\langle r, G(r) \oplus m \rangle$。

(b) To encrypt $m \in \{0,1\}^n$, output the ciphertext $m \oplus F_k(0^n)$.

(b) 要加密 $m \in \{0,1\}^n$，输出密文 $m \oplus F_k(0^n)$。

(c) To encrypt $m \in \{0,1\}^{2n}$, parse $m$ as $m_1\|m_2$ with $|m_1| = |m_2|$, then choose uniform $r \in \{0,1\}^n$ and send $\langle r, m_1 \oplus F_k(r), m_2 \oplus F_k(r+1) \rangle$.

(c) 要加密 $m \in \{0,1\}^{2n}$，将 $m$ 解析为 $m_1\|m_2$，其中 $|m_1| = |m_2|$，然后选择均匀的 $r \in \{0,1\}^n$ 并发送 $\langle r, m_1 \oplus F_k(r), m_2 \oplus F_k(r+1) \rangle$。

3.21 Let $\Pi$ denote Construction 3.28 instantiated with the keyed function from Example 3.25. Describe and analyze an attack showing that $\Pi$ is not CPA-secure.

3.21 令 $\Pi$ 表示用示例 3.25 中的带密钥函数实例化的构造 3.28。描述并分析一个攻击，证明 $\Pi$ 不是 CPA 安全的。

3.22 Give a formal definition of CPA-security for stateful encryption, and prove that the synchronized stream-cipher mode of operation satisfies your definition if the underlying stream cipher is secure.

3.22 给出有状态加密的 CPA 安全性的形式化定义，并证明如果底层流密码是安全的，同步流密码工作模式满足你的定义。

3.23 Prove that the unsynchronized stream-cipher mode of operation (Construction 3.31) is CPA-secure if the underlying stream cipher is secure.

3.23 证明如果底层流密码是安全的，非同步流密码工作模式（构造 3.31）是 CPA 安全的。

3.24 Let F be a pseudorandom function, and consider the following construction of a stream cipher accepting an n-bit initialization vector:

3.24 设 F 是一个伪随机函数，考虑以下接受 n 比特初始化向量的流密码构造：

- $\operatorname{Init}(s, IV)$ outputs st = (s, IV).

  $\operatorname{Init}(s, IV)$ 输出 st = (s, IV)。

- $\operatorname{Next}(s, IV)$ outputs $y := F_s(IV)$ and $\mathrm{st}^{\prime} = (s, IV + 1)$.

  $\operatorname{Next}(s, IV)$ 输出 $y := F_s(IV)$ 和 $\mathrm{st}^{\prime} = (s, IV + 1)$。

Show that this stream cipher is not secure.

证明该流密码是不安全的。

3.25 Let $F$ be a pseudorandom permutation. Consider the mode of operation in which a uniform value $IV \in \{0,1\}^n$ is chosen, and the $i$th ciphertext block $c_i$ is computed as $c_i := F_k(IV + i + m_i)$, where addition is modulo ${2}^n$. Show that this scheme is not EAV-secure.

3.25 设 $F$ 是一个伪随机置换。考虑一种工作模式，其中选择一个均匀值 $IV \in \{0,1\}^n$，第 $i$ 个密文分组 $c_i$ 计算为 $c_i := F_k(IV + i + m_i)$，其中加法在模 ${2}^n$ 下进行。证明该方案不是 EAV 安全的。

3.26 Say CBC-mode encryption is used with a block cipher having a 256-bit key and 128-bit block length to encrypt a 1024-bit message. What is the length of the resulting ciphertext?

3.26 假设使用 CBC 模式加密，分组密码具有 256 比特密钥和 128 比特分组长度，要加密一条 1024 比特的消息。所得密文的长度是多少？

3.27 Give the details of the proof by reduction of Equation (3.13).

3.27 给出式 (3.13) 的归约证明的细节。

3.28 For any function $g : \{0,1\}^n \to \{0,1\}^n$, define $g^{\$}(\cdot)$ to be a probabilistic oracle that, on input ${1}^n$, chooses uniform $r \in \{0,1\}^n$ and returns $\langle r, g(r) \rangle$. A keyed function $F$ is a weak pseudorandom function if for all PPT algorithms $D$, there exists a negligible function $\mathsf{negl}$ such that:

3.28 对于任意函数 $g : \{0,1\}^n \to \{0,1\}^n$，定义 $g^{\$}(\cdot)$ 为一个概率预言机，它在输入 ${1}^n$ 时选择均匀的 $r \in \{0,1\}^n$ 并返回 $\langle r, g(r) \rangle$。一个带密钥的函数 $F$ 称为**弱伪随机函数**（weak pseudorandom function），如果对于所有 PPT 算法 $D$，存在一个可忽略函数 $\mathsf{negl}$ 使得：

$$\left|\Pr[D^{F_{k}^{\$}(\cdot)}(1^{n})=1]-\Pr[D^{f^{\$}(\cdot)}(1^{n})=1]\right|\leq\mathsf{negl}(n),$$

where $k \in \{0,1\}^n$ and $f \in \mathsf{Func}_n$ are chosen uniformly.

其中 $k \in \{0,1\}^n$ 和 $f \in \mathsf{Func}_n$ 是均匀选择的。

(a) Prove that if $F$ is pseudorandom then it is weakly pseudorandom.

(a) 证明如果 $F$ 是伪随机的，那么它是弱伪随机的。

(b) Let $F^{\prime}$ be a pseudorandom function, and define

(b) 设 $F^{\prime}$ 是一个伪随机函数，定义

$$F_{k}(x)\stackrel{\mathrm{def}}{=}\begin{cases}F_{k}^{\prime}(x) & \text{if } x \text{ is even}\\ F_{k}^{\prime}(x+1) & \text{if } x \text{ is odd.}\end{cases}$$

Prove that F is weakly pseudorandom, but not pseudorandom.

证明 F 是弱伪随机的，但不是伪随机的。

(c) Is CTR-mode encryption using a weak pseudorandom function necessarily CPA-secure? Prove your answer.

(c) 使用弱伪随机函数的 CTR 模式加密是否必然是 CPA 安全的？证明你的答案。

(d) Prove that Construction 3.28 is CPA-secure if F is a weak pseudo-random function.

(d) 证明如果 F 是弱伪随机函数，构造 3.28 是 CPA 安全的。

3.29 What is the effect of a single bit flip in the ciphertext when using the CBC, OFB, and CTR modes of operation?

3.29 使用 CBC、OFB 和 CTR 工作模式时，密文中的单个比特翻转会产生什么影响？

3.30 What is the effect of a dropped ciphertext block (e.g., if the transmitted ciphertext $c_1, c_2, c_3, \ldots$ is received as $c_1, c_3, \ldots$) when using the CBC, OFB, and CTR modes of operation?

3.30 使用 CBC、OFB 和 CTR 工作模式时，丢失一个密文分组（例如，传输的密文 $c_1, c_2, c_3, \ldots$ 被接收为 $c_1, c_3, \ldots$）会产生什么影响？

3.31 Consider a variant of CTR mode where a uniform $IV \in \{0,1\}^n$ is chosen and the $i$th ciphertext block is computed as $c_i := m_i \oplus F_k(IV + i)$. Prove that this variant is CPA-secure. What concrete-security bound do you obtain?

3.31 考虑 CTR 模式的一个变体，其中选择一个均匀的 $IV \in \{0,1\}^n$，第 $i$ 个密文分组计算为 $c_i := m_i \oplus F_k(IV + i)$。证明该变体是 CPA 安全的。你得到了什么具体安全性界？

3.32 Show that the scheme from Exercise 3.31 is not secure as a nonce-based encryption scheme if the nonce is used as the IV.

3.32 证明如果使用 nonce 作为 IV，习题 3.31 中的方案作为基于 nonce 的加密方案是不安全的。

3.33 Show that CBC mode is not secure as a nonce-based encryption scheme if the nonce is used as the IV.

3.33 证明如果使用 nonce 作为 IV，CBC 模式作为基于 nonce 的加密方案是不安全的。
