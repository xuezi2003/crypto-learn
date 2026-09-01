## 12.5 RSA-Based Encryption　基于 RSA 的加密

In this section we turn our attention to encryption schemes based on the RSA assumption defined in Section 9.2.4. We remark that although RSA-based encryption is still in use, there is currently a gradual shift away from using RSA—and toward using CDH/DDH-based cryptosystems relying on elliptic-curve groups—because of the longer key lengths required for RSA-based schemes. We refer to Section 10.4 for further discussion.

本节把注意力转向基于 9.2.4 节所定义 RSA 假设的加密方案。需要指出的是，尽管基于 RSA 的加密仍在使用，但由于此类方案需要更长的密钥长度，目前人们正逐渐从 RSA 转向基于椭圆曲线群的 CDH/DDH 密码体制。进一步讨论见 10.4 节。

### 12.5.1 Plain RSA Encryption　朴素 RSA 加密

We begin by describing a simple encryption scheme based on the RSA problem. Although the scheme is insecure, it provides a useful starting point for the secure schemes that follow.

我们首先描述一个基于 RSA 问题的简单加密方案。虽然这个方案并不安全，但它为随后给出的安全方案提供了有益的出发点。

Let GenRSA be a PPT algorithm that, on input $1^n$, outputs a modulus $N$ that is the product of two $n$-bit primes, along with integers $e,d$ satisfying $ed=1 \bmod \phi(N)$. (As usual, the algorithm may fail with negligible probability but we ignore that here.) Recall from Section 9.2.4 that such an algorithm can be easily constructed from any algorithm GenModulus that outputs a composite modulus $N$ along with its factorization; see Algorithm 12.25.

设 $\mathsf{GenRSA}$ 是一个 PPT 算法，以 $1^n$ 为输入，输出一个模数 $N$（它是两个 $n$ 比特素数的乘积）以及满足 $ed=1 \bmod \phi(N)$ 的整数 $e,d$。（与往常一样，该算法可能以可忽略的概率失败，这里我们忽略这一点。）回顾 9.2.4 节，这样的算法可以很容易地由任意一个输出合数模数 $N$ 及其因子分解的算法 GenModulus 构造出来；见算法 12.25。

ALGORITHM 12.25
RSA key generation GenRSA

Input: Security parameter $1^{n}$
Output: N, e, d as described in the text
$(N, p, q) \leftarrow \mathsf{GenModulus}(1^{n})$
$\phi(N) := (p - 1) \cdot (q - 1)$
choose $e > 1$ such that $\gcd(e, \phi(N)) = 1$
compute $d := [e^{-1} \bmod \phi(N)]$
return $N, e, d$

算法 12.25
RSA 密钥生成 $\mathsf{GenRSA}$

输入：安全参数 $1^{n}$
输出：如正文所述的 N, e, d
$(N, p, q) \leftarrow \mathsf{GenModulus}(1^{n})$
$\phi(N) := (p - 1) \cdot (q - 1)$
选择满足 $\gcd(e, \phi(N)) = 1$ 的 $e > 1$
计算 $d := [e^{-1} \bmod \phi(N)]$
返回 $N, e, d$

Let $N, e, d$ be as above, and let $c = m^e \bmod N$ for some $m \in \mathbb{Z}_N^*$. RSA encryption relies on the fact that someone who knows $d$ can recover $m$ from $c$ by computing $[c^d \bmod N]$; this works because

设 $N, e, d$ 如上所述，并对某个 $m \in \mathbb{Z}_N^*$ 令 $c = m^e \bmod N$。RSA 加密所依据的事实是：知道 $d$ 的人可以通过计算 $[c^d \bmod N]$ 从 $c$ 恢复出 $m$；这之所以可行，是因为

$$
c^{d}=(m^{e})^{d}=m^{e d}=m\bmod N,
$$

as discussed in Section 9.2.4. On the other hand, without knowledge of $d$—even if $N$ and $e$ are known—the RSA assumption (cf. Definition 9.46) implies that it is difficult to recover $m$ from $c$, at least if $m$ is chosen uniformly from $\mathbb{Z}_N^*$. This naturally suggests the public-key encryption scheme shown as Construction 12.26: The receiver runs $\mathsf{GenRSA}$ to obtain $N, e, d$; it publishes $N$ and $e$ as its public key, and keeps $d$ in its private key. To encrypt a message $m \in \mathbb{Z}_N^*$, a sender computes the ciphertext $c := [m^e \bmod N]$. As we have just noted, the receiver—who knows $d$—can decrypt $c$ and recover $m$.

如 9.2.4 节所讨论的。另一方面，在不知道 $d$ 的情况下——即使知道 $N$ 和 $e$——RSA 假设（参见定义 9.46）意味着从 $c$ 恢复 $m$ 是困难的，至少当 $m$ 从 $\mathbb{Z}_N^*$ 中均匀选取时是如此。这自然而然地引出构造 12.26 所示的公钥加密方案：接收方运行 $\mathsf{GenRSA}$ 得到 $N, e, d$，将 $N$ 和 $e$ 作为公钥公布，并把 $d$ 保存在私钥中。要加密消息 $m \in \mathbb{Z}_N^*$，发送方计算密文 $c := [m^e \bmod N]$。正如刚才所述，知道 $d$ 的接收方可以解密 $c$ 并恢复出 $m$。

**CONSTRUCTION 12.26**

**构造 12.26**

Let GenRSA be as in the text. Define a public-key encryption scheme as follows:

设 $\mathsf{GenRSA}$ 如正文所述。如下定义一个公钥加密方案：

- Gen: on input $1^{n}$ run $\mathsf{GenRSA}(1^{n})$ to obtain $N, e$, and $d$. The public key is $\langle N, e \rangle$ and the private key is $\langle N, d \rangle$.

- Gen：以 $1^{n}$ 为输入，运行 $\mathsf{GenRSA}(1^{n})$ 得到 $N, e$ 和 $d$。公钥为 $\langle N, e \rangle$，私钥为 $\langle N, d \rangle$。

- Enc: on input a public key $pk = \langle N, e \rangle$ and a message $m \in \mathbb{Z}_N^*$, compute the ciphertext

- Enc：以公钥 $pk = \langle N, e \rangle$ 和消息 $m \in \mathbb{Z}_N^*$ 为输入，计算密文

$$
c:=[m^{e}\bmod N].
$$

- Dec: on input a private key $sk = \langle N, d \rangle$ and a ciphertext $c \in \mathbb{Z}_N^*$, compute the message

- Dec：以私钥 $sk = \langle N, d \rangle$ 和密文 $c \in \mathbb{Z}_N^*$ 为输入，计算消息

$$
m:=[c^{d}\bmod N].
$$


**The plain RSA encryption scheme.**

**朴素 RSA 加密方案。**


The following gives a worked example of the above (see also Example 9.49).

下面给出上述方案的一个具体算例（另见例 9.49）。

**Example 12.27**

**例 12.27**

Say GenRSA outputs $(N, e, d) = (391, 3, 235)$. (Note that $391 = 17 \cdot 23$ and so $\phi(391) = 16 \cdot 22 = 352$. Moreover, $3 \cdot 235 = 1 \bmod 352$.) So the public key is $\langle 391, 3 \rangle$ and the private key is $\langle 391, 235 \rangle$.

设 $\mathsf{GenRSA}$ 输出 $(N, e, d) = (391, 3, 235)$。（注意 $391 = 17 \cdot 23$，所以 $\phi(391) = 16 \cdot 22 = 352$；而且 $3 \cdot 235 = 1 \bmod 352$。）于是公钥为 $\langle 391, 3 \rangle$，私钥为 $\langle 391, 235 \rangle$。

To encrypt the message $m = 158 \in \mathbb{Z}_{391}^*$ using the public key $(391,3)$, we simply compute $c := [158^3 \bmod 391] = 295$; this is the ciphertext. To decrypt, the receiver computes $[295^{235} \bmod 391] = 158$.

要用公钥 $(391,3)$ 加密消息 $m = 158 \in \mathbb{Z}_{391}^*$，只需计算 $c := [158^3 \bmod 391] = 295$，这就是密文。解密时，接收方计算 $[295^{235} \bmod 391] = 158$。

Is the plain RSA encryption scheme secure? The factoring assumption implies that it is computationally infeasible for an attacker who is given the public key to derive the corresponding private key; see Section 9.2.5. This is necessary—but not sufficient—for a public-key encryption scheme to be secure. The RSA assumption implies that if the message $m$ is chosen uniformly from $\mathbb{Z}_N^*$ then an eavesdropper given $N$, $e$, and $c$ (namely, the public key and the ciphertext) cannot recover $m$ in its entirety. But these are weak guarantees, and fall short of the level of security we want. In particular, they leave open the possibility that an attacker can recover the message when it is not chosen uniformly from $\mathbb{Z}_N^*$—and, indeed, when $m$ is chosen from a small range it is easy to see that an attacker can compute $m$ from the public key and ciphertext. In addition, it does not rule out the possibility that an attacker can learn partial information about the message, even when it is uniform. (In fact, this is known to be possible.) Moreover, plain RSA encryption is deterministic and so cannot be CPA-secure, as we have discussed in Section 12.2.1.

朴素 RSA 加密方案安全吗？因子分解假设意味着：给定公钥的攻击者在计算上无法推出对应的私钥（见 9.2.5 节）。这是公钥加密方案安全的必要条件——但并非充分条件。RSA 假设意味着：如果消息 $m$ 从 $\mathbb{Z}_N^*$ 中均匀选取，那么窃听者即使拿到 $N$、$e$ 和 $c$（即公钥与密文）也无法完整恢复 $m$。但这些都是较弱的保证，达不到我们想要的安全级别。特别地，它们并不排除攻击者在消息并非均匀取自 $\mathbb{Z}_N^*$ 时恢复消息的可能——事实上，当 $m$ 取自很小的取值范围时，容易看出攻击者能从公钥和密文算出 $m$。此外，即便消息是均匀选取的，这也不排除攻击者获知消息部分信息的可能（事实上，已知这是做得到的）。再者，朴素 RSA 加密是确定性的，因此如 12.2.1 节所讨论的，它不可能是选择明文安全（CPA）的。

### More Attacks on Plain RSA　对朴素 RSA 的更多攻击

We have already noted that plain RSA encryption is not CPA-secure. Nevertheless, there may be a temptation to use plain RSA for encrypting “random messages” and/or in situations where leaking a few bits of information about the message is acceptable. We warn against this in general, and provide here a few examples of what can go wrong. (Some of the attacks assume $e = 3$. In several cases the attacks can be extended, at least partially, to larger $e$; in any case, as noted in Section 9.2.4,
 setting $e = 3$ is often done in practice. The attacks should be taken as demonstrating that Construction 12.26 is inadequate, not as indicating that using $e = 3$ is a bad choice in general.)

我们已经指出，朴素 RSA 加密不是选择明文安全的。尽管如此，人们可能仍会想用朴素 RSA 来加密“随机消息”，或用在泄露消息的少量比特尚可接受的场合。我们总体上反对这种做法，并在此给出几个可能出问题的例子。（其中一些攻击假设 $e = 3$。在若干情形下，这些攻击至少可以部分地推广到更大的 $e$；无论如何，正如 9.2.4 节所指出的，实践中常常取 $e = 3$。应当把这些攻击看作表明构造 12.26 并不合用，而不是说取 $e = 3$ 总体上是个糟糕的选择。）

**A quadratic improvement in recovering $m$.**

**恢复 $m$ 的平方根级加速。**

Since plain RSA encryption is deterministic, if an attacker knows that $m < B$ then the attacker can determine $m$ from the ciphertext $c = [m^e \bmod N]$ in time $\mathcal{O}(B)$ using the brute-force attack discussed in Section 12.2.1. One might hope, however, that plain RSA encryption can be used if $B$ is large, i.e., if the message is chosen from a reasonably large set of values. One possible scenario where this might occur is in the context of hybrid encryption (cf. Section 12.3), where the “message” is a uniform $n$-bit key and so $B = 2^n$. Unfortunately, there is a clever attack that recovers $m$, with high probability, in time roughly $\mathcal{O}(\sqrt{B})$. This can make a significant difference in practice: a $2^{80}$-time attack (say) is infeasible, but an attack running in time $2^{40}$ is relatively easy to carry out.

由于朴素 RSA 加密是确定性的，如果攻击者知道 $m < B$，就可以用 12.2.1 节讨论的穷举攻击，在 $\mathcal{O}(B)$ 时间内从密文 $c = [m^e \bmod N]$ 确定 $m$。不过人们或许希望，只要 $B$ 较大——即消息取自一个相当大的取值集合——就仍然可以使用朴素 RSA 加密。一个可能出现这种情形的场景是混合加密（参见 12.3 节）：此时“消息”是一个均匀的 $n$ 比特密钥，于是 $B = 2^n$。不幸的是，有一种巧妙的攻击能以高概率在大约 $\mathcal{O}(\sqrt{B})$ 的时间内恢复 $m$。这在实践中会造成显著差别：例如，$2^{80}$ 量级的攻击是不可行的，但运行时间为 $2^{40}$ 的攻击实施起来相对容易。

A description of the attack is given as Algorithm 12.28. In our description, we assume $B = 2^n$ and let $\alpha \in (\frac{1}{2}, 1)$ denote some fixed constant (see below). Binary search is used in the second-to-last line to check whether there exists an $r$ with $x_r = [s^e \bmod N]$. The time for the attack is dominated by the time to perform $2T = \mathcal{O}(2^{\alpha n})$ exponentiations.

该攻击的描述见算法 12.28。在我们的描述中，假设 $B = 2^n$，并用 $\alpha \in (\frac{1}{2}, 1)$ 表示某个固定常数（见下文）。倒数第二行用二分搜索检查是否存在满足 $x_r = [s^e \bmod N]$ 的 $r$。该攻击的时间主要取决于执行 $2T = \mathcal{O}(2^{\alpha n})$ 次幂运算所需的时间。

ALGORITHM 12.28
An attack on plain RSA encryption

Input: Public key $\langle N, e \rangle$; ciphertext $c$; bound $2^n$
Output: $m < 2^n$ such that $m^e = c \bmod N$

set $T := 2^{\alpha n}$

for $r = 1$ to $T$:
 $x_r := [c/r^e \bmod N]$

sort the pairs $\{(r, x_r)\}_{r=1}^T$ by their second component
for $s = 1$ to $T$:
    if $[s^e \bmod N] \stackrel{?}{=} x_r$ for some $r$
        return $[r \cdot s \bmod N]$

算法 12.28
针对朴素 RSA 加密的一种攻击

输入：公钥 $\langle N, e \rangle$；密文 $c$；上界 $2^n$
输出：满足 $m^e = c \bmod N$ 的 $m < 2^n$

令 $T := 2^{\alpha n}$

for $r = 1$ to $T$:
 $x_r := [c/r^e \bmod N]$

将数对 $\{(r, x_r)\}_{r=1}^T$ 按第二分量排序
for $s = 1$ to $T$:
    if 存在某个 $r$ 使 $[s^e \bmod N] \stackrel{?}{=} x_r$
        return $[r \cdot s \bmod N]$

We now sketch why the attack recovers $m$ with high probability. Let $c = m^e \bmod N$. For appropriate choice of $\alpha \approx \frac{1}{2}$, it can be shown that if $m$ is a uniform $n$-bit integer then with high probability there exist $r, s$ with $1 < r \leq s \leq 2^{\alpha n}$ for which $m = r \cdot s$. (For example, if $n = 64$ and so $m$ is a uniform 64-bit string, then with probability 0.35 there exist $r, s$ of length at most 34 bits such that $m = r \cdot s$. See the references at the end of the chapter for details.) Assuming this to be the case, the above algorithm finds $m$ since

现在概述该攻击为何能以高概率恢复 $m$。设 $c = m^e \bmod N$。可以证明：当适当选取 $\alpha \approx \frac{1}{2}$ 时，如果 $m$ 是均匀的 $n$ 比特整数，则以高概率存在满足 $1 < r \leq s \leq 2^{\alpha n}$ 的 $r, s$ 使得 $m = r \cdot s$。（例如，若 $n = 64$，从而 $m$ 是均匀的 64 比特串，则以概率 0.35 存在长度至多为 34 比特的 $r, s$ 使得 $m = r \cdot s$。详见本章末的参考文献。）假设情况确实如此，那么上述算法能找到 $m$，因为

$$
c=m^{e}=(r\cdot s)^{e}=r^{e}\cdot s^{e}\bmod N,
$$

and so $x_r = c/r^e = s^e \bmod N$ with $r, s \leq T$.

从而 $x_r = c/r^e = s^e \bmod N$，其中 $r, s \leq T$。

**Encrypting short messages using small $e$.**

**用小 $e$ 加密短消息。**

The previous attack shows how to recover a message $m$ known to be smaller than some bound $B$ in time roughly $\mathcal{O}(\sqrt{B})$. Here we show how to do the same thing in time $\mathsf{poly}(\|N\|)$ if $B \leq N^{1/e}$ (where this means the $e$th root of $N$ as a real number).

前一种攻击展示了如何在大约 $\mathcal{O}(\sqrt{B})$ 的时间内恢复一个已知小于某上界 $B$ 的消息 $m$。这里我们展示：如果 $B \leq N^{1/e}$（这里指 $N$ 作为实数的 $e$ 次方根），就可以在 $\mathsf{poly}(\|N\|)$ 时间内做到同样的事。

The attack relies on the observation that when $m < N^{1/e}$, raising $m$ to the $e$th power modulo $N$ involves no modular reduction; i.e., $[m^e \bmod N]$ is equal to the integer $m^e$. This means that given the ciphertext $c = [m^e \bmod N]$, an attacker can determine $m$ by computing $m := c^{1/e}$ over the integers (i.e., not modulo N); this can be done easily in time $\mathsf{poly}(\|c\|) = \mathsf{poly}(\|N\|)$ since finding $e$th roots is easy over the integers and hard only when working modulo N.

该攻击依据如下观察：当 $m < N^{1/e}$ 时，对 $m$ 做模 $N$ 的 $e$ 次幂不涉及任何取模约简；也就是说，$[m^e \bmod N]$ 就等于整数 $m^e$。这意味着，给定密文 $c = [m^e \bmod N]$，攻击者只需在整数上（即不做模 $N$ 运算）计算 $m := c^{1/e}$ 即可确定 $m$；这可以在 $\mathsf{poly}(\|c\|) = \mathsf{poly}(\|N\|)$ 时间内轻松完成，因为求 $e$ 次方根在整数上是容易的，只有在模 $N$ 下才是困难的。

For small $e$ this represents a serious weakness of plain RSA encryption. For example, if we take $e = 3$ and assume $\|N\| \approx 2048$ bits, then the attack works even when $m$ is a uniform 256-bit string; this once again rules out security of plain RSA even when used as part of a hybrid encryption scheme.

对于较小的 $e$，这构成朴素 RSA 加密的严重弱点。例如，取 $e = 3$ 并设 $\|N\| \approx 2048$ 比特，那么即使 $m$ 是均匀的 256 比特串，该攻击也照样奏效；这再次否定了朴素 RSA 的安全性，哪怕它只是作为混合加密方案的一部分来使用。

**Encrypting a partially known message.**

**加密部分已知的消息。**

This attack assumes a sender who encrypts a message, part of which is known to the adversary (something that should not lead to an attack when using a secure scheme). We rely on a powerful theorem due to Coppersmith that we state without proof:

这种攻击假设发送方加密一条消息，而该消息的一部分为敌手所知（在使用安全的方案时，这本不应导致攻击）。我们依赖 Coppersmith 提出的一个强有力的定理，这里只陈述而不证明：

THEOREM 12.29 Let $p(x)$ be a polynomial of degree $e$. Then in time $\mathsf{poly}(\|N\|, e)$ one can find all $m$ such that $p(m) = 0 \bmod N$ and $|m| \leq N^{1/e}$.

定理 12.29　设 $p(x)$ 是次数为 $e$ 的多项式。那么可以在 $\mathsf{poly}(\|N\|, e)$ 时间内找出所有满足 $p(m) = 0 \bmod N$ 且 $|m| \leq N^{1/e}$ 的 $m$。

