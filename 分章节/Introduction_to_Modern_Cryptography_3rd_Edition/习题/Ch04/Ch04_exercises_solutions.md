# 第四章　习题解答

> *Introduction to Modern Cryptography (3rd ed.), Katz & Lindell — Chapter 4 Exercises*

---

## 习题 4.1　带 Vrfy 预言机的 MAC 安全性

> **题目**　(a) 给出敌手同时拥有 Mac、Vrfy 预言机时的安全性定义；(b) 使用规范验证的确定性 MAC 满足定义 4.2 $\Rightarrow$ 也满足 (a)。

**(a) 定义**。在 $\mathsf{Mac\text{-}forge}$ 实验中，敌手 $\mathcal{A}$ 获得输入 ${1}^n$、访问 $\mathsf{Mac}_k(\cdot)$ **与** $\mathsf{Vrfy}_k(\cdot,\cdot)$ 两个预言机，可自适应查询；最终输出 $(m^*,t^*)$。令 $\mathcal{Q}$ 为 $\mathcal{A}$ 提交给 Mac 预言机的消息集合。$\mathcal{A}$ 成功当且仅当 $m^*\notin\mathcal{Q}$ **且** $\mathsf{Vrfy}_k(m^*,t^*)=1$。方案安全若对所有 PPT $\mathcal{A}$，$\Pr[\mathsf{Mac\text{-}forge}_{\mathcal{A},\Pi}(n)=1]\le\mathsf{negl}(n)$。

**(b)** 设 $\Pi$ 是确定性、使用规范验证（$\mathsf{Vrfy}_k(m,t)=1\iff t=\mathsf{Mac}_k(m)$）的安全 MAC。设 $\mathcal{A}$ 是 (a) 意义下的敌手（有 Mac、Vrfy 两个预言机），成功概率 $\varepsilon$，Vrfy 查询次数不超过多项式 $q(n)$。构造定义 4.2 意义下的敌手 $\mathcal{B}$（仅有 Mac 预言机）：$\mathcal{B}$ 模拟 $\mathcal{A}$，Mac 查询直接转发；并在开始时均匀猜一个下标 $j\leftarrow\{1,\ldots,q(n)\}$。对 $\mathcal{A}$ 的第 $i$ 次 Vrfy 查询 $(m,t)$：

- 若 $m\in\mathcal{Q}$（已查询过，$\mathcal{B}$ 知道 $\mathsf{Mac}_k(m)$）：由确定性 + 规范验证，如实应答 $[t\overset?=\mathsf{Mac}_k(m)]$；
- 若 $m\notin\mathcal{Q}$：若 $i=j$，$\mathcal{B}$ 立即以 $(m,t)$ 作为自己的输出并停机；否则应答 ${0}$。

若 $\mathcal{A}$ 最终输出 $(m^*,t^*)$ 而 $\mathcal{B}$ 未提前停机，$\mathcal{B}$ 输出 $(m^*,t^*)$。

**分析。** $\mathcal{A}$ 在 (a) 下成功（$(m^*,t^*)$ 有效且 $m^*\notin\mathcal{Q}$）的来源只有两种：

- **(i) 最终输出本身**：这本身就是 4.2 意义的伪造，$\mathcal{B}$ 原样输出即成功（只要模拟未因提前停机而失真——在情形 (i) 中无妨）；
- **(ii) 某次"$m\notin\mathcal{Q}$ 的 Vrfy 查询"其实有效**：该 $(m,t)$ 也是 4.2 意义的伪造（$m\notin\mathcal{Q}$ 且 $\mathsf{Vrfy}_k(m,t)=1$）。$\mathcal{B}$ 以 ${1}/q(n)$ 的概率猜中这次查询的下标 $j$ 并正确输出它。

注意情形 (ii) 恰是模拟可能失真的地方（$\mathcal{B}$ 对有效查询答了 0）；但只要某次有效查询存在，$\mathcal{B}$ 就有 ${1}/q$ 概率恰好停在那里、把失真发生前的查询本身变成伪造。合并两情形：

$$\Pr[\mathsf{Mac\text{-}forge}_{\mathcal{B},\Pi}(n)=1]\ge\frac{\varepsilon(n)}{q(n)},$$

由 $\Pi$ 满足定义 4.2 知右端可忽略，故 $\varepsilon$ 可忽略，$\Pi$ 满足 (a)。$\blacksquare$

---

## 习题 4.2　安全（定义 4.2）但带 Vrfy 预言机时不安全的 MAC

> **题目**　假设安全 MAC 存在，构造满足 4.2 但在 4.1(a)（敌手额外有 Vrfy 预言机）下不安全的 MAC。

**关键想法：把"密钥泄漏"门控在有效标签之后。** 4.2 与 4.1(a) 的成功判定确实由同一个 $\mathsf{Vrfy}$ 给出，且 4.2 敌手只能输出一个 $(m,t)$ 盲猜，而 4.1(a) 敌手可把 $\mathsf{Vrfy}$ 当搜索预言机自适应探测。要让探测能逐位读出密钥、盲猜却无从下手，正确手法是：**只有当查询附带一个有效标签时才泄露密钥比特**。探测查询打在**已经查询过**的消息上（$m\in\mathcal Q$，其标签合法），因此探测本身不构成伪造；而最终伪造仍要求在新消息上给出有效标签，归约到原方案。

**构造（KL 官方题解）。** 设 $\Pi=(\mathsf{Gen},\mathsf{Mac},\mathsf{Vrfy})$ 是安全 MAC（密钥 $k\in\{0,1\}^n$）。新方案 $\Pi^{\prime}=(\mathsf{Gen},\mathsf{Mac}^{\prime},\mathsf{Vrfy}^{\prime})$ 的标签形如四元组 $\langle c,t,i,b\rangle$（$c$ 为控制位，$i\in\{1,\ldots,n\}$ 为下标，$b$ 为单比特）：

- $\mathsf{Mac}^{\prime}_k(m)$：计算 $t\leftarrow\mathsf{Mac}_k(m)$，输出 $\langle 0,t,0,0\rangle$。
- $\mathsf{Vrfy}^{\prime}_k(m,\langle c,t,i,b\rangle)$：
  - 若 $c=0$：输出 ${1}\iff\mathsf{Vrfy}_k(m,t)=1$；
  - 若 $c=1$：输出 ${1}\iff\mathsf{Vrfy}_k(m,t)=1$ **且** $k$ 的第 $i$ 位 $k_i=b$。

正确性显然（$\mathsf{Vrfy}^{\prime}_k(m,\mathsf{Mac}^{\prime}_k(m))=1$ 走 $c=0$ 分支）。

**$\Pi^{\prime}$ 满足定义 4.2（无 Vrfy 预言机时安全）。** 设 $\mathcal A$ 攻 $\Pi^{\prime}$，构造攻 $\Pi$ 的 $\mathcal B$：$\mathcal B$ 把 $\mathcal A$ 的 Mac 查询 $m$ 转发给自己的 $\mathsf{Mac}_k(\cdot)$ 预言机，把返回的 $t$ 包装成 $\langle 0,t,0,0\rangle$ 交给 $\mathcal A$。当 $\mathcal A$ 输出 $(m^*,\langle c^*,t^*,i^*,b^*\rangle)$ 时，$\mathcal B$ 输出 $(m^*,t^*)$。

无论 $c^*=0$ 还是 $c^*=1$，$\mathsf{Vrfy}^{\prime}_k(m^*,\langle c^*,t^*,i^*,b^*\rangle)=1$ 都以 $\mathsf{Vrfy}_k(m^*,t^*)=1$ 为前提；且 $\mathcal A$ 成功要求 $m^*\notin\mathcal Q$。故 $\mathcal A$ 成功 $\Rightarrow$ $\mathcal B$ 成功：

