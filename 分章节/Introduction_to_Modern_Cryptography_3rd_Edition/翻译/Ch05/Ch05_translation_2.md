## 5.3 Authenticated Encryption Schemes　5.3 认证加密方案

### 5.3.1 Generic Constructions　5.3.1 通用构造

It is tempting to think that any reasonable combination of a CPA-secure encryption scheme and a secure message authentication code should result in an authenticated encryption scheme. In this section we show that this is not the case. This demonstrates that even secure cryptographic tools can be combined in such a way that the result is insecure, and highlights once again the importance of definitions and proofs of security. On the positive side, we show how encryption and message authentication can be combined properly to achieve joint secrecy and integrity.

人们很容易认为，把一个 CPA 安全的加密方案和一个安全的消息认证码以任何合理的方式组合起来，就应该得到一个认证加密方案。在本节中我们表明情况并非如此。这说明即使是安全的密码学工具，也可能以某种方式组合后导致结果是不安全的，这再次凸显了安全性定义与证明的重要性。从积极的一面来看，我们展示了如何正确地组合加密与消息认证，从而同时实现机密性和完整性。

Throughout, let $\Pi_E = (\mathsf{Enc}, \mathsf{Dec})$ be a CPA-secure encryption scheme and let $\Pi_M = (\mathsf{Mac}, \mathsf{Vrfy})$ denote a strongly secure MAC, where key generation in both schemes simply involves choosing a uniform n-bit key. There are three natural approaches to combining encryption and message authentication using independent $^1$ keys $k_E$ and $k_M$ for $\Pi_E$ and $\Pi_M$, respectively:

在本节中，设 $\Pi_E = (\mathsf{Enc}, \mathsf{Dec})$ 是一个 CPA 安全的加密方案，设 $\Pi_M = (\mathsf{Mac}, \mathsf{Vrfy})$ 表示一个强安全的 MAC，其中两个方案的密钥生成都仅仅是选择一个均匀的 n 比特密钥。有三种自然的方式，使用独立的 $^1$ 密钥 $k_E$ 和 $k_M$（分别用于 $\Pi_E$ 和 $\Pi_M$）来组合加密与消息认证：

$^{1}$ Independent cryptographic keys should always be used when different schemes are combined. We return to this point at the end of this section.

$^{1}$ 当组合不同方案时，应当始终使用独立的密码学密钥。我们将在本节末尾再次回到这一点。

1. Encrypt-and-authenticate: In this approach, encryption and message authentication are computed independently in parallel. That is, given a message $m$, the sender transmits the ciphertext $\langle c, t \rangle$ where:

$$
c\leftarrow\mathsf{Enc}_{k_{E}}(m)\ \text{and}\ t\leftarrow\mathsf{Mac}_{k_{M}}(m).
$$

The receiver decrypts $c$ to recover $m$; assuming no error occurred, it then verifies the tag $t$. If $\mathsf{Vrfy}_{k_M}(m,t) = 1$, the receiver outputs $m$; otherwise, it outputs an error.

   加密与认证（encrypt-and-authenticate）：在这种方法中，加密与消息认证独立并行地计算。也就是说，给定消息 $m$，发送方传输密文 $\langle c, t \rangle$，其中：

$$
c\leftarrow\mathsf{Enc}_{k_{E}}(m)\ \text{and}\ t\leftarrow\mathsf{Mac}_{k_{M}}(m).
$$

   接收方解密 $c$ 以恢复 $m$；假设没有发生错误，随后它验证标签 $t$。如果 $\mathsf{Vrfy}_{k_M}(m,t) = 1$，接收方输出 $m$；否则输出一个错误。

2. Authenticate-then-encrypt: Here a tag t is first computed, and then the message and tag are encrypted together. That is, given a message m, the sender transmits the ciphertext c computed as:

$$
t\leftarrow\mathsf{Mac}_{k_{M}}(m)\ \text{and}\ c\leftarrow\mathsf{Enc}_{k_{E}}(m\|t).
$$

The receiver decrypts $c$ to obtain $m\|t$; assuming no error occurred, it then verifies the tag $t$. As before, if $\mathsf{Vrfy}_{k_M}(m,t) = 1$ the receiver outputs $m$; otherwise, it outputs an error.

   先认证再加密（authenticate-then-encrypt）：这里首先计算标签 $t$，然后将消息与标签一起加密。也就是说，给定消息 $m$，发送方传输如下计算的密文 $c$：

$$
t\leftarrow\mathsf{Mac}_{k_{M}}(m)\ \text{and}\ c\leftarrow\mathsf{Enc}_{k_{E}}(m\|t).
$$

   接收方解密 $c$ 得到 $m\|t$；假设没有发生错误，随后它验证标签 $t$。与前面一样，如果 $\mathsf{Vrfy}_{k_M}(m,t) = 1$，接收方输出 $m$；否则输出一个错误。

3. Encrypt-then-authenticate: In this case, the message m is first encrypted and then a tag is computed over the result. That is, the ciphertext is the pair $\langle c, t \rangle$ where:

$$
c\leftarrow\mathsf{Enc}_{k_{E}}(m)\ \text{and}\ t\leftarrow\mathsf{Mac}_{k_{M}}(c).
$$

(See also Construction 5.6.) If $\mathsf{Vrfy}_{k_M}(c,t) = 1$, then the receiver decrypts $c$ and outputs the result; otherwise, it outputs an error.

   先加密再认证（encrypt-then-authenticate）：在这种情况下，消息 $m$ 首先被加密，然后对其结果计算标签。也就是说，密文是二元组 $\langle c, t \rangle$，其中：

$$
c\leftarrow\mathsf{Enc}_{k_{E}}(m)\ \text{and}\ t\leftarrow\mathsf{Mac}_{k_{M}}(c).
$$

   （另见构造 5.6。）如果 $\mathsf{Vrfy}_{k_M}(c,t) = 1$，则接收方解密 $c$ 并输出结果；否则输出一个错误。

We analyze each of the above approaches when they are instantiated with "generic" secure components, i.e., when instantiated with an arbitrary CPA-secure encryption scheme and an arbitrary strongly secure MAC (cf. Definition 4.3). We are looking for an approach that provides joint secrecy and integrity when using any (secure) components, and so reject as "unsafe" any approach for which this is not the case. This reduces the likelihood of implementation flaws. Specifically, an approach might be implemented by making calls to an "encryption subroutine" and a "message authentication subroutine," and the implementation of those subroutines may be changed at some later point in time. (This commonly occurs when cryptographic libraries are updated, or when standards are modified.) An approach whose security depends on the details of how its underlying components are implemented—rather than on the security they provide—is therefore dangerous.

我们分析上述每种方法在用“通用”安全组件实例化时的表现，即用任意的 CPA 安全加密方案和任意的强安全 MAC（参见定义 4.3）来实例化。我们寻找的是一种在使用任何（安全的）组件时都能提供联合机密性与完整性的方法，因此把任何做不到这一点的方法当作“不安全”的而加以拒绝。这降低了实现缺陷的可能性。具体而言，一种方法可能通过调用“加密子程序”和“消息认证子程序”来实现，而这些子程序的实现可能在将来的某个时刻被更改。（这常见于密码库更新或标准修订时。）因此，一种其安全性依赖于底层组件实现细节——而非它们所提供的安全性——的方法是危险的。

We stress that if an approach is rejected this does not mean that it is insecure for all possible instantiations of the components; it does, however, mean that any instantiation of the approach must be carefully analyzed and proven secure before it is used.

我们强调，如果一种方法被拒绝，这并不意味着它对于组件的所有可能实例化都是不安全的；然而，这确实意味着该方法的任何实例化在使用之前都必须经过仔细分析并被证明是安全的。

Encrypt-and-authenticate. Recall that in this approach encryption and message authentication are carried out independently. Given a message $m$, the ciphertext is $\langle c, t \rangle$ where $c \leftarrow \mathsf{Enc}_{k_E}(m)$ and $t \leftarrow \mathsf{Mac}_{k_M}(m)$. This approach is problematic since it may not achieve even the most basic level of secrecy. To see this, note that even a strongly secure MAC does not guarantee any secrecy and so it is possible for the tag $t$ to leak information about $m$ to an eavesdropper. (As a trivial example, consider a strongly secure MAC where the first bit of the tag is always equal to the first bit of the message.) So the encrypt-and-authenticate approach may yield a scheme that is not even EAV-secure.