Due to the dependence of the running time on $e$, the attack is only practical for small $e$. In what follows we assume $e = 3$ for concreteness.

由于运行时间依赖于 $e$，该攻击只对较小的 $e$ 才实际可行。下文为具体起见，假设 $e = 3$。

Assume a sender encrypts a message $m = m_1 \parallel m_2$, where $m_1$ is known but $m_2$ is not. Say $m_2$ is k bits long, so $m = 2^k \cdot m_1 + m_2$. Given the resulting ciphertext $c = [(m_1 \parallel m_2)^3 \bmod N]$, an eavesdropper can define $p(x) \stackrel{\mathrm{def}}{=} (2^k \cdot m_1 + x)^3 - c$, a cubic polynomial. This polynomial has $m_2$ as a root (modulo $N$), and $|m_2| < 2^k$. Theorem 12.29 thus implies that the attacker can compute $m_2$ efficiently as long as $2^k \leq N^{1/3}$. A similar attack works when $m_2$ is known but $m_1$ is not.

假设发送方加密消息 $m = m_1 \parallel m_2$，其中 $m_1$ 已知而 $m_2$ 未知。设 $m_2$ 长 k 比特，于是 $m = 2^k \cdot m_1 + m_2$。给定所得密文 $c = [(m_1 \parallel m_2)^3 \bmod N]$，窃听者可以定义三次多项式 $p(x) \stackrel{\mathrm{def}}{=} (2^k \cdot m_1 + x)^3 - c$。该多项式以 $m_2$ 为根（模 $N$ 意义下），且 $|m_2| < 2^k$。于是定理 12.29 意味着，只要 $2^k \leq N^{1/3}$，攻击者就能高效地算出 $m_2$。当 $m_2$ 已知而 $m_1$ 未知时，类似的攻击同样有效。

**Encrypting related messages.**³ This attack assumes a sender who encrypts two related messages to the same receiver (something that should not result in an attack when using a secure encryption scheme). Assume the sender encrypts both $m$ and $m+\delta$, where the offset $\delta$ is known but $m$ is not. Given the two ciphertexts $c_1 = [m^e \bmod N]$ and $c_2 = [(m+\delta)^e \bmod N]$, an eavesdropper can define the two polynomials $f_1(x) \overset{\mathrm{def}}{=} x^e - c_1$ and $f_2(x) \overset{\mathrm{def}}{=} (x+\delta)^e - c_2$, each of degree $e$. Note that $x = m$ is a root (modulo $N$) of both polynomials, and so the linear term $(x-m)$ is a factor of both. Thus, if the greatest common divisor of $f_1(x)$ and $f_2(x)$ (modulo $N$) is linear, it will reveal $m$. The greatest common divisor can be computed in time $\mathsf{poly}(\|N\|, e)$ using an algorithm similar to the one in Appendix B.1.2; thus, this attack is feasible for small $e$.

**加密相关的消息。**³ 这种攻击假设发送方向同一接收方加密两条相关的消息（在使用安全的加密方案时，这同样不应导致攻击）。假设发送方加密 $m$ 和 $m+\delta$，其中偏移量 $\delta$ 已知而 $m$ 未知。给定两个密文 $c_1 = [m^e \bmod N]$ 和 $c_2 = [(m+\delta)^e \bmod N]$，窃听者可以定义两个次数均为 $e$ 的多项式 $f_1(x) \overset{\mathrm{def}}{=} x^e - c_1$ 和 $f_2(x) \overset{\mathrm{def}}{=} (x+\delta)^e - c_2$。注意，$x = m$ 同时是这两个多项式的根（模 $N$ 意义下），因此一次式 $(x-m)$ 是两者共同的因子。于是，如果 $f_1(x)$ 与 $f_2(x)$（模 $N$）的最大公因式是一次的，它就会暴露 $m$。该最大公因式可以用与附录 B.1.2 中类似的算法在 $\mathsf{poly}(\|N\|, e)$ 时间内算出；因此，这一攻击对较小的 $e$ 是可行的。

> $^3$ This attack relies on some algebra slightly beyond what we have covered in this book.

> $^3$ 该攻击用到的代数知识略微超出本书范围。

Sending the same message to multiple receivers.⁴ Our final attack assumes a sender who encrypts the same message to multiple receivers (something that, once again, should not result in an attack when using a secure encryption scheme). Let $e = 3$, and say the same message $m$ is encrypted to three different parties holding public keys $pk_1 = \langle N_1, 3 \rangle$, $pk_2 = \langle N_2, 3 \rangle$, and $pk_3 = \langle N_3, 3 \rangle$, respectively. Assume $\gcd(N_i, N_j) = 1$ for distinct $i, j$ (if not, then at least one of the moduli can be factored immediately and the message $m$ can be easily recovered). An eavesdropper sees

向多个接收方发送同一消息。⁴ 我们的最后一种攻击假设发送方向多个接收方加密同一条消息（再说一次，在使用安全的加密方案时，这本不应导致攻击）。令 $e = 3$，并设同一条消息 $m$ 被分别加密给三个不同的参与方，他们持有的公钥依次为 $pk_1 = \langle N_1, 3 \rangle$、$pk_2 = \langle N_2, 3 \rangle$ 和 $pk_3 = \langle N_3, 3 \rangle$。假设对不同的 $i, j$ 都有 $\gcd(N_i, N_j) = 1$（如若不然，则至少有一个模数可以被立即分解，从而很容易恢复消息 $m$）。窃听者看到

$$
c_{1}=[m^{3}\bmod N_{1}],\quad c_{2}=[m^{3}\bmod N_{2}],\quad\text{and}\quad c_{3}=[m^{3}\bmod N_{3}].
$$

Let $N^* = N_1 N_2 N_3$. An extended version of the Chinese remainder theorem says that there exists a unique non-negative integer $\hat{c} < N^*$ such that

令 $N^* = N_1 N_2 N_3$。中国剩余定理的推广形式表明，存在唯一的非负整数 $\hat{c} < N^*$ 满足

$$
\hat{c}=c_{1}\bmod N_{1}
$$

$$
\hat{c}=c_{2}\bmod N_{2}
$$

$$
\hat{c}=c_{3}\bmod N_{3}.
$$

Moreover, using techniques similar to those shown in Section 9.1.5 it is possible to compute $\hat{c}$ efficiently given the public keys and the above ciphertexts. Note finally that $m^3$ satisfies the above equations, and $m^3 < N^*$ since $m < \min\{N_1, N_2, N_3\}$. This means that $\hat{c} = m^3$ over the integers (i.e., with no modular reduction taking place), and so the message $m$ can be recovered by computing the integer cube root of $\hat{c}$.

此外，利用与 9.1.5 节所示类似的技术，给定公钥和上述密文即可高效地算出 $\hat{c}$。最后注意，$m^3$ 满足上述方程组，且由 $m < \min\{N_1, N_2, N_3\}$ 可知 $m^3 < N^*$。这意味着在整数上（即不发生任何取模约简）有 $\hat{c} = m^3$，因此只要计算 $\hat{c}$ 的整数立方根就能恢复消息 $m$。

> $^4$ This attack relies on the Chinese remainder theorem presented in Section 9.1.5.

> $^4$ 该攻击依赖于 9.1.5 节介绍的中国剩余定理。

### 12.5.2 Padded RSA and PKCS #1 v1.5　填充 RSA 与 PKCS #1 v1.5

Although plain RSA is insecure, it does suggest one general approach to public-key encryption based on the RSA problem: to encrypt a message $m$ using public key $\langle N, e \rangle$, first map $m$ to an element $\hat{m} \in \mathbb{Z}_N^*$; then compute the ciphertext $c := [\hat{m}^e \bmod N]$. To decrypt a ciphertext $c$, the receiver computes $\hat{m} := [c^d \bmod N]$ and then recovers the original message $m$. For the receiver to be able to recover the message, the mapping from messages to elements of $\mathbb{Z}_N^*$ must be (efficiently) reversible. For a scheme following this approach to have a hope of being CPA-secure, the mapping must be randomized so encryption is not deterministic. This is, of course, a necessary condition but not a sufficient one, and security of the encryption scheme depends critically on the specific mapping that is used.

尽管朴素 RSA 并不安全，但它确实提示了基于 RSA 问题构造公钥加密的一种一般思路：要用公钥 $\langle N, e \rangle$ 加密消息 $m$，先把 $m$ 映射为元素 $\hat{m} \in \mathbb{Z}_N^*$，再计算密文 $c := [\hat{m}^e \bmod N]$。解密密文 $c$ 时，接收方计算 $\hat{m} := [c^d \bmod N]$，然后恢复原始消息 $m$。为了使接收方能够恢复消息，从消息到 $\mathbb{Z}_N^*$ 元素的映射必须是（高效）可逆的。而遵循这一思路的方案要想有望达到选择明文安全，该映射还必须是随机化的，使加密不再是确定性的。当然，这只是必要条件而非充分条件，加密方案的安全性关键取决于所用的具体映射。

One simple implementation of the above idea is to randomly pad the message before encrypting. That is, to map a message $m$ (viewed as a bit-string) to an element of $\mathbb{Z}_N^*$, the sender chooses a uniform bit-string $r \in \{0,1\}^\ell$ (for some appropriate $\ell$) and sets $\hat{m} := r\|m$; the resulting value can naturally be interpreted as an integer in $\mathbb{Z}_N^*$. (This mapping is clearly reversible.) See Construction 12.30, where the bounds on $\ell(n)$ and the length of $m$ ensure that the integer $\hat{m}$ is less than $N$.

上述思想的一种简单实现是在加密前对消息做随机填充。也就是说，为了把消息 $m$（视为比特串）映射为 $\mathbb{Z}_N^*$ 中的元素，发送方选取均匀的比特串 $r \in \{0,1\}^\ell$（$\ell$ 取某个适当的值），并令 $\hat{m} := r\|m$；所得的值可以自然地解释为 $\mathbb{Z}_N^*$ 中的整数。（该映射显然是可逆的。）见构造 12.30，其中对 $\ell(n)$ 和 $m$ 长度的限制确保整数 $\hat{m}$ 小于 $N$。

**CONSTRUCTION 12.30**

**构造 12.30**

Let GenRSA be as before, and let $\ell$ be a function with $\ell(n) < 2n$. Define a public-key encryption scheme as follows:

设 $\mathsf{GenRSA}$ 如前所述，并设 $\ell$ 是满足 $\ell(n) < 2n$ 的函数。如下定义一个公钥加密方案：

- Gen: on input $1^n$, run $\mathsf{GenRSA}(1^n)$ to obtain $(N, e, d)$. Output the public key $pk = \langle N, e \rangle$, and the private key $sk = \langle N, d \rangle$.

- Gen：以 $1^n$ 为输入，运行 $\mathsf{GenRSA}(1^n)$ 得到 $(N, e, d)$。输出公钥 $pk = \langle N, e \rangle$ 和私钥 $sk = \langle N, d \rangle$。

- Enc: on input a public key $pk = \langle N, e \rangle$ and a message $m \in \{0,1\}^{|N|- \ell(n)-1}$, choose a uniform string $r \in \{0,1\}^{\ell(n)}$ and interpret $\hat{m} := r\|m$ as an element of $\mathbb{Z}_N^*$. Output the ciphertext

- Enc：以公钥 $pk = \langle N, e \rangle$ 和消息 $m \in \{0,1\}^{|N|- \ell(n)-1}$ 为输入，选取均匀串 $r \in \{0,1\}^{\ell(n)}$，并把 $\hat{m} := r\|m$ 解释为 $\mathbb{Z}_N^*$ 中的元素。输出密文

$$
c:=[\hat{m}^{e}\bmod N].
$$

- Dec: on input a private key $sk = \langle N, d \rangle$ and a ciphertext $c \in \mathbb{Z}_N^*$, compute

- Dec：以私钥 $sk = \langle N, d \rangle$ 和密文 $c \in \mathbb{Z}_N^*$ 为输入，计算

$$
\hat{m}:=[c^{d}\bmod N],
$$

and output the $\|N\| - \ell(n) - 1$ least-significant bits of $\hat{m}$.

并输出 $\hat{m}$ 的 $\|N\| - \ell(n) - 1$ 个最低有效位。

The padded RSA encryption scheme.

填充 RSA 加密方案。

The construction is parameterized by a value $\ell$ that determines the length of the random padding used. Security of the scheme depends on $\ell$. There is an obvious brute-force attack on the scheme that runs in time $2^{\ell}$, so if $\ell$ is too short (in particular, if $\ell(n) = \mathcal{O}(\log n)$), the scheme is insecure. At the other extreme, the result we show in the following section shows that when the padding is as large as possible, and $m$ is just a single bit, then it is possible to prove security based on the RSA assumption. In intermediate cases, the situation is less clear: for certain $\ell$ we cannot prove security based on the RSA assumption but no polynomial-time attacks are known either. We defer further discussion until after our treatment of PKCS #1 v1.5 next.

该构造由决定随机填充长度的值 $\ell$ 参数化。方案的安全性取决于 $\ell$。该方案存在一个运行时间为 $2^{\ell}$ 的明显的穷举攻击，因此若 $\ell$ 太短（特别地，若 $\ell(n) = \mathcal{O}(\log n)$），方案就不安全。在另一个极端，下一节给出的结果表明：当填充长度取到尽可能大、而 $m$ 仅为单个比特时，可以基于 RSA 假设证明安全性。介于两者之间的情况则不太明朗：对某些 $\ell$，我们既无法基于 RSA 假设证明安全性，也没有已知的多项式时间攻击。进一步的讨论留待下文介绍完 PKCS #1 v1.5 之后进行。

RSA PKCS #1 v1.5. The RSA Laboratories Public-Key Cryptography Standard (PKCS) #1 version 1.5, issued in 1993, utilizes a variant of padded RSA encryption. For a public key $pk = \langle N, e \rangle$ of the usual form, let $k$ denote the length of $N$ in bytes; i.e., $k$ is the integer satisfying $2^{8(k-1)} \leq N < 2^{8k}$. Messages $m$ to be encrypted are assumed to have length an integer number of bytes ranging from one to $k-11$. Encryption of a D-byte message $m$ is computed as

**RSA PKCS #1 v1.5。**

RSA 实验室的公钥密码学标准（PKCS）#1 的 1.5 版本发布于 1993 年，采用了填充 RSA 加密的一个变体。对于通常形式的公钥 $pk = \langle N, e \rangle$，用 $k$ 表示 $N$ 的字节长度；即 $k$ 是满足 $2^{8(k-1)} \leq N < 2^{8k}$ 的整数。假定待加密消息 $m$ 的长度为整数个字节，范围从 1 到 $k-11$。对 D 字节消息 $m$ 的加密按下式计算：

$$
[\left(\mathtt{0x00}\middle|\mathtt{0x02}\middle|r\middle|\mathtt{0x00}\middle|m\right)^{e}\bmod{N}],
$$

where $r$ is a randomly generated, $(k-D-3)$-byte string with none of its bytes equal to $\mathtt{0x00}$. (This latter condition enables the message to be unambiguously recovered upon decryption.) Note that the maximum allowed length of $m$ ensures that $r$ is at least 8 bytes long.

其中 $r$ 是随机生成的 $(k-D-3)$ 字节串，且其任何字节都不等于 $\mathtt{0x00}$。（后一条件使得解密时能够无歧义地恢复消息。）注意，$m$ 的最大允许长度保证了 $r$ 至少为 8 字节长。

Unfortunately, PKCS #1 v1.5 as specified is not CPA-secure because it allows using random padding that is too short. This is best illustrated by showing that an attacker can determine the initial portion of a message known to have many trailing 0s. For simplicity, say $m = b \| \underbrace{0 \cdots 0}_{L}$ where $b \in \{0,1\}$ is unknown and $m$ is as long as possible (so $L = 8 \cdot (k - 11) - 1$). Encryption of $m$ gives a ciphertext $c$ with

不幸的是，按照标准规定的 PKCS #1 v1.5 并不是选择明文安全的，因为它允许使用过短的随机填充。最能说明这一点的是：攻击者可以确定一条已知带有许多尾部 0 的消息的开头部分。为简单起见，设 $m = b \| \underbrace{0 \cdots 0}_{L}$，其中 $b \in \{0,1\}$ 未知，且 $m$ 取到最长（于是 $L = 8 \cdot (k - 11) - 1$）。加密 $m$ 得到的密文 $c$ 满足

$$
c=(\mathtt{0x00}\|\mathtt{0x02}\|r\|\mathtt{0x00}\|b\|0\cdots0)^{e}\bmod N.
$$

An attacker can compute $c^{\prime} := c/(2^L)^e \bmod N$; note that

攻击者可以计算 $c^{\prime} := c/(2^L)^e \bmod N$；注意

$$
c^{\prime}=\left(\frac{\mathtt{0x00}\|\mathtt{0x02}\|r\|\mathtt{0x00}\|b\|0\cdots0}{10\cdots0}\right)^{e}=(\mathtt{0x02}\|r\|\mathtt{0x00}\|b)^{e}\bmod N.
$$