$$\Pr[\mathsf{Mac\text{-}forge}_{\mathcal A,\Pi^{\prime}}(n)=1]\le\Pr[\mathsf{Mac\text{-}forge}_{\mathcal B,\Pi}(n)=1]\le\mathsf{negl}(n).$$

（直观：$\mathcal A$ 的 Mac 查询只能拿到 $c=0$ 的标签，永远接触不到 $c=1$ 分支；要在新消息上触发 $c=1$ 分支，先得有该消息的有效 $\Pi$ 标签——那本身就是伪造 $\Pi$。）

**$\Pi^{\prime}$ 在 4.1(a) 下不安全（有 Vrfy 预言机时可逐位盗钥）。** 敌手 $\mathcal A$：

1. 任取消息 $m$（如 $m=0^n$），查询 Mac 预言机得 $\langle 0,t,0,0\rangle$，其中 $\mathsf{Vrfy}_k(m,t)=1$；
2. 对 $i=1,\ldots,n$，查询 $\mathsf{Vrfy}^{\prime}_k(m,\langle 1,t,i,0\rangle)$：返回 ${1}\iff k_i=0$（因 $\mathsf{Vrfy}_k(m,t)=1$ 恒成立，判定退化为密钥位比较）。$n$ 次查询即完整恢复 $k$；
3. 任选新消息 $m^*\notin\mathcal Q$，用 $k$ 自行计算 $t^*\leftarrow\mathsf{Mac}_k(m^*)$，输出 $(m^*,\langle 0,t^*,0,0\rangle)$。

第 2 步的探测查询都打在 $m\in\mathcal Q$ 上，不构成伪造；第 3 步 $\mathsf{Vrfy}^{\prime}_k(m^*,\langle 0,t^*,0,0\rangle)=1$ 且 $m^*\notin\mathcal Q$，成功概率 ${1}$。

**回应原"存疑"。** (1) 不需要"消息空间挖洞"，也不需要随机化 $\mathsf{Mac}$——上述确定性构造即可。(2) 原分析中"泄露 1 比特就会被 4.2 敌手以 ${1}/{2}$ 概率伪造"的困难由**门控**化解：$c=1$ 分支只在 $\mathsf{Vrfy}_k(m,t)=1$ 时才比较密钥位，4.2 敌手在新消息上拿不出有效 $t$，盲猜 $\langle 1,t,i,b\rangle$ 等价于直接伪造 $\Pi$。(3) 两定义共用同一 $\mathsf{Vrfy}$ 作成功判定这一点并不矛盾——区别在于攻击过程：4.1(a) 敌手能用 Vrfy 预言机在**旧消息**上探测密钥，4.2 敌手不能。（本构造与第三版教师手册的官方解答逐字一致。）$\blacksquare$

---

## 习题 4.3　命题 4.4：确定性 + 规范验证 $\Rightarrow$ 强安全

> **题目**　Prove Proposition 4.4.
> **题目**　证明命题 4.4（确定性 + 规范验证的 MAC 满足定义 4.2 ⇒ 也满足定义 4.3 的强安全）。

设 $\Pi$ 确定、使用规范验证（$\mathsf{Vrfy}_k(m,t)=1\iff t=\mathsf{Mac}_k(m)$），且安全（定义 4.2）。证强安全（定义 4.3：$\mathsf{Mac\text{-}sforge}$，敌手输出 $(m^*,t^*)$，成功当 $t^*$ 有效且 $(m^*,t^*)\notin\mathcal{Q}$，$\mathcal{Q}$ 是 Mac 预言机返回的 (消息,标签) 对集合）。

设 $\mathcal{A}$ 是攻 $\mathsf{Mac\text{-}sforge}$ 的 PPT 敌手，成功概率 $\varepsilon$。构造攻 $\mathsf{Mac\text{-}forge}$ 的 $\mathcal{A}^{\prime}$：模拟 $\mathcal{A}$，对 Mac 查询如实转发，记录 $\mathcal{Q}$；$\mathcal{A}$ 输出 $(m^*,t^*)$。$\mathcal{A}^{\prime}$ 输出 $(m^*,t^*)$。在 $\mathsf{Mac\text{-}forge}$ 中成功需 $m^*\notin\mathcal{Q}_m$（消息集合）且 $t^*$ 有效。

分析 $\mathcal{A}$ 成功（$(m^*,t^*)$ 有效且 $\notin\mathcal{Q}$）的两种情形：
- $m^*\notin\mathcal{Q}_m$：则 $\mathcal{A}^{\prime}$ 也成功（$m^*$ 新、$t^*$ 有效）。
- $m^*\in\mathcal{Q}_m$：即 $m^*$ 曾被 Mac 查询，返回 $(m^*,\mathsf{Mac}_k(m^*))\in\mathcal{Q}$。因 $\Pi$ 确定性，$\mathsf{Mac}_k(m^*)$ 唯一。$(m^*,t^*)\notin\mathcal{Q}$ 且有效 $\Rightarrow t^*=\mathsf{Mac}_k(m^*)$（规范验证）但 $(m^*,t^*)\ne(m^*,\mathsf{Mac}_k(m^*))$——矛盾（$t^*=\mathsf{Mac}_k(m^*)$ 即 $(m^*,t^*)=(m^*,\mathsf{Mac}_k(m^*))\in\mathcal{Q}$）。故此情形不可能。

因此 $\mathcal{A}$ 成功 $\Rightarrow m^*\notin\mathcal{Q}_m$ $\Rightarrow$ $\mathcal{A}^{\prime}$ 成功，$\varepsilon\le\Pr[\mathcal{A}^{\prime}\ \text{成功}]$，由 $\Pi$ 安全知可忽略。$\blacksquare$

---

## 习题 4.4　安全但非强安全的 MAC

> **题目**　假设安全 MAC 存在，证存在安全（4.2）但非强安全（4.3）的 MAC。

设 $\Pi^{\prime}=(\mathsf{Mac}^{\prime},\mathsf{Vrfy}^{\prime})$ 安全（消息长 $n$，标签 $\{0,1\}^n$）。构造 $\Pi$：标签空间 $\{0,1\}^n\cup\{0,1\}^{n-1}$（含短标签）。

- $\mathsf{Mac}_k(m)=\mathsf{Mac}^{\prime}_k(m)$（输出长 $n$）；
- $\mathsf{Vrfy}_k(m,t)=1\iff t=\mathsf{Mac}^{\prime}_k(m)$ **或** $t=\mathsf{Mac}^{\prime}_k(m)$ 的前 $n-1$ 位（即截断标签也接受）。

**安全（4.2）**：设 $\mathcal A$ 输出 $(m^*,t^*)$ 有效、$m^*\notin\mathcal{Q}$。构造攻 $\Pi^{\prime}$ 的 $\mathcal B$：模拟 $\mathcal A$（Mac 查询转发），当 $\mathcal A$ 输出 $(m^*,t^*)$ 时，若 $|t^*|=n$ 则 $\mathcal B$ 输出 $(m^*,t^*)$；若 $|t^*|=n-1$ 则 $\mathcal B$ 随机猜一位 $b$，输出 $(m^*,t^*\|b)$。$\mathcal A$ 成功时，要么 $t^*=\mathsf{Mac}^{\prime}_k(m^*)$（$\mathcal B$ 直接成功），要么 $t^*$ 是 $\mathsf{Mac}^{\prime}_k(m^*)$ 的前 $n-1$ 位（$\mathcal B$ 以 ${1}/{2}$ 概率补对最后一位而成功）。故 $\Pr[\mathcal B\ \text{成功}]\ge\tfrac12\Pr[\mathcal A\ \text{成功}]$，由 $\Pi^{\prime}$ 安全知 $\mathcal A$ 成功概率可忽略。

