## 12.4 CDH/DDH-Based Encryption　基于 CDH/DDH 的加密

So far we have discussed public-key encryption abstractly, but have not yet seen any concrete examples of public-key encryption schemes (or KEMs). Here we explore some constructions based on the Diffie–Hellman problems. (The Diffie–Hellman problems are introduced in Section 9.3.2.)

到目前为止，我们只是抽象地讨论了公钥加密，尚未见过任何具体的公钥加密方案（或 KEM）实例。本节探讨若干基于 Diffie–Hellman 问题的构造。（Diffie–Hellman 问题在 9.3.2 节介绍。）

### 12.4.1 El Gamal Encryption　El Gamal 加密

In 1985, Taher El Gamal observed that the Diffie–Hellman key-exchange protocol (cf. Section 11.3) could be adapted to give a public-key encryption scheme. Recall that in the Diffie–Hellman protocol, Alice sends a message to Bob and then Bob responds with a message to Alice; based on these messages, Alice and Bob can derive a shared value $k$ which is indistinguishable (to an eavesdropper) from a uniform element of some group $\mathbb{G}$. We could imagine Bob using that shared value to encrypt a message $m \in \mathbb{G}$ by simply sending $k \cdot m$ to Alice; Alice can clearly recover $m$ using her knowledge of $k$, and we will argue below that an eavesdropper learns nothing about $m$.

1985 年，Taher El Gamal 注意到，Diffie–Hellman 密钥交换协议（参见 11.3 节）可以改造为公钥加密方案。回顾 Diffie–Hellman 协议：Alice 向 Bob 发送一条消息，Bob 再向 Alice 回复一条消息；基于这些消息，Alice 和 Bob 可以导出一个共享值 $k$，它（在窃听者看来）与某群 $\mathbb{G}$ 中的均匀元素不可区分。可以设想 Bob 用这个共享值来加密消息 $m \in \mathbb{G}$：只需把 $k \cdot m$ 发给 Alice。Alice 知道 $k$，显然能恢复出 $m$，而下面将论证窃听者得不到关于 $m$ 的任何信息。

In the El Gamal encryption scheme we simply change our perspective on the above interaction. We view Alice's initial message as her public key, and Bob's reply (both his initial response and $k \cdot m$) as a ciphertext. CPA-security based on the decisional Diffie–Hellman (DDH) assumption follows fairly easily from security of the Diffie–Hellman key-exchange protocol (Theorem 11.3).

在 El Gamal 加密方案中，我们只是转换了对上述交互过程的观察视角：把 Alice 的第一条消息视为她的公钥，把 Bob 的回复（包括他的初始应答和 $k \cdot m$）视为密文。基于判定性 Diffie–Hellman（DDH）假设的选择明文安全性，可以相当容易地由 Diffie–Hellman 密钥交换协议的安全性（定理 11.3）推出。

In our formal treatment, we begin by stating and proving a simple lemma that underlies the El Gamal encryption scheme. Let $\mathbb{G}$ be a finite group, and let $m \in \mathbb{G}$ be an arbitrary element. The lemma states that multiplying $m$ by a uniform group element $k$ yields a uniformly distributed group element $c$. Importantly, the distribution of $c$ is independent of $m$; this means that $c$ contains no information about $m$.

在正式论述中，先陈述并证明一个作为 El Gamal 加密方案基础的简单引理。设 $\mathbb{G}$ 为有限群，$m \in \mathbb{G}$ 为任意元素。该引理指出：把 $m$ 乘以一个均匀的群元素 $k$，得到的 $c$ 是均匀分布的群元素。重要的是，$c$ 的分布与 $m$ 无关；这意味着 $c$ 不携带关于 $m$ 的任何信息。

LEMMA 12.15 Let $\mathbb{G}$ be a finite group, and let $m \in \mathbb{G}$ be arbitrary. Then choosing uniform $k \in \mathbb{G}$ and setting $c := k \cdot m$ results in a uniformly distributed $c \in \mathbb{G}$. Put differently, for any $\hat{c} \in \mathbb{G}$, we have

引理 12.15　设 $\mathbb{G}$ 为有限群，$m \in \mathbb{G}$ 为任意元素。均匀选取 $k \in \mathbb{G}$ 并令 $c := k \cdot m$，则得到的 $c \in \mathbb{G}$ 服从均匀分布。换言之，对任意 $\hat{c} \in \mathbb{G}$，有

$$
\Pr[k\cdot m=\hat{c}]=1/|\mathbb{G}|,
$$

where the probability is taken over uniform choice of $k \in \mathbb{G}$.

其中概率取自对 $k \in \mathbb{G}$ 的均匀选取。

PROOF Let $\hat{c} \in \mathbb{G}$ be arbitrary. Then

证明　任取 $\hat{c} \in \mathbb{G}$。则

$$
\Pr[k\cdot m=\hat{c}]=\Pr[k=\hat{c}\cdot m^{-1}].
$$

Since $k$ is uniform, the probability that $k$ is equal to the fixed element $\hat{c} \cdot m^{-1}$ is exactly $1/|\mathbb{G}|$.

由于 $k$ 是均匀的，$k$ 恰好等于固定元素 $\hat{c} \cdot m^{-1}$ 的概率正是 $1/|\mathbb{G}|$。

The above lemma suggests a way to construct a perfectly secret private-key encryption scheme with message space $\mathbb{G}$. The sender and receiver share as their secret key a uniform element $k \in \mathbb{G}$. To encrypt the message $m \in \mathbb{G}$, the sender computes the ciphertext $c := k \cdot m$. The receiver can recover the message from the ciphertext $c$ by computing $m := c/k$. Perfect secrecy follows immediately from the lemma above. In fact, we have already seen this scheme in a different guise—the one-time pad encryption scheme is an instantiation of this approach, with the underlying group $\mathbb{G}$ being the set $\{0,1\}^{\ell}$ under the operation of bit-wise XOR.

上述引理提示了一种构造完美保密私钥加密方案的方法，其消息空间为 $\mathbb{G}$。发送方与接收方共享一个均匀元素 $k \in \mathbb{G}$ 作为密钥。加密消息 $m \in \mathbb{G}$ 时，发送方计算密文 $c := k \cdot m$；接收方由密文 $c$ 计算 $m := c/k$ 即可恢复消息。完美保密性由上面的引理直接得到。事实上，我们已经在另一种形态下见过这个方案——一次一密加密方案就是该方法的一个实例，其底层群 $\mathbb{G}$ 是集合 $\{0,1\}^{\ell}$，群运算为逐比特异或。

We can adapt the above ideas to the public-key setting by providing the parties with a way to generate a shared, “random-looking” value $k$ by interacting over a public channel. This should sound familiar since it is exactly what the Diffie–Hellman protocol achieves. We proceed with the details.

只要能让通信双方通过在公开信道上交互，生成一个共享的、“看起来随机”的值 $k$，就可以把上述思想改造到公钥场景。这听起来应当很熟悉，因为这正是 Diffie–Hellman 协议所实现的功能。下面给出具体细节。

As in Section 9.3.2, let $\mathcal{G}$ be a polynomial-time algorithm that takes as input $1^n$ and (except possibly with negligible probability) outputs a description of a cyclic group $\mathbb{G}$, its order $q$ (with $\|q\| = n$), and a generator $g$. The El Gamal encryption scheme is described in Construction 12.16.

与 9.3.2 节一样，设 $\mathcal{G}$ 是一个多项式时间算法，输入 $1^n$，输出循环群 $\mathbb{G}$ 的描述、其阶 $q$（满足 $\|q\| = n$）以及生成元 $g$（例外情形的发生概率可忽略）。El Gamal 加密方案见构造 12.16。

**CONSTRUCTION 12.16**

Let G be as in the text. Define a public-key encryption scheme as follows:

- Gen: on input $1^n$ run $\mathcal{G}(1^n)$ to obtain $(\mathbb{G}, q, g)$. Then choose a uniform $x \in \mathbb{Z}_q$ and compute $h := g^x$. The public key is $\langle \mathbb{G}, q, g, h \rangle$ and the private key is $\langle \mathbb{G}, q, g, x \rangle$. The message space is $\mathbb{G}$.

