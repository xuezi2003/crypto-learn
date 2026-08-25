# The Four Core Models: System, Trust, Threat, and Trust Assumptions

# Abstract:


本文档旨在区分密码学协议设计中四个至关重要但容易混淆的构建模块System Model,Trust Model,Threat Model,Trust Assumption。以 **VSS (Verifiable Secret Sharing)** 协议为例。（一些思考与理解，maybe存在一些不准确的地方希望指正与补充）


> **结合 VSS Simplified 的理解总结**

[Verifiable Secret Sharing Simplified.pdf](<./assets/Verifiable Secret Sharing Simplified.pdf>)
<!-- 飞书原始链接: https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=MTY3MzFhY2Y0ODFkOGUzNTYzMTQ1ZmRiODdjZTRlYTVfZTBlMTdlZGZmOTAzMTE4ZmRlYTMwZDdhYmJlNzM4NjZfSUQ6NzU3Nzc1NjExNTY5ODQ2OTg0MV8xNzg1NDYxODk0OjE3ODU0NjU0OTRfVjM -->

## What is VSS

为了帮助大家更直观了解下列基于VSS的例子，这里粗略介绍一下VSS整个协议流程

**参与方（Parties）**

- **Dealer**：持有秘密 s，负责将秘密拆分成份额发给节点。
- **n 个节点 Nodes**：每个节点 i 拿到一个份额share，并在之后可与多个节点共同重建出秘密s。

**两个阶段（Phases）**

**Sharing Phase（分发阶段）**

- Dealer 运行协议，把秘密编码成 n 份 shares，通过点对点信道发给每个节点。
- 同时，Dealer 会在公共广播信道上发送一些“承诺信息”（例如多项式承诺、承诺向量等），让每个节点可以本地检查：“我拿到的这一份是否和大家的份额是否都来自同一个秘密？”

**Reconstruction Phase（重构阶段）**

- 当大家需要恢复秘密时，每个诚实节点把自己手上的 share（以及必要的证明）发出来。
- 只要收集到足够多（比如 t+1 个）通过验证的份额，诚实节点就可以用插值等算法恢复出唯一的秘密 sss。


## System Model


**定义**：协议运行的环境，可以看作基础设施。它描述了协议算法是在什么样的组件上运行的，以及这些组件具备的能力与接口。

在整个 VSS 协议运行的世界中，包含了以下组件：

- **所有的协议参与者**：

  - 包括一个分发方 **Dealer**。
  - 包括n个节点 **Nodes**。
- **组件能力与接口**：

  - **通信能力**：Dealer 与 Nodes 存在点对点的私密认证信道（一对一通信，内容加密，并且身份通过验证的通信媒介），广播信道。
  - **基础设施**：如 PKI（公钥基础设施）。
- **网络环境**：

  - 同步（Synchronous）：消息传输的延迟有一个已知且不变的上界，即消息一定会在这一最大延迟时间内到达。
  - 异步（Asynchronous）消息传输的延迟是任意但有限的，消息一定会到但是不知道什么时候会到。

---

## Trust Model


**定义**：在整个 System Model 中，界定哪些实体或设施是可信的，哪些是不被信任的（信任边界）。

在上述 System Model 中定义出的可信范围包括：

- **信任的界定 :**

  - 模型规定：在同步网络 (Synchronous) 下，信任模型基于 $n \geq 2t+1$（即坏人不超过一半）。
  - 模型规定：在异步网络 (Asynchronous) 下，信任模型调整为 $n \geq 3t+1$（即坏人不超过三分之一）。
- **参与方的信任:**

  - 模型设定 Dealer 既可能是**可信的**（需保护隐私），也可能是**恶意的**（需防止欺诈），协议必须同时处理这两种情况 。
  - nodes中存在恶意的节点，以及诚实节点。
- **可信任的基础设施：**

  - 广播信道，Dealer和nodes的点对点的私密认证信道
  - PKI

---

## Threat Model


**定义**：描述敌手（Adversary）的能力大小以及类型。

- **腐化能力**：

  - **静态敌手 (Static Adversary)**：能提前腐化 t个节点。
  - **攻击行为**：这些被腐化的恶意节点可以完全偏离协议执行。
- **计算能力**：

  - 通常假设为 **PPT**（概率多项式时间），即敌手受到计算能力的限制，无法攻破数学难题。

---

## Security Assumption

**定义：**包含了我们呢所依赖的数学难题（Hardness）与协议运行环境中的配置或一些基础设施的信任前提（Trust）

- **Computational Hardness Assumptions**在群 **G** 中求解离散对数是困难的。 整个协议的安全性（包括 Pedersen Commitment 的 Hiding/Binding 性质）完全建立在 DL 假设之上，**不依赖**其他更强的假设。

  > 协议依赖的数学难题。我们假设在多项式时间（PPT）内，敌手无法攻破这些数学问题。

  - **Discrete Logarithm (DL) Assumption:**


-  **Trust  Assumption** 假设所有节点在协议开始前已拥有经过认证的公钥pk。 协议利用 PKI 来进行签名认证（ACK机制）和加密（Dual-threshold 中的 VE），从而避免了复杂的交互 。

  >    指协议运行所必需的环境配置或对基础设施的信任前提。

  - **PKI Model (公钥基础设施):**

  - **No Trusted Setup (无须可信设置):**
  
    -  假设系统**不需要**一个可信第三方来生成公共参考串（CRS）。 这是一个关键的“零信任”假设。不同于许多需要 "Powers-of-Tau" 设置的方案，本协议假设只需公开的群参数即可运行，消除了对“可信初始化仪式”的依赖 。


- **Trust Model**和**Trust Assumption**里面都提到了PKI，而区别在于：

  - **在 Trust Model 中：** 它是**组件**。我们声称System Model中有这一可信设施，把它划入可信边界内，作为协议运行的基础工具。
  - **在 Trust Assumption 中：** 它是**安全前提**。我们列出具体的**条件假设**（如私钥安全、算法不可伪造），如果这些条件被打破，上述可信设施就会失效。


## 总结


这四点是容易混淆但至关重要的组成部分。很多优秀的论文（包括 VSS 这一篇）并不会特意开辟一章来罗列这四点，而是将这种整体叙述穿插在写作中：

- **Intro部分**：给出一个整体的System Model 帮助读者搭建一个大体的理解框架。
- **Contributions 部分**：在提及本文贡献以及突破时，将Trust Assumption与其他有关方向的成果对比，凸显理论优势的同时又给出了之后协议设计基于的Trust Assumption，同时帮助读者更好地理解System Model 。
- **Def部分：**严格定义了Threat Model ，并且在对敌手能力分析之后也帮助读者对Trust Model有一个直观理解。

在有了类似上述这般铺垫以后，所有的设计动机与算法实现都与之紧密相连，也就显得更加自然。