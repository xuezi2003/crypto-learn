# 附录 A：数学基础

> 本文件为 KL《Introduction to Modern Cryptography (3rd ed.)》官方附录 A（Mathematical Background）的纯中文译文，编号与公式均与原文一致。
> 注：带 \* 号的章节为教材标记的选读内容，首次阅读时可跳过。

## A.1 恒等式与不等式

我们列出全书各处会用到的若干标准恒等式与不等式。

**定理 A.1**（二项式展开定理）设 $x, y$ 为实数，$n$ 为正整数，则

$$
(x+y)^{n}=\sum_{i=0}^{n}\binom{n}{i}x^{i}y^{n-i}.
$$

**命题 A.2** 对所有 $x \geq 1$，有 $(1 - 1/x)^x \leq e^{-1}$。

**命题 A.3** 对所有 x，有 ${1} - x \leq e^{-x}$。

**命题 A.4** 对所有满足 ${0} \leq x \leq 1$ 的 x，有

$$
e^{-x}\leq1-\left(1-\frac{1}{e}\right)\cdot x\leq1-\frac{x}{2}.
$$

## A.2 渐近记号

我们使用标准记号来表示函数的渐近行为。

**定义 A.5** 设 $f(n)$、$g(n)$ 是从非负整数到非负实数的函数。则：

- $f(n) = \mathcal{O}(g(n))$ 表示存在正整数 $c$ 和 $n^{\prime}$，使得对所有 $n > n^{\prime}$，有 $f(n) \leq c \cdot g(n)$。

- $f(n) = \Omega(g(n))$ 表示存在正整数 $c$ 和 $n^{\prime}$，使得对所有 $n > n^{\prime}$，有 $f(n) \geq c \cdot g(n)$。

- $f(n) = \Theta(g(n))$ 表示存在正整数 $c_1, c_2$ 和 $n^{\prime}$，使得对所有 $n > n^{\prime}$，有 $c_1 \cdot g(n) \leq f(n) \leq c_2 \cdot g(n)$。

- $f(n) = o(g(n))$ 表示 $\lim_{n \to \infty} \frac{f(n)}{g(n)} = 0$。

- $f(n) = \omega(g(n))$ 表示 $\lim_{n \to \infty} \frac{f(n)}{g(n)} = \infty$。

**例 A.6**

设 $f(n) = n^{4} + 3n + 500$。则：

- $f(n) = \mathcal{O}(n^4).$

- $f(n) = \mathcal{O}(n^5)$。事实上，$f(n) = o(n^5)$。

- $f(n) = \Omega(n^3 \log n)$。事实上，$f(n) = \omega(n^3 \log n)$。

- $f(n) = \Theta(n^4)$。

## A.3 基本概率

我们假定读者熟悉基本概率论，其水平相当于典型本科离散数学课程所覆盖的内容。这里仅提醒读者一些记号与基本事实。

若 $E$ 是一个事件，则 $\bar{E}$ 表示该事件的补事件，即 $E$ 不发生的事件。由定义，$\Pr[E] = 1 - \Pr[\bar{E}]$。若 $E_1$ 和 $E_2$ 是事件，则 $E_1 \land E_2$ 表示它们的合取，即 $E_1$ 与 $E_2$ 同时发生的事件。由定义，$\Pr[E_1 \land E_2] \leq \Pr[E_1]$。若 $\Pr[E_1 \land E_2] = \Pr[E_1] \cdot \Pr[E_2]$，则称事件 $E_1$ 和 $E_2$ 独立。

若 $E_1$ 和 $E_2$ 是事件，则 $E_1 \vee E_2$ 表示它们的析取，即 $E_1$ 或 $E_2$ 至少一个发生的事件。由定义可得 $\Pr[E_1 \vee E_2] \ge \Pr[E_1]$。联合界（union bound）常常是该量的一个非常有用的上界。

**命题 A.7**（联合界）

$$
\Pr[E_{1}\vee E_{2}]\leq\Pr[E_{1}]+\Pr[E_{2}].
$$

对任意事件 $E_{1}, \ldots, E_{k}$ 反复应用联合界，可得

$$
\Pr\left[\bigvee_{i=1}^{k}E_{i}\right]\leq\sum_{i=1}^{k}\Pr[E_{i}].
$$

给定 $E_2$ 时 $E_1$ 的条件概率，记为 $\Pr[E_1 \mid E_2]$，定义为

