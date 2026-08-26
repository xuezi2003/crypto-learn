# Chapter 15: *Advanced Topics in Public-Key Encryption*　第 15 章　公钥加密的高级主题

In Chapter 12 we saw several examples of public-key encryption schemes used in practice. Here, we explore some schemes that are currently more of theoretical interest—although in some cases it is possible that these schemes (or variants thereof) will be used more widely in the future.

在第 12 章中，我们看到了若干实际使用的公钥加密方案。本章将探讨一些目前更多停留在理论兴趣层面的方案——尽管在某些情形下，这些方案（或其变体）未来有可能得到更广泛的应用。

We begin with a treatment of trapdoor permutations, a generalization of one-way permutations, and show how to use them to construct public-key encryption schemes. Trapdoor permutations neatly encapsulate the key characteristics of the RSA permutation that make it so useful. As such, they often provide a useful abstraction for designing new cryptosystems.

我们首先讨论陷门置换——单向置换的一种推广——并展示如何用它构造公钥加密方案。陷门置换凝练地刻画了 RSA 置换之所以如此有用的关键特性，因此常常为设计新的密码体制提供一种有用的抽象。

Next, we present three schemes based on problems related to factoring:

接下来，我们介绍三个基于与因子分解相关问题的方案：

- The Paillier encryption scheme is an example of an encryption scheme that is homomorphic. This property turns out to be useful for constructing more-complex cryptographic protocols, something we touch on briefly in Section 15.3.
- Paillier 加密方案是同态加密方案的一个例子。这一性质对构造更复杂的密码协议很有用，我们将在 15.3 节简要谈及这一点。

- The Goldwasser–Micali encryption scheme is of historical interest as the first scheme to be proven CPA-secure. It is also homomorphic, and uses some interesting number theory that can be applied in other contexts.
- Goldwasser–Micali 加密方案具有历史意义：它是第一个被证明满足选择明文安全的方案。它也是同态的，并且用到了一些可用于其他场合的有趣数论。

- Finally, we discuss the Rabin trapdoor permutation, which can be used to construct a public-key encryption scheme. Although superficially similar to the RSA trapdoor permutation, the Rabin trapdoor permutation is distinguished by the fact that its security is based directly on the hardness of factoring. (Recall from Section 9.2.5 that hardness of the RSA problem appears to be a stronger assumption.)
- 最后，我们讨论 Rabin 陷门置换，可以用它构造公钥加密方案。尽管表面上与 RSA 陷门置换相似，Rabin 陷门置换的突出之处在于其安全性直接建立在因子分解的困难性之上。（回顾 9.2.5 节可知，RSA 问题的困难性似乎是一个更强的假设。）

## 15.1 Encryption from Trapdoor Permutations　由陷门置换构造加密

In Section 12.5.3 we saw how to construct a CPA-secure public-key encryption scheme based on the RSA assumption. By distilling those properties of RSA that are used in the construction, and defining an abstract notion that encapsulates those properties, we obtain a general template for constructing secure encryption schemes based on any primitive satisfying the same set of properties. Trapdoor permutations turn out to be the “right” abstraction here.

在 12.5.3 节中，我们看到如何基于 RSA 假设构造一个选择明文安全的公钥加密方案。通过提炼 RSA 在该构造中所用到的那些性质，并定义一个刻画这些性质的抽象概念，我们就得到了一个通用模板，可以基于任何满足同一组性质的原语来构造安全的加密方案。陷门置换正是这里“恰当的”抽象。

In the following section we define (families of) trapdoor permutations and observe that the RSA family of one-way permutations (Construction 9.77) satisfies the additional requirements needed to be a family of trapdoor permutations. In Section 15.1.2 we generalize the construction from Section 12.5.3 and show that public-key encryption can be constructed from any trapdoor permutation. These results will be used again in Section 15.5, where we show a second example of a trapdoor permutation, this time based directly on the factoring assumption.

在接下来的一小节中，我们定义陷门置换（族），并看到 RSA 单向置换族（构造 9.77）满足成为陷门置换族所需的额外要求。在 15.1.2 节中，我们把 12.5.3 节的构造加以推广，证明可以由任意陷门置换构造公钥加密。这些结果还将在 15.5 节再次用到，届时我们将给出陷门置换的第二个例子，这一次直接建立在因子分解假设之上。

In this section we rely on the material from Section 9.4.1 or, alternately, Chapter 8.

本节内容依赖于 9.4.1 节（或第 8 章）的材料。

### 15.1.1 Trapdoor Permutations　陷门置换

Recall the definitions of families of functions and families of one-way permutations from Section 9.4.1. In that section, we showed that the RSA assumption naturally gives rise to a family of one-way permutations. The astute reader may have noticed that the construction we gave (Construction 9.77) has a special property that was not remarked upon there: namely, the parameter-generation algorithm Gen outputs some additional information along with I that enables efficient inversion of $f_1$. We refer to such additional information as a trapdoor, and call families of one-way permutations with this additional property families of trapdoor permutations. A formal definition follows.

回顾 9.4.1 节中函数族与单向置换族的定义。在该节中我们说明了，RSA 假设自然地给出一个单向置换族。细心的读者可能已经注意到，我们给出的构造（构造 9.77）有一个当时未曾指出的特殊性质：参数生成算法 $\mathsf{Gen}$ 在输出 $I$ 的同时，还输出一些额外信息，使得对 $f_I$ 的高效求逆成为可能。我们把这种额外信息称为陷门，并把具有这一附加性质的单向置换族称为陷门置换族。下面给出正式定义。

DEFINITION 15.1 A tuple of polynomial-time algorithms (Gen, Samp, f, Inv) is a family of trapdoor permutations (or a trapdoor permutation) if:

定义 15.1　设 $(\mathsf{Gen}, \mathsf{Samp}, f, \mathsf{Inv})$ 为一组多项式时间算法，若满足下列条件，则称其为一个陷门置换族（或简称陷门置换）：

- The probabilistic parameter-generation algorithm Gen, on input ${1}^n$, outputs $(I, \mathsf{td})$ with $|I| \geq n$. Each value of $I$ defines a set $\mathcal{D}_I$ that constitutes the domain and range of a permutation (i.e., bijection) $f_I : \mathcal{D}_I \to \mathcal{D}_I$.
- 概率参数生成算法 $\mathsf{Gen}$ 以 ${1}^n$ 为输入，输出 $(I, \mathsf{td})$，其中 $|I| \geq n$。每个 $I$ 的值定义一个集合 $\mathcal{D}_I$，它同时是一个置换（即双射）$f_I : \mathcal{D}_I \to \mathcal{D}_I$ 的定义域和值域。

Let $\mathsf{Gen}_{1}$ denote the algorithm that results by running Gen and outputting only I. Then ($\mathsf{Gen}_{1}$, Samp, f) is a family of one-way permutations.

记 $\mathsf{Gen}_{1}$ 为运行 $\mathsf{Gen}$ 但只输出 $I$ 所得的算法。那么 $(\mathsf{Gen}_{1}, \mathsf{Samp}, f)$ 是一个单向置换族。

- Let $(I, \mathsf{td})$ be an output of $\mathsf{Gen}(1^n)$. The deterministic inverting algorithm $\mathsf{Inv}$, on input $\mathsf{td}$ and $y \in \mathcal{D}_I$, outputs $x \in \mathcal{D}_I$. We denote this by $x := \mathsf{Inv}_{\mathsf{td}}(y)$. It is required that with all but negligible probability over $(I, \mathsf{td})$ output by $\mathsf{Gen}(1^n)$ and uniform choice of $x \in \mathcal{D}_I$, we have
- 设 $(I, \mathsf{td})$ 为 $\mathsf{Gen}(1^n)$ 的输出。确定性求逆算法 $\mathsf{Inv}$ 以 $\mathsf{td}$ 和 $y \in \mathcal{D}_I$ 为输入，输出 $x \in \mathcal{D}_I$，记作 $x := \mathsf{Inv}_{\mathsf{td}}(y)$。要求：除可忽略的概率外，对 $\mathsf{Gen}(1^n)$ 输出的 $(I, \mathsf{td})$ 与均匀选取的 $x \in \mathcal{D}_I$，都有

$$
\mathsf{Inv}_{\mathsf{td}}(f_{I}(x))=x.
$$

As shorthand, we drop explicit mention of $\mathsf{Samp}$ and simply refer to trap-door permutation $(\mathsf{Gen}, f, \mathsf{Inv})$. For $(I, \mathsf{td})$ output by $\mathsf{Gen}$ we write $x \leftarrow \mathcal{D}_I$ to denote uniform selection of $x \in \mathcal{D}_I$ (with the understanding that this is done by algorithm *Samp*).

作为简写，我们不再显式提及 $\mathsf{Samp}$，而直接称陷门置换 $(\mathsf{Gen}, f, \mathsf{Inv})$。对于 $\mathsf{Gen}$ 输出的 $(I, \mathsf{td})$，我们用 $x \leftarrow \mathcal{D}_I$ 表示均匀选取 $x \in \mathcal{D}_I$（默认这一步由算法 *Samp* 完成）。

The second condition above implies that $f_{I}$ cannot be efficiently inverted without td, but the final condition means that $f_{I}$ can be efficiently inverted with td. It is immediate that Construction 9.77 can be modified to give a family of trapdoor permutations if the RSA problem is hard relative to GenRSA, and so we refer to that construction as the RSA trapdoor permutation.

上面的第二个条件意味着：没有 $\mathsf{td}$ 就无法高效地求逆 $f_{I}$；而最后一个条件则意味着：有了 $\mathsf{td}$ 就可以高效地求逆 $f_{I}$。由此立即可知，若 RSA 问题相对于 $\mathsf{GenRSA}$ 是困难的，则可以将构造 9.77 修改为一个陷门置换族，因此我们称该构造为 RSA 陷门置换。

### 15.1.2 Public-Key Encryption from Trapdoor Permutations　由陷门置换构造公钥加密

We now sketch how a public-key encryption scheme can be constructed from an arbitrary family of trapdoor permutations. The construction is simply a generalization of what was already done for the specific RSA trapdoor permutation in Section 12.5.3.

我们现在勾勒如何由任意陷门置换族构造公钥加密方案。该构造只是把 12.5.3 节中针对具体 RSA 陷门置换所做的事加以推广。

We begin by (re-)introducing the notion of a hard-core predicate. This is the natural adaptation of Definition 8.4 to our context, and also generalizes our previous discussion of one specific hard-core predicate for the RSA trapdoor permutation in Section 12.5.3.

我们首先（重新）引入难核谓词的概念。它是定义 8.4 在当前语境下的自然变体，也推广了我们在 12.5.3 节中针对 RSA 陷门置换的那个具体难核谓词的讨论。

DEFINITION 15.2 Let $\Pi = (\mathsf{Gen}, f, \mathsf{Inv})$ be a family of trapdoor permutations, and let $\mathsf{hc}$ be a deterministic polynomial-time algorithm that, on input $I$ and $x \in \mathcal{D}_I$, outputs a single bit $\mathsf{hc}_I(x)$. We say that $\mathsf{hc}$ is a hard-core predicate of $\Pi$ if for every probabilistic polynomial-time algorithm $\mathcal{A}$ there is a negligible function $\mathsf{negl}$ such that

定义 15.2　设 $\Pi = (\mathsf{Gen}, f, \mathsf{Inv})$ 是一个陷门置换族，$\mathsf{hc}$ 是一个确定性多项式时间算法，以 $I$ 和 $x \in \mathcal{D}_I$ 为输入，输出单个比特 $\mathsf{hc}_I(x)$。若对每一个概率多项式时间算法 $\mathcal{A}$，都存在可忽略函数 $\mathsf{negl}$ 使得

$$
\Pr[\mathcal{A}(I,f_{I}(x))=\mathsf{hc}_{I}(x)]\leq\frac{1}{2}+\mathsf{negl}(n),
$$

where the probability is taken over the experiment in which $\mathsf{Gen}(1^{n})$ is run to generate $(I, \mathsf{td})$ and then $x$ is chosen uniformly from $\mathcal{D}_{I}$.

则称 $\mathsf{hc}$ 是 $\Pi$ 的一个难核谓词；上式中的概率取自如下实验：运行 $\mathsf{Gen}(1^{n})$ 生成 $(I, \mathsf{td})$，然后从 $\mathcal{D}_{I}$ 中均匀选取 $x$。

The asymmetry provided by trapdoor permutations implies that anyone who knows the trapdoor $\mathsf{td}$ associated with $I$ can recover $x$ from $f_I(x)$ and thus compute $\mathsf{hc}_I(x)$ from $f_I(x)$. But given only $I$, it is infeasible to compute $\mathsf{hc}_I(x)$ from $f_I(x)$ for a uniform $x$.

陷门置换提供的不对称性意味着：任何知道与 $I$ 相关联的陷门 $\mathsf{td}$ 的人，都能从 $f_I(x)$ 恢复 $x$，从而由 $f_I(x)$ 计算出 $\mathsf{hc}_I(x)$；但若只给定 $I$，对均匀选取的 $x$，由 $f_I(x)$ 计算 $\mathsf{hc}_I(x)$ 是不可行的。

The following can be proved by a suitable modification of Theorem 8.5:

对定理 8.5 作适当修改即可证明下面的结论：

THEOREM 15.3 Given a family of trapdoor permutations $\Pi$, there is a family of trapdoor permutations $\widehat{\Pi}$ with a hard-core predicate $\mathsf{hc}$ for $\widehat{\Pi}$.

定理 15.3　给定一个陷门置换族 $\Pi$，存在一个陷门置换族 $\widehat{\Pi}$ 以及 $\widehat{\Pi}$ 的难核谓词 $\mathsf{hc}$。

Given a family of trapdoor permutations $\Pi = (\mathsf{Gen}, f, \mathsf{Inv})$ with hard-core predicate $\mathsf{hc}$, we can construct a single-bit encryption scheme via the following approach (see Construction 15.4 below, and compare to Construction 12.32): To generate keys, run $\widehat{\mathsf{Gen}}(1^n)$ to obtain $(I, \mathsf{td})$; the public key is $I$ and the private key is $\mathsf{td}$. Given a public key $I$, encryption of a message $m \in \{0,1\}$ works by choosing uniform $r \in \mathcal{D}_I$ subject to the constraint that $\mathsf{hc}_I(r) = m$, and then setting the ciphertext equal to $f_I(r)$. In order to decrypt, the receiver uses td to recover $r$ from $f_I(r)$ and then outputs the message $m := \mathsf{hc}_I(r)$.

给定一个带难核谓词 $\mathsf{hc}$ 的陷门置换族 $\Pi = (\mathsf{Gen}, f, \mathsf{Inv})$，可以按如下方式构造一个单比特加密方案（见下面的构造 15.4，并与构造 12.32 对比）：生成密钥时，运行 $\widehat{\mathsf{Gen}}(1^n)$ 得到 $(I, \mathsf{td})$；公钥为 $I$，私钥为 $\mathsf{td}$。给定公钥 $I$，加密消息 $m \in \{0,1\}$ 的方法是：均匀选取满足约束 $\mathsf{hc}_I(r) = m$ 的 $r \in \mathcal{D}_I$，然后令密文等于 $f_I(r)$。解密时，接收方用 $\mathsf{td}$ 从 $f_I(r)$ 恢复 $r$，然后输出消息 $m := \mathsf{hc}_I(r)$。

