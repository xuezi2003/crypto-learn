# 第六章　习题解答

> *Introduction to Modern Cryptography (3rd ed.), Katz & Lindell — Chapter 6 Exercises*

---

## 习题 6.1　第二原像抗性、原像抗性的定义与蕴含

> **题目**　(a) 给出第二原像抗性 (SPR) 与原像抗性 (PR) 的形式化定义；(b)(a) CR $\Rightarrow$ SPR；(b) 压缩函数（${2}n\to n$）SPR $\Rightarrow$ PR。

**(a) 定义**（基于碰撞实验 $\mathsf{Hash\text{-}coll}$ 的变体）：

- **SPR 实验** $\mathsf{Hash\text{-}secpre}_{\mathcal{A},\mathcal{H}}(n)$：均匀 $s\leftarrow\mathsf{Gen}(1^n)$ 与均匀 $x\leftarrow\{0,1\}^{\ell^{\prime}(n)}$；$\mathcal{A}(s,x)$ 输出 $x^{\prime}$；成功当 $x^{\prime}\ne x$ 且 $H^s(x^{\prime})=H^s(x)$。$\mathcal{H}$ 是 SPR 若对所有 PPT $\mathcal{A}$ 成功概率可忽略。
- **PR 实验** $\mathsf{Hash\text{-}pre}_{\mathcal{A},\mathcal{H}}(n)$：均匀 $s\leftarrow\mathsf{Gen}(1^n)$ 与均匀 $x\leftarrow\{0,1\}^{\ell^{\prime}(n)}$，令 $y=H^s(x)$；$\mathcal{A}(s,y)$ 输出 $x^{\prime}$；成功当 $H^s(x^{\prime})=y$。$\mathcal{H}$ 是 PR 若成功概率可忽略。

**(b)(a) CR $\Rightarrow$ SPR**。设 $\mathcal{A}$ 以概率 $\varepsilon$ 攻破 SPR（给定 $s,x$ 输出 $x^{\prime}\ne x$ 使 $H^s(x^{\prime})=H^s(x)$）。构造 CR 攻击者 $\mathcal{A}^{\prime}$：收到 $s$，自选均匀 $x\leftarrow\{0,1\}^{\ell^{\prime}}$，运行 $\mathcal{A}(s,x)$ 得 $x^{\prime}$，输出 $(x,x^{\prime})$。$x^{\prime}\ne x$ 且 $H^s(x^{\prime})=H^s(x)$，即找到碰撞，成功概率 $\varepsilon$。CR $\Rightarrow\varepsilon$ 可忽略 $\Rightarrow$ SPR。

**(b)(b) 压缩函数 ${2}n\to n$ 的 SPR $\Rightarrow$ PR**。设 $\mathcal{A}$ 以概率 $\varepsilon$ 攻破 PR（给定 $s,y=H^s(x)$ 输出 $x^{\prime}$ 使 $H^s(x^{\prime})=y$）。构造 SPR 攻击者 $\mathcal{A}^{\prime}$：收到 $(s,x)$（$x$ 均匀），计算 $y=H^s(x)$，运行 $\mathcal{A}(s,y)$ 得 $x^{\prime}$。若 $x^{\prime}\ne x$ 则 $(x,x^{\prime})$ 是第二原像（$H^s(x^{\prime})=y=H^s(x)$）。

关键是 $\Pr[x^{\prime}=x\ \text{且}\ \mathcal{A}\ \text{成功}]$ 可忽略：不妨设 $\mathcal{A}$ 确定（固定其随机带最优值），对固定的 $s$ 与每个可能的像 $y$，$\mathcal{A}(s,y)$ 是**唯一**确定的值 $x^{\prime}_y$；事件"$x^{\prime}=x$"要求 $x=x^{\prime}_y$ 且 $H^s(x)=y$，即 $x$ 取遍 $\{x^{\prime}_y:\ H^s(x^{\prime}_y)=y\}$——至多 ${2}^n$ 个值（每个 $y$ 贡献至多一个）。均匀 $x$ 落入该集合的概率 $\le 2^n/2^{2n}=2^{-n}$。故

$$\Pr[\mathcal{A}^{\prime}\ \text{成功}]\ge\varepsilon(n)-2^{-n},$$

SPR $\Rightarrow\varepsilon$ 可忽略 $\Rightarrow$ PR。（压缩性不可少：正是定义域 ${2}^{2n}$ 远大于值域 ${2}^n$ 才使"恰撞上挑战 $x$ 本身"可忽略。）$\blacksquare$

---

## 习题 6.2　$H^{s_1,s_2}(x)=H_1^{s_1}(x)\|H_2^{s_2}(x)$

> **题目**　(a) 至少一个 CR $\Rightarrow$ CR；(b) SPR/PR 是否类似？

**(a) CR**。设 $H_1$ 是 CR（$H_2$ 任意）。若 $\mathcal{A}$ 找到 $H$ 的碰撞 $(x,x^{\prime})$：$H_1^{s_1}(x)\|H_2^{s_2}(x)=H_1^{s_1}(x^{\prime})\|H_2^{s_2}(x^{\prime})$ $\Rightarrow$ $H_1^{s_1}(x)=H_1^{s_1}(x^{\prime})$ **且** $H_2^{s_2}(x)=H_2^{s_2}(x^{\prime})$。前者即 $H_1$ 的碰撞（$x\ne x^{\prime}$）。故 $H$ 的碰撞给出 $H_1$（或 $H_2$）的碰撞。若两者都 CR，则 $H$ CR（归约：碰撞必然在某一分量上构成碰撞，但敌手不知哪个；任取 $H_1$ 归约，碰撞 $\Rightarrow H_1$ 碰撞，成功概率即 $H$ 碰撞概率）。**至少一个 CR 即 $H$ CR**。

**(b) SPR/PR 是否类似？**

- **SPR：类似成立**（只要 $H_1,H_2$ 之一 SPR，$H$ 就 SPR）。设 $H_1$ 是 SPR。归约：$\mathcal{B}$ 攻 $H_1$ 的 SPR，收到 $(s_1,x)$（$x$ 均匀）；$\mathcal{B}$ 自行运行 $\mathsf{Gen}_2$ 得 $s_2$，把 $((s_1,s_2),x)$ 交给 $H$ 的 SPR 敌手 $\mathcal{A}$——分布与真实实验一致。$\mathcal{A}$ 输出 $x^{\prime}\ne x$ 使 $H^{s_1,s_2}(x^{\prime})=H^{s_1,s_2}(x)$，特别地 $H_1^{s_1}(x^{\prime})=H_1^{s_1}(x)$，$\mathcal{B}$ 输出 $x^{\prime}$ 即成功。成功概率 $=\mathcal{A}$ 的成功概率，故可忽略。

