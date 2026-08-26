# Chapter 13: Digital Signature Schemes　第 13 章　数字签名方案

## 13.1 Digital Signatures – An Overview　数字签名——概述

In the previous chapter we explored how public-key encryption can be used to achieve secrecy in the public-key setting. Integrity (or authenticity) in the public-key setting is provided using digital signature schemes. These can be viewed as the public-key analogue of message authentication codes although, as we will see, there are several important differences between these primitives.

在上一章中，我们探讨了如何利用公钥加密在公钥场景下实现保密性。公钥场景下的完整性（或称真实性）则由数字签名方案来提供。数字签名可以看作消息认证码在公钥场景下的对应物，不过正如我们将看到的，这两种原语之间存在若干重要差异。

Signature schemes allow a signer $S$ who has established a public key $pk$ to "sign" a message using the associated private key $sk$ in such a way that anyone who knows $pk$ (and knows that this public key was established by $S$) can verify that the message originated from $S$ and was not modified in transit. (Note that, in contrast to public-key encryption, in the context of digital signatures the owner of the public key acts as the sender.) As a prototypical application, consider a software company that wants to disseminate software updates in an authenticated manner; that is, when the company releases an update it should be possible for any of its clients to verify that the update is authentic, and a malicious third party should never be able to fool a client into accepting an update that was not actually released by the company. To do this, the company can generate a public key $pk$ along with a private key $sk$, and then distribute $pk$ in some reliable manner to its clients while keeping $sk$ secret. (As in the case of public-key encryption, we assume that this initial distribution of the public key is carried out correctly so that all clients have a correct copy of $pk$. In the current example, $pk$ could be bundled with the original software purchased by a client.) When releasing a software update $m$, the company computes a digital signature $\sigma$ on $m$ using its private key $sk$, and sends $(m, \sigma)$ to every client. Each client can verify the authenticity of $m$ by checking that $\sigma$ is a correct signature on $m$ with respect to the public key $pk$.

签名方案使得已建立公钥 $pk$ 的签名者 $S$ 能够用相应的私钥 $sk$ 对消息进行“签名”，并使得任何知道 $pk$（且知道该公钥由 $S$ 建立）的人都能验证消息确实来自 $S$、且在传输过程中未被篡改。（注意，与公钥加密不同，在数字签名的语境中，公钥的拥有者充当发送方。）一个典型的应用是：某软件公司希望以可认证的方式分发软件更新；也就是说，当公司发布更新时，其任何客户都应能验证该更新是真实可信的，而恶意的第三方绝不应能骗过客户、使其接受一个并非由该公司实际发布的更新。为此，公司可以生成一对公钥 $pk$ 与私钥 $sk$，然后以某种可靠的方式把 $pk$ 分发给客户，同时对 $sk$ 保密。（与公钥加密的情形一样，我们假设公钥的初始分发被正确完成，从而所有客户都持有 $pk$ 的正确副本。在当前这个例子中，$pk$ 可以随客户购买的原始软件一起捆绑分发。）发布软件更新 $m$ 时，公司用私钥 $sk$ 计算 $m$ 的数字签名 $\sigma$，并把 $(m, \sigma)$ 发送给每个客户。每个客户都可以通过检验 $\sigma$ 是否是 $m$ 关于公钥 $pk$ 的正确签名，来验证 $m$ 的真实性。

A malicious party might try to issue a fraudulent update by sending $(m^{\prime}, \sigma^{\prime})$ to a client, where $m^{\prime}$ represents an update that was never released by the company. This $m^{\prime}$ might be a modified version of some previous update, or it might be completely new and unrelated to any prior updates. If the signature scheme is “secure” (in a sense we will define more carefully soon), however, then when the client attempts to verify $\sigma^{\prime}$ it will find that this is an invalid signature on $m^{\prime}$ with respect to $pk$, and will therefore reject the signature. The client will reject even if $m^{\prime}$ is modified only slightly from a genuine update $m$.

恶意方可能试图向客户发送 $(m^{\prime}, \sigma^{\prime})$ 来发布欺诈性更新，其中 $m^{\prime}$ 表示一个公司从未发布过的更新。这个 $m^{\prime}$ 可能是对以往某个更新的修改版本，也可能是与此前任何更新都毫无关联的全新内容。然而，如果签名方案是“安全的”（其确切含义我们很快将仔细定义），那么当客户尝试验证 $\sigma^{\prime}$ 时，会发现它不是 $m^{\prime}$ 关于 $pk$ 的有效签名，从而拒绝该签名。即使 $m^{\prime}$ 只是在某个真实更新 $m$ 的基础上做了轻微改动，客户也会拒绝。

The above is not just a theoretical application of digital signatures, but one that is in widespread use today for distributing software updates.

以上并非只是数字签名的理论应用——如今分发软件更新时广泛采用的做法正是如此。

### Comparison to Message Authentication Codes　与消息认证码的比较

Both message authentication codes and digital signature schemes are used to ensure the integrity of transmitted messages. Although the discussion in Chapter 11 comparing the public-key and private-key settings focused mainly on encryption, that discussion applies also to message integrity. Using digital signatures rather than message authentication codes simplifies key distribution and management, especially when a sender needs to communicate with multiple receivers as in the software-update example above. By using a digital signature scheme the sender avoids having to establish a distinct secret key with each potential receiver, and avoids having to compute a separate MAC tag with respect to each such key. Instead, the sender need only compute a single signature that can be verified by all recipients.

消息认证码和数字签名方案都用于保证所传输消息的完整性。第 11 章中比较公钥场景与私钥场景的讨论虽然主要围绕加密展开，但同样适用于消息完整性。使用数字签名而非消息认证码，可以简化密钥的分发与管理，当发送方需要与多个接收方通信时尤其如此——正如上面的软件更新例子。采用数字签名方案，发送方就无需与每个潜在接收方分别建立不同的密钥，也无需针对每个这样的密钥单独计算一个 MAC 标签；相反，发送方只需计算一个签名，所有接收方都能验证它。

A qualitative advantage that digital signatures have as compared to message authentication codes is that signatures are publicly verifiable. This means that if a receiver verifies that a signature on a given message is legitimate, then all other parties who receive this signed message will also verify it as legitimate. This feature is not achieved by message authentication codes if the signer shares a separate key with each receiver: in such a setting a malicious sender might compute a correct MAC tag with respect to the key it shares with receiver A but an incorrect MAC tag with respect to the key it shares with a different user B. In this case, A knows that he received an authentic message from the sender but has no guarantee that B will agree.

与消息认证码相比，数字签名的一个本质性的优点在于签名是公开可验证的。这意味着：如果某个接收方验证了给定消息上的签名是合法的，那么收到该已签名消息的所有其他方也都会验证其为合法。若签名者与每个接收方分别共享不同的密钥，消息认证码就无法实现这一特性：在这种情形下，恶意的发送方可能对它与接收方 A 共享的密钥计算出正确的 MAC 标签，却对它与另一用户 B 共享的密钥计算出错误的 MAC 标签。这样一来，A 知道自己收到的是来自发送方的真实消息，但无法保证 B 也会认可。

Public verifiability implies that signatures are transferable: a signature $\sigma$ on a message $m$ by a signer S can be shown to a third party, who can then verify herself that $\sigma$ is a legitimate signature on $m$ with respect to S's public key (here, we assume this third party also knows S's public key). By making a copy of the signature, this third party can then show the signature to another party and convince them that S authenticated m, and so on. Public verifiability and transferability are essential for the application of digital signatures to certificates and public-key infrastructures, as we will discuss in Section 13.6.

公开可验证性意味着签名是可转移的：签名者 S 对消息 $m$ 的签名 $\sigma$ 可以出示给第三方，该第三方可以自行验证 $\sigma$ 确实是 $m$ 关于 S 公钥的合法签名（此处我们假设该第三方也知道 S 的公钥）。通过复制该签名，这个第三方还可以把它出示给另一方，使对方相信 S 认证了 m，依此类推。正如我们将在 13.6 节讨论的，公开可验证性与可转移性对于数字签名在证书和公钥基础设施中的应用至关重要。

Digital signature schemes also provide the very important property of non-repudiation. This means that once $S$ signs a message he cannot later deny having done so (assuming the public key of $S$ is widely publicized and distributed). This aspect of digital signatures is crucial for legal applications where a recipient may need to prove to a third party (say, a judge) that a signer did indeed “certify” a particular message (e.g., a contract): assuming $S$’s public key is known to the judge, or is otherwise publicly available, a valid signature on a message serves as convincing evidence that $S$ indeed signed that message. Message authentication codes simply cannot provide non-repudiation. To see this, say users $S$ and $R$ share a key $k_{SR}$, and $S$
sends a message $m$ to $R$ along with a (valid) MAC tag $t$ computed using this key. Since the judge does not know $k_{SR}$ (indeed, this key is kept secret by $S$ and $R$), there is no way for the judge to determine whether $t$ is valid or not. If $R$ were to reveal the key $k_{SR}$ to the judge, there would be no way for the judge to know whether this is the “actual” key that $S$ and $R$ shared, or whether it is some “fake” key manufactured by $R$. Finally, even if we assume the judge can somehow obtain the actual key $k_{SR}$ shared by the parties, there is no way for the judge to distinguish whether $S$ generated $t$ or whether $R$ did—this is because message authentication codes are a symmetric-key primitive; anything $S$ can do, $R$ can do also.

数字签名方案还提供一项非常重要的性质——不可否认性。这意味着一旦 $S$ 对某条消息签了名，他事后就无法否认自己签过（前提是 $S$ 的公钥已被广泛公布和分发）。数字签名的这一特性对法律应用至关重要：在这类应用中，接收方可能需要向第三方（比如法官）证明签名者确实“认证”过某条特定消息（例如一份合同）。假设法官知道 $S$ 的公钥，或该公钥可以公开获得，那么消息上的一个有效签名就是 $S$ 确实签署过该消息的有力证据。消息认证码则根本无法提供不可否认性。为看清这一点，设用户 $S$ 与 $R$ 共享密钥 $k_{SR}$，$S$ 向 $R$ 发送消息 $m$，并附上用这个密钥计算出的（有效）MAC 标签 $t$。由于法官不知道 $k_{SR}$（这个密钥确实由 $S$ 和 $R$ 保密），法官无从判断 $t$ 是否有效。即便 $R$ 把密钥 $k_{SR}$ 透露给法官，法官也无法知道这究竟是 $S$ 与 $R$ 共享的“真实”密钥，还是 $R$ 伪造出来的某个“假”密钥。最后，即使我们假设法官能设法获得双方共享的真实密钥 $k_{SR}$，法官仍然无法区分 $t$ 究竟是 $S$ 生成的还是 $R$ 生成的——这是因为消息认证码是一种对称密钥原语：$S$ 能做的任何事，$R$ 也能做。

As in the case of private-key vs. public-key encryption, message authentication codes have the advantage of being shorter and roughly 2–3 orders of magnitude more efficient to generate/verify than digital signatures. Thus, in situations where public verifiability, transferability, and/or non-repudiation are not needed, and the sender communicates primarily with a single recipient (with whom it is able to share a secret key), message authentication codes should be used.

与私钥加密和公钥加密的对比类似，消息认证码的优点是更短，且生成/验证的效率比数字签名高约 2–3 个数量级。因此，在不需要公开可验证性、可转移性和/或不可否认性，且发送方主要与单一接收方通信（并能与之共享密钥）的场合，应当使用消息认证码。

### Relation to Public-Key Encryption　与公钥加密的关系

Digital signatures are often mistakenly viewed as the “inverse” of public-key encryption, with the roles of the sender and receiver interchanged. Historically, $^{1}$ in fact, it has been suggested that digital signatures can be obtained by “reversing” public-key encryption, i.e., signing a message $m$ by decrypting it (using the private key) to obtain $\sigma$, and verifying a signature $\sigma$ by encrypting it (using the corresponding public key) and checking whether the result is m. The suggestion to construct signature schemes in this way is completely unfounded: in most cases, it is simply inapplicable, and even in cases where it can be applied it results in signature schemes that are not secure.

数字签名常被误认为是公钥加密的“逆操作”，只是发送方与接收方的角色互换。事实上，历史上$^{1}$曾有人提出，可以通过“反转”公钥加密来获得数字签名，即：对消息 $m$ 签名就是用（私钥）解密 $m$ 得到 $\sigma$，而验证签名 $\sigma$ 就是用（相应的公钥）加密它，并检查结果是否等于 m。这种构造签名方案的思路是完全没有根据的：在大多数情况下它根本行不通；即便在可以套用的情形下，得到的签名方案也不安全。

> $^{1}$ This view no doubt arose because, as we will see in Section 13.4.1, plain RSA signatures are the reverse of plain RSA encryption. However, neither plain RSA signatures nor plain RSA encryption meet even minimal notions of security.
> $^{1}$ 这种看法无疑源于：正如我们将在 13.4.1 节看到的，朴素 RSA 签名恰好是朴素 RSA 加密的逆。然而，朴素 RSA 签名与朴素 RSA 加密连最低限度的安全性概念都不满足。

## 13.2 Definitions　定义

Digital signatures are the public-key counterpart of message authentication codes, and their syntax and security guarantees are analogous. The algorithm that the sender applies to a message is here denoted Sign (rather than Mac), and the output of this algorithm is now called a signature (rather than a tag).

数字签名是消息认证码在公钥场景下的对应物，其语法与安全保证也是类似的。发送方作用于消息的算法这里记作 Sign（而不是 Mac），该算法的输出现在称为签名（而不是标签）。

The algorithm that the receiver applies to a message and a signature in order to check validity is still denoted Vrfy.

接收方为检验有效性而作用于消息与签名的算法仍记作 Vrfy。

DEFINITION 13.1 A (digital) signature scheme consists of three probabilistic polynomial-time algorithms (Gen, Sign, Vrfy) such that:

定义 13.1　一个（数字）签名方案由三个概率多项式时间算法 (Gen, Sign, Vrfy) 组成，满足：

1. The key-generation algorithm Gen takes as input a security parameter ${1}^{n}$ and outputs a pair of keys (pk, sk). These are called the public key and the private key, respectively. We assume that $pk$ and $sk$ each has length at least $n$, and that $n$ can be determined from $pk$ or sk.

   密钥生成算法 Gen 以安全参数 ${1}^{n}$ 为输入，输出一对密钥 (pk, sk)。它们分别称为公钥与私钥。我们假设 $pk$ 和 $sk$ 的长度都至少为 $n$，且 $n$ 可以由 $pk$ 或 sk 确定。

2. The signing algorithm Sign takes as input a private key $sk$ and a message $m$ from some message space (that may depend on pk). It outputs a signature $\sigma$, and we write this as $\sigma \leftarrow \mathsf{Sign}_{sk}(m)$.

   签名算法 Sign 以私钥 $sk$ 和来自某个消息空间（该空间可能依赖于 pk）的消息 $m$ 为输入。它输出一个签名 $\sigma$，记作 $\sigma \leftarrow \mathsf{Sign}_{sk}(m)$。

3. The deterministic verification algorithm Vrfy takes as input a public key pk, a message m, and a signature $\sigma$. It outputs a bit b, with $b=1$ meaning valid and $b=0$ meaning invalid. We write this as $b:=\mathsf{Vrfy}_{pk}(m,\sigma)$.

   确定性的验证算法 Vrfy 以公钥 pk、消息 m 和签名 $\sigma$ 为输入。它输出一个比特 b，$b=1$ 表示有效，$b=0$ 表示无效。记作 $b:=\mathsf{Vrfy}_{pk}(m,\sigma)$。

It is required that except with negligible probability over (pk, sk) output by $\mathrm{Gen}(1^n)$, it holds that $\mathrm{Vrfy}_{pk}(m, \mathrm{Sign}_{sk}(m)) = 1$ for every (legal) message $m$.

要求：除可忽略的概率外，对于 $\mathrm{Gen}(1^n)$ 输出的 (pk, sk)，等式 $\mathrm{Vrfy}_{pk}(m, \mathrm{Sign}_{sk}(m)) = 1$ 对每条（合法）消息 $m$ 都成立。

If there is a function $\ell$ such that for every $(pk,sk)$ output by $\mathsf{Gen}(1^n)$ the message space is $\{0,1\}^{\ell(n)}$, then we say that (Gen, Sign, Vrfy) is a signature scheme for messages of length $\ell(n)$.

如果存在函数 $\ell$，使得对于 $\mathsf{Gen}(1^n)$ 输出的每个 $(pk,sk)$，消息空间都是 $\{0,1\}^{\ell(n)}$，那么我们称 (Gen, Sign, Vrfy) 是用于长度为 $\ell(n)$ 的消息的签名方案。

We call $\sigma$ a valid signature on a message $m$ (with respect to some public key $pk$ understood from the context) if $\mathsf{Vrfy}_{pk}(m, \sigma) = 1$.

若 $\mathsf{Vrfy}_{pk}(m, \sigma) = 1$，我们称 $\sigma$ 是消息 $m$ 的一个有效签名（相对于上下文可知的某个公钥 $pk$）。

A signature scheme is used in the following way. One party $S$, who acts as the sender, runs $\mathsf{Gen}(1^n)$ to obtain keys $(pk, sk)$. The public key $pk$ is then publicized as belonging to $S$; e.g., $S$ can put the public key on its webpage or place it in some public directory. As in the case of public-key encryption, we assume that any other party is able to obtain a legitimate copy of $S$'s public key (see discussion below). When $S$ wants to authenticate a message $m$, it computes the signature $\sigma \leftarrow \mathsf{Sign}_{sk}(m)$ and sends $(m, \sigma)$. Upon receipt of $(m, \sigma)$, a receiver who knows $pk$ can verify the authenticity of $m$ by checking whether $\mathsf{Vrfy}_{\text{pk}}(m, \sigma) \overset{?}{=} 1$. This establishes both that $S$ sent $m$, and also that $m$ was not modified in transit. As in the case of message authentication codes, however, it does not say anything about when $m$ was sent, and replay attacks are still possible (see Section 4.2).

签名方案的使用方式如下：充当发送方的一方 $S$ 运行 $\mathsf{Gen}(1^n)$ 得到密钥 $(pk, sk)$。随后公钥 $pk$ 被公布为属于 $S$；例如，$S$ 可以把公钥放在自己的网页上，或放入某个公共目录中。与公钥加密的情形一样，我们假设任何其他方都能获得 $S$ 公钥的合法副本（见下文讨论）。当 $S$ 想要认证一条消息 $m$ 时，它计算签名 $\sigma \leftarrow \mathsf{Sign}_{sk}(m)$ 并发送 $(m, \sigma)$。收到 $(m, \sigma)$ 后，知道 $pk$ 的接收方可以通过检查 $\mathsf{Vrfy}_{\text{pk}}(m, \sigma) \overset{?}{=} 1$ 是否成立来验证 $m$ 的真实性。这既确认了 $m$ 是 $S$ 发出的，也确认了 $m$ 在传输过程中未被篡改。不过，与消息认证码的情形一样，它并不能说明 $m$ 是何时发送的，重放攻击仍然可能发生（参见 4.2 节）。

The assumption that parties are able to obtain a legitimate copy of S's public key implies that S is able to transmit at least one message (namely, $pk$ itself) in a reliable and authenticated manner. If S is able to transmit messages reliably, however, then why does it need a signature scheme at all? The answer is that reliable distribution of $pk$ may be difficult and expensive, but using a signature scheme means that such distribution need only be carried out once, after which an unlimited number of messages can subsequently be sent reliably. Furthermore, as we will discuss in Section 13.6, signature schemes themselves are used to ensure the reliable distribution of other public keys. They thus serve as a central tool for setting up a “public-key infrastructure” to address the key-distribution problem.

各方都能获得 S 公钥的合法副本这一假设，意味着 S 能够以可靠且经认证的方式传输至少一条消息（即 $pk$ 本身）。那么，既然 S 能够可靠地传输消息，为什么还需要签名方案呢？答案是：可靠地分发 $pk$ 可能既困难又昂贵，但使用签名方案意味着这种分发只需进行一次，此后便可以可靠地发送任意数量的消息。此外，正如我们将在 13.6 节讨论的，签名方案本身也被用来保证其他公钥的可靠分发。因此，签名方案是建立“公钥基础设施”以解决密钥分发问题的核心工具。

Security of signature schemes. For a fixed public key pk generated by a signer $S$, a forgery is a message $m$ along with a valid signature $\sigma$, where $m$ was not previously signed by $S$. Security of a signature scheme means that an adversary should be unable to output a forgery even if it obtains signatures on many other messages of its choice. This is the direct analogue of the definition of security for message authentication codes, and we refer the reader to Section 4.2 for motivation and further discussion.

**签名方案的安全性。**

对于签名者 $S$ 生成的某个固定公钥 pk，一个伪造是指一条消息 $m$ 连同其上的一个有效签名 $\sigma$，其中 $m$ 此前未曾被 $S$ 签名过。签名方案的安全性意味着：敌手即使能获得它自己选择的许多其他消息上的签名，也应无法输出一个伪造。这与消息认证码的安全性定义直接对应，其动机与进一步讨论请读者参阅 4.2 节。

The formal definition of security is essentially the same as Definition 4.2, with the main difference being that here the adversary is given a public key. Let $\Pi = (\mathrm{Gen}, \mathrm{Sign}, \mathrm{Vrfy})$ be a signature scheme, and consider the following experiment for an adversary $\mathcal{A}$ and parameter $n$:

安全性的形式化定义与定义 4.2 基本相同，主要区别在于这里敌手被给予一个公钥。设 $\Pi = (\mathrm{Gen}, \mathrm{Sign}, \mathrm{Vrfy})$ 是一个签名方案，考虑下面针对敌手 $\mathcal{A}$ 与参数 $n$ 的实验：

The signature experiment $\mathsf{Sig-forge}_{\mathcal{A},\Pi}(n)$:

签名实验 $\mathsf{Sig-forge}_{\mathcal{A},\Pi}(n)$：

1. Gen ${1}^{n}$ is run to obtain keys $(pk, sk)$.

   运行 Gen ${1}^{n}$ 得到密钥 $(pk, sk)$。

2. Adversary $\mathcal{A}$ is given $pk$ and access to an oracle $\mathsf{Sign}_{sk}(\cdot)$. The adversary then outputs $(m,\sigma)$. Let $\mathcal{Q}$ denote the set of all queries that $\mathcal{A}$ asked its oracle.

   敌手 $\mathcal{A}$ 被给予 $pk$ 以及对预言机 $\mathsf{Sign}_{sk}(\cdot)$ 的访问权。然后敌手输出 $(m,\sigma)$。记 $\mathcal{Q}$ 为 $\mathcal{A}$ 向其预言机提出的所有查询组成的集合。

3. $\mathcal{A}$ succeeds if and only if (1) $\mathsf{Vrfy}_{pk}(m,\sigma)=1$ and (2) $m\notin\mathcal{Q}$. In this case the output of the experiment is defined to be 1.

   $\mathcal{A}$ 成功当且仅当 (1) $\mathsf{Vrfy}_{pk}(m,\sigma)=1$ 且 (2) $m\notin\mathcal{Q}$。此时实验的输出定义为 1。

DEFINITION 13.2 A signature scheme $\Pi = (\mathrm{Gen}, \mathrm{Sign}, \mathrm{Vrfy})$ is existentially unforgeable under an adaptive chosen-message attack, or just secure, if for all probabilistic polynomial-time adversaries $\mathcal{A}$, there is a negligible function $\mathsf{negl}$ such that:

定义 13.2　若对于所有概率多项式时间敌手 $\mathcal{A}$，都存在可忽略函数 $\mathsf{negl}$ 使得下式成立，则称签名方案 $\Pi = (\mathrm{Gen}, \mathrm{Sign}, \mathrm{Vrfy})$ 在自适应选择消息攻击下是存在性不可伪造的，或简称安全的：

$$\Pr[\mathsf{Sig-forge}_{\mathcal{A},\Pi}(n)=1]\leq\mathsf{negl}(n).$$

Strong security can be defined analogously to Definition 4.3.

强安全性可以用与定义 4.3 类似的方式定义。

