# Chapter 4: Message Authentication Codes　第四章　消息认证码

## 4.1 Message Integrity　4.1 消息完整性

### 4.1.1 Secrecy vs. Integrity　4.1.1 机密性与完整性

A basic goal of cryptography is to enable parties to communicate securely. But what does "secure communication" entail? In Chapter 3 we showed how it is possible to achieve secrecy; that is, we showed how encryption can be used to prevent a passive eavesdropper from learning anything about messages sent over an open channel. However, not all security concerns are related to secrecy, and not all adversaries are limited to passive eavesdropping. In many cases, it is of equal or greater importance to guarantee message integrity (or message authentication) against an active adversary who can inject messages on the channel or modify messages in transit. We consider two motivating examples corresponding to the settings of Figures 1.1 and 1.2, respectively.

密码学的一个基本目标是使各方能够安全地通信。但“安全通信”意味着什么？在第 3 章中，我们展示了如何实现机密性；也就是说，我们展示了如何使用加密来防止被动的窃听者了解通过开放信道发送的消息的任何内容。然而，并非所有的安全关切都与机密性相关，也并非所有的敌手都仅限于被动窃听。在许多情况下，同样甚至更为重要的是，要保证消息完整性（或消息认证），以抵御能够在信道上注入消息或篡改传输中消息的活跃敌手。我们考虑两个启发性示例，分别对应于图 1.1 和图 1.2 的场景。

Imagine first a user communicating with her bank over the Internet. When the bank receives a request to transfer \$1,000 from the user's account to the account of some other user X, the bank has to consider the following:

首先设想一个用户通过互联网与她的银行通信的场景。当银行收到一个请求，要求从该用户的账户向另一用户 X 的账户转账 \$1,000 时，银行必须考虑以下问题：

1. Is the request authentic? That is, did the user in question really issue this request, or was the request issued by an adversary (perhaps X itself) who is impersonating the legitimate user?

   该请求是否真实可信？也就是说，该用户是否真的发出了这个请求，还是由冒充合法用户的敌手（可能是 X 本身）发出的？

2. Assuming a transfer request was issued by the legitimate user, is the request received by the bank exactly the same as what was sent by that user? Or was, e.g., the transfer amount modified as the request was sent across the Internet?

   假设转账请求是由合法用户发出的，银行收到的请求是否与该用户发送的完全相同？或者，例如转账金额在请求通过互联网传输时是否被篡改了？

Note that standard error-correction techniques do not suffice for the second concern. Error-correcting codes are only intended to detect and recover from "random" errors that affect a small portion of the transmission, but they do nothing to protect against a malicious adversary who can choose exactly where to introduce an arbitrary number of changes.

注意，标准的纠错技术不足以应对第二个问题。纠错码仅旨在检测和恢复影响传输中小部分的“随机”错误，但它们无法抵御能够精确选择在何处引入任意数量更改的恶意敌手。

