# 第三章　习题解答

> *Introduction to Modern Cryptography (3rd ed.), Katz & Lindell — Chapter 3 Exercises*

---

## 习题 3.1　可忽略函数的封闭性质（命题 3.6）

> **题目**　Prove Proposition 3.6: (1) $\mathrm{negl}_3=\mathrm{negl}_1+\mathrm{negl}_2$ is negligible; (2) for any polynomial $p$, $\mathrm{negl}_4=p\cdot\mathrm{negl}_1$ is negligible.
> **题目**　证明命题 3.6：(1) $\mathrm{negl}_3=\mathrm{negl}_1+\mathrm{negl}_2$ 是可忽略的；(2) 对任意多项式 $p$，$\mathrm{negl}_4=p\cdot\mathrm{negl}_1$ 是可忽略的。

**证明**　回忆：$f$ 可忽略指对任意多项式 $d$，$\exists N\ \forall n>N:\ f(n)<1/d(n)$。

(1) 任取多项式 $d$。因 $\mathrm{negl}_1,\mathrm{negl}_2$ 可忽略，$\exists N_1,N_2$ 使 $n>N_1$ 时 $\mathrm{negl}_1(n)<\tfrac{1}{2d(n)}$，$n>N_2$ 时 $\mathrm{negl}_2(n)<\tfrac{1}{2d(n)}$。于是 $n>\max(N_1,N_2)$ 时 $\mathrm{negl}_3(n)<\tfrac{1}{d(n)}$。故 $\mathrm{negl}_3$ 可忽略。

(2) 任取多项式 $d$。$p(n)\cdot d(n)$ 仍是多项式。由 $\mathrm{negl}_1$ 可忽略，$\exists N$ 使 $n>N$ 时 $\mathrm{negl}_1(n)<\tfrac{1}{p(n)d(n)}$，从而 $\mathrm{negl}_4(n)=p(n)\mathrm{negl}_1(n)<\tfrac{1}{d(n)}$。故 $\mathrm{negl}_4$ 可忽略。$\blacksquare$

---

## 习题 3.2　任意长消息下"等长限制"不可省

> **题目**　Prove that Definition 3.8 cannot be satisfied if $\Pi$ can encrypt arbitrary-length messages and the adversary is not restricted to outputting equal-length messages.
> **题目**　证明：如果 $\Pi$ 可以加密任意长度的消息，且敌手在 $\mathsf{PrivK}^{\mathsf{eav}}_{\mathcal{A},\Pi}(n)$ 中不受限于输出等长消息，则定义 3.8 无法满足。

设 $q(n)$ 为加密单比特明文所得密文长度的多项式上界。构造敌手 $\mathcal{A}$：输出 $m_0=0\in\{0,1\}$，$m_1\leftarrow\{0,1\}^{q(n)+2}$（均匀）。收到挑战密文 $c$ 后，令 $|c|$ 为其长度：

$$ b^{\prime}=\begin{cases}0,& |c|\le q(n),\\ 1,& |c|>q(n).\end{cases} $$

当 $b=0$ 时 $c=\mathsf{Enc}_k(m_0)$，由 $q$ 的定义 $|c|\le q(n)$，故 $b^{\prime}=0=b$；当 $b=1$ 时 $c=\mathsf{Enc}_k(m_1)$，而 $|m_1|=q(n)+2$，故 $|c|\ge q(n)+2>q(n)$，$b^{\prime}=1=b$。于是 $\Pr[\mathsf{PrivK}^{\mathsf{eav}}_{\mathcal{A},\Pi}(n)=1]=1$，定义 3.8 不可能满足。$\blacksquare$

---

## 习题 3.3　限定明文长度时可构造等价 EAV 安全方案

> **题目**　若 $\mathsf{Enc}_k$ 仅对长度不超过 $\ell(n)$ 的消息有定义，构造在"不限等长"的 $\mathsf{PrivK}^{\mathsf{eav}}$ 中满足定义 3.8 的方案。

设 $(\mathsf{Gen},\mathsf{Enc}^{\prime},\mathsf{Dec}^{\prime})$ 为一固定长度 $\ell(n)$ 的 EAV 安全方案（如构造 3.17 的 $\ell(n)$ 版本，依赖 PRG）。定义新方案：

- $\mathsf{Gen}$ 不变；
- 对长度 $|m|\le\ell(n)-1$ 的 $m$，先编码 $\hat m=m\|\,1\|\,0^{\ell(n)-|m|-1}$（追加一个 1 再补 0 至长度 $\ell(n)$），再输出 $c=\mathsf{Enc}^{\prime}_k(\hat m)$；
- $\mathsf{Dec}_k(c)=\,$从 $\mathsf{Dec}^{\prime}_k(c)$ 中删除末尾所有 0，再去掉最后一个 1 得 $m$。

所有送入 $\mathsf{Enc}^{\prime}$ 的明文长度恰为 $\ell(n)$，故所有密文等长，长度不泄露任何信息。归约：若存在不限等长的敌手 $\mathcal{A}$ 以非可忽略优势攻破新方案，则 $\mathcal{A}^{\prime}$（在内部对 $\mathcal{A}$ 提交的消息对做上述编码后转发给 $\mathsf{Enc}^{\prime}$ 预言机）以相同优势攻破原固定长度 EAV 安全方案，矛盾。$\blacksquare$

---

## 习题 3.4　定义 3.8 与 3.9 的等价

> **题目**　Prove the equivalence of Definition 3.8 and Definition 3.9.
> **题目**　证明定义 3.8 与定义 3.9 的等价性。

记 $p_b=\Pr[\mathsf{out}_{\mathcal{A}}(\mathsf{PrivK}^{\mathsf{eav}}(n,b))=1]$。在 $\mathsf{PrivK}^{\mathsf{eav}}(n)$ 中 $b$ 均匀，实验输出 1（即 $b^{\prime}=b$）当且仅当"$b=0$ 且 $b^{\prime}=0$"或"$b=1$ 且 $b^{\prime}=1$"：

$$\Pr[\mathsf{PrivK}^{\mathsf{eav}}_{\mathcal{A},\Pi}(n)=1]=\tfrac12(1-p_0)+\tfrac12 p_1=\tfrac12+\tfrac12(p_1-p_0).$$

故 $\Pr[\mathsf{PrivK}^{\mathsf{eav}}=1]\le\tfrac12+\mathsf{negl}(n)\iff |p_1-p_0|\le 2\,\mathsf{negl}(n)$。又 $f$ 可忽略 $\iff$ ${2}f$ 可忽略（常数倍封闭），二者等价。$\blacksquare$

---

## 习题 3.5　$G(s)=s\|s$ 不是 PRG

> **题目**　$G(s)\overset{\mathrm{def}}=s\|s$。给出攻击。

设 $|s|=n$，$|G(s)|=2n$。区分器 $D$ 收到 $r\in\{0,1\}^{2n}$，将 $r$ 拆成前后各 $n$ 比特 $r_1,r_2$，若 $r_1=r_2$ 输出 1，否则输出 0。

- 若 $r=G(s)$：恒有 $r_1=r_2=s$，$\Pr[D(G(U_n))=1]=1$；
- 若 $r\leftarrow\{0,1\}^{2n}$ 均匀：$\Pr[r_1=r_2]=2^{-n}$。

优势 ${1}-2^{-n}$，不可忽略，故 $G$ 不是 PRG。$\blacksquare$

---

## 习题 3.6　PRG 的几种变形

> **题目**　$G$ 是 PRG（扩张因子 $\ell$）。判断各 $G^{\prime}$ 是否必为 PRG。