- **PR：不类似。** 反例：设 $G$ 是原像抗性的哈希函数（$G^s:\{0,1\}^n\to\{0,1\}^n$）。对 $x=x_L\|x_R\in\{0,1\}^{2n}$（$|x_L|=|x_R|=n$）定义

$$H_1^{s_1}(x)=G^{s_1}(x_R)\|x_L,\qquad H_2^{s_2}(x)=G^{s_2}(x_L)\|x_R.$$

$H_1$ 原像抗性：归约到 $G$——$\mathcal{B}$ 收到 $(s_1,g)$（$g=G^{s_1}(x_R)$，$x_R$ 均匀），自选均匀 $x_L$，把 $g\|x_L$ 交给 $H_1$ 的原像敌手 $\mathcal{A}$（分布与真实挑战一致）；$\mathcal{A}$ 输出 $x^{\prime}_L\|x^{\prime}_R$ 满足 $G^{s_1}(x^{\prime}_R)\|x^{\prime}_L=g\|x_L$，$\mathcal{B}$ 输出 $x^{\prime}_R$ 即得 $g$ 的原像。$H_2$ 同理。但

$$H^{s_1,s_2}(x)=G^{s_1}(x_R)\,\|\,x_L\,\|\,G^{s_2}(x_L)\,\|\,x_R$$

直接暴露 $x_L,x_R$：给定 $y=H^{s_1,s_2}(x)$，读出 $x_L,x_R$ 拼回 $x$ 即得原像，成功概率 ${1}$。故 $H_1,H_2$ 均 PR 而 $H$ 非 PR，PR 的类似论断不成立。

**官方解答的另一反例（第三版教师手册 6.2，更简洁）**：取 PR 哈希 $\hat H^s:\{0,1\}^n\to\{0,1\}^{n/4}$，令 $H_1^s(x_1\|x_2)=x_1\|\hat H^s(x_2)$（压缩且 PR），$H_2^s(x_1\|x_2)=x_2$。则 $H^{s_1,s_2}(x_1\|x_2)=x_1\|\hat H^{s_1}(x_2)\|x_2$，直接读出 $x_1\|x_2$，求原像平凡。$\blacksquare$

---

## 习题 6.3　$\hat H^s(x)=H^s(H^s(x))$ 是否 CR？

> **题目**　$H$ 是 CR，$\hat H$ 是否必 CR？

**是**。若 $\mathcal{A}$ 找到 $\hat H$ 的碰撞 $(x,x^{\prime})$：$H^s(H^s(x))=H^s(H^s(x^{\prime}))$。令 $u=H^s(x),u^{\prime}=H^s(x^{\prime})$，则 $H^s(u)=H^s(u^{\prime})$。两种情形：

- $u\ne u^{\prime}$：则 $(u,u^{\prime})$ 是 $H^s$ 的碰撞，矛盾 CR。
- $u=u^{\prime}$：即 $H^s(x)=H^s(x^{\prime})$。若 $x\ne x^{\prime}$（碰撞前提），则 $(x,x^{\prime})$ 是 $H^s$ 的碰撞，矛盾 CR。

两种情形都给出 $H$ 的碰撞。归约：CR 敌手收到 $s$，模拟 $\mathcal{A}$（用 $H^s$）找到 $\hat H$ 碰撞，按上述分析输出 $H$ 碰撞。故 $\hat H$ CR。$\blacksquare$

---

## 习题 6.4　定理 6.4 的归约证明

> **题目**　给出 Merkle–Damgård 变换保 CR 的归约（定理 6.4）。

**归约**。设压缩函数 $(\mathsf{Gen},h)$（${2}n\to n$，输入 $n+n^{\prime}$）是 CR。设 $\mathcal{A}$ 以概率 $\varepsilon$ 找到 $H^s$（M-D 输出）的碰撞 $(x,x^{\prime})$。构造找 $h^s$ 碰撞的 $\mathcal{C}$：收到 $s$，运行 $\mathcal{A}(s)$ 得 $(x,x^{\prime})$（$H^s(x)=H^s(x^{\prime})$，$x\ne x^{\prime}$）。按定理 6.4 证明的两种情形分析：

- **$|x|\ne|x^{\prime}|$**（填充后最后块 $x_B$ 编码不同长度）：M-D 最后一步 $z_B=h^s(z_{B-1}\|x_B)$、$z^{\prime}_{B^{\prime}}=h^s(z^{\prime}_{B^{\prime}-1}\|x^{\prime}_{B^{\prime}})$。$z_B=z^{\prime}_{B^{\prime}}$ 但 $x_B\ne x^{\prime}_{B^{\prime}}$（长度编码不同）$\Rightarrow$ $(z_{B-1}\|x_B,\ z^{\prime}_{B^{\prime}-1}\|x^{\prime}_{B^{\prime}})$ 是 $h^s$ 的碰撞。$\mathcal{C}$ 输出之。
- **$|x|=|x^{\prime}|$**：$B=B^{\prime}$，块数同。令 $I_i=z_{i-1}\|x_i$（$h^s$ 的第 $i$ 输入），$I^{\prime}_i$ 类似。$I_{B+1}=z_B=H^s(x)=H^s(x^{\prime})=z^{\prime}_B=I^{\prime}_{B+1}$。取最大 $N$ 使 $I_N\ne I^{\prime}_N$（存在，因 $x\ne x^{\prime}$ 且 $|x|=|x^{\prime}|$ $\Rightarrow$ 某 $x_i\ne x^{\prime}_i$）。$N\le B$（因 $I_{B+1}=I^{\prime}_{B+1}$）。由 $N$ 最大性 $I_{N+1}=I^{\prime}_{N+1}$ $\Rightarrow z_N=z^{\prime}_N$，而 $I_N=z_{N-1}\|x_N\ne z^{\prime}_{N-1}\|x^{\prime}_N=I^{\prime}_N$，但 $h^s(I_N)=z_N=z^{\prime}_N=h^s(I^{\prime}_N)$ $\Rightarrow$ $(I_N,I^{\prime}_N)$ 是 $h^s$ 碰撞。$\mathcal{C}$ 输出之。