**非强安全（4.3）**：敌手 Mac 查询 $m_1$ 得 $t_1=\mathsf{Mac}^{\prime}_k(m_1)$（长 $n$）。输出 $(m_1,t_1[1..n-1])$（前 $n-1$ 位）：$\mathsf{Vrfy}_k(m_1,t_1[1..n-1])=1$（截断分支），且 $(m_1,t_1[1..n-1])\ne(m_1,t_1)\in\mathcal{Q}$（标签不同）。故是 $\mathsf{Mac\text{-}sforge}$ 成功，非强安全。$\blacksquare$

---

## 习题 4.5　双块 PRF-MAC 是否安全

> **题目**　消息 $m_0\|m_1$（各 $n-1$ 位），$\mathsf{Mac}_k(m)=F_k(0\|m_0)\|F_k(1\|m_1)$。是否安全？

**不安全（剪切拼接攻击）。** 标签的两半分别只绑定消息的一半，敌手可把两次查询的标签交叉重组：

1. 查询 $m^{(1)}=a\|b$，得 $t^{(1)}=F_k(0\|a)\|F_k(1\|b)$；
2. 查询 $m^{(2)}=c\|d$（$c\ne a,\ d\ne b$），得 $t^{(2)}=F_k(0\|c)\|F_k(1\|d)$；
3. 伪造 $m^*=a\|d$（$\ne m^{(1)},m^{(2)}$，故 $\notin\mathcal Q$），标签 $t^*=F_k(0\|a)\|F_k(1\|d)$，即 $t^{(1)}$ 的左半拼接 $t^{(2)}$ 的右半——两半都已知。

$\mathsf{Vrfy}_k(m^*,t^*)=1$ 恒成立，伪造成功概率 ${1}$。（前缀 ${0}/1$ 只防止前后两半互换，不防止**跨消息**重组。）$\blacksquare$

---

## 习题 4.6　几种不安全的 PRF-MAC（线性可重组）

> **题目**　$F$ 是 PRF。以下各 MAC 即使认证固定长度消息也不安全。

三者的共同弱点：tag 是若干 $F_k(\cdot)$ 值的**线性组合**，敌手可由若干次查询线性重组出一条新消息的有效 tag。

**(a) $t=F_k(m_1)\oplus\cdots\oplus F_k(m_\ell)$（$m_i\in\{0,1\}^n$）。** 查询单块消息 $m=a$ 得 $t_a=F_k(a)$；查询二块消息 $a\|b$ 得 $t_{ab}=F_k(a)\oplus F_k(b)$。于是 $F_k(b)=t_{ab}\oplus t_a$。伪造**单块**新消息 $b$（$b\notin\mathcal Q$），tag $=F_k(b)=t_{ab}\oplus t_a$。成功。

**(b) $t=F_k(\langle1\rangle\|m_1)\oplus\cdots\oplus F_k(\langle\ell\rangle\|m_\ell)$（$m_i$ 长 $n/2$）。** 即便固定 $\ell=2$ 也可破。取互异块 $a,b,c,d$，查询三条消息：
- $m^{(1)}=(a,b)$，得 $y_1=F_k(\langle1\rangle\|a)\oplus F_k(\langle2\rangle\|b)$；
- $m^{(2)}=(a,c)$，得 $y_2=F_k(\langle1\rangle\|a)\oplus F_k(\langle2\rangle\|c)$；
- $m^{(3)}=(d,b)$，得 $y_3=F_k(\langle1\rangle\|d)\oplus F_k(\langle2\rangle\|b)$。

由 $y_1\oplus y_2\oplus y_3$：$F_k(\langle1\rangle\|a)$ 与 $F_k(\langle2\rangle\|b)$ 各出现两次被抵消，剩下
$$y_1\oplus y_2\oplus y_3=F_k(\langle1\rangle\|d)\oplus F_k(\langle2\rangle\|c),$$
恰是新消息 $m^*=(d,c)$ 的 tag。$m^*\notin\{m^{(1)},m^{(2)},m^{(3)}\}$，伪造成功。（位置标签 $\langle i\rangle$ 仅绑定位置，线性结构仍允许跨消息重组。）

**(c) $t=F_k(r)\oplus F_k(\langle1\rangle\|m_1)\oplus\cdots$，tag 为 $\langle r,t\rangle$。** 敌手可**自选 $r$** 使 $F_k(r)$ 与某块抵消。对单块消息 $m^*$（$m^*\notin\mathcal Q$），取 $r^*=\langle1\rangle\|m^*$，则 $F_k(r^*)=F_k(\langle1\rangle\|m^*)$，二者在 $t$ 中相加相消，得 $t^*=0^n$。输出 $(m^*,\langle r^*,0^n\rangle)$：$\mathsf{Vrfy}$ 重算 $F_k(r^*)\oplus F_k(\langle1\rangle\|m^*)=0=t^*$，验证通过。伪造成功。$\blacksquare$

---

## 习题 4.7　$F_k(m_1)\|F_k(F_k(m_2))$ 不安全

> **题目**　消息 $m_1\|m_2$（各 $n$），tag $=F_k(m_1)\|F_k(F_k(m_2))$。

记 $a=F_k(0^n)$（待求）。攻击：

1. 查询 $m=0^n\|0^n$，得 tag $=F_k(0^n)\|F_k(F_k(0^n))=a\|F_k(a)$。故敌手同时学到 $a=F_k(0^n)$ 与 $b=F_k(a)$。

2. 伪造新消息 $m^*=a\|0^n$（即 $m_1^*=a,m_2^*=0^n$）。其 tag 应为
$$F_k(m_1^*)\|F_k(F_k(m_2^*))=F_k(a)\|F_k(F_k(0^n))=F_k(a)\|F_k(a)=b\|b.$$
$b=F_k(a)$ 已知，输出 $(a\|0^n,\,b\|b)$。

验证：$m^*=a\|0^n$ 与查询的 ${0}^n\|0^n$ 不同（$a=F_k(0^n)$ 以压倒概率 $\ne0^n$），故 $m^*\notin\mathcal Q$；tag $b\|b$ 由上式正确。伪造成功。$\blacksquare$

---

## 习题 4.8　安全确定 MAC 但 Mac 非 PRF

> **题目**　给安全、确定 MAC，使 $\mathsf{Mac}_k(\cdot)$ 不是 PRF。

取构造 4.5 的安全 MAC $\mathsf{Mac}_k(m)=F_k(m)$（$F$ PRF）——它是 PRF。要破坏 PRF 性质但保 MAC 安全：在标签末尾追加固定比特。定义 $\mathsf{Mac}_k(m)=F_k(m)\|0$（标签长 $n+1$）。$\mathsf{Vrfy}_k(m,t)=1\iff t=F_k(m)\|0$。

- **MAC 安全**：归约到构造 4.5（伪造等价于在 $F_k(m^*)$ 上猜中，多一位固定 ${0}$ 不增熵）。
- **非 PRF**：$\mathsf{Mac}_k(\cdot)$ 输出恒以 ${0}$ 结尾；区分器检测输出末位是否为 ${0}$：$\mathsf{Mac}_k$ 时概率 1，均匀 $f$（长 $n+1$）时概率 ${1}/{2}$。优势 ${1}/{2}$，非 PRF。$\blacksquare$

---

## 习题 4.9　构造 4.5 用弱 PRF 是否安全

> **题目**　构造 4.5（$\mathsf{Mac}_k(m)=F_k(m)$）用弱 PRF（习题 3.28）是否安全？