$$
\Pr[E_{1}\mid E_{2}]\stackrel{\mathrm{def}}{=}\frac{\Pr[E_{1}\wedge E_{2}]}{\Pr[E_{2}]}
$$

只要 $\Pr[E_2] \neq 0$。（若 $\Pr[E_2] = 0$，则 $\Pr[E_1 \mid E_2]$ 无定义。）它表示在事件 $E_2$ 已发生的前提下事件 $E_1$ 发生的概率。由定义立即得到

$$
\Pr[E_{1}\land E_{2}]=\Pr[E_{1}\mid E_{2}]\cdot\Pr[E_{2}];
$$

即使 $\Pr[E_2] = 0$，该等式也成立，只需按显然的方式把右端解释为乘以零。

由此我们可以轻松导出贝叶斯定理。

**定理 A.8**（贝叶斯定理）若 $\Pr[E_2] \neq 0$，则

$$
\Pr[E_{1}\mid E_{2}]=\frac{\Pr[E_{2}\mid E_{1}]\cdot\Pr[E_{1}]}{\Pr[E_{2}]}.
$$

**证明** 这是因为

$$
\Pr[E_{1}\mid E_{2}]=\frac{\Pr[E_{1}\land E_{2}]}{\Pr[E_{2}]}=\frac{\Pr[E_{2}\land E_{1}]}{\Pr[E_{2}]}=\frac{\Pr[E_{2}\mid E_{1}]\cdot\Pr[E_{1}]}{\Pr[E_{2}]}.
$$

设 $E_1, \ldots, E_n$ 是互不相交的事件，即对所有 $i \neq j$ 有 $\Pr[E_i \land E_j] = 0$。也就是说，$\{E_i\}$ 中至多有一个发生。再假定对所有 $i$，$\Pr[E_i] > 0$。则对任意事件 $F$

$$
\begin{aligned}
\Pr[F]&\leq\sum_{i=1}^{n}\Pr[F\land E_{i}]\\
&=\sum_{i=1}^{n}\Pr[F\mid E_{i}]\cdot\Pr[E_{i}],
\end{aligned}
$$

当 $\Pr[E_1 \lor \cdots \lor E_n] = 1$ 时取等号。一个特殊情形是取 $E_1$ 与 $\bar{E}_1$ 作为互不相交的事件。对任意事件 $E_2$ 取 $F = E_1 \lor E_2$，可得到联合界的一个可能更紧的版本：

$$
\begin{aligned}
\Pr[E_{1}\lor E_{2}]&=\Pr[E_{1}\lor E_{2}\mid E_{1}]\cdot\Pr[E_{1}]+\Pr[E_{1}\lor E_{2}\mid\bar{E}_{1}]\cdot\Pr[\bar{E}_{1}]\\
&\leq\Pr[E_{1}]+\Pr[E_{2}\mid\bar{E}_{1}].
\end{aligned}
$$

> **译者注（推导思路）**：第一行是把 $F = E_1 \vee E_2$ 按全概率公式在 $E_1$ 与其补事件上分解；其中 $\Pr[E_1\vee E_2\mid E_1] = 1$（$E_1$ 已发生则并集必发生），$\Pr[E_1\vee E_2\mid \bar{E}_1] = \Pr[E_2\mid \bar{E}_1]$（$E_1$ 不发生则并集发生等价于 $E_2$ 发生）。第二行的 $\le$ 来自 $\Pr[\bar{E}_1] \le 1$ 的放缩。与普通联合界 $\Pr[E_1]+\Pr[E_2]$ 相比，当 $\Pr[E_2\mid \bar{E}_1] \le \Pr[E_2]$（即 $E_2$ 与 $E_1$ 正相关）时该界更紧。

把它推广到 $n$ 个事件，我们得到

**命题 A.9**

$$
\Pr[\bigvee_{i=1}^{n}E_{i}]\leq\Pr[E_{1}]+\sum_{i=2}^{n}\Pr[E_{i}\mid\bar{E}_{1}\land\cdots\land\bar{E}_{i-1}].
$$

### \*有用的概率界

我们回顾一些术语，并陈述一些标准的概率界；这些内容在基础离散数学课程中可能不会遇到。本节材料仅在 8.3 节中使用。

