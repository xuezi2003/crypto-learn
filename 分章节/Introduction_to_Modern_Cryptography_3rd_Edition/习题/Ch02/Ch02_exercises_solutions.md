# 第二章　习题解答

> *Introduction to Modern Cryptography (3rd ed.), Katz & Lindell — Chapter 2 Exercises*

---

## 习题 2.1　不妨假设 Gen 均匀选钥

> **题目**　Prove that, by redefining the key space, we may assume that the key-generation algorithm Gen chooses a uniform key from the key space, without changing $\Pr[C = c \mid M = m]$ for any $m, c$.
>
> Hint: Define the key space to be the set of all possible random bits used by the randomized algorithm Gen.
>
> **题目**　证明：通过重新定义密钥空间，可以假设密钥生成算法 Gen 从密钥空间中均匀选钥，且任意 $m,c$ 的 $\Pr[C=c\mid M=m]$ 不变。
>
> 提示：把密钥空间定义为随机化算法 Gen 可能用到的所有随机比特的集合。

设随机化算法 Gen 使用 $n$ 位均匀随机带 $r\in\{0,1\}^{n}$，记 $\mathsf{Gen}(r)$ 为 Gen 在随机带 $r$ 上的（确定性）输出。重定义方案如下：

- 新密钥空间 $\mathcal{K}^{\prime}=\{0,1\}^{n}$，$\mathsf{Gen}^{\prime}$ 均匀输出 $r\leftarrow\{0,1\}^{n}$；
- $\mathsf{Enc}^{\prime}_r(m)=\mathsf{Enc}_{\mathsf{Gen}(r)}(m)$，$\mathsf{Dec}^{\prime}_r(c)=\mathsf{Dec}_{\mathsf{Gen}(r)}(c)$。

由于 $r$ 均匀时 $\mathsf{Gen}(r)$ 的分布恰好就是原 Gen 的输出分布，对任意 $m\in\mathcal{M}$、$c\in\mathcal{C}$：

$$\Pr[\mathsf{Enc}^{\prime}_{K^{\prime}}(m)=c]=\Pr_{r}\big[\mathsf{Enc}_{\mathsf{Gen}(r)}(m)=c\big]=\Pr[\mathsf{Enc}_{K}(m)=c].$$

由式 (2.2)，$\Pr[C=c\mid M=m]=\Pr[\mathsf{Enc}_K(m)=c]$，故新方案下该条件概率不变。正确性同样保持（$\mathsf{Gen}(r)$ 本身就是原方案的一个合法密钥）。因此总可以不失一般性地假设 Gen 从密钥空间中均匀选钥。

---

## 习题 2.2　不妨假设 Enc 是确定算法

> **题目**　Prove that, by redefining the key space as well as the encryption algorithm, we may assume that encryption is deterministic without changing $\Pr[C=c\mid M=m]$ for any $m, c$.
> **题目**　证明：通过同时换掉密钥空间和加密算法（把 Enc 的随机带也塞进密钥），可以假设 Enc 是确定性的，且任意 $m,c$ 的 $\Pr[C=c\mid M=m]$ 不变。

设随机化的 Enc 对每个密钥使用 $s$ 位均匀随机带 $r\in\{0,1\}^{s}$，记 $\mathsf{Enc}_k(m;r)$ 为 Enc 在随机带 $r$ 上的确定输出。思路是把"加密的硬币"塞进密钥：

- 新密钥空间 $\mathcal{K}^{\prime}=\mathcal{K}\times\{0,1\}^{s}$；$\mathsf{Gen}^{\prime}$ 先运行原 Gen 得到 $k$，再独立均匀地选 $r\leftarrow\{0,1\}^{s}$，输出 $(k,r)$；
- $\mathsf{Enc}^{\prime}_{(k,r)}(m)=\mathsf{Enc}_k(m;r)$（随机带已固定在密钥里，故为确定算法）；
- $\mathsf{Dec}^{\prime}_{(k,r)}(c)=\mathsf{Dec}_k(c)$。

对任意 $m, c$：

$$\Pr[\mathsf{Enc}^{\prime}_{K^{\prime}}(m)=c]=\sum_{k}\Pr[K=k]\cdot\Pr_{r}\big[\mathsf{Enc}_k(m;r)=c\big]=\sum_{k}\Pr[K=k]\cdot\Pr[\mathsf{Enc}_k(m)=c]=\Pr[\mathsf{Enc}_K(m)=c],$$

其中第二步是因为 $r$ 均匀时 $\mathsf{Enc}_k(m;r)$ 的分布就是原随机化加密 $\mathsf{Enc}_k(m)$ 的分布。故 $\Pr[C=c\mid M=m]$ 不变，而 $\mathsf{Enc}^{\prime}$ 是确定的。正确性也保持：$\mathsf{Dec}^{\prime}_{(k,r)}(\mathsf{Enc}^{\prime}_{(k,r)}(m))=\mathsf{Dec}_k(\mathsf{Enc}_k(m;r))=m$ 以概率 1 成立。

---

## 习题 2.3　"密文均匀分布"是完全保密的充分非必要条件

> **题目**　Prove or refute: An encryption scheme with message space $\mathcal{M}$ is perfectly secret if and only if for every probability distribution on $\mathcal{M}$ and every $c_0, c_1 \in \mathcal{C}$ we have $\Pr[C = c_0] = \Pr[C = c_1]$.
> **题目**　证明或反驳：消息空间为 $\mathcal{M}$ 的加密方案完全保密，当且仅当对 $\mathcal{M}$ 上的任意概率分布与任意 $c_0, c_1 \in \mathcal{C}$，都有 $\Pr[C = c_0] = \Pr[C = c_1]$。

**驳倒（iff 不成立）**：该条件（对任意明文分布，密文都在 $\mathcal{C}$ 上均匀）是**充分但非必要**的。

**充分性**：取集中在 $m$ 上的点质量分布，则 $\Pr[C=c]=\Pr[\mathsf{Enc}_K(m)=c]$。题设条件给出：对任意 $m$ 与任意 $c_0,c_1$，$\Pr[\mathsf{Enc}_K(m)=c_0]=\Pr[\mathsf{Enc}_K(m)=c_1]$，即 $\Pr[\mathsf{Enc}_K(m)=c]=1/|\mathcal{C}|$ 与 $m$ 无关。这满足式 (2.1)，由引理 2.5 方案完全保密。

**非必要（反例，官方题解思路）**：对一次一密稍作修改：$\mathsf{Enc}_k(m)=(m\oplus k)\,\|\,b$，其中 $b$ 独立于 $k,m$，以概率 ${1}/{4}$ 取 ${0}$、以概率 ${3}/{4}$ 取 ${1}$；$\mathsf{Dec}_k(c)$ 丢掉最后一位再异或 $k$。对任意 $m\in\{0,1\}^{\ell}$ 与 $c'=c\|b$：