记 $G:\{0,1\}^n\to\{0,1\}^{\ell(n)}$。"是否必为 PRG"指对**任意** PRG $G$ 该 $G^{\prime}$ 是否都是 PRG；若否，给一个 PRG $G$ 使 $G^{\prime}$ 不安全。

**(a) $G^{\prime}(s)=G(\bar s)$：是 PRG。** $s$ 均匀时 $\bar s$ 亦均匀，故 $G^{\prime}(U_n)=G(\bar U_n)$ 与 $G(U_n)$ 同分布，后者伪随机。

**(b) $G^{\prime}(s)=\overline{G(s)}$：是 PRG。** 若 $D$ 以优势 $\varepsilon$ 区分 $G^{\prime}(U)$ 与均匀，令 $D^{\prime}(r)=D(\bar r)$，则 $D^{\prime}$ 以优势 $\varepsilon$ 区分 $G(U)$（取补即 $G^{\prime}(U)$）与均匀（取补仍均匀），与 $G$ 是 PRG 矛盾。

**(c) $G^{\prime}(s)=G(0^{|s|}\|s)$：未必是 PRG。** 反例：取 PRG $H:\{0,1\}^{2n}\to\{0,1\}^{\ell(2n)}$，定义
$$G(x)=\begin{cases}0^{\ell(2n)},& x\text{ 的前半为 }0^n,\\ H(x),& \text{否则}.\end{cases}$$
均匀 ${2}n$ 比特输入前半为 ${0}^n$ 的概率仅 ${2}^{-n}$，故 $G(U_{2n})$ 与 $H(U_{2n})$ 统计距离 $\le 2^{-n}$，$G$ 仍是 PRG。但 $G^{\prime}(s)=G(0^n\|s)$ 恒落入"前半为 ${0}^n$"分支，输出恒 ${0}^{\ell(2n)}$；区分器检测"输出全 ${0}$"即以压倒优势区分。

**(d) $G^{\prime}(s)=G(s)\|G(s+1)$：未必是 PRG。** 反例：取 PRG $F:\{0,1\}^{n-1}\to\{0,1\}^{n+1}$，定义 $G:\{0,1\}^{n}\to\{0,1\}^{n+1}$ 为 $G(s)=F(\lfloor s/2\rfloor)$。
- $G$ 是 PRG：$s$ 均匀时 $\lfloor s/2\rfloor$ 在 $\{0,1\}^{n-1}$ 上均匀，$G(U_n)=F(U_{n-1})$ 伪随机。
- 对偶数 $s$，$\lfloor s/2\rfloor=\lfloor(s+1)/2\rfloor$，故 $G(s)=G(s+1)$；偶数 $s$ 占比 ${1}/{2}$。
- 区分器把 $G^{\prime}(s)$（长 ${2}(n+1)$）拆成前后各 $n+1$ 比特，检测二者是否相等：$\Pr[\text{等}\mid G^{\prime}]\ge 1/2$，而均匀串两半相等概率 ${2}^{-(n+1)}$。优势 $\ge 1/2-2^{-(n+1)}$，不可忽略。$\blacksquare$

---

## 习题 3.7　基于实验的 PRG 定义及其等价性

> **题目**　用 $\mathsf{PRG}_{\mathcal{A},G}(n)$ 实验定义 PRG，证明与定义 3.14 等价。

**定义**：$G$ 是 PRG，若对所有 PPT $\mathcal{A}$，$\Pr[\mathsf{PRG}_{\mathcal{A},G}(n)=1]\le\tfrac12+\mathsf{negl}(n)$。

**等价性**。记 $p_G=\Pr[\mathcal{A}(G(U_n))=1]$，$p_R=\Pr[\mathcal{A}(U_{\ell(n)})=1]$。实验中 $b=0$（取均匀 $r$）时 $\mathcal{A}(r)$ 输出 1 的概率为 $p_R$，输出 0 的概率 ${1}-p_R$；$b=1$（取 $G(s)$）时输出 1 的概率 $p_G$。实验成功（$b^{\prime}=b$）：

$$\Pr[\mathsf{PRG}_{\mathcal{A},G}(n)=1]=\tfrac12(1-p_R)+\tfrac12 p_G=\tfrac12+\tfrac12(p_G-p_R).$$

故实验定义 $\le\tfrac12+\mathsf{negl}$ $\iff$ $|p_G-p_R|\le 2\,\mathsf{negl}$ $\iff$ 定义 3.14（$|p_G-p_R|$ 可忽略）。$\blacksquare$

---

## 习题 3.8　定理 3.16 的逆

> **题目**　若 $G$ 不是 PRG，则构造 3.17 在窃听者面前没有不可区分加密。

构造 3.17：$\mathsf{Enc}_k(m)=G(k)\oplus m$。$G$ 不是 PRG $\Rightarrow$ $\exists$ PPT $D$ 以非可忽略优势 $\varepsilon(n)$ 区分 $G(U_n)$ 与 $U_{\ell(n)}$。构造敌手 $\mathcal{A}$：

1. 输出 $m_0=0^{\ell(n)}$，$m_1\leftarrow\{0,1\}^{\ell(n)}$（均匀）；
2. 收到挑战 $c$ 后，输出 $b^{\prime}=D(c)$。

分析：$b=0$ 时 $c=G(k)$，$\Pr[\mathsf{out}(n,0)=1]=\Pr[D(G(U_n))=1]=p_G$；$b=1$ 时 $c=G(k)\oplus m_1$，$m_1$ 均匀独立于 $G(k)$，故 $c$ 在 $\{0,1\}^{\ell(n)}$ 上均匀，$\Pr[\mathsf{out}(n,1)=1]=\Pr[D(U_{\ell})=1]=p_R$。由定义 3.9，$|p_G-p_R|=\varepsilon(n)$ 非可忽略 $\Rightarrow$ 方案非 EAV 安全。$\blacksquare$

---

## 习题 3.9　"不同消息"多重加密不可区分

> **题目**　(a) 给出"多重不同消息"不可区分定义；(b) 构造 3.17 不满足；(c) 给出满足该定义的确定性方案。

**(a) 定义**：方案 $\Pi$ 在窃听者面前对**不同**消息的多重加密不可区分，若对所有 PPT $\mathcal{A}$：

- $\mathcal{A}$ 输出两个**由互不相同消息组成**的等长向量 $\vec m_0=(m_0^1,\ldots,m_0^t)$、$\vec m_1=(m_1^1,\ldots,m_1^t)$（每个向量内部无重复，等长）；
- 均匀选 $b$，把 $(\mathsf{Enc}_k(m_b^1),\ldots,\mathsf{Enc}_k(m_b^t))$ 给 $\mathcal{A}$；
- 要求 $\Pr[\mathcal A\ \text{输出}\ b]\le\tfrac12+\mathsf{negl}(n)$。

**(b) 构造 3.17 不满足该定义。** $\mathsf{Enc}_k(m)=G(k)\oplus m$ 是确定性的。敌手取 $\vec m_0=(0^\ell,1^\ell)$、$\vec m_1=(0^\ell,0^{\ell-1}1)$（每个向量内部消息互不相同，合法）。收到 $(c_1,c_2)$ 后计算 $c_1\oplus c_2$：对构造 3.17 恒有 $c_1\oplus c_2=m_b^1\oplus m_b^2$。$\vec m_0$ 两分量的异或为 ${1}^\ell$，$\vec m_1$ 的为 ${0}^{\ell-1}1$，二者不等；敌手输出 ${0}$ 当且仅当 $c_1\oplus c_2=1^\ell$，成功概率 ${1}$。

**(c)** 取构造 3.28（随机化）：$\mathsf{Enc}_k(m)=\langle r,F_k(r)\oplus m\rangle$，$r$ 每次独立均匀。即使方案"状态无关"，每次加密用新鲜随机量 $r$，对至多多项式条消息，各 $r$ 几乎必然互不相同（生日界），每个密文独立近乎一次性密码本，可证满足 (a) 的定义。$\blacksquare$