**CONSTRUCTION 15.4**

Let $\widehat{\Pi} = (\widehat{\mathsf{Gen}}, f, \mathsf{Inv})$ be a family of trapdoor permutations with hard-core predicate $\mathsf{hc}$. Define a public-key encryption scheme as follows:

- Gen: on input ${1}^n$, run $\widehat{\mathsf{Gen}}(1^n)$ to obtain $(I, \mathsf{td})$. Output the public key $I$ and the private key $\mathsf{td}$.

- Enc: on input a public key $I$ and a message $m \in \{0,1\}$, choose a uniform $r \in \mathcal{D}_I$ subject to the constraint that $\mathsf{hc}_I(r) = m$. Output the ciphertext $c := f_I(r)$.

- Dec: on input a private key td and a ciphertext c, compute the value $r := \mathsf{Inv}_{\mathsf{td}}(c)$ and output the message $\mathsf{hc}_I(r)$.

Public-key encryption from any family of trapdoor permutations.

**构造 15.4**

设 $\widehat{\Pi} = (\widehat{\mathsf{Gen}}, f, \mathsf{Inv})$ 是一个带难核谓词 $\mathsf{hc}$ 的陷门置换族。定义如下的公钥加密方案：

- Gen：以 ${1}^n$ 为输入，运行 $\widehat{\mathsf{Gen}}(1^n)$ 得到 $(I, \mathsf{td})$。输出公钥 $I$ 与私钥 $\mathsf{td}$。

- Enc：以公钥 $I$ 和消息 $m \in \{0,1\}$ 为输入，均匀选取满足约束 $\mathsf{hc}_I(r) = m$ 的 $r \in \mathcal{D}_I$。输出密文 $c := f_I(r)$。

- Dec：以私钥 $\mathsf{td}$ 和密文 $c$ 为输入，计算 $r := \mathsf{Inv}_{\mathsf{td}}(c)$，输出消息 $\mathsf{hc}_I(r)$。

由任意陷门置换族构造的公钥加密。

A proof of security follows along the lines of the proof of Theorem 12.33.

安全性的证明沿用定理 12.33 的证明思路。

THEOREM 15.5 If $\hat{\Pi}$ is a family of trapdoor permutations with hard-core predicate $\mathsf{hc}$, then Construction 15.4 is CPA-secure.

定理 15.5　若 $\widehat{\Pi}$ 是一个带难核谓词 $\mathsf{hc}$ 的陷门置换族，则构造 15.4 是选择明文安全的。

PROOF Let $\Pi$ denote Construction 15.4. We prove that $\Pi$ has indistinguishable encryptions in the presence of an eavesdropper; by Proposition 12.3, this implies it is CPA-secure.

证明　记 $\Pi$ 为构造 15.4。我们证明 $\Pi$ 在窃听者存在时具有不可区分的加密；由命题 12.3，这意味着它是选择明文安全的。

We first observe that hc must be unbiased in the following sense. Let

我们首先注意到，$\mathsf{hc}$ 必须在下述意义下是无偏的。令

$$
\delta_{0}(n)\overset{\mathrm{def}}{=}\Pr_{\scriptstyle(I,\mathsf{td})\leftarrow\widehat{\mathsf{Gen}}(1^{n});x\leftarrow\mathcal{D}_{I}}[\mathsf{hc}_{I}(x)=0]
$$

and

以及

$$
\delta_{1}(n)\overset{\mathrm{def}}{=}\underbrace{\Pr}_{(I,\mathsf{td})\leftarrow\widehat{\mathsf{Gen}}(1^{n});x\leftarrow\mathcal{D}_{I}}[\mathsf{hc}_{I}(x)=1].
$$

Then there is a negligible function $\mathsf{negl}$ such that

那么存在可忽略函数 $\mathsf{negl}$ 使得

$$
\delta_{0}(n),\delta_{1}(n)\geq\frac{1}{2}-\mathsf{negl}(n);
$$

if not, then an attacker who simply outputs the more frequently occurring bit would violate Definition 15.2.

否则，一个仅输出出现频率较高的比特的攻击者就会违反定义 15.2。

Now let $\mathcal{A}$ be a probabilistic polynomial-time adversary. Without loss of generality, we may assume $m_0 = 0$ and $m_1 = 1$ in experiment $\mathsf{PubK}_{\mathcal{A},\Pi}^{\mathsf{eav}}(n)$.

现在令 $\mathcal{A}$ 为一个概率多项式时间敌手。不失一般性，可以假设实验 $\mathsf{PubK}_{\mathcal{A},\Pi}^{\mathsf{eav}}(n)$ 中 $m_0 = 0$、$m_1 = 1$。

We then have

于是我们有

$$
\begin{aligned}
\Pr[\mathsf{PubK}_{\mathcal{A},\Pi}^{\mathsf{eav}}(n)=1]&=\frac{1}{2}\cdot\Pr[\mathcal{A}(pk,c)=0\mid c\text{ is an encryption of }0]\\
&\quad+\frac{1}{2}\cdot\Pr[\mathcal{A}(pk,c)=1\mid c\text{ is an encryption of }1].
\end{aligned}
$$

But then

但这样一来

$$
\begin{aligned}
&\Pr[\mathcal{A}(I,f_{I}(x))=\mathsf{hc}_{I}(x)]\\
&=\delta_{0}(n)\cdot\Pr[\mathcal{A}(I,f_{I}(x))=0\mid\mathsf{hc}_{I}(x)=0]\\
&\quad+\delta_{1}(n)\cdot\Pr[\mathcal{A}(I,f_{I}(x))=1\mid\mathsf{hc}_{I}(x)=1]\\
&\geq\left(\frac{1}{2}-\mathsf{negl}(n)\right)\cdot\Pr[\mathcal{A}(I,f_{I}(x))=0\mid\mathsf{hc}_{I}(x)=0]\\
&\quad+\left(\frac{1}{2}-\mathsf{negl}(n)\right)\cdot\Pr[\mathcal{A}(I,f_{I}(x))=1\mid\mathsf{hc}_{I}(x)=1]\\
&\geq\frac{1}{2}\cdot\Pr[\mathcal{A}(I,f_{I}(x))=0\mid\mathsf{hc}_{I}(x)=0]\\
&\quad+\frac{1}{2}\cdot\Pr[\mathcal{A}(I,f_{I}(x))=1\mid\mathsf{hc}_{I}(x)=1]-2\cdot\mathsf{negl}(n)\\
&=\Pr[\mathsf{PubK}_{\mathcal{A},\Pi}^{\mathsf{eav}}(n)=1]-2\cdot\mathsf{negl}(n).
\end{aligned}
$$

Since $\mathsf{hc}$ is a hard-core predicate for $\widehat{\Pi}$, there is a negligible function $\mathsf{negl}^{\prime}$ such that $\mathsf{negl}^{\prime}(n) \geq \Pr[\mathcal{A}(I, f_I(x)) = \mathsf{hc}_I(x)]$; this means that

由于 $\mathsf{hc}$ 是 $\widehat{\Pi}$ 的难核谓词，存在可忽略函数 $\mathsf{negl}^{\prime}$ 使得 $\mathsf{negl}^{\prime}(n) \geq \Pr[\mathcal{A}(I, f_I(x)) = \mathsf{hc}_I(x)]$；这意味着

$$
\Pr[\mathsf{PubK}_{\mathcal{A},\Pi}^{\mathsf{eav}}(n)=1]\leq\mathsf{negl}^{\prime}(n)+2\cdot\mathsf{negl}(n),
$$

completing the proof.

证毕。

**Encrypting longer messages.**

Using Claim 12.7, we know that we can extend Construction 15.4 to encrypt $\ell$-bit messages using ciphertexts $\ell$ times as long. Better efficiency can be obtained by constructing a KEM, following along the lines of Construction 12.34. We leave the details as an exercise.

**加密更长的消息。**

利用断言 12.7 可知，可以把构造 15.4 扩展为加密 $\ell$ 比特消息的方案，代价是密文长度变为 $\ell$ 倍。仿照构造 12.34 的思路构造一个 KEM 可以获得更好的效率。细节留作习题。

## 15.2 The Paillier Encryption Scheme　Paillier 加密方案

In this section we describe the Paillier encryption scheme, a public-key encryption scheme whose security is based on an assumption related (but not known to be equivalent) to the hardness of factoring. This encryption scheme is particularly interesting because it possesses some nice homomorphic properties, as we will discuss further in Section 15.2.3.

本节介绍 Paillier 加密方案——一个公钥加密方案，其安全性建立在一个与因子分解困难性相关（但尚不知道是否等价）的假设之上。这个加密方案之所以特别有趣，是因为它具有一些良好的同态性质，我们将在 15.2.3 节进一步讨论。

The Paillier encryption scheme utilizes the group $\mathbb{Z}_{N^2}^*$, the multiplicative group of elements in the range $\{1, \ldots, N^2\}$ that are relatively prime to $N$, for $N$ a product of two distinct primes. To understand the scheme it is helpful to first understand the structure of $\mathbb{Z}_{N^2}^*$. A useful characterization of this group is given by the following proposition, which says, among other things, that $\mathbb{Z}_{N^2}^*$ is isomorphic to $\mathbb{Z}_N \times \mathbb{Z}_N^*$ (cf. Definition 9.23) for $N$ of the form we will be interested in. We prove the proposition in the next section. (The reader willing to accept the proposition on faith can skip to Section 15.2.2.)

Paillier 加密方案使用群 $\mathbb{Z}_{N^2}^*$，其中 $N$ 是两个不同素数的乘积，$\mathbb{Z}_{N^2}^*$ 是 $\{1, \ldots, N^2\}$ 中所有与 $N$ 互素的元素构成的乘法群。要理解该方案，最好先理解 $\mathbb{Z}_{N^2}^*$ 的结构。下面的命题给出了这个群的一个有用刻画：对我们所关心形式的 $N$，$\mathbb{Z}_{N^2}^*$ 同构于 $\mathbb{Z}_N \times \mathbb{Z}_N^*$（参见定义 9.23）。我们在下一小节证明该命题。（愿意直接接受该命题的读者可以跳到 15.2.2 节。）

PROPOSITION 15.6 Let $N = pq$, where $p, q$ are distinct odd primes of equal length. Then:

命题 15.6　设 $N = pq$，其中 $p, q$ 是长度相等的不同奇素数。那么：

1. $\gcd(N,\phi(N))=1$

1. $\gcd(N,\phi(N))=1$

2. For any integer $a \geq 0$, we have $(1 + N)^a = (1 + aN) \mod N^2$.

2. 对任意整数 $a \geq 0$，有 $(1 + N)^a = (1 + aN) \mod N^2$。

As a consequence, the order of $(1+N)$ in $\mathbb{Z}_{N^2}^*$ is $N$. That is, $(1+N)^N = 1 \bmod N^2$ and $(1+N)^a \neq 1 \bmod N^2$ for any ${1} \leq a < N$.

作为推论，$(1+N)$ 在 $\mathbb{Z}_{N^2}^*$ 中的阶为 $N$。也就是说，$(1+N)^N = 1 \bmod N^2$，且对任意 ${1} \leq a < N$ 都有 $(1+N)^a \neq 1 \bmod N^2$。

3. $\mathbb{Z}_N \times \mathbb{Z}_N^*$ is isomorphic to $\mathbb{Z}_{N^2}^*$, with isomorphism $f\colon \mathbb{Z}_N \times \mathbb{Z}_N^* \to \mathbb{Z}_{N^2}^*$ given by

3. $\mathbb{Z}_N \times \mathbb{Z}_N^*$ 同构于 $\mathbb{Z}_{N^2}^*$，同构映射 $f\colon \mathbb{Z}_N \times \mathbb{Z}_N^* \to \mathbb{Z}_{N^2}^*$ 给出如下：

$$
f(a,b)=\left[(1+N)^{a}\cdot b^{N}\bmod N^{2}\right].
$$

In light of the last part of the above proposition, we introduce some convenient notation. With $N$ understood, and $x \in \mathbb{Z}_{N^2}^*, a \in \mathbb{Z}_N$, $b \in \mathbb{Z}_N^*$, we write $x \leftrightarrow (a,b)$ if $f(a,b) = x$ where $f$ is the isomorphism from the proposition above. One way to think about this notation is that it means “$x$ in $\mathbb{Z}_{N^2}^*$ corresponds to $(a,b)$ in $\mathbb{Z}_N \times \mathbb{Z}_N^*$.” We have used the same notation in this book with regard to the isomorphism $\mathbb{Z}_N^* \simeq \mathbb{Z}_p^* \times \mathbb{Z}_q^*$ given by the Chinese remainder theorem; we keep the notation because in both cases it refers to an isomorphism of groups. Nevertheless, there should be no confusion since the group $\mathbb{Z}_{N^2}^*$ and the above proposition are only used in this section. We remark that here the isomorphism—but not its inverse—is efficiently computable even without the factorization of $N$.

鉴于上述命题的最后一部分，我们引入一个方便的记号。在 $N$ 已知的前提下，对 $x \in \mathbb{Z}_{N^2}^*, a \in \mathbb{Z}_N$，$b \in \mathbb{Z}_N^*$，若 $f(a,b) = x$（其中 $f$ 是上述命题中的同构映射），则记 $x \leftrightarrow (a,b)$。这个记号可以理解为“$\mathbb{Z}_{N^2}^*$ 中的 $x$ 对应于 $\mathbb{Z}_N \times \mathbb{Z}_N^*$ 中的 $(a,b)$”。本书此前对由中国剩余定理给出的同构 $\mathbb{Z}_N^* \simeq \mathbb{Z}_p^* \times \mathbb{Z}_q^*$ 也用过同样的记号；我们保留这个记号，因为两种情形下它指的都是群同构。不过应该不会引起混淆，因为群 $\mathbb{Z}_{N^2}^*$ 和上述命题只在本节使用。需要指出的是，这里的同构映射——但不包括它的逆——即使不知道 $N$ 的分解也是可以高效计算的。

### 15.2.1 The Structure of $\mathbb{Z}_{N^{2}}^{*}$　$\mathbb{Z}_{N^{2}}^{*}$ 的结构

This section is devoted to a proof of Proposition 15.6. Throughout, we let $N, p, q$ be as in the proposition.

本小节专门用于证明命题 15.6。以下始终设 $N, p, q$ 如该命题所述。

CLAIM 15.7 $\gcd(N,\phi(N))=1$.

断言 15.7　$\gcd(N,\phi(N))=1$。

