# 第一章　习题解答

> *Introduction to Modern Cryptography (3rd ed.), Katz & Lindell — Chapter 1 Exercises*

---

## 习题 1.1　解密单表替换密码

> **题目**　Decrypt the ciphertext provided at the end of the section on mono-alphabetic substitution ciphers.
> **题目**　解密单表替换密码一节末尾给出的那段密文。

**密文**（244 字符，已对照原 PDF 核实）：
```
JGRMQOYGHMVBJWRWQFPWHGFFDQGFPFZRKBEEBJIZQQOCIBZKLFAFGQVFZFWWEOGWOPFGFHWOLPHLRLOLF
DMFGQWBLWBWQOLKFWBYLBLYLFSFLJGRMQBOLWJVFPFWQVHQWFFPQOQVFPQOCFPOGFWFJIGFQVHLHLROQV
FGWJVFPFOLFHGQVQVFILEOGQILHQFQGIQVVOSFAFGBWQVHQWIJVWJVFPFWHGFIWIHZZRQGBABHZQOCGFHX
```

### 解题方法（频率分析，依教材 1.3 节）

**第一步：统计单字频率**，得密文字母频率降序为
$$F(15.2\%),\ Q(10.7\%),\ W(8.6\%),\ G(7.8\%),\ L(7.0\%),\ O(6.6\%),\ V(6.1\%),\ H(5.7\%),\dots$$
对照英语频率降序 $E,T,A,O,I,N,S,H,R,\dots$，可初步猜 $F\to e$。

**第二步：用最高频 $n$-gram 锁定强锚点**。统计发现三字母组 $\texttt{QVF}$ 出现 4 次、双字母组 $\texttt{QV}$ 出现 9 次——这正是英语中的 **THE / TH**，故
$$Q\to t,\quad V\to h,\quad F\to e.$$

**第三步：辨认长词**。密文开头的 `JGRMQOYGHMVBJ`（13 字母）配合 $Q\to t$ 等锚点，模式恰好匹配 **cryptographic**，从而一次性确定 10 个字母的映射：
$$J\to c,\ G\to r,\ R\to y,\ M\to p,\ Q\to t,\ O\to o,\ Y\to g,\ H\to a,\ V\to h,\ B\to i.$$
紧随其后的 `WRWQFPW` 则是 **systems**（得 $W\to s,\ P\to m$），`HGF` 是 **are**，`FLJGRMQBOL` 是 **encryption**（得 $L\to n$），`VOSFAFG` 是 **however**（得 $S\to w,\ A\to v$）。注意 `LFSFL` 虽呈 12321 模式、易误猜为 **level**，实则是跨词片段 **new en**[cryption]（n-e-w-e-n）——词边界未知时的典型陷阱，须靠与其他锚点交叉验证排除。

**第四步：确定剩余字母**。$D\to x,\ K\to d,\ Z\to l,\ E\to f,\ I\to u$ 等由 `extremely`、`difficult`、`such` 等词交叉锁定；最后用 bigram 评分做 hill-climbing 辅助搜索，最低频的 $b,n,v,w,k$ 五个字母按单词拼写（`build`、`new`、`however`、`break`、`trivial`）交叉验证定稿。

### 完整密钥（明文 → 密文置换）

```
明文: a b c d e f g h i k l m n o p r s t u v w x y z
密文: H C J K F E Y V B X Z P L O M G W Q I A S D R *
      (* j, q, z 未在明文中出现，对应密文 N, T, U，不影响解密)
```

### 解密结果

逐字解密得（无需任何猜测修补，即为规范英文）：
> cryptographic systems are extremely difficult to build nevertheless for some reason many nonexperts insist on designing new encryption schemes that seem to them to be more secure than any other scheme on earth the unfortunate truth however is that such schemes are usually trivial to break

按英语规范断句：
> **Cryptographic systems are extremely difficult to build. Nevertheless, for some reason, many nonexperts insist on designing new encryption schemes that seem to them to be more secure than any other scheme on earth. The unfortunate truth, however, is that such schemes are usually trivial to break.**