---

## 习题 3.10　无条件存在小输入长度的 PRF

> **题目**　证明存在 $F:\{0,1\}^*\times\{0,1\}^*\to\{0,1\}$，$\ell_{key}(n)=n$、$\ell_{in}(n)=\log n$ 的 PRF（无条件）。

输入长度 $\log n$ 意味着定义域只有 $n$ 个点。定义 $F$ 如下：密钥 $k\in\{0,1\}^n$ 解释为 $n$ 比特串；对输入 $x\in\{0,1\}^{\log n}$（视为 $[0,n)$ 中整数 $i$），输出 $F_k(x)=k$ 的第 $i$ 个比特。

**$F$ 是 PRF**：均匀 $f\in\mathsf{Func}_{\log n,n}$ 在 $n$ 个输入上各独立均匀输出 1 比特；均匀 $k\in\{0,1\}^n$ 在 $n$ 个位置各独立均匀——这两个分布在 $n$ 个查询点上**完全相同**（都是 $n$ 个独立均匀比特）。故任意敌手（甚至无穷算力）都无法区分，优势 0。无任何计算假设。$\blacksquare$

---

## 习题 3.11　几种 PRF 变形

> **题目**　$F$ 是保长 PRF。判断各 $F^{\prime}_k:\{0,1\}^{n-1}\to\{0,1\}^{2n}$ 是否 PRF。

**(a) $F^{\prime}_k(x)=F_k(0\|x)\|F_k(0\|x)$：不是。** 输出前后两半恒等。区分器检测 $y_1=y_2$：$F^{\prime}$ 时概率 1，真随机时 ${2}^{-n}$。

**(b) $F^{\prime}_k(x)=F_k(0\|x)\|F_k(1\|x)$：是 PRF。** 归约：若 $D$ 以 $\varepsilon$ 区分 $F^{\prime}$ 与 $f^{\prime}\leftarrow\mathsf{Func}_{n-1,2n}$，构造 $D^{\prime}$ 访问预言机 $\mathcal O\in\{F_k,f\}$，对 $D$ 的查询 $x$ 以 $(\mathcal O(0\|x),\mathcal O(1\|x))$ 应答。$\mathcal O=F_k$ 时 $D^{\prime}$ 模拟 $F^{\prime}$；$\mathcal O=f$ 均匀时，$f(0\|x),f(1\|x)$ 在不同输入上独立均匀，恰为均匀 $f^{\prime}(x)$，故模拟真随机。优势 $\varepsilon$ 传递，与 $F$ 是 PRF 矛盾。

**(c) $F^{\prime}_k(x)=F_k(0\|x)\|F_k(x\|0)$：不是。** 注意 $F^{\prime}_k(0^{n-1})=F_k(0^n)\|F_k(0^n)$，前后半相等；而区分器只需查询 $x=0^{n-1}$ 即可（同 (a)）。

**(d) $F^{\prime}_k(x)=F_k(0\|x)\|F_k(x\|1)$：不是。** 注意两组求值点 $\{0\|x\}$ 与 $\{x\|1\}$ 会**相交**：取 $x_1=1^{n-1}$、$x_2=01^{n-2}$（$n\ge2$），则

$${0}\|x_1=01^{n-1}=x_2\|1.$$

于是

$$F^{\prime}_k(x_1)\ \text{的前半}\ =\ F_k(0\|x_1)=F_k(x_2\|1)\ =\ F^{\prime}_k(x_2)\ \text{的后半},$$

恒成立；而均匀 $f^{\prime}:\{0,1\}^{n-1}\to\{0,1\}^{2n}$ 在 $x_1\ne x_2$ 上取值独立，该等式成立概率仅 ${2}^{-n}$。区分器查询 $x_1,x_2$ 并检验"$x_1$ 输出的前半 $=x_2$ 输出的后半"，优势 ${1}-2^{-n}$，故非 PRF。$\blacksquare$

---

## 习题 3.12　满足多重加密 EAV 但非 CPA 的方案

> **题目**　假设 PRF 存在，构造满足定义 3.18 但不满足定义 3.21 的方案。

**注意**：直接用构造 3.17 不行——它是确定性的，本身就不满足定义 3.18（多重 EAV 下取 $\vec m_0=(m,m)$、$\vec m_1=(m,m^{\prime})$ 即被区分）。正确做法是在一个 CPA 安全方案上附加"只有加密预言机才能利用"的泄漏。

**构造。** 设 $F$ 是保长 PRF，定义

$$\mathsf{Enc}_k(m)=\langle r,\ F_k(r)\oplus m,\ F_k(m)\rangle,\qquad r\leftarrow\{0,1\}^n\ \text{均匀},$$

即在构造 3.28 的密文 $\langle r,F_k(r)\oplus m\rangle$ 后追加第三分量 $F_k(m)$。$\mathsf{Dec}_k$ 取前两个分量按构造 3.28 解密。

**满足定义 3.18（多重加密 EAV）。** 归约到 $F$ 的伪随机性：把 $F_k$ 换成均匀 $f$。第 $i$ 条密文为 $\langle r_i,f(r_i)\oplus m_b^i,f(m_b^i)\rangle$。各 $r_i$ 互不碰撞（$q$ 条消息时碰撞概率 $\le q^2/2^n$，生日界）时 $f(r_i)$ 独立均匀，$f(r_i)\oplus m_b^i$ 均匀且与 $b$ 无关；$f(m_b^i)$ 也均匀、与 $b$ 无关。故理想情形下敌手视图与 $b$ 统计无关（差距 $\le q^2/2^n$），优势为 0；换回 $F_k$ 至多再差一个 PRF 区分优势。故 3.18 意义下优势可忽略。

**不满足定义 3.21（CPA）。** 敌手先查询加密预言机 $\mathsf{Enc}_k(0^n)$，得 $\langle r_0,\,\cdot\,,\,F_k(0^n)\rangle$，记下 $F_k(0^n)$；再输出挑战对 $m_0=0^n$、$m_1=1^n$。挑战密文 $\langle r^*,\,\cdot\,,\,F_k(m_b)\rangle$：检验第三分量是否等于 $F_k(0^n)$——$b=0$ 时恒相等；$b=1$ 时 $F_k(1^n)=F_k(0^n)$ 的概率可忽略（把 $F_k$ 换成均匀 $f$ 后该概率为 ${2}^{-n}$，由 PRF 性其在 $F_k$ 下也可忽略，否则立即可区分）。敌手据此判定 $b$，成功概率 $\approx1$。

（直觉：第三分量把"$F_k$ 在明文处的值"明文写出；EAV 敌手无预言机，只看到均匀-looking 的 $f(m_b^i)$；CPA 敌手却能先取 $F_k(0^n)$ 再与挑战对照。）

**另一构造（第三版教师手册的官方解答，更贴合题目 hint 的"自适应查询"）**：密钥为 $\langle k,s\rangle$（各 $n$ 比特）；$\mathsf{Enc}_{\langle k,s\rangle}(m)$ 若 $m=s$ 输出 $\langle 0,k,s,s\rangle$（直接泄 $k$），否则输出 $\langle 1,s,r,F_k(r)\oplus m\rangle$。CPA 敌手先查询 ${0}^n$ 从密文第二分量读出 $s$，再（自适应地）查询 $s$ 得到 $k$，随后任意破解挑战；EAV 下挑战消息击中均匀 $s$ 的概率可忽略，方案退化为构造 3.28 而安全。$\blacksquare$

---

## 习题 3.13　基于实验的 PRF 定义