## 13.3 The Hash-and-Sign Paradigm　哈希-签名范式

As in the case of public-key vs. private-key encryption, “native” signature schemes are orders of magnitude less efficient than message authentication codes. Fortunately, as with hybrid encryption (see Section 12.3), it is possible to obtain the functionality of digital signatures at the asymptotic cost of a private-key operation, at least for sufficiently long messages. This can be done using the hash-and-sign approach, discussed next.

与公钥加密和私钥加密的对比一样，“原生”签名方案的效率比消息认证码低好几个数量级。幸运的是，正如混合加密（参见 12.3 节）那样，至少对于足够长的消息，渐近意义上只需承担私钥操作的代价，即可获得数字签名的功能。这可以通过接下来讨论的哈希-签名方法来实现。

The intuition behind the hash-and-sign approach is straightforward. Say we have a signature scheme for messages of length $\ell$, and wish to sign a (longer) message $m \in \{0,1\}^*$. Rather than sign $m$ itself, we can instead use a hash function $H$ to hash the message to a fixed-length digest $H(m)$ of length $\ell$, and then sign the resulting digest. This approach is exactly analogous to the hash-and-MAC approach discussed in Section 6.3.1.

哈希-签名方法背后的直觉很直接。假设我们有一个用于长度为 $\ell$ 的消息的签名方案，现在想对一条（更长的）消息 $m \in \{0,1\}^*$ 签名。我们可以不直接对 $m$ 本身签名，而是先用哈希函数 $H$ 把消息散列成长度为 $\ell$ 的定长摘要 $H(m)$，再对所得的摘要签名。这种方法与 6.3.1 节讨论的哈希-认证（hash-and-MAC）方法完全类似。

**CONSTRUCTION 13.3**

Let $\Pi = (\mathrm{Gen}, \mathrm{Sign}, \mathrm{Vrfy})$ be a signature scheme for messages of length $\ell(n)$, and let $\Pi_{H} = (\mathrm{Gen}_{H}, H)$ be a hash function with output length $\ell(n)$. Construct signature scheme $\Pi^{\prime} = (\mathrm{Gen}^{\prime}, \mathrm{Sign}^{\prime}, \mathrm{Vrfy}^{\prime})$ as follows:

**构造 13.3**

设 $\Pi = (\mathrm{Gen}, \mathrm{Sign}, \mathrm{Vrfy})$ 是用于长度为 $\ell(n)$ 的消息的签名方案，$\Pi_{H} = (\mathrm{Gen}_{H}, H)$ 是输出长度为 $\ell(n)$ 的哈希函数。按如下方式构造签名方案 $\Pi^{\prime} = (\mathrm{Gen}^{\prime}, \mathrm{Sign}^{\prime}, \mathrm{Vrfy}^{\prime})$：

- Gen': on input ${1}^n$, run $\mathsf{Gen}(1^n)$ to obtain $(pk, sk)$ and run $\mathsf{Gen}_H(1^n)$ to obtain $s$; the public key is $\langle pk, s \rangle$ and the private key is $\langle sk, s \rangle$.

- Gen'：输入 ${1}^n$ 时，运行 $\mathsf{Gen}(1^n)$ 得到 $(pk, sk)$，并运行 $\mathsf{Gen}_H(1^n)$ 得到 $s$；公钥为 $\langle pk, s \rangle$，私钥为 $\langle sk, s \rangle$。

- Sign': on input a private key $\langle sk, s \rangle$ and a message $m \in \{0,1\}^{*}$, output $\sigma \leftarrow \mathsf{Sign}_{sk}(H^{s}(m))$.

- Sign'：输入私钥 $\langle sk, s \rangle$ 与消息 $m \in \{0,1\}^{*}$ 时，输出 $\sigma \leftarrow \mathsf{Sign}_{sk}(H^{s}(m))$。

- $\operatorname{Vrfy}^{\prime}$: on input a public key $\langle pk, s \rangle$, a message $m \in \{0,1\}^*$, and a signature $\sigma$, output 1 if and only if $\operatorname{Vrfy}_{pk}(H^s(m), \sigma) \stackrel{?}{=} 1$.

- $\operatorname{Vrfy}^{\prime}$：输入公钥 $\langle pk, s \rangle$、消息 $m \in \{0,1\}^*$ 与签名 $\sigma$ 时，输出 1 当且仅当 $\operatorname{Vrfy}_{pk}(H^s(m), \sigma) \stackrel{?}{=} 1$。

The hash-and-sign paradigm.

哈希-签名范式。

THEOREM 13.4 If $\Pi$ is a secure signature scheme for messages of length $\ell$ and $\Pi_{H}$ is collision resistant, then Construction 13.3 is a secure signature scheme (for arbitrary-length messages).

定理 13.4　若 $\Pi$ 是用于长度为 $\ell$ 的消息的安全签名方案，且 $\Pi_{H}$ 抗碰撞，则构造 13.3 是一个安全的签名方案（适用于任意长度的消息）。

The proof of this theorem is almost identical to that of Theorem 6.6.

该定理的证明与定理 6.6 的证明几乎完全相同。

## 13.4 RSA-Based Signatures　基于 RSA 的签名

We begin our consideration of concrete signature schemes with a discussion of schemes based on the RSA assumption.

我们对具体签名方案的考察，从基于 RSA 假设的方案开始。

### 13.4.1 Plain RSA Signatures　朴素 RSA 签名

We first describe a simple, RSA-based signature scheme. Although the scheme is insecure, it serves as a useful starting point.

我们首先描述一个简单的基于 RSA 的签名方案。虽然这个方案并不安全，但它是一个有用的起点。

As usual, let $\mathsf{GenRSA}$ be a PPT algorithm that, on input ${1}^n$, outputs a modulus $N$ that is the product of two $n$-bit primes (except with negligible probability), along with integers $e, d$ satisfying $ed = 1 \bmod \phi(N)$. Key generation in plain RSA involves simply running $\mathsf{GenRSA}$, and outputting $\langle N, e \rangle$ as the public key and $\langle N, d \rangle$ as the private key. To sign a message $m \in \mathbb{Z}_N^*$, the signer computes $\sigma := [m^d \bmod N]$. Verification of a signature $\sigma$ on a message $m$ with respect to the public key $\langle N, e \rangle$ is carried out by checking whether $m \overset{?}{=} \sigma^e \bmod N$. See Construction 13.5.

按惯例，设 $\mathsf{GenRSA}$ 是一个概率多项式时间算法，输入 ${1}^n$ 时输出一个模数 $N$（除可忽略的概率外，$N$ 是两个 $n$ 比特素数的乘积），以及满足 $ed = 1 \bmod \phi(N)$ 的整数 $e, d$。朴素 RSA 的密钥生成就是运行 $\mathsf{GenRSA}$，输出 $\langle N, e \rangle$ 作为公钥、$\langle N, d \rangle$ 作为私钥。要对消息 $m \in \mathbb{Z}_N^*$ 签名，签名者计算 $\sigma := [m^d \bmod N]$。验证签名 $\sigma$ 是否为消息 $m$ 关于公钥 $\langle N, e \rangle$ 的签名，通过检查 $m \overset{?}{=} \sigma^e \bmod N$ 是否成立来完成。见构造 13.5。

**CONSTRUCTION 13.5**

Let GenRSA be as in the text. Define a signature scheme as follows:

**构造 13.5**

设 GenRSA 如正文所述。按如下方式定义一个签名方案：

Gen: on input ${1}^n$ run GenRSA( ${1}^n$) to obtain $(N,e,d)$. The public key is $\langle N,e\rangle$ and the private key is $\langle N,d\rangle$.

Gen：输入 ${1}^n$ 时，运行 GenRSA(${1}^n$) 得到 $(N,e,d)$。公钥为 $\langle N,e\rangle$，私钥为 $\langle N,d\rangle$。

- Sign: on input a private key $sk = \langle N, d \rangle$ and a message $m \in \mathbb{Z}_N^*$, compute the signature

- Sign：输入私钥 $sk = \langle N, d \rangle$ 与消息 $m \in \mathbb{Z}_N^*$ 时，计算签名

$$\sigma:=[m^{d}\bmod N].$$

- Vrfy: on input a public key $pk = \langle N, e \rangle$, a message $m \in \mathbb{Z}_N^*$, and a signature $\sigma \in \mathbb{Z}_N^*$, output 1 if and only if

- Vrfy：输入公钥 $pk = \langle N, e \rangle$、消息 $m \in \mathbb{Z}_N^*$ 与签名 $\sigma \in \mathbb{Z}_N^*$ 时，输出 1 当且仅当

$$m\stackrel{?}{=}[\sigma^{e}\bmod N].$$

**The plain RSA signature scheme.**

**朴素 RSA 签名方案。**

It is easy to see that verification of a legitimately generated signature is always successful since

容易看出，对合法生成的签名进行验证总是成功的，因为

$$\sigma^{e}=(m^{d})^{e}=m^{[{e d}\bmod\phi(N)]}=m^{1}=m\bmod N.$$

One might expect this scheme to be secure since, for an adversary knowing only the public key $\langle N, e \rangle$, computing a valid signature on a message m seems to require solving the RSA problem (since the signature is exactly the eth root of m). Unfortunately, this reasoning is incorrect. For one thing, the RSA assumption only implies hardness of computing a signature (that is, computing an eth root) of a uniform message m; it says nothing about hardness of computing a signature on a nonuniform m or on some message m of the attacker's choice. Moreover, the RSA assumption says nothing about what an attacker might be able to do once it learns signatures on other messages. The following examples demonstrate that both of these observations lead to attacks on the plain RSA signature scheme.

有人可能期望这个方案是安全的，因为对于只知道公钥 $\langle N, e \rangle$ 的敌手来说，计算消息 m 上的有效签名似乎需要求解 RSA 问题（因为签名恰好是 m 的 e 次根）。不幸的是，这种推理是错误的。一方面，RSA 假设只蕴含了对均匀分布的消息 m 计算签名（即计算 e 次根）是困难的；它并没有说明对非均匀分布的 m、或对攻击者自己选择的某个消息 m 计算签名是否困难。另一方面，RSA 假设也没有说明攻击者在获知其他消息上的签名之后能够做些什么。下面的例子表明，这两点观察都导致了对朴素 RSA 签名方案的攻击。

**A no-message attack.**

**无消息攻击。**

The first attack we describe generates a forgery using the public key alone, without obtaining any signatures from the legitimate signer. The attack works as follows: given a public key $pk = \langle N, e \rangle$, choose a uniform $\sigma \in \mathbb{Z}_N^*$ and compute $m := [\sigma^e \bmod N]$. Then output the forgery $(m, \sigma)$. It is immediate that $\sigma$ is a valid signature on $m$, and this is a forgery since no signatures at all were issued by the owner of the public key. We conclude that the plain RSA signature scheme does not satisfy Definition 13.2.

我们描述的第一种攻击只利用公钥就能生成伪造，无需从合法签名者处获得任何签名。攻击过程如下：给定公钥 $pk = \langle N, e \rangle$，均匀选取 $\sigma \in \mathbb{Z}_N^*$，计算 $m := [\sigma^e \bmod N]$，然后输出伪造 $(m, \sigma)$。显然 $\sigma$ 是 $m$ 上的有效签名，而这是一个伪造，因为公钥的拥有者从未签发过任何签名。我们得出结论：朴素 RSA 签名方案不满足定义 13.2。

One might argue that this does not constitute a “realistic” attack since the adversary has “no control” over the message m for which it forges a valid signature. This is irrelevant as far as Definition 13.2 is concerned, and we have already discussed (in Chapter 4) why it is dangerous to assume any semantics for messages that are going to be authenticated using any cryptographic scheme. Moreover, the adversary does have some control over m: for example, by choosing multiple, uniform values of $\sigma$ it can (with high probability) obtain an m with a few bits set in some desired way. By choosing $\sigma$ in some specific manner, it may also be possible to influence the resulting message for which a forgery is output.

有人可能会争辩说，这并不构成“现实的”攻击，因为敌手对它所伪造有效签名的消息 m“没有控制力”。就定义 13.2 而言，这一点无关紧要；而且我们已经（在第 4 章）讨论过，对将要用密码方案认证的消息假设任何语义都是危险的。况且，敌手对 m 确实有一定的控制力：例如，通过选取多个均匀的 $\sigma$ 值，它可以（以高概率）得到一个按某种期望方式设定了若干比特的 m。通过以某种特定方式选取 $\sigma$，它还可能影响最终输出伪造所对应的消息。

Forging a signature on an arbitrary message. A more damaging attack on the plain RSA signature scheme requires the adversary to obtain two signatures from the signer, but allows the adversary to output a forged signature on any message of its choice. Say the adversary wants to forge a signature on the message $m \in \mathbb{Z}_N^*$ with respect to the public key $pk = \langle N, e \rangle$. The adversary chooses arbitrary $m_1, m_2 \in \mathbb{Z}_N^*$ distinct from $m$ such that $m = m_1 \cdot m_2 \mod N$. It then obtains signatures $\sigma_1, \sigma_2$ on $m_1, m_2$, respectively. Finally, it outputs $\sigma := [\sigma_1 \cdot \sigma_2 \mod N]$ as a valid signature on $m$. This works because

**对任意消息伪造签名。**

对朴素 RSA 签名方案更具破坏力的一种攻击，需要敌手从签名者处获得两个签名，但允许敌手对它自选的任意消息输出伪造签名。设敌手想要在公钥 $pk = \langle N, e \rangle$ 下伪造消息 $m \in \mathbb{Z}_N^*$ 上的签名。敌手任意选取两个与 $m$ 不同的 $m_1, m_2 \in \mathbb{Z}_N^*$，使得 $m = m_1 \cdot m_2 \mod N$。然后它分别获得 $m_1, m_2$ 上的签名 $\sigma_1, \sigma_2$。最后输出 $\sigma := [\sigma_1 \cdot \sigma_2 \mod N]$ 作为 $m$ 上的有效签名。这是可行的，因为

$$\sigma^{e}=(\sigma_{1}\cdot\sigma_{2})^{e}=(m_{1}^{d}\cdot m_{2}^{d})^{e}=m_{1}^{e d}\cdot m_{2}^{e d}=m_{1}\cdot m_{2}=m\bmod N,$$

using the fact that $\sigma_{1}, \sigma_{2}$ are valid signatures on $m_{1}, m_{2}$.

这里用到 $\sigma_{1}, \sigma_{2}$ 分别是 $m_{1}, m_{2}$ 上的有效签名这一事实。

Being able to forge a signature on an arbitrary message is devastating. Nevertheless, one might argue that this attack is unrealistic since an adversary will not be able to convince a signer to sign the exact messages $m_1$ and $m_2$. Once again, this is irrelevant as far as Definition 13.2 is concerned. Furthermore, it is dangerous to make assumptions about what messages the signer may or may not be willing to sign. For example, a client may use a signature scheme to authenticate to a server by signing a random challenge sent by the server. Here, a malicious server would be able to obtain a signature on any message(s) of its choice. More generally, it may be possible for the adversary to choose $m_1$ and $m_2$ as “legitimate” messages that the signer will agree to sign. Finally, note that the attack can be generalized: if an adversary obtains valid signatures on $q$ arbitrary messages $M = \{m_1, \ldots, m_q\}$, then the adversary can output a valid signature on any of ${2}^q - q$ other messages obtained by taking products of subsets of $M$ (of size different from 1).

能够对任意消息伪造签名是毁灭性的。尽管如此，仍有人可能争辩说这种攻击不现实，因为敌手无法说服签名者对恰好是 $m_1$ 和 $m_2$ 的消息签名。再说一次，就定义 13.2 而言这无关紧要。而且，对签名者可能愿意或不愿意签署哪些消息作出假设是危险的。例如，客户可能通过对服务器发来的随机挑战值签名来向服务器认证自己，此时恶意的服务器就能获得它自选任意消息上的签名。更一般地说，敌手有可能把 $m_1$ 和 $m_2$ 选成签名者会同意签署的“合法”消息。最后注意，该攻击可以推广：如果敌手获得了 $q$ 个任意消息 $M = \{m_1, \ldots, m_q\}$ 上的有效签名，那么它可以对另外 ${2}^q - q$ 个消息中的任意一个输出有效签名——这些消息由 $M$ 的（大小不为 1 的）子集相乘得到。

### 13.4.2 RSA-FDH and PKCS #1 Standards　RSA-FDH 与 PKCS #1 标准

One can attempt to prevent the attacks from the previous section by applying some transformation to messages before signing them. That is, the signer will now specify as part of its public key a (deterministic) function $H$ with certain cryptographic properties (described below) mapping messages to $\mathbb{Z}_N^*$; the signature on a message $m$ will be $\sigma := [H(m)^d \bmod N]$, and verification of the signature $\sigma$ on the message $m$ will be done by checking whether $\sigma^e \stackrel{?}{=} H(m) \bmod N$. See Construction 13.6.

可以尝试在签名之前对消息施加某种变换，以阻止上一节的攻击。也就是说，签名者现在把某个具有特定密码学性质（见下文）、将消息映射到 $\mathbb{Z}_N^*$ 的（确定性）函数 $H$ 指定为其公钥的一部分；消息 $m$ 上的签名为 $\sigma := [H(m)^d \bmod N]$，而验证消息 $m$ 上的签名 $\sigma$ 则通过检查 $\sigma^e \stackrel{?}{=} H(m) \bmod N$ 是否成立来完成。见构造 13.6。

**CONSTRUCTION 13.6**

Let GenRSA be as in the previous sections, and construct a signature scheme as follows:

**构造 13.6**

设 GenRSA 如前面各节所述，按如下方式构造签名方案：

Gen: on input ${1}^n$, run $\mathsf{GenRSA}(1^n)$ to compute $(N, e, d)$. The public key is $\langle N, e \rangle$ and the private key is $\langle N, d \rangle$.

Gen：输入 ${1}^n$ 时，运行 $\mathsf{GenRSA}(1^n)$ 计算 $(N, e, d)$。公钥为 $\langle N, e \rangle$，私钥为 $\langle N, d \rangle$。

As part of key generation, a function $H: \{0,1\}^* \to \mathbb{Z}_N^*$ is specified, but we leave this implicit.

作为密钥生成的一部分，还要指定一个函数 $H: \{0,1\}^* \to \mathbb{Z}_N^*$，但我们将其隐含不写。

- Sign: on input a private key $\langle N,d\rangle$ and a message $m\in\{0,1\}^{*}$, compute

- Sign：输入私钥 $\langle N,d\rangle$ 与消息 $m\in\{0,1\}^{*}$ 时，计算

$$\sigma:=[H(m)^{d}\bmod N].$$

- Vrfy: on input a public key $\langle N, e \rangle$, a message $m$, and a signature $\sigma$, output 1 if and only if

- Vrfy：输入公钥 $\langle N, e \rangle$、消息 $m$ 与签名 $\sigma$ 时，输出 1 当且仅当

$$\sigma^{e}\stackrel{?}{=}H(m)\bmod N.$$

**The RSA-FDH signature scheme.**

**RSA-FDH 签名方案。**

What properties does $H$ need in order for this construction to be secure?

要使该构造安全，$H$ 需要具备哪些性质？

At a minimum, to prevent the no-message attack it should be infeasible for an attacker to start with $\sigma$, compute $\hat{m} := [\sigma^e \bmod N]$, and then find a message $m$ such that $H(m) = \hat{m}$. This, in particular, means that $H$ should be hard to invert in some sense. To prevent the second attack, we need an $H$ that does not admit “multiplicative relations,” that is, for which it is hard to find three messages $m, m_1, m_2$ with $H(m) = H(m_1) \cdot H(m_2) \bmod N$. Finally, it must be hard to find collisions in $H$: if $H(m_1) = H(m_2)$, then $m_1$ and $m_2$ have the same signature and forgery becomes trivial.

最起码，为阻止无消息攻击，攻击者从某个 $\sigma$ 出发、计算 $\hat{m} := [\sigma^e \bmod N]$、再找出满足 $H(m) = \hat{m}$ 的消息 $m$，应当是不可行的。这尤其意味着 $H$ 在某种意义上应当难以求逆。为阻止第二种攻击，我们需要 $H$ 不存在“乘法关系”，即难以找到满足 $H(m) = H(m_1) \cdot H(m_2) \bmod N$ 的三个消息 $m, m_1, m_2$。最后，在 $H$ 中寻找碰撞必须是困难的：若 $H(m_1) = H(m_2)$，则 $m_1$ 与 $m_2$ 拥有相同的签名，伪造就变得轻而易举。

There is no known way to choose $H$ so that Construction 13.6 can be proven secure. However, it is possible to prove security if $H$ is modeled as a random oracle that maps its inputs uniformly onto $\mathbb{Z}_N^*$; the resulting scheme is called the RSA full-domain hash (RSA-FDH) signature scheme. One can check that a random function of this sort satisfies the requirements discussed in the previous paragraph: a random function (with large range) is hard to invert, does not have any easy-to-find multiplicative relations, and is collision resistant. Of course, this informal reasoning does not rule out all possible attacks, but the proof of security below does.

目前尚不知道如何选择 $H$ 才能使构造 13.6 被证明是安全的。然而，如果把 $H$ 建模为一个将输入均匀映射到 $\mathbb{Z}_N^*$ 上的随机预言机，就可以证明安全性；所得方案称为 RSA 全域哈希（RSA-FDH）签名方案。可以验证，这类随机函数满足上一段讨论的要求：（值域很大的）随机函数难以求逆、不存在易于找到的乘法关系，并且是抗碰撞的。当然，这种非形式化的推理并不能排除所有可能的攻击，但下文的安全性证明可以做到。

Before continuing, we stress that it is critical for the range of $H$ to be (close to) all of $\mathbb{Z}_N^*$; in particular it does not suffice to simply let $H$ be an “off-the-shelf” cryptographic hash function such as SHA-2. (The output length of SHA-2 is much smaller than the length of RSA moduli used in practice.) Indeed, practical attacks on Construction 13.6 are known if the output length of $H$ is too small (e.g., if the output length is 256 bits as would be the case if a version of SHA-2 were used directly as $H$).

在继续之前要强调：$H$ 的值域（接近）覆盖整个 $\mathbb{Z}_N^*$ 是至关重要的；特别是，仅仅让 $H$ 是 SHA-2 这类“现成的”密码学哈希函数是不够的。（SHA-2 的输出长度远小于实际使用的 RSA 模数的长度。）事实上，如果 $H$ 的输出长度过小，针对构造 13.6 的实用攻击是已知的（例如输出长度为 256 比特时——若直接把某个版本的 SHA-2 用作 $H$ 就会是这种情况）。

Before turning to the formal proof, we provide some intuition. Our goal is to prove that if the RSA problem is hard relative to GenRSA, then RSA-FDH is secure when $H$ is modeled as a random oracle. We consider first security against a no-message attack, i.e., when the adversary $\mathcal{A}$ cannot request any signatures. Here the adversary is limited to making queries to the random oracle, and we assume without loss of generality that $\mathcal{A}$ always makes exactly $q$ (distinct) queries to $H$ and that if the adversary outputs a forgery $(m, \sigma)$ then it had previously queried $m$ to $H$.

在给出形式化证明之前，我们先提供一些直觉。我们的目标是证明：如果 RSA 问题相对于 GenRSA 是困难的，那么当 $H$ 被建模为随机预言机时，RSA-FDH 是安全的。首先考虑针对无消息攻击的安全性，即敌手 $\mathcal{A}$ 不能请求任何签名的情形。此时敌手只能向随机预言机发起查询；不失一般性，我们假设 $\mathcal{A}$ 总是恰好向 $H$ 提出 $q$ 次（互不相同的）查询，且若敌手输出伪造 $(m, \sigma)$，则它此前已向 $H$ 查询过 $m$。

