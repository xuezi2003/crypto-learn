# Chapter 7: Practical Constructions of Symmetric-Key Primitives　第七章　对称密钥原语的实际构造

In previous chapters we have demonstrated how secure encryption schemes and message authentication codes can be constructed from cryptographic primitives such as pseudorandom generators (aka stream ciphers), pseudo-random permutations (aka block ciphers), and hash functions. One question we have not yet addressed, though, is how these cryptographic primitives are constructed in the first place, or even whether they exist at all! In the next chapter we will study this question from a theoretical point of view, and show constructions of pseudorandom generators and pseudorandom permutations based on quite weak assumptions. (It turns out that collision-resistant hash functions are more difficult to construct, and appear to require stronger assumptions. We will see a provably secure construction in Section 9.4.2.) In this chapter, our focus will be on comparatively heuristic—but far more efficient—constructions of these primitives that are widely used in practice.

在前几章中，我们展示了如何从伪随机生成器（又称流密码）、伪随机置换（又称分组密码）和哈希函数等密码学原语构造安全的加密方案和消息认证码。然而，我们尚未回答的一个问题是：这些密码学原语本身是如何构造的，甚至它们是否真的存在！在下一章中，我们将从理论角度研究这个问题，并展示基于相当弱的假设构造伪随机生成器和伪随机置换的方法。（事实证明，抗碰撞哈希函数更难构造，似乎需要更强的假设。我们将在 9.4.2 节看到一个可证明安全的构造。）在本章中，我们将聚焦于这些原语的相对启发式、但效率高得多的构造，这些构造在实践中被广泛使用。

The constructions we will explore in this chapter are heuristic in the sense that they cannot be proven secure based on any weaker assumption. Nevertheless, they are based on a number of sound design principles that can be justified by theoretical analysis. Perhaps more importantly, many of these constructions have withstood years of public scrutiny and attempted cryptanalysis; given this, it is quite reasonable to assume they are secure.

本章中我们将探讨的构造是启发式的，意思是不可能基于任何更弱的假设来证明它们的安全性。尽管如此，它们基于若干可通过理论分析加以证实的合理设计原则。或许更重要的是，许多构造已经经受住了多年的公开审查和密码分析尝试；鉴于此，完全可以合理地假设它们是安全的。

In some sense there is no fundamental difference between assuming, say, that factoring is hard and assuming that AES (a block cipher we will study later in this chapter) is a pseudorandom permutation. There is, however, a significant qualitative difference between these assumptions. $^{1}$ The primary difference is that the former assumption relates to a weaker requirement: the assumption that large integers are hard to factor is arguably simpler and more natural than the assumption that AES with a uniform key is indistinguishable from a random permutation. Other relevant differences are that factoring has been studied much longer than the problem of distinguishing AES from a random permutation, and that factoring was recognized as a hard problem by mathematicians independent of any cryptographic applications. The factoring problem has also been studied for a longer period of time.

在某种意义上，假设整数分解困难与假设 AES（一种我们将在本章后面学习的分组密码）是伪随机置换之间没有根本区别。然而，这两种假设之间存在显著的定性差异。$^{1}$ 主要区别在于前一种假设涉及更弱的要求：假设大整数难以分解可以说比假设使用均匀密钥的 AES 与随机置换不可区分更简单、更自然。其他相关差异包括：对整数分解的研究时间远长于对区分 AES 与随机置换问题的研究，而且整数分解被数学家认定为困难问题，与任何密码学应用无关。整数分解问题也被研究了更长的时间。

$^{1}$ This discussion assumes the reader has some familiarity with number-theoretic assumptions such as the factoring assumption; see Chapter 9.

$^{1}$ 本讨论假设读者对整数分解假设等数论假设有一定的了解；参见第 9 章。

**Aims of This Chapter　本章目标**

The main aims of this chapter are (1) to present some design principles used in the construction of modern cryptographic primitives, and (2) to introduce the reader to some popular schemes used in the real world. We caution that:

本章的主要目标是：(1) 介绍现代密码学原语构造中使用的一些设计原则，(2) 向读者介绍一些实际使用的流行方案。我们要提醒的是：

- It is not the aim of this chapter to teach readers how to design new cryptographic primitives. On the contrary, we believe that the design of new primitives requires significant expertise and effort, and is not something to be attempted lightly. Those who are interested in developing additional expertise in this area are advised to read the more advanced references included at the end of the chapter.

  本章的目的不是教读者如何设计新的密码学原语。相反，我们认为新原语的设计需要大量的专业知识和精力，不应轻易尝试。有兴趣在此领域进一步深造的读者，建议阅读本章末尾列出的更高级参考文献。

- It is not our intent to present all the low-level details of the various primitives we discuss here, and our descriptions should not be relied upon for implementation. In fact, our descriptions are sometimes purposefully inaccurate, as we omit certain details that are not relevant to the broader conceptual point we are trying to emphasize.

  我们并非旨在呈现此处讨论的各种原语的所有底层细节，我们的描述不应当作实现的依据。事实上，我们的描述有时故意不够精确，因为我们省略了与我们要强调的更广泛概念要点无关的某些细节。

## 7.1 Stream Ciphers　7.1 流密码

Recall from Section 3.6.1 that a stream cipher is defined by two deterministic algorithms (Init, Next). The Init algorithm takes as input a key $k$ (sometimes also called a seed) and optionally an initialization vector $IV$, and returns an initial state $st$. The Next algorithm can then be called repeatedly (updating the state after each invocation) to generate an unbounded stream of random-looking bits. A stream cipher that does not take an $IV$ should behave like a pseudorandom generator: namely, when the key $k$ is uniform then the sequence of generated bits should be indistinguishable from a sequence of uniform and independent bits. When a stream cipher takes an $IV$ then it should act like a pseudorandom function; that is, for a uniform key $k$ and distinct (known) initialization vectors $IV_1, IV_2, \ldots, IV_\ell$, the $\ell$ sequences of bits generated using $k$ and each $IV$ should be indistinguishable from $\ell$ sequences of independent, uniform bits. We refer to Section 3.6.1 for formal definitions.

回顾 3.6.1 节可知，流密码由两个确定性算法 (Init, Next) 定义。Init 算法以密钥 $k$（有时也称为种子）和可选的初始化向量 $IV$ 为输入，返回一个初始状态 $st$。然后可以重复调用 Next 算法（每次调用后更新状态）来生成无限长的看似随机的比特流。不接受 $IV$ 的流密码应当表现得像伪随机生成器：即当密钥 $k$ 均匀时，生成的比特序列应当与均匀且独立的比特序列不可区分。接受 $IV$ 的流密码应当表现得像伪随机函数；即对于均匀密钥 $k$ 和不同的（已知的）初始化向量 $IV_1, IV_2, \ldots, IV_\ell$，使用 $k$ 和每个 $IV$ 生成的 $\ell$ 条比特序列应当与 $\ell$ 条独立的均匀比特序列不可区分。形式化定义参见 3.6.1 节。