---

## 习题 1.2　单表替换密码的形式化定义

> **题目**　Provide a formal definition of the Gen, Enc, and Dec algorithms for the mono-alphabetic substitution cipher.
> **题目**　给出单表替换密码的 Gen、Enc、Dec 算法的形式化定义。

设字母表为 $\Sigma=\{0,\dots,25\}$，明文/密文空间 $\mathcal{M}=\mathcal{C}=\Sigma^{*}$（字母串）。密钥是一个置换 $\pi:\Sigma\to\Sigma$（即 $\Sigma$ 上的双射），$\pi^{-1}$ 为其逆置换。

- **Gen**：从所有 ${26}!$ 个置换中均匀随机选取一个作为密钥 $k=\pi$。
 $$\mathsf{Gen}: \ \pi \xleftarrow{\$} \mathrm{Sym}(\Sigma).$$
- **Enc**：对明文 $m=m_1\cdots m_\ell$，逐字符应用置换：
 $$\mathsf{Enc}_\pi(m_1\cdots m_\ell)=c_1\cdots c_\ell,\quad c_i=\pi(m_i).$$
- **Dec**：对密文逐字符应用逆置换：
 $$\mathsf{Dec}_\pi(c_1\cdots c_\ell)=m_1\cdots m_\ell,\quad m_i=\pi^{-1}(c_i).$$

正确性由 $\pi^{-1}(\pi(m_i))=m_i$ 立得。密钥空间 $|\mathcal{K}|=26!\approx 2^{88}$。

---

## 习题 1.3　维吉尼亚密码的形式化定义

> **题目**　Provide a formal definition of the Gen, Enc, and Dec algorithms for the Vigenère cipher. (Note: there are several plausible choices for Gen; choose one.)
> **题目**　给出维吉尼亚密码的 Gen、Enc、Dec 算法的形式化定义。注意：Gen 有多种合理的选择，请任选一种。

设 $\Sigma=\{0,\dots,25\}$。Gen 有多种合理选择（周期 $t$ 固定 / 随机等），下面取"固定上界 $T$、周期与密钥均随机"版本。

- **Gen**：先均匀选取周期 $t\in\{1,\dots,T\}$，再独立均匀地选取 $t$ 个密钥字符 $k_1,\dots,k_t\in\Sigma$：
 $$\mathsf{Gen}: \ t\xleftarrow{\$}\{1,\dots,T\},\quad k_i\xleftarrow{\$}\Sigma\ (i=1,\dots,t).$$
- **Enc**：明文第 $i$ 个字符按密钥第 $((i-1)\bmod t)+1$ 个字符移位：
 $$\mathsf{Enc}_k(m_1\cdots m_\ell)=c_1\cdots c_\ell,\quad c_i=\big[m_i+k_{((i-1)\bmod t)+1}\big]\bmod 26.$$
- **Dec**：反向移位：
 $$\mathsf{Dec}_k(c_1\cdots c_\ell)=m_1\cdots m_\ell,\quad m_i=\big[c_i-k_{((i-1)\bmod t)+1}\big]\bmod 26.$$

正确性：$\big[[m_i+k_j]\bmod 26 - k_j\big]\bmod 26=m_i$。当 $t=1$ 时退化为移位密码。密钥空间大小 $\sum_{t=1}^{T}26^{t}$。

---

## 习题 1.4　区分移位密码与周期 $>1$ 的维吉尼亚密码

> **题目**　Say you are given a ciphertext that corresponds to English-language text that was encrypted using either the shift cipher or the Vigenère cipher with period greater than 1. How could you tell which was the case?
>
> **题目**　给定一段对应英文文本的密文，它是用移位密码或周期大于 1 的维吉尼亚密码加密的。如何判断属于哪一种情形？

**用密文的重合指数（index of coincidence）判别。** 对密文统计各字符频率 $q_i$，计算
$$IC = \sum_{i=0}^{25} q_i^{\,2}.$$