**否**。弱 PRF 仅在**均匀随机输入**点上伪随机，但 MAC 敌手可**自选消息** $m$ 查询 $\mathsf{Mac}_k(m)=F_k(m)$——即自选 $F_k$ 的输入点。构造 4.5 的安全性证明需 $F$ 在敌手自选点上伪随机（强 PRF），弱 PRF 不够。

具体反例：用习题 3.28(b) 的弱 PRF $F_k(x)=F^{\prime}_k(x)$（$x$ 偶）、$F^{\prime}_k(x+1)$（$x$ 奇）。敌手：

1. 查询奇数消息 $m=0^{n-1}1$，得 $t=F_k(m)=F^{\prime}_k(m+1)$；
2. 伪造 $m^*=m+1=0^{n-2}10$（偶数，$m^*\ne m$ 故 $\notin\mathcal{Q}$），标签 $t$。

$\mathsf{Vrfy}_k(m^*,t)=1$ 当且仅当 $F_k(m^*)=F^{\prime}_k(m^*)=F^{\prime}_k(m+1)\overset?=t$，恒成立。伪造成功概率 ${1}$，故构造 4.5 用弱 PRF 不必安全。$\blacksquare$

---

## 习题 4.10　构造 4.7 在带 Vrfy 预言机时仍安全

> **题目**　假设 $\Pi^{\prime}$ 安全且规范验证，证构造 4.7 在 4.1(a)（带 Vrfy）下安全。

构造 4.7 对每块 $m_i$ 用 $\Pi^{\prime}$ 认证块 $r\|\ell\|i\|m_i$。$\Pi^{\prime}$ 规范验证 + 确定（假设），由命题 4.4，$\Pi^{\prime}$ 强安全。

带 Vrfy 预言机的敌手 $\mathcal{A}$ 能对任意 $(m,t=\langle r,t_1,\ldots,t_d\rangle)$ 查询 $\mathsf{Vrfy}$。由构造，$\mathsf{Vrfy}_k(m,t)=1$ 当且仅当对所有 $i$，$\mathsf{Vrfy}^{\prime}_k(r\|\ell\|i\|m_i,t_i)=1$。每次成功的 Vrfy 查询实际上给敌手一组 $(r\|\ell\|i\|m_i,t_i)$ 有效对——相当于对 $\Pi^{\prime}$ 的额外 Mac 查询。归约：把这些 Vrfy 揭示的有效块加入 $\Pi^{\prime}$ 的查询集合 $\mathcal{Q}^{\prime}$。$\mathcal{A}$ 在新消息 $m^*$ 上伪造 $\Rightarrow$ 某 block $r^*\|\ell^*\|i^*\|m^*_i$ 未在 $\mathcal{Q}^{\prime}$ 中（由 $\ell,i,r$ 编码的"新性"论证，同定理 4.8）$\Rightarrow$ 对 $\Pi^{\prime}$ 的强安全伪造。故安全。$\blacksquare$

---

## 习题 4.11　构造 4.7 在 $\Pi^{\prime}$ 强安全时强安全

> **题目**　Prove that Construction 4.7 is strongly secure if $\Pi^{\prime}$ is strongly secure.
> **题目**　证明：如果 $\Pi^{\prime}$ 是强安全的，那么构造 4.7 是强安全的。

强安全（$\mathsf{Mac\text{-}sforge}$）允许伪造的 $(m^*,t^*)$ 是已查询消息上的**新标签**。构造 4.7 的标签含随机标识符 $r$，同一消息两次认证的 $r$ 几乎不同（$r$ 均匀 $n/4$ 比特，碰撞概率 $q^2/2^{n/4}$ 可忽略）。强安全伪造需 $(m^*,t^*)\notin\mathcal{Q}$ 有效。归约同定理 4.8，但用 $\Pi^{\prime}$ 的**强**安全：若 $r^*$ 与某查询的 $r_j$ 不同，则各 block 输入 $r^*\|\ell^*\|i\|m^*_i$ 全新，对 $\Pi^{\prime}$ 是新 (block,tag) 对；若 $r^*=r_j$（几乎不发生），由 $\Pi^{\prime}$ 强安全，$t^*_i$ 必等于已返回的 $t^{(j)}_i$，则 $t^*=t^{(j)}$，$(m^*,t^*)$ 是否 $\in\mathcal{Q}$ 取决于 $m^*=m^{(j)}$。综合得强安全。$\blacksquare$

---

## 习题 4.12　构造 4.7 的"末块标记位"修改

> **题目**　改 $t_i=F_k(r\|b\|i\|m_i)$，$b=0$（非末块）、$b=1$（末块）。证明安全，并问优势。

**安全性**：末块用 $b=1$、其余 $b=0$，使末块的认证输入与非末块严格区分。这阻止"删末块"或"在不同长度间移植块"的攻击。归约同定理 4.8（$\ell$ 已编码长度，$b$ 进一步标记位置类型）。

**优势**：编码 $b$ 用 1 比特，使接收方能区分"该块是否为最后一块"，从而**无需事先约定消息长度**即可安全认证变长消息（块 $b=1$ 标记结束）。这比原构造（需 $\ell$ 编码、长度上界 ${2}^{n/4}$）更灵活，且允许流式处理（发送方不需预先知道总长度，只要在最后一块设 $b=1$）。$\blacksquare$

---

## 习题 4.13　基本 CBC-MAC 用于不同长度

> **题目**　We explore what happens when the basic CBC-MAC construction is used with messages of different lengths.
> **题目**　我们探讨当基本 CBC-MAC 构造用于不同长度的消息时会发生什么。

**(a) 发送方只认证长 ${2}n$ 消息，接收方不限长度**。敌手查询 $m=m_1\|m_2$（长 ${2}n$）得 tag $t=F_k(F_k(m_1)\oplus m_2)$（$t_0=0^n,t_1=F_k(m_1),t_2=F_k(t_1\oplus m_2)$）。伪造长 ${4}n$ 消息 $m^*=m_1\|m_2\|m_3\|m_4$：选 $m_3=t$（即查询所得 tag）、$m_4$ 任意。计算 $m^*$ 的 CBC-MAC：$t_1=F_k(m_1),t_2=F_k(t_1\oplus m_2)=t,t_3=F_k(t_2\oplus m_3)=F_k(t\oplus t)=F_k(0^n),t_4=F_k(t_3\oplus m_4)$。需使 $t_4$ 已知：再查询 $m^{\prime}=0^n\|m_4$（长 ${2}n$）得 $t^{\prime}=F_k(F_k(0^n)\oplus m_4)=F_k(t_3\oplus m_4)=t_4$。故 $m^*=m_1\|m_2\|t\|m_4$ 的 tag $=t^{\prime}$（已知），伪造成功（$m^*$ 长 ${4}n\notin\mathcal{Q}$）。

**(b) 接收方只接受 3 块消息**（发送方可认证任意 $n$ 的倍数长）。敌手：

1. 查询 2 块消息 $m_1\|m_2$，得 $t=F_k(F_k(m_1)\oplus m_2)$；
2. 查询 1 块消息 ${0}^n$，得 $t_0=F_k(0^n)$；
3. 伪造 3 块消息 $m^*=m_1\|m_2\|t$（长度 ${3}n$ 且 $\notin\mathcal{Q}$），标签 $t_0$。

验证 $m^*$ 的 CBC 链：$t_1=F_k(m_1)$，$t_2=F_k(t_1\oplus m_2)=t$（第 1 步所查），$t_3=F_k(t_2\oplus t)=F_k(0^n)=t_0$（第 2 步所查）。故 $\mathsf{Mac}_k(m^*)=t_0$ 已知，伪造成功。$\blacksquare$

