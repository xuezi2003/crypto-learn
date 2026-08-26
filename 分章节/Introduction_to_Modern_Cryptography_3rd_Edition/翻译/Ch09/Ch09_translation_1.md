## Part III: Public-Key (Asymmetric) Cryptography　第三部分：公钥（非对称）密码学

# Chapter 9: Number Theory and Cryptographic Hardness Assumptions　第九章　数论与密码学困难性假设

Modern cryptosystems are invariably based on an assumption that some problem is hard. In Chapters 3–5, for example, we saw that private-key cryptography—both encryption schemes and message authentication codes—can be based on the assumption that pseudorandom permutations (a.k.a. block ciphers) exist. On the face of it, the assumption that pseudorandom permutations exist seems quite strong and unnatural, and it is reasonable to ask whether this assumption is true or whether there is any evidence to support it. In Chapter 7 we explored how block ciphers are constructed in practice. The fact that these constructions have resisted attack serves as an indication that the existence of pseudorandom permutations is plausible. Still, it may be difficult to believe that there are no efficient distinguishing attacks on existing block ciphers. Moreover, the current state of our theory is such that we do not know how to prove the pseudorandomness of any of the existing practical constructions relative to any “simpler” or “more reasonable” assumption. All in all, this is not an entirely satisfying state of affairs.

现代密码体制无一例外都建立在“某个问题是困难的”这一假设之上。例如在第 3–5 章中我们看到，私钥密码学——包括加密方案与消息认证码——可以建立在“伪随机置换（又称分组密码）存在”这一假设之上。表面上看，伪随机置换的存在似乎是一个相当强而且不自然的假设，因此自然要问：这个假设究竟是不是真的？有没有支持它的证据？第 7 章探讨了分组密码在实践中如何构造。这些构造经受住了攻击，这一事实表明伪随机置换的存在是可信的。尽管如此，要相信现有分组密码不存在高效的区分攻击，可能仍然很难。此外，以我们目前的理论水平，还不知道如何相对于任何“更简单”或“更合理”的假设来证明现有实用构造的伪随机性。总而言之，这并不是一个完全令人满意的局面。

In contrast, as mentioned in Chapter 3 (and investigated in detail in Chapter 8) it is possible to prove that pseudorandom permutations exist based on the much milder assumption that one-way functions exist. (Informally, a function is one-way if it is easy to compute but hard to invert; see Section 9.4.1.) Apart from a brief discussion in Section 8.1.2, however, we have not seen any concrete examples of functions believed to be one-way.

相比之下，正如第 3 章所述（并在第 8 章中详细研究过），可以基于温和得多的假设——“单向函数存在”——来证明伪随机置换的存在。（非正式地说，若一个函数易于计算却难以求逆，则它是单向的；见 9.4.1 节。）然而，除了 8.1.2 节的简要讨论之外，我们还没有见过任何被认为是单向函数的具体例子。

One goal of this chapter is to introduce various problems believed to be “hard,” and to present conjectured one-way functions based on those problems. $^{1}$ As such, this chapter can be viewed as a culmination of a “top down” approach to private-key cryptography. (See Figure 9.1.) That is, in Chapters 3–5 we have shown that private-key cryptography can be based on pseudorandom functions and permutations. We have then seen that the latter can be instantiated in practice using block ciphers, as explored in Chapter 7, or can be provably constructed from any one-way function, as shown in Chapter 8. Here, we take this one step further and show how one-way functions can be based on certain hard mathematical problems.

本章的目标之一是介绍各种被认为是“困难的”问题，并给出基于这些问题的候选单向函数。$^{1}$ 这样，本章可以视为私钥密码学“自顶向下”方法的集大成者。（见图 9.1。）也就是说，在第 3–5 章中我们已经证明私钥密码学可以建立在伪随机函数和伪随机置换之上；随后我们看到，后者既可以用分组密码在实践中实例化（如第 7 章所述），也可以从任意单向函数出发可证明地构造出来（如第 8 章所示）。这里我们更进一步，展示如何把单向函数建立在某些困难的数学问题之上。

$^{1}$ Recall we currently do not know how to prove that one-way functions exist, so the best we can do is base one-way functions on assumptions regarding the hardness of certain problems.

$^{1}$ 回顾一下，我们目前尚不知道如何证明单向函数存在，因此我们所能做的，就是把单向函数建立在关于某些问题困难性的假设之上。