- Enc: on input a public key $pk = \langle \mathbb{G}, q, g, h \rangle$ and a message $m \in \mathbb{G}$, choose a uniform $y \in \mathbb{Z}_q$ and output the ciphertext

$$
\langle g^{y},~h^{y}\cdot m\rangle.
$$

- Dec: on input a private key $sk = \langle \mathbb{G}, q, g, x \rangle$ and a ciphertext $\langle c_1, c_2 \rangle$, output

$$
\hat{m}:=c_{2}/c_{1}^{x}.
$$


**The El Gamal encryption scheme.**

**构造 12.16**

设 $\mathcal{G}$ 如正文所述。定义如下公钥加密方案：

- Gen：输入 $1^n$，运行 $\mathcal{G}(1^n)$ 得到 $(\mathbb{G}, q, g)$。然后均匀选取 $x \in \mathbb{Z}_q$ 并计算 $h := g^x$。公钥为 $\langle \mathbb{G}, q, g, h \rangle$，私钥为 $\langle \mathbb{G}, q, g, x \rangle$。消息空间为 $\mathbb{G}$。

- Enc：输入公钥 $pk = \langle \mathbb{G}, q, g, h \rangle$ 和消息 $m \in \mathbb{G}$，均匀选取 $y \in \mathbb{Z}_q$，输出密文

$$
\langle g^{y},~h^{y}\cdot m\rangle.
$$

- Dec：输入私钥 $sk = \langle \mathbb{G}, q, g, x \rangle$ 和密文 $\langle c_1, c_2 \rangle$，输出

$$
\hat{m}:=c_{2}/c_{1}^{x}.
$$

**El Gamal 加密方案。**

To see that decryption succeeds, let $\langle c_1, c_2 \rangle = \langle g^y, h^y \cdot m \rangle$ with $h = g^x$. Then

为验证解密正确，设 $\langle c_1, c_2 \rangle = \langle g^y, h^y \cdot m \rangle$，其中 $h = g^x$。于是

$$
\hat{m}=\frac{c_{2}}{c_{1}^{x}}=\frac{h^{y}\cdot m}{(g^{y})^{x}}=\frac{(g^{x})^{y}\cdot m}{g^{x y}}=\frac{g^{x y}\cdot m}{g^{x y}}=m.
$$

**Example 12.17**

**例 12.17**

Let $q = 83$ and $p = 2q + 1 = 167$, and let $\mathbb{G}$ denote the group of quadratic residues (i.e., squares) modulo $p$. (Since $p$ and $q$ are prime, $\mathbb{G}$ is a subgroup of $\mathbb{Z}_p^*$ with order $q$. See Section 9.3.3.) Since the order of $\mathbb{G}$ is prime, any element of $\mathbb{G}$ except 1 is a generator; take $g = [2^2 = 4 \bmod 167]$. Say the receiver chooses secret key $37 \in \mathbb{Z}_{83}$ and so the public key is

令 $q = 83$、$p = 2q + 1 = 167$，令 $\mathbb{G}$ 表示模 $p$ 的二次剩余（即平方）构成的群。（由于 $p$ 和 $q$ 都是素数，$\mathbb{G}$ 是 $\mathbb{Z}_p^*$ 的 $q$ 阶子群。见 9.3.3 节。）由于 $\mathbb{G}$ 的阶是素数，除 1 以外的任何元素都是生成元；取 $g = [2^2 = 4 \bmod 167]$。设接收方选取私钥 $37 \in \mathbb{Z}_{83}$，于是公钥为

$$
pk=\langle p,q,g,h\rangle=\langle167,83,4,[4^{37}\bmod167]\rangle=\langle167,83,4,76\rangle,
$$

where we use $p$ to represent $\mathbb{G}$ (it is assumed that the receiver knows that the group is the set of quadratic residues modulo $p$).

其中用 $p$ 来代表 $\mathbb{G}$（假定接收方知道该群是模 $p$ 二次剩余构成的集合）。

Say a sender encrypts the message $m = 65 \in \mathbb{G}$ (note $65 = 30^2 \bmod 167$ and so 65 is an element of $\mathbb{G}$). If $y = 71$, the ciphertext is

设发送方加密消息 $m = 65 \in \mathbb{G}$（注意 $65 = 30^2 \bmod 167$，故 65 是 $\mathbb{G}$ 的元素）。若 $y = 71$，则密文为

$$
\langle[4^{71}\bmod{167}],[76^{71}\cdot65\bmod{167}]\rangle=\langle132,{44}\rangle.
$$

To decrypt, the receiver first computes $124 = [132^{37} \bmod 167]$; then, since $66 = [124^{-1} \bmod 167]$, the receiver recovers $m = 65 = [44 \cdot 66 \bmod 167]$.

解密时，接收方先计算 $124 = [132^{37} \bmod 167]$；再由 $66 = [124^{-1} \bmod 167]$，恢复出 $m = 65 = [44 \cdot 66 \bmod 167]$。

We now prove security of the scheme. (The reader may want to compare the proof of the following to the proofs of Theorems 3.16 and 11.3.)

现在证明该方案的安全性。（读者不妨将下面的证明与定理 3.16 和定理 11.3 的证明相对照。）

THEOREM 12.18 If the DDH problem is hard relative to G, then the El Gamal encryption scheme is CPA-secure.

定理 12.18　若 DDH 问题相对于 $\mathcal{G}$ 是困难的，则 El Gamal 加密方案是选择明文安全的。

PROOF Let $\Pi$ denote the El Gamal encryption scheme. We prove that $\Pi$ has indistinguishable encryptions in the presence of an eavesdropper; by Proposition 12.3, this implies it is CPA-secure.

证明　令 $\Pi$ 表示 El Gamal 加密方案。我们证明 $\Pi$ 在窃听者存在时具有不可区分的加密；由命题 12.3，这意味着它是选择明文安全的。

Let $\mathcal{A}$ be a probabilistic polynomial-time adversary. We want to show that there is a negligible function $\mathsf{negl}$ such that

设 $\mathcal{A}$ 为概率多项式时间敌手。我们要证明存在可忽略函数 $\mathsf{negl}$ 使得

$$
\Pr[\mathsf{PubK}_{\mathcal{A},\Pi}^{\mathsf{eav}}(n)=1]\leq\frac{1}{2}+\mathsf{negl}(n).
$$

Consider the modified “encryption scheme” $\widetilde{\Pi}$ where $\mathsf{Gen}$ is the same as in $\Pi$, but encryption of a message $m$ with respect to the public key $\langle \mathbb{G}, q, g, h \rangle$ is done by choosing uniform $y, z \in \mathbb{Z}_q$ and outputting the ciphertext

考虑修改后的“加密方案”$\widetilde{\Pi}$：其中 $\mathsf{Gen}$ 与 $\Pi$ 相同，但在公钥 $\langle \mathbb{G}, q, g, h \rangle$ 下加密消息 $m$ 时，均匀选取 $y, z \in \mathbb{Z}_q$ 并输出密文

$$
\langle g^{y},~g^{z}\cdot m\rangle.
$$

Although $\widetilde{\Pi}$ is not actually an encryption scheme (as there is no way for the receiver to decrypt), the experiment $\mathsf{PubK}_{\mathcal{A},\widetilde{\Pi}}^{\mathsf{eav}}(n)$ is still well-defined since that experiment depends only on the key-generation and encryption algorithms.

虽然 $\widetilde{\Pi}$ 实际上并不是一个加密方案（因为接收方无法解密），但实验 $\mathsf{PubK}_{\mathcal{A},\widetilde{\Pi}}^{\mathsf{eav}}(n)$ 仍然是良定义的，因为该实验只涉及密钥生成算法和加密算法。

Lemma 12.15 and the discussion that immediately follows it imply that the second component of the ciphertext in scheme $\widetilde{\Pi}$ is a uniformly distributed group element and, in particular, is independent of the message $m$ being encrypted. (Remember that $g^z$ is a uniform element of $\mathbb{G}$ when z is chosen uniformly from $\mathbb{Z}_q$.) The first component of the ciphertext is trivially independent of m. Taken together, this means that the entire ciphertext contains no information about m. It follows that