PROOF Recall that $\phi(N) = (p-1)(q-1)$. Assume $p > q$ without loss of generality. Since $p$ is prime and $p > p-1 > q-1$, clearly $\gcd(p, \phi(N)) = 1$. Similarly, $\gcd(q, q-1) = 1$. Now, if $\gcd(q, p-1) \neq 1$ then $\gcd(q, p-1) = q$
since $q$ is prime. But then $(p-1)/q \geq 2$, contradicting the assumption that $p$ and $q$ have the same length.

证明　回忆 $\phi(N) = (p-1)(q-1)$。不失一般性，假设 $p > q$。由于 $p$ 是素数且 $p > p-1 > q-1$，显然 $\gcd(p, \phi(N)) = 1$。类似地，$\gcd(q, q-1) = 1$。现在，若 $\gcd(q, p-1) \neq 1$，则因 $q$ 是素数，必有 $\gcd(q, p-1) = q$。但这样一来 $(p-1)/q \geq 2$，与 $p$ 和 $q$ 长度相等的假设矛盾。

CLAIM 15.8 For $a \geq 0$ an integer, we have $(1 + N)^a = 1 + aN \mod N^2$. Thus, the order of $(1 + N)$ in $\mathbb{Z}_{N^2}^*$ is $N$.

断言 15.8　对整数 $a \geq 0$，有 $(1 + N)^a = 1 + aN \mod N^2$。因此，$(1 + N)$ 在 $\mathbb{Z}_{N^2}^*$ 中的阶为 $N$。

PROOF Using the binomial expansion theorem (Theorem A.1):

证明　利用二项式展开定理（定理 A.1）：

$$
(1+N)^{a}=\sum_{i=0}^{a}\binom{a}{i}N^{i}.
$$

Reducing the right-hand side modulo $N^2$, all terms with $i \geq 2$ become 0 and so $(1+N)^a = 1+aN \mod N^2$. The smallest nonzero $a$ such that $(1+N)^a = 1 \bmod N^2$ is therefore $a = N$.

将右端对 $N^2$ 取模，所有 $i \geq 2$ 的项都变为 0，因此 $(1+N)^a = 1+aN \mod N^2$。于是，满足 $(1+N)^a = 1 \bmod N^2$ 的最小非零 $a$ 就是 $a = N$。

CLAIM 15.9 The group $\mathbb{Z}_N \times \mathbb{Z}_N^*$ is isomorphic to the group $\mathbb{Z}_{N^2}^{*}$, with isomorphism $f\colon \mathbb{Z}_N \times \mathbb{Z}_N^* \to \mathbb{Z}_{N^2}^{*}$ given by $f(a, b) = [(1 + N)^a \cdot b^N \mod N^2]$.

断言 15.9　群 $\mathbb{Z}_N \times \mathbb{Z}_N^*$ 同构于群 $\mathbb{Z}_{N^2}^{*}$，同构映射 $f\colon \mathbb{Z}_N \times \mathbb{Z}_N^* \to \mathbb{Z}_{N^2}^{*}$ 由 $f(a, b) = [(1 + N)^a \cdot b^N \mod N^2]$ 给出。

PROOF Note that $(1+N)^{a} \cdot b^{N}$ does not have a factor in common with $N^{2}$ since $\gcd((1+N), N^{2}) = 1$ and $\gcd(b, N^{2}) = 1$ (because $b \in \mathbb{Z}_{N}^{*}$). So $(1+N)^{a} \cdot b^{N} \bmod N^{2}$ lies in $\mathbb{Z}_{N^{2}}^{*}$. We now prove that $f$ is an isomorphism.

证明　注意 $(1+N)^{a} \cdot b^{N}$ 与 $N^{2}$ 没有公共因子，因为 $\gcd((1+N), N^{2}) = 1$ 且 $\gcd(b, N^{2}) = 1$（由于 $b \in \mathbb{Z}_{N}^{*}$）。所以 $(1+N)^{a} \cdot b^{N} \bmod N^{2}$ 落在 $\mathbb{Z}_{N^{2}}^{*}$ 中。下面证明 $f$ 是一个同构。

We first show that $f$ is a bijection. Since

我们首先证明 $f$ 是双射。由于

$$
\begin{aligned}
|\mathbb{Z}_{N^{2}}^{*}|=\phi(N^{2})=p\cdot(p-1)\cdot q\cdot(q-1)&=pq\cdot(p-1)(q-1)\\
&=|\mathbb{Z}_{N}|\cdot|\mathbb{Z}_{N}^{*}|=|\mathbb{Z}_{N}\times\mathbb{Z}_{N}^{*}|
\end{aligned}
$$

(see Theorem 9.19 for the second equality), it suffices to show that $f$ is one-to-one. Say $a_1, a_2 \in \mathbb{Z}_N$ and $b_1, b_2 \in \mathbb{Z}_N^*$ are such that $f(a_1, b_1) = f(a_2, b_2)$. Then:

（第二个等号见定理 9.19），只需证明 $f$ 是单射。设 $a_1, a_2 \in \mathbb{Z}_N$ 与 $b_1, b_2 \in \mathbb{Z}_N^*$ 满足 $f(a_1, b_1) = f(a_2, b_2)$。那么：

$$
(1+N)^{a_{1}-a_{2}}\cdot(b_{1}/b_{2})^{N}=1\bmod N^{2}. \tag{15.1}
$$

(Note that $b_2 \in \mathbb{Z}_N^*$ and thus $b_2 \in \mathbb{Z}_{N^2}^*$, and so $b_2$ has a multiplicative inverse modulo $N^2$.) Raising both sides to the power $\phi(N)$ and using the fact that the order of $\mathbb{Z}_{N^2}^*$ is $\phi(N^2) = N \cdot \phi(N)$ we obtain

（注意 $b_2 \in \mathbb{Z}_N^*$，从而 $b_2 \in \mathbb{Z}_{N^2}^*$，因此 $b_2$ 在模 $N^2$ 下有乘法逆元。）将等式两端取 $\phi(N)$ 次幂，并利用 $\mathbb{Z}_{N^2}^*$ 的阶为 $\phi(N^2) = N \cdot \phi(N)$ 这一事实，得到

$$
\begin{aligned}
(1+N)^{(a_{1}-a_{2})\cdot\phi(N)}\cdot(b_{1}/b_{2})^{N\cdot\phi(N)}&=1\bmod N^{2}\\
\Rightarrow(1+N)^{(a_{1}-a_{2})\cdot\phi(N)}&=1\bmod N^{2}.
\end{aligned}
$$

By Claim 15.8, $(1+N)$ has order $N$ modulo $N^2$. Applying Proposition 9.54, we see that $(a_1 - a_2) \cdot \phi(N) = 0 \bmod N$ and so $N$ divides $(a_1 - a_2) \cdot \phi(N)$. Since $\gcd(N, \phi(N)) = 1$ by Claim 15.7, it follows that $N \mid (a_1 - a_2)$. Since $a_1, a_2 \in \mathbb{Z}_N$, this can only occur if $a_1 = a_2$.

由断言 15.8，$(1+N)$ 在模 $N^2$ 下的阶为 $N$。应用命题 9.54 可知 $(a_1 - a_2) \cdot \phi(N) = 0 \bmod N$，即 $N$ 整除 $(a_1 - a_2) \cdot \phi(N)$。而由断言 15.7 有 $\gcd(N, \phi(N)) = 1$，于是 $N \mid (a_1 - a_2)$。由于 $a_1, a_2 \in \mathbb{Z}_N$，这只有在 $a_1 = a_2$ 时才可能发生。

Returning to Equation (15.1) and setting $a_1 = a_2$, we thus have $b_1^N = b_2^N \bmod N^2$. This implies $b_1^N = b_2^N \bmod N$. Since $N$ is relatively prime to $\phi(N)$, the order of $\mathbb{Z}_N^*$, exponentiation to the power $N$ is a bijection in $\mathbb{Z}_N^*$ (cf. Corollary 9.17). This means that $b_1 = b_2 \bmod N$; since $b_1, b_2 \in \mathbb{Z}_N^*$, we have $b_1 = b_2$. We conclude that $f$ is one-to-one, and hence a bijection.

回到式 (15.1) 并令 $a_1 = a_2$，于是有 $b_1^N = b_2^N \bmod N^2$。这蕴含 $b_1^N = b_2^N \bmod N$。由于 $N$ 与 $\mathbb{Z}_N^*$ 的阶 $\phi(N)$ 互素，取 $N$ 次幂是 $\mathbb{Z}_N^*$ 上的双射（参见推论 9.17）。这意味着 $b_1 = b_2 \bmod N$；又因 $b_1, b_2 \in \mathbb{Z}_N^*$，故 $b_1 = b_2$。我们得出结论：$f$ 是单射，因而是双射。

To show that $f$ is an isomorphism, we show that $f(a_1,b_1)\cdot f(a_2,b_2)=f(a_1+a_2,b_1\cdot b_2)$. (Note that multiplication on the left-hand side of the equality takes place modulo $N^2$, while addition/multiplication on the right-hand side takes place modulo $N$.) We have:

为证明 $f$ 是同构，我们证明 $f(a_1,b_1)\cdot f(a_2,b_2)=f(a_1+a_2,b_1\cdot b_2)$。（注意，等号左端的乘法在模 $N^2$ 下进行，而右端的加法/乘法在模 $N$ 下进行。）我们有：

$$
\begin{aligned}
f(a_{1},b_{1})\cdot f(a_{2},b_{2})&=\left((1+N)^{a_{1}}\cdot b_{1}^{N}\right)\cdot\left((1+N)^{a_{2}}\cdot b_{2}^{N}\right)\bmod N^{2}\\
&=(1+N)^{a_{1}+a_{2}}\cdot(b_{1}b_{2})^{N}\bmod N^{2}.
\end{aligned}
$$

Since $(1+N)$ has order $N$ modulo $N^{2}$ (by Claim 15.8), we can apply Proposition 9.53 and obtain

由于 $(1+N)$ 在模 $N^{2}$ 下的阶为 $N$（由断言 15.8），可以应用命题 9.53 得到

$$
\begin{aligned}
f(a_{1},b_{1})\cdot f(a_{2},b_{2})&=(1+N)^{a_{1}+a_{2}}\cdot(b_{1}b_{2})^{N}\bmod N^{2}\\
&=(1+N)^{[a_{1}+a_{2}\bmod N]}\cdot(b_{1}b_{2})^{N}\bmod N^{2}.
\end{aligned} \tag{15.2}
$$

We are not yet done, since $b_1b_2$ in Equation (15.2) represents multiplication modulo $N^2$ whereas we would like it to be modulo $N$. Let $b_1b_2 = r + \gamma N$, where $\gamma, r$ are integers with ${1} \leq r < N$ ($r$ cannot be 0 since $b_1, b_2 \in \mathbb{Z}_N^*$ and so their product cannot be divisible by $N$). Note that $r = b_1b_2 \mod N$. We also have

证明尚未完成，因为式 (15.2) 中的 $b_1b_2$ 表示模 $N^2$ 下的乘法，而我们希望它是模 $N$ 下的。记 $b_1b_2 = r + \gamma N$，其中 $\gamma, r$ 为整数且 ${1} \leq r < N$（$r$ 不能为 0：因为 $b_1, b_2 \in \mathbb{Z}_N^*$，它们的乘积不可能被 $N$ 整除）。注意 $r = b_1b_2 \mod N$。我们还有

$$
\begin{aligned}
(b_{1}b_{2})^{N}&=(r+\gamma N)^{N}\bmod N^{2}\\
&=\sum_{k=0}^{N}\binom{N}{k}r^{N-k}(\gamma N)^{k}\bmod N^{2}\\
&=r^{N}+N\cdot r^{N-1}\cdot(\gamma N)=r^{N}=([b_{1}b_{2}\bmod N])^{N}\bmod N^{2},
\end{aligned}
$$

using the binomial expansion theorem as in Claim 15.8. Plugging this in to Equation (15.2) we get the desired result:

其中与断言 15.8 一样使用了二项式展开定理。把它代入式 (15.2)，就得到所要的结果：

$$
\begin{aligned}
f(a_{1},b_{1})\cdot f(a_{2},b_{2})&=(1+N)^{[a_{1}+a_{2}\bmod N]}\cdot(b_{1}b_{2}\bmod N)^{N}\bmod N^{2}\\
&=f(a_{1}+a_{2},b_{1}b_{2}),
\end{aligned}
$$

proving that $f$ is an isomorphism from $\mathbb{Z}_N \times \mathbb{Z}_N^*$ to $\mathbb{Z}_{N^2}^*$.

这就证明了 $f$ 是从 $\mathbb{Z}_N \times \mathbb{Z}_N^*$ 到 $\mathbb{Z}_{N^2}^*$ 的同构。

### 15.2.2 The Paillier Encryption Scheme　Paillier 加密方案

Let $N = pq$ be a product of two distinct primes of equal length. Proposition 15.6 says that $\mathbb{Z}_N \times \mathbb{Z}_N^*$ is isomorphic to $\mathbb{Z}_{N^2}^*$, with isomorphism given by $f(a, b) = [(1+N)^a \cdot b^N \mod N^2]$. A consequence is that a uniform element $y \in \mathbb{Z}_{N^2}^*$ corresponds to a uniform element $(a, b) \in \mathbb{Z}_N \times \mathbb{Z}_N^*$ or, in other words, an element $(a, b)$ with uniform $a \in \mathbb{Z}_N$ and uniform $b \in \mathbb{Z}_N^*$.

设 $N = pq$ 为两个长度相等的不同素数的乘积。命题 15.6 指出，$\mathbb{Z}_N \times \mathbb{Z}_N^*$ 同构于 $\mathbb{Z}_{N^2}^*$，同构映射由 $f(a, b) = [(1+N)^a \cdot b^N \mod N^2]$ 给出。由此可知，$\mathbb{Z}_{N^2}^*$ 中的均匀元素 $y$ 对应于 $\mathbb{Z}_N \times \mathbb{Z}_N^*$ 中的均匀元素 $(a, b)$——换句话说，即 $a \in \mathbb{Z}_N$ 与 $b \in \mathbb{Z}_N^*$ 分别均匀的元素 $(a, b)$。

Call $y \in \mathbb{Z}_{N^2}^*$ an $N$th residue modulo $N^2$ if $y$ is an $N$th power, that is, if there exists an $x \in \mathbb{Z}_{N^2}^*$ with $y = x^N \mod N^2$. We denote the set of $N$th residues modulo $N^2$ by $\mathsf{Res}(N^2)$. Let us characterize the $N$th residues in $\mathbb{Z}_{N^2}^*$. Taking any $x \in \mathbb{Z}_{N^2}^*$ with $x \leftrightarrow (a, b)$ and raising it to the $N$th power gives:

若 $y \in \mathbb{Z}_{N^2}^*$ 是一个 $N$ 次幂——即存在 $x \in \mathbb{Z}_{N^2}^*$ 使得 $y = x^N \mod N^2$——则称 $y$ 是模 $N^2$ 的一个 $N$ 次剩余。模 $N^2$ 的 $N$ 次剩余的集合记作 $\mathsf{Res}(N^2)$。下面来刻画 $\mathbb{Z}_{N^2}^*$ 中的 $N$ 次剩余。任取 $x \in \mathbb{Z}_{N^2}^*$ 且 $x \leftrightarrow (a, b)$，将其取 $N$ 次幂得：

