# 第五章　习题解答

> *Introduction to Modern Cryptography (3rd ed.), Katz & Lindell — Chapter 5 Exercises*

---

## 习题 5.1　CBC/OFB/CTR 不是 CCA 安全的

> **题目**　Show that the CBC, OFB, and CTR modes do not give CCA-secure schemes.
> **题目**　证明 CBC、OFB 和 CTR 工作模式不能得到 CCA 安全的方案。

三者都具有**可塑性（malleability）**：对密文做受控修改会使明文按可预测方式变化。CCA 敌手利用解密预言机（查询任意非挑战密文）即可据此区分。

**统一攻击**（取单块，$m_0=0^n,m_1=1^n$）。

CBC：$c^*=\langle IV^*,c_1^*\rangle$，明文 $m=F_k^{-1}(c_1^*)\oplus IV^*$，故修改 $IV$ 直接翻转明文。敌手取 $c^{\prime}=\langle IV^*\oplus1^n,c_1^*\rangle$（$c^{\prime}\ne c^*$，允许查询），解密预言机返回 $m^{\prime}=F_k^{-1}(c_1^*)\oplus(IV^*\oplus1^n)=m_b\oplus1^n$。若 $b=0$ 则 $m^{\prime}=1^n$，若 $b=1$ 则 $m^{\prime}=0^n$；敌手判定 $b$，成功概率 1。

OFB/CTR：pad 流与密文无关，$m=c\oplus\mathsf{pad}$。挑战 $c^*=m_b\oplus\mathsf{pad}^*$。敌手取 $c^{\prime}=c^*\oplus1^n$（$\ne c^*$），解密返回 $m^{\prime}=c^{\prime}\oplus\mathsf{pad}^*=m_b\oplus1^n$。同样判定 $b$，成功概率 1。

三者皆非 CCA 安全。$\blacksquare$

---

## 习题 5.2　CBC 填充预言机攻击伪代码（3 分组）

> **题目**　Write pseudocode for obtaining the entire plaintext for a 3-block ciphertext via a padding-oracle attack on CBC with PKCS #7.
> **题目**　编写伪代码：通过对 CBC 的 PKCS #7 填充预言机攻击，恢复一个 3 分组密文的完整明文。

输入：观察到的 3 分组密文 $\langle IV,c_1,c_2\rangle$（即 2 块编码数据 $m_1,m_2$，各 $L$ 字节），可访问填充预言机 $\mathcal{O}(c)$ 返回"填充是否正确"。记 $F_k^{-1}$ 的作用通过预言机反映。

```
PaddingOracle(c):                          # 返回 True 当且仅当填充正确
    return query_server(c)

# ---- 第一步：求 m_2 的填充字节数 b ----
def find_padding_length(IV, c1, c2):
    for pos in 0..L-1:                     # 修改 c1 的第 pos 字节
        c1' = c1
        c1'[pos] ^= 1                      # 翻转一个比特/字节
        if not PaddingOracle(<IV, c1', c2>):# 填充被破坏
            return L - pos                  # 最左被破坏位置揭示 b

# ---- 第二步：逐字节恢复 m_2，然后 m_1 ----
def recover_block(Cprev, Ccur):            # 恢复 Enc(Cprev XOR m) 中的 m，Cprev 是前一密文块
    m = [0]*L
    b = L                                  # 目标填充值，从 1 到 L
    for k in 1..L:                         # 恢复倒数第 k 字节（目标使末 k 字节均为 k）
        padval = k
        # 构造 Cprev' 使 (解密结果) 末 k 字节均为 padval
        for i in (L-k+1)..L:               # 已恢复字节 + 当前字节
            Cprev'[i] = Ccur_intermediate[i] XOR padval   # 调整使明文第 i 字节 = padval
        # 在剩余可能值中扫描第 (L-k) 字节（即 m 的倒数第 k 字节）
        for guess in 0..255:
            Cprev'[L-k] = guess
            if PaddingOracle(<Cprev', Ccur>):  # 填充正确 ⇒ intermediate[L-k] XOR guess = padval
                m[L-k] = guess XOR padval XOR original_intermediate[L-k]
                record intermediate[L-k] = guess XOR padval
                break
    return m

m2 = recover_block(c1, c2)
m1 = recover_block(IV, c1)
plaintext = decode_pad(m1 || m2)           # 剥离 PKCS #7 填充
```

 核心：对每个目标字节，利用填充预言机二分/穷举 256 个候选值，使末尾形成合法填充（$\mathtt{0x}k\cdots\mathtt{0x}k$），从而由"填充正确"反推出中间值 $F_k^{-1}(c_i)$ 的对应字节，再 XOR 前一密文块得明文字节。3 分组（$IV,c_1,c_2$）共 ${2}L$ 字节明文，每字节至多 256 次查询，总计 $\le512L$ 次。$\blacksquare$