引理 12.15 及紧随其后的讨论表明，方案 $\widetilde{\Pi}$ 中密文的第二个分量是均匀分布的群元素，特别地，它与被加密的消息 $m$ 无关。（记住，当 z 从 $\mathbb{Z}_q$ 中均匀选取时，$g^z$ 是 $\mathbb{G}$ 中的均匀元素。）密文的第一个分量显然与 m 无关。合起来看，这意味着整个密文不包含关于 m 的任何信息。于是有

$$
\Pr[\mathsf{PubK}_{\mathcal{A},\widetilde{\Pi}}^{\mathsf{eav}}(n)=1]=\frac{1}{2}.
$$

Now consider the following PPT algorithm $D$ that attempts to solve the DDH problem relative to $\mathcal{G}$. Recall that $D$ receives $(\mathbb{G}, q, g, h_1, h_2, h_3)$ where $h_1 = g^x$, $h_2 = g^y$, and $h_3$ is either $g^{xy}$ or $g^z$ (for uniform $x, y, z)$; the goal of $D$ is to determine which is the case.

现在考虑如下试图求解相对于 $\mathcal{G}$ 的 DDH 问题的 PPT 算法 $D$。回顾：$D$ 接收 $(\mathbb{G}, q, g, h_1, h_2, h_3)$，其中 $h_1 = g^x$、$h_2 = g^y$，而 $h_3$ 是 $g^{xy}$ 或 $g^z$（$x, y, z$ 均为均匀选取）；$D$ 的目标是判断属于哪种情形。

**Algorithm D:**

The algorithm is given $(\mathbb{G}, q, g, h_1, h_2, h_3)$ as input.

- Set $pk = \langle \mathbb{G}, q, g, h_1 \rangle$ and run $\mathcal{A}(pk)$ to obtain two messages $m_0, m_1 \in \mathbb{G}$.

- Choose a uniform bit b, and set $c_1 := h_2$ and $c_2 := h_3 \cdot m_b$.

- Give the ciphertext $\langle c_1, c_2 \rangle$ to $\mathcal{A}$ and obtain an output bit $b^{\prime}$. If $b^{\prime} = b$, output 1; otherwise, output 0.

**算法 D：**

算法以 $(\mathbb{G}, q, g, h_1, h_2, h_3)$ 为输入。

- 令 $pk = \langle \mathbb{G}, q, g, h_1 \rangle$，运行 $\mathcal{A}(pk)$ 得到两条消息 $m_0, m_1 \in \mathbb{G}$。

- 均匀选取比特 b，令 $c_1 := h_2$、$c_2 := h_3 \cdot m_b$。

- 将密文 $\langle c_1, c_2 \rangle$ 交给 $\mathcal{A}$，得到输出比特 $b^{\prime}$。若 $b^{\prime} = b$，输出 1；否则输出 0。

Let us analyze the behavior of $D$. There are two cases to consider:

下面分析 $D$ 的行为。需要分两种情形讨论：

Case 1: Say the input to $D$ is generated by running $\mathcal{G}(1^n)$ to obtain $(\mathbb{G}, q, g)$, then choosing uniform $x, y, z \in \mathbb{Z}_q$, and finally setting $h_1 := g^x, h_2 := g^y$, and $h_3 := g^z$. Then $D$ runs $\mathcal{A}$ on a public key constructed as

情形 1：设 $D$ 的输入按如下方式生成：运行 $\mathcal{G}(1^n)$ 得到 $(\mathbb{G}, q, g)$，再均匀选取 $x, y, z \in \mathbb{Z}_q$，最后令 $h_1 := g^x, h_2 := g^y$、$h_3 := g^z$。此时 $D$ 运行 $\mathcal{A}$ 所用的公钥构造为

$$
pk=\langle\mathbb{G},q,g,g^{x}\rangle
$$

and a ciphertext constructed as

密文构造为

$$
\langle c_{1},c_{2}\rangle=\langle g^{y},g^{z}\cdot m_{b}\rangle.
$$

We see that in this case the view of $\mathcal{A}$ when run as a subroutine by $D$ is distributed identically to $\mathcal{A}$'s view in experiment $\mathsf{PubK}_{\mathcal{A},\widetilde{\Pi}}^{\mathsf{eav}}(n)$. Since $D$ outputs 1 exactly when the output $b^{\prime}$ of $\mathcal{A}$ is equal to $b$, we have that

可见，在这种情形下，$\mathcal{A}$ 作为 $D$ 的子程序运行时的视图，与 $\mathcal{A}$ 在实验 $\mathsf{PubK}_{\mathcal{A},\widetilde{\Pi}}^{\mathsf{eav}}(n)$ 中的视图分布完全相同。由于 $D$ 恰在 $\mathcal{A}$ 的输出 $b^{\prime}$ 等于 $b$ 时输出 1，故有

$$
\Pr[D(\mathbb{G},q,g,g^{x},g^{y},g^{z})=1]=\Pr[\mathsf{PubK}_{\mathcal{A},\widetilde{\Pi}}^{\mathsf{eav}}(n)=1]=\frac{1}{2}.
$$

Case 2: Say the input to $D$ is generated by running $\mathcal{G}(1^n)$ to obtain $(\mathbb{G}, q, g)$, then choosing uniform $x, y \in \mathbb{Z}_q$, and finally setting $h_1 := g^x$, $h_2 := g^y$, and $h_3 := g^{xy}$. Then $D$ runs $\mathcal{A}$ on a public key constructed as

情形 2：设 $D$ 的输入按如下方式生成：运行 $\mathcal{G}(1^n)$ 得到 $(\mathbb{G}, q, g)$，再均匀选取 $x, y \in \mathbb{Z}_q$，最后令 $h_1 := g^x$、$h_2 := g^y$、$h_3 := g^{xy}$。此时 $D$ 运行 $\mathcal{A}$ 所用的公钥构造为

$$
pk=\langle\mathbb{G},q,g,g^{x}\rangle
$$

and a ciphertext constructed as

密文构造为

$$
\langle c_{1},c_{2}\rangle=\langle g^{y},g^{x y}\cdot m_{b}\rangle=\langle g^{y},(g^{x})^{y}\cdot m_{b}\rangle.
$$

We see that in this case the view of $\mathcal{A}$ when run as a subroutine by $D$ is distributed identically to $\mathcal{A}$'s view in experiment $\mathsf{PubK}_{\mathcal{A},\Pi}^{\mathsf{eav}}(n)$. Since $D$ outputs 1 exactly when the output $b^{\prime}$ of $\mathcal{A}$ is equal to $b$, we have that

可见，在这种情形下，$\mathcal{A}$ 作为 $D$ 的子程序运行时的视图，与 $\mathcal{A}$ 在实验 $\mathsf{PubK}_{\mathcal{A},\Pi}^{\mathsf{eav}}(n)$ 中的视图分布完全相同。由于 $D$ 恰在 $\mathcal{A}$ 的输出 $b^{\prime}$ 等于 $b$ 时输出 1，故有

$$
\Pr[D(\mathbb{G},q,g,g^{x},g^{y},g^{x y})=1]=\Pr[\mathsf{PubK}_{\mathcal{A},\Pi}^{\mathsf{eav}}(n)=1].
$$

Under the assumption that the DDH problem is hard relative to $\mathcal{G}$, there is a negligible function $\mathsf{negl}$ such that

在 DDH 问题相对于 $\mathcal{G}$ 困难的假设下，存在可忽略函数 $\mathsf{negl}$ 使得

$$
\begin{aligned}
\mathsf{negl}(n)&\geq\left|\Pr[D(\mathbb{G},q,g,g^{x},g^{y},g^{z})=1]-\Pr[D(\mathbb{G},q,g,g^{x},g^{y},g^{xy})=1]\right|\\
&=\left|\frac{1}{2}-\Pr[\mathsf{PubK}_{\mathcal{A},\Pi}^{\mathsf{eav}}(n)=1]\right|.
\end{aligned}
$$

This implies $\Pr[\mathsf{PubK}_{\mathcal{A},\Pi}^{\mathsf{eav}}(n)=1]\leq\tfrac{1}{2}+\mathsf{negl}(n)$, completing the proof.

这意味着 $\Pr[\mathsf{PubK}_{\mathcal{A},\Pi}^{\mathsf{eav}}(n)=1]\leq\tfrac{1}{2}+\mathsf{negl}(n)$，证毕。

### El Gamal Implementation Issues　El Gamal 的实现问题