（离散、实值）随机变量 $X$ 是一个从某个实数有限集 $S$ 中按概率取值的变量。若 $X$ 不取负值，则称它是非负的；若 $S = \{0,1\}$，则称 $X$ 是 $0/1$ 随机变量。若对所有 $b_1, \ldots, b_k$ 都有 $\Pr[X_1 = b_1 \land \cdots \land X_k = b_k] = \prod_{i=1}^k \Pr[X_i = b_i]$，则称 $0/1$ 随机变量 $X_1, \ldots, X_k$ 独立。

我们用 $\mathsf{Exp}[X]$ 表示随机变量 $X$ 的期望；若 $X$ 在集合 $S$ 中取值，则 $\mathsf{Exp}[X] \overset{\mathrm{def}}{=} \sum_{s \in S} s \cdot \Pr[X = s]$。最重要的一个事实是期望具有线性性：对随机变量 $X_1, \ldots, X_k$（可以有任意依赖关系），有 $\mathsf{Exp}[\sum_i X_i] = \sum_i \mathsf{Exp}[X_i]$。若 $X_1, X_2$ 独立，则 $\mathsf{Exp}[X_i \cdot X_j] = \mathsf{Exp}[X_i] \cdot \mathsf{Exp}[X_j]$。

当我们对 $X$ 所知甚少时，马尔可夫不等式很有用。

**命题 A.10**（马尔可夫不等式）设 $X$ 是非负随机变量，$v > 0$。则 $\Pr[X \geq v] \leq \mathsf{Exp}[X]/v$。

**证明** 设 $X$ 在集合 $S$ 中取值。我们有

$$
\begin{aligned}
\mathsf{Exp}[X]&=\sum_{s\in S}s\cdot\Pr[X=s]\\
&\geq\sum_{x\in S,x<v}\Pr[X=x]\cdot0+\sum_{x\in S,x\geq v}v\cdot\Pr[X=x]\\
&=v\cdot\Pr[X\geq v].
\end{aligned}
$$

由此即得所需结果。

$X$ 的方差（variance）记为 $\mathsf{Var}[X]$，度量 $X$ 偏离其期望的程度。我们有 $\mathsf{Var}[X] \stackrel{\mathrm{def}}{=} \mathsf{Exp}[(X - \mathsf{Exp}[X])^2] = \mathsf{Exp}[X^2] - \mathsf{Exp}[X]^2$，并且容易证明 $\mathsf{Var}[aX + b] = a^2\mathsf{Var}[X]$。对 $0/1$ 随机变量 $X_i$，有 $\mathsf{Var}[X_i] \leq 1/4$，因为此时 $\mathsf{Exp}[X_i] = \mathsf{Exp}[X_i^2]$，故 $\mathsf{Var}[X_i] = \mathsf{Exp}[X_i](1 - \mathsf{Exp}[X_i])$，当 $\mathsf{Exp}[X_i] = \frac{1}{2}$ 时取到最大值。

**命题 A.11**（切比雪夫不等式）设 $X$ 是一个随机变量，$\delta > 0$。则：

$$
\Pr[|X-\mathsf{Exp}[X]|\geq\delta]\leq\frac{\mathsf{Var}[X]}{\delta^{2}}.
$$

**证明** 定义非负随机变量 $Y \overset{\mathrm{def}}{=} (X - \mathsf{Exp}[X])^2$，然后应用马尔可夫不等式。于是，

$$
\begin{aligned}
\Pr[|X-\mathsf{Exp}[X]|\geq\delta]&=\Pr[(X-\mathsf{Exp}[X])^{2}\geq\delta^{2}]\\
&\leq\frac{\mathsf{Exp}[(X-\mathsf{Exp}[X])^{2}]}{\delta^{2}}=\frac{\mathsf{Var}[X]}{\delta^{2}}.
\end{aligned}
$$

若对每个 $i \neq j$ 和每个 $b_i, b_j \in \{0,1\}$ 都有

$$
\Pr[X_{i}=b_{i}~\land~X_{j}=b_{j}]=\Pr[X_{i}=b_{i}]\cdot\Pr[X_{j}=b_{j}].
$$