A very different scenario where the need for message integrity arises in practice is with regard to web cookies. The HTTP protocol used for web traffic is stateless, so when a client and server communicate in some session (e.g., when a user [client] shops at a merchant's [server's] website), any state generated as part of that session (e.g., the contents of the user's shopping cart) is often placed in a "cookie" that is stored by the user and included along with each message the user sends to the merchant. Assume the cookie stored by some user includes the items in the user's shopping cart along with a price for each item, as might be done if the merchant offers different prices to different users (reflecting discounts and promotions, or user-specific pricing). It would be undesirable for the user to be able to modify the cookie it stores so as to alter the prices of the items in its cart. The merchant thus needs a technique to ensure the integrity of the cookie that it stores at the user. Note that the contents of the cookie (namely, the items and their prices) are not secret and, in fact, must be known by the user. The problem here is purely one of integrity.

在实际中，另一个需要消息完整性的截然不同的场景涉及 Web Cookie。用于 Web 流量的 HTTP 协议是无状态的，因此当客户端和服务器在某个会话中通信时（例如，当用户[客户端]在商家[服务器]的网站上购物时），该会话产生的任何状态（例如用户购物车的内容）通常被放置在一个由用户存储的 "cookie" 中，并随用户发送给商家的每条消息一起发送。假设某个用户存储的 cookie 包含用户购物车中的商品以及每件商品的价格——如果商家对不同用户提供不同价格（反映折扣、促销或特定于用户的定价），则可能出现这种情况。如果允许用户修改其存储的 cookie，从而改变购物车中商品的价格，那是不可取的。因此，商家需要一种技术来确保其存储在用户处的 cookie 的完整性。注意，cookie 的内容（即商品及其价格）并非秘密，实际上用户必须知道它们。这里的问题纯粹是完整性问题。

In general, one cannot assume the integrity of communication without taking specific measures to ensure it. Indeed, any unprotected online purchase order, online banking operation, email, or SMS message cannot, in general, be trusted to have originated from the claimed source and to have been unmodified in transit. Unfortunately, people are generally trusting and so information like the caller-ID or an email return address are taken to be "proofs of origin" in many cases, even though they are relatively easy to forge. This leaves the door open to potentially damaging attacks.

一般来说，在没有采取特定措施确保通信完整性的情况下，不能假定其是完整的。实际上，任何未受保护的在线订购单、网上银行操作、电子邮件或短信消息，通常都不能信任它们确实来自声称的源且在传输过程中未被篡改。不幸的是，人们通常容易轻信他人，因此像来电显示或电子邮件回复地址这样的信息在许多情况下被视为“来源证明”，尽管它们相对容易被伪造。这为潜在的破坏性攻击留下了可乘之机。

In this chapter we will show how to achieve message integrity by using cryptographic techniques to detect any spoofed messages or any tampering of messages sent over an unprotected communication channel. Note that we cannot hope to prevent message injection or message tampering altogether, as that can only be defended against at the physical level. Instead, what we will guarantee is that any such behavior will be detected by the honest parties.

在本章中，我们将展示如何通过使用密码学技术来检测任何伪造的消息或对通过未保护通信信道发送的消息的任何篡改，从而实现消息完整性。注意，我们不能指望完全阻止消息注入或消息篡改，因为只有物理层面才能防御这些行为。相反，我们将保证的是，任何此类行为都将被诚实方检测到。

### 4.1.2 Encryption vs. Message Authentication　4.1.2 加密与消息认证

Just as the goals of secrecy and message integrity are different, so are the techniques and tools for achieving them. Unfortunately, secrecy and integrity are often confused and unnecessarily intertwined, so let us be clear up front: encryption does not (in general) provide any integrity, and encryption should not be assumed to ensure message authentication unless it is specifically designed with that purpose in mind (something we will return to in Section 5.2).

正如机密性和消息完整性的目标不同，实现它们的技术和工具也不同。不幸的是，机密性和完整性常常被混淆且不必要地纠缠在一起，因此让我们从一开始就明确：加密（通常）不提供任何完整性，并且除非专门为此目的而设计（我们将在 5.2 节回到这个问题），否则不应假定加密能保证消息认证。

One might mistakenly think that encryption solves the problem of message authentication. (In fact, this is a common error.) This is due to the fuzzy, and incorrect, reasoning that since a ciphertext completely hides the contents of the message, an adversary cannot possibly modify an encrypted message in any meaningful way. Despite its intuitive appeal, this reasoning is completely false. We illustrate this point by showing that all the encryption schemes we have seen thus far do not provide message integrity.

有人可能会错误地认为加密解决了消息认证问题。（事实上，这是一个常见错误。）这是因为一种模糊且不正确的推理：既然密文完全隐藏了消息的内容，敌手就不可能以任何有意义的方式修改加密后的消息。尽管这种推理具有直观吸引力，但它完全错误。我们通过展示迄今为止所见的所有加密方案都不提供消息完整性来说明这一点。

Encryption using stream ciphers. Consider encryption schemes in which the sender generates a pseudorandom pad based on a shared key (and possibly an IV) and then computes a ciphertext by XORing the resulting pad with a message, as in Constructions 3.17, 3.28, and 3.31 as well as OFB and CTR modes. Ciphertexts in this case are very easy to manipulate: flipping any bit in the ciphertext results in the same bit being flipped in the message that is recovered upon decryption. Thus, given a ciphertext $c$ that encrypts a (possibly unknown) message $m$, it is possible for an adversary to generate a modified ciphertext $c^{\prime}$ such that $m^{\prime} := \mathsf{Dec}_k(c^{\prime})$ is the same as $m$ but with a specific set of bits flipped. This simple attack can have severe consequences. As an example, consider the case of a user encrypting some dollar amount she wants to transfer from her bank account, where the amount is represented in binary. Flipping the least significant bit has the effect of changing this amount by 1, and flipping the 11th least significant bit changes the amount by more than 1,000! Interestingly, the adversary does not necessarily learn whether it is increasing or decreasing the initial amount, i.e., whether it is flipping a 0 to a 1 or vice versa. But if the adversary has some partial knowledge about the amount—say, that it is less than 1,000 to begin with—then the modifications it introduces can have a predictable effect.

使用流密码的加密。考虑这样一种加密方案：发送方基于共享密钥（可能还有 IV）生成一个伪随机填充，然后通过将生成的填充与消息进行 XOR 运算来计算密文，如构造 3.17、3.28、3.31 以及 OFB 和 CTR 模式。在这种情况下，密文非常容易操控：翻转密文中的任何比特，都会导致解密恢复的消息中同一比特被翻转。因此，给定一个加密了（可能未知）消息 $m$ 的密文 $c$，敌手可以生成一个修改后的密文 $c^{\prime}$，使得 $m^{\prime} := \mathsf{Dec}_k(c^{\prime})$ 与 $m$ 相同，但特定的比特集合被翻转了。这种简单的攻击可能产生严重后果。例如，考虑一个用户加密了她想从银行账户转账的美元金额，该金额以二进制表示。翻转最低有效位会使该金额改变 1，而翻转第 11 个最低有效位则会使金额改变超过 1,000！有趣的是，敌手不一定知道自己是在增加还是减少初始金额，即不知道自己翻转的是把 0 变成 1 还是相反。但如果敌手对该金额已有部分了解——例如已知它一开始就小于 1,000——那么敌手引入的修改就会产生可预测的效果。

We stress that this attack does not contradict the secrecy of the encryption scheme. In fact, the exact same attack applies to the one-time pad encryption scheme, showing that even perfect secrecy is not sufficient to ensure the most basic level of message integrity.

我们强调，这种攻击并不与加密方案的机密性相矛盾。事实上，完全相同的攻击也适用于一次一密加密方案，这表明即使是完美保密也不足以确保最基本级别的消息完整性。

Encryption using block ciphers. The attack described above exploits the fact that flipping a single bit in a ciphertext keeps the underlying plaintext unchanged except for the corresponding bit (which is also flipped). One might hope that encryption schemes using block ciphers in a more sophisticated way would prevent such attacks since, for example, if decryption involves inverting a (strong) pseudorandom permutation $F$ on some portion $x$ of the ciphertext then $F_k^{-1}(x)$ and $F_k^{-1}(x^{\prime})$ will be completely uncorrelated if $x$ and $x^{\prime}$ differ in even a single bit. Nevertheless, single-bit modifications of a ciphertext can still cause partially predictable changes in the plaintext. For example, when using ECB mode, flipping a bit in the ith block of a ciphertext affects only the ith block of the plaintext—all other blocks remain unchanged. (Of course, ECB mode does not even guarantee the most basic notion of secrecy, but that is irrelevant for the present discussion.) Although the effect on the ith block of the plaintext may be impossible to predict, changing that one block (while leaving everything else unchanged) may represent a harmful attack. Moreover, the order of plaintext blocks can be changed (without garbling any block) by simply changing the order of the corresponding ciphertext blocks, and the message can be truncated by dropping ciphertext blocks.

使用分组密码的加密。上述攻击利用了以下事实：翻转密文中的单个比特，除了相应的比特（也被翻转）外，底层明文保持不变。有人可能希望以更复杂的方式使用分组密码的加密方案能够防止此类攻击，因为例如，如果解密涉及对密文的某部分 $x$ 求逆一个（强）伪随机置换 $F$，那么若 $x$ 和 $x^{\prime}$ 即使仅一个比特不同，$F_k^{-1}(x)$ 和 $F_k^{-1}(x^{\prime})$ 也将完全不相关。然而，密文的单比特修改仍可能导致明文中部分可预测的变化。例如，使用 ECB 模式时，翻转密文第 i 块中的一个比特仅影响明文的第 i 块——所有其他块保持不变。（当然，ECB 模式甚至不保证最基本的机密性概念，但这与当前讨论无关。）尽管对明文第 i 块的影响可能无法预测，但改变这一块（而保持其他所有内容不变）可能构成有害攻击。此外，只需改变相应密文块的顺序即可改变明文块的顺序（而不会破坏任何块），并且可以通过丢弃密文块来截断消息。

For CBC mode, flipping the $j$th bit of the $IV$ changes only the $j$th bit of the first message block $m_1$ (since $m_1 := F_k^{-1}(c_1) \oplus IV^{\prime}$, where $IV^{\prime}$ is the modified $IV$); all other plaintext blocks remain unchanged. Therefore, the first block of a CBC-encrypted message can be modified arbitrarily. We will see in Section 5.1.1 that this simple attack can have disastrous consequences.

对于 CBC 模式，翻转 $IV$ 的第 $j$ 位仅改变第一个消息块 $m_1$ 的第 $j$ 位（因为 $m_1 := F_k^{-1}(c_1) \oplus IV^{\prime}$，其中 $IV^{\prime}$ 是修改后的 $IV$）；所有其他明文块保持不变。因此，CBC 加密消息的第一个块可以被任意修改。我们将在 5.1.1 节看到，这种简单的攻击可能带来灾难性后果。

Finally, observe that all the encryption schemes we have seen thus far have the property that every string of a certain length is a valid ciphertext, and so corresponds to some valid message. It is therefore trivial for an adversary to "spoof" a message on behalf of one of the communicating parties—by sending an arbitrary string of the correct length—even if the adversary has no idea what the underlying message will be. In the context of message integrity, even an attack of this sort should be ruled out.

最后，注意迄今为止我们看到的所有加密方案都具有这样的性质：每个具有某个固定长度的字符串都是一个合法密文，因此对应于某个有效消息。因此，敌手可以轻而易举地代表通信方之一“伪造”一条消息——只需发送一个任意正确长度的字符串即可——即使敌手完全不知道底层消息是什么。在消息完整性的语境中，即使是这种攻击也应该被排除。

## 4.2 Message Authentication Codes (MACs) – Definitions　4.2 消息认证码(MAC)——定义

We have seen that, in general, encryption does not solve the problem of message integrity. Rather, an additional mechanism is needed that will enable the communicating parties to know whether or not a message was tampered with. The right tool for this task is a message authentication code (MAC).

我们已经看到，一般来说，加密并不能解决消息完整性问题。相反，还需要一种额外的机制，使通信方能够知道消息是否被篡改过。完成这一任务的正确工具是消息认证码（MAC）。

The aim of a message authentication code is to prevent an adversary from modifying a message sent by one party to another, or from injecting a new message, without the receiver detecting that the message did not originate from the intended party. As in the case of encryption, this is only possible if the communicating parties have some secret information that the adversary does not know (otherwise nothing can prevent an adversary from impersonating the party sending the message). Here, we continue to consider the private-key setting where the communicating parties share a secret key.

消息认证码的目标是防止敌手修改一方发送给另一方的消息，或注入新消息，而不被接收方检测到消息并非来自预期的发送方。与加密的情况一样，这只有在通信方拥有敌手不知道的秘密信息时才有可能（否则无法阻止敌手冒充发送消息的一方）。在此，我们继续考虑通信方共享一个密钥的私钥设置。

As in the case of private-key encryption, there are two canonical application scenarios for MACs (cf. Section 1.2): ensuring integrity for two parties communicating with each other (as in our earlier example of a user communicating with her bank), or for one user communicating "with himself" over time (as in our earlier example involving web cookies, or a user protecting the contents of his hard drive).

与私钥加密的情况一样，MAC 有两种典型的应用场景（参见 1.2 节）：确保两个相互通信的方之间的完整性（如我们之前用户与银行通信的例子），或确保一个用户随时间“与自己”通信的完整性（如我们之前涉及 Web Cookie 的例子，或用户保护其硬盘内容的例子）。

### The Syntax of a Message Authentication Code　消息认证码的语法

Before formally defining security of a message authentication code, we first define what a MAC is and how it is used. Two users who wish to communicate in an authenticated manner begin by generating and sharing a secret key $k$ in advance of their communication. When one party wants to send a message $m$ to the other, she computes a tag $t$ based on the message and the shared key, and sends the message $m$ along with $t$ to the other party. The tag is computed using a tag-generation algorithm $\mathsf{Mac}$; thus, rephrasing what we have just said, the sender of a message $m$ computes $t \leftarrow \mathsf{Mac}_k(m)$ and transmits $(m, t)$ to the receiver. Upon receiving $(m, t)$, the second party verifies whether $t$ is a valid tag on the message $m$ (with respect to the shared key) or not. This is done by running a verification algorithm $\mathsf{Vrfy}$ that takes as input the shared key as well as a message $m$ and a tag $t$, and indicates whether the given tag is valid. Formally:

在形式化定义消息认证码的安全性之前，我们首先定义什么是 MAC 以及如何使用它。希望以认证方式进行通信的两个用户在通信开始前先生成并共享一个秘密密钥 $k$。当一方想要向另一方发送消息 $m$ 时，她基于消息和共享密钥计算一个标签 $t$，并将消息 $m$ 连同 $t$ 一起发送给另一方。标签是使用标签生成算法 $\mathsf{Mac}$ 计算的；因此，重述我们刚才所说的，消息 $m$ 的发送方计算 $t \leftarrow \mathsf{Mac}_k(m)$ 并将 $(m, t)$ 传输给接收方。收到 $(m, t)$ 后，第二方验证 $t$ 是否是消息 $m$ 上的有效标签（相对于共享密钥）。这通过运行验证算法 $\mathsf{Vrfy}$ 来完成，该算法以共享密钥以及消息 $m$ 和标签 $t$ 为输入，指示给定标签是否有效。形式化地：

DEFINITION 4.1 A message authentication code (or MAC) consists of three probabilistic polynomial-time algorithms ($\mathsf{Gen}$, $\mathsf{Mac}$, $\mathsf{Vrfy}$) such that:

**定义 4.1** 一个消息认证码（MAC）由三个概率多项式时间算法（$\mathsf{Gen}$, $\mathsf{Mac}$, $\mathsf{Vrfy}$）组成，满足：

1. The key-generation algorithm $\mathsf{Gen}$ takes as input the security parameter ${1}^n$ and outputs a key $k$ with $|k| \geq n$.

   密钥生成算法 $\mathsf{Gen}$ 以安全参数 ${1}^n$ 为输入，输出一个密钥 $k$，满足 $|k| \geq n$。

2. The tag-generation algorithm $\mathsf{Mac}$ takes as input a key $k$ and a message $m \in \{0,1\}^*$, and outputs a tag $t$. Since this algorithm may be randomized, we write this as $t \leftarrow \mathsf{Mac}_k(m)$.

   标签生成算法 $\mathsf{Mac}$ 以密钥 $k$ 和消息 $m \in \{0,1\}^*$ 为输入，输出一个标签 $t$。由于该算法可能是随机化的，我们写作 $t \leftarrow \mathsf{Mac}_k(m)$。

3. The deterministic verification algorithm $\mathsf{Vrfy}$ takes as input a key $k$, a message $m$, and a tag $t$. It outputs a bit $b$, with $b = 1$ meaning valid and $b = 0$ meaning invalid. We write this as $b := \mathsf{Vrfy}_k(m, t)$.

   确定性验证算法 $\mathsf{Vrfy}$ 以密钥 $k$、消息 $m$ 和标签 $t$ 为输入，输出一个比特 $b$，其中 $b = 1$ 表示有效，$b = 0$ 表示无效。我们写作 $b := \mathsf{Vrfy}_k(m, t)$。

It is required that for every $n$, every key $k$ output by $\mathsf{Gen}(1^n)$, and every $m \in \{0,1\}^*$, it holds that $\mathsf{Vrfy}_k(m, \mathsf{Mac}_k(m)) = 1$.
要求对于每个 $n$、每个由 $\mathsf{Gen}(1^n)$ 输出的密钥 $k$ 以及每个 $m \in \{0,1\}^*$，都有 $\mathsf{Vrfy}_k(m, \mathsf{Mac}_k(m)) = 1$。

If there is a function $\ell$ such that for every $k$ output by $\mathsf{Gen}(1^n)$, algorithm $\mathsf{Mac}_k$ is only defined for messages $m \in \{0,1\}^{\ell(n)}$, then we call the scheme a fixed-length MAC for messages of length $\ell(n)$.
如果存在函数 $\ell$，使得对于每个由 $\mathsf{Gen}(1^n)$ 输出的密钥 $k$，算法 $\mathsf{Mac}_k$ 仅对消息 $m \in \{0,1\}^{\ell(n)}$ 有定义，则称该方案为适用于长度为 $\ell(n)$ 的消息的固定长度 MAC。

As with private-key encryption, $\mathsf{Gen}(1^n)$ almost always simply chooses a uniform key $k \in \{0,1\}^n$, and we omit $\mathsf{Gen}$ in that case.

与私钥加密一样，$\mathsf{Gen}(1^n)$ 几乎总是简单地选择一个均匀密钥 $k \in \{0,1\}^n$，在这种情况下我们省略 $\mathsf{Gen}$。

Canonical verification. For deterministic message authentication codes (i.e., where $\mathsf{Mac}$ is a deterministic algorithm), the canonical way to perform verification is simply to re-compute the tag and check for equality. In other words, $\mathsf{Vrfy}_k(m, t)$ first computes $\tilde{t} := \mathsf{Mac}_k(m)$ and then outputs 1 if and only if $\tilde{t} = t$. Even for deterministic MACs, though, it is useful to define a separate $\mathsf{Vrfy}$ algorithm to explicitly distinguish the semantics of authenticating a message to be sent vs. verifying authenticity of a message that was received.

规范验证。对于确定性消息认证码（即 $\mathsf{Mac}$ 是确定性算法的情况），执行验证的规范方式是简单地重新计算标签并检查是否相等。换句话说，$\mathsf{Vrfy}_k(m, t)$ 首先计算 $\tilde{t} := \mathsf{Mac}_k(m)$，然后当且仅当 $\tilde{t} = t$ 时输出 1。然而，即使对于确定性 MAC，定义单独的 $\mathsf{Vrfy}$ 算法也是有用的，以明确区分认证待发送消息与验证已接收消息的真实性这两种语义。

### Security of Message Authentication Codes　消息认证码的安全性

We now define the default notion of security for message authentication codes. The intuitive idea behind the definition is that no efficient adversary should be able to generate a valid tag on any "new" message that was not previously sent (and authenticated) by one of the communicating parties.

现在我们定义消息认证码的默认安全概念。该定义背后的直观思想是：任何高效敌手都不应能在“新”消息上生成有效标签——这里的“新”是指该消息此前未被通信方中的任何一方发送（并认证）过。

As with any security definition, to formalize this notion we need to define both the adversary's power as well as what should be considered a "break" of a scheme. As usual, we consider only probabilistic polynomial-time adversaries $^{1}$

与任何安全定义一样，要形式化这一概念，我们需要定义敌手的能力以及什么应该被视为对方案的“攻破”。与往常一样，我们只考虑概率多项式时间敌手 $^{1}$

$^{1}$ See Section 4.6 for a discussion of information-theoretic message authentication, where no computational restrictions are placed on the adversary.

$^{1}$ 关于信息论消息认证的讨论见 4.6 节，在那里对敌手不施加任何计算限制。

and so the real question is how we model the adversary's interaction with the communicating parties. In the setting of message authentication, an adversary observing the communication between the honest parties may be able to see all the messages sent by those parties along with their corresponding tags. The adversary may also be able to influence the content of those messages, whether directly or indirectly (if, e.g., external actions of the adversary affect the messages sent by the parties). This is true, for example, in the web cookie example from earlier, where the user's own actions influence the contents of the cookie being stored on his computer.

因此，真正的问题是我们如何建模敌手与通信方的交互。在消息认证的设置中，观察诚实方之间通信的敌手可以看到这些方发送的所有消息及其对应的标签。敌手还可能能够影响这些消息的内容，无论是直接还是间接的（例如，如果敌手的外部行为影响了各方发送的消息）。例如，在我们之前的 Web Cookie 示例中，用户自己的行为影响存储在其计算机上的 cookie 的内容。

To model the above, we allow the adversary to request tags for any messages of its choice. Formally, we give the adversary access to a MAC oracle $\mathsf{Mac}_k(\cdot)$; the adversary can repeatedly submit any message $m$ of its choice to this oracle, and is given in return a tag $t \leftarrow \mathsf{Mac}_k(m)$. (For a fixed-length MAC, only messages of the correct length can be submitted.)

为了对上述情形建模，我们允许敌手为其选择的任何消息请求标签。形式化地，我们赋予敌手对 MAC 预言机 $\mathsf{Mac}_k(\cdot)$ 的访问权限；敌手可以反复向该预言机提交其任意选择的消息 $m$，并（从预言机）获得标签 $t \leftarrow \mathsf{Mac}_k(m)$ 作为响应。（对于固定长度 MAC，只能提交正确长度的消息。）

An attacker "breaks" the scheme if it succeeds in outputting a forgery, i.e., if it outputs a message m along with a tag t such that (1) t is a valid tag on the message m (i.e., $\mathsf{Vrfy}_{k}(m,t)=1$), and (2) the honest parties had not previously authenticated m (i.e., the adversary had not previously requested a tag on the message m from its oracle). These conditions imply that if the adversary were to send $(m,t)$ to one of the honest parties, then that party would be mistakenly fooled into thinking that m originated from the other legitimate party (since $\mathsf{Vrfy}_{k}(m,t)=1$) even though it did not.

如果敌手成功输出一个伪造，即它输出一个消息 $m$ 和标签 $t$，满足 (1) $t$ 是消息 $m$ 上的有效标签（即 $\mathsf{Vrfy}_{k}(m,t)=1$），且 (2) 诚实方之前未认证过 $m$（即敌手之前未从预言机请求过消息 m 的标签），则称敌手“攻破”了方案。这些条件意味着，如果敌手将 $(m,t)$ 发送给诚实方之一，那么该方就会被愚弄，错误地认为 m 来自另一个合法方（因为 $\mathsf{Vrfy}_{k}(m,t)=1$），尽管实际上并非如此。

A MAC that cannot be broken in the above sense is said to be existentially unforgeable under an adaptive chosen-message attack. "Existentially unforgeable" refers to the fact that the adversary is unable to forge a valid tag on any message; this should hold even if the attacker can carry out an "adaptive chosen-message attack" by which it is able to obtain tags on arbitrary messages chosen adaptively during its attack.

一个在上述意义上不可攻破的 MAC 被称为是**自适应选择消息攻击下的存在性不可伪造**的。“存在性不可伪造”指的是敌手无法在任何消息上伪造有效标签；即使攻击者能够执行“自适应选择消息攻击”（即在其攻击过程中自适应地选择任意消息并获取其标签），这一性质也应当成立。

The above discussion leads us to consider the following experiment for a message authentication code $\Pi = (\mathsf{Gen}, \mathsf{Mac}, \mathsf{Vrfy})$, an adversary $\mathcal{A}$, and security parameter $n$:

上述讨论引导我们考虑以下关于消息认证码 $\Pi = (\mathsf{Gen}, \mathsf{Mac}, \mathsf{Vrfy})$、敌手 $\mathcal{A}$ 和安全参数 $n$ 的实验：

The message authentication experiment $\mathsf{Mac-forge}_{\mathcal{A},\Pi}(n)$:

消息认证实验 $\mathsf{Mac-forge}_{\mathcal{A},\Pi}(n)$：

1. A key $k$ is generated by running $\mathsf{Gen}(1^{n})$.

   通过运行 $\mathsf{Gen}(1^{n})$ 生成密钥 $k$。

2. The adversary A is given input ${1}^n$ and oracle access to $\mathsf{Mac}_k(\cdot)$. The adversary eventually outputs $(m,t)$. Let Q denote the set of all queries that A submitted to its oracle.

   敌手 $\mathcal{A}$ 获得输入 ${1}^n$ 和对 $\mathsf{Mac}_k(\cdot)$ 的预言机访问。敌手最终输出 $(m,t)$。设 $\mathcal{Q}$ 表示 $\mathcal{A}$ 向其预言机提交的所有查询的集合。

3. $\mathcal{A}$ succeeds if and only if (1) $\mathsf{Vrfy}_{k}(m, t) = 1$ and (2) $m \notin \mathcal{Q}$. In that case the output of the experiment is defined to be 1.

   当且仅当 (1) $\mathsf{Vrfy}_{k}(m, t) = 1$ 且 (2) $m \notin \mathcal{Q}$ 时，$\mathcal{A}$ 成功。此时实验的输出定义为 1。

A MAC is secure if no efficient adversary can succeed in the above experiment with non-negligible probability.

如果没有任何高效敌手能够以不可忽略的概率在上述实验中成功，则称 MAC 是安全的。

DEFINITION 4.2 A message authentication code $\Pi = (\mathsf{Gen}, \mathsf{Mac}, \mathsf{Vrfy})$ is existentially unforgeable under an adaptive chosen-message attack, or just secure, if for all probabilistic polynomial-time adversaries A, there is a negligible function $\mathsf{negl}$ such that:

$$
\Pr[\mathsf{Mac-forge}_{\mathcal{A},\Pi}(n)=1]\leq\mathsf{negl}(n).
$$

**定义 4.2** 一个消息认证码 $\Pi = (\mathsf{Gen}, \mathsf{Mac}, \mathsf{Vrfy})$ 是**自适应选择消息攻击下的存在性不可伪造**的，或简称为安全的，如果对于所有概率多项式时间敌手 A，存在一个可忽略函数 $\mathsf{negl}$ 使得：

$$
\Pr[\mathsf{Mac-forge}_{\mathcal{A},\Pi}(n)=1]\leq\mathsf{negl}(n).
$$

Is the definition too strong? The above definition is rather strong in two respects. First, the adversary is allowed to repeatedly request tags for any messages of its choice. Second, the adversary is considered to have "broken" the scheme if it can output a valid tag on any previously unauthenticated message. One might object that both these components of the definition are unrealistic and overly strong, as in "real-world" usage of a MAC the honest parties would only authenticate "meaningful" messages (over which the adversary might have only limited control), and a forgery would only be damaging if it involved forging a valid tag on a "meaningful" message. Why not tailor the definition to capture this?

这个定义是否过强？上述定义在两个方面相当强。首先，敌手被允许重复为其选择的任何消息请求标签。其次，如果敌手能够输出任何先前未认证消息上的有效标签，就被认为“攻破”了方案。有人可能会反对说，定义中的这两个方面都不现实且过于强硬，因为在 MAC 的“真实世界”使用中，诚实方只会认证“有意义的”消息（敌手对此可能只有有限的控制），而只有当伪造涉及在“有意义的”消息上伪造有效标签时才会造成损害。为什么不据此调整定义来涵盖这种情况呢？

The crucial point is that what constitutes a meaningful message is entirely application dependent. While some applications of a MAC may only ever authenticate English-language messages, other applications may authenticate spreadsheet files, others database entries, and others raw data. Protocols may also be designed where anything will be authenticated—in fact, certain user-authentication protocols do exactly this. By making the definition of security for MACs as strong as possible, we ensure that secure MACs are broadly applicable for a wide range of purposes, without having to worry about compatibility of the MAC with the semantics of specific applications.

关键点在于，什么构成有意义的消息完全取决于应用。虽然 MAC 的某些应用可能只认证英文消息，但其他应用可能认证电子表格文件、数据库条目或原始数据。协议也可能被设计成对任何内容都进行认证——事实上，某些用户认证协议正是这样做的。通过使 MAC 的安全定义尽可能强，我们确保安全的 MAC 能够广泛适用于多种目的，而不必担心 MAC 与特定应用语义的兼容性。

Replay attacks. The above definition, and message authentication codes by themselves, offer no protection against replay attacks in which an attacker simply re-sends a previously authenticated message along with its (valid) tag. The fact that replay attacks are not accounted for in the definition does not mean they are not a serious security concern! Consider again the scenario where a user (say, Alice) sends a request to her bank to transfer \$1,000 from her account to some other user (say, Bob). In doing so, Alice can compute a tag and append it to her request so the bank knows the request is authentic. If the MAC is secure, Bob will be unable to intercept the request and change the amount to \$10,000 because this would involve forging a valid tag on a previously unauthenticated message. However, nothing prevents Bob from replaying Alice's message (along with its tag) ten times to the bank. If the bank accepts each of those messages, the net effect is still that \$10,000 will be transferred to Bob's account rather than the desired \$1,000.

重放攻击。上述定义以及消息认证码本身，不提供对重放攻击的保护——在重放攻击中，攻击者只是重新发送先前已认证的消息及其（有效的）标签。定义未考虑重放攻击这一事实并不意味着它们不是严重的安全问题！再次考虑一个场景：用户（比如 Alice）向她的银行发送请求，要求从她的账户向另一用户（比如 Bob）转账 \$1,000。在这样做时，Alice 可以计算一个标签并附加到她的请求上，以便银行知道请求是真实的。如果 MAC 是安全的，Bob 将无法拦截请求并将金额改为 \$10,000，因为这涉及在先前未认证的消息上伪造有效标签。然而，没有什么能阻止 Bob 将 Alice 的消息（连同其标签）向银行重放十次。如果银行接受每一条这样的消息，最终结果仍然是 \$10,000 将转入 Bob 的账户，而不是期望的 \$1,000。

Despite the real threat that replay attacks represent, a MAC by itself cannot protect against such attacks since verification is stateless (and so every time a valid pair $(m, t)$ is presented to the verification algorithm, it will always output 1). Instead, protection against replay attacks—if such protection is necessary in a given scenario—must be handled by some higher-level application. The reason the definition of a MAC is structured this way is, once again, because we are unwilling to assume any semantics for applications that use MACs; in particular, the decision as to whether or not a replayed message should be treated as "valid" may be application dependent.

尽管重放攻击构成真正的威胁，但 MAC 本身无法防御此类攻击，因为验证是无状态的（因此每次向验证算法呈现有效的 $(m, t)$ 时，它总是输出 1）。相反，对重放攻击的防御——如果在特定场景中需要这种防御——必须由某个更高级别的应用来处理。MAC 定义之所以这样设计，同样是因为我们不愿对使用 MAC 的应用假定任何语义；特别是，关于重放的消息是否应被视为“有效”的决定可能是与应用相关的。

Two common techniques for preventing replay attacks are to use sequence numbers (also known as counters) or time-stamps. The first approach requires the communicating users to maintain (synchronized) state, and can be problematic when users communicate over a lossy channel where messages are occasionally dropped (though this problem can be mitigated). In the second approach using time-stamps, the sender appends the current time $T$ (say, to the nearest millisecond) to the message before authenticating, and sends $T$ along with the message and the resulting tag $t$. When the receiver obtains $T, m, t$, it verifies that $t$ is a valid tag on $m\|T$ and that $T$ is within some acceptable clock skew of its own current time $T^{\prime}$. This method has its own drawbacks, including the need for the sender and receiver to maintain closely synchronized clocks, and the possibility that a replay attack can still take place if it is done quickly enough (specifically, within the acceptable time window). We will discuss replay attacks further (in a more general context) in Section 5.4.

防止重放攻击的两种常见技术是使用序列号（也称为计数器）或时间戳。第一种方法要求通信用户维护（同步的）状态，并且当用户通过偶尔丢包的有损耗信道通信时可能会有问题（尽管这个问题可以缓解）。在使用时间戳的第二种方法中，发送方在认证之前将当前时间 $T$（例如精确到毫秒）附加到消息上，并将 $T$ 与消息以及结果标签 $t$ 一起发送。当接收方获得 $T, m, t$ 时，它验证 $t$ 是 $m\|T$ 上的有效标签，并且 $T$ 在其自身当前时间 $T^{\prime}$ 的某个可接受时钟偏差范围内。这种方法有其自身的缺点，包括发送方和接收方需要保持紧密同步的时钟，以及重放攻击若足够快（即落在可接受的时间窗口内）则仍可能发生。我们将在 5.4 节（在更一般的语境下）进一步讨论重放攻击。

Strong unforgeability. As defined, a secure MAC ensures that an adversary cannot generate a valid tag on a message that was never previously authenticated. But it does not rule out the possibility that an attacker might be able to generate a new, valid tag on a previously authenticated message. In other words, a secure MAC guarantees that an attacker who learns tags $t_1, \ldots$ on messages $m_1, \ldots$ will be unable to forge a valid tag $t$ on any message $m \notin \{m_1, \ldots\}$. However, it may be possible for that adversary to generate a different valid tag $t^{\prime}_i \neq t_i$ on some previously authenticated message $m_i$. In standard applications of MACs, this type of adversarial behavior is not a concern. Nevertheless, in some settings it is useful to consider a stronger definition of security for MACs where such behavior is ruled out.

强不可伪造性。按定义，一个安全的 MAC 确保敌手无法在从未被认证过的消息上生成有效标签。但它并不排除攻击者可能在已认证的消息上生成一个新的、有效的标签。换句话说，一个安全的 MAC 保证学习到消息 $m_1, \ldots$ 上的标签 $t_1, \ldots$ 的攻击者将无法在任何 $m \notin \{m_1, \ldots\}$ 的消息上伪造有效标签 $t$。然而，该敌手可能能够在某个已认证的消息 $m_i$ 上生成一个不同的有效标签 $t^{\prime}_i \neq t_i$。在 MAC 的标准应用中，这种类型的敌手行为不是问题。尽管如此，在某些设置中，考虑一个排除此类行为的更强的 MAC 安全定义是有用的。

To model this formally, we consider a modified experiment Mac-sforge that is defined in exactly the same way as Mac-forge, except that now the set $\mathcal{Q}$ contains pairs of oracle queries and their associated responses. (That is, $(m,t) \in \mathcal{Q}$ if $\mathcal{A}$ queried $\mathsf{Mac}_k(m)$ and received in response the tag $t$.) The adversary $\mathcal{A}$ succeeds (and experiment Mac-sforge evaluates to 1) if and only if $\mathcal{A}$ outputs $(m,t)$ such that $\mathsf{Vrfy}_k(m,t) = 1$ and $(m,t) \notin \mathcal{Q}$.

为了形式化地建模这一点，我们考虑一个修改后的实验 Mac-sforge，其定义与 Mac-forge 完全相同，只是现在集合 $\mathcal{Q}$ 包含预言机查询及其相关联的响应。（即，如果 $\mathcal{A}$ 查询了 $\mathsf{Mac}_k(m)$ 并收到标签 $t$ 作为响应，则 $(m,t) \in \mathcal{Q}$。）敌手 $\mathcal{A}$ 成功（实验 Mac-sforge 评估为 1）当且仅当 $\mathcal{A}$ 输出 $(m,t)$ 使得 $\mathsf{Vrfy}_k(m,t) = 1$ 且 $(m,t) \notin \mathcal{Q}$。

DEFINITION 4.3 A message authentication code $\Pi = (\mathsf{Gen}, \mathsf{Mac}, \mathsf{Vrfy})$ is strongly secure if for all probabilistic polynomial-time adversaries $\mathcal{A}$, there is a negligible function $\mathsf{negl}$ such that:

$$
\Pr[\mathsf{Mac-sforge}_{\mathcal{A},\Pi}(n)=1]\leq\mathsf{negl}(n).
$$

**定义 4.3** 一个消息认证码 $\Pi = (\mathsf{Gen}, \mathsf{Mac}, \mathsf{Vrfy})$ 是**强安全**的，如果对于所有概率多项式时间敌手 $\mathcal{A}$，存在一个可忽略函数 $\mathsf{negl}$ 使得：

$$
\Pr[\mathsf{Mac-sforge}_{\mathcal{A},\Pi}(n)=1]\leq\mathsf{negl}(n).
$$

It is not hard to see that if a secure MAC uses canonical verification then it is also strongly secure. This is important since many real-world MACs use canonical verification. We leave the proof of the following as an exercise.

不难看出，如果一个安全的 MAC 使用规范验证，那么它也是强安全的。这一点很重要，因为许多现实世界的 MAC 都使用规范验证。我们将以下命题的证明留作练习。

PROPOSITION 4.4 Let $\Pi = (\mathsf{Gen}, \mathsf{Mac}, \mathsf{Vrfy})$ be a secure (deterministic) MAC that uses canonical verification. Then $\Pi$ is strongly secure.

**命题 4.4** 设 $\Pi = (\mathsf{Gen}, \mathsf{Mac}, \mathsf{Vrfy})$ 是一个使用规范验证的安全（确定性）MAC。则 $\Pi$ 是强安全的。

Verification queries. Definitions 4.2 and 4.3 consider an adversary given access to a MAC oracle, which corresponds to a real-world adversary who can influence an honest sender to generate a tag for some message $m$. One could also consider an adversary who interacts with an honest receiver, sending $(m,t)$ to the receiver to learn whether $\mathsf{Vrfy}_k(m,t) = 1$. Such an adversary could be captured formally in the natural way by giving the adversary in the above definitions access to a verification oracle as well.

验证查询。定义 4.2 和 4.3 考虑的是拥有 MAC 预言机访问权限的敌手，这对应于能够影响诚实的发送方为某个消息 $m$ 生成标签的现实世界敌手。我们还可以考虑与诚实接收方交互的敌手，它向接收方发送 $(m,t)$ 以了解 $\mathsf{Vrfy}_k(m,t) = 1$ 是否成立。要形式化地刻画这类敌手，自然的方式是在上述定义中额外赋予敌手对验证预言机的访问权限。

A definition that incorporates a verification oracle in this way is, perhaps, the "right" way to define security for message authentication codes. It turns out, however, that for MACs that use canonical verification it makes no difference: any such MAC that satisfies Definition 4.2 also satisfies the definitional variant in which verification queries are allowed. Moreover, any strongly secure MAC remains strongly secure even if verification queries are possible. In general, however, allowing verification queries can make a difference. Since most MACs covered in this book (as well as MACs used in practice) use canonical verification and/or are strongly secure, we use the traditional definitions that omit access to a verification oracle.

将验证预言机以这种方式纳入定义或许是定义消息认证码安全性的“正确”方式。然而，对于使用规范验证的 MAC 而言，这并无区别：任何满足定义 4.2 的此类 MAC 也满足允许验证查询的定义变体。此外，任何强安全的 MAC 即使允许验证查询也仍然是强安全的。然而，一般来说，允许验证查询可能会产生差别。由于本书涵盖的大多数 MAC（以及实践中使用的 MAC）都使用规范验证和/或具有强安全性，我们使用省略验证预言机访问的传统定义。

A potential timing attack. One issue not addressed by the above discussion of verification queries is the possibility of carrying out a timing attack on MAC verification. Here, we consider an adversary who can send message/tag pairs to the receiver—thus using the receiver as a verification oracle—and learn not only whether the receiver accepts or rejects, but also the time it takes for the receiver to make this decision. We show that if such an attack is possible then a natural implementation of MAC verification leads to an easily exploitable vulnerability. (In our usual cryptographic definitions of security, the attacker learns only the output of the oracles it has access to, but nothing else. The attack we describe here, which is an example of a side-channel attack, shows that certain real-world attacks are not captured by the usual definitions.)

潜在的时序攻击。上述关于验证查询的讨论未涉及的一个问题是在 MAC 验证上实施时序攻击的可能性。在此，我们考虑这样的敌手：它能向接收方发送消息/标签对——从而把接收方用作验证预言机——并且不仅知道接收方是接受还是拒绝，还知道接收方做出这一判断所花费的时间。我们证明，如果这种攻击是可能的，那么 MAC 验证的自然实现会导致一个易于利用的漏洞。（在我们通常的密码学安全定义中，攻击者只了解其有权访问的预言机的输出，除此之外一无所知。我们在此描述的攻击，是侧信道攻击的一个示例，表明某些现实世界的攻击并未被通常的定义所捕捉。）

Concretely, assume a MAC using canonical verification. To verify a tag t on a message m, the receiver computes $t^{\prime} := \mathsf{Mac}_k(m)$ and then compares $t^{\prime}$ to t, outputting 1 if and only if $t^{\prime}$ and t are equal. Assume this comparison is implemented using a standard routine (like $\text{strncmp}$ in C) that compares t and $t^{\prime}$ one byte at a time, and rejects as soon as the first unequal byte is encountered. The observation is that, when implemented in this way, the time to reject differs depending on the position of the first unequal byte.

具体来说，假设一个使用规范验证的 MAC。为了验证消息 $m$ 上的标签 $t$，接收方计算 $t^{\prime} := \mathsf{Mac}_k(m)$，然后将 $t^{\prime}$ 与 t 进行比较，当且仅当 $t^{\prime}$ 和 t 相等时输出 1。假设这种比较使用一个标准例程（如 C 语言中的 $\text{strncmp}$）实现，该例程逐字节比较 t 和 $t^{\prime}$，一旦遇到第一个不相等的字节就拒绝。注意，以这种方式实现时，拒绝的时间取决于第一个不相等字节的位置。

It is possible to use this seemingly inconsequential information to forge a tag on any desired message $m$. Say the attacker knows the first $i$ bytes of the (unique) valid tag for $m$. (At the outset, $i = 0$.) The attacker can learn the next byte of the valid tag by sending $(m, t_0)$, ..., $(m, t_{255})$ to the receiver, where $t_j$ is the string with the first $i$ bytes set correctly, the $(i+1)$st byte equal to $j$ (in hexadecimal), and the remaining bytes set to $\mathtt{0x00}$. All these tags will likely be rejected (if not, then the attacker succeeds anyway); however, for exactly one of these tags the first $(i+1)$ bytes will be correct and rejection will take slightly longer than the rest. If $t_j$ is the tag that caused rejection to take the longest, the attacker learns that the $(i+1)$st byte of the valid tag is $j$. In this way, the attacker learns each byte of the valid tag using at most 256 queries to the verification oracle. For a 16-byte tag, this attack requires at most ${16} \cdot 256 = 4096$ verification queries to learn the entire tag.

可以利用这种看似无关紧要的信息来伪造任意期望消息 $m$ 上的标签。假设攻击者知道 $m$ 的（唯一）有效标签的前 $i$ 个字节。（一开始，$i = 0$。）攻击者可以通过向接收方发送 $(m, t_0)$、...、$(m, t_{255})$ 来学习有效标签的下一个字节，其中 $t_j$ 是一个字符串，其前 $i$ 个字节设置正确，第 $(i+1)$ 个字节等于 $j$（十六进制），其余字节设置为 $\mathtt{0x00}$。所有这些标签很可能被拒绝（如果没有被拒绝，那么攻击者无论如何都成功了）；然而，对于其中恰好一个标签，前 $(i+1)$ 个字节将是正确的，拒绝所需的时间将比其他标签稍长。如果 $t_j$ 是导致拒绝时间最长的标签，攻击者就知道有效标签的第 $(i+1)$ 个字节是 $j$。通过这种方式，攻击者使用最多 256 次对验证预言机的查询即可学习有效标签的每个字节。对于一个 16 字节的标签，这种攻击最多需要 ${16} \cdot 256 = 4096$ 次验证查询即可学习整个标签。

One might wonder whether this attack is realistic, as it requires access to a verification oracle as well as the ability to measure the difference in time taken to compare i vs. $i+1$ bytes. In fact, such attacks have been carried out against real systems! As just one example, MACs were used to verify code updates in the Xbox 360, and the implementation of MAC verification took roughly 2.2 milliseconds to compare each byte. Attackers were able to exploit this and load pirated games onto the hardware.

有人可能会怀疑这种攻击是否现实，因为它需要访问验证预言机以及测量比较 i 个字节与 $i+1$ 个字节所需时间差异的能力。事实上，这种攻击已经在真实系统上实施过！仅举一个例子，Xbox 360 使用 MAC 来验证代码更新，而 MAC 验证的实现大约需要 2.2 毫秒来比较每个字节。攻击者能够利用这一点将盗版游戏加载到硬件上。

Based on the above, we conclude that MAC verification should use time-independent string comparison that always compares all bytes.

基于上述，我们得出结论：MAC 验证应使用常数时间（与内容无关）的字符串比较，即始终比较所有字节。

## 4.3 Constructing Secure Message Authentication Codes　4.3 构造安全消息认证码

### 4.3.1 A Fixed-Length MAC　4.3.1 固定长度MAC

Pseudorandom functions are a natural tool for constructing secure message authentication codes. Intuitively, if the tag $t$ is obtained by applying a pseudorandom function to the message $m$, then forging a tag on a previously unauthenticated message requires the adversary to correctly guess the value of the pseudorandom function at a "new" input point. The probability of guessing the value of a random function on a new point is ${2}^{-n}$ (if the output length of the function is $n$). The probability of guessing such a value for a pseudorandom function can be only negligibly greater.

伪随机函数是构造安全消息认证码的自然工具。直观地说，如果标签 $t$ 是通过将伪随机函数应用于消息 $m$ 得到的，那么伪造一个先前未认证消息上的标签需要敌手正确猜测伪随机函数在“新”输入点上的值。在一个新点上猜测随机函数值的概率是 ${2}^{-n}$（如果函数的输出长度为 $n$）。而对于伪随机函数，猜中这种值的概率至多比前者大一个可忽略的量。

The above idea, shown in Construction 4.5, gives a secure fixed-length MAC for short messages. In Section 4.3.2, we show how to extend this to handle messages of arbitrary length. We explore more efficient constructions of MACs for arbitrary-length messages in Sections 4.4, 4.5, and 6.3.2.

上述思想如构造 4.5 所示，给出了一个适用于短消息的安全固定长度 MAC。在 4.3.2 节中，我们将展示如何将其扩展以处理任意长度的消息。我们将在 4.4、4.5 和 6.3.2 节中探索更高效的任意长度消息 MAC 构造。

> **CONSTRUCTION 4.5**　**构造 4.5**
>
> Let F be a (length preserving) pseudorandom function. Define a fixed-length MAC for messages of length n as follows:
>
> - Mac: on input a key $k \in \{0,1\}^n$ and a message $m \in \{0,1\}^n$, output the tag $t := F_k(m)$.
>
> - $\mathsf{Vrfy}$: on input a key $k \in \{0,1\}^n$, a message $m \in \{0,1\}^n$, and a tag $t \in \{0,1\}^n$, output 1 if and only if $t \overset{?}{=} F_k(m)$.
>
> A fixed-length MAC from any pseudorandom function.
>
> 设 F 是一个（长度保持的）伪随机函数。定义适用于长度为 n 的消息的固定长度 MAC 如下：
>
> - Mac：输入密钥 $k \in \{0,1\}^n$ 和消息 $m \in \{0,1\}^n$，输出标签 $t := F_k(m)$。
>
> - $\mathsf{Vrfy}$：输入密钥 $k \in \{0,1\}^n$、消息 $m \in \{0,1\}^n$ 和标签 $t \in \{0,1\}^n$，当且仅当 $t \overset{?}{=} F_k(m)$ 时输出 1。
>
> 来自任意伪随机函数的固定长度 MAC。

THEOREM 4.6 If F is a pseudorandom function, then Construction 4.5 is a secure fixed-length MAC for messages of length n.

**定理 4.6** 如果 F 是一个伪随机函数，则构造 4.5 是一个适用于长度为 n 的消息的安全固定长度 MAC。

PROOF As in the analysis of previous schemes based on pseudorandom functions, we first replace the pseudorandom function with a truly random function and show that this has limited impact on an adversary's success probability. We then analyze the scheme when using a truly random function.

**证明** 与之前基于伪随机函数的方案分析一样，我们首先将伪随机函数替换为真随机函数，并证明这对敌手的成功概率影响有限。然后我们分析使用真随机函数时的方案。

Let A be a probabilistic polynomial-time adversary. Consider the message authentication code $\widetilde{\Pi} = (\mathsf{Gen}, \mathsf{Mac}, \mathsf{Vrfy})$ which is the same as $\Pi = (\mathsf{Mac}, \mathsf{Vrfy})$ in Construction 4.5 except that a truly random function $f$ is used instead of the pseudorandom function $F_k$. That is, $\widetilde{\mathsf{Gen}}(1^n)$ works by choosing a uniform function $f \in \mathsf{Func}_n$, and $\widetilde{\mathsf{Mac}}$ computes a tag just as $\mathsf{Mac}$ does except that $f$ is used instead of $F_k$.

设 A 是一个概率多项式时间敌手。考虑消息认证码 $\widetilde{\Pi} = (\mathsf{Gen}, \mathsf{Mac}, \mathsf{Vrfy})$，它与构造 4.5 中的 $\Pi = (\mathsf{Mac}, \mathsf{Vrfy})$ 相同，只是使用真随机函数 $f$ 代替了伪随机函数 $F_k$。也就是说，$\widetilde{\mathsf{Gen}}(1^n)$ 通过选择均匀函数 $f \in \mathsf{Func}_n$ 来工作，而 $\widetilde{\mathsf{Mac}}$ 计算标签的方式与 $\mathsf{Mac}$ 相同，只是使用 $f$ 代替 $F_k$。

We show that there is a negligible function $\mathsf{negl}$ such that

$$
\left|\Pr[\mathsf{Mac-forge}_{\mathcal{A},\Pi}(n)=1]-\Pr[\mathsf{Mac-forge}_{\mathcal{A},\widetilde{\Pi}}(n)=1]\right|\leq\mathsf{negl}(n). \tag{4.1}
$$

我们证明存在一个可忽略函数 $\mathsf{negl}$ 使得

$$
\left|\Pr[\mathsf{Mac-forge}_{\mathcal{A},\Pi}(n)=1]-\Pr[\mathsf{Mac-forge}_{\mathcal{A},\widetilde{\Pi}}(n)=1]\right|\leq\mathsf{negl}(n). \tag{4.1}
$$

To prove this, we construct a polynomial-time distinguisher $D$ that is given oracle access to some function $\mathcal{O}$, and whose goal is to determine whether $\mathcal{O}$ is pseudorandom (i.e., equal to $F_k$ for uniform $k \in \{0,1\}^n$) or random (i.e., equal to $f$ for uniform $f \in \mathsf{Func}_n$). To do this, $D$ simulates the message authentication experiment for $\mathcal{A}$ and observes whether $\mathcal{A}$ succeeds in outputting a valid tag on a "new" message. If so, $D$ guesses that its oracle is a pseudo-random function; otherwise, $D$ guesses that its oracle is a random function. In detail:

为了证明这一点，我们构造一个多项式时间区分器 $D$，它被赋予对某个函数 $\mathcal{O}$ 的预言机访问，目标是确定 $\mathcal{O}$ 是伪随机的（即等于对均匀 $k \in \{0,1\}^n$ 的 $F_k$）还是随机的（即等于对均匀 $f \in \mathsf{Func}_n$ 的 $f$）。为此，$D$ 为 $\mathcal{A}$ 模拟消息认证实验，并观察 $\mathcal{A}$ 是否成功地在“新”消息上输出了有效标签。如果是，$D$ 猜测其预言机是伪随机函数；否则，$D$ 猜测其预言机是随机函数。具体如下：

**Distinguisher D:**　**区分器 D：**

D is given input ${1}^n$ and access to an oracle $\mathcal{O} : \{0,1\}^n \to \{0,1\}^n$, and works as follows:
D 获得输入 ${1}^n$ 和对预言机 $\mathcal{O} : \{0,1\}^n \to \{0,1\}^n$ 的访问，工作如下：

1. Run $\mathcal{A}(1^n)$. Whenever $\mathcal{A}$ queries its MAC oracle on a message $m$ (i.e., whenever $\mathcal{A}$ requests a tag on a message $m$), answer this query in the following way:

   运行 $\mathcal{A}(1^n)$。每当 $\mathcal{A}$ 查询其 MAC 预言机关于消息 $m$ 时（即每当 $\mathcal{A}$ 请求消息 $m$ 上的标签），按以下方式回答该查询：

   Query O with m and obtain response t; return t to A.

   以 m 查询 O 并获得响应 t；将 t 返回给 A。

2. When $\mathcal{A}$ outputs $(m,t)$ at the end of its execution, do:

   当 $\mathcal{A}$ 在其执行结束时输出 $(m,t)$ 时，执行：

   (a) Query O with m and obtain response $t^{\prime}$.

   (a) 以 m 查询 O 并获得响应 $t^{\prime}$。

   (b) If (1) $t^{\prime} = t$ and (2) A never queried its MAC oracle on m, then output 1; otherwise, output 0.

   (b) 如果 (1) $t^{\prime} = t$ 且 (2) A 从未在其 MAC 预言机上查询过 m，则输出 1；否则输出 0。

It is clear that D runs in polynomial time.

显然，$D$ 在多项式时间内运行。

If $D$'s oracle is $F_k$ for a uniform $k$, then the view of $\mathcal{A}$ when run as a subroutine by $D$ is distributed identically to the view of $\mathcal{A}$ in experiment $\mathsf{Mac-forge}_{\mathcal{A},\Pi}(n)$. Moreover, $D$ outputs 1 exactly when $\mathsf{Mac-forge}_{\mathcal{A},\Pi}(n) = 1$. Therefore

$$
\Pr[D^{F_{k}(\cdot)}(1^{n})=1]=\Pr[\mathsf{Mac-forge}_{\mathcal{A},\Pi}(n)=1],
$$

where $k \in \{0,1\}^n$ is chosen uniformly on the left-hand side above. If $D$'s oracle is a random function, then the view of $\mathcal{A}$ when run as a subroutine by $D$ is distributed identically to the view of $\mathcal{A}$ in experiment $\mathsf{Mac-forge}_{\mathcal{A},\widetilde{\Pi}}(n)$, and again $D$ outputs 1 exactly when $\mathsf{Mac-forge}_{\mathcal{A},\widetilde{\Pi}}(n) = 1$. Thus,

$$
\Pr[D^{f(\cdot)}(1^{n})=1]=\Pr[\mathsf{Mac-forge}_{\mathcal{A},\widetilde{\Pi}}(n)=1],
$$

where $f \in \mathsf{Func}_n$ is chosen uniformly. Since $F$ is a pseudorandom function and $D$ runs in polynomial time, there is a negligible function $\mathsf{negl}$ such that

$$
\left|\Pr[D^{F_{k}(\cdot)}(1^{n})=1]-\Pr[D^{f(\cdot)}(1^{n})=1]\right|\leq\mathsf{negl}(n).
$$

如果 $D$ 的预言机是对均匀 $k$ 的 $F_k$，那么当 $\mathcal{A}$ 作为 $D$ 的子程序运行时，$\mathcal{A}$ 的视图与 $\mathcal{A}$ 在实验 $\mathsf{Mac-forge}_{\mathcal{A},\Pi}(n)$ 中的视图分布相同。此外，$D$ 输出 1 当且仅当 $\mathsf{Mac-forge}_{\mathcal{A},\Pi}(n) = 1$。因此

$$
\Pr[D^{F_{k}(\cdot)}(1^{n})=1]=\Pr[\mathsf{Mac-forge}_{\mathcal{A},\Pi}(n)=1],
$$

其中左侧的 $k \in \{0,1\}^n$ 是均匀选择的。如果 $D$ 的预言机是一个随机函数，那么当 $\mathcal{A}$ 作为 $D$ 的子程序运行时，$\mathcal{A}$ 的视图与 $\mathcal{A}$ 在实验 $\mathsf{Mac-forge}_{\mathcal{A},\widetilde{\Pi}}(n)$ 中的视图分布相同，并且 $D$ 输出 1 当且仅当 $\mathsf{Mac-forge}_{\mathcal{A},\widetilde{\Pi}}(n) = 1$。因此

$$
\Pr[D^{f(\cdot)}(1^{n})=1]=\Pr[\mathsf{Mac-forge}_{\mathcal{A},\widetilde{\Pi}}(n)=1],
$$

其中 $f \in \mathsf{Func}_n$ 是均匀选择的。由于 $F$ 是伪随机函数且 $D$ 在多项式时间内运行，存在一个可忽略函数 $\mathsf{negl}$ 使得

$$
\left|\Pr[D^{F_{k}(\cdot)}(1^{n})=1]-\Pr[D^{f(\cdot)}(1^{n})=1]\right|\leq\mathsf{negl}(n).
$$

This implies Equation (4.1).

这意味着式 (4.1)。

To complete the proof, we observe that

$$
\Pr[\mathsf{Mac-forge}_{\mathcal{A},\widetilde{\Pi}}(n)=1]\leq2^{-n}. \tag{4.2}
$$

because for any message $m \notin \mathcal{Q}$ that $\mathcal{A}$ did not query to its MAC oracle, the tag $t^{\prime} = f(m)$ is uniformly distributed in $\{0,1\}^n$ from $\mathcal{A}$'s point of view (since the values of $f$ on all inputs are uniform and independent). Thus, the probability that $\mathcal{A}$ can correctly guess $t^{\prime}$ (for any $m \notin \mathcal{Q}$) is ${2}^{-n}$.

为了完成证明，我们观察到

$$
\Pr[\mathsf{Mac-forge}_{\mathcal{A},\widetilde{\Pi}}(n)=1]\leq2^{-n}. \tag{4.2}
$$

因为对于任何 $\mathcal{A}$ 未查询其 MAC 预言机的消息 $m \notin \mathcal{Q}$，从 $\mathcal{A}$ 的角度看，标签 $t^{\prime} = f(m)$ 均匀分布在 $\{0,1\}^n$ 中（因为 $f$ 在所有输入上的值都是均匀且独立的）。因此，$\mathcal{A}$ 能够正确猜测 $t^{\prime}$（对于任何 $m \notin \mathcal{Q}$）的概率是 ${2}^{-n}$。

Equations (4.1) and (4.2) together show that

$$
\Pr[\mathsf{Mac-forge}_{\mathcal{A},\Pi}(n)=1]\leq2^{-n}+\mathsf{negl}(n),
$$

completing the proof of the theorem.

式 (4.1) 和 (4.2) 共同表明

$$
\Pr[\mathsf{Mac-forge}_{\mathcal{A},\Pi}(n)=1]\leq2^{-n}+\mathsf{negl}(n),
$$

至此完成了定理的证明。

### 4.3.2 Domain Extension for MACs　4.3.2 MAC的域扩展

Construction 4.5 is important in that it shows a general paradigm for constructing secure message authentication codes from pseudorandom functions. Unfortunately, the construction is only capable of handling fixed-length messages that are furthermore rather short. $^{2}$ These limitations are unacceptable in most real-world applications. We show here how a MAC handling arbitrary-length messages can be constructed from any fixed-length MAC for messages of length $n$. The construction we show is not very efficient and is unlikely to be used in practice; far more efficient constructions of secure MACs are known, as we will see later. We include the present construction for its simplicity and generality, and for pedagogical purposes.

构造 4.5 之所以重要，是因为它展示了一种从伪随机函数构造安全消息认证码的通用范式。不幸的是，该构造只能处理固定长度的消息，而且这些消息还相当短。$^{2}$ 这些限制在大多数现实世界的应用中是不可接受的。我们在此展示如何从任何适用于长度为 $n$ 的消息的固定长度 MAC 构造出处理任意长度消息的 MAC。我们展示的构造效率不高，不太可能用于实践；已知存在高效得多的安全 MAC 构造，我们稍后会看到。我们包含此构造是出于其简单性和通用性，以及教学目的。

$^{2}$ Given a pseudorandom function taking arbitrary-length inputs, Construction 4.5 would yield a secure MAC for messages of arbitrary length. Likewise, a pseudorandom function with a larger domain would yield a secure MAC for longer messages. However, existing practical pseudorandom functions (i.e., block ciphers) take short, fixed-length inputs.

$^{2}$ 给定一个接受任意长度输入的伪随机函数，构造 4.5 将产生一个适用于任意长度消息的安全 MAC。类似地，定义域更大的伪随机函数将产生适用于更长消息的安全 MAC。然而，现有的实用伪随机函数（即分组密码）接受的是短的、固定长度的输入。

Let $\Pi^{\prime} = (\mathsf{Mac}^{\prime}, \mathsf{Vrfy}^{\prime})$ be a secure fixed-length MAC for messages of length $n$. Before presenting the construction of a MAC for arbitrary-length messages based on $\Pi^{\prime}$, we rule out some simple ideas and describe some canonical attacks that must be prevented.

设 $\Pi^{\prime} = (\mathsf{Mac}^{\prime}, \mathsf{Vrfy}^{\prime})$ 是一个适用于长度为 $n$ 的消息的安全固定长度 MAC。在给出基于 $\Pi^{\prime}$ 的任意长度消息 MAC 的构造之前，我们先排除一些简单的想法，并描述一些必须防止的典型攻击。

1. A natural first idea is to parse the message $m$ as a sequence of $n$-bit blocks $m_1, \ldots, m_d$ and authenticate each block separately, i.e., compute $t_i := \mathsf{Mac}_k^{\prime}(m_i)$ and output $\langle t_1, \ldots, t_d \rangle$ as the tag. This prevents an adversary from sending any previously unauthenticated block without being detected. However, it does not prevent a block re-ordering attack in which the attacker shuffles the order of blocks in an authenticated message. Specifically, if $\langle t_1, t_2 \rangle$ is a valid tag on the message $m_1, m_2$ (with $m_1 \neq m_2$), then an attacker can construct a valid tag $\langle t_2, t_1 \rangle$ on the (new) message $m_2, m_1$, something that is not allowed by Definition 4.2.

   一个自然的初步想法是将消息 $m$ 解析为 $n$ 比特块的序列 $m_1, \ldots, m_d$，并对每个块分别进行认证，即计算 $t_i := \mathsf{Mac}_k^{\prime}(m_i)$ 并输出 $\langle t_1, \ldots, t_d \rangle$ 作为标签。这可以防止敌手在未被检测到的情况下发送任何先前未认证的块。然而，这并不能防止**块重排攻击**，即攻击者打乱已认证消息中块的顺序。具体来说，如果 $\langle t_1, t_2 \rangle$ 是消息 $m_1, m_2$（$m_1 \neq m_2$）上的有效标签，那么攻击者可以在（新的）消息 $m_2, m_1$ 上构造有效标签 $\langle t_2, t_1 \rangle$，这是定义 4.2 所不允许的。

2. We can prevent the previous attack by authenticating a block index along with each block. That is, we now compute $t_i = \mathsf{Mac}_k^{\prime}(i\|m_i)$ for all $i$, and output $\langle t_1, \ldots, t_d \rangle$ as the tag. (Note that now $|m_i| < n$.) This does not prevent a truncation attack whereby an attacker simply drops blocks from the end of the message (and drops the corresponding blocks of the tag as well).

   我们可以通过在每个块中附加块索引来防止上述攻击。也就是说，我们现在对所有 $i$ 计算 $t_i = \mathsf{Mac}_k^{\prime}(i\|m_i)$，并输出 $\langle t_1, \ldots, t_d \rangle$ 作为标签。（注意，现在 $|m_i| < n$。）但这不能防止**截断攻击**，即攻击者简单地丢弃消息末尾的块（同时也丢弃标签中相应的块）。

3. A truncation attack can be thwarted by additionally authenticating the message length along with each block. (Authenticating the message length as a separate block does not work. Do you see why?) That is, compute $t_i = \mathsf{Mac}_k^{\prime}(\ell \|i\|m_i)$ for all $i$, where $\ell$ denotes the length of the message in bits. (Once again, the block length $|m_i|$ will need to decrease.) This scheme is vulnerable to a "mix-and-match" attack where the adversary combines blocks from different messages. For example, if the adversary obtains tags $\langle t_1, \ldots, t_d \rangle$ and $\langle t^{\prime}_1, \ldots, t^{\prime}_d \rangle$ on messages $m = m_1, \ldots, m_d$ and $m^{\prime} = m^{\prime}_1, \ldots, m^{\prime}_d$, respectively, it can output the valid tag $\langle t_1, t^{\prime}_2, t_3, t^{\prime}_4, \ldots \rangle$ on the message $m_1, m^{\prime}_2, m_3, m^{\prime}_4, \ldots$.

   截断攻击可以通过额外在每个块中认证消息长度来阻止。（将消息长度作为一个单独的块进行认证是不行的。你知道为什么吗？）也就是说，对所有 $i$ 计算 $t_i = \mathsf{Mac}_k^{\prime}(\ell \|i\|m_i)$，其中 $\ell$ 表示消息的比特长度。（再次提醒，块长度 $|m_i|$ 需要减小。）这种方案容易受到“混合匹配”攻击，即敌手组合来自不同消息的块。例如，如果敌手分别获得消息 $m = m_1, \ldots, m_d$ 和 $m^{\prime} = m^{\prime}_1, \ldots, m^{\prime}_d$ 上的标签 $\langle t_1, \ldots, t_d \rangle$ 和 $\langle t^{\prime}_1, \ldots, t^{\prime}_d \rangle$，它可以在消息 $m_1, m^{\prime}_2, m_3, m^{\prime}_4, \ldots$ 上输出有效标签 $\langle t_1, t^{\prime}_2, t_3, t^{\prime}_4, \ldots \rangle$。

We can prevent this last attack by also including a random "message identifier" in each block that prevents the attacker from combining blocks from different messages. This leads us to Construction 4.7. (The scheme only handles messages of length less than ${2}^{n/4}$, but this is an exponential bound.)

我们可以通过在每个块中包含一个随机“消息标识符”来防止这最后一种攻击，该标识符阻止攻击者组合来自不同消息的块。这引导我们得到构造 4.7。（该方案只处理长度小于 ${2}^{n/4}$ 的消息，但这是一个指数级界限。）

THEOREM 4.8 If $\Pi^{\prime}$ is a secure fixed-length MAC for messages of length n, then Construction 4.7 is a secure MAC (for arbitrary-length messages).

**定理 4.8** 如果 $\Pi^{\prime}$ 是一个适用于长度为 n 的消息的安全固定长度 MAC，则构造 4.7 是一个安全的（适用于任意长度消息的）MAC。

> **CONSTRUCTION 4.7**　**构造 4.7**
>
> Let $\Pi^{\prime} = (\mathsf{Mac}^{\prime}, \mathsf{Vrfy}^{\prime})$ be a fixed-length MAC for messages of length n. Define a MAC as follows:
>
> - Mac: on input a key $k \in \{0,1\}^n$ and a message $m \in \{0,1\}^*$ of (nonzero) length $\ell < 2^{n/4}$, parse m as d blocks $m_1, \ldots, m_d$, each of length $n/4$. (The final block is padded with 0s if necessary.) Choose a uniform message identifier $r \in \{0,1\}^{n/4}$. For $i = 1, \ldots, d$, compute $t_i \leftarrow \mathsf{Mac}_k^{\prime}(r\|\ell\|i\|m_i)$, where $i, \ell$ are encoded as strings of length $n/4$.$^{\dagger}$ Output the tag $t := \langle r, t_1, \ldots, t_d \rangle$.
>
> - $\mathsf{Vrfy}$: on input a key $k \in \{0,1\}^n$, a message $m \in \{0,1\}^*$ of nonzero length $\ell < 2^{n/4}$, and a tag $t = \langle r, t_1, \ldots, t_{d^{\prime}} \rangle$, parse $m$ as $d$ blocks $m_1, \ldots, m_d$, each of length $n/4$. (The final block is padded with 0s if necessary.) Output 1 if and only if $d^{\prime} = d$ and $\mathsf{Vrfy}^{\prime}_k(r\|\ell\|i\|m_i, t_i) = 1$ for ${1} \leq i \leq d$.
>
> $^{\dagger}$ Note that i and $\ell$ can be encoded using n/4 bits because i, $\ell < 2^{n/4}$.
>
> A MAC for arbitrary-length messages from any fixed-length MAC.
>
> 设 $\Pi^{\prime} = (\mathsf{Mac}^{\prime}, \mathsf{Vrfy}^{\prime})$ 是一个适用于长度为 n 的消息的固定长度 MAC。定义 MAC 如下：
>
> - Mac：输入密钥 $k \in \{0,1\}^n$ 和（非零）长度 $\ell < 2^{n/4}$ 的消息 $m \in \{0,1\}^*$，将 m 解析为 d 个块 $m_1, \ldots, m_d$，每个块长度为 $n/4$。（如有必要，最后一个块用 0 填充。）均匀选取消息标识符 $r \in \{0,1\}^{n/4}$。对于 $i = 1, \ldots, d$，计算 $t_i \leftarrow \mathsf{Mac}_k^{\prime}(r\|\ell\|i\|m_i)$，其中 $i, \ell$ 编码为长度为 $n/4$ 的字符串。$^{\dagger}$ 输出标签 $t := \langle r, t_1, \ldots, t_d \rangle$。
>
> - $\mathsf{Vrfy}$：输入密钥 $k \in \{0,1\}^n$、（非零）长度 $\ell < 2^{n/4}$ 的消息 $m \in \{0,1\}^*$ 和标签 $t = \langle r, t_1, \ldots, t_{d^{\prime}} \rangle$，将 $m$ 解析为 $d$ 个块 $m_1, \ldots, m_d$，每个块长度为 $n/4$。（如有必要，最后一个块用 0 填充。）当且仅当 $d^{\prime} = d$ 且对所有 ${1} \leq i \leq d$ 有 $\mathsf{Vrfy}^{\prime}_k(r\|\ell\|i\|m_i, t_i) = 1$ 时输出 1。
>
> $^{\dagger}$ 注意 i 和 $\ell$ 可以使用 n/4 比特编码，因为 i, $\ell < 2^{n/4}$。
>
> 来自任意固定长度 MAC 的任意长度消息 MAC。

PROOF The intuition is that since $\Pi^{\prime}$ is secure, an adversary cannot introduce a new block with a valid tag (with respect to $\Pi^{\prime}$). Furthermore, the extra information included in each block prevents the various attacks (dropping blocks, re-ordering blocks, etc.) sketched earlier. We prove security by showing that those attacks are the only ones possible.

**证明** 直观地说，由于 $\Pi^{\prime}$ 是安全的，敌手无法引入一个带有（相对于 $\Pi^{\prime}$ 的）有效标签的新块。此外，每个块中包含的额外信息能防止之前概述的各种攻击（丢弃块、重排块等）。我们通过证明这些攻击是唯一可能的攻击来证明安全性。

Let $\Pi$ be the MAC given by Construction 4.7, and let $\mathcal{A}$ be a probabilistic polynomial-time adversary. We show that $\Pr[\mathsf{Mac-forge}_{\mathcal{A},\Pi}(n)=1]$ is negligible. We first introduce some notation that will be used in the proof. Let $\mathsf{repeat}$ denote the event that the same random identifier is used in two of the tags returned by the MAC oracle in experiment $\mathsf{Mac-forge}_{\mathcal{A},\Pi}(n)$. Denoting the final output of $\mathcal{A}$ by $(m,t=\langle r,t_1,\ldots\rangle)$, where $m$ has length $\ell$ and is parsed as $m=m_1,\ldots$, we let $\mathsf{NewBlock}$ be the event that at least one of the blocks $r\|\ell\|i\|m_i$ was never previously authenticated by $\mathsf{Mac}^{\prime}$ in the course of answering $\mathcal{A}$'s Mac queries. (Note that, by construction of $\Pi$, it is easy to tell exactly which blocks are authenticated by $\mathsf{Mac}_k^{\prime}$ when computing $\mathsf{Mac}_k(m)$.) Informally, $\mathsf{NewBlock}$ is the event that $\mathcal{A}$ tries to forge a valid tag on a block that was never authenticated by the underlying fixed-length MAC $\Pi^{\prime}$.

设 $\Pi$ 为构造 4.7 所给出的 MAC，设 $\mathcal{A}$ 为概率多项式时间敌手。我们证明 $\Pr[\mathsf{Mac-forge}_{\mathcal{A},\Pi}(n)=1]$ 是可忽略的。我们首先引入一些将在证明中使用的记号。令 $\mathsf{repeat}$ 表示在实验 $\mathsf{Mac-forge}_{\mathcal{A},\Pi}(n)$ 中，MAC 预言机返回的两个标签使用了相同的随机标识符这一事件。记 $\mathcal{A}$ 的最终输出为 $(m,t=\langle r,t_1,\ldots\rangle)$，其中 $m$ 的长度为 $\ell$ 并解析为 $m=m_1,\ldots$，我们令 $\mathsf{NewBlock}$ 表示在回答 $\mathcal{A}$ 的 Mac 查询过程中，至少有一个块 $r\|\ell\|i\|m_i$ 从未被 $\mathsf{Mac}^{\prime}$ 认证过的事件。（注意，根据 $\Pi$ 的构造，在计算 $\mathsf{Mac}_k(m)$ 时很容易确切知道哪些块被 $\mathsf{Mac}_k^{\prime}$ 认证了。）非正式地说，$\mathsf{NewBlock}$ 是 $\mathcal{A}$ 试图在一个从未被底层固定长度 MAC $\Pi^{\prime}$ 认证过的块上伪造有效标签的事件。

We have:

$$
\begin{aligned}
\Pr[\mathsf{Mac-forge}_{\mathcal{A},\Pi}(n)=1]&=\Pr[\mathsf{Mac-forge}_{\mathcal{A},\Pi}(n)=1\land \mathsf{repeat}]\\
&\quad+\Pr[\mathsf{Mac-forge}_{\mathcal{A},\Pi}(n)=1\land\overline{\mathsf{repeat}}\land \mathsf{NewBlock}]\\
&\quad+\Pr[\mathsf{Mac-forge}_{\mathcal{A},\Pi}(n)=1\land\overline{\mathsf{repeat}}\land\overline{\mathsf{NewBlock}}]\\
&\leq\Pr[\mathsf{repeat}]\\
&\quad+\Pr[\mathsf{Mac-forge}_{\mathcal{A},\Pi}(n)=1\land \mathsf{NewBlock}]\\
&\quad+\Pr[\mathsf{Mac-forge}_{\mathcal{A},\Pi}(n)=1\land\overline{\mathsf{repeat}}\land\overline{\mathsf{NewBlock}}].
\end{aligned} \tag{4.3}
$$

我们有：

$$
\begin{aligned}
\Pr[\mathsf{Mac-forge}_{\mathcal{A},\Pi}(n)=1]&=\Pr[\mathsf{Mac-forge}_{\mathcal{A},\Pi}(n)=1\land \mathsf{repeat}]\\
&\quad+\Pr[\mathsf{Mac-forge}_{\mathcal{A},\Pi}(n)=1\land\overline{\mathsf{repeat}}\land \mathsf{NewBlock}]\\
&\quad+\Pr[\mathsf{Mac-forge}_{\mathcal{A},\Pi}(n)=1\land\overline{\mathsf{repeat}}\land\overline{\mathsf{NewBlock}}]\\
&\leq\Pr[\mathsf{repeat}]\\
&\quad+\Pr[\mathsf{Mac-forge}_{\mathcal{A},\Pi}(n)=1\land \mathsf{NewBlock}]\\
&\quad+\Pr[\mathsf{Mac-forge}_{\mathcal{A},\Pi}(n)=1\land\overline{\mathsf{repeat}}\land\overline{\mathsf{NewBlock}}].
\end{aligned} \tag{4.3}
$$

We show that the first two terms of Equation (4.3) are negligible, and the final term is 0. This implies $\Pr[\mathsf{Mac-forge}_{\mathcal{A},\Pi}(n) = 1]$ is negligible, as desired.

我们证明式 (4.3) 的前两项是可忽略的，最后一项为 0。这意味着 $\Pr[\mathsf{Mac-forge}_{\mathcal{A},\Pi}(n) = 1]$ 是可忽略的，如所需。

To see that $\Pr[\mathsf{repeat}]$ is negligible, let $q = q(n)$ be the number of MAC oracle queries made by A. To answer the ith oracle query of A, the oracle chooses $r_i$ uniformly from a set of size ${2}^{n/4}$. The probability of event $\mathsf{repeat}$ is exactly the probability that $r_i = r_j$ for some $i \neq j$. Applying Lemma A.15, we have $\Pr[\mathsf{repeat}] \leq q^2/2^{n/4}$. Since q is polynomial (because A is a PPT adversary), this value is negligible.

为证 $\Pr[\mathsf{repeat}]$ 可忽略，设 $q = q(n)$ 为 A 进行的 MAC 预言机查询次数。为了回答 A 的第 i 次预言机查询，预言机从大小为 ${2}^{n/4}$ 的集合中均匀选择 $r_i$。事件 $\mathsf{repeat}$ 的概率恰好是存在某个 $i \neq j$ 使得 $r_i = r_j$ 的概率。应用引理 A.15，我们有 $\Pr[\mathsf{repeat}] \leq q^2/2^{n/4}$。由于 q 是多项式的（因为 A 是一个 PPT 敌手），该值是可忽略的。

We next consider the final term in Equation (4.3). We argue that if $\mathsf{Mac-forge}_{\mathcal{A},\Pi}(n) = 1$, but $\mathsf{repeat}$ did not occur, then it must be the case that $\mathsf{NewBlock}$ occurred. In other words,

$$
\Pr[\mathsf{Mac-forge}_{\mathcal{A},\Pi}(n)=1\land\overline{\mathsf{repeat}}\land\overline{\mathsf{NewBlock}}]=0.
$$

This is, in some sense, the heart of the proof.

接下来我们考虑式 (4.3) 中的最后一项。我们论证，如果 $\mathsf{Mac-forge}_{\mathcal{A},\Pi}(n) = 1$ 但 $\mathsf{repeat}$ 未发生，则 $\mathsf{NewBlock}$ 必然发生。换句话说，

$$
\Pr[\mathsf{Mac-forge}_{\mathcal{A},\Pi}(n)=1\land\overline{\mathsf{repeat}}\land\overline{\mathsf{NewBlock}}]=0.
$$

在某种意义上，这是证明的核心。

Again let $q = q(n)$ denote the number of MAC oracle queries made by $\mathcal{A}$, and let $r_i$ denote the random identifier used to answer the $i$th oracle query of $\mathcal{A}$. If $\mathsf{repeat}$ does not occur then the values $r_1, \ldots, r_q$ are distinct. Recall that $(m, t = \langle r, t_1, \ldots \rangle)$ is the output of $\mathcal{A}$. If $r \notin \{r_1, \ldots, r_q\}$, then $\mathsf{NewBlock}$ clearly occurs. If not, then $r = r_j$ for some unique $j$ (because $\mathsf{repeat}$ did not occur), and the blocks $r\|\ell\|1\|m_1, \ldots$ could then not possibly have been authenticated during the course of answering any $\mathsf{Mac}$ queries other than the $j$th such query. Let $m^{(j)}$ be the message that was used by $\mathcal{A}$ for its $j$th oracle query, and let $\ell_j$ be its length. There are two cases to consider:

再次设 $q = q(n)$ 表示 $\mathcal{A}$ 进行的 MAC 预言机查询次数，并设 $r_i$ 为用于回答 $\mathcal{A}$ 的第 i 次预言机查询的随机标识符。如果 $\mathsf{repeat}$ 未发生，则值 $r_1, \ldots, r_q$ 互不相同。回顾 $(m, t = \langle r, t_1, \ldots \rangle)$ 是 $\mathcal{A}$ 的输出。如果 $r \notin \{r_1, \ldots, r_q\}$，则 $\mathsf{NewBlock}$ 显然发生。如果不是，则由于 $\mathsf{repeat}$ 未发生，对于某个唯一的 $j$ 有 $r = r_j$，并且除了第 j 次查询外，在回答任何其他 $\mathsf{Mac}$ 查询的过程中，不可能认证过块 $r\|\ell\|1\|m_1, \ldots$。设 $m^{(j)}$ 是 $\mathcal{A}$ 在第 j 次预言机查询中使用的消息，并设 $\ell_j$ 为其长度。需要考虑两种情况：

Case 1: $\ell \neq \ell_j$. The blocks authenticated when answering the $j$th Mac query all have $\ell_j \neq \ell$ in the second position. So $r\|\ell\|1\|m_1$, in particular, was never authenticated in the course of answering the $j$th Mac query, and $\mathsf{NewBlock}$ occurs.

Case 2: $\ell = \ell_j$. If $\mathsf{Mac-forge}_{\mathcal{A},\Pi}(n) = 1$, then we must have $m \neq m^{(j)}$. Let $m^{(j)} = m_1^{(j)}, \ldots$ Since $m$ and $m^{(j)}$ have equal length, there must be at least one index $i$ for which $m_i \neq m_i^{(j)}$. The block $r\|\ell\|i\|m_i$ was then never authenticated in the course of answering the $j$th Mac query. (Because $i$ is included in the third position of the block, the block $r\|\ell\|i\|m_i$ could only possibly have been authenticated if $r\|\ell\|i\|m_i = r_j\|\ell_j\|i\|m_i^{(j)}$, but this is not true since $m_i \neq m_i^{(j)}$.)

情况 1：$\ell \neq \ell_j$。在回答第 j 次 Mac 查询时认证的所有块，第二位都为 $\ell_j$（$\neq \ell$）。因此，特别地，$r\|\ell\|1\|m_1$ 从未在回答第 j 次 Mac 查询的过程中被认证过，且 $\mathsf{NewBlock}$ 发生。

情况 2：$\ell = \ell_j$。如果 $\mathsf{Mac-forge}_{\mathcal{A},\Pi}(n) = 1$，则必须有 $m \neq m^{(j)}$。设 $m^{(j)} = m_1^{(j)}, \ldots$。由于 $m$ 和 $m^{(j)}$ 长度相等，必须存在至少一个索引 $i$ 使得 $m_i \neq m_i^{(j)}$。那么块 $r\|\ell\|i\|m_i$ 在回答第 j 次 Mac 查询的过程中从未被认证过。（因为 $i$ 包含在块的第三个位置，只有当 $r\|\ell\|i\|m_i = r_j\|\ell_j\|i\|m_i^{(j)}$ 时，块 $r\|\ell\|i\|m_i$ 才有可能被认证过，但由于 $m_i \neq m_i^{(j)}$，这不成立。）

To complete the proof of the theorem, we bound the second term on the right-hand side of Equation (4.3). Here we rely on the security of $\Pi^{\prime}$. We construct a PPT adversary $\mathcal{A}^{\prime}$ who attacks the fixed-length MAC $\Pi^{\prime}$ and succeeds in outputting a valid tag on a previously unauthenticated message with probability

$$
\Pr[\mathsf{Mac-forge}_{\mathcal{A}^{\prime},\Pi^{\prime}}(n)=1]\geq\Pr[\mathsf{Mac-forge}_{\mathcal{A},\Pi}(n)=1\land\mathsf{NewBlock}]. \tag{4.4}
$$

为了完成定理的证明，我们对式 (4.3) 右边的第二项进行界定。这里我们依赖 $\Pi^{\prime}$ 的安全性。我们构造一个 PPT 敌手 $\mathcal{A}^{\prime}$，它攻击固定长度 MAC $\Pi^{\prime}$，并以以下概率成功输出一个先前未认证消息上的有效标签：

$$
\Pr[\mathsf{Mac-forge}_{\mathcal{A}^{\prime},\Pi^{\prime}}(n)=1]\geq\Pr[\mathsf{Mac-forge}_{\mathcal{A},\Pi}(n)=1\land\mathsf{NewBlock}]. \tag{4.4}
$$

Security of $\Pi^{\prime}$ means that the left-hand side is negligible, implying that $\Pr[\mathsf{Mac-forge}_{\mathcal{A},\Pi}(n)=1\land\mathsf{NewBlock}]$ is negligible as well.

$\Pi^{\prime}$ 的安全性意味着左边是可忽略的，从而蕴涵 $\Pr[\mathsf{Mac-forge}_{\mathcal{A},\Pi}(n)=1\land\mathsf{NewBlock}]$ 也是可忽略的。

The construction of $\mathcal{A}^{\prime}$ is the obvious one and so we describe it briefly. $\mathcal{A}^{\prime}$ runs $\mathcal{A}$ as a subroutine, and answers the request by $\mathcal{A}$ for a tag on $m$ by choosing $r \leftarrow \{0,1\}^{n/4}$ itself, parsing $m$ appropriately, and making the necessary queries to its own MAC oracle $\mathsf{Mac}_k^{\prime}(\cdot)$. When $\mathcal{A}$ outputs $(m,t = \langle r,t_1,\ldots\rangle)$, then $\mathcal{A}^{\prime}$ checks whether $\mathsf{NewBlock}$ occurs. (This is easy to do since $\mathcal{A}^{\prime}$ can keep track of all the queries it makes to its own oracle.) If so, then $\mathcal{A}^{\prime}$ finds the first block $r\|\ell\|i\|m_i$ that was never previously authenticated by $\mathsf{Mac}^{\prime}$ and outputs $(r\|\ell\|i\|m_i,t_i)$. (If not, $\mathcal{A}^{\prime}$ outputs nothing.)

$\mathcal{A}^{\prime}$ 的构造是显而易见的，因此我们简要描述。$\mathcal{A}^{\prime}$ 将 $\mathcal{A}$ 作为子程序运行，并通过自己选择 $r \leftarrow \{0,1\}^{n/4}$、适当解析 $m$ 并向其自身的 MAC 预言机 $\mathsf{Mac}_k^{\prime}(\cdot)$ 进行必要的查询来回答 $\mathcal{A}$ 对消息 $m$ 的标签请求。当 $\mathcal{A}$ 输出 $(m,t = \langle r,t_1,\ldots\rangle)$ 时，$\mathcal{A}^{\prime}$ 检查 $\mathsf{NewBlock}$ 是否发生。（这很容易做到，因为 $\mathcal{A}^{\prime}$ 可以跟踪其向自己预言机发出的所有查询。）如果是，则 $\mathcal{A}^{\prime}$ 找到第一个从未被 $\mathsf{Mac}^{\prime}$ 认证过的块 $r\|\ell\|i\|m_i$ 并输出 $(r\|\ell\|i\|m_i,t_i)$。（如果不是，$\mathcal{A}^{\prime}$ 不输出任何内容。）

The view of $\mathcal{A}$ when run as a subroutine by $\mathcal{A}^{\prime}$ is distributed identically to the view of $\mathcal{A}$ in experiment $\mathsf{Mac-forge}_{\mathcal{A},\Pi}(n)$, and so the probabilities of events $\mathsf{Mac-forge}_{\mathcal{A},\Pi}(n) = 1$ and $\mathsf{NewBlock}$ do not change. If $\mathsf{NewBlock}$ occurs then $\mathcal{A}^{\prime}$ outputs a block $r\|\ell\|i\|m_i$ that was never previously authenticated by its own MAC oracle; if $\mathsf{Mac-forge}_{\mathcal{A},\Pi}(n) = 1$ then the tag on every block is valid (with respect to $\Pi^{\prime}$), and so in particular this is true for the block output by $\mathcal{A}^{\prime}$. This means that whenever $\mathsf{Mac-forge}_{\mathcal{A},\Pi}(n) = 1$ and $\mathsf{NewBlock}$ occur we have $\mathsf{Mac-forge}_{\mathcal{A},\Pi^{\prime}}(n) = 1$, proving Equation (4.4) and completing the proof of the theorem.

当 $\mathcal{A}$ 作为 $\mathcal{A}^{\prime}$ 的子程序运行时，其视图与 $\mathcal{A}$ 在实验 $\mathsf{Mac-forge}_{\mathcal{A},\Pi}(n)$ 中的视图分布相同，因此事件 $\mathsf{Mac-forge}_{\mathcal{A},\Pi}(n) = 1$ 和 $\mathsf{NewBlock}$ 的概率不变。如果 $\mathsf{NewBlock}$ 发生，则 $\mathcal{A}^{\prime}$ 输出一个从未被其自身 MAC 预言机认证过的块 $r\|\ell\|i\|m_i$；如果 $\mathsf{Mac-forge}_{\mathcal{A},\Pi}(n) = 1$，则每个块上的标签都是有效的（相对于 $\Pi^{\prime}$），因此特别地，$\mathcal{A}^{\prime}$ 输出的块也是有效的。这意味着每当 $\mathsf{Mac-forge}_{\mathcal{A},\Pi}(n) = 1$ 且 $\mathsf{NewBlock}$ 发生时，我们有 $\mathsf{Mac-forge}_{\mathcal{A},\Pi^{\prime}}(n) = 1$，证明了式 (4.4) 并完成了定理的证明。