We briefly discuss some practical issues related to El Gamal encryption.

下面简要讨论与 El Gamal 加密有关的一些实际问题。

Sharing public parameters. Our description of the El Gamal encryption scheme in Construction 12.16 requires the receiver to run $\mathcal{G}$ to generate $\mathbb{G}$, $q, g$. In practice, it is common for these parameters to be generated and fixed “once-and-for-all,” and then shared by multiple receivers. (Of course, each receiver must choose their own secret value $x$ and publish their own public key $h = g^x$.) For example, NIST has published a set of recommended parameters suitable for use in the El Gamal encryption scheme. Sharing parameters in this way does not impact security (assuming the parameters were generated correctly and honestly in the first place). Looking ahead, we remark that this is in contrast to the case of RSA, where parameters cannot safely be shared (see Section 12.5.1).

共享公开参数。构造 12.16 中对 El Gamal 加密方案的描述要求接收方运行 $\mathcal{G}$ 来生成 $\mathbb{G}$、$q, g$。实践中常见的做法是把这些参数“一次性”生成并固定下来，供多个接收方共享。（当然，每个接收方必须选取自己的秘密值 $x$ 并公布自己的公钥 $h = g^x$。）例如，NIST 已发布了一套适用于 El Gamal 加密方案的推荐参数。以这种方式共享参数并不影响安全性（前提是参数最初是以正确且诚实的方式生成的）。这里预先指出（详见后文）：这与 RSA 的情形相反，RSA 的参数无法安全地共享（见 12.5.1 节）。

Choice of group. As discussed in Section 9.3.2, the group order $q$ should be prime. As far as specific groups are concerned, elliptic curves are one increasingly popular choice; an alternative is to let $\mathbb{G}$ be a prime-order subgroup of $\mathbb{Z}_p^*$, for $p$ prime. We refer to Section 10.4 for a tabulation of recommended key lengths for achieving different levels of security.

群的选择。如 9.3.2 节所讨论的，群的阶 $q$ 应为素数。至于具体选用哪个群，椭圆曲线是日益流行的一种选择；另一种做法是对素数 $p$，取 $\mathbb{G}$ 为 $\mathbb{Z}_p^*$ 的素数阶子群。达到不同安全强度所推荐的密钥长度汇总表见 10.4 节。

**The message space.**

**消息空间。**

An inconvenient aspect of the El Gamal encryption scheme is that the message space is a group $\mathbb{G}$ rather than bit-strings of some specified length. For some choices of the group, it is possible to address this by defining a reversible encoding of bit-strings as group elements. In such cases, the sender can first encode their message $m \in \{0,1\}^{\ell}$ as a group element $\hat{m} \in \mathbb{G}$ and then apply El Gamal encryption to $\hat{m}$. The receiver can decrypt as in Construction 12.16 to obtain the encoded message $\hat{m}$, and then reverse the encoding to recover the original message $m$.

El Gamal 加密方案一个不便之处在于，其消息空间是群 $\mathbb{G}$，而不是某种指定长度的比特串。对于某些群的选择，可以定义比特串到群元素的可逆编码来解决这个问题。此时，发送方先把消息 $m \in \{0,1\}^{\ell}$ 编码为群元素 $\hat{m} \in \mathbb{G}$，再对 $\hat{m}$ 施加 El Gamal 加密；接收方按构造 12.16 解密得到编码后的消息 $\hat{m}$，再逆转编码恢复原始消息 $m$。

A simpler approach is to use (a variant of) El Gamal encryption as part of a hybrid encryption scheme. For example, the sender could choose a uniform group element $m \in \mathbb{G}$, encrypt this using the El Gamal encryption scheme, and then encrypt their actual message using a private-key encryption scheme and key $H(m)$, where $H : \mathbb{G} \to \{0,1\}^n$ is an appropriate key-derivation function (see the following section). In this case, it would be more efficient to use the DDH-based KEM that we describe next.

更简单的做法是把 El Gamal 加密（的某个变体）用作混合加密方案的一部分。例如，发送方可以均匀选取群元素 $m \in \mathbb{G}$，用 El Gamal 加密方案加密它，再以 $H(m)$ 为密钥、用私钥加密方案加密真正的消息，其中 $H : \mathbb{G} \to \{0,1\}^n$ 是适当的密钥派生函数（见下一节）。在这种情况下，使用接下来要介绍的基于 DDH 的 KEM 会更高效。

### 12.4.2 DDH-Based Key Encapsulation　基于 DDH 的密钥封装

At the end of the previous section we noted that El Gamal encryption can be used as part of a hybrid encryption scheme by simply encrypting a uniform group element $m$ and using a hash of that element as a key. But this is wasteful! The proof of security for El Gamal encryption shows that $c_1^x$ (where $c_1$ is the first component of the ciphertext, and $x$ is the private key of the receiver) is already indistinguishable from a uniform group element, so the sender/receiver may as well use that to derive a key. Construction 12.19
illustrates the KEM that follows this approach. Note the resulting ciphertext consists of just a single group element. In contrast, if we were to use El Gamal encryption of a uniform group element, the ciphertext would contain two group elements.

上一节末尾提到，只需加密一个均匀群元素 $m$ 并以该元素的散列值作为密钥，就可以把 El Gamal 加密用作混合加密方案的一部分。但这是浪费！El Gamal 加密的安全性证明表明，$c_1^x$（其中 $c_1$ 是密文的第一个分量，$x$ 是接收方的私钥）已经与均匀群元素不可区分，因此发送方/接收方不妨直接用它来导出密钥。构造 12.19 展示了遵循这一思路的 KEM。注意，所得密文只包含一个群元素；相比之下，若用 El Gamal 加密一个均匀群元素，密文将包含两个群元素。

**CONSTRUCTION 12.19**

Let G be as in the previous section. Define a KEM as follows:

- Gen: on input $1^n$ run $\mathcal{G}(1^n)$ to obtain $(\mathbb{G}, q, g)$. Choose a uniform $x \in \mathbb{Z}_q$ and set $h := g^x$. Also specify a function $H : \mathbb{G} \to \{0,1\}^{\ell(n)}$ for some function $\ell$ (see text). The public key is $\langle \mathbb{G}, q, g, h, H \rangle$ and the private key is $\langle \mathbb{G}, q, g, x \rangle$.

- Encaps: on input a public key $pk = \langle \mathbb{G}, q, g, h, H \rangle$, choose a uniform $y \in \mathbb{Z}_q$ and output the ciphertext $g^y$ and the key $H(h^y)$.

- Decaps: on input a private key $sk = \langle \mathbb{G}, q, g, x \rangle$ and a ciphertext $c \in \mathbb{G}$, output the key $H(c^x)$.

**An “El Gamal-like” KEM.**

**构造 12.19**

设 $\mathcal{G}$ 如上一节所述。定义如下 KEM：

- Gen：输入 $1^n$，运行 $\mathcal{G}(1^n)$ 得到 $(\mathbb{G}, q, g)$。均匀选取 $x \in \mathbb{Z}_q$ 并令 $h := g^x$。此外指定一个函数 $H : \mathbb{G} \to \{0,1\}^{\ell(n)}$，其中 $\ell$ 为某个函数（见正文）。公钥为 $\langle \mathbb{G}, q, g, h, H \rangle$，私钥为 $\langle \mathbb{G}, q, g, x \rangle$。

- Encaps：输入公钥 $pk = \langle \mathbb{G}, q, g, h, H \rangle$，均匀选取 $y \in \mathbb{Z}_q$，输出密文 $g^y$ 和密钥 $H(h^y)$。

- Decaps：输入私钥 $sk = \langle \mathbb{G}, q, g, x \rangle$ 和密文 $c \in \mathbb{G}$，输出密钥 $H(c^x)$。

**一个“类 El Gamal”的 KEM。**