则称 $0/1$ 随机变量 $X_1, \ldots, X_m$ 两两独立（pairwise independent）。若 $X_1, \ldots, X_m$ 两两独立，则 $\mathsf{Var}[\sum_{i=1}^{m} X_i] = \sum_{i=1}^{m} \mathsf{Var}[X_i]$。（这可由如下事实推出：当 $i \neq j$ 时，利用两两独立性有 $\mathsf{Exp}[X_i \cdot X_j] = \mathsf{Exp}[X_i] \cdot \mathsf{Exp}[X_j]$。）切比雪夫不等式的一个重要推论如下。

**推论 A.12** 设 $X_1, \ldots, X_m$ 是两两独立的随机变量，具有相同的期望 $\mu$ 和方差 $\sigma^2$。则对每个 $\delta > 0$，

$$
\Pr\left[\left|\frac{\sum_{i=1}^{m} X_{i}}{m}-\mu\right|\geq\delta\right]\leq\frac{\sigma^{2}}{\delta^{2}m}.
$$

**证明** 由期望的线性性，$\mathsf{Exp}[\sum_{i=1}^{m} X_i/m] = \mu$。把切比雪夫不等式应用于随机变量 $\sum_{i=1}^{m} X_i/m$，我们有

$$
\Pr\left[\left|\frac{\sum_{i=1}^{m} X_{i}}{m}-\mu\right|\geq\delta\right]\leq\frac{\mathsf{Var}\left[\frac{1}{m}\cdot\sum_{i=1}^{m} X_{i}\right]}{\delta^{2}}.
$$

利用两两独立性，

$$
\mathsf{Var}\left[\frac{1}{m}\cdot\sum_{i=1}^{m}X_{i}\right]=\frac{1}{m^{2}}\sum_{i=1}^{m}\mathsf{Var}[X_{i}]=\frac{1}{m^{2}}\sum_{i=1}^{m}\sigma^{2}=\frac{\sigma^{2}}{m}.
$$

把上述两个等式结合起来即得所需不等式。

设 $0/1$ 随机变量 $X_1, \ldots, X_m$ 各自提供对某个固定（未知）比特 $b$ 的一个估计。也就是说，对所有 $i$ 有 $\Pr[X_i = b] \geq 1/2 + \varepsilon$，其中 $\varepsilon > 0$。

我们可以通过查看 $X_1$ 的值来估计 $b$；该估计以概率 $\Pr[X_1 = b]$ 正确。更好的估计可以通过查看 $X_1, \ldots, X_m$ 的值并取其中出现次数更多的值（多数表决）来获得。下面的命题允许我们在 $\{X_i\}$ 两两独立时分析这种做法的效果。

**命题 A.13** 固定 $\varepsilon > 0$ 和 $b \in \{0,1\}$，设 $\{X_i\}$ 是两两独立的 $0/1$ 随机变量，且对所有 $i$ 有 $\Pr[X_i = b] \geq \frac{1}{2} + \varepsilon$。考虑如下过程：记录 $m$ 个值 $X_1, \ldots, X_m$，把 $X$ 设为出现严格多数（strict majority）的那个值。则

$$
\Pr[X\neq b]\leq\frac{1}{4\cdot\varepsilon^{2}\cdot m}.
$$

**证明** 由对称性，我们可以假定 $b = 1$。则 $\mathsf{Exp}[X_i] \geq \frac{1}{2} + \varepsilon$；我们假定 $\mathsf{Exp}[X_i] = \frac{1}{2} + \varepsilon$，因为这是最坏情形。设 $X$ 表示 $\{X_i\}$ 的严格多数值，并注意 $X \neq 1$ 当且仅当 $\sum_{i=1}^m X_i \leq m/2$。于是

$$
\begin{aligned}
\Pr[X\neq1]&=\Pr\left[\sum_{i=1}^{m}X_{i}\leq m/2\right]\\
&=\Pr\left[\frac{\sum_{i=1}^{m}X_{i}}{m}-\frac{1}{2}\leq0\right]\\
&=\Pr\left[\frac{\sum_{i=1}^{m}X_{i}}{m}-\left(\frac{1}{2}+\varepsilon\right)\leq-\varepsilon\right]\\
&\leq\Pr\left[\left|\frac{\sum_{i=1}^{m}X_{i}}{m}-\left(\frac{1}{2}+\varepsilon\right)\right|\geq\varepsilon\right].
\end{aligned}
$$

由于对所有 $i$ 有 $\mathsf{Var}[X_i] \leq 1/4$，应用上一推论可得 $\Pr[X \neq 1] \leq \frac{1}{4\varepsilon^2 m}$，正如命题所述。