$$
[x^{N}\bmod N^{2}]\leftrightarrow(a,b)^{N}=(N\cdot a\bmod N,b^{N}\bmod N)=(0,b^{N}\bmod N).
$$

(Recall that the group operation in $\mathbb{Z}_N \times \mathbb{Z}_N^*$ is addition modulo $N$ in the first component and multiplication modulo $N$ in the second component.) Moreover, we claim that any element $y$ with $y \leftrightarrow (0,b)$ is an $N$th residue. To see this, recall that $\gcd(N, \phi(N)) = 1$ and so $d \stackrel{\mathrm{def}}{=} [N^{-1} \mod \phi(N)]$ exists. So

（回忆一下，$\mathbb{Z}_N \times \mathbb{Z}_N^*$ 中的群运算在第一个分量上是模 $N$ 加法，在第二个分量上是模 $N$ 乘法。）此外，我们断言：任何满足 $y \leftrightarrow (0,b)$ 的元素 $y$ 都是 $N$ 次剩余。为看清这一点，回忆 $\gcd(N, \phi(N)) = 1$，因此 $d \stackrel{\mathrm{def}}{=} [N^{-1} \mod \phi(N)]$ 存在。于是

$$
(a,[b^{d}\bmod N])^{N}=(N a\bmod N,[b^{d N}\bmod N])=(0,b)\leftrightarrow y
$$

for any $a \in \mathbb{Z}_N$. We have thus shown that $\mathsf{Res}(N^2)$ corresponds to the set

对任意 $a \in \mathbb{Z}_N$ 成立。至此我们证明了 $\mathsf{Res}(N^2)$ 对应于集合

$$
\left\{\left(0,b\right)\mid b\in\mathbb{Z}_{N}^{\ast}\right\}.
$$

The above also demonstrates that the number of $N$th roots of any $y \in \mathsf{Res}(N^2)$ is exactly $N$, and so computing $N$th powers is an $N$-to-1 function. As such, if $r \in \mathbb{Z}_{N^2}^*$ is uniform then $[r^N \bmod N^2]$ is a uniform element of $\mathsf{Res}(N^2)$.

上述论证还表明，任何 $y \in \mathsf{Res}(N^2)$ 的 $N$ 次根恰好有 $N$ 个，因此计算 $N$ 次幂是一个 $N$ 对 1 的函数。这样一来，若 $r \in \mathbb{Z}_{N^2}^*$ 均匀分布，则 $[r^N \bmod N^2]$ 是 $\mathsf{Res}(N^2)$ 中的均匀元素。

The decisional composite residuosity problem, roughly speaking, is to distinguish a uniform element of $\mathbb{Z}_{N^2}^*$ from a uniform element of $\mathsf{Res}(N^2)$. Formally, let $\mathsf{GenModulus}$ be a polynomial-time algorithm that, on input ${1}^n$, outputs $(N, p, q)$ where $N = pq$, and $p$ and $q$ are $n$-bit primes (except with probability negligible in $n$). Then:

粗略地说，判定性合数剩余性问题就是区分 $\mathbb{Z}_{N^2}^*$ 中的均匀元素与 $\mathsf{Res}(N^2)$ 中的均匀元素。形式化地，设 $\mathsf{GenModulus}$ 是一个多项式时间算法，以 ${1}^n$ 为输入，输出 $(N, p, q)$，其中 $N = pq$ 且 $p$ 和 $q$ 是 $n$ 比特素数（除关于 $n$ 可忽略的概率外）。那么：

DEFINITION 15.10 The decisional composite residuosity problem is hard relative to GenModulus if for all probabilistic polynomial-time algorithms D there is a negligible function negl such that

定义 15.10　若对所有概率多项式时间算法 $\mathcal{D}$，都存在可忽略函数 $\mathsf{negl}$ 使得

$$
\left|\Pr[D(N,[r^{N}\bmod N^{2}])=1]-\Pr[D(N,r)=1]\right|\leq\mathsf{negl}(n),
$$

where in each case the probabilities are taken over the experiment in which $\mathsf{GenModulus}(1^n)$ outputs $(N, p, q)$, and then a uniform $r \in \mathbb{Z}_{N^2}^*$ is chosen. (Recall that $[r^N \bmod N^2]$ is a uniform element of $\mathsf{Res}(N^2)$.)

则称判定性合数剩余性问题相对于 $\mathsf{GenModulus}$ 是困难的；上式中两个概率都取自如下实验：$\mathsf{GenModulus}(1^n)$ 输出 $(N, p, q)$，然后均匀选取 $r \in \mathbb{Z}_{N^2}^*$。（回忆 $[r^N \bmod N^2]$ 是 $\mathsf{Res}(N^2)$ 中的均匀元素。）

The decisional composite residuosity (DCR) assumption is the assumption that there is a GenModulus relative to which the decisional composite residuosity problem is hard.

判定性合数剩余性（DCR）假设是指：存在某个 $\mathsf{GenModulus}$，使得判定性合数剩余性问题相对于它是困难的。

As we have discussed, elements of $\mathbb{Z}_{N^2}^*$ have the form $(r^{\prime}, r)$ with $r^{\prime}$ and $r$ arbitrary (in the appropriate groups), whereas $N$th residues have the form $(0, r)$ with $r \in \mathbb{Z}_N^*$ arbitrary. The DCR assumption is that it is hard to distinguish uniform elements of the first type from uniform elements of the second type. This suggests the following abstract way to encrypt a message $m \in \mathbb{Z}_N$ with respect to a public key $N$: choose a uniform $N$th residue $(0, r)$ and set the ciphertext equal to

如前所述，$\mathbb{Z}_{N^2}^*$ 的元素形如 $(r^{\prime}, r)$，其中 $r^{\prime}$ 与 $r$ 任意（分别取自相应的群）；而 $N$ 次剩余形如 $(0, r)$，其中 $r \in \mathbb{Z}_N^*$ 任意。DCR 假设说的就是：难以区分第一类的均匀元素与第二类的均匀元素。这提示了如下一种相对于公钥 $N$ 加密消息 $m \in \mathbb{Z}_N$ 的抽象方式：均匀选取一个 $N$ 次剩余 $(0, r)$，并令密文等于

$$
c\leftrightarrow(m,1)\cdot(0,r)=(m+0,1\cdot r)=(m,r).
$$

Without worrying for now how this can be carried out efficiently by the sender, or how the receiver can decrypt, let us simply convince ourselves (on an intuitive level) that this is secure. Since a uniform $N$th residue $(0, r)$ cannot be distinguished from a uniform element $(r^{\prime}, r)$, the ciphertext as constructed above is indistinguishable (from the point of an eavesdropper who does not know the factorization of $N$) from the ciphertext

暂且不去关心发送方如何高效地完成这一步、接收方又如何解密，我们先（在直觉层面上）让自己相信这是安全的。由于均匀的 $N$ 次剩余 $(0, r)$ 无法与均匀元素 $(r^{\prime}, r)$ 区分，上面构造的密文（在不知道 $N$ 的分解的窃听者看来）与密文

$$
c^{\prime}\leftrightarrow(m,1)\cdot(r^{\prime},r)=([m+r^{\prime}\bmod N],r)
$$

for uniform $r^{\prime} \in \mathbb{Z}_N$ and $r \in \mathbb{Z}_N^*$. Lemma 12.15 shows that $[m + r^{\prime} \mod N]$ is uniformly distributed in $\mathbb{Z}_N$ and so, in particular, this ciphertext $c^{\prime}$ is independent of the message $m$. CPA-security follows. A formal proof that proceeds exactly along these lines is given further below.

不可区分，其中 $r^{\prime} \in \mathbb{Z}_N$ 与 $r \in \mathbb{Z}_N^*$ 均匀分布。引理 12.15 表明 $[m + r^{\prime} \mod N]$ 在 $\mathbb{Z}_N$ 中均匀分布，因此特别地，密文 $c^{\prime}$ 与消息 $m$ 无关。选择明文安全由此得证。后文将给出一个严格沿此思路展开的形式化证明。

Before turning to the formal description and proof of security, we show how encryption and decryption can be performed efficiently.

在给出正式描述与安全性证明之前，我们先说明加密和解密如何高效完成。

**Encryption.**

We have described encryption above as though it is taking place in $\mathbb{Z}_N \times \mathbb{Z}_N^*$. In fact it takes place in the isomorphic group $\mathbb{Z}_{N^2}^*$. That is, the sender generates a ciphertext $c \in \mathbb{Z}_{N^2}^*$ by choosing a uniform $^1 r \in \mathbb{Z}_N^*$ and then computing

**加密。**

上面对加密的描述仿佛是在 $\mathbb{Z}_N \times \mathbb{Z}_N^*$ 中进行的，但实际上它发生在与之同构的群 $\mathbb{Z}_{N^2}^*$ 中。也就是说，发送方均匀$^{1}$选取 $r \in \mathbb{Z}_N^*$，然后计算

$$
c:=[(1+N)^{m}\cdot r^{N}\bmod N^{2}].
$$

Observe that

注意到

$$
c=\left((1+N)^{m}\cdot1^{N}\right)\cdot\left((1+N)^{0}\cdot r^{N}\right)\bmod N^{2}\leftrightarrow(m,1)\cdot(0,r),
$$

and so $c \leftrightarrow (m, r)$ as desired.

从而如我们所愿有 $c \leftrightarrow (m, r)$。

> $^1$ We remark that it does not make any difference whether the sender chooses uniform $r \in \mathbb{Z}_N^*$ or uniform $r \in \mathbb{Z}_{N^2}^*$, since in either case the distribution of $[r^N \bmod N^2]$ is the same (as can be verified by looking at what happens in the isomorphic group $\mathbb{Z}_N \times \mathbb{Z}_N^*$).

> $^1$ 需要指出，发送方无论是均匀选取 $r \in \mathbb{Z}_N^*$ 还是均匀选取 $r \in \mathbb{Z}_{N^2}^*$ 都没有任何区别，因为两种情形下 $[r^N \bmod N^2]$ 的分布相同（考察同构群 $\mathbb{Z}_N \times \mathbb{Z}_N^*$ 中发生的情况即可验证这一点）。

Decryption. We now describe how decryption can be performed efficiently given the factorization of $N$. For $c$ constructed as above, we claim that $m$ is recovered by the following steps:

解密。我们现在描述在已知 $N$ 的分解时如何高效解密。对于如上构造的 $c$，我们断言按以下步骤即可恢复 $m$：

- Set $\hat{c} := [c^{\phi(N)} \bmod N^2]$.
- 令 $\hat{c} := [c^{\phi(N)} \bmod N^2]$。

- Set $\hat{m} := (\hat{c} - 1)/N$. (Note that this is carried out over the integers.)
- 令 $\hat{m} := (\hat{c} - 1)/N$。（注意这一步在整数上进行。）

- Set $m := [\hat{m} \cdot \phi(N)^{-1} \mod N]$.
- 令 $m := [\hat{m} \cdot \phi(N)^{-1} \mod N]$。

To see why this works, let $c \leftrightarrow (m, r)$ for an arbitrary $r \in \mathbb{Z}_N^*$. Then

为看清其原理，设 $c \leftrightarrow (m, r)$，其中 $r \in \mathbb{Z}_N^*$ 任意。那么

$$
\begin{aligned}
\hat{c}&\stackrel{\mathrm{def}}{=}\left[c^{\phi(N)}\bmod N^{2}\right]\\
&\leftrightarrow(m,r)^{\phi(N)}\\
&=\left(\left[m\cdot\phi(N)\bmod N\right],\left[r^{\phi(N)}\bmod N\right]\right)\\
&=\left(\left[m\cdot\phi(N)\bmod N\right],1\right).
\end{aligned}
$$

By Proposition 15.6(3), this means that $\hat{c} = (1 + N)^{[m \cdot \phi(N) \bmod N]} \bmod N^2$. Using Proposition 15.6(2), we know that

由命题 15.6(3)，这意味着 $\hat{c} = (1 + N)^{[m \cdot \phi(N) \bmod N]} \bmod N^2$。再利用命题 15.6(2)，可知

$$
\hat{c}=(1+N)^{[m\cdot\phi(N)\bmod N]}=(1+[m\cdot\phi(N)\bmod N]\cdot N)\bmod N^{2}
$$

Since ${1}+[m \cdot \phi(N) \mod N] \cdot N$ is always less than $N^2$ we can drop the $\bmod N^2$ at the end and view the above as an equality over the integers. Thus, $\hat{m} \stackrel{\mathrm{def}}{=} (\hat{c} - 1)/N = [m \cdot \phi(N) \bmod N]$ and, finally,

由于 ${1}+[m \cdot \phi(N) \mod N] \cdot N$ 总小于 $N^2$，我们可以去掉末尾的 $\bmod N^2$，把上式视为整数上的等式。于是 $\hat{m} \stackrel{\mathrm{def}}{=} (\hat{c} - 1)/N = [m \cdot \phi(N) \bmod N]$，最后

$$
m=[\hat{m}\cdot\phi(N)^{-1}\bmod N],
$$

as required. (Note that $\phi(N)$ is invertible modulo $N$ since $\gcd(N, \phi(N)) = 1$.)

即为所求。（注意，由于 $\gcd(N, \phi(N)) = 1$，$\phi(N)$ 在模 $N$ 下可逆。）

We give a complete description of the Paillier encryption scheme, followed by an example of the above calculations.

下面给出 Paillier 加密方案的完整描述，随后给出一个上述计算过程的例子。

**CONSTRUCTION 15.11**

Let $\mathsf{GenModulus}$ be a polynomial-time algorithm that, on input ${1}^{n}$, outputs $(N, p, q)$ where $N = pq$ and $p$ and $q$ are $n$-bit primes (except with probability negligible in $n$). Define the following encryption scheme:

- Gen: on input ${1}^n$ run $\mathsf{GenModulus}({1}^n)$ to obtain $(N, p, q)$. The public key is $N$, and the private key is $\langle N, \phi(N) \rangle$.

- Enc: on input a public key $N$ and a message $m \in \mathbb{Z}_N$, choose a uniform $r \leftarrow \mathbb{Z}_N^*$ and output the ciphertext

$$
c:=\bigl[(1+N)^{m}\cdot r^{N}\bmod N^{2}\bigr].
$$

- Dec: on input a private key $\langle N, \phi(N) \rangle$ and a ciphertext $c$, compute

$$
m:=\left[\frac{[c^{\phi(N)}\bmod N^{2}]-1}{N}\cdot\phi(N)^{-1}\bmod N\right].
$$

The Paillier encryption scheme.

**构造 15.11**