> **题目**　用 $\mathsf{PRF}_{\mathcal{A},F}(n)$ 定义 PRF，证明与定义 3.24 等价。

**定义**：$F$ 是 PRF，若对所有 PPT $\mathcal{A}$，$\Pr[\mathsf{PRF}_{\mathcal{A},F}(n)=1]\le\tfrac12+\mathsf{negl}(n)$。

**等价**。记 $p_F=\Pr[\mathcal{A}^{F_k(\cdot)}(1^n)=1]$（$k$ 均匀），$p_R=\Pr[\mathcal{A}^{f(\cdot)}(1^n)=1]$（$f\leftarrow\mathsf{Func}_n$ 均匀）。$b=0$ 对应 $f$，$b=1$ 对应 $F_k$。实验成功 $=\tfrac12(1-p_R)+\tfrac12 p_F=\tfrac12+\tfrac12(p_F-p_R)$。故 $\le\tfrac12+\mathsf{negl}\iff|p_F-p_R|\le 2\,\mathsf{negl}\iff$定义 3.24。$\blacksquare$

---

## 习题 3.14　$F_k(x)=k\& x$ 不是 PRF

> **题目**　"$\&$" 为按位与。给出攻击。

区分器 $D$：查询 $x_1=1^n$ 得 $y_1=F_k(1^n)=k$；再查询任意 $x_2$ 得 $y_2$，检验 $y_2\overset?=k\&x_2=y_1\&x_2$。若相等输出 1，否则 0。

- $\mathcal O=F_k$：$y_2=k\&x_2=y_1\&x_2$ 恒成立，$\Pr[D=1]=1$；
- $\mathcal O=f$ 均匀：$y_1=f(1^n)$ 均匀，$y_2=f(x_2)$ 独立均匀，$\Pr[y_2=y_1\&x_2]=2^{-n}$。

优势 ${1}-2^{-n}$，非可忽略。（更简洁：$F_k(1^n)=k$ 直接泄露整个密钥，查询 ${1}^n$ 后即可预测任意点。）$\blacksquare$

---

## 习题 3.15　仿射函数 $F_{A,b}(x)=Ax+b$ 不是 PRF

> **题目**　$A$ 为 $n\times n$ 布尔矩阵，$b$ 为 $n$ 维布尔向量，模 2 运算。给出攻击。

利用仿射结构 $F_{A,b}(x)\oplus F_{A,b}(y)=A(x\oplus y)$（与 $b$、与具体 $x,y$ 仅通过 $x\oplus y$ 有关）。区分器 $D$：查询三个点 $x,y,x\oplus y$（取 $x=1^n,y=0^n,x\oplus y=1^n$ 不行，需不同；取 $x=e_1,y=e_2,z=e_1\oplus e_2$），得 $u=F(x),v=F(y),w=F(z)$。检验 $u\oplus v\oplus w\overset?=F(0^n)$。

由仿射性 $u\oplus v\oplus w = A x+b\oplus A y+b\oplus A z+b = A(x\oplus y\oplus z)\oplus b$。若取 $z=x\oplus y\oplus 0^n$ 即 $x\oplus y\oplus z=0^n$，则上式 $=b=F(0^n)$，恒成立。

- $F_{A,b}$：$\Pr[D=1]=1$；
- 均匀 $f$：$u\oplus v\oplus w$ 均匀，等于 $f(0^n)$ 概率 ${2}^{-n}$。

优势 ${1}-2^{-n}$，非 PRF。$\blacksquare$

---

## 习题 3.16　由 PRF 构造 PRG

> **题目**　$F$ 保长 PRF，$G(s)=F_s(\langle1\rangle)\|\cdots\|F_s(\langle\ell\rangle)$ 是扩张 $\ell\cdot n$ 的 PRG。

设 $\langle i\rangle$ 为 $i$ 的 $n$ 比特编码。归约：若 $D$ 以 $\varepsilon$ 区分 $G(U_n)$（长 $\ell n$）与均匀 $U_{\ell n}$，构造区分器 $D^{\prime}$：访问 $\mathcal O\in\{F_k,f\}$，对 $i=1,\ldots,\ell$ 查询 $\mathcal O(\langle i\rangle)$ 得 $y_i$，拼接 $r=y_1\|\cdots\|y_\ell$ 后运行 $D(r)$。

- $\mathcal O=F_k$：$r=F_k(\langle1\rangle)\|\cdots\|F_k(\langle\ell\rangle)=G(k)$，$D^{\prime}$ 输出 $D(G(U_n))$；
- $\mathcal O=f$ 均匀：因 $\langle1\rangle,\ldots,\langle\ell\rangle$ 互不相同，$y_1,\ldots,y_\ell$ 独立均匀，$r\equiv U_{\ell n}$，$D^{\prime}$ 输出 $D(U_{\ell n})$。

$D^{\prime}$ 优势 $\varepsilon$，与 $F$ 是 PRF 矛盾。故 $G$ 是 PRG。$\blacksquare$

---

## 习题 3.17　伪随机置换未必是强伪随机置换

> **题目**　假设 PRP 存在，构造是 PRP 但非强 PRP 的 $F$。

设 $P$ 是伪随机置换。构造 $F$ 使**正向查询公开点 ${0}^n$ 直接返回密钥 $k$**：令 $F_k(0^n)=k$ 且 $F_k(k)=0^n$（把 ${0}^n$ 与 $k$ 的像对调）。

**构造（保持置换）**。设 $a=P_k^{-1}(k)$、$b=P_k^{-1}(0^n)$。把 $P_k$ 在四个输入 $\{0^n,k,a,b\}$ 上的像重排为
$$F_k(0^n)=k,\quad F_k(k)=0^n,\quad F_k(a)=P_k(0^n),\quad F_k(b)=P_k(k),$$
其余 $x\notin\{0^n,k,a,b\}$ 上 $F_k(x)=P_k(x)$。这四点的像集合未变（$\{k,0^n,P_k(0^n),P_k(k)\}$ 与原像集合相同），故 $F_k$ 仍是 $\{0,1\}^n$ 上的置换。退化情形（$k=0^n$ 或四点合并）概率 ${2}^{-n}$，可忽略。

**$F$ 是 PRP。** $F_k$ 与 $P_k$ 至多在四点不同，其中 $k,a,b$ 都是密钥依赖的随机点。任意多项式次查询命中 $\{k,a,b\}$ 的概率 $\le 3q/2^n$（可忽略）；命中 ${0}^n$ 时所得 $F_k(0^n)=k$ 仍均匀（$k$ 均匀），与均匀置换 $f(0^n)$ 同分布。故区分 $F_k$ 与均匀置换的优势 $\le$ 区分 $P_k$ 与均匀的优势 $+\,3q/2^n$，可忽略。

**$F$ 非强 PRP。** 强 PRP 敌手有正、逆双向预言机，此处只需正向：
1. 正向查询 ${0}^n$，得 $a=F_k(0^n)=k$；
2. 正向查询 $a(=k)$，得 $F_k(k)=0^n$；
3. 输出 ${1}$ 当且仅当 $F_k(F_k(0^n))=0^n$。

对 $F$ 该检测恒成立（$\Pr=1$）；对均匀置换 $f$，$f(f(0^n))=0^n$ 当且仅当 $f(0^n)=f^{-1}(0^n)$，概率 ${2}^{-n}$。优势 ${1}-2^{-n}$，故 $F$ 非强 PRP。$\blacksquare$

---

## 习题 3.18　抗选择明文完全保密不可达

> **题目**　把定义 3.21 改成"完全保密版"（无计算限制、误差 0），证明不可达。

**定义**（完全 CPA 保密）：方案 $\Pi$ 完全 CPA 保密，若对**所有**（甚至无穷算力）敌手 $\mathcal{A}$，$\Pr[\mathsf{PrivK}^{\mathsf{cpa}}_{\mathcal{A},\Pi}(n)=1]=\tfrac12$。