The construction leaves the key-derivation function $H$ unspecified, and there are several options for instantiated it. (See Section 6.6.4 for more on key derivation in general.) One possibility is to choose a function $H : \mathbb{G} \to \{0,1\}^{\ell}$ that is (close to) regular, meaning that for each possible key $k \in \{0,1\}^{\ell}$ the number of group elements that map to $k$ is approximately the same. (Formally, we need a negligible function $\mathsf{negl}$ such that

该构造未指定密钥派生函数 $H$，实例化时有若干可选方案。（关于密钥派生的一般性讨论见 6.6.4 节。）一种可能是选取一个（接近）正则的函数 $H : \mathbb{G} \to \{0,1\}^{\ell}$，即对每个可能的密钥 $k \in \{0,1\}^{\ell}$，映射到 $k$ 的群元素个数大致相同。（严格地说，需要存在可忽略函数 $\mathsf{negl}$ 使得

$$
\frac{1}{2}\cdot\textstyle\sum_{k\in\{0,1\}^{\ell(n)}}\left|\Pr[H(g)=k]-2^{-\ell(n)}\right|\leq\mathsf{negl}(n),
$$

where the probability is taken over uniform $g \in \mathbb{G}$. This means the distribution of the key is statistically close to uniform.) Both the complexity of $H$, as well as the achievable key length $\ell$, depend on the specific group $\mathbb{G}$ used.

其中概率取自均匀的 $g \in \mathbb{G}$。这意味着密钥的分布在统计上接近均匀。）$H$ 的复杂度以及可实现的密钥长度 $\ell$，都依赖于具体使用的群 $\mathbb{G}$。

A second possibility is to let $H$ be a keyed function, where the (uniform) key for $H$ is included as part of the receiver's public key. This works if $H$ is a strong extractor, as mentioned briefly in Section 6.6.4. Appropriate choice of $\ell$ here (to ensure that the resulting key is statistically close to uniform) will depend on the size of $\mathbb{G}$.

第二种可能是令 $H$ 为带密钥的函数，并把 $H$ 的（均匀）密钥作为接收方公钥的一部分。若 $H$ 是强提取器（strong extractor），这种做法可行，如 6.6.4 节简要提及的那样。这里 $\ell$ 的适当选取（以确保所得密钥在统计上接近均匀）取决于 $\mathbb{G}$ 的大小。

In either of the above cases, a proof of CPA-security based on the decisional Diffie–Hellman (DDH) assumption follows easily by adapting the proof of security for the Diffie–Hellman key-exchange protocol (Theorem 11.3).

在上述两种情形下，基于判定性 Diffie–Hellman（DDH）假设的选择明文安全性证明，都可以通过改写 Diffie–Hellman 密钥交换协议的安全性证明（定理 11.3）容易地得到。

THEOREM 12.20 If the DDH problem is hard relative to G, and H is chosen as described, then Construction 12.19 is a CPA-secure KEM.

定理 12.20　若 DDH 问题相对于 $\mathcal{G}$ 是困难的，且 $H$ 按上述方式选取，则构造 12.19 是选择明文安全的 KEM。

If one is willing to model $H$ as a random oracle, Construction 12.19 can be proven CPA-secure based on the (weaker) computational Diffie–Hellman (CDH) assumption. We discuss this in the following section.

若愿意把 $H$ 建模为随机预言机，则可以基于（更弱的）计算性 Diffie–Hellman（CDH）假设证明构造 12.19 是选择明文安全的。下一节讨论这一点。

### 12.4.3 \*A CDH-Based KEM in the Random-Oracle Model　\*随机预言机模型中基于 CDH 的 KEM

In this section, we show that if one is willing to model $H$ as a random oracle, then Construction 12.19 can be proven CPA-secure based on the CDH assumption. (Readers may want to review Section 6.5 to remind themselves of the random-oracle model.) Intuitively, the CDH assumption implies that an attacker observing $h = g^x$ (from the public key) and the ciphertext $c = g^y$ cannot compute $\mathsf{DH}_g(h, c) = h^y$. In particular, then, an attacker cannot query $h^y$ to the random oracle. But this means that the encapsulated key $H(h^y)$ is completely random from the attacker's point of view. This intuition is turned into a formal proof below.

本节证明：若愿意把 $H$ 建模为随机预言机，则可以基于 CDH 假设证明构造 12.19 是选择明文安全的。（读者不妨复习 6.5 节，回顾随机预言机模型。）直观地说，CDH 假设意味着：攻击者观察到 $h = g^x$（来自公钥）和密文 $c = g^y$ 后，无法计算 $\mathsf{DH}_g(h, c) = h^y$。特别地，攻击者也就无法向随机预言机查询 $h^y$。而这意味着在攻击者看来，封装密钥 $H(h^y)$ 是完全随机的。下面把这一直观转化为严格证明。

As indicated by the intuition above, the proof inherently relies on modeling $H$ as a random oracle. $^2$ Specifically, the proof relies on the facts that (1) the only way to learn $H(h^y)$ is to explicitly query $h^y$ to $H$, which would mean that the attacker has solved a CDH instance (this is called “extractability” in Section 6.5.1), and (2) if an attacker does not query $h^y$ to $H$, then the value $H(h^y)$ is uniform from the attacker's point of view. These properties only hold—indeed, they only make sense—if $H$ is modeled as a random oracle.

如上述直观所示，该证明本质上依赖于把 $H$ 建模为随机预言机。$^2$ 具体而言，证明依赖两个事实：(1) 获知 $H(h^y)$ 的唯一途径是向 $H$ 显式查询 $h^y$，而这意味着攻击者已经求解了一个 CDH 实例（这在 6.5.1 节中称为“可提取性”）；(2) 若攻击者没有向 $H$ 查询 $h^y$，那么在攻击者看来 $H(h^y)$ 是均匀的。这些性质只有当 $H$ 被建模为随机预言机时才成立——事实上，也只有在这种建模下它们才有意义。

> $^2$ This is true as long as we wish to rely only on the CDH assumption. As noted earlier, a proof without random oracles is possible if we rely on the stronger DDH assumption.

> $^2$ 只要我们希望只依赖 CDH 假设，情况便是如此。如前所述，若依赖更强的 DDH 假设，则可以不借助随机预言机给出证明。

THEOREM 12.21 If the CDH problem is hard relative to G, and H is modeled as a random oracle, then Construction 12.19 is CPA-secure.

定理 12.21　若 CDH 问题相对于 $\mathcal{G}$ 是困难的，且 $H$ 被建模为随机预言机，则构造 12.19 是选择明文安全的。

PROOF Let $\Pi$ denote Construction 12.19, and let $\mathcal{A}$ be a PPT adversary. We want to show that there is a negligible function $\mathsf{negl}$ such that

证明　令 $\Pi$ 表示构造 12.19，$\mathcal{A}$ 为 PPT 敌手。我们要证明存在可忽略函数 $\mathsf{negl}$ 使得

$$
\Pr[\mathsf{KEM}_{\mathcal{A},\Pi}^{\mathsf{cpa}}(n)=1]\leq\frac{1}{2}+\mathsf{negl}(n).
$$

The above probability is also taken over uniform choice of the function $H$, to which $\mathcal{A}$ is given oracle access.

上述概率还包括对函数 $H$ 的均匀选取，$\mathcal{A}$ 可以以预言机方式访问 $H$。

Consider an execution of experiment $\mathsf{KEM}_{\mathcal{A},\Pi}^{\mathsf{cpa}}(n)$ in which the public key is $\langle \mathbb{G}, q, g, h \rangle$ and the ciphertext is $c = g^y$, and let $\mathsf{Query}$ be the event that $\mathcal{A}$ queries $\mathsf{DH}_g(h, c) = h^y$ to $H$. We have

考虑实验 $\mathsf{KEM}_{\mathcal{A},\Pi}^{\mathsf{cpa}}(n)$ 的一次执行，其中公钥为 $\langle \mathbb{G}, q, g, h \rangle$、密文为 $c = g^y$，令 $\mathsf{Query}$ 表示 $\mathcal{A}$ 向 $H$ 查询 $\mathsf{DH}_g(h, c) = h^y$ 这一事件。有

$$
\begin{aligned}
\Pr[\mathsf{KEM}_{\mathcal{A},\Pi}^{\mathsf{cpa}}(n)=1]&=\Pr[\mathsf{KEM}_{\mathcal{A},\Pi}^{\mathsf{cpa}}(n)=1\land\overline{\mathsf{Query}}]\\
&\quad+\Pr[\mathsf{KEM}_{\mathcal{A},\Pi}^{\mathsf{cpa}}(n)=1\land\mathsf{Query}]\\
&\leq\Pr[\mathsf{KEM}_{\mathcal{A},\Pi}^{\mathsf{cpa}}(n)=1\land\overline{\mathsf{Query}}]+\Pr[\mathsf{Query}].
\end{aligned} \tag{12.18}
$$

