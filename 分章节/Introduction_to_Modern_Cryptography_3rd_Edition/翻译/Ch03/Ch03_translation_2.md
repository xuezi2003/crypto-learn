## 3.3 Constructing an EAV-Secure Encryption Scheme　3.3 构造 EAV 安全的加密方案

Having defined what it means for an encryption scheme to be secure, the reader may expect us to turn immediately to constructions of secure encryption schemes. Before doing so, however, we need to introduce the notion of pseudorandom generators (PRGs), which are important building blocks for private-key encryption. This, in turn, will lead to a discussion of pseudorandomness, which plays a fundamental role in cryptography in general and private-key encryption in particular.

在定义了加密方案的安全性含义之后，读者可能期望我们立即转向安全加密方案的构造。然而，在此之前，我们需要介绍伪随机生成器（PRG）的概念，它是私钥加密的重要基本构件。这将进而引发对伪随机性的讨论，而伪随机性在密码学中普遍发挥着基础性作用，在私钥加密中尤其如此。

### 3.3.1 Pseudorandom Generators　3.3.1 伪随机生成器

A pseudorandom generator G is an efficient, deterministic algorithm for transforming a short, uniform string (called a seed) into a longer, "uniform-looking" (or "pseudorandom") output string. Stated differently, a pseudorandom generator uses a small amount of true randomness in order to generate a large amount of pseudorandomness. This is useful whenever a large number of random(-looking) bits are needed, since generating true random bits is often difficult and slow. (See the discussion at the beginning of Chapter 2.) Pseudorandom generators have been studied since at least the 1940s when they were used for running statistical simulations. In that context, researchers proposed various statistical tests that a pseudorandom generator should pass in order to be considered "good." As a simple example, one could require that the first bit of the output of a pseudorandom generator should be equal to 1 with probability very close to 1/2 (where the probability is taken over uniform choice of the seed), since the first bit of a uniform string is equal to 1 with probability exactly 1/2. As another example, the parity of any fixed subset of the output bits should also be 1 with probability very close to 1/2. More complex statistical tests can also be considered.

伪随机生成器 G 是一种高效的确定性算法，它将一个短的均匀串（称为种子）转换成一个更长的、“看起来均匀”（或“伪随机”）的输出串。换句话说，伪随机生成器使用少量的真随机性来生成大量的伪随机性。每当需要大量随机（或看起来随机的）比特时，这都非常有用，因为生成真随机比特通常困难且缓慢。（参见第 2 章开头的讨论。）伪随机生成器至少从 20 世纪 40 年代起就得到了研究，当时它们被用于运行统计模拟。在那个背景下，研究者提出了各种统计检验，一个伪随机生成器必须通过这些检验才能被认为是“好的”。作为一个简单例子，可以要求伪随机生成器输出的第一比特等于 1 的概率非常接近 1/2（其中概率是在种子的均匀选择上计算的），因为均匀串的第一比特等于 1 的概率恰好是 1/2。另一个例子是，输出比特中任意固定子集的奇偶性也应以非常接近 1/2 的概率为 1。还可以考虑更复杂的统计检验。

This historical approach to determining the quality of some candidate pseudorandom generator is unsatisfying, as it is not clear when passing some set of statistical tests is sufficient to guarantee the soundness of using a candidate pseudorandom generator for some application. (In particular, there may be another statistical test that does successfully distinguish the output of the generator from true random bits.) The historical approach is even more problematic when using pseudorandom generators for cryptographic applications; there, security may be compromised if any attacker is able to distinguish the output of a pseudorandom generator from uniform, and we do not know in advance what strategy an attacker might use.

这种判断候选伪随机生成器质量的历史方法并不令人满意，因为我们不清楚通过一组统计检验何时足以保证将候选伪随机生成器用于某个应用是可靠的。（特别地，可能存在另一个统计检验，它确实能够成功区分生成器的输出与真随机比特。）当将伪随机生成器用于密码学应用时，历史方法甚至更成问题；在那里，如果任何攻击者能够区分伪随机生成器的输出与均匀串，安全性就可能受到损害，而我们无法预先知道攻击者可能使用什么策略。

The above considerations motivated a cryptographic approach to defining pseudorandom generators in the 1980s. The basic realization was that a good pseudorandom generator should pass all (efficient) statistical tests. That is, for any efficient statistical test (or distinguisher) $D$, the probability that $D$ returns 1 when given the output of the pseudorandom generator should be close to the probability that $D$ returns 1 when given a uniform string of the same length. Informally, then, this means the output of a pseudorandom generator "looks like" a uniformly generated string to any efficient observer.

上述考虑推动了 20 世纪 80 年代定义伪随机生成器的密码学方法。其基本认识是，一个好的伪随机生成器应该能够通过所有（高效）统计检验。也就是说，对于任何高效的统计检验（或区分器）$D$，当给定伪随机生成器的输出时 $D$ 返回 1 的概率，应接近于当给定相同长度的均匀串时 $D$ 返回 1 的概率。因此，非正式地说，这意味着伪随机生成器的输出对于任何高效的观察者来说“看起来像是”均匀生成的串。

We begin by defining what it means for a distribution to be pseudorandom. Let Dist be a distribution on $\ell$-bit strings. (This means that Dist assigns some probability to every string in $\{0,1\}^{\ell}$; sampling from Dist means that we choose an $\ell$-bit string according to this probability distribution.) Informally, Dist is pseudorandom if the experiment in which a string is sampled from Dist is indistinguishable from the experiment in which a uniform string of length $\ell$ is sampled. (Strictly speaking, since we are in an asymptotic setting we need to speak of the pseudorandomness of a sequence of distributions $\mathsf{Dist} = \{\mathsf{Dist}_n\}$, where distribution $\mathsf{Dist}_n$ is used for security parameter $n$. We ignore this point in our current discussion.) More precisely, it should be infeasible for any polynomial-time algorithm to determine (better than guessing) whether it is given a string sampled according to Dist, or whether it is given a uniform $\ell$-bit string. This means that a pseudorandom string is just as good as a uniform string, as long as we consider only polynomial-time observers. We stress that it does not make sense to say that any fixed string is "pseudorandom," in the same way that it is meaningless to refer to any fixed string as "uniform." Rather, pseudorandomness is a property of a distribution on strings. (Nevertheless, we sometimes informally call a string output by a pseudorandom generator a "pseudorandom string" in the same way we might say that a string sampled according to the uniform distribution is a "uniform string.") Just as indistinguishability is a computational relaxation of perfect secrecy, pseudorandomness is a computational relaxation of true randomness.

我们首先定义一个分布为伪随机意味着什么。令 Dist 是 $\ell$ 比特串上的一个分布。（这意味着 Dist 对 $\{0,1\}^{\ell}$ 中的每个串赋予某个概率；从 Dist 中采样意味着我们根据这个概率分布选择一个 $\ell$ 比特串。）非正式地说，如果从 Dist 中采样一个串的实验与采样一个长度为 $\ell$ 的均匀串的实验不可区分，则 Dist 是伪随机的。（严格来说，由于我们处于渐近设定中，我们需要讨论分布序列 $\mathsf{Dist} = \{\mathsf{Dist}_n\}$ 的伪随机性，其中分布 $\mathsf{Dist}_n$ 用于安全参数 $n$。在当前讨论中我们忽略这一点。）更精确地说，任何多项式时间算法应该无法（以优于猜测的方式）确定它被给定的串是根据 Dist 采样得到的，还是均匀的 $\ell$ 比特串。这意味着，只要我们只考虑多项式时间的观察者，伪随机串就与均匀串一样好。我们强调，说某个固定的串是“伪随机的”是没有意义的，就像说某个固定的串是“均匀的”也是没有意义的。相反，伪随机性是串上分布的一个性质。（尽管如此，我们有时非正式地将伪随机生成器输出的串称为“伪随机串”，就像我们可能说根据均匀分布采样的串是“均匀串”一样。）正如不可区分性是完美保密的一种计算松弛，伪随机性是真随机性的一种计算松弛。

Let $G$ be an efficiently computable function that maps strings of length $n$ to outputs of length $\ell(n) > n$, and define $\mathsf{Dist}_n$ to be the distribution on $\ell(n)$ bit strings obtained by choosing a uniform $s \in \{0,1\}^n$ and outputting $G(s)$. Then $G$ is a pseudorandom generator if and only if the distribution $\mathsf{Dist}_n$ (technically, the sequence of distributions $\{\mathsf{Dist}_n\}$) is pseudorandom.

设 $G$ 是一个高效可计算的函数，它将长度为 $n$ 的串映射到长度为 $\ell(n) > n$ 的输出，并定义 $\mathsf{Dist}_n$ 为通过选择均匀的 $s \in \{0,1\}^n$ 并输出 $G(s)$ 所得到的 $\ell(n)$ 比特串上的分布。那么，$G$ 是一个伪随机生成器当且仅当分布 $\mathsf{Dist}_n$（技术上讲，分布序列 $\{\mathsf{Dist}_n\}$）是伪随机的。

The formal definition. As discussed above, $G$ is a pseudorandom generator if no efficient distinguisher can detect whether it is given a string output by $G$ or a string chosen uniformly at random. As in Definition 3.9, this is formalized by requiring that every efficient algorithm outputs 1 with almost the same probability when given $G(s)$ (for uniform seed $s$) or a uniform string. (For an equivalent definition analogous to Definition 3.8, see Exercise 3.7.) We obtain a definition in the asymptotic setting by letting the security parameter $n$ determine the length of the seed, and insisting that $G$ be computable by an efficient algorithm. As a technicality, we also require that $G$'s output be longer than its input; otherwise, $G$ is not very useful or interesting.

形式化定义。如上所述，如果不存在高效的区分器能够检测出它被给定的是 $G$ 输出的串还是均匀随机选择的串，则 $G$ 是一个伪随机生成器。如同定义 3.9，这通过要求每个高效算法在给定 $G(s)$（对于均匀种子 $s$）或均匀串时以几乎相同的概率输出 1 来形式化。（关于类似于定义 3.8 的等价定义，见习题 3.7。）我们通过让安全参数 $n$ 决定种子的长度，并要求 $G$ 可由高效算法计算，来获得渐近设定下的定义。作为一个技术细节，我们还要求 $G$ 的输出长于其输入；否则 $G$ 就没有太大用处或意义。

DEFINITION 3.14 Let $G$ be a deterministic polynomial-time algorithm such that for any $n$ and any input $s \in \{0,1\}^n$, the result $G(s)$ is a string of length $\ell(n)$. $G$ is a pseudorandom generator if the following conditions hold:

定义 3.14 设 $G$ 是一个确定性的多项式时间算法，使得对于任意 $n$ 和任意输入 $s \in \{0,1\}^n$，结果 $G(s)$ 是一个长度为 $\ell(n)$ 的串。如果以下条件成立，则 $G$ 是一个**伪随机生成器**：

1. (Expansion.) For every n it holds that $\ell(n) > n$.

   （扩展性。）对于每个 $n$，有 $\ell(n) > n$。

2. (Pseudorandomness.) For any PPT algorithm $D$, there is a negligible function $\mathsf{negl}$ such that

   （伪随机性。）对于任意 PPT 算法 $D$，存在一个可忽略函数 $\mathsf{negl}$，使得

   $$
   \left|\Pr[D(G(s))=1]-\Pr[D(r)=1]\right|\leq\mathsf{negl}(n),
   $$

   where the first probability is taken over uniform choice of $s \in \{0,1\}^n$ and the randomness of $D$, and the second probability is taken over uniform choice of $r \in \{0,1\}^{\ell(n)}$ and the randomness of $D$.

   其中第一个概率是在 $s \in \{0,1\}^n$ 的均匀选择和 $D$ 的随机性上计算的，第二个概率是在 $r \in \{0,1\}^{\ell(n)}$ 的均匀选择和 $D$ 的随机性上计算的。

We call $\ell(n)$ the expansion factor of G.

我们称 $\ell(n)$ 为 G 的**扩展因子**。

We give an example of an insecure pseudorandom generator to gain familiarity with the definition.

我们给出一个不安全的伪随机生成器的例子，以熟悉该定义。

**Example 3.15**　**示例 3.15**

Define $G(s)$ to output $s$ followed by $\oplus_{i=1}^{n} s_{i}$ (i.e., the XOR of all the bits of $s$), so the expansion factor of $G$ is $\ell(n) = n + 1$. The output of $G$ can be distinguished easily from uniform. Consider the following efficient distinguisher $D$: on input a string $w$, output 1 if and only if the final bit of $w$ is equal to the XOR of all the preceding bits of $w$. Since this holds for all strings output by $G$, we have $\Pr[D(G(s)) = 1] = 1$. On the other hand, if $r$ is uniform, the final bit of $r$ is uniform and so $\Pr[D(r) = 1] = \frac{1}{2}$. The quantity $\left|\frac{1}{2} - 1\right|$ is constant, not negligible, and so $G$ is not a pseudorandom generator. (Note that $D$ is not always "correct," since it sometimes outputs 1 even when given a uniform string. But $D$ is still a good distinguisher.)

定义 $G(s)$ 输出 $s$ 后接 $\oplus_{i=1}^{n} s_{i}$（即 $s$ 所有比特的异或），因此 $G$ 的扩展因子为 $\ell(n) = n + 1$。$G$ 的输出可以轻松地与均匀串区分开来。考虑以下高效的区分器 $D$：在输入串 $w$ 时，当且仅当 $w$ 的最后一位等于 $w$ 所有前面位的异或时输出 1。由于这对 $G$ 输出的所有串都成立，我们有 $\Pr[D(G(s)) = 1] = 1$。另一方面，如果 $r$ 是均匀的，$r$ 的最后一位是均匀的，因此 $\Pr[D(r) = 1] = \frac{1}{2}$。量 $\left|\frac{1}{2} - 1\right|$ 是常数，不是可忽略的，因此 $G$ 不是伪随机生成器。（注意 $D$ 并不总是“正确”的，因为即使在给定均匀串时它有时也会输出 1。但 $D$ 仍然是一个好的区分器。）

Discussion. The distribution of the output of a pseudorandom generator $G$ is far from uniform. To see this, consider the case that $\ell(n) = 2n$ and so $G$ doubles the length of its input. Under the uniform distribution on $\{0,1\}^{2n}$, each of the ${2}^{2n}$ possible strings is chosen with probability exactly ${2}^{-2n}$. In contrast, consider the distribution of the output of $G$ when it is run on a uniform $n$-bit seed. The number of different strings in the range of $G$ is at most ${2}^n$. The fraction of strings of length ${2}n$ that are in the range of $G$ is thus at most ${2}^n/2^{2n} = 2^{-n}$, and we see that the vast majority of strings of length ${2}n$ have probability 0 of being output by $G$.

讨论。伪随机生成器 $G$ 的输出分布远非均匀。为了理解这一点，考虑 $\ell(n) = 2n$ 的情况，此时 $G$ 将其输入长度加倍。在 $\{0,1\}^{2n}$ 上的均匀分布下，${2}^{2n}$ 个可能的串每个都以恰好 ${2}^{-2n}$ 的概率被选中。相比之下，考虑 $G$ 在均匀的 $n$ 比特种子上运行时输出的分布。$G$ 值域中不同串的数目最多为 ${2}^n$。因此，长度为 ${2}n$ 的串中属于 $G$ 值域的比例最多为 ${2}^n/2^{2n} = 2^{-n}$，我们看到绝大多数长度为 ${2}n$ 的串被 $G$ 输出的概率为 0。