---

## 习题 4.14　CBC-MAC 的两种不安全修改

> **题目**　Prove that the following modifications of basic CBC-MAC do not yield a secure MAC (even for fixed-length messages):
> **题目**　证明以下对基本 CBC-MAC 的修改不能产生安全的 MAC（即使对于固定长度的消息）：

**(a) 输出所有 $t_1,\ldots,t_\ell$（Vrfy 只验 $t_\ell$）**：敌手查询 $m=m_1\|m_2$（2 块）得 $(t_1,t_2)=(F_k(m_1),F_k(F_k(m_1)\oplus m_2))$。由 $t_1=F_k(m_1)$ 已知，伪造消息 $m^*=m_1$（1 块）的 tag $=t_1$（已知），$m^*\notin\mathcal{Q}$，伪造成功（Vrfy 只验 $t_\ell=t_1$）。

**(b) 随机初始块 $t_0$**：$\mathsf{Mac}$ 输出 $\langle t_0,t_\ell\rangle$，$t_0$ 均匀，$t_i=F_k(t_{i-1}\oplus m_i)$。敌手查询 $m=m_1$（1 块）得 $\langle t_0,t_1\rangle$，$t_1=F_k(t_0\oplus m_1)$。敌手自选新 $t_0^{\prime}$，伪造 $m^*=t_0\oplus m_1\oplus t_0^{\prime}$（使 $t_0^{\prime}\oplus m^*=t_0\oplus m_1$）：则 $t_1^{\prime}=F_k(t_0^{\prime}\oplus m^*)=F_k(t_0\oplus m_1)=t_1$（已知）。输出 $\langle t_0^{\prime},t_1\rangle$ 对消息 $m^*$，$m^*\notin\mathcal{Q}$，伪造成功。$\blacksquare$

---

## 习题 4.15　末尾追加长度 + 基本 CBC-MAC 不安全

> **题目**　把 $|m|$ 追加到 $m$ 末尾再做基本 CBC-MAC，处理任意长消息。证明不安全。

记 $\mathsf{Tag}(m)=\mathsf{CBC}_k(m\|\langle|m|\rangle)$（$\langle|m|\rangle$ 为比特长度的 $n$ 比特编码）。不安全的原因：长度块在**末尾**，于是它可以被敌手当作**数据块**安插进另一条消息的中部，把两条独立消息的链"同步"到一起（mix-and-match）。

**攻击（4 次查询）。** 取两个不同的单块消息 $m,m^{\prime}$（$|m|=|m^{\prime}|=n$）：

1. 查询 $m$，得 $t=\mathsf{Tag}(m)=F_k(F_k(m)\oplus\langle n\rangle)$；
2. 查询 $m^{\prime}$，得 $t^{\prime}=F_k(F_k(m^{\prime})\oplus\langle n\rangle)$；
3. 查询 2 块消息 $m^{\prime}\|\langle n\rangle$：其 CBC 输入为 $m^{\prime}\|\langle n\rangle\|\langle 2n\rangle$，链为 $F_k(m^{\prime})\to t^{\prime}\to F_k(t^{\prime}\oplus\langle2n\rangle)$，故得 $u=F_k(t^{\prime}\oplus\langle2n\rangle)$；
4. 查询 3 块消息 $m^{\prime}\|\langle n\rangle\|\langle 2n\rangle$：链为 $F_k(m^{\prime})\to t^{\prime}\to u\to F_k(u\oplus\langle3n\rangle)$，故得 $v=F_k(u\oplus\langle3n\rangle)$。

**伪造**：$m^*=m\,\|\,\langle n\rangle\,\|\,(t\oplus t^{\prime}\oplus\langle2n\rangle)$（3 块），标签 $v$。验证 $m^*$ 的 CBC 链（输入 $m\|\langle n\rangle\|(t\oplus t^{\prime}\oplus\langle2n\rangle)\|\langle3n\rangle$）：

- $z_1=F_k(m)$；
- $z_2=F_k(z_1\oplus\langle n\rangle)=t$（即第 1 步的 $t$）；
- $z_3=F_k(z_2\oplus(t\oplus t^{\prime}\oplus\langle2n\rangle))=F_k(t^{\prime}\oplus\langle2n\rangle)=u$（即第 3 步的 $u$）；
- $z_4=F_k(z_3\oplus\langle3n\rangle)=F_k(u\oplus\langle3n\rangle)=v$（即第 4 步的 $v$）。

故 $\mathsf{Tag}(m^*)=v$ 已知。$m^*\notin\mathcal{Q}$（首块为 $m\ne m^{\prime}$，与 4 次查询的消息均不同），伪造成功概率 ${1}$。

**对比**：把长度**前置**（4.4.2 节）则编码前缀自由，攻击失效；末尾追加使"长度块"可被挪作数据块，是病根。$\blacksquare$

---

## 习题 4.16　零填充至定长 $\ell\cdot2^n$ 再 CBC-MAC

> **题目**　消息 $m$（长 $\le\ell\cdot2^n$）零填充至恰 $\ell\cdot2^n$，再基本 CBC-MAC。是否安全？

**不安全**（长度信息丢失）。两个不同长度消息 $m,m^{\prime}$ 若零填充后**相同**，则 CBC-MAC 相同。例如 $m=0$ 与 $m^{\prime}=00$（均零填充为全零）有相同 tag。敌手查询 $m$ 得 $t$，伪造 $m^{\prime}$（$m^{\prime}\ne m$ 但填充后相同）的 tag $=t$，$m^{\prime}\notin\mathcal{Q}$，伪造成功。**零填充丢失长度 $\Rightarrow$ 碰撞**。$\blacksquare$

---

## 习题 4.17　某编码非前缀自由

> **题目**　编码：$m$ 追加 0 至非零 $n$ 倍数得 $\hat m$，再前置 $|\hat m|/n$（块数，$n$ 比特编码）。证其非前缀自由。

按定义（§4.4.2），编码 $\mathsf{encode}$ 前缀自由指：对任意 $m_1\ne m_2$，$\mathsf{encode}(m_1)$ 不是 $\mathsf{encode}(m_2)$ 的前缀。由于任何串都是**自身**的前缀，这首先要求编码单射。

**该编码不单射。** 取长度非 $n$ 倍数的消息 $m$，令 $m^{\prime}=m\|0$（$m^{\prime}\ne m$）。补 0 只是继续追加 0，故 $m$ 与 $m^{\prime}$ 补齐到"非零 $n$ 倍数"后得到**同一个** $\hat m$，块数自然也相同：

$$\mathsf{encode}(m)=\langle|\hat m|/n\rangle\,\|\,\hat m=\mathsf{encode}(m^{\prime}).$$

例如 $n=4$ 时 $m=0$ 与 $m^{\prime}=00$ 的编码都是 $\langle1\rangle\|0000$。于是 $\mathsf{encode}(m)$（自身）是 $\mathsf{encode}(m^{\prime})$ 的前缀，违反前缀自由定义。

**根源**：前置的是**块数**而非比特长度，补 0 的数量被丢弃，消息无法从编码唯一还原。（对比习题 4.18：前置比特长度 $|m|$，编码单射且前缀自由。）$\blacksquare$

---

## 习题 4.18　4.4.2 节的变长编码是前缀自由

> **题目**　证 4.4.2 节描述的变长编码（前置长度）前缀自由。

4.4.2 节编码：对消息 $m$（长 $<n\cdot2^n$），前置 $|m|$（$n$ 比特编码），再按需补 0 至 $n$ 倍数。即编码 $\mathsf{enc}(m)=\langle|m|\rangle\|m\|0^*$（补零至 $n$ 倍数）。