![Image](https://lsky.jerryxue.top/i/2026/08/25/6a8d6a5ac37e7.jpg)

**FIGURE 9.1: Private-key cryptography: a top-down approach. / 图 9.1：私钥密码学：一种自顶向下的方法**

The examples we explore are number theoretic in nature, and we therefore begin with a short introduction to number theory. Because we are also interested in problems that can be solved efficiently (even a one-way function must be easy to compute in one direction, and cryptographic schemes must admit efficient algorithms for the honest parties), we also initiate a study of algorithmic number theory. Even the reader who is familiar with number theory is encouraged to read this chapter, since algorithmic aspects are typically ignored in a purely mathematical treatment of these topics.

我们要探讨的例子本质上都是数论的，因此首先简要介绍数论。由于我们也关心能够高效求解的问题（即便是单向函数，也必须在一个方向上易于计算；而密码方案必须为诚实方提供高效算法），所以我们还要开始学习算法数论。即使是熟悉数论的读者也建议阅读本章，因为对这些主题的纯数学处理通常忽略算法层面的内容。

A second goal of this chapter is to develop the material needed for public-key cryptography, whose study we will begin in Chapter 11. Strikingly, although in the private-key setting there exist efficient constructions of the necessary primitives (both block ciphers and hash functions) without invoking any number theory, in the public-key setting all known constructions rely on hard number-theoretic problems. The material in this chapter thus serves not only as a culmination of our study of private-key cryptography, but also as the foundation for our treatment of public-key cryptography.

本章的另一个目标是为公钥密码学准备所需的基础，对其研究将从第 11 章开始。令人惊讶的是，在私钥场景中，无需借助任何数论就能高效构造出所需的原语（分组密码和哈希函数皆如此）；而在公钥场景中，所有已知的构造都依赖于困难的数论问题。因此，本章内容既是我们私钥密码学研究的集大成者，也是后续公钥密码学研究的基础。

## 9.1 Preliminaries and Basic Group Theory　预备知识与基础群论

We begin with a review of prime numbers and basic modular arithmetic. Even the reader who has seen these topics before should skim the next two sections since some of the material may be new and we include proofs for most of the stated results.

我们首先回顾素数与基本模算术。即使以前见过这些内容的读者，也应浏览接下来的两小节，因为其中有些内容可能是新的，而且我们对所陈述的大多数结果都给出了证明。

### 9.1.1 Primes and Divisibility　素数与整除性

The set of integers is denoted by $\mathbb{Z}$. For $a, b \in \mathbb{Z}$, we say that $a$ divides $b$, written $a \mid b$, if there exists an integer $c$ such that $ac = b$. If $a$ does not divide $b$, we write $a \nmid b$. (We are primarily interested in the case where $a, b$, and $c$ are all positive, although the definition makes sense even when one or more of them is negative or zero.) A simple observation is that if $a \mid b$ and $a \mid c$ then $a \mid (Xb + Yc)$ for any $X, Y \in \mathbb{Z}$.

整数集记作 $\mathbb{Z}$。设 $a, b \in \mathbb{Z}$，若存在整数 $c$ 使得 $ac = b$，则称 $a$ 整除 $b$，记作 $a \mid b$；若 $a$ 不整除 $b$，则记作 $a \nmid b$。（尽管当其中某个或多个数为负数或零时该定义依然有意义，但我们主要关心的是 $a, b, c$ 均为正数的情形。）一个简单的观察是：若 $a \mid b$ 且 $a \mid c$，则对任意 $X, Y \in \mathbb{Z}$ 都有 $a \mid (Xb + Yc)$。

If $a \mid b$ and $a$ is positive, we call $a$ a divisor of $b$. If in addition $a \not\in \{1, b\}$ then $a$ is called a nontrivial divisor, or a factor, of $b$. A positive integer $p > 1$ is prime if it has no factors; i.e., it has only two divisors: 1 and itself. A positive integer greater than 1 that is not prime is called composite. By convention, the number 1 is neither prime nor composite.

若 $a \mid b$ 且 $a$ 为正数，则称 $a$ 是 $b$ 的因子。若进一步有 $a \not\in \{1, b\}$，则称 $a$ 是 $b$ 的非平凡因子。若正整数 $p > 1$ 没有非平凡因子——也就是说，它只有 1 和自身这两个因子——则称 $p$ 是素数。大于 1 且不是素数的正整数称为合数。按照约定，数 1 既不是素数也不是合数。

A fundamental theorem of arithmetic is that every integer greater than 1 can be expressed uniquely (up to ordering) as a product of primes. That is, any positive integer $N > 1$ can be written as $N = \prod_i p_i^{e_i}$, where the $\{p_i\}$ are distinct primes and $e_i \geq 1$ for all $i$; furthermore, the $\{p_i\}$ (and $\{e_i\}$) are uniquely determined up to ordering.

算术的一个基本定理是：每个大于 1 的整数都可以唯一地（在不计次序的意义下）表示为若干素数的乘积。也就是说，任意正整数 $N > 1$ 都可写成 $N = \prod_i p_i^{e_i}$，其中诸 $\{p_i\}$ 是互不相同的素数且对所有 $i$ 都有 $e_i \geq 1$；而且 $\{p_i\}$（连同 $\{e_i\}$）在不计次序的意义下是唯一确定的。

We are familiar with the process of division with remainder from elementary school. The following proposition formalizes this notion.

带余除法我们从小学起就已熟悉。下面的命题将这一概念形式化。

PROPOSITION 9.1 Let $a$ be an integer and let $b$ be a positive integer. Then there exist unique integers $q, r$ for which $a = qb + r$ and ${0} \leq r < b$.

命题 9.1　设 $a$ 为整数，$b$ 为正整数。那么存在唯一的整数 $q, r$，使得 $a = qb + r$ 且 ${0} \leq r < b$。

Furthermore, given integers $a$ and $b$ as in the proposition it is possible to compute $q$ and $r$ in polynomial time; see Appendix B.1. (An algorithm's running time is measured as a function of the length(s) of its input(s). An important point in the context of algorithmic number theory is that integer inputs are always assumed to be represented in binary. The running time of an algorithm taking as input an integer $N$ is therefore measured in terms of $\|N\|$, the length of the binary representation of $N$. Note that $\|N\| = \lfloor\log N\rfloor + 1$.

此外，对命题中的整数 $a$ 和 $b$，可以在多项式时间内计算出 $q$ 和 $r$；见附录 B.1。（算法的运行时间以其输入长度的函数来度量。在算法数论的背景下，重要的一点是：整数输入总是假定以二进制表示。因此，以整数 $N$ 为输入的算法，其运行时间以 $\|N\|$——即 $N$ 的二进制表示长度——来度量。）注意 $\|N\| = \lfloor\log N\rfloor + 1$。

The greatest common divisor of two integers $a, b$, written $\gcd(a, b)$, is the largest integer $c$ such that $c \mid a$ and $c \mid b$. (We leave $\gcd(0, 0)$ undefined.) The notion of greatest common divisor makes sense when either or both of $a, b$ are negative but we will typically have $a, b \geq 1$; anyway, $\gcd(a, b) = \gcd(|a|, |b|)$. Note that $\gcd(b, 0) = \gcd(0, b) = b$; also, if $p$ is prime then $\gcd(a, p)$ is either equal to 1 or $p$. If $\gcd(a, b) = 1$ we say that $a$ and $b$ are relatively prime.

两个整数 $a, b$ 的最大公因子记作 $\gcd(a, b)$，是满足 $c \mid a$ 且 $c \mid b$ 的最大整数 $c$。（$\gcd(0, 0)$ 未定义。）最大公因子的概念在 $a, b$ 之一或两者为负数时同样有意义，但我们通常取 $a, b \geq 1$；无论如何都有 $\gcd(a, b) = \gcd(|a|, |b|)$。注意 $\gcd(b, 0) = \gcd(0, b) = b$；另外，若 $p$ 是素数，则 $\gcd(a, p)$ 要么等于 1 要么等于 $p$。若 $\gcd(a, b) = 1$，则称 $a$ 与 $b$ 互素。

The following is a useful result:

下面是一个有用的结果：

PROPOSITION 9.2 Let $a, b$ be positive integers. Then there exist integers $X, Y$ such that $Xa + Yb = \gcd(a, b)$. Furthermore, $\gcd(a, b)$ is the smallest positive integer that can be expressed in this way.

命题 9.2　设 $a, b$ 为正整数。那么存在整数 $X, Y$ 使得 $Xa + Yb = \gcd(a, b)$。此外，$\gcd(a, b)$ 是能表示成这种形式的最小正整数。

PROOF Consider the set $I \overset{\mathrm{def}}{=} \{\hat{X}a + \hat{Y}b \mid \hat{X}, \hat{Y} \in \mathbb{Z}\}$. Note that $a, b \in I$, and so $I$ certainly contains some positive integers. Let $d$ be the smallest positive integer in $I$. We show that $d = \gcd(a, b)$; since $d$ can be written as $d = Xa + Yb$ for some $X, Y \in \mathbb{Z}$ (because $d \in I$), this proves the theorem.

证明　考虑集合 $I \overset{\mathrm{def}}{=} \{\hat{X}a + \hat{Y}b \mid \hat{X}, \hat{Y} \in \mathbb{Z}\}$。注意 $a, b \in I$，所以 $I$ 当然含有一些正整数。令 $d$ 为 $I$ 中最小的正整数。我们来证明 $d = \gcd(a, b)$；由于 $d$ 可以写成 $d = Xa + Yb$（其中 $X, Y \in \mathbb{Z}$，因为 $d \in I$），这就证明了该定理。

To show that $d = \gcd(a, b)$, we must prove that $d \mid a$ and $d \mid b$, and that $d$ is the largest integer with this property. In fact, we can show that $d$ divides every element in $I$. To see this, take an arbitrary $c \in I$ and write $c = X^{\prime}a + Y^{\prime}b$ with $X^{\prime}, Y^{\prime} \in \mathbb{Z}$. Using division with remainder (Proposition 9.1) we have that $c = qd + r$ with $q, r$ integers and ${0} \leq r < d$. Then

为证 $d = \gcd(a, b)$，我们必须证明 $d \mid a$ 且 $d \mid b$，并且 $d$ 是具有该性质的最大整数。事实上，我们可以证明 $d$ 整除 $I$ 中的每一个元素。为此，任取 $c \in I$ 并写 $c = X^{\prime}a + Y^{\prime}b$，其中 $X^{\prime}, Y^{\prime} \in \mathbb{Z}$。利用带余除法（命题 9.1），有 $c = qd + r$，其中 $q, r$ 为整数且 ${0} \leq r < d$。于是

$$
r=c-qd=X^{\prime}a+Y^{\prime}b-q(Xa+Yb)=(X^{\prime}-qX)a+(Y^{\prime}-qY)b\in I.
$$

If $r \neq 0$, this contradicts our choice of $d$ as the smallest positive integer in I (because $r < d$). So, $r = 0$ and hence $d \mid c$. This shows that $d$ divides every element of I.

若 $r \neq 0$，则与 $d$ 为 $I$ 中最小正整数的选取相矛盾（因为 $r < d$）。所以 $r = 0$，从而 $d \mid c$。这表明 $d$ 整除 $I$ 的每个元素。

Since $a \in I$ and $b \in I$, the above shows that $d|a$ and $d|b$ and so $d$ is a common divisor of $a$ and $b$. It remains to show that it is the greatest common divisor. Assume there is an integer $d^{\prime} > d$ such that $d^{\prime}|a$ and $d^{\prime}|b$. Then by the observation made earlier, $d^{\prime}|Xa + Yb$. Since the latter is equal to $d$, this means $d^{\prime}|d$. But this is impossible if $d^{\prime}$ is larger than $d$. We conclude that $d$ is the largest integer dividing both $a$ and $b$, and hence $d = \gcd(a,b)$.

由于 $a \in I$ 且 $b \in I$，上述论证表明 $d|a$ 且 $d|b$，故 $d$ 是 $a$ 与 $b$ 的一个公共因子。剩下还需证明它是最大的公共因子。假设存在整数 $d^{\prime} > d$ 满足 $d^{\prime}|a$ 且 $d^{\prime}|b$。那么由前面得到的观察可知 $d^{\prime}|Xa + Yb$。由于后者等于 $d$，这意味着 $d^{\prime}|d$；但若 $d^{\prime}$ 大于 $d$，这是不可能的。我们得出结论：$d$ 是同时整除 $a$ 与 $b$ 的最大整数，因而 $d = \gcd(a,b)$。

Given $a$ and $b$, the Euclidean algorithm can be used to compute $\gcd(a,b)$ in polynomial time. The extended Euclidean algorithm can be used to compute $X,Y$ (as in the above proposition) in polynomial time as well. See Appendix B.1.2 for details.

给定 $a$ 和 $b$，可以用欧几里得算法在多项式时间内计算 $\gcd(a,b)$；扩展欧几里得算法同样可以在多项式时间内计算出（上述命题中的）$X,Y$。细节见附录 B.1.2。

The preceding proposition is very useful in proving additional results about divisibility. We show two examples now.

前面的命题在证明关于整除性的其他结论时非常有用。下面给出两个例子。

PROPOSITION 9.3 If $c$ | $ab$ and $\gcd(a,c)=1$, then $c$ | $b$. Thus, if $p$ is prime and $p$ | $ab$ then either $p$ | $a$ or $p$ | $b$.

命题 9.3　若 $c$ | $ab$ 且 $\gcd(a,c)=1$，则 $c$ | $b$。因此，若 $p$ 是素数且 $p$ | $ab$，则 $p$ | $a$ 或 $p$ | $b$。

PROOF Since $c$ | $ab$ we have $\gamma c = ab$ for some integer $\gamma$. If $\gcd(a,c) = 1$ then, by the previous proposition, we know there exist integers $X,Y$ such that ${1} = Xa + Yc$. Multiplying both sides by $b$, we obtain

证明　由 $c$ | $ab$ 可知存在整数 $\gamma$ 使得 $\gamma c = ab$。若 $\gcd(a,c) = 1$，则由前述命题可知存在整数 $X,Y$ 使得 ${1} = Xa + Yc$。两边同乘 $b$，得到

$$
b=Xab+Ycb=X\gamma c+Ycb=c\cdot(X\gamma+Yb).
$$

Since $(X\gamma+Yb)$ is an integer, it follows that $c|b$.

由于 $(X\gamma+Yb)$ 是整数，故 $c|b$。

The second part of the proposition follows from the fact that if $p \nmid a$ and $p$ is prime then $\gcd(a, p) = 1$.

命题的第二部分由如下事实得出：若 $p \nmid a$ 且 $p$ 是素数，则 $\gcd(a, p) = 1$。

PROPOSITION 9.4 If $a|N$, $b|N$, and $\gcd(a,b)=1$, then $ab|N$.

命题 9.4　若 $a|N$、$b|N$ 且 $\gcd(a,b)=1$，则 $ab|N$。

PROOF Write $ac = N$, $bd = N$, and (using Proposition 9.2) ${1} = Xa + Yb$, where $c, d, X, Y$ are all integers. Multiplying both sides of the last equation by $N$ we obtain

证明　记 $ac = N$、$bd = N$，并且（利用命题 9.2）${1} = Xa + Yb$，其中 $c, d, X, Y$ 均为整数。将最后一个等式两边同乘 $N$，得到

$$
N=X a N+Y b N=X a b d+Y b a c=a b(X d+Y c),
$$

showing that ab|N.

即证得 $ab|N$。

### 9.1.2 Modular Arithmetic　模算术

Let $a, b, N \in \mathbb{Z}$ with $N > 1$. We use the notation $[a \bmod N]$ to denote the remainder of $a$ upon division by $N$. In more detail: by Proposition 9.1 there exist unique $q, r$ with $a = qN + r$ and ${0} \leq r < N$, and we define $[a \bmod N]$ to be equal to this $r$. Note therefore that ${0} \leq [a \bmod N] < N$. We refer to the process of mapping $a$ to $[a \bmod N]$ as reduction modulo $N$.

设 $a, b, N \in \mathbb{Z}$ 且 $N > 1$。我们用记号 $[a \bmod N]$ 表示 $a$ 除以 $N$ 所得的余数。具体地说：由命题 9.1，存在唯一的 $q, r$ 使得 $a = qN + r$ 且 ${0} \leq r < N$，我们就把 $[a \bmod N]$ 定义为这个 $r$。于是显然有 ${0} \leq [a \bmod N] < N$。我们把从 $a$ 得到 $[a \bmod N]$ 的过程称为模 $N$ 归约（reduction modulo $N$）。

We say that $a$ and $b$ are congruent modulo $N$, written $a = b \bmod N$, if $[a \bmod N] = [b \bmod N]$, i.e., if the remainder when $a$ is divided by $N$ is the same as the remainder when $b$ is divided by $N$. Note that $a = b \bmod N$ if and only if $N \mid (a - b)$. By way of notation, in an expression such as

若 $[a \bmod N] = [b \bmod N]$——也就是说，$a$ 除以 $N$ 所得的余数与 $b$ 除以 $N$ 所得的余数相同——则称 $a$ 与 $b$ 模 $N$ 同余，记作 $a = b \bmod N$。注意 $a = b \bmod N$ 当且仅当 $N \mid (a - b)$。作为记号约定，在形如

$$
a=b=c=\cdots=z\bmod N,
$$

the understanding is that every equal sign in this sequence (and not just the last) refers to congruence modulo $N$.

的表达式中，其含义是每个等号（而不仅仅是最后一个）都表示模 $N$ 的同余。

Note that $a = [b \mod N]$ implies $a = b \mod N$, but not vice versa. For example, $36 = 21 \bmod 15$ but ${36} \neq [21 \mod 15] = 6$. On the other hand, $[a \mod N] = [b \mod N]$ if and only if $a = b \mod N$.

注意，$a = [b \mod N]$ 蕴含 $a = b \mod N$，但反之不然。例如 $36 = 21 \bmod 15$，但 ${36} \neq [21 \mod 15] = 6$。另一方面，$[a \mod N] = [b \mod N]$ 当且仅当 $a = b \mod N$。

Congruence modulo $N$ is an equivalence relation, i.e., it is reflexive ($a = a \bmod N$ for all $a$), symmetric ($a = b \bmod N$ implies $b = a \bmod N$), and transitive (if $a = b \bmod N$ and $b = c \bmod N$, then $a = c \bmod N$). Congruence modulo $N$ also obeys the standard rules of arithmetic with respect to addition, subtraction, and multiplication; so, for example, if $a = a^{\prime}$ $\bmod N$ and $b = b^{\prime}$ $\bmod N$ then $(a + b) = (a^{\prime} + b^{\prime}) \bmod N$ and $ab = a^{\prime}b^{\prime}$ $\bmod N$. A consequence is that we can “reduce and then add/multiply” instead of having to “add/multiply and then reduce,” which can often simplify calculations.

模 $N$ 同余是一种等价关系，也就是说：它是自反的（对所有 $a$ 都有 $a = a \bmod N$）、对称的（由 $a = b \bmod N$ 可得 $b = a \bmod N$），并且是传递的（若 $a = b \bmod N$ 且 $b = c \bmod N$，则 $a = c \bmod N$）。模 $N$ 同余在加法、减法和乘法上也遵循标准的算术规则；例如，若 $a = a^{\prime}$ $\bmod N$ 且 $b = b^{\prime}$ $\bmod N$，则 $(a + b) = (a^{\prime} + b^{\prime}) \bmod N$ 且 $ab = a^{\prime}b^{\prime}$ $\bmod N$。由此带来的一个便利是：我们可以“先归约再做加法/乘法”，而不必“先做加法/乘法再归约”，这常常能简化计算。

**Example 9.5**　**例 9.5**

Let us compute $[1093028 \cdot 190301 \mod 100]$. Since 1093028 = 28 mod 100 and 190301 = 1 mod 100, we have

我们来计算 $[1093028 \cdot 190301 \mod 100]$。由于 1093028 = 28 mod 100 且 190301 = 1 mod 100，故有

$$
\begin{aligned}
1093028\cdot190301&=\left[1093028\bmod100\right]\cdot\left[190301\bmod100\right]\bmod100\\
&=28\cdot1=28\bmod100.
\end{aligned}
$$

The alternate way of calculating the answer (i.e., computing the product ${1093028} \cdot 190301$ and then reducing the result modulo 100) is less efficient.

另一种计算方法（即先算出乘积 ${1093028} \cdot 190301$，再把结果对 100 归约）效率较低。

Congruence modulo $N$ does not (in general) respect division. That is, if $a = a^{\prime} \mod N$ and $b = b^{\prime} \mod N$ then it is not necessarily true that $a/b = a^{\prime}/b^{\prime} \mod N$; in fact, the expression “$a/b \mod N$” is not necessarily well-defined. As a specific example that often causes confusion, $ab = cb \mod N$ does not necessarily imply that $a = c \mod N$.

模 $N$ 同余一般不保持除法。也就是说，若 $a = a^{\prime} \mod N$ 且 $b = b^{\prime} \mod N$，并不一定有 $a/b = a^{\prime}/b^{\prime} \mod N$；事实上，“$a/b \mod N$”这个表达式未必有意义。举一个常引起混淆的具体例子：由 $ab = cb \mod N$ 不一定能推出 $a = c \mod N$。

**Example 9.6**　**例 9.6**

Take $N = 24$. Then ${3} \cdot 2 = 6 = 15 \cdot 2 \mod 24$, but ${3} \neq 15 \mod 24$.

取 $N = 24$。此时 ${3} \cdot 2 = 6 = 15 \cdot 2 \mod 24$，但 ${3} \neq 15 \mod 24$。

In certain cases, however, we can define a meaningful notion of division. If for a given integer $b$ there exists an integer $c$ such that $bc = 1 \mod N$, we say that $b$ is invertible modulo $N$ and call $c$ a (multiplicative) inverse of $b$ modulo $N$. Clearly, ${0}$ is never invertible. It is also not difficult to show that if $c$ is a multiplicative inverse of $b$ modulo $N$ then so is $[c \mod N]$. Furthermore, if $c^{\prime}$ is another multiplicative inverse of $b$ then $[c \mod N] = [c^{\prime} \mod N]$. When $b$ is invertible we can therefore simply let $b^{-1}$ denote the unique multiplicative inverse of $b$ that lies in the range $\{1, \ldots, N-1\}$.

不过在某些情形下，我们可以定义一种有意义的除法概念。若对给定的整数 $b$ 存在整数 $c$ 使得 $bc = 1 \mod N$，则称 $b$ 模 $N$ 可逆，并称 $c$ 为 $b$ 模 $N$ 的一个（乘法）逆元。显然，${0}$ 永远不可逆。也不难证明：若 $c$ 是 $b$ 模 $N$ 的乘法逆元，则 $[c \mod N]$ 也是。此外，若 $c^{\prime}$ 是 $b$ 的另一个乘法逆元，则 $[c \mod N] = [c^{\prime} \mod N]$。因此当 $b$ 可逆时，可以直接用 $b^{-1}$ 表示落在范围 $\{1, \ldots, N-1\}$ 内的那个唯一的乘法逆元。

When $b$ is invertible modulo $N$, we define division by $b$ modulo $N$ as multiplication by $b^{-1}$ (i.e., we define $[a/b \bmod N] \stackrel{\mathrm{def}}{=} [ab^{-1} \bmod N]$.) We stress that division by $b$ is only defined when $b$ is invertible. If $ab = cb \bmod N$ and $b$ is invertible, then we may divide each side of the equation by $b$ (or, really, multiply each side by $b^{-1}$) to obtain

当 $b$ 模 $N$ 可逆时，我们把“模 $N$ 除以 $b$”定义为“乘以 $b^{-1}$”（即定义 $[a/b \bmod N] \stackrel{\mathrm{def}}{=} [ab^{-1} \bmod N]$）。我们强调，只有当 $b$ 可逆时才能定义除以 $b$。若 $ab = cb \bmod N$ 且 $b$ 可逆，则可将等式两边同除以 $b$（或者确切地说，同乘 $b^{-1}$），得到

$$
(ab)\cdot b^{-1}=(cb)\cdot b^{-1}\bmod N\quad\Rightarrow\quad a=c\bmod N.
$$

We see that in this case, division works as expected. Thus, invertible integers modulo N are “nicer” to work with, in some sense.

可见在这种情形下，除法如预期那样运作。因此在某种意义上，模 $N$ 下可逆的整数用起来更“方便”。

The natural question is: which integers are invertible modulo a given modulus $N$? We can fully answer this question using Proposition 9.2:

一个自然的问题是：哪些整数在给定模数 $N$ 下可逆？利用命题 9.2 可以完整回答这个问题：

PROPOSITION 9.7 Let $b, N$ be integers, with $b \geq 1$ and $N > 1$. Then $b$ is invertible modulo $N$ if and only if $\gcd(b, N) = 1$.

命题 9.7　设 $b, N$ 为整数，其中 $b \geq 1$ 且 $N > 1$。那么 $b$ 模 $N$ 可逆当且仅当 $\gcd(b, N) = 1$。

PROOF Assume $b$ is invertible modulo $N$, and let $c$ denote its inverse. Since $bc = 1 \bmod N$, this implies that $bc - 1 = \gamma N$ for some $\gamma \in \mathbb{Z}$. Equivalently, $bc - \gamma N = 1$. Since, by Proposition 9.2, $\gcd(b, N)$ is the smallest positive integer that can be expressed in this way, and there is no positive integer smaller than 1, this implies that $\gcd(b, N) = 1$.

证明　假设 $b$ 模 $N$ 可逆，令 $c$ 为其逆元。由 $bc = 1 \bmod N$ 可知，存在某个 $\gamma \in \mathbb{Z}$ 使 $bc - 1 = \gamma N$，等价地即 $bc - \gamma N = 1$。由于（根据命题 9.2）$\gcd(b, N)$ 是能表示成这种形式的最小正整数，而又不存在小于 1 的正整数，故 $\gcd(b, N) = 1$。

Conversely, if $\gcd(b, N) = 1$ then by Proposition 9.2 there exist integers $X, Y$ such that $Xb + YN = 1$. Reducing each side of this equation modulo $N$ gives $Xb = 1 \bmod N$, and we see that $X$ is a multiplicative inverse of $b$. (In fact, this gives an efficient algorithm to compute inverses.)

反之，若 $\gcd(b, N) = 1$，则由命题 9.2 存在整数 $X, Y$ 使得 $Xb + YN = 1$。将等式两边模 $N$ 归约，得 $Xb = 1 \bmod N$，可见 $X$ 就是 $b$ 的一个乘法逆元。（事实上，这给出了一个计算逆元的高效算法。）

**Example 9.8**　**例 9.8**

Let $b=11$ and $N=17$. Then $(-3)\cdot11+2\cdot17=1$, and so ${14}=[-3\bmod{17}]$ is the inverse of 11. One can verify that ${14}\cdot11=1\bmod{17}$.

取 $b=11$、$N=17$。此时 $(-3)\cdot11+2\cdot17=1$，故 ${14}=[-3\bmod{17}]$ 是 11 的逆元。可以验证 ${14}\cdot11=1\bmod{17}$。

Addition, subtraction, multiplication, and computation of inverses (when they exist) modulo $N$ can all be carried out in polynomial time; see Appendix B.2. Exponentiation (i.e., computing $[a^b \bmod N]$ for $b > 0$ an integer) can also be computed in polynomial time; see Appendix B.2.3.

模 $N$ 的加法、减法、乘法以及逆元计算（当逆元存在时）都可以在多项式时间内完成；见附录 B.2。幂运算（即对整数 $b > 0$ 计算 $[a^b \bmod N]$）同样可以在多项式时间内完成；见附录 B.2.3。

### 9.1.3 Groups　群

Let $\mathbb{G}$ be a set. A binary operation $\circ$ on $\mathbb{G}$ is simply a function $\circ(\cdot,\cdot)$ that maps two elements of $\mathbb{G}$ to another element of $\mathbb{G}$. If $g,h\in\mathbb{G}$ then instead of using the cumbersome notation $\circ(g,h)$, we write $g\circ h$.

设 $\mathbb{G}$ 是一个集合。$\mathbb{G}$ 上的二元运算 $\circ$ 就是一个函数 $\circ(\cdot,\cdot)$，它把 $\mathbb{G}$ 中的两个元素映射为 $\mathbb{G}$ 中的另一个元素。若 $g,h\in\mathbb{G}$，为避免 $\circ(g,h)$ 这种繁琐的记号，我们写作 $g\circ h$。

We now introduce the important notion of a group.

现在我们引入群这一重要概念。

DEFINITION 9.9 A group is a set G along with a binary operation $\circ$ for which the following conditions hold:

定义 9.9　群由一个集合 $\mathbb{G}$ 与其上的一个二元运算 $\circ$ 构成，且满足以下条件：

- (Closure:) For all $g, h \in \mathbb{G}$, $g \circ h \in \mathbb{G}$.

  （封闭性：）对所有 $g, h \in \mathbb{G}$，都有 $g \circ h \in \mathbb{G}$。

- (Existence of an identity:) There exists an identity $e \in \mathbb{G}$ such that for all $g \in \mathbb{G}$, $e \circ g = g = g \circ e$.

  （单位元的存在性：）存在单位元 $e \in \mathbb{G}$，使得对所有 $g \in \mathbb{G}$ 都有 $e \circ g = g = g \circ e$。

- (Existence of inverses:) For all $g \in \mathbb{G}$ there exists an element $h \in \mathbb{G}$ such that $g \circ h = e = h \circ g$. Such an $h$ is called an inverse of $g$.

  （逆元的存在性：）对所有 $g \in \mathbb{G}$，存在元素 $h \in \mathbb{G}$ 使得 $g \circ h = e = h \circ g$。这样的 $h$ 称为 $g$ 的逆元。

- (Associativity:) For all $g_1, g_2, g_3 \in \mathbb{G}$, $(g_1 \circ g_2) \circ g_3 = g_1 \circ (g_2 \circ g_3)$.

  （结合律：）对所有 $g_1, g_2, g_3 \in \mathbb{G}$，都有 $(g_1 \circ g_2) \circ g_3 = g_1 \circ (g_2 \circ g_3)$。

When $\mathbb{G}$ has a finite number of elements, we say $\mathbb{G}$ is finite and let $|\mathbb{G}|$ denote the order of the group (that is, the number of elements in $\mathbb{G}$).

当 $\mathbb{G}$ 含有有限个元素时，我们称 $\mathbb{G}$ 是有限群，并用 $|\mathbb{G}|$ 表示该群的阶（即 $\mathbb{G}$ 中元素的个数）。

A group G with operation $\circ$ is abelian if the following holds:

具有运算 $\circ$ 的群 $\mathbb{G}$ 如果还满足以下条件，就称为阿贝尔群：

- (Commutativity:) For all $g, h \in \mathbb{G}$, $g \circ h = h \circ g$.

  （交换律：）对所有 $g, h \in \mathbb{G}$，都有 $g \circ h = h \circ g$。

When the binary operation is understood, we simply call the set G a group.

当二元运算不言自明时，我们就直接把集合 $\mathbb{G}$ 称为群。

We will always deal with finite, abelian groups. We will be careful to specify, however, when a result requires these assumptions.

我们处理的总是有限的阿贝尔群。不过，当某个结果需要这些假设时，我们会明确指出。

Associativity implies that we do not need to include parentheses when writing long expressions; that is, the notation $g_1 \circ g_2 \circ \cdots \circ g_n$ is unambiguous since it does not matter in what order we evaluate the operation $\circ$.

结合律意味着书写长表达式时无需加括号；也就是说，记号 $g_1 \circ g_2 \circ \cdots \circ g_n$ 没有歧义，因为我们按什么顺序执行运算 $\circ$ 并不影响结果。

One can show that the identity element in a group $\mathbb{G}$ is unique, and so we can therefore refer to the identity of a group. One can also show that each element $g$ of a group has a unique inverse. See Exercise 9.1.

可以证明，群 $\mathbb{G}$ 的单位元是唯一的，因此我们可以直接说“群的单位元”。还可以证明，群的每个元素 $g$ 都有唯一的逆元。见习题 9.1。

If $\mathbb{G}$ is a group, a set $\mathbb{H} \subseteq \mathbb{G}$ is a subgroup of $\mathbb{G}$ if $\mathbb{H}$ itself forms a group under the same operation associated with $\mathbb{G}$. To check that $\mathbb{H}$ is a subgroup, we need to verify closure, existence of identity and inverses, and associativity as per Definition 9.9. (In fact, associativity—as well as commutativity if $\mathbb{G}$ is abelian—is inherited automatically from $\mathbb{G}$.) Every group $\mathbb{G}$ always has the trivial subgroups $\mathbb{G}$ and $\{1\}$. We call $\mathbb{H}$ a strict subgroup of $\mathbb{G}$ if $\mathbb{H} \neq \mathbb{G}$.

若 $\mathbb{G}$ 是群，而集合 $\mathbb{H} \subseteq \mathbb{G}$ 在 $\mathbb{G}$ 所带的同一运算下自身也构成群，则称 $\mathbb{H}$ 是 $\mathbb{G}$ 的子群。要验证 $\mathbb{H}$ 是子群，需按定义 9.9 逐一验证封闭性、单位元与逆元的存在性以及结合律。（实际上，结合律——以及当 $\mathbb{G}$ 是阿贝尔群时的交换律——会自动从 $\mathbb{G}$ 继承。）任何群 $\mathbb{G}$ 总有平凡子群 $\mathbb{G}$ 和 $\{1\}$。若 $\mathbb{H} \neq \mathbb{G}$，则称 $\mathbb{H}$ 是 $\mathbb{G}$ 的真子群。

In general, we will not use the notation $\circ$ to denote the group operation. Instead, we will use either additive notation or multiplicative notation depending on the group under discussion. This does not imply that the group operation corresponds to integer addition or multiplication; it is merely useful notation. When using additive notation, the group operation applied to two elements $g, h$ is denoted $g + h$; the identity is denoted by 0; the inverse of an element $g$ is denoted by $-g$; and we write $h - g$ in place of $h + (-g)$. When using multiplicative notation, the group operation applied to $g, h$ is denoted by $g \cdot h$ or simply $gh$; the identity is denoted by 1; the inverse of an element $g$ is denoted by $g^{-1}$; and we sometimes write $h/g$ in place of $hg^{-1}$.

一般而言，我们不再用记号 $\circ$ 表示群的运算，而是根据所讨论的群选用加法记号或乘法记号。这并不意味着群运算对应于整数的加法或乘法，这只是记号上的便利。使用加法记号时，作用在两个元素 $g, h$ 上的群运算记作 $g + h$；单位元记作 0；元素 $g$ 的逆元记作 $-g$；并把 $h - g$ 作为 $h + (-g)$ 的简写。使用乘法记号时，作用在 $g, h$ 上的群运算记作 $g \cdot h$ 或简写为 $gh$；单位元记作 1；元素 $g$ 的逆元记作 $g^{-1}$；有时也把 $h/g$ 作为 $hg^{-1}$ 的简写。

At this point, it may be helpful to see some examples.

此时看几个例子可能有助于理解。

**Example 9.10**　**例 9.10**

A set may be a group under one operation, but not another. For example, the set of integers $\mathbb{Z}$ is an abelian group under addition: the identity is the element 0, and every integer $g$ has inverse $-g$. On the other hand, it is not a group under multiplication since, for example, the integer 2 does not have a multiplicative inverse in the integers.

同一个集合在一种运算下可能是群，在另一种运算下却未必。例如，整数集 $\mathbb{Z}$ 在加法下是阿贝尔群：单位元是元素 0，每个整数 $g$ 的逆元是 $-g$。另一方面，它在乘法下不是群——例如，整数 2 在整数中就没有乘法逆元。

**Example 9.11**　**例 9.11**

The set of real numbers $\mathbb{R}$ is not a group under multiplication, since 0 does not have a multiplicative inverse. The set of nonzero real numbers, however, is an abelian group under multiplication with identity 1.

实数集 $\mathbb{R}$ 在乘法下不是群，因为 0 没有乘法逆元。然而，非零实数构成的集合在乘法下是以 1 为单位元的阿贝尔群。

The following example introduces the group $\mathbb{Z}_N$ that we will use frequently.

下面的例子引入我们将频繁使用的群 $\mathbb{Z}_N$。

**Example 9.12**　**例 9.12**

Let $N > 1$ be an integer. The set $\{0, \ldots, N-1\}$ with respect to addition modulo $N$ (i.e., where $a + b \overset{\mathrm{def}}{=} [a + b \mod N]$) is an abelian group of order $N$. Closure is obvious; associativity and commutativity follow from the fact that the integers satisfy these properties; the identity is 0; and, since $a + (N - a) = 0 \bmod N$, it follows that the inverse of any element $a$ is $\left[(N - a) \mod N\right]$. We denote this group by $\mathbb{Z}_N$. (We will also sometimes use $\mathbb{Z}_N$ to denote the set $\{0, \ldots, N-1\}$ without regard to any particular group operation.) $\diamondsuit$

设 $N > 1$ 为整数。集合 $\{0, \ldots, N-1\}$ 关于模 $N$ 加法（即规定 $a + b \overset{\mathrm{def}}{=} [a + b \mod N]$）构成一个阶为 $N$ 的阿贝尔群。封闭性显然；结合律与交换律由整数本身的相应性质得出；单位元是 0；又因为 $a + (N - a) = 0 \bmod N$，所以任意元素 $a$ 的逆元是 $\left[(N - a) \mod N\right]$。我们把这个群记作 $\mathbb{Z}_N$。（有时我们也直接用 $\mathbb{Z}_N$ 表示集合 $\{0, \ldots, N-1\}$，不涉及任何具体的群运算。）$\diamondsuit$

We end this section with an easy lemma that formalizes a “cancelation law” for groups.

本节以一个简单的引理作结，它形式化了群的“消去律”。

LEMMA 9.13 Let $\mathbb{G}$ be a group and $a,b,c \in \mathbb{G}$. If $ac = bc$, then $a = b$. In particular, if $ac = c$ then $a$ is the identity in $\mathbb{G}$.

引理 9.13　设 $\mathbb{G}$ 是群，且 $a,b,c \in \mathbb{G}$。若 $ac = bc$，则 $a = b$。特别地，若 $ac = c$，则 $a$ 是 $\mathbb{G}$ 中的单位元。

PROOF We know ac = bc. Multiplying both sides by the unique inverse $c^{-1}$ of c, we obtain a = b. In detail:

证明　已知 $ac = bc$。两边同乘 $c$ 的唯一逆元 $c^{-1}$，即得 $a = b$。具体写出来就是：

$$
ac=bc\ \Rightarrow\ (ac)c^{-1}=(bc)\cdot c^{-1}\ \Rightarrow\ a(cc^{-1})=b(cc^{-1})\ \Rightarrow\ a\cdot1=b\cdot1,
$$

i.e., a = b.

也就是 $a = b$。

Compare the above proof to the discussion (preceding Proposition 9.7) regarding a cancelation law for division modulo N. As indicated by the similarity, the invertible elements modulo N form a group under multiplication modulo N. We will return to this example in more detail shortly.

可将上述证明与命题 9.7 之前关于“模 $N$ 除法消去律”的讨论加以比较。正如两者的相似性所暗示的，模 $N$ 下可逆的元素在模 $N$ 乘法下构成一个群。我们稍后会更详细地回到这个例子。

#### Group Exponentiation　群的幂运算

It is often useful to be able to describe the group operation applied $m$ times to a fixed element $g$, where $m$ is a positive integer. When using additive notation, we express this as $m \cdot g$ or mg; that is,

能够描述“对固定元素 $g$ 施加 $m$ 次群运算”往往很有用，其中 $m$ 是正整数。使用加法记号时，我们把它表示为 $m \cdot g$ 或 mg；即

$$
mg=m\cdot g\stackrel{\mathrm{def}}{=}\underbrace{g+\cdots+g}_{m\text{ times}}.
$$

Note that $m$ is an integer, while $g$ is a group element. So $mg$ does not represent the group operation applied to $m$ and $g$ (indeed, we are working in a group where the group operation is written additively). Thankfully, however, the notation “behaves as it should”; so, for example, if $g \in \mathbb{G}$ and $m, m^{\prime}$ are integers then $(mg) + (m^{\prime} g) = (m + m^{\prime}) g$, $m(m^{\prime} g) = (mm^{\prime}) g$, and ${1} \cdot g = g$. In an abelian group $\mathbb{G}$ with $g, h \in \mathbb{G}$, $(mg) + (mh) = m(g + h)$.

注意 $m$ 是整数，而 $g$ 是群元素，因此 $mg$ 并不表示对 $m$ 和 $g$ 施加群运算（况且我们所考虑的群的运算本来就是按加法书写的）。好在这种记号“行为端正”：例如，若 $g \in \mathbb{G}$ 且 $m, m^{\prime}$ 为整数，则 $(mg) + (m^{\prime} g) = (m + m^{\prime}) g$、$m(m^{\prime} g) = (mm^{\prime}) g$、${1} \cdot g = g$。在阿贝尔群 $\mathbb{G}$ 中，若 $g, h \in \mathbb{G}$，则 $(mg) + (mh) = m(g + h)$。

When using multiplicative notation, we express application of the group operation m times to an element g by $g^m$. That is,

使用乘法记号时，对元素 $g$ 施加 $m$ 次群运算记作 $g^m$。即

$$
g^{m}\stackrel{\mathrm{def}}{=}\underbrace{g\cdots g}_{m\text{ times}}.
$$

The familiar rules of exponentiation hold: $g^m \cdot g^{m^{\prime}} = g^{m+m^{\prime}}$, $(g^m)^{m^{\prime}} = g^{mm^{\prime}}$, and $g^1 = g$. Also, if $\mathbb{G}$ is an abelian group and $g$, $h \in \mathbb{G}$ then $g^m \cdot h^m = (gh)^m$. All these are simply “translations” of the results from the previous paragraph to the setting of groups written multiplicatively rather than additively.

熟悉的幂运算法则依然成立：$g^m \cdot g^{m^{\prime}} = g^{m+m^{\prime}}$、$(g^m)^{m^{\prime}} = g^{mm^{\prime}}$、$g^1 = g$。另外，若 $\mathbb{G}$ 是阿贝尔群且 $g, h \in \mathbb{G}$，则 $g^m \cdot h^m = (gh)^m$。这些不过是把上一段的结果“翻译”到以乘法而非加法书写的群的情境中而已。

The above notation is extended in the natural way to the case when $m$ is zero or a negative integer. When using additive notation we define ${0} \cdot g \overset{\mathrm{def}}{=} 0$ (note that the 0 on the left-hand side is the integer 0 while the 0 on the right-hand side is the identity element of the group) and define $(-m) \cdot g \overset{\mathrm{def}}{=} m \cdot (-g)$ for $m$ a positive integer. Observe that $-g$ is the inverse of $g$ and, as one would expect, $(-m) \cdot g = -(mg)$. When using multiplicative notation, $g^0 \overset{\mathrm{def}}{=} 1$ and $g^{-m} \overset{\mathrm{def}}{=} (g^{-1})^m$. Again, $g^{-1}$ is the inverse of $g$, and we have $g^{-m} = (g^m)^{-1}$.

上面的记号可以按自然的方式推广到 $m$ 为零或负整数的情形。使用加法记号时，我们定义 ${0} \cdot g \overset{\mathrm{def}}{=} 0$（注意左边的 0 是整数 0，右边的 0 则是群的单位元），并对正整数 $m$ 定义 $(-m) \cdot g \overset{\mathrm{def}}{=} m \cdot (-g)$。可以看到，$-g$ 正是 $g$ 的逆元，而且不出所料地有 $(-m) \cdot g = -(mg)$。使用乘法记号时，定义 $g^0 \overset{\mathrm{def}}{=} 1$ 与 $g^{-m} \overset{\mathrm{def}}{=} (g^{-1})^m$。同样，$g^{-1}$ 是 $g$ 的逆元，并且有 $g^{-m} = (g^m)^{-1}$。

Let $g \in \mathbb{G}$ and $b \geq 0$ be an integer. Then the exponentiation $g^b$ can be computed using polynomially many group operations in $\mathbb{G}$. Thus, if the group operation can be computed in polynomial time then so can exponentiation. This is discussed in Appendix B.2.3.

设 $g \in \mathbb{G}$ 且 $b \geq 0$ 为整数。那么幂 $g^b$ 可以用 $\mathbb{G}$ 中多项式次群运算计算出来。因此，如果群运算可以在多项式时间内完成，那么幂运算也可以。这将在附录 B.2.3 中讨论。

We now know enough to prove the following remarkable result:

现在我们已具备足够的知识来证明下面这个出色的结果：

THEOREM 9.14 Let $\mathbb{G}$ be a finite group with $m = |\mathbb{G}|$, the order of the group. Then for any element $g \in \mathbb{G}$, it holds that $g^m = 1$.

定理 9.14　设 $\mathbb{G}$ 是有限群，$m = |\mathbb{G}|$ 为群的阶。那么对任意元素 $g \in \mathbb{G}$ 都有 $g^m = 1$。

PROOF We prove the theorem only when $\mathbb{G}$ is abelian (although it holds for any finite group). Fix arbitrary $g \in \mathbb{G}$, and let $g_1, \ldots, g_m$ be the elements of $\mathbb{G}$. We claim that

证明　我们只在 $\mathbb{G}$ 是阿贝尔群时证明本定理（尽管它对任意有限群都成立）。固定任意 $g \in \mathbb{G}$，并设 $g_1, \ldots, g_m$ 为 $\mathbb{G}$ 的全部元素。我们断言

$$
g_{1}\cdot g_{2}\cdots g_{m}=(g g_{1})\cdot(g g_{2})\cdots(g g_{m}).
$$

To see this, note that $gg_i = gg_j$ implies $g_i = g_j$ by Lemma 9.13. So each of the $m$ elements in parentheses on the right-hand side is distinct. Because there are exactly $m$ elements in $\mathbb{G}$, the $m$ elements being multiplied together on the right-hand side are simply all elements of $\mathbb{G}$ in some permuted order. Since $\mathbb{G}$ is abelian, the order in which elements are multiplied does not matter, and so the right-hand side is equal to the left-hand side.

为看出这一点，注意由引理 9.13，$gg_i = gg_j$ 蕴含 $g_i = g_j$。所以右边括号里的 $m$ 个元素两两不同。由于 $\mathbb{G}$ 中恰有 $m$ 个元素，右边相乘的这 $m$ 个元素正是 $\mathbb{G}$ 的全部元素的某种排列。又因为 $\mathbb{G}$ 是阿贝尔群，元素相乘的顺序无关紧要，故右边等于左边。

Again using the fact that G is abelian, we can “pull out” all occurrences of $g$ and obtain

再次利用 $\mathbb{G}$ 是阿贝尔群这一事实，可以把所有的 $g$ “提取出来”，得到

$$
g_{1}\cdot g_{2}\cdots g_{m}=(g g_{1})\cdot(g g_{2})\cdots(g g_{m})=g^{m}\cdot(g_{1}\cdot g_{2}\cdots g_{m}).
$$

Appealing once again to Lemma 9.13, this implies $g^{m}=1$.

再次借助引理 9.13，由此可得 $g^{m}=1$。

An important corollary of the above is that we can work “modulo the group order” in the exponent:

上述结果的一个重要推论是：我们可以在指数上“模群的阶”进行运算：

COROLLARY 9.15 Let $\mathbb{G}$ be a finite group with $m = |\mathbb{G}| > 1$. Then for any $g \in \mathbb{G}$ and any integer $x$, we have $g^x = g^{[x \mod m]}$.

推论 9.15　设 $\mathbb{G}$ 是有限群，$m = |\mathbb{G}| > 1$。那么对任意 $g \in \mathbb{G}$ 和任意整数 $x$，都有 $g^x = g^{[x \mod m]}$。

PROOF Say $x = qm + r$, where $q, r$ are integers and $r = [x \mod m]$. Then

证明　设 $x = qm + r$，其中 $q, r$ 为整数且 $r = [x \mod m]$。那么

$$
g^{x}=g^{q m+r}=g^{q m}\cdot g^{r}=(g^{m})^{q}\cdot g^{r}=1^{q}\cdot g^{r}=g^{r}
$$

(using Theorem 9.14), as claimed.

（其中用到定理 9.14），断言得证。

**Example 9.16**　**例 9.16**

Written additively, the above corollary says that if $g$ is an element in a group of order $m$, then $x \cdot g = [x \bmod m] \cdot g$. As an example, consider the group $\mathbb{Z}_{15}$ of order m = 15, and take g = 11. The corollary says that

用加法记号表述，上述推论说明：若 $g$ 是阶为 $m$ 的群中的元素，则 $x \cdot g = [x \bmod m] \cdot g$。举例来说，考虑阶为 $m = 15$ 的群 $\mathbb{Z}_{15}$，取 $g = 11$。该推论表明

$$
{152}\cdot11=\left[152\bmod15\right]\cdot11=2\cdot11=11+11=22=7\bmod15.
$$

The above agrees with the fact (cf. Example 9.5) that we can “reduce and then multiply” rather than having to “multiply and then reduce.”

上式与例 9.5 中的事实一致：我们可以“先归约再相乘”，而不必“先相乘再归约”。

Another corollary that will be extremely useful for cryptographic applications is the following:

下面这个推论对密码学应用极为有用：

COROLLARY 9.17 Let $\mathbb{G}$ be a finite group with $m = |\mathbb{G}| > 1$. Let $e > 0$ be an integer, and define the function $f_e : \mathbb{G} \to \mathbb{G}$ by $f_e(g) = g^e$. If $\gcd(e, m) = 1$, then $f_e$ is a permutation (i.e., a bijection). Moreover, if $d = e^{-1} \bmod m$ then $f_d$ is the inverse of $f_e$. (Note by Proposition 9.7, $\gcd(e, m) = 1$ implies $e$ is invertible modulo $m$.)

推论 9.17　设 $\mathbb{G}$ 是有限群，$m = |\mathbb{G}| > 1$。设 $e > 0$ 为整数，并定义函数 $f_e : \mathbb{G} \to \mathbb{G}$ 为 $f_e(g) = g^e$。若 $\gcd(e, m) = 1$，则 $f_e$ 是置换（即双射）。此外，若 $d = e^{-1} \bmod m$，则 $f_d$ 是 $f_e$ 的逆。（由命题 9.7 可知，$\gcd(e, m) = 1$ 意味着 $e$ 模 $m$ 可逆。）

PROOF Since $\mathbb{G}$ is finite, the second part of the claim implies the first; thus, we need only show that $f_d$ is the inverse of $f_e$. This is true because for any $g \in \mathbb{G}$, we have

证明　由于 $\mathbb{G}$ 是有限的，断言的后半部分蕴含前半部分；因此只需证明 $f_d$ 是 $f_e$ 的逆。这是因为对任意 $g \in \mathbb{G}$，有

$$
f_{d}\left(f_{e}(g)\right)=f_{d}(g^{e})=(g^{e})^{d}=g^{e d}=g^{[e d\bmod m]}=g^{1}=g,
$$

where the fourth equality follows from Corollary 9.15.

其中第四个等号由推论 9.15 得出。

### 9.1.4 The Group $\mathbb{Z}_{N}^{*}$　群 $\mathbb{Z}_{N}^{*}$

As discussed in Example 9.12, the set $\mathbb{Z}_N = \{0, \ldots, N-1\}$ is a group under addition modulo $N$. Can we define a group with respect to multiplication modulo $N$? In doing so, we will have to eliminate those elements in $\mathbb{Z}_N$ that are not invertible; e.g., we will have to eliminate 0 since it has no multiplicative inverse. Nonzero elements may also fail to be invertible (cf. Proposition 9.7).

如例 9.12 所述，集合 $\mathbb{Z}_N = \{0, \ldots, N-1\}$ 在模 $N$ 加法下构成群。那么，能否在模 $N$ 乘法下定义一个群呢？为此必须去掉 $\mathbb{Z}_N$ 中不可逆的元素；例如必须去掉 0，因为它没有乘法逆元。非零元素同样可能不可逆（参见命题 9.7）。

Which elements $b \in \{1, \ldots, N-1\}$ are invertible modulo $N$? Proposition 9.7 says that these are exactly the elements $b$ for which $\gcd(b, N) = 1$. We have also seen in Section 9.1.2 that whenever $b$ is invertible, it has an inverse lying in the range $\{1, \ldots, N-1\}$. This leads us to define, for any $N > 1$, the set

$\{1, \ldots, N-1\}$ 中哪些元素 $b$ 模 $N$ 可逆？命题 9.7 表明，恰好就是那些满足 $\gcd(b, N) = 1$ 的元素 $b$。我们在 9.1.2 节还看到，只要 $b$ 可逆，它的逆元就落在范围 $\{1, \ldots, N-1\}$ 内。于是，对任意 $N > 1$，我们定义集合

$$
\mathbb{Z}_{N}^{*}\stackrel{\mathrm{def}}{=}\left\{b\in\{1,\ldots,N-1\}~\middle|~\gcd(b,N)=1\right\};
$$

i.e., $\mathbb{Z}_N^*$ consists of integers in the set $\{1, \ldots, N-1\}$ that are relatively prime to $N$. The group operation is multiplication modulo $N$; i.e., $ab \overset{\mathrm{def}}{=} [ab \bmod N]$.

也就是说，$\mathbb{Z}_N^*$ 由集合 $\{1, \ldots, N-1\}$ 中与 $N$ 互素的整数组成。群运算取模 $N$ 乘法，即 $ab \overset{\mathrm{def}}{=} [ab \bmod N]$。

We claim that $\mathbb{Z}_N^*$ is an abelian group with respect to this operation. Since 1 is always in $\mathbb{Z}_N^*$, the set clearly contains an identity element. The discussion above shows that each element in $\mathbb{Z}_N^*$ has a multiplicative inverse in the same set. Commutativity and associativity follow from the fact that these properties hold over the integers. To show that closure holds, let $a, b \in \mathbb{Z}_N^*$; then $[ab \bmod N]$ has inverse $[b^{-1}a^{-1} \bmod N]$, which means that $\gcd([ab \bmod N], N) = 1$ and so $ab \in \mathbb{Z}_N^*$. Summarizing:

我们断言 $\mathbb{Z}_N^*$ 关于这一运算构成阿贝尔群。由于 1 总是在 $\mathbb{Z}_N^*$ 中，该集合显然含有单位元。上面的讨论表明，$\mathbb{Z}_N^*$ 中每个元素在同一集合内都有乘法逆元。交换律与结合律由整数上成立的相应性质直接得出。至于封闭性，设 $a, b \in \mathbb{Z}_N^*$，则 $[ab \bmod N]$ 以 $[b^{-1}a^{-1} \bmod N]$ 为逆元，这意味着 $\gcd([ab \bmod N], N) = 1$，故 $ab \in \mathbb{Z}_N^*$。总结如下：

PROPOSITION 9.18 Let $N > 1$ be an integer. Then $\mathbb{Z}_N^*$ is an abelian group under multiplication modulo $N$.

命题 9.18　设 $N > 1$ 为整数。那么 $\mathbb{Z}_N^*$ 在模 $N$ 乘法下构成阿贝尔群。

Define $\phi(N) \overset{\mathrm{def}}{=} |\mathbb{Z}_N^*|$, the order of the group $\mathbb{Z}_N^*$. ($\phi$ is called the Euler $\phi$ function.) What is the value of $\phi(N)$? First consider the case when $N = p$ is prime. Then all elements in $\{1, \ldots, p-1\}$ are relatively prime to $p$, and so $\phi(p) = |\mathbb{Z}_p^*| = p-1$. Next consider the case that $N = pq$, where $p, q$ are distinct primes. If an integer $a \in \{1, \ldots, N-1\}$ is not relatively prime to $N$, then either $p \mid a$ or $q \mid a$ ($a$ cannot be divisible by both $p$ and $q$ since this would imply $pq \mid a$ but $a < N = pq$). The elements in $\{1, \ldots, N-1\}$ divisible by $p$ are exactly the $(q-1)$ elements $p, 2p, 3p, \ldots, (q-1)p$, and the elements divisible by $q$ are exactly the $(p-1)$ elements $q, 2q, \ldots, (p-1)q$. The number of elements remaining (i.e., those that are neither divisible by $p$ nor $q$) is therefore given by

定义 $\phi(N) \overset{\mathrm{def}}{=} |\mathbb{Z}_N^*|$，即群 $\mathbb{Z}_N^*$ 的阶。（$\phi$ 称为欧拉 $\phi$ 函数。）$\phi(N)$ 的值是多少？先考虑 $N = p$ 为素数的情形：此时 $\{1, \ldots, p-1\}$ 中所有元素都与 $p$ 互素，故 $\phi(p) = |\mathbb{Z}_p^*| = p-1$。再考虑 $N = pq$（$p, q$ 为不同素数）的情形。若整数 $a \in \{1, \ldots, N-1\}$ 与 $N$ 不互素，则 $p \mid a$ 或 $q \mid a$（$a$ 不可能同时被 $p$ 和 $q$ 整除，否则将有 $pq \mid a$，而 $a < N = pq$）。$\{1, \ldots, N-1\}$ 中被 $p$ 整除的元素恰好是 $p, 2p, 3p, \ldots, (q-1)p$ 这 $(q-1)$ 个，被 $q$ 整除的元素恰好是 $q, 2q, \ldots, (p-1)q$ 这 $(p-1)$ 个。因此剩余元素的个数（也就是既不被 $p$ 也不被 $q$ 整除的那些）为

$$
(N-1)-(q-1)-(p-1)=pq-p-q+1=(p-1)(q-1).
$$

We have thus proved that $\phi(N) = (p - 1)(q - 1)$ when $N$ is the product of two distinct primes $p$ and $q$.

这样就证明了：当 $N$ 是两个不同素数 $p$ 与 $q$ 的乘积时，$\phi(N) = (p - 1)(q - 1)$。

You are asked to prove the following general result (used only rarely in the rest of the book) in Exercise 9.4:

请读者在习题 9.4 中证明下面的一般结果（本书其余部分很少用到）：

THEOREM 9.19 Let $N = \prod_i p_i^{e_i}$, where the $\{p_i\}$ are distinct primes and $e_i \geq 1$. Then $\phi(N) = \prod_i p_i^{e_i - 1}(p_i - 1)$.

定理 9.19　设 $N = \prod_i p_i^{e_i}$，其中诸 $\{p_i\}$ 是不同的素数且 $e_i \geq 1$。那么 $\phi(N) = \prod_i p_i^{e_i - 1}(p_i - 1)$。

**Example 9.20**　**例 9.20**

Take $N = 15 = 5 \cdot 3$. Then $\mathbb{Z}_{15}^* = \{1,2,4,7,8,11,13,14\}$ and $|\mathbb{Z}_{15}^*| = 8 = 4 \cdot 2 = \phi(15)$. The inverse of ${8}$ in $\mathbb{Z}_{15}^*$ is ${2}$, since ${8} \cdot 2 = 16 = 1 \mod 15$.

取 $N = 15 = 5 \cdot 3$。此时 $\mathbb{Z}_{15}^* = \{1,2,4,7,8,11,13,14\}$，且 $|\mathbb{Z}_{15}^*| = 8 = 4 \cdot 2 = \phi(15)$。${8}$ 在 $\mathbb{Z}_{15}^*$ 中的逆元是 ${2}$，因为 ${8} \cdot 2 = 16 = 1 \mod 15$。

We have shown that $\mathbb{Z}_N^*$ is a group of order $\phi(N)$. The following are now easy corollaries of Theorem 9.14 and Corollary 9.17:

已经证明 $\mathbb{Z}_N^*$ 是阶为 $\phi(N)$ 的群。于是，由定理 9.14 和推论 9.17 可以立刻得到以下两条推论：

COROLLARY 9.21 Take arbitrary integer $N > 1$ and $a \in \mathbb{Z}_N^*$. Then

推论 9.21　取任意整数 $N > 1$ 与 $a \in \mathbb{Z}_N^*$。那么

$$
a^{\phi(N)}=1\bmod N.
$$

For the specific case that $N = p$ is prime and $a \in \{1, \ldots, p-1\}$, we have

特别地，当 $N = p$ 为素数且 $a \in \{1, \ldots, p-1\}$ 时，有

$$
a^{p-1}=1\bmod p.
$$

COROLLARY 9.22 Fix $N > 1$. For integer $e > 0$ define $f_e: \mathbb{Z}_N^* \to \mathbb{Z}_N^*$ by $f_e(x) = [x^e \bmod N]$. If $e$ is relatively prime to $\phi(N)$ then $f_e$ is a permutation. Moreover, if $d = e^{-1} \bmod \phi(N)$ then $f_d$ is the inverse of $f_e$.

推论 9.22　固定 $N > 1$。对整数 $e > 0$ 定义 $f_e: \mathbb{Z}_N^* \to \mathbb{Z}_N^*$ 为 $f_e(x) = [x^e \bmod N]$。若 $e$ 与 $\phi(N)$ 互素，则 $f_e$ 是置换。此外，若 $d = e^{-1} \bmod \phi(N)$，则 $f_d$ 是 $f_e$ 的逆。

### 9.1.5 \*Isomorphisms and the Chinese Remainder Theorem　\*同构与中国剩余定理

Two groups are isomorphic if they have the same underlying structure. From a mathematical point of view, an isomorphism of a group G provides an alternate, but equivalent, way of thinking about G. From a computational perspective, an isomorphism provides a different way to represent elements in G, which can often have a significant impact on algorithmic efficiency.

若两个群具有相同的底层结构，则称它们是同构的。从数学角度看，群 $\mathbb{G}$ 的同构提供了思考 $\mathbb{G}$ 的另一种方式，尽管表述不同但完全等价。从计算角度看，同构给出了表示 $\mathbb{G}$ 中元素的另一种方式，而这往往会对算法效率产生显著影响。

DEFINITION 9.23 Let $\mathbb{G},\mathbb{H}$ be groups with respect to the operations $\circ_{\mathbb{G}},\circ_{\mathbb{H}}$, respectively. A function $f:\mathbb{G}\to\mathbb{H}$ is an isomorphism from $\mathbb{G}$ to $\mathbb{H}$ if:

定义 9.23　设 $\mathbb{G},\mathbb{H}$ 分别是关于运算 $\circ_{\mathbb{G}},\circ_{\mathbb{H}}$ 的群。函数 $f:\mathbb{G}\to\mathbb{H}$ 称为从 $\mathbb{G}$ 到 $\mathbb{H}$ 的同构，如果：

1. f is a bijection, and

   $f$ 是双射，并且

2. For all $g_1, g_2 \in \mathbb{G}$ we have $f(g_1 \circ_{\mathbb{G}} g_2) = f(g_1) \circ_{\mathbb{H}} f(g_2)$.

   对所有 $g_1, g_2 \in \mathbb{G}$，都有 $f(g_1 \circ_{\mathbb{G}} g_2) = f(g_1) \circ_{\mathbb{H}} f(g_2)$。

If there exists an isomorphism from $\mathbb{G}$ to $\mathbb{H}$ then we say that these groups are isomorphic and write $\mathbb{G} \simeq \mathbb{H}$.

若存在从 $\mathbb{G}$ 到 $\mathbb{H}$ 的同构，则称这两个群同构，记作 $\mathbb{G} \simeq \mathbb{H}$。

In essence, an isomorphism from $\mathbb{G}$ to $\mathbb{H}$ is just a renaming of elements of $\mathbb{G}$ as elements of $\mathbb{H}$. Note that if $\mathbb{G}$ is finite and $\mathbb{G} \simeq \mathbb{H}$, then $\mathbb{H}$ must be finite and of the same size as $\mathbb{G}$. Also, if there exists an isomorphism $f$ from $\mathbb{G}$ to $\mathbb{H}$ then $f^{-1}$ is an isomorphism from $\mathbb{H}$ to $\mathbb{G}$. It is possible, however, that $f$ is efficiently computable while $f^{-1}$ is not (or vice versa).

从本质上讲，从 $\mathbb{G}$ 到 $\mathbb{H}$ 的同构不过是把 $\mathbb{G}$ 的元素改名为 $\mathbb{H}$ 的元素。注意，若 $\mathbb{G}$ 有限且 $\mathbb{G} \simeq \mathbb{H}$，则 $\mathbb{H}$ 必定有限且与 $\mathbb{G}$ 大小相同。另外，若 $f$ 是从 $\mathbb{G}$ 到 $\mathbb{H}$ 的同构，则 $f^{-1}$ 就是从 $\mathbb{H}$ 到 $\mathbb{G}$ 的同构。但是，可能出现 $f$ 可以高效计算而 $f^{-1}$ 不能的情形（反之亦然）。

The aim of this section is to use the language of isomorphisms to better understand the group structure of $\mathbb{Z}_N$ and $\mathbb{Z}_N^*$ when $N = pq$ is a product of two distinct primes. We first need to introduce the notion of a direct product of groups. Given groups $\mathbb{G}$, $\mathbb{H}$ with group operations $\circ_{\mathbb{G}}$, $\circ_{\mathbb{H}}$, respectively, we define a new group $\mathbb{G} \times \mathbb{H}$ (the direct product of $\mathbb{G}$ and $\mathbb{H}$) as follows. The elements of $\mathbb{G} \times \mathbb{H}$ are ordered pairs $(g, h)$ with $g \in \mathbb{G}$ and $h \in \mathbb{H}$; thus, if $\mathbb{G}$ has $n$ elements and $\mathbb{H}$ has $n^{\prime}$ elements, $\mathbb{G} \times \mathbb{H}$ has $n \cdot n^{\prime}$ elements. The group operation $\circ$ on $\mathbb{G} \times \mathbb{H}$ is applied component-wise; that is:

本节旨在用同构的语言更好地理解：当 $N = pq$ 为两个不同素数的乘积时，$\mathbb{Z}_N$ 与 $\mathbb{Z}_N^*$ 的群结构。为此首先需要引入群的直积的概念。给定群 $\mathbb{G}$、$\mathbb{H}$，其群运算分别为 $\circ_{\mathbb{G}}$、$\circ_{\mathbb{H}}$，我们如下定义新群 $\mathbb{G} \times \mathbb{H}$（$\mathbb{G}$ 与 $\mathbb{H}$ 的直积）：$\mathbb{G} \times \mathbb{H}$ 的元素是有序对 $(g, h)$，其中 $g \in \mathbb{G}$、$h \in \mathbb{H}$；于是，若 $\mathbb{G}$ 有 $n$ 个元素、$\mathbb{H}$ 有 $n^{\prime}$ 个元素，则 $\mathbb{G} \times \mathbb{H}$ 有 $n \cdot n^{\prime}$ 个元素。$\mathbb{G} \times \mathbb{H}$ 上的群运算 $\circ$ 逐分量进行，即：

$$
(g,h)\circ(g^{\prime},h^{\prime})\stackrel{\mathrm{def}}{=}(g\circ_{\mathbb{G}}g^{\prime},h\circ_{\mathbb{H}}h^{\prime}).
$$

We leave it to Exercise 9.8 to verify that $\mathbb{G} \times \mathbb{H}$ is indeed a group. The above notation can be extended to direct products of more than two groups in the natural way, although we will not need this for what follows.

$\mathbb{G} \times \mathbb{H}$ 确实构成群的验证留作习题 9.8。上述记号还可以自然地推广到多于两个群的直积，不过后续内容并不需要。

We may now state and prove the Chinese remainder theorem.

现在可以陈述并证明中国剩余定理了。

THEOREM 9.24 (Chinese remainder theorem) Let N = pq where p, q > 1 are relatively prime. Then

定理 9.24　（中国剩余定理）设 $N = pq$，其中 $p, q > 1$ 且互素。那么

$$
\mathbb{Z}_{N}\simeq\mathbb{Z}_{p}\times\mathbb{Z}_{q}\quad\text{and}\quad\mathbb{Z}_{N}^{*}\simeq\mathbb{Z}_{p}^{*}\times\mathbb{Z}_{q}^{*}.
$$

Moreover, let $f$ be the function mapping elements $x \in \{0, \ldots, N-1\}$ to pairs $(x_p, x_q)$ with $x_p \in \{0, \ldots, p-1\}$ and $x_q \in \{0, \ldots, q-1\}$ defined by

此外，设 $f$ 是把元素 $x \in \{0, \ldots, N-1\}$ 映为数对 $(x_p, x_q)$（其中 $x_p \in \{0, \ldots, p-1\}$、$x_q \in \{0, \ldots, q-1\}$）的函数，定义为

$$
f(x)\stackrel{\mathrm{def}}{=}([x\bmod p],[x\bmod q]).
$$

Then $f$ is an isomorphism from $\mathbb{Z}_N$ to $\mathbb{Z}_p \times \mathbb{Z}_q$, and the restriction of $f$ to $\mathbb{Z}_N^*$ is an isomorphism from $\mathbb{Z}_N^*$ to $\mathbb{Z}_p^* \times \mathbb{Z}_q^*$.

那么 $f$ 是从 $\mathbb{Z}_N$ 到 $\mathbb{Z}_p \times \mathbb{Z}_q$ 的同构，并且 $f$ 在 $\mathbb{Z}_N^*$ 上的限制是从 $\mathbb{Z}_N^*$ 到 $\mathbb{Z}_p^* \times \mathbb{Z}_q^*$ 的同构。

PROOF For any $x \in \mathbb{Z}_N$ the output $f(x)$ is a pair of elements $(x_p, x_q)$ with $x_p \in \mathbb{Z}_p$ and $x_q \in \mathbb{Z}_q$. We claim that if $x \in \mathbb{Z}_N^*$, then $(x_p, x_q) \in \mathbb{Z}_p^* \times \mathbb{Z}_q^*$. Indeed, if $x_p \notin \mathbb{Z}_p^*$ then this means that $\gcd([x \bmod p], p) \neq 1$. But then $\gcd(x, p) \neq 1$. This implies $\gcd(x, N) \neq 1$, contradicting the assumption that $x \in \mathbb{Z}_N^*$. (An analogous argument holds if $x_q \notin \mathbb{Z}_q^*$.)

证明　对任意 $x \in \mathbb{Z}_N$，输出 $f(x)$ 是一对元素 $(x_p, x_q)$，其中 $x_p \in \mathbb{Z}_p$、$x_q \in \mathbb{Z}_q$。我们断言：若 $x \in \mathbb{Z}_N^*$，则 $(x_p, x_q) \in \mathbb{Z}_p^* \times \mathbb{Z}_q^*$。确实如此：若 $x_p \notin \mathbb{Z}_p^*$，则意味着 $\gcd([x \bmod p], p) \neq 1$，进而有 $\gcd(x, p) \neq 1$。这意味着 $\gcd(x, N) \neq 1$，与 $x \in \mathbb{Z}_N^*$ 的假设矛盾。（若 $x_q \notin \mathbb{Z}_q^*$，同理可证。）

We now show that $f$ is an isomorphism from $\mathbb{Z}_N$ to $\mathbb{Z}_p \times \mathbb{Z}_q$. (The proof that it is an isomorphism from $\mathbb{Z}_N^*$ to $\mathbb{Z}_p^* \times \mathbb{Z}_q^*$ is similar.) Let us start by proving that $f$ is one-to-one. Say $f(x) = (x_p, x_q) = f(x^{\prime})$. Then $x = x_p = x^{\prime} \bmod p$ and $x = x_q = x^{\prime} \bmod q$. This in turn implies that $(x - x^{\prime})$ is divisible by both $p$ and $q$. Since $\gcd(p, q) = 1$, Proposition 9.4 says that $pq = N$ divides $(x - x^{\prime})$. But then $x = x^{\prime} \bmod N$. For $x, x^{\prime} \in \mathbb{Z}_N$, this means that $x = x^{\prime}$ and so $f$ is indeed one-to-one. Since $|\mathbb{Z}_N| = N = p \cdot q = |\mathbb{Z}_p| \cdot |\mathbb{Z}_q|$, the sizes of $\mathbb{Z}_N$ and $\mathbb{Z}_p \times \mathbb{Z}_q$ are the same. This in combination with the fact that $f$ is one-to-one implies that $f$ is bijective.

现在证明 $f$ 是从 $\mathbb{Z}_N$ 到 $\mathbb{Z}_p \times \mathbb{Z}_q$ 的同构。（它是从 $\mathbb{Z}_N^*$ 到 $\mathbb{Z}_p^* \times \mathbb{Z}_q^*$ 的同构的证明类似。）先证 $f$ 是单射。设 $f(x) = (x_p, x_q) = f(x^{\prime})$，则 $x = x_p = x^{\prime} \bmod p$ 且 $x = x_q = x^{\prime} \bmod q$。进而这意味着 $(x - x^{\prime})$ 同时被 $p$ 和 $q$ 整除。由于 $\gcd(p, q) = 1$，由命题 9.4 可知 $pq = N$ 整除 $(x - x^{\prime})$，于是 $x = x^{\prime} \bmod N$。而对 $x, x^{\prime} \in \mathbb{Z}_N$ 来说，这就意味着 $x = x^{\prime}$，故 $f$ 确实是单射。又因为 $|\mathbb{Z}_N| = N = p \cdot q = |\mathbb{Z}_p| \cdot |\mathbb{Z}_q|$，$\mathbb{Z}_N$ 与 $\mathbb{Z}_p \times \mathbb{Z}_q$ 的大小相同；结合 $f$ 为单射的事实可知 $f$ 是双射。

In the following paragraph, let $+_N$ denote addition modulo $N$, and let $\boxplus$ denote the group operation in $\mathbb{Z}_p \times \mathbb{Z}_q$ (i.e., addition modulo $p$ in the first component and addition modulo $q$ in the second component). To conclude the proof that $f$ is an isomorphism from $\mathbb{Z}_N$ to $\mathbb{Z}_p \times \mathbb{Z}_q$, we need to show that for all $a, b \in \mathbb{Z}_N$ it holds that $f(a +_N b) = f(a) \boxplus f(b)$.

在下一段中，令 $+_N$ 表示模 $N$ 加法，令 $\boxplus$ 表示 $\mathbb{Z}_p \times \mathbb{Z}_q$ 中的群运算（即第一个分量做模 $p$ 加法、第二个分量做模 $q$ 加法）。为完成“$f$ 是从 $\mathbb{Z}_N$ 到 $\mathbb{Z}_p \times \mathbb{Z}_q$ 的同构”的证明，还需证明：对所有 $a, b \in \mathbb{Z}_N$ 都有 $f(a +_N b) = f(a) \boxplus f(b)$。

To see that this is true, note that

为验证这一点，注意

$$
\begin{aligned}
f(a+_{N} b)&=\left(\left[(a+_{N} b)\bmod p\right],\left[(a+_{N} b)\bmod q\right]\right)\\
&=\left(\left[(a+b)\bmod p\right],\left[(a+b)\bmod q\right]\right)\\
&=\left(\left[a\bmod p\right],\left[a\bmod q\right]\right)\boxplus\left(\left[b\bmod p\right],\left[b\bmod q\right]\right)=f(a)\boxplus f(b).
\end{aligned}
$$

(For the second equality, above, we use the fact that $[[X \bmod N] \bmod p] = [[X \bmod p] \bmod p]$ when $p \mid N$; see Exercise 9.9.)

（上面第二个等号用到了如下事实：当 $p \mid N$ 时 $[[X \bmod N] \bmod p] = [[X \bmod p] \bmod p]$；见习题 9.9。）

An extension of the Chinese remainder theorem says that if $p_1, p_2, \ldots, p_\ell$ are pairwise relatively prime (i.e., $\gcd(p_i, p_j) = 1$ for all $i \neq j$) and $N \overset{\mathrm{def}}{=} \prod_{i=1}^\ell p_i$, then

中国剩余定理的一个推广是：若 $p_1, p_2, \ldots, p_\ell$ 两两互素（即对所有 $i \neq j$ 都有 $\gcd(p_i, p_j) = 1$），且 $N \overset{\mathrm{def}}{=} \prod_{i=1}^\ell p_i$，则

$$
\mathbb{Z}_{N}\simeq\mathbb{Z}_{p_{1}}\times\cdots\times\mathbb{Z}_{p_{\ell}}\quad\text{and}\quad\mathbb{Z}_{N}^{*}\simeq\mathbb{Z}_{p_{1}}^{*}\times\cdots\times\mathbb{Z}_{p_{\ell}}^{*}.
$$

An isomorphism in each case is obtained by a natural extension of the one used in the theorem above.

两种情形下的同构都可由上面定理中所用的同构自然推广而得到。

By way of notation, with $N$ understood and $x \in \{0,1,\ldots,N-1\}$ we write $x \leftrightarrow (x_p, x_q)$ for $x_p = [x \bmod p]$ and $x_q = [x \bmod q]$. That is, $x \leftrightarrow (x_p, x_q)$ if and only if $f(x) = (x_p, x_q)$, where $f$ is as in the theorem above. One way to think about this notation is that it means “$x$ (in $\mathbb{Z}_N$) corresponds to $(x_p, x_q)$ (in $\mathbb{Z}_p \times \mathbb{Z}_q)$.” The same notation is used when dealing with $x \in \mathbb{Z}_N$.

关于记号：在 $N$ 已明确的前提下，对 $x \in \{0,1,\ldots,N-1\}$，若 $x_p = [x \bmod p]$ 且 $x_q = [x \bmod q]$，则写作 $x \leftrightarrow (x_p, x_q)$。也就是说，$x \leftrightarrow (x_p, x_q)$ 当且仅当 $f(x) = (x_p, x_q)$，其中 $f$ 如上述定理所示。理解这一记号的一种方式是：它表示“$x$（在 $\mathbb{Z}_N$ 中）对应于 $(x_p, x_q)$（在 $\mathbb{Z}_p \times \mathbb{Z}_q$ 中）”。处理 $x \in \mathbb{Z}_N$ 时也使用同样的记号。

**Example 9.25**　**例 9.25**

Take ${15} = 5 \cdot 3$, and consider $\mathbb{Z}_{15}^* = \{1,2,4,7,8,11,13,14\}$. The Chinese remainder theorem says this group is isomorphic to $\mathbb{Z}_5^* \times \mathbb{Z}_3^*$. We can compute

取 ${15} = 5 \cdot 3$，并考虑 $\mathbb{Z}_{15}^* = \{1,2,4,7,8,11,13,14\}$。中国剩余定理表明这个群同构于 $\mathbb{Z}_5^* \times \mathbb{Z}_3^*$。我们可以计算出

$$
\begin{array}{c}
1\leftrightarrow(1,1)\quad2\leftrightarrow(2,2)\quad4\leftrightarrow(4,1)\quad7\leftrightarrow(2,1)\\
8\leftrightarrow(3,2)\quad11\leftrightarrow(1,2)\quad13\leftrightarrow(3,1)\quad14\leftrightarrow(4,2)
\end{array}
$$

where each pair $(a, b)$ with $a \in \mathbb{Z}_5^*$ and $b \in \mathbb{Z}_3^*$ appears exactly once.

其中每个数对 $(a, b)$（$a \in \mathbb{Z}_5^*$，$b \in \mathbb{Z}_3^*$）恰好出现一次。

#### Using the Chinese Remainder Theorem　中国剩余定理的使用

If two groups are isomorphic, then they both serve as representations of the same underlying “algebraic structure.” Nevertheless, the choice of which representation to use can affect the computational efficiency of group operations. We discuss this abstractly, and then in the specific context of $\mathbb{Z}_N$ and $\mathbb{Z}_N^*$.

若两个群同构，则二者都是同一个底层“代数结构”的表示。尽管如此，选用哪一种表示会影响群运算的计算效率。我们先抽象地讨论这一点，然后再放到 $\mathbb{Z}_N$ 与 $\mathbb{Z}_N^*$ 的具体情境中来看。

Let $\mathbb{G}$, $\mathbb{H}$ be groups with operations $\circ_{\mathbb{G}}$, $\circ_{\mathbb{H}}$, respectively, and say $f$ is an isomorphism from $\mathbb{G}$ to $\mathbb{H}$ where both $f$ and $f^{-1}$ can be computed efficiently. Then for $g_1, g_2 \in \mathbb{G}$ we can compute $g = g_1 \circ_{\mathbb{G}} g_2$ in two ways: either by directly computing the group operation in $\mathbb{G}$, or via the following steps:

设 $\mathbb{G}$、$\mathbb{H}$ 分别是带有运算 $\circ_{\mathbb{G}}$、$\circ_{\mathbb{H}}$ 的群，并设 $f$ 是从 $\mathbb{G}$ 到 $\mathbb{H}$ 的同构，且 $f$ 与 $f^{-1}$ 都能高效计算。那么对 $g_1, g_2 \in \mathbb{G}$，我们可以用两种方式计算 $g = g_1 \circ_{\mathbb{G}} g_2$：要么直接在 $\mathbb{G}$ 中执行群运算，要么经由以下步骤：

1. Compute $h_{1} = f(g_{1})$ and $h_{2} = f(g_{2})$;

   计算 $h_{1} = f(g_{1})$ 与 $h_{2} = f(g_{2})$；

2. Compute $h = h_1 \circ_{\mathbb{H}} h_2$ using the group operation in $\mathbb{H}$;

   用 $\mathbb{H}$ 中的群运算计算 $h = h_1 \circ_{\mathbb{H}} h_2$；

3. Compute $g = f^{-1}(h)$.

   计算 $g = f^{-1}(h)$。

The above extends in the natural way when we want to compute multiple group operations in $\mathbb{G}$ (e.g., to compute $g^x$ for some integer $x$). Which method is better depends on the relative efficiency of computing the group operation in each group, as well as the efficiency of computing $f$ and $f^{-1}$.

当我们想在 $\mathbb{G}$ 中连续计算多次群运算时（例如对某个整数 $x$ 计算 $g^x$），上述做法可以自然推广。哪种方法更好，取决于在各个群中执行群运算的相对效率，以及计算 $f$ 与 $f^{-1}$ 本身的效率。

We now turn to the specific case of computations modulo $N$, when $N = pq$ is a product of distinct primes. The Chinese remainder theorem shows that addition, multiplication, or exponentiation (which is just repeated multiplication) modulo $N$ can be “transformed” to analogous operations modulo $p$ and $q$. Building on Example 9.25, we show some simple examples with $N = 15$.

现在转向模 $N$ 计算的具体情形，其中 $N = pq$ 是不同素数的乘积。中国剩余定理表明：模 $N$ 的加法、乘法或幂运算（幂不过是反复相乘）都可以“转化”为模 $p$ 和模 $q$ 下的相应运算。在例 9.25 的基础上，我们给出几个 $N = 15$ 的简单例子。

**Example 9.26**　**例 9.26**

Say we want to compute the product ${14} \cdot 13$ modulo 15 (i.e., in $\mathbb{Z}_{15}^*$). Example 9.25 gives ${14} \leftrightarrow (4,2)$ and ${13} \leftrightarrow (3,1)$. In $\mathbb{Z}_5^* \times \mathbb{Z}_3^*$, we have

假设我们要计算乘积 ${14} \cdot 13$ 模 15 的结果（即在 $\mathbb{Z}_{15}^*$ 中）。由例 9.25 知 ${14} \leftrightarrow (4,2)$、${13} \leftrightarrow (3,1)$。在 $\mathbb{Z}_5^* \times \mathbb{Z}_3^*$ 中，

$$
(4,2)\cdot(3,1)=([4\cdot3\bmod5],[2\cdot1\bmod3])=(2,2).
$$

Note $(2,2) \leftrightarrow 2$, which is the correct answer since ${14} \cdot 13 = 2 \mod 15$.

注意到 $(2,2) \leftrightarrow 2$，这正是正确答案，因为 ${14} \cdot 13 = 2 \mod 15$。

**Example 9.27**　**例 9.27**

Say we want to compute ${11}^{53} \mod 15$. Example 9.25 gives ${11} \leftrightarrow (1, 2)$. Notice that ${2} = -1 \mod 3$ and so

假设我们要计算 ${11}^{53} \mod 15$。由例 9.25 知 ${11} \leftrightarrow (1, 2)$。注意到 ${2} = -1 \mod 3$，于是

$$
(1,2)^{53}=([1^{53}\bmod5],[(-1)^{53}\bmod3])=(1,[-1\bmod3])=(1,2).
$$

Thus, ${11}^{53}$ mod 15 = 11.

因此 ${11}^{53}$ mod 15 = 11。

**Example 9.28**　**例 9.28**

Say we want to compute $[29^{100} \mod 35]$. We first compute the correspondence ${29} \leftrightarrow ([29 \mod 5], [29 \mod 7]) = ([-1 \mod 5], 1)$. Using the Chinese remainder theorem, we have

假设我们要计算 $[29^{100} \mod 35]$。先求出对应关系 ${29} \leftrightarrow ([29 \mod 5], [29 \mod 7]) = ([-1 \mod 5], 1)$。利用中国剩余定理，有

$$
([-1\bmod5],1)^{100}=([(-1)^{100}\bmod5],[1^{100}\bmod7])=(1,1),
$$

and it is immediate that $(1,1)\leftrightarrow 1$. We conclude that $[29^{100}\bmod 35]=1$.

并且显然有 $(1,1)\leftrightarrow 1$。我们得出 $[29^{100}\bmod 35]=1$。

**Example 9.29**　**例 9.29**

Say we want to compute $[18^{25} \bmod 35]$. We have ${18} \leftrightarrow (3,4)$ and so

假设我们要计算 $[18^{25} \bmod 35]$。由 ${18} \leftrightarrow (3,4)$ 可知

$$
{18}^{25}\bmod{35}\leftrightarrow(3,4)^{25}=([3^{25}\bmod{5}],[4^{25}\bmod{7}]).
$$

Since $\mathbb{Z}_5^*$ is a group of order 4, we can “work modulo 4 in the exponent” (cf. Corollary 9.15) and see that

由于 $\mathbb{Z}_5^*$ 是阶为 4 的群，我们可以“在指数上模 4 进行运算”（参见推论 9.15），从而

$$
{3}^{25}=3^{[25\bmod4]}=3^{1}=3\bmod5.
$$

Similarly,

类似地，

$$
{4}^{25}=4^{[25\bmod6]}=4^{1}=4\bmod7.
$$

Thus, $([3^{25} \bmod 5], [4^{25} \bmod 7]) = (3, 4) \leftrightarrow 18$ and so $[18^{25} \bmod 35] = 18$.

于是 $([3^{25} \bmod 5], [4^{25} \bmod 7]) = (3, 4) \leftrightarrow 18$，故 $[18^{25} \bmod 35] = 18$。

One thing we have not yet discussed is how to convert back and forth between the representation of an element modulo $N$ and its representation modulo $p$ and $q$. The conversion can be carried out efficiently provided the factorization of $N$ is known. Assuming $p$ and $q$ are known, it is easy to map an element $x$ modulo $N$ to its corresponding representation modulo $p$ and $q$: the element x corresponds to ([x mod p], [x mod q]), and both the modular reductions can be carried out efficiently (cf. Appendix B.2).

还有一个尚未讨论的问题：如何在元素的模 $N$ 表示与其模 $p$、模 $q$ 表示之间来回转换。只要知道 $N$ 的分解，转换就能高效完成。假定 $p$ 和 $q$ 已知，把模 $N$ 的元素 $x$ 映到其对应的模 $p$、模 $q$ 表示很容易：元素 $x$ 对应于 $([x \bmod p], [x \bmod q])$，而这两次模归约都能高效完成（参见附录 B.2）。

For the other direction, we make use of the following observation: an element with representation $(x_{p}, x_{q})$ can be written as

反方向的转换则利用以下观察：具有表示 $(x_{p}, x_{q})$ 的元素可以写为

$$
(x_{p},x_{q})=x_{p}\cdot(1,0)+x_{q}\cdot(0,1).
$$

So, if we can find elements ${1}_p, 1_q \in \{0, \ldots, N-1\}$ such that ${1}_p \leftrightarrow (1,0)$ and ${1}_q \leftrightarrow (0,1)$, then (appealing to the Chinese remainder theorem) we know that

于是，如果能找到元素 ${1}_p, 1_q \in \{0, \ldots, N-1\}$ 使得 ${1}_p \leftrightarrow (1,0)$ 且 ${1}_q \leftrightarrow (0,1)$，那么（借助中国剩余定理）我们知道

$$
(x_{p},x_{q})\leftrightarrow[(x_{p}\cdot 1_{p}+x_{q}\cdot 1_{q})\bmod N].
$$

Since $p, q$ are distinct primes, $\gcd(p, q) = 1$. We can use the extended Euclidean algorithm (cf. Appendix B.1.2) to find integers $X, Y$ such that

由于 $p, q$ 是不同的素数，$\gcd(p, q) = 1$。我们可以用扩展欧几里得算法（参见附录 B.1.2）找到整数 $X, Y$ 使得

$$
Xp+Yq=1.
$$

Note that $Yq = 0 \bmod q$ and $Yq = 1 - Xp = 1 \bmod p$. This means that $[Yq \bmod N] \leftrightarrow (1,0)$; i.e., $[Yq \bmod N] = 1_p$. Similarly, $[Xp \bmod N] = 1_q$.

注意 $Yq = 0 \bmod q$，且 $Yq = 1 - Xp = 1 \bmod p$。这意味着 $[Yq \bmod N] \leftrightarrow (1,0)$，即 $[Yq \bmod N] = 1_p$。类似地，$[Xp \bmod N] = 1_q$。

In summary, we can convert an element represented as $(x_p, x_q)$ to its representation modulo $N$ in the following way (assuming $p$ and $q$ are known):

总结起来，可以把表示为 $(x_p, x_q)$ 的元素按下述方式转换为模 $N$ 的表示（假定 $p$ 和 $q$ 已知）：

1. Compute $X, Y$ such that $Xp + Yq = 1$.

   计算 $X, Y$ 使得 $Xp + Yq = 1$。

2. Set ${1}_{p} := [Y q \bmod N]$ and ${1}_{q} := [X p \bmod N]$.

   令 ${1}_{p} := [Y q \bmod N]$，${1}_{q} := [X p \bmod N]$。

3. Compute $x := [(x_p \cdot 1_p + x_q \cdot 1_q) \mod N]$.

   计算 $x := [(x_p \cdot 1_p + x_q \cdot 1_q) \mod N]$。

If many such conversions will be performed, then ${1}_{p}, 1_{q}$ can be computed once-and-for-all in a preprocessing phase.

若要执行很多次这样的转换，则 ${1}_{p}, 1_{q}$ 可以在预处理阶段一次性算好。

**Example 9.30**　**例 9.30**

Take $p = 5$, $q = 7$, and $N = 5 \cdot 7 = 35$. Say we are given the representation $(4,3)$ and want to convert this to the corresponding element of $\mathbb{Z}_{35}$. Using the extended Euclidean algorithm, we compute

取 $p = 5$、$q = 7$、$N = 5 \cdot 7 = 35$。假设给定表示 $(4,3)$，希望把它转换为 $\mathbb{Z}_{35}$ 中对应的元素。利用扩展欧几里得算法，可计算得

$$
{3}\cdot5-2\cdot7=1.
$$

Thus, ${1}_p = [-2 \cdot 7 \mod 35] = 21$ and ${1}_q = [3 \cdot 5 \mod 35] = 15$. (We can check that these are correct: e.g., for ${1}_p = 21$ we can verify that $[21 \mod 5] = 1$ and $[21 \mod 7] = 0$.) Using these values, we can then compute

于是 ${1}_p = [-2 \cdot 7 \mod 35] = 21$，${1}_q = [3 \cdot 5 \mod 35] = 15$。（可以核验它们是正确的：例如对 ${1}_p = 21$，可验证 $[21 \mod 5] = 1$ 且 $[21 \mod 7] = 0$。）利用这些值便可计算

$$
\begin{aligned}
(4,3)&=4\cdot(1,0)+3\cdot(0,1)\\
&\leftrightarrow[4\cdot1_{p}+3\cdot1_{q}\bmod35]\\
&=[4\cdot21+3\cdot15\bmod35]=24.
\end{aligned}
$$

Since 24 = 4 mod 5 and 24 = 3 mod 7, this is indeed the correct result.

由于 24 = 4 mod 5 且 24 = 3 mod 7，这确实是正确的结果。