**不可达**。设消息空间含两个不同消息 $m_0,m_1$。无穷算力敌手 $\mathcal{A}$ 的策略：

1. 用加密预言机对 $m_0$ 和 $m_1$ 各查询充分多次（查询次数不受多项式限制），任意精度地估计出**当前密钥 $k$** 下两条消息的密文分布 $p_0,p_1$；
2. 输出挑战对 $(m_0,m_1)$，收到挑战密文 $c$ 后做似然比检验：输出 ${0}$ 当且仅当 $p_0(c)\ge p_1(c)$。

**分析。** 固定任意密钥 $k$：若 $p_0=p_1$（两分布完全相同），则 $\mathsf{Dec}_k$ 对取自同一分布的密文既要（以正确性要求的概率）输出 $m_0$、又要输出 $m_1$，与 $\mathsf{Dec}_k$ 是函数矛盾。故对每个 $k$ 都有 $p_0\ne p_1$，即总变差 $\delta_k\overset{\mathrm{def}}{=}\mathsf{TV}(p_0,p_1)>0$。似然比检验是最优区分器，成功概率恰为 $\tfrac12+\tfrac12\delta_k>\tfrac12$。对 $k$ 取期望后仍严格大于 $\tfrac12$。

（注：关键不是"有限密钥下分布必不同"这类计数论证，而是**完美正确性**迫使 $p_0\ne p_1$；加密预言机让敌手能把这两个分布精确学到手。）故完全 CPA 保密不可达。$\blacksquare$

---

## 习题 3.19　基于 PRP 的随机化方案 CPA 安全

> **题目**　$\mathsf{Enc}_k(m)$：均匀 $r\in\{0,1\}^{n/2}$，$c=F_k(r\|m)$（$|m|=n/2$）。给出解密并证 CPA 安全。

**解密**：$\mathsf{Dec}_k(c)=F_k^{-1}(c)$ 的后 $n/2$ 比特（$F_k^{-1}(c)=r\|m$，丢弃前 $n/2$ 比特 $r$）。正确性：$\mathsf{Dec}_k(\mathsf{Enc}_k(m))=F_k^{-1}(F_k(r\|m))$ 的后半 $=m$。

**CPA 安全**。归约到 $F$ 的伪随机性。先把 $F_k$ 换成均匀置换 $f\leftarrow\mathsf{Perm}_n$，由 PRP 安全引敌手优势仅多 $\mathsf{negl}$。在均匀置换下，每次加密取均匀 $r$（$n/2$ 比特）输出 $f(r\|m)$。对 $m_b$，密文 $=f$ 在某均匀点 $r\|m_b$ 的像。由于 $f$ 是均匀置换，$f(r\|m_b)$ 对未知 $f$ 而言均匀——**只要各加密（预言机查询与挑战）所用输入点 $r\|m$ 互不碰撞**。两个不同加密使用相同 $r\|m$ 当且仅当 $r$ 相同且 $m$ 相同；对至多 $q(n)$ 次查询，$r$ 碰撞概率 $\le q(n)^2/2^{n/2}$（生日界，可忽略）。无碰撞时所有密文是独立均匀 $n$ 比特串，方案完全保密（信息论），敌手优势 0。

合并：$\Pr[\mathsf{PrivK}^{\mathsf{cpa}_{\mathcal{A},\Pi}}(n)=1]\le\tfrac12+\mathsf{negl}(n)$。$\blacksquare$

---

## 习题 3.20　判断 EAV / CPA 安全

> **题目**　$F$ 保长 PRF，$G$ PRG（扩张 $n+1$）。各方案是否 EAV / CPA 安全（密钥均匀 $k\in\{0,1\}^n$）。

**(a) 加密 $m\in\{0,1\}^{n+1}$：均匀 $r\in\{0,1\}^n$，输出 $\langle r,G(r)\oplus m\rangle$。**
**既非 EAV 也非 CPA 安全。** 密钥 $k$ 根本未用；pad 是 $G(r)$，而 $r$ 明文写在密文里。任何拿到密文 $\langle r,s\rangle$ 的人都能自行计算 $G(r)$（$G$ 公开），由 $s\oplus G(r)=m$ 直接还原明文。敌手读出 $m_b$，成功概率 1。

**(b) 加密 $m\in\{0,1\}^n$：$c=m\oplus F_k(0^n)$。**
**EAV 安全，非 CPA 安全。** 确定性加密，pad 恒为 $F_k(0^n)$。
- EAV：挑战 $c=m_b\oplus F_k(0^n)$，$F_k(0^n)$ 对敌手伪随机，$c$ 近一次性密码本，故 EAV 安全（归约同定理 3.16）。
- CPA：敌手先查询任意 $m$ 得 $c=m\oplus F_k(0^n)$，算出 $F_k(0^n)=c\oplus m$；再对挑战 $c^*=m_b\oplus F_k(0^n)$ 解出 $m_b$。成功概率 1。（多次加密 EAV 同样不安全。）

**(c) 加密 $m\in\{0,1\}^{2n}$：$m=m_1\|m_2$，均匀 $r\in\{0,1\}^n$，$c=\langle r,m_1\oplus F_k(r),m_2\oplus F_k(r+1)\rangle$。**
**EAV 安全且 CPA 安全。** 这是 CTR 模式（计数器 $r,r+1$）。归约：换 $F_k$ 为均匀 $f$，$f(r),f(r+1)$ 在两个不同输入上独立均匀；CPA 下至多 $q$ 次查询，各计数器点 $\{r_i,r_i+1\}$ 间碰撞概率 $\le(2q)^2/2^n$（生日界，可忽略）；无碰撞时每块 pad 独立均匀，信息论安全。故 CPA 安全（标准 CTR 安全性）。$\blacksquare$

---

## 习题 3.21　构造 3.28 用 $F_k(x)=k\oplus x$ 非 CPA 安全

> **题目**　$\Pi$ 为构造 3.28（$\langle r,F_k(r)\oplus m\rangle$），$F$ 取自例 3.25（$F_k(x)=k\oplus x$）。

CPA 敌手 $\mathcal{A}$：

1. 查询加密预言机得任意 $m$ 的密文 $\langle r,F_k(r)\oplus m\rangle=\langle r,k\oplus r\oplus m\rangle$，由 $m,r$ 已知算出 $k$（$k=(k\oplus r\oplus m)\oplus r\oplus m$）；
2. 选 $m_0,m_1$，收到挑战 $\langle r^*,F_k(r^*)\oplus m_b\rangle$，用已知 $k$ 计算 $F_k(r^*)=k\oplus r^*$，解出 $m_b$。

成功概率 1，非 CPA 安全。$\blacksquare$

---

## 习题 3.22　状态加密的 CPA 安全定义 + 同步流密码模式

> **题目**　(a) 给出状态加密 CPA 安全定义；(b) 同步流密码模式满足之。

**(a) 定义**。状态加密方案 $(\mathsf{Init},\mathsf{Enc},\mathsf{Dec})$：$\mathsf{Init}$ 生成初始状态 $\mathsf{st}$；$\mathsf{Enc}$ 接受密钥与状态，输出密文与更新后状态。CPA 实验 $\mathsf{PrivK}^{\mathsf{cpa}}_{\mathcal{A},\Pi}(n)$：

1. $\mathsf{Gen}(1^n)$ 生成 $k$；$\mathsf{st}\leftarrow\mathsf{Init}(k)$（发送方状态）；
2. $\mathcal{A}^{E_k(\cdot)}(1^n)$ 可查询加密预言机（每次更新状态），输出等长 $m_0,m_1$；
3. 均匀 $b$，发送方用当前状态加密 $m_b$ 得挑战 $c$（状态相应更新）；
4. $\mathcal{A}$ 继续访问预言机，输出 $b^{\prime}$；
5. 实验 1 当 $b^{\prime}=b$。