$\mathcal{C}$ 成功概率 $\varepsilon$。$h$ 是 CR $\Rightarrow\varepsilon$ 可忽略 $\Rightarrow H$ CR。$\blacksquare$

---

## 习题 6.5　M-D 变换推广至 $n+1\to n$ 压缩函数

> **题目**　压缩函数 $(\mathsf{Gen},h)$ 输入 $n+1$、输出 $n$。构造处理任意长 $L<2^n$ 输入的 CR 哈希。

**构造**（逐比特处理）。$h^s:\{0,1\}^{n+1}\to\{0,1\}^n$。对输入 $x\in\{0,1\}^*$，长 $L<2^n$：

1. 填充：向 $x$ 追加一个 1，再追加 0 使总长度为 $n$ 的倍数；再追加 $L$ 的 $n$ 比特编码。得比特串 $x_1x_2\cdots x_{B\cdot n}$（$n$ 的倍数）。再将其划分为 $(n+1)$ 比特块？——输入 $n+1$ 但每次只能喂 1 新比特 + $n$ 状态。

逐比特 M-D：状态 $z_i\in\{0,1\}^n$（$n$ 比特），每次输入 1 个消息比特 $b_i$：$z_i=h^s(z_{i-1}\|b_i)$。具体：

1. 设 $x$ 长 $L$。构造填充串 $x\|1\|0^*\|L$（追加 1，补 0 至长度为 $n$ 倍数减 ... ），使最终长度恰为 $L^{\prime}=n\cdot\lceil(L+1+n)/n\rceil$ 比特。把填充后串视为比特序列 $b_1b_2\cdots b_{L^{\prime}}$。
2. $z_0=\mathsf{IV}$（固定 $n$ 比特）。对 $i=1,\ldots,L^{\prime}$：$z_i=h^s(z_{i-1}\|b_i)$。
3. 输出 $z_{L^{\prime}}$。

每次 $h^s$ 输入 $(z_{i-1},b_i)$ 长 $n+1$，输出 $z_i$ 长 $n$——状态压缩 1 比特，新并入 1 比特，保持状态 $n$ 比特。

**CR 证明**：归约同定理 6.4。设 $\mathcal{A}$ 找到碰撞 $(x,x^{\prime})$。$H^s(x)=H^s(x^{\prime})$。沿计算链回溯：填充保证 $|x|\|1\|0^*\|L$ 编码唯一（前缀自由，因末尾含 $L$ 编码），故 $|x|\ne|x^{\prime}|$ 或 $|x|=|x^{\prime}|$ 分别处理；在某步骤 $i$，$z_{i-1}\|b_i\ne z^{\prime}_{i-1}\|b^{\prime}_i$ 但 $h^s(z_{i-1}\|b_i)=z_i=z^{\prime}_i=h^s(z^{\prime}_{i-1}\|b^{\prime}_i)$——$h^s$ 碰撞。长度编码防止"长度扩展"攻击（4.13 型）。故 $h$ CR $\Rightarrow H$ CR。$\blacksquare$

---

## 习题 6.6　Merkle–Damgård 变形（初始值嵌入消息）不安全

> **题目**　变形：填充使长度比 $n^{\prime}$ 倍数多 $n$，解析为 $z_0\|x_1\cdots x_B$（$|z_0|=n,|x_i|=n^{\prime}$），$z_i=h^s(z_{i-1}\|x_i)$，输出 $z_B$。

该变形把**初始链值 $z_0$ 嵌入消息**，于是敌手能把某次哈希的**输出**当作另一条消息的 $z_0$，把两段独立计算的链粘合起来。

**攻击**。
1. 取消息 $m_1$，填充形式 $z_0\|x_1$（一块状态、一块数据），输出 $t_1=h^s(z_0\|x_1)$。
2. 取消息 $m_2$，填充形式 $t_1\|x_2$（以 $t_1$ 作 $z_0$），输出 $t_2=h^s(t_1\|x_2)$。
3. 取消息 $m_3$，填充形式 $z_0\|x_1\|x_2$（三块），其链为
$$z_1=h^s(z_0\|x_1)=t_1,\qquad z_2=h^s(z_1\|x_2)=h^s(t_1\|x_2)=t_2.$$

故 $H^s(m_2)=t_2=H^s(m_3)$，而 $m_2\ne m_3$（$m_2$ 两块、$m_3$ 三块，长度不同）。碰撞得到。敌手只需查询 $m_1$ 得 $t_1$，即可构造 $m_2$ 并与 $m_3$ 碰撞。$\blacksquare$

---

## 习题 6.7　M-D 变形（不安全，提示 $h^s(0^n,0^{n^{\prime}})=0^n$）

> **题目**　变形：填充至 $n^{\prime}$ 倍数（不加长度），$z_0=0^n$，$z_i=h^s(z_{i-1}\|x_i)$，输出 $z_B$。假设 CR 压缩函数存在，证存在 CR 的 $h$ 使此变形不 CR。

**构造 $h$**：取 CR 压缩函数 $g:\{0,1\}^{n+n^{\prime}}\to\{0,1\}^n$。定义 $h^s(a\|b)$（$|a|=n,|b|=n^{\prime}$）：

$$h^s(a\|b)=\begin{cases}0^n,& a=0^n\ \text{且}\ b=0^{n^{\prime}},\\ g^s(a\|b),& \text{否则}.\end{cases}$$

（即 $(0^n,0^{n^{\prime}})$ 是固定点，输出 ${0}^n$。）

**$h$ 是 CR**：$h$ 与 $g$ 仅在单点 $(0^n,0^{n^{\prime}})$ 处不同（输出 ${0}^n$ 而非 $g^s(0^n\|0^{n^{\prime}})$）。均匀 $s$ 下，敌手找到 $h$ 碰撞：要么在非 $(0^n,0^{n^{\prime}})$ 点（归约 $g$ CR），要么涉及固定点。涉及固定点：需 $(a,b)\ne(0^n,0^{n^{\prime}})$ 使 $h^s(a\|b)=0^n=h^s(0^n\|0^{n^{\prime}})$，即 $g^s(a\|b)=0^n$——找到 $g$ 输出为特定值的原像，对 CR 压缩函数仍难（CR 不直接保证，但均匀 $g$ 输出 ${0}^n$ 的原像存在却难找）。综合 $h$ 仍 CR（详细：$h$ 的碰撞要么是 $g$ 的碰撞，要么涉及"输出 ${0}^n$"的两点，后者概率受 $g$ 的抗原像性控制，可忽略）。