若 $\{X_{i}\}$ 独立，则可以得到更好的界：

**命题 A.14**（切尔诺夫界）固定 $\varepsilon > 0$ 和 $b \in \{0,1\}$，设 $\{X_i\}$ 是独立的 0/1 随机变量，且对所有 $i$ 有 $\Pr[X_i = b] = \frac{1}{2} + \varepsilon$。它们的多数值不是 $b$ 的概率至多为 $e^{-\varepsilon^2 m/2}$。

## A.4 “生日”问题

若从大小为 $N$ 的集合中均匀选取 $q$ 个元素 $y_1, \ldots, y_q$，那么存在不同的 $i, j$ 使得 $y_i = y_j$ 的概率是多少？我们把所述事件称为碰撞（collision），并用 $\mathsf{coll}(q, N)$ 表示该事件的概率。这个问题与所谓的“生日”问题相关，后者问：一个群体需要有多少人，才能使群体中某两人生日相同这一事件以概率 ${1}/2$ 发生？为看出二者的联系，令 $y_i$ 表示群体中第 $i$ 个人的生日。若群体中有 $q$ 个人，则我们有 $q$ 个从 $\{1, \ldots, 365\}$ 中均匀选取的值 $y_1, \ldots, y_q$，这里作了简化假设：生日在非闰年的 365 天中均匀且独立地分布。此外，生日相同对应于一次碰撞，即不同的 $i, j$ 满足 $y_i = y_j$。于是，生日问题的答案就是使 $\mathsf{coll}(q, 365) \geq 1/2$ 成立的最小（整）值 $q$。（答案或许令你惊讶——只需 $q = 23$ 人即可！）

下面表明：当 $q \leq \sqrt{2N}$ 时，碰撞概率为 $\Theta(q^2/N)$；等价地，当 $q = \Theta(\sqrt{N})$ 时，碰撞概率为常数。

**引理 A.15** 固定正整数 $N$，设 $q \leq \sqrt{2N}$ 个元素 $y_1, \ldots, y_q$ 从大小为 $N$ 的集合中均匀且独立地选取。则

$$
\frac{q\cdot(q-1)}{4N}\leq1-e^{-q(q-1)/2N}\leq\mathsf{coll}(q,N)\leq\frac{q\cdot(q-1)}{2N}.
$$

**证明** 上界对任意 $q$ 均成立，用联合界（命题 A.7）的简单应用即可证明。回忆碰撞意味着存在不同的 $i,j$ 使得 $y_i = y_j$。设 $\mathsf{Coll}$ 表示碰撞事件，设 $\mathsf{Coll}_{i,j}$ 表示 $y_i = y_j$ 这一事件。显然，对任意不同的 $i,j$ 有 $\Pr[\mathsf{Coll}_{i,j}] = 1/N$。此外，$\mathsf{Coll} = \bigvee_{i \neq j} \mathsf{Coll}_{i,j}$，于是反复应用联合界可得

$$
\begin{aligned}
\Pr\left[\mathsf{Coll}\right]&=\Pr\left[\bigvee_{i\neq j}\mathsf{Coll}_{i,j}\right]\\
&\leq\sum_{i\neq j}\Pr\left[\mathsf{Coll}_{i,j}\right]=\binom{q}{2}\cdot\frac{1}{N}.
\end{aligned}
$$

对于下界，设 $\mathsf{NoColl}_i$ 表示 $y_1, \ldots, y_i$ 之间没有碰撞的事件；即对所有 $j < k \leq i$，$y_j \neq y_k$。则 $\mathsf{NoColl}_q = \overline{\mathsf{Coll}}$ 是完全不发生碰撞的事件。若 $\mathsf{NoColl}_q$ 发生，则对所有 $i \leq q$，$\mathsf{NoColl}_i$ 必然也已发生。因此，

$$
\Pr[\mathsf{NoColl}_{q}]=\Pr[\mathsf{NoColl}_{1}]\cdot\Pr[\mathsf{NoColl}_{2}\mid\mathsf{NoColl}_{1}]\cdots\Pr[\mathsf{NoColl}_{q}\mid\mathsf{NoColl}_{q-1}].
$$

