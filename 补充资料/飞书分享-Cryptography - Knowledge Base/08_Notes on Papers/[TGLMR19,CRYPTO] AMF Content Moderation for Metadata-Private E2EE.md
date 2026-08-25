# [TGLMR19,CRYPTO] AMF: Content Moderation for Metadata-Private E2EE

> 源文件：`[TGLMR19,CRYPTO] AMF Content Moderation for Metadata-Private E2EE.pdf`（PDF 原文保留，本文由 OCR 识别生成，轻微修正拼写）

**SUMMARY**: This paper proposes an asymmetric message franking scheme that can work in metadata private messaging system.

**Observation**: In fact, this paper constructs a deniable designated-two-verifier signature scheme. The biggest contribution of this paper is the analysis of deniability.

## 1 Setting & Goals

### 1.1 Setting

（Fig. 1: Overview of different settings for content moderation or messaging。标准设定下，跨平台发送的消息关联发送者与接收者身份，平台即审核者；元数据私有设定下，消息的发送者/接收者身份对平台（及审核者）隐藏；第三方设定下，审核者与平台分离。AMF 原语面向后两种设定。）

### 1.2 Security Goals

There are two parts of security that AMF requires, i.e., accountability and deniability.

**Accountability**
- Receiver binding
- Sender binding
- Unforgeability

**Deniability**

- **Universal deniability**: This property is implemented by some kind of indistinguishability. When the signature is indistinguishable to the users except the verifier, a forger can forge valid signature with random values.
- Receiver compromise deniability
- Judge compromise deniability

## 2 Roadmap

### Naive solution - Digital signature

A naive solution to implement asymmetric message franking is a digital signature. We can assume that every user has a key pair (pk, sk) and the sender signs a message when sending.

However, this does not preserve deniability since conventional digital signature is public verifiable. Anyone who knows the sender's public can verify this signature, which leaks the sender's identity.

### Designated-verifier signature

To resolve the above problem, the authors use designated-verifier signature (DVS) to construct AMF. Specifically, the authors extend conventional DVS from two parties to three parties. Here, recipient and platform are the only two verifiers of the signature.

### Deniable designated-verifier signature

Finally, the construction should preserve deniability and verifiability. Therefore, the authors use sigma protocol to implement variable deniability.

**Distinguisher 判定表**（哪一方持有 $sk$ 时可区分伪造签名）：

| | 0 | 1 | 0 | 1 | 0 | 1 | 0 | 1 | 0 | 1 |
|--|---|---|---|---|---|---|---|---|---|---|
| $sk_A$ | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 1 | 1 | 1 |
| $sk_R$ | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | 1 | 1 |
| Forger | ☑/● | ● | ● | ● | ● | ● | ● | ●◆ | ● | ● |

## 3 Methodology

**方案算法（Fig. 5）**：AMF 方案由以下算法组成，关系 $\mathcal{R}$ 定义其 SPoK：

$$\mathcal{R}=\left\{\left((t,u,v,w),(g,pk_s,pk_j,J,R,E_J)\right):\left(pk_s=g^{t}\lor J=g^{u}\right)\land\left((J=(pk_j)^{v}\land E_J=g^{v})\lor R=g^{w}\right)\right\}$$