**变形不 CR**：消息 $m=0^{n^{\prime}}$（单块，填充后仍 ${0}^{n^{\prime}}$，$z_0=0^n$）：$z_1=h^s(0^n\|0^{n^{\prime}})=0^n$（固定点），输出 ${0}^n$。消息 $m^{\prime}=0^{n^{\prime}}\|0^{n^{\prime}}$（两块）：$z_1=h^s(0^n\|0^{n^{\prime}})=0^n$，$z_2=h^s(0^n\|0^{n^{\prime}})=0^n$，输出 ${0}^n$。$m\ne m^{\prime}$（长度不同）但输出相同 ${0}^n$——碰撞！变形不 CR。$\blacksquare$

---

## 习题 6.8　非 CR 压缩函数经 M-D 仍可得 CR 哈希

> **题目**　假设 CR 哈希存在，构造非 CR 的压缩函数 $(\mathsf{Gen},h)$，但 M-D 变换所得 $(\mathsf{Gen},H)$ 是 CR 的。

**构造。** 设 $\hat h^s:\{0,1\}^{2n-1}\to\{0,1\}^{n-1}$ 是 CR 压缩函数。定义 $h^s:\{0,1\}^{2n}\to\{0,1\}^n$：

$$h^s(0\|x)=0\|\hat h^s(x),\qquad h^s(1\|x)=1^n\qquad(x\in\{0,1\}^{2n-1}).$$

**$h$ 非 CR**：任取 $x\ne x^{\prime}$，$h^s(1\|x)=1^n=h^s(1\|x^{\prime})$，碰撞直接可得。

**$H$（M-D，取首比特为 ${0}$ 的 $IV$）是 CR。** 关键观察：M-D 链值 $z_i$（$i\ge0$）的首比特恒为 ${0}$——$z_0=IV$ 首比特为 ${0}$；若 $z_{i-1}$ 首比特为 ${0}$，则 $h^s$ 的输入 $z_{i-1}\|x_i$ 首比特为 ${0}$，落入 ${0}\|x$ 分支，$z_i=0\|\hat h^s(\cdot)$ 首比特仍为 ${0}$，归纳即得。换言之，"${1}\|x$ 恒映射 ${1}^n$"的退化分支在 M-D 链中**不可达**，整条链与"对 $\hat h$（经 ${0}\|\cdot$ 嵌入）做标准 M-D"完全一致。形式化：设 $H^s(x)=H^s(x^{\prime})$（$x\ne x^{\prime}$），按定理 6.4 的回溯论证找到首个 $I_N\ne I^{\prime}_N$ 但 $h^s(I_N)=h^s(I^{\prime}_N)$；两输入首比特都是 ${0}$，剥去首位后给出 $\hat h^s$ 的碰撞。故 $\hat h$ CR $\Rightarrow H$ CR。

直观：$h$ 的碰撞只存在于一个 M-D 链永远到不了的分支上，故缺陷不被触发。（本构造与第三版教师手册的官方解答逐字一致。）$\blacksquare$

---

## 习题 6.9　压缩函数原像抗性 ⟹ M-D 哈希原像抗性？

> **题目**　Prove or disprove: if $(\mathsf{Gen}, h)$ is preimage resistant, then so is the hash function $(\mathsf{Gen}, H)$ obtained by applying the Merkle–Damgård transform to $(\mathsf{Gen}, h)$.
> **题目**　证明或反驳：如果 $(\mathsf{Gen}, h)$ 是原像抗性的，那么对其应用 Merkle–Damgård 变换得到的哈希函数 $(\mathsf{Gen}, H)$ 也是原像抗性的。

> **结论：不成立（disprove）。**（原解答"成立"有误，下面先指出其归约为何失效，再给出反例。）

**自然归约为何失效。** 设 $\mathcal A$ 是 $H$ 的原像敌手：收到 $s$ 与 $y=H^s(x)$（$x$ 均匀、定长 $\ell(n)$），输出 $x^{\prime}$ 使 $H^s(x^{\prime})=y$。$x^{\prime}$ 的 M-D 链最后一步 $z^{\prime}_{B-1}\|x^{\prime}_B$ 确是 $y$ 在 $h^s$ 下的原像，且归约器 $\mathcal C$ 可用公开的 $h^s$ 重算 $x^{\prime}$ 的链、读出这一点——这部分没错。问题在于：$\mathcal C$ 攻 $h$ 的原像抗性时，拿到的挑战是 $y=h^s(u)$（$u$ 均匀于 $\{0,1\}^{n+n^{\prime}}$），它只能把 $y$ 直接交给 $\mathcal A$；而 $\mathcal A$ 的成功保证只对 $y\leftarrow H^s(\text{均匀 }x)$ 的分布成立，$h^s(U_{n+n^{\prime}})$ 与 $H^s(U_{\ell(n)})$ 两个分布一般毫无关系，$\mathcal A$ 在前者上可以完全失败。归约走不通——下面的反例说明结论本身为假。

**反例。** 设 $(\mathsf{Gen},g)$ 是原像抗性的压缩函数（$g^s:\{0,1\}^{n+n^{\prime}}\to\{0,1\}^n$）。取 M-D 参数 $\ell=n^{\prime}$（长度域占满一个分组，构造 6.3 允许），定义

$$h^s(z\|b)=\begin{cases}0^n,& b=\langle L\rangle\ \text{为某个}\ L<2^{n^{\prime}/2}\ \text{的长度编码},\\ g^s(z\|b),& \text{否则}.\end{cases}$$

（即：所有"末块是合法长度编码"的输入被压成常数 ${0}^n$。塌陷集大小为 ${2}^n\cdot2^{n^{\prime}/2}$，占定义域比例 ${2}^{-n^{\prime}/2}$，可忽略。）