- 若为**移位密码**：整个密文相当于英文文本整体平移，字符频率分布形状不变，故 $IC\approx \sum p_i^{\,2}\approx 0.065$。
- 若为**周期 $t>1$ 的维吉尼亚密码**：密文是 $t$ 个不同移位交织的结果，频率被"抚平"，趋于均匀，故 $IC\approx \sum (1/26)^2\approx 0.038$。

因此 $IC$ 接近 ${0}.065$ 即移位密码，接近 ${0}.038$ 即维吉尼亚密码。补充验证：对疑似维吉尼亚的情形，可用 1.11 提到的 $S_\tau$ 在不同 $\tau$ 下的取值找到周期。

---

## 习题 1.5　实现移位密码与维吉尼亚密码的攻击

> **题目**　Implement the attacks described in this chapter for the shift cipher and the Vigenère cipher.
> **题目**　实现本章描述的针对移位密码与维吉尼亚密码的攻击。

下面给出核心实现。

### 移位密码攻击（教材式 (1.2) 频率法）

```python
def attack_shift(ct):
    # p_i: 英文第 i 个字母频率（教材图 1.3）
    p = [0.082,0.015,0.028,0.043,0.127,0.022,0.020,0.061,0.070,0.002,
         0.008,0.040,0.024,0.067,0.075,0.019,0.001,0.060,0.063,0.091,
         0.028,0.010,0.023,0.002,0.020,0.001]
    n = len(ct)
    q = [ct.count(chr(i+ord('A')))/n for i in range(26)]
    best_k, best_score = 0, -1
    for k in range(26):                       # 对每个候选密钥 k
        score = sum(p[i]*q[(i+k) % 26] for i in range(26))  # 教材式 (1.2) 的 I_k
        if score > best_score:
            best_score, best_k = score, k     # 真密钥处 I_k≈0.065 且为最大者
    return best_k
```

（教材原文的判据是"$I_k$ 最接近 0.065"，实现中取 $I_k$ 最大者：真密钥处 $I_k\approx\sum p_i^2\approx0.065$ 恰为峰值，两种判据在实际中一致，取最大更易于自动化。）

### 维吉尼亚密码攻击（重合指数定周期 + 每流频率分析）

```python
def attack_vigenere(ct, Tmax=20):
    # 步骤 (a): 由 S_tau ≈ 0.065 确定周期 t
    n = len(ct)
    def S(tau):
        seq = ct[0::tau]                                    # 第 0 个流
        q = [seq.count(chr(i+65))/len(seq) for i in range(26)]
        return sum(x*x for x in q)
    # τ 为 t 的倍数时 S_τ 同样 ≈0.065，故取最小的超过阈值 0.06 的 τ
    cands = [tau for tau in range(1, min(Tmax, n)+1) if S(tau) > 0.06]
    t = min(cands) if cands else max(range(1, min(Tmax, n)+1), key=S)

    # 步骤 (b): 对每个流用移位攻击还原该密钥位
    key = []
    for j in range(t):
        key.append(attack_shift(ct[j::t]))
    return ''.join(chr(k+65) for k in key)
```

自检验证：对已知移位的英文文本可正确还原移位密钥；对以教材示例密钥 `beads`（周期 5）加密的较长英文文本，攻击正确定出周期 5 并逐流还原出密钥 `BEADS`。

---

## 习题 1.6　256 字节字母表 + XOR 的版本

> **题目**　The shift and Vigenère ciphers can also be defined on the 256-character alphabet consisting of all possible bytes (8-bit strings), and using XOR instead of modular addition.
>
> **(a)**　Provide a formal definition of both schemes in this case.
>
> **(b)**　Discuss how the attacks we have shown in this chapter can be modified to break these schemes.
>
> **题目**　移位密码和维吉尼亚密码也可以定义在由所有可能字节（8 位串）构成的 256 字符字母表上，并用 XOR 代替模加法。
>
> **(a)**　给出此种情形下两个方案的形式化定义。
>
> **(b)**　讨论本章介绍的攻击可以如何修改，以攻破这些方案。