现在，$\Pr[\mathsf{NoColl}_{1}] = 1$，因为 $y_{1}$ 不可能与自身碰撞。此外，若事件 $\mathsf{NoColl}_{i}$ 发生，则 $\{y_{1}, \ldots, y_{i}\}$ 含有 $i$ 个不同的值；所以 $y_{i+1}$ 与这些值之一碰撞的概率为 $\frac{i}{N}$，从而 $y_{i+1}$ 不与其中任何值碰撞的概率为 ${1} - \frac{i}{N}$。这意味着

$$
\Pr[\mathsf{NoColl}_{i+1}\mid\mathsf{NoColl}_{i}]=1-\frac{i}{N},
$$

于是

$$
\Pr[\mathsf{NoColl}_{q}]=\prod_{i=1}^{q-1}\left(1-\frac{i}{N}\right).
$$

由于对所有 $i$ 有 $i/N < 1$，由不等式 A.3 得 ${1} - \frac{i}{N} \leq e^{-i/N}$，从而

$$
\Pr[\mathsf{NoColl}_{q}]\leq\prod_{i=1}^{q-1}e^{-i/N}=e^{-\sum_{i=1}^{q-1}(i/N)}=e^{-q(q-1)/2N}.
$$

我们得出结论

$$
\Pr[\mathsf{Coll}]=1-\Pr[\mathsf{NoColl}_{q}]\geq1-e^{-q(q-1)/2N}\geq\frac{q(q-1)}{4N},
$$

最后一步用到了不等式 A.4（注意 $q(q-1)/2N < 1$）。

作为引理 A.15 的一个简单应用，我们证明任何伪随机置换同时也是伪随机函数（参见命题 3.26）。回忆伪随机置换满足 $\ell_{in} = \ell_{out}$，即其输入长度与输出长度相等。此处的证明改编自文献 [27]。

**命题 A.16** 若 $F$ 是伪随机置换，且 $\ell_{out}(n) \geq n$，则 $F$ 也是伪随机函数。

**证明** 为记号简洁起见，我们假定 $\ell_{in} = \ell_{out} = n$。证明的核心在于表明：随机置换与随机函数（在多项式次查询的意义下）不可区分。设 $D$ 是一个算法，$q = q(n)$ 是 $D$ 向其预言机发起的查询次数。（不失一般性，我们假定 $D$ 总是恰好发起 $q$ 次查询，并且从不重复查询。）我们允许 $D$ 拥有无限的计算能力（因此可假定它是确定性的），但假定它发起的查询次数 $q$ 是多项式的。我们证明

$$
\left|\Pr_{f\leftarrow\mathsf{Func}_{n}}[D^{f(\cdot)}(1^{n})=1]-\Pr_{f\leftarrow\mathsf{Perm}_{n}}[D^{f(\cdot)}(1^{n})=1]\right|<\frac{q^{2}}{2^{n+1}}. \tag{A.1}
$$

其直观如下：$D$ 能察觉其预言机 $f$ 并非置换的唯一途径，就是观察到一次碰撞，即两个不同的输入映射到同一个输出。然而，向随机函数查询 $q$ 次时发现这样的碰撞的概率至多为 $\mathsf{coll}(q, 2^n) \leq q^2/2^n$，对任何多项式 $q$ 都是可忽略的。

形式化地，设 $\mathsf{Coll}$ 是 $D$ 的两次查询返回相同结果这一事件。我们首先断言

$$
\Pr_{f\leftarrow\mathsf{Func}_{n}}[D^{f(\cdot)}(1^{n})=1\mid\overline{\mathsf{Coll}}]=\Pr_{f\leftarrow\mathsf{Perm}_{n}}[D^{f(\cdot)}(1^{n})=1]. \tag{A.2}
$$

为看清这一点，注意 $D$ 的行为完全由 $q$ 元组的集合 $S \subseteq (\{0,1\}^n)^q$ 刻画：$\vec{a} = (a_1, \ldots, a_q) \in S$ 当且仅当对每个 $i$，$D$ 在第 $i$ 次预言机查询中收到响应 $a_i$ 时都输出 1。设 $\mathsf{distinct} \subset(\{0,1\}^n)^q$ 表示各分量互不相同的 $q$ 元组的集合。当 $f$ 是置换时，每个 $\vec{a} \in \mathsf{distinct}$ 等可能发生，而 $\vec{a} \notin \mathsf{distinct}$ 不可能发生；因此