设 $\mathsf{GenModulus}$ 是一个多项式时间算法，以 ${1}^{n}$ 为输入，输出 $(N, p, q)$，其中 $N = pq$ 且 $p$ 和 $q$ 是 $n$ 比特素数（除关于 $n$ 可忽略的概率外）。定义如下加密方案：

- Gen：以 ${1}^n$ 为输入，运行 $\mathsf{GenModulus}({1}^n)$ 得到 $(N, p, q)$。公钥为 $N$，私钥为 $\langle N, \phi(N) \rangle$。

- Enc：以公钥 $N$ 和消息 $m \in \mathbb{Z}_N$ 为输入，均匀选取 $r \leftarrow \mathbb{Z}_N^*$，输出密文

$$
c:=\bigl[(1+N)^{m}\cdot r^{N}\bmod N^{2}\bigr].
$$

- Dec：以私钥 $\langle N, \phi(N) \rangle$ 和密文 $c$ 为输入，计算

$$
m:=\left[\frac{[c^{\phi(N)}\bmod N^{2}]-1}{N}\cdot\phi(N)^{-1}\bmod N\right].
$$

Paillier 加密方案。

**Example 15.12**

Let $N = 11 \cdot 17 = 187$ (and so $N^2 = 34969$), and consider encrypting the message $m = 175$ and then decrypting the corresponding ciphertext. Choosing $r = 83 \in \mathbb{Z}_{187}^*$, we compute the ciphertext

**例 15.12**

令 $N = 11 \cdot 17 = 187$（于是 $N^2 = 34969$），考虑加密消息 $m = 175$，再解密相应的密文。选取 $r = 83 \in \mathbb{Z}_{187}^*$，计算密文

$$
c:=[(1+187)^{175}\cdot83^{187}\bmod34969]=23911
$$

corresponding to (175,83). To decrypt, note that $\phi(N) = 160$. So we first compute $\hat{c} := [23911^{160} \mod 34969] = 25620$. Subtracting 1 and dividing by 187 gives $\hat{m} := (25620 - 1)/187 = 137$; since ${90} = [160^{-1} \mod 187]$, the message is recovered as $m := [137 \cdot 90 \mod 187] = 175$.

它对应于 (175,83)。解密时，注意 $\phi(N) = 160$。先计算 $\hat{c} := [23911^{160} \mod 34969] = 25620$；减去 1 再除以 187 得 $\hat{m} := (25620 - 1)/187 = 137$；由于 ${90} = [160^{-1} \mod 187]$，消息恢复为 $m := [137 \cdot 90 \mod 187] = 175$。

THEOREM 15.13 If the decisional composite residuosity problem is hard relative to GenModulus, then the Paillier encryption scheme is CPA-secure.

定理 15.13　若判定性合数剩余性问题相对于 $\mathsf{GenModulus}$ 是困难的，则 Paillier 加密方案是选择明文安全的。

PROOF Let $\Pi$ denote the Paillier encryption scheme. We prove that $\Pi$ has indistinguishable encryptions in the presence of an eavesdropper; by Theorem 12.6 this implies that it is CPA-secure.

证明　记 $\Pi$ 为 Paillier 加密方案。我们证明 $\Pi$ 在窃听者存在时具有不可区分的加密；由定理 12.6，这意味着它是选择明文安全的。

Let $\mathcal{A}$ be an arbitrary probabilistic polynomial-time adversary. Consider the following PPT algorithm $D$ that attempts to solve the decisional composite residuosity problem relative to $\mathsf{GenModulus}$:

设 $\mathcal{A}$ 为任意的概率多项式时间敌手。考虑下面这个试图求解相对于 $\mathsf{GenModulus}$ 的判定性合数剩余性问题的 PPT 算法 $D$：

Algorithm $D$:

算法 $D$：

The algorithm is given $N$, $y$ as input.

该算法以 $N$、$y$ 为输入。

- Set $pk = N$ and run $\mathcal{A}(pk)$ to obtain two messages $m_{0}, m_{1}$.
- 令 $pk = N$，运行 $\mathcal{A}(pk)$ 得到两个消息 $m_{0}, m_{1}$。

- Choose a uniform bit $b$ and set $c := [(1 + N)^{m_b} \cdot y \bmod N^2]$.
- 均匀选取比特 $b$，令 $c := [(1 + N)^{m_b} \cdot y \bmod N^2]$。

- Give the ciphertext $c$ to $\mathcal{A}$ and obtain an output bit $b^{\prime}$. If $b^{\prime} = b$, output 1; otherwise, output 0.
- 把密文 $c$ 交给 $\mathcal{A}$，得到输出比特 $b^{\prime}$。若 $b^{\prime} = b$ 则输出 1，否则输出 0。

Let us analyze the behavior of $D$. There are two cases to consider:

我们来分析 $D$ 的行为。需要分两种情形：

Case 1: Say the input to $D$ was generated by running $\mathsf{GenModulus}(1^n)$ to obtain $(N,p,q)$, choosing uniform $r \in \mathbb{Z}_{N^2}^*$, and setting $y := [r^N \bmod N^2]$. (That is, $y$ is a uniform element of $\mathsf{Res}(N^2)$.) In this case,

情形 1：设 $D$ 的输入是按如下方式生成的：运行 $\mathsf{GenModulus}(1^n)$ 得到 $(N,p,q)$，均匀选取 $r \in \mathbb{Z}_{N^2}^*$，并令 $y := [r^N \bmod N^2]$。（也就是说，$y$ 是 $\mathsf{Res}(N^2)$ 中的均匀元素。）在这种情形下，

$$
c=[(1+N)^{m_{b}}\cdot r^{N}\bmod N^{2}]
$$

for uniform $r \in \mathbb{Z}_{N^2}^*$. Recalling that the distribution on $[r^N \bmod N^2]$ is the same whether $r$ is chosen uniformly from $\mathbb{Z}_N^*$ or from $\mathbb{Z}_{N^2}^*$, we see that in this case the view of $\mathcal{A}$ when run as a subroutine by $D$ is distributed identically to $\mathcal{A}$'s view in experiment $\mathsf{PubK}_{\mathcal{A},\Pi}^{\mathsf{eav}}(n)$. Since $D$ outputs 1 exactly when the output $b^{\prime}$ of $\mathcal{A}$ is equal to $b$, we have

其中 $r \in \mathbb{Z}_{N^2}^*$ 均匀分布。回忆无论 $r$ 是从 $\mathbb{Z}_N^*$ 还是从 $\mathbb{Z}_{N^2}^*$ 中均匀选取，$[r^N \bmod N^2]$ 的分布都相同；由此可见，在这种情形下，$\mathcal{A}$ 作为 $D$ 的子程序运行时的视图，与它在实验 $\mathsf{PubK}_{\mathcal{A},\Pi}^{\mathsf{eav}}(n)$ 中的视图分布完全相同。由于 $D$ 恰好当 $\mathcal{A}$ 的输出 $b^{\prime}$ 等于 $b$ 时输出 1，我们有

$$
\Pr\big[D(N,[r^{N}\bmod N^{2}])=1\big]=\Pr[\mathsf{PubK}_{\mathcal{A},\Pi}^{\mathsf{eav}}(n)=1],
$$

where the first probability is taken over the experiment as in Definition 15.10.

其中第一个概率取自定义 15.10 所述的实验。

Case 2: Say the input to $D$ was generated by running $\mathsf{GenModulus}(1^n)$ to obtain $(N,p,q)$ and choosing uniform $y \in \mathbb{Z}_{N^2}^*$. We claim that the view of $\mathcal{A}$ in this case is independent of the bit $b$. This follows because $y$ is a uniform element of the group $\mathbb{Z}_{N^2}^*$, and so the ciphertext $c$ is uniformly distributed in $\mathbb{Z}_{N^2}^*$ (see Lemma 12.15), independent of $m$. Thus, the probability that $b^{\prime} = b$ in this case is exactly $\frac{1}{2}$. That is,

情形 2：设 $D$ 的输入是按如下方式生成的：运行 $\mathsf{GenModulus}(1^n)$ 得到 $(N,p,q)$，并均匀选取 $y \in \mathbb{Z}_{N^2}^*$。我们断言，这种情形下 $\mathcal{A}$ 的视图与比特 $b$ 无关。这是因为 $y$ 是群 $\mathbb{Z}_{N^2}^*$ 中的均匀元素，所以密文 $c$ 在 $\mathbb{Z}_{N^2}^*$ 中均匀分布（见引理 12.15），与 $m$ 无关。于是，这种情形下 $b^{\prime} = b$ 的概率恰好是 $\frac{1}{2}$。也就是说，

$$
\Pr[D(N,r)=1]=\frac{1}{2},
$$

where the probability is taken over the experiment as in Definition 15.10.

其中概率取自定义 15.10 所述的实验。

Combining the above, we see that

综合上述两种情形，可得

$$
\begin{aligned}
&\left|\Pr\left[D(N,[r^{N}\bmod N^{2}])=1\right]-\Pr[D(N,r)=1]\right|\\
&=\left|\Pr[\mathsf{PubK}_{\mathcal{A},\Pi}^{\mathsf{eav}}(n)=1]-\tfrac{1}{2}\right|.
\end{aligned}
$$

By the assumption that the decisional composite residuosity problem is hard relative to GenModulus, there is a negligible function $\mathsf{negl}$.

由“判定性合数剩余性问题相对于 $\mathsf{GenModulus}$ 是困难的”这一假设，存在可忽略函数 $\mathsf{negl}$ 使得

$$
\left|\Pr[\mathsf{PubK}_{\mathcal{A},\Pi}^{\mathsf{eav}}(n)=1]-\textstyle\frac{1}{2}\right|\leq\mathsf{negl}(n).
$$

Thus $\Pr[\mathsf{PubK}_{\mathcal{A},\Pi}^{\mathsf{eav}}(n)=1]\leq\tfrac{1}{2}+\mathsf{negl}(n)$, completing the proof.

于是 $\Pr[\mathsf{PubK}_{\mathcal{A},\Pi}^{\mathsf{eav}}(n)=1]\leq\tfrac{1}{2}+\mathsf{negl}(n)$，证毕。

### 15.2.3 Homomorphic Encryption　同态加密

The Paillier encryption scheme is useful in a number of settings because it is homomorphic. Roughly, a homomorphic encryption scheme enables (certain) computations to be performed on encrypted data, yielding a ciphertext containing the encrypted result. In the case of Paillier encryption, the computation that can be performed is (modular) addition. Specifically, fix a public key $pk = N$. Then the Paillier scheme has the property that multiplying an encryption of $m_1$ and an encryption of $m_2$ (with multiplication done modulo $N^2$) results in an encryption of $[m_1 + m_2 \mod N]$; this is because

Paillier 加密方案之所以在许多场合有用，是因为它是同态的。粗略地说，同态加密方案允许对加密数据执行（某些）计算，得到一个包含加密结果的密文。就 Paillier 加密而言，可执行的计算是（模）加法。具体地，固定公钥 $pk = N$。Paillier 方案具有如下性质：把 $m_1$ 的加密与 $m_2$ 的加密相乘（乘法在模 $N^2$ 下进行），得到的就是 $[m_1 + m_2 \mod N]$ 的加密；这是因为

$$
\begin{aligned}
&\left((1+N)^{m_{1}}\cdot r_{1}^{N}\right)\cdot\left((1+N)^{m_{2}}\cdot r_{2}^{N}\right)\\
&\quad=(1+N)^{\left[m_{1}+m_{2}\bmod N\right]}\cdot(r_{1}r_{2})^{N}\bmod N^{2}.
\end{aligned}
$$

Although the ability to add encrypted values may not seem very useful, it suffices for several interesting applications including voting, discussed below.

尽管对加密值做加法的能力看起来未必有多大用处，但它已经足以支持若干有趣的应用，包括下文讨论的投票。

We present a general definition, of which Paillier encryption is a special case.

我们给出一个一般性定义，Paillier 加密是它的一个特例。

DEFINITION 15.14 A public-key encryption scheme $(\mathsf{Gen}, \mathsf{Enc}, \mathsf{Dec})$ is homomorphic if for all $n$ and all $(pk, sk)$ output by $\mathsf{Gen}(1^n)$, it is possible to define groups $\mathcal{M}, \mathcal{C}$ (depending on pk only) such that:

定义 15.14　称一个公钥加密方案 $(\mathsf{Gen}, \mathsf{Enc}, \mathsf{Dec})$ 是同态的，如果对所有 $n$ 以及 $\mathsf{Gen}(1^n)$ 输出的所有 $(pk, sk)$，都可以定义群 $\mathcal{M}, \mathcal{C}$（仅依赖于 $pk$），使得：

- The message space is $\mathcal{M}$, and all ciphertexts output by $\mathsf{Enc}_{pk}$ are elements of $\mathcal{C}$. For notational convenience, we write $\mathcal{M}$ as an additive group and $\mathcal{C}$ as a multiplicative group.
- 消息空间是 $\mathcal{M}$，且 $\mathsf{Enc}_{pk}$ 输出的所有密文都是 $\mathcal{C}$ 的元素。为方便起见，我们把 $\mathcal{M}$ 写成加法群，把 $\mathcal{C}$ 写成乘法群。

- For any $m_1, m_2 \in \mathcal{M}$, any $c_1$ output by $\mathsf{Enc}_{pk}(m_1)$, and any $c_2$ output by $\mathsf{Enc}_{pk}(m_2)$, it holds that
- 对任意 $m_1, m_2 \in \mathcal{M}$、$\mathsf{Enc}_{pk}(m_1)$ 输出的任意 $c_1$ 以及 $\mathsf{Enc}_{pk}(m_2)$ 输出的任意 $c_2$，都有

$$
\mathsf{Dec}_{sk}(c_{1}\cdot c_{2})=m_{1}+m_{2}.
$$

Moreover, the distribution on ciphertexts obtained by encrypting $m_{1}$, encrypting $m_{2}$, and then multiplying the results is identical to the distribution on ciphertexts obtained by encrypting $m_{1} + m_{2}$.

此外，先分别加密 $m_{1}$、$m_{2}$ 再将结果相乘所得的密文分布，与直接加密 $m_{1} + m_{2}$ 所得的密文分布完全相同。

The last part of the definition ensures that if ciphertexts $c_1 \leftarrow \mathsf{Enc}_{pk}(m_1)$ and $c_2 \leftarrow \mathsf{Enc}_{pk}(m_2)$ are generated and the result $c_3 := c_1 \cdot c_2$ is computed, then the resulting ciphertext $c_3$ contains no more information about $m_1$ or $m_2$ than the sum $m_3$.

定义的最后一部分保证了：若生成密文 $c_1 \leftarrow \mathsf{Enc}_{pk}(m_1)$ 和 $c_2 \leftarrow \mathsf{Enc}_{pk}(m_2)$，再计算 $c_3 := c_1 \cdot c_2$，那么所得密文 $c_3$ 所包含的关于 $m_1$ 或 $m_2$ 的信息，不会比它们的和 $m_3$ 所包含的更多。