| 算法 | 安全概念 | 第一条子句的证明方式 $(pk_s = g^t \lor J = g^u)$ | 第二条子句的证明方式 $((J=(pk_j)^v \land E_J=g^v) \lor R=g^w)$ | Verify? | Judge? |
|------|----------|-------------------------------------------------|-----------------------------------------------------------|---------|--------|
| Frank | Correctness | $\alpha \leftarrow \mathbb{Z}_p$, $J \leftarrow (pk_j)^\alpha$; $t = sk_s$ | $\beta \leftarrow \mathbb{Z}_p$, $R \leftarrow (pk_r)^\beta$; $v = \alpha$ | ✓ | ✓ |
| Forge | Univ. den. | $\gamma \leftarrow \mathbb{Z}_p$, $J \leftarrow g^\gamma$; $u = \gamma$ | $\delta \leftarrow \mathbb{Z}_p$, $R \leftarrow g^\delta$; $w = \delta$ | ✗ | ✗ |
| RForge | R. comp. den. | $\gamma \leftarrow \mathbb{Z}_p$, $J \leftarrow g^\gamma$; $u = \gamma$ | $\beta \leftarrow \mathbb{Z}_p$, $R \leftarrow (pk_r)^\beta$; $w = \beta \cdot sk_r$ | ✓ | ✗ |
| JForge | J. comp. den. | $\alpha \leftarrow \mathbb{Z}_p$, $J \leftarrow (pk_j)^\alpha$; $u = \alpha \cdot sk_j$ | $\beta \leftarrow \mathbb{Z}_p$, $R \leftarrow (pk_r)^\beta$; $v = \alpha$ | ✓ | ✓ |

**各算法（Fig. 5）**：

- $\mathsf{Frank}(sk_s, pk_r, pk_j, msg)$：$(\alpha,\beta) \leftarrow \mathbb{Z}_p^2$；$J \leftarrow (pk_j)^\alpha$，$R \leftarrow (pk_r)^\beta$，$E_J \leftarrow g^\alpha$，$E_R \leftarrow g^\beta$；$x \leftarrow (sk_s, \bot, \alpha, \bot)$，$y \leftarrow (g, pk_s, pk_j, J, R, E_J)$；$\pi \leftarrow \mathsf{SPoK}^{\mathcal{R}}.prove(msg, x, y)$；返回 $(\pi, J, R, E_J, E_R)$。
- $\mathsf{Forge}(pk_s, pk_r, pk_j, msg)$：$(\alpha,\beta,\gamma) \leftarrow \mathbb{Z}_p^3$；$J \leftarrow g^\gamma$，$R \leftarrow (pk_r)^\beta$，$E_J \leftarrow g^\alpha$，$E_R \leftarrow g^\beta$；$x = (\bot, \gamma, \bot, \beta \cdot sk_r)$；返回 $(\pi, J, R, E_J, E_R)$。
- $\mathsf{RForge}(pk_s, sk_r, pk_j, msg)$：$(\alpha,\beta,\gamma) \leftarrow \mathbb{Z}_p^3$；$J \leftarrow g^\gamma$，$R \leftarrow (pk_r)^\beta$，$E_J \leftarrow g^\alpha$，$E_R \leftarrow g^\beta$；$x = (\bot, \gamma, \bot, \beta \cdot sk_r)$。
- $\mathsf{JForge}(pk_s, pk_r, sk_j, msg)$：$(\alpha,\beta) \leftarrow \mathbb{Z}_p^2$；$J \leftarrow (pk_j)^\alpha$，$R \leftarrow (pk_r)^\beta$，$E_J \leftarrow g^\alpha$，$E_R \leftarrow g^\beta$；$x \leftarrow (\bot, \alpha \cdot sk_j, \alpha, \bot)$。
- $\mathsf{Verify}(pk_s, sk_r, pk_j, msg, \sigma)$：解析 $(\pi, J, R, E_J, E_R) \leftarrow \sigma$；$b_1 \leftarrow R = E_R^{sk_r}$；$b_2 \leftarrow \mathsf{SPoK}^{\mathcal{R}}.verify(msg, \pi, y)$；返回 $b_1 \land b_2$。
- $\mathsf{Judge}(pk_s, pk_r, sk_j, msg, \sigma)$：解析 $(\pi, J, R, E_J, E_R) \leftarrow \sigma$；$b_1 \leftarrow J = E_J^{sk_j}$；$b_2 \leftarrow \mathsf{SPoK}^{\mathcal{R}}.verify(msg, \pi, y)$；返回 $b_1 \land b_2$。