If $\Pr[\overline{\mathsf{Query}}] = 0$ then $\Pr[\mathsf{KEM}_{\mathcal{A},\Pi}^{\mathsf{cpa}}(n) = 1 \land \overline{\mathsf{Query}}] = 0$. Otherwise,

若 $\Pr[\overline{\mathsf{Query}}] = 0$，则 $\Pr[\mathsf{KEM}_{\mathcal{A},\Pi}^{\mathsf{cpa}}(n) = 1 \land \overline{\mathsf{Query}}] = 0$。否则，

$$
\begin{aligned}
\Pr[\mathsf{KEM}_{\mathcal{A},\Pi}^{\mathsf{cpa}}(n)=1\land\overline{\mathsf{Query}}]&=\Pr[\mathsf{KEM}_{\mathcal{A},\Pi}^{\mathsf{cpa}}(n)=1\mid\overline{\mathsf{Query}}]\cdot\Pr[\overline{\mathsf{Query}}]\\
&\leq\Pr[\mathsf{KEM}_{\mathcal{A},\Pi}^{\mathsf{cpa}}(n)=1\mid\overline{\mathsf{Query}}].
\end{aligned}
$$

In experiment $\mathsf{KEM}_{\mathcal{A},\Pi}^{\mathsf{cpa}}(n)$, the adversary $\mathcal{A}$ is given the public key and the ciphertext, plus either the encapsulated key $k \overset{\mathrm{def}}{=} H(h^y)$ or a uniform key. If Query does not occur, then $k$ is uniformly distributed from the perspective of the adversary, and so there is no way $\mathcal{A}$ can distinguish between these two possibilities. This means that

在实验 $\mathsf{KEM}_{\mathcal{A},\Pi}^{\mathsf{cpa}}(n)$ 中，敌手 $\mathcal{A}$ 获得公钥和密文，外加封装密钥 $k \overset{\mathrm{def}}{=} H(h^y)$ 或一个均匀密钥。若事件 $\mathsf{Query}$ 不发生，那么在敌手看来 $k$ 服从均匀分布，因此 $\mathcal{A}$ 无法区分这两种可能。这意味着

$$
\Pr[\mathsf{KEM}_{\mathcal{A},\Pi}^{\mathsf{cpa}}(n)=1\mid\overline{\mathsf{Query}}]=\frac{1}{2}.
$$

Returning to Equation (12.18), we thus have

回到式 (12.18)，于是有

$$
\Pr[\mathsf{KEM}_{{\mathcal A},\Pi}^{\mathsf{cpa}}(n)=1]\leq\frac{1}{2}+\Pr[\mathsf{Query}].
$$

We next show that $\Pr[\mathsf{Query}]$ is negligible, completing the proof.

下面证明 $\Pr[\mathsf{Query}]$ 是可忽略的，由此完成证明。

Let $t = t(n)$ be a (polynomial) upper bound on the number of queries that $\mathcal{A}$ makes to the random oracle $H$. Define the following PPT algorithm $\mathcal{A}^{\prime}$ for the CDH problem relative to $\mathcal{G}$:

设 $t = t(n)$ 是 $\mathcal{A}$ 向随机预言机 $H$ 发起查询次数的（多项式）上界。定义如下求解相对于 $\mathcal{G}$ 的 CDH 问题的 PPT 算法 $\mathcal{A}^{\prime}$：

Algorithm A':

The algorithm is given $\mathbb{G}, q, g, h, c$ as input.

- Set $pk := \langle \mathbb{G}, q, g, h \rangle$ and choose a uniform $k \in \{0,1\}^{\ell}$.

- Run $\mathcal{A}(pk, c, k)$. When $\mathcal{A}$ makes a query to $H$, answer it by choosing a fresh, uniform $\ell$-bit string.

- At the end of $\mathcal{A}$'s execution, let $y_1, \ldots, y_t$ be the list of queries that $\mathcal{A}$ has made to $H$. Choose a uniform index $i \in \{1, \ldots, t\}$ and output $y_i$.

算法 A'：

算法以 $\mathbb{G}, q, g, h, c$ 为输入。

- 令 $pk := \langle \mathbb{G}, q, g, h \rangle$，并均匀选取 $k \in \{0,1\}^{\ell}$。

- 运行 $\mathcal{A}(pk, c, k)$。当 $\mathcal{A}$ 向 $H$ 发起查询时，选取一个全新的均匀 $\ell$ 比特串作为回答。

- 在 $\mathcal{A}$ 执行结束时，设 $y_1, \ldots, y_t$ 为 $\mathcal{A}$ 已向 $H$ 发起的查询列表。均匀选取下标 $i \in \{1, \ldots, t\}$ 并输出 $y_i$。

We are interested in the probability with which $\mathcal{A}^{\prime}$ solves the CDH problem, i.e., $\Pr[\mathcal{A}^{\prime}(\mathbb{G}, q, g, h, c) = \mathsf{DH}_g(h, c)]$, where the probability is taken over $\mathbb{G}, q, g$ output by $\mathcal{G}(1^n)$, uniform $h, c \in \mathbb{G}$, and the randomness of $\mathcal{A}^{\prime}$. To analyze this probability, note first that event $\mathsf{Query}$ is still well-defined in the execution of $\mathcal{A}^{\prime}$, even though $\mathcal{A}^{\prime}$ cannot detect whether it occurs. Moreover, the probability of event $\mathsf{Query}$ when $\mathcal{A}$ is run as a subroutine by $\mathcal{A}^{\prime}$ is identical to the probability of $\mathsf{Query}$ in experiment $\mathsf{KEM}_{\mathcal{A},\Pi}^{\mathsf{cpa}}(n)$. This follows because the view of $\mathcal{A}$ is identical in both cases until event $\mathsf{Query}$ occurs: in each case, $\mathbb{G}, q, g$ are output by $\mathcal{G}(1^n)$; in each case, $h$ and $c$ are uniform elements of $\mathbb{G}$ and $k$ is a uniform $\ell$-bit string, and in each case queries to $H$ other than $H(\mathsf{DH}_g(h, c))$ are answered with a uniform $\ell$-bit string. (In $\mathsf{KEM}_{\mathcal{A},\Pi}^{\mathsf{cpa}}(n)$, the query $H(\mathsf{DH}_g(h, c))$ is answered with the actual encapsulated key, which is equal to $k$ with probability $1/2$, whereas when $\mathcal{A}$ is run as a subroutine by $\mathcal{A}^{\prime}$ the query $H(\mathsf{DH}_g(h, c))$ is answered with a uniform $\ell$-bit string that is independent of $k$. But when this query is made, event $\mathsf{Query}$ occurs.)

我们关心 $\mathcal{A}^{\prime}$ 求解 CDH 问题的概率，即 $\Pr[\mathcal{A}^{\prime}(\mathbb{G}, q, g, h, c) = \mathsf{DH}_g(h, c)]$，其中概率取自 $\mathcal{G}(1^n)$ 输出的 $\mathbb{G}, q, g$、均匀的 $h, c \in \mathbb{G}$ 以及 $\mathcal{A}^{\prime}$ 自身的随机性。为分析该概率，首先注意：即使 $\mathcal{A}^{\prime}$ 无法检测事件 $\mathsf{Query}$ 是否发生，该事件在 $\mathcal{A}^{\prime}$ 的执行中仍然是良定义的。而且，$\mathcal{A}$ 作为 $\mathcal{A}^{\prime}$ 的子程序运行时事件 $\mathsf{Query}$ 的概率，与实验 $\mathsf{KEM}_{\mathcal{A},\Pi}^{\mathsf{cpa}}(n)$ 中 $\mathsf{Query}$ 的概率相同。这是因为，在事件 $\mathsf{Query}$ 发生之前，$\mathcal{A}$ 在两种情形下的视图完全相同：两种情形中，$\mathbb{G}, q, g$ 都由 $\mathcal{G}(1^n)$ 输出；$h$ 和 $c$ 都是 $\mathbb{G}$ 中的均匀元素，$k$ 都是均匀的 $\ell$ 比特串；对 $H$ 的除 $H(\mathsf{DH}_g(h, c))$ 以外的查询，都以均匀的 $\ell$ 比特串作答。（在 $\mathsf{KEM}_{\mathcal{A},\Pi}^{\mathsf{cpa}}(n)$ 中，查询 $H(\mathsf{DH}_g(h, c))$ 以真实的封装密钥作答，它以 $1/2$ 的概率等于 $k$；而当 $\mathcal{A}$ 作为 $\mathcal{A}^{\prime}$ 的子程序运行时，该查询以与 $k$ 独立的均匀 $\ell$ 比特串作答。但一旦发起这个查询，事件 $\mathsf{Query}$ 就发生了。）