**$h$ 仍原像抗性。** 挑战：均匀 $u=(z_u\|b_u)$，$y=h^s(u)$。$u$ 落入塌陷集的概率仅 ${2}^{-n^{\prime}/2}$；其余情形 $y=g^s(u)$。敌手找 $h^s$ 下 $y$ 的原像只有两条路：(i) 输出塌陷集中的点——其像恒为 ${0}^n$，仅当 $y=0^n$ 时成功，而 $\Pr[y=0^n]\le2^{-n^{\prime}/2}+\Pr[g^s(U)=0^n]$，后一项可忽略（若 $g^s(U)$ 以不可忽略概率取 ${0}^n$，则 ${0}^n$ 有不可忽略比例的原像，硬编码其一即破 $g$ 的原像抗性）；(ii) 输出 $g^s$ 下 $y$ 的原像——归约到 $g$ 的原像抗性。合起来成功概率可忽略。

**$H$ 非原像抗性。** 按构造 6.3 的填充（追加 ${1}$、补 ${0}$、末块写入 $\ell=n^{\prime}$ 比特的长度 $L$），**任何**多项式长消息 $x$ 的最后一个分组都是 $x_B=\langle L\rangle$，落入塌陷分支，故

$$H^s(x)=h^s(z_{B-1}\|\langle L\rangle)=0^n.$$

原像实验中 $y=H^s(x)=0^n$ 恒成立；敌手输出**任意**与 $x$ 等长的 $x^{\prime}$（原像抗性甚至允许 $x^{\prime}=x$），都有 $H^s(x^{\prime})=0^n=y$。成功概率 ${1}$。

> **注**　本质：$h$ 的原像抗性只约束**均匀**输入，感知不到可忽略密度的弱子集；而 M-D 填充把"长度"编码进最后一次压缩的输入，使**每条**链都终止于该弱子集——$H$ 被完全击穿。这正是 Rogaway–Shrimpton 指出的"M-D 保持碰撞抗性，但不保持原像抗性"。**官方题解印证**（第二版教师手册 5.8，即本题）："This is, in general, false"，反例与本解相同——取 PR 的 $h$ 但令 $h^s(x\|\langle L\rangle)=0^n$，则每个 $L$ 比特输入经 M-D 都哈希到 ${0}^n$。$\blacksquare$

---

## 习题 6.10　压缩函数第二原像抗性 ⟹ M-D 哈希第二原像抗性？

> **题目**　Prove or disprove: if $(\mathsf{Gen}, h)$ is second-preimage resistant, then so is the hash function $(\mathsf{Gen}, H)$ obtained by applying the Merkle–Damgård transform to $(\mathsf{Gen}, h)$.
> **题目**　证明或反驳：如果 $(\mathsf{Gen}, h)$ 是第二原像抗性的，那么对其应用 Merkle–Damgård 变换得到的哈希函数 $(\mathsf{Gen}, H)$ 也是第二原像抗性的。

> **结论：不成立（disprove）。**

**先给"中途命中"攻击正确定位。** 给定均匀 $x$（$B$ 块）与 $y=H^s(x)$，敌手熟知 $x$ 的全部中间链值 $z_0,\ldots,z_B$；若另一前缀的链终点命中某个 $z_i$，拼接 $x_{i+1}\cdots x_B$ 即得第二原像——这正是 Dean / Kelsey–Schneier 长消息第二原像攻击的思想：每次尝试命中概率约 $(B+1)/2^n$，期望 ${2}^n/(B+1)$ 次尝试命中（拼接后长度块会变，Kelsey–Schneier 用"可扩展消息"把总长调回 $L$，总复杂度约 $k\cdot2^{n/2+1}+2^{n-k}$，$B=2^k$）。但它仍是**指数时间**，在 KL 的渐近框架（PPT 敌手、可忽略成功概率）下不构成"不保持"的证据。严格的 disprove 需要显式反例，关键是利用"**$h$ 的 SPR 实验用均匀输入，而 M-D 的每条链都从固定 $IV$ 出发**"这一分布差异。

**反例。** 设 $(\mathsf{Gen},g)$ 是 SPR 的压缩函数（$g^s:\{0,1\}^{n+n^{\prime}}\to\{0,1\}^n$）。定义

$$h^s(z\|b)=\begin{cases}0^n,& z=IV\ (\text{构造 6.3 的固定初始值}),\\ g^s(z\|b),& \text{否则}.\end{cases}$$

**$h$ 仍 SPR。** 挑战为均匀 $u=(z_u\|b_u)$ 与 $y=h^s(u)$。$z_u=IV$ 的概率仅 ${2}^{-n}$；其余情形 $y=g^s(u)$。敌手要输出 $u^{\prime}\ne u$ 使 $h^s(u^{\prime})=y$，途径有二：(i) $u^{\prime}$ 落在退化集（$z^{\prime}=IV$）——其像恒为 ${0}^n$，仅当 $y=0^n$ 时成功，$\Pr[y=0^n]\le2^{-n}+\Pr[g^s(U)=0^n]$，后一项可忽略（否则 ${0}^n$ 有不可忽略比例的原像，硬编码其一：SPR 敌手在 $g^s(u)=0^n$ 时输出该点，与 $u$ 相等的概率可忽略，即破 $g$ 的 SPR）；(ii) $u^{\prime}$ 不在退化集——则 $g^s(u^{\prime})=y=g^s(u)$ 且 $u^{\prime}\ne u$，直接归约到 $g$ 的 SPR。合起来成功概率可忽略。

**$H$ 非 SPR。** 给定 SPR 实验的挑战消息 $x$（均匀、任意多项式长度）：

- 若 $x$ 填充后至少两块：令 $x^{\prime}$ 为把 $x$ 的**第一块**翻转一比特（长度不变）。$x^{\prime}$ 与 $x$ 的第一次压缩都是 $h^s(IV\|\cdot)=0^n$，故两者链值从 $z_1=0^n$ 起完全相同；长度相同、长度块相同，于是 $H^s(x^{\prime})=H^s(x)$。$x^{\prime}\ne x$，成功概率 ${1}$。
- 若 $x$ 填充后只有一块：$H^s(x)=h^s(IV\|x_1)=0^n$ 对该长度的**所有**消息成立，任取另一同长消息即得第二原像。