### (a) 形式化定义

设 $\Sigma=\{0,1\}^{8}$（所有 8 位字节，$|\Sigma|=256$）。

- **移位（XOR）密码**：$k\in\Sigma$，
 $$\mathsf{Enc}_k(m)=m\oplus k,\qquad \mathsf{Dec}_k(c)=c\oplus k.$$
- **维吉尼亚（XOR）密码**：密钥为字节串 $k=k_1\cdots k_t$，$k_i\in\Sigma$，
 $$\mathsf{Enc}_k(m_1\cdots m_\ell)=c_1\cdots c_\ell,\quad c_i=m_i\oplus k_{((i-1)\bmod t)+1},$$
 $$\mathsf{Dec}_k(c)_i=c_i\oplus k_{((i-1)\bmod t)+1}.$$

正确性来自 XOR 的自逆性 $(x\oplus k)\oplus k=x$。XOR 与模 ${2}^8$ 加法都是 $\Sigma$ 上的固定双射，从密码分析角度看二者**等价**：把字节看作 ${0}\sim255$，XOR $k$ 与加 $k$（不进位）一样是一个逐位的固定置换。

### (b) 攻击的修改

原理不变，只把"26 字母频率"换成"256 字节频率"：

1. **移位（XOR）密码**：对每个候选 $k\in\Sigma$，用明文字节频率分布 $p_i$（如英文 ASCII 文本中各字节频率）计算 $I_k=\sum_i p_i\cdot q_{i\oplus k}$，取最大者。或直接穷举 256 个 $k$。
2. **维吉尼亚（XOR）密码**：仍用重合指数 $S_\tau$ 定周期，再对每个字节流独立做 XOR 移位攻击。对一般文件（含可打印 ASCII）字节频率同样高度不均匀，攻击依然有效。

---

## 习题 1.7　为何重合指数法不能用 $\sum_i p_i$？

> **题目**　The index of coincidence method relies on a known value for the sum of the squares of plaintext-letter frequencies (cf. Equation (1.1)). Why would it not work using the sum $\sum_i p_i$ itself?
>
> **题目**　重合指数方法依赖于明文字母频率平方和的已知取值（参见式 (1.1)）。为什么改用 $\sum_i p_i$ 本身就不行了？

因为 $\sum_i p_i$ 是个**与密钥无关的常数**，无法提供任何判别信息：

$$\sum_{i=0}^{25} p_i = p_0+p_1+\cdots+p_{25} = 1,$$

这是概率归一化的必然结果——任何字母分布（无论怎么置换、移位）的频率之和都恒为 ${1}$。因此对每个候选周期 $\tau$，$\sum_i q_i$ 都等于 ${1}$，无法在正确周期处出现峰值。

而平方和 $\sum_i p_i^{\,2}\approx 0.065$ 之所以有效，是因为平方是**非线性**的：它放大高频字母的贡献、压缩低频字母，从而保留了分布的"形状"。英语（高度不均匀）的 $\sum p_i^{\,2}\approx 0.065$，而均匀分布的 $\sum (1/26)^2\approx 0.038$，两者显著不同，才能在正确对齐 / 正确周期处给出可辨识的峰值。线性求和恰好把这种形状信息抹平了。

---

## 习题 1.8　选择明文攻击下三种密码的破译

> **题目**　Show that the shift, substitution, and Vigenère ciphers are all trivial to break using a chosen-plaintext attack. How much chosen plaintext is needed to recover the key for each of the ciphers?
>
> **题目**　证明移位密码、单表替换密码和维吉尼亚密码在选择明文攻击下都不堪一击。对每种密码，恢复密钥各需要多少选择明文？

在选择明文攻击下，攻击者可获取任意明文对应的密文，即直接查询加密预言机 $\mathsf{Enc}_k(\cdot)$。