The Paillier encryption scheme with $pk = N$ is homomorphic with $\mathcal{M} = \mathbb{Z}_N$ and $\mathcal{C} = \mathbb{Z}_{N^2}^*$. This is not the first example of a homomorphic encryption scheme we have seen; El Gamal encryption is also homomorphic. Specifically, for public key $pk = \langle \mathbb{G}, q, g, h \rangle$ we can take $\mathcal{M} = \mathbb{G}$ and $\mathcal{C} = \mathbb{G} \times \mathbb{G}$; then

以 $pk = N$ 为公钥的 Paillier 加密方案是同态的，其中 $\mathcal{M} = \mathbb{Z}_N$、$\mathcal{C} = \mathbb{Z}_{N^2}^*$。这并不是我们见过的第一个同态加密方案——El Gamal 加密也是同态的。具体地，对公钥 $pk = \langle \mathbb{G}, q, g, h \rangle$，可以取 $\mathcal{M} = \mathbb{G}$、$\mathcal{C} = \mathbb{G} \times \mathbb{G}$；于是

$$
\langle g^{y_{1}},~h^{y_{1}}\cdot m_{1}\rangle\cdot\langle g^{y_{2}},~h^{y_{2}}\cdot m_{2}\rangle=\langle g^{y_{1}+y_{2}},~h^{y_{1}+y_{2}}\cdot m_{1}m_{2}\rangle,
$$

where multiplication of ciphertexts is component-wise. The Goldwasser-Micali encryption scheme we will see later is also homomorphic (see Exercise 15.11).

其中密文的乘法按分量进行。后文将看到的 Goldwasser–Micali 加密方案也是同态的（见习题 15.11）。

A nice feature of Paillier encryption is that it is homomorphic over a large additive group (namely, $\mathbb{Z}_N$). To see an application of this, consider the following distributed voting scheme, where $\ell$ voters can vote “no” or “yes” and the goal is to tabulate the number of “yes” votes:

Paillier 加密的一个良好特性是：它在一个很大的加法群（即 $\mathbb{Z}_N$）上是同态的。作为这一点的应用，考虑下面的分布式投票方案：$\ell$ 个投票人每人可以投“反对”或“赞成”，目标是统计“赞成”票的总数：

1. A voting authority generates a public key N for the Paillier encryption scheme and publicizes N.

1. 一个投票管理机构生成 Paillier 加密方案的公钥 $N$，并将 $N$ 公开。

2. Let 0 stand for a “no,” and let 1 stand for a “yes.” Each voter casts their vote by encrypting it. That is, voter $i$ casts her vote $v_i$ by computing $c_i := [(1 + N)^{v_i} \cdot (r_i)^N \mod N^2]$ for a uniform $r_i \in \mathbb{Z}_N^*$.

2. 用 0 表示“反对”，1 表示“赞成”。每个投票人通过加密来投出自己的选票。也就是说，投票人 $i$ 均匀选取 $r_i \in \mathbb{Z}_N^*$，计算 $c_i := [(1 + N)^{v_i} \cdot (r_i)^N \mod N^2]$ 来投出选票 $v_i$。

3. Each voter broadcasts their vote $c_{i}$. These votes are then publicly aggregated by computing

3. 每个投票人广播自己的选票 $c_{i}$。随后，这些选票通过计算下式公开汇总：

$$
c_{\mathrm{total}}:=\left[\prod_{i=1}^{\ell}c_{i}\bmod N^{2}\right].
$$

4. The authority is given $c_{total}$. (We assume the authority has not been able to observe what goes on until now.) By decrypting it, the authority obtains the vote total

4. 管理机构得到 $c_{total}$。（我们假设管理机构在此之前无法观察到任何事情。）对其解密，管理机构就得到选票总数

$$
v_{total}\stackrel{\mathrm{def}}{=}\sum_{i=1}^{\ell}v_{i}\bmod N.
$$

If $\ell$ is small (so that $v_{\text{total}} \ll N$), there is no wrap-around modulo $N$ and $v_{\text{total}} = \sum_{i=1}^{\ell} v_i$.

若 $\ell$ 很小（从而 $v_{\text{total}} \ll N$），则不会发生模 $N$ 的回绕，于是 $v_{\text{total}} = \sum_{i=1}^{\ell} v_i$。