> **注**　本质与 6.9 相同：退化集 $\{(IV,b)\}$ 对均匀输入密度 ${2}^{-n}$，$h$ 的 SPR 感知不到；但 M-D 每条链的**第一步**都落在其中，$H$ 被击穿。文献结论一致：M-D 保持碰撞抗性，但不保持 SPR（渐近意义下）；Kelsey–Schneier 攻击则说明即使对"好"的 $h$，M-D 对超长消息的 SPR 也有具体的（生日级、仍指数的）弱化。**官方题解印证**（第三版教师手册 6.10）："This is, in general, false"，其反例取 SPR 的 $h$ 满足 (a) 任何输出的前 $n/2$ 比特为 ${0}$，(b) $h^s(0^{n/2}\|y)=0^n$（$|y|=3n/2$）——于是任何至少两块的消息链到第二步即得 $z_2=0^n$ 并保持，$H^s$ 对 ${2}n$ 比特输入恒为 ${0}^n$。与本解的 $IV$ 退化反例异曲同工。$\blacksquare$

---

## 习题 6.11　$\mathsf{Mac}_k(m)=H(k\|m)$ 的安全性

> **题目**　(a) $H$ 建模为随机预言机时安全；(b) $H$ 经 M-D 构造时不安全。

**(a) ROM 下安全**。$H$ 是随机预言机，$k$ 均匀。敌手查询 Mac 预言机得 $H(k\|m_i)$（消息 $m_i$）。要在 $m^*\notin\{m_i\}$ 上伪造需 $H(k\|m^*)$。$k$ 未知，敌手对 $H$ 的查询 $H(x)$ 中 $x=k\|m^*$ 的概率：$k$ 是 $n$ 比特，敌手多项式次查询 $H$，命中 $k$ 的概率 $q/2^n$（可忽略）。未命中则 $H(k\|m^*)$ 均匀，猜中概率 ${2}^{-\ell}$。故安全。

**(b) M-D 下不安全**（长度扩展攻击）。$H$ 经 M-D 构造：$H(k\|m)$ 的内部链以 $k$ 为秘密前缀开始。敌手查询 Mac 得 $t=H(k\|m)$。**M-D 长度扩展**：已知 $H(k\|m)=t$（即 M-D 链的最终状态 $t$，对应填充后输入 $k\|m\|\mathsf{pad}$），敌手可构造 $m^{\prime}=m\|\mathsf{pad}_{k\|m}\|y$（追加填充和新数据 $y$），并计算 $H(k\|m^{\prime})$：

$H(k\|m^{\prime})$ 的 M-D 链：先用 $k\|m\|\mathsf{pad}$ 计算（敌手已知其结果 $t$），再从 $t$ 继续链 $h^s(t\|y_1),h^s(\cdot\|y_2),\ldots$。敌手**知道** $t$ 作为中间状态，且 $h^s$ 是 M-D 的压缩函数——但敌手不知密钥 $s$？在 M-D 哈希中 $s$ 公开（无密钥哈希）！故敌手可自行计算 $h^s$。因此 $H(k\|m^{\prime})=h^s(t\|y_1\|\cdots)$ 可由敌手算出，无需 Mac 预言机。$m^{\prime}\ne m$（更长），伪造成功。**故 $\mathsf{Mac}_k(m)=H(k\|m)$ 在 M-D 下不安全**（长度扩展）。$\blacksquare$

---

## 习题 6.12　生日问题：3500 首歌

> **题目**　3500 首歌随机播放，听到重复前需播放多少首（概率 $\ge50\%$）？

生日问题：$N$ 个可能值，$q$ 次均匀采样，存在重复的概率 $\approx 1-e^{-q(q-1)/(2N)}$。要 $\ge0.5$：$q(q-1)/(2N)\ge\ln2\approx0.693$，$q\approx\sqrt{2N\ln2}\approx1.177\sqrt{N}$。$N=3500$，$q\approx1.177\cdot\sqrt{3500}\approx1.177\cdot59.16\approx69.6$。

**约 70 首后**，听到重复的概率 $\ge50\%$。$\blacksquare$

---

## 习题 6.13　两组均匀采样，存在跨组相等的概率

> **题目**　均匀 $y_1,\ldots,y_q\in\{0,1\}^\ell$ 与 $y^{\prime}_1,\ldots,y^{\prime}_q\in\{0,1\}^\ell$。$\Pr[\exists i,j:y_i=y^{\prime}_j]=？$

记 $N=2^\ell$。对固定 $i,j$，$\Pr[y_i=y^{\prime}_j]=1/N$。$\Pr[\forall i,j:y_i\ne y^{\prime}_j]=\Pr[\{y^{\prime}_1,\ldots,y^{\prime}_q\}\cap\{y_1,\ldots,y_q\}=\emptyset]$。

固定 $\{y_i\}$（$q$ 个值），每个 $y^{\prime}_j$ 落入这 $q$ 个值的概率 $q/N$，不落入概率 ${1}-q/N$。$q$ 个 $y^{\prime}_j$ 独立（条件于 $\{y_i\}$，若 $y_i$ 互不相同）：

$\Pr[\text{无跨组相等}]\approx(1-q/N)^q\approx e^{-q^2/N}$（当 $y_i$ 互不相同，$q\ll N$）。

更精确（$y_i$ 可能有内部重复）：$\Pr[\exists i,j:y_i=y^{\prime}_j]=1-\Pr[\forall j:y^{\prime}_j\notin\{y_i\}]=1-\prod_{j}(1-|\{y_i\}|/N)\approx1-(1-q/N)^q\approx1-e^{-q^2/N}$。

当 $q\approx\sqrt{N}=2^{\ell/2}$，概率 $\approx1-e^{-1}\approx0.63$。$\blacksquare$

---

## 习题 6.14　$F_k(x)=H(k\oplus x)$ 的 ${2}^{n/2}$ 密钥恢复攻击

> **题目**　$H:\{0,1\}^n\to\{0,1\}^{2n}$，$F_k(x)=H(k\oplus x)$，$k\in\{0,1\}^n$。预言机访问 $F_k(\cdot)$，${2}^{n/2}$ 时间恢复 $k$。

**攻击**（用习题 6.13）。敌手查询 $F_k$ 在 $q\approx2^{n/2}$ 个**均匀点** $x_1,\ldots,x_q$，得 $y_i=F_k(x_i)=H(k\oplus x_i)$。另**自行**计算 $H$（$H$ 公开无密钥）在 $q$ 个均匀点 $r_1,\ldots,r_q\in\{0,1\}^n$，得 $y^{\prime}_j=H(r_j)$。