Say there is an efficient adversary $\mathcal{A}$ that carries out a no-message attack and makes exactly $q$ queries to $H$. We construct an efficient algorithm $\mathcal{A}^{\prime}$ solving the RSA problem relative to $\mathsf{GenRSA}$. Given input $(N, e, y)$, algorithm $\mathcal{A}^{\prime}$ runs $\mathcal{A}$ on the public key $pk = \langle N, e \rangle$. Let $m_1, \ldots, m_q$ denote the $q$ (distinct) queries that $\mathcal{A}$ makes to $H$. Our algorithm $\mathcal{A}^{\prime}$ answers these random-oracle queries of $\mathcal{A}$ with uniform elements of $\mathbb{Z}_N^*$ except for one query—say, the $i$th query, chosen uniformly from the oracle queries of $\mathcal{A}$—that is answered with $y$ itself. Note that, from the point of view of $\mathcal{A}$, all its random-oracle queries are answered with uniform elements of $\mathbb{Z}_N^*$ (recall that $y$ is uniform as well, although it is not chosen by $\mathcal{A}^{\prime}$), and so $\mathcal{A}$ has no information about $i$. Moreover, the view of $\mathcal{A}$ when run as a subroutine by $\mathcal{A}^{\prime}$ is identically distributed to the view of $\mathcal{A}$ when attacking the original signature scheme.

假设存在一个高效敌手 $\mathcal{A}$ 实施无消息攻击，恰好向 $H$ 提出 $q$ 次查询。我们构造一个求解相对于 $\mathsf{GenRSA}$ 的 RSA 问题的高效算法 $\mathcal{A}^{\prime}$。给定输入 $(N, e, y)$，算法 $\mathcal{A}^{\prime}$ 以公钥 $pk = \langle N, e \rangle$ 运行 $\mathcal{A}$。记 $m_1, \ldots, m_q$ 为 $\mathcal{A}$ 向 $H$ 提出的 $q$ 次（互不相同的）查询。我们的算法 $\mathcal{A}^{\prime}$ 用 $\mathbb{Z}_N^*$ 中的均匀元素回答 $\mathcal{A}$ 的这些随机预言机查询，但有一次例外——比如说第 $i$ 次查询（$i$ 从 $\mathcal{A}$ 的预言机查询中均匀选取）——用 $y$ 本身来回答。注意，从 $\mathcal{A}$ 的视角看，它的所有随机预言机查询都是用 $\mathbb{Z}_N^*$ 中的均匀元素回答的（回想一下，$y$ 也是均匀的，尽管它不是由 $\mathcal{A}^{\prime}$ 选取的），因此 $\mathcal{A}$ 对 $i$ 一无所知。而且，$\mathcal{A}$ 作为 $\mathcal{A}^{\prime}$ 的子程序运行时的视图，与 $\mathcal{A}$ 攻击原始签名方案时的视图分布完全相同。

If $\mathcal{A}$ outputs a forgery $(m,\sigma)$ then, because $m\in\{m_1,\ldots,m_q\}$, with probability ${1}/q$ we will have $m=m_i$. In that case,

如果 $\mathcal{A}$ 输出伪造 $(m,\sigma)$，那么由于 $m\in\{m_1,\ldots,m_q\}$，以 ${1}/q$ 的概率会有 $m=m_i$。此时

$$\sigma^{e}=H(m)=H(m_{i})=y\bmod N$$

and $\mathcal{A}^{\prime}$ can output $\sigma$ as the solution to its given RSA instance $(N,e,y)$. We conclude that if $\mathcal{A}$ outputs a forgery with probability $\varepsilon$, then $\mathcal{A}^{\prime}$ solves the RSA problem with probability $\varepsilon/q$. Since $q$ is polynomial, we conclude that $\varepsilon$ must be negligible if the RSA problem is hard relative to $\mathsf{GenRSA}$.

于是 $\mathcal{A}^{\prime}$ 可以输出 $\sigma$ 作为给定 RSA 实例 $(N,e,y)$ 的解。我们得出结论：如果 $\mathcal{A}$ 以概率 $\varepsilon$ 输出伪造，那么 $\mathcal{A}^{\prime}$ 以概率 $\varepsilon/q$ 求解 RSA 问题。由于 $q$ 是多项式，我们得出：若 RSA 问题相对于 $\mathsf{GenRSA}$ 是困难的，则 $\varepsilon$ 必是可忽略的。

Handling the case when the adversary is allowed to request signatures on messages of its choice is more difficult. The complication arises since our algorithm $\mathcal{A}^{\prime}$ above does not know the decryption exponent $d$, yet now has to compute valid signatures on messages queried by $\mathcal{A}$ to its signing oracle. This seems impossible (and possibly even contradictory!) until we realize that $\mathcal{A}^{\prime}$ can correctly compute a signature on a message $m$ as long as it sets $H(m)$ to be equal to $[\sigma^e \bmod N]$ for a known value $\sigma$. (Here we are using the fact that the random oracle is “programmable.”) If $\sigma$ is uniform then $[\sigma^e \bmod N]$ is uniform as well, and so the random oracle is still emulated “properly” by $\mathcal{A}^{\prime}$.

处理敌手可以请求其自选消息上签名的情形更为困难。困难在于：我们前面的算法 $\mathcal{A}^{\prime}$ 并不知道解密指数 $d$，但现在却必须对 $\mathcal{A}$ 向其签名预言机查询的消息计算出有效签名。这似乎不可能（甚至自相矛盾！）——直到我们意识到：只要 $\mathcal{A}^{\prime}$ 把 $H(m)$ 设定为等于 $[\sigma^e \bmod N]$（其中 $\sigma$ 是它已知的值），它就能正确计算消息 $m$ 上的签名。（这里我们利用了随机预言机是“可编程的”这一事实。）若 $\sigma$ 是均匀的，则 $[\sigma^e \bmod N]$ 也是均匀的，因此 $\mathcal{A}^{\prime}$ 仍然“恰当地”模拟了随机预言机。

The above intuition is formalized in the proof of the following:

上述直觉在以下定理的证明中得以形式化：

THEOREM 13.7 If the RSA problem is hard relative to $\mathsf{GenRSA}$ and $H$ is modeled as a random oracle, then Construction 13.6 is secure.

定理 13.7　若 RSA 问题相对于 $\mathsf{GenRSA}$ 是困难的，且 $H$ 被建模为随机预言机，则构造 13.6 是安全的。

PROOF Let $\Pi = (\mathrm{Gen}, \mathrm{Sign}, \mathrm{Vrfy})$ denote Construction 13.6, and let $\mathcal{A}$ be a probabilistic polynomial-time adversary. We assume without loss of generality that if $\mathcal{A}$ requests a signature on a message $m$, or outputs a forgery $(m, \sigma)$, then it previously queried $m$ to $H$. Let $q(n)$ be a polynomial upper bound on the number of queries $\mathcal{A}$ makes to $H$ on security parameter $n$; we assume without loss of generality that $\mathcal{A}$ makes exactly $q(n)$ distinct queries to $H$.

证明　记 $\Pi = (\mathrm{Gen}, \mathrm{Sign}, \mathrm{Vrfy})$ 为构造 13.6，设 $\mathcal{A}$ 是一个概率多项式时间敌手。不失一般性，我们假设：若 $\mathcal{A}$ 请求消息 $m$ 上的签名，或输出伪造 $(m, \sigma)$，则它此前已向 $H$ 查询过 $m$。设 $q(n)$ 是 $\mathcal{A}$ 在安全参数为 $n$ 时向 $H$ 发起查询次数的多项式上界；不失一般性，假设 $\mathcal{A}$ 恰好向 $H$ 提出 $q(n)$ 次互不相同的查询。

For convenience, we list the steps of experiment $\mathsf{Sig-forge}_{\mathcal{A},\Pi}(n)$:

为方便起见，我们列出实验 $\mathsf{Sig-forge}_{\mathcal{A},\Pi}(n)$ 的步骤：

1. $\mathsf{GenRSA}({1}^{n})$ is run to obtain $(N,e,d)$. A random function $H:\{0,1\}^{*} \to \mathbb{Z}_{N}^{*}$ is chosen.

   运行 $\mathsf{GenRSA}({1}^{n})$ 得到 $(N,e,d)$。选取一个随机函数 $H:\{0,1\}^{*} \to \mathbb{Z}_{N}^{*}$。

2. The adversary $\mathcal{A}$ is given $pk = \langle N, e \rangle$, and may query $H$ as well as a signing oracle $\mathsf{Sign}_{\langle N, d \rangle}(\cdot)$ that, on input a message $m$, returns $\sigma := [H(m)^d \bmod N]$.

   敌手 $\mathcal{A}$ 被给予 $pk = \langle N, e \rangle$，并可查询 $H$ 以及签名预言机 $\mathsf{Sign}_{\langle N, d \rangle}(\cdot)$——后者输入消息 $m$ 时返回 $\sigma := [H(m)^d \bmod N]$。

3. $\mathcal{A}$ outputs $(m,\sigma)$, where it had not previously requested a signature on $m$. The output of the experiment is 1 if and only if $\sigma^{e}=H(m)\bmod N$.

   $\mathcal{A}$ 输出 $(m,\sigma)$，其中它此前未曾请求过 $m$ 上的签名。实验输出 1 当且仅当 $\sigma^{e}=H(m)\bmod N$。

We define a modified experiment $\mathsf{Sig-forge}^{\prime}_{\mathcal{A},\Pi}(n)$ in which a guess is made at the outset as to which message (from among the $q$ messages that $\mathcal{A}$ queries to $H$) will correspond to the eventual forgery (if any) output by $\mathcal{A}$:

我们定义一个修改后的实验 $\mathsf{Sig-forge}^{\prime}_{\mathcal{A},\Pi}(n)$：在实验一开始就猜测——在 $\mathcal{A}$ 向 $H$ 查询的 $q$ 个消息中——哪一个将对应于 $\mathcal{A}$ 最终输出的伪造（如果有的话）：

1. Choose uniform $j \in \{1, \ldots, q\}$.

   均匀选取 $j \in \{1, \ldots, q\}$。

2. $\mathsf{GenRSA}({1}^{n})$ is run to obtain $(N,e,d)$. A random function $H:\{0,1\}^{*} \to \mathbb{Z}_{N}^{*}$ is chosen.

   运行 $\mathsf{GenRSA}({1}^{n})$ 得到 $(N,e,d)$。选取一个随机函数 $H:\{0,1\}^{*} \to \mathbb{Z}_{N}^{*}$。

3. The adversary $\mathcal{A}$ is given $pk = \langle N, e \rangle$, and may query $H$ as well as a signing oracle $\mathsf{Sign}_{\langle N, d \rangle}(\cdot)$ that, on input a message $m$, returns $\sigma := [H(m)^d \bmod N]$.

   敌手 $\mathcal{A}$ 被给予 $pk = \langle N, e \rangle$，并可查询 $H$ 以及签名预言机 $\mathsf{Sign}_{\langle N, d \rangle}(\cdot)$——后者输入消息 $m$ 时返回 $\sigma := [H(m)^d \bmod N]$。

4. $\mathcal{A}$ outputs $(m,\sigma)$, where it had not previously requested a signature on $m$. Let $i$ be such that $m=m_i$.^2 The output of the experiment is 1 if and only if $\sigma^e=H(m)\bmod N$ and $j=i$.

   $\mathcal{A}$ 输出 $(m,\sigma)$，其中它此前未曾请求过 $m$ 上的签名。设 $i$ 满足 $m=m_i$。^2 实验输出 1 当且仅当 $\sigma^e=H(m)\bmod N$ 且 $j=i$。

> $^2$ Here $m_i$ denotes the $i$th query made to $H$. Recall, by assumption, that if $\mathcal{A}$ requests a signature on a message $m$, then it must have previously queried $m$ to $H$.

> $^2$ 这里 $m_i$ 表示向 $H$ 提出的第 $i$ 次查询。回想一下，根据假设，若 $\mathcal{A}$ 请求消息 $m$ 上的签名，则它必已事先向 $H$ 查询过 $m$。

Since $j$ is uniform and independent of everything else, the probability that $j = i$ (even conditioned on the event that $\mathcal{A}$ outputs a forgery) is exactly ${1}/q$. Therefore $\Pr[\mathsf{Sig-forge}^{\prime}_{\mathcal{A},\Pi}(n) = 1] = \frac{1}{q(n)} \cdot \Pr[\mathsf{Sig-forge}_{\mathcal{A},\Pi}(n) = 1]$.

由于 $j$ 是均匀的且与其他一切相互独立，$j = i$ 的概率（即使以 $\mathcal{A}$ 输出伪造为条件）恰好是 ${1}/q$。因此 $\Pr[\mathsf{Sig-forge}^{\prime}_{\mathcal{A},\Pi}(n) = 1] = \frac{1}{q(n)} \cdot \Pr[\mathsf{Sig-forge}_{\mathcal{A},\Pi}(n) = 1]$。

Now consider the modified experiment $\mathsf{Sig-forge}_{\mathcal{A},\Pi}^{\prime\prime}(n)$ in which the experiment is aborted if $\mathcal{A}$ ever requests a signature on the message $m_j$ (where $m_j$ denotes the $j$th message queried to $H$, and $j$ is the uniform value chosen at the outset). This does not change the probability that the output of the experiment is 1, since if $\mathcal{A}$ ever requests a signature on $m_{j}$ then it cannot possibly output a forgery on $m_{j}$. In words,

现在考虑修改后的实验 $\mathsf{Sig-forge}_{\mathcal{A},\Pi}^{\prime\prime}(n)$：若 $\mathcal{A}$ 请求消息 $m_j$ 上的签名，则实验中止（这里 $m_j$ 表示向 $H$ 查询的第 $j$ 个消息，$j$ 是最初均匀选取的值）。这并不改变实验输出 1 的概率，因为若 $\mathcal{A}$ 请求了 $m_{j}$ 上的签名，它就不可能再输出 $m_{j}$ 上的伪造。换言之，

$$\begin{aligned}\Pr[\mathsf{Sig-forge}_{\mathcal{A},\Pi}^{\prime \prime}(n)=1]&=\Pr[\mathsf{Sig-forge}_{\mathcal{A},\Pi}^{\prime}(n)=1]\\&=\frac{\Pr[\mathsf{Sig-forge}_{\mathcal{A},\Pi}(n)=1]}{q(n)}.\end{aligned} \tag{13.1}$$

Finally, consider the following algorithm $A^{\prime}$ solving the RSA problem:

最后，考虑下面这个求解 RSA 问题的算法 $A^{\prime}$：

Algorithm A':

算法 A'：

The algorithm is given $(N, e, y)$ as input.

算法以 $(N, e, y)$ 为输入。

1. Choose uniform $j \in \{1, \ldots, q\}$.

   均匀选取 $j \in \{1, \ldots, q\}$。

2. Run $\mathcal{A}$ on input the public key $pk = \langle N, e \rangle$. Store triples $(\cdot, \cdot, \cdot)$ in a table, initially empty. An entry $(m_i, \sigma_i, y_i)$ indicates that $\mathcal{A}^{\prime}$ has set $H(m_i) = y_i$, and $\sigma_i^e = y_i \bmod N$.

   以公钥 $pk = \langle N, e \rangle$ 为输入运行 $\mathcal{A}$。把三元组 $(\cdot, \cdot, \cdot)$ 存入一张初始为空的表中。表项 $(m_i, \sigma_i, y_i)$ 表示 $\mathcal{A}^{\prime}$ 已设定 $H(m_i) = y_i$，且 $\sigma_i^e = y_i \bmod N$。

3. When $\mathcal{A}$ makes its $i$th random-oracle query $H(m_{i})$, answer it as follows:

   当 $\mathcal{A}$ 发起其第 $i$ 次随机预言机查询 $H(m_{i})$ 时，按如下方式回答：

- If $i = j$, return $y$ as the answer to the query.

- 若 $i = j$，返回 $y$ 作为该查询的回答。

- Else choose uniform $\sigma_i \in \mathbb{Z}_N^*$, compute $y_i := [\sigma_i^e \bmod N]$, return $y_i$ as the answer to the query, and store $(m_i, \sigma_i, y_i)$ in the table.

- 否则，均匀选取 $\sigma_i \in \mathbb{Z}_N^*$，计算 $y_i := [\sigma_i^e \bmod N]$，返回 $y_i$ 作为该查询的回答，并把 $(m_i, \sigma_i, y_i)$ 存入表中。

When $\mathcal{A}$ requests a signature on message $m$, let $i$ be such that $m = m_i$ and answer the query as follows$^3$:

当 $\mathcal{A}$ 请求消息 $m$ 上的签名时，设 $i$ 满足 $m = m_i$，按如下方式回答该查询$^3$：

- If $i = j$ then $\mathcal{A}^{\prime}$ aborts.

- 若 $i = j$，则 $\mathcal{A}^{\prime}$ 中止。

- If $i \neq j$ then there is an entry $(m_i, \sigma_i, y_i)$ in the table. Return $\sigma_i$ as the answer to the query.

- 若 $i \neq j$，则表中存在表项 $(m_i, \sigma_i, y_i)$。返回 $\sigma_i$ 作为该查询的回答。

> $^3$ Here $m_i$ denotes the $i$th query made to $H$. Recall, by assumption, that if $\mathcal{A}$ requests a signature on a message $m$, then it must have previously queried $m$ to $H$.
> $^3$ 这里 $m_i$ 表示向 $H$ 提出的第 $i$ 次查询。回想一下，根据假设，若 $\mathcal{A}$ 请求消息 $m$ 上的签名，则它必已事先向 $H$ 查询过 $m$。

4. At the end of $\mathcal{A}$'s execution, it outputs $(m,\sigma)$. If $m=m_j$ and $\sigma^e=y\bmod N$, then output $\sigma$.

   在 $\mathcal{A}$ 执行结束时，它输出 $(m,\sigma)$。若 $m=m_j$ 且 $\sigma^e=y\bmod N$，则输出 $\sigma$。

Clearly, $\mathcal{A}^{\prime}$ runs in probabilistic polynomial time. Say the input $(N, e, y)$ to $\mathcal{A}^{\prime}$ is generated by running $\mathsf{GenRSA}(1^n)$ to obtain $(N, e, d)$, and then choosing uniform $y \in \mathbb{Z}_N^*$. The crucial observation is that the view of $\mathcal{A}$ when run as a subroutine by $\mathcal{A}^{\prime}$ is identical to the view of $\mathcal{A}$ in experiment $\mathsf{Sig-forge}_{\mathcal{A}, \Pi}^{\prime\prime}(n)$. In particular, all $\mathsf{Sign-oracle}$ queries are answered correctly, and each of the random-oracle queries of $\mathcal{A}$ when run as a subroutine by $\mathcal{A}^{\prime}$ is answered with a uniform element of $\mathbb{Z}_N^*$:

显然，$\mathcal{A}^{\prime}$ 在概率多项式时间内运行。设 $\mathcal{A}^{\prime}$ 的输入 $(N, e, y)$ 是这样生成的：运行 $\mathsf{GenRSA}(1^n)$ 得到 $(N, e, d)$，然后均匀选取 $y \in \mathbb{Z}_N^*$。关键的观察是：$\mathcal{A}$ 作为 $\mathcal{A}^{\prime}$ 的子程序运行时的视图，与 $\mathcal{A}$ 在实验 $\mathsf{Sig-forge}_{\mathcal{A}, \Pi}^{\prime\prime}(n)$ 中的视图完全相同。特别地，所有签名预言机查询都被正确回答，且 $\mathcal{A}$ 作为 $\mathcal{A}^{\prime}$ 的子程序运行时的每一次随机预言机查询，都是用 $\mathbb{Z}_N^*$ 中的均匀元素回答的：

- The query $H(m_j)$ is answered with $y$, a uniform element of $\mathbb{Z}_N^*$.

- 查询 $H(m_j)$ 用 $y$ 回答，而 $y$ 是 $\mathbb{Z}_N^*$ 中的均匀元素。

- Queries $H(m_i)$ with $i \neq j$ are answered with $y_i = [\sigma_i^e \bmod N]$, where $\sigma_i$ is uniform in $\mathbb{Z}_N^*$. Since exponentiation to the $eth$ power is a one-to-one function, $y_i$ is uniformly distributed as well.

- 对 $i \neq j$ 的查询 $H(m_i)$ 用 $y_i = [\sigma_i^e \bmod N]$ 回答，其中 $\sigma_i$ 在 $\mathbb{Z}_N^*$ 中均匀。由于 $e$ 次幂运算是一一映射，$y_i$ 也是均匀分布的。

Finally, observe that whenever experiment $\mathsf{Sig-forge}_{\mathcal{A},\Pi}^{\prime\prime}(n)$ would output 1, then $\mathcal{A}^{\prime}$ outputs a correct solution to its given RSA instance. This follows since $\mathsf{Sig-forge}_{\mathcal{A},\Pi}^{\prime\prime}(n) = 1$ implies that $j = i$ and $\sigma^e = H(m_i) \mod N$. Now, when $j = i$, algorithm $\mathcal{A}^{\prime}$ does not abort and in addition $H(m_i) = y$. Thus, $\sigma^e = H(m_i) = y \mod N$, and so $\sigma$ is the desired inverse. Using Equation (13.1), this means that

最后注意，每当实验 $\mathsf{Sig-forge}_{\mathcal{A},\Pi}^{\prime\prime}(n)$ 输出 1 时，$\mathcal{A}^{\prime}$ 就输出给定 RSA 实例的一个正确解。这是因为 $\mathsf{Sig-forge}_{\mathcal{A},\Pi}^{\prime\prime}(n) = 1$ 蕴含 $j = i$ 且 $\sigma^e = H(m_i) \mod N$。而当 $j = i$ 时，算法 $\mathcal{A}^{\prime}$ 不会中止，且另有 $H(m_i) = y$。于是 $\sigma^e = H(m_i) = y \mod N$，故 $\sigma$ 就是所求的逆元。利用式 (13.1)，这意味着

$$\begin{aligned}\Pr[\mathsf{RSA\text{-}inv}_{\mathcal{A}^{\prime},\mathsf{GenRSA}}(n)=1]&=\Pr[\mathsf{Sig-forge}^{\prime \prime}_{\mathcal{A},\Pi}(n)=1]\\&=\frac{\Pr[\mathsf{Sig-forge}_{\mathcal{A},\Pi}(n)=1]}{q(n)}.\end{aligned} \tag{13.2}$$

If the RSA problem is hard relative to GenRSA, there is a negligible function $\mathsf{negl}$ such that $\Pr[\mathsf{RSA-inv}_{\mathcal{A}^{\prime},\mathsf{GenRSA}}(n) = 1] \leq \mathsf{negl}(n)$. Since $q(n)$ is polynomial, we conclude from Equation (13.2) that $\Pr[\mathsf{Sig-forge}_{\mathcal{A},\Pi}(n) = 1]$ is negligible as well. This completes the proof.

如果 RSA 问题相对于 GenRSA 是困难的，则存在可忽略函数 $\mathsf{negl}$ 使得 $\Pr[\mathsf{RSA-inv}_{\mathcal{A}^{\prime},\mathsf{GenRSA}}(n) = 1] \leq \mathsf{negl}(n)$。由于 $q(n)$ 是多项式，由式 (13.2) 可知 $\Pr[\mathsf{Sig-forge}_{\mathcal{A},\Pi}(n) = 1]$ 也是可忽略的。证明完毕。

RSA PKCS #1 standards. RSA PKCS #1 v1.5 specifies a signature scheme that is very similar to RSA-FDH. A more-complex scheme that can be viewed as a randomized variant of RSA-FDH has been included in the PKCS #1 standard since version 2.1.

**RSA PKCS #1 标准。**

RSA PKCS #1 v1.5 规定了一个与 RSA-FDH 非常相似的签名方案。另一个更复杂、可视为 RSA-FDH 随机化变体的方案，自 2.1 版本起被纳入 PKCS #1 标准。

## 13.5 Signatures from the Discrete-Logarithm Problem　基于离散对数问题的签名

Signature schemes can be based on the discrete-logarithm assumption as well, although the assumption does not lend itself as readily to signatures as the RSA assumption does. In Sections 13.5.1 and 13.5.2 we describe the Schnorr signature scheme that can be proven secure in the random-oracle model. In Section 13.5.3 we describe the DSA and ECDSA signature schemes; these standardized schemes are widely used even though they have no full proof of security.