Finally, observe that when $\mathsf{Query}$ occurs then $\mathsf{DH}_g(h,c) \in \{y_1,\ldots,y_t\}$ by definition, and so $\mathcal{A}^{\prime}$ outputs the correct result $\mathsf{DH}_g(h,c)$ with probability at least $1/t$. We therefore conclude that

最后注意，当 $\mathsf{Query}$ 发生时，由定义有 $\mathsf{DH}_g(h,c) \in \{y_1,\ldots,y_t\}$，因此 $\mathcal{A}^{\prime}$ 以至少 $1/t$ 的概率输出正确结果 $\mathsf{DH}_g(h,c)$。于是得出结论

$$
\Pr[\mathcal{A}^{\prime}(\mathbb{G},q,g,h,c)=\mathsf{DH}_{g}(h,c)]\geq\Pr[\mathsf{Query}]/t,
$$

or $\Pr[\mathsf{Query}] \leq t \cdot \Pr[\mathcal{A}^{\prime}(\mathbb{G}, q, g, h, c) = \mathsf{DH}_g(h, c)]$. Since the CDH problem is hard relative to $\mathcal{G}$ and $t$ is polynomial, this implies that $\Pr[\mathsf{Query}]$ is negligible and completes the proof.

即 $\Pr[\mathsf{Query}] \leq t \cdot \Pr[\mathcal{A}^{\prime}(\mathbb{G}, q, g, h, c) = \mathsf{DH}_g(h, c)]$。由于 CDH 问题相对于 $\mathcal{G}$ 是困难的且 $t$ 是多项式，这意味着 $\Pr[\mathsf{Query}]$ 是可忽略的，证毕。

In the next section we will see that Construction 12.19 can even be shown to be secure against chosen-ciphertext attacks based on a stronger variant of the CDH assumption (if we continue to model $H$ as a random oracle).

下一节将看到，若继续把 $H$ 建模为随机预言机，基于 CDH 假设的一个更强变体甚至可以证明构造 12.19 在选择密文攻击下是安全的。

### 12.4.4 \*Chosen-Ciphertext Security and DHIES/ECIES　\*选择密文安全与 DHIES/ECIES

The El Gamal encryption scheme is vulnerable to chosen-ciphertext attacks. This follows from the fact that it is malleable. Recall that an encryption scheme is malleable, informally, if given a ciphertext $c$ that is an encryption of some unknown message $m$, it is possible to generate a modified ciphertext $c^{\prime}$ that is an encryption of a message $m^{\prime}$ having some known relation to $m$. In the case of El Gamal encryption, consider an adversary $\mathcal{A}$ who intercepts a ciphertext $c = \langle c_1, c_2 \rangle$ encrypted using the public key $pk = \langle \mathbb{G}, q, g, h \rangle$, and who then constructs the modified ciphertext $c^{\prime} = \langle c_1, c_2^{\prime} \rangle$ where $c^{\prime}_2 = c_2 \cdot \alpha$ for some $\alpha \in \mathbb{G}$. If $c$ is an encryption of a message $m \in \mathbb{G}$ (which may be unknown to $\mathcal{A}$), we have $c_1 = g^y$ and $c_2 = h^y \cdot m$ for some $y \in \mathbb{Z}_q$. But then

El Gamal 加密方案不能抵抗选择密文攻击，这是因为它具有可延展性。回顾一下：非正式地说，若给定某个未知消息 $m$ 的加密 $c$ 后，能够生成修改后的密文 $c^{\prime}$，使其成为与 $m$ 有某种已知关系的消息 $m^{\prime}$ 的加密，则称该加密方案是可延展的。就 El Gamal 加密而言，考虑敌手 $\mathcal{A}$ 截获了用公钥 $pk = \langle \mathbb{G}, q, g, h \rangle$ 加密的密文 $c = \langle c_1, c_2 \rangle$，然后构造修改后的密文 $c^{\prime} = \langle c_1, c_2^{\prime} \rangle$，其中 $c^{\prime}_2 = c_2 \cdot \alpha$，$\alpha \in \mathbb{G}$ 为某个群元素。若 $c$ 是消息 $m \in \mathbb{G}$（$\mathcal{A}$ 可能并不知道 $m$）的加密，则对某个 $y \in \mathbb{Z}_q$ 有 $c_1 = g^y$ 且 $c_2 = h^y \cdot m$。但这样一来

$$
c_{1}=g^{y}\quad\text{and}\quad c_{2}^{\prime}=h^{y}\cdot(\alpha\cdot m),
$$

and so $c^{\prime}$ is a valid encryption of the message $\alpha \cdot m$. In other words, $\mathcal{A}$ can transfoan encryption of the (unknown) message $m$ into an encryption of the (unknown) message $\alpha \cdot m$. As discussed in Scenario 3 in Section 12.2.3, this sort of attack can have serious consequences.

于是 $c^{\prime}$ 就是消息 $\alpha \cdot m$ 的有效加密。换言之，$\mathcal{A}$ 可以把（未知）消息 $m$ 的加密变换为（未知）消息 $\alpha \cdot m$ 的加密。如 12.2.3 节场景 3 所讨论的，这类攻击可能造成严重后果。

The KEM discussed in the previous section might also be malleable depending on the key-derivation function $H$ being used. If $H$ is modeled as a random oracle, however, then such attacks no longer seem possible. In fact, one can prove in this case that Construction 12.19 is CCA-secure (which, as we have noted, implies non-malleability) based on the gap-CDH assumption. Recall the CDH assumption is that given group elements $g^x$ and $g^y$ (for some generator $g$), it is infeasible to compute $g^{xy}$. The gap-CDH assumption says that this remains infeasible even given access to an oracle $\mathcal{O}_y$ such that $\mathcal{O}_y(U, V)$ returns 1 exactly when $V = U^y$. Stated differently, the gap-CDH assumption is that the CDH problem remains hard even given an oracle that solves the DDH problem. (We do not give a formal definition since we do not use the assumption in the rest of the book.) The gap-CDH assumption is believed to hold for all cryptographic groups in which the DDH assumption holds.

上一节讨论的 KEM 也可能是可延展的，这取决于所使用的密钥派生函数 $H$。然而，若把 $H$ 建模为随机预言机，这类攻击似乎就不再可行。事实上，这种情况下可以基于 gap-CDH 假设证明构造 12.19 是选择密文安全的（如前所述，这意味着不可延展性）。回顾 CDH 假设：给定群元素 $g^x$ 和 $g^y$（对某个生成元 $g$），计算 $g^{xy}$ 是不可行的。gap-CDH 假设则称，即使攻击者能访问一个满足“$\mathcal{O}_y(U, V)$ 恰在 $V = U^y$ 时返回 1”的预言机 $\mathcal{O}_y$，上述计算仍然不可行。换言之，gap-CDH 假设是说：即使给定一个能求解 DDH 问题的预言机，CDH 问题仍然是困难的。（本书其余部分不再使用该假设，故不给出正式定义。）人们相信，在所有 DDH 假设成立的密码学群中，gap-CDH 假设都成立。

A proof of the following is very similar to the proof of Theorem 12.38.

下面定理的证明与定理 12.38 的证明非常相似。

THEOREM 12.22 If the gap-CDH problem is hard relative to G, and H is modeled as a random oracle, then Construction 12.19 is CCA-secure.

定理 12.22　若 gap-CDH 问题相对于 $\mathcal{G}$ 是困难的，且 $H$ 被建模为随机预言机，则构造 12.19 是选择密文安全的。