Key features of the above are that no voter learns anyone else's vote, and calculation of the total is publicly verifiable if the authority is trusted to correctly compute $v_{total}$ from $c_{total}$. Also, the authority obtains the correct total without learning any individual votes. (Here, we assume the authority cannot see voters' ciphertexts. In Section 15.3.3 we show a protocol in which votes are kept hidden from authorities even if they see all the communication.) We assume all voters act honestly (and only try to learn others' votes based on information they observe); an entire research area of cryptography is dedicated to addressing potential threats from participants who might be malicious and not follow the protocol.

上述方案的关键特性在于：任何投票人都无法得知他人的选票；并且只要信任管理机构能由 $c_{total}$ 正确计算 $v_{total}$，总数的计算就是公开可验证的。此外，管理机构得到正确的总数，却无从得知任何个人的选票。（这里我们假设管理机构看不到投票人的密文。在 15.3.3 节中，我们将给出一个即使管理机构看到全部通信、选票仍然对其保密的协议。）我们假设所有投票人都诚实行事（只会根据自己观察到的信息去推测他人选票）；密码学中有一整个研究领域，专门应对参与者可能怀有恶意、不遵守协议所带来的潜在威胁。

## 15.3 Secret Sharing and Threshold Encryption　秘密共享与门限加密

Motivated by the discussion of distributed voting in the previous section, we briefly consider secure (interactive) protocols. Such protocols can be significantly more complicated than the basic cryptographic primitives (e.g., encryption and signature schemes) we have focused on until now, both because they can involve multiple parties exchanging several rounds of messages, as well as because they are intended to realize more-complex security requirements.

受上一节分布式投票讨论的启发，我们简要考察安全的（交互式）协议。这类协议可能比我们迄今为止所关注的基本密码学原语（例如加密方案与签名方案）复杂得多，原因既在于它们可能涉及多方交换多轮消息，也在于它们旨在实现更为复杂的安全性需求。

The goal of this section is mainly to give the reader a taste of this fascinating area, and no attempt is made at being comprehensive or complete. Although the protocols presented here can be proven secure (with respect to appropriate definitions), we omit formal definitions, details, and proofs and instead rely on informal discussion.

本节的目的主要是让读者领略这一引人入胜的领域，并不追求全面或完备。尽管这里给出的协议都可以（相对于适当的定义）被证明是安全的，但我们略去形式化定义、细节与证明，代之以非正式的讨论。

### 15.3.1 Secret Sharing　秘密共享

Consider the following problem. A dealer holds a secret $s \in \{0,1\}^{\ell}$ say, a nuclear-launch code—that it wishes to share among some set of $N$ users $P_1, \ldots, P_N$ by giving each user a share. Any $t$ users should be able to pool their shares and reconstruct the secret, but no coalition of fewer than $t$ users should get any information about $s$ from their collective shares (beyond whatever information they had about $s$ already). We refer to such a sharing mechanism as a $(t, N)$-threshold secret-sharing scheme. Such a scheme ensures that $s$ is not revealed without sufficient authorization, while also guaranteeing availability of $s$ when needed (since any $t$ users can reconstruct it). Beyond their direct application, secret-sharing schemes are also a building block of many cryptographic protocols.

考虑如下问题。一个分发者持有秘密 $s \in \{0,1\}^{\ell}$——比如说，一个核发射代码——希望把它分发给由 $N$ 个用户 $P_1, \ldots, P_N$ 组成的集合，方法是给每个用户一个份额。任意 $t$ 个用户应当能够汇集他们的份额并重构出该秘密，但任何少于 $t$ 个用户的联盟都不应能从他们的集体份额中获得关于 $s$ 的任何信息（除了他们本来就掌握的关于 $s$ 的信息）。我们把这样的共享机制称为 $(t, N)$-门限秘密共享方案。这样的方案确保 $s$ 在没有足够授权的情况下不会被泄露，同时又保证在需要时 $s$ 是可用的（因为任意 $t$ 个用户都能重构它）。除了直接应用之外，秘密共享方案还是许多密码学协议的构建模块。

There is a simple solution for the case $t = N$. The dealer chooses uniform $s_1, \ldots, s_{N-1} \in \{0,1\}^\ell$ and sets $s_N := s \oplus \left( \bigoplus_{i=1}^{N-1} s_i \right)$; the share of user $P_i$ is $s_i$. Since $\bigoplus_{i=1}^{N} s_i = s$ by construction, clearly all the users together can recover $s$. However, the shares of any coalition of $N-1$ users are (jointly) uniform and independent of $s$, and thus reveal no information about $s$. This is clear when the coalition is $P_1, \ldots, P_{N-1}$. In the general case, when the coalition includes everyone except for $P_j$ ($j \neq N$), this is true because $s_1, \ldots, s_{j-1}, s_{j+1}, \ldots, s_{N-1}$ are uniform and independent of $s$ by construction, and

当 $t = N$ 时有一个简单的解法。分发者均匀选取 $s_1, \ldots, s_{N-1} \in \{0,1\}^\ell$，并令 $s_N := s \oplus \left( \bigoplus_{i=1}^{N-1} s_i \right)$；用户 $P_i$ 的份额就是 $s_i$。由于按构造有 $\bigoplus_{i=1}^{N} s_i = s$，显然全体用户一起就能恢复 $s$。然而，任意 $N-1$ 个用户联盟的份额（联合来看）均匀且与 $s$ 独立，因此不泄露关于 $s$ 的任何信息。当联盟恰为 $P_1, \ldots, P_{N-1}$ 时，这一点是显而易见的。一般地，当联盟包含除 $P_j$（$j \neq N$）以外的所有用户时，结论同样成立：因为由构造可知 $s_1, \ldots, s_{j-1}, s_{j+1}, \ldots, s_{N-1}$ 均匀且与 $s$ 独立，并且

$$
s_{N}=s\oplus\left(\bigoplus_{i<N,i\neq j}s_{i}\right)\oplus s_{j};
$$

thus, even conditioned on some fixed values for $s$ and the shares of the other members of the coalition, the share $s_{N}$ of user $P_{N}$ is uniform because $s_{j}$ is uniform and independent of s.

由此，即使固定了 $s$ 以及联盟其他成员份额的取值，用户 $P_{N}$ 的份额 $s_{N}$ 依然是均匀的，因为 $s_{j}$ 均匀且与 $s$ 独立。

We can extend this to obtain a solution for $t < N$. The basic idea is to replicate the above scheme for each subset $T \subset N$ of size $t$. That is, for each such subset $T = \{P_{i_1}, \ldots, P_{i_t}\}$, we choose uniform shares $s_{T,i_1}, \ldots, s_{T,i_t}$ subject to the constraint that $\oplus_{j=1}^t s_{T,i_j} = s$, and give $s_{T,i_j}$ to user $P_{i_j}$. It is not hard to see that this satisfies the requirements.

我们可以对这个方案加以扩展，得到 $t < N$ 时的解法。基本想法是对每个大小为 $t$ 的子集 $T \subset N$（原书此处的 $N$ 指用户集合 $\{P_1, \ldots, P_N\}$）复制上述方案。也就是说，对每个这样的子集 $T = \{P_{i_1}, \ldots, P_{i_t}\}$，在约束 $\oplus_{j=1}^t s_{T,i_j} = s$ 下均匀选取份额 $s_{T,i_1}, \ldots, s_{T,i_t}$，并把 $s_{T,i_j}$ 分给用户 $P_{i_j}$。不难看出这满足各项要求。

Unfortunately, this extension of the original scheme is not efficient. Each user now stores a share $s_{T,i}$ for every subset T of which she is a member. For each user there are $\binom{N-1}{t-1}$ such subsets, which is exponential in N if $t \approx N/2$.

遗憾的是，原方案的这一扩展并不高效。现在每个用户都要为自己所属的每个子集 T 存储一个份额 $s_{T,i}$。对每个用户而言，这样的子集共有 $\binom{N-1}{t-1}$ 个；当 $t \approx N/2$ 时，这个数目关于 $N$ 是指数级的。

**Shamir’s scheme.** Fortunately, it is possible to do significantly better using a secret-sharing scheme introduced by Adi Shamir (of RSA fame). This scheme is based on polynomials $^2$ over a finite field $\mathbb{F}$, where $\mathbb{F}$ is chosen so that $s \in \mathbb{F}$ and $|\mathbb{F}| > N$. (See Appendix A.5 for a brief discussion of finite fields.) Before describing the scheme, we briefly review some background related to polynomials over a field $\mathbb{F}$.

**Shamir 方案。**

幸运的是，借助 Adi Shamir（因 RSA 而闻名）提出的一种秘密共享方案，可以做得好得多。该方案基于有限域 $\mathbb{F}$ 上的多项式 $^2$，其中 $\mathbb{F}$ 的选取须满足 $s \in \mathbb{F}$ 且 $|\mathbb{F}| > N$。（关于有限域的简要讨论见附录 A.5。）在描述该方案之前，我们先简要回顾一些与域 $\mathbb{F}$ 上多项式相关的背景知识。

> $^2$ A degree-$t$ polynomial $p$ over $\mathbb{F}$ is given by $p(X) = \sum_{i=0}^{t} a_i X^i$, where $a_i \in \mathbb{F}$ and $X$ is a formal variable. (Note that we allow $a_t = 0$ and so we really mean a polynomial of degree at most $t$.) Any such polynomial naturally defines a function mapping $\mathbb{F}$ to itself, given by evaluating the polynomial on its input.

> $^2$ $\mathbb{F}$ 上的 $t$ 次多项式 $p$ 形如 $p(X) = \sum_{i=0}^{t} a_i X^i$，其中 $a_i \in \mathbb{F}$，$X$ 为形式变元。（注意我们允许 $a_t = 0$，因此实际所指是次数至多为 $t$ 的多项式。）任何这样的多项式都自然地定义了一个从 $\mathbb{F}$ 映射到自身的函数，即在输入上求该多项式的值。

A value $x \in \mathbb{F}$ is a root of a polynomial $p$ if $p(x) = 0$. We use the well-known fact that any nonzero, degree-t polynomial over a field has at most $t$ roots. This implies:

若 $p(x) = 0$，则称值 $x \in \mathbb{F}$ 是多项式 $p$ 的根。我们要用到众所周知的事实：域上任意非零的 $t$ 次多项式至多有 $t$ 个根。由此可得：

COROLLARY 15.15 Any two distinct degree-$t$ polynomials $p$ and $q$ agree on at most $t$ points.

推论 15.15　任意两个不同的 $t$ 次多项式 $p$ 与 $q$ 至多在 $t$ 个点上取值相同。

PROOF If not, then the nonzero, degree-$t$ polynomial $p - q$ would have more than $t$ roots.

证明　否则的话，非零的 $t$ 次多项式 $p - q$ 就会有多于 $t$ 个根。

Shamir’s scheme relies on the fact that for any $t$ pairs of elements $(x_1, y_1)$, $\ldots$, ( $x_t$, $y_t$ ) from $\mathbb{F}$ (with the $\{x_i\}$ distinct), there is a unique polynomial $p$ of degree $t-1$ such that $p(x_i)=y_i$ for ${1}\leq i\leq t$. We can prove this quite easily. The fact that there exists such a $p$ uses standard polynomial interpolation.

Shamir 方案依赖于如下事实：对取自 $\mathbb{F}$ 的任意 $t$ 对元素 $(x_1, y_1)$, $\ldots$, ( $x_t$, $y_t$ )（诸 $\{x_i\}$ 互不相同），存在唯一的次数为 $t-1$ 的多项式 $p$，使得对所有 ${1}\leq i\leq t$ 都有 $p(x_i)=y_i$。这一点很容易证明。这样的 $p$ 存在，依据的是标准的多项式插值。

In detail: for $i = 1, \ldots, t$, define the degree-$(t - 1)$ polynomial

具体地：对 $i = 1, \ldots, t$，定义次数为 $(t - 1)$ 的多项式

$$
\delta_{i}(X)\stackrel{\mathrm{def}}{=}\frac{\prod_{j=1,j\neq i}^{t}(X-x_{j})}{\prod_{j=1,j\neq i}^{t}(x_{i}-x_{j})}.
$$

Note that $\delta_i(x_j) = 0$ for any $j \neq i$, and $\delta_i(x_i) = 1$. So $p(X) \stackrel{\mathrm{def}}{=} \sum_{i=1}^t \delta_i(X) \cdot y_i$ is a polynomial of degree $(t-1)$ with $p(x_i) = y_i$ for ${1} \leq i \leq t$. (We remark that this, in fact, demonstrates that the desired polynomial $p$ can be found efficiently.) Uniqueness follows from Corollary 15.15.

注意，对任意 $j \neq i$ 都有 $\delta_i(x_j) = 0$，而 $\delta_i(x_i) = 1$。于是 $p(X) \stackrel{\mathrm{def}}{=} \sum_{i=1}^t \delta_i(X) \cdot y_i$ 是一个次数为 $(t-1)$ 的多项式，且对所有 ${1} \leq i \leq t$ 都有 $p(x_i) = y_i$。（我们指出，这实际上也表明所需的多项式 $p$ 可以被高效地求出。）唯一性则由推论 15.15 得出。

We now describe Shamir’s $(t, N)$-threshold secret-sharing scheme. Let $\mathbb{F}$ be a finite field that contains the domain of possible secrets, and with $|\mathbb{F}| > N$. Let $x_1, \ldots, x_N \in \mathbb{F}$ be distinct, nonzero elements that are fixed and publicly known. (Such elements exist since $|\mathbb{F}| > N$) The scheme works as follows:

现在我们来描述 Shamir 的 $(t, N)$-门限秘密共享方案。设 $\mathbb{F}$ 是一个有限域，它包含可能的秘密所在的定义域，且满足 $|\mathbb{F}| > N$。设 $x_1, \ldots, x_N \in \mathbb{F}$ 是互不相同、非零的元素，它们是固定的且公开已知。（由于 $|\mathbb{F}| > N$，这样的元素是存在的。）该方案的工作方式如下：

Sharing: Given a secret $s \in \mathbb{F}$, the dealer chooses uniform $a_1, \ldots, a_{t-1} \in \mathbb{F}$ and defines the polynomial $p(X) \overset{\mathrm{def}}{=} s + \sum_{i=1}^{t-1} a_i X^i$. This is a uniform degree-$(t-1)$ polynomial with constant term $s$. The share of user $P_i$ is $s_i := p(x_i) \in \mathbb{F}$.

共享：给定秘密 $s \in \mathbb{F}$，分发者均匀选取 $a_1, \ldots, a_{t-1} \in \mathbb{F}$，并定义多项式 $p(X) \overset{\mathrm{def}}{=} s + \sum_{i=1}^{t-1} a_i X^i$。这是一个均匀选取的 $(t-1)$ 次多项式，常数项为 $s$。用户 $P_i$ 的份额为 $s_i := p(x_i) \in \mathbb{F}$。

Reconstruction: Say $t$ users $P_{i_1}, \ldots, P_{i_t}$ pool their shares $s_{i_1}, \ldots, s_{i_t}$. Using polynomial interpolation, they compute the unique degree$(t-1)$ polynomial $p^{\prime}$ for which $p^{\prime}(x_{i_j}) = s_{i_j}$ for ${1} \leq j \leq t$. The secret is $p^{\prime}(0)$.

重构：设有 $t$ 个用户 $P_{i_1}, \ldots, P_{i_t}$ 汇集他们的份额 $s_{i_1}, \ldots, s_{i_t}$。利用多项式插值，他们计算出唯一的次数为 $(t-1)$ 的多项式 $p^{\prime}$，使得对所有 ${1} \leq j \leq t$ 都有 $p^{\prime}(x_{i_j}) = s_{i_j}$。秘密即为 $p^{\prime}(0)$。

It is clear that reconstruction works since $p^{\prime}=p$ and $p(0)=s$.

显然重构是可行的，因为 $p^{\prime}=p$ 且 $p(0)=s$。

It remains to show that any $t-1$ users learn nothing about the secret $s$ from their shares. By symmetry, it suffices to consider the shares of users $P_{1},\ldots,P_{t-1}$. We claim that for any secret $s$, the shares $s_{1},\ldots,s_{t-1}$ are (jointly) uniform. Since the dealer chooses $a_{1},\ldots,a_{t-1}$ uniformly, this follows if we show that there is a one-to-one correspondence between the polynomial $p$ chosen by the dealer and the shares $s_{1},\ldots,s_{t-1}$. But this is a direct consequence of Corollary 15.15.

剩下要证明的是：任意 $t-1$ 个用户都无法从各自的份额中获知关于秘密 $s$ 的任何信息。由对称性，只需考虑用户 $P_{1},\ldots,P_{t-1}$ 的份额。我们断言：对任意秘密 $s$，份额 $s_{1},\ldots,s_{t-1}$ 都是（联合）均匀的。由于分发者均匀选取 $a_{1},\ldots,a_{t-1}$，只要证明分发者所选的多项式 $p$ 与份额 $s_{1},\ldots,s_{t-1}$ 之间存在一一对应，即可得出这一结论。而这正是推论 15.15 的直接推论。

### 15.3.2 Verifiable Secret Sharing　可验证秘密共享

So far we have considered passive attacks in which $t-1$ users may try to use their shares to learn information about the secret. But we may also be concerned about active, malicious behavior. Here there are two separate concerns: First, a corrupted dealer may give inconsistent shares to the users, i.e., such that different secrets are recovered depending on which t users pool their shares. Second, in the reconstruction phase a malicious user may present a different share from the one given to them by the dealer, and thus affect the recovered secret. (While this could be addressed by having the dealer sign the shares, this does not work when the dealer itself may be dishonest.) Verifiable secret-sharing (VSS) schemes prevent both these attacks.

迄今为止我们考虑的都是被动攻击：$t-1$ 个用户可能试图利用自己的份额获取关于秘密的信息。但我们还可能关心主动的恶意行为。这里有两个彼此独立的问题：其一，被腐化的分发者可能给各用户不一致的份额，也就是说，随着汇集份额的是哪 $t$ 个用户不同，恢复出的秘密也会不同。其二，在重构阶段，某个恶意用户可能出示与分发者发给他的份额不同的份额，从而影响恢复出的秘密。（虽然可以让分发者对份额签名来解决后一个问题，但当分发者本身可能不诚实时，这种做法就行不通了。）可验证秘密共享（verifiable secret-sharing, VSS）方案能够同时防止这两种攻击。

More formally, we allow any $t-1$ users to be corrupted and to collude with each other and, possibly, the dealer. We require: (1a) at the end of the sharing phase, a secret $s$ is defined such that any set of users that includes $t$ uncorrupted users will successfully recover $s$ in the reconstruction phase; moreover, (1b) if the dealer is honest, then $s$ corresponds to the dealer's secret. In addition, (2) when the dealer is honest then, as before, any set of $t-1$ corrupted users learns nothing about the secret from their shares and any public information the dealer publishes. Since we want there to be $t$ uncorrupted users even if $t-1$ users are corrupted, we require $N \geq t + (t-1)$ or $N > 2t$; in other words, we assume a majority of the users remain uncorrupted.

更形式化地说，我们允许任意 $t-1$ 个用户被腐化并相互勾结，还可能与分发者勾结。我们要求：(1a) 在共享阶段结束时确定了一个秘密 $s$，使得任何包含 $t$ 个未腐化用户的用户集合都能在重构阶段成功恢复 $s$；此外，(1b) 若分发者是诚实的，则 $s$ 对应于分发者的秘密。另外，(2) 当分发者诚实时，如前所述，任意 $t-1$ 个被腐化的用户都无法从他们的份额以及分发者公开的任何信息中获知关于秘密的任何内容。因为我们希望即使有 $t-1$ 个用户被腐化，仍有 $t$ 个未腐化的用户存在，所以要求 $N \geq t + (t-1)$，即 $N > 2t$；换句话说，我们假设多数用户保持未腐化。

> 译注：原书此处印作 “$N \geq t + (t-1)$ or $N > 2t$”。严格地说，$N \geq t + (t-1)$ 即 $N \geq 2t - 1$，等价于 $N > 2t - 2$。

We describe a VSS scheme due to Feldman that relies on an algorithm $\mathcal{G}$ relative to which the discrete-logarithm problem is hard. For simplicity, we describe it in the random-oracle model and let $H$ denote a function to be modeled as a random oracle. We also assume that some trusted parameters $(\mathbb{G}, q, g)$, generated using $\mathcal{G}(1^n)$, are published in advance, where $q$ is prime and so $\mathbb{Z}_q$ is a field. Finally, we assume that all users have access to a broadcast channel, such that a message broadcast by any user is heard by everyone.

我们描述一种由 Feldman 提出的 VSS 方案，它依赖于一个算法 $\mathcal{G}$，相对于该算法离散对数问题是困难的。为简单起见，我们在随机预言机模型下描述该方案，并令 $H$ 表示一个将被建模为随机预言机的函数。我们还假设某些可信参数 $(\mathbb{G}, q, g)$ 已事先公布，这些参数由 $\mathcal{G}(1^n)$ 生成，其中 $q$ 是素数，因而 $\mathbb{Z}_q$ 是一个域。最后，我们假设所有用户都能访问一个广播信道，任一用户广播的消息所有人都能听到。

The sharing phase now involves the N users running an interactive protocol with the dealer that proceeds as follows:

此时，共享阶段由 $N$ 个用户与分发者运行一个交互式协议，过程如下：

1. To share a secret $s$, the dealer chooses uniform $a_0 \in \mathbb{Z}_q$ and then shares $a_0$ as in Shamir's scheme. That is, the dealer chooses uniform $a_1, \ldots, a_{t-1} \in \mathbb{Z}_q$ and defines the polynomial $p(X) \overset{\mathrm{def}}{=} \sum_{j=0}^{t-1} a_j X^j$. The dealer sends the share $s_i := p(i) = \sum_{j=0}^{t-1} a_j \cdot i^j$ to user $P_i$.³

1. 要共享秘密 $s$，分发者均匀选取 $a_0 \in \mathbb{Z}_q$，然后按 Shamir 方案的方式共享 $a_0$。也就是说，分发者均匀选取 $a_1, \ldots, a_{t-1} \in \mathbb{Z}_q$，并定义多项式 $p(X) \overset{\mathrm{def}}{=} \sum_{j=0}^{t-1} a_j X^j$。分发者把份额 $s_i := p(i) = \sum_{j=0}^{t-1} a_j \cdot i^j$ 发送给用户 $P_i$。³

> $^3$ Note that we are now setting $x_i = i$, which is fine since we are using the field $\mathbb{Z}_q$.

> $^3$ 注意我们现在取 $x_i = i$；由于使用的是域 $\mathbb{Z}_q$，这样做是没有问题的。

In addition, the dealer publicly broadcasts the values $A_0 := g^{a_0}, \ldots$, $A_{t-1} := g^{a_{t-1}}$, and the “masked secret” $c := H(a_0) \oplus s$.

此外，分发者公开广播值 $A_0 := g^{a_0}, \ldots$, $A_{t-1} := g^{a_{t-1}}$，以及“被掩盖的秘密” $c := H(a_0) \oplus s$。

2. Each user $P_{i}$ verifies that its share $s_{i}$ satisfies

2. 每个用户 $P_{i}$ 验证自己的份额 $s_{i}$ 是否满足

$$
g^{s_{i}}\stackrel{?}{=}\prod_{j=0}^{t-1}(A_{j})^{i^{j}}.
$$

If not, $P_{i}$ publicly broadcasts a complaint.

若不满足，则 $P_{i}$ 公开广播一条投诉。

Note that if the dealer is honest, we have

注意，若分发者是诚实的，则有

$$
\prod_{j=0}^{t-1}(A_{j})^{i^{j}}=\prod_{j=0}^{t-1}\left(g^{a_{j}}\right)^{i^{j}}=g^{\sum_{j=0}^{t-1}a_{j}\cdot i^{j}}=g^{p(i)}=g^{s_{i}}, \tag{15.3}
$$

and so no honest user will complain. Since there are at most $t-1$ corrupted users, there are at most $t-1$ complaints if the dealer is honest.

所以不会有诚实用户投诉。由于被腐化的用户至多 $t-1$ 个，因此当分发者诚实的时候，投诉至多 $t-1$ 条。

3. If more than $t-1$ users complain, the dealer is disqualified and the protocol is aborted. Otherwise, the dealer responds to a complaint from $P_{i}$ by broadcasting $s_{i}$. If this share does not satisfy Equation (15.3) (or if the dealer refuses to respond to a complaint at all), the dealer is disqualified and the protocol is aborted. Otherwise, $P_{i}$ uses the broadcast value (rather than the value it received in the first round) as its share.

3. 如果投诉的用户超过 $t-1$ 个，则分发者被取消资格，协议中止。否则，对于来自 $P_{i}$ 的投诉，分发者通过广播 $s_{i}$ 来回应。如果该份额不满足式 (15.3)（或者分发者干脆拒绝对投诉作出回应），则分发者被取消资格，协议中止。否则，$P_{i}$ 使用广播出的值（而不是它在第一轮收到的值）作为自己的份额。

In the reconstruction phase, say a group of users (that includes at least $t$ uncorrupted users) pool their shares. A share $s_i$ provided by a user $P_i$ is discarded if it does not satisfy Equation (15.3). Among the remaining shares, any $t$ of them are used to recover $a_0$ exactly as in Shamir's scheme. The original secret is then computed as $s := c \oplus H(a_0)$.

在重构阶段，设有某组用户（其中至少包含 $t$ 个未腐化的用户）汇集他们的份额。若用户 $P_i$ 提供的份额 $s_i$ 不满足式 (15.3)，则将其丢弃。在剩下的份额中任取 $t$ 个，按照与 Shamir 方案完全相同的方式来恢复 $a_0$。随后计算原始秘密 $s := c \oplus H(a_0)$。

We now argue that this protocol meets the desired security requirements. We first show that, assuming the dealer is not disqualified, the value recovered in the reconstruction phase is uniquely determined by the public information; specifically, the recovered value is $c \oplus H(\log_g A_0)$. (Combined with the fact that an honest dealer is never disqualified, this proves that conditions (1a) and (1b) hold.) Define $a_i := \log_g A_i$ for ${0} \leq i \leq t - 1$; the $\{a_i\}$ cannot be computed efficiently if the discrete-logarithm problem is hard, but they are still well-defined. Define the polynomial $p(X) \overset{\mathrm{def}}{=} \sum_{i=0}^{t-1} a_i X^i$. Any share $s_i$, contributed by party $P_i$, that is not discarded during the reconstruction phase must satisfy Equation (15.3), and hence satisfies $s_i = p(i)$. It follows that, regardless of which shares are used, the parties will reconstruct polynomial $p$, compute $a_0 = p(0)$, and then recover $s = c \oplus H(a_0)$.

下面我们论证该协议满足所期望的安全需求。我们首先证明：假设分发者未被取消资格，那么重构阶段恢复出的值由公开信息唯一确定；具体而言，恢复出的值为 $c \oplus H(\log_g A_0)$。（结合“诚实的分发者绝不会被取消资格”这一事实，这就证明了条件 (1a) 和 (1b) 成立。）对 ${0} \leq i \leq t - 1$ 定义 $a_i := \log_g A_i$；若离散对数问题是困难的，这些 $\{a_i\}$ 无法被高效计算，但它们仍然是良定义的。定义多项式 $p(X) \overset{\mathrm{def}}{=} \sum_{i=0}^{t-1} a_i X^i$。重构阶段中任何一方 $P_i$ 提交的、未被丢弃的份额 $s_i$ 必然满足式 (15.3)，因而满足 $s_i = p(i)$。由此可知，无论使用了哪些份额，各方都会重构出多项式 $p$，计算 $a_0 = p(0)$，进而恢复 $s = c \oplus H(a_0)$。

It is also possible to show that condition (2) holds for computationally bounded adversaries if the discrete-logarithm problem is hard for $\mathcal{G}$. (In contrast to Shamir's secret-sharing scheme, secrecy here is no longer unconditional. Unconditionally secure VSS schemes are possible, but are beyond the scope of our treatment.) Intuitively, this is because the secret $s$ is masked by the random value $H(a_0)$, and the information given to any $t-1$ users in the sharing phase—namely, their shares and the public values $\{A_i\}$—reveals only $g^{a_0}$, from which it is hard to compute $a_0$. This intuition can be made rigorous, but we do not do so here.

还可以证明：若离散对数问题对 $\mathcal{G}$ 而言是困难的，则条件 (2) 对计算能力有界的敌手成立。（与 Shamir 秘密共享方案不同，这里的保密性不再是无条件的。无条件安全的 VSS 方案是存在的，但超出了我们的讨论范围。）直观地说，这是因为秘密 $s$ 被随机值 $H(a_0)$ 所掩盖，而共享阶段透露给任意 $t-1$ 个用户的信息——即他们的份额和公开值 $\{A_i\}$——只揭示了 $g^{a_0}$，从中难以计算出 $a_0$。这一直觉可以严格化，但此处不作展开。

### 15.3.3 Threshold Encryption and Electronic Voting　门限加密与电子投票

In Section 15.2.3 we introduced the notion of homomorphic encryption schemes and gave the Paillier encryption scheme as an example. Here we show a different homomorphic encryption scheme that is a variant of El Gamal encryption. Specifically, given a public key $pk = \langle \mathbb{G}, q, g, h \rangle$ as in regular El Gamal encryption, we now encrypt a message $m \in \mathbb{Z}_q$ by setting $M := g^m$, choosing a uniform $y \in \mathbb{Z}_q$, and sending the ciphertext $c := \langle g^y, h^y \cdot M \rangle$. To decrypt, the receiver recovers $M$ as in standard El Gamal decryption and then computes $m := \log_g M$. Although this is not efficient if $m$ comes from a large domain, if $m$ is from a small domain—as it will be in our application—then the receiver can compute $\log_g M$ efficiently using exhaustive search. The advantage of this variant scheme is that it is homomorphic with respect to addition in $\mathbb{Z}_q$. That is,

在 15.2.3 节中我们介绍了同态加密方案的概念，并给出了 Paillier 加密方案作为例子。这里我们展示另一种同态加密方案，它是 El Gamal 加密的一个变体。具体来说，给定与常规 El Gamal 加密一样的公钥 $pk = \langle \mathbb{G}, q, g, h \rangle$，现在这样加密消息 $m \in \mathbb{Z}_q$：令 $M := g^m$，均匀选取 $y \in \mathbb{Z}_q$，并发送密文 $c := \langle g^y, h^y \cdot M \rangle$。解密时，接收方像标准 El Gamal 解密那样恢复出 $M$，然后计算 $m := \log_g M$。虽然当 $m$ 来自很大的定义域时这样做并不高效，但如果 $m$ 来自小的定义域——在我们的应用中正是如此——那么接收方可以用穷举搜索高效地计算 $\log_g M$。这个变体方案的优点在于它关于 $\mathbb{Z}_q$ 中的加法是同态的。也就是说，

$$
\langle g^{y_{1}},~h^{y_{1}}\cdot g^{m_{1}}\rangle\cdot\langle g^{y_{2}},~h^{y_{2}}\cdot g^{m_{2}}\rangle=\langle g^{y_{1}+y_{2}},~h^{y_{1}+y_{2}}\cdot g^{m_{1}+m_{2}}\rangle.
$$

Recall that the basic approach to electronic voting using homomorphic encryption has each voter $i$ encrypt her vote $v_i \in \{0,1\}$ to obtain a ciphertext $c_i$. Once everyone has voted, the ciphertexts are multiplied to obtain an encryption of the sum $v_{total} \stackrel{\mathrm{def}}{=} \sum_i v_i \bmod q = \sum_i v_i$. (The value $q$ is, in practice, large enough so that no wrap-around modulo $q$ occurs.) Since ${0} \leq v_{total} \leq \ell$, where $\ell$ is the total number of voters, an authority with the private key can efficiently decrypt the final ciphertext and recover $v_{total}$.

回顾一下，利用同态加密实现电子投票的基本做法是：每个投票人 $i$ 加密自己的选票 $v_i \in \{0,1\}$ 得到密文 $c_i$。所有人投票完毕后，将各密文相乘，得到和 $v_{total} \stackrel{\mathrm{def}}{=} \sum_i v_i \bmod q = \sum_i v_i$ 的一个加密。（实践中 $q$ 取得足够大，因此不会发生模 $q$ 的回绕。）由于 ${0} \leq v_{total} \leq \ell$（$\ell$ 为投票人总数），持有私钥的管理机构可以高效地解密最终密文并恢复 $v_{total}$。

A drawback of this approach is that the authority is trusted, both to (correctly) decrypt the final ciphertext as well as not to decrypt any of the individual voters' ciphertexts. (In Section 15.2.3 we assumed the authority could not see the individual voters' ciphertexts.) We might instead prefer to distribute trust among a set of $N$ authorities, such that any set of $t$ authorities is able to jointly decrypt an agreed-upon ciphertext (this ensures availability even if some authorities are down or unwilling to help decrypt), but no collection of $t-1$ authorities is able to decrypt any ciphertext on their own (this ensures privacy as long as fewer than $t$ authorities are corrupted).

这种做法的一个缺陷在于管理机构必须被信任：既要相信它会（正确地）解密最终密文，又要相信它不会去解密任何单个投票人的密文。（在 15.2.3 节中我们假设管理机构看不到各个投票人的密文。）我们或许更愿意把信任分散到一组共 $N$ 个管理机构之中：任意 $t$ 个管理机构能够共同解密一份约定的密文（即使某些管理机构宕机或不愿协助解密，也能保证可用性），而任意 $t-1$ 个管理机构的组合都无法自行解密任何密文（只要被腐化的管理机构少于 $t$ 个，就能保证隐私性）。

At first glance, it may seem that secret sharing solves the problem. If we share the private key among the $N$ authorities, then no set of $t-1$ authorities learns the private key and so they cannot decrypt. On the other hand, any $t$ authorities can pool their shares, recover the private key, and then decrypt any desired ciphertext.

初看起来，似乎秘密共享就能解决这个问题。如果把私钥在 $N$ 个管理机构之间共享，那么任何 $t-1$ 个管理机构都得不到私钥，因而无法解密；另一方面，任意 $t$ 个管理机构可以汇集各自的份额、恢复私钥，然后解密任何想要的密文。

A little thought shows that this does not quite work. If the authorities reconstruct the private key in order to decrypt some ciphertext, then as part of this process all the authorities learn the private key! Thus, afterward, any authority could decrypt any ciphertext of its choice, on its own.

稍加思考就会发现这并不完全可行。如果这些管理机构为了解密某个密文而重构私钥，那么作为这一过程的组成部分，所有管理机构都会得知私钥！这样一来，事后任何一个管理机构都可以自行解密自己选定的任意密文。

We need instead a modified approach in which the “secret” (namely, the private key) is never reconstructed in the clear, yet is implicitly reconstructed only enough to enable decryption of one, agreed-upon ciphertext. We can achieve this for the specific case of El Gamal encryption in the following way. Fix a public key $pk = \langle \mathbb{G}, q, g, h \rangle$, and let $x \in \mathbb{Z}_q$ be the private key, i.e., $g^x = h$. Each authority is given a share $x_i \in \mathbb{Z}_q$ exactly as in Shamir’s secret-sharing scheme. That is, a uniform degree-$(t-1)$ polynomial $p$ with $p(0) = x$ is chosen, and the $i$th authority is given $x_i := p(i)$. (We assume a trusted dealer who knows $x$ and securely deletes it once it is shared. It is possible to eliminate the dealer entirely, but this is beyond our present scope.)

我们需要的是一种改进的方法：“秘密”（即私钥）永远不以明文形式被重构，而只是被隐式地重构到刚好足以解密某一份约定密文的程度。针对 El Gamal 加密这一特定情形，我们可以按下述方式做到这一点。固定公钥 $pk = \langle \mathbb{G}, q, g, h \rangle$，设私钥为 $x \in \mathbb{Z}_q$，即 $g^x = h$。每个管理机构得到的份额 $x_i \in \mathbb{Z}_q$ 与 Shamir 秘密共享方案中的完全一样。也就是说，均匀选取一个次数为 $(t-1)$ 的多项式 $p$，使其满足 $p(0) = x$，第 $i$ 个管理机构得到 $x_i := p(i)$。（我们假设存在一个知道 $x$ 的可信分发者，它在完成共享后安全删除 $x$。完全去掉分发者也是可能的，但这超出了当前的讨论范围。）

Now, say some $t$ authorities $i_1, \ldots, i_t$ wish to jointly decrypt a ciphertext $\langle c_1, c_2 \rangle$. To do so, authority $i_j$ first publishes the value $w_j := c_1^{x_{i_j}}$. Recall from the previous section that there exist publicly computable polynomials $\{\delta_j(X)\}$ (that depend on the identities of these $t$ authorities) such that $p(X) \overset{\mathrm{def}}{=} \sum_{j=1}^{t} \delta_j(X) \cdot x_{i_j}$. Setting $\delta_j \overset{\mathrm{def}}{=} \delta_j(0)$, we see that there exist publicly computable values $\delta_1, \ldots, \delta_t \in \mathbb{Z}_q$ for which $x = p(0) = \sum_{j=1}^{t} \delta_j \cdot x_{i_j}$. Any authority can then compute

现在，设有某 $t$ 个管理机构 $i_1, \ldots, i_t$ 想要共同解密密文 $\langle c_1, c_2 \rangle$。为此，管理机构 $i_j$ 先公布值 $w_j := c_1^{x_{i_j}}$。回忆前一节的内容：存在可公开计算的多项式 $\{\delta_j(X)\}$（它们依赖于这 $t$ 个管理机构的身份），使得 $p(X) \overset{\mathrm{def}}{=} \sum_{j=1}^{t} \delta_j(X) \cdot x_{i_j}$。令 $\delta_j \overset{\mathrm{def}}{=} \delta_j(0)$，可以看到存在可公开计算的值 $\delta_1, \ldots, \delta_t \in \mathbb{Z}_q$，使得 $x = p(0) = \sum_{j=1}^{t} \delta_j \cdot x_{i_j}$。于是任何管理机构都能计算

$$
M^{\prime}:=\frac{c_{2}}{\prod_{j=1}^{t}w_{j}^{\delta_{j}}}.
$$

(They can then each compute $\log_g M$, if desired.) To see that this correctly recovers the message, say $c_1 = g^y$ and $c_2 = h^y \cdot M$. Then

（如有需要，它们随后各自计算 $\log_g M$。）为说明这确实正确恢复了消息，设 $c_1 = g^y$、$c_2 = h^y \cdot M$。那么

$$
\prod_{j=1}^{t}w_{j}^{\delta_{j}}=\prod_{j=1}^{t}c_{1}^{x_{i_{j}}\delta_{j}}=c_{1}^{\sum_{j=1}^{t}x_{i_{j}}\delta_{j}}=c_{1}^{p(0)}=c_{1}^{x},
$$

and so

于是

$$
M^{\prime}\stackrel{\mathrm{def}}{=}\frac{c_{2}}{\prod_{j=1}^{t}w_{j}^{\delta_{j}}}=\frac{h^{y}\cdot M}{c_{1}^{x}}=\frac{(g^{x})^{y}\cdot M}{(g^{y})^{x}}=M.
$$

Note that any set of $t-1$ corrupted authorities learns nothing about the private key $x$ from their shares. Moreover, it is possible to show that they learn nothing from the decryption process beyond the recovered value $M$.

注意，任意 $t-1$ 个被腐化的管理机构都无法从各自的份额中获得关于私钥 $x$ 的任何信息。此外，还可以证明：除恢复出的值 $M$ 之外，它们从解密过程中得不到任何其他信息。

Malicious (active) adversaries. Our treatment above assumes that the authorities decrypting some ciphertext all behave correctly. (If they do not, it would be easy for any of them to cause an incorrect result by publishing an arbitrary value $w_j$.) We also assume that voters behave honestly, and encrypt a vote of either 0 or 1. (Note that a voter could unfairly sway the election by encrypting a large value or a negative value.) Potential malicious behavior of this sort can be prevented using techniques beyond the scope of this book.

**恶意（主动）敌手。**

上面的讨论假设参与解密某个密文的所有管理机构行为都是正确的。（如果不正确，那么其中任何一个管理机构都可以通过公布一个任意值 $w_j$ 轻易导致错误结果。）我们还假设投票人诚实行事，加密的选票非 0 即 1。（注意，投票人可以通过加密一个很大的值或负值来不公平地左右选举结果。）这类潜在的恶意行为可以利用超出本书范围的技术加以防范。