$$\Pr[\mathsf{Enc}_K(m)=c']=\Pr[K=m\oplus c]\cdot\Pr[B=b]=2^{-\ell}\cdot\Pr[B=b],$$

取值与 $m$ 无关，由引理 2.5 该方案**完全保密**。但密文不均匀：$\Pr[C=0^{\ell+1}]=2^{-\ell}\cdot\frac14\neq 2^{-\ell}\cdot\frac34=\Pr[C=0^{\ell}1]$，题设条件不成立。故"iff"为假。

（直观：完全保密只要求密文分布**与明文无关**，并不要求它对 $c$ 均匀——每个 $c$ 的概率 $p_c$ 可以随 $c$ 变化，只要对所有 $m$ 相同即可。）

---

## 习题 2.4　后验等不等于先验，而不是所有消息等可能

> **题目**　Prove or refute: For every perfectly secret encryption scheme it holds that for every distribution on $\mathcal{M}$, every $m, m^{\prime} \in \mathcal{M}$, and every $c \in \mathcal{C}$: $\Pr[M=m\mid C=c]=\Pr[M=m^{\prime}\mid C=c]$.
> **题目**　证明或反驳：对每个完全保密的加密方案，对 $\mathcal{M}$ 上的任意分布、任意 $m, m^{\prime} \in \mathcal{M}$ 与任意 $c \in \mathcal{C}$，都有 $\Pr[M=m\mid C=c]=\Pr[M=m^{\prime}\mid C=c]$。

**驳倒。** 定义 2.3 要求的是同一 $m$ 的**后验等于先验**，并非要求看到密文后所有消息变得等可能。

反例就用教材例 2.1：单字符移位密码（由习题 2.14(a) 它完全保密），取 $\Pr[M=\mathtt{a}]=0.7$、$\Pr[M=\mathtt{z}]=0.3$。例 2.1 已算出

$$\Pr[M=\mathtt{a}\mid C=\mathtt{B}]=0.7\ \neq\ 0.3=\Pr[M=\mathtt{z}\mid C=\mathtt{B}].$$

即密文 $\mathtt{B}$ 没有泄露任何信息（后验恰等于各自的先验 ${0.7}$ 与 ${0.3}$），但两个后验概率显然不相等。题述命题为假。

---

## 习题 2.5　定义 2.6 中不妨假设敌手是确定的

> **题目**　Prove that in Definition 2.6 we may assume $\mathcal{A}$ is deterministic without loss of generality.
> **题目**　证明：在定义 2.6 中可以不失一般性地假设 $\mathcal{A}$ 是确定性的。

设 $\mathcal{A}$ 为随机化敌手，其随机带 $R$ 与实验中的其他随机性（Gen、$b$、Enc）独立。把 $\mathcal{A}$ 的硬币固定为 $r$ 所得确定敌手记为 $\mathcal{A}_r$，其成功概率记为 $p_r=\Pr\big[\mathsf{PrivK}^{\mathsf{eav}}_{\mathcal{A}_r,\Pi}=1\big]$。对 $R$ 取全概率：

$$\Pr\big[\mathsf{PrivK}^{\mathsf{eav}}_{\mathcal{A},\Pi}=1\big]=\sum_{r}\Pr[R=r]\cdot p_r.$$

若定义 2.6 的条件对所有**确定**敌手成立，则每个 $p_r=1/2$，于是加权和也是 $\sum_r\Pr[R=r]\cdot\frac12=\frac12$，即条件对所有随机化敌手自动成立。反过来，确定敌手本就是随机化敌手的子集，"对所有随机化敌手成立"当然蕴含"对所有确定敌手成立"。

故两种量化方式等价：随机化敌手的成功率只是若干确定敌手成功率的凸组合，不会超过其中最优者；在定义 2.6 中假设 $\mathcal{A}$ 确定不损失一般性。

---

## 习题 2.6　证明引理 2.7（完全保密 ⟺ 完全不可区分）

> **题目**　Prove Lemma 2.7.
> **题目**　证明引理 2.7：完全保密 ⟺ 完全不可区分。

**（⇒）完全保密 ⟹ 完全不可区分。** 由引理 2.5，式 (2.1) 成立：对任意 $m,m^{\prime}$ 与任意 $c$，

$$p_c\ \stackrel{\mathrm{def}}{=}\ \Pr[\mathsf{Enc}_K(m)=c]\ =\ \Pr[\mathsf{Enc}_K(m^{\prime})=c].$$

任取敌手 $\mathcal{A}$（由习题 2.5 可设其确定），设它输出 $(m_0,m_1)$，并在收到密文 $c$ 后输出 $b^{\prime}=\mathcal{A}(c)$。则

$$\begin{aligned}\Pr\big[\mathsf{PrivK}^{\mathsf{eav}}_{\mathcal{A},\Pi}=1\big]&=\frac12\Pr[\mathcal{A}(c)=0\mid b=0]+\frac12\Pr[\mathcal{A}(c)=1\mid b=1]\\ &=\frac12\sum_{c}p_c\,\mathbf{1}[\mathcal{A}(c)=0]+\frac12\sum_{c}p_c\,\mathbf{1}[\mathcal{A}(c)=1]\\ &=\frac12\sum_{c}p_c=\frac12,\end{aligned}$$

因为每个 $c$ 恰被 $\mathbf{1}[\mathcal{A}(c)=0]$、$\mathbf{1}[\mathcal{A}(c)=1]$ 之一计数。

**（⇐）逆否：不完全保密 ⟹ 不完全可区分。** 若不完全保密，由引理 2.5 存在 $m_0,m_1\in\mathcal{M}$ 与 $c_0\in\mathcal{C}$ 使 $\Pr[\mathsf{Enc}_K(m_0)=c_0]\neq\Pr[\mathsf{Enc}_K(m_1)=c_0]$；不妨设

$$p_0\stackrel{\mathrm{def}}{=}\Pr[\mathsf{Enc}_K(m_0)=c_0]\ >\ p_1\stackrel{\mathrm{def}}{=}\Pr[\mathsf{Enc}_K(m_1)=c_0].$$

构造 $\mathcal{A}$：输出 $(m_0,m_1)$；收到挑战密文 $c$ 后，若 $c=c_0$ 输出 ${0}$，否则输出均匀随机比特。则

$$\begin{aligned}\Pr\big[\mathsf{PrivK}^{\mathsf{eav}}_{\mathcal{A},\Pi}=1\big]&=\frac12\Big(p_0+\tfrac{1-p_0}{2}\Big)+\frac12\Big(\tfrac{1-p_1}{2}\Big)\\ &=\frac12+\frac{p_0-p_1}{4}\ >\ \frac12,\end{aligned}$$

故方案不是完全可区分的。$\blacksquare$

> **关于官方题解。** 官方题解（Solutions Manual）对逆否方向的构造与我们一致——"收到 $\tilde c$ 输出 ${0}$，否则均匀猜"，但其化简结果 $\tfrac14+\tfrac14\Pr[\mathsf{Enc}_K(m_0)=\tilde c]+\tfrac14\Pr[\mathsf{Enc}_K(m_1)\ne\tilde c]$ 写成 $\ne\tfrac12$ 时，隐含了 $\Pr[\mathsf{Enc}_K(m_0)=\tilde c]>\Pr[\mathsf{Enc}_K(m_1)=\tilde c]$ 这一"不妨设"假设（否则成功率反而 $<1/2$，不能反证）。我们上面的写法显式声明了"不妨设 $p_0>p_1$"，论证严格闭合。

---

## 习题 2.7　一次性密码本的十六进制异或

> **题目**　What is the ciphertext that results when the plaintext 0x012345 (written in hex) is encrypted using the one-time pad with key 0xFFEEDD?
> **题目**　用密钥 0xFFEEDD 的一次性密码本加密明文 0x012345（十六进制表示），所得密文是什么？

逐字节异或：

$$\mathtt{0x01}\oplus\mathtt{0xFF}=\mathtt{0xFE},\qquad \mathtt{0x23}\oplus\mathtt{0xEE}=\mathtt{0xCD},\qquad \mathtt{0x45}\oplus\mathtt{0xDD}=\mathtt{0x98},$$

（例如 $\texttt{0010 0011}\oplus\texttt{1110 1110}=\texttt{1100 1101}$。）故密文为

$$\mathtt{0xFECD98}.$$

---

## 习题 2.8　两个小方案是否完全保密

> **题目**　For each of the following encryption schemes, state whether the scheme is perfectly secret. Justify your answer in each case.
>
> **(a)**　The message space is $\mathcal{M} = \{0, \ldots, 4\}$, and Gen chooses a uniform key from the key space $\mathcal{K} = \{0, \ldots, 5\}$. $\mathsf{Enc}_k(m)$ returns $[m + k \bmod 5]$, and $\mathsf{Dec}_k(c)$ returns $[c - k \bmod 5]$.
>
> **(b)**　The message space is $\mathcal{M} = \{m \in \{0,1\}^{\ell} \mid \text{the last bit of } m \text{ is } 0\}$. Gen chooses a uniform key from $\{0,1\}^{\ell-1}$. $\mathsf{Enc}_k(m)$ returns ciphertext $m \oplus (k\|0)$, and $\mathsf{Dec}_k(c)$ returns $c \oplus (k\|0)$.
>
> **题目**　对下列各加密方案，判断其是否完全保密，并在每种情况下说明理由。
>
> **(a)**　消息空间为 $\mathcal{M} = \{0, \ldots, 4\}$，Gen 从密钥空间 $\mathcal{K} = \{0, \ldots, 5\}$ 中均匀选钥。$\mathsf{Enc}_k(m)$ 返回 $[m + k \bmod 5]$，$\mathsf{Dec}_k(c)$ 返回 $[c - k \bmod 5]$。
>
> **(b)**　消息空间为 $\mathcal{M} = \{m \in \{0,1\}^{\ell} \mid m \text{ 的末位为 } 0\}$。Gen 从 $\{0,1\}^{\ell-1}$ 中均匀选钥。$\mathsf{Enc}_k(m)$ 返回密文 $m \oplus (k\|0)$，$\mathsf{Dec}_k(c)$ 返回 $c \oplus (k\|0)$。

### (a) $\mathcal{M}=\{0,\dots,4\}$，$\mathcal{K}=\{0,\dots,5\}$ 均匀，$\mathsf{Enc}_k(m)=[m+k\bmod 5]$

**不完全保密。** 密钥空间比模数多一个元素，$k=0$ 与 $k=5$ 的作用相同（${5}\equiv0\pmod 5$），于是密文偏向明文本身：

$$\Pr[\mathsf{Enc}_K(0)=0]=\Pr[K\in\{0,5\}]=\frac{2}{6}=\frac13,\qquad \Pr[\mathsf{Enc}_K(1)=0]=\Pr[K=4]=\frac16.$$

两者不等，式 (2.1) 不满足，由引理 2.5 不完全保密。

### (b) $\mathcal{M}=\{m\in\{0,1\}^{\ell}\mid m\text{ 末位为 }0\}$，$\mathcal{K}=\{0,1\}^{\ell-1}$ 均匀，$\mathsf{Enc}_k(m)=m\oplus(k\|0)$

**完全保密。** 密文末位恒为 ${0}$，故 $\mathcal{C}=\{$末位为 ${0}$ 的 $\ell$ 位串$\}$，$|\mathcal{C}|=2^{\ell-1}$。对任意 $m\in\mathcal{M}$（末位为 ${0}$）与 $c\in\mathcal{C}$（末位为 ${0}$），$m\oplus c$ 末位为 ${0}$，故存在唯一的 $k^{\prime}\in\{0,1\}^{\ell-1}$ 使 $m\oplus c=k^{\prime}\|0$，于是

$$\Pr[\mathsf{Enc}_K(m)=c]=\Pr[K=k^{\prime}]=2^{-(\ell-1)},$$

与 $m,c$ 无关，由引理 2.5 完全保密。（实质是对前 $\ell-1$ 个"自由位"做一次性密码本；末位是公开已知的常数 ${0}$，不含任何信息。）

---

## 习题 2.9　$\mathsf{Enc}_k(m)=[m+k\bmod 3]$ 的三种参数

> **题目**　In each of the following schemes, $\mathsf{Enc}_k(m) = [m+k \mod 3]$. State in each case whether the scheme is perfectly secret, and justify your answers.
>
> **(a)**　The message space is $\mathcal{M} = \{0,1\}$, and Gen chooses a uniform key from the key space $\mathcal{K} = \{0,1\}$.
>
> **(b)**　The message space is $\mathcal{M} = \{0,1,2\}$, and Gen chooses a uniform key from the key space $\mathcal{K} = \{0,1,2\}$.
>
> **(c)**　The message space is $\mathcal{M} = \{0,1\}$, and Gen chooses a uniform key from the key space $\mathcal{K} = \{0,1,2\}$.
>
> **题目**　下列各方案中 $\mathsf{Enc}_k(m) = [m+k \mod 3]$。逐一判断各方案是否完全保密，并说明理由。
>
> **(a)**　消息空间为 $\mathcal{M} = \{0,1\}$，Gen 从密钥空间 $\mathcal{K} = \{0,1\}$ 中均匀选钥。
>
> **(b)**　消息空间为 $\mathcal{M} = \{0,1,2\}$，Gen 从密钥空间 $\mathcal{K} = \{0,1,2\}$ 中均匀选钥。
>
> **(c)**　消息空间为 $\mathcal{M} = \{0,1\}$，Gen 从密钥空间 $\mathcal{K} = \{0,1,2\}$ 中均匀选钥。

### (a) $\mathcal{M}=\{0,1\}$，$\mathcal{K}=\{0,1\}$ 均匀

**不完全保密。** 枚举全部四个 $(m,k)$ 组合：$m=0$ 时 $c\in\{0,1\}$ 各以概率 ${1}/{2}$；$m=1$ 时 $c\in\{1,2\}$ 各以概率 ${1}/{2}$（注意 ${1}+1\bmod 3=2$ 发生了回绕）。于是

$$\Pr[\mathsf{Enc}_K(0)=0]=\frac12\ \neq\ 0=\Pr[\mathsf{Enc}_K(1)=0].$$

陷阱正在于此：模数 ${3}$ 与消息/密钥取值范围 $\{0,1\}$ 不匹配，回绕只在 $(m,k)=(1,1)$ 时发生，破坏了平衡。

### (b) $\mathcal{M}=\mathcal{K}=\{0,1,2\}$ 均匀

**完全保密。** 对任意 $m,c\in\mathbb{Z}_3$：

$$\Pr[\mathsf{Enc}_K(m)=c]=\Pr[K=c-m\bmod 3]=\frac13,$$

由引理 2.5 完全保密。这就是群 $\mathbb{Z}_3$ 上的一次性密码本（也可用香农定理：$|\mathcal{M}|=|\mathcal{K}|=|\mathcal{C}|=3$，且每个 $(m,c)$ 对应唯一密钥 $k=c-m\bmod 3$）。

### (c) $\mathcal{M}=\{0,1\}$，$\mathcal{K}=\{0,1,2\}$ 均匀

**完全保密。** 对任意 $m\in\{0,1\}$ 与 $c\in\{0,1,2\}$，恰有唯一密钥 $k=c-m\bmod 3$ 使 $\mathsf{Enc}_k(m)=c$，故

$$\Pr[\mathsf{Enc}_K(m)=c]=\frac13,$$

与 $m,c$ 无关，由引理 2.5 完全保密。注意这里 $|\mathcal{K}|=3>|\mathcal{M}|=2$，与定理 2.11 不矛盾——该定理只要求 $|\mathcal{K}|\ge|\mathcal{M}|$。

（2.8、2.9 各小题的密文分布已逐一枚举验证，见 `solve_ex2_8_2_9.py`。）

---

## 习题 2.10　变长消息空间 $\mathcal{M}=\{0,1\}^{\le\ell}$

> **题目**　The following questions concern the message space $\mathcal{M} = \{0,1\}^{\le\ell}$, the set of all nonempty binary strings of length at most $\ell$.
>
> **(a)**　Consider the encryption scheme in which Gen chooses a uniform key from $\mathcal{K} = \{0,1\}^{\ell}$, and $\mathsf{Enc}_k(m)$ outputs $k_{|m|} \oplus m$, where $k_t$ denotes the first $t$ bits of $k$. Show that this scheme is not perfectly secret for message space $\mathcal{M}$.
>
> **(b)**　Design a perfectly secret encryption scheme for message space $\mathcal{M}$.
>
> **题目**　以下问题涉及消息空间 $\mathcal{M} = \{0,1\}^{\le\ell}$，即所有长度不超过 $\ell$ 的非空二进制串的集合。
>
> **(a)**　考虑如下加密方案：Gen 从 $\mathcal{K} = \{0,1\}^{\ell}$ 中均匀选钥，$\mathsf{Enc}_k(m)$ 输出 $k_{|m|} \oplus m$，其中 $k_t$ 表示 $k$ 的前 $t$ 位。证明该方案在消息空间 $\mathcal{M}$ 上不是完全保密的。
>
> **(b)**　为消息空间 $\mathcal{M}$ 设计一个完全保密的加密方案。

### (a) $\mathcal{K}=\{0,1\}^{\ell}$ 均匀、$\mathsf{Enc}_k(m)=k_{|m|}\oplus m$ 不完全保密

密文长度恒等于明文长度，**长度本身泄露信息**。取 $c=00$（长 2 的密文）：

$$\Pr[\mathsf{Enc}_K(0)=00]=0\quad(\text{长 1 的明文输出长 1 的密文}),\qquad \Pr[\mathsf{Enc}_K(00)=00]=\Pr[k\text{ 前两位为 }00]=\frac14>0.$$

式 (2.1) 不满足，由引理 2.5 不完全保密。

### (b) 设计完全保密方案

先定长编码：$\mathrm{pad}(m)=m\,\|\,1\,\|\,0^{\ell-|m|}$，长度恒为 $\ell+1$，且可逆（解码时从尾部删去所有 ${0}$，再删去紧挨着的那个 ${1}$，剩余即 $m$）。方案：

- **Gen**：均匀选 $k\leftarrow\{0,1\}^{\ell+1}$；
- **Enc**：$\mathsf{Enc}_k(m)=\mathrm{pad}(m)\oplus k$；
- **Dec**：$\mathsf{Dec}_k(c)=\mathrm{unpad}(c\oplus k)$。

对任意 $m\in\mathcal{M}$、$c\in\{0,1\}^{\ell+1}$：

$$\Pr[\mathsf{Enc}_K(m)=c]=\Pr[K=\mathrm{pad}(m)\oplus c]=2^{-(\ell+1)},$$

由引理 2.5 完全保密。密钥量比一次性密码本多 1 位，用于隐藏长度：$|\mathcal{M}|=\sum_{i=1}^{\ell}2^{i}=2^{\ell+1}-2\le 2^{\ell+1}=|\mathcal{K}|$，符合定理 2.11。

---

## 习题 2.11　剔除全零密钥的一次性密码本

> **题目**　When using the one-time pad with the key $k = 0^\ell$, the message is sent in the clear. Someone suggests modifying the one-time pad by having Gen choose $k$ uniformly from the set of nonzero keys. Is this modified scheme still perfectly secret?
> **题目**　使用一次性密码本时，若密钥 $k = 0^\ell$，消息将以明文形式发送。有人建议修改一次性密码本：令 Gen 从非零密钥的集合中均匀选取 $k$。修改后的方案是否仍然完全保密？

**不再完全保密。** 剔除了 ${0}^{\ell}$ 后，明文永远不可能等于密文：

$$\Pr[\mathsf{Enc}_K(m)=m]=\Pr[K=0^{\ell}]=0,$$

而对任意 $m^{\prime}\neq m$：

$$\Pr[\mathsf{Enc}_K(m^{\prime})=m]=\Pr[K=m^{\prime}\oplus m]=\frac{1}{2^{\ell}-1}>0.$$

由引理 2.5（取 $c=m$）不完全保密。直观：攻击者看到密文 $c$ 即可排除"明文就是 $c$"。

显式敌手：输出 $m_0\neq m_1$；收到 $c$ 后，若 $c=m_0$ 输出 ${1}$，若 $c=m_1$ 输出 ${0}$，否则均匀猜。由于 $b=0$ 时 $c\neq m_0$ 恒成立、$b=1$ 时 $c\neq m_1$ 恒成立，可算得

$$\Pr\big[\mathsf{PrivK}^{\mathsf{eav}}_{\mathcal{A},\Pi}=1\big]=\frac{2^{\ell}}{2(2^{\ell}-1)}=\frac12+\frac{1}{2(2^{\ell}-1)}>\frac12.$$

---

## 习题 2.12　固定周期 2 的维吉尼亚：区分 $\mathtt{aaa}$ 与 $\mathtt{aab}$

> **题目**　Let $\Pi$ denote the Vigenère cipher with message space of all 3-character strings and period $t = 2$. $\mathcal{A}$ outputs $m_0 = \mathtt{aaa}$, $m_1 = \mathtt{aab}$, and on ciphertext $c$ outputs 0 iff the first and third characters of $c$ are equal. Compute $\Pr[\mathsf{PrivK}^{\mathsf{eav}}_{\mathcal{A},\Pi}=1]$.
> **题目**　设 $\Pi$ 是消息空间为全部 3 字符串、周期 $t = 2$ 的维吉尼亚密码。$\mathcal{A}$ 输出 $m_0 = \mathtt{aaa}$、$m_1 = \mathtt{aab}$，并在收到密文 $c$ 后当且仅当 $c$ 的第 1 个与第 3 个字符相等时输出 0。计算 $\Pr[\mathsf{PrivK}^{\mathsf{eav}}_{\mathcal{A},\Pi}=1]$。

周期 $t=2$，密钥 $(k_1,k_2)$ 在 ${26}^2$ 个取值上均匀；加密为 $c=(m_1+k_1,\ m_2+k_2,\ m_3+k_1)$——**第 1、3 位共用 $k_1$**。

- $b=0$（加密 $\mathtt{aaa}$）：$c=(k_1,\,k_2,\,k_1)$，$c_1=c_3$ 恒成立，$\mathcal{A}$ 必输出 ${0}$；
- $b=1$（加密 $\mathtt{aab}$）：$c=(k_1,\,k_2,\,1+k_1)$，$c_1=c_3\iff k_1\equiv 1+k_1\pmod{26}$，不可能，$\mathcal{A}$ 必输出 ${1}$。

$$\Pr\big[\mathsf{PrivK}^{\mathsf{eav}}_{\mathcal{A},\Pi}=1\big]=\frac12\cdot 1+\frac12\cdot 1=\boxed{1}.$$

（数值穷举全部 ${26}^2$ 个密钥验证，见 `solve_ex2_12_2_13.py`。）

---

## 习题 2.13　随机周期 $t\in\{1,2,3\}$ 的维吉尼亚

> **题目**　Let $\Pi$ denote the Vigenère cipher with message space of all 3-character strings, where the period $t$ is chosen uniformly from $\{1,2,3\}$ and the key is then a uniform string of length $t$.
>
> **(a)**　Define $\mathcal{A}$ as follows: $\mathcal{A}$ outputs $m_0 = \mathtt{aab}$ and $m_1 = \mathtt{abb}$. When given a ciphertext $c$, it outputs ${0}$ if the first character of $c$ is the same as the second character of $c$, and outputs ${1}$ otherwise. Compute $\Pr\big[\mathsf{PrivK}^{\mathsf{eav}}_{\mathcal{A},\Pi}=1\big]$.
>
> **(b)**　Construct and analyze an adversary $\mathcal{A}^{\prime}$ for which $\Pr\big[\mathsf{PrivK}^{\mathsf{eav}}_{\mathcal{A}^{\prime},\Pi}=1\big]$ is greater than your answer from part (a).
>
> **题目**　设 $\Pi$ 是消息空间为全部 3 字符串的维吉尼亚密码，其中周期 $t$ 从 $\{1,2,3\}$ 中均匀选取，密钥为长度 $t$ 的均匀随机串。
>
> **(a)**　定义敌手 $\mathcal{A}$ 如下：$\mathcal{A}$ 输出 $m_0 = \mathtt{aab}$、$m_1 = \mathtt{abb}$；收到密文 $c$ 后，若 $c$ 的第 1 个字符与第 2 个字符相同则输出 ${0}$，否则输出 ${1}$。计算 $\Pr\big[\mathsf{PrivK}^{\mathsf{eav}}_{\mathcal{A},\Pi}=1\big]$。
>
> **(b)**　构造并分析一个敌手 $\mathcal{A}^{\prime}$，使 $\Pr\big[\mathsf{PrivK}^{\mathsf{eav}}_{\mathcal{A}^{\prime},\Pi}=1\big]$ 大于你在 (a) 中得到的答案。

### (a) 计算给定敌手的成功概率

$\mathcal{A}$ 输出 $m_0=\mathtt{aab}$、$m_1=\mathtt{abb}$；收到 $c$ 后，若 $c_1=c_2$ 输出 ${0}$，否则输出 ${1}$。按周期分类：

**$b=0$（$\mathtt{aab}$，即 $(0,0,1)$）：**

| 周期 | 密文 | $c_1=c_2$ 的概率 |
|---|---|---|
| $t=1$ | $(k,\,k,\,1+k)$ | ${1}$（恒成立） |
| $t=2$ | $(k_1,\,k_2,\,1+k_1)$ | $k_1=k_2$：${1}/26$ |
| $t=3$ | $(k_1,\,k_2,\,1+k_3)$ | $k_1=k_2$：${1}/26$ |

$$\Pr[\mathcal{A}\text{ 输出 }0\mid b=0]=\frac13\Big(1+\frac{1}{26}+\frac{1}{26}\Big)=\frac{14}{39}.$$

**$b=1$（$\mathtt{abb}$，即 $(0,1,1)$）：**

| 周期 | 密文 | $c_1=c_2$ 的概率 |
|---|---|---|
| $t=1$ | $(k,\,1+k,\,1+k)$ | ${0}$（$k\neq1+k$） |
| $t=2$ | $(k_1,\,1+k_2,\,1+k_1)$ | $k_1=1+k_2$：${1}/26$ |
| $t=3$ | $(k_1,\,1+k_2,\,1+k_3)$ | $k_1=1+k_2$：${1}/26$ |

$$\Pr[\mathcal{A}\text{ 输出 }1\mid b=1]=1-\frac13\Big(0+\frac{1}{26}+\frac{1}{26}\Big)=1-\frac{1}{39}=\frac{38}{39}.$$

合并：

$$\Pr\big[\mathsf{PrivK}^{\mathsf{eav}}_{\mathcal{A},\Pi}=1\big]=\frac12\cdot\frac{14}{39}+\frac12\cdot\frac{38}{39}=\frac12\cdot\frac{52}{39}=\boxed{\frac23}\approx0.667.$$

### (b) 构造更强的敌手 $\mathcal{A}^{\prime}$

$\mathcal{A}^{\prime}$：输出 $m_0=\mathtt{aaa}$、$m_1=\mathtt{abc}$；收到 $c$ 后，若 $c_1=c_3$ 输出 ${0}$，否则输出 ${1}$。

**$b=0$（$\mathtt{aaa}$）**：$t=1$ 时 $c=(k,k,k)$、$t=2$ 时 $c=(k_1,k_2,k_1)$，均使 $c_1=c_3$ **必然**成立；$t=3$ 时 $c=(k_1,k_2,k_3)$ 独立均匀，$c_1=c_3$ 以概率 ${1}/26$：

$$\Pr[\mathcal{A}^{\prime}\text{ 输出 }0\mid b=0]=\frac13+\frac13+\frac{1}{78}=\frac{53}{78}.$$

**$b=1$（$\mathtt{abc}$，即 $(0,1,2)$）**：$t=1$ 时 $c=(k,1+k,2+k)$、$t=2$ 时 $c=(k_1,1+k_2,2+k_1)$，均有 $c_3-c_1\equiv2\pmod{26}$，$c_1\neq c_3$ **必然**成立；$t=3$ 时 $c_1=c_3\iff k_1=2+k_3$，概率 ${1}/26$：

$$\Pr[\mathcal{A}^{\prime}\text{ 输出 }1\mid b=1]=1-\frac{1}{3}\cdot\frac{1}{26}=\frac{77}{78}.$$

合并：

$$\Pr\big[\mathsf{PrivK}^{\mathsf{eav}}_{\mathcal{A}^{\prime},\Pi}=1\big]=\frac12\cdot\frac{53}{78}+\frac12\cdot\frac{77}{78}=\frac{65}{78}=\boxed{\frac56}\approx0.833\ >\ \frac23.$$

改进原因：$\mathtt{aaa}$ 在 $t=1$ 与 $t=2$ 两个周期下都必然留下 $c_1=c_3$ 的结构（两个周期都被"利用"），而 $\mathtt{abc}$ 在任何周期下都几乎不可能出现 $c_1=c_3$，两条消息的特征事件概率差被拉到最大。（各概率已穷举全部周期与密钥精确验证，见 `solve_ex2_12_2_13.py`。）

---

## 习题 2.14　移位/替换/维吉尼亚何时完全保密

> **题目**　In this exercise, we look at different conditions under which the shift, mono-alphabetic substitution, and Vigenère ciphers are perfectly secret:
>
> **(a)**　Prove that if only a single character is encrypted, then the shift cipher is perfectly secret.
>
> **(b)**　What is the largest message space $\mathcal{M}$ for which the mono-alphabetic substitution cipher provides perfect secrecy?
>
> **(c)**　Prove that the Vigenère cipher using (fixed) period $t$ is perfectly secret when used to encrypt messages of length $t$.
>
> Reconcile this with the attacks shown in the previous chapter.
>
> **题目**　本题考察移位密码、单表替换密码与维吉尼亚密码完全保密的各种条件：
>
> **(a)**　证明：若只加密单个字符，则移位密码是完全保密的。
>
> **(b)**　单表替换密码能提供完全保密的最大消息空间 $\mathcal{M}$ 是什么？
>
> **(c)**　证明：用（固定）周期 $t$ 的维吉尼亚密码加密长度恰为 $t$ 的消息时，它是完全保密的。
>
> 说明上述结论与上一章给出的攻击如何相容。

### (a) 只加密单个字符时，移位密码完全保密

$\mathcal{M}=\mathbb{Z}_{26}$（单字符），$k\leftarrow\mathbb{Z}_{26}$ 均匀，$\mathsf{Enc}_k(m)=[m+k\bmod 26]$。对任意 $m,c$：

$$\Pr[\mathsf{Enc}_K(m)=c]=\Pr[K=c-m\bmod 26]=\frac{1}{26},$$

由引理 2.5 完全保密。这正是字母表 $\mathbb{Z}_{26}$ 上的一次性密码本。

### (b) 单表替换密码完全保密的最大消息空间

密钥空间为全部置换，$|\mathcal{K}|=26!$。由定理 2.11，任何完全保密方案必须 $|\mathcal{M}|\le|\mathcal{K}|=26!$。这个界**可以达到**：取

$$\mathcal{M}=\{\text{26 个字母各恰好出现一次的长 26 字符串}\}\quad(\text{即全字母表的所有排列}),\qquad |\mathcal{M}|=26!.$$

对任意 $m\in\mathcal{M}$ 与任意长 26 的 $c$：

- 若 $c$ 也无重复字母，则把 $m$ 逐位映到 $c$ 的置换 $\pi$ 被 26 个位置**完全确定且唯一**（$m$ 中字母互异保证 $\pi$ 良定，$c$ 中字母互异保证 $\pi$ 是置换），故 $\Pr[\mathsf{Enc}_K(m)=c]=1/26!$；
- 若 $c$ 有重复字母，则 $\Pr[\mathsf{Enc}_K(m)=c]=0$（$\pi$ 是单射）。

两种取值都与 $m$ 无关，由引理 2.5 完全保密。故最大消息空间的大小为 ${26}!$。

（常用的特例：所有**单字符**消息构成的空间，$|\mathcal{M}|=26$——此时对每个 $m,c$ 恰有 ${25}!$ 个置换映 $m\mapsto c$，概率 ${25}!/26!=1/26$，同样完全保密。）

### (c) 固定周期 $t$、消息长度恰为 $t$ 的维吉尼亚完全保密

密钥 $k\leftarrow\mathbb{Z}_{26}^{\,t}$ 均匀，$\mathsf{Enc}_k(m)=m+k$（逐位模 26）。对任意 $m,c\in\mathbb{Z}_{26}^{\,t}$：

$$\Pr[\mathsf{Enc}_K(m)=c]=\Pr[K=c-m]=26^{-t},$$

由引理 2.5 完全保密——这就是群 $\mathbb{Z}_{26}^{\,t}$ 上的一次性密码本。

**与第 1 章攻击的调和**：完全保密的前提是**一个密钥只加密一段长度不超过 $t$ 的消息**，密钥与消息等长且不复用。第 1 章的攻击之所以成立，是因为用长 $t$ 的密钥去加密**远长于 $t$** 的消息：同一密钥字母被重复用于许多位置，频率结构得以保留（Kasiski 检验、重合指数、逐流频率分析才有素材）；定理 2.11 也说明 ${26}^t$ 个密钥不可能对 ${26}^{t+1}$ 量级明文的空间完全保密。两种陈述的适用前提不同，并不矛盾。

---

## 习题 2.15　$|\mathcal{K}|<|\mathcal{M}|$ 时直接构造区分敌手

> **题目**　Give a direct proof that a scheme satisfying Definition 2.6 must have $|\mathcal{K}| \ge |\mathcal{M}|$: let $\Pi$ be any encryption scheme with $|\mathcal{K}| < |\mathcal{M}|$, and show an $\mathcal{A}$ for which $\Pr[\mathsf{PrivK}^{\mathsf{eav}}_{\mathcal{A},\Pi}=1] > \frac12$.
>
> Hint: It may be easier to let $\mathcal{A}$ be randomized.
>
> **题目**　直接证明满足定义 2.6 的方案必有 $|\mathcal{K}| \ge |\mathcal{M}|$：设 $\Pi$ 是满足 $|\mathcal{K}| < |\mathcal{M}|$ 的任意加密方案，构造一个 $\mathcal{A}$ 使 $\Pr[\mathsf{PrivK}^{\mathsf{eav}}_{\mathcal{A},\Pi}=1] > \frac12$。
>
> 提示：让 $\mathcal{A}$ 随机化可能更容易。

设 $|\mathcal{K}|<|\mathcal{M}|$。构造随机化敌手 $\mathcal{A}$：

1. 均匀选 $m_0\leftarrow\mathcal{M}$，再均匀选 $m_1\leftarrow\mathcal{M}\setminus\{m_0\}$，输出 $(m_0,m_1)$；
2. 收到挑战密文 $c$ 后，计算 $\mathcal{M}(c)=\{\mathsf{Dec}_k(c):k\in\mathcal{K}\}$（Dec 确定，故 $|\mathcal{M}(c)|\le|\mathcal{K}|$）。若 $m_0\in\mathcal{M}(c)$ 而 $m_1\notin\mathcal{M}(c)$ 输出 ${0}$；若 $m_1\in\mathcal{M}(c)$ 而 $m_0\notin\mathcal{M}(c)$ 输出 ${1}$；否则均匀猜。

**分析。** 当 $b=0$ 时 $c$ 是 $m_0$ 的合法加密，故 $m_0\in\mathcal{M}(c)$ 恒成立：若 $m_1\notin\mathcal{M}(c)$，$c$ 不可能是 $m_1$ 的加密，$\mathcal{A}$ 必胜；若 $m_1\in\mathcal{M}(c)$，$\mathcal{A}$ 以 ${1}/{2}$ 获胜：

$$\Pr[\text{赢}\mid b=0]=1-\frac12\,\Pr[m_1\in\mathcal{M}(c)\mid b=0].$$

给定 $b=0$ 时，$\mathcal{M}(c)$ 大小至多为 $|\mathcal{K}|$ 且含 $m_0$，而 $m_1$ 在 $\mathcal{M}\setminus\{m_0\}$（$|\mathcal{M}|-1$ 个候选）上均匀，故

$$\Pr[m_1\in\mathcal{M}(c)\mid b=0]\ \le\ \frac{|\mathcal{K}|-1}{|\mathcal{M}|-1}.$$

对 $b=1$ 同理有 $\Pr[m_0\in\mathcal{M}(c)\mid b=1]\le(|\mathcal{K}|-1)/(|\mathcal{M}|-1)$。合并：

$$\Pr\big[\mathsf{PrivK}^{\mathsf{eav}}_{\mathcal{A},\Pi}=1\big]\ \ge\ 1-\frac12\cdot\frac{|\mathcal{K}|-1}{|\mathcal{M}|-1}\ >\ 1-\frac12=\frac12,$$

最后一步严格不等号成立是因为 $|\mathcal{K}|<|\mathcal{M}|\Rightarrow|\mathcal{K}|-1<|\mathcal{M}|-1$。$\blacksquare$

（直观：密钥太少，一个密文最多"解释" $|\mathcal{K}|$ 条明文；随机挑的两条明文以正概率落在可解释集之外，从而被直接排除。这正是定理 2.11 的"敌手版"证明。）

---

## 习题 2.16　同一 8 位密钥重复用于单字符 ASCII 的一次性密码本

> **题目**　The following questions concern multiple encryptions of single-character ASCII plaintexts with the one-time pad using the same 8-bit key. You may assume that the plaintexts are either (upper- or lower-case) English letters or the space character.
>
> **(a)**　Say you see the ciphertexts $\mathtt{1011\,0111}$ and $\mathtt{1110\,0111}$. What can you deduce about the plaintext characters these correspond to?
>
> **(b)**　Say you see the three ciphertexts $\mathtt{0110\,0110}$, $\mathtt{0011\,0010}$, and $\mathtt{0010\,0011}$. What can you deduce about the plaintext characters these correspond to?
>
> Hint: Focus on the second bit of the ciphertexts.
>
> **题目**　以下问题涉及用同一个 8 位密钥的一次性密码本对多个单字符 ASCII 明文的加密。可假设明文是大写或小写英文字母，或空格字符。
>
> **(a)**　若你看到密文 $\mathtt{1011\,0111}$ 和 $\mathtt{1110\,0111}$，关于它们对应的明文字符，你能推断出什么？
>
> **(b)**　若你看到三条密文 $\mathtt{0110\,0110}$、$\mathtt{0011\,0010}$、$\mathtt{0010\,0011}$，关于它们对应的明文字符，你能推断出什么？
>
> 提示：关注密文的第 2 位。

**关键事实**（ASCII 的第 2 高位）：空格为 $\mathtt{0x20}=\texttt{0010 0000}$（第 2 位为 ${0}$）；大写字母 $\mathtt{0x41}$–$\mathtt{0x5A}$ 与小写字母 $\mathtt{0x61}$–$\mathtt{0x7A}$ 均为 $\texttt{01xx xxxx}$（第 2 位为 ${1}$）。同一密钥下 $c_i\oplus c_j=m_i\oplus m_j$，故**异或的第 2 位为 ${1}$ ⟺ 两个明文字符恰好一个是空格**。

### (a) 密文 $\texttt{1011 0111}$ 与 $\texttt{1110 0111}$

$$c_1\oplus c_2=\texttt{0101 0000}=\mathtt{0x50},\quad\text{第 2 位为 }1\ \Rightarrow\ \text{恰有一个空格}.$$

若 $m_1=$ 空格，则 $m_2=\mathtt{0x20}\oplus\mathtt{0x50}=\mathtt{0x70}=\mathtt{p}$（小写，合法）；对称地 $m_2=$ 空格、$m_1=\mathtt{p}$ 也合法。其余组合均落在允许字符集之外（字母 $\oplus\ \mathtt{0x50}$ 得到控制符或数字/符号区，除非先减去空格）。

**结论**：两个明文字符是**空格和 $\mathtt{p}$**，但无法确定谁对应哪条密文。

### (b) 密文 $\texttt{0110 0110}$、$\texttt{0011 0010}$、$\texttt{0010 0011}$

$$c_1\oplus c_2=\mathtt{0x54},\qquad c_1\oplus c_3=\mathtt{0x45},\qquad c_2\oplus c_3=\mathtt{0x11}.$$

看第 2 位：$c_1\oplus c_2$、$c_1\oplus c_3$ 的第 2 位为 ${1}$，$c_2\oplus c_3$ 的第 2 位为 ${0}$。故 $m_1$ 与 $m_2,m_3$ "类型"相反，而 $m_2,m_3$ 同类型。$m_2,m_3$ 不可能都是空格（否则二者相等，与 $c_2\neq c_3$ 矛盾），所以**都是字母，$m_1$ 是空格**。于是

$$m_2=\mathtt{0x20}\oplus\mathtt{0x54}=\mathtt{0x74}=\mathtt{t},\qquad m_3=\mathtt{0x20}\oplus\mathtt{0x45}=\mathtt{0x65}=\mathtt{e},$$

且自洽性检查通过：$\mathtt{t}\oplus\mathtt{e}=\mathtt{0x74}\oplus\mathtt{0x65}=\mathtt{0x11}=c_2\oplus c_3$ ✓。

**结论**：三条明文依次是**空格、$\mathtt{t}$、$\mathtt{e}$**（暴力枚举全部合法明文组合可验证这是唯一解，见 `solve_ex2_16.py`）。这正是 VENONA 式"密钥复用"攻击的缩影：异或消去密钥后，明文统计结构暴露无遗。

---

## 习题 2.17　放松正确性后的短密钥完全保密

> **题目**　Assume we only require $\Pr[\mathsf{Dec}_K(\mathsf{Enc}_K(m)) = m] \ge 2^{-t}$ for all $m$. Show that perfect secrecy can be achieved with $|\mathcal{K}| < |\mathcal{M}|$ when $t \ge 1$, and prove a lower bound on $|\mathcal{K}|$ in terms of $t$.
> **题目**　假设我们只要求对所有 $m$ 成立 $\Pr[\mathsf{Dec}_K(\mathsf{Enc}_K(m)) = m] \ge 2^{-t}$。证明当 $t \ge 1$ 时可以在 $|\mathcal{K}| < |\mathcal{M}|$ 的条件下实现完全保密，并用 $t$ 证明 $|\mathcal{K}|$ 的一个下界。

### 构造（达到 $|\mathcal{K}|=2^{-t}|\mathcal{M}|$）

取 $\mathcal{M}=\{0,1\}^{\ell}$（$\ell\ge t$），$\mathcal{K}=\{0,1\}^{\ell-t}$（Gen 均匀）：

- **Enc**：$\mathsf{Enc}_k(m)$ 均匀选 $r\leftarrow\{0,1\}^{t}$，输出 $c=m\oplus(k\|r)$；
- **Dec**：$\mathsf{Dec}_k(c)=c\oplus(k\|0^{t})$。

- **完全保密**：$k\|r$ 在 $\{0,1\}^{\ell}$ 上均匀，故对任意 $m,c$，$\Pr[\mathsf{Enc}_K(m)=c]=2^{-\ell}$，由引理 2.5 完全保密（密文分布与明文无关）。
- **放松正确性**：$\mathsf{Dec}_k(\mathsf{Enc}_k(m))=m\oplus(0^{\ell-t}\|r)=m\iff r=0^{t}$，概率恰为 ${2}^{-t}$ ✓。
- **短密钥**：$|\mathcal{K}|=2^{\ell-t}=2^{-t}|\mathcal{M}|<|\mathcal{M}|$（$t\ge1$）✓。

### 下界：$|\mathcal{K}|\ge 2^{-t}|\mathcal{M}|$

由习题 2.1，不妨设 Gen 在 $\mathcal{K}$ 上均匀。记

$$q(k,m)\stackrel{\mathrm{def}}{=}\Pr[\mathsf{Dec}_k(\mathsf{Enc}_k(m))=m]\in[0,1]$$

（对 Enc/Dec 的随机性取概率）。放松正确性给出：对所有 $m$，$\frac{1}{|\mathcal{K}|}\sum_k q(k,m)\ge 2^{-t}$，对 $m$ 求和得

$$
\sum_{m}\sum_{k}q(k,m)\ \ge\ |\mathcal{M}|\,|\mathcal{K}|\,2^{-t}.\tag{*}
$$

另一方面，固定 $k$，按 $\mathsf{Dec}_k(c)$ 的取值归并：

$$\sum_{m}q(k,m)=\sum_{c}\sum_{m}\Pr[\mathsf{Enc}_k(m)=c]\cdot\Pr[\mathsf{Dec}_k(c)=m]=\sum_{c}\Pr\big[\mathsf{Enc}_k\big(\mathsf{Dec}_k(c)\big)=c\big]\ \le\ \sum_{c}\max_{m}\Pr[\mathsf{Enc}_k(m)=c].$$

由完全保密（式 (2.1)），$p_c\stackrel{\mathrm{def}}{=}\Pr[\mathsf{Enc}_K(m)=c]$ 与 $m$ 无关；而密钥均匀给出

$$p_c=\frac{1}{|\mathcal{K}|}\sum_{k^{\prime}}\Pr[\mathsf{Enc}_{k^{\prime}}(m)=c]\ \ge\ \frac{1}{|\mathcal{K}|}\Pr[\mathsf{Enc}_k(m)=c],$$

即 $\max_m\Pr[\mathsf{Enc}_k(m)=c]\le|\mathcal{K}|\,p_c$。于是 $\sum_m q(k,m)\le|\mathcal{K}|\sum_c p_c=|\mathcal{K}|$（$\{p_c\}$ 是密文分布，和为 1），对 $k$ 求和得

$$
\sum_{m}\sum_{k}q(k,m)\ \le\ |\mathcal{K}|^{2}.\tag{**}
$$

联立 $(*)$ 与 $(**)$：$|\mathcal{K}|^{2}\ge|\mathcal{M}|\,|\mathcal{K}|\,2^{-t}$，即

$$|\mathcal{K}|\ \ge\ 2^{-t}\,|\mathcal{M}|.$$

上述构造取到等号，故该下界是紧的。$t=0$ 时退化为定理 2.11（$|\mathcal{K}|\ge|\mathcal{M}|$）；每牺牲一半正确性，密钥空间即可减半。$\blacksquare$

---

## 习题 2.18　$\varepsilon$-完全保密

> **题目**　Let $\varepsilon > 0$ be a constant. Say an encryption scheme is $\varepsilon$-perfectly secret if for every adversary $\mathcal{A}$ it holds that $\Pr\big[\mathsf{PrivK}^{\mathsf{eav}}_{\mathcal{A},\Pi}=1\big] \le \frac{1}{2} + \varepsilon$. (Compare to Definition 2.6.) Consider a variant of the one-time pad where $\mathcal{M} = \{0,1\}^{\ell}$ and the key is chosen uniformly from an arbitrary set $\mathcal{K} \subseteq \{0,1\}^{\ell}$ with $|\mathcal{K}| = (1 - \varepsilon) \cdot 2^{\ell}$; encryption and decryption are otherwise the same.
>
> **(a)**　Prove that this scheme is $\varepsilon$-perfectly secret.
>
> **(b)**　Prove that this scheme is $\big(\frac{\varepsilon}{2(1-\varepsilon)}\big)$-perfectly secret when $\varepsilon \le 1/2$. (Note that $\frac{\varepsilon}{2(1-\varepsilon)} \le \varepsilon$ here, so this is an improvement over part (a).)
>
> **(c)**　Prove that any deterministic scheme that is $\varepsilon$-perfectly secret must have $|\mathcal{K}| \ge (1 - 2\varepsilon) \cdot |\mathcal{M}|$. (Note: It is an open question to prove a tight lower bound that also holds for randomized schemes.)
>
> **题目**　设 $\varepsilon > 0$ 为常数。称一个加密方案是 $\varepsilon$-完全保密的，若对任意敌手 $\mathcal{A}$ 都有 $\Pr\big[\mathsf{PrivK}^{\mathsf{eav}}_{\mathcal{A},\Pi}=1\big] \le \frac{1}{2} + \varepsilon$。（对比定义 2.6。）考虑一次性密码本的如下变体：$\mathcal{M} = \{0,1\}^{\ell}$，密钥从满足 $|\mathcal{K}| = (1 - \varepsilon) \cdot 2^{\ell}$ 的任意集合 $\mathcal{K} \subseteq \{0,1\}^{\ell}$ 中均匀选取；加密与解密算法与原来相同。
>
> **(a)**　证明该方案是 $\varepsilon$-完全保密的。
>
> **(b)**　证明当 $\varepsilon \le 1/2$ 时，该方案是 $\big(\frac{\varepsilon}{2(1-\varepsilon)}\big)$-完全保密的。（注意此时 $\frac{\varepsilon}{2(1-\varepsilon)} \le \varepsilon$，故这是对 (a) 的改进。）
>
> **(c)**　证明：任何 $\varepsilon$-完全保密的确定性方案都必须满足 $|\mathcal{K}| \ge (1 - 2\varepsilon) \cdot |\mathcal{M}|$。（注：对随机化方案同样成立的紧下界仍是一个公开问题。）

**预备**：与习题 2.5 同理可设 $\mathcal{A}$ 确定。设 $\mathcal{A}$ 输出 $(m_0,m_1)$，记 $Z=\mathcal{A}^{-1}(0)$、$O=\mathcal{A}^{-1}(1)$。由于 $k$ 在 $\mathcal{K}$ 上均匀，$b$ 给定时密文 $c=m_b\oplus k$ 在

$$S_b\ \stackrel{\mathrm{def}}{=}\ m_b\oplus\mathcal{K}=\{m_b\oplus k:k\in\mathcal{K}\},\qquad |S_b|=|\mathcal{K}|=(1-\varepsilon)\,2^{\ell}$$

上均匀分布，故

$$
\Pr[\text{赢}]=\frac{1}{2|\mathcal{K}|}\Big(\sum_{c\in S_0}\mathbf{1}[c\in Z]+\sum_{c\in S_1}\mathbf{1}[c\in O]\Big)=\frac{|Z\cap S_0|+|O\cap S_1|}{2|\mathcal{K}|}.\tag{†}
$$

另外注意（当 $\varepsilon\le 1/2$ 时 $|S_0|=|S_1|=(1-\varepsilon)2^{\ell}\ge 2^{\ell-1}$，而 $|S_0\cup S_1|\le 2^{\ell}$）：

$$|S_0\cap S_1|=|S_0|+|S_1|-|S_0\cup S_1|\ \ge\ 2(1-\varepsilon)2^{\ell}-2^{\ell}=(1-2\varepsilon)\,2^{\ell},$$
$$
|S_0\setminus S_1|=|S_0|-|S_0\cap S_1|\ \le\ (1-\varepsilon)2^{\ell}-(1-2\varepsilon)2^{\ell}=\varepsilon\,2^{\ell},\quad\text{同理 }|S_1\setminus S_0|\le\varepsilon\,2^{\ell}.\tag{‡}
$$

### (a) 该方案是 $\varepsilon$-完全保密的

若 $\varepsilon\ge 1/2$，则 $\frac12+\varepsilon\ge1$，平凡成立。下设 $\varepsilon<1/2$。把 $(†)$ 的分子改写并放缩：

$$|Z\cap S_0|+|O\cap S_1|=|S_1|+|Z\cap S_0|-|Z\cap S_1|\ \le\ |\mathcal{K}|+|S_0\setminus S_1|\ \le\ (1-\varepsilon)2^{\ell}+\varepsilon\,2^{\ell}=2^{\ell},$$

其中用了 $O\cap S_1=S_1\setminus(Z\cap S_1)$ 与 $(‡)$。代回 $(†)$：

$$\Pr[\text{赢}]\ \le\ \frac{2^{\ell}}{2(1-\varepsilon)2^{\ell}}=\frac{1}{2(1-\varepsilon)}\ \le\ \frac12+\varepsilon,$$

末一步等价于 ${1}\le(1+2\varepsilon)(1-\varepsilon)=1+\varepsilon-2\varepsilon^{2}$，即 $\varepsilon(1-2\varepsilon)\ge0$，在 ${0}<\varepsilon\le1/2$ 时成立。$\blacksquare$

### (b) 加强为 $\frac{\varepsilon}{2(1-\varepsilon)}$-完全保密（$\varepsilon\le1/2$）

最优敌手的成功概率由两个密文分布的统计距离精确刻画：$\max_{\mathcal{A}}\Pr[\text{赢}]=\frac12+\frac12\,\Delta(P_0,P_1)$，其中 $P_b$ 是 $S_b$ 上的均匀分布。直接计算：

$$\Delta(P_0,P_1)=\frac12\sum_{c}\Big|\frac{\mathbf{1}[c\in S_0]}{|\mathcal{K}|}-\frac{\mathbf{1}[c\in S_1]}{|\mathcal{K}|}\Big|=\frac{|S_0\mathbin{\triangle}S_1|}{2|\mathcal{K}|}\ \le\ \frac{2\cdot\varepsilon\,2^{\ell}}{2(1-\varepsilon)2^{\ell}}=\frac{\varepsilon}{1-\varepsilon},$$

（对称差的两半各不超过 $\varepsilon 2^{\ell}$，见 $(‡)$。）故对任意 $\mathcal{A}$：

$$\Pr\big[\mathsf{PrivK}^{\mathsf{eav}}_{\mathcal{A},\Pi}=1\big]\ \le\ \frac12+\frac{\varepsilon}{2(1-\varepsilon)},$$

即方案是 $\frac{\varepsilon}{2(1-\varepsilon)}$-完全保密的；$\varepsilon\le1/2$ 时 $\frac{\varepsilon}{2(1-\varepsilon)}\le\varepsilon$，确实优于 (a)。$\blacksquare$

### (c) 确定方案的下界 $|\mathcal{K}|\ge(1-2\varepsilon)|\mathcal{M}|$

设确定方案 $\Pi$（Enc、Dec 确定；由习题 2.1 设 Gen 均匀）是 $\varepsilon$-完全保密的。沿用习题 2.15 的敌手 $\mathcal{A}$（随机选 $m_0\leftarrow\mathcal{M}$、$m_1\leftarrow\mathcal{M}\setminus\{m_0\}$；恰好一个在 $\mathcal{M}(c)=\{\mathsf{Dec}_k(c):k\in\mathcal{K}\}$ 中时输出对应下标，否则均匀猜）。同样的分析给出

$$\Pr[\text{赢}]\ \ge\ 1-\frac12\cdot\frac{|\mathcal{K}|-1}{|\mathcal{M}|-1}.$$

若 $|\mathcal{K}|<(1-2\varepsilon)|\mathcal{M}|$，则 $\frac{|\mathcal{K}|-1}{|\mathcal{M}|-1}<1-2\varepsilon$（交叉相乘即见），于是

$$\Pr[\text{赢}]\ >\ 1-\frac{1-2\varepsilon}{2}=\frac12+\varepsilon,$$

与 $\varepsilon$-完全保密矛盾。故 $|\mathcal{K}|\ge(1-2\varepsilon)|\mathcal{M}|$。$\blacksquare$（直观：$\varepsilon$ 越小越接近完全保密，密钥空间就越不能低于定理 2.11 的 $|\mathcal{M}|$；$\varepsilon=0$ 时恰回到定理 2.11。）

---

## 习题 2.19　同一密钥加密两条消息的"完全保密"

> **题目**　In this problem we consider definitions of perfect secrecy for the encryption of two messages (using the same key). Here we consider distributions on pairs of messages from the message space $\mathcal{M}$; we let $M_1, M_2$ be random variables denoting the first and second message, respectively. (These random variables are not assumed to be independent.) We generate a (single) key $k$, sample a pair of messages $(m_1, m_2)$ according to the given distribution, and then compute ciphertexts $c_1 \leftarrow \mathsf{Enc}_k(m_1)$ and $c_2 \leftarrow \mathsf{Enc}_k(m_2)$; this induces a distribution on pairs of ciphertexts and we let $C_1, C_2$ be the corresponding random variables.
>
> **(a)**　Say encryption scheme (Gen, Enc, Dec) is *perfectly secret for two messages* if for all distributions on $\mathcal{M} \times \mathcal{M}$, all $m_1, m_2 \in \mathcal{M}$, and all ciphertexts $c_1, c_2 \in \mathcal{C}$ with $\Pr[C_1 = c_1 \wedge C_2 = c_2] > 0$:
> $$\Pr[M_1 = m_1 \wedge M_2 = m_2 \mid C_1 = c_1 \wedge C_2 = c_2] = \Pr[M_1 = m_1 \wedge M_2 = m_2].$$
> Prove that no encryption scheme can satisfy this definition.
>
> Hint: Take $c_1 = c_2$.
>
> **(b)**　Say encryption scheme (Gen, Enc, Dec) is *perfectly secret for two distinct messages* if for all distributions on $\mathcal{M} \times \mathcal{M}$ where the first and second messages are guaranteed to be different (i.e., distributions on pairs of distinct messages), all $m_1, m_2 \in \mathcal{M}$, and all $c_1, c_2 \in \mathcal{C}$ with $\Pr[C_1 = c_1 \wedge C_2 = c_2] > 0$:
> $$\Pr[M_1 = m_1 \wedge M_2 = m_2 \mid C_1 = c_1 \wedge C_2 = c_2] = \Pr[M_1 = m_1 \wedge M_2 = m_2].$$
> Show an encryption scheme that provably satisfies this definition.
>
> Hint: The encryption scheme you propose need not be efficient, although an efficient solution is possible.
>
> **题目**　本题考虑用同一密钥加密两条消息时完全保密的几种定义。我们考虑消息空间 $\mathcal{M}$ 上的消息对分布，用随机变量 $M_1, M_2$ 分别表示第一、第二条消息（不假设这两个随机变量相互独立）。生成一个（单个）密钥 $k$，按给定分布采样消息对 $(m_1, m_2)$，再计算密文 $c_1 \leftarrow \mathsf{Enc}_k(m_1)$ 与 $c_2 \leftarrow \mathsf{Enc}_k(m_2)$；这诱导出密文对上的分布，记相应的随机变量为 $C_1, C_2$。
>
> **(a)**　称加密方案 (Gen, Enc, Dec) **对两条消息完全保密**，若对 $\mathcal{M} \times \mathcal{M}$ 上的所有分布、所有 $m_1, m_2 \in \mathcal{M}$ 以及所有满足 $\Pr[C_1 = c_1 \wedge C_2 = c_2] > 0$ 的密文 $c_1, c_2 \in \mathcal{C}$，都有 $\Pr[M_1 = m_1 \wedge M_2 = m_2 \mid C_1 = c_1 \wedge C_2 = c_2] = \Pr[M_1 = m_1 \wedge M_2 = m_2]$。证明：不存在满足该定义的加密方案。
>
> 提示：取 $c_1 = c_2$。
>
> **(b)**　称加密方案 (Gen, Enc, Dec) **对两条不同消息完全保密**，若对 $\mathcal{M} \times \mathcal{M}$ 上所有保证第一条与第二条消息不同的分布（即不同消息对上的分布）、所有 $m_1, m_2 \in \mathcal{M}$ 以及所有满足 $\Pr[C_1 = c_1 \wedge C_2 = c_2] > 0$ 的 $c_1, c_2 \in \mathcal{C}$，都有 $\Pr[M_1 = m_1 \wedge M_2 = m_2 \mid C_1 = c_1 \wedge C_2 = c_2] = \Pr[M_1 = m_1 \wedge M_2 = m_2]$。给出一个可证明满足该定义的加密方案。
>
> 提示：所提出的加密方案不必是高效的，尽管存在高效的解法。

### (a) 不存在满足该定义的方案

**思路**：要推翻一个"对所有分布、所有密文对成立"的全称定义，只需任取方案并构造**一个**反例。支点只有一条：**同一密钥下密文相等 ⟹ 明文相等**（正确性保证一个密文在同一密钥下只解出一个明文），即密文的相等性必然泄露明文的相等性——提示建议取 $c_1=c_2$ 正是此意。

任取方案与 $m\neq m^{\prime}$（$|\mathcal{M}|>1$）。取如下消息分布（"两明文相同"与"不同"的先验各占一半，故"是否相同"本身是有信息量的）：

$$\Pr[(M_1,M_2)=(m,m)]=\Pr[(M_1,M_2)=(m,m^{\prime})]=\frac12.$$

取 $\hat c$ 使 $\Pr[\mathsf{Enc}_K(m)=\hat c]>0$，考虑事件 $E=\{C_1=\hat c\ \wedge\ C_2=\hat c\}$。

- **分支 $(m,m)$**：$\Pr[E\mid(m,m)]=\sum_k\Pr[K=k]\,\Pr[\mathsf{Enc}_k(m)=\hat c]^{2}>0$。（平方的来源：两条消息共用同一密钥 $k$，但两次加密的内部随机性相互独立，条件在 $k$ 上后，两条密文各自以概率 $\Pr[\mathsf{Enc}_k(m)=\hat c]$ 等于 $\hat c$。$>0$ 的来源：把 $\hat c$ 满足的条件 $\Pr[\mathsf{Enc}_K(m)=\hat c]>0$ 按 $k$ 展开，即知至少存在一个 $k$ 同时使 $\Pr[K=k]>0$ 与 $\Pr[\mathsf{Enc}_k(m)=\hat c]>0$。）
- **分支 $(m,m^{\prime})$**：$E$ 要求同一密钥 $k$ 既以正概率把 $m$ 加密为 $\hat c$、又以正概率把 $m^{\prime}$ 加密为 $\hat c$。但完全正确性要求：$\mathsf{Enc}_k(m)$ 的每个可能输出都解密为 $m$，$\mathsf{Enc}_k(m^{\prime})$ 的每个可能输出都解密为 $m^{\prime}$，而 $\mathsf{Dec}_k(\hat c)$ 取值唯一——二者不能同时发生。故 $\Pr[E\mid(m,m^{\prime})]=0$。

于是 $\Pr[E]=\frac12\Pr[E\mid(m,m)]>0$（$E$ 确实可能被观测到）。而 $E$ 在 $(m,m^{\prime})$ 分支下概率为 ${0}$，故一旦观测到 $c_1=c_2=\hat c$，该分支即被排除，后验直接跳到 ${1}$：

$$\Pr[M_1=m\wedge M_2=m\mid E]=1\ \neq\ \frac12=\Pr[M_1=m\wedge M_2=m],$$

违反定义。$\blacksquare$

### (b) 对"两条不同消息"完全保密的方案

**构造（随机单射密钥）**：取 $\mathcal{M}=\{0,1\}^{\ell}$，$\mathcal{C}=\{0,1\}^{\ell+1}$，记 $N=2^{\ell+1}$。Gen 均匀选取一个从 $\mathcal{M}$ 到 $\mathcal{C}$ 的**单射** $\pi$ 作为密钥（共 $N!/(N-2^{\ell})!$ 个，密钥巨大，但题目允许非高效方案）；$\mathsf{Enc}_\pi(m)=\pi(m)$，Dec 为相应的逆映射。

**分析**：随机单射的基本性质——对任意不同的 $m_1\neq m_2$ 与不同的 $c_1\neq c_2$，

$$\Pr[\pi(m_1)=c_1\ \wedge\ \pi(m_2)=c_2]=\frac{1}{N(N-1)},$$

与 $(m_1,m_2)$ 无关（像在"无重复有序对"上均匀）。任取满足 $M_1\neq M_2$（以概率 1）的分布，对 $c_1\neq c_2$：

$$\Pr[C_1=c_1\wedge C_2=c_2]=\sum_{(m_1,m_2)}\Pr[(m_1,m_2)]\cdot\frac{1}{N(N-1)}=\frac{1}{N(N-1)},$$

由贝叶斯公式，后验 $=$ 先验，定义满足 ✓。（(a) 的障碍恰好被绕开：$m_1\neq m_2$ 以概率 1 保证 $c_1\neq c_2$，"密文相等"这条泄露信道在此分布类上概率为 ${0}$，定义对 $c_1=c_2$ 不施加任何要求。）

**高效替代**（题目提示存在）：把 $\mathcal{M}=\mathcal{C}=\mathrm{GF}(2^{\ell})$，密钥 $(a,b)$ 均匀取自 $\mathrm{GF}(2^{\ell})^{*}\times\mathrm{GF}(2^{\ell})$，$\mathsf{Enc}_{(a,b)}(m)=am+b$。对 $m_1\neq m_2$ 与 $c_1\neq c_2$，方程组 $am_i+b=c_i$ 有**唯一**解 $a=(c_1-c_2)/(m_1-m_2)$、$b=c_1-am_1$，故 $(C_1,C_2)$ 在无重复有序对上均匀，分析同上，而加解密完全高效。

---

### 附：相关脚本（与本解答同目录，位于 `习题/Ch02/`）

| 脚本 | 用途 |
|---|---|
| `solve_ex2_8_2_9.py` | 2.8 / 2.9（附 2.10(a)、2.11）：枚举全部 $(m,k)$，按引理 2.5 逐一枚举密文分布，判定各小方案是否完全保密 |
| `solve_ex2_12_2_13.py` | 2.12 / 2.13：按分数精确枚举全部周期与密钥，验证 $\Pr[\mathsf{PrivK}^{\mathsf{eav}}=1]$ 分别为 ${1}$、${2}/{3}$、${5}/{6}$ |
| `solve_ex2_16.py` | 2.16：在允许字符集（大小写字母与空格）内暴力枚举，验证 (a) 恰为 $\{$空格, p$\}$、(b) 唯一解为 $\{$空格, t, e$\}$ |