$$
\Pr_{f\leftarrow\mathsf{Perm}_{n}}[D^{f(\cdot)}(1^{n})=1]=\frac{|S\cap\mathsf{distinct}|}{|\mathsf{distinct}|}.
$$

当 $f$ 是随机函数时，$(\{0,1\}^n)^q$ 中每个 $q$ 元组以概率 ${2}^{-nq}$ 出现。于是，利用贝叶斯定理

$$
\begin{aligned}
\Pr_{f\leftarrow\mathsf{Func}_{n}}[D^{f(\cdot)}(1^{n})=1\mid\overline{\mathsf{Coll}}]&=\frac{\Pr_{f\leftarrow\mathsf{Func}_{n}}[D^{f(\cdot)}(1^{n})=1\land\overline{\mathsf{Coll}}]}{\Pr_{f\leftarrow\mathsf{Func}_{n}}[\overline{\mathsf{Coll}}]}\\
&=\frac{2^{-nq}\cdot|S\cap\mathsf{distinct}|}{2^{-nq}\cdot|\mathsf{distinct}|}.
\end{aligned}
$$

于是式 (A.2) 成立。

作为推论，

$$
\begin{aligned}
&\left|\Pr_{f\leftarrow\mathsf{Func}_{n}}[D^{f(\cdot)}(1^{n})=1]-\Pr_{f\leftarrow\mathsf{Perm}_{n}}[D^{f(\cdot)}(1^{n})=1]\right|\\
&=\left|\Pr_{f\leftarrow\mathsf{Func}_{n}}[D^{f(\cdot)}(1^{n})=1\mid\overline{\mathsf{Coll}}]\cdot\Pr[\overline{\mathsf{Coll}}]\right.\\
&\quad\left.+\Pr_{f\leftarrow\mathsf{Func}_{n}}[D^{f(\cdot)}(1^{n})=1\mid\mathsf{Coll}]\cdot\Pr[\mathsf{Coll}]-\Pr_{f\leftarrow\mathsf{Perm}_{n}}[D^{f(\cdot)}(1^{n})=1]\right|\\
&=\left|\Pr_{f\leftarrow\mathsf{Func}_{n}}[D^{f(\cdot)}(1^{n})=1\mid\mathsf{Coll}]\cdot\Pr[\mathsf{Coll}]-\Pr_{f\leftarrow\mathsf{Perm}_{n}}[D^{f(\cdot)}(1^{n})=1]\cdot\Pr[\mathsf{Coll}]\right|\\
&\leq\Pr[\mathsf{Coll}].
\end{aligned}
$$

结合引理 A.15，这蕴含式 (A.1)，证明完成。

虽然上述结果表明伪随机置换（PRP）在渐近意义下也是伪随机函数（PRF），但它也揭示了一个具体的安全差距：即用 $q$ 次查询即可把 PRP 与 PRF 区分开，区分概率为 $\mathcal{O}(q^2/2^{\ell_{out}(n)})$。在实际使用分组密码并在分析中将其当作 PRF 处理时，记住这一点很重要。

## A.5 \*有限域

本书只在很少的地方用到有限域，但为完备起见，我们给出定义和一些基本事实。进一步的细节可参见任何抽象代数教材。

**定义 A.17**（有限）域是一个（有限）集合 $\mathbb{F}$ 连同两个二元运算 $+$、$\cdot$，满足以下条件：

- $\mathbb{F}$ 关于运算 $+$ 构成交换群。我们用 ${0}$ 表示该群的单位元。

- $\mathbb{F} \setminus \{0\}$ 关于运算 $\cdot$ 构成交换群。我们用 ${1}$ 表示该群的单位元。

- （分配律：）对所有 $a, b, c \in \mathbb{F}$，有 $a \cdot (b + c) = ab + ac$。

与通常一样，我们常常用 $ab$ 代替 $a \cdot b$。

$a \in \mathbb{F}$ 的加法逆元记为 $-a$，是满足 $a + (-a) = 0$ 的唯一元素；我们把 $b + (-a)$ 写作 $b - a$。$a \in \mathbb{F} \setminus \{0\}$ 的乘法逆元记为 $a^{-1}$，是满足 $aa^{-1} = 1$ 的唯一元素；我们常把 $ba^{-1}$ 写作 $b/a$。

**例 A.18**