**前缀自由**：设 $\mathsf{enc}(m)$ 是 $\mathsf{enc}(m^{\prime})$ 的前缀。两者都以 $n$ 比特长度域开头：$\langle|m|\rangle$ 与 $\langle|m^{\prime}|\rangle$。若 $\mathsf{enc}(m)$ 是 $\mathsf{enc}(m^{\prime})$ 前缀，则前 $n$ 比特相同 $\Rightarrow |m|=|m^{\prime}|$。长度相同后，数据域 $m$ 与 $m^{\prime}$ 长度相同（均 $|m|$），补零也相同。故 $\mathsf{enc}(m)=\mathsf{enc}(m^{\prime})$，$m=m^{\prime}$。不存在真前缀关系。$\blacksquare$

---

## 习题 4.19　按长度派生子密钥的 CBC-MAC 安全

> **题目**　$\mathsf{Mac}_k(m)$：先算 $k_\ell=F_k(\ell)$（$\ell=|m|$），再用基本 CBC-MAC 以"密钥"$k_\ell$。证安全。

对不同长度 $\ell$，使用不同子密钥 $k_\ell=F_k(\ell)$，相当于各长度独立 MAC。归约：$F$ PRF $\Rightarrow$ 各 $k_\ell$ 伪独立。具体：换 $F_k$ 为均匀 $f$，则 $k_\ell=f(\ell)$ 在不同 $\ell$ 上独立均匀，各长度 CBC-MAC 独立（用定理 4.10/4.13 的固定长度安全性）。敌手在长度 $\ell^*$ 上伪造需破"以均匀 $k_{\ell^*}$ 为密钥的基本 CBC-MAC"，由基本 CBC-MAC 固定长度安全知不可。$F$ PRF 使 $f$ 与 $F_k$ 不可区分。故任意长安全。$\blacksquare$

---

## 习题 4.20　基本 CBC-MAC 用"安全 MAC 但非 PRF"未必安全

> **题目**　$F$ 是长度 $n$ 消息的安全确定 MAC（未必 PRF）。基本 CBC-MAC 用 $F$ 是否安全？

**否**。$F$ 仅 MAC 安全（抗新消息伪造），但 CBC-MAC 的迭代结构 $t_i=F_k(t_{i-1}\oplus m_i)$ 把 $F$ 当**函数**用，需 PRF 性质。反例：取 $F_k$ 为某安全 MAC 但 $F_k(0^n)=0^n$（固定点）。则 CBC-MAC 对消息 $m=0^n\|0^n$：$t_1=F_k(0^n)=0^n$，$t_2=F_k(0^n\oplus0^n)=F_k(0^n)=0^n$。对 $m^{\prime}=0^n$（单块）：$t=F_k(0^n)=0^n$。故 $m,m^{\prime}$ 同 tag ${0}^n$。敌手查询 $m=0^n$ 得 ${0}^n$，伪造 $m^{\prime}=0^n\|0^n$（新消息）tag ${0}^n$。

需构造 $F_k$ 既是安全 MAC 又满足 $F_k(0^n)=0^n$：取安全 MAC $F^{\prime}$（PRF 型），定义 $F_k(x)=0^n$（$x=0^n$），否则 $F^{\prime}_k(x)$。$F$ 仍是 MAC 安全（固定点 ${0}^n$ 单点不破坏新消息伪造抵抗力，因敌手已知 $F_k(0^n)=0^n$ 但 ${0}^n\in\mathcal{Q}$；新消息 $x\ne0^n$ 上归约 $F^{\prime}$）。但 CBC-MAC 用 $F$ 因固定点产生碰撞，不安全。$\blacksquare$

---

## 习题 4.21　GMAC/Poly1305 中 nonce 复用导致伪造

> **题目**　同一 nonce $r$ 认证两条不同消息，构造高概率伪造。

GMAC/Poly1305 基于差分通用函数 $h_k(m)=m(k)$（多项式求值），标签 $t=h_k(m)+\mathsf{Enc}_k(r)$（$r$ 为 nonce）。两条消息 $m,m^{\prime}$ 用同 $r$ 得 $t=h_k(m)+\mathsf{Enc}_k(r)$、$t^{\prime}=h_k(m^{\prime})+\mathsf{Enc}_k(r)$。敌手已知 $(m,t),(m^{\prime},t^{\prime})$（来自 Mac 预言机），则 $t-t^{\prime}=h_k(m)-h_k(m^{\prime})=m(k)-m^{\prime}(k)=(m-m^{\prime})(k)$。$m-m^{\prime}$ 是次数 $<\ell$ 的非零多项式（因 $m\ne m^{\prime}$），故 $k$ 可由 $t-t^{\prime}$ 与 $m-m^{\prime}$ 求出（在域上解 $(m-m^{\prime})(X)=t-t^{\prime}$，至多 $\ell$ 个根，但 $m-m^{\prime}$ 次数 $<\ell$ 且最高次系数非零 $\Rightarrow$ 至多 $\ell-1$ 个根）。

**直接伪造**（不需恢复 $k$）：对任意新消息 $m^*$，敌手需 $t^*=h_k(m^*)+\mathsf{Enc}_k(r)$。已知 $\mathsf{Enc}_k(r)=t-h_k(m)=t-m(k)$。敌手知 $t,m$，但不知 $k$。然而由 $t-t^{\prime}=(m-m^{\prime})(k)$ 可解 $k$（若 $m-m^{\prime}$ 次数 1，即 $m,m^{\prime}$ 长度相关使 $m-m^{\prime}$ 线性）：取 $m,m^{\prime}$ 单块（长度 1），$m(X)=m_1 X+m_2$（$m_2$ 编码长度），$m-m^{\prime}=(m_1-m^{\prime}_1)X+(m_2-m^{\prime}_2)$。若长度同则 $m_2=m^{\prime}_2$，$m-m^{\prime}=(m_1-m^{\prime}_1)X$，$(m-m^{\prime})(k)=(m_1-m^{\prime}_1)k=t-t^{\prime}$ $\Rightarrow k=(t-t^{\prime})/(m_1-m^{\prime}_1)$（$m_1\ne m^{\prime}_1$）。**敌手恢复 $k$**！然后用 $k$ 计算任意 $m^*$ 的 $h_k(m^*)$，加 $\mathsf{Enc}_k(r)=t-h_k(m)$ 得 $t^*$，伪造任意新消息。成功概率 1（单块、同长、$m_1\ne m^{\prime}_1$）。$\blacksquare$

---

## 习题 4.22　判断三种函数是否 $\ell/|\mathbb{F}|$-差分通用

> **题目**　Prove or disprove whether the following functions are $\ell/|\mathbb{F}|$-difference universal. In each case assume $\mathcal{K} = \mathbb{F}$ and $\mathcal{M} = \mathbb{F}^{<\ell}$, and for a message $m = (m_1, \ldots, m_{\ell^{\prime} - 1})$ let $m_{\ell^{\prime}} \in \mathbb{F}$ be an encoding of $\ell^{\prime} - 1$.
> **题目**　证明或反驳以下函数是否为 $\ell/|\mathbb{F}|$-差分通用的。在每种情况下假设 $\mathcal{K} = \mathbb{F}$、$\mathcal{M} = \mathbb{F}^{<\ell}$，并且对消息 $m = (m_1, \ldots, m_{\ell^{\prime} - 1})$，令 $m_{\ell^{\prime}} \in \mathbb{F}$ 是 $\ell^{\prime} - 1$ 的编码。