It is interesting to observe that the same construction (namely, Construction 12.19) can be analyzed under different assumptions and in different models, yielding different results. Assuming only that the DDH problem is hard (and for $H$ chosen appropriately), the scheme is CPA-secure. If we model $H$ as a random oracle (which imposes more stringent requirements on H), then we obtain CPA-security under the weaker CDH assumption, and CCA-security under the stronger gap-CDH assumption.

值得注意的是，同一个构造（即构造 12.19）可以在不同的假设和不同的模型下进行分析，并得出不同的结果。仅假设 DDH 问题困难（并适当选取 $H$）时，该方案是选择明文安全的。若把 $H$ 建模为随机预言机（这对 $H$ 提出了更严格的要求），则在更弱的 CDH 假设下得到选择明文安全，在更强的 gap-CDH 假设下得到选择密文安全。

**CONSTRUCTION 12.23**

Let $\mathcal{G}$ be as in the text. Let $\Pi_E = (\mathsf{Enc}^{\prime}, \mathsf{Dec}^{\prime})$ be a private-key encryption scheme, and let $\Pi_M = (\mathsf{Mac}, \mathsf{Vrfy})$ be a message authentication code. Define a public-key encryption scheme as follows:

- Gen: On input $1^n$ run $\mathcal{G}(1^n)$ to obtain $(\mathbb{G}, q, g)$. Choose uniform $x \in \mathbb{Z}_q$, set $h := g^x$, and specify a function $H : \mathbb{G} \to \{0,1\}^{2n}$. The public key is $\langle \mathbb{G}, q, g, h, H \rangle$ and the private key is $\langle \mathbb{G}, q, g, x, H \rangle$.

- Enc: On input a public key $pk = \langle \mathbb{G}, q, g, h, H \rangle$, choose a uniform $y \in \mathbb{Z}_q$ and set $k_E \| k_M := H(h^y)$. Compute $c^{\prime} \leftarrow \mathsf{Enc}_{k_E}^{\prime}(m)$, and output the ciphertext $\langle g^y, c^{\prime}, \mathsf{Mac}_{k_M}(c^{\prime}) \rangle$.

- Dec: On input a private key $sk = \langle \mathbb{G}, q, g, x, H \rangle$ and a ciphertext $\langle c, c^{\prime}, t \rangle$, output $\perp$ if $c \notin \mathbb{G}$. Else, compute $k_E \parallel k_M := H(c^x)$. If $\mathsf{Vrfy}_{k_M}(c^{\prime}, t) \neq 1$ then output $\perp$; otherwise, output $\mathsf{Dec}_{k_E}^{\prime}(c^{\prime})$.

**DHIES/ECIES.**

**构造 12.23**

设 $\mathcal{G}$ 如正文所述。令 $\Pi_E = (\mathsf{Enc}^{\prime}, \mathsf{Dec}^{\prime})$ 为私钥加密方案，$\Pi_M = (\mathsf{Mac}, \mathsf{Vrfy})$ 为消息认证码。定义如下公钥加密方案：

- Gen：输入 $1^n$，运行 $\mathcal{G}(1^n)$ 得到 $(\mathbb{G}, q, g)$。均匀选取 $x \in \mathbb{Z}_q$，令 $h := g^x$，并指定函数 $H : \mathbb{G} \to \{0,1\}^{2n}$。公钥为 $\langle \mathbb{G}, q, g, h, H \rangle$，私钥为 $\langle \mathbb{G}, q, g, x, H \rangle$。

- Enc：输入公钥 $pk = \langle \mathbb{G}, q, g, h, H \rangle$，均匀选取 $y \in \mathbb{Z}_q$，令 $k_E \| k_M := H(h^y)$。计算 $c^{\prime} \leftarrow \mathsf{Enc}_{k_E}^{\prime}(m)$，输出密文 $\langle g^y, c^{\prime}, \mathsf{Mac}_{k_M}(c^{\prime}) \rangle$。

- Dec：输入私钥 $sk = \langle \mathbb{G}, q, g, x, H \rangle$ 和密文 $\langle c, c^{\prime}, t \rangle$，若 $c \notin \mathbb{G}$ 则输出 $\perp$。否则，计算 $k_E \parallel k_M := H(c^x)$。若 $\mathsf{Vrfy}_{k_M}(c^{\prime}, t) \neq 1$ 则输出 $\perp$；否则输出 $\mathsf{Dec}_{k_E}^{\prime}(c^{\prime})$。

**DHIES/ECIES。**

CCA-secure encryption with Construction 12.19. Combining the KEM in Construction 12.19 with any CCA-secure private-key encryption scheme yields a CCA-secure public-key encryption scheme. (See Theorem 12.14.) Instantiating this approach using Construction 5.6 for the private-key component matches what is done in DHIES/ECIES, variants of which are included in the ISO/IEC 18033-2 standard for public-key encryption. (See Construction 12.23.) Encryption of a message $m$ in these schemes takes the form

基于构造 12.19 的选择密文安全加密。把构造 12.19 中的 KEM 与任意选择密文安全的私钥加密方案组合，即可得到选择密文安全的公钥加密方案。（见定理 12.14。）用构造 5.6 实例化其中的私钥加密部分，正好对应 DHIES/ECIES 的做法，其变体已被纳入公钥加密标准 ISO/IEC 18033-2。（见构造 12.23。）在这些方案中，消息 $m$ 的加密形式为

$$
\langle g^{y},~\mathsf{Enc}_{k_{E}}^{\prime}(m),\mathsf{Mac}_{k_{M}}(c^{\prime})\rangle,
$$

where $\mathsf{Enc}^{\prime}$ denotes a CPA-secure private-key encryption scheme and $c^{\prime}$ denotes $\mathsf{Enc}_{k_E}^{\prime}(m)$. DHIES, the Diffie–Hellman Integrated Encryption Scheme, can be used generically to refer to any scheme of this form, or to refer specifically to the case when the group $\mathbb{G}$ is a cyclic subgroup of a finite field. ECIES, the Elliptic Curve Integrated Encryption Scheme, refers to the case when $\mathbb{G}$ is an elliptic-curve group. We remark that in Construction 12.23 it is critical to check during decryption that $c$, the first component of the ciphertext, is in $\mathbb{G}$. Otherwise, an attacker might request decryption of a malformed ciphertext $\langle c, c^{\prime}, t \rangle$ in which $c \notin \mathbb{G}$; decrypting such a ciphertext (i.e., without returning $\perp$) might leak information about the private key.

其中 $\mathsf{Enc}^{\prime}$ 表示选择明文安全的私钥加密方案，$c^{\prime}$ 表示 $\mathsf{Enc}_{k_E}^{\prime}(m)$。DHIES 即 Diffie–Hellman 集成加密方案（Diffie–Hellman Integrated Encryption Scheme），既可泛指具有这种形式的任何方案，也可特指群 $\mathbb{G}$ 为有限域（乘法群）中循环子群的情形。ECIES 即椭圆曲线集成加密方案（Elliptic Curve Integrated Encryption Scheme），指 $\mathbb{G}$ 为椭圆曲线群的情形。需要指出，在构造 12.23 中，解密时检查密文的第一个分量 $c$ 是否属于 $\mathbb{G}$ 至关重要。否则，攻击者可能请求解密一个满足 $c \notin \mathbb{G}$ 的畸形密文 $\langle c, c^{\prime}, t \rangle$；对这样的密文进行解密（即不返回 $\perp$）可能泄露私钥信息。

By Theorem 5.7, encrypting a message and then applying a (strong) message authentication code yields a CCA-secure private-key encryption scheme. Combining this with Theorem 12.14, we conclude:

由定理 5.7，先加密消息再施加（强）消息认证码，可得到选择密文安全的私钥加密方案。结合定理 12.14，得出结论：

COROLLARY 12.24 Let $\Pi_E$ be a CPA-secure private-key encryption scheme, and let $\Pi_M$ be a strongly secure message authentication code. If the gap-CDH problem is hard relative to $\mathcal{G}$, and $H$ is modeled as a random oracle, then Construction 12.23 is a CCA-secure public-key encryption scheme.

推论 12.24　令 $\Pi_E$ 为选择明文安全的私钥加密方案，$\Pi_M$ 为强安全的消息认证码。若 gap-CDH 问题相对于 $\mathcal{G}$ 是困难的，且 $H$ 被建模为随机预言机，则构造 12.23 是选择密文安全的公钥加密方案。