加密与认证。回忆在这种方法中，加密与消息认证是独立进行的。给定消息 $m$，密文为 $\langle c, t \rangle$，其中 $c \leftarrow \mathsf{Enc}_{k_E}(m)$ 且 $t \leftarrow \mathsf{Mac}_{k_M}(m)$。这种方法是有问题的，因为它可能连最基本级别的机密性都达不到。为说明这一点，注意即使是强安全的 MAC 也不保证任何机密性，因此标签 $t$ 有可能向窃听者泄露关于 $m$ 的信息。（作为一个平凡的例子，考虑一个强安全的 MAC，其标签的第一比特总是等于消息的第一比特。）因此，加密与认证方法可能产生一个甚至不是 EAV 安全的方案。

The encrypt-and-authenticate approach is insecure against chosen-plaintext attacks even when instantiated with standard components (as opposed to the somewhat contrived example in the previous paragraph). In particular, if a deterministic MAC like CBC-MAC is used, then the tag computed on a message (for some fixed key $k_{M}$) is the same every time. This allows an eavesdropper to identify when the same message is sent twice, something that is not possible for a CPA-secure scheme. Many MACs used in practice are deterministic, so this represents a real concern.

即使采用标准组件来实例化（不同于上一段中那个略显人为的例子），加密与认证方法在选择明文攻击下也是不安全的。特别地，如果使用像 CBC-MAC 这样的确定性 MAC，那么在某个固定密钥 $k_{M}$ 下对一条消息计算出的标签每次都相同。这使得窃听者能够识别出同一条消息何时被发送了两次，而这对于 CPA 安全的方案是不可能的。实践中使用的许多 MAC 都是确定性的，因此这代表了一种现实的担忧。

Authenticate-then-encrypt. Here, a tag $t \leftarrow \mathsf{Mac}_{k_M}(m)$ is first computed; then $m\|t$ is encrypted and the ciphertext $c \leftarrow \mathsf{Enc}_{k_E}(m\|t)$ is transmitted. This combination also does not necessarily yield an authenticated encryption scheme. We have already encountered a CPA-secure encryption scheme for which this approach is insecure: the CBC-mode-with-padding scheme discussed in Section 5.1.1. (We assume in what follows that the reader is familiar with that section.) Recall that this scheme works by first padding the plaintext (which in our case will be $m\|t$) in a specific way so the result is a multiple of the block length, and then encrypting the result using CBC mode. During decryption, if an error in the padding is detected after performing the CBC-mode decryption, then a “bad padding” error is returned. With regard to the authenticate-then-encrypt approach, this means there are now two sources of potential decryption failure: the padding may be incorrect, or the tag may not verify. Schematically, the decryption algorithm $\mathsf{Dec}^{\prime}$ in the combined scheme works as follows:

先认证再加密。这里首先计算标签 $t \leftarrow \mathsf{Mac}_{k_M}(m)$；然后对 $m\|t$ 加密，并传输密文 $c \leftarrow \mathsf{Enc}_{k_E}(m\|t)$。这种组合同样不一定产生认证加密方案。我们已经遇到过一种使该方法不安全的 CPA 安全加密方案：5.1.1 节讨论的带填充的 CBC 模式方案。（在下面的讨论中，我们假设读者已熟悉那一节。）回忆该方案的工作方式：首先以特定方式对明文（在我们的情形中将是 $m\|t$）进行填充，使结果成为分组长度的整数倍，然后使用 CBC 模式对结果加密。在解密期间，如果在执行 CBC 模式解密后检测到填充错误，则返回一个“填充错误”。对于先认证再加密方法，这意味着现在有两个潜在的解密失败来源：填充可能不正确，或者标签可能无法通过验证。概略地说，组合方案中的解密算法 $\mathsf{Dec}^{\prime}$ 工作如下：

$$
\mathsf{Dec}_{k_{E},k_{M}}^{\prime}(c):
$$

1. Compute $\tilde{m} := \mathsf{Dec}_{k_E}(c)$. If an error in the padding is detected (i.e., $\tilde{m} = \perp$), return “bad padding” and stop.

   计算 $\tilde{m} := \mathsf{Dec}_{k_E}(c)$。如果检测到填充错误（即 $\tilde{m} = \perp$），返回“填充错误”并停止。

2. Otherwise, parse $\tilde{m}$ as $m\|t$. If $\mathsf{Vrfy}_{k_M}(m,t) = 1$ return $m$; else, output "authentication failure."

   否则，将 $\tilde{m}$ 解析为 $m\|t$。如果 $\mathsf{Vrfy}_{k_M}(m,t) = 1$ 则返回 $m$；否则输出“认证失败”。