---

## 习题 5.3　CTR 模式的填充预言机攻击

> **题目**　CTR + PKCS #7 填充，描述填充预言机攻击。

CTR 模式：$c_i=m_i\oplus F_k(IV+i)$。填充在加密前施加，故明文 $m$（含填充）与 pad 异或得 $c$。敌手观察 $c=\langle IV,c_1,\ldots\rangle$，pad 流 $p_i=F_k(IV+i)$。

**攻击**：CTR 中修改 $c_i$ 的某比特直接翻转 $(m\text{ 的对应比特})$（因 $m_i=c_i\oplus p_i$，$p_i$ 不变）。敌手可受控修改明文的填充字节。填充预言机检验的是**解密后明文的填充**是否合法。

逐字节恢复：对最后一块 $c_\ell$（含填充），要恢复其明文字节 $m_\ell[j]$。CTR 下 $m_\ell[j]=c_\ell[j]\oplus p_\ell[j]$。敌手不知 $p_\ell[j]$，但可**调整 $c_\ell[j]$** 使末尾形成合法填充：枚举 $c_\ell[L]$（最后字节）使 $m_\ell[L]=\mathtt{0x01}$（合法 1 字节填充）——填充预言机返回正确时，$m_\ell[L]=c_\ell[L]\oplus p_\ell[L]=\mathtt{0x01}$，解出 $p_\ell[L]$；进而 $m_\ell[L]_{\text{原}}=c_\ell[L]_{\text{原}}\oplus p_\ell[L]$。逐字节向前推进（构造末 $k$ 字节均 $=0xk$）。每字节 256 次查询。

（与 CBC 不同，CTR 的 pad 与密文块无关，故无需"中间值"——直接得 pad 字节，再还原明文。）$\blacksquare$

---

## 习题 5.4　构造 5.6 用非强安全 MAC 时不 CCA 安全

> **题目**　Construction 5.6（encrypt-then-authenticate）用安全但非强安全 MAC，未必 CCA 安全。

构造 5.6：密文 $\langle c,t\rangle$，$c=\mathsf{Enc}_{k_E}(m)$，$t=\mathsf{Mac}_{k_M}(c)$；解密先验 $t$，通过则解密 $c$。强安全 MAC 保证敌手不能产生**任何**新有效 $(c,t)$。若 MAC 仅安全（非强），敌手可能在**已认证密文 $c$** 上产生**新标签** $t^{\prime}\ne t$ 使 $\mathsf{Vrfy}_{k_M}(c,t^{\prime})=1$。

构造反例 MAC（习题 4.4）：$\mathsf{Mac}^{\prime}_k(c)=F_k(c)$（PRF），$\mathsf{Vrfy}_k(c,t)=1$ 当 $t=F_k(c)$ 或 $t=F_k(c)[1..n-1]$（截断也接受）。这是安全但非强安全 MAC。CCA 攻击：

1. 加密预言机对 $m_0=0^n,m_1=1^n$ 之一得挑战 $\langle c^*,t^*\rangle$。敌手构造 $t^{\prime}^*=$ $t^*$ 的前 $n-1$ 位（截断）。因 $\mathsf{Vrfy}_{k_M}(c^*,t^{\prime}^*)=1$（截断分支），且 $\langle c^*,t^{\prime}^*\rangle\ne\langle c^*,t^*\rangle$（挑战密文），故 $\langle c^*,t^{\prime}^*\rangle$ **允许**查询解密预言机！
2. 解密预言机返回 $\mathsf{Dec}_{k_E}(c^*)=m_b$，敌手直接得知 $m_b$，判定 $b$，成功概率 1。

故非强安全 MAC 使构造 5.6 不 CCA 安全。$\blacksquare$

---

## 习题 5.5　构造 5.6 用任意加密 + 任意安全 MAC 仍不可伪造

> **题目**　Construction 5.6 with any encryption scheme and any secure MAC is unforgeable.
> **题目**　构造 5.6（encrypt-then-authenticate）配合任意加密方案与任意安全 MAC 都是不可伪造的。

不可伪造（定义 5.2）：敌手获加密预言机，输出 $(c,t)$，成功当 $m=\mathsf{Dec}_{k_E}(c)\ne\bot$ 且 $m\notin\mathcal{Q}$（$\mathcal{Q}$ 为加密预言机加密过的消息集）。