由习题 6.13，以概率 $\approx0.63$ 存在 $i,j$ 使 $y_i=y^{\prime}_j$，即 $H(k\oplus x_i)=H(r_j)$。若 $H$ 抗碰撞（或近似单射），则 $k\oplus x_i=r_j$ $\Rightarrow$ $k=r_j\oplus x_i$（**恢复 $k$**）。

总时间：$q$ 次预言机查询 $+q$ 次 $H$ 计算 $+$ 寻找碰撞 $y_i=y^{\prime}_j$（用哈希表 $O(q)$）。$q=2^{n/2}$，总 $\approx2^{n/2}$——优于蛮力 ${2}^n$。**成功概率 $\approx0.63$**（生日命中）。$\blacksquare$

---

## 习题 6.15　$F_k(x)=H(k\|x)$ 在 ROM 下是 PRF

> **题目**　6.5.1 节的 $F_k(x)=H(k\|x)$（$|k|=|x|=n$），$H$ 随机预言机。证 PRF。

PRF 实验：$b=0$ 给 $F_k(\cdot)=H(k\|\cdot)$（$k$ 均匀），$b=1$ 给均匀随机函数 $f:\{0,1\}^n\to\{0,1\}^n$（独立于 $H$）。敌手 $\mathcal{A}$ 可访问 $H$ 与目标函数预言机。

**证明**。$\mathcal{A}$ 多项式次查询目标预言机于点 $x_1,\ldots,x_q$（互不相同，WLOG）。若 $b=0$：目标应答 $H(k\|x_i)$。这些是 $H$ 在点 $k\|x_1,\ldots,k\|x_q$ 的值。$\mathcal{A}$ 也可能直接查询 $H$ 于其他点。关键：$k$ 均匀，$\mathcal{A}$ 通过 $H$ 查询命中某 $k\|x$ 的概率 $\le(q_H+q)/2^n$（$q_H$ 为 $H$ 查询数），可忽略（其中 $q$ 是目标查询使 $\mathcal{A}$ 不知 $k\|x_i$ 的具体值）。

条件于"$\mathcal{A}$ 从未直接查询 $H$ 于任何 $k\|x_i$"（以压倒概率成立）：目标应答 $H(k\|x_i)$ 对 $\mathcal{A}$ 而言是**均匀独立**的（随机预言机在未查询点取值均匀，且 $k\|x_i$ 互不相同）。这恰是均匀随机函数 $f$ 的行为。故 $\mathcal{A}$ 在 $b=0$ 与 $b=1$ 下视图统计不可区分（差距仅 $\mathcal{A}$ 直接查 $H$ 命中 $k\|$ 的可忽略概率）。故 $F$ 是 PRF。$\blacksquare$

---

## 习题 6.16　定理 6.11：Merkle 树保 CR

> **题目**　$(\mathsf{Gen}_H,H)$ CR $\Rightarrow$ $(\mathsf{Gen}_H,\mathcal{MT}_t)$ CR（固定 $t$）。

Merkle 树：叶子 $h_i=H(x_i)$，内部节点 $=H(\text{左子},\text{右子})$，根 $=\mathcal{MT}_t(x_1,\ldots,x_t)$。

**归约**。设 $\mathcal{A}$ 找到 $\mathcal{MT}_t$ 的碰撞：$(x_1,\ldots,x_t)\ne(x^{\prime}_1,\ldots,x^{\prime}_t)$ 但 $\mathcal{MT}_t(x)=\mathcal{MT}_t(x^{\prime})$。沿树比较两棵树：根相同，但叶不同（因输入不同）。从根向下找**最低分歧点**——某节点 $v$ 在两树中值相同但其子节点值不同（左或右子不同）。

形式化：两树根值相同。若两树在根的左、右子值都相同，递归向下。因叶不同，最终在某内部节点 $v$ 处：两树的 $v$ 值相同，但 $v$ 的（左,右）子值对**不同**（至少一侧不同）。该节点 $v$ 的值 $=H(L,R)=H(L^{\prime},R^{\prime})$，而 $(L,R)\ne(L^{\prime},R^{\prime})$——**$H$ 的碰撞**。构造 $\mathcal{C}$：运行 $\mathcal{A}$ 得两输入，按上述找分歧节点，输出 $(L\|R,L^{\prime}\|R^{\prime})$ 作为 $H$ 碰撞。$\mathcal{C}$ 成功概率 $=\mathcal{A}$ 成功概率。$H$ CR $\Rightarrow\mathcal{MT}_t$ CR。$\blacksquare$

---

## 习题 6.17　$t$ 不固定时 Merkle 树碰撞

> **题目**　找 $x_1,\ldots,x_t$ 与 $x^{\prime}_1,\ldots,x^{\prime}_{2t}$ 使 $\mathcal{MT}_t(x)=\mathcal{MT}_{2t}(x^{\prime})$。

**攻击（$t=1$ 与 ${2}t=2$）。** $\mathcal{MT}_1(x_1)=H(x_1)$（单叶，根即 $H(x_1)$），$\mathcal{MT}_2(x^{\prime}_1,x^{\prime}_2)=H(H(x^{\prime}_1)\|H(x^{\prime}_2))$。任取 $x^{\prime}_1,x^{\prime}_2$，令

$$x_1=H(x^{\prime}_1)\,\|\,H(x^{\prime}_2),$$

则

$$\mathcal{MT}_1(x_1)=H(x_1)=H(H(x^{\prime}_1)\|H(x^{\prime}_2))=\mathcal{MT}_2(x^{\prime}_1,x^{\prime}_2),$$

而输入 $\{x_1\}$（1 个值）与 $\{x^{\prime}_1,x^{\prime}_2\}$（2 个值）不同——碰撞。一般地，对任意 $t$，$\mathcal{MT}_{2t}$ 的根 $=H(L\|R)$（$L,R$ 为两棵子树的根），故取 $x_1=L\|R$ 作为 $\mathcal{MT}_1$ 的输入即与 $\mathcal{MT}_{2t}$ 碰撞。根源：叶哈希与内部节点哈希没有**域分离**，一棵树的中层值可以被"伪装"成另一棵（不同规模）树的叶。$\blacksquare$