Assuming the attacker can distinguish between the two error messages, the attacker can apply the chosen-ciphertext attack described in Section 5.1.1 to recover the entire original plaintext from a given ciphertext. (This is due to the fact that the padding-oracle attack shown in Section 5.1.1 relies only on the ability to learn whether or not there was a padding error, something that is revealed by Dec'.) This type of attack has been carried out successfully in the real world in various settings, e.g., in configurations of TLS that used authenticate-then-encrypt.

假设攻击者能够区分这两种错误消息，攻击者就可以应用 5.1.1 节中描述的选择密文攻击，从给定密文中恢复整个原始明文。（这是因为 5.1.1 节中展示的填充预言机攻击只依赖于能否获知是否发生了填充错误，而这正是 Dec' 所泄露的。）此类攻击已在现实世界中的多种环境下被成功实施，例如在使用先认证再加密的 TLS 配置中。

One way to fix the above would be to ensure that only a single error message is returned, regardless of the source of decryption failure. This is an unsatisfying solution for several reasons: (1) there may be legitimate reasons (e.g., usability, debugging) to have multiple error messages; (2) forcing the error messages to be the same means that the combination is no longer truly generic, i.e., it requires the implementer of the authenticate-then-encrypt approach to be aware of what error messages are returned by the underlying CPA-secure encryption scheme; (3) most of all, it is extraordinarily hard to ensure that the different errors cannot be distinguished since, e.g., even a difference in the time to return each of these errors may allow an adversary to distinguish between them (cf. our earlier discussion of timing attacks at the end of Section 4.2). Some versions of TLS tried using only a single error message with the authenticate-then-encrypt approach, but a padding-oracle attack was still successfully carried out using small differences in timing.

修复上述问题的一种方法是确保无论解密失败的来源如何，都只返回单一的错误消息。由于以下几个原因，这并不能令人满意：(1) 可能有合理的理由（例如可用性、调试）要保留多种错误消息；(2) 强制错误消息相同意味着该组合不再是真正通用的，即它要求先认证再加密方法的实现者了解底层 CPA 安全加密方案返回哪些错误消息；(3) 最重要的是，要确保不同的错误无法被区分是极其困难的，因为例如即使返回每种错误所用时间的差异都可能使敌手区分它们（参见我们先前在 4.2 节末尾对时序攻击的讨论）。某些版本的 TLS 尝试在先认证再加密方法中只使用单一错误消息，但利用微小的时序差异仍然成功实施了填充预言机攻击。

Finally, we note that there are other counterexamples (that do not rely on distinguishing between different errors) showing that authenticate-then-encrypt does not necessarily provide authenticated encryption.

最后，我们指出还存在其他反例（不依赖于区分不同错误）表明先认证再加密不一定能提供认证加密。

> **CONSTRUCTION 5.6**　**构造 5.6**
>
> Let $\Pi_E = (\mathsf{Enc}, \mathsf{Dec})$ be a private-key encryption scheme and let $\Pi_M = (\mathsf{Mac}, \mathsf{Vrfy})$ be a message authentication code, where in each case key generation is done by simply choosing a uniform $n$-bit key. Define a private-key encryption scheme $(\mathsf{Gen}^{\prime}, \mathsf{Enc}^{\prime}, \mathsf{Dec}^{\prime})$ as follows:
>
> - Gen': on input ${1}^n$, choose independent, uniform $k_E, k_M \in \{0,1\}^n$ and output the key $(k_E, k_M)$.
>
> - Enc': on input a key $(k_E, k_M)$ and a plaintext message $m$, compute $c \leftarrow \mathsf{Enc}_{k_E}(m)$ and $t \leftarrow \mathsf{Mac}_{k_M}(c)$. Output the ciphertext $\langle c, t \rangle$.
>
> - Dec': on input a key $(k_E, k_M)$ and a ciphertext $\langle c, t \rangle$, first check if $\mathsf{Vrfy}_{k_M}(c, t) \overset{?}{=} 1$. If yes, output $\mathsf{Dec}_{k_E}(c)$; if no, output $\perp$.
>
> 设 $\Pi_E = (\mathsf{Enc}, \mathsf{Dec})$ 是一个私钥加密方案，设 $\Pi_M = (\mathsf{Mac}, \mathsf{Vrfy})$ 是一个消息认证码，其中每种情形下密钥生成都仅仅是选择一个均匀的 $n$ 比特密钥。定义私钥加密方案 $(\mathsf{Gen}^{\prime}, \mathsf{Enc}^{\prime}, \mathsf{Dec}^{\prime})$ 如下：
>
> - Gen'：输入 ${1}^n$，选择独立、均匀的 $k_E, k_M \in \{0,1\}^n$，输出密钥 $(k_E, k_M)$。
>
> - Enc'：输入密钥 $(k_E, k_M)$ 和明文消息 $m$，计算 $c \leftarrow \mathsf{Enc}_{k_E}(m)$ 和 $t \leftarrow \mathsf{Mac}_{k_M}(c)$。输出密文 $\langle c, t \rangle$。
>
> - Dec'：输入密钥 $(k_E, k_M)$ 和密文 $\langle c, t \rangle$，首先检查是否 $\mathsf{Vrfy}_{k_M}(c, t) \overset{?}{=} 1$。若是，输出 $\mathsf{Dec}_{k_E}(c)$；若否，输出 $\perp$。
>
> The encrypt-then-authenticate approach.
>
> 先加密再认证方法。

Encrypt-then-authenticate. In this approach, the message is first encrypted and then a MAC is computed over the result. That is, the ciphertext is now the pair $\langle c, t \rangle$ where

先加密再认证。在这种方法中，消息首先被加密，然后对其结果计算 MAC。也就是说，密文现在是二元组 $\langle c, t \rangle$，其中

$$
c\leftarrow\mathsf{Enc}_{k_{E}}(m)\ \text{and}\ t\leftarrow\mathsf{Mac}_{k_{M}}(c).
$$

Decryption of $\langle c, t \rangle$ outputs an error if $\mathsf{Vrfy}_{k_M}(c, t) \neq 1$, and otherwise outputs $\mathsf{Dec}_{k_E}(c)$. See Construction 5.6 for a formal description.

如果 $\mathsf{Vrfy}_{k_M}(c, t) \neq 1$，则对 $\langle c, t \rangle$ 的解密输出一个错误，否则输出 $\mathsf{Dec}_{k_E}(c)$。形式化描述见构造 5.6。

This approach is sound. As intuition for why, say a ciphertext $\langle c, t \rangle$ is valid if $t$ is a valid tag on $c$. Strong security of the MAC ensures that an adversary will be unable to generate any valid ciphertext that it did not receive from its encryption oracle. This immediately implies that Construction 5.6 is unforgeable. Moreover, it effectively renders the decryption oracle useless: for every ciphertext $\langle c, t \rangle$ the adversary submits to its decryption oracle, the adversary either already knows the decryption (if it received $\langle c, t \rangle$ from its encryption oracle) or will receive an error. (Observe also that the tag is verified before decryption takes place; thus, errors during decryption cannot leak anything about the plaintext, in contrast to the padding-oracle attack we saw against the authenticate-then-encrypt approach.) Therefore, CCA-security of the combined scheme reduces to CPA-security of $\Pi_E$.

这种方法是可靠的。直观理由如下：如果 $t$ 是 $c$ 的有效标签，我们就称密文 $\langle c, t \rangle$ 是有效的。MAC 的强安全性保证了敌手将无法生成任何它未曾从其加密预言机处获得的有效密文。这立即蕴含构造 5.6 是不可伪造的。此外，它实际上使解密预言机变得无用：对于敌手提交给其解密预言机的每个密文 $\langle c, t \rangle$，敌手要么已经知道其解密结果（如果它从加密预言机处收到过 $\langle c, t \rangle$），要么将收到一个错误。（还要注意，标签在解密发生之前就被验证了；因此，解密期间的错误不会泄露关于明文的任何信息，这与我们针对先认证再加密方法看到的填充预言机攻击形成对比。）因此，组合方案的 CCA 安全性归约到 $\Pi_E$ 的 CPA 安全性。

THEOREM 5.7 Let $\Pi_{E}$ be a CPA-secure private-key encryption scheme, and let $\Pi_{M}$ be a strongly secure message authentication code. Then Construction 5.6 is an authenticated encryption scheme.

**定理 5.7** 设 $\Pi_{E}$ 是 CPA 安全的私钥加密方案，设 $\Pi_{M}$ 是强安全的消息认证码。则构造 5.6 是一个认证加密方案。

PROOF We show that the scheme $\Pi$ resulting from Construction 5.6 is unforgeable, and that it is CCA-secure. (See Definition 5.3.) Toward this end, we first show that strong security of $\Pi_M$ implies that (except with negligible probability) any “new” ciphertexts an adversary submits to its decryption oracle will result in an error. This immediately implies unforgeability. (In fact, it is stronger than unforgeability.) It also renders the decryption oracle useless, and allows us to reduce CCA-security of $\Pi$ to CPA-security of $\Pi_E$.

**证明** 我们证明由构造 5.6 得到的方案 $\Pi$ 是不可伪造的，并且是 CCA 安全的。（参见定义 5.3。）为此，我们首先证明 $\Pi_M$ 的强安全性蕴含（除了以可忽略概率外）敌手提交给其解密预言机的任何“新”密文都将导致错误。这立即蕴含不可伪造性。（事实上，它比不可伪造性更强。）它也使解密预言机变得无用，并允许我们将 $\Pi$ 的 CCA 安全性归约到 $\Pi_E$ 的 CPA 安全性。

In more detail, let $\mathcal{A}$ be a PPT adversary attacking Construction 5.6 in a chosen-ciphertext attack (cf. Definition 5.1). Say a ciphertext that $\mathcal{A}$ submits to its decryption oracle is new if $\mathcal{A}$ did not receive it from its encryption oracle or as the challenge ciphertext. A ciphertext $\langle c, t \rangle$ is valid (with respect to the secret key $(k_E, k_M)$ chosen as part of the experiment) if $\mathsf{Vrfy}_{k_M}(c, t) = 1$. Let $\mathsf{ValidQuery}$ be the event that $\mathcal{A}$ submits a new, valid ciphertext to its decryption oracle. We prove:

更详细地说，设 $\mathcal{A}$ 是在选择密文攻击中攻击构造 5.6 的 PPT 敌手（参见定义 5.1）。如果 $\mathcal{A}$ 提交给其解密预言机的某个密文并非来自其加密预言机或挑战密文，则称该密文是新的。如果 $\mathsf{Vrfy}_{k_M}(c, t) = 1$，则称密文 $\langle c, t \rangle$（相对于作为实验一部分选择的秘密密钥 $(k_E, k_M)$）是有效的。令 $\mathsf{ValidQuery}$ 为 $\mathcal{A}$ 向其解密预言机提交一个新的、有效的密文这一事件。我们证明：

CLAIM 5.8 $\Pr[\mathsf{ValidQuery}]$ is negligible.

**断言 5.8** $\Pr[\mathsf{ValidQuery}]$ 是可忽略的。

PROOF Intuitively, this is because if $\mathsf{ValidQuery}$ occurs then the adversary has forged a new, valid pair $(c,t)$ in the Mac-sforge experiment. Let $q(\cdot)$ be a polynomial upper bound on the number of decryption-oracle queries made by $\mathcal{A}$, and consider the following adversary $\mathcal{A}_M$ attacking the message authentication code $\Pi_M$:

**证明** 直观上，这是因为如果 $\mathsf{ValidQuery}$ 发生，则敌手在 Mac-sforge 实验中伪造了一个新的、有效的对 $(c,t)$。令 $q(\cdot)$ 为 $\mathcal{A}$ 所作解密预言机查询数目的多项式上界，考虑以下攻击消息认证码 $\Pi_M$ 的敌手 $\mathcal{A}_M$：

Adversary $\mathcal{A}_{M}$:

敌手 $\mathcal{A}_{M}$：

 $\mathcal{A}_M$ is given input ${1}^n$ and has access to a MAC oracle $\mathsf{Mac}_{k_M}(\cdot)$.

 $\mathcal{A}_M$ 获得输入 ${1}^n$ 并可访问 MAC 预言机 $\mathsf{Mac}_{k_M}(\cdot)$。

1. Choose uniform $k_E \in \{0,1\}^n$ and $i \in \{1,\ldots,q(n)\}$.

   选择均匀的 $k_E \in \{0,1\}^n$ 和 $i \in \{1,\ldots,q(n)\}$。

2. Run A on input ${1}^{n}$. When A makes an encryption-oracle query for the message m, answer it as follows:

   在输入 ${1}^{n}$ 上运行 $\mathcal{A}$。当 $\mathcal{A}$ 对消息 $m$ 作加密预言机查询时，按如下方式回答：

   (i) Compute $c \leftarrow \mathsf{Enc}_{k_E}(m)$.
   (i) 计算 $c \leftarrow \mathsf{Enc}_{k_E}(m)$。

   (ii) Query c to the MAC oracle and receive t in response.
   (ii) 将 $c$ 查询到 MAC 预言机并收到 $t$ 作为响应。

   Return $\langle c,t\rangle$ to A.
   将 $\langle c,t\rangle$ 返回给 $\mathcal{A}$。

The challenge ciphertext is prepared in the exact same way (with a uniform bit $b \in \{0,1\}$ chosen to select the message $m_b$ that gets encrypted).

挑战密文以完全相同的方式准备（选择一个均匀比特 $b \in \{0,1\}$ 来选定被加密的消息 $m_b$）。

When $\mathcal{A}$ makes a decryption-oracle query for the ciphertext $\langle c,t\rangle$, answer it as follows: If this is the $i$th decryption-oracle query, output $(c,t)$ and halt. Otherwise:

当 $\mathcal{A}$ 对密文 $\langle c,t\rangle$ 作解密预言机查询时，按如下方式回答：如果这是第 $i$ 次解密预言机查询，则输出 $(c,t)$ 并停机。否则：

   (i) If $\langle c, t \rangle$ was a response to a previous encryption-oracle query for a message m, return m.
   (i) 如果 $\langle c, t \rangle$ 是先前对某消息 $m$ 的加密预言机查询的响应，则返回 $m$。

   (ii) Otherwise, return $\bot$.
   (ii) 否则，返回 $\bot$。

In essence, $\mathcal{A}_M$ is “guessing” that the ith decryption-oracle query of $\mathcal{A}$ is the first new, valid query $\mathcal{A}$ makes. In that case, $\mathcal{A}_M$ indeed outputs a new, valid message/tag pair $(c, t)$.

本质上，$\mathcal{A}_M$ 在“猜测” $\mathcal{A}$ 的第 i 次解密预言机查询就是 $\mathcal{A}$ 所作的第一个新的、有效的查询。在此情形下，$\mathcal{A}_M$ 确实输出了一个新的、有效的消息/标签对 $(c, t)$。

Clearly $\mathcal{A}_M$ runs in polynomial time. We now analyze the probability that $\mathcal{A}_M$ outputs a new, valid message/tag pair. The key point is that the view of $\mathcal{A}$ when run as a subroutine by $\mathcal{A}_M$ is distributed identically to the view of $\mathcal{A}$ in experiment $\mathsf{PrivK}_{\mathcal{A},\Pi}^{\mathsf{cca}}(n)$ until event $\mathsf{ValidQuery}$ occurs. To see this, note that responses to the encryption-oracle queries of $\mathcal{A}$ (as well as the challenge ciphertext) are simulated perfectly by $\mathcal{A}_M$. As for the decryption-oracle queries of $\mathcal{A}$, until $\mathsf{ValidQuery}$ occurs these are all simulated properly. In case (i) this is obvious. As for case (ii), if the ciphertext $\langle c, t \rangle$ submitted to the decryption oracle is new, then as long as $\mathsf{ValidQuery}$ has not yet occurred the correct answer to that query is indeed $\bot$. (Recall also that $\mathcal{A}$ is disallowed from submitting the challenge ciphertext to the decryption oracle.)

显然 $\mathcal{A}_M$ 在多项式时间内运行。我们现在分析 $\mathcal{A}_M$ 输出一个新的、有效的消息/标签对的概率。关键在于，$\mathcal{A}$ 作为 $\mathcal{A}_M$ 的子程序运行时的视图，与 $\mathcal{A}$ 在实验 $\mathsf{PrivK}_{\mathcal{A},\Pi}^{\mathsf{cca}}(n)$ 中直到事件 $\mathsf{ValidQuery}$ 发生之前的视图分布相同。为看清这一点，注意 $\mathcal{A}$ 的加密预言机查询（以及挑战密文）的响应都被 $\mathcal{A}_M$ 完美地模拟了。至于 $\mathcal{A}$ 的解密预言机查询，在 $\mathsf{ValidQuery}$ 发生之前它们都被正确地模拟了。情形 (i) 中这是显然的。至于情形 (ii)，如果提交给解密预言机的密文 $\langle c, t \rangle$ 是新的，那么只要 $\mathsf{ValidQuery}$ 尚未发生，该查询的正确答案确实是 $\bot$。（还要回忆 $\mathcal{A}$ 被禁止向解密预言机提交挑战密文。）

Because the view of $\mathcal{A}$ when run as a subroutine by $\mathcal{A}_M$ is distributed identically to the view of $\mathcal{A}$ in experiment $\mathsf{PrivK}_{\mathcal{A},\Pi}^{\mathsf{cca}}(n)$ until event $\mathsf{ValidQuery}$ occurs, the probability of event $\mathsf{ValidQuery}$ in experiment $\mathsf{Mac-sforge}_{\mathcal{A}_M,\Pi_M}(n)$ is the same as the probability of that event in experiment $\mathsf{PrivK}_{\mathcal{A},\Pi}^{\mathsf{cca}}(n)$.

由于 $\mathcal{A}$ 作为 $\mathcal{A}_M$ 的子程序运行时的视图，与 $\mathcal{A}$ 在实验 $\mathsf{PrivK}_{\mathcal{A},\Pi}^{\mathsf{cca}}(n)$ 中直到事件 $\mathsf{ValidQuery}$ 发生之前的视图分布相同，所以事件 $\mathsf{ValidQuery}$ 在实验 $\mathsf{Mac-sforge}_{\mathcal{A}_M,\Pi_M}(n)$ 中发生的概率与该事件在实验 $\mathsf{PrivK}_{\mathcal{A},\Pi}^{\mathsf{cca}}(n)$ 中发生的概率相同。

If $\mathcal{A}_M$ correctly guesses the first index $i$ for which $\mathsf{ValidQuery}$ occurs, $\mathcal{A}_M$ outputs $(c,t)$ for which $\mathsf{Vrfy}_{k_M}(c,t) = 1$ (since $\langle c,t \rangle$ is valid) and for which it was never given tag $t$ in response to the query $\mathsf{Mac}_{k_M}(c)$ (since $\langle c,t \rangle$ is new). In this case, then, $\mathcal{A}_M$ succeeds in experiment $\mathsf{Mac-sforge}_{\mathcal{A}_M, \Pi_M}(n)$. The probability that $\mathcal{A}_M$ guesses $i$ correctly is ${1}/q(n)$. Therefore

如果 $\mathcal{A}_M$ 正确猜到了 $\mathsf{ValidQuery}$ 发生的第一个索引 $i$，则 $\mathcal{A}_M$ 输出的 $(c,t)$ 满足 $\mathsf{Vrfy}_{k_M}(c,t) = 1$（因为 $\langle c,t \rangle$ 是有效的），并且对于该 $(c,t)$，它从未在查询 $\mathsf{Mac}_{k_M}(c)$ 的响应中得到过标签 $t$（因为 $\langle c,t \rangle$ 是新的）。因此在这种情况下，$\mathcal{A}_M$ 在实验 $\mathsf{Mac-sforge}_{\mathcal{A}_M, \Pi_M}(n)$ 中成功。$\mathcal{A}_M$ 猜中 $i$ 的概率为 ${1}/q(n)$。因此

$$
\Pr[\mathsf{Mac-sforge}_{\mathcal{A}_{M},\Pi_{M}}(n)=1]\geq\Pr[\mathsf{ValidQuery}]/q(n).
$$

Since $\Pi_{M}$ is a strongly secure MAC and q is polynomial, we conclude that $\Pr[\mathsf{ValidQuery}]$ is negligible.

由于 $\Pi_{M}$ 是强安全的 MAC 且 q 是多项式，我们得出 $\Pr[\mathsf{ValidQuery}]$ 是可忽略的。

We use Claim 5.8 to prove security of $\Pi$. The easier step is to prove that $\Pi$ is unforgeable. This follows immediately from the claim, and so we just provide informal reasoning. Observe first that the adversary in the unforgeable encryption experiment is a restricted version of the adversary in the chosen-ciphertext experiment. (In the former, the adversary only has access to an encryption oracle.) An attacker succeeds in the unforgeable encryption experiment only if it outputs a ciphertext $\langle c, t \rangle$ that is valid and new. But Claim 5.8 shows precisely that the probability of doing so is negligible.

我们用断言 5.8 来证明 $\Pi$ 的安全性。较容易的一步是证明 $\Pi$ 是不可伪造的。这可由该断言立即得出，因此我们只给出非正式的推理。首先注意到，不可伪造加密实验中的敌手是选择密文实验中敌手的一个受限制版本。（前者中，敌手只能访问加密预言机。）攻击者只有在输出一个有效且新的密文 $\langle c, t \rangle$ 时，才能在不可伪造加密实验中成功。但断言 5.8 恰好表明这样做的概率是可忽略的。

It is slightly more involved to prove that $\Pi$ is CCA-secure. Let $\mathcal{A}$ again be a probabilistic polynomial-time adversary attacking $\Pi$ in a chosen-ciphertext attack. We have

证明 $\Pi$ 是 CCA 安全的要稍微复杂一些。设 $\mathcal{A}$ 仍为在选择密文攻击中攻击 $\Pi$ 的概率多项式时间敌手。我们有

$$
\begin{aligned}
\Pr&[\mathsf{PrivK}_{\mathcal{A},\Pi}^{\mathsf{cca}}(n)=1]\\
&\leq\Pr[\mathsf{ValidQuery}]+\Pr[\mathsf{PrivK}_{\mathcal{A},\Pi}^{\mathsf{cca}}(n)=1\land\overline{\mathsf{ValidQuery}}].
\end{aligned} \tag{5.2}
$$

We have already shown that $\Pr[\mathsf{ValidQuery}]$ is negligible. We show next that there is a negligible function $\mathsf{negl}$ such that

我们已经证明了 $\Pr[\mathsf{ValidQuery}]$ 是可忽略的。接下来我们证明存在一个可忽略函数 $\mathsf{negl}$ 使得

$$
\Pr[\mathsf{PrivK}_{\mathcal{A},\Pi}^{\mathsf{cca}}(n)=1\land\overline{\mathsf{ValidQuery}}]\leq\frac{1}{2}+\mathsf{negl}(n).
$$

To prove this, we rely on CPA-security of $\Pi_{E}$. Consider the following adversary $\mathcal{A}_{E}$ attacking $\Pi_{E}$ in a chosen-plaintext attack:

为证明这一点，我们依赖 $\Pi_{E}$ 的 CPA 安全性。考虑以下在选择明文攻击中攻击 $\Pi_{E}$ 的敌手 $\mathcal{A}_{E}$：

Adversary $\mathcal{A}_{E}$:

敌手 $\mathcal{A}_{E}$：

 $\mathcal{A}_E$ is given input ${1}^n$ and has access to $\mathsf{Enc}_{k_E}(\cdot)$.

 $\mathcal{A}_E$ 获得输入 ${1}^n$ 并可访问 $\mathsf{Enc}_{k_E}(\cdot)$。

1. Choose uniform $k_M \in \{0,1\}^n$.

   选择均匀的 $k_M \in \{0,1\}^n$。

2. Run A on input ${1}^{n}$. When A makes an encryption-oracle query for the message m, answer it as follows:

   在输入 ${1}^{n}$ 上运行 $\mathcal{A}$。当 $\mathcal{A}$ 对消息 $m$ 作加密预言机查询时，按如下方式回答：

   (i) Query $m$ to $\mathsf{Enc}_{k_E}(\cdot)$ and receive $c$ in response.
   (i) 将 $m$ 查询到 $\mathsf{Enc}_{k_E}(\cdot)$ 并收到 $c$ 作为响应。

   (ii) Compute $t \leftarrow \mathsf{Mac}_{k_M}(c)$ and return $\langle c, t \rangle$ to $\mathcal{A}$.
   (ii) 计算 $t \leftarrow \mathsf{Mac}_{k_M}(c)$ 并将 $\langle c, t \rangle$ 返回给 $\mathcal{A}$。

When $\mathcal{A}$ makes a decryption-oracle query for the ciphertext $\langle c,t\rangle$, answer it as follows: If $\langle c,t\rangle$ was a response to a previous encryption-oracle query for a message $m$, return $m$. Otherwise, return $\perp$.

当 $\mathcal{A}$ 对密文 $\langle c,t\rangle$ 作解密预言机查询时，按如下方式回答：如果 $\langle c,t\rangle$ 是先前对某消息 $m$ 的加密预言机查询的响应，则返回 $m$。否则返回 $\perp$。

3. When $\mathcal{A}$ outputs messages $(m_0, m_1)$, output those same messages and receive a challenge ciphertext $c$ in response. Compute $t \leftarrow \mathsf{Mac}_{k_M}(c)$, and return $\langle c, t \rangle$ to $\mathcal{A}$ as the challenge ciphertext. Continue answering $\mathcal{A}$'s oracle queries as above.

   当 $\mathcal{A}$ 输出消息 $(m_0, m_1)$ 时，输出这些相同的消息并收到一个挑战密文 $c$ 作为响应。计算 $t \leftarrow \mathsf{Mac}_{k_M}(c)$，并将 $\langle c, t \rangle$ 作为挑战密文返回给 $\mathcal{A}$。继续如上回答 $\mathcal{A}$ 的预言机查询。

4. Output the same bit $b^{\prime}$ that is output by A.

   输出 A 所输出的相同比特 $b^{\prime}$。

Notice that $\mathcal{A}_E$ does not need a decryption oracle because it simply assumes that any decryption query by $\mathcal{A}$ that was not the result of a previous encryption-oracle query is invalid.

注意 $\mathcal{A}_E$ 不需要解密预言机，因为它简单地假设 $\mathcal{A}$ 的任何并非先前加密预言机查询结果的解密查询都是无效的。

Clearly, $\mathcal{A}_E$ runs in probabilistic polynomial time. Furthermore, the view of $\mathcal{A}$ when run as a subroutine by $\mathcal{A}_E$ is distributed identically to the view of $\mathcal{A}$ in experiment $\mathsf{PrivK}_{\mathcal{A},\Pi}^{\mathsf{cca}}(n)$ as long as event $\mathsf{ValidQuery}$ never occurs. Therefore, the probability that $\mathcal{A}_E$ succeeds is at least the probability that $\mathcal{A}$ succeeds and $\mathsf{ValidQuery}$ does not occur; i.e.,

显然，$\mathcal{A}_E$ 在概率多项式时间内运行。此外，只要事件 $\mathsf{ValidQuery}$ 从未发生，$\mathcal{A}$ 作为 $\mathcal{A}_E$ 的子程序运行时的视图与 $\mathcal{A}$ 在实验 $\mathsf{PrivK}_{\mathcal{A},\Pi}^{\mathsf{cca}}(n)$ 中的视图分布相同。因此，$\mathcal{A}_E$ 成功的概率至少是 $\mathcal{A}$ 成功且 $\mathsf{ValidQuery}$ 不发生的概率；即，

$$
\begin{aligned}
\Pr[\mathsf{PrivK}_{\mathcal{A}_{E},\Pi_{E}}^{\mathsf{cpa}}(n)=1]&\geq\Pr[\mathsf{PrivK}_{\mathcal{A}_{E},\Pi_{E}}^{\mathsf{cpa}}(n)=1\land\overline{\mathsf{ValidQuery}}]\\
&=\Pr[\mathsf{PrivK}_{\mathcal{A},\Pi}^{\mathsf{cca}}(n)=1\land\overline{\mathsf{ValidQuery}}].
\end{aligned}
$$

Since $\Pi_E$ is CPA-secure, there exists a negligible function $\mathsf{negl}$ such that $\Pr[\mathsf{PrivK}_{\mathcal{A}_E,\Pi_E}^{\mathsf{cpa}}(n) = 1] \leq \frac{1}{2} + \mathsf{negl}(n)$. Together with Equation (5.2), this proves that $\Pi$ is CCA-secure.

由于 $\Pi_E$ 是 CPA 安全的，存在一个可忽略函数 $\mathsf{negl}$ 使得 $\Pr[\mathsf{PrivK}_{\mathcal{A}_E,\Pi_E}^{\mathsf{cpa}}(n) = 1] \leq \frac{1}{2} + \mathsf{negl}(n)$。结合式 (5.2)，这证明了 $\Pi$ 是 CCA 安全的。

The need for independent keys. We conclude this section by stressing a basic principle of cryptography: different instances of cryptographic primitives should always use independent keys. To illustrate this, we consider what can happen to the encrypt-then-authenticate methodology if the same key $k$ is used for both encryption and authentication. Let $F$ be a strong pseudorandom permutation. It follows that $F^{-1}$ is a strong pseudorandom permutation also. Define $\mathsf{Enc}_k(m) = F_k(m\|r)$ for $m \in \{0,1\}^{n/2}$ and a uniform $r \in \{0,1\}^{n/2}$; it can be shown that this encryption scheme is CPA-secure. (In fact, it is even CCA-secure; see Exercise 5.9.) Define $\mathsf{Mac}_k(c) = F_k^{-1}(c)$; this is just Construction 4.5, so is strongly secure. However, using these schemes with the same key $k$ to encrypt-then-authenticate a message $m$ yields:

独立密钥的必要性。我们通过强调密码学的一个基本原则来结束本节：密码学原语的不同实例应当始终使用独立的密钥。为说明这一点，我们考虑如果加密和认证使用同一个密钥 $k$，先加密再认证方法会发生什么。设 $F$ 是一个强伪随机置换。由此可得 $F^{-1}$ 也是强伪随机置换。对 $m \in \{0,1\}^{n/2}$ 和均匀的 $r \in \{0,1\}^{n/2}$，定义 $\mathsf{Enc}_k(m) = F_k(m\|r)$；可以证明该加密方案是 CPA 安全的。（事实上，它甚至是 CCA 安全的；见习题 5.9。）定义 $\mathsf{Mac}_k(c) = F_k^{-1}(c)$；这正是构造 4.5，因而是强安全的。然而，用这些方案在同一个密钥 $k$ 下对消息 $m$ 进行先加密再认证，得到：

$$
\mathsf{Enc}_{k}(m),\mathsf{Mac}_{k}(\mathsf{Enc}_{k}(m))=F_{k}(m\|r),F_{k}^{-1}(F_{k}(m\|r))=F_{k}(m\|r),m\|r,
$$

and so the message $m$ is revealed in the clear! This does not in any way contradict Theorem 5.7, since Construction 5.6 expressly requires that $k_{M}, k_{E}$ be chosen independently. We encourage the reader to determine where this independence is used in the proof of Theorem 5.7.

于是消息 $m$ 就被明文泄露了！这绝不与定理 5.7 矛盾，因为构造 5.6 明确要求 $k_{M}, k_{E}$ 被独立地选择。我们鼓励读者找出定理 5.7 的证明中何处用到了这种独立性。

Authenticated encryption with associated data. As described at the end of Section 5.2.1, there are settings where a message $m$ is encrypted along with associated data $d$ that requires integrity but not secrecy. It is easy to modify the encrypt-then-authenticate approach to handle this: simply compute $c \leftarrow \mathsf{Enc}_{k_E}(m)$ followed by $t \leftarrow \mathsf{Mac}_{k_M}(d\|c)$.

带关联数据的认证加密。如 5.2.1 节末尾所述，在某些场景下，消息 $m$ 与需要完整性但不需要机密性的关联数据 $d$ 一起被加密。很容易修改先加密再认证方法来处理这一点：只需先计算 $c \leftarrow \mathsf{Enc}_{k_E}(m)$，再计算 $t \leftarrow \mathsf{Mac}_{k_M}(d\|c)$。

### 5.3.2 Standardized Schemes　5.3.2 标准化方案

We close this chapter by briefly describing three AE schemes used in practice that are each inspired by one of the approaches discussed earlier. As usual, our aim here is not to provide an exact description of these schemes, but rather just a high-level understanding of the constructions.

我们通过简要描述实践中使用的三种 AE 方案来结束本章，每种方案都受到前面讨论的某种方法的启发。与往常一样，我们的目的不是提供这些方案的精确描述，而只是给出对其构造的高层次理解。

GCM (Galois/counter mode). GCM can be viewed as following the encrypt-then-authenticate paradigm, with CTR mode (cf. Section 3.6.3) as the underlying encryption scheme and GMAC (cf. Section 4.5.2) as the underlying message authentication code. The main differences from the generic combination described in the previous section are that (1) the keys used for encryption and authentication are not independent and (2) the same IV is used both for CTR-mode encryption and as the nonce for GMAC. Both these changes can be proven secure for the particular way they are done by GCM.

GCM（Galois/计数器模式，Galois/counter mode）。GCM 可被视为遵循先加密再认证范式，以 CTR 模式（参见 3.6.3 节）作为底层加密方案，以 GMAC（参见 4.5.2 节）作为底层消息认证码。与上一节描述的通用组合相比，主要区别在于：(1) 用于加密和认证的密钥不是独立的；(2) 同一个 IV 既用于 CTR 模式加密，也作为 GMAC 的 nonce。对于 GCM 所采用的特定方式，这两个改动都可以被证明是安全的。

One important property to be aware of when using GCM is that if the IV ever repeats, then not only does secrecy fail for the two messages encrypted using the same IV, but integrity of the scheme may be completely broken. This is due to a property of GMAC discussed in Exercise 4.21. For this reason, great care must be taken to ensure that IVs do not repeat when using GCM.

使用 GCM 时需要注意的一个重要性质是：如果 IV 重复，那么不仅使用同一 IV 加密的两条消息的机密性会失效，方案的完整性也可能被完全破坏。这是由习题 4.21 中讨论的 GMAC 的一个性质导致的。因此，在使用 GCM 时必须格外小心，以确保 IV 不重复。

When GCM is instantiated with the AES block cipher (see Section 7.2.5) it is extremely fast on most modern processors due to dedicated hardware instructions for both AES and the field operations used in GMAC. The scheme is also highly parallelizable.

当 GCM 用 AES 分组密码（见 7.2.5 节）实例化时，由于 AES 和 GMAC 中使用的域运算都有专用硬件指令，它在大多数现代处理器上极其快速。该方案还高度可并行化。

CCM (Counter with CBC-MAC). CCM follows the authenticate-then-encrypt approach, with CTR mode as the underlying encryption scheme and CBC-MAC (cf. Section 4.4.1) as the underlying message authentication code. Moreover, the same key k is used for both. Although—as discussed in the previous section—the authenticate-then-encrypt approach is not secure in general, and problems can occur when the keys used for encryption and authentication are not independent, CCM itself can be proven secure.

CCM（带 CBC-MAC 的计数器模式，Counter with CBC-MAC）。CCM 遵循先认证再加密方法，以 CTR 模式作为底层加密方案，以 CBC-MAC（参见 4.4.1 节）作为底层消息认证码。此外，二者使用同一个密钥 $k$。尽管如上一节所讨论的——先认证再加密方法一般而言并不安全，并且当加密和认证所用的密钥不独立时可能出现问题——但 CCM 本身可以被证明是安全的。

Because CCM relies only on a block cipher using a single key, it is easy to implement. However, CCM is relatively slow (it requires two block-cipher evaluations per plaintext block) and cannot be fully parallelized. In addition, it does not work in an on-line fashion, since it requires the message length to be known before encryption begins. (This is because the length is prepended to the message before CBC-MAC is computed, as discussed in Section 4.4.1.)

由于 CCM 只依赖使用单一密钥的分组密码，它易于实现。然而，CCM 相对较慢（每个明文块需要两次分组密码求值），并且无法完全并行化。此外，它不能以在线方式工作，因为它要求在加密开始前就知道消息长度。（这是因为长度在计算 CBC-MAC 之前被加在消息前面，如 4.4.1 节所讨论的。）

ChaCha20–Poly1305. This scheme relies on the encrypt-then-authenticate approach, where the underlying encryption is done using the stream cipher ChaCha20 (cf. Section 7.1.5) in unsynchronized mode (cf. Section 3.6.2) and the MAC used is Poly1305 (cf. Section 4.5.2) with ChaCha20 used here to instantiate the pseudorandom function. This scheme is extremely fast in software, and is becoming the method of choice on platforms where the dedicated hardware instructions used by GCM are not available.

ChaCha20–Poly1305。该方案依赖先加密再认证方法，其中底层加密使用流密码 ChaCha20（参见 7.1.5 节）以非同步模式（参见 3.6.2 节）完成，所用的 MAC 是 Poly1305（参见 4.5.2 节），其中用 ChaCha20 来实例化伪随机函数。该方案在软件上极其快速，正成为不具备 GCM 所用专用硬件指令的平台上的首选方法。

## 5.4 Secure Communication Sessions　5.4 安全通信会话

We briefly describe the application of authenticated encryption to the setting of two parties who wish to communicate “securely”—namely, with joint secrecy and integrity—over the course of a communication session. (For the purposes of this section, a communication session is simply a period of time during which the communicating parties maintain state.) In our treatment here we are deliberately informal; a formal definition is quite involved, and this topic arguably lies more in the area of network security than cryptography.

我们简要描述认证加密在如下场景中的应用：两方希望在一次通信会话的过程中“安全地”通信——即同时具有机密性和完整性。（就本节而言，通信会话就是通信各方维持状态的一段时间。）我们在这里有意采用非正式的处理；形式化的定义相当复杂，而且这个主题可以说更多属于网络安全而非密码学的范畴。

Let $\Pi = (\mathsf{Enc}, \mathsf{Dec})$ be an authenticated encryption scheme. Consider two parties $A$ and $B$ who share a key $k$ and wish to use this key to secure their communication over the course of a session. The obvious thing to do here is to use $\Pi$: Whenever, say, $A$ wants to transmit a message $m$ to $B$, she computes $c \leftarrow \mathsf{Enc}_k(m)$ and sends $c$ to $B$; in turn, $B$ decrypts $c$ to recover the result (ignoring the result if decryption returns $\perp$). Likewise, the same procedure is followed when $B$ wants to send a message to $A$. This simple approach, however, is vulnerable to various potential attacks:

设 $\Pi = (\mathsf{Enc}, \mathsf{Dec})$ 是一个认证加密方案。考虑共享密钥 $k$ 的两方 $A$ 和 $B$，他们希望在一次会话的过程中使用该密钥来保护其通信。这里显而易见的做法是使用 $\Pi$：每当 $A$ 想要向 $B$ 传输消息 $m$ 时，她计算 $c \leftarrow \mathsf{Enc}_k(m)$ 并将 $c$ 发送给 $B$；相应地，$B$ 解密 $c$ 以恢复结果（如果解密返回 $\perp$ 则忽略结果）。同样，当 $B$ 想要向 $A$ 发送消息时也遵循相同的过程。然而，这种简单的方法容易受到多种潜在攻击：

Re-ordering attack: An attacker can swap the order of messages. For example, if $A$ transmits $c_1$ (an encryption of $m_1$) and subsequently transmits $c_2$ (an encryption of $m_2$), an attacker who has some control over the network can deliver $c_2$ before $c_1$ and thus cause $B$ to output the messages in the wrong order.

重排攻击（re-ordering attack）：攻击者可以交换消息的顺序。例如，如果 $A$ 发送 $c_1$（$m_1$ 的加密），随后发送 $c_2$（$m_2$ 的加密），对网络有一定控制能力的攻击者可以先于 $c_1$ 投递 $c_2$，从而导致 $B$ 以错误顺序输出消息。

Replay attack: An attacker can replay a (valid) ciphertext c sent previously by one of the parties. This would cause one party to output a message twice, even though the other party only sent it once.

重放攻击（replay attack）：攻击者可以重放先前由某一方发送的（有效的）密文 $c$。这将导致一方把某条消息输出两次，即使另一方只发送过一次。

Message-dropping attack: An attacker may drop some of the messages sent between A and B. Although nothing can prevent the attacker from doing this, we might at least hope that such behavior would be detected by the parties.

消息丢弃攻击（message-dropping attack）：攻击者可能丢弃 A 和 B 之间发送的某些消息。虽然没有任何办法能阻止攻击者这样做，但我们至少希望这种行为能被各方检测到。

Reflection attack: An attacker can take a ciphertext c sent from A to B and send it back to A. This would cause A to output a message m, even though B never sent such a message.

反射攻击（reflection attack）：攻击者可以截取从 $A$ 发送给 $B$ 的密文 $c$，并将其发回给 $A$。这将导致 $A$ 输出某条消息 $m$，即使 $B$ 从未发送过这样的消息。

The above list of attacks is not exhaustive, and is just an example of some of the challenges involved in achieving secure communication.

上述攻击列表并非详尽无遗，只是实现安全通信所涉及挑战的一些示例。

The above attacks can be addressed using counters to handle the first three and a directionality bit to prevent the fourth. $^2$ We describe these in tandem. Each party maintains two counters $\mathsf{ctr}_{A,B}$ and $\mathsf{ctr}_{B,A}$ keeping track of the number of messages sent from $A$ to $B$ (resp., $B$ to $A$) during the session. These counters are initialized to 0 and incremented each time a party sends or receives a (valid) message. The parties also agree on a bit $b_{A,B}$, and define $b_{B,A}$ to be its complement. (One way to do this is to set $b_{A,B} = 0$ iff the identity of $A$ is lexicographically smaller than the identity of $B$.)

要应对上述攻击，可以用计数器处理前三种攻击，并用一个方向比特防止第四种。$^2$ 我们一并描述这些机制。每一方维护两个计数器 $\mathsf{ctr}_{A,B}$ 和 $\mathsf{ctr}_{B,A}$，分别记录会话期间从 $A$ 发送到 $B$（以及从 $B$ 发送到 $A$）的消息数目。这些计数器被初始化为 0，并在每次一方发送或接收一条（有效的）消息时递增。双方还商定一个比特 $b_{A,B}$，并定义 $b_{B,A}$ 为其补。（一种做法是当且仅当 $A$ 的身份按字典序小于 $B$ 的身份时令 $b_{A,B} = 0$。）

$^{2}$ In practice, reflection attacks are often solved by simply having separate keys for each direction (i.e., the parties use a key $k_A$ for messages sent from $A$ to $B$, and an independent key $k_B$ for messages sent from $B$ to $A$).

$^{2}$ 在实践中，反射攻击通常通过为每个方向使用独立的密钥来解决（即各方对从 $A$ 发送到 $B$ 的消息使用密钥 $k_A$，对从 $B$ 发送到 $A$ 的消息使用独立的密钥 $k_B$）。

When $A$ wants to transmit a message $m$ to $B$, she computes the ciphertext $c \leftarrow \mathsf{Enc}_k(b_{A,B} \|\mathsf{ctr}_{A,B}\|m)$ and sends $c$; she then increments $\mathsf{ctr}_{A,B}$. Upon receiving $c$, party $B$ decrypts; if the result is $\perp$, he immediately rejects. Otherwise, he parses the decrypted message as $b\|\mathsf{ctr}\|m$. If $b = b_{A,B}$ and $\mathsf{ctr} = \mathsf{ctr}_{A,B}$, then $B$ outputs $m$ and increments $\mathsf{ctr}_{A,B}$; otherwise, $B$ rejects. The above steps, $\text{mutatis mutandis}$, are applied when $B$ sends a message to $A$.

当 $A$ 想要向 $B$ 传输消息 $m$ 时，她计算密文 $c \leftarrow \mathsf{Enc}_k(b_{A,B} \|\mathsf{ctr}_{A,B}\|m)$ 并发送 $c$；然后她递增 $\mathsf{ctr}_{A,B}$。收到 $c$ 后，$B$ 进行解密；如果结果为 $\perp$，他立即拒绝。否则，他将解密后的消息解析为 $b\|\mathsf{ctr}\|m$。如果 $b = b_{A,B}$ 且 $\mathsf{ctr} = \mathsf{ctr}_{A,B}$，则 $B$ 输出 $m$ 并递增 $\mathsf{ctr}_{A,B}$；否则 $B$ 拒绝。当 $B$ 向 $A$ 发送消息时，应用上述步骤并作必要的相应变更（mutatis mutandis）。

### References and Additional Reading　参考文献与延伸阅读

Chosen-ciphertext attacks (in the context of public-key encryption) were first formally defined by Naor and Yung [147] and Rackoff and Simon [168], and have received much subsequent attention as well [17, 68, 112]. The padding-oracle attack originated in the work of Vaudenay [199].

选择密文攻击（在公钥加密的语境下）最早由 Naor 和 Yung [147] 以及 Rackoff 和 Simon [168] 形式化定义，并在随后受到广泛关注 [17, 68, 112]。填充预言机攻击起源于 Vaudenay [199] 的工作。

The importance of authenticated encryption was first explicitly highlighted by Katz and Yung [111] and Bellare and Namprempre [21]. Definition 5.4 is due to Shrimpton [184], who also proves Theorem 5.5. Bellare and Namprempre [21] analyze the three generic approaches discussed here, though the idea of using encrypt-then-authenticate for achieving CCA-security goes back at least to the work of Dolev et al. [68]. Krawczyk [122] examines other methods for achieving secrecy and authentication, and also analyzes specific instantiations of the authenticate-then-encrypt approach.

认证加密的重要性最早由 Katz 和 Yung [111] 以及 Bellare 和 Namprempre [21] 明确强调。定义 5.4 归功于 Shrimpton [184]，他还证明了定理 5.5。Bellare 和 Namprempre [21] 分析了这里讨论的三种通用方法，尽管使用先加密再认证来实现 CCA 安全性的思想至少可追溯到 Dolev 等人 [68] 的工作。Krawczyk [122] 研究了实现机密性与认证的其他方法，并分析了先认证再加密方法的若干具体实例化。

GCM is due to McGrew and Viega [136]. CCM was proposed by Whiting, Housley, and Ferguson [204] and proven secure by Jonsson [104]. ChaCha20-Poly1305 is specified in RFC 8439 [154].

GCM 归功于 McGrew 和 Viega [136]。CCM 由 Whiting、Housley 和 Ferguson [204] 提出并由 Jonsson [104] 证明了安全性。ChaCha20-Poly1305 在 RFC 8439 [154] 中规定。

### Exercises　习题

5.1 Show that the CBC, OFB, and CTR modes of operation do not give CCA-secure encryption schemes.

5.1 证明 CBC、OFB 和 CTR 工作模式不能给出 CCA 安全的加密方案。

5.2 Write pseudocode for obtaining the entire plaintext for a 3-block ciphertext via a padding-oracle attack on CBC-mode encryption using PKCS #7 padding, as sketched in the text.

5.2 如正文所述，写出针对使用 PKCS #7 填充的 CBC 模式加密进行填充预言机攻击、从而从一个 3 分组的密文获得整个明文的伪代码。

5.3 Describe a padding-oracle attack on CTR-mode encryption, assuming PKCS #7 padding is used to pad messages to a multiple of the block length before encrypting.

5.3 描述针对 CTR 模式加密的填充预言机攻击，假设在加密前使用 PKCS #7 填充将消息填充为分组长度的整数倍。

5.4 Show that Construction 5.6 is not necessarily CCA-secure if it is instantiated with a secure MAC that is not strongly secure.

5.4 证明如果用安全的但非强安全的 MAC 来实例化构造 5.6，则它不一定是 CCA 安全的。

5.5 Prove that Construction 5.6 is unforgeable when instantiated with any encryption scheme (even if not CPA-secure) and any secure MAC (even if not strongly secure).

5.5 证明当用任意加密方案（即使不是 CPA 安全的）和任意安全的 MAC（即使不是强安全的）实例化时，构造 5.6 是不可伪造的。

5.6 Consider a strengthened version of unforgeability where $\mathcal{A}$ is additionally given access to a decryption oracle.

5.6 考虑不可伪造性的一个加强版本，其中 $\mathcal{A}$ 额外被授予对解密预言机的访问。

(a) Write a formal definition for this version of unforgeability.

(a) 写出这一版本不可伪造性的形式化定义。

(b) Prove that Construction 5.6 satisfies this stronger definition if $\Pi_{M}$ is a strongly secure MAC.

(b) 证明如果 $\Pi_{M}$ 是强安全的 MAC，则构造 5.6 满足这一更强的定义。

(c) Show by counterexample that Construction 5.6 need not satisfy this stronger definition if $\Pi_{M}$ is a secure MAC that is not strongly secure. (Compare to the previous exercise.)

(c) 用反例证明如果 $\Pi_{M}$ 是安全的但非强安全的 MAC，则构造 5.6 不一定满足这一更强的定义。（与前一习题比较。）

5.7 Prove that the authenticate-then-encrypt approach, instantiated with any CPA-secure encryption scheme and any secure MAC, yields a CPA-secure encryption scheme that is unforgeable.

5.7 证明先认证再加密方法用任意 CPA 安全的加密方案和任意安全的 MAC 实例化后，得到一个不可伪造的 CPA 安全加密方案。

5.8 Let $F$ be a strong pseudorandom permutation, and define a fixed-length encryption scheme (Enc, Dec) as follows: On input $m \in \{0,1\}^{n/2}$ and key $k \in \{0,1\}^{n}$, algorithm $\mathsf{Enc}$ chooses a uniform string $r \in \{0,1\}^{n/2}$ of length $n/2$ and computes $c := F_k(r\|m)$.

5.8 设 $F$ 是一个强伪随机置换，定义固定长度加密方案 (Enc, Dec) 如下：输入 $m \in \{0,1\}^{n/2}$ 和密钥 $k \in \{0,1\}^{n}$，算法 $\mathsf{Enc}$ 选择一个长度为 $n/2$ 的均匀字符串 $r \in \{0,1\}^{n/2}$，并计算 $c := F_k(r\|m)$。

Show how to decrypt, and prove that this scheme is CCA-secure for messages of length n/2.

说明如何解密，并证明该方案对于长度为 n/2 的消息是 CCA 安全的。

5.9 Show that the scheme in the previous exercise is not an authenticated encryption scheme.

5.9 证明上一习题中的方案不是认证加密方案。

5.10 Show a CPA-secure private-key encryption scheme that is unforgeable but is not CCA-secure.

5.10 给出一个 CPA 安全的私钥加密方案，它是不可伪造的但不是 CCA 安全的。