构造 5.6 的 $\mathsf{Vrfy}_{k_M}(c,t)=1\Rightarrow t$ 是 $c$ 的有效 MAC 标签。加密预言机对 $m_i$ 返回 $\langle c_i,t_i\rangle$，$t_i=\mathsf{Mac}_{k_M}(c_i)$，故敌手已知的有效 (密文,标签) 对为 $\{(c_i,t_i)\}$，对应密文集合 $\{c_i\}$。

敌手输出 $(c^*,t^*)$ 有效 $\Rightarrow$ $\mathsf{Vrfy}_{k_M}(c^*,t^*)=1$，即 $(c^*,t^*)$ 是对密文 $c^*$ 的有效 MAC。若 $c^*\notin\{c_i\}$（新密文），则 $(c^*,t^*)$ 是 MAC 在**新消息** $c^*$ 上的伪造，违反 MAC 安全性。若 $c^*=c_i$（某已加密密文），则 $m^*=\mathsf{Dec}_{k_E}(c_i)=m_i\in\mathcal{Q}$，不满足 $m^*\notin\mathcal{Q}$，非成功伪造。

故敌手成功 $\Rightarrow$ $c^*$ 新 $\Rightarrow$ 违反 MAC 安全。**未用加密方案的安全性**（CPA 安全或任何性质都不需要），也**未用 MAC 的强安全性**（仅用基本安全，因密文 $c^*$ 是 MAC 的"消息"，$c^*$ 新即 MAC 消息新）。故任意加密 + 任意安全 MAC 即不可伪造。$\blacksquare$

---

## 习题 5.6　带解密预言机的加强不可伪造性

> **题目**　(a) 定义；(b) 构造 5.6 在 $\Pi_M$ 强安全时满足；(c) $\Pi_M$ 非强安全时未必满足。

**(a) 定义**。加强实验 $\mathsf{Enc\text{-}Forge}^{\mathsf{cca}}$：敌手获 $\mathsf{Enc}_k(\cdot)$ **与** $\mathsf{Dec}_k(\cdot)$ 两个预言机（解密预言机对挑战密文本身除外），最终输出 $(c^*,t^*)$（或对加密方案，输出密文 $c^*$）。成功当 $\mathsf{Dec}_k(c^*)\ne\bot$ 且 $c^*$ 不是先前从加密/解密预言机获得的。即：敌手不能产生任何**新的有效密文**，即使有解密预言机。

**(b) $\Pi_M$ 强安全 $\Rightarrow$ 构造 5.6 满足**。类似定理 5.7 中 Claim 5.8 的论证：强安全 MAC 保证敌手不能产生新有效 (密文,标签) 对 $(c^*,t^*)$，即使知道若干旧对。设 $\mathsf{ValidQuery}$ 为敌手输出新有效对的事件，则由 $\Pi_M$ 强安全（$\mathsf{Mac\text{-}sforge}$ 实验），$\Pr[\mathsf{ValidQuery}]$ 可忽略（归约：把敌手当 $\mathsf{Mac\text{-}sforge}$ 敌手，第一次新有效对即伪造）。故加强不可伪造成立。

**(c) $\Pi_M$ 非强安全 $\Rightarrow$ 未必满足**。反例同习题 5.4：截断标签也接受的 MAC。敌手用加密预言机得 $\langle c,t\rangle$；输出 $(c,t[1..n-1])$（截断标签）：$\mathsf{Vrfy}_{k_M}(c,t[1..n-1])=1$（截断分支），$(c,t[1..n-1])$ 是**新对**（标签不同于加密预言机返回的 $t$），故为加强意义下的"新有效密文"，伪造成功。$\blacksquare$

---

## 习题 5.7　authenticate-then-encrypt 是 CPA 安全且不可伪造

> **题目**　Authenticate-then-encrypt（先算 tag，再连同消息加密）用任意 CPA 安全加密 + 任意安全 MAC $\Rightarrow$ CPA 安全且不可伪造。

方案：$t=\mathsf{Mac}_{k_M}(m)$，$c=\mathsf{Enc}_{k_E}(m\|t)$。