| 密码 | 密钥内容 | 所需选择明文 | 说明 |
|---|---|---|---|
| 移位密码 | 1 个移位值 $k\in\{0,\dots,25\}$ | **1 个字符** | 选明文 `a`，密文 $\mathsf{Enc}_k(\texttt{a})$ 即给出 $k$。 |
| 单表替换 | 26 字母的置换 $\pi$ | **含全部 26 字母的 1 段明文（26 字符）** | 选明文 `abcdefghijklmnopqrstuvwxyz`，其密文直接读出整个 $\pi$。 |
| 维吉尼亚（周期 $t$） | $t$ 个移位值 | **长度 $\ge t$ 的 1 段明文（最少 $t$ 个字符）** | 周期 $t$ 时明文第 $i$ 位用 $k_{((i-1)\bmod t)+1}$ 加密，故长 $t$ 的明文让每个密钥位恰好各用一次：选一段长 $t$ 的已知明文（最简单如 $t$ 个 `a`），密文第 $i$ 位即读出 $k_i$（$i=1,\dots,t$）。 |

综上：移位密码 1 个字符；单表替换 26 个字符（整个字母表）；维吉尼亚密码 $t$ 个字符（$t$ 为周期，且需知道 $t$）。

---

## 习题 1.9　口令为 `abcd` 或 `bedg`：移位密码

> **题目**　Assume an attacker knows that a user's password is either abcd or bedg. Say the user encrypts his password using the shift cipher, and the attacker sees the resulting ciphertext. Show how the attacker can determine the user's password, or explain why this is not possible.
>
> **题目**　假设攻击者知道某用户的口令要么是 abcd 要么是 bedg。用户用移位密码加密口令，攻击者看到了所得的密文。说明攻击者如何确定用户的口令，或解释为何不可能做到。

**可以确定。** 记两个候选口令的逐位差（模 26）：
$$\texttt{bedg}-\texttt{abcd} = (1,3,1,3),$$
这是一个**非常数**序列。在移位密码（等价于周期 ${1}$ 的维吉尼亚）下，两个口令的可达密文集合分别为
$$\{\texttt{abcd}\text{ 移位 }k:k\in\mathbb{Z}_{26}\},\qquad \{\texttt{bedg}\text{ 移位 }k:k\in\mathbb{Z}_{26}\},$$
两集合**不相交**（数值验证：二者各 26 个密文，重叠为 0）。因此任何一条密文至多能由其中一个口令产生。

**判定方法**：对观察到的密文 $c=c_1c_2c_3c_4$，分别计算其与 `abcd`、`bedg` 的逐位差（模 26）：
$$d^{(1)}_i=c_i-\texttt{abcd}_i,\qquad d^{(2)}_i=c_i-\texttt{bedg}_i.$$
若 $d^{(1)}_1=d^{(1)}_2=d^{(1)}_3=d^{(1)}_4$（四个差全相等），则口令为 `abcd`，密钥即该公共差值；否则口令为 `bedg`（其四个差必全等）。

---

## 习题 1.10　维吉尼亚密码：周期 2、3、4

> **题目**　Repeat the previous exercise for the Vigenère cipher using period 2, using period 3, and using period 4.
>
> **题目**　对维吉尼亚密码分别用周期 2、周期 3、周期 4，重复上一题。

结论（已用代码遍历全部密钥验证）：

| 周期 | 是否可区分 | 原因 |
|---|---|---|
| **2** | **不可区分** | 差序列 $(1,3,1,3)$ 恰为周期 2，可被一个周期 2 的密钥差吸收：$\texttt{bedg}=\texttt{abcd}$ 经密钥 $(1,3)$ 移位即得。两可达密文集合完全重合（各 676 个，重叠 676）。 |
| **3** | **可区分** | 差序列 $(1,3,1,3)$ 不是周期 3（周期 3 要求第 1、4 位相等，而 ${1}\ne 3$），无法被任何周期 3 密钥吸收。两可达集合不交（重叠 0）。 |
| **4** | **不可区分** | 周期 4 的密钥长度等于口令长度 4，每个位置独立移位（等价一次性密码本），任意差都能吸收。两可达集合完全重合（各 ${26}^4$ 个，全部重叠）。 |