In this section we consider three stream ciphers constructed in very different ways. Trivium is a standardized stream cipher that is very efficient in hardware. It is based on feedback shift registers, a topic of independent interest that we discuss in Sections 7.1.1 and 7.1.2. $\mathsf{RC4}$ is a software-optimized stream cipher developed in 1987 that was widely used for over twenty years. Although several weaknesses in RC4 have been discovered (and it should no longer be used), it is still interesting to study. We end with a discussion of ChaCha20, a modern stream cipher with good performance in software that has been adopted as a replacement for RC4 in several internet standards.

在本节中，我们考虑三种以截然不同的方式构造的流密码。Trivium 是一种标准化的流密码，在硬件上非常高效。它基于反馈移位寄存器，这是一个具有独立研究价值的主题，我们在 7.1.1 和 7.1.2 节中讨论。$\mathsf{RC4}$ 是一种于 1987 年开发、面向软件优化的流密码，曾被广泛使用超过二十年。虽然 RC4 的若干弱点已被发现（且不应再使用），但它仍然值得研究。我们最后讨论 ChaCha20，这是一种在软件上具有良好性能的现代流密码，已被多个互联网标准采纳为 RC4 的替代品。

### 7.1.1 Linear-Feedback Shift Registers　7.1.1 线性反馈移位寄存器

We begin by discussing linear-feedback shift registers (LFSRs). These have been used historically for pseudorandom-number generation, as they are extremely efficient to implement in hardware, and generate output with good statistical properties. By themselves, however, they do not give cryptographically strong pseudorandom generators. Nevertheless, LFSRs (and their nonlinear generalizations that we discuss in the next section) can be used as a component of secure stream-cipher designs.

我们首先讨论线性反馈移位寄存器（linear-feedback shift register，LFSR）。LFSR 在历史上被用于伪随机数生成，因为它们在硬件中实现极为高效，且生成的输出具有良好的统计性质。然而，LFSR 本身并不能给出密码学上强的伪随机生成器。尽管如此，LFSR（以及我们在下一节讨论的非线性推广）可以作为安全流密码设计的一个组件。