**不可伪造**：敌手输出 $c^*$，$\mathsf{Dec}_{k_E}(c^*)=m^*\|t^*$，成功当 $m^*\notin\mathcal{Q}$ 且 $t^*$ 有效。但 CPA 敌手只有加密预言机（返回 $c_i=\mathsf{Enc}_{k_E}(m_i\|t_i)$），无从获得 MAC 预言机；然而不可伪造实验中敌手也是只有加密预言机。$c^*$ 解密出 $m^*\|t^*$，若 $m^*\notin\mathcal{Q}$ 且 $t^*=\mathsf{Mac}_{k_M}(m^*)$——敌手不知 $\mathsf{Mac}_{k_M}(m^*)$（无 MAC 预言机），猜中概率受 MAC 安全性控制（即使 $m^*$ 是新消息，输出有效 $t^*$ 概率可忽略）。归约：若敌手以 $\varepsilon$ 成功，则其输出含新消息 $m^*$ 上的有效标签 $t^*$，构造 MAC 伪造敌手（向加密预言机查询 $m^*$ 得 $c^*$，反推 $t^*$？需解密能力）。

更直接：因加密为 CPA 安全，$c^*$ 解密结果 $m^*\|t^*$ 中，$t^*$ 要有效（$=\mathsf{Mac}_{k_M}(m^*)$）而敌手无 MAC 预言机——本质上敌手输出的 $c^*$ 解密后含"猜测的 $t^*$"，命中真标签概率受 MAC 不可预测性限制（可忽略）。故不可伪造。

**CPA 安全**：加密的是 $m\|t$（$t$ 是 $m$ 的确定函数）。$\mathsf{Enc}_{k_E}$ 是 CPA 安全的，加密 $m\|t$ 与加密任意等长消息不可区分。形式化：若 CPA 敌手 $\mathcal{A}$ 以优势 $\varepsilon$ 区分 $m_0\|t_0$ 与 $m_1\|t_1$ 的加密（$t_b=\mathsf{Mac}_{k_M}(m_b)$），构造 CPA 攻击 $\Pi_E$ 的敌手 $\mathcal{A}^{\prime}$：对 $\mathcal{A}$ 的加密查询 $m$，自行计算 $t=\mathsf{Mac}_{k_M}(m)$，向 $\Pi_E$ 预言机查询 $m\|t$ 得 $c$ 返回。挑战同理：$\mathcal{A}$ 输出 $m_0,m_1$，$\mathcal{A}^{\prime}$ 输出 $m_0\|t_0,m_1\|t_1$。$\Pi_E$ CPA 安全 $\Rightarrow$ $\mathcal{A}^{\prime}$ 优势可忽略 $\Rightarrow$ $\mathcal{A}$ 优势可忽略。$\blacksquare$

---

## 习题 5.8　强 PRP 加密方案的解密与 CPA 安全

> **题目**　$\mathsf{Enc}_k(m)$：均匀 $r\in\{0,1\}^{n/2}$，$c=F_k(r\|m)$（$|m|=n/2$，$F$ 强 PRP）。给出解密，证对 $n/2$ 长消息 CPA 安全。

**解密**：$\mathsf{Dec}_k(c)=F_k^{-1}(c)$ 的后 $n/2$ 比特（$F_k^{-1}(c)=r\|m$，丢弃前 $n/2$ 比特 $r$）。正确性显然。

**CPA 安全**。归约到 $F$ 是 PRP。换 $F_k$ 为均匀置换 $f\in\mathsf{Perm}_n$：每次加密取均匀 $r$（$n/2$ 比特），输出 $f(r\|m)$。$f$ 是均匀置换，$f(r\|m)$ 对未知 $f$ 均匀——**只要各加密所用输入点 $r\|m$ 互不碰撞**。两点碰撞需 $r$ 与 $r^{\prime}$ 相等且 $m=m^{\prime}$；对至多 $q(n)$ 次查询，$r$ 碰撞概率 $\le q(n)^2/2^{n/2}$（生日界，可忽略）。无碰撞时，所有密文是独立均匀 $n$ 比特串，敌手优势 0。合并 CPA 优势 $\le\mathsf{Adv}^{\mathsf{PRP}}+q^2/2^{n/2}$ 可忽略。（详见第 3 章习题 3.19。）$\blacksquare$

---

## 习题 5.9　习题 5.8 方案不是认证加密方案

> **题目**　Show that the scheme in Exercise 5.8 is not an authenticated encryption scheme.
> **题目**　证明习题 5.8 中的方案不是认证加密方案。

认证加密 = CCA 安全 + 不可伪造（定义 5.3）。该方案**不可伪造**（见习题 5.5 类比：标签……实际上此方案无 MAC，仅加密），但**不 CCA 安全**。CCA 攻击：