方案 CPA 安全若对所有 PPT $\mathcal{A}$，$\Pr[\mathsf{PrivK}^{\mathsf{cpa}}=1]\le\tfrac12+\mathsf{negl}$。（关键：通信双方状态同步前进；预言机与挑战共用同一递增状态。）

**(b)** 同步流密码模式：发送、接收方共享流密码输出流 $y_1,y_2,\ldots$（伪随机），第 $i$ 条消息 $m$ 的密文 $c=m\oplus y_i$（用流中下一段与 $m$ 等长部分异或）。归约：若 $\mathcal{A}$ 以 $\varepsilon$ 攻破，则把流密码输出换成真随机带时方案为一次性密码本（完全保密），$\mathcal{A}$ 优势 0；由流密码安全性，真随机与伪随机不可区分，故 $\mathcal{A}$ 在真方案下优势 $\le\varepsilon_{\text{stream}}+\mathsf{negl}$ 可忽略。$\blacksquare$

---

## 习题 3.23　非同步流密码模式（构造 3.31）CPA 安全

> **题目**　Prove that the unsynchronized stream-cipher mode of operation (Construction 3.31) is CPA-secure if the underlying stream cipher is secure.
> **题目**　证明：如果底层流密码是安全的，非同步流密码工作模式（构造 3.31）是 CPA 安全的。

构造 3.31（即 CTR 思想）：每次加密用新鲜均匀 nonce $r$，输出 $\langle r, F_k(r)\oplus m\rangle$（多块则 $F_k(r),F_k(r+1),\ldots$）。归约同定理 3.30/CTR 安全性证明：换 $F_k$ 为均匀 $f$，各加密用独立均匀 $r$，至多 $q$ 次查询时计数器集合碰撞概率 $\le(q\ell)^2/2^n$（$\ell$ 块数，可忽略），无碰撞即信息论完全保密；$F$ 是 PRF 使替换仅引入 $\mathsf{negl}$ 偏差。故 CPA 安全。$\blacksquare$

---

## 习题 3.24　一个流密码构造的安全性

> **题目**　$\mathsf{Init}(s,IV)$ 输出 $\mathsf{st}=(s,IV)$；$\mathsf{Next}(s,IV)$ 输出 $y=F_s(IV)$，$\mathsf{st}^{\prime}=(s,IV+1)$。证明该流密码不安全。

**先明确判定标准（§3.6.1）。** KL 对"接受 IV 的流密码"的安全性定义是：均匀选取种子 $s$ 后，$\mathsf{Init}(s,\cdot)$ 可在**不同的 $IV$ 上反复运行**，要求所得各输出流看起来**相互独立均匀**。形式化地，定义 keyed function

$$F^{\ell}_s(IV)\overset{\mathrm{def}}{=}\mathsf{GetBits}_1(\mathsf{Init}(s,IV),1^{\ell}),$$

流密码安全当且仅当 $F^{\ell}$ 对任意多项式 $\ell$ 是**伪随机函数**（以 $IV$ 为输入）。注意：该定义天然允许敌手**自选多个 $IV$**（PRF 实验），而非只观测单段流。

本构造的输出流为 $F_s(IV),F_s(IV+1),F_s(IV+2),\ldots$，即

$$F^{\ell}_s(IV)=F_s(IV)\,\|\,F_s(IV+1)\,\|\,\cdots\,\|\,F_s(IV+\ell-1).$$

**攻击（不同 $IV$ 的计数器区间重叠）。** 区分器 $D$ 查询两个点：

- $IV$：得 $y_1\|y_2\|\cdots\|y_\ell$，其中 $y_i=F_s(IV+i-1)$；
- $IV+1$：得 $z_1\|z_2\|\cdots\|z_\ell$，其中 $z_i=F_s(IV+i)$。

则恒有 $z_i=y_{i+1}$（$i=1,\ldots,\ell-1$）：**第二段流就是第一段流左移一个分组**。$D$ 检验 $z_1\|\cdots\|z_{\ell-1}\overset?=y_2\|\cdots\|y_\ell$：

- $\mathcal O=F^{\ell}_s$：恒成立，$\Pr[D=1]=1$；
- $\mathcal O=f$（均匀函数）：两次调用的输出是独立均匀串，该等式成立概率 ${2}^{-n(\ell-1)}$。

优势 ${1}-2^{-n(\ell-1)}$，不可忽略，故 $F^{\ell}$ 不是 PRF，流密码不安全。$\blacksquare$

**两点澄清（回应原"存疑"）。**

1. **不需要"$IV$ 重复"。** 同一 $IV$ 重复初始化当然也使两流完全相同，但上面的攻击只用两个**不同**的 $IV$（$IV$ 与 $IV+1$），更本质：构造用 $IV+i$ 作 $F_s$ 的输入，使不同 $IV$ 的计数器区间 $[IV,IV+\ell)$ 可以重叠。对照构造 3.30：它用 ${3}n/4$ 比特 $IV$ 拼接计数器 $F_s(IV\|\langle i\rangle)$，不同 $IV$ 的求值点天然**不相交**，因而安全。
2. **与 CTR 模式不矛盾。** 若把实验换成"单次会话、$IV$ 均匀、只观测一段流"，该构造确实可证伪随机（就是 CTR 密钥流）；事实上以它为密钥流的非同步加密方案（构造 3.31 式，每次加密均匀新鲜选 $IV$）仍是 CPA 安全的。但 KL §3.6.1 对流密码的安全定义更强——要求**自选多 $IV$** 下输出流独立均匀（$F^\ell$ 是 PRF），本构造不满足。这说明"流密码安全（KL 定义）"是相应加密模式 CPA 安全的**充分而非必要**条件。

> **官方题解印证**（第三版教师手册）：取 $\ell=2n$，则 $G^{2n}_s(IV)=F_s(IV)\|F_s(IV+1)$，于是 $G^{2n}_s(IV)$ 的后半与 $G^{2n}_s(IV+1)$ 的前半恒等，立即可区分——与上面的移位攻击相同。

---

## 习题 3.25　$c_i=F_k(IV+i+m_i)$ 非 EAV 安全

> **题目**　$F$ 为伪随机置换，均匀 $IV\in\{0,1\}^n$，$c_i=F_k(IV+i+m_i)$（加法模 ${2}^n$）。证明非 EAV 安全。

**攻击（两块消息）。** EAV 敌手输出 $m_0=(0,1)$、$m_1=(1,0)$（各两块，等长）。挑战密文 $(c_1,c_2)$：

- $b=0$：$c_1=F_k(IV+1+0)=F_k(IV+1)$，$c_2=F_k(IV+2+1)=F_k(IV+3)$；
- $b=1$：$c_1=F_k(IV+1+1)=F_k(IV+2)$，$c_2=F_k(IV+2+0)=F_k(IV+2)$。

$F_k$ 是**置换**：$b=0$ 时 $IV+1\not\equiv IV+3\pmod{2^n}$（$n\ge2$），故 $c_1\ne c_2$ 恒成立；$b=1$ 时 $c_1=c_2$ 恒成立。敌手输出 ${1}$ 当且仅当 $c_1=c_2$，成功概率 ${1}$。故非 EAV 安全。$\blacksquare$

---

## 习题 3.26　CBC 模式密文长度

> **题目**　分组密码 256 比特密钥、128 比特分组，CBC 加密 1024 比特消息。