![Image](https://lsky.jerryxue.top/i/2026/08/19/6a85c5382cb7e.jpg)

**FIGURE 7.1: A linear-feedback shift register.**

**图 7.1：一个线性反馈移位寄存器。**

An LFSR consists of an array of $n$ registers $s_{n-1},\ldots,s_0$ along with a feedback loop specified by a set of $n$ boolean feedback coefficients $c_{n-1},\ldots,c_0$. (See Figure 7.1.) The size of the array is called the degree of the LFSR. Each register stores a single bit, and the state $\mathbf{st}$ of an LFSR at any point in time consists of the bits contained in its registers. The state of an LFSR is updated in each of a series of "clock ticks" by shifting the values in all the registers to the right, and setting the new value of the left-most register equal to the XOR of some subset of the current registers determined by the feedback coefficients. That is, if the state at some time $t$ is $s_{n-1}^{(t)},\ldots,s_0^{(t)}$, then the state after the next clock tick is $s_{n-1}^{(t+1)},\ldots,s_0^{(t+1)}$ with

LFSR 包含一个由 $n$ 个寄存器 $s_{n-1},\ldots,s_0$ 组成的阵列，以及一个由 $n$ 个布尔反馈系数 $c_{n-1},\ldots,c_0$ 指定的反馈回路。（见图 7.1。）阵列的大小称为 LFSR 的次数。每个寄存器存储一个比特，LFSR 在任意时刻的状态 $\mathbf{st}$ 由其各寄存器中包含的比特组成。在每个时钟节拍，LFSR 的状态按如下方式更新：将所有寄存器中的值右移，并把最左边寄存器的新值设为由反馈系数决定的当前寄存器某个子集的异或。也就是说，如果某时刻 $t$ 的状态为 $s_{n-1}^{(t)},\ldots,s_0^{(t)}$，则下一个时钟节拍后的状态为 $s_{n-1}^{(t+1)},\ldots,s_0^{(t+1)}$，其中

$$
\begin{align*}s_{i}^{(t+1)}&:=s_{i+1}^{(t)},\quad&i&=0,\ldots,n-2\\s_{n-1}^{(t+1)}&:=\bigoplus_{i=0}^{n-1}c_{i} s_{i}^{(t)}.\end{align*}
$$

Figure 7.1 shows a degree-4 LFSR with $c_0 = c_2 = 1$ and $c_1 = c_3 = 0$.

图 7.1 展示了一个次数为 4 的 LFSR，其中 $c_0 = c_2 = 1$ 且 $c_1 = c_3 = 0$。

At each clock tick, the LFSR outputs the value of the right-most register $s_0$. If the initial state of the LFSR is $s_{n-1}^{(0)}, \ldots, s_0^{(0)}$, the first $n$ bits of the output stream are exactly $s_0^{(0)}, \ldots, s_{n-1}^{(0)}$. The next output bit is $s_{n-1}^{(1)} = \bigoplus_{i=0}^{n-1} c_i s_i^{(0)}$. In general, if we denote the output bits by $y_0, y_1, \ldots$, where $y_i = s_0^{(i)}$, then

在每个时钟节拍，LFSR 输出最右边寄存器 $s_0$ 的值。如果 LFSR 的初始状态为 $s_{n-1}^{(0)}, \ldots, s_0^{(0)}$，则输出流的前 $n$ 个比特恰好是 $s_0^{(0)}, \ldots, s_{n-1}^{(0)}$。下一个输出比特是 $s_{n-1}^{(1)} = \bigoplus_{i=0}^{n-1} c_i s_i^{(0)}$。一般地，如果我们记输出比特为 $y_0, y_1, \ldots$，其中 $y_i = s_0^{(i)}$，则

$$
\begin{array}{l l}{y_{i}=s_{i}^{(0)}}&{i=0,\ldots,n-1}\\ {y_{i}=\bigoplus_{j=0}^{n-1}c_{j}y_{i-n+j}}&{i>n-1.}\\ \end{array}
$$

As an example using the LFSR from Figure 7.1, if the initial state is $(s_3, s_2, s_1, s_0) = (0, 0, 1, 1)$ then the states for the first five time periods are

以图 7.1 中的 LFSR 为例，如果初始状态为 $(s_3, s_2, s_1, s_0) = (0, 0, 1, 1)$，则前五个时段的状态为

| (0,0,1,1) |
| --- |
| (1,0,0,1) |
| (1,1,0,0) |
| (1,1,1,0) |
| (1,1,1,1) |

and the output (which can be read off the right-most column of the above) is the stream of bits 1, 1, 0, 0, 1, ...

而输出（可以从上面最右列读出）是比特流 1, 1, 0, 0, 1, ...

A degree-$n$ LFSR can be used to define a stream cipher (Init, Next) in the natural way. Init takes as input an $n$-bit key $k$ and sets the initial state of the LFSR to $k$. Next corresponds to one clock tick, outputting a single bit and updating the state of the LFSR accordingly.

次数为 $n$ 的 LFSR 可以自然地定义出流密码 (Init, Next)。Init 以 $n$ 比特密钥 $k$ 为输入，将 LFSR 的初始状态设为 $k$。Next 对应一个时钟节拍，即输出一个比特并相应更新 LFSR 的状态。

A degree-$n$ LFSR has ${2}^n$ possible states corresponding to the possible values of the bits in its registers. Define the transition graph of an LFSR to be a directed graph with a vertex corresponding to each state, and an edge from one vertex $v$ to another vertex $v^{\prime}$ if updating the state corresponding to $v$ in one clock tick results in the state corresponding to $v^{\prime}$. (Thus, each vertex has a single outgoing edge.) We further label the edges of the graph with the bit that would be output by the LFSR when making the corresponding transition. For example, in the transition graph for the LFSR from Figure 7.1 the vertex $(1,0,0,1)$ has an edge to the vertex $(1,1,0,0)$ labeled with the bit '1.' Choosing a random initial state for the LFSR and then updating the LFSR in a series of clock ticks is thus equivalent to choosing a random initial vertex $v$ and then following the path of directed edges (and outputting the corresponding bits on those edges) beginning at $v$.

次数为 $n$ 的 LFSR 有 ${2}^n$ 个可能的状态，对应于其寄存器中比特的可能取值。将 LFSR 的状态转移图定义为一个有向图：每个状态对应一个顶点；若顶点 $v$ 对应的状态经过一个时钟节拍的更新后变为顶点 $v^{\prime}$ 对应的状态，则从 $v$ 到 $v^{\prime}$ 有一条边。（因此每个顶点只有一条出边。）我们进一步用 LFSR 在执行相应转移时输出的比特标记图的边。例如，在图 7.1 中 LFSR 的状态转移图中，顶点 $(1,0,0,1)$ 有一条边指向顶点 $(1,1,0,0)$，标记为比特 ‘1’。为 LFSR 选择一个随机初始状态，然后在一系列时钟节拍中更新 LFSR，这等价于选择一个随机初始顶点 $v$，然后从 $v$ 出发沿着有向边的路径（并输出这些边上对应的比特）行进。

A degree-$n$ LFSR will eventually repeat some previous state; once it does, it will then repeatedly cycle among some set of states, and the bits it outputs will begin repeating as well. This corresponds to being in a cycle of the transition graph. The LFSR is $\text{maximum length}$ if it cycles through all ${2}^n - 1$ nonzero states before repeating; i.e., its transition graph contains a cycle through all ${2}^n - 1$ nonzero states. (In the transition graph for any LFSR, the all-0 state has a self-loop. If the all-0 state is ever reached the LFSR remains in that state forever.) If an LFSR is maximum length then, when initialized in any nonzero state, it will cycle through all ${2}^n - 1$ nonzero states. Whether an LFSR is maximum length depends only on its feedback coefficients. It is well understood how to set the feedback coefficients so as to obtain a maximum-length LFSR, although the details are beyond the scope of this book.

次数为 $n$ 的 LFSR 最终会重复某个先前状态；一旦如此，它将在某个状态集合中循环往复，输出的比特也将开始重复。这对应于处于状态转移图的一个环中。如果 LFSR 在重复之前遍历所有 ${2}^n - 1$ 个非零状态，则称该 LFSR 为**最大长度**的；即其状态转移图包含一个经过所有 ${2}^n - 1$ 个非零状态的环。（在任何 LFSR 的状态转移图中，全 0 状态有一个自环。一旦达到全 0 状态，LFSR 将永远停留在该状态。）如果 LFSR 是最大长度的，那么当以任意非零状态初始化时，它将遍历所有 ${2}^n - 1$ 个非零状态。LFSR 是否为最大长度的仅取决于其反馈系数。如何设置反馈系数以获得最大长度 LFSR 是众所周知的，尽管其细节超出了本书的范围。

Key-recovery attacks on LFSRs. The output of a maximum-length LFSR has good statistical properties; as just one example, the output stream contains roughly an equal number of 0s and 1s. Nevertheless, LFSRs are not secure stream ciphers. If we assume the feedback coefficients of the LFSR are known (as we should, following Kerckhoffs' principle), then the first $n$ bits of output from a degree-$n$ LFSR reveal the initial state (i.e., the key); once that is known, all future output bits can be computed. One might try to prevent this by using the key to also set the feedback coefficients; even in this case, however, the attacker can learn the entire key after observing at most ${2}n$ output bits. The first $n$ output bits $y_0, \ldots, y_{n-1}$ of the LFSR reveal the entire initial state, as before. Given the next $n$ output bits $y_n, \ldots, y_{2n-1}$, the attacker can set up a system of $n$ linear equations in the $n$ unknown feedback coefficients $c_{n-1}, \ldots, c_0$:

针对 LFSR 的密钥恢复攻击。最大长度 LFSR 的输出具有良好的统计性质；仅举一例，输出流中包含大致相等数量的 0 和 1。然而，LFSR 不是安全的流密码。如果我们假设 LFSR 的反馈系数是公开的（根据 Kerckhoffs 原则我们应当如此假设），那么次数为 $n$ 的 LFSR 的前 $n$ 个输出比特就暴露了初始状态（即密钥）；一旦知道了初始状态，所有未来的输出比特都可以被计算。人们可能试图用密钥同时设置反馈系数来防止这一点；但即使在这种情况下，攻击者在观察最多 ${2}n$ 个输出比特后也能恢复出完整密钥。如前所述，LFSR 的前 $n$ 个输出比特 $y_0, \ldots, y_{n-1}$ 暴露了完整的初始状态。给定接下来的 $n$ 个输出比特 $y_n, \ldots, y_{2n-1}$，攻击者可以建立关于 $n$ 个未知反馈系数 $c_{n-1}, \ldots, c_0$ 的 $n$ 个线性方程组：

$$
y_{n}=c_{n-1}y_{n-1}\oplus\cdots\oplus c_{0}y_{0}
$$

$$
\cdots
$$

$$
y_{2n-1}=c_{n-1}y_{2n-2}\oplus\cdots\oplus c_{0}y_{n-1}.
$$

One can show that for a maximum-length LFSR the above equations are linearly independent (modulo 2), and so uniquely determine the feedback coefficients. The coefficients can thus be found efficiently using linear algebra. (If the LFSR is not maximum length, then variants of this attack still apply.) With the feedback coefficients and the initial state known, all subsequent output bits of the LFSR can again be easily determined.

可以证明，对于最大长度的 LFSR，上述方程是（模 2）线性无关的，因此唯一确定反馈系数。于是可以用线性代数高效地求出这些系数。（如果 LFSR 不是最大长度的，该攻击的变体仍然适用。）已知反馈系数和初始状态后，LFSR 的所有后续输出比特同样可以容易地确定。

### 7.1.2 Adding Nonlinearity　7.1.2 引入非线性

The linear relationships between the output bits of an LFSR enable an easy attack. To thwart such attacks, we must introduce some nonlinearity, i.e., using ANDs/ORs of secret values and not just their XOR. There are several different approaches to doing so, and we only explore some of them here. All the ideas we discuss can also be combined with each other in different ways.

LFSR 输出比特之间的线性关系使得攻击变得容易。为了阻止此类攻击，我们必须引入一些非线性，即使用秘密值的与/或（AND/OR）运算而不仅仅是异或（XOR）。有多种不同的方法可以做到这一点，我们这里只探讨其中一部分。我们讨论的所有思想也可以以不同方式相互组合。

Nonlinear feedback. One obvious way to introduce nonlinearity is to make the feedback loop nonlinear; we refer to the result simply as a feedback shift register (FSR). An FSR will again consist of an array of registers, each containing a single bit. As before, the state of the FSR is updated in each of a series of clock ticks by shifting the values in all the registers to the right; now, however, the new value of the left-most register will be a nonlinear function of the current registers. In other words, if the state at some time $t$ is $s_{n-1}^{(t)}, \ldots, s_0^{(t)}$, then the state after the next clock tick is $s_{n-1}^{(t+1)}, \ldots, s_0^{(t+1)}$ with

非线性反馈。引入非线性的一种显而易见的方法是使反馈回路非线性；我们将结果简称为反馈移位寄存器（feedback shift register，FSR）。FSR 同样由寄存器阵列组成，每个寄存器包含一个比特。与之前一样，FSR 在每个时钟节拍都把所有寄存器中的值右移来更新状态；但现在，最左边寄存器的新值将是当前寄存器的非线性函数。换句话说，如果某时刻 $t$ 的状态为 $s_{n-1}^{(t)}, \ldots, s_0^{(t)}$，则下一个时钟节拍后的状态为 $s_{n-1}^{(t+1)}, \ldots, s_0^{(t+1)}$，其中

$$
\begin{aligned}&s_{i}^{(t+1)}:=s_{i+1}^{(t)},\quad i=0,\ldots,n-2\\&s_{n-1}^{(t+1)}:=g(s_{n-1}^{(t)},\ldots,s_{0}^{(t)})\end{aligned}
$$

for some arbitrary (nonlinear) function $g$. As before, the FSR outputs the value of the right-most register $s_0$ at each clock tick. For security, $g$ should be balanced in the sense that $\Pr[g(s_{n-1}, \ldots, s_0) = 1] \approx 1/2$, where the probability is over uniform choice of $s_{n-1}, \ldots, s_0$.

其中 $g$ 是某个任意（非线性）函数。与之前一样，FSR 在每个时钟节拍输出最右边寄存器 $s_0$ 的值。为了安全性，$g$ 应当是平衡的，即 $\Pr[g(s_{n-1}, \ldots, s_0) = 1] \approx 1/2$，其中概率取遍 $s_{n-1}, \ldots, s_0$ 的均匀选择。

Nonlinear output. Another approach is to introduce nonlinearity in the output sequence. In the most basic case, we could have an LFSR as before (where the new value of the left-most register is again computed as a linear function of the current registers), but where the output at each clock tick is a nonlinear function $g$ (called the filter) of the current registers, rather than just the right-most register. This construction is sometimes called a filter generator. As before, $g$ should be balanced so that the output stream will not have any obvious bias.

非线性输出。另一种方法是在输出序列中引入非线性。在最基本的情形中，我们可以使用与之前相同的 LFSR（其中最左边寄存器的新值仍然是当前寄存器的线性函数），但每个时钟节拍的输出是当前寄存器的非线性函数 $g$（称为滤波器），而不仅仅是最右边寄存器的值。这种构造有时称为滤波生成器（filter generator）。与之前一样，$g$ 应当是平衡的，以使输出流不具有任何明显的偏差。

Combination generators. Yet another possibility is to use more than one LFSR, and to generate the final output stream by combining the outputs of the individual LFSRs in some nonlinear way. This gives what is known as a (nonlinear) combination generator. The individual LFSRs need not have the same degree, and in fact the cycle length of the combination generator will be maximized if they do not have the same degree.

组合生成器。另一种可能是使用多个 LFSR，通过某种非线性方式组合各个 LFSR 的输出来生成最终输出流。这种构造称为（非线性）组合生成器（combination generator）。各个 LFSR 的次数不必相同；事实上，如果它们的次数不同，组合生成器的周期长度将达到最大。

The way in which the output streams of the underlying LFSRs are combined must be done so as to ensure the final output is unbiased; simply computing the AND of the underlying output streams, for example, would result in output bits that are biased toward 0. Care must also be taken to ensure that the final output of the combination generator is not too highly correlated with any of the output streams of the underlying LFSRs, as high correlation can lead to attacks. For example, consider combining three LFSRs $A$, $B$, and $C$ generating output streams $a_0, a_1, \ldots, b_0, b_1, \ldots$, and $c_0, c_1, \ldots$, respectively, by setting the $i$th output bit of the combination generator equal to $y_i := (a_i \land b_i) \oplus c_i$ (where $\land$ denotes binary AND). If the degrees of the individual LFSRs are $n_a, n_b$, and $n_c$, then the overall state has length $n_a + n_b + n_c$ and we might hope that the best attack distinguishing the output of the combination generator from uniform requires time ${2}^{n_a + n_b + n_c}$. But observe that if we treat each bit of each of the underlying output streams as uniform, then $a_i \land b_i$ is equal to 0 with probability ${3}/{4}$, and so $\Pr[c_i = y_i] = 3/4$. Thus, given a long output stream $y_0, y_1, \ldots$ of the combination generator, an attacker can enumerate all ${2}^{n_c}$ possible values of the initial state for LFSR $C$ and compute the output sequence $c_0, c_1, \ldots$ for each one. The correct initial state for $C$ will result in a sequence that agrees with the observed output stream roughly ${3}/{4}$ of the time; moreover, with high probability, no other candidate state will. The allows the attacker to obtain the initial state of $C$ in time ${2}^{n_c}$. Having done so, it can then recover the initial states of LFSRs $A$ and $B$ in time at most ${2}^{n_a + n_b}$. (See Exercise 7.4 for a better attack.)

底层 LFSR 输出流的组合方式必须确保最终输出是无偏的；例如，简单地对底层输出流计算 AND 将导致输出比特偏向 0。还必须注意，组合生成器的最终输出与任何底层 LFSR 的输出流之间的相关性不能过高，因为高相关性可能导致攻击。例如，考虑把三个 LFSR $A$、$B$ 和 $C$ 组合起来：它们分别生成输出流 $a_0, a_1, \ldots$、$b_0, b_1, \ldots$ 和 $c_0, c_1, \ldots$，并把组合生成器的第 $i$ 个输出比特设为 $y_i := (a_i \land b_i) \oplus c_i$（其中 $\land$ 表示二进制 AND）。如果各个 LFSR 的次数分别为 $n_a, n_b$ 和 $n_c$，则总状态长度为 $n_a + n_b + n_c$，我们或许希望，区分组合生成器输出与均匀串的最佳攻击需要 ${2}^{n_a + n_b + n_c}$ 的时间。但注意，如果我们把每个底层输出流的每个比特都视为均匀分布的，那么 $a_i \land b_i$ 等于 0 的概率为 ${3}/{4}$，因此 $\Pr[c_i = y_i] = 3/4$。于是，给定组合生成器的一个长输出流 $y_0, y_1, \ldots$，攻击者可以枚举 LFSR $C$ 的初始状态的所有 ${2}^{n_c}$ 个可能值，并为每一个计算输出序列 $c_0, c_1, \ldots$。$C$ 的正确初始状态产生的序列与观察到的输出流约有 ${3}/{4}$ 的时间一致；此外，其他候选状态以很高的概率做不到这一点。这使得攻击者能够在 ${2}^{n_c}$ 时间内获得 $C$ 的初始状态。在此基础上，攻击者可以在至多 ${2}^{n_a + n_b}$ 时间内恢复 LFSR $A$ 和 $B$ 的初始状态。（更好的攻击见习题 7.4。）

### 7.1.3 Trivium　7.1.3 Trivium

To illustrate the ideas from the previous section, we briefly describe the stream cipher Trivium. This stream cipher was selected as part of the portfolio of the eSTREAM project, a European effort completed in 2008 whose goal was to develop new stream ciphers. Trivium was designed to have a simple
description and a compact hardware implementation.

为了说明上一节的思想，我们简要描述 Trivium 流密码。该流密码入选了 eSTREAM 项目的算法组合，eSTREAM 是一个于 2008 年完成的欧洲项目，目标是开发新的流密码。Trivium 的设计目标是描述简单、硬件实现紧凑。

![Image](https://lsky.jerryxue.top/i/2026/08/19/6a85c53da1f2b.jpg)

**FIGURE 7.2: A schematic illustration of Trivium with (from top to bottom) three coupled, nonlinear FSRs A, B, and C.**

**图 7.2：Trivium 的示意图，从上到下为三个耦合的非线性 FSR A、B 和 C。**

Trivium uses three coupled, nonlinear FSRs denoted by A, B, and C and having degrees 93, 84, and 111, respectively. (See Figure 7.2.) The state of Trivium is simply the 288 bits comprising the values in all the registers of these FSRs. At each clock tick, the output of each FSR is the XOR of its right-most register and one additional register; the output of Trivium is the XOR of the output bits of the three FSRs. The FSRs are coupled: at each clock tick, the new value of the left-most register of each FSR is computed as a function of one of the registers in the same FSR and a subset of the registers from a second FSR. The feedback function in each case is nonlinear.

Trivium 使用三个耦合的非线性 FSR，分别记为 A、B 和 C，次数分别为 93、84 和 111。（见图 7.2。）Trivium 的状态就是这些 FSR 所有寄存器中的值构成的 288 个比特。在每个时钟节拍，每个 FSR 的输出是其最右边寄存器与一个额外寄存器的异或；Trivium 的输出是三个 FSR 输出比特的异或。这些 FSR 是耦合的：在每个时钟节拍，每个 FSR 最左边寄存器的新值是同一 FSR 中一个寄存器与第二个 FSR 中一部分寄存器的函数。每种情况下的反馈函数都是非线性的。

The *Init algorithm* of Trivium accepts an 80-bit key and an 80-bit IV. The key is loaded into the 80 left-most registers of A, and the IV is loaded into the 80 left-most registers of B. The remaining registers are set to 0, except for the three right-most registers of C, which are set to 1. The FSRs are then run for 4·288 clock ticks (with the output discarded), and the resulting state is taken as the initial state.

Trivium 的 Init 算法接受 80 比特密钥和 80 比特 IV。密钥被加载到 A 的 80 个最左边寄存器中，IV 被加载到 B 的 80 个最左边寄存器中。其余寄存器设为 0，但 C 的三个最右边寄存器设为 1。然后 FSR 运行 4·288 个时钟节拍（输出被丢弃），所得状态作为初始状态。

To date, no cryptanalytic attacks better than exhaustive search are known against Trivium.

迄今为止，尚未发现比穷举搜索更好的针对 Trivium 的密码分析攻击。

### 7.1.4 RC4　7.1.4 RC4

LFSRs are efficient when implemented in hardware, but have poor performance in software. For this reason, alternate designs of stream ciphers have been explored. A prominent example is RC4, which was designed by Ron Rivest in 1987. RC4 is remarkable for its speed and simplicity, and resisted serious attack for several years. While RC4 is still occasionally used, recent attacks have shown serious cryptographic weaknesses in RC4 and it is no longer recommended for cryptographic applications.

LFSR 在硬件实现中很高效，但在软件中性能较差。出于这个原因，人们探索了流密码的其他设计。一个突出的例子是 RC4，由 Ron Rivest 于 1987 年设计。RC4 以其速度和简洁性著称，并在数年间抵御了严重的攻击。虽然 RC4 仍偶尔被使用，但最近的攻击揭示了 RC4 中严重的密码学弱点，它不再被推荐用于密码学应用。

> **ALGORITHM 7.1**　**算法 7.1**
>
> Init algorithm for RC4
>
> Input: 16-byte key k
> Output: Initial state $(S, i, j)$
> (Note: All addition is modulo 256)
>
> for $i = 0$ to 255:
>    $S[i] := i$
>    $k[i] := k[i \mod 16]$
>
> $j := 0$
>
> for $i = 0$ to 255:
>    $j := j + S[i] + k[i]$
>     Swap $S[i]$ and $S[j]$
>
> $i := 0, j := 0$
>
> return initial state $(S, i, j)$
>
> RC4 的 Init 算法
>
> 输入：16 字节密钥 $k$
> 输出：初始状态 $(S, i, j)$
> （注：所有加法模 256）
>
> 对 $i = 0$ 到 255：
>    $S[i] := i$
>    $k[i] := k[i \mod 16]$
>
> $j := 0$
>
> 对 $i = 0$ 到 255：
>    $j := j + S[i] + k[i]$
>     交换 $S[i]$ 和 $S[j]$
>
> $i := 0, j := 0$
>
> 返回初始状态 $(S, i, j)$

> **ALGORITHM 7.2**　**算法 7.2**
>
> Next algorithm for RC4
>
> Input: Current state $(S,i,j)$
> Output: Output byte $y$; updated state $(S,i,j)$
> (Note: All addition is modulo 256)
>
> $i:=i+1$
> $j:=j+S[i]$
> Swap $S[i]$ and $S[j]$
> $t:=S[i]+S[j]$
> $y:=S[t]$
> return $y$ and $(S,i,j)$
>
> RC4 的 Next 算法
>
> 输入：当前状态 $(S,i,j)$
> 输出：输出字节 $y$；更新后的状态 $(S,i,j)$
> （注：所有加法模 256）
>
> $i:=i+1$
> $j:=j+S[i]$
> 交换 $S[i]$ 和 $S[j]$
> $t:=S[i]+S[j]$
> $y:=S[t]$
> 返回 $y$ 和 $(S,i,j)$

The state of RC4 consists of a 256-byte array $S$, which always contains a permutation of the elements ${0}, \ldots,255$, along with two values $i, j \in \{0, \ldots,255\}$. For simplicity we assume a 16-byte (128-bit) key $k$, although the algorithm can handle keys 1–256 bytes long. We index the bytes of $S$ as $S[0], \ldots,S[255]$, and the bytes of the key as $k[0], \ldots,k[15]$.

RC4 的状态由一个 256 字节数组 $S$（始终包含 ${0}, \ldots,255$ 的一个排列）和两个值 $i, j \in \{0, \ldots,255\}$ 组成。为简单起见，我们假设使用 16 字节（128 比特）的密钥 $k$，尽管该算法可以处理 1–256 字节长的密钥。我们把 $S$ 的字节记作 $S[0], \ldots,S[255]$，把密钥的字节记作 $k[0], \ldots,k[15]$。

The $\mathsf{Init}$ algorithm for RC4 is presented as Algorithm 7.1. During initialization, S is first set to the identity permutation (i.e., with $S[i] = i$ for all i) and k is expanded to 256 bytes by repeating it as many times as needed. Then each entry of S is swapped at least once with another entry of S at some "pseudorandom" location. The indices i, j are set to 0, and $(S, i, j)$ is output as the initial state.

RC4 的 Init 算法如算法 7.1 所示。在初始化期间，$S$ 首先被设为恒等排列（即对所有 $i$ 有 $S[i] = i$），$k$ 则按需重复，扩展为 256 字节。然后 $S$ 的每个条目至少与 $S$ 中某个“伪随机”位置的条目交换一次。索引 $i$、$j$ 被设为 0，$(S, i, j)$ 作为初始状态输出。

The initial state is used to generate a sequence of output bytes using the Next algorithm in Algorithm 7.2. Each time Next is called, the index i is simply incremented (modulo 256), and j is changed in some "pseudorandom" way. Entries $S[i]$ and $S[j]$ are swapped, and the value of S at position $S[i] + S[j]$ (again computed modulo 256) is output. Note that each entry of S is swapped with an entry of S (possibly itself) at least once every 256 iterations, ensuring good "mixing" of the permutation S.

初始状态用于使用算法 7.2 中的 Next 算法生成一系列输出字节。每次调用 Next 时，索引 $i$ 只是递增（模 256），$j$ 以某种“伪随机”方式改变。$S[i]$ 和 $S[j]$ 被交换，$S$ 在位置 $S[i] + S[j]$（同样模 256 计算）处的值被输出。注意，$S$ 的每个条目至少每 256 次迭代就会与 S 的某个条目（可能是自身）交换一次，这保证了排列 S 的良好“混合”。

RC4 was not designed to take an $IV$ as input; however, in practice an $IV$ is often incorporated by simply concatenating it with the actual key $k^{\prime}$ before initialization. That is, a random $IV$ of the desired length is chosen, $k$ is set equal to the concatenation of $IV$ and $k^{\prime}$ (this can be done by either prepending or appending $IV$), and then $\mathsf{Init}$ is run as in Algorithm 7.1 to generate an initial state. Output bits are then produced using Algorithm 7.2 exactly as before. Assuming RC4 is being used in unsynchronized mode (see Section 3.6.2), the IV would then be sent in the clear to the receiver—who knows the actual key $k^{\prime}$—thus enabling the sender and receiver to generate the same initial state and hence the same output stream. This method of incorporating an IV was used in the Wired Equivalent Privacy (WEP) encryption standard for protecting communications in 802.11 wireless networks.

RC4 设计时并未将 $IV$ 作为输入；然而在实践中，通常的做法是在初始化之前把 $IV$ 简单地与实际密钥 $k^{\prime}$ 拼接。即，选择所需长度的随机 $IV$，将 $k$ 设为 $IV$ 与 $k^{\prime}$ 的拼接（$IV$ 既可前置也可后置），然后如算法 7.1 那样运行 $\mathsf{Init}$ 生成初始状态。之后像之前一样用算法 7.2 产生输出比特。假设 RC4 以非同步模式使用（参见 3.6.2 节），IV 将以明文发送给知道实际密钥 $k^{\prime}$ 的接收方，从而使发送方和接收方生成相同的初始状态，进而生成相同的输出流。这种纳入 IV 的方法曾被用于有线等效保密（Wired Equivalent Privacy，WEP）加密标准，以保护 802.11 无线网络中的通信。

One should be concerned by this unprincipled way of modifying RC4 to accept an IV. Even if RC4 were secure when used without an IV as originally intended, there is no reason to believe that it should be secure when modified to use an IV as just described. Indeed, contrary to the key, the IV is revealed to an attacker (since it is sent in the clear); furthermore, using different IVs with the same fixed key $k^{\prime}$—as would be done when using RC4 in unsynchronized mode—means that related values k are being used to initialize the state of RC4. As we will see below, both of these issues lead to attacks when RC4 is used in this fashion.

人们应当对修改 RC4 以接受 IV 的这种缺乏原则的做法感到担忧。即使 RC4 在按原始设计不带 IV 使用时是安全的，也没有理由相信在按上述方式修改为使用 IV 时它仍然安全。事实上，与密钥不同，IV 对攻击者是公开的（因为它以明文发送）；此外，在非同步模式下使用 RC4 时，不同的 IV 会与同一个固定密钥 $k^{\prime}$ 一起使用，这意味着相互关联的 $k$ 值被用于初始化 RC4 的状态。正如下面我们将看到的，当 RC4 以这种方式使用时，这两个问题都会导致攻击。

Attacks on RC4. Various attacks on RC4 have been known for several years. Due to this, RC4 should no longer be used; instead, a more modern stream cipher or block cipher should be used in its place. We describe some basic attacks here to give a flavor for the techniques involved.

针对 RC4 的攻击。针对 RC4 的各种攻击已为人所知多年。因此，RC4 不应再被使用；取而代之的应是一种更现代的流密码或分组密码。我们在此描述一些基本攻击，以展示所涉及技术的特点。

We begin by demonstrating a simple statistical attack on RC4 that does not rely on the honest parties' using an IV. Specifically, we show that the second output byte of RC4 is (slightly) biased toward 0. Let $S_t$ denote the array $S$ of the RC4 state after $t$ iterations of $\text{Next}$, with $S_0$ denoting the initial array. Treating $S_0$ (heuristically) as a uniform permutation of $\{0, \ldots, 255\}$, with probability ${1}/256 \cdot (1 - 1/255) \approx 1/256$ it holds that $S_0[2] = 0$ and $X \overset{\mathrm{def}}{=} S_0[1] \neq 2$. Assume for a moment that this is the case. Then in the first iteration of $\text{Next}$, the value of $i$ is incremented to 1, and $j$ is set equal to $S_0[i] = S_0[1] = X$. Then entries $S_0[1]$ and $S_0[X]$ are swapped, so that at the end of the iteration we have $S_1[X] = S_0[1] = X$. In the second iteration, $i$ is incremented to 2 and $j$ is assigned the value

我们首先展示一种不依赖于诚实方使用 IV 的简单统计攻击。具体来说，我们证明 RC4 的第二个输出字节（略微）偏向 0。令 $S_t$ 表示 Next 的 $t$ 次迭代后 RC4 状态中的数组 $S$，其中 $S_0$ 表示初始数组。若（启发式地）将 $S_0$ 视为 $\{0, \ldots, 255\}$ 的均匀排列，则以 ${1}/256 \cdot (1 - 1/255) \approx 1/256$ 的概率有 $S_0[2] = 0$ 且 $X \overset{\mathrm{def}}{=} S_0[1] \neq 2$。暂且假设情况如此。则在 Next 的第一次迭代中，$i$ 的值递增为 1，$j$ 被设为 $S_0[i] = S_0[1] = X$。然后 $S_0[1]$ 和 $S_0[X]$ 被交换，从而在该迭代结束时 $S_1[X] = S_0[1] = X$。在第二次迭代中，$i$ 递增为 2，$j$ 被赋值为

$$
j+S_{1}[i]=X+S_{1}[2]=X+S_{0}[2]=X,
$$

since $S_{0}[2]=0$. Then entries $S_{1}[2]$ and $S_{1}[X]$ are swapped, so that $S_{2}[X]=S_{1}[2]=S_{0}[2]=0$ and $S_{2}[2]=S_{1}[X]=X$. Finally, the value of $S_{2}$ at position $S_{2}[i]+S_{2}[j]=S_{2}[2]+S_{2}[X]=X$ is output; this is exactly the value $S_{2}[X]=0$.

因为 $S_{0}[2]=0$。然后 $S_{1}[2]$ 和 $S_{1}[X]$ 被交换，使得 $S_{2}[X]=S_{1}[2]=S_{0}[2]=0$ 且 $S_{2}[2]=S_{1}[X]=X$。最后，$S_{2}$ 在位置 $S_{2}[i]+S_{2}[j]=S_{2}[2]+S_{2}[X]=X$ 处的值被输出；这恰好是值 $S_{2}[X]=0$。

When $S_{0}[2] \neq 0$ the second output byte is uniformly distributed. Overall, then, the probability that the second output byte is 0 is roughly

当 $S_{0}[2] \neq 0$ 时，第二个输出字节均匀分布。因此总体上，第二个输出字节为 0 的概率大约为

$$
\begin{aligned}\Pr[S_{0}[2]=0 \text{ and } S_{0}[1]\neq2]+\frac{1}{256}\cdot\Pr[S_{0}[2]\neq0]&=\frac{1}{256}+\frac{1}{256}\cdot\left(1-\frac{1}{256}\right)\\&\approx\frac{2}{256},\end{aligned}
$$

or roughly twice what would be expected for a uniform value.

即大约是均匀取值时预期概率的两倍。

By itself the above might not be viewed as a particularly serious attack, although it does indicate underlying structural problems with RC4. Moreover, statistical biases like the above have been found in other output bytes of RC4, and it has been shown that these biases are sufficiently large to allow for the recovery of plaintext when RC4 is used for encryption.

上述攻击本身可能不被视为特别严重的攻击，但它确实表明 RC4 存在底层的结构性问题。此外，在 RC4 的其他输出字节中也发现了类似的统计偏差，并且已经证明这些偏差大到足以在 RC4 用于加密时恢复明文。

A more devastating attack against RC4 is possible when an IV is incorporated by prepending it to the key. This attack can be used to recover the key, regardless of its length, and is thus more serious than a distinguishing attack such as the one described above. Importantly, this attack can be used to completely break the WEP encryption standard mentioned earlier, and was influential in getting the standard replaced.

当 IV 被前置到密钥上时，可以对 RC4 实施更具破坏性的攻击。这种攻击可用于恢复密钥（无论其长度如何），因此比上面描述的区分攻击更为严重。重要的是，这种攻击可用于完全破解前面提到的 WEP 加密标准，并对推动该标准被替换发挥了重要作用。

The core of the attack is a way to extend knowledge of the first $n$ bytes of $k$ to knowledge of the first $n+1$ bytes of $k$. Note that when an $IV$ is prepended to the actual key $k^{\prime}$ (so $k = IV\|k^{\prime}$), the first few bytes of $k$ are given to the attacker for free! If the $IV$ is $n$ bytes long, then an adversary can use this attack to first recover the $(n+1)$st byte of $k$ (which is the first byte of the real key $k^{\prime}$), then the next byte of $k$, and so on, until it learns the entire key.

攻击的核心是一种把对 $k$ 前 $n$ 个字节的了解扩展到前 $n+1$ 个字节的方法。注意，当 $IV$ 前置于实际密钥 $k^{\prime}$（因此 $k = IV\|k^{\prime}$）时，$k$ 的前几个字节对攻击者来说唾手可得！如果 $IV$ 长 $n$ 字节，则敌手可以使用这种攻击首先恢复 $k$ 的第 $(n+1)$ 个字节（即真实密钥 $k^{\prime}$ 的第一个字节），然后是 $k$ 的下一个字节，依此类推，直到恢复出整个密钥。

Assume the IV is 3 bytes long, as is the case for WEP. The attacker waits until the first two bytes of the IV have a specific form. The attack can be carried out with several possibilities for the first two bytes of the IV, but we look at the case where the IV takes the form $IV = (3,255,X)$ for X an arbitrary byte. This means, of course, that $k[0] = 3,k[1] = 255$, and $k[2] = X$ in Algorithm 7.1. One can check that after the first four iterations of the second loop of $\mathsf{Init}$, we have

假设 IV 长 3 字节，WEP 即是如此。攻击者等待 IV 的前两个字节取特定形式。该攻击对 IV 前两个字节的多种取值都适用，但我们考察 IV 形如 $IV = (3,255,X)$（$X$ 为任意字节）的情况。这当然意味着在算法 7.1 中 $k[0] = 3$、$k[1] = 255$、$k[2] = X$。可以验证，在 Init 第二个循环的前四次迭代后，我们有

$$
S[0]=3,\quad S[1]=0,\quad S[3]=X+6+k[3].
$$

In the next 252 iterations of the *Init* algorithm, i is always greater than 3. So the values of $S[0], S[1]$, and $S[3]$ are not subsequently modified as long as j never takes on the values 0, 1, or 3. If we (heuristically) treat j as taking on a uniform value in each iteration, this means that $S[0], S[1]$, and $S[3]$ are not subsequently modified with probability $(253/256)^{252} \approx 0.05$, or 5% of the time. Assuming this is the case, the first byte output by *Next* will be $S[3] = X + 6 + k[3]$; since X is known, this reveals $k[3]$.

在 Init 算法接下来的 252 次迭代中，$i$ 始终大于 3。因此只要 $j$ 从不取值 0、1或 3，$S[0]$、$S[1]$ 和 $S[3]$ 的值就不会被后续修改。如果我们（启发式地）将 $j$ 视为在每次迭代中取均匀值，这意味着 $S[0]$、$S[1]$ 和 $S[3]$ 不被后续修改的概率为 $(253/256)^{252} \approx 0.05$，即 5% 的时间。假设情况如此，Next 输出的第一个字节将是 $S[3] = X + 6 + k[3]$；由于 X 是已知的，这揭示了 $k[3]$。

So, the attacker knows that 5% of the time the first byte of the output is related to $k[3]$ as described above. (This is much better than random guessing, which is correct ${1}/256 = 0.4\%$ of the time.) By collecting sufficiently many samples of the first byte of the output—for several IVs of the correct form—the attacker obtains a high-confidence estimate for $k[3]$.

因此，攻击者知道，有 5% 的时间输出首字节与 $k[3]$ 之间存在上述关系。（这比随机猜测好得多，后者的正确率为 ${1}/256 = 0.4\%$。）通过收集足够多的输出首字节样本（使用多个形式正确的 IV），攻击者可以对 $k[3]$ 做出高置信度的估计。

### 7.1.5 ChaCha20　7.1.5 ChaCha20

ChaCha20, introduced in 2008, is a stream cipher intended to be extremely efficient in software. It is available as a replacement for RC4 in many systems and—as described in Section 5.3.2—is combined with the Poly1305 message authentication code to construct an authenticated encryption scheme widely used in the TLS protocol. We give a high-level description of ChaCha20 that gives the main ideas of the scheme, but refer elsewhere for the low-level details.

ChaCha20 于 2008 年提出，是一种力求在软件中实现极高效率的流密码。它在许多系统中可作为 RC4 的替代品，并且——如 5.3.2 节所述——与 Poly1305 消息认证码结合，构造了一种在 TLS 协议中广泛使用的认证加密方案。我们给出 ChaCha20 的高层描述，展示该方案的主要思想，底层细节请参阅其他资料。

The core of ChaCha20 is a fixed permutation $P$ that operates on 512-bit strings. This permutation is carefully constructed to be both highly efficient and "cryptographically strong." To improve efficiency, it was designed to rely primarily on only three assembly-level instructions operating on 32-bit words: Addition (modulo ${2}^{32}$), bitwise (cyclic) Rotation, and XOR; $P$ is thus an example of what is called an ARX-based design. From a cryptographic point of view, $P$ is intended to be a suitable instantiation of a "random permutation," and constructions based on $P$ can be analyzed in the so-called random-permutation model. By analogy with the random-oracle model (see Section 6.5), the random-permutation model assumes that all parties are given access to oracles for a uniform permutation $P$ as well as its inverse $P^{-1}$. In this model, as in the random-oracle model, the only way to compute $P$ (or $P^{-1}$) is to explicitly query those oracles. (We refer to Section 7.3.3 for an example of a proof of security in the random-permutation model.)

ChaCha20 的核心是一个对 512 比特串进行操作的固定置换 $P$。该置换经过精心构造，既高效又“密码学上强”。为了提高效率，它被设计为主要依赖三种对 32 比特字进行操作的汇编级指令：加法（模 ${2}^{32}$）、按位（循环）移位和异或；因此 $P$ 是所谓的基于 ARX 的设计的一个例子。从密码学角度看，$P$ 旨在成为“随机置换”的合适实例化，基于 $P$ 的构造可以在所谓的随机置换模型中进行分析。类似于随机预言机模型（参见 6.5 节），随机置换模型假设所有参与方都能访问均匀置换 $P$ 及其逆 $P^{-1}$ 的预言机。在这个模型中，与随机预言机模型一样，计算 $P$（或 $P^{-1}$）的唯一方式是显式查询这些预言机。（随机置换模型中安全性证明的例子参见 7.3.3 节。）

In ChaCha20, the permutation P is used to construct a pseudorandom function F taking a 256-bit key and mapping 128-bit inputs to 512-bit outputs. This keyed function F is defined as

在 ChaCha20 中，置换 $P$ 用于构造一个伪随机函数 $F$，它接受 256 比特密钥，将 128 比特输入映射为 512 比特输出。这个带密钥的函数 $F$ 定义为

$$
F_{k}(x)\stackrel{\mathrm{def}}{=}P(\mathsf{const}\|k\|x)\boxplus\mathsf{const}\|k\|x,
$$

where const is a 128-bit constant. (Above, '$\boxplus$' denotes word-wise modular addition.) F can be shown to be a pseudorandom function if P is modeled as a random permutation.

其中 const 是 128 比特常数。（上式中，‘$\boxplus$’ 表示按字的模加法。）如果 P 被建模为随机置换，则可以证明 F 是伪随机函数。

The ChaCha20 stream cipher itself is then constructed from $F$ as in Construction 3.30. Specifically, given a 256-bit seed $s$ and an initialization vector $IV \in \{0,1\}^{64}$, the output of the stream cipher is $F_s(IV\|\langle0\rangle)$, $F_s(IV\|\langle1\rangle)$, ..., where the counter values $\langle0\rangle$, $\langle1\rangle$, etc., are encoded as 64-bit integers.

ChaCha20 流密码本身则按构造 3.30 的方式由 $F$ 构造而成。具体来说，给定 256 比特种子 $s$ 和初始化向量 $IV \in \{0,1\}^{64}$，流密码的输出为 $F_s(IV\|\langle0\rangle)$、$F_s(IV\|\langle1\rangle)$、⋯⋯，其中计数器值 $\langle0\rangle$、$\langle1\rangle$ 等被编码为 64 比特整数。