挑战 $c^*=F_k(r^*\|m_b)$（$m_0,m_1$ 任取不同，长 $n/2$）。敌手构造 $c^{\prime}$：因 $F_k$ 是置换，$c^*$ 对应唯一明文 $r^*\|m_b$。敌手无法直接改 $c^*$。但可利用解密预言机对**其他**密文查询来区分。具体：敌手选 $m_0=0^{n/2},m_1=1^{n/2}$。挑战 $c^*=F_k(r^*\|m_b)$。敌手取均匀 $\tilde r\ne r^*$（猜测），构造 $\tilde c=F_k(\tilde r\|m_0)$？不知 $F_k$。

换攻击（利用解密预言机返回**整段** $r\|m$）：解密预言机对 $c^*$ 本身被禁，但敌手可构造 $c^{\prime\prime}$ 使其解密结果的**前 $n/2$ 比特（$r$ 部分）**可控。因 $\mathsf{Dec}_k$ 返回 $F_k^{-1}(c)$ 的后半（$m$），丢弃 $r$——敌手只见到 $m$，不见 $r$。故解密预言机返回 $m$，对 $c^*$ 禁用。

**真正的 CCA 攻击**：敌手利用 $F_k$ 是置换——对挑战 $c^*=F_k(r^*\|m_b)$，敌手向解密预言机查询 $c^*\oplus\Delta$（$\Delta$ 使 $c^*\oplus\Delta\ne c^*$，允许）。返回 $m^{\prime}=F_k^{-1}(c^*\oplus\Delta)$ 的后半。但这与 $m_b$ 无直接关系（$F_k^{-1}$ 雪崩）。

更简洁：该方案**不 CCA 安全**因为它**非可塑**性不成立——其实它是基于强 PRP 的，密文整体是置换输出，看似难篡改。但**不可伪造性**也不成立（无 MAC，任意 $n$ 比特串都是合法密文，解密得某 $r\|m$）。定义 5.3 要求不可伪造：敌手输出"新有效密文" $c^*$（$\mathsf{Dec}_k(c^*)\ne\bot$）。但本方案 $\mathsf{Dec}_k(c)\ne\bot$ 对**任意** $c$ 成立（置换总有原像），故敌手输出任意 $c^*$ 即"有效"，且 $m^*=\mathsf{Dec}_k(c^*)$ 对新 $c^*$ 一般是新消息 $m^*\notin\mathcal{Q}$。**不可伪造性失败**，故非认证加密。

（核心：无 MAC 的纯加密方案，任何 $c$ 都"有效"，不可伪造不成立。）$\blacksquare$

---

## 习题 5.10　CPA 安全 + 不可伪造，但非 CCA 安全

> **题目**　给出一个 CPA 安全、不可伪造，但非 CCA 安全的私钥加密方案。

**方案**：构造 5.6（encrypt-then-authenticate），其中加密用任意 CPA 安全方案 $\Pi_E$，MAC 用一个**安全但非强安全**的 MAC（如习题 4.4：截断标签也接受，$\mathsf{Vrfy}_k(c,t)=1\iff t=\mathsf{Mac}^{\prime}_k(c)\ \text{或}\ t=\mathsf{Mac}^{\prime}_k(c)$ 的前 $n-1$ 位）。密文 $\langle c,t\rangle$，$c=\mathsf{Enc}_{k_E}(m)$，$t=\mathsf{Mac}_{k_M}(c)$。

**三条性质**：
- **不可伪造**：由习题 5.5，构造 5.6 用**任意**安全 MAC 即不可伪造（不要求强安全，也不要求加密 CPA 安全）。
- **CPA 安全**：CPA 敌手只访问加密预言机，见到的是 $\langle c,t\rangle$，其中 $t$ 由 $c$ 完全确定。加密部分 $\mathsf{Enc}_{k_E}$ 是 CPA 安全，故 $c$ 不泄露 $m$；$t$ 是 $c$ 的函数，不增加关于 $m$ 的信息。归约：CPA 攻击者把对 $\langle c,t\rangle$ 的区分归约到对 $c$ 本身的区分（同习题 5.7）。
- **非 CCA 安全**：这正是习题 5.4 所证。非强安全 MAC 使敌手能为**已认证的挑战密文 $c^*$** 构造一个**新标签** $t^{\prime}^*$（截断标签）使 $\mathsf{Vrfy}_{k_M}(c^*,t^{\prime}^*)=1$；于是 $\langle c^*,t^{\prime}^*\rangle\ne\langle c^*,t^*\rangle$（挑战密文本身），**允许**提交给解密预言机，返回 $\mathsf{Dec}_{k_E}(c^*)=m_b$，敌手直接得知 $m_b$，成功概率 1。

故该方案 CPA 安全、不可伪造，但非 CCA 安全。$\blacksquare$

---