消息 1024 比特 $= 8$ 个 128 比特块。CBC 密文 $=$ IV（1 块，128 比特）$+$ 8 个密文块 $= 9\times128=1152$ 比特 $=144$ 字节。（密钥长度 256 比特不影响密文长度。）$\blacksquare$

---

## 习题 3.27　式 (3.13) 的归约细节

> **题目**　给出 CTR 模式（构造 3.28 的多块/CPA 版）式 (3.13) 的归约证明。

式 (3.13) 形如 $\Pr[\mathsf{PrivK}^{\mathsf{cpa}}_{\mathcal{A},\Pi}(n)=1]\le\tfrac12+\mathsf{Adv}_{D}(n)+\dfrac{q(n)^2}{2^n}$，其中 $q$ 为 $\mathcal{A}$ 的加密预言机查询数，$\mathsf{Adv}_D$ 为 PRF 区分优势。

**归约**。设 $\mathcal{A}$ 攻破 $\Pi$（CTR，pad 为 $F_k(IV),F_k(IV+1),\ldots$）。构造 PRF 区分器 $D$：访问 $\mathcal O\in\{F_k,f\}$，模拟 $\mathsf{PrivK}^{\mathsf{cpa}}$：

1. $\mathcal A$ 每次加密查询消息 $m$（$\ell$ 块），$D$ 自选均匀 $IV$，对 $j=0,\ldots,\ell-1$ 查询 $\mathcal O(IV+j)$ 得 pad 块，与 $m$ 的块异或得密文，返回给 $\mathcal A$；
2. 挑战 $m_0,m_1$ 同理：$D$ 选均匀 $IV^*$，用 $\mathcal O(IV^*+j)$ 加密 $m_b$；
3. 输出 $\mathcal A$ 的猜测 $b^{\prime}$；$D$ 据此猜 $\mathcal O$ 是 $F_k$ 还是 $f$。

**分析**。若 $\mathcal O=F_k$：$D$ 完美模拟真方案，$\Pr[D^{F_k}=1\mid\mathcal A\ \text{成功}]$ 反映 $\mathcal A$ 真实优势。若 $\mathcal O=f$ 均匀：各 pad 块为 $f$ 在不同点取值，**只要所有查询点 $IV+j$ 互不碰撞**即独立均匀，方案退化为信息论一次性密码本，$\mathcal A$ 优势 0。碰撞事件 $\mathsf{coll}$：至多 $q\ell$ 个计数器点中存在相等，由生日界 $\Pr[\mathsf{coll}]\le(q(n)\ell)^2/2^{n+1}\le q(n)^2/2^n$（取每查询块数 $\ell$ 为常数或吸收）。由联合界：

$$\Pr[\mathsf{PrivK}^{\mathsf{cpa}}_{\mathcal A,\Pi}=1]\le\Pr[\mathsf{coll}]+\tfrac12\le\tfrac12+\tfrac{q(n)^2}{2^n}.$$

把"用 $f$"时 $\mathcal A$ 的优势（0，条件不碰撞）与"用 $F_k$"时的优势相减，得 $\mathsf{Adv}_D\ge\mathsf{Adv}_{\mathcal A}-q(n)^2/2^n$。故 $\mathsf{Adv}_{\mathcal A}\le\mathsf{Adv}_D+q(n)^2/2^n$，即式 (3.13)。$\blacksquare$

---

## 习题 3.28　弱伪随机函数

> **题目**　$g^{\$}$：输入 ${1}^n$，均匀 $r$，返回 $\langle r,g(r)\rangle$。$F$ 弱 PRF：$|Pr[D^{F_k^{\$}}=1]-Pr[D^{f^{\$}}=1]|\le\mathsf{negl}$。

**(a) PRF $\Rightarrow$ 弱 PRF**。弱 PRF 仅给敌手**随机输入点**上的取值（$r$ 由 $g^{\$}$ 自选均匀），而 (强) PRF 抵抗敌手**自选输入点**。自选输入是更强能力，故 PRF $\Rightarrow$ 弱 PRF。归约：$D$ 访问 $F_k$（或 $f$），自行模拟 $g^{\$}$：每次均匀选 $r$，查询 $\mathcal O(r)$，返回 $\langle r,\mathcal O(r)\rangle$。$\mathcal O=F_k$ 即 $F_k^{\$}$，$\mathcal O=f$ 即 $f^{\$}$，优势完全传递。

**(b) $F_k(x)=F^{\prime}_k(x)$（$x$ 偶），$F^{\prime}_k(x+1)$（$x$ 奇）**。$F$ 不是 PRF：查询 $x$ 与 $x+1$（$x$ 偶），得 $F_k(x)=F^{\prime}_k(x)$、$F_k(x+1)=F^{\prime}_k(x)$，二者**相等**；均匀 $f$ 时 $f(x),f(x+1)$ 独立，相等概率 ${2}^{-n}$。区分器检测相邻偶/奇点输出相等，优势 $\approx1$。

$F$ 是弱 PRF：$g^{\$}$ 给的输入 $r$ 均匀，$F_k(r)$ 仅在 $r$ 偶时 $=F^{\prime}_k(r)$、$r$ 奇时 $=F^{\prime}_k(r+1)$（$=F^{\prime}_k$ 在偶点 $r+1$ 的值）。对均匀 $r$，无论奇偶 $F_k(r)$ 都是 $F^{\prime}_k$ 在某均匀**偶**点上的值——偶点分布是 $\{0,1\}^n$ 上的近均匀（差一个最低位），且各次 $r$ 独立时偶点几乎不碰撞，故 $F_k^{\$}$ 与 $F_k'^{\$}$ 分布几乎相同；$F^{\prime}$ 是 PRF $\Rightarrow$ 弱 PRF，传递得 $F$ 弱 PRF。

**(c) CTR 用弱 PRF 未必 CPA 安全**。CTR 模式中加密预言机使敌手**自选明文**，对应 pad 输入 $IV$ 虽由加密方均匀选取，但敌手通过已知明文可得 $\langle IV,F_k(IV)\rangle$——$IV$ 均匀，看似仅需弱 PRF。但 CTR 的多块用 $IV,IV+1,\ldots$，其中 $IV+1,IV+2$ **不是均匀独立**的点（一旦 $IV$ 均匀，$IV+1$ 也均匀但与 $IV$ 相关）。弱 PRF 仅保证**独立均匀**点上的伪随机性，不保证 $IV$ 与 $IV+1$ 联合伪随机。用 (b) 的 $F$：取 $IV$ 偶，则 $F_k(IV)=F^{\prime}_k(IV)$、$F_k(IV+1)=F^{\prime}_k(IV)$ 相等，两块 pad 相同 $\Rightarrow$ 加密 $m_1\|m_2$ 时 $c_1\oplus c_2=m_1\oplus m_2$ 泄露明文关系。故 CTR 用弱 PRF **不**必 CPA 安全。

**(d) 构造 3.28 用弱 PRF 仍 CPA 安全**。构造 3.28 每块加密用**新鲜均匀** $r$（非 $IV+i$），即 $\langle r,F_k(r)\oplus m\rangle$，$r$ 每次独立均匀。这恰是 $g^{\$}$ 语义：敌手得到 $\langle r,F_k(r)\rangle$，$r$ 均匀独立。归约：$D$ 模拟 CPA 实验，对每次加密自选均匀 $r$ 查询 $\mathcal O^{\$}$ 得 $\langle r,\mathcal O(r)\rangle$。$\mathcal O=F_k$ 模拟真方案；$\mathcal O=f$ 均匀时各 pad 独立均匀（$r$ 互不碰撞概率由生日界控制），信息论安全。故 $\mathsf{Adv}_{\mathcal A}\le\mathsf{Adv}_D+q^2/2^n$。弱 PRF $\Rightarrow$ 构造 3.28 CPA 安全。$\blacksquare$