This in particular means that it is trivial to distinguish between a random string and a pseudorandom string given an unlimited amount of time. Let $G$ be as above and consider the exponential-time distinguisher $D$ that works as follows: $D(w)$ outputs 1 if and only if there exists an $s \in \{0,1\}^n$ such that $G(s) = w$. (This computation is carried out in exponential time by exhaustively computing $G(s)$ for every $s \in \{0,1\}^n$. Recall that by Kerckhoffs' principle, the specification of $G$ is known to $D$.) Now, if $w$ were output by $G$, then $D$ outputs 1 with probability 1. In contrast, if $w$ is uniformly distributed in $\{0,1\}^{2n}$, then the probability that there exists an $s$ with $G(s) = w$ is at most ${2}^{-n}$, and so $D$ outputs 1 in this case with probability at most ${2}^{-n}$. So

这尤其意味着，在拥有无限时间的情况下，区分随机串和伪随机串是平凡的。设 $G$ 如上所述，考虑如下指数时间区分器 $D$：$D(w)$ 输出 1 当且仅当存在 $s \in \{0,1\}^n$ 使得 $G(s) = w$。（该计算通过穷举地计算每个 $s \in \{0,1\}^n$ 的 $G(s)$ 以指数时间完成。回想一下，根据 Kerckhoffs 原则，$G$ 的规范对 $D$ 是已知的。）现在，如果 $w$ 是由 $G$ 输出的，那么 $D$ 以概率 1 输出 1。相反，如果 $w$ 在 $\{0,1\}^{2n}$ 中均匀分布，那么存在 $s$ 使得 $G(s) = w$ 的概率最多为 ${2}^{-n}$，因此在这种情况下 $D$ 以最多 ${2}^{-n}$ 的概率输出 1。于是

$$
\left|\Pr[D(r)=1]-\Pr[D(G(s))=1]\right|\geq1-2^{-n},
$$

which is large. This is just another example of a brute-force attack, and does not contradict the pseudorandomness of G since the attack is not efficient.

这个差值很大。这仅是穷举攻击的另一个例子，并不与 G 的伪随机性相矛盾，因为该攻击不是高效的。

The seed and its length. The seed for a pseudorandom generator is analogous to the key used by an encryption scheme, and—just as in the case of a cryptographic key—the seed $s$ must be chosen uniformly and be kept secret from any adversary if we want $G(s)$ to look random. Another important point, evident from the above discussion of brute-force attacks, is that $s$ must be long enough so that it is not feasible to enumerate all possible seeds. In an asymptotic sense this is taken care of by setting the length of the seed equal to the security parameter, so exhaustive search over all possible seeds requires exponential time. In practice, the seed length $n$ must at least be large enough so that a brute-force attack running in time ${2}^n$ is infeasible.

种子及其长度。伪随机生成器的种子类似于加密方案使用的密钥，并且——就像密码学密钥的情况一样——如果我们希望 $G(s)$ 看起来随机，种子 $s$ 必须均匀选择并对任何敌手保密。从上述关于穷举攻击的讨论中可以看出的另一个重要点是，$s$ 必须足够长，使得穷举所有可能的种子不可行。在渐近意义上，这通过将种子长度设为等于安全参数来处理，因此对所有可能种子的穷举搜索需要指数时间。在实践中，种子长度 $n$ 必须至少足够大，使得运行时间为 ${2}^n$ 的穷举攻击不可行。

On the existence of pseudorandom generators. Do pseudorandom generators exist? They certainly seem difficult to construct, and one may rightly ask whether any algorithm $G$ satisfies Definition 3.14. Although we do not know how to unconditionally prove the existence of pseudorandom generators, we have strong reasons to believe they exist for any (polynomial) expansion factor. For one, they can be constructed under the rather weak assumption that one-way functions exist (which is true if certain problems like factoring are hard); this is discussed in detail in Chapter 8. We also have several practical constructions of candidate pseudorandom generators called stream ciphers for which no efficient distinguishers are known; see Section 3.6.1 for details and Section 7.1 for concrete examples. In this chapter, we simply assume pseudorandom generators exist for any polynomial expansion factor, and explore how they can be used to build secure encryption schemes. Doing so in a sound way relies on the idea of proofs by reduction, which we describe next.

关于伪随机生成器的存在性。伪随机生成器存在吗？它们看起来确实难以构造，人们有理由发问：是否有任何算法 $G$ 满足定义 3.14。虽然我们不知道如何无条件地证明伪随机生成器的存在性，但我们有充分理由相信它们对于任何（多项式）扩展因子都是存在的。一方面，它们在相当弱的假设——单向函数存在（如果某些问题如整数分解是困难的，则单向函数存在）——下可以被构造出来；这将在第 8 章中详细讨论。我们还有几种实际的候选伪随机生成器构造，称为流密码，对于这些构造，目前没有已知的高效区分器；详见 3.6.1 节，具体例子见 7.1 节。在本章中，我们简单地假定伪随机生成器对于任何多项式扩展因子都存在，并探索如何使用它们来构建安全的加密方案。以可靠的方式做到这一点依赖于归约证明的思想，我们接下来描述这一思想。

### 3.3.2 Proofs by Reduction　3.3.2 归约证明

If we wish to prove that a given construction (e.g., encryption scheme) is computationally secure, then—unless the scheme is information-theoretically secure—we must rely on unproven assumptions. Our strategy will be to assume that some mathematical problem is hard, or that some low-level cryptographic primitive is secure, and then to prove that the given construction based on that problem/primitive is secure as long as our initial assumption is correct. In Section 1.4.2 we have already explained in great detail the advantages of this approach, so we do not repeat those arguments here.

如果我们希望证明某个给定的构造（例如加密方案）是计算安全的，那么——除非该方案是信息论安全的——我们必须依赖未经证明的假设。我们的策略是假设某个数学问题是困难的，或者某个低层密码原语是安全的，然后证明基于该问题/原语的给定构造在我们的初始假设正确的前提下是安全的。在 1.4.2 节中我们已经详细解释过这种方法的优点，因此在此不再重复那些论证。

A proof that some cryptographic construction $\Pi$ is secure as long as some underlying problem X is hard generally proceeds by presenting an explicit reduction showing how to transform any efficient adversary A that succeeds in "breaking" $\Pi$ into an efficient algorithm $A^{\prime}$ that solves X. Since this is so important, we walk through a high-level outline of the steps of such a proof in detail. (We will see numerous concrete examples throughout the book, beginning with the proof of Theorem 3.16 in the next section.) We start with the assumption that some problem X cannot be solved (in some precisely defined sense) by any polynomial-time algorithm, except with negligible probability. We then want to prove that some cryptographic construction $\Pi$ is secure (again, in some sense that is precisely defined). A proof by reduction proceeds via the following steps (see also Figure 3.1):

某个密码学构造 $\Pi$ 在某个底层问题 X 困难的条件下是安全的，其证明通常通过给出一个显式的归约来进行，该归约展示了如何将任何成功“攻破” $\Pi$ 的高效敌手 $\mathcal{A}$ 转换成一个解决 X 的高效算法 $\mathcal{A}^{\prime}$。由于这非常重要，我们详细地走一遍此类证明步骤的高层概览。（本书中我们将看到大量具体例子，从下一节定理 3.16 的证明开始。）我们从以下假设开始：某个问题 X（在某个精确定义的意义下）不能被任何多项式时间算法解决，除非以可忽略的概率。然后我们想证明某个密码学构造 $\Pi$ 是安全的（同样，在某个精确定义的意义下）。归约证明通过以下步骤进行（另见图 3.1）：

1. Fix some efficient (i.e., probabilistic polynomial-time) adversary $\mathcal{A}$ attacking $\Pi$. Denote this adversary's success probability by $\varepsilon(n)$.

   固定某个攻击 $\Pi$ 的高效（即概率多项式时间）敌手 $\mathcal{A}$。记该敌手的成功概率为 $\varepsilon(n)$。

2. Construct an efficient algorithm $\mathcal{A}^{\prime}$ that attempts to solve problem X by using adversary $\mathcal{A}$ as a subroutine. An important point here is that $\mathcal{A}^{\prime}$ knows nothing about how $\mathcal{A}$ works; the only thing $\mathcal{A}^{\prime}$ knows is that $\mathcal{A}$ is expecting to attack $\Pi$. So, given some input instance x of problem X, our algorithm $\mathcal{A}^{\prime}$ will simulate for $\mathcal{A}$ an instance of $\Pi$ such that:

   构造一个高效算法 $\mathcal{A}^{\prime}$，它通过将敌手 $\mathcal{A}$ 作为子程序来尝试解决问题 X。这里的一个重要点是，$\mathcal{A}^{\prime}$ 对 $\mathcal{A}$ 如何工作一无所知；$\mathcal{A}^{\prime}$ 唯一知道的是 $\mathcal{A}$ 期望攻击 $\Pi$。因此，给定问题 X 的某个输入实例 x，我们的算法 $\mathcal{A}^{\prime}$ 将为 $\mathcal{A}$ 模拟一个 $\Pi$ 的实例，使得：

   (a) As far as $\mathcal{A}$ can tell, it is interacting with $\Pi$. That is, the view of $\mathcal{A}$ when run as a subroutine by $\mathcal{A}^{\prime}$ should be distributed identically to (or at least close to) the view of $\mathcal{A}$ when it interacts with $\Pi$ itself.

   (a) 就 $\mathcal{A}$ 所能感知到的而言，它正在与 $\Pi$ 交互。也就是说，$\mathcal{A}$ 在被 $\mathcal{A}^{\prime}$ 作为子程序运行时的视图，应与 $\mathcal{A}$ 在与 $\Pi$ 本身交互时的视图分布相同（或至少接近）。

   (b) When $\mathcal{A}$ succeeds in "breaking" the instance of $\Pi$ that is being simulated by $\mathcal{A}^{\prime}$, this should allow $\mathcal{A}^{\prime}$ to solve the instance x it was given, at least with inverse polynomial probability ${1}/p(n)$.

   (b) 当 $\mathcal{A}$ 成功“攻破”了 $\mathcal{A}^{\prime}$ 正在模拟的 $\Pi$ 实例时，这应使得 $\mathcal{A}^{\prime}$ 能够解决它被给定的实例 x，至少以逆多项式概率 ${1}/p(n)$。

I.e., we attempt to reduce the problem of solving X to the problem of breaking $\Pi$.

也就是说，我们试图将解决问题 X 归约为攻破 $\Pi$ 的问题。

![Image](https://lsky.jerryxue.top/i/2026/08/22/6a88f9dcd3cec.jpg)

**FIGURE 3.1: A high-level overview of a proof by reduction.**

**图 3.1：归约证明的高层概览。**

3. Taken together, the above imply that $\mathcal{A}^{\prime}$ solves X with probability $\varepsilon(n)/p(n)$. Now, if $\varepsilon(n)$ is not negligible then neither is $\varepsilon(n)/p(n)$. Moreover, if $\mathcal{A}$ is efficient then we obtain an efficient algorithm $\mathcal{A}^{\prime}$ solving X with non-negligible probability, contradicting our initial assumption.

   综合起来，上述表明 $\mathcal{A}^{\prime}$ 以概率 $\varepsilon(n)/p(n)$ 解决 X。现在，如果 $\varepsilon(n)$ 不是可忽略的，那么 $\varepsilon(n)/p(n)$ 也不是可忽略的。此外，如果 $\mathcal{A}$ 是高效的，那么我们就得到一个以不可忽略概率解决 X 的高效算法 $\mathcal{A}^{\prime}$，这与我们的初始假设相矛盾。

4. Given our assumption regarding X, we conclude that no efficient adversary A can succeed in breaking $\Pi$ with non-negligible probability. Stated differently, $\Pi$ is computationally secure.

   鉴于我们对 X 的假设，我们得出结论：没有高效敌手 $\mathcal{A}$ 能够以不可忽略概率成功攻破 $\Pi$。换句话说，$\Pi$ 是计算安全的。

As an illustration of the above idea, we show in the following section how to use a pseudorandom generator $G$ to construct an encryption scheme, and we prove the encryption scheme secure by showing that any attacker who can "break" the encryption scheme can be used to distinguish the output of $G$ from a uniform string. Under the assumption that $G$ is a pseudorandom generator, then, the encryption scheme is secure.

作为上述思想的示例，我们在下一节展示如何使用伪随机生成器 $G$ 来构造一个加密方案，并通过证明任何能够“攻破”该加密方案的攻击者都可以被用来区分 $G$ 的输出与均匀串，从而证明该加密方案是安全的。于是，在 $G$ 是伪随机生成器的假设下，该加密方案是安全的。

### 3.3.3 EAV-Security from a Pseudorandom Generator　3.3.3 基于伪随机生成器的 EAV 安全性

A pseudorandom generator provides a natural way to construct a secure, fixed-length encryption scheme with a key shorter than the message. Recall that in the one-time pad (see Section 2.2), encryption is done by XORing a random pad with the message. The crucial insight is that we can use a pseudorandom pad instead. Rather than sharing this long, pseudorandom pad, however, the sender and receiver can instead share a uniform seed that is used to generate the pad when needed (see Figure 3.2); this seed will be shorter than the pad and hence shorter than the message. As for security, the intuition is that a pseudorandom string "looks random" to any polynomial-time adversary and so a computationally bounded eavesdropper cannot distinguish between a message encrypted using the one-time pad or a message encrypted using this "pseudo-" one-time pad encryption scheme.

伪随机生成器提供了一种自然的方式来构造密钥比消息短的安全定长加密方案。回顾一次一密（见 2.2 节），加密是通过将随机填充与消息异或来完成的。关键的洞察是我们可以使用伪随机填充来代替。然而，发送方和接收方无需共享这个长的伪随机填充，而是可以共享一个均匀种子，在需要时用该种子生成填充（见图 3.2）；这个种子将比填充短，因而比消息短。至于安全性，直觉是伪随机串对任何多项式时间敌手“看起来是随机的”，因此一个计算受限的窃听者无法区分使用一次一密加密的消息和使用这种“伪”一次一密加密方案加密的消息。

![Image](https://lsky.jerryxue.top/i/2026/08/22/6a88f9ddaa1d7.jpg)

**FIGURE 3.2: Encryption with a pseudorandom generator.**

**图 3.2：使用伪随机生成器的加密。**

The encryption scheme. Fix some message length $\ell(n)$ and let $G$ be a pseudorandom generator with expansion factor $\ell(n)$ (that is, $|G(s)| = \ell(|s|)$). Recall that an encryption scheme is defined by three algorithms: a key-generation algorithm $\mathsf{Gen}$, an encryption algorithm $\mathsf{Enc}$, and a decryption algorithm $\mathsf{Dec}$. The key-generation algorithm is the trivial one: $\mathsf{Gen}(1^n)$ simply outputs a uniform key $k \in \{0,1\}^n$. Encryption works by applying $G$ to the key (which serves as a seed) in order to obtain a pad that is then XORed with the plaintext. Decryption applies $G$ to the key and XORs the resulting pad with the ciphertext to recover the message. The scheme is described formally in Construction 3.17. In Section 3.6.2, we describe how stream ciphers are used to implement a variant of this scheme in practice.

加密方案。固定某个消息长度 $\ell(n)$，令 $G$ 是一个扩展因子为 $\ell(n)$ 的伪随机生成器（即 $|G(s)| = \ell(|s|)$）。回忆加密方案由三个算法定义：密钥生成算法 $\mathsf{Gen}$、加密算法 $\mathsf{Enc}$ 和解密算法 $\mathsf{Dec}$。密钥生成算法是平凡的：$\mathsf{Gen}(1^n)$ 简单地输出一个均匀密钥 $k \in \{0,1\}^n$。加密通过对密钥（作为种子）应用 $G$ 来获得一个填充，然后将该填充与明文异或。解密对密钥应用 $G$，并将所得的填充与密文异或以恢复消息。该方案在构造 3.17 中形式化描述。在 3.6.2 节中，我们描述了流密码如何在实践中用于实现该方案的一个变体。

> **CONSTRUCTION 3.17**　**构造 3.17**
>
> Let G be a pseudorandom generator with expansion factor $\ell(n)$. Define a fixed-length private-key encryption scheme for messages of length $\ell(n)$ as follows:
>
> Gen: on input ${1}^n$, choose uniform $k \in \{0,1\}^n$ and output it as the key.
>
> - Enc: on input a key $k \in \{0,1\}^n$ and a message $m \in \{0,1\}^{\ell(n)}$, output the ciphertext
>
> $$
> c:=G(k)\oplus m.
> $$
>
> - Dec: on input a key $k \in \{0,1\}^{n}$ and a ciphertext $c \in \{0,1\}^{\ell(n)}$, output the message $m := G(k) \oplus c$.
>
> 设 G 是一个扩展因子为 $\ell(n)$ 的伪随机生成器。为长度为 $\ell(n)$ 的消息定义如下的定长私钥加密方案：
>
> Gen：输入 ${1}^n$，选择均匀的 $k \in \{0,1\}^n$ 并作为密钥输出。
>
> - Enc：输入密钥 $k \in \{0,1\}^n$ 和消息 $m \in \{0,1\}^{\ell(n)}$，输出密文
>
> $$
> c:=G(k)\oplus m.
> $$
>
> - Dec：输入密钥 $k \in \{0,1\}^{n}$ 和密文 $c \in \{0,1\}^{\ell(n)}$，输出消息 $m := G(k) \oplus c$。
>
> A private-key encryption scheme based on any pseudorandom generator.
> 一个基于任意伪随机生成器的私钥加密方案。

THEOREM 3.16 If G is a pseudorandom generator, then Construction 3.17 is an EAV-secure, fixed-length private-key encryption scheme for messages of length $\ell(n)$.

定理 3.16 如果 G 是一个伪随机生成器，那么构造 3.17 是一个 EAV 安全的定长私钥加密方案，适用于长度为 $\ell(n)$ 的消息。

PROOF Let $\Pi$ denote Construction 3.17. We show that $\Pi$ satisfies Definition 3.8 (under the assumption that $G$ is a pseudorandom generator). Namely, we show that for any probabilistic polynomial-time adversary $\mathcal{A}$ there is a negligible function $\mathsf{negl}$ such that

证明 令 $\Pi$ 表示构造 3.17。我们证明 $\Pi$ 满足定义 3.8（在 $G$ 是伪随机生成器的假设下）。即，我们证明对于任何概率多项式时间敌手 $\mathcal{A}$，存在一个可忽略函数 $\mathsf{negl}$，使得

$$
\Pr\left[\mathsf{PrivK}_{\mathcal{A},\Pi}^{\mathsf{eav}}(n)=1\right]\leq\frac{1}{2}+\mathsf{negl}(n).\tag{3.3}
$$

The intuition is that if $\Pi$ used a uniform pad in place of the pseudorandom pad $G(k)$, then the resulting scheme would be identical to the one-time pad encryption scheme and $\mathcal{A}$ would be unable to correctly guess which message was encrypted with probability any better than ${1}/2$. Thus, if Equation (3.3) does not hold then $\mathcal{A}$ must implicitly be distinguishing the output of $G$ from a random string. We make this explicit by showing a reduction; namely, by showing how to use $\mathcal{A}$ to construct an efficient distinguisher $D$, with the property that $D$'s ability to distinguish the output of $G$ from a uniform string is directly related to $\mathcal{A}$'s ability to determine which message was encrypted by $\Pi$. Security of $G$ then implies security of $\Pi$.

直觉是，如果 $\Pi$ 使用均匀填充代替伪随机填充 $G(k)$，那么所得方案将等同于一次一密加密方案，$\mathcal{A}$ 将无法以优于 ${1}/2$ 的概率正确猜测哪条消息被加密了。因此，如果式 (3.3) 不成立，那么 $\mathcal{A}$ 必然在隐式地区分 $G$ 的输出与随机串。我们通过展示一个归约来使其显式化；即，展示如何使用 $\mathcal{A}$ 构造一个高效的区分器 $D$，使得 $D$ 区分 $G$ 输出与均匀串的能力与 $\mathcal{A}$ 确定 $\Pi$ 加密了哪条消息的能力直接相关。于是 $G$ 的安全性蕴含 $\Pi$ 的安全性。

Let $\mathcal{A}$ be an arbitrary PPT adversary. We construct a distinguisher $D$ that takes a string $w$ as input, and whose goal is to determine whether $w$ was chosen uniformly (i.e., $w$ is a "random string") or whether $w$ was generated by choosing a uniform $k$ and computing $w := G(k)$ (i.e., $w$ is a "pseudorandom string"). We construct $D$ so that it emulates the eavesdropping experiment for $\mathcal{A}$, as described below, and observes whether $\mathcal{A}$ succeeds or not. If $\mathcal{A}$ succeeds then $D$ guesses that $w$ must be a pseudorandom string, while if $\mathcal{A}$ does not succeed then $D$ guesses that $w$ is a random string. In detail:

令 $\mathcal{A}$ 是一个任意的 PPT 敌手。我们构造一个以串 $w$ 为输入的区分器 $D$，其目标是确定 $w$ 是均匀选择的（即 $w$ 是一个“随机串”），还是通过选择均匀的 $k$ 并计算 $w := G(k)$ 生成的（即 $w$ 是一个“伪随机串”）。我们构造 $D$ 使其模拟 $\mathcal{A}$ 的窃听实验（如下所述），并观察 $\mathcal{A}$ 是否成功。如果 $\mathcal{A}$ 成功，则 $D$ 猜测 $w$ 应当是伪随机串；如果 $\mathcal{A}$ 不成功，则 $D$ 猜测 $w$ 是随机串。详细地：

> **Distinguisher D:**　**区分器 D：**
>
> D is given as input a string $w \in \{0,1\}^{\ell(n)}$. (We assume that n can be determined from $\ell(n)$.)
>
> 1. Run $\mathcal{A}(1^n)$ to obtain a pair of messages $m_0, m_1 \in \{0,1\}^{\ell(n)}$.
> 2. Choose a uniform bit $b \in \{0,1\}$. Set $c := w \oplus m_b$.
> 3. Give c to A and obtain output $b^{\prime}$. Output 1 if $b^{\prime} = b$, and output 0 otherwise.
>
> D 被给定一个输入串 $w \in \{0,1\}^{\ell(n)}$。（我们假定 n 可以从 $\ell(n)$ 确定。）
> 1. 运行 $\mathcal{A}(1^n)$ 获得一对消息 $m_0, m_1 \in \{0,1\}^{\ell(n)}$。
> 2. 选择一个均匀比特 $b \in \{0,1\}$。设 $c := w \oplus m_b$。
> 3. 将 c 交给 A 并获得输出 $b^{\prime}$。如果 $b^{\prime} = b$ 则输出 1，否则输出 0。
>
> D clearly runs in polynomial time (assuming $\mathcal{A}$ does).
>
> D 显然在多项式时间内运行（假定 $\mathcal{A}$ 如此）。

Before analyzing the behavior of $D$, we define a modified encryption scheme $\widetilde{\Pi} = (\widetilde{\mathsf{Gen}}, \widetilde{\mathsf{Enc}}, \widetilde{\mathsf{Dec}})$ that is exactly the one-time pad encryption scheme, except that we now incorporate a security parameter that determines the length of the message to be encrypted. That is, $\widetilde{\mathsf{Gen}}(1^n)$ outputs a uniform key $k$ of length $\ell(n)$, and the encryption of message $m \in \{0,1\}^{\ell(n)}$ using key $k \in \{0,1\}^{\ell(n)}$ is the ciphertext $c := k \oplus m$. (Decryption can be done as usual, but is inessential to what follows.) Perfect secrecy of the one-time pad implies

在分析 $D$ 的行为之前，我们定义一个修改后的加密方案 $\widetilde{\Pi} = (\widetilde{\mathsf{Gen}}, \widetilde{\mathsf{Enc}}, \widetilde{\mathsf{Dec}})$，它正好是一次一密加密方案，只是我们现在引入了一个安全参数来决定要加密消息的长度。也就是说，$\widetilde{\mathsf{Gen}}(1^n)$ 输出一个长度为 $\ell(n)$ 的均匀密钥 $k$，使用密钥 $k \in \{0,1\}^{\ell(n)}$ 对消息 $m \in \{0,1\}^{\ell(n)}$ 加密的密文是 $c := k \oplus m$。（解密可以照常进行，但对后续内容不重要。）一次一密的完美保密性意味着

$$
\Pr\left[\mathsf{PrivK}_{\mathcal{A},\widetilde{\Pi}}^{\mathsf{eav}}(n)=1\right]=\frac{1}{2}.
$$

To analyze the behavior of $D$, the main observations are:

为分析 $D$ 的行为，主要观察如下：

1. If $w$ is chosen uniformly from $\{0,1\}^{\ell(n)}$, then the view of $\mathcal{A}$ when run as a subroutine by $D$ is distributed identically to the view of $\mathcal{A}$ in experiment $\mathsf{PrivK}_{\mathcal{A},\widetilde{\Pi}}^{\mathsf{eav}}(n)$. This is because when $\mathcal{A}$ is run as a subroutine by $D(w)$ in this case, $\mathcal{A}$ is given a ciphertext $c = w\oplus m_b$ where $w\in\{0,1\}^{\ell(n)}$ is uniform. Since $D$ outputs 1 exactly when $\mathcal{A}$ succeeds in its eavesdropping experiment, we therefore have (using Equation (3.4))

   如果 $w$ 从 $\{0,1\}^{\ell(n)}$ 中均匀选择，那么 $\mathcal{A}$ 在被 $D$ 作为子程序运行时的视图，与 $\mathcal{A}$ 在实验 $\mathsf{PrivK}_{\mathcal{A},\widetilde{\Pi}}^{\mathsf{eav}}(n)$ 中的视图分布相同。这是因为当 $\mathcal{A}$ 在这种情况下被 $D(w)$ 作为子程序运行时，$\mathcal{A}$ 被给定的密文是 $c = w\oplus m_b$，其中 $w\in\{0,1\}^{\ell(n)}$ 是均匀的。由于 $D$ 恰好当 $\mathcal{A}$ 在其窃听实验中成功时输出 1，因此我们（利用式 (3.4)）有

   $$
   \begin{array}{r l}&{\Pr_{w\leftarrow\{0,1\}^{\ell(n)}}[D(w)=1]=\Pr\left[\mathsf{PrivK}_{\mathcal{A},\widetilde{\Pi}}^{\mathsf{eav}}(n)=1\right]=\frac{1}{2}.} \tag{3.4}\end{array}
   $$

   (The subscript on the first probability just makes explicit that $w$ is chosen uniformly from $\{0,1\}^{\ell(n)}$ there.)

   （第一个概率的下标只是明确表示 $w$ 是从 $\{0,1\}^{\ell(n)}$ 中均匀选择的。）

2. If $w$ is instead generated by choosing uniform $k \in \{0,1\}^n$ and then setting $w := G(k)$, the view of $\mathcal{A}$ when run as a subroutine by $D$ is distributed identically to the view of $\mathcal{A}$ in experiment $\mathsf{PrivK}_{\mathcal{A},\Pi}^{\mathsf{eav}}(n)$. This is because $\mathcal{A}$, when run as a subroutine by $D$, is now given a ciphertext $c = w \oplus m_b$ where $w = G(k)$ for a uniform $k \in \{0,1\}^n$. Thus,

   如果 $w$ 改为通过选择均匀的 $k \in \{0,1\}^n$ 然后设 $w := G(k)$ 来生成，那么 $\mathcal{A}$ 在被 $D$ 作为子程序运行时的视图，与 $\mathcal{A}$ 在实验 $\mathsf{PrivK}_{\mathcal{A},\Pi}^{\mathsf{eav}}(n)$ 中的视图分布相同。这是因为 $\mathcal{A}$ 在被 $D$ 作为子程序运行时，现在被给定的密文是 $c = w \oplus m_b$，其中对于均匀的 $k \in \{0,1\}^n$ 有 $w = G(k)$。因此，

   $$
   \begin{array}{r}{\Pr_{k\leftarrow\{0,1\}^{n}}\big[D\big(G(k)\big)=1\big]=\Pr\left[\mathsf{PrivK}_{\mathcal{A},\Pi}^{\mathsf{eav}}(n)=1\right].} \tag{3.5}\end{array}
   $$

Since $G$ is a pseudorandom generator (and since $D$ runs in polynomial time), we know there is a negligible function $\mathsf{negl}$ such that

由于 $G$ 是一个伪随机生成器（且 $D$ 在多项式时间内运行），我们知道存在一个可忽略函数 $\mathsf{negl}$，使得

$$
\left|\Pr_{k\leftarrow\{0,1\}^{n}}[D(G(k))=1]-\Pr_{w\leftarrow\{0,1\}^{\ell(n)}}[D(w)=1]\right|\leq\mathsf{negl}(n).\tag{3.6}
$$

Using Equations (3.5) and (3.6), we thus see that

利用式 (3.5) 和 (3.6)，我们于是看到

$$
\left|\Pr\left[\mathsf{PrivK}_{\mathcal{A},\Pi}^{\mathsf{eav}}(n)=1\right]-\frac{1}{2}\right|\leq\mathsf{negl}(n),
$$

which implies $\Pr\left[\operatorname{PrivK}_{\mathcal{A},\Pi}^{\mathsf{eav}}(n)=1\right]\leq\tfrac{1}{2}+\mathsf{negl}(n)$. Since $\mathcal{A}$ was an arbitrary PPT adversary, this completes the proof that $\Pi$ is EAV-secure.

这意味着 $\Pr\left[\operatorname{PrivK}_{\mathcal{A},\Pi}^{\mathsf{eav}}(n)=1\right]\leq\tfrac{1}{2}+\mathsf{negl}(n)$。由于 $\mathcal{A}$ 是任意的 PPT 敌手，这就完成了对 $\Pi$ 是 EAV 安全的证明。

It is easy to get lost in the details of the proof and wonder whether anything has been gained as compared to the one-time pad; after all, the one-time pad also encrypts an $\ell$-bit message by XORing it with an $\ell$-bit string! The point of the construction, of course, is that the shared key k can be much shorter than the $\ell$-bit string $G(k)$. In particular, using the above scheme it may be possible to securely encrypt a 1 Mb file using only a 128-bit key. By relying on computational secrecy we have thus circumvented the impossibility result of Theorem 2.11, which states that any perfectly secret encryption scheme must use a key at least as long as the message.

人们很容易在证明的细节中迷失方向，并怀疑与一次一密相比是否获得了任何进展；毕竟，一次一密也是通过将 $\ell$ 比特消息与 $\ell$ 比特串异或来加密的！当然，该构造的关键在于共享密钥 $k$ 可以远短于 $\ell$ 比特串 $G(k)$。特别地，使用上述方案，可以用仅 128 位的密钥安全地加密 1 Mb 的文件。通过依赖计算保密性，我们绕过了定理 2.11 的不可能性结果，该定理指出任何完美保密的加密方案必须使用至少与消息等长的密钥。

Reductions—a discussion. We do not prove unconditionally that Construction 3.17 is secure. Rather, we prove that it is secure under the assumption that $G$ is a pseudorandom generator. This approach of reducing the security of a higher-level construction to a lower-level primitive has a number of advantages (as discussed in Section 1.4.2). One of these advantages is that, in general, it is easier to design a lower-level primitive than a higher-level one; it is also easier, in general, to directly analyze an algorithm $G$ with respect to a lower-level definition than to analyze a more complex scheme $\Pi$ with respect to a higher-level definition. This does not mean that constructing a pseudorandom generator is "easy," only that it is easier than constructing an encryption scheme from scratch. (In the present case the encryption scheme does nothing except XOR the output of a pseudorandom generator with the message and so this isn't quite true. Soon, however, we will see more complex constructions and in those cases the ability to reduce the task to a simpler one is very useful.) Another advantage is that the construction can be instantiated with any pseudorandom generator $G$, providing some flexibility to the users of the scheme.

归约——讨论。我们并非无条件地证明构造 3.17 是安全的。相反，我们证明它在 $G$ 是伪随机生成器的假设下是安全的。这种将高层构造的安全性归约到低层原语的方法具有许多优点（如 1.4.2 节所讨论的）。其中一个优点是，通常设计低层原语比设计高层原语更容易；通常，直接针对低层定义分析算法 $G$ 也比针对高层定义分析更复杂的方案 $\Pi$ 更容易。这并不意味着构造伪随机生成器是“容易的”，只是说它比从头开始构造加密方案更容易。（在当前情况下，加密方案除了将伪随机生成器的输出与消息异或之外什么也没做，因此这一点并不完全正确。然而，很快我们将看到更复杂的构造，在这些情况下，将任务归约到更简单问题的能力非常有用。）另一个优点是，该构造可以用任何伪随机生成器 $G$ 来实例化，为方案的用户提供了一定的灵活性。

Concrete security. Although Theorem 3.16 and its proof are in an asymptotic setting, we can readily adapt the proof to bound the concrete security of the encryption scheme in terms of the concrete security of $G$. Fix some value of $n$ for the remainder of this discussion, and let $\Pi$ now denote Construction 3.17 using this value of $n$. Assume $G$ is $(t,\varepsilon)$-pseudorandom (for the given value of $n$), in the sense that for all distinguishers $D$ running in time at most $t$ we have

具体安全性。虽然定理 3.16 及其证明是在渐近设定中，但我们可以轻松地调整该证明，根据 $G$ 的具体安全性来界定加密方案的具体安全性。在本讨论的剩余部分固定某个 $n$ 值，并令 $\Pi$ 现在表示使用该 $n$ 值的构造 3.17。假设 $G$ 是 $(t,\varepsilon)$-伪随机的（对于给定的 $n$ 值），即对于所有运行时间最多为 $t$ 的区分器 $D$，我们有

$$
\left|\Pr[D(G(s))=1]-\Pr[D(r)=1]\right|\leq\varepsilon.\tag{3.7}
$$

(Think of $t \approx 2^{80}$ CPU cycles and $\varepsilon \approx 2^{-60}$, though precise values are irrelevant for our discussion.) We claim that $\Pi$ is $(t-t^{\prime}, \varepsilon)$-secure for some (small) constant $t^{\prime}$, in the sense that for all $\mathcal{A}$ running in time at most $t-t^{\prime}$ we have

（可以把 $t \approx 2^{80}$ CPU 周期和 $\varepsilon \approx 2^{-60}$ 作为参考，尽管精确值对我们的讨论无关紧要。）我们断言 $\Pi$ 是 $(t-t^{\prime}, \varepsilon)$-安全的（对于某个（小的）常数 $t^{\prime}$），即对于所有运行时间最多为 $t-t^{\prime}$ 的 $\mathcal{A}$，我们有

$$
\Pr\left[\mathsf{PrivK}_{\mathcal{A},\Pi}^{\mathsf{eav}}=1\right]\leq\frac{1}{2}+\varepsilon.\tag{3.8}
$$

(Note that the above are now fixed numbers, not functions of $n$, since we have fixed $n$ and are no longer in an asymptotic setting.) To see this, let $\mathcal{A}$ be an arbitrary adversary running in time at most $t - t^{\prime}$. Distinguisher $D$, as constructed in the proof of Theorem 3.16, has very little overhead besides running $\mathcal{A}$; setting $t^{\prime}$ appropriately ensures that $D$ runs in time at most $t$. Our assumption on the concrete security of $G$ then implies Equation (3.7); proceeding exactly as in the proof of Theorem 3.16, we obtain Equation (3.8).

（注意，上述现在是固定数值，而不是 $n$ 的函数，因为我们固定了 $n$ 且不再处于渐近设定中。）要理解这一点，令 $\mathcal{A}$ 是运行时间最多为 $t - t^{\prime}$ 的任意敌手。在定理 3.16 的证明中构造的区分器 $D$，除了运行 $\mathcal{A}$ 之外只有很小的开销；适当设置 $t^{\prime}$ 可以确保 $D$ 的运行时间最多为 $t$。我们对 $G$ 具体安全性的假设意味着式 (3.7)；完全按照定理 3.16 的证明进行，我们得到式 (3.8)。

## 3.4 Stronger Security Notions　3.4 更强的安全性概念

Until now we have considered a relatively weak definition of security in which the adversary only passively eavesdrops on a single ciphertext sent between the honest parties. Here we consider stronger security notions.

到目前为止，我们考虑了一种相对较弱的安全性定义，其中敌手仅被动地窃听诚实方之间发送的单个密文。现在我们考虑更强的安全性概念。

### 3.4.1 Security for Multiple Encryptions　3.4.1 多重加密的安全性

Definition 3.8 deals with the case where the communicating parties transmit a single ciphertext that is observed by an eavesdropper. It would be convenient, however, if the communicating parties could securely send multiple ciphertexts to each other—all generated using the same key—even if an eavesdropper might observe all of them. For such applications we need an encryption scheme secure for the encryption of multiple messages.

定义 3.8 处理的是通信双方传输单个密文且该密文被窃听者观察到的情况。然而，如果通信双方能够安全地相互发送多个密文——所有这些密文都使用同一个密钥生成——即使窃听者可能观察到全部密文，那将会很方便。对于这类应用，我们需要一个对加密多条消息安全的加密方案。

We begin with an appropriate definition of security for this setting. As in the case of Definition 3.8, we first introduce an appropriate experiment defined for any encryption scheme $\Pi$, adversary $\mathcal{A}$, and security parameter $n$:

我们首先给出适用于该场景的安全性定义。如同定义 3.8 的情况，我们首先引入一个为任意加密方案 $\Pi$、敌手 $\mathcal{A}$ 和安全参数 $n$ 定义的实验：

The multiple-message eavesdropping experiment $\mathsf{PrivK}_{\mathcal{A},\Pi}^{\mathsf{mult}}(n)$:

多重消息窃听实验 $\mathsf{PrivK}_{\mathcal{A},\Pi}^{\mathsf{mult}}(n)$：

1. The adversary $\mathcal{A}$ is given input ${1}^n$, and outputs a pair of equal-length lists of messages $\vec{M}_0 = (m_{0,1}, \ldots, m_{0,t})$ and $\vec{M}_1 = (m_{1,1}, \ldots, m_{1,t})$, with $|m_{0,i}| = |m_{1,i}|$ for all $i$.

   敌手 $\mathcal{A}$ 获得输入 ${1}^n$，并输出一对等长的消息列表 $\vec{M}_0 = (m_{0,1}, \ldots, m_{0,t})$ 和 $\vec{M}_1 = (m_{1,1}, \ldots, m_{1,t})$，且对所有 $i$ 有 $|m_{0,i}| = |m_{1,i}|$。

2. A key k is generated by running $\mathsf{Gen}(1^n)$, and a uniform bit $b \in \{0,1\}$ is chosen. For all $i$, the ciphertext $c_i \leftarrow \mathsf{Enc}_k(m_{b,i})$ is computed and the list $\vec{C} = (c_1, \ldots, c_t)$ is given to $\mathcal{A}$.

   通过运行 $\mathsf{Gen}(1^n)$ 生成密钥 $k$，并选择一个均匀比特 $b \in \{0,1\}$。对所有 $i$，计算密文 $c_i \leftarrow \mathsf{Enc}_k(m_{b,i})$，并将列表 $\vec{C} = (c_1, \ldots, c_t)$ 交给 $\mathcal{A}$。

3. A outputs a bit b'.

   $\mathcal{A}$ 输出一个比特 $b'$。

4. The output of the experiment is defined to be 1 if $b^{\prime} = b$, and 0 otherwise.

   实验的输出定义为：如果 $b^{\prime} = b$ 则为 1，否则为 0。

The definition of security is the same as before, except that it now refers to the above experiment.

安全性的定义与之前相同，只是现在参照上述实验。

DEFINITION 3.18 A private-key encryption scheme $\Pi = (\mathrm{Gen}, \mathrm{Enc}, \mathrm{Dec})$ has indistinguishable multiple encryptions in the presence of an eavesdropper if for all probabilistic polynomial-time adversaries $\mathcal{A}$ there is a negligible function $\mathsf{negl}$ such that

定义 3.18 私钥加密方案 $\Pi = (\mathrm{Gen}, \mathrm{Enc}, \mathrm{Dec})$ 在窃听者存在的情况下具有**不可区分的多重加密**（indistinguishable multiple encryptions），如果对于所有概率多项式时间敌手 $\mathcal{A}$，存在一个可忽略函数 $\mathsf{negl}$，使得

$$
\Pr\left[\mathsf{PrivK}_{\mathcal{A},\Pi}^{\mathsf{mult}}(n)=1\right]\leq\frac{1}{2}+\mathsf{negl}(n).
$$

Any scheme that has indistinguishable multiple encryptions in the presence of an eavesdropper clearly also satisfies Definition 3.8, since experiment $\mathsf{PrivK}_{\mathcal{A},\Pi}^{\mathsf{eav}}(n)$ corresponds to the special case of $\mathsf{PrivK}_{\mathcal{A},\Pi}^{\mathsf{mult}}(n)$ where the adversary outputs two lists containing only a single message each. In fact, our new definition is strictly stronger than Definition 3.8, as the following shows.

任何在窃听者存在的情况下具有不可区分多重加密的方案显然也满足定义 3.8，因为实验 $\mathsf{PrivK}_{\mathcal{A},\Pi}^{\mathsf{eav}}(n)$ 对应于 $\mathsf{PrivK}_{\mathcal{A},\Pi}^{\mathsf{mult}}(n)$ 的特殊情况，即敌手输出两个各只包含一条消息的列表。事实上，我们的新定义严格强于定义 3.8，如下所示。

PROPOSITION 3.19 There is a private-key encryption scheme that has indistinguishable encryptions in the presence of an eavesdropper, but not indistinguishable multiple encryptions in the presence of an eavesdropper.

命题 3.19 存在一种私钥加密方案，它在窃听者存在的情况下具有不可区分加密，但不具有窃听者存在情况下的不可区分多重加密。

PROOF We do not have to look far to find an example of an encryption scheme satisfying the proposition. The one-time pad is perfectly secret, and so also has indistinguishable encryptions in the presence of an eavesdropper. We show that it is not secure in the sense of Definition 3.18. (We have discussed this attack in Chapter 2 already; here, we merely analyze the attack with respect to Definition 3.18.)

证明 我们不必费太大力气就能找到满足该命题的加密方案示例。一次一密是完美保密的，因此也在窃听者存在的情况下具有不可区分加密。我们证明它在定义 3.18 的意义下是不安全的。（我们已经在第 2 章中讨论过这种攻击；在此，我们仅针对定义 3.18 来分析该攻击。）

Concretely, consider the following adversary $\mathcal{A}$ attacking the scheme $\Pi$ (in the sense defined by experiment $\mathsf{PrivK}_{\mathcal{A},\Pi}^{\mathsf{mult}}(n)$): $\mathcal{A}$ outputs $\vec{M}_0 = (0^\ell, 0^\ell)$ and $\vec{M}_1 = (0^\ell, 1^\ell)$. (The first contains the same message twice, while the second contains two different messages.) Let $\vec{C} = (c_1, c_2)$ be the list of ciphertexts that $\mathcal{A}$ receives. If $c_1 = c_2$, then $\mathcal{A}$ outputs $b^{\prime} = 0$; otherwise, $\mathcal{A}$ outputs $b^{\prime} = 1$.

具体地，考虑以下攻击方案 $\Pi$ 的敌手 $\mathcal{A}$（在实验 $\mathsf{PrivK}_{\mathcal{A},\Pi}^{\mathsf{mult}}(n)$ 定义的意义下）：$\mathcal{A}$ 输出 $\vec{M}_0 = (0^\ell, 0^\ell)$ 和 $\vec{M}_1 = (0^\ell, 1^\ell)$。（前者包含两次相同的消息，而后者包含两条不同的消息。）令 $\vec{C} = (c_1, c_2)$ 是 $\mathcal{A}$ 收到的密文列表。如果 $c_1 = c_2$，则 $\mathcal{A}$ 输出 $b^{\prime} = 0$；否则 $\mathcal{A}$ 输出 $b^{\prime} = 1$。

We now analyze the probability that $b^{\prime} = b$. The crucial point is that the one-time pad is deterministic, so encrypting the same message twice (using the same key) yields the same ciphertext. Thus, if b = 0 then we must have $c_1 = c_2$ and $\mathcal{A}$ outputs 0 in this case. On the other hand, if b = 1 then a different message is encrypted each time; hence $c_1 \neq c_2$ and $\mathcal{A}$ outputs 1. We conclude that $\mathcal{A}$ correctly outputs $b^{\prime} = b$ with probability 1, and so the encryption scheme is not secure with respect to Definition 3.18.

我们现在分析 $b^{\prime} = b$ 的概率。关键点在于一次一密是确定性的，因此使用同一密钥两次加密相同的消息会产生相同的密文。因此，如果 b = 0，则必然有 $c_1 = c_2$，此时 $\mathcal{A}$ 输出 0。另一方面，如果 b = 1，则每次加密不同的消息；因此 $c_1 \neq c_2$，$\mathcal{A}$ 输出 1。我们得出结论：$\mathcal{A}$ 以概率 1 正确输出 $b^{\prime} = b$，因此该加密方案相对于定义 3.18 是不安全的。

Necessity of probabilistic encryption. The above might appear to show that Definition 3.18 is impossible to achieve using any encryption scheme. This is true as long as the encryption scheme is (stateless $^{2}$ and) deterministic, and so encrypting the same message multiple times using the same key always yields the same result. This is important enough to state as a theorem.

概率性加密的必要性。上述结果似乎表明，任何加密方案都不可能满足定义 3.18。只要加密方案是（无状态的 $^{2}$ 且）确定性的，这一点就确实成立，因为此时使用同一密钥多次加密同一消息总会产生相同的结果。这一点足够重要，值得将其表述为一个定理。

$^{2}$ A stateful encryption scheme may, e.g., maintain a counter as part of its state and use that when encrypting. This too could be used to achieve security for multiple encryptions, but we focus on the more common stateless case here.

$^{2}$ 有状态加密方案可以（例如）维护一个计数器作为其状态的一部分，并在加密时使用它。这也可以用来实现多重加密的安全性，但我们在这里关注更常见的无状态情形。

THEOREM 3.20 If $\Pi$ is an encryption scheme in which $\mathsf{Enc}$ is a deterministic function of the key and the message, then $\Pi$ cannot have indistinguishable multiple encryptions in the presence of an eavesdropper.

定理 3.20 如果 $\Pi$ 是一个加密方案，其中 $\mathsf{Enc}$ 是密钥和消息的一个确定性函数，那么 $\Pi$ 不可能在窃听者存在的情况下具有不可区分多重加密。

This should not be interpreted to mean that Definition 3.18 is too strong. Indeed, leaking to an eavesdropper the fact that two encrypted messages are the same can be a significant security breach. (Consider, e.g., a scenario in which someone encrypts a series of yes/no answers!)

这不应被解释为定义 3.18 太强。事实上，向窃听者泄露两个加密消息相同这一事实可能是一个重大的安全漏洞。（例如，考虑某人加密一系列是/否答案的场景！）

To construct a scheme secure for encrypting multiple messages, we must design a scheme in which encryption is randomized, so that when the same message is encrypted multiple times different ciphertexts can be produced. This may seem impossible since decryption must always be able to recover the message. However, we will soon see how to achieve it.

为了构造对于加密多条消息安全的方案，我们必须设计一个加密过程是随机的方案，使得当同一消息被加密多次时可以产生不同的密文。这看起来似乎不可能，因为解密必须始终能够恢复消息。然而，我们很快将看到如何实现这一点。

While achieving security for the encryption of multiple messages is important, we do not extensively consider Definition 3.18 itself but instead focus on the stronger definition that we introduce in the following section.

虽然实现多条消息加密的安全性很重要，但我们并不深入讨论定义 3.18 本身，而是专注于下一节中引入的更强定义。

### 3.4.2 Chosen-Plaintext Attacks and CPA-Security　3.4.2 选择明文攻击与 CPA 安全性

Chosen-plaintext attacks capture the ability of an adversary to exercise (partial) control over what the honest parties encrypt. Imagine a scenario in which two honest parties share a key $k$, and the attacker can influence those parties to encrypt messages $m_1, m_2, \ldots$ (using $k$) and send the resulting ciphertexts over a channel that the attacker can observe. At some later point in time, the attacker observes a ciphertext corresponding to some unknown message m encrypted using the same key k; let us even assume that the attacker knows that m is one of two possibilities $m_0, m_1$. Security against chosen-plaintext attacks means that even in this case the attacker cannot tell which of those two messages was encrypted with probability significantly better than random guessing. (For now we revert back to the case where the eavesdropper is given only a single encryption of an unknown message. Shortly, we will return to consideration of the multiple-message case.)

选择明文攻击刻画了敌手对诚实方加密内容进行（部分）控制的能力。设想一个场景，其中两个诚实方共享密钥 $k$，攻击者可以影响这些方使用 $k$ 加密消息 $m_1, m_2, \ldots$，并将生成的密文通过攻击者可观察的通道发送出去。在稍后的某个时间点，攻击者观察到一个对应于使用同一密钥 $k$ 加密的未知消息 $m$ 的密文；我们甚至假设攻击者知道 m 是两种可能性 $m_0, m_1$ 之一。抵抗选择明文攻击的安全性意味着，即使在这种情况下，攻击者也不能以显著优于随机猜测的概率判断这两个消息中哪一个被加密了。（现在我们回到窃听者仅被给予一个未知消息的单个加密的情况。稍后我们将回到对多消息情况的考虑。）

Chosen-plaintext attacks in the real world. Are chosen-plaintext attacks a realistic concern? For starters, note that chosen-plaintext attacks also encompass known-plaintext attacks—in which the attacker knows some of the messages being encrypted, even if it does not get to choose them—as a special case. Moreover, there are several real-world scenarios in which an adversary might have significant influence over what messages get encrypted. A simple example is given by an attacker typing on a terminal, which in turn encrypts everything the adversary types using a key (unknown to the attacker) shared with a remote server. Here the attacker exactly controls what gets encrypted, and the encryption scheme should still reveal nothing when it is used—with the same key—to encrypt data typed by another user.

现实世界中的选择明文攻击。选择明文攻击是现实问题吗？首先，注意选择明文攻击也把已知明文攻击——即攻击者知道某些被加密的消息、但并不能选择它们——作为特例包含在内。此外，在现实世界中有几种场景，敌手可能对哪些消息被加密有重大影响。一个简单的例子是攻击者在终端上打字，终端反过来使用与远程服务器共享的密钥（攻击者未知）加密攻击者输入的所有内容。在这里，攻击者精确控制着什么被加密，而加密方案在使用同一密钥加密另一用户输入的数据时仍不应泄露任何信息。

Interestingly, chosen-plaintext attacks have also been used successfully as part of historical efforts to break military encryption schemes. For example, during World War II the British placed mines at certain locations, knowing that the Germans—when finding those mines—would encrypt the locations and send them back to headquarters. Those encrypted messages were used by cryptanalysts at Bletchley Park to break the German encryption scheme.

有趣的是，选择明文攻击也曾在历史上破解军事加密方案的行动中得到成功运用。例如，在第二次世界大战期间，英国人在某些地点放置水雷，他们知道德国人在发现这些水雷时会加密这些位置并发送回总部。这些加密消息被布莱切利园的密码分析者用来破解德国的加密方案。

Another example is given by the famous story involving the Battle of Midway. In May 1942, US Navy cryptanalysts intercepted an encrypted message from the Japanese that they were able to partially decode. The result indicated that the Japanese were planning an attack on AF, where AF was a ciphertext fragment that the US was unable to decode. For other reasons, the US believed that Midway Island was the target. Unfortunately, their attempts to convince planners in Washington that this was the case were futile; the general belief was that Midway could not possibly be the target. The Navy cryptanalysts devised the following plan: They instructed US forces at Midway to send a fake message that their freshwater supplies were low. The Japanese intercepted this message and immediately sent an encrypted message to their superiors that "AF is low on water." The Navy cryptanalysts now had their proof that AF corresponded to Midway, and the US dispatched three aircraft carriers to that location. The result was that Midway was saved, and the Japanese incurred significant losses. This battle was a turning point in the war between the US and Japan in the Pacific.

另一个例子是涉及中途岛战役的著名故事。1942 年 5 月，美国海军密码分析者截获了一条来自日本的加密消息，他们能够部分解码。结果表明日本人正在计划攻击 AF，其中 AF 是一个美国无法解码的密文片段。基于其他原因，美国认为中途岛是目标。不幸的是，他们试图说服华盛顿的决策者相信这一点的努力是徒劳的；普遍的看法是中途岛不可能是目标。海军密码分析者设计了以下计划：他们指示中途岛的美军发送一条虚假消息，声称他们的淡水供应不足。日本人截获了这条消息，并立即向其上级发送了一条加密消息，说“AF 缺水”。海军密码分析者现在有了 AF 对应于中途岛的证据，美国派遣了三艘航空母舰到该位置。结果是中途岛得救，而日本人遭受了重大损失。这场战役是美日太平洋战争的转折点。

The Navy cryptanalysts here carried out a chosen-plaintext attack, as they were able to influence the Japanese (albeit in a roundabout way) to encrypt the word "Midway." If the Japanese encryption scheme had been secure against chosen-plaintext attacks, this strategy by the US cryptanalysts would not have worked (and history may have turned out very differently)!

这里的海军密码分析者实施了一次选择明文攻击，因为他们能够影响日本人（尽管是以一种迂回的方式）加密“中途岛”这个词。如果日本的加密方案能够抵抗选择明文攻击，美国密码分析者的这一策略就不会奏效（历史可能会变得截然不同）！

CPA-security. In the formal definition we model chosen-plaintext attacks by giving the adversary $\mathcal{A}$ access to an encryption oracle, viewed as a "black box" that encrypts messages of $\mathcal{A}$'s choice using a key $k$ that is unknown to $\mathcal{A}$. That is, we imagine $\mathcal{A}$ has access to an "oracle" $\mathsf{Enc}_k(\cdot)$; when $\mathcal{A}$ queries this oracle by providing it with a message $m$ as input, the oracle returns a ciphertext $c \leftarrow \mathsf{Enc}_k(m)$ as the reply. (If $\mathsf{Enc}$ is randomized, the oracle uses fresh randomness each time it answers a query.) The adversary can interact with the encryption oracle adaptively, as many times as it likes.

CPA 安全性。在形式化定义中，我们通过给予敌手 $\mathcal{A}$ 访问加密预言机的权限来建模选择明文攻击，该预言机被视为一个“黑盒”，使用 $\mathcal{A}$ 未知的密钥 $k$ 来加密 $\mathcal{A}$ 选择的消息。也就是说，我们设想 $\mathcal{A}$ 可以访问一个“预言机” $\mathsf{Enc}_k(\cdot)$；当 $\mathcal{A}$ 通过向该预言机提供消息 $m$ 作为输入来查询时，预言机返回密文 $c \leftarrow \mathsf{Enc}_k(m)$ 作为回复。（如果 $\mathsf{Enc}$ 是随机化的，预言机在每次回答查询时使用新的随机性。）敌手可以自适应地、任意多次地与加密预言机交互。

Consider the following experiment defined for any encryption scheme $\Pi = (\mathsf{Gen}, \mathsf{Enc}, \mathsf{Dec})$, adversary $\mathcal{A}$, and value n for the security parameter:

考虑以下为任意加密方案 $\Pi = (\mathsf{Gen}, \mathsf{Enc}, \mathsf{Dec})$、敌手 $\mathcal{A}$ 和安全参数值 n 定义的实验：

The CPA indistinguishability experiment $\mathsf{PrivK}_{\mathcal{A},\Pi}^{\mathsf{cpa}}(n)$:

CPA 不可区分性实验 $\mathsf{PrivK}_{\mathcal{A},\Pi}^{\mathsf{cpa}}(n)$：

1. A key $k$ is generated by running $\mathsf{Gen}(1^{n})$.

   通过运行 $\mathsf{Gen}(1^{n})$ 生成密钥 $k$。

2. The adversary A is given input ${1}^n$ and oracle access to $\mathsf{Enc}_k(\cdot)$ and outputs a pair of messages $m_0, m_1$ of the same length.

   敌手 $\mathcal{A}$ 获得输入 ${1}^n$ 以及对 $\mathsf{Enc}_k(\cdot)$ 的预言机访问权限，并输出一对等长的消息 $m_0, m_1$。

3. A uniform bit $b \in \{0,1\}$ is chosen, and then a ciphertext $c \leftarrow \mathsf{Enc}_k(m_b)$ is computed and given to $\mathcal{A}$.

   选择一个均匀比特 $b \in \{0,1\}$，然后计算密文 $c \leftarrow \mathsf{Enc}_k(m_b)$ 并交给 $\mathcal{A}$。

4. The adversary A continues to have oracle access to $\mathsf{Enc}_k(\cdot)$, and outputs a bit $b^{\prime}$.

   敌手 $\mathcal{A}$ 继续拥有对 $\mathsf{Enc}_k(\cdot)$ 的预言机访问权限，并输出一个比特 $b^{\prime}$。

5. The output of the experiment is defined to be 1 if $b^{\prime} = b$, and 0 otherwise. In the former case, we say that A succeeds.

   实验的输出定义为：如果 $b^{\prime} = b$ 则为 1，否则为 0。在前一种情况下，我们说 $\mathcal{A}$ 成功。

DEFINITION 3.21 A private-key encryption scheme $\Pi = (\mathsf{Gen}, \mathsf{Enc}, \mathsf{Dec})$ has indistinguishable encryptions under a chosen-plaintext attack, or is CPA-secure, if for all probabilistic polynomial-time adversaries $\mathcal{A}$ there is a negligible function $\mathsf{negl}$ such that

定义 3.21 私钥加密方案 $\Pi = (\mathsf{Gen}, \mathsf{Enc}, \mathsf{Dec})$ 在**选择明文攻击下具有不可区分加密**，或者是 **CPA 安全**的，如果对于所有概率多项式时间敌手 $\mathcal{A}$，存在一个可忽略函数 $\mathsf{negl}$，使得

$$
\Pr\left[\mathsf{PrivK}_{\mathcal{A},\Pi}^{\mathsf{cpa}}(n)=1\right]\leq\frac{1}{2}+\mathsf{negl}(n),
$$

where the probability is taken over the randomness used by $\mathcal{A}$, as well as the randomness used in the experiment.

其中概率是在 $\mathcal{A}$ 使用的随机性以及实验中使用的随机性上计算的。

CPA-security is nowadays the minimal notion of security an encryption scheme should satisfy, though it is becoming more common to require even stronger security notions that we will discuss in Chapter 5.

CPA 安全如今是加密方案应该满足的最基本安全性概念，尽管要求更强的安全性概念（我们将在第 5 章讨论）正变得越来越常见。

### 3.4.3 CPA-Security for Multiple Encryptions　3.4.3 多重加密的 CPA 安全性

Definition 3.21 can be extended to the case of multiple encryptions in the same way that Definition 3.8 is extended to give Definition 3.18, i.e., by using lists of plaintexts. Here, we take a different approach that is somewhat simpler and has the advantage of modeling attackers that can adaptively choose pairs of plaintexts to be encrypted. Specifically, we now give the attacker access to a "left-or-right" oracle $\mathsf{LR}_{k,b}$ that, on input a pair of equal-length messages $m_0, m_1$, computes the ciphertext $c \leftarrow \mathsf{Enc}_k(m_b)$ and returns $c$. That is, if $b = 0$ then the adversary always receives an encryption of the "left" plaintext, and if $b = 1$ then it always receives an encryption of the "right" plaintext. The bit $b$ is a uniform bit chosen at the beginning of the experiment, and as in previous definitions the goal of the attacker is to guess $b$.

定义 3.21 可以扩展到多重加密的情况，就像定义 3.8 被扩展为定义 3.18 那样，即使用明文列表。在此，我们采用一种不同的方法，它稍微简单一些，并具有对能够自适应选择要加密的明文对的攻击者进行建模的优点。具体来说，我们现在给予攻击者访问“左右”（left-or-right）预言机 $\mathsf{LR}_{k,b}$ 的权限，该预言机在输入一对等长消息 $m_0, m_1$ 时，计算密文 $c \leftarrow \mathsf{Enc}_k(m_b)$ 并返回 $c$。也就是说，如果 $b = 0$，则敌手总是收到“左”明文的加密；如果 $b = 1$，则总是收到“右”明文的加密。比特 $b$ 是在实验开始时选择的均匀比特，并且与之前的定义一样，攻击者的目标是猜测 $b$。

Consider the following experiment defined for any encryption scheme $\Pi = (\mathsf{Gen}, \mathsf{Enc}, \mathsf{Dec})$, adversary $\mathcal{A}$, and value $n$ for the security parameter:

考虑以下为任意加密方案 $\Pi = (\mathsf{Gen}, \mathsf{Enc}, \mathsf{Dec})$、敌手 $\mathcal{A}$ 和安全参数值 $n$ 定义的实验：

The LR-oracle experiment $\mathsf{PrivK}_{\mathcal{A},\Pi}^{\mathsf{LR-cpa}}(n)$:

LR-预言机实验 $\mathsf{PrivK}_{\mathcal{A},\Pi}^{\mathsf{LR-cpa}}(n)$：

1. A key $k$ is generated by running $\mathsf{Gen}(1^{n})$.

   通过运行 $\mathsf{Gen}(1^{n})$ 生成密钥 $k$。

2. A uniform bit $b \in \{0,1\}$ is chosen.

   选择一个均匀比特 $b \in \{0,1\}$。

3. The adversary $\mathcal{A}$ is given input ${1}^n$ and oracle access to $\mathsf{LR}_{k,b}(\cdot,\cdot)$, as defined above.

   敌手 $\mathcal{A}$ 获得输入 ${1}^n$ 以及对如上定义的 $\mathsf{LR}_{k,b}(\cdot,\cdot)$ 的预言机访问权限。

4. The adversary A outputs a bit b'.

   敌手 $\mathcal{A}$ 输出一个比特 $b'$。

5. The output of the experiment is defined to be 1 if $b^{\prime} = b$, and 0 otherwise. In the former case, we say that A succeeds.

   实验的输出定义为：如果 $b^{\prime} = b$ 则为 1，否则为 0。在前一种情况下，我们说 $\mathcal{A}$ 成功。

DEFINITION 3.22 Private-key encryption scheme $\Pi$ has indistinguishable multiple encryptions under a chosen-plaintext attack, or is CPA-secure for multiple encryptions, if for all probabilistic polynomial-time adversaries A there is a negligible function $\mathsf{negl}$ such that

定义 3.22 私钥加密方案 $\Pi$ 在**选择明文攻击下具有不可区分多重加密**，或者对于多重加密是 **CPA 安全**的，如果对于所有概率多项式时间敌手 A，存在一个可忽略函数 $\mathsf{negl}$，使得

$$
\Pr\left[\mathsf{PrivK}_{\mathcal{A},\Pi}^{\mathsf{LR-cpa}}(n)=1\right]\leq\frac{1}{2}+\mathsf{negl}(n),
$$

where the probability is taken over the randomness used by $\mathcal{A}$ and the randomness used in the experiment.

其中概率是在 $\mathcal{A}$ 使用的随机性以及实验中使用的随机性上计算的。

Note that an attacker given access to $\mathsf{LR}_{k,b}$ can simulate access to an encryption oracle: to obtain the encryption of a message $m$, the attacker simply queries $\mathsf{LR}_{k,b}(m, m)$. Given this observation, it is immediate that if $\Pi$ is CPA-secure for multiple encryptions then it is also CPA-secure. It should also be clear that if $\Pi$ is CPA-secure for multiple encryptions then it has indistinguishable multiple encryptions in the presence of an eavesdropper. In other words, Definition 3.22 is at least as strong as Definitions 3.18 and 3.21.

注意，获得 $\mathsf{LR}_{k,b}$ 访问权限的攻击者可以模拟对加密预言机的访问：要获得消息 $m$ 的加密，攻击者只需查询 $\mathsf{LR}_{k,b}(m, m)$。基于这一观察，立即可得：如果 $\Pi$ 对于多重加密是 CPA 安全的，那么它也是 CPA 安全的。同样清楚的是，如果 $\Pi$ 对于多重加密是 CPA 安全的，那么它在窃听者存在的情况下具有不可区分多重加密。换句话说，定义 3.22 至少与定义 3.18 和 3.21 一样强。

It turns out that CPA-security is equivalent to CPA-security for multiple encryptions. (This stands in contrast to the case of eavesdropping adversaries; cf. Proposition 3.19.) We state the following without proof; an analogous result in the public-key setting is proved in Section 12.2.2.

结果证明，CPA 安全与多重加密的 CPA 安全是等价的。（这与窃听者敌手的情况形成对比；参见命题 3.19。）我们不加证明地陈述如下；公钥设定中的类似结果将在 12.2.2 节中证明。

THEOREM 3.23 Any private-key encryption scheme that is CPA-secure is also CPA-secure for multiple encryptions.

定理 3.23 任何 CPA 安全的私钥加密方案对于多重加密也是 CPA 安全的。

Thus, it suffices to prove that a scheme is CPA-secure (for a single encryption), and we may then conclude that it is CPA-secure for multiple encryptions as well.

因此，只需证明一个方案是 CPA 安全的（对于单个加密），我们就可以得出结论：它对于多重加密也是 CPA 安全的。

Fixed-length vs. arbitrary-length messages. An advantage of working with the notion of CPA-security for multiple messages (or, equivalently, CPA-security) is that it allows us to treat fixed-length encryption schemes without loss of generality. In particular, given any CPA-secure fixed-length encryption scheme $\Pi = (\mathsf{Gen}, \mathsf{Enc}, \mathsf{Dec})$, it is possible to construct a CPA-secure encryption scheme $\Pi^{\prime} = (\mathsf{Gen}^{\prime}, \mathsf{Enc}^{\prime}, \mathsf{Dec}^{\prime})$ for arbitrary-length messages quite easily. For simplicity, say $\Pi$ encrypts messages that are 1-bit long. Leave $\mathsf{Gen}^{\prime}$ the same as $\mathsf{Gen}$. Define $\mathsf{Enc}_k^{\prime}$ for any message $m$ (having some arbitrary length $\ell$) as $\mathsf{Enc}_k^{\prime}(m) = \mathsf{Enc}_{k}(m_1), \ldots, \mathsf{Enc}_{k}(m_\ell)$, where $m_i$ denotes the $i$th bit of $m$. Decryption is done in the natural way. It follows from Theorem 3.23 that if $\Pi$ is CPA-secure then so is $\Pi^{\prime}$.

定长与任意长度消息。使用多重消息 CPA 安全（或等价地，CPA 安全）概念的一个优点是，它允许我们处理定长加密方案而不失一般性。特别地，给定任何 CPA 安全的定长加密方案 $\Pi = (\mathsf{Gen}, \mathsf{Enc}, \mathsf{Dec})$，可以很容易地构造一个适用于任意长度消息的 CPA 安全加密方案 $\Pi^{\prime} = (\mathsf{Gen}^{\prime}, \mathsf{Enc}^{\prime}, \mathsf{Dec}^{\prime})$。为简单起见，假设 $\Pi$ 加密长度为 1 比特的消息。保持 $\mathsf{Gen}^{\prime}$ 与 $\mathsf{Gen}$ 相同。对于任意消息 $m$（具有某个任意长度 $\ell$），定义 $\mathsf{Enc}_k^{\prime}(m) = \mathsf{Enc}_{k}(m_1), \ldots, \mathsf{Enc}_{k}(m_\ell)$，其中 $m_i$ 表示 $m$ 的第 $i$ 比特。解密以自然的方式进行。由定理 3.23 可知，如果 $\Pi$ 是 CPA 安全的，那么 $\Pi^{\prime}$ 也是 CPA 安全的。

There are more efficient ways to encrypt messages of arbitrary length than by adapting a fixed-length encryption scheme in this manner. We explore this further in Section 3.6.

有比以这种方式改造定长加密方案更高效的方法来加密任意长度的消息。我们将在 3.6 节进一步探讨这一点。