**统一规律**：把长 $n$ 的口令看作 $\mathbb{Z}_{26}^{\,n}$ 中的向量；周期 $t$ 的全部维吉尼亚密钥构成子群
$$H_t=\{(k_1,\dots,k_t,\,k_1,\dots)\}\subseteq\mathbb{Z}_{26}^{\,n}\quad(\text{即周期为 } t \text{ 的序列}).$$
口令 $p$ 的可达密文集合恰为陪集 $p+H_t$；两个陪集**要么完全相等，要么完全不相交**，且
$$p+H_t=p^{\prime}+H_t\ \Longleftrightarrow\ \Delta=p^{\prime}-p\in H_t\ \Longleftrightarrow\ \Delta\text{ 是以 } t \text{ 为周期的序列}.$$
本题 $\Delta=(1,3,1,3)$：对 $t=2$ 成立（不可区分）；对 $t=3$ 不成立（可区分）；$t\ge n=4$ 时 $H_t=\mathbb{Z}_{26}^{\,n}$，必然不可区分；$t=1$（移位密码）要求 $\Delta$ 为常数列，不满足，故可区分。

---

## 习题 1.11　非英语明文对维吉尼亚攻击的影响

> **题目**　The attack on the Vigenère cipher has two steps: (a) find the key length by identifying $\tau$ with $S_{\tau} \approx 0.065$ (cf. Equation (1.3)) and (b) for each character of the key, find $j$ maximizing $I_j$ (cf. Equation (1.2)), using $\{p_i\}$ corresponding to English text. What happens in each case if the underlying plaintext is in a language other than English?
>
> **题目**　维吉尼亚攻击分两步：(a) 通过找出使 $S_\tau\approx 0.065$ 的 $\tau$ 来确定密钥长度（参见式 (1.3)）；(b) 对密钥的每个字符，找使 $I_j$ 最大的 $j$（参见式 (1.2)），其中 $\{p_i\}$ 取英语文本的频率。若底层明文是英语以外的语言，每一步分别会怎样？

两步都**依赖明文语言的频率统计量**，换语言则阈值与频率表都要相应更换。

- **步骤 (a)（定周期）**：阈值 ${0}.065$ 来自英语的 $\sum_i p_i^{\,2}$。不同语言的字母分布不均程度不同，$\sum_i p_i^{\,2}$ 也不同（如英语 $\approx0.065$，俄语、法语、德语各有差异）。若仍套用英语的 ${0}.065$：
  - 真实周期 $\tau=t$ 处的 $S_\tau$ 实际接近**该语言**的 $\sum p_i^2$，可能与 ${0}.065$ 偏离，导致峰值被漏判或错判；
  - 用错的阈值会定出错误的密钥长度。
  
  正确做法：用**目标语言**的 $\sum p_i^2$ 作为阈值去识别 $S_\tau$ 的峰值。

- **步骤 (b)（定每个密钥位）**：$I_j=\sum_i p_i\cdot q_{i+j}$ 用英语 $\{p_i\}$。若明文是别的语言，其真实字母频率 $\{p_i^{(\text{lang})}\}$ 不同，则
  - 在正确移位 $j=k_\text{true}$ 处，$I_j$ 不再是最大（因为用的 $p_i$ 与实际分布不匹配）；
  - 会还原出错误的密钥字符。
  
  正确做法：用**目标语言的字母频率表** $\{p_i^{(\text{lang})}\}$ 代入 $I_j$。

简言之：整套方法的**结构**（重合指数定周期 + 逐流频率对齐）对任何自然语言都适用，但所有"英语常数"（${0}.065$ 这个平方和、字母频率向量 $\{p_i\}$）都必须换成**对应语言的统计量**，否则两步都会失败。