The integer $\mathtt{0x02}\|r\|\mathtt{0x00}\|b$ is 75 bits long (note that $\mathtt{0x02} = 00000010$, and all the high-order 0-bits don't count), and so an attacker can now apply the “short-message attack,” or the attack based on encrypting a partially known message, from the previous section. To avoid these attacks we need to take $r$ of length at least $\|N\|/e$. Even if $e$ is large, however, the “quadratic-improvement attack” from the previous section shows that $r$ can be recovered, with high probability, in time roughly $2^{\|r\|/2}$.

整数 $\mathtt{0x02}\|r\|\mathtt{0x00}\|b$ 只有 75 比特长（注意 $\mathtt{0x02} = 00000010$，所有高位的 0 比特都不计入长度），因此攻击者现在可以套用上一节的“短消息攻击”，或者基于加密部分已知消息的攻击。要避免这些攻击，需要取 $r$ 的长度至少为 $\|N\|/e$。然而，即使 $e$ 较大，上一节的“平方根级加速攻击”也表明，$r$ 可以以高概率在大约 $2^{\|r\|/2}$ 的时间内被恢复。

If we force $r$ to be roughly half the length of $N$, and correspondingly reduce the maximum message length, then it is reasonable to conjecture that the encryption scheme in PKCS #1 v1.5 is CPA-secure. (We stress, however, that no proof of security based on the RSA assumption is known.) Nevertheless, because of a serious chosen-ciphertext attack on the scheme, described briefly in Section 12.5.5, newer versions of the PKCS #1 standard have been introduced and should be used instead.

如果强制让 $r$ 的长度大约为 $N$ 的一半，并相应缩短消息的最大长度，那么就有较充分的理由猜想 PKCS #1 v1.5 中的加密方案是选择明文安全的。（不过我们强调，目前尚不知道任何基于 RSA 假设的安全性证明。）尽管如此，由于存在针对该方案的一种严重的选择密文攻击（12.5.5 节将简要介绍），人们引入了更新版本的 PKCS #1 标准，应当改用新版本。

### 12.5.3 \*CPA-Secure Encryption without Random Oracles　\*无随机预言机的选择明文安全加密

In this section we show an encryption scheme that can be proven to be CPA-secure based on the RSA assumption. We begin by describing a specific hard-core predicate (see Section 8.1.3) for the RSA problem and then show how to use that hard-core predicate to encrypt a single bit. We then extend this scheme to give a KEM.

本节展示一个可以基于 RSA 假设证明为选择明文安全的加密方案。我们首先描述 RSA 问题的一个具体的难核谓词（见 8.1.3 节），然后展示如何利用该难核谓词加密单个比特，最后把该方案扩展为一个 KEM。

The schemes described in this section are mainly of theoretical interest and are not used in practice. This is because they are less efficient than alternative RSA-based constructions that can be proven secure in the random-oracle model (cf. Section 6.5). We will see examples of such encryption schemes in the sections that follow.

本节描述的方案主要具有理论意义，实践中并不使用。这是因为它们的效率不如另一些能在随机预言机模型中证明安全的基于 RSA 的构造（参见 6.5 节）。我们将在随后的几节中看到这类加密方案的例子。

**A hard-core predicate for the RSA problem.**

**RSA 问题的难核谓词。**

Loosely speaking, the RSA assumption says that given $N, e$, and $[x^e \bmod N]$ (for $x$ chosen uniformly from $\mathbb{Z}_N^*$), it is infeasible to recover $x$. By itself, this says nothing about the computational difficulty of computing some specific information about $x$. Can we isolate some particular bit of information about $x$ that is hard to compute from $N, e$ and $[x^e \bmod N]$? The notion of a hard-core predicate captures exactly this requirement. (Hard-core predicates were introduced in Section 8.1.3. The fact that the RSA assumption gives a family of one-way permutations is discussed in Section 9.4.1. Our treatment here, however, is self-contained.) It is possible to show that the least-significant bit of $x$, denoted $\mathsf{lsb}(x)$, is a hard-core predicate for the RSA problem.

粗略地说，RSA 假设断言：给定 $N, e$ 和 $[x^e \bmod N]$（其中 $x$ 从 $\mathbb{Z}_N^*$ 中均匀选取），恢复 $x$ 是不可行的。单就这一点而言，它对“计算关于 $x$ 的某些特定信息”的计算难度只字未提。我们能否分离出关于 $x$ 的某一比特信息，使它难以从 $N, e$ 和 $[x^e \bmod N]$ 算出？难核谓词这一概念刻画的正是这一要求。（难核谓词在 8.1.3 节引入；RSA 假设给出一族单向置换这一事实在 9.4.1 节讨论。不过，我们此处的处理是自足的。）可以证明，$x$ 的最低有效位（记作 $\mathsf{lsb}(x)$）是 RSA 问题的一个难核谓词。

Define the following experiment for a given algorithm $\mathsf{GenRSA}$ (with the usual behavior) and algorithm $\mathcal{A}$:

对给定的算法 $\mathsf{GenRSA}$（行为如前所述）和算法 $\mathcal{A}$，定义如下实验：

The RSA hard-core predicate experiment $\mathsf{RSA\text{-}lsb}_{A,\mathsf{GenRSA}}(1^{n})$:

RSA 难核谓词实验 $\mathsf{RSA\text{-}lsb}_{A,\mathsf{GenRSA}}(1^{n})$：

1. Run $\mathsf{GenRSA}(1^{n})$ to obtain $(N,e,d)$.

   运行 $\mathsf{GenRSA}(1^{n})$ 得到 $(N,e,d)$。

2. Choose a uniform $x \in \mathbb{Z}_N^*$ and compute $y := [x^e \bmod N]$.

   均匀选取 $x \in \mathbb{Z}_N^*$，并计算 $y := [x^e \bmod N]$。

3. $\mathcal{A}$ is given $N, e, y$, and outputs a bit $b$.

   将 $N, e, y$ 交给 $\mathcal{A}$，$\mathcal{A}$ 输出一个比特 $b$。

4. The output of the experiment is 1 if and only if $\mathsf{lsb}(x)=b$.

   当且仅当 $\mathsf{lsb}(x)=b$ 时，实验输出为 1。

Observe that $\mathsf{lsb}(x)$ is a uniform bit when $x \in \mathbb{Z}_N^*$ is uniform. $\mathcal{A}$ can guess $\mathsf{lsb}(x)$ with probability $1/2$ by simply outputting a uniform bit $b$. The following theorem states that if the RSA problem is hard, then no efficient algorithm $\mathcal{A}$ can do significantly better than this; i.e., the least-significant bit is a hard-core predicate of the RSA permutation.

注意，当 $x \in \mathbb{Z}_N^*$ 均匀时，$\mathsf{lsb}(x)$ 是一个均匀比特。$\mathcal{A}$ 只要输出一个均匀比特 $b$，就能以 $1/2$ 的概率猜中 $\mathsf{lsb}(x)$。下面的定理表明：如果 RSA 问题是困难的，那么任何高效算法 $\mathcal{A}$ 都无法明显做得更好；也就是说，最低有效位是 RSA 置换的难核谓词。

THEOREM 12.31 If the RSA problem is hard relative to GenRSA then for all probabilistic polynomial-time algorithms $\mathcal{A}$ there is a negligible function $\mathsf{negl}$ such that $\Pr[\mathsf{RSA\text{-}lsb}_{\mathcal{A},\mathsf{GenRSA}}(n)=1] \leq \frac{1}{2} + \mathsf{negl}(n)$.

定理 12.31　如果 RSA 问题相对于 $\mathsf{GenRSA}$ 是困难的，那么对所有概率多项式时间算法 $\mathcal{A}$，都存在可忽略函数 $\mathsf{negl}$ 使得 $\Pr[\mathsf{RSA\text{-}lsb}_{\mathcal{A},\mathsf{GenRSA}}(n)=1] \leq \frac{1}{2} + \mathsf{negl}(n)$。

A full proof of this theorem is beyond the scope of this book. However, we provide some intuition for the theorem by sketching a proof of a weaker result: that the RSA assumption implies $\Pr[\mathsf{RSA\text{-}lsb}_{\mathcal{A},\mathsf{GenRSA}}(n)=1]<1$ for all probabilistic polynomial-time $\mathcal{A}$. To prove this we show that an efficient algorithm that always correctly computes $\mathsf{lsb}(r)$ from $N,e$, and $[r^e \bmod N]$ can be used to efficiently recover $x$ (in its entirety) from $N,e$, and $[x^e \bmod N]$.

该定理的完整证明超出本书范围。不过，我们通过概述一个较弱结果的证明来提供关于该定理的一些直观认识：RSA 假设意味着对所有概率多项式时间的 $\mathcal{A}$ 都有 $\Pr[\mathsf{RSA\text{-}lsb}_{\mathcal{A},\mathsf{GenRSA}}(n)=1]<1$。为证明这一点，我们展示：一个总能从 $N,e$ 和 $[r^e \bmod N]$ 正确算出 $\mathsf{lsb}(r)$ 的高效算法，可以被用来从 $N,e$ 和 $[x^e \bmod N]$ 高效地（完整地）恢复 $x$。

Fix $N$ and $e$, and let $\mathcal{A}$ be an algorithm such that $\mathcal{A}([r^e \bmod N]) = \mathsf{lsb}(r)$. Given $N, e$, and $y = [x^e \bmod N]$, we will recover the bits of $x$ one-by-one, from least to most significant. To determine $\mathsf{lsb}(x)$ we simply run $\mathcal{A}(y)$. There are now two cases:

固定 $N$ 和 $e$，并设 $\mathcal{A}$ 是满足 $\mathcal{A}([r^e \bmod N]) = \mathsf{lsb}(r)$ 的算法。给定 $N, e$ 和 $y = [x^e \bmod N]$，我们将从最低有效位到最高有效位逐位恢复 $x$。要确定 $\mathsf{lsb}(x)$，只需运行 $\mathcal{A}(y)$。接下来分两种情形：

Case 1: $\mathsf{lsb}(x) = 0$. Note that $y/2^e = (x/2)^e \bmod N$, and because $x$ is even (i.e., $\mathsf{lsb}(x) = 0$), 2 divides the integer x. So $x/2$ is just the right-wise bit-shift of $x$, and $\mathsf{lsb}(x/2)$ is equal to $2\mathsf{sb}(x)$, the 2nd-least-significant bit of $x$. So we can obtain $2\mathsf{sb}(x)$ by computing $y^{\prime} := [y/2^e \bmod N]$ and then running $\mathcal{A}(y^{\prime})$.

情形 1：$\mathsf{lsb}(x) = 0$。注意 $y/2^e = (x/2)^e \bmod N$，且因为 $x$ 是偶数（即 $\mathsf{lsb}(x) = 0$），2 整除整数 x。所以 $x/2$ 就是 $x$ 右移一位的结果，而 $\mathsf{lsb}(x/2)$ 等于 $2\mathsf{sb}(x)$，即 $x$ 的次低有效位。于是，我们可以通过计算 $y^{\prime} := [y/2^e \bmod N]$ 再运行 $\mathcal{A}(y^{\prime})$ 来得到 $2\mathsf{sb}(x)$。

Case 2: $\mathsf{lsb}(x) = 1$. Here $[x/2 \bmod N] = (x + N)/2$. So $\mathsf{lsb}([x/2 \bmod N])$ is equal to $2\mathsf{sb}(x + N)$; the latter is equal to $1 \oplus {2}\mathsf{sb}(N) \oplus {2}\mathsf{sb}(x)$ (we have a carry bit in the second position because both $x$ and $N$ are odd). So if we compute $y^{\prime} := [y/2^e \bmod N]$, then $2\mathsf{sb}(x) = \mathcal{A}(y^{\prime}) \oplus 1 \oplus {2}\mathsf{sb}(N)$.

情形 2：$\mathsf{lsb}(x) = 1$。此时 $[x/2 \bmod N] = (x + N)/2$。所以 $\mathsf{lsb}([x/2 \bmod N])$ 等于 $2\mathsf{sb}(x + N)$；后者等于 $1 \oplus {2}\mathsf{sb}(N) \oplus {2}\mathsf{sb}(x)$（因为 $x$ 和 $N$ 都是奇数，在第二位上有一个进位比特）。因此，只要计算 $y^{\prime} := [y/2^e \bmod N]$，就有 $2\mathsf{sb}(x) = \mathcal{A}(y^{\prime}) \oplus 1 \oplus {2}\mathsf{sb}(N)$。

Continuing in this way, we can recover all the bits of x.

以这种方式继续下去，我们可以恢复 x 的全部比特。

**Encrypting one bit.**

**加密单个比特。**

We can use the hard-core predicate identified above to encrypt a single bit. The idea is straightforward: to encrypt the message $m \in \{0,1\}$, the sender chooses uniform $r \in \mathbb{Z}_N^*$ subject to the constraint that $\mathsf{lsb}(r) = m$; the ciphertext is $c := [r^e \bmod N]$. See Construction 12.32.

我们可以利用上面确定的难核谓词来加密单个比特。思路很直接：要加密消息 $m \in \{0,1\}$，发送方在满足 $\mathsf{lsb}(r) = m$ 的约束下均匀选取 $r \in \mathbb{Z}_N^*$；密文为 $c := [r^e \bmod N]$。见构造 12.32。

**CONSTRUCTION 12.32**

**构造 12.32**

Let GenRSA be as usual, and define a public-key encryption scheme as follows:

设 $\mathsf{GenRSA}$ 如常，并如下定义一个公钥加密方案：

- Gen: on input $1^n$, run $\mathsf{GenRSA}(1^n)$ to obtain $(N,e,d)$. Output the public key $pk=\langle N,e\rangle$, and the private key $sk=\langle N,d\rangle$.

- Gen：以 $1^n$ 为输入，运行 $\mathsf{GenRSA}(1^n)$ 得到 $(N,e,d)$。输出公钥 $pk=\langle N,e\rangle$ 和私钥 $sk=\langle N,d\rangle$。

- Enc: on input a public key $pk = \langle N, e \rangle$ and a message $m \in \{0,1\}$, choose a uniform $r \in \mathbb{Z}_N^*$ subject to the constraint that $\mathsf{lsb}(r) = m$. Output the ciphertext $c := [r^e \bmod N]$.

- Enc：以公钥 $pk = \langle N, e \rangle$ 和消息 $m \in \{0,1\}$ 为输入，在满足 $\mathsf{lsb}(r) = m$ 的约束下均匀选取 $r \in \mathbb{Z}_N^*$。输出密文 $c := [r^e \bmod N]$。

- Dec: on input a private key $sk = \langle N, d \rangle$ and a ciphertext $c$, compute $r := [c^d \bmod N]$ and output $\mathsf{lsb}(r)$.

- Dec：以私钥 $sk = \langle N, d \rangle$ 和密文 $c$ 为输入，计算 $r := [c^d \bmod N]$，并输出 $\mathsf{lsb}(r)$。

Single-bit encryption using a hard-core predicate for RSA.

使用 RSA 难核谓词的单比特加密。

THEOREM 12.33 If the RSA problem is hard relative to GenRSA then Construction 12.32 is CPA-secure.

定理 12.33　如果 RSA 问题相对于 $\mathsf{GenRSA}$ 是困难的，那么构造 12.32 是选择明文安全的。

PROOF Let $\Pi$ denote Construction 12.32. We prove that $\Pi$ has indistinguishable encryptions in the presence of an eavesdropper; by Proposition 12.3, this implies it is CPA-secure.

证明　用 $\Pi$ 表示构造 12.32。我们证明 $\Pi$ 在窃听者存在下具有不可区分的加密；由命题 12.3，这蕴含它是选择明文安全的。

Let $\mathcal{A}$ be a probabilistic polynomial-time adversary. Without loss of generality, we may assume $m_0 = 0$ and $m_1 = 1$ in experiment $\mathsf{PubK}_{\mathcal{A},\Pi}^{\mathsf{eav}}(n)$. So

设 $\mathcal{A}$ 是概率多项式时间敌手。不失一般性，我们可以假设实验 $\mathsf{PubK}_{\mathcal{A},\Pi}^{\mathsf{eav}}(n)$ 中 $m_0 = 0$、$m_1 = 1$。于是

$$
\begin{aligned}
\Pr[\mathsf{PubK}_{\mathcal{A},\Pi}^{\mathsf{eav}}(n)=1]=&\frac{1}{2}\cdot\Pr[\mathcal{A}(N,e,c)=0\mid c\text{ is an encryption of }0]\\
&+\frac{1}{2}\cdot\Pr[\mathcal{A}(N,e,c)=1\mid c\text{ is an encryption of }1].
\end{aligned}
$$

Consider running $\mathcal{A}$ in experiment $\mathsf{RSA\text{-}lsb}$. By definition,

考虑在实验 $\mathsf{RSA\text{-}lsb}$ 中运行 $\mathcal{A}$。由定义，

$$
\Pr[\mathsf{RSA\text{-}lsb}_{\mathcal{A},\mathsf{GenRSA}}(n)=1]=\Pr[\mathcal{A}\left(N,e,[r^{e}\bmod N]\right)=\mathsf{lsb}(r)],
$$

where $r$ is uniform in $\mathbb{Z}_N^*$. Since $\Pr[\mathsf{lsb}(r) = 1] = 1/2$, we have

其中 $r$ 在 $\mathbb{Z}_N^*$ 中均匀。由于 $\Pr[\mathsf{lsb}(r) = 1] = 1/2$，我们有

$$
\begin{aligned}
\Pr[\mathsf{RSA\text{-}lsb}_{\mathcal{A},\mathsf{GenRSA}}(n)=1]&=\frac{1}{2}\cdot\Pr[\mathcal{A}\left(N,e,[r^{e}\bmod N]\right)=0\mid\mathsf{lsb}(r)=0]\\
&\quad+\frac{1}{2}\cdot\Pr[\mathcal{A}\left(N,e,[r^{e}\bmod N]\right)=1\mid\mathsf{lsb}(r)=1].
\end{aligned}
$$

Noting that encrypting $m \in \{0,1\}$ corresponds exactly to choosing uniform $r$ subject to the constraint that $\mathsf{lsb}(r) = m$, we see that

注意到加密 $m \in \{0,1\}$ 恰好对应于在满足 $\mathsf{lsb}(r) = m$ 的约束下均匀选取 $r$，我们看出

$$
\Pr[\mathsf{PubK}_{\mathcal{A},\Pi}^{\mathsf{eav}}(n)=1]=\Pr[\mathsf{RSA\text{-}lsb}_{\mathcal{A},\mathsf{GenRSA}}(n)=1].
$$

Theorem 12.31 thus implies that there is a negligible function $\mathsf{negl}$ such that

于是定理 12.31 意味着存在可忽略函数 $\mathsf{negl}$ 使得

$$
\Pr[\mathsf{PubK}_{\mathcal{A},\Pi}^{\mathsf{eav}}(n)=1]\leq\frac{1}{2}+\mathsf{negl}(n),
$$

as desired.

这正是所要证明的。

Constructing a KEM. We now show how to extend Construction 12.32 so as to obtain a KEM with key length $n$. A naive way of doing this would be to simply choose a uniform, $n$-bit key $k$ and then encrypt the bits of $k$ one-by-one using $n$ invocations of Construction 12.32. This would result in a rather long ciphertext consisting of $n$ elements of $\mathbb{Z}_N^*$.

**构造 KEM。** 我们现在展示如何扩展构造 12.32，以得到一个密钥长度为 $n$ 的 KEM。一种朴素的做法是直接均匀选取一个 $n$ 比特密钥 $k$，然后调用 $n$ 次构造 12.32 逐比特加密 $k$。这会得到一个很长的密文，由 $\mathbb{Z}_N^*$ 的 $n$ 个元素组成。

A better approach is for the sender to apply the RSA permutation (namely, raising to the $e$th power modulo $N$) repeatedly, starting from an initial, uniform value $c_{1}$. That is, the sender will successively compute $c_{1}^{e}$, followed by $(c_{1}^{e})^{e}=c_{1}^{e^{2}}$, and so on, up to $c_{1}^{e^{n}}$ (all modulo $N$). The final value $[c_{1}^{e^{n}}\bmod N]$ will be the ciphertext, and the sequence of bits $\mathsf{lsb}(c_{1}),\mathsf{lsb}(c_{1}^{e}),\ldots,\mathsf{lsb}(c_{1}^{e^{n-1}})$ is the key. To decrypt a ciphertext $c$, the receiver simply reverses this process, successively computing $c^{d},(c^{d})^{d}=c^{d^{2}}$ up to $c^{d^{n}}$ (again, all modulo $N$) to recover the initial value $c_{1}=c^{d^{n}}$ used by the sender. Having recovered $c_{1}$, as well as the intermediate values $c_{1}^{e^{n}},\ldots,c_{1}^{e}$, the receiver can compute the key.

一种更好的做法是：发送方从一个初始的均匀值 $c_{1}$ 出发，反复应用 RSA 置换（即模 $N$ 的 $e$ 次幂）。也就是说，发送方依次计算 $c_{1}^{e}$，接着是 $(c_{1}^{e})^{e}=c_{1}^{e^{2}}$，如此继续，直到 $c_{1}^{e^{n}}$（全部在模 $N$ 下进行）。最终值 $[c_{1}^{e^{n}}\bmod N]$ 就是密文，而比特序列 $\mathsf{lsb}(c_{1}),\mathsf{lsb}(c_{1}^{e}),\ldots,\mathsf{lsb}(c_{1}^{e^{n-1}})$ 就是密钥。要解密密文 $c$，接收方只需把这一过程反过来：依次计算 $c^{d},(c^{d})^{d}=c^{d^{2}}$，直到 $c^{d^{n}}$（同样全部在模 $N$ 下进行），从而恢复发送方所用的初始值 $c_{1}=c^{d^{n}}$。恢复出 $c_{1}$ 以及中间值 $c_{1}^{e^{n}},\ldots,c_{1}^{e}$ 之后，接收方即可算出密钥。

It is possible to implement decryption more efficiently using the fact that the receiver knows the order of the group $\mathbb{Z}_N^*$. At key-generation time, the receiver can pre-compute $d^{\prime} := [d^n \bmod \phi(N)]$ and store $d^{\prime}$ as part of its private key. To decrypt, the receiver can then directly compute $c_1 := [c^{d^{\prime}} \bmod N]$, after which it can compute $c_1^e, \ldots, c_1^{e^n}$. (Exponentiations to the power $e$ are more efficient than exponentiations to the power $d$ since $e \ll d$ in practice.) This works, of course, since

利用接收方知道群 $\mathbb{Z}_N^*$ 的阶这一事实，可以更高效地实现解密。在密钥生成时，接收方可以预先计算 $d^{\prime} := [d^n \bmod \phi(N)]$，并把 $d^{\prime}$ 存为私钥的一部分。解密时，接收方就可以直接计算 $c_1 := [c^{d^{\prime}} \bmod N]$，然后再计算 $c_1^e, \ldots, c_1^{e^n}$。（由于实践中 $e \ll d$，$e$ 次幂运算比 $d$ 次幂运算更高效。）这当然是可行的，因为

$$
c^{d^{n}}\bmod N=c^{[d^{n} \bmod \phi(N)]}=c^{d^{\prime}}\bmod N.
$$

The above is formally described as Construction 12.34.

上述内容形式化为构造 12.34。

**CONSTRUCTION 12.34**

**构造 12.34**

Let GenRSA be as usual, and define a KEM as follows:

设 $\mathsf{GenRSA}$ 如常，并如下定义一个 KEM：

- Gen: on input $1^n$, run $\mathsf{GenRSA}(1^n)$ to obtain $(N, e, d)$. Then compute $d^{\prime} := [d^n \bmod \phi(N)]$ (note that $\phi(N)$ can be computed from $(N, e, d)$ or obtained during the course of running GenRSA). Output $pk = \langle N, e \rangle$ and $sk = \langle N, d^{\prime}\rangle$.

- Gen：以 $1^n$ 为输入，运行 $\mathsf{GenRSA}(1^n)$ 得到 $(N, e, d)$。然后计算 $d^{\prime} := [d^n \bmod \phi(N)]$（注意 $\phi(N)$ 可以由 $(N, e, d)$ 算出，也可以在运行 GenRSA 的过程中获得）。输出 $pk = \langle N, e \rangle$ 和 $sk = \langle N, d^{\prime}\rangle$。

- Encaps: on input $pk = \langle N, e \rangle$, choose a uniform $c_1 \in \mathbb{Z}_N^*$. Then for $i = 1, \ldots, n$ do:

- Encaps：以 $pk = \langle N, e \rangle$ 为输入，均匀选取 $c_1 \in \mathbb{Z}_N^*$。然后对 $i = 1, \ldots, n$ 执行：

   1. Compute $k_i := \mathsf{lsb}(c_i)$.

      计算 $k_i := \mathsf{lsb}(c_i)$。

   2. Compute $c_{i+1} := [c_i^e \bmod N]$.

      计算 $c_{i+1} := [c_i^e \bmod N]$。

   Output the ciphertext $c_{n+1}$ and the key $k = k_1 \cdots k_n$.

   输出密文 $c_{n+1}$ 和密钥 $k = k_1 \cdots k_n$。

- Decaps: on input $sk = \langle N, d^{\prime} \rangle$ and a ciphertext $c$, compute $c_1 := [c^{d^{\prime}} \bmod N]$. Then for $i = 1, \ldots, n$ do:

- Decaps：以 $sk = \langle N, d^{\prime} \rangle$ 和密文 $c$ 为输入，计算 $c_1 := [c^{d^{\prime}} \bmod N]$。然后对 $i = 1, \ldots, n$ 执行：

   1. Compute $k_i := \mathsf{lsb}(c_i)$.

      计算 $k_i := \mathsf{lsb}(c_i)$。

   2. Compute $c_{i+1} := [c_i^e \bmod N]$.

      计算 $c_{i+1} := [c_i^e \bmod N]$。

   Output the key $k = k_1 \cdots k_n$.

   输出密钥 $k = k_1 \cdots k_n$。

A KEM using a hard-core predicate for RSA.

使用 RSA 难核谓词的 KEM。

The construction is reminiscent of the approach used to construct a pseudorandom generator from a one-way permutation toward the end of Section 8.4.2. If we let $f$ denote the RSA permutation relative to some public key $\langle N, e \rangle$ (i.e., $f(x) \overset{\mathrm{def}}{=} [x^e \bmod N]$), then CPA-security of Construction 12.34 is equivalent to pseudorandomness of $\mathsf{lsb}(f^{n-1}(c_1)), \ldots, \mathsf{lsb}(c_1)$ even conditioned on the value $c = f^n(c_1)$. This, in turn, can be proven using Theorem 12.31 and the techniques from Section 8.4.2. (The only difference is that in Section 8.4.2 the value $f^n(c_1)$ was itself a uniform $n$-bit string, whereas here it is a uniform element of $\mathbb{Z}_N^*$. Pseudorandomness of the successive hard-core predicates is independent of the domain of $f$.) Summarizing:

该构造让人想起 8.4.2 节末尾由单向置换构造伪随机生成器所用的方法。如果用 $f$ 表示相对于某个公钥 $\langle N, e \rangle$ 的 RSA 置换（即 $f(x) \overset{\mathrm{def}}{=} [x^e \bmod N]$），那么构造 12.34 的选择明文安全性就等价于：即使以 $c = f^n(c_1)$ 的值为条件，$\mathsf{lsb}(f^{n-1}(c_1)), \ldots, \mathsf{lsb}(c_1)$ 仍是伪随机的。而后者又可以用定理 12.31 和 8.4.2 节的技术来证明。（唯一的差别是：在 8.4.2 节中，$f^n(c_1)$ 本身是均匀的 $n$ 比特串，而在这里它是 $\mathbb{Z}_N^*$ 中的均匀元素。相继各难核谓词的伪随机性与 $f$ 的定义域无关。）总结如下：

THEOREM 12.35 If the RSA problem is hard relative to GenRSA then Construction 12.34 is a CPA-secure KEM.

定理 12.35　如果 RSA 问题相对于 $\mathsf{GenRSA}$ 是困难的，那么构造 12.34 是一个选择明文安全的 KEM。

Efficiency. Construction 12.34 is reasonably efficient. To be concrete, assume that $n = 128$, the RSA modulus $N$ is 2048 bits long, and the public exponent $e$ is 3 so that exponentiation to the power $e$ modulo $N$ can be computed using two modular multiplications. (See Appendix B.2.3.) Encryption then requires $2n = 256$ modular multiplications. Decryption can be done with one full modular exponentiation (at the cost of approximately $1.5 \cdot 2048 = 3072$ modular multiplications) plus an additional 256 modular multiplications. The cost of decryption is thus only about 8% less efficient than for the plain RSA encryption scheme. Encryption is significantly more expensive than in plain RSA, but in many applications decryption time is more important (since it may be implemented by a server that is performing thousands of decryptions simultaneously).

**效率。** 构造 12.34 相当高效。具体地说，假设 $n = 128$，RSA 模数 $N$ 长 2048 比特，公开指数 $e$ 为 3，于是模 $N$ 的 $e$ 次幂运算可以用两次模乘法完成。（见附录 B.2.3。）此时加密需要 $2n = 256$ 次模乘法。解密则可以用一次完整的模幂运算（代价约为 $1.5 \cdot 2048 = 3072$ 次模乘法）加上额外的 256 次模乘法完成。因此，解密的开销仅比朴素 RSA 加密方案高约 8%。加密比朴素 RSA 昂贵得多，但在许多应用中解密时间更为重要（因为解密可能由一台同时要执行数千次解密的服务器来完成）。

### 12.5.4 OAEP and PKCS #1 v2　OAEP 与 PKCS #1 v2

We now consider CCA-security for RSA-based encryption schemes. We begin by showing that all the RSA-based encryption schemes we have seen so far are vulnerable to chosen-ciphertext attacks.

现在考虑基于 RSA 的加密方案的选择密文安全（CCA）。我们首先说明：到目前为止见过的所有基于 RSA 的加密方案都无法抵御选择密文攻击。

Plain RSA encryption. Plain RSA is not even CPA-secure. But it does ensure that if $m \in \mathbb{Z}_N^*$ is uniform then an attacker who eavesdrops on the encryption $c = [m^e \bmod N]$ of $m$ with respect to the public key $\langle N, e \rangle$ cannot recover $m$. Even this weak guarantee no longer holds in a setting where chosen-ciphertext attacks are possible. As in the case of El Gamal encryption, this is a consequence of the fact that plain RSA is malleable: given the encryption $c = [m^e \bmod N]$ of an unknown message $m$, it is easy to generate a ciphertext $c^{\prime}$ that is an encryption of $[2m \bmod N]$ by setting

**朴素 RSA 加密。** 朴素 RSA 甚至不是选择明文安全的。但它确实能保证：如果 $m \in \mathbb{Z}_N^*$ 是均匀的，那么窃听到 $m$ 在公钥 $\langle N, e \rangle$ 下的加密 $c = [m^e \bmod N]$ 的攻击者无法恢复 $m$。而在可能发生选择密文攻击的环境中，就连这点微弱的保证也不再成立。与 El Gamal 加密的情形一样，这是朴素 RSA 具有可延展性的结果：给定未知消息 $m$ 的加密 $c = [m^e \bmod N]$，只要令

$$
\begin{aligned}
c^{\prime}&:=[2^{e}\cdot c\bmod N]\\
&=2^{e}\cdot m^{e}=(2m)^{e}\bmod N.
\end{aligned}
$$

In fact, we have used this observation several times already.

事实上，我们已经多次用到过这一观察。

RSA PKCS #1 v1.5. Padded RSA encryption, which is conjectured to be CPA-secure for the right setting of the parameters, is vulnerable to essentially the same attack as plain RSA encryption is. But there is also a more interesting chosen-ciphertext attack on PKCS #1 v1.5 encryption that, in contrast to an attack that exploits malleability, does not require full access to a decryption oracle; it only requires access to a "partial" decryption oracle that indicates whether or not decryption of some ciphertext returns an error. This makes the attack much more practical, as it can be carried out whenever an attacker can distinguish a decryption success from a decryption failure, as in the case of the padding-oracle attack discussed in Section 5.1.1.

**RSA PKCS #1 v1.5。** 填充 RSA 加密被猜想在参数设置恰当时是选择明文安全的，但它仍会受到与朴素 RSA 加密本质上相同的攻击。不过，针对 PKCS #1 v1.5 加密还有一种更有意思的选择密文攻击：与利用可延展性的攻击不同，它不需要对解密预言机的完全访问；它只需要访问一个“部分”解密预言机，该预言机会指示某个密文的解密是否返回错误。这使该攻击实用得多，因为只要攻击者能区分解密成功与解密失败就能实施——正如 5.1.1 节讨论的填充预言机攻击的情形。

Recall that the public-key encryption scheme defined in the PKCS #1 v1.5 standard uses a variant of padded RSA encryption where the padding is done in a specific way. In particular, the two high-order bytes of the padded message are always $\mathtt{0x00}\|\mathtt{0x02}$. When decrypting, the receiver is supposed to check that the two high-order bytes of the intermediate result match these values, and return an error if this is not the case. In 1998, Bleichenbacher developed a chosen-ciphertext attack that exploits the fact that this check is done. Roughly, given a ciphertext $c$ that corresponds to an honest encryption of some unknown message $m$ with respect to a public key $\langle N, e \rangle$, Bleichenbacher's attack repeatedly chooses uniform $s \in \mathbb{Z}_N^*$ and submits the ciphertext $c^{\prime} := [s^e \cdot c \bmod N]$ to the receiver. Say $c = [\hat{m}^e \bmod N]$ where

回想一下，PKCS #1 v1.5 标准定义的公钥加密方案使用的是填充 RSA 加密的一个变体，其中填充以特定的方式完成。特别地，填充后消息的最高两个字节总是 $\mathtt{0x00}\|\mathtt{0x02}$。解密时，接收方应当检查中间结果的最高两个字节是否与这些值相符，若不相符则返回错误。1998 年，Bleichenbacher 提出了一种选择密文攻击，利用的正是“会进行这一检查”的事实。粗略地说，给定密文 $c$——它对应于某个未知消息 $m$ 在公钥 $\langle N, e \rangle$ 下的诚实加密——Bleichenbacher 的攻击反复选取均匀的 $s \in \mathbb{Z}_N^*$，并把密文 $c^{\prime} := [s^e \cdot c \bmod N]$ 提交给接收方。设 $c = [\hat{m}^e \bmod N]$，其中

$$
\hat{m}=\mathtt{0x00}\|\mathtt{0x02}\|r\|\mathtt{0x00}\|m,
$$

as specified by PKCS #1 v1.5. Then decryption of $c^{\prime}$ will give the intermediate result $\hat{m}^{\prime} = [s \cdot \hat{m} \bmod N]$, and the receiver will return an error unless the top two bytes of $\hat{m}^{\prime}$ are exactly 0x00||0x02. (Other checks are done as well, but we ignore those for simplicity.) Thus, whenever decryption succeeds the attacker learns that the top two bytes of $s \cdot \hat{m} \bmod N$ are 0x00||0x02, where $s$ is known. Sufficiently many equations of this type suffice for the attacker to learn $\hat{m}$ and recover all of the original message $m$.

如 PKCS #1 v1.5 所规定的那样。那么解密 $c^{\prime}$ 将给出中间结果 $\hat{m}^{\prime} = [s \cdot \hat{m} \bmod N]$，而除非 $\hat{m}^{\prime}$ 的最高两个字节恰好是 0x00||0x02，否则接收方都会返回错误。（还会进行其他检查，但为简单起见我们将其忽略。）因此，每当解密成功，攻击者就知道 $s \cdot \hat{m} \bmod N$ 的最高两个字节是 0x00||0x02，其中 $s$ 是已知的。足够多这样的方程就足以让攻击者求出 $\hat{m}$，进而恢复整个原始消息 $m$。

**The CPA-secure KEM.**

**选择明文安全的 KEM。**

In Section 12.5.3 we showed a construction of a KEM that can be proven CPA-secure based on the RSA assumption. That construction is also insecure against a chosen-ciphertext attack; we leave the details as an exercise.

在 12.5.3 节我们展示了一个可以基于 RSA 假设证明为选择明文安全的 KEM 构造。该构造在选择密文攻击下也不安全；细节留作习题。

### RSA-OAEP　RSA-OAEP

We explore a construction of CCA-secure encryption from RSA using what is called optimal asymmetric encryption padding (OAEP). The resulting RSA-OAEP scheme follows the idea (used also in Section 12.5.2) of taking a message $m$, mapping it to an element $\hat{m} \in \mathbb{Z}_N^*$, and then letting $c = [\hat{m}^e \bmod N]$ be the ciphertext. The transformation here, however, is more complex than before. A version of RSA-OAEP has been standardized as part of RSA PKCS #1 since version 2.0.

我们来探索一种利用所谓最优非对称加密填充（optimal asymmetric encryption padding, OAEP）从 RSA 构造选择密文安全加密的方法。由此得到的 RSA-OAEP 方案沿袭了下述思路（12.5.2 节也曾使用）：取一条消息 $m$，把它映射为 $\mathbb{Z}_N^*$ 中的元素 $\hat{m}$，再令 $c = [\hat{m}^e \bmod N]$ 作为密文。不过，这里的变换比之前更为复杂。RSA-OAEP 的一个版本自 2.0 版起已被标准化，成为 RSA PKCS #1 的一部分。

Let $\ell(n)$, $k(n)$ be integer-valued functions with $k(n) = \Theta(n)$, and such that $\ell(n) + 2k(n)$ is less than the bit-length of moduli output by $\mathsf{GenRSA}(1^n)$. Fix $n$, and let $\ell = \ell(n)$ and $k = k(n)$. Let $G : \{0, 1\}^k \to \{0, 1\}^{\ell+k}$ and $H : \{0, 1\}^{\ell+k} \to \{0, 1\}^k$ be two hash functions that will be modeled as independent random oracles. (Although using more than one random oracle was not discussed in Section 6.5.1, we can do so in the natural way.) The transformation defined by OAEP is based on a two-round Feistel network with $G$ and $H$ as round functions; see Figure 12.4. Mapping a message $m \in \{0, 1\}^\ell$ to $\hat{m}$ is done as follows: first set $m^{\prime} := m\|0^k$ and choose a uniform $r \in \{0, 1\}^k$. Then compute

设 $\ell(n)$、$k(n)$ 为整数值函数，满足 $k(n) = \Theta(n)$，且 $\ell(n) + 2k(n)$ 小于 $\mathsf{GenRSA}(1^n)$ 输出的模数的比特长度。固定 $n$，令 $\ell = \ell(n)$、$k = k(n)$。设 $G : \{0, 1\}^k \to \{0, 1\}^{\ell+k}$ 和 $H : \{0, 1\}^{\ell+k} \to \{0, 1\}^k$ 是两个哈希函数，分析中它们将被建模为相互独立的随机预言机。（虽然 6.5.1 节未曾讨论过使用多个随机预言机的情形，但我们可以按自然的方式这样做。）OAEP 定义的变换基于一个以 $G$ 和 $H$ 为轮函数的两轮 Feistel 网络；见图 12.4。把消息 $m \in \{0, 1\}^\ell$ 映射到 $\hat{m}$ 的做法如下：先置 $m^{\prime} := m\|0^k$，并均匀选取 $r \in \{0, 1\}^k$。然后计算

$$
t:=m^{\prime}\oplus G(r)\in\{0,1\}^{\ell+k},\quad s:=r\oplus H(t)\in\{0,1\}^{k},
$$

and set $\hat{m} := s\|t$.

并置 $\hat{m} := s\|t$。

![Image](https://lsky.jerryxue.top/i/2026/08/25/6a8d86e4c67f6.jpg)

**FIGURE 12.4: The OAEP transformation. / 图 12.4：OAEP 变换**

(The PKCS #1 standard differs from what we have described, but the differences are unimportant for our purposes.) To encrypt a message $m$ with respect to the public key $\langle N, e \rangle$, the sender generates $\hat{m}$ as above and outputs the ciphertext $c := [\hat{m}^e \bmod N]$. (Note that $\hat{m}$, interpreted as an integer, is less than $N$ because of the constraints on $\ell, k$.)

（PKCS #1 标准与我们描述的有所差异，但这些差异对我们的目的无关紧要。）要用公钥 $\langle N, e \rangle$ 加密消息 $m$，发送方按上述方式生成 $\hat{m}$，并输出密文 $c := [\hat{m}^e \bmod N]$。（注意，由于 $\ell, k$ 所受的约束，$\hat{m}$ 按整数解释时小于 $N$。）

To decrypt, the receiver computes $\hat{m} := [c^d \bmod N]$ and lets $s\|t := \hat{m}$ with $s$ and $t$ of the appropriate lengths. It then inverts the Feistel network by computing $r := H(t) \oplus s$ and $m^{\prime} := G(r) \oplus t$. Importantly, the receiver then verifies that the trailing $k$ bits of $m^{\prime}$ are all 0; if not, the ciphertext is rejected and an error message is returned. Otherwise, the $k$ least-significant 0s of $m^{\prime}$ are discarded, and the remaining $\ell$ bits of $m^{\prime}$ are output as the message. This process is described in Construction 12.36.

解密时，接收方计算 $\hat{m} := [c^d \bmod N]$，并将 $s\|t := \hat{m}$ 按相应的长度解析出 $s$ 与 $t$。然后它通过计算 $r := H(t) \oplus s$ 和 $m^{\prime} := G(r) \oplus t$ 来逆转该 Feistel 网络。重要的是，接收方接着要验证 $m^{\prime}$ 的末尾 $k$ 个比特是否全为 0；若不是，则拒绝该密文并返回错误消息。否则，丢弃 $m^{\prime}$ 中最低有效位的 $k$ 个 0，并把 $m^{\prime}$ 其余的 $\ell$ 个比特作为消息输出。这一过程见构造 12.36。

RSA-OAEP can be proven to be CCA-secure based on the RSA assumption if $G$ and $H$ are modeled as random oracles. The proof is rather complicated, and we do not give it here; instead, we merely provide some intuition. First consider CPA-security. During encryption the sender computes

在把 $G$ 和 $H$ 建模为随机预言机的前提下，可以基于 RSA 假设证明 RSA-OAEP 是选择密文安全的。该证明相当复杂，我们在此不予给出，只提供一些直觉。先考虑选择明文安全性。加密过程中发送方计算

$$
m^{\prime}:=m\|0^{k},\quad t:=m^{\prime}\oplus G(r),\quad s:=r\oplus H(t)
$$

for uniform $r$; the ciphertext is $[(s\|t)^{e}\bmod N]$. If the attacker never queries $r$ to $G$ then, since we model $G$ as a random function, the value $G(r)$ is uniform from the attacker's point of view and so $m$ is masked with a uniform string just as in the one-time pad encryption scheme. Thus, if the attacker never queries $r$ to $G$ then no information about the message is leaked.

其中 $r$ 是均匀的；密文为 $[(s\|t)^{e}\bmod N]$。如果攻击者从未向 $G$ 查询过 $r$，那么由于我们把 $G$ 建模为随机函数，$G(r)$ 在攻击者看来便是均匀的，因而 $m$ 就像在一次一密加密方案中那样被一个均匀串掩蔽。于是，若攻击者从不向 $G$ 查询 $r$，就不会泄露关于消息的任何信息。

Can the attacker query $r$ to $G$? The value of $r$ is itself masked by $H(t)$. So the attacker has no information about $r$ unless it first queries $t$ to $H$. If the attacker does not query $t$ to $H$ then the attacker may get lucky and guess $r$ anyway, but if $r$ is sufficiently long the probability of doing so is negligible.

攻击者能向 $G$ 查询 $r$ 吗？$r$ 的值本身又被 $H(t)$ 掩蔽。所以除非攻击者先向 $H$ 查询过 $t$，否则它对 $r$ 一无所知。如果攻击者不向 $H$ 查询 $t$，它也可能碰运气猜中 $r$，但只要 $r$ 足够长，这样做的概率就是可忽略的。

**CONSTRUCTION 12.36**

**构造 12.36**

Let GenRSA be as in the previous sections, and $\ell, k$ be as described in the text. Let $G : \{0,1\}^k \to \{0,1\}^{\ell+k}$ and $H : \{0,1\}^{\ell+k} \to \{0,1\}^k$ be functions. Construct a public-key encryption scheme as follows:

设 $\mathsf{GenRSA}$ 与前几节相同，$\ell, k$ 如正文所述。设 $G : \{0,1\}^k \to \{0,1\}^{\ell+k}$ 和 $H : \{0,1\}^{\ell+k} \to \{0,1\}^k$ 为两个函数。如下构造一个公钥加密方案：

- Gen: on input $1^n$, run $\mathsf{GenRSA}(1^n)$ to obtain $(N,e,d)$. The public key is $\langle N,e\rangle$ and the private key is $\langle N,d\rangle$.

- Gen：以 $1^n$ 为输入，运行 $\mathsf{GenRSA}(1^n)$ 得到 $(N,e,d)$。公钥为 $\langle N,e\rangle$，私钥为 $\langle N,d\rangle$。

- Enc: on input a public key $\langle N, e \rangle$ and a message $m \in \{0,1\}^{\ell}$, set $m^{\prime} := m\|0^k$ and choose a uniform $r \in \{0,1\}^k$. Then compute

- Enc：以公钥 $\langle N, e \rangle$ 和消息 $m \in \{0,1\}^{\ell}$ 为输入，置 $m^{\prime} := m\|0^k$，并均匀选取 $r \in \{0,1\}^k$。然后计算

$$
t:=m^{\prime}\oplus G(r),\quad s:=r\oplus H(t)
$$

and set $\hat{m} := s\|t$. Output the ciphertext $c := [\hat{m}^{e} \bmod N]$.

并置 $\hat{m} := s\|t$。输出密文 $c := [\hat{m}^{e} \bmod N]$。

- Dec: on input a private key $\langle N, d \rangle$ and a ciphertext $c \in \mathbb{Z}_N^*$, compute $\hat{m} := [c^d \bmod N]$. If $\|\hat{m}\| > \ell + 2k$, output $\perp$. Otherwise, parse $\hat{m}$ as $s\|t$ with $s \in \{0,1\}^k$ and $t \in \{0,1\}^{\ell+k}$. Compute $r := H(t) \oplus s$ and $m^{\prime} := G(r) \oplus t$. If the $k$ least-significant bits of $m^{\prime}$ are not all 0, output $\perp$. Otherwise, output the $\ell$ most-significant bits of $m^{\prime}$.

- Dec：以私钥 $\langle N, d \rangle$ 和密文 $c \in \mathbb{Z}_N^*$ 为输入，计算 $\hat{m} := [c^d \bmod N]$。若 $\|\hat{m}\| > \ell + 2k$，输出 $\perp$。否则把 $\hat{m}$ 解析为 $s\|t$，其中 $s \in \{0,1\}^k$、$t \in \{0,1\}^{\ell+k}$。计算 $r := H(t) \oplus s$ 和 $m^{\prime} := G(r) \oplus t$。若 $m^{\prime}$ 的最低有效 $k$ 个比特不全为 0，输出 $\perp$。否则输出 $m^{\prime}$ 的最高有效 $\ell$ 个比特。

**The RSA-OAEP encryption scheme.**

**RSA-OAEP 加密方案。**

Can the attacker query $t$ to $H$? Doing so would require the attacker to compute $t$ from $(s\|t)^e \bmod N$. Note that doing so does not directly solve the RSA problem, which instead would require computing both $s$ and $t$. Nevertheless, for the right settings of the parameters it is possible to show that recovering $t$ is computationally infeasible if the RSA problem is hard.

攻击者能向 $H$ 查询 $t$ 吗？这要求攻击者从 $(s\|t)^e \bmod N$ 算出 $t$。注意这样做并未直接求解 RSA 问题——后者要求同时算出 $s$ 和 $t$。尽管如此，在参数设置恰当时可以证明：如果 RSA 问题是困难的，恢复 $t$ 在计算上就是不可行的。

Arguing CCA-security involves additional complications, but the basic idea is to show that every decryption-oracle query $c$ made by the attacker falls into one of two categories: either the attacker obtained $c$ by legally encrypting some message $m$ itself (in which case the attacker learns nothing from the decryption query), or else decryption of $c$ returns an error. This is a consequence of the fact that the receiver checks that the $k$ least-significant bits of $m^{\prime}$ are 0 during decryption; if the attacker did not generate the ciphertext $c$ using the prescribed encryption algorithm, the probability that this condition holds is negligible. The formal proof is complicated by the fact that the attacker's decryption-oracle queries must be answered correctly without knowledge of the private key, which means there must be an efficient way to determine whether to return an error or not and, if not, what message to return. This is accomplished by looking at the adversary's queries to the random oracles $G, H$.

论证选择密文安全性还会带来额外的复杂性，但基本思路是证明攻击者发出的每个解密预言机查询 $c$ 都属于两类之一：要么 $c$ 是攻击者自己合法加密某条消息 $m$ 得到的（此时攻击者从该解密查询中一无所获），要么对 $c$ 的解密返回错误。这是接收方在解密时检查 $m^{\prime}$ 的最低有效 $k$ 个比特是否为 0 所带来的结果；如果攻击者不是用规定的加密算法生成密文 $c$，这一条件成立的概率是可忽略的。形式化证明的复杂之处在于：必须在不知道私钥的情况下正确回答攻击者的解密预言机查询，这意味着必须存在一种高效方法来判断是否应返回错误，以及在不应返回错误时该返回什么消息。这一点可以通过考察敌手对随机预言机 $G, H$ 的查询来实现。

Manger's chosen-ciphertext attack on PKCS #1 v2.0. In 2001, James Manger showed a chosen-ciphertext attack against certain implementations of the RSA encryption scheme specified in PKCS #1 v2.0—even though what was specified was a variant of RSA-OAEP! Since Construction 12.36 can be proven to be CCA-secure, how is this possible?

**Manger 对 PKCS #1 v2.0 的选择密文攻击。** 2001 年，James Manger 针对 PKCS #1 v2.0 所规定的 RSA 加密方案的某些实现给出了一个选择密文攻击——尽管标准里规定的正是 RSA-OAEP 的一个变体！既然构造 12.36 可以被证明是选择密文安全的，这怎么可能？

Examining the decryption algorithm in Construction 12.36, note that there are two ways an error can occur: either $\hat{m} \in \mathbb{Z}_N^*$ is too large, or $m^{\prime} \in \{0,1\}^{\ell+k}$ does not have enough trailing 0s. In Construction 12.36, the receiver is supposed to return the same error (denoted $\perp$) in either case. In some implementations, however, the receiver would output different errors depending on which step failed. This single bit of additional information enabled a chosen-ciphertext attack that could recover a message $m$ in its entirety from a corresponding ciphertext using only $\approx \|N\|$ queries to an oracle leaking the type of error upon decryption. This shows the importance of implementing cryptographic schemes exactly as specified, since the resulting proof and analysis may no longer apply if aspects of the scheme are changed.

考察构造 12.36 的解密算法可以注意到，出错有两种途径：要么 $\hat{m} \in \mathbb{Z}_N^*$ 过大，要么 $m^{\prime} \in \{0,1\}^{\ell+k}$ 没有足够的末尾 0。在构造 12.36 中，无论哪种情况，接收方都应返回同一个错误（记作 $\perp$）。然而在某些实现中，接收方会根据失败发生在哪一步而输出不同的错误。仅凭这一比特的额外信息，就可以实施一种选择密文攻击：只需向一个会在解密时泄露错误类型的预言机进行约 $\|N\|$ 次查询，就能从相应密文完整恢复消息 $m$。这说明严格按照规范实现密码方案何等重要——一旦方案的若干方面被改动，原有的证明和分析可能就不再适用。

Note that even if the same error is returned in both cases, an attacker might be able to determine where the error occurs if the time to return the error is different. (This is a great example of how an attacker is not limited to examining the inputs/outputs of an algorithm, but can use side-channel information to attack a scheme.) Implementations should ensure that the time to return an error is identical in either case.

注意，即使两种情况下返回相同的错误，如果返回错误所花的时间不同，攻击者也可能据此判断错误发生在哪一步。（这是一个极好的例子，说明攻击者并不局限于检查算法的输入/输出，还可以利用侧信道信息来攻击方案。）实现应当确保两种情况下返回错误的时间完全相同。

### 12.5.5 \*A CCA-Secure KEM in the Random-Oracle Model　\*随机预言机模型中的选择密文安全 KEM

We show here a construction of an RSA-based KEM that is CCA-secure in the random-oracle model; this scheme is included as part of the ISO/IEC 18033-2 standard for public-key encryption. (Recall from Theorem 12.14 that any such construction can be used in conjunction with any CCA-secure private-key encryption scheme to give a CCA-secure public-key encryption scheme.) As compared to the RSA-OAEP scheme from the previous section, the main advantage is the simplicity of both the construction and its proof of security. Its main disadvantage is that it results in longer ciphertexts when encrypting short messages since it requires the KEM/DEM paradigm whereas RSA-OAEP does not. For encrypting long messages, however, RSA-OAEP would also be used as part of a hybrid encryption scheme, and would result in an encryption scheme having similar efficiency to what would be obtained using the KEM shown here.

我们在这里给出一个在随机预言机模型中选择密文安全的基于 RSA 的 KEM 构造；该方案已被纳入公钥加密的 ISO/IEC 18033-2 标准。（回忆定理 12.14：任何这样的构造都可以与任意选择密文安全的私钥加密方案结合，得到选择密文安全的公钥加密方案。）与上一节的 RSA-OAEP 方案相比，它的主要优点是构造和安全证明都很简洁；主要缺点是加密短消息时会得到更长的密文，因为它需要用到 KEM/DEM 范式，而 RSA-OAEP 不需要。不过对于长消息而言，RSA-OAEP 同样会作为混合加密方案的一部分来使用，所得加密方案的效率与本节所示 KEM 得到的相近。

The public key of the scheme includes $\langle N, e \rangle$ as usual, as well as a specification of a function $H : \mathbb{Z}_N^* \to \{0,1\}^n$ that will be modeled as a random oracle in the analysis. (This function can be based on some underlying cryptographic hash function, as discussed in Section 6.5. We omit the details.) To encapsulate a key, the sender chooses uniform $r \in \mathbb{Z}_N^*$ and then computes the ciphertext $c := [r^e \bmod N]$ and the key $k := H(r)$. To decrypt a ciphertext $c$, the receiver simply recovers $r$ in the usual way and then re-derives the same key $k := H(r)$. See Construction 12.37.

该方案的公钥照常包含 $\langle N, e \rangle$，还包含函数 $H : \mathbb{Z}_N^* \to \{0,1\}^n$ 的说明，分析中 $H$ 将被建模为随机预言机。（这个函数可以基于某个底层密码学哈希函数来实现，如 6.5 节所讨论；细节从略。）为了封装密钥，发送方均匀选取 $r \in \mathbb{Z}_N^*$，然后计算密文 $c := [r^e \bmod N]$ 和密钥 $k := H(r)$。解密密文 $c$ 时，接收方只需按通常方式恢复 $r$，再重新导出同样的密钥 $k := H(r)$。见构造 12.37。

CPA-security of the scheme is immediate. Indeed, the ciphertext $c$ is equal to $[r^e \bmod N]$ for uniform $r \in \mathbb{Z}_N^*$, and so the RSA assumption implies that an eavesdropper who observes $c$ will be unable to compute $r$. This means, in turn, that (except with negligible probability) the eavesdropper will not query $r$ to $H$, and thus the value of the key $k \stackrel{\mathrm{def}}{=} H(r)$ will remain uniform from the attacker's point of view.

该方案的选择明文安全性是显然的。事实上，密文 $c$ 等于均匀 $r \in \mathbb{Z}_N^*$ 对应的 $[r^e \bmod N]$，因此由 RSA 假设可知，观察到 $c$ 的窃听者无法计算出 $r$。这又意味着（除去可忽略的概率外）窃听者不会向 $H$ 查询 $r$，从而密钥 $k \stackrel{\mathrm{def}}{=} H(r)$ 的值在攻击者看来保持均匀。

**CONSTRUCTION 12.37**

**构造 12.37**

Let GenRSA be as usual, and construct a KEM as follows:

设 $\mathsf{GenRSA}$ 如常，并如下构造一个 KEM：

- Gen: on input $1^n$, run $\mathsf{GenRSA}(1^n)$ to compute $(N, e, d)$. The public key is $\langle N, e \rangle$, and the private key is $\langle N, d \rangle$.

- Gen：以 $1^n$ 为输入，运行 $\mathsf{GenRSA}(1^n)$ 计算 $(N, e, d)$。公钥为 $\langle N, e \rangle$，私钥为 $\langle N, d \rangle$。

As part of key generation, a function $H: \mathbb{Z}_N^* \to \{0,1\}^n$ is specified, but we leave this implicit.

作为密钥生成的一部分，还要指定一个函数 $H: \mathbb{Z}_N^* \to \{0,1\}^n$，但我们将其隐含处理。

- Encaps: on input public key $\langle N, e \rangle$, choose a uniform $r \in \mathbb{Z}_N^*$. Output the ciphertext $c := [r^e \bmod N]$ and the key $k := H(r)$.

- Encaps：以公钥 $\langle N, e \rangle$ 为输入，均匀选取 $r \in \mathbb{Z}_N^*$。输出密文 $c := [r^e \bmod N]$ 和密钥 $k := H(r)$。

- Decaps: on input private key $\langle N, d \rangle$ and a ciphertext $c \in \mathbb{Z}_N^*$, compute $r := [c^d \bmod N]$ and output the key $k := H(r)$.

- Decaps：以私钥 $\langle N, d \rangle$ 和密文 $c \in \mathbb{Z}_N^*$ 为输入，计算 $r := [c^d \bmod N]$ 并输出密钥 $k := H(r)$。

A CCA-secure KEM (in the random-oracle model).

一个（随机预言机模型中的）选择密文安全 KEM。

In fact, the above extends to show CCA-security as well. This is because answering a decapsulation-oracle query for any ciphertext $\tilde{c} \neq c$ only involves evaluating $H$ at some input $[\tilde{c}^d \bmod N] = \tilde{r} \neq r$. Thus, the attacker's decapsulation-oracle queries do not reveal any additional information about the key $H(r)$ encapsulated by the challenge ciphertext. (A formal proof is slightly more involved since we must show how it is possible to simulate the answers to decapsulation-oracle queries without knowledge of the private key. Nevertheless, this turns out to be not very difficult.)

实际上，上述论证可以直接延伸以证明选择密文安全性。这是因为回答针对任何密文 $\tilde{c} \neq c$ 的解封装预言机查询，只涉及在某个输入 $[\tilde{c}^d \bmod N] = \tilde{r} \neq r$ 处对 $H$ 求值。因此，攻击者的解封装预言机查询不会泄露关于挑战密文所封装密钥 $H(r)$ 的任何额外信息。（形式化证明稍显繁琐，因为我们必须说明如何在不知道私钥的情况下模拟解封装预言机查询的回答。不过事实证明这并不困难。）

THEOREM 12.38 If the RSA problem is hard relative to GenRSA and H is modeled as a random oracle, then Construction 12.37 is CCA-secure.

定理 12.38　如果 RSA 问题相对于 $\mathsf{GenRSA}$ 是困难的且 $H$ 被建模为随机预言机，那么构造 12.37 是选择密文安全的。

PROOF Let $\Pi$ denote Construction 12.37, and let $\mathcal{A}$ be a probabilistic polynomial-time adversary. For convenience, and because this is the first proof where we use the full power of the random-oracle model, we explicitly describe the steps of experiment $\mathsf{KEM}_{\mathcal{A},\Pi}^{\mathsf{cca}}(n)$:

证明　用 $\Pi$ 表示构造 12.37，并设 $\mathcal{A}$ 是概率多项式时间敌手。为方便起见，也由于这是我们首次在证明中动用随机预言机模型的全部威力，我们明确写出实验 $\mathsf{KEM}_{\mathcal{A},\Pi}^{\mathsf{cca}}(n)$ 的各个步骤：

1. $\mathsf{GenRSA}(1^n)$ is run to obtain $(N, e, d)$. In addition, a random function $H: \mathbb{Z}_N^* \to \{0,1\}^n$ is chosen.

   运行 $\mathsf{GenRSA}(1^n)$ 得到 $(N, e, d)$。此外，选取一个随机函数 $H: \mathbb{Z}_N^* \to \{0,1\}^n$。

2. Uniform $r \in \mathbb{Z}_N^*$ is chosen, and the ciphertext $c := [r^e \bmod N]$ and key $k := H(r)$ are computed.

   均匀选取 $r \in \mathbb{Z}_N^*$，计算密文 $c := [r^e \bmod N]$ 和密钥 $k := H(r)$。

3. A uniform bit $b \in \{0,1\}$ is chosen. If $b = 0$ set $\hat{k} := k$. If $b = 1$ then choose a uniform $\hat{k} \in \{0,1\}^n$.

   均匀选取比特 $b \in \{0,1\}$。若 $b = 0$ 则置 $\hat{k} := k$；若 $b = 1$ 则均匀选取 $\hat{k} \in \{0,1\}^n$。

4. $\mathcal{A}$ is given $pk = \langle N, e \rangle$, $c$, and $\hat{k}$, and may query $H(\cdot)$ (on any input) and the decapsulation oracle $\mathsf{Decaps}_{\langle N, d \rangle}(\cdot)$ on any ciphertext $\hat{c} \neq c$.

   将 $pk = \langle N, e \rangle$、$c$ 和 $\hat{k}$ 交给 $\mathcal{A}$；它可以（对任意输入）查询 $H(\cdot)$，并对任意满足 $\hat{c} \neq c$ 的密文查询解封装预言机 $\mathsf{Decaps}_{\langle N, d \rangle}(\cdot)$。

5. A outputs a bit $b^{\prime}$. The output of the experiment is defined to be 1 if $b^{\prime} = b$, and 0 otherwise.

   $\mathcal{A}$ 输出比特 $b^{\prime}$。若 $b^{\prime} = b$ 则实验输出定义为 1；否则为 0。

In an execution of experiment $\mathsf{KEM}_{\mathcal{A},\Pi}^{\mathsf{cca}}(n)$, let $\mathsf{Query}$ be the event that, at any point during its execution, $\mathcal{A}$ queries $r$ to the random oracle $H$. We let $\mathsf{Success}$ denote the event that $b^{\prime} = b$ (i.e., the experiment outputs 1). Then

在实验 $\mathsf{KEM}_{\mathcal{A},\Pi}^{\mathsf{cca}}(n)$ 的一次执行中，令 $\mathsf{Query}$ 表示执行过程中的某一时刻 $\mathcal{A}$ 向随机预言机 $H$ 查询 $r$ 这一事件。令 $\mathsf{Success}$ 表示事件 $b^{\prime} = b$（即实验输出 1）。那么

$$
\begin{aligned}
\Pr[\mathsf{Success}]&=\Pr\left[\mathsf{Success}\land\overline{\mathsf{Query}}\right]+\Pr[\mathsf{Success}\land\mathsf{Query}]\\
&\leq\Pr\left[\mathsf{Success}\land\overline{\mathsf{Query}}\right]+\Pr[\mathsf{Query}],
\end{aligned}
$$

where all probabilities are taken over the randomness used in experiment $\mathsf{KEM}_{\mathcal{A},\Pi}^{\mathsf{cca}}(n)$. We show that $\Pr\left[\mathsf{Success} \wedge \overline{\mathsf{Query}}\right] \leq \frac{1}{2}$ and that $\Pr[\mathsf{Query}]$ is negligible. The theorem follows.

其中所有概率都取遍实验 $\mathsf{KEM}_{\mathcal{A},\Pi}^{\mathsf{cca}}(n)$ 中使用的随机性。我们将证明 $\Pr\left[\mathsf{Success} \wedge \overline{\mathsf{Query}}\right] \leq \frac{1}{2}$，且 $\Pr[\mathsf{Query}]$ 可忽略。定理即得证。

We first argue that $\Pr[\mathsf{Success} \land \overline{\mathsf{Query}}] \leq \frac{1}{2}$. If $\Pr[\mathsf{Query}] = 0$ this is immediate. Otherwise, $\Pr[\mathsf{Success} \land \overline{\mathsf{Query}}] \leq \Pr[\mathsf{Success} \mid \overline{\mathsf{Query}}]$. Now, conditioned on $\overline{\mathsf{Query}}$, the value of the correct key $k = H(r)$ is uniform because $H$ is a random function. Consider $\mathcal{A}$'s information about $k$ in experiment $\mathsf{KEM}_{\mathcal{A}, \Pi}^{\mathsf{cca}}(n)$. The public key $pk$ and ciphertext $c$, by themselves, do not contain any information about $k$. (They do uniquely determine $r$, but since $H$ is chosen independently of anything else, this gives no information about $H(r)$.) Queries that $\mathcal{A}$ makes to $H$ also do not reveal any information about $r$, unless $\mathcal{A}$ queries $r$ to $H$ (in which case $\mathsf{Query}$ occurs); this, again, relies on the fact that $H$ is a random function. Finally, queries that $\mathcal{A}$ makes to its decapsulation oracle only reveal $H(\tilde{r})$ for $\tilde{r} \neq r$. This follows from the fact that $\mathsf{Decaps}_{\langle N, d\rangle}(\tilde{c}) = H(\tilde{r})$ where $\tilde{r} = [\tilde{c}^d \bmod N]$, but $\tilde{c} \neq c$ implies $\tilde{r} \neq r$. Once again, this and the fact that $H$ is a random function mean that no information about $H(r)$ is revealed unless $\mathsf{Query}$ occurs.

我们首先论证 $\Pr[\mathsf{Success} \land \overline{\mathsf{Query}}] \leq \frac{1}{2}$。若 $\Pr[\mathsf{Query}] = 0$，这是显然的。否则，$\Pr[\mathsf{Success} \land \overline{\mathsf{Query}}] \leq \Pr[\mathsf{Success} \mid \overline{\mathsf{Query}}]$。现在，以 $\overline{\mathsf{Query}}$ 为条件，正确密钥 $k = H(r)$ 的值是均匀的，因为 $H$ 是一个随机函数。考虑实验 $\mathsf{KEM}_{\mathcal{A}, \Pi}^{\mathsf{cca}}(n)$ 中 $\mathcal{A}$ 关于 $k$ 的信息。公钥 $pk$ 和密文 $c$ 本身不包含关于 $k$ 的任何信息。（它们确实唯一确定 $r$，但由于 $H$ 的选取独立于其他一切，这不提供关于 $H(r)$ 的任何信息。）$\mathcal{A}$ 对 $H$ 发出的查询同样不会泄露关于 $r$ 的任何信息，除非它向 $H$ 查询了 $r$（此时 $\mathsf{Query}$ 发生）；这再次依赖于 $H$ 是随机函数这一事实。最后，$\mathcal{A}$ 向其解封装预言机发出的查询只会泄露 $\tilde{r} \neq r$ 时的 $H(\tilde{r})$。这是因为 $\mathsf{Decaps}_{\langle N, d\rangle}(\tilde{c}) = H(\tilde{r})$，其中 $\tilde{r} = [\tilde{c}^d \bmod N]$，而 $\tilde{c} \neq c$ 蕴含 $\tilde{r} \neq r$。同样地，这一点连同 $H$ 是随机函数的事实意味着：除非 $\mathsf{Query}$ 发生，否则不会泄露关于 $H(r)$ 的任何信息。

The above shows that, as long as $\mathsf{Query}$ does not occur, the value of the correct key $k$ is uniform even given $\mathcal{A}$'s view of the public key, ciphertext, and the answers to all its oracle queries. In that case, then, there is no way $\mathcal{A}$ can distinguish (any better than random guessing) whether $\hat{k}$ is the correct key or a uniform, independent key. Therefore, $\Pr\left[\mathsf{Success}\mid\overline{\mathsf{Query}}\right] = \frac{1}{2}$.

上面的论述表明：只要 $\mathsf{Query}$ 不发生，即使给定 $\mathcal{A}$ 能看到的公钥、密文以及其所有预言机查询的回答，正确密钥 $k$ 的值仍是均匀的。于是在这种情况下，$\mathcal{A}$ 无从辨别（至多与随机猜测相当）$\hat{k}$ 究竟是正确的密钥还是一个均匀且独立的密钥。因此，$\Pr\left[\mathsf{Success}\mid\overline{\mathsf{Query}}\right] = \frac{1}{2}$。

We highlight that nowhere in the above argument did we rely on the fact that $\mathcal{A}$ is computationally bounded, and in fact $\Pr\left[\mathsf{Success} \land \overline{\mathsf{Query}}\right] \leq \frac{1}{2}$ even if no computational restrictions are placed on $\mathcal{A}$. This indicates part of the power of the random-oracle model.

我们强调，上述论证没有在任何地方用到“$\mathcal{A}$ 的计算能力受限”这一事实；实际上，即使对 $\mathcal{A}$ 不施加任何计算上的限制，$\Pr\left[\mathsf{Success} \land \overline{\mathsf{Query}}\right] \leq \frac{1}{2}$ 也成立。这显示了随机预言机模型威力的一角。

To complete the proof of the theorem, we show

为完成定理的证明，我们来证明

CLAIM 12.39 If the RSA problem is hard relative to GenRSA and H is modeled as a random oracle, then Pr[Query] is negligible.

断言 12.39　如果 RSA 问题相对于 $\mathsf{GenRSA}$ 是困难的且 $H$ 被建模为随机预言机，那么 Pr[Query] 可忽略。

To prove this, we construct an algorithm $\mathcal{A}^{\prime}$ that uses $\mathcal{A}$ as a subroutine. $\mathcal{A}^{\prime}$ is given an instance $N, e, c$ of the RSA problem, and its goal is to compute $r$ for which $r^e = c \bmod N$. To do so, it will run $\mathcal{A}$, answering its queries to $H$ and Decaps. Handling queries to $H$ is simple, since $\mathcal{A}^{\prime}$ can just return a random value. Queries to Decaps are trickier, however, since $\mathcal{A}^{\prime}$ does not know the private key associated with the effective public key $\langle N, e \rangle$.

为证明这一点，我们构造一个以 $\mathcal{A}$ 为子例程的算法 $\mathcal{A}^{\prime}$。$\mathcal{A}^{\prime}$ 拿到 RSA 问题的一个实例 $N, e, c$，其目标是计算出满足 $r^e = c \bmod N$ 的 $r$。为此，它将运行 $\mathcal{A}$，回答其对 $H$ 和 Decaps 的查询。处理对 $H$ 的查询很简单，因为 $\mathcal{A}^{\prime}$ 只需返回一个随机值即可。然而对 Decaps 的查询更棘手，因为 $\mathcal{A}^{\prime}$ 不知道与有效公钥 $\langle N, e \rangle$ 相关联的私钥。

On further thought, however, decapsulation queries are also easy to answer since $\mathcal{A}^{\prime}$ can just return a random value here as well. That is, although the query $\mathsf{Decaps}(\tilde{c})$ is supposed to be computed by first computing $\tilde{r}$ such that $\tilde{r}^e = \tilde{c} \bmod N$ and then evaluating $H(\tilde{r})$, the result is just a uniform value. Thus, $\mathcal{A}^{\prime}$ can simply return a random value without performing the intermediate computation. The only “catch” is that $\mathcal{A}^{\prime}$ must ensure consistency between its answers to $H$-queries and $\mathsf{Decaps}$-queries; namely, it must ensure that for any $\tilde{r}$, $\tilde{c}$ with $\tilde{r}^e = \tilde{c} \bmod N$ it holds that $H(\tilde{r}) = \mathsf{Decaps}(\tilde{c})$. This is handled using simple bookkeeping and lists $L_H$ and $L_{\mathsf{Decaps}}$ that keep track of the answers $\mathcal{A}^{\prime}$ has given in response to the respective oracle queries. We now give the details.

但进一步思考便会发现，解封装查询其实同样容易回答，因为 $\mathcal{A}^{\prime}$ 在这里也可以直接返回一个随机值。也就是说，虽然查询 $\mathsf{Decaps}(\tilde{c})$ 本应先计算满足 $\tilde{r}^e = \tilde{c} \bmod N$ 的 $\tilde{r}$、再对 $H(\tilde{r})$ 求值来得到答案，但其结果只是一个均匀值。因此，$\mathcal{A}^{\prime}$ 可以不做中间计算而直接返回随机值。唯一的“麻烦”在于：$\mathcal{A}^{\prime}$ 必须保证对 $H$ 查询和对 $\mathsf{Decaps}$ 查询的回答彼此一致；具体地说，它必须保证对任意满足 $\tilde{r}^e = \tilde{c} \bmod N$ 的 $\tilde{r}, \tilde{c}$ 都有 $H(\tilde{r}) = \mathsf{Decaps}(\tilde{c})$。这一点可以用简单的簿记以及列表 $L_H$ 和 $L_{\mathsf{Decaps}}$ 来处理，它们分别记录 $\mathcal{A}^{\prime}$ 对相应预言机查询已给出的回答。下面给出细节。

**Algorithm $\mathcal{A}'$:**

**算法 $\mathcal{A}'$：**

The algorithm is given $(N, e, c)$ as input.

该算法以 $(N, e, c)$ 为输入。

1. Initialize empty lists $L_H$, $L_{\mathsf{Decaps}}$. Choose a uniform $k \in \{0,1\}^n$ and store $(c,k)$ in $L_{\mathsf{Decaps}}$.

   初始化空列表 $L_H$、$L_{\mathsf{Decaps}}$。均匀选取 $k \in \{0,1\}^n$，并把 $(c,k)$ 存入 $L_{\mathsf{Decaps}}$。

2. Choose a uniform bit $b \in \{0,1\}$. If $b = 0$ set $\hat{k} := k$. If $b = 1$ then choose a uniform $\hat{k} \in \{0,1\}^n$. Run $\mathcal{A}$ on $\langle N,e\rangle$, $c$, and $\hat{k}$.

   均匀选取比特 $b \in \{0,1\}$。若 $b = 0$ 则置 $\hat{k} := k$；若 $b = 1$ 则均匀选取 $\hat{k} \in \{0,1\}^n$。以 $\langle N,e\rangle$、$c$ 和 $\hat{k}$ 运行 $\mathcal{A}$。

When $\mathcal{A}$ makes a query $H(\tilde{r})$, answer it as follows:

当 $\mathcal{A}$ 发出查询 $H(\tilde{r})$ 时，按如下方式回答：

- If there is an entry in $L_{H}$ of the form $(\tilde{r}, k)$ for some $k$, return $k$.

  若 $L_{H}$ 中存在形如 $(\tilde{r}, k)$（$k$ 为某个值）的条目，则返回 $k$。

- Otherwise, let $\tilde{c} := [\tilde{r}^{e} \bmod N]$. If there is an entry in $L_{\mathsf{Decaps}}$ of the form $(\tilde{c}, k)$ for some $k$, return $k$ and store $(\tilde{r}, k)$ in $L_{H}$.

  否则，令 $\tilde{c} := [\tilde{r}^{e} \bmod N]$。若 $L_{\mathsf{Decaps}}$ 中存在形如 $(\tilde{c}, k)$（$k$ 为某个值）的条目，则返回 $k$，并把 $(\tilde{r}, k)$ 存入 $L_{H}$。

- Otherwise, choose a uniform $k \in \{0,1\}^n$, return $k$, and store $(\tilde{r}, k)$ in $L_H$.

  否则，均匀选取 $k \in \{0,1\}^n$，返回 $k$，并把 $(\tilde{r}, k)$ 存入 $L_H$。

When $\mathcal{A}$ makes a query $\mathsf{Decaps}(\tilde{c})$, answer it as follows:

当 $\mathcal{A}$ 发出查询 $\mathsf{Decaps}(\tilde{c})$ 时，按如下方式回答：

- If there is an entry in $L_{\mathsf{Decaps}}$ of the form $(\tilde{c}, k)$ for some $k$, return $k$.

  若 $L_{\mathsf{Decaps}}$ 中存在形如 $(\tilde{c}, k)$（$k$ 为某个值）的条目，则返回 $k$。

- Otherwise, for each entry $(\tilde{r}, k) \in L_H$, check if $\tilde{r}^e = \tilde{c} \bmod N$ and, if so, output k.

  否则，对 $L_H$ 中的每个条目 $(\tilde{r}, k)$，检验是否 $\tilde{r}^e = \tilde{c} \bmod N$；若是，则输出 k。

- Otherwise, choose a uniform $k \in \{0,1\}^{n}$, return k, and store $(\tilde{c}, k)$ in $L_{\mathsf{Decaps}}$.

  否则，均匀选取 $k \in \{0,1\}^{n}$，返回 k，并把 $(\tilde{c}, k)$ 存入 $L_{\mathsf{Decaps}}$。

3. At the end of $\mathcal{A}$'s execution, if there is an entry $(r,k)$ in $L_H$ for which $r^e = c \bmod N$ then return $r$.

   在 $\mathcal{A}$ 执行结束时，若 $L_H$ 中存在满足 $r^e = c \bmod N$ 的条目 $(r,k)$，则返回 $r$。

Clearly $\mathcal{A}^{\prime}$ runs in polynomial time, and the view of $\mathcal{A}$ when run as a subroutine by $\mathcal{A}^{\prime}$ in experiment $\mathsf{RSA\text{-}inv}_{\mathcal{A}^{\prime}, \mathsf{GenRSA}}(n)$ is identical to the view of $\mathcal{A}$ in experiment $\mathsf{KEM}_{\mathcal{A},\Pi}^{\mathsf{cca}}(n)$: the inputs given to $\mathcal{A}$ clearly have the right distribution, the answers to $\mathcal{A}^{\prime}$'s oracle queries are consistent, and the responses to all $H$-queries are uniform and independent. Finally, $\mathcal{A}^{\prime}$ outputs the correct solution exactly when Query occurs. Hardness of the RSA problem relative to GenRSA thus implies that $\Pr[\mathsf{Query}]$ is negligible, as required.

显然 $\mathcal{A}^{\prime}$ 的运行时间是多项式的，而且在实验 $\mathsf{RSA\text{-}inv}_{\mathcal{A}^{\prime}, \mathsf{GenRSA}}(n)$ 中作为 $\mathcal{A}^{\prime}$ 的子例程运行时，$\mathcal{A}$ 的视图与其在实验 $\mathsf{KEM}_{\mathcal{A},\Pi}^{\mathsf{cca}}(n)$ 中的视图完全相同：交给 $\mathcal{A}$ 的输入显然具有正确的分布，$\mathcal{A}^{\prime}$ 对预言机查询的回答是一致的，并且所有 $H$ 查询的回答都是均匀且独立的。最后，$\mathcal{A}^{\prime}$ 恰好在 Query 发生时输出正确解。于是，RSA 问题相对于 $\mathsf{GenRSA}$ 的困难性蕴含 $\Pr[\mathsf{Query}]$ 可忽略，证毕。

It is worth remarking on the various properties of the random-oracle model (see Section 6.5.1) that are used in the above proof. First, we rely on the fact that the value $H(r)$ is uniform unless $r$ is queried to $H$—even if $H$ is queried on multiple other values $\tilde{r} \neq r$. We also, implicitly, use extractability to argue that the attacker cannot query r to H; otherwise, we could use this attacker to solve the RSA problem. Finally, the proof relies on programmability in order to simulate the adversary's decapsulation-oracle queries.

值得一提的是上述证明用到的随机预言机模型的各种性质（见 6.5.1 节）。首先，我们依赖于这样一个事实：除非 $r$ 被查询给 $H$，否则 $H(r)$ 的值是均匀的——即便 $H$ 已在其他多个值 $\tilde{r} \neq r$ 上被查询过也是如此。我们还隐式地利用可提取性来论证攻击者无法向 $H$ 查询 r；否则，我们就可以利用这样的攻击者求解 RSA 问题。最后，证明还依赖可编程性来模拟敌手的解封装预言机查询。

### 12.5.6 RSA Implementation Issues and Pitfalls　RSA 的实现问题与陷阱

We close this section with a brief discussion of some issues related to the implementation of RSA-based schemes, and some pitfalls to be aware of.

本节结尾简要讨论与基于 RSA 的方案的实现相关的一些问题，以及一些需要留意的陷阱。

**Using Chinese remaindering.**

**使用中国剩余定理。**

In implementations of RSA-based encryption, the receiver can use the Chinese remainder theorem (Section 9.1.5) to speed up computation of $e$th roots modulo N during decryption. Specifically, let $N = pq$ and say the receiver wishes to compute the $e$th root of some value $y$ using $d = [e^{-1} \bmod \phi(N)]$. The receiver can use the correspondence $[y^d \bmod N] \leftrightarrow ([y^d \bmod p], [y^d \bmod q])$ to compute the partial results

在基于 RSA 加密的实现中，接收方可以利用中国剩余定理（9.1.5 节）来加速解密时模 N 的 $e$ 次根的计算。具体地说，设 $N = pq$，接收方想利用 $d = [e^{-1} \bmod \phi(N)]$ 计算某个值 $y$ 的 $e$ 次根。接收方可以利用对应关系 $[y^d \bmod N] \leftrightarrow ([y^d \bmod p], [y^d \bmod q])$ 先计算部分结果

$$
x_{p}:=[y^{d}\bmod p]=\left[y^{\left[d\bmod(p-1)\right]}\bmod p\right] \tag{12.19}
$$

and

和

$$
x_{q}:=[y^{d}\bmod q]=\left[y^{[d\bmod(q-1)]}\bmod q\right], \tag{12.20}
$$

and then combine these to obtain $x \leftrightarrow (x_p, x_q)$, as discussed in Section 9.1.5.

然后把二者组合起来得到 $x \leftrightarrow (x_p, x_q)$，如 9.1.5 节所述。

Note that $[d \bmod (p-1)]$ and $[d \bmod (q-1)]$ could be pre-computed since they are independent of y.

注意，$[d \bmod (p-1)]$ 和 $[d \bmod (q-1)]$ 可以预先算好，因为它们与 y 无关。

Why is this better? Assume exponentiation modulo an $\ell$-bit integer takes $\gamma \cdot \ell^3$ operations for some constant $\gamma$. If $p, q$ are each $n$ bits long, then naively computing $[y^d \bmod N]$ takes $\gamma \cdot (2n)^3 = 8\gamma \cdot n^3$ steps (because $\|N\| = 2n$). Using Chinese remainder reduces this to roughly $2 \cdot (\gamma \cdot n^3)$ steps (because $\|p\| = \|q\| = n$), or roughly $1/4$ of the time.

为什么这样更好？假设对一个 $\ell$ 比特整数做模幂运算需要 $\gamma \cdot \ell^3$ 次操作，其中 $\gamma$ 为常数。如果 $p, q$ 各长 $n$ 比特，那么朴素地计算 $[y^d \bmod N]$ 需要 $\gamma \cdot (2n)^3 = 8\gamma \cdot n^3$ 步（因为 $\|N\| = 2n$）。使用中国剩余定理可将此降至约 $2 \cdot (\gamma \cdot n^3)$ 步（因为 $\|p\| = \|q\| = n$），即约为原来的 $1/4$ 时间。

**Example 12.40**

**例 12.40**

We revisit Example 9.49. Recall that $N = 143 = 11 \cdot 13$ and $d = 103$, and $y = 64$ there. To calculate $[64^{103} \bmod 143]$ we compute

我们重新考察例 9.49。回忆那里有 $N = 143 = 11 \cdot 13$、$d = 103$、$y = 64$。为计算 $[64^{103} \bmod 143]$，我们先算出

$$
\begin{aligned}
\left(\left[64\bmod11\right],\left[64\bmod13\right]\right)^{103}&=\left(\left[\left(-2\right)^{103}\bmod11\right],\left[\left(-1\right)^{103}\bmod13\right]\right)\\
&=\left(\left[\left(-2\right)^{\left[103\bmod10\right]}\bmod11\right],-1\right)\\
&=\left(\left[-8\bmod11\right],-1\right)=(3,-1).
\end{aligned}
$$

We can compute $1_p = 78 \leftrightarrow (1,0)$ and $1_q = 66 \leftrightarrow (0,1)$, as discussed in Section 9.1.5. (Note these values can be pre-computed, as they are independent of $y$.) Then $(3,-1) \leftrightarrow 3 \cdot 1_p - 1_q = 3 \cdot 78 - 66 = 168 = 25 \bmod 143$, in agreement with the answer previously obtained.

如 9.1.5 节所述，我们可以计算出 $1_p = 78 \leftrightarrow (1,0)$ 和 $1_q = 66 \leftrightarrow (0,1)$。（注意这些值与 $y$ 无关，因而可以预先计算。）于是 $(3,-1) \leftrightarrow 3 \cdot 1_p - 1_q = 3 \cdot 78 - 66 = 168 = 25 \bmod 143$，与前文得到的答案一致。

**A fault attack when using Chinese remaindering.**

**使用中国剩余定理时的故障攻击。**

When using Chinese remaindering as just described, one should be aware of a potential attack that can be carried out if faults occur (or can be induced to occur by an attacker, e.g., by hardware tampering) during the course of the computation.

在按刚才所述使用中国剩余定理时，应当警惕一种潜在攻击：如果在计算过程中发生故障（或攻击者能够诱发故障，例如通过硬件篡改），该攻击便可实施。

Consider what happens if $[y^d \bmod N]$ is computed twice: the first time with no error (giving the correct result $x$), but the second time with an error during computation of Equation (12.20) but not Equation (12.19) (the same attack applies in the opposite case). The second computation yields an incorrect result $x^{\prime}$ for which $x^{\prime} = x \bmod p$ but $x^{\prime} \neq x \bmod q$. This means that $p \mid (x^{\prime} - x)$ but $q \not\mid (x^{\prime} - x)$. But then $\gcd(x^{\prime} - x, N) = p$, yielding the factorization of $N$.

考虑如果把 $[y^d \bmod N]$ 计算两次会发生什么：第一次没有出错（得到正确结果 $x$），第二次在计算式 (12.20) 时出错而在式 (12.19) 上没有出错（反向情形同理可行）。第二次计算给出一个错误结果 $x^{\prime}$，满足 $x^{\prime} = x \bmod p$ 但 $x^{\prime} \neq x \bmod q$。这意味着 $p \mid (x^{\prime} - x)$ 而 $q \not\mid (x^{\prime} - x)$。于是 $\gcd(x^{\prime} - x, N) = p$，从而得到了 $N$ 的因子分解。

One possible countermeasure is to verify correctness of the result before using it, by checking that $x^e = y \bmod N$. (Since $\|e\| \ll \|d\|$, using Chinese remaindering still gives better efficiency.) This is recommended in hardware implementations.

一种可能的对策是在使用结果之前验证其正确性，即检验 $x^e = y \bmod N$ 是否成立。（由于 $\|e\| \ll \|d\|$，使用中国剩余定理仍能带来更高的效率。）硬件实现中建议采用这一做法。

Dependent public keys I. When multiple receivers wish to utilize the same encryption scheme, they should use independent public keys. This and the following attack demonstrate what can go wrong when this is not done.

**相关联的公钥 I。** 当多个接收方希望使用同一个加密方案时，他们应当使用相互独立的公钥。本段以及下一段的攻击说明了不这样做会导致什么问题。

Imagine a company wants to use the same modulus $N$ for each of its employees. Since it is not desirable for messages encrypted to one employee to be read by any other employee, the company issues different $(e_i, d_i)$ pairs to each employee. That is, the public key of the $i$th employee is $pk_i = \langle N, e_i \rangle$ and their private key is $sk = \langle N, d_i \rangle$, where $e_i \cdot d_i = 1 \bmod \phi(N)$ for all $i$.

设想一家公司想让其所有员工共用同一个模数 $N$。由于发给某位员工的加密消息不应被任何其他员工读懂，公司为每位员工发放不同的 $(e_i, d_i)$ 对。也就是说，第 $i$ 位员工的公钥是 $pk_i = \langle N, e_i \rangle$，私钥是 $sk = \langle N, d_i \rangle$，其中对所有 $i$ 都有 $e_i \cdot d_i = 1 \bmod \phi(N)$。

This approach is insecure and allows any employee to read messages encrypted to all other employees. The reason is that, as noted in Section 9.2.4, given $N$ and $e_i$, $d_i$ with $e_i \cdot d_i = 1 \bmod \phi(N)$, the factorization of $N$ can be efficiently computed. Given the factorization of $N$, of course, it is possible to compute $d_j := e_j^{-1} \bmod \phi(N)$ for any $j$.

这种做法是不安全的：它使任意员工都能读到加密发给所有其他员工的消息。原因在于，正如 9.2.4 节所指出的，给定 $N$ 以及满足 $e_i \cdot d_i = 1 \bmod \phi(N)$ 的 $e_i, d_i$，就可以高效算出 $N$ 的因子分解。而一旦得到 $N$ 的因子分解，当然就能对任意 $j$ 计算 $d_j := e_j^{-1} \bmod \phi(N)$。

Dependent public keys II. The attack just shown allows any employee to decrypt messages sent to any other employee. This still leaves the possibility that sharing the modulus $N$ is fine as long as all employees trust each other (or, alternatively, as long as confidentiality need only be preserved against outsiders but not against other members of the company). Here we show a scenario indicating that sharing a modulus is still a bad idea, at least when plain RSA encryption is used.

**相关联的公钥 II。** 刚才展示的攻击使任意员工都能解密发给任何其他员工的消息。这仍然留下这样一种可能：只要所有员工互相信任（或者说，只要保密性只需抵御外部人员、不需抵御公司内部的其他成员），共享模数 $N$ 就没什么问题。这里我们给出一个场景，表明共享模数仍然是个坏主意——至少在使用朴素 RSA 加密时如此。

Say the same message $m$ is encrypted and sent to two different (known) employees with public keys $(N, e_1)$ and $(N, e_2)$ where $e_1 \neq e_2$. Assume further that $\gcd(e_1, e_2) = 1$. Then an eavesdropper sees the two ciphertexts

设同一条消息 $m$ 被加密并发送给两个不同的（已知）员工，其公钥分别为 $(N, e_1)$ 和 $(N, e_2)$，其中 $e_1 \neq e_2$。进一步假设 $\gcd(e_1, e_2) = 1$。那么窃听者会看到两个密文

$$
c_{1}=m^{e_{1}}\bmod N\quad\text{and}\quad c_{2}=m^{e_{2}}\bmod N.
$$

Since $\gcd(e_1, e_2) = 1$, there exist integers $X, Y$ such that $X e_1 + Y e_2 = 1$ by Proposition 9.2. Moreover, given the public exponents $e_1$ and $e_2$ it is possible to efficiently compute $X$ and $Y$ using the extended Euclidean algorithm (see Appendix B.1.2). We claim that $m = [c_1^X \cdot c_2^Y \bmod N]$, which can easily be calculated. This is true because

由于 $\gcd(e_1, e_2) = 1$，由命题 9.2 可知存在整数 $X, Y$ 使得 $X e_1 + Y e_2 = 1$。而且给定公开指数 $e_1$ 和 $e_2$，可以用扩展欧几里得算法（见附录 B.1.2）高效算出 $X$ 和 $Y$。我们断言 $m = [c_1^X \cdot c_2^Y \bmod N]$，而这很容易计算。理由如下：

$$
c_{1}^{X}\cdot c_{2}^{Y}=m^{X e_{1}}m^{Y e_{2}}=m^{X e_{1}+Y e_{2}}=m^{1}=m\bmod N.
$$

A similar attack applies when using padded RSA or RSA-OAEP if the sender uses the same transformed message $\hat{m}$ when encrypting to two users.

如果发送方向两个用户加密时使用了相同的变换后消息 $\hat{m}$，那么类似的攻击也适用于填充 RSA 或 RSA-OAEP。

**Randomness quality in RSA key generation.**

**RSA 密钥生成中的随机性质量。**

Throughout this book, we always assume that honest parties have access to sufficient, high-quality randomness. When this assumption is violated then security may fail to hold. For example, if an $\ell$-bit string is chosen from some set $S \subset \{0,1\}^{\ell}$ rather than uniformly from $\{0,1\}^{\ell}$, then an attacker can perform a brute-force search (in time $\mathcal{O}(|S|)$) to attack the system.

在整本书中，我们总是假设诚实各方能够获得充足的高质量随机性。当这一假设被违反时，安全性就可能失效。例如，如果一个 $\ell$ 比特串是从某个集合 $S \subset \{0,1\}^{\ell}$ 而非从 $\{0,1\}^{\ell}$ 中均匀选出的，攻击者就可以进行暴力搜索（耗时 $\mathcal{O}(|S|)$）来攻击系统。

In some cases the situation may be even worse. Consider in particular the case of RSA key generation, where random bits $r_p$ is used to choose the first prime $p$, and random bits $r_q$ is used to generate the second prime $q$. Assume further that many public/private keys are generated using the same source of poor-quality randomness, in which $r_p, r_q$ are each chosen uniformly from some set $S$ of size $2^s$. After generating roughly $2^{s/2}$ public keys (see Appendix A.4), we expect to obtain two different moduli $N, N^{\prime}$ that were generated using identical randomness $r_p = r_p^{\prime}$ but different randomness $r_q \neq r_q^{\prime}$. These two moduli share a prime factor which can be easily found by computing $\gcd(N, N^{\prime})$. An attacker can attempt to exploit this by scraping the Internet for a large set of RSA public keys, computing their pairwise gcds, and thus hoping to factor some subset of them. Although computing pairwise gcds of $2^{s/2}$ moduli would naively take time $\mathcal{O}(2^s)$, it turns out that this can be significantly improved using a “divide-and-conquer” approach that is beyond the scope of this book. The upshot is that an attacker can factor a small number of public moduli in time less than $2^s$. Note also that the attack works even if the set $S$ is unknown to the attacker.

在某些情况下，情形可能更糟。特别考虑 RSA 密钥生成的情形：用随机比特 $r_p$ 选出第一个素数 $p$，用随机比特 $r_q$ 生成第二个素数 $q$。进一步假设许多公钥/私钥是用同一个低质量的随机性来源生成的，其中 $r_p, r_q$ 各自从某个大小为 $2^s$ 的集合 $S$ 中均匀选出。在生成约 $2^{s/2}$ 个公钥之后（见附录 A.4），我们可以期望得到两个不同的模数 $N, N^{\prime}$，它们是用相同的随机性 $r_p = r_p^{\prime}$ 但不同的随机性 $r_q \neq r_q^{\prime}$ 生成的。这两个模数共享一个素因子，通过计算 $\gcd(N, N^{\prime})$ 就能轻易找到它。攻击者可以尝试加以利用：从互联网上抓取大量 RSA 公钥，计算它们的两两 gcd，从而有望分解其中的一部分。虽然朴素地计算 $2^{s/2}$ 个模数的两两 gcd 需要 $\mathcal{O}(2^s)$ 时间，但事实证明，利用一种超出本书范围的“分治”方法可以显著改进这一点。其结果是，攻击者可以在少于 $2^s$ 的时间内分解少量公开的模数。还要注意，即使攻击者不知道集合 $S$，该攻击依然奏效。

The above scenario was verified experimentally by two research teams working independently, who carried out exactly the above attack on public keys obtained over the Internet, and were able to successfully factor a significant fraction of the keys they found.

上述场景已被两个独立工作的研究团队通过实验证实：他们对从互联网上获取的公钥实施了恰如上述的攻击，并成功分解了其所找到密钥中的相当一部分。

## References and Additional Reading　参考文献与延伸阅读

The idea of public-key encryption was first proposed in the open literature by Diffie and Hellman [65]. Rivest, Shamir, and Adleman [171] introduced the RSA assumption and proposed a public-key encryption scheme based on this assumption. As pointed out in the previous chapter, other pioneers of public-key cryptography include Merkle and Rabin (in academic publications) and Ellis, Cocks, and Williamson (in classified publications).

公钥加密的思想最早由 Diffie 和 Hellman [65] 在公开文献中提出。Rivest、Shamir 和 Adleman [171] 提出了 RSA 假设，并基于该假设给出了一个公钥加密方案。正如上一章所指出的，公钥密码学的其他先驱还包括 Merkle 和 Rabin（见于学术出版物），以及 Ellis、Cocks 和 Williamson（见于涉密出版物）。

Definition 12.2 is rooted in the seminal work of Goldwasser and Micali [87], who were also the first to recognize the necessity of probabilistic encryption for satisfying this definition. As noted in Chapter 4, chosen-ciphertext attacks were first formally defined by Naor and Yung [147] and Rackoff and Simon [168]. The expository article by Shoup [180] discusses the importance of security against chosen-ciphertext attacks. Bellare et al. give a unified, modern treatment of various security notions for public-key encryption [18].

定义 12.2 根植于 Goldwasser 和 Micali [87] 的开创性工作；他们也是最早认识到必须采用概率加密才能满足该定义的人。如第 4 章所述，选择密文攻击最早由 Naor 和 Yung [147] 以及 Rackoff 和 Simon [168] 正式定义。Shoup [180] 的综述文章讨论了抵御选择密文攻击的重要性。Bellare 等人对公钥加密的各种安全性概念给出了统一的现代论述 [18]。

A proof of CPA-security for hybrid encryption was first given by Blum and Goldwasser [40]. The case of CCA-security was treated in [63].

混合加密选择明文安全性的证明最早由 Blum 和 Goldwasser [40] 给出；选择密文安全的情形则在 [63] 中处理。

Somewhat amazingly, the El Gamal encryption scheme [77] was not suggested until 1984, even though it can be viewed as a direct transformation of the Diffie–Hellman key-exchange protocol (see Exercise 12.4). DHIES was introduced in [2]. The ISO/IEC 18033-2 standard for public-key encryption can be found at http://www.shoup.net/iso.

有点令人惊讶的是，El Gamal 加密方案 [77] 直到 1984 年才被提出，尽管它可以看作是对 Diffie–Hellman 密钥交换协议的直接改造（见习题 12.4）。DHIES 出自 [2]。公钥加密的 ISO/IEC 18033-2 标准可在 http://www.shoup.net/iso 找到。

Plain RSA encryption corresponds to the original scheme introduced by Rivest, Shamir, and Adleman [171]. The attacks on plain RSA encryption described in Section 12.5.1 are due to [186, 62, 92, 55, 44]; see [137, Chapter 8] and [42] for additional attacks and further information. Proofs of Coppersmith's theorem can be found in the original work [54] or several subsequent expositions (e.g., [76, 135]).

朴素 RSA 加密对应于 Rivest、Shamir 和 Adleman [171] 最初提出的方案。12.5.1 节描述的对朴素 RSA 加密的攻击出自 [186, 62, 92, 55, 44]；更多攻击与更多信息见 [137, Chapter 8] 和 [42]。Coppersmith 定理的证明可见原始工作 [54]，或若干后续阐述（如 [76, 135]）。

The PKCS #1 standards are available as RFCs [107, 108, 145]. For progress toward proving security of the padded RSA encryption scheme, see the work of Smith and Zhang [189]. The chosen-plaintext attack on PKCS #1 v1.5 described here is due to Coron et al. [57]. A description of Bleichenbacher's chosen-ciphertext attack on PKCS #1 v1.5 can be found in the original paper [38]. See the work of Bardou et al. [13] for subsequent improvements.

PKCS #1 标准以 RFC 形式发布 [107, 108, 145]。关于证明填充 RSA 加密方案安全性的进展，见 Smith 和 Zhang [189] 的工作。这里描述的对 PKCS #1 v1.5 的选择明文攻击出自 Coron 等人 [57]。Bleichenbacher 对 PKCS #1 v1.5 的选择密文攻击的描述可见原始论文 [38]；后续改进见 Bardou 等人 [13] 的工作。

Proofs of Theorem 12.31, and generalizations, can be found in [8, 94, 73, 7]. See Section 15.1.2 for a general treatment of schemes of this form. Construction 12.37 appears to have been introduced and first analyzed by Shoup [181]. OAEP was introduced by Bellare and Rogaway [25]. The original proof of security for OAEP was later found to be flawed; other proofs have since been given [43, 182, 75]. For details of Manger's chosen-ciphertext attack on implementations of PKCS #1 v2.0, see [133].

定理 12.31 的证明及其推广可见 [8, 94, 73, 7]。对这类方案的一般性论述见 15.1.2 节。构造 12.37 似乎是由 Shoup [181] 引入并首次分析的。OAEP 由 Bellare 和 Rogaway [25] 提出。OAEP 原始的安全性证明后来被发现有缺陷；此后又有其他证明给出 [43, 182, 75]。Manger 对 PKCS #1 v2.0 实现的选择密文攻击的详情见 [133]。

The pairwise-gcd attack described in Section 12.5.6 was carried out by Lenstra et al. [125] and Heninger et al. [96].

12.5.6 节描述的两两 gcd 攻击由 Lenstra 等人 [125] 以及 Heninger 等人 [96] 实施。

When using any encryption scheme in practice, the question arises as to what key length to use. This issue should not be taken lightly, and we refer the reader to Section 10.4 and references therein for an in-depth treatment.

在实践中使用任何加密方案时，都会产生应当使用多长密钥的问题。这个问题不容轻视，深入的讨论请读者参阅 10.4 节及相关文献。

The first efficient CCA-secure public-key encryption scheme not relying on the random-oracle model was shown by Cramer and Shoup [58] based on the DDH assumption. Subsequently, Hoffheinz and Kiltz have shown an efficient CCA-secure scheme without random oracles based on the RSA assumption [100].

第一个不依赖随机预言机模型的高效选择密文安全公钥加密方案由 Cramer 和 Shoup [58] 基于 DDH 假设给出。随后，Hoffheinz 和 Kiltz 基于 RSA 假设给出了一个无需随机预言机的高效选择密文安全方案 [100]。

## Exercises　习题

12.1 Assume a public-key encryption scheme for single-bit messages with no decryption error. Show that, given $pk$ and a ciphertext $c$ computed via $c \leftarrow \mathsf{Enc}_{pk}(m)$, it is possible for an unbounded adversary to determine $m$ with probability 1.

12.1 假设有一个针对单比特消息、且无解密错误的公钥加密方案。证明：给定 $pk$ 和经 $c \leftarrow \mathsf{Enc}_{pk}(m)$ 计算出的密文 $c$，无界敌手能够以概率 1 确定 $m$。

12.2 Show that for any CPA-secure public-key encryption scheme for single-bit messages, the length of the ciphertext must be superlogarithmic in the security parameter.

12.2 证明：对任何针对单比特消息的选择明文安全公钥加密方案，密文长度必须是安全参数的超对数函数。

Hint: If not, the range of possible ciphertexts has polynomial size.

提示：否则，所有可能密文构成的集合规模为多项式。

12.3 Say a public-key encryption scheme $(\mathsf{Gen}, \mathsf{Enc}, \mathsf{Dec})$ is one-way if any PPT adversary $\mathcal{A}$ has negligible probability of success in the following experiment:

12.3 称公钥加密方案 $(\mathsf{Gen}, \mathsf{Enc}, \mathsf{Dec})$ 是单向的，如果任何 PPT 敌手 $\mathcal{A}$ 在以下实验中的成功概率都可忽略：

$\mathsf{Gen}(1^{n})$ is run to obtain keys $(pk, sk)$.

运行 $\mathsf{Gen}(1^{n})$ 得到密钥 $(pk, sk)$。

- A uniform message $m$ in the message space is chosen, and a ciphertext $c \leftarrow \mathsf{Enc}_{pk}(m)$ is computed.

- 在消息空间中均匀选取一条消息 $m$，并计算密文 $c \leftarrow \mathsf{Enc}_{pk}(m)$。

- $\mathcal{A}$ is given $pk$ and $c$, and outputs a message $m^{\prime}$. We say $\mathcal{A}$ succeeds if $m^{\prime} = m$.

- 将 $pk$ 和 $c$ 交给 $\mathcal{A}$，$\mathcal{A}$ 输出消息 $m^{\prime}$。若 $m^{\prime} = m$ 则称 $\mathcal{A}$ 成功。

(a) Construct a CPA-secure KEM in the random-oracle model based on a one-way public-key encryption scheme with message space $\{0,1\}^{n}$.

(a) 在随机预言机模型中，基于一个消息空间为 $\{0,1\}^{n}$ 的单向公钥加密方案构造一个选择明文安全的 KEM。

(b) Can a deterministic public-key encryption scheme be one-way? If not, prove impossibility; if so, give a construction based on any of the assumptions introduced in this book.

(b) 确定性的公钥加密方案可能是单向的吗？若不可能，证明其不可能性；若可能，基于本书引入的任一假设给出一个构造。

12.4 Show that any two-round key-exchange protocol (that is, where each party sends a single message) satisfying Definition 11.1 can be converted into a CPA-secure public-key encryption scheme.

12.4 证明：任何满足定义 11.1 的两轮密钥交换协议（即每一方只发送一条消息的协议）都可以转换为选择明文安全的公钥加密方案。

12.5 Show that Claim 12.7 does not hold in the setting of CCA-security.

12.5 证明断言 12.7 在选择密文安全的设定下不成立。

12.6 Consider the following public-key encryption scheme. The public key is $(\mathbb{G}, q, g, h)$ and the private key is x, generated exactly as in the El Gamal encryption scheme. In order to encrypt a bit b, the sender does the following:

12.6 考虑如下公钥加密方案。公钥是 $(\mathbb{G}, q, g, h)$，私钥是 x，二者完全按照 El Gamal 加密方案的方式生成。为了加密比特 b，发送方如下操作：

(a) If $b = 0$ then choose a uniform $y \in \mathbb{Z}_q$ and compute $c_1 := g^y$ and $c_2 := h^y$. The ciphertext is $\langle c_1, c_2 \rangle$.

(a) 若 $b = 0$，则均匀选取 $y \in \mathbb{Z}_q$，计算 $c_1 := g^y$ 和 $c_2 := h^y$。密文为 $\langle c_1, c_2 \rangle$。

(b) If $b = 1$ then choose independent uniform $y, z \in \mathbb{Z}_q$, compute $c_1 := g^y$ and $c_2 := g^z$, and set the ciphertext equal to $\langle c_1, c_2 \rangle$.

(b) 若 $b = 1$，则独立地均匀选取 $y, z \in \mathbb{Z}_q$，计算 $c_1 := g^y$ 和 $c_2 := g^z$，并把密文取为 $\langle c_1, c_2 \rangle$。

Show that it is possible to decrypt efficiently given knowledge of x. Prove that this encryption scheme is CPA-secure if the decisional Diffie–Hellman problem is hard relative to G.

证明：在已知 x 的情况下可以高效解密。并证明：如果判定性 Diffie–Hellman 问题相对于 $\mathcal{G}$ 是困难的，那么该加密方案是选择明文安全的。

12.7 Consider the following variant of El Gamal encryption. Let $p = 2q + 1$, let $\mathbb{G}$ be the group of squares modulo $p$ (so $\mathbb{G}$ is a subgroup of $\mathbb{Z}_p^*$ of order $q$), and let $g$ be a generator of $\mathbb{G}$. The private key is $(\mathbb{G}, g, q, x)$ and the public key is $(\mathbb{G}, g, q, h)$, where $h = g^x$ and $x \in \mathbb{Z}_q$ is chosen uniformly. To encrypt a message $m \in \mathbb{Z}_p$, choose a uniform $r \in \mathbb{Z}_q$, compute $c_1 := g^r \bmod p$ and $c_2 := h^r + m \bmod p$, and let the ciphertext be $\langle c_1, c_2 \rangle$. Is this scheme CPA-secure? Prove your answer.

12.7 考虑 El Gamal 加密的如下变体。设 $p = 2q + 1$，设 $\mathbb{G}$ 为模 p 的平方元构成的群（即 $\mathbb{G}$ 是 $\mathbb{Z}_p^*$ 中阶为 $q$ 的子群），并设 g 是 $\mathbb{G}$ 的生成元。私钥为 $(\mathbb{G}, g, q, x)$，公钥为 $(\mathbb{G}, g, q, h)$，其中 $h = g^x$，而 $x \in \mathbb{Z}_q$ 均匀选取。要加密消息 $m \in \mathbb{Z}_p$，均匀选取 $r \in \mathbb{Z}_q$，计算 $c_1 := g^r \bmod p$ 与 $c_2 := h^r + m \bmod p$，并取密文为 $\langle c_1, c_2 \rangle$。该方案是选择明文安全的吗？证明你的答案。

12.8 Consider the following protocol for two parties A and B to flip a fair coin (more complicated versions of this might be used for Internet gambling): (1) a trusted party T publishes her public key pk; (2) then A chooses a uniform bit $b_{A}$, encrypts it using $pk$, and announces the ciphertext $c_{A}$ to B and T; (3) next, B acts symmetrically and announces a ciphertext $c_{B} \neq c_{A}$; (4) T decrypts both $c_{A}$ and $c_{B}$, and the parties XOR the results to obtain the value of the coin.

12.8 考虑如下供两方 A 和 B 抛掷均匀硬币的协议（其更复杂的版本可用于互联网赌博）：(1) 一个可信方 T 公布她的公钥 pk；(2) 然后 A 均匀选取比特 $b_{A}$，用 pk 加密之，并向 B 和 T 公布密文 $c_{A}$；(3) 接着 B 对称地行事，公布一个满足 $c_{B} \neq c_{A}$ 的密文 $c_{B}$；(4) T 解密 $c_{A}$ 与 $c_{B}$，双方将结果异或得到硬币的值。

(a) Argue that even if A is dishonest (but B is honest), the final value of the coin is uniformly distributed.

(a) 论证：即使 A 不诚实（但 B 诚实），硬币的最终值也是均匀分布的。

(b) Assume the parties use El Gamal encryption (where the bit $b$ is encoded as the group element $g^b$ before being encrypted—note that efficient decryption is still possible). Show how a dishonest $B$ can bias the coin to any value he likes.

(b) 假设双方使用 El Gamal 加密（其中比特 b 在加密前先编码为群元素 $g^b$——注意高效解密仍然可行）。展示不诚实的 B 如何能把硬币偏向他所希望的任意值。

(c) Suggest what type of encryption scheme would be appropriate to use here. Can you define an appropriate notion of security and prove that your suggestion achieves this definition?

(c) 建议此处适合使用哪类加密方案。你能定义一个合适的安全性概念，并证明你的建议达到该定义吗？

12.9 Prove formally that the El Gamal encryption scheme is not CCA-secure.

12.9 形式化证明 El Gamal 加密方案不是选择密文安全的。

12.10 In Section 12.4.4 we showed that El Gamal encryption is malleable, and specifically that given a ciphertext $\langle c_1, c_2 \rangle$ that is the encryption of some unknown message $m$, it is possible to produce a ciphertext $\langle c_1, c^{\prime}_2 \rangle$ that is the encryption of $\alpha \cdot m$ (for known $\alpha$). A receiver who receives both these ciphertexts might be suspicious since both ciphertexts share the first component. Show that it is possible to generate $\langle c^{\prime}_1, c^{\prime}_2 \rangle$ that is the encryption of $\alpha \cdot m$, with $c^{\prime}_1 \neq c_1$ and $c^{\prime}_2 \neq c_2$.

12.10 在 12.4.4 节我们展示了 El Gamal 加密的可延展性，具体地说：给定某个未知消息 m 的加密 $\langle c_1, c_2 \rangle$，可以造出 $\alpha \cdot m$（$\alpha$ 已知）的加密 $\langle c_1, c^{\prime}_2 \rangle$。同时收到这两个密文的接收者可能会起疑，因为两个密文的第一个分量相同。证明可以造出 $\alpha \cdot m$ 的加密 $\langle c^{\prime}_1, c^{\prime}_2 \rangle$，使得 $c^{\prime}_1 \neq c_1$ 且 $c^{\prime}_2 \neq c_2$。

12.11 Prove Theorem 12.22.

12.11 证明定理 12.22。

12.12 One of the attacks on plain RSA discussed in Section 12.5.1 involves a sender who encrypts two related messages using the same public key. Formulate an appropriate definition of security ruling out such attacks, and show that any CPA-secure public-key encryption scheme satisfies your definition.

12.12 12.5.1 节讨论的对朴素 RSA 的攻击之一涉及这样的发送者：他用同一公钥加密两条相关的消息。给出一个恰当的安全性定义来排除这类攻击，并证明任何选择明文安全的公钥加密方案都满足你的定义。

12.13 One of the attacks on plain RSA discussed in Section 12.5.1 involves a sender who encrypts the same message to three different receivers. Formulate an appropriate definition of security ruling out such attacks, and show that any CPA-secure public-key encryption scheme satisfies your definition.

12.13 12.5.1 节讨论的对朴素 RSA 的攻击之一涉及这样的发送者：他把同一条消息加密发给三个不同的接收者。给出一个恰当的安全性定义来排除这类攻击，并证明任何选择明文安全的公钥加密方案都满足你的定义。

12.14 Consider the following modified version of padded RSA encryption: Assume messages to be encrypted have length exactly $\|N\|$/2. To encrypt, first compute $\hat{m} := \mathtt{0x00}\|r\|\mathtt{0x00}\|m$ where $r$ is a uniform string of length $\|N\|/2 - 16$. Then compute the ciphertext $c := [\hat{m}^e \bmod N]$. When decrypting a ciphertext $c$, the receiver computes $\hat{m} := [c^d \bmod N]$ and returns an error if $\hat{m}$ does not consist of 0x00 followed by $\|N\|$/2 - 16 arbitrary bits followed by 0x00. Show that this scheme is not CCA-secure. Why is it easier to construct a chosen-ciphertext attack on this scheme than on PKCS #1 v1.5?

12.14 考虑填充 RSA 加密的如下修改版本：假设待加密消息的长度恰为 $\|N\|$/2。加密时，先计算 $\hat{m} := \mathtt{0x00}\|r\|\mathtt{0x00}\|m$，其中 r 是长度为 $\|N\|/2 - 16$ 的均匀串。然后计算密文 $c := [\hat{m}^e \bmod N]$。解密密文 c 时，接收方计算 $\hat{m} := [c^d \bmod N]$，若 $\hat{m}$ 不是由 0x00 开头、随后是 $\|N\|$/2 - 16 个任意比特、再跟着 0x00 组成，则返回错误。证明该方案不是选择密文安全的。为什么对该方案构造选择密文攻击比对 PKCS #1 v1.5 更容易？

12.15 Consider the RSA-based encryption scheme in which a user encrypts a message $m \in \{0,1\}^{\ell}$ with respect to the public key $\langle N,e\rangle$ by computing $\hat{m} := H(m)\|m$ and outputting the ciphertext $[\hat{m}^{e} \bmod N]$. (Here, let $H : \{0,1\}^{\ell} \to \{0,1\}^{n}$ and assume $\ell + n < \|N\|$.) Is this scheme CPA-secure if $H$ is modeled as a random oracle?

12.15 考虑如下基于 RSA 的加密方案：用户以公钥 $\langle N,e\rangle$ 加密消息 $m \in \{0,1\}^{\ell}$ 时，计算 $\hat{m} := H(m)\|m$ 并输出密文 $[\hat{m}^{e} \bmod N]$。（此处设 $H : \{0,1\}^{\ell} \to \{0,1\}^{n}$，并假设 $\ell + n < \|N\|$。）如果 $H$ 被建模为随机预言机，该方案是选择明文安全的吗？

12.16 Show a chosen-ciphertext attack on Construction 12.34.

12.16 给出对构造 12.34 的一个选择密文攻击。

12.17 Say three users have RSA public keys $\langle N_1, 3 \rangle$, $\langle N_2, 3 \rangle$, and $\langle N_3, 3 \rangle$ (i.e., they all use $e = 3$), with $N_1 < N_2 < N_3$. Consider the following method for sending the same message $m \in \{0,1\}^{\ell}$ to each of these parties: choose a uniform $r \leftarrow \mathbb{Z}_{N_1}^*$, and send to everyone the same ciphertext

12.17 设三个用户的 RSA 公钥分别为 $\langle N_1, 3 \rangle$、$\langle N_2, 3 \rangle$ 和 $\langle N_3, 3 \rangle$（即他们都使用 $e = 3$），且 $N_1 < N_2 < N_3$。考虑如下向这些参与方发送同一消息 $m \in \{0,1\}^{\ell}$ 的方法：均匀选取 $r \leftarrow \mathbb{Z}_{N_1}^*$，并把同一密文

$$
\left\langle[r^{3}\bmod N_{1}],[r^{3}\bmod N_{2}],[r^{3}\bmod N_{3}],H(r)\oplus m\right\rangle,
$$

where $H: \mathbb{Z}_{N_1}^* \to \{0,1\}^{\ell}$. Assume $\|N_1\| = \|N_2\| = \|N_3\| = n \ll \ell$.

发给每个人，其中 $H: \mathbb{Z}_{N_1}^* \to \{0,1\}^{\ell}$。假设 $\|N_1\| = \|N_2\| = \|N_3\| = n \ll \ell$。

(a) Show that this is not CPA-secure, and an adversary can recover $m$ from the ciphertext even when H is modeled as a random oracle.

(a) 证明这不是选择明文安全的：即使 $H$ 被建模为随机预言机，敌手也能从密文中恢复 $m$。

Hint: See Section 12.5.1.

提示：见 12.5.1 节。

(b) Show a simple way to fix this and get a CPA-secure method that transmits a ciphertext of length $3\ell + \mathcal{O}(n)$.

(b) 展示一种简单的修复方法，得到一种传输长度为 $3\ell + \mathcal{O}(n)$ 的密文的选择明文安全方法。

(c) Show a better approach that is still CPA-secure but with a cipher-text of length $\ell + \mathcal{O}(n)$.

(c) 展示一种更好的方法，它仍然是选择明文安全的，但密文长度为 $\ell + \mathcal{O}(n)$。

12.18 Let $\Pi = (\mathsf{Gen}, \mathsf{Enc}, \mathsf{Dec})$ be a CPA-secure public-key encryption scheme, and let $\Pi^{\prime} = (\mathsf{Gen}^{\prime}, \mathsf{Enc}^{\prime}, \mathsf{Dec}^{\prime})$ be a CCA-secure private-key encryption scheme. Consider the following construction:

12.18 设 $\Pi = (\mathsf{Gen}, \mathsf{Enc}, \mathsf{Dec})$ 是选择明文安全的公钥加密方案，$\Pi^{\prime} = (\mathsf{Gen}^{\prime}, \mathsf{Enc}^{\prime}, \mathsf{Dec}^{\prime})$ 是选择密文安全的私钥加密方案。考虑如下构造：

**CONSTRUCTION 12.41**

**构造 12.41**

Let $H: \{0,1\}^n \to \{0,1\}^n$ be a function. Construct a public-key encryption scheme as follows:

设 $H: \{0,1\}^n \to \{0,1\}^n$ 为函数。如下构造一个公钥加密方案：

- Gen*: on input $1^n$, run $\mathsf{Gen}(1^n)$ to obtain $(pk, sk)$. Output these as the public and private keys, respectively.

- Gen*：以 $1^n$ 为输入，运行 $\mathsf{Gen}(1^n)$ 得到 $(pk, sk)$。分别输出它们作为公钥和私钥。

- Enc*: on input a public key $pk$ and a message $m \in \{0,1\}^n$, choose a uniform $r \in \{0,1\}^n$ and output the ciphertext

- Enc*：以公钥 $pk$ 和消息 $m \in \{0,1\}^n$ 为输入，均匀选取 $r \in \{0,1\}^n$ 并输出密文

$$
\langle \mathsf{Enc}_{pk}(r), \mathsf{Enc}_{H(r)}^{\prime}(m) \rangle.
$$

- Dec*: on input a private key $sk$ and a ciphertext $\langle c_1, c_2 \rangle$, compute $r := \mathsf{Dec}_{sk}(c_1)$ and set $k := H(r)$. Then output $\mathsf{Dec}_{k}^{\prime}(c_2)$.

- Dec*：以私钥 $sk$ 和密文 $\langle c_1, c_2 \rangle$ 为输入，计算 $r := \mathsf{Dec}_{sk}(c_1)$ 并置 $k := H(r)$。然后输出 $\mathsf{Dec}_{k}^{\prime}(c_2)$。

Does the above construction have indistinguishable encryptions under a chosen-ciphertext attack, if H is modeled as a random oracle? If yes, provide a proof. If not, where does the approach used to prove Theorem 12.38 break down?

如果 $H$ 被建模为随机预言机，上述构造在选择密文攻击下是否具有不可区分的加密？若是，给出证明；若否，用于证明定理 12.38 的方法在何处失效？

12.19 Consider the following variant of Construction 12.32:

12.19 考虑构造 12.32 的如下变体：

**CONSTRUCTION 12.42**

**构造 12.42**

Let GenRSA be as usual, and define a public-key encryption scheme as follows:

设 $\mathsf{GenRSA}$ 如常，并如下定义一个公钥加密方案：

- Gen: on input $1^n$, run $\mathsf{GenRSA}(1^n)$ to obtain $(N, e, d)$. Output the public key $pk = \langle N, e \rangle$, and the private key $sk = \langle N, d \rangle$.

- Gen：以 $1^n$ 为输入，运行 $\mathsf{GenRSA}(1^n)$ 得到 $(N, e, d)$。输出公钥 $pk = \langle N, e \rangle$ 和私钥 $sk = \langle N, d \rangle$。

- Enc: on input a public key $pk = \langle N, e \rangle$ and a message $m \in \{0,1\}$, choose a uniform $r \in \mathbb{Z}_N^*$. Output the ciphertext $\langle [r^e \bmod N], \mathsf{lsb}(r) \oplus m\rangle$.

- Enc：以公钥 $pk = \langle N, e \rangle$ 和消息 $m \in \{0,1\}$ 为输入，均匀选取 $r \in \mathbb{Z}_N^*$。输出密文 $\langle [r^e \bmod N], \mathsf{lsb}(r) \oplus m\rangle$。

- Dec: on input a private key $sk = \langle N, d \rangle$ and a ciphertext $\langle c, b \rangle$, compute $r := [c^d \bmod N]$ and output $\mathsf{lsb}(r) \oplus b$.

- Dec：以私钥 $sk = \langle N, d \rangle$ 和密文 $\langle c, b \rangle$ 为输入，计算 $r := [c^d \bmod N]$ 并输出 $\mathsf{lsb}(r) \oplus b$。

Prove that this scheme is CPA-secure.

证明该方案是选择明文安全的。

12.20 Fix an RSA public key $\langle N, e \rangle$ and assume we have an algorithm $\mathcal{A}$ that always correctly computes $\mathsf{lsb}(x)$ given $[x^e \bmod N]$. Write full pseudocode for an algorithm $\mathcal{A}^{\prime}$ that computes $x$ from $[x^e \bmod N]$.

12.20 固定一个 RSA 公钥 $\langle N, e \rangle$，并假设我们有算法 $\mathcal{A}$：给定 $[x^e \bmod N]$ 时总能正确计算 $\mathsf{lsb}(x)$。写出一个从 $[x^e \bmod N]$ 计算 x 的算法 $\mathcal{A}^{\prime}$ 的完整伪代码。