由 9.1.4 节的结果可知，对任意素数 $p$，集合 $\{0, \ldots, p-1\}$ 关于模 $p$ 的加法与乘法构成一个有限域。我们把这个域记为 $\mathbb{F}_p$。

有限域有丰富的理论。就我们的目的而言，只需要几个基本事实。$\mathbb{F}$ 的阶（order）是 $\mathbb{F}$ 中元素的个数（假定它是有限的）。回忆：若 $q = p^r$（$p$ 为素数，$r \geq 1$ 为整数），则 $q$ 是素幂（prime power）。

**定理 A.19** 若 $\mathbb{F}$ 是有限域，则 $\mathbb{F}$ 的阶是素幂。反之，对每个素幂 $q$，存在一个阶为 $q$ 的有限域，而且这样的域在元素重新标记的意义下是唯一的。

对 $q = p^r$（$p$ 为素数），我们用 $\mathbb{F}_q$ 表示阶为 $q$ 的（唯一）域。我们把 $p$ 称为 $\mathbb{F}_q$ 的特征（characteristic）。

与群的情形一样，若 $n$ 是正整数且 $a \in \mathbb{F}$，则

$$
n\cdot a{\stackrel{\mathrm{def}}{=}}\underbrace{a+\cdots+a}_{n\text{ times}}\quad\text{and}\quad a^{n}{\stackrel{\mathrm{def}}{=}}\underbrace{a\cdots a}_{n\text{ times}}.
$$

记号按自然方式推广到 $n \leq 0$ 的情形。

**定理 A.20** 设 $\mathbb{F}_q$ 是特征为 $p$ 的有限域。则对所有 $a \in \mathbb{F}_q$，有 $p \cdot a = 0$。

设 $q = p^r$，$p$ 为素数。当 $r = 1$ 时，我们在例 A.18 中已看到，$\mathbb{F}_q = \mathbb{F}_p$ 可取为集合 $\{0, \ldots, p-1\}$，运算为模 $p$ 的加法与乘法。但需要注意的是：当 $r > 1$ 时，集合 $\{0, \ldots, q-1\}$ 关于模 $q$ 的加法与乘法并不构成域。例如，取 $q = 3^2 = 9$，则元素 3 在模 9 意义下没有乘法逆元。

特征为 $p$ 的有限域可以用 $\mathbb{F}_p$ 上的多项式来表示。我们给出一个例子以展示这种构造的大致思路，而不讨论构造为何有效，也不描述一般情形。我们借助 $\mathbb{F}_2$ 上的多项式来构造域 $\mathbb{F}_4$。固定多项式 $r(x) = x^2 + x + 1$，注意 $r(x)$ 在 $\mathbb{F}_2$ 上没有根，因为 $r(0) = r(1) = 1$（回忆我们工作在 $\mathbb{F}_2$ 中，这意味着所有运算都在模 2 意义下进行）。正如我们可以在实数域上引入虚数 $i$ 作为 $x^2 + 1$ 的根一样，我们可以在 $\mathbb{F}_2$ 上引入一个值 $\omega$ 作为 $r(x)$ 的根；即 $\omega^2 = -\omega - 1$。然后我们定义 $\mathbb{F}_4$ 为 $\mathbb{F}_2$ 上 $\omega$ 的所有一次多项式构成的集合；即 $\mathbb{F}_4 = \{0, 1, \omega, \omega + 1\}$。$\mathbb{F}_4$ 中的加法就是通常的多项式加法，只需记住系数上的运算在 $\mathbb{F}_2$ 中进行（即模 2）。$\mathbb{F}_4$ 中的乘法是多项式乘法（同样，系数上的运算按模 2 进行），随后作代入 $\omega^2 = -\omega - 1$；这也保证了结果落在 $\mathbb{F}_4$ 中。所以，例如

$$
\omega+(\omega+1)=2\omega+1=1
$$

以及

$$
\left(\omega+1\right)\cdot\left(\omega+1\right)=\omega^{2}+2\omega+1=\left(-\omega-1\right)+1=-\omega=\omega.
$$

虽然并不显然，但可以验证这是一个域；唯一难以验证的条件是每个非零元都有乘法逆元。

我们只需要另外一个结果。

**定理 A.21** 设 $\mathbb{F}_q$ 是阶为 $q$ 的有限域。则交换群 $\mathbb{F}_q \setminus \{0\}$ 关于 $\cdot$ 构成一个阶为 $q - 1$ 的循环群。