回忆：$h$ 是 $\varepsilon$-DU 若对任意不同 $m,m^{\prime}$ 与任意 $\Delta$，$\Pr_k[h_k(m)-h_k(m^{\prime})=\Delta]\le\varepsilon$。此处 $k\leftarrow\mathbb{F}$，$h_k(m)$ 是某多项式在 $k$ 处求值。

**(a) $h^{\prime}_k(m)=m^{\prime}(k)$，$m^{\prime}(X)=m_1X^\ell+m_2X^{\ell-1}+\cdots+m_{\ell^{\prime}}X^{\ell-\ell^{\prime}+1}$**（固定高次 $\ell$，长度 $\ell^{\prime}$ 决定最低次）。$h^{\prime}_k(m)-h^{\prime}_k(m^{\prime})-\Delta=(m^{\prime}-m^{\prime\prime}-\Delta)(k)$ 是次数 $\le\ell$ 多项式。若 $m\ne m^{\prime}$，$m^{\prime}-m^{\prime\prime}$ 非零多项式（次数 $\le\ell$），故 $m^{\prime}-m^{\prime\prime}-\Delta$ 次数 $\le\ell$，至多 $\ell$ 个根 $\Rightarrow \Pr[\cdot=\Delta]\le\ell/|\mathbb{F}|$。**是 $\ell/|\mathbb{F}|$-DU**。

**(b) $h^{\prime\prime}_k(m)=m^{\prime\prime}(k)$，$m^{\prime\prime}(X)=m_1X^{\ell^{\prime}-1}+\cdots+m_{\ell^{\prime}}$**（次数随长度 $\ell^{\prime}-1$ 变）。**不是 $\ell/|\mathbb{F}|$-DU**。反例：取 $m,m^{\prime}$ 长度不同使 $m^{\prime\prime}-m^{\prime\prime\prime}$ 为**零多项式**。如 $m=(a)$（$\ell^{\prime}=1$，$m^{\prime\prime}=m_1=a$ 常数）、$m^{\prime}=(b)$（$m^{\prime\prime\prime}=b$），$m^{\prime\prime}-m^{\prime\prime\prime}=a-b$。若 $a=b$ 则 $m=m^{\prime}$（排除）。取 $m=(a)$、$m^{\prime}=(a,a)$（$\ell^{\prime}=2$，$m^{\prime\prime\prime}=aX+a$）：$m^{\prime\prime}-m^{\prime\prime\prime}=a-(aX+a)=-aX$，次数 1，根 1 个 $\Rightarrow$ 对 $\Delta=0$，$\Pr[-ak=0]=1/|\mathbb{F}|$（若 $a\ne0$），$\le\ell/|\mathbb{F}|$。看似 OK。但取 $m,m^{\prime}$ 使 $m^{\prime\prime}=m^{\prime\prime\prime}$：$m=(a)$（$m^{\prime\prime}=a$）、$m^{\prime}=(0,a)$（$\ell^{\prime}=2$，$m^{\prime\prime\prime}=0\cdot X+a=a$）。$m^{\prime\prime}=m^{\prime\prime\prime}=a$！则 $h^{\prime\prime}_k(m)=h^{\prime\prime}_k(m^{\prime})$ 对所有 $k$，$\Pr[h^{\prime\prime}_k(m)-h^{\prime\prime}_k(m^{\prime})=0]=1\gg\ell/|\mathbb{F}|$。**不是** $\ell/|\mathbb{F}|$-DU（长度未在多项式中编码，不同长度可产生相同多项式）。

**(c) $h^{\prime\prime\prime}_k(m)=m^{\prime\prime\prime}(k)$，$m^{\prime\prime\prime}(X)=m_1X+\cdots+m_{\ell^{\prime}}X^{\ell^{\prime}}$**（无常数项，最高次体现长度）。**不是** $\ell/|\mathbb{F}|$-DU：取 $m=(0)$（$\ell^{\prime}=1$，$m^{\prime\prime\prime}(X)=0\cdot X=0$，零多项式）与 $m^{\prime}=(0,0)$（$\ell^{\prime}=2$，$m^{\prime\prime\prime\prime}(X)=0$，同为零多项式）。两者多项式相同（皆为零），故 $h^{\prime\prime\prime}_k(m)=h^{\prime\prime\prime}_k(m^{\prime})=0$ 对所有 $k$ 成立，$\Pr[h^{\prime\prime\prime}_k(m)-h^{\prime\prime\prime}_k(m^{\prime})=0]=1\gg\ell/|\mathbb{F}|$。全零消息使多项式退化为零，不同长度产生相同零多项式，DU 失败。$\blacksquare$

---

## 习题 4.23　多项式 DU 函数非强通用

> **题目**　证 4.5.2 节多项式 $h_k(m)=m(k)$ 不是强通用。

强通用要求：对任意不同 $m,m^{\prime}$ 与任意 $t,t^{\prime}$，$\Pr_k[h_k(m)=t\land h_k(m^{\prime})=t^{\prime}]=1/|\mathcal{T}|^2$。

取 $m,m^{\prime}$ 使 $m(k),m^{\prime}(k)$ **相关**。例：$\mathbb{F}$ 任取，$m=(1)$（$\ell^{\prime}=1$，$m(X)=1\cdot X+m_2$，$m_2$ 编码长度 ${0}$），$m^{\prime}=(2)$（$m^{\prime}(X)=2X+m_2$）。则 $m(k)=k+c,m^{\prime}(k)=2k+c$（$c=m_2$）。给定 $h_k(m)=t$ 即 $k=t-c$，则 $h_k(m^{\prime})=2(t-c)+c=2t-c$ **完全确定**。故 $\Pr[h_k(m^{\prime})=t^{\prime}\mid h_k(m)=t]=\begin{cases}1,&t^{\prime}=2t-c\\0,&\text{否则}\end{cases}$，**不等于** ${1}/{|\mathbb{F}|}$。非强通用。$\blacksquare$

---

## 习题 4.24　$h_{k_0,\ldots,k_\ell}(m)=k_0+\sum_i k_im_i$ 强通用

> **题目**　$\mathcal{K}=\mathbb{Z}_p^{\ell+1},\mathcal{M}=\mathbb{Z}_p^\ell,\mathcal{T}=\mathbb{Z}_p$。

强通用：对任意不同 $m,m^{\prime}\in\mathbb{Z}_p^\ell$、任意 $t,t^{\prime}\in\mathbb{Z}_p$，证 $\Pr[k_0+\sum k_im_i=t\ \land\ k_0+\sum k_im^{\prime}_i=t^{\prime}]=1/p^2$。

这是关于未知量 $k_0,k_1,\ldots,k_\ell$（均匀于 $\mathbb{Z}_p$）的线性方程组：

$$\begin{cases}k_0+\sum_i k_im_i=t,\\ k_0+\sum_i k_im^{\prime}_i=t^{\prime}.\end{cases}$$

两式相减：$\sum_i k_i(m_i-m^{\prime}_i)=t-t^{\prime}$。因 $m\ne m^{\prime}$，存在 $j$ 使 $m_j\ne m^{\prime}_j$，即 $m_j-m^{\prime}_j\ne0$，该方程可解出 $k_j=(t-t^{\prime}-\sum_{i\ne j}k_i(m_i-m^{\prime}_i))/(m_j-m^{\prime}_i)$（对任意固定其余 $k_i$ 有唯一解）。一旦 $k_1,\ldots,k_\ell$ 固定（满足此方程），第一式唯一确定 $k_0=t-\sum k_im_i$。故对任意 $t,t^{\prime}$，满足两方程的 $(k_0,\ldots,k_\ell)$ 数目 $=p^{\ell-1}$（自由 $k_i$，$i\ne j$，共 $\ell-1$ 个，$k_j,k_0$ 被唯一确定）。密钥总数 $p^{\ell+1}$，故概率 $p^{\ell-1}/p^{\ell+1}=1/p^2=1/|\mathcal{T}|^2$。强通用。$\blacksquare$