签名方案也可以基于离散对数假设，尽管该假设不像 RSA 假设那样直接适用于签名。在 13.5.1 节和 13.5.2 节中，我们描述可在随机预言机模型中证明安全的 Schnorr 签名方案。在 13.5.3 节中，我们描述 DSA 和 ECDSA 签名方案；这两个标准化方案虽没有完整的安全性证明，却被广泛使用。

### 13.5.1 Identification Schemes and Signatures　身份识别方案与签名

The underlying intuition for the Schnorr signature scheme is best explained by taking a slight detour to discuss (public-key) identification schemes. We then describe the Fiat-Shamir transform that can be used to convert identification schemes to signature schemes in the random-oracle model. Finally,
we present the Schnorr identification scheme—and corresponding signature scheme—based on the discrete-logarithm problem.

要解释 Schnorr 签名方案背后的直觉，最好先稍微绕个弯，讨论一下（公钥）身份识别方案。然后我们描述 Fiat–Shamir 变换，它可以在随机预言机模型中把身份识别方案转换成签名方案。最后，我们给出基于离散对数问题的 Schnorr 身份识别方案以及相应的签名方案。

### Identification Schemes　身份识别方案

An identification scheme is an interactive protocol that allows one party to prove its identity (i.e., to authenticate itself) to another. This is a very natural notion, and it is common nowadays to authenticate oneself when logging in to a website. We call the party identifying herself (e.g., the user) the “prover,” and the party verifying the identity (e.g., the web server) the “verifier.” Here, we are interested in the public-key setting where the prover and verifier do not share any secret information (such as a password) in advance; instead, the verifier only knows the public key of the prover. Successful execution of the identification protocol convinces the verifier that it is communicating with the intended prover rather than an imposter.

身份识别方案是一种交互式协议，允许一方向另一方证明自己的身份（即向另一方认证自己）。这是一个非常自然的概念，如今登录网站时进行身份认证就是常见的例子。我们把证明自身身份的一方（如用户）称为“证明者”（prover），把验证身份的一方（如网站服务器）称为“验证者”（verifier）。这里我们关注公钥场景：证明者与验证者事先并不共享任何秘密信息（如口令），验证者只知道证明者的公钥。身份识别协议的成功执行使验证者确信，自己正在与目标证明者而非冒充者通信。

We will only consider three-round identification protocols of a specific form, where the prover is specified by two algorithms $\mathcal{P}_1$, $\mathcal{P}_2$ and the verifier's side of the protocol is specified by an algorithm V. The prover runs $\mathcal{P}_1(sk)$ using its private key $sk$ to obtain an initial message $I$ along with some state $\mathbf{st}$, and initiates the protocol by sending $I$ to the verifier. In response, the verifier sends a challenge $r$ chosen uniformly from some set $\Omega_{pk}$ defined by the prover's public key $pk$. Next, the prover runs $\mathcal{P}_2(sk, \mathbf{st}, r)$ to compute a response $s$ that it sends back to the verifier. Finally, the verifier computes $\mathcal{V}(pk, r, s)$ and accepts if and only if this results in the initial message $I$; see Figure 13.1. Of course, for correctness we require that if the legitimate prover executes the protocol correctly then the verifier should always accept.

我们只考虑一种特定形式的三轮身份识别协议：证明者由两个算法 $\mathcal{P}_1$、$\mathcal{P}_2$ 刻画，协议中验证者一侧由算法 V 刻画。证明者用自己的私钥 $sk$ 运行 $\mathcal{P}_1(sk)$，得到初始消息 $I$ 和某个状态 $\mathbf{st}$，并通过把 $I$ 发送给验证者来发起协议。作为回应，验证者发送一个从由证明者公钥 $pk$ 定义的某个集合 $\Omega_{pk}$ 中均匀选取的挑战值 $r$。接着，证明者运行 $\mathcal{P}_2(sk, \mathbf{st}, r)$ 计算出响应 $s$ 并发回给验证者。最后，验证者计算 $\mathcal{V}(pk, r, s)$，当且仅当其结果为初始消息 $I$ 时接受；见图 13.1。当然，从正确性角度我们要求：若合法的证明者正确执行协议，验证者应当总是接受。