---

## 习题 3.29　单比特翻转的影响

> **题目**　What is the effect of a single bit flip in the ciphertext when using the CBC, OFB, and CTR modes of operation?
> **题目**　使用 CBC、OFB 和 CTR 工作模式时，密文中的单个比特翻转会产生什么影响？

| 模式 | 单比特翻转影响 |
|---|---|
| CBC | 翻转密文块 $c_i$ 的若干比特：对应**明文块 $m_i$** 的相同比特被翻转（$m_i=F_k^{-1}(c_i)\oplus c_{i-1}$，$c_i$ 进入 $F_k^{-1}$ 经扩散使 $m_i$ 整块"乱"，而 $m_{i+1}=F_k^{-1}(c_{i+1})\oplus c_i$ 中 $c_i$ 直接异或，故 $m_{i+1}$ 的对应比特精确翻转）。即：$m_i$ 整块损坏、$m_{i+1}$ 受控单比特翻转、其余块不受影响。 |
| OFB | pad 与密文无关（pad 由 $IV$ 经反复 $F_k$ 生成），翻转 $c_i$ 比特仅翻转 $m_i$ 对应比特，其余明文块完全不受影响。 |
| CTR | 同 OFB：pad 由 $IV+i$ 生成与密文无关，翻转 $c_i$ 比特精确翻转 $m_i$ 对应比特，其余块不受影响。 |

$\blacksquare$

---

## 习题 3.30　丢弃一个密文块的影响

> **题目**　What is the effect of a dropped ciphertext block (e.g., if the transmitted ciphertext $c_1, c_2, c_3, \ldots$ is received as $c_1, c_3, \ldots$) when using the CBC, OFB, and CTR modes of operation?
> **题目**　使用 CBC、OFB 和 CTR 工作模式时，丢失一个密文分组（例如，传输的密文 $c_1, c_2, c_3, \ldots$ 被接收为 $c_1, c_3, \ldots$）会产生什么影响？

设传输 $c_1,c_2,c_3,\ldots$，接收为 $c_1,c_3,\ldots$（丢弃 $c_2$）。

- **CBC**：解密 $m_i=F_k^{-1}(c_i)\oplus c_{i-1}$。$c_2$ 丢失后，$c_3$ 被当作第二块，$m^{\prime}_2=F_k^{-1}(c_3)\oplus c_1\ne m_3$；后续所有块 $m^{\prime}_i=F_k^{-1}(c_{i+1})\oplus c_i$（错位）全错。**自丢失处起全部明文损坏且错位**，且无法恢复同步。
- **OFB**：pad 序列 $y_1,y_2,y_3,\ldots$ 与密文块独立（由 $IV$ 生成）。$m_i=c_i\oplus y_i$。丢弃 $c_2$ 后，接收方仍按 $y_1,y_2,y_3,\ldots$ 解密：$m^{\prime}_1=c_1\oplus y_1=m_1$ 正确，$m^{\prime}_2=c_3\oplus y_2\ne m_3$（pad 错位）。**自丢弃处起所有后续明文错位损坏**（pad 流与密文流失同步）。
- **CTR**：同 OFB，pad 流 $F_k(IV+1),F_k(IV+2),\ldots$ 与密文独立。丢弃密文块使后续 pad 与密文错位，**自丢弃处起全部后续明文损坏**。

（CBC 还丢失了块间链接关系；OFB/CTR 问题是 pad 与密文失步。）$\blacksquare$

---

## 习题 3.31　CTR 变体 $c_i=m_i\oplus F_k(IV+i)$ CPA 安全

> **题目**　Consider a variant of CTR mode where a uniform $IV \in \{0,1\}^n$ is chosen and the $i$th ciphertext block is computed as $c_i := m_i \oplus F_k(IV + i)$. Prove that this variant is CPA-secure. What concrete-security bound do you obtain?
> **题目**　考虑 CTR 模式的一个变体：选择一个均匀的 $IV \in \{0,1\}^n$，第 $i$ 个密文分组计算为 $c_i := m_i \oplus F_k(IV + i)$。证明该变体是 CPA 安全的，并说明得到的具体安全界。

该变体与标准 CTR 一致。归约同习题 3.27：换 $F_k$ 为均匀 $f$，各 $F_k(IV+i)$ 在不同 $(IV+i)$ 上独立均匀；至多 $q$ 次查询、每次 $\ell$ 块，计数器点碰撞概率 $\le(q\ell)^2/2^{n+1}$（生日界）。无碰撞时信息论完全保密。故 CPA 安全。

**具体安全界**：$\Pr[\mathsf{PrivK}^{\mathsf{cpa}}=1]\le\tfrac12+\mathsf{Adv}^{\mathsf{PRF}}_{F}(n)+\dfrac{(q(n)\cdot\ell(n))^2}{2^{n+1}}$，其中 $q$ 为加密查询数、$\ell$ 为消息块数上界。$\blacksquare$

---

## 习题 3.32　习题 3.31 方案作 nonce 加密（nonce 作 IV）不安全

> **题目**　Show that the scheme from Exercise 3.31 is not secure as a nonce-based encryption scheme if the nonce is used as the IV.
> **题目**　证明：如果使用 nonce 作为 IV，习题 3.31 中的方案作为基于 nonce 的加密方案是不安全的。

nonce 加密要求 nonce 不重复（但可由敌手选择）。若敌手选同一 nonce $=IV$ 加密两条不同消息，则两次 pad 完全相同 $F_k(IV+1),F_k(IV+2),\ldots$，密文异或即明文异或，泄密。具体：敌手选 nonce $N$，先"加密预言机"得 $m_0$ 的密文 $c=m_0\oplus\mathsf{pad}$（pad 从 $F_k(N+1)$ 起）；再用同一 $N$ 作挑战，得 $c^*=m_b\oplus\mathsf{pad}$；$c\oplus c^*=m_0\oplus m_b$ 判定 $b$。故 nonce 模式下不安全。$\blacksquare$

---

## 习题 3.33　CBC 作 nonce 加密（nonce 作 IV）不安全

> **题目**　Show that CBC mode is not secure as a nonce-based encryption scheme if the nonce is used as the IV.
> **题目**　证明：如果使用 nonce 作为 IV，CBC 模式作为基于 nonce 的加密方案是不安全的。

CBC 中 $c_0=IV$。nonce 模式允许敌手选 nonce $N$ 作 IV 且可重复使用。CBC 加密单块：$c_1=F_k(m_1\oplus IV)$。

敌手用**同一 IV** 加密两条单块消息 $m_0,m_1$（先查询 $m_0$ 得 $c=F_k(m_0\oplus IV)$，再以同 IV 挑战 $m_b$ 得 $c^*=F_k(m_b\oplus IV)$）。若 $m_0\oplus IV\ne m_b\oplus IV$（即 $m_0\ne m_b$，一般成立），因 $F_k$ 置换，$c\ne c^*$；但这只说明不同。如何判 $b$？取 $m_0,m_1$ 使 $m_0\oplus IV$ 与 $m_1\oplus IV$ 满足某可检测关系不行（$F_k$ 不可逆预测）。

改用：敌手选 IV $=0^n$、消息 $m_0=0^n$、$m_1=x$（任意非零）。查询 $m_0$ 得 $c_0=F_k(0^n\oplus0^n)=F_k(0^n)$。挑战：$b=0\Rightarrow c^*=F_k(0^n)=c_0$；$b=1\Rightarrow c^*=F_k(x)\ne c_0$（置换）。敌手检测 $c^*\overset?=c_0$：$b=0$ 时恒等、$b=1$ 时恒不等，成功概率 1。故 CBC nonce 模式（IV 复用）不安全。$\blacksquare$