---

## 习题 4.25　$h_{K,v}(m)=Km\oplus v$（布尔）强通用

> **题目**　$K$ 为 $\ell\times n$ 布尔矩阵，$v$ 为 $\ell$ 维向量，$m\in\{0,1\}^n$，模 2。

强通用：对任意不同 $m,m^{\prime}\in\{0,1\}^n$、任意 $t,t^{\prime}\in\{0,1\}^\ell$，证 $\Pr[Km\oplus v=t\ \land\ Km^{\prime}\oplus v=t^{\prime}]=2^{-2\ell}$。

由 $Km\oplus v=t$、$Km^{\prime}\oplus v=t^{\prime}$ 相减（异或）：$K(m\oplus m^{\prime})=t\oplus t^{\prime}$。$m\ne m^{\prime}$ $\Rightarrow$ $m\oplus m^{\prime}\ne0$，设其第 $j$ 位为 1。$K(m\oplus m^{\prime})$ 的第 $i$ 行 $=\sum_l K_{il}(m\oplus m^{\prime})_l=\ K$ 第 $i$ 行与 $m\oplus m^{\prime}$ 的内积。因 $(m\oplus m^{\prime})_j=1$，对每行 $i$，固定 $K$ 中除第 $j$ 列外的元素后，$K_{ij}$ 唯一确定（使第 $i$ 行内积 $=(t\oplus t^{\prime})_i$）。故 $K$ 的第 $j$ 列（$\ell$ 比特）被唯一确定，其余 $(\ell-1)\cdot n+\ ... $ 自由。再由 $Km\oplus v=t$ 唯一确定 $v=t\oplus Km$。

满足两方程的 $(K,v)$ 数目：$K$ 自由度 $(\ell\times n)-\ell$（第 $j$ 列 $\ell$ 比特被定）$=\ell n-\ell$，$v$ 被唯一确定（0 自由）。总数 ${2}^{\ell n-\ell}$。密钥总数 ${2}^{\ell n}\cdot2^\ell={2}^{\ell n+\ell}$。概率 ${2}^{\ell n-\ell}/{2}^{\ell n+\ell}={2}^{-2\ell}={1}/{|\mathcal{T}|^2}$。强通用。$\blacksquare$

---

## 习题 4.26　Toeplitz 矩阵版本强通用

> **题目**　$K$ 为 $\ell\times n$ Toeplitz 矩阵（对角线常数），$h_{K,v}(m)=Km\oplus v$。

强通用证明同 4.25，关键是 $K(m\oplus m^{\prime})=t\oplus t^{\prime}$ 给 $\ell$ 个线性方程，未知为 Toeplitz 矩阵的 $\ell+n-1$ 个对角参数 $K_n,K_{n+1},\ldots,K_{n+\ell-1}$。$K(m\oplus m^{\prime})$ 的第 $i$ 行 $=\sum_j K_{i,j}(m\oplus m^{\prime})_j=\sum_j K_{n+i-j}(m\oplus m^{\prime})_j$（用 Toeplitz $K_{i,j}=K_{n+i-j}$ 的重新指标，取决于矩阵形式）。这是关于 $K_n,\ldots,K_{n+\ell-1}$ 的线性方程。因 $m\oplus m^{\prime}\ne0$，方程组秩 $\ell$（可证系数矩阵满秩），唯一确定 $\ell$ 个参数；其余 $n-1$ 个 Toeplitz 参数自由。再由 $Km\oplus v=t$ 唯一确定 $v$。

满足方程的密钥数：Toeplitz 参数 $(\ell+n-1)-\ell+n\to$ 自由 $(n-1)$ 个，$v$ 0 自由 $\Rightarrow$ ${2}^{n-1}$。密钥总数 ${2}^{\ell+n-1}\cdot2^\ell$。概率 ${2}^{n-1}/{2}^{\ell+n-1+\ell}={2}^{-2\ell}={1}/{|\mathcal{T}|^2}$。强通用。

**优势**：Toeplitz 矩阵仅 $\ell+n-1$ 个参数（vs 一般矩阵 $\ell n$ 个），**密钥更短**（$O(\ell+n)$ vs $O(\ell n)$），认证开销更低。$\blacksquare$

---

## 习题 4.27　两次 MAC（two-time MAC）的定义与构造

> **题目**　Define an appropriate notion of a $\varepsilon$-secure two-time MAC, and give a construction that meets your definition.
> **题目**　定义 $\varepsilon$-安全的两次 MAC 的适当概念，并给出满足你定义的构造。

**定义**（$\varepsilon$-安全两次 MAC）：MAC $\Pi$ 是 $\varepsilon$-安全的两次 MAC，若对任何（不必多项式有界的）敌手 $\mathcal{A}$：$\mathcal{A}$ 可自适应查询 $\mathsf{Mac}_k(\cdot)$ **至多两次**，得 $(m_1,t_1),(m_2,t_2)$，然后输出 $(m^*,t^*)$ 且 $m^*\notin\{m_1,m_2\}$，都有 $\Pr[\mathsf{Vrfy}_k(m^*,t^*)=1]\le\varepsilon$。

**注意**：习题 4.24 的强通用函数 $h(m)=k_0+\sum_i k_im_i$ 只能当**一次** MAC 用——它是仿射的：敌手查询 $m_1,m_2$ 得 $t_1,t_2$ 后，对 $m^*=2m_1-m_2\ (\mathrm{mod}\ p)$ 可直接算出 $h(m^*)=k_0+\sum k_i(2m_{1,i}-m_{2,i})=2t_1-t_2$，伪造成功。两次安全需要**三点独立**（给定两点的求值后，第三点的求值仍均匀），二次多项式恰好提供。

**构造（二次多项式 MAC）**。取素数 $p$（$n$ 比特），消息空间 $\mathbb{Z}_p$，密钥 $(k_0,k_1,k_2)\leftarrow\mathbb{Z}_p^3$ 均匀，

$$\mathsf{Mac}_{k_0,k_1,k_2}(m)=k_0+k_1m+k_2m^2\bmod p,$$

验证算法重算比较。

**安全性**：$\varepsilon=1/p$。固定任意互异的 $m_1,m_2,m^*\in\mathbb{Z}_p$ 与任意 $t_1,t_2,t^*$。关于未知量 $k_0,k_1,k_2$ 的三个方程

$$k_0+k_1m_i+k_2m_i^2=t_i\ (i=1,2),\qquad k_0+k_1m^*+k_2(m^*)^2=t^*$$

的系数矩阵是 Vandermonde 矩阵，行列式 $(m_2-m_1)(m^*-m_1)(m^*-m_2)\not\equiv0\pmod p$，故对每组 $(t_1,t_2,t^*)$ 恰有**唯一**密钥满足全部三式。于是

$$\Pr[h(m^*)=t^*\mid h(m_1)=t_1\land h(m_2)=t_2]=\frac{1}{p},$$

即给定两次标签后，任意新消息的标签在敌手看来仍均匀于 $\mathbb{Z}_p$，伪造（猜中）概率 ${1}/p$。故该构造是 $\tfrac1p$-安全的两次 MAC。（推广到 $\ell$ 次查询：用 $\ell$ 次多项式 $k_0+\sum_{j=1}^{\ell}k_jm^j$，同理 Vandermonde 给出 $\varepsilon=1/p$；与 4.6.3 节的下界 $\varepsilon\ge 1/\sqrt[\ell+1]{|\mathcal K|}$ 相洽。）$\blacksquare$