![Image](https://lsky.jerryxue.top/i/2026/08/25/6a8d86e9329df.jpg)

**FIGURE 13.1: A three-round identification scheme. / 图 13.1：三轮身份识别方案。**

For technical reasons, we assume identification schemes that are “non-degenerate,” which intuitively means that there are many possible initial messages I, and none has a high probability of being sent. Formally, a scheme is non-degenerate if for every private key sk and any fixed initial message I, the probability that $\mathcal{P}_1(sk)$ outputs I is negligible. (Any identification scheme can be trivially modified to be non-degenerate by sending a uniform n-bit string along with the initial message.)

出于技术上的原因，我们假设身份识别方案是“非退化的”，直观地说就是可能的初始消息 I 有很多个，且任何一个都不会以很高的概率被发送。形式化地说，若对每个私钥 sk 和任意固定的初始消息 I，$\mathcal{P}_1(sk)$ 输出 I 的概率都是可忽略的，则称该方案是非退化的。（任何身份识别方案都可以平凡地修改为非退化的：只需随初始消息一起发送一个均匀的 n 比特串即可。）

The basic security requirement of an identification scheme is that an adversary who does not know the prover's secret key should be unable to fool the verifier into accepting. This should hold even if the attacker is able to passively eavesdrop on multiple (honest) executions of the protocol between the prover and verifier. We formalize such eavesdropping via an oracle $\mathsf{Trans}_{sk}$ that, when called without any input, runs an honest execution of the protocol and returns to the adversary the entire transcript $(I, r, s)$ of the interaction.

身份识别方案的基本安全要求是：不知道证明者密钥的敌手应无法骗过验证者使其接受。即使攻击者能够被动窃听证明者与验证者之间协议的多次（诚实）执行，这一点也应成立。我们通过一个预言机 $\mathsf{Trans}_{sk}$ 来形式化这种窃听：该预言机被调用时不需要输入，它运行协议的一次诚实执行，并把交互的完整记录 $(I, r, s)$ 返回给敌手。

Let $\Pi = (\mathrm{Gen}, \mathcal{P}_1, \mathcal{P}_2, \mathcal{V})$ be an identification scheme, and consider the following experiment for an adversary $\mathcal{A}$ and parameter $n$:

设 $\Pi = (\mathrm{Gen}, \mathcal{P}_1, \mathcal{P}_2, \mathcal{V})$ 是一个身份识别方案，考虑下面针对敌手 $\mathcal{A}$ 与参数 $n$ 的实验：

The identification experiment $\mathsf{Ident}_{\mathcal{A},\Pi}(n)$:

身份识别实验 $\mathsf{Ident}_{\mathcal{A},\Pi}(n)$：

1. Gen ${1}^{n}$ is run to obtain keys $(pk, sk)$.

   运行 Gen ${1}^{n}$ 得到密钥 $(pk, sk)$。

2. Adversary $\mathcal{A}$ is given $pk$ and access to an oracle $\mathsf{Trans}_{sk}$ that it can query as often as it likes.

   敌手 $\mathcal{A}$ 被给予 $pk$ 以及对预言机 $\mathsf{Trans}_{sk}$ 的访问权，可任意多次查询。

3. At any point during the experiment, $\mathcal{A}$ outputs a message I. A uniform challenge $r \in \Omega_{pk}$ is chosen and given to $\mathcal{A}$, who responds with some s. ($\mathcal{A}$ may continue to query $\mathsf{Trans}_{sk}$ even after receiving r.)

   在实验的任意时刻，$\mathcal{A}$ 输出一条消息 I。随后均匀选取挑战值 $r \in \Omega_{pk}$ 并交给 $\mathcal{A}$，$\mathcal{A}$ 以某个 s 作答。（$\mathcal{A}$ 即使在收到 r 之后也可以继续查询 $\mathsf{Trans}_{sk}$。）

4. The experiment outputs 1 if and only if $\mathcal{V}(pk, r, s) \overset{?}{=} I$.

   实验输出 1 当且仅当 $\mathcal{V}(pk, r, s) \overset{?}{=} I$。

DEFINITION 13.8 An identification scheme $\Pi = (\mathrm{Gen}, \mathcal{P}_1, \mathcal{P}_2, \mathcal{V})$ is secure against a passive attack, or just secure, if for all probabilistic polynomial-time adversaries $\mathcal{A}$, there exists a negligible function $\mathrm{negl}$ such that:

定义 13.8　若对于所有概率多项式时间敌手 $\mathcal{A}$，都存在可忽略函数 $\mathrm{negl}$ 使得下式成立，则称身份识别方案 $\Pi = (\mathrm{Gen}, \mathcal{P}_1, \mathcal{P}_2, \mathcal{V})$ 在被动攻击下是安全的，或简称安全的：

$$\Pr[{{\mathsf{Ident}}}_{{\mathcal{A}},\Pi}(n)=1]\leq{\mathsf{negl}}(n).$$

It is also possible to consider stronger notions of security, for example, where the adversary can also carry out active attacks on the protocol by impersonating a verifier and possibly sending maliciously chosen values r. We will not need this for our application to signature schemes.

也可以考虑更强的安全性概念，例如敌手还能对协议实施主动攻击——冒充验证者并可能发送恶意选取的值 r。不过，在签名方案的应用中我们并不需要这些。

### From Identification Schemes to Signatures　从身份识别方案到签名

The Fiat-Shamir transform (Construction 13.9) provides a way to convert any (interactive) identification scheme into a (non-interactive) signature scheme. The basic idea is for the signer to act as a prover, running the identification protocol by itself. That is, to sign a message $m$, the signer first computes $I$, and next generates the challenge $r$ by applying some function $H$ to $I$ and $m$. It then derives the correct response $s$. The signature on $m$ is $(r,s)$, which can be verified by (1) recomputing $I := \mathcal{V}(pk, r, s)$ and then (2) checking that $H(I, m) \overset{?}{=} r$.

Fiat–Shamir 变换（构造 13.9）提供了一种把任何（交互式）身份识别方案转换为（非交互式）签名方案的方法。基本思想是让签名者充当证明者，自己运行身份识别协议。也就是说，要对消息 $m$ 签名，签名者先计算 $I$，再把某个函数 $H$ 作用于 $I$ 和 $m$ 生成挑战值 $r$，然后导出正确的响应 $s$。$m$ 上的签名是 $(r,s)$，验证方法是：(1) 重新计算 $I := \mathcal{V}(pk, r, s)$；(2) 检查 $H(I, m) \overset{?}{=} r$ 是否成立。

**CONSTRUCTION 13.9**

Let $(\mathrm{Gen}_{id}, \mathcal{P}_1, \mathcal{P}_2, \mathcal{V})$ be an identification scheme, and construct a signature scheme as follows:

**构造 13.9**

设 $(\mathrm{Gen}_{id}, \mathcal{P}_1, \mathcal{P}_2, \mathcal{V})$ 是一个身份识别方案，按如下方式构造签名方案：

Gen: on input ${1}^n$, simply run $\mathsf{Gen}_{id}(1^n)$ to obtain keys $pk$, $sk$.

Gen：输入 ${1}^n$ 时，直接运行 $\mathsf{Gen}_{id}(1^n)$ 得到密钥 $pk$、$sk$。

The public key $pk$ specifies a set of challenges $\Omega_{pk}$. As part of key generation, a function $H: \{0,1\}^* \to \Omega_{pk}$ is specified, but we leave this implicit.

公钥 $pk$ 指定了挑战值集合 $\Omega_{pk}$。作为密钥生成的一部分，还要指定一个函数 $H: \{0,1\}^* \to \Omega_{pk}$，但我们将其隐含不写。

- Sign: on input a private key $sk$ and a message $m \in \{0,1\}^{*}$, do:

- Sign：输入私钥 $sk$ 与消息 $m \in \{0,1\}^{*}$ 时，执行：

1. Compute $(I, \mathbf{st}) \leftarrow \mathcal{P}_1(sk)$.

   计算 $(I, \mathbf{st}) \leftarrow \mathcal{P}_1(sk)$。

2. Compute $r := H(I, m)$.

   计算 $r := H(I, m)$。

3. Compute $s := \mathcal{P}_2(sk, \mathbf{st}, r)$.

   计算 $s := \mathcal{P}_2(sk, \mathbf{st}, r)$。

Output the signature $(r, s)$.

输出签名 $(r, s)$。

- Vrfy: on input a public key $pk$, a message $m$, and a signature $(r, s)$, compute $I := \mathcal{V}(pk, r, s)$ and output 1 if and only if

- Vrfy：输入公钥 $pk$、消息 $m$ 与签名 $(r, s)$ 时，计算 $I := \mathcal{V}(pk, r, s)$，输出 1 当且仅当

$$H(I,m)\stackrel{?}{=}r.$$

The Fiat-Shamir transform.

Fiat–Shamir 变换。

A signature $(r,s)$ is “bound” to a specific message $m$ because $r$ is a function of both $I$ and $m$; changing $m$ thus results in a completely different $r$. If $H$ is modeled as a random oracle mapping inputs uniformly onto $\Omega_{pk}$, then the challenge $r$ is uniform; intuitively, it will be just as difficult for an adversary (who does not know $sk$) to find a valid signature $(r,s)$ on a message $m$ as it would be to impersonate the prover in an honest execution of the protocol. This intuition is formalized in the proof of the following theorem.

签名 $(r,s)$ 被“绑定”到特定消息 $m$ 上，因为 $r$ 同时是 $I$ 和 $m$ 的函数，改变 $m$ 就会得到完全不同的 $r$。如果把 $H$ 建模为将输入均匀映射到 $\Omega_{pk}$ 上的随机预言机，那么挑战值 $r$ 就是均匀的；直观地说，对（不知道 $sk$ 的）敌手而言，找到消息 $m$ 上的有效签名 $(r,s)$，与在协议的一次诚实执行中冒充证明者同样困难。以下定理的证明将这一直觉形式化。

THEOREM 13.10 Let $\Pi$ be an identification scheme, and let $\Pi^{\prime}$ be the signature scheme that results by applying the Fiat-Shamir transform to it. If $\Pi$ is secure and H is modeled as a random oracle, then $\Pi^{\prime}$ is secure.

定理 13.10　设 $\Pi$ 是一个身份识别方案，$\Pi^{\prime}$ 是对其施加 Fiat–Shamir 变换得到的签名方案。若 $\Pi$ 是安全的且 $H$ 被建模为随机预言机，则 $\Pi^{\prime}$ 是安全的。

PROOF Let $\mathcal{A}^{\prime}$ be a probabilistic polynomial-time adversary attacking the signature scheme $\Pi^{\prime}$, with $q = q(n)$ an upper bound on the number of queries that $\mathcal{A}^{\prime}$ makes to $H$. We make a number of simplifying assumptions without loss of generality. First, we assume that $\mathcal{A}^{\prime}$ makes any given query to $H$ only once. We also assume that after being given a signature $(r, s)$ on a message $m$ with $\mathcal{V}(pk, r, s) = I$, the adversary $\mathcal{A}^{\prime}$ never queries $H(I, m)$ (since it knows the answer will be $r$). Finally, we assume that if $\mathcal{A}^{\prime}$ outputs a forged signature $(r, s)$ on a message $m$ with $\mathcal{V}(pk, r, s) = I$, then $\mathcal{A}^{\prime}$ had previously queried $H(I, m)$.

证明　设 $\mathcal{A}^{\prime}$ 是攻击签名方案 $\Pi^{\prime}$ 的概率多项式时间敌手，$q = q(n)$ 是 $\mathcal{A}^{\prime}$ 向 $H$ 发起查询次数的上界。不失一般性，我们作若干简化假设。首先，假设 $\mathcal{A}^{\prime}$ 对同一个查询只向 $H$ 询问一次。其次，假设在得到消息 $m$ 上的签名 $(r, s)$（其中 $\mathcal{V}(pk, r, s) = I$）之后，敌手 $\mathcal{A}^{\prime}$ 绝不再查询 $H(I, m)$（因为它知道答案就是 $r$）。最后，假设若 $\mathcal{A}^{\prime}$ 输出消息 $m$ 上的伪造签名 $(r, s)$（其中 $\mathcal{V}(pk, r, s) = I$），则 $\mathcal{A}^{\prime}$ 此前已查询过 $H(I, m)$。

We construct an efficient adversary $\mathcal{A}$ that uses $\mathcal{A}^{\prime}$ as a subroutine and attacks the identification scheme $\Pi$:

我们构造一个高效敌手 $\mathcal{A}$，它以 $\mathcal{A}^{\prime}$ 为子程序来攻击身份识别方案 $\Pi$：

**Algorithm $\mathcal{A}$:**

**算法 $\mathcal{A}$：**

The algorithm is given $pk$ and access to an oracle $\mathsf{Trans}_{sk}$.

算法被给予 $pk$ 以及对预言机 $\mathsf{Trans}_{sk}$ 的访问权。

1. Choose uniform $j \in \{1, \ldots, q\}$.

   均匀选取 $j \in \{1, \ldots, q\}$。

2. Run $\mathcal{A}^{\prime}(pk)$. Answer its queries as follows:

   运行 $\mathcal{A}^{\prime}(pk)$。按如下方式回答它的查询：

When $\mathcal{A}^{\prime}$ makes its $i$th random-oracle query $H(I_{i}, m_{i})$, answer it as follows:

当 $\mathcal{A}^{\prime}$ 发起其第 $i$ 次随机预言机查询 $H(I_{i}, m_{i})$ 时，按如下方式回答：

• If $i = j$, output $I_j$ and receive in return a challenge $r$.

• 若 $i = j$，输出 $I_j$，并收到返回的挑战值 $r$。

Return $r$ to $\mathcal{A}^{\prime}$ as the answer to its query.

把 $r$ 返回给 $\mathcal{A}^{\prime}$ 作为其查询的回答。

If $i \neq j$, choose a uniform $r \in \Omega_{pk}$ and return $r$ as the answer to the query.

若 $i \neq j$，均匀选取 $r \in \Omega_{pk}$ 并返回 $r$ 作为该查询的回答。

When $\mathcal{A}^{\prime}$ requests a signature on $m$, answer it as follows:

当 $\mathcal{A}^{\prime}$ 请求 $m$ 上的签名时，按如下方式回答：

(a) Query $\mathsf{Trans}_{sk}$ to obtain a transcript $(I, r, s)$ of an honest execution of the protocol.

(a) 查询 $\mathsf{Trans}_{sk}$，获得协议一次诚实执行的记录 $(I, r, s)$。

(b) Return the signature $(r, s)$

(b) 返回签名 $(r, s)$。

3. If $\mathcal{A}^{\prime}$ outputs a forged signature $(r, s)$ on a message $m$, compute $I := \mathcal{V}(pk, r, s)$ and check whether $(I, m) \overset{?}{=} (I_j, m_j)$. If so, then output $s$. Otherwise, abort.

   若 $\mathcal{A}^{\prime}$ 输出消息 $m$ 上的伪造签名 $(r, s)$，计算 $I := \mathcal{V}(pk, r, s)$ 并检查 $(I, m) \overset{?}{=} (I_j, m_j)$ 是否成立。若成立，则输出 $s$；否则中止。

The view of $\mathcal{A}^{\prime}$ when run as a subroutine by $\mathcal{A}$ in experiment $\mathsf{Ident}_{\mathcal{A},\Pi}(n)$ is almost identical to the view of $\mathcal{A}^{\prime}$ in experiment $\mathsf{Sig-forge}_{\mathcal{A}^{\prime},\Pi^{\prime}}(n)$. Indeed, all the $H$-queries that $\mathcal{A}^{\prime}$ makes are answered with a uniform value from $\Omega_{pk}$, and all the signing queries that $\mathcal{A}^{\prime}$ makes are answered with valid signatures having the correct distribution. The only difference between the views is that when $\mathcal{A}^{\prime}$ is run as a subroutine by $\mathcal{A}$ it is possible for there to be an inconsistency in the answers $\mathcal{A}^{\prime}$ receives from its queries to $H$: specifically, this happens if $\mathcal{A}$ ever answers a signing query for a message $m$ using a transcript $(I,r,s)$ for which $H(I,m)$ is already defined (that is, $\mathcal{A}^{\prime}$ had previously queried $(I,m)$ to $H$) and $H(I,m) \neq r$. However, if $\Pi$ is non-degenerate then this only ever happens with negligible probability. Thus, the probability that $\mathcal{A}^{\prime}$ outputs a forgery when run as a subroutine by $\mathcal{A}$ is $\Pr[\mathsf{Sig-forge}_{\mathcal{A}^{\prime},\Pi^{\prime}}(n)=1] - \mathsf{negl}(n)$ for some negligible function *negl*.

在实验 $\mathsf{Ident}_{\mathcal{A},\Pi}(n)$ 中，$\mathcal{A}^{\prime}$ 作为 $\mathcal{A}$ 的子程序运行时的视图，与 $\mathcal{A}^{\prime}$ 在实验 $\mathsf{Sig-forge}_{\mathcal{A}^{\prime},\Pi^{\prime}}(n)$ 中的视图几乎完全相同。事实上，$\mathcal{A}^{\prime}$ 发起的所有 $H$ 查询都是用 $\Omega_{pk}$ 中均匀选取的值回答的，所有签名查询也都是用具有正确分布的有效签名回答的。两种视图之间唯一的差别在于：当 $\mathcal{A}^{\prime}$ 作为 $\mathcal{A}$ 的子程序运行时，$\mathcal{A}^{\prime}$ 从 $H$ 查询得到的回答有可能出现不一致——具体地说，如果 $\mathcal{A}$ 用某条记录 $(I,r,s)$ 回答关于消息 $m$ 的签名查询，而 $H(I,m)$ 已经被定义过（即 $\mathcal{A}^{\prime}$ 此前曾向 $H$ 查询过 $(I,m)$）且 $H(I,m) \neq r$，就会发生这种情况。然而，若 $\Pi$ 是非退化的，这种情况发生的概率是可忽略的。因此，$\mathcal{A}^{\prime}$ 作为 $\mathcal{A}$ 的子程序运行时输出伪造的概率为 $\Pr[\mathsf{Sig-forge}_{\mathcal{A}^{\prime},\Pi^{\prime}}(n)=1] - \mathsf{negl}(n)$，其中 negl 是某个可忽略函数。

Consider an execution of experiment $\mathsf{Ident}_{\mathcal{A},\Pi}(n)$ in which $\mathcal{A}^{\prime}$ outputs a forged signature $(r,s)$ on a message $m$, and let $I:=\mathcal{V}(pk,r,s)$. Since $j$ is uniform and independent of everything else, the probability that $(I,m)=(I_j,m_j)$ (even conditioned on the event that $\mathcal{A}^{\prime}$ outputs a forgery) is exactly ${1}/q$. (Recall we assume that if $\mathcal{A}^{\prime}$ outputs a forged signature $(r,s)$ on a message $m$ with $\mathcal{V}(pk,r,s)=I$, then $\mathcal{A}^{\prime}$ had previously queried $H(I,m)$. When both events happen, $\mathcal{A}$ successfully impersonates the prover. Indeed, $\mathcal{A}$ sends $I_j$ as its initial message, receives in response a challenge $r$, and responds with $s$. But $H(I_j,m_j)=r$ and (since the forged signature is valid) $\mathcal{V}(pk,r,s)=I$. Putting everything together, we see that

考虑实验 $\mathsf{Ident}_{\mathcal{A},\Pi}(n)$ 的一次执行，其中 $\mathcal{A}^{\prime}$ 输出消息 $m$ 上的伪造签名 $(r,s)$，并令 $I:=\mathcal{V}(pk,r,s)$。由于 $j$ 是均匀的且与其他一切相互独立，$(I,m)=(I_j,m_j)$ 的概率（即使以 $\mathcal{A}^{\prime}$ 输出伪造为条件）恰好是 ${1}/q$。（回想一下，我们假设若 $\mathcal{A}^{\prime}$ 输出消息 $m$ 上的伪造签名 $(r,s)$（其中 $\mathcal{V}(pk,r,s)=I$），则 $\mathcal{A}^{\prime}$ 此前已查询过 $H(I,m)$。当这两个事件同时发生时，$\mathcal{A}$ 就成功地冒充了证明者。事实上，$\mathcal{A}$ 发送 $I_j$ 作为初始消息，收到挑战值 $r$ 作为回应，并以 $s$ 作答。而 $H(I_j,m_j)=r$，且（由于伪造的签名是有效的）$\mathcal{V}(pk,r,s)=I$。综合起来，我们得到

$$\Pr[\mathsf{Ident}_{\mathcal{A},\Pi}(n)=1]\geq\frac{1}{q(n)}\cdot\left(\Pr[\mathsf{Sig-forge}_{\mathcal{A}^{\prime},\Pi^{\prime}}(n)=1]-\mathsf{negl}(n)\right)$$

or

即

$$\Pr[\mathsf{Sig-forge}_{\mathcal{A}^{\prime},\Pi^{\prime}}(n)=1]\leq q(n)\cdot\Pr[\mathsf{Ident}_{\mathcal{A},\Pi}(n)=1]+\mathsf{negl}(n).$$

If $\Pi$ is secure then $\Pr[\mathrm{Ident}_{\mathcal{A},\Pi}(n)=1]$ is negligible; since $q(n)$ is polynomial this implies that $\Pr[\mathrm{Sig-forge}_{\mathcal{A}^{\prime},\Pi^{\prime}}(n)=1]$ is also negligible. Because $\mathcal{A}^{\prime}$ was arbitrary, this means $\Pi^{\prime}$ is secure.

若 $\Pi$ 是安全的，则 $\Pr[\mathrm{Ident}_{\mathcal{A},\Pi}(n)=1]$ 是可忽略的；由于 $q(n)$ 是多项式，这意味着 $\Pr[\mathrm{Sig-forge}_{\mathcal{A}^{\prime},\Pi^{\prime}}(n)=1]$ 也是可忽略的。由于 $\mathcal{A}^{\prime}$ 是任意的，这说明 $\Pi^{\prime}$ 是安全的。

### 13.5.2 The Schnorr Identification/Signature Schemes　Schnorr 身份识别/签名方案

The Schnorr identification scheme is based on hardness of the discrete-logarithm problem. Let $\mathcal{G}$ be a polynomial-time algorithm that takes as input ${1}^n$ and (except possibly with negligible probability) outputs a description of a cyclic group $\mathbb{G}$, its order $q$ (with $\|q\| = n$), and a generator $g$. To generate its keys, the prover runs $\mathcal{G}(1^n)$ to obtain $(\mathbb{G}, q, g)$, chooses a uniform $x \in \mathbb{Z}_q$, and sets $y := g^x$; the public key is $\langle \mathbb{G}, q, g, y \rangle$ and the private key is $x$. To execute the protocol (see Figure 13.2), the prover begins by choosing a uniform $k \in \mathbb{Z}_q$ and setting $I := g^k$; it sends $I$ as the initial message. The verifier chooses and sends a uniform challenge $r \in \mathbb{Z}_q$; in response, the prover computes $s := [rx + k \bmod q]$. The verifier accepts if and only if $g^s \cdot y^{-r} \stackrel{?}{=} I$. Correctness holds because

Schnorr 身份识别方案基于离散对数问题的困难性。设 $\mathcal{G}$ 是一个多项式时间算法，输入 ${1}^n$ 时（除可忽略的概率外）输出一个循环群 $\mathbb{G}$ 的描述、其阶 $q$（满足 $\|q\| = n$）以及一个生成元 $g$。为生成密钥，证明者运行 $\mathcal{G}(1^n)$ 得到 $(\mathbb{G}, q, g)$，均匀选取 $x \in \mathbb{Z}_q$，并置 $y := g^x$；公钥为 $\langle \mathbb{G}, q, g, y \rangle$，私钥为 $x$。执行协议时（见图 13.2），证明者首先均匀选取 $k \in \mathbb{Z}_q$ 并置 $I := g^k$，把 $I$ 作为初始消息发出。验证者选取并发送一个均匀的挑战值 $r \in \mathbb{Z}_q$；作为回应，证明者计算 $s := [rx + k \bmod q]$。验证者接受当且仅当 $g^s \cdot y^{-r} \stackrel{?}{=} I$。正确性成立，因为

$$g^{s}\cdot y^{-r}=g^{r x+k}\cdot(g^{x})^{-r}=g^{k}=I.$$

Note that $I$ is uniform in $\mathbb{G}$, and so the scheme is non-degenerate.

注意，$I$ 在 $\mathbb{G}$ 中是均匀的，因此该方案是非退化的。

Before giving the proof, we provide some high-level intuition. A first important observation is that passive eavesdropping is of no help to the attacker. The reason is that the attacker can simulate transcripts of honest executions on its own, based only on the public key and without knowledge of the private key. To do this, the attacker just reverses the order of the steps: it first chooses uniform and independent $r, s \in \mathbb{Z}_q$ and then sets $I := g^s \cdot y^{-r}$. In an honest transcript $(I, r, s)$, the initial message $I$ is a uniform element of $\mathbb{G}$, the challenge is an independent, uniform element of $\mathbb{Z}_q$, and $s$ is then uniquely determined as $s = \log_g(I \cdot y^r)$.

在给出证明之前，我们先提供一些高层直觉。第一个重要的观察是：被动窃听对攻击者毫无帮助。原因在于，攻击者仅凭公钥、无需知道私钥，就能自行模拟诚实执行的记录。为此，攻击者只需把各步骤的顺序颠倒过来：先均匀且独立地选取 $r, s \in \mathbb{Z}_q$，再置 $I := g^s \cdot y^{-r}$。在诚实的记录 $(I, r, s)$ 中，初始消息 $I$ 是 $\mathbb{G}$ 中的均匀元素，挑战值是 $\mathbb{Z}_q$ 中与 $I$ 独立的均匀元素，而 $s$ 随后被唯一确定为 $s = \log_g(I \cdot y^r)$。

![Image](https://lsky.jerryxue.top/i/2026/08/25/6a8d86ef91c81.jpg)

**FIGURE 13.2: An execution of the Schnorr identification scheme. / 图 13.2：Schnorr 身份识别方案的一次执行。**

Simulated transcripts constructed by an attacker have the same distribution: $r \in \mathbb{Z}_q$ is uniform and, because $s$ is uniform in $\mathbb{Z}_q$ and independent of $r$, we see that $I$ is uniform in $\mathbb{G}$ and independent of $r$. Finally, $s$ is uniquely determined as satisfying the same constraint as before. Due to this, we may effectively assume that when attacking the identification scheme, an attacker does not eavesdrop on honest executions at all.

攻击者构造的模拟记录具有相同的分布：$r \in \mathbb{Z}_q$ 是均匀的，且由于 $s$ 在 $\mathbb{Z}_q$ 中均匀并与 $r$ 独立，可知 $I$ 在 $\mathbb{G}$ 中均匀且与 $r$ 独立；最后，$s$ 被唯一确定，满足与之前相同的约束。正因如此，我们实际上可以假设：攻击者在攻击该身份识别方案时根本不窃听诚实执行。

So, we have reduced to an attacker who gets a public key $y$, sends an initial message $I$, is given in response a uniform challenge $r$, and then must send a response $s$ for which $g^s \cdot y^{-r} = I$. Informally, if an attacker is able to do this with high probability then it must, in particular, be able to compute correct responses $s_1, s_2$ to at least two different challenges $r_1, r_2 \in \mathbb{Z}_q$. Note

于是，问题归结为这样的攻击者：它获得公钥 $y$，发送初始消息 $I$，收到一个均匀的挑战值 $r$，然后必须发送满足 $g^s \cdot y^{-r} = I$ 的响应 $s$。非形式地说，如果攻击者能以高概率做到这一点，那么特别地，它必须能对至少两个不同的挑战值 $r_1, r_2 \in \mathbb{Z}_q$ 计算出正确的响应 $s_1, s_2$。注意

$$g^{s_{1}}\cdot y^{-r_{1}}=I=g^{s_{2}}\cdot y^{-r_{2}},$$

and so $g^{s_1-s_2} = y^{r_1-r_2}$. But this implies that the attacker (who, recall, is able to generate $s_1$ in response to $r_1$, and $s_2$ in response to $r_2$) can implicitly compute the discrete logarithm

于是 $g^{s_1-s_2} = y^{r_1-r_2}$。但这意味着攻击者（回想一下，它能对 $r_1$ 生成响应 $s_1$、对 $r_2$ 生成响应 $s_2$）可以隐式地计算离散对数

$$\log_{g}y=[\left(s_{1}-s_{2}\right)\cdot\left(r_{1}-r_{2}\right)^{-1}\bmod q],$$

contradicting the assumed hardness of the discrete-logarithm problem.

这与离散对数问题被假定的困难性相矛盾。

THEOREM 13.11 If the discrete-logarithm problem is hard relative to G, then the Schnorr identification scheme is secure.

定理 13.11　若离散对数问题相对于 $\mathcal{G}$ 是困难的，则 Schnorr 身份识别方案是安全的。

PROOF Let $\Pi$ denote the Schnorr identification scheme, and let $\mathcal{A}$ be a PPT adversary attacking the scheme. We construct the following PPT algorithm $\mathcal{A}^{\prime}$ solving the discrete-logarithm problem relative to $\mathcal{G}$:

证明　记 $\Pi$ 为 Schnorr 身份识别方案，设 $\mathcal{A}$ 是攻击该方案的概率多项式时间敌手。我们构造下面这个求解相对于 $\mathcal{G}$ 的离散对数问题的概率多项式时间算法 $\mathcal{A}^{\prime}$：

Algorithm A':

算法 A'：

The algorithm is given G, q, g, y as input.

算法以 G, q, g, y 为输入。

1. Run $\mathcal{A}(pk)$, answering all its queries to $\mathsf{Trans}_{sk}$ as described in the intuition given previously.

   运行 $\mathcal{A}(pk)$，按照前面直觉部分所述的方式回答它对 $\mathsf{Trans}_{sk}$ 的所有查询。

2. When $\mathcal{A}$ outputs $I$, choose a uniform $r_1 \in \mathbb{Z}_q$ as the challenge. Give $r_1$ to $\mathcal{A}$, who responds with $s_1$.

   当 $\mathcal{A}$ 输出 $I$ 时，均匀选取 $r_1 \in \mathbb{Z}_q$ 作为挑战值。把 $r_1$ 交给 $\mathcal{A}$，$\mathcal{A}$ 以 $s_1$ 作答。

3. Run $\mathcal{A}(pk)$ a second time (from the beginning), using the same randomness as before except for uniform and independent $r_2 \in \mathbb{Z}_q$. Eventually, $\mathcal{A}$ responds with $s_2$.

   第二次（从头开始）运行 $\mathcal{A}(pk)$，使用与之前相同的随机性，只是挑战值换成均匀且独立的 $r_2 \in \mathbb{Z}_q$。最终，$\mathcal{A}$ 以 $s_2$ 作答。

4. If $g^{s_1} \cdot y^{-r_1} = I$ and $g^{s_2} \cdot y^{-r_2} = I$ and $r_1 \neq r_2$ then output $[(s_1 - s_2) \cdot (r_1 - r_2)^{-1} \mod q]$. Else, output nothing.

   若 $g^{s_1} \cdot y^{-r_1} = I$ 且 $g^{s_2} \cdot y^{-r_2} = I$ 且 $r_1 \neq r_2$，则输出 $[(s_1 - s_2) \cdot (r_1 - r_2)^{-1} \mod q]$；否则不输出任何内容。

Considering a single run of $\mathcal{A}$ as a subroutine of $\mathcal{A}^{\prime}$, let $\omega$ denote the randomness used in that execution except for the challenge itself. So, $\omega$ comprises any randomness used by $\mathcal{G}$, the choice of (unknown) private key $x$, any randomness used by $\mathcal{A}$ itself, and the randomness used by $\mathcal{A}^{\prime}$ when answering queries to $\mathsf{Trans}_{sk}$. Define $V(\omega, r)$ to be equal to 1 if and only if $\mathcal{A}$ correctly responds to challenge $r$ when randomness $\omega$ is used in the rest of the execution. For any fixed $\omega$, define $\delta_\omega \stackrel{\mathrm{def}}{=} \Pr_r[V(\omega, r) = 1];$ having fixed $\omega$, this is the probability over choice of the challenge $r$ that $\mathcal{A}$ responds correctly.

考虑 $\mathcal{A}$ 作为 $\mathcal{A}^{\prime}$ 子程序的单次运行，记 $\omega$ 为该次执行中除挑战值本身以外所用的全部随机性。于是，$\omega$ 包括 $\mathcal{G}$ 所用的任何随机性、（未知的）私钥 $x$ 的选取、$\mathcal{A}$ 自身所用的任何随机性，以及 $\mathcal{A}^{\prime}$ 回答 $\mathsf{Trans}_{sk}$ 查询时所用的随机性。定义 $V(\omega, r)$ 等于 1 当且仅当：在执行其余部分使用随机性 $\omega$ 时，$\mathcal{A}$ 对挑战值 $r$ 给出了正确的响应。对任意固定的 $\omega$，定义 $\delta_\omega \stackrel{\mathrm{def}}{=} \Pr_r[V(\omega, r) = 1]$；固定 $\omega$ 之后，这就是对挑战值 $r$ 的选取而言 $\mathcal{A}$ 正确响应的概率。

Define $\delta(n) \stackrel{\mathrm{def}}{=} \Pr[\mathsf{Ident}_{\mathcal{A},\Pi}(n) = 1]$. Since the simulation of the $\mathsf{Trans}_{sk}$ oracle is perfect, we have

定义 $\delta(n) \stackrel{\mathrm{def}}{=} \Pr[\mathsf{Ident}_{\mathcal{A},\Pi}(n) = 1]$。由于对 $\mathsf{Trans}_{sk}$ 预言机的模拟是完美的，我们有

$$\begin{array}{r}{\delta(n)=\Pr_{\omega,r}[V(\omega,r)=1]=\sum_{\omega}\Pr[\omega]\cdot\delta_{\omega}.}\end{array}$$

Moreover, the intuition preceding the proof shows that $\mathcal{A}^{\prime}$ correctly computes the discrete logarithm of $y$ whenever $\mathcal{A}$ succeeds twice and $r_1 \neq r_2$. Thus:

此外，证明之前的直觉表明：只要 $\mathcal{A}$ 两次都成功且 $r_1 \neq r_2$，$\mathcal{A}^{\prime}$ 就能正确计算 $y$ 的离散对数。于是：

$$\begin{align*}\Pr[\mathsf{DLog}_{\mathcal{A}^{\prime},\mathcal{G}}(n)=1]&=\Pr_{\omega,r_{1},r_{2}}[V(\omega,r_{1})\land V(\omega,r_{2})\land r_{1}\neq r_{2}]\\&\geq\Pr_{\omega,r_{1},r_{2}}[V(\omega,r_{1})\land V(\omega,r_{2})]-\Pr_{\omega,r_{1},r_{2}}[r_{1}=r_{2}]\\&=\sum_{\omega}\Pr[\omega]\cdot(\delta_{\omega})^{2}-1/q\\&\geq\left(\sum_{\omega}\Pr[\omega]\cdot\delta_{\omega}\right)^{2}-1/q\\&=\delta(n)^{2}-1/q,\end{align*}$$

using Jensen’s inequality in the second-to-last step. (Jensen’s inequality says that $\sum_i a_i \cdot b_i^2 \geq (\sum_i a_i)^{-1} \cdot (\sum_i a_i \cdot b_i)^2$ for positive $\{a_i\}$.) If the discrete-logarithm problem is hard relative to $\mathcal{G}$ then $\Pr[\mathsf{DLog}_{\mathcal{A}^{\prime},\mathcal{G}}(n) = 1]$ is negligible. Since ${1}/q$ is negligible (because $\|q\| = n$), this implies that $\delta(n)$ is also negligible, and so $\Pi$ is a secure identification scheme.

其中倒数第二步使用了 Jensen 不等式。（Jensen 不等式是说：对正数 $\{a_i\}$ 有 $\sum_i a_i \cdot b_i^2 \geq (\sum_i a_i)^{-1} \cdot (\sum_i a_i \cdot b_i)^2$。）若离散对数问题相对于 $\mathcal{G}$ 是困难的，则 $\Pr[\mathsf{DLog}_{\mathcal{A}^{\prime},\mathcal{G}}(n) = 1]$ 是可忽略的。由于 ${1}/q$ 是可忽略的（因为 $\|q\| = n$），这意味着 $\delta(n)$ 也是可忽略的，因此 $\Pi$ 是一个安全的身份识别方案。

The Schnorr signature scheme is obtained by applying the Fiat-Shamir transform to the Schnorr identification scheme. See Construction 13.12.

对 Schnorr 身份识别方案施加 Fiat–Shamir 变换，就得到 Schnorr 签名方案。见构造 13.12。

**CONSTRUCTION 13.12**

Let $\mathcal{G}$ be as described in the text.

**构造 13.12**

设 $\mathcal{G}$ 如正文所述。

- Gen: run $\mathcal{G}(1^n)$ to obtain $(\mathbb{G}, q, g)$. Choose a uniform $x \in \mathbb{Z}_q$ and set $y := g^x$. The private key is $x$ and the public key is $(\mathbb{G}, q, g, y)$. As part of key generation, a function $H : \{0,1\}^* \to \mathbb{Z}_q$ is specified, but we leave this implicit.

- Gen：运行 $\mathcal{G}(1^n)$ 得到 $(\mathbb{G}, q, g)$。均匀选取 $x \in \mathbb{Z}_q$ 并置 $y := g^x$。私钥为 $x$，公钥为 $(\mathbb{G}, q, g, y)$。作为密钥生成的一部分，还要指定一个函数 $H : \{0,1\}^* \to \mathbb{Z}_q$，但我们将其隐含不写。

- Sign: on input a private key $x$ and a message $m \in \{0,1\}^*$, choose uniform $k \in \mathbb{Z}_q$ and set $I := g^k$. Then compute $r := H(I,m)$, followed by $s := [rx + k \bmod q]$. Output the signature $(r,s)$.

- Sign：输入私钥 $x$ 与消息 $m \in \{0,1\}^*$ 时，均匀选取 $k \in \mathbb{Z}_q$ 并置 $I := g^k$。然后计算 $r := H(I,m)$，接着计算 $s := [rx + k \bmod q]$。输出签名 $(r,s)$。

- Vrfy: on input a public key $(\mathbb{G}, q, g, y)$, a message $m$, and a signature $(r, s)$, compute $I := g^s \cdot y^{-r}$ and output 1 if $H(I, m) \overset{?}{=} r$.

- Vrfy：输入公钥 $(\mathbb{G}, q, g, y)$、消息 $m$ 与签名 $(r, s)$ 时，计算 $I := g^s \cdot y^{-r}$，若 $H(I, m) \overset{?}{=} r$ 则输出 1。

EdDSA is an efficient, standardized version of Schnorr signatures that uses a specific elliptic-curve group.

EdDSA 是 Schnorr 签名的一个高效的标准化版本，使用特定的椭圆曲线群。

### 13.5.3 DSA and ECDSA　DSA 与 ECDSA

The Digital Signature Algorithm (DSA) and Elliptic Curve Digital Signature Algorithm (ECDSA) are based on the discrete-logarithm problem in different classes of groups. They have been around in some form since 1991, and are both included in the current Digital Signature Standard (DSS) issued by NIST (although in 2019 NIST proposed to deprecate DSA).

数字签名算法（DSA）与椭圆曲线数字签名算法（ECDSA）基于不同种类群中的离散对数问题。它们自 1991 年起就以某种形式存在，并且都被纳入 NIST 发布的现行数字签名标准（DSS）（尽管 NIST 于 2019 年提议弃用 DSA）。

Both schemes follow a common template and can be viewed as being constructed from an underlying identification scheme (see the previous section). Let $\mathbb{G}$ be a cyclic group of prime order $q$ with generator $g$. Consider the following identification scheme in which the prover's private key is $x$ and public key is $(\mathbb{G}, q, g, y)$ with $y = g^x$.

两个方案遵循同一个模板，都可以看作是从某个底层身份识别方案构造出来的（见上一节）。设 $\mathbb{G}$ 是素数阶 $q$ 的循环群，生成元为 $g$。考虑下面这个身份识别方案：证明者的私钥为 $x$，公钥为 $(\mathbb{G}, q, g, y)$，其中 $y = g^x$。

1. The prover chooses uniform $k \in \mathbb{Z}_q^*$ and sends $I := g^k$.

   证明者均匀选取 $k \in \mathbb{Z}_q^*$ 并发送 $I := g^k$。

2. The verifier chooses and sends uniform $\alpha, r \in \mathbb{Z}_q$ as the challenge.

   验证者选取并发送均匀的 $\alpha, r \in \mathbb{Z}_q$ 作为挑战值。

3. The prover sends $s := [k^{-1} \cdot (\alpha + xr) \mod q]$ as the response.

   证明者发送 $s := [k^{-1} \cdot (\alpha + xr) \mod q]$ 作为响应。

4. The verifier accepts if $s \neq 0$ and $g^{\alpha s^{-1}} \cdot y^{rs^{-1}} \stackrel{?}{=} I$.

   若 $s \neq 0$ 且 $g^{\alpha s^{-1}} \cdot y^{rs^{-1}} \stackrel{?}{=} I$，则验证者接受。

Note $s \neq 0$ unless $\alpha = -xr \bmod q$, which occurs with negligible probability. Assuming $s \neq 0$, the inverse $s^{-1} \bmod q$ exists and

注意，除非 $\alpha = -xr \bmod q$（其发生的概率可忽略），否则 $s \neq 0$。假设 $s \neq 0$，则逆元 $s^{-1} \bmod q$ 存在，并且

$$g^{\alpha s^{-1}} \cdot y^{r s^{-1}} = g^{\alpha s^{-1}} \cdot g^{x r s^{-1}} = g^{(\alpha+x r)\cdot s^{-1}} = g^{(\alpha+x r)\cdot k\cdot(\alpha+x r)^{-1}}=I.$$

We thus see that correctness holds with all but negligible probability.

由此可见，除可忽略的概率外，正确性成立。

One can show that this identification scheme is secure if the discrete-logarithm problem is hard relative to $\mathcal{G}$. We merely sketch the argument, assuming familiarity with the results of the previous section. First of all, transcripts of honest executions can be simulated: to do so, simply choose uniform $\alpha, r \in \mathbb{Z}_q$ and $s \in \mathbb{Z}_q^*$, and then set $I := g^{\alpha s^{-1}} \cdot y^{rs^{-1}}$. (This no longer gives a perfect simulation, but it is close enough.) Moreover, if an attacker outputs an initial message $I$ for which it can give correct responses $s_1, s_2 \in \mathbb{Z}_q^*$ to distinct challenges $(\alpha, r_1), (\alpha, r_2)$ then

可以证明，如果离散对数问题相对于 $\mathcal{G}$ 是困难的，那么这个身份识别方案是安全的。假定读者已熟悉上一节的结果，我们这里只概述论证思路。首先，诚实执行的记录是可以模拟的：只需均匀选取 $\alpha, r \in \mathbb{Z}_q$ 和 $s \in \mathbb{Z}_q^*$，然后置 $I := g^{\alpha s^{-1}} \cdot y^{rs^{-1}}$。（这不再是完美的模拟，但已足够接近。）此外，如果攻击者输出一个初始消息 $I$，并且能对不同的挑战值 $(\alpha, r_1), (\alpha, r_2)$ 分别给出正确的响应 $s_1, s_2 \in \mathbb{Z}_q^*$，那么

$$g^{\alpha s_{1}^{-1}}\cdot y^{r_{1}s_{1}^{-1}}=I=g^{\alpha s_{2}^{-1}}\cdot y^{r_{2}s_{2}^{-1}},$$

and so $g^{\alpha(s_{1}^{-1}-s_{2}^{-1})} = y^{r_{1}s_{1}^{-1}-r_{2}s_{2}^{-1}}$ and $\log_{g} y$ can be computed as in the previous section. The same holds if the attacker gives correct responses to distinct challenges $(\alpha_{1}, r), (\alpha_{2}, r)$.

于是 $g^{\alpha(s_{1}^{-1}-s_{2}^{-1})} = y^{r_{1}s_{1}^{-1}-r_{2}s_{2}^{-1}}$，从而可以像上一节那样计算出 $\log_{g} y$。若攻击者能对不同的挑战值 $(\alpha_{1}, r), (\alpha_{2}, r)$ 给出正确响应，结论同样成立。

The DSA/ECDSA signature schemes are constructed by “collapsing” the above identification scheme into a non-interactive algorithm run by the signer. In contrast to the Fiat-Shamir transform, however, the transformation here is carried out as follows (see Construction 13.13):

DSA/ECDSA 签名方案是通过把上述身份识别方案“折叠”成由签名者运行的非交互式算法来构造的。不过，与 Fiat–Shamir 变换不同，这里的转换按如下方式进行（见构造 13.13）：

- Set $\alpha := H(m)$, where $m$ is the message being signed and $H$ is a cryptographic hash function.

- 令 $\alpha := H(m)$，其中 $m$ 是被签名的消息，$H$ 是密码学哈希函数。

- Set $r := F(I)$ for a (specified) function $F : \mathbb{G} \to \mathbb{Z}_q$. Here, $F$ is a “simple” function that is not intended to act like a random oracle.

- 令 $r := F(I)$，其中 $F : \mathbb{G} \to \mathbb{Z}_q$ 是一个（指定的）函数。这里 $F$ 是一个“简单”的函数，并不指望它像随机预言机那样工作。

The function $F$ depends on the group $\mathbb{G}$, which in turn depends on the scheme. In DSA, $\mathbb{G}$ is taken to be an order-$q$ subgroup of $\mathbb{Z}_p^*$, for $p$ prime (cf. Section 9.3.3), and $F(I) \overset{\mathrm{def}}{=} [I \bmod q]$. In ECDSA, $\mathbb{G}$ is an order-$q$ subgroup of an elliptic-curve group $E(\mathbb{Z}_p)$, for $p$ prime.$^4$ Recall from Section 9.3.4 that any element of such a group can be represented as a pair $(x, y) \in \mathbb{Z}_p \times \mathbb{Z}_p$. The function $F$ in this case is defined as $F((x, y)) \overset{\mathrm{def}}{=} [x \bmod q]$.

函数 $F$ 依赖于群 $\mathbb{G}$，而 $\mathbb{G}$ 又取决于具体方案。在 DSA 中，$\mathbb{G}$ 取为 $\mathbb{Z}_p^*$（$p$ 为素数）的 $q$ 阶子群（参见 9.3.3 节），且 $F(I) \overset{\mathrm{def}}{=} [I \bmod q]$。在 ECDSA 中，$\mathbb{G}$ 是椭圆曲线群 $E(\mathbb{Z}_p)$（$p$ 为素数）的 $q$ 阶子群。$^4$ 回忆 9.3.4 节，这种群中的任何元素都可以表示为数对 $(x, y) \in \mathbb{Z}_p \times \mathbb{Z}_p$。此时的函数 $F$ 定义为 $F((x, y)) \overset{\mathrm{def}}{=} [x \bmod q]$。

> $^4$ ECDSA also allows elliptic curves over other fields, but we have only covered the case of prime fields in Section 9.3.4.

> $^4$ ECDSA 也允许其他域上的椭圆曲线，但我们在 9.3.4 节中只介绍了素数域的情形。

**CONSTRUCTION 13.13**

Let $\mathcal{G}$ be as in the text.

**构造 13.13**

设 $\mathcal{G}$ 如正文所述。

Gen: on input ${1}^n$, run $\mathcal{G}(1^n)$ to obtain $(\mathbb{G}, q, g)$. Choose uniform $x \in \mathbb{Z}_q$ and set $y := g^x$. The public key is $\langle \mathbb{G}, q, g, y \rangle$ and the private key is $x$.

Gen：输入 ${1}^n$ 时，运行 $\mathcal{G}(1^n)$ 得到 $(\mathbb{G}, q, g)$。均匀选取 $x \in \mathbb{Z}_q$ 并置 $y := g^x$。公钥为 $\langle \mathbb{G}, q, g, y \rangle$，私钥为 $x$。

As part of key generation, two functions $H: \{0,1\}^* \to \mathbb{Z}_q$ and $F: \mathbb{G} \to \mathbb{Z}_q$ are specified, but we leave this implicit.

作为密钥生成的一部分，还要指定两个函数 $H: \{0,1\}^* \to \mathbb{Z}_q$ 和 $F: \mathbb{G} \to \mathbb{Z}_q$，但我们将其隐含不写。

- Sign: on input the private key $x$ and a message $m \in \{0,1\}^*$, choose uniform $k \in \mathbb{Z}_q^*$ and set $r := F(g^k)$. Then compute $s := [k^{-1} \cdot (H(m) + xr) \mod q]$. (If $r = 0$ or $s = 0$ then start again with a fresh choice of $k$.) Output the signature $(r,s)$.

- Sign：输入私钥 $x$ 与消息 $m \in \{0,1\}^*$ 时，均匀选取 $k \in \mathbb{Z}_q^*$ 并置 $r := F(g^k)$。然后计算 $s := [k^{-1} \cdot (H(m) + xr) \mod q]$。（若 $r = 0$ 或 $s = 0$，则重新选取 $k$ 再来一次。）输出签名 $(r,s)$。

- Vrfy: on input a public key $\langle \mathbb{G}, q, g, y \rangle$, a message $m \in \{0,1\}^*$, and a signature $(r,s)$ with $r,s \neq 0 \bmod q$, output 1 if and only if

- Vrfy：输入公钥 $\langle \mathbb{G}, q, g, y \rangle$、消息 $m \in \{0,1\}^*$ 与签名 $(r,s)$（满足 $r,s \neq 0 \bmod q$）时，输出 1 当且仅当

$$r\stackrel{?}{=}F\left(g^{H(m)\cdot s^{-1}}y^{r\cdot s^{-1}}\right).$$

**DSA and ECDSA—abstractly.**

**DSA 与 ECDSA——抽象描述。**

Assuming hardness of the discrete-logarithm problem, DSA and ECDSA can be proven secure if $H$ and $F$ are modeled as random oracles. As we have discussed above, however, while the random-oracle model may be reasonable for H, it is not an appropriate model for F. No proofs of security are known for the specific choices of F in the standard. Nevertheless, DSA and ECDSA have been used and studied for decades without any attacks being found.

在离散对数问题困难的假设下，如果把 $H$ 和 $F$ 都建模为随机预言机，那么 DSA 和 ECDSA 可以被证明是安全的。然而，正如我们上面讨论过的，随机预言机模型对 $H$ 或许还算合理，对 $F$ 却并不是一个恰当的模型。对于标准中 $F$ 的具体取法，目前尚不知道任何安全性证明。尽管如此，DSA 和 ECDSA 已被使用和研究了数十年，至今未发现任何攻击。

**Proper generation of $k$.**

**正确生成 $k$。**

The DSA/ECDSA schemes specify that the signer should choose a uniform $k \in \mathbb{Z}_q^*$ when computing a signature. Failure to choose $k$ properly (e.g., due to poor random-number generation) can lead to catastrophic results. For starters, if an attacker can predict the value of $k$ used to compute a signature $(r,s)$ on a message $m$, then they can compute the signer's private key. This is true because $s = k^{-1} \cdot (H(m) + xr) \mod q$, and if $k$ is known then the only unknown is the private key $x$.

DSA/ECDSA 方案规定，签名者在计算签名时应均匀选取 $k \in \mathbb{Z}_q^*$。未能正确选取 $k$（例如由于随机数生成质量差）可能导致灾难性后果。首先，如果攻击者能预测用于计算消息 $m$ 上签名 $(r,s)$ 的 $k$ 值，那么它就能计算出签名者的私钥。这是因为 $s = k^{-1} \cdot (H(m) + xr) \mod q$，一旦 $k$ 已知，唯一的未知量就是私钥 $x$。

Even if $k$ is unpredictable, the attacker can compute the signer's private key if the same $k$ is ever used to generate two different signatures. The attacker can easily tell when this happens because then $r$ repeats as well. Say $(r, s_1)$ and $(r, s_2)$ are signatures on messages $m_1$ and $m_2$, respectively. Then

即使 $k$ 不可预测，只要同一个 $k$ 曾被用于生成两个不同的签名，攻击者就能计算出签名者的私钥。攻击者很容易察觉这种情况的发生，因为此时 $r$ 也会重复出现。设 $(r, s_1)$ 和 $(r, s_2)$ 分别是消息 $m_1$ 和 $m_2$ 上的签名。那么

$$\begin{aligned}&s_{1}=k^{-1}\cdot(H(m_{1})+xr)\bmod q\\&s_{2}=k^{-1}\cdot(H(m_{2})+xr)\bmod q.\\ \end{aligned}$$

Subtracting gives $s_1 - s_2 = k^{-1}(H(m_1) - H(m_2)) \bmod q$, from which $k$ can be computed; given $k$, the attacker can determine the private key $x$ as in the previous paragraph. This very attack was used by hackers to extract the master private key from the Sony PlayStation (PS3) in 2010.

两式相减得 $s_1 - s_2 = k^{-1}(H(m_1) - H(m_2)) \bmod q$，由此即可计算出 $k$；有了 $k$，攻击者就能像上一段所述那样确定私钥 $x$。2010 年，黑客正是利用这种攻击从索尼 PlayStation（PS3）中提取出了主私钥。

## 13.6 Certificates and Public-Key Infrastructures　证书与公钥基础设施

In this section we briefly discuss one of the primary applications of digital signatures: the secure distribution of public keys. This brings us full circle in our discussion of public-key cryptography. In this and the previous chapter we have seen how to use public-key cryptography once public keys are securely distributed. Now we show how public-key cryptography itself can be used to securely distribute public keys. This may sound circular, but it is not. What we will show is that once a single public key, belonging to a trusted party, is distributed in a secure fashion, that key can be used to "bootstrap" the secure distribution of arbitrarily many other public keys. Thus, at least in principle, the problem of secure key distribution need only be solved once.

在本节中，我们简要讨论数字签名的主要应用之一：公钥的安全分发。这使我们关于公钥密码学的讨论形成了一个完整的闭环。在本章和上一章中，我们已经看到在公钥被安全分发的前提下如何使用公钥密码学；现在我们要展示公钥密码学本身如何被用来安全地分发公钥。这听起来像是循环论证，但其实不然。我们将展示的是：一旦属于某个可信方的单个公钥以安全的方式被分发出去，这个密钥就可以用来“引导”任意多个其他公钥的安全分发。因此，至少在原则上，密钥安全分发问题只需解决一次。

The key notion here is a digital certificate, which is simply a signature binding an entity to some public key. To be concrete, say a party Charlie has generated keys ($pk_C, sk_C$) for a secure digital signature scheme (in this section, we will only be concerned with signature schemes satisfying Definition 13.2). Assume further that another party Bob has also generated keys ( $pk_B, sk_B$) (in the present discussion, these may be keys for either a signature scheme or a public-key encryption scheme), and that Charlie knows that $pk_B$ is Bob's public key. Then Charlie can compute the signature

这里的关键概念是数字证书，它无非就是把某个实体与某个公钥绑定在一起的一个签名。具体来说，设一方 Charlie 已为某个安全的数字签名方案生成了密钥 ($pk_C, sk_C$)（在本节中，我们只关心满足定义 13.2 的签名方案）。进一步假设另一方 Bob 也已生成密钥 ( $pk_B, sk_B$)（在当前的讨论中，这可以是签名方案的密钥，也可以是公钥加密方案的密钥），且 Charlie 知道 $pk_B$ 是 Bob 的公钥。于是 Charlie 可以计算签名

$$\mathsf{cert}_{C\to B}~{\stackrel{\mathrm{def}}{=}}~\mathsf{Sign}_{sk_C}(\text{``Bob's key is } pk_B\text{''})$$

and give this signature to Bob. We call $\mathsf{cert}_{C \to B}$ a certificate for Bob's key issued by Charlie. In practice a certificate should unambiguously identify the party holding a particular public key and so a more uniquely descriptive term than “Bob” would be used, for example, Bob’s full name and email address, or the URL of Bob’s website.

并把这个签名交给 Bob。我们称 $\mathsf{cert}_{C \to B}$ 是由 Charlie 为 Bob 的密钥签发的证书。在实践中，证书应当无歧义地标识持有特定公钥的一方，因此会使用比“Bob”更具唯一性的标识信息，例如 Bob 的全名和电子邮件地址，或 Bob 网站的 URL。

Now say Bob wants to communicate with some other party Alice who already knows $pk_C$. Bob can send $(pk_B, \mathsf{cert}_{C \to B})$ to Alice, who can then verify that $\mathsf{cert}_{C \to B}$ is indeed a valid signature on the message ‘Bob’s key is $pk_B$, with respect to $pk_C$. Assuming verification succeeds, Alice now knows that Charlie has signed the indicated message. If Alice trusts Charlie, she can accept $pk_B$ as Bob’s legitimate public key.

现在假设 Bob 想与另一方 Alice 通信，而 Alice 已经知道 $pk_C$。Bob 可以把 $(pk_B, \mathsf{cert}_{C \to B})$ 发送给 Alice，Alice 随后可以验证 $\mathsf{cert}_{C \to B}$ 确实是消息“Bob 的密钥是 $pk_B$”关于 $pk_C$ 的有效签名。若验证成功，Alice 便知道 Charlie 已签署了上述消息。如果 Alice 信任 Charlie，她就可以把 $pk_B$ 接受为 Bob 的合法公钥。

All communication between Bob and Alice can occur over an insecure and unauthenticated channel. If an active adversary interferes with the transmission of $(pk_B, \mathsf{cert}_{C \to B})$ from Bob to Alice, that adversary will be unable to generate a valid certificate linking Bob to any other public key $pk^{\prime}_B$ unless Charlie had previously signed some other certificate linking Bob with $pk^{\prime}_B$ (in which case this is anyway not much of an attack). This all assumes that Charlie is not dishonest and that his private key has not been compromised.

Bob 与 Alice 之间的全部通信都可以在不安全、未经认证的信道上进行。如果主动敌手干扰 $(pk_B, \mathsf{cert}_{C \to B})$ 从 Bob 到 Alice 的传输，那么除非 Charlie 此前曾签发过把 Bob 与另一个公钥 $pk^{\prime}_B$ 绑定的其他证书（那样的话这也算不上什么攻击），否则该敌手无法生成把 Bob 与任何其他公钥 $pk^{\prime}_B$ 关联起来的有效证书。这一切都建立在 Charlie 诚实、且其私钥未被泄露的假设之上。

We have omitted many details in the above description. Most prominently, we have not discussed how Alice learns $pk_{C}$ in the first place; how Charlie can be sure that $pk_{B}$ is Bob's public key; and how Alice decides whether to trust Charlie. Fully specifying such details (and others) defines a public-key infrastructure (PKI) that enables the widespread distribution of public keys. A variety of different PKI models have been suggested, and we mention a few of the more popular ones now. Our treatment here will be kept at a relatively high level, and the reader interested in further details is advised to consult the references at the end of this chapter.

上面的描述省略了许多细节。最突出的是，我们没有讨论：Alice 最初是如何获知 $pk_{C}$ 的；Charlie 如何能确信 $pk_{B}$ 是 Bob 的公钥；以及 Alice 如何决定是否信任 Charlie。把这些细节（以及其他细节）完整地规定下来，就定义了一个公钥基础设施（PKI），它使公钥的大规模分发成为可能。人们已提出多种不同的 PKI 模型，我们现在介绍其中较流行的几种。这里的论述将保持在较高的层面上，想进一步了解细节的读者可以参阅本章末尾的参考文献。

**A single certificate authority.**

**单一证书颁发机构。**

The simplest PKI assumes a single certificate authority (CA) who is completely trusted by everybody and who issues certificates for everyone's public key. A certificate authority would not typically be a person, but would more likely be a company whose business it is to certify public keys, a government agency, or perhaps a department within an organization (although in this latter case the CA would likely only be used by people within the organization). Anyone who wants to rely on the services of the CA would have to obtain a legitimate copy of the CA's public key $pk_{CA}$. Clearly, this step must be carried out in a secure fashion since if some party obtains an incorrect version of $pk_{CA}$ then that party may not be able to obtain an authentic copy of anyone else's public key. This means that $pk_{CA}$ must be distributed over an authenticated channel. The easiest way of doing this is via physical means: for example, if the CA is within an organization then any employee can obtain an authentic copy of $pk_{CA}$ directly from the CA on their first day of work. If the CA is a company, then other users would have to go to this company at some point and, say, pick up a USB stick that contains the CA's public key. This inconvenient step need only be carried out once.

最简单的 PKI 假设存在单一的证书颁发机构（CA）：它被所有人完全信任，并为每个人的公钥签发证书。证书颁发机构通常不是个人，而更可能是一家以认证公钥为业务的公司、一个政府机构，或某个组织内部的部门（不过在后一种情形下，该 CA 大概只被组织内部的人使用）。任何想依赖 CA 服务的人都必须获得 CA 公钥 $pk_{CA}$ 的合法副本。显然，这一步必须以安全的方式进行，因为若某方获得了错误的 $pk_{CA}$，它就可能无法获得其他任何方公钥的真实副本。这意味着 $pk_{CA}$ 必须经过认证的信道分发。最简单的做法是借助物理手段：例如，若 CA 在某个组织内部，任何员工都可以在入职第一天直接从 CA 处获得 $pk_{CA}$ 的真实副本。若 CA 是一家公司，那么其他用户就得在某个时候亲自前往该公司，比如领取一个存有 CA 公钥的 U 盘。这个不便的步骤只需进行一次。

A common way for a CA to distribute its public key in practice is to “bundle” this public key with some other software. For example, this occurs today in many popular web browsers: a CA's public key is provided together with the browser, and the browser is programmed to automatically verify certificates as they arrive. (Actually, modern web browsers have public keys of multiple CAs hard-wired into their code, and so more accurately fall into the "multiple CA" model discussed below.)

在实践中，CA 分发其公钥的一种常见方式是把公钥与其他软件“捆绑”在一起。例如，当今许多流行的浏览器就是这样做的：CA 的公钥随浏览器一同提供，浏览器被编程为在收到证书时自动验证它们。（实际上，现代浏览器把多个 CA 的公钥固化在代码中，因此更准确地说是属于下文讨论的“多 CA”模型。）

The mechanism by which a CA issues a certificate to some party Bob must also be very carefully controlled, although the details may vary from CA to CA. As one example, Bob may have to show up in person with a copy of his public key $pk_{B}$ along with identification proving that his name (or his email address) is what he claims. Only then would the CA issue the certificate.

CA 向某方 Bob 签发证书的机制也必须受到非常严格的控制，尽管具体细节可能因 CA 而异。举例来说，Bob 可能需要亲自到场，出示其公钥 $pk_{B}$ 的副本，并附上身份证明，以证实他的名字（或电子邮件地址）确如他所声称的那样。只有这样，CA 才会签发证书。

In the model where there is a single CA, parties completely trust this CA to issue certificates only when appropriate; this is why it is crucial that a detailed verification process be used before a certificate is issued. As a consequence, if Alice receives a certificate $\mathsf{cert}_{CA \to B}$ certifying that $pk_B$ is Bob's public key, Alice will accept this assertion as valid, and use $pk_B$ as Bob's public key.

在单一 CA 模型中，各方完全信任该 CA 只在适当的时候才签发证书；正因如此，在签发证书之前执行详尽的核验流程至关重要。这样一来，如果 Alice 收到证书 $\mathsf{cert}_{CA \to B}$——它证明 $pk_B$ 是 Bob 的公钥——Alice 就会认可这一断言并认定其有效，把 $pk_B$ 当作 Bob 的公钥来使用。

Multiple certificate authorities. While the model in which there is only one CA is simple and appealing, it is not very practical. For one thing, outside of a single organization it is unlikely for everyone to trust the same CA. This need not imply that anyone thinks the CA is corrupt; it could simply be the case that someone finds the CA's verification process to be insufficient (say, the CA asks for only one form of identification when generating a certificate but Alice would prefer that two be used instead). Moreover, the CA is a single point of failure for the entire system. If the CA is corrupt, or can be bribed, or even if the CA is merely lax with the way it protects its private key, the legitimacy of issued certificates may be called into question. It is also inconvenient for all parties who want certificates to have to contact this CA.

**多个证书颁发机构。**

单一 CA 模型虽然简单且有吸引力，但并不太实用。一方面，在单一组织之外，不太可能所有人都信任同一个 CA。这并不意味着有人认为该 CA 腐败——也可能只是有人认为该 CA 的核验流程不够充分（比如说，CA 在生成证书时只要求一种身份证明，而 Alice 希望要求两种）。另一方面，CA 是整个系统的单点故障。如果 CA 腐败、可以被贿赂，甚至哪怕只是 CA 在保护其私钥方面有所松懈，已签发证书的正当性都可能受到质疑。而且，让所有想要证书的各方都必须联系这同一个 CA，也很不方便。

One approach to alleviating these issues is to rely on multiple CAs. A party Bob who wants to obtain a certificate on his public key can choose which CA(s) it wants to issue a certificate, and a party Alice who is presented with a certificate, or even multiple certificates issued by different CAs, can choose which CA's certificates she trusts. There is no harm in having Bob obtain a certificate from more than one CA (apart from some inconvenience and expense for Bob), but Alice must be more careful since the security of her communication is ultimately only as good as the least-secure CA that she trusts. That is, say Alice trusts two CAs $CA_{1}$ and $CA_{2}$, and $CA_{2}$ is corrupted by an adversary. Then, although this adversary will not be able to forge certificates issued by $CA_{1}$, it will be able to issue fake certificates in the name of $CA_{2}$ for any identity/public key of its choice. This is a real problem in current systems. As mentioned earlier, operating systems/web browsers typically come pre-configured with many CAs' public keys, and the default setting is for all these CAs to be treated as equally trustworthy. Essentially any company willing to pay, however, can be included as a CA. So the list of pre-configured CAs includes some reputable, well-established companies along with other, newer companies whose trustworthiness cannot be easily established. It is left to the user to manually configure their settings so as to only accept certificates from CAs the user trusts.

缓解这些问题的一种方法是依赖多个 CA。想要为其公钥获得证书的 Bob 可以选择由哪个（或哪些）CA 来签发证书；而 Alice 面对一份证书（甚至是不同 CA 签发的多份证书）时，则可以选择信任哪个 CA 的证书。Bob 从多个 CA 获取证书并无害处（除了对 Bob 带来一些不便和开销），但 Alice 必须更加谨慎，因为她通信的安全性最终取决于她所信任的 CA 中最不安全的那个。也就是说，设 Alice 信任两个 CA——$CA_{1}$ 和 $CA_{2}$，而 $CA_{2}$ 被敌手腐蚀。那么，尽管该敌手无法伪造 $CA_{1}$ 签发的证书，它却能够以 $CA_{2}$ 的名义为其自选的任何身份/公钥签发假证书。这是当前系统中真实存在的问题。如前所述，操作系统/浏览器通常预置了许多 CA 的公钥，且默认设置是把所有这些 CA 一视同仁地视为可信。然而，基本上任何愿意付费的公司都能被纳入 CA 之列。因此，预置 CA 的名单中既有一些信誉卓著、历史悠久的公司，也有一些较新的、可信度难以确认的公司。只能由用户手动配置相关设置，使其只接受来自自己信任的 CA 的证书。

Delegation and certificate chains. Another approach which alleviates some of the burden on a single CA (but does not address the security concerns of having a single point of failure) is to use certificate chains. We present the idea for certificate chains of length 2, although it is easy to see that everything we say generalizes to chains of arbitrary length.

**委托与证书链。**

另一种能减轻单一 CA 部分负担（但并未解决单点故障带来的安全隐患）的方法是使用证书链。我们以长度为 2 的证书链为例来介绍这一思想，不过不难看出，这里所说的一切都可以推广到任意长度的链。

Say Charlie, acting as a CA, issues a certificate for Bob as in our original discussion. Assume further that Bob's key $pk_{B}$ is a public key for a signature scheme. Bob, in turn, can issue his own certificates for other parties. For example, Bob may issue a certificate for Alice of the form

假设 Charlie 以 CA 的身份按照我们先前的讨论为 Bob 签发了一份证书。再进一步假设 Bob 的密钥 $pk_{B}$ 是某个签名方案的公钥。于是，Bob 又可以为其他各方签发自己的证书。例如，Bob 可能为 Alice 签发如下形式的证书

$$\mathsf{cert}_{B\to A}~{\stackrel{\mathrm{def}}{=}}~\mathsf{Sign}_{sk_B}(\text{``Alice's key is } pk_A\text{''}).$$

Now, if Alice wants to communicate with some fourth party Dave who knows Charlie's public key (but not Bob's), then Alice can send

现在，如果 Alice 想与第四方 Dave 通信，而 Dave 知道 Charlie 的公钥（却不知道 Bob 的公钥），那么 Alice 可以把

$$pk_{A},\mathsf{cert}_{B\to A},pk_{B},\mathsf{cert}_{C\to B},$$

to Dave. What can Dave deduce from this? Well, he can first verify that Charlie, whom he trusts and whose public key is already in his possession, has signed a certificate $\mathsf{cert}_{C \to B}$ indicating that $pk_B$ indeed belongs to someone named Bob. Dave can also verify that this person named Bob has signed a certificate $\mathsf{cert}_{B \to A}$ indicating that $pk_A$ indeed belongs to Alice. If Dave trusts Charlie to issue certificates only to trustworthy people, then Dave may accept $pk_A$ as being the authentic key of Alice.

发给 Dave。Dave 能由此推断出什么？他可以首先验证：他信任的、且其公钥已在他手中的 Charlie，确实签署了证书 $\mathsf{cert}_{C \to B}$，该证书表明 $pk_B$ 确实属于一个名为 Bob 的人。Dave 还可以验证这个名为 Bob 的人签署了证书 $\mathsf{cert}_{B \to A}$，该证书表明 $pk_A$ 确实属于 Alice。如果 Dave 相信 Charlie 只给值得信任的人签发证书，那么 Dave 就可以接受 $pk_A$ 为 Alice 的真实密钥。

We highlight that in this example stronger semantics are associated with a certificate $\mathsf{cert}_{C\to B}$. In our prior discussion, a certificate of this form was only an assertion that Bob holds public key $pk_B$. Now, a certificate asserts that Bob holds public key $pk_B$ and Bob is trusted to issue other certificates. When Charlie signs a certificate for Bob having these stronger semantics, Charlie is, in effect, delegating his ability to issue certificates to Bob. Bob can now act as a proxy for Charlie, issuing certificates on Charlie's behalf.

我们要强调，在这个例子中，与证书 $\mathsf{cert}_{C\to B}$ 相关联的是更强的语义。在先前的讨论中，这种形式的证书只是断言 Bob 持有公钥 $pk_B$；而现在，证书断言 Bob 持有公钥 $pk_B$，并且 Bob 受信任可以去签发其他证书。当 Charlie 为 Bob 签署一份具有这些更强语义的证书时，Charlie 实际上是把自己签发证书的能力委托给了 Bob。此后 Bob 可以充当 Charlie 的代理，代表 Charlie 签发证书。

Coming back to a CA-based PKI, we can imagine one “root” CA and $n$ “second-level” CAs $CA_1, \ldots, CA_n$. The root CA can issue certificates for each of the second-level CAs, who can then in turn issue certificates for other principles holding public keys. This eases the burden on the root CA, and also makes it more convenient for parties to obtain certificates (since they may now contact the second-level CA who is closest to them, for example). On the other hand, managing these second-level CAs may be difficult, and their presence means that there are now more points of attack in the system.

回到基于 CA 的 PKI，我们可以设想一个“根”CA 和 $n$ 个“二级”CA——$CA_1, \ldots, CA_n$。根 CA 可以为每个二级 CA 签发证书，而各二级 CA 进而可以为持有公钥的其他主体签发证书。这减轻了根 CA 的负担，也让各方获取证书更为便利（例如，他们现在可以联系离自己最近的二级 CA）。另一方面，管理这些二级 CA 可能比较困难，而且它们的存在意味着系统中出现了更多的攻击点。

**The “web of trust” model.**

**“信任网”模型。**

The last example of a PKI we will discuss is a fully distributed model, with no central points of trust, called the “web of trust.” A variant of this model is used by the PGP (“Pretty Good Privacy”) email-encryption software for distribution of public keys.

我们要讨论的最后一种 PKI 是一种完全分布式的模型，它没有任何中心化的信任点，称为“信任网”（web of trust）。PGP（“Pretty Good Privacy”）电子邮件加密软件在分发公钥时采用的就是这种模型的一个变体。

In the “web of trust” model, anyone can issue certificates to anyone else and each user has to make their own decision about how much trust to place in certificates issued by other users. As an example of how this might work, say a user Alice is already in possession of public keys $pk_1, pk_2, pk_3$ for some users $C_1, C_2, C_3$. (We discuss below how these public keys might initially be obtained by Alice.) Another user Bob who wants to communicate with Alice might have certificates $\mathsf{cert}_{C_1 \to B}$, $\mathsf{cert}_{C_3 \to B}$, and $\mathsf{cert}_{C_4 \to B}$, and will send these certificates (along with his public key $pk_B$) to Alice. Alice cannot verify $\mathsf{cert}_{C_4 \to B}$ (since she doesn't have $C_4$'s public key), but she can verify the other two certificates. Now she has to decide how much trust she places in $C_1$ and $C_3$. She may decide to accept $pk_B$ if she unequivocally trusts $C_1$, or if she trusts both $C_1$ and $C_3$ to a lesser extent. (She may, for example, consider it likely that either $C_1$ or $C_3$ is corrupt, but consider it unlikely for them both to be corrupt.)

在“信任网”模型中，任何人都可以给任何其他人签发证书，而每个用户必须自行决定对其他用户所签发证书给予多少信任。举一个可能的运作方式为例：设用户 Alice 已经持有某些用户 $C_1, C_2, C_3$ 的公钥 $pk_1, pk_2, pk_3$（我们稍后讨论 Alice 最初如何获得这些公钥）。另一个想与 Alice 通信的用户 Bob 可能持有证书 $\mathsf{cert}_{C_1 \to B}$、$\mathsf{cert}_{C_3 \to B}$ 和 $\mathsf{cert}_{C_4 \to B}$，他会把这些证书（连同他的公钥 $pk_B$）发送给 Alice。Alice 无法验证 $\mathsf{cert}_{C_4 \to B}$（因为她没有 $C_4$ 的公钥），但可以验证另外两份证书。此时她必须决定自己对 $C_1$ 和 $C_3$ 有多少信任。如果她毫无保留地信任 $C_1$，或者对 $C_1$ 和 $C_3$ 都有较低程度的信任，她就可能决定接受 $pk_B$。（例如，她可能认为 $C_1$ 或 $C_3$ 中有一人被腐蚀是有可能的，但两人同时被腐蚀则不太可能。）

In this model, as described, users are expected to collect both public keys of other parties, as well as certificates on their own public key. In the context of PGP, this used to be done at “key-signing parties” where PGP users got together (say, at a conference), gave each other authentic copies of their public keys, and issued certificates for each other. In general the users at a key-signing party may not know each other, but they can check a driver’s license, say, before accepting or issuing a certificate for someone’s public key.

按照上述描述，在这种模型中，用户既要收集其他各方的公钥，也要收集针对自己公钥的证书。就 PGP 而言，过去人们通过“密钥签名聚会”（key-signing party）来完成这件事：PGP 用户聚在一起（比如在一次会议上），互相交换各自公钥的真实副本，并互相为对方签发证书。一般而言，参加密钥签名聚会的用户彼此可能并不相识，但在接受或为某人的公钥签发证书之前，他们可以查验对方的驾照等证件。

Public keys and certificates can also be stored in a central database, and this is done for PGP (see http://pgp.mit.edu). When Alice wants to send an encrypted message to Bob, she can search for Bob's public key in this database; along with Bob's public key, the database will return a list of all certificates it holds that have been issued for Bob's public key. It is also possible that multiple public keys for Bob will be found in the database, and each of these public keys may be certified by certificates issued by a different set of parties. Once again, Alice then needs to decide how much trust to place in any of these public keys before using them.

公钥和证书也可以存放在一个中央数据库中，PGP 正是这么做的（见 http://pgp.mit.edu）。当 Alice 想给 Bob 发送加密消息时，她可以在这个数据库中搜索 Bob 的公钥；数据库除了返回 Bob 的公钥之外，还会返回它所保存的、为 Bob 公钥签发的全部证书的列表。数据库中也可能找到 Bob 的多个不同公钥，而且其中每个公钥可能由不同的一组主体所签发的证书来认证。同样，Alice 在使用其中任何一个公钥之前，都需要决定对其信任多少。

The web of trust model is attractive because it does not require trust in any central authority. On the other hand, while it may work well for the average user encrypting their email, it does not seem appropriate for settings where security is more critical, or for the distribution of organizational public keys (e.g., for e-commerce on the web). If a user wants to communicate with his bank, for example, it is unlikely that he would trust people he met at a conference to certify his bank's public key, and also unlikely that a bank representative will go to a key-signing party to get the bank's key certified.

信任网模型的吸引力在于它不要求信任任何中央机构。然而，尽管它对加密自己电子邮件的普通用户来说可能效果不错，但对于安全性更为关键的场合，或对于组织公钥的分发（例如网络上的电子商务）而言，它似乎并不合适。例如，一个用户想与自己的银行通信时，他不太可能信任在会议上结识的人去认证银行的公钥；同样，银行的代表也不太可能去参加密钥签名聚会来为银行的密钥获得认证。

### Invalidating Certificates　使证书失效

One important issue we have not yet touched upon at all is the fact that certificates should generally not be valid indefinitely. An employee may leave a company, in which case he or she is no longer allowed to receive encrypted communication from others within the company; a user's private key might also be stolen, at which point the user (assuming they know about the theft) will want to generate a new set of public/private keys and remove the old public key from circulation. In either of these scenarios, we need a way to render previously issued certificates invalid.

我们至今完全没有触及的一个重要问题是：证书一般不应无限期地有效。员工可能离开公司，此时他/她就不再被允许接收公司内部其他人的加密通信；用户的私钥也可能被盗，此时该用户（假如知晓失窃一事）会希望生成一套新的公钥/私钥，并让旧公钥停止流通。无论哪种情形，我们都需要一种办法使先前签发的证书失效。

Approaches for handling these issues are varied and complex, and we will only mention two relatively simple ideas that, in some sense, represent opposite extremes. (Improving these methods is an active area of real-world network-security research.)

处理这些问题的方法多种多样且相当复杂，这里只提及两种相对简单的想法，它们在某种意义上代表了两个极端。（改进这些方法是现实世界网络安全研究中一个活跃的方向。）

Expiration. One method for preventing certificates from being used indefinitely is to include an expiry date as part of the certificate. A certificate issued by a CA Charlie for Bob's public key might now have the form

**有效期。**

防止证书被无限期使用的一种方法是在证书中加入失效日期。由 CA Charlie 为 Bob 公钥签发的证书现在可以形如

$$\mathsf{cert}_{C\to B}\stackrel{\mathrm{def}}{=}\mathsf{Sign}_{sk_C}(\text{``Bob's key is } pk_B\text{''}, \text{date}),$$

where date is some date in the future at which point the certificate becomes invalid. (For example, one year from the day the certificate is issued.) When another user verifies this certificate, they need to know not only $pk_{B}$ but also the expiry date, and they now need to check not only that the signature is valid, but also that the expiry date has not passed. A user who holds a certificate must contact the CA to get a new certificate issued whenever their current one expires; at this point, the CA verifies the identity/credentials of the user again before issuing another certificate.

其中 date 是未来的某个日期，届时证书即告失效。（例如，自签发之日起一年。）其他用户验证这份证书时，不仅需要知道 $pk_{B}$，还需要知道失效日期；他们此时不仅要检查签名是否有效，还要检查失效日期是否已过。持有证书的用户必须在当前证书到期时联系 CA 换发新证书；届时，CA 会再次核验用户的身份/凭证，然后才签发新证书。

Using expiry dates provides a very coarse-grained solution to the problems mentioned earlier. If an employee leaves a company the day after getting a certificate, and the certificate expires one year after its issuance date, then this employee can use his or her public key illegitimately for an entire year until the expiry date passes. For this reason, this approach is typically used in conjunction with other methods such as the one we describe next.

使用失效日期为前面提到的问题提供了一种非常粗粒度的解决方案。如果一名员工在拿到证书的第二天就离开公司，而证书要到签发一年后才失效，那么这名员工就可以不正当地使用其公钥长达一整年，直至失效日期过去。因此，这种方法通常与下文介绍的其他方法配合使用。

Revocation. When an employee leaves an organization, or a user's private key is stolen, we would like the certificates that have been issued for their public keys to become invalid immediately, or at least as soon as possible. This can be achieved by having the CA explicitly revoke the certificate. For simplicity we assume a single CA, but everything we say applies more generally if the user had certificates issued by multiple CAs.

**吊销。**

当员工离开组织，或用户的私钥被盗时，我们希望为其公钥签发的证书立即失效，或至少尽快失效。这可以通过让 CA 显式吊销证书来实现。为简单起见，我们假设只有一个 CA，但我们所说的一切在用户持有多份由不同 CA 签发的证书的一般情形下同样适用。

There are many different ways revocation can be handled. One possibility (the only one we will discuss) is for the CA to include a serial number in every certificate it issues; that is, a certificate will now have the form

处理吊销的方式有很多种。一种可能性（也是我们将要讨论的唯一一种）是让 CA 在其签发的每份证书中都包含一个序列号；也就是说，证书现在形如

$$\mathsf{cert}_{C\to B}\overset{\operatorname{def}}{=}\mathsf{Sign}_{sk_C}(\text{``Bob's key is } pk_B\text{''}, \#\#\#),$$

where “###” represents the serial number of this certificate. Each certificate should have a unique serial number, and the CA will store the information (Bob, $pk_B$, ####) for each certificate it generates.

其中 “###” 代表该证书的序列号。每份证书都应有唯一的序列号，并且 CA 会为自己生成的每份证书存储信息 (Bob, $pk_B$, ####)。

If a user Bob's private key corresponding to a public key $pk_{B}$ is stolen, Bob can alert the CA to this fact. (The CA must verify Bob's identity here,
to prevent another user from falsely revoking a certificate issued to Bob.) The CA will then search its database to find the serial number associated with the certificate issued for Bob and $pk_{B}$. At the end of each day, say, the CA will then generate a certificate revocation list (CRL) with the serial numbers of all revoked certificates, and sign the CRL and the current date. The signed CRL is then widely distributed or otherwise made available to potential verifiers. Verification of a certificate now requires checking that the signature in the certificate is valid, checking that the serial number does not appear on the most current revocation list, and verifying the CA's signature on the revocation list itself.

如果持有公钥 $pk_{B}$ 的用户 Bob 的对应私钥被盗，Bob 可以把这件事告知 CA。（此时 CA 必须核验 Bob 的身份，以防其他用户虚假吊销发给 Bob 的证书。）随后，CA 会检索自己的数据库，找出与为 Bob 和 $pk_{B}$ 签发的证书相关联的序列号。比如说，每天结束时，CA 会生成一份列有所有已吊销证书序列号的证书吊销列表（CRL），并对该 CRL 和当前日期进行签名。签名后的 CRL 随后被广泛分发，或以其他方式提供给潜在的验证者。此后，验证一份证书需要：检查证书中的签名是否有效；检查该序列号没有出现在最新的吊销列表上；以及验证 CA 在吊销列表本身上的签名。

In this approach the way we have described it, there is a gap of at most one day before a certificate becomes invalid. This offers more flexibility than an approach based only on expiry dates.

在我们所描述的这种方法下，从证书被吊销到失效之间最多有一天的间隔。与仅依赖失效日期的方法相比，这提供了更大的灵活性。

## 13.7 Putting It All Together – TLS　综合运用——TLS

The Transport Layer Security (TLS) protocol is used by your web browser every time you securely connect to a website using https. TLS is a standardized protocol based on a precursor called SSL (or Secure Sockets Layer) that was developed by Netscape in the mid-1990s. TLS version 1.0 was released in 1999, and then updated to version 1.1 in 2006, version 1.2 in 2008, and version 1.3 (the current version) in 2018. In this section, we describe the "cryptographic core" of the TLS protocol; this serves as a nice culmination of everything we have covered in the book so far, and also demonstrates the real-world applicability of what we have learned. Our description corresponds roughly to TLS 1.3 but, as usual, we have slightly simplified and abstracted parts of the protocol in order to convey the main point, and our description should not be relied upon for an implementation. (The actual protocol is more complex, and also includes several other interesting features that are outside the scope of this book.) We do not formally define or prove security of the protocol; this is a topic of active research.

传输层安全（TLS）协议在你的浏览器每次使用 https 安全连接到某个网站时都会被用到。TLS 是一个标准化协议，其前身是由 Netscape 在 20 世纪 90 年代中期开发的 SSL（安全套接字层）。TLS 1.0 版于 1999 年发布，随后于 2006 年更新为 1.1 版、2008 年更新为 1.2 版、2018 年更新为 1.3 版（即当前版本）。本节描述 TLS 协议的“密码学核心”；这是对迄今为止本书所学内容的一次很好的综合运用，同时也展示了我们所学知识在现实世界中的适用性。我们的描述大致对应 TLS 1.3，但照例我们对协议的部分内容做了简化和抽象以便传达要点，因此切不可依据这里的描述去做实现。（实际协议更为复杂，还包含若干超出本书范围的其他有趣特性。）我们不正式定义或证明该协议的安全性；这是一个活跃的研究课题。

The TLS protocol allows a client (e.g., a web browser) and a server (e.g., a website) to agree on a set of shared keys and then use those keys to encrypt and authenticate their subsequent communication. It consists of two parts: a handshake protocol that performs (authenticated) key exchange to establish the shared keys, and a record-layer protocol that uses those shared keys to encrypt/authenticate the parties' communication. Although TLS allows for clients to authenticate to servers, it is primarily used only for authentication of servers to clients because typically only servers have certificates. (After a TLS session is established, client-to-server authentication—if desired—can be done at the application layer by, e.g., having the client send a password.)

TLS 协议允许客户端（如浏览器）与服务器（如网站）就一组共享密钥达成一致，然后用这些密钥对其后续通信进行加密和认证。它由两部分组成：握手协议（handshake protocol），执行（经认证的）密钥交换以建立共享密钥；记录层协议（record-layer protocol），使用这些共享密钥对各方的通信进行加密/认证。虽然 TLS 允许客户端向服务器认证身份，但它主要只用于服务器向客户端的认证，因为通常只有服务器才拥有证书。（在 TLS 会话建立之后，如果需要客户端到服务器的认证，可以在应用层完成，例如由客户端发送口令。）

**The handshake protocol.**

**握手协议。**

We describe the basic flow of the handshake protocol in the most typical case. At the outset, the client $C$ holds a set of CAs' public keys $\{pk_1, \ldots, pk_n\}$, and the server $S$ holds keys $(pk_S, sk_S)$ for a digital signature scheme along with a certificate $\mathsf{cert}_{i \to S}$ on $pk_S$ issued by one of the CAs whose public key $C$ knows. The parties run the following steps.

我们描述最典型情形下握手协议的基本流程。一开始，客户端 $C$ 持有一组 CA 的公钥 $\{pk_1, \ldots, pk_n\}$；服务器 $S$ 持有某个数字签名方案的密钥 $(pk_S, sk_S)$，以及由 $C$ 知道其公钥的某个 CA 在 $pk_S$ 上签发的证书 $\mathsf{cert}_{i \to S}$。双方执行以下步骤。

1. $C$ begins by sending to $S$ the initial message of the Diffie–Hellman key-exchange protocol (cf. Section 11.3). This message includes a specification of the underlying group $\mathbb{G}$ being used by the client (along with the group order $q$ and a generator $g$), as well as the value $g^x$ for a random secret value $x$ chosen by the client. The underlying group is selected by the client from a set of standardized options, and can be either a prime-order subgroup of $\mathbb{Z}_p^*$ for some prime $p$ or an elliptic-curve group. The client also sends a uniform value (a “nonce”) $N_C \in \{0,1\}^n$.

   $C$ 首先向 $S$ 发送 Diffie–Hellman 密钥交换协议（参见 11.3 节）的初始消息。这条消息包括客户端所选底层群 $\mathbb{G}$ 的规格说明（连同群的阶 $q$ 与生成元 $g$），以及客户端所选随机秘密值 $x$ 对应的值 $g^x$。底层群由客户端从一组标准化选项中选取，可以是某个素数 $p$ 对应的 $\mathbb{Z}_p^*$ 的素数阶子群，也可以是一个椭圆曲线群。客户端还会发送一个均匀选取的值（即“随机数”，nonce）$N_C \in \{0,1\}^n$。

This message from $C$ also includes information about which cryptographic algorithms (or ciphersuites) are supported by the client.

   这条来自 $C$ 的消息还包括客户端支持哪些密码算法（或密码套件，ciphersuite）的信息。

2. $S$ completes the Diffie–Hellman key exchange by sending a message to the client containing $g^y$ for a random secret value $y$ chosen by the server. The server also includes its own uniform value $N_S \in \{0,1\}^n$.

   $S$ 向客户端发送一条包含 $g^y$ 的消息来完成 Diffie–Hellman 密钥交换，其中 $y$ 是服务器选取的一个随机秘密值。服务器还会附上自己均匀选取的值 $N_S \in \{0,1\}^n$。

At this point, $S$ can compute a shared secret $K = g^{xy}$. It applies a key-derivation function (cf. Section 6.6.4) to $K$ to derive keys $k^{\prime}_S, k^{\prime}_C, k_S, k_C$ for an authenticated encryption (AE) scheme. Supported AE schemes include GCM, CCM, and ChaCha20-Poly1305 (cf. Section 5.3.2).

   此时，$S$ 可以计算出共享秘密 $K = g^{xy}$。它把一个密钥派生函数（参见 6.6.4 节）作用于 $K$，为认证加密（AE）方案推导出密钥 $k^{\prime}_S, k^{\prime}_C, k_S, k_C$。所支持的 AE 方案包括 GCM、CCM 和 ChaCha20-Poly1305（参见 5.3.2 节）。

Finally, $S$ sends its public key $pk_S$ and its certificate $\mathsf{cert}_{i\to S}$, along with a signature $\sigma$ computed by the server (using its long-term key $sk_S$) on the handshake messages exchanged thus far. These values sent by the server are all encrypted using $k^{\prime}_S$.

   最后，$S$ 发送自己的公钥 $pk_S$ 和证书 $\mathsf{cert}_{i\to S}$，以及一个签名 $\sigma$——它是服务器（使用其长期密钥 $sk_S$）对迄今交换的握手消息计算的签名。服务器发送的这些值全部用 $k^{\prime}_S$ 加密。

3. C computes $K$ from the server's response, and also derives the keys $k_{S}^{\prime}$, $k_{C}^{\prime}$, $k_{S}$, and $k_{C}$. It uses $k_{S}^{\prime}$ to recover $pk_{S}$ and the associated certificate, as well as the signature $\sigma$. The client checks whether one of the CA's public keys that it holds matches the CA who issued $S$'s certificate. If so, $C$ verifies the certificate (and also checks that it has not expired or been revoked) and, if this was successful, learns that $pk_{S}$ is indeed $S$'s public key. $C$ then verifies the signature $\sigma$ on the handshake messages with respect to $pk_{S}$, and aborts if verification fails.

   C 由服务器的响应计算出 $K$，同样推导出密钥 $k_{S}^{\prime}$、$k_{C}^{\prime}$、$k_{S}$ 和 $k_{C}$。它用 $k_{S}^{\prime}$ 恢复出 $pk_{S}$ 及相应的证书，还有签名 $\sigma$。客户端检查自己持有的某个 CA 公钥是否与签发 $S$ 证书的那个 CA 相匹配。若匹配，$C$ 就验证该证书（同时检查它没有过期、也没有被吊销）；如果验证成功，则得知 $pk_{S}$ 确实是 $S$ 的公钥。接着，$C$ 关于 $pk_{S}$ 验证握手消息上的签名 $\sigma$，若验证失败则中止。

Finally, $C$ computes a MAC of the handshake messages exchanged thus far using $k^{\prime}_{C}$. It sends the result back to $S$, who verifies the tag before proceeding to the record-layer protocol.

   最后，$C$ 用 $k^{\prime}_{C}$ 计算迄今所交换握手消息的 MAC，并把结果发回给 $S$；$S$ 在进入记录层协议之前先验证该标签。

At the end of the handshake protocol, $C$ and $S$ share session keys $k_C$ and $k_S$ that they can use to encrypt and authenticate their subsequent communication. (The keys $k^{\prime}_C$, $k^{\prime}_S$ are only used for the handshake.)

握手协议结束时，$C$ 与 $S$ 共享会话密钥 $k_C$ 和 $k_S$，可以用它们对其后续通信进行加密和认证。（密钥 $k^{\prime}_C$、$k^{\prime}_S$ 只用于握手过程。）

As some intuition for why the handshake protocol is secure, note first that since $C$ verifies the certificate, it knows that $pk_S$ is the correct public key of the intended server. If the signature $\sigma$ is valid, then $C$ knows it must be communicating with the server because only someone with knowledge of the associated secret key $sk_S$ could have generated a valid signature. (It is important here that the handshake messages being signed have high entropy, so as to prevent a replay attack. This is why the client includes a random nonce $N_C$ as part of its initial message.) Moreover, since the server signs all the messages of the Diffie–Hellman key-exchange protocol, $C$ knows that none of those values were modified in transit as would be the case if an active adversary were carrying out a man-in-the-middle attack (see Section 11.3). Of course, the Diffie–Hellman protocol itself ensures that a passive eavesdropper learns nothing about $K$ (and hence nothing about the derived keys) from the messages exchanged. In summary, then, by the end of the handshake phase $C$ knows that it shares keys $k_C, k_S$ with the legitimate $S$, and that no adversary could have learned anything about those keys.

关于握手协议为何安全，可以先给出如下直觉：由于 $C$ 验证了证书，它知道 $pk_S$ 是目标服务器的正确公钥。如果签名 $\sigma$ 有效，那么 $C$ 就知道与自己通信的一定是那台服务器，因为只有知道相应私钥 $sk_S$ 的人才能生成有效签名。（这里很重要的一点是，被签名的握手消息必须具有高熵，以防止重放攻击。这正是客户端在其初始消息中包含随机数 $N_C$ 的原因。）此外，由于服务器对 Diffie–Hellman 密钥交换协议的所有消息都进行了签名，$C$ 知道这些值没有一个在传输中被篡改——而若主动敌手正在实施中间人攻击，就会出现这种篡改（见 11.3 节）。当然，Diffie–Hellman 协议本身就保证了被动窃听者无法从交换的消息中获知关于 $K$ 的任何信息（因而也无法获知关于所推导密钥的任何信息）。总而言之，到握手阶段结束时，$C$ 知道自己与合法的 $S$ 共享密钥 $k_C, k_S$，并且没有任何敌手能获知关于这些密钥的任何信息。

TLS version 1.2 provided a variant that allowed $C$ and $S$ to agree on shared keys using public-key encryption instead of Diffie–Hellman key exchange. In that variant, the server's long-term keys ( $pk_S$, $sk_S$) corresponded to a public-key encryption scheme, and the client simply chose a key K and encrypted it using $pk_S$. (Several other aspects of the protocol were also different, and in particular the client verified the certificate on the server's public key before encryption was done.) This variant was purposefully eliminated in version 1.3 due to the desire to ensure forward secrecy, i.e., secrecy of previous session keys in the event of a server compromise. Diffie–Hellman key exchange provides forward secrecy since the server's "ephemeral" secret value $y$ used in the handshake protocol can be erased once the handshake is finished; without $y$ an eavesdropper has no way to recover $K$. On the other hand, using public-key encryption as just described does not provide forward secrecy since the server's long-term secret key $sk_S$ cannot be erased; if an adversary obtains it, then it can decrypt ciphertexts from past executions of the handshake protocol and recover the session keys used by the parties involved.

TLS 1.2 版提供了一种变体，允许 $C$ 和 $S$ 使用公钥加密而非 Diffie–Hellman 密钥交换来商定共享密钥。在那个变体中，服务器的长期密钥 $(pk_S, sk_S)$ 对应于一个公钥加密方案，客户端只需选取一个密钥 K 并用 $pk_S$ 加密它。（该协议的其他若干方面也有所不同，特别是客户端会在加密之前验证服务器公钥上的证书。）出于确保前向安全的考虑——即在服务器被攻破的情况下先前会话密钥仍然保密——这个变体在 1.3 版中被有意移除。Diffie–Hellman 密钥交换能够提供前向安全，因为握手中使用的服务器“临时”秘密值 $y$ 可以在握手结束后被擦除；没有 $y$，窃听者就无法恢复 $K$。相反，如上所述使用公钥加密则不提供前向安全，因为服务器的长期私钥 $sk_S$ 无法被擦除；一旦敌手获得它，就能解密过去各次握手协议执行中产生的密文，从而恢复有关各方使用的会话密钥。

**The record-layer protocol.**

**记录层协议。**

Once keys have been agreed upon by $C$ and $S$, the parties use those keys to encrypt and authenticate all their subsequent communication using an AE scheme. $C$ uses $k_{C}$ for the messages it sends to $S$, whereas $S$ uses $k_{S}$ for the messages it sends to $C$. Sequence numbers are used to prevent replay attacks, as discussed in Section 5.4.

一旦 $C$ 和 $S$ 商定了密钥，双方就用这些密钥并通过某个 AE 方案对其后续的全部通信进行加密和认证。$C$ 用 $k_{C}$ 保护它发送给 $S$ 的消息，而 $S$ 用 $k_{S}$ 保护它发送给 $C$ 的消息。如 5.4 节所讨论的，序号被用来防止重放攻击。

## 13.8 \*Signcryption　签密

To close this chapter, we briefly and informally discuss the issue of joint secrecy and integrity in the public-key setting. While this parallels our treatment from Section 5.2, the fact that we are now in the public-key setting introduces several additional complications.

作为本章的收尾，我们简要而非形式化地讨论公钥场景中保密性与完整性的联合处理问题。虽然这与我们在 5.2 节的处理方式类似，但如今身处公钥场景这一事实带来了若干额外的复杂因素。

We consider a setting in which all relevant parties have public/private keys for both encrypting and signing. We let $(ek, dk)$ denote a (public) encryption key and (private) decryption key, and use $(vk, sk)$ for a (public) verification key and (private) signing key. We assume all parties know all public keys.

我们考虑这样一个场景：所有相关方都同时拥有用于加密和签名的公钥/私钥。我们用 $(ek, dk)$ 表示（公开的）加密密钥和（私有的）解密密钥，用 $(vk, sk)$ 表示（公开的）验证密钥和（私有的）签名密钥。假设所有各方都知道所有的公钥。

Informally, our goal is to design a mechanism that allows a sender $S$ to send a message $m$ to a receiver $R$ while ensuring that (1) no other party in the network can learn any information about $m$ (i.e., secrecy) and (2) $R$ is assured that the message came from $S$ (i.e., integrity). We consider both of these security properties even against active (e.g., chosen-ciphertext) attacks by other parties in the system.

非形式地说，我们的目标是设计一种机制，使发送方 $S$ 能够把消息 $m$ 发送给接收方 $R$，同时保证：(1) 网络中的其他任何一方都无法获知关于 $m$ 的任何信息（即保密性）；(2) $R$ 能确信消息来自 $S$（即完整性）。即使面对系统中其他方发起的主动（例如选择密文）攻击，我们也要求这两个安全性质成立。

Following our discussion in Section 5.2, a natural idea is to use an “encryption-authenticate” approach in which $S$ sends $\langle S, c, \mathsf{Sign}_{sk_S}(c) \rangle$ to $R$, where $c$ is an encryption of $m$ using $R$’s encryption key $ek_R$. (We explicitly include the sender’s identity here for convenience.) However, there is a clever chosen-ciphertext attack here regardless of the encryption scheme used. Having observed a transmission as above, another (adversarial) party $A$ can strip off $S$’s signature and replace it with its own, sending $\langle A, c, \mathsf{Sign}_{sk_A}(c) \rangle$ to $R$. In this case, $R$ would not detect anything wrong, and would mistakenly think that $A$ has sent it the message $m$. If $R$ replies to $A$, or otherwise behaves toward $A$ in a way that depends on the contents of the message, then $A$ can potentially learn the unknown message $m$.

按照 5.2 节的讨论，一个自然的想法是采用“先加密后认证”的方法：$S$ 把 $\langle S, c, \mathsf{Sign}_{sk_S}(c) \rangle$ 发送给 $R$，其中 $c$ 是用 $R$ 的加密密钥 $ek_R$ 对 $m$ 加密的结果。（为方便起见，我们在这里显式地写出发送方的身份。）然而，无论使用何种加密方案，这里都存在一种巧妙的选择密文攻击。观察到如上所述的那次传输之后，另一个（恶意的）方 $A$ 可以剥掉 $S$ 的签名并换上自己的签名，把 $\langle A, c, \mathsf{Sign}_{sk_A}(c) \rangle$ 发送给 $R$。这种情况下，$R$ 察觉不到任何异常，会误以为是 $A$ 给它发了消息 $m$。如果 $R$ 回复 $A$，或以其他任何依赖于消息内容的方式对待 $A$，那么 $A$ 就有可能得知未知消息 $m$。

(Another problem with this scheme, although somewhat independent of our discussion here, is that it no longer provides non-repudiation. That is, $R$ cannot easily prove to a third party that $S$ has signed the message $m$, at least not without divulging its own decryption key $dk_{R}$.)

（这个方案的另一个问题——尽管与我们这里的讨论多少有些独立——是它不再提供不可否认性。也就是说，$R$ 无法轻易向第三方证明 $S$ 签署了消息 $m$，至少在不泄露自己的解密密钥 $dk_{R}$ 的情况下做不到。）

One could instead try an “authenticate-then-encrypt” approach. Here, $S$ would first compute a signature $\sigma \leftarrow \mathsf{Sign}_{sk_S}(m)$ and then send

另一种做法是尝试“先认证后加密”的方法。此时，$S$ 会先计算签名 $\sigma \leftarrow \mathsf{Sign}_{sk_S}(m)$，然后发送

$$\langle S,\mathsf{Enc}_{ek_{R}}(m\|\sigma)\rangle.$$

(Note that this solves the non-repudiation issue mentioned above.) If the encryption scheme is only CPA-secure then problems just like those mentioned in Section 5.2 apply, so let us assume a CCA-secure encryption scheme is used instead. Even then, there is an attack that can be carried out by a malicious $R$. Upon receiving $\langle S, \mathsf{Enc}_{ek_R}(m\|\sigma)\rangle$ from $S$, a malicious $R$ can decrypt to obtain $m\|\sigma$, and then re-encrypt and send $\langle S, \mathsf{Enc}_{ek_{R^{\prime}}}(m\|\sigma)\rangle$ to another receiver $R^{\prime}$. This (honest) receiver $R^{\prime}$ will then think that $S$ sent it the message $m$. This can have serious consequences, e.g., if $m$ is the message “I owe you \$100.”

（注意，这解决了上面提到的不可否认性问题。）如果加密方案只有 CPA 安全性，那么与 5.2 节所提到的类似问题依然存在，因此让我们假设改用 CCA 安全的加密方案。即便如此，仍然存在一种可由恶意 $R$ 实施的攻击。收到来自 $S$ 的 $\langle S, \mathsf{Enc}_{ek_R}(m\|\sigma)\rangle$ 后，恶意 $R$ 可以解密得到 $m\|\sigma$，然后重新加密并把 $\langle S, \mathsf{Enc}_{ek_{R^{\prime}}}(m\|\sigma)\rangle$ 发送给另一个接收方 $R^{\prime}$。这个（诚实的）接收方 $R^{\prime}$ 随后会以为 $S$ 给它发了消息 $m$。这可能造成严重后果，例如当 $m$ 是消息“I owe you \$100.”（我欠你 100 美元）时。

These attacks can be prevented if parties are more careful about how they handle identifiers. When encrypting, a sender should encrypt its own identity along with the message; when signing, a party should sign the identity of the intended recipient along with what is being signed. For example, the second approach would be modified so that $S$ first computes $\sigma \leftarrow \mathsf{Sign}_{sk_S}(m \| R)$, and then sends $\langle S, \mathsf{Enc}_{ek_R}(S\|m\|\sigma)\rangle$ to $R$. When decrypting, the receiver should check that the decrypted value includes the (purported) sender's identity; when verifying, the receiver should check that what was signed incorporates its own identity. When including identities in this way, both authenticate-then-encrypt and encrypt-then-authenticate are secure if a CCA-secure encryption scheme and a strongly secure signature scheme are used.

只要各方在处理标识符时更加小心，这些攻击是可以防止的。加密时，发送方应把自己的身份连同消息一起加密；签名时，签署方应把目标接收方的身份连同被签署的内容一起签名。例如，可以把第二种方法修改为：$S$ 先计算 $\sigma \leftarrow \mathsf{Sign}_{sk_S}(m \| R)$，然后把 $\langle S, \mathsf{Enc}_{ek_R}(S\|m\|\sigma)\rangle$ 发送给 $R$。解密时，接收方应检查解密结果中包含（所称的）发送方身份；验证时，接收方应检查被签署的内容纳入了自己的身份。按这种方式纳入身份之后，只要使用 CCA 安全的加密方案和强安全的签名方案，“先认证后加密”与“先加密后认证”就都是安全的。

## References and Additional Reading　参考文献与延伸阅读

Notable early work on signatures includes that of Diffie and Hellman [65], Rabin [165, 166], Rivest, Shamir, and Adleman [171], and Goldwasser, Micali, and Yao [89]. For an extensive treatment of signature schemes beyond what is covered here, see the monograph by Katz [109].

关于数字签名的著名早期工作包括 Diffie 与 Hellman [65]、Rabin [165, 166]、Rivest、Shamir 与 Adleman [171]，以及 Goldwasser、Micali 与 Yao [89] 的工作。要了解超出本书范围的、关于签名方案的详尽论述，可参见 Katz [109] 的专著。

Goldwasser, Micali, and Rivest [88] defined the notion of existential unforgeability under an adaptive chosen-message attack, and also gave the first construction of a stateful signature scheme satisfying this definition.

Goldwasser、Micali 与 Rivest [88] 定义了在自适应选择消息攻击下的存在性不可伪造概念，并给出了第一个满足该定义的有状态签名方案构造。

Plain RSA signatures date to the original RSA paper [171]. RSA-FDH was proposed by Bellare and Rogaway in their paper introducing the random-oracle model [24], although the idea (without proof) of using a cryptographic hash function to prevent algebraic attacks can be traced back to Rabin [166]. A later improvement of RSA-FDH [26] was standardized in PKCS #1 v2.1.

朴素 RSA 签名可追溯到最初的 RSA 论文 [171]。RSA-FDH 由 Bellare 与 Rogaway 在其引入随机预言机模型的论文 [24] 中提出，不过利用密码学哈希函数来阻止代数攻击的想法（当时未给出证明）可以追溯至 Rabin [166]。RSA-FDH 的一个后续改进版本 [26] 已被标准化为 PKCS #1 v2.1。

The Fiat-Shamir transform [72] and the Schnorr signature scheme [175] both date to the late-1980s. The proof of Theorem 13.10 is due to Abdalla et al. [1] and the proof of Theorem 13.11 is inspired by Bellare and Neven [22]. The DSA and ECDSA standards are described in [150, 151].

Fiat–Shamir 变换 [72] 与 Schnorr 签名方案 [175] 都诞生于 20 世纪 80 年代末。定理 13.10 的证明归功于 Abdalla 等人 [1]，定理 13.11 的证明则受 Bellare 与 Neven [22] 的启发。DSA 与 ECDSA 标准见 [150, 151]。

The notion of certificates was first described by Kohnfelder [118] in his undergraduate thesis. Public-key infrastructures are discussed in greater detail in [113, Chapter 15]; see also [3, 69]. The TLS version 1.3 standard is available as an RFC [170]. A formal treatment of combined secrecy and integrity in the public-key setting is given by An et al. [10].

证书的概念最早由 Kohnfelder [118] 在其本科毕业论文中描述。公钥基础设施在 [113，第 15 章] 中有更详细的讨论；另见 [3, 69]。TLS 1.3 版标准以 RFC 形式发布 [170]。An 等人 [10] 给出了公钥场景中保密性与完整性联合处理的规范化论述。

## Exercises　习题

13.1 Show that Construction 4.7 for constructing a variable-length MAC from any fixed-length MAC can also be used (with appropriate modifications) to construct a signature scheme for arbitrary-length messages from any signature scheme for messages of fixed length $\ell(n) \geq n$.

习题 13.1　证明：构造 4.7——由任意定长 MAC 构造变长 MAC——也可以（经适当修改后）用于从任意针对长度为 $\ell(n) \geq n$ 的定长消息的签名方案，构造出针对任意长度消息的签名方案。

13.2 In Section 13.4.1 we showed an attack on the plain RSA signature scheme in which an attacker forges a signature on an arbitrary message using two signing queries. Show how an attacker can forge a signature on an arbitrary message using a single signing query.

习题 13.2　在 13.4.1 节中，我们给出了对朴素 RSA 签名方案的一种攻击：攻击者用两次签名查询伪造出任意消息上的签名。证明攻击者如何只用一次签名查询就能伪造任意消息上的签名。

13.3 Assume the RSA problem is hard. Show that the plain RSA signature scheme satisfies the following weak definition of security: an attacker is given the public key $\langle N, e \rangle$ and a uniform message $m \in \mathbb{Z}_N^*$. The adversary succeeds if it can output a valid signature on $m$ without making any signing queries.

习题 13.3　假设 RSA 问题是困难的。证明朴素 RSA 签名方案满足如下弱安全性定义：给攻击者公钥 $\langle N, e \rangle$ 和一条均匀的消息 $m \in \mathbb{Z}_N^*$；如果敌手能在不做任何签名查询的情况下输出 $m$ 上的有效签名，则敌手成功。

13.4 Consider a “padded RSA” signature scheme where the public key is $\langle N, e \rangle$ as usual, and a signature on a message $m \in \{0,1\}^{\ell}$ is computed by choosing uniform $r \in \{0,1\}^{2n-\ell-1}$ and outputting $[(r\|m)^d \bmod N]$.

习题 13.4　考虑一个“填充 RSA”签名方案：公钥照常是 $\langle N, e \rangle$，消息 $m \in \{0,1\}^{\ell}$ 上的签名通过均匀选取 $r \in \{0,1\}^{2n-\ell-1}$ 并输出 $[(r\|m)^d \bmod N]$ 来计算。

(a) How can verification be done for this scheme?

(a) 该方案的验证如何进行？

(b) Show that this scheme is insecure.

(b) 证明该方案是不安全的。

13.5 Another approach (besides hashing) that has been explored to construct secure RSA-based signatures is to encode the message before applying the RSA permutation. Here the signer fixes a public encoding function $\text{enc} : \{0,1\}^\ell \to \mathbb{Z}_N^*$ as part of its public key, and the signature on a message $m$ is $\sigma := [\text{enc}(m)^d \mod N]$.

习题 13.5　除哈希之外，人们探索过的另一种构造安全 RSA 签名的方法是在施加 RSA 置换之前先对消息进行编码。这里，签名者把一个公开的编码函数 $\text{enc} : \{0,1\}^\ell \to \mathbb{Z}_N^*$ 固定为其公钥的一部分，消息 $m$ 上的签名为 $\sigma := [\text{enc}(m)^d \bmod N]$。

(a) How is verification performed in such a scheme?

(a) 这种方案的验证是如何进行的？

(b) Suggest an appropriate encoding function for $\ell \ll \|N\|$ that heuristically prevents the “no-message attack” described in Section 13.4.1.

(b) 针对 $\ell \ll \|N\|$ 的情形，提出一种合适的编码函数，使其启发式地阻止 13.4.1 节所描述的“无消息攻击”。

(c) Show that encoded RSA is insecure if $\text{enc}(m) = m\|0^{\kappa/10}$ (where $\kappa \stackrel{\mathrm{def}}{=} \|N\|, |m| \stackrel{\mathrm{def}}{=} 4\kappa/5$, and $m$ is not the all-0 message). Assume $e = 3$.

(c) 证明：若 $\text{enc}(m) = m\|0^{\kappa/10}$（其中 $\kappa \stackrel{\mathrm{def}}{=} \|N\|$、$|m| \stackrel{\mathrm{def}}{=} 4\kappa/5$，且 $m$ 不是全 0 消息），则编码 RSA 是不安全的。设 $e = 3$。

(d) Show that encoded RSA is insecure for $\text{enc}(m) = m\|0\|m$ (where $|m| \stackrel{\mathrm{def}}{=} (\|N\| - 1)/2$ and $m$ is not the all-0 message). Assume $e = 3$.

(d) 证明：对于 $\text{enc}(m) = m\|0\|m$（其中 $|m| \stackrel{\mathrm{def}}{=} (\|N\| - 1)/2$，且 $m$ 不是全 0 消息），编码 RSA 是不安全的。设 $e = 3$。

(e) Show attacks in parts (c) and (d) for arbitrary e.

(e) 对任意 $e$ 给出 (c)、(d) 两问中的攻击。

13.6 Consider a variant of the Fiat–Shamir transform in which the signature is $(I, s)$ rather than $(r, s)$ and verification is changed in the natural way. Show that if the underlying identification scheme is secure, then this variant signature scheme is secure as well.

习题 13.6　考虑 Fiat–Shamir 变换的一个变体：签名为 $(I, s)$ 而非 $(r, s)$，验证也按自然方式相应改变。证明：如果底层的身份识别方案是安全的，那么这个变体签名方案同样是安全的。

13.7 Show that ECDSA is not strongly secure. Specifically, show that if $(r, s)$ is a valid signature on a message $m$, then so is $(r, -s)$.

习题 13.7　证明 ECDSA 不是强安全的。具体而言，证明如果 $(r, s)$ 是消息 $m$ 上的有效签名，那么 $(r, -s)$ 也是。

Hint: You will need to consider the representation of elliptic-curve points.

提示：你需要考虑椭圆曲线点的表示。

13.8 Consider a variant of DSA in which the message space is $\mathbb{Z}_q$ and $H$ is omitted. (So the second component of the signature is now $s := [k^{-1} \cdot (m + xr) \mod q]$.) Show that this variant is not secure.

习题 13.8　考虑 DSA 的一个变体：消息空间为 $\mathbb{Z}_q$ 且省略 $H$。（此时签名的第二个分量变为 $s := [k^{-1} \cdot (m + xr) \mod q]$。）证明这个变体是不安全的。

13.9 Assume revocation of certificates is handled in the following way: when a user Bob claims that the private key corresponding to his public key $pk_{B}$ has been stolen, the user sends to the CA a statement of this fact signed with respect to $pk_{B}$. Upon receiving such a signed message, the CA revokes the appropriate certificate.

习题 13.9　假设证书吊销按如下方式处理：当用户 Bob 声称与其公钥 $pk_{B}$ 相应的私钥被盗时，该用户向 CA 发送一份关于此事的声明，并用 $pk_{B}$ 对应的私钥签名。CA 收到这条签名消息后就吊销相应的证书。

Explain why it is not necessary for the CA to check Bob's identity in this case. In particular, explain why it is of no concern that an adversary who has stolen Bob's private key can forge signatures with respect to $pk_{B}$.

解释为什么在这种情况下 CA 无须核验 Bob 的身份。特别地，解释为什么“窃取了 Bob 私钥的敌手能够伪造关于 $pk_{B}$ 的签名”这一点无关紧要。