---

## 习题 6.18　$ t$ 可变时仍 CR 的 Merkle 树修改

> **题目**　修改 Merkle 树使 $t$ 可变时仍 CR。

**修改**：在每个内部节点的 $H$ 输入中**加入树的深度/位置信息**，使不同 $t$（或不同位置）的节点不可混淆。具体：节点在第 $d$ 层、左/右位置，计算 $H(d\|\text{左子}\|\text{右子})$（前置层数 $d$）；叶计算 $H(`leaf`\|i\|x_i)$（前置标记 `leaf` 与索引）。

更简洁（标准做法）：在每个 $H$ 调用前**前置一个表示"节点类型与深度"的标签**：叶为 $H(0\|x_i)$，深度 $d$ 内部节点为 $H(1\|d\|L\|R)$。这样叶哈希与内部节点哈希、不同深度的节点哈希，因前缀不同而不会混淆，阻止习题 6.17 的"伪装"攻击。

**CR 证明**：归约同 6.16，分歧节点的 $(标签\|L\|R)\ne(标签^{\prime}\|L^{\prime}\|R^{\prime})$ 给出 $H$ 碰撞；6.17 型攻击因标签区分叶与节点而失败（单叶的 $H(0\|x)$ 与 $\mathcal{MT}_2$ 根 $H(1\|1\|L\|R)$ 前缀不同，不会相等除非 $H$ 碰撞）。$\blacksquare$

---

## 习题 6.19　Merkle 树存储验证的形式化与证明

> **题目**　(a) 安全性定义；(b) Merkle 树协议形式化；(c) 证明。

**(a) 定义**（客户端在服务器存储 $t$ 文件，取回时验证完整性）。实验 $\mathsf{Retrieve}_{\mathcal{A},\Pi}(n)$：客户端用 $\Pi$ 存储 $x_1,\ldots,x_t$（诚实执行）；敌手（恶意服务器）$\mathcal{A}$ 观察存储；客户端请求第 $i$ 文件，$\mathcal{A}$ 返回 $(x^{\prime},\pi)$（$x^{\prime}$ 与证明 $\pi$）；$\Pi$ 的验证算法 $\mathsf{Vrfy}$ 接受或拒绝。$\mathcal{A}$ 成功当 $\mathsf{Vrfy}$ 接受 $(x^{\prime},\pi)$ 且 $x^{\prime}\ne x_i$。方案安全若成功概率可忽略（基于 CR）。

**(b) Merkle 树协议**：客户端计算根 $h=\mathcal{MT}_t(x_1,\ldots,x_t)$，上传所有文件与树到服务器，本地仅存 $h$（与 $t$）。取回 $x_i$ 时，服务器返回 $x_i$ 与"兄弟路径"证明 $\pi_i$（从叶 $i$ 到根路径上各节点的兄弟节点值）。客户端重算根 $h^{\prime}$ 并验证 $h^{\prime}\overset?=h$。

**(c) 证明**（基于 $H$ CR）：若恶意服务器返回 $(x^{\prime}_i,\pi^{\prime})$ 使验证通过（$h^{\prime}=h$）且 $x^{\prime}_i\ne x_i$。重算过程：叶 $h^{\prime}_i=H(x^{\prime}_i)\ne H(x_i)$（因 $x^{\prime}_i\ne x_i$，若 $H$ CR 则 $H(x^{\prime}_i)\ne H(x_i)$）。沿路径重算到根，与存储的 $h$ 比较。因 $h^{\prime}_i\ne h_i$（叶不同），重算根 $h^{\prime}=h$ 要求路径上**某节点**的输入在两情形下不同但 $H$ 输出相同——即 $H$ 碰撞（同 6.16 归约）。具体：客户端重算用 $x^{\prime}_i$（敌手给的）得 $h^{\prime}_i=H(x^{\prime}_i)$；真实存储用 $x_i$ 得 $h_i=H(x_i)$。验证通过 $\Rightarrow h^{\prime}=h$。从叶到根，存在某层节点 $v$：用 $h^{\prime}_i$ 重算的 $v^{\prime}$ 与真实的 $v$ 值相同，但其子值不同（叶层 $h^{\prime}_i\ne h_i$）$\Rightarrow H$ 碰撞。与 $H$ CR 矛盾。故敌手成功概率可忽略。$\blacksquare$

---

## 习题 6.20　承诺方案在 ROM 下安全

> **题目**　6.6.5 节承诺方案（$\mathsf{com}=H(m\|r)$，$r$ 均匀 $n$ 比特）在 ROM 下安全。

承诺方案安全性 = 隐藏 + 绑定（定义 6.13）。

**隐藏**：实验中 $\mathcal{A}$ 给 $\mathsf{com}=H(m_b\|r)$（$b$ 均匀，$r$ 均匀 $n$ 比特），猜 $b$。$H$ 随机预言机，$r$ 均匀未知。$\mathcal{A}$ 多项式次查询 $H$，命中 $m_b\|r$（对某 $b$）的概率：$r$ 是 $n$ 比特，$\Pr[\mathcal{A}\ \text{查到}\ m_0\|r\ \text{或}\ m_1\|r]\le2q/2^n$（可忽略，$q$ 为 $H$ 查询数）。未命中则 $H(m_b\|r)$ 对 $\mathcal{A}$ 均匀，与 $b$ 无关。故 $\Pr[\mathsf{Hiding}=1]\le1/2+\mathsf{negl}$。

**绑定**：$\mathcal{A}$ 输出 $(\mathsf{com},m,r,m^{\prime},r^{\prime})$，$m\ne m^{\prime}$，$H(m\|r)=\mathsf{com}=H(m^{\prime}\|r^{\prime})$。因 $m\ne m^{\prime}$，$m\|r\ne m^{\prime}\|r^{\prime}$（前缀 $m$ 不同），故 $(m\|r,m^{\prime}\|r^{\prime})$ 是 $H$ 的碰撞。ROM 下 $H$ 抗碰撞（6.5.1 节已证随机预言机 CR，碰撞概率 $O(q^2/2^{\ell_{out}})$ 可忽略）。故 $\Pr[\mathsf{Binding}=1]\le\mathsf{negl}$。

合并：承诺方案在 ROM 下安全。$\blacksquare$
