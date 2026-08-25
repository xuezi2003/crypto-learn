# Chapter 5: CCA-Security and Authenticated Encryption　第五章　CCA 安全性与认证加密

In previous chapters we studied two different notions of security for parties communicating over an open communication channel. In Chapter 3 we focused on the goal of secrecy against a passive adversary who simply eavesdrops on the parties' communication, and showed CPA-secure encryption schemes realizing this goal. In Chapter 4 we explored integrity against an active adversary who can inject messages on the channel or otherwise tamper with the parties' communication, and described how message authentication codes can be used to achieve this notion. We consider the missing piece—secrecy in the presence of an active adversary—in Section 5.1, and introduce the relevant notion of CCA-security there. Beginning in Section 5.2, we then consider the natural question of how to construct encryption schemes that achieve both secrecy and integrity simultaneously.

在前几章中，我们研究了各方在开放通信信道上通信时的两种不同安全概念。在第 3 章中，我们关注的是针对仅窃听各方通信的被动敌手的机密性目标，并展示了实现该目标的 CPA 安全加密方案。在第 4 章中，我们探讨了针对能够在信道上注入消息或以其他方式篡改各方通信的活跃敌手的完整性，并描述了如何使用消息认证码来实现这一概念。我们将在 5.1 节考虑缺失的一环——活跃敌手存在下的机密性——并在那里引入 CCA 安全性的相关概念。从 5.2 节开始，我们接着考虑一个自然的问题：如何构造同时实现机密性和完整性的加密方案。

## 5.1 Chosen-Ciphertext Attacks and CCA-Security　5.1 选择密文攻击与 CCA 安全性

We have so far considered encryption schemes secure only against passive (eavesdropping) adversaries. (Even though chosen-plaintext attacks allow an adversary to control what gets encrypted, the adversary in that setting is still limited to passively observing ciphertexts transmitted by the honest parties.) In the previous chapter, we discussed the importance of also defending against active attackers who may interfere with or modify the communication between the honest parties, focusing there on the case of message integrity. What might the effect of active attacks be when it comes to secrecy?

迄今为止，我们考虑的加密方案仅针对被动（窃听）敌手是安全的。（尽管选择明文攻击允许敌手控制被加密的内容，但在该场景下敌手仍仅限于被动观察诚实方传输的密文。）在上一章中，我们讨论了防御可能干扰或修改诚实方之间通信的活跃攻击者的重要性，当时重点关注的是消息完整性的情形。当涉及机密性时，主动攻击可能产生什么影响呢？

Consider a scenario in which a sender encrypts a message $m$ and then transmits the resulting ciphertext $c$. An attacker who can tamper with the communication can modify $c$ to generate another ciphertext $c^{\prime}$ that is received by the other party. This receiver will then decrypt $c^{\prime}$ to obtain a message $m^{\prime}$. If $m^{\prime} \neq m$ (and $m^{\prime} \neq \bot$), this is a violation of integrity. What is of interest to us here, however, is the potential impact on secrecy. In particular, if the attacker learns partial information about $m^{\prime}$—say, from subsequent behavior of the receiver—might that reveal information about the original message $m$?

考虑这样一个场景：发送方加密消息 $m$，然后传输所得密文 $c$。能够篡改通信的攻击者可以修改 $c$，生成另一个被另一方接收的密文 $c^{\prime}$。该接收方随后解密 $c^{\prime}$ 得到消息 $m^{\prime}$。如果 $m^{\prime} \neq m$（且 $m^{\prime} \neq \bot$），就构成了对完整性的破坏。然而，我们在此感兴趣的是对机密性的潜在影响。特别地，如果攻击者获知了关于 $m^{\prime}$ 的部分信息——比如说，从接收方的后续行为中——这是否会泄露关于原始消息 $m$ 的信息？

This type of attack, in which an adversary causes a receiver to decrypt ciphertexts that the adversary generates, is called a chosen-ciphertext attack. Chosen-ciphertext attacks are possible, in principle, any time an attacker has the ability to inject traffic on the channel between the sender and receiver. There are many scenarios in which this can occur. (See also the discussion in Section 12.2.3 regarding chosen-ciphertext attacks in the public-key setting.) In the Midway example from Section 3.4.2, for example, US cryptanalysts could have sent encrypted messages containing the fragment AF to the Japanese; by monitoring their subsequent behavior (e.g., movement of troops and the like), the US could have learned information about what AF meant.

敌手致使接收方解密由其自身生成的密文，这类攻击称为选择密文攻击（chosen-ciphertext attack）。原则上，只要攻击者有能力在发送方与接收方之间的信道上注入流量，选择密文攻击就是可能的。有许多场景会发生这种情况。（另见 12.2.3 节关于公钥设置下选择密文攻击的讨论。）例如，在 3.4.2 节的中途岛（Midway）例子中，美国密码分析人员本可以向日本人发送包含片段 AF 的加密消息；通过监视他们随后的行为（例如部队调动之类），美国本可以获知关于 AF 含义的信息。

Alternatively, imagine a client sending encrypted messages to a server. If an adversary can impersonate the client and send ciphertexts to the server that appear to originate from the client, the server will decrypt those ciphertexts and the adversary may learn something about the result; for example, the attacker may be able to deduce when a ciphertext decrypts to an ill-formed plaintext (e.g., one that is not formatted correctly) based on the server's reaction (e.g., if the server sends an error message). In Section 5.1.1 we describe in detail an attack of exactly this sort where an attacker is able to leverage the information leaked from these decryptions to learn the entire contents of some other encrypted message! Such attacks have been carried out in practice on web servers to learn the contents of encrypted TLS sessions.

或者，设想一个客户端向服务器发送加密消息。如果敌手可以冒充客户端，向服务器发送看似源自客户端的密文，服务器将解密这些密文，而敌手可能获知关于解密结果的某些信息；例如，攻击者可能能够根据服务器的反应（例如服务器是否发送错误消息）推断出某个密文何时解密为格式错误的明文（即格式不正确的明文）。在 5.1.1 节中，我们将详细描述一种正是此类的攻击：攻击者能够利用从这些解密中泄露的信息，来获知另一条加密消息的全部内容！此类攻击已在实践中针对 Web 服务器实施，用于获知加密 TLS 会话的内容。

### 5.1.1 Padding-Oracle Attacks　5.1.1 填充预言机攻击

We motivate the importance of security against chosen-ciphertext attacks by showing a real-world example where such attacks can be devastating. We consider a setting in which a client sends messages encrypted using CBC-mode encryption to a server. We assume the attacker can impersonate the client and send ciphertexts of its choice to the server, which the server will then decrypt. We assume further that the attacker can tell when the resulting decrypted messages are valid (in a sense we will define below) or not. Such information is frequently easy to obtain since, for example, the server might request retransmission or terminate a session if it receives a ciphertext that does not decrypt correctly, and either of those events would be detectable by the attacker. The attack has been shown to work in practice on various deployed protocols.

我们通过展示一个此类攻击可能造成毁灭性后果的真实世界例子，来阐明抗选择密文攻击安全性的重要性。我们考虑这样一个场景：客户端向服务器发送使用 CBC 模式加密的消息。我们假设攻击者可以冒充客户端，向服务器发送其选择的密文，服务器随后会解密这些密文。我们进一步假设攻击者能够判断解密得到的消息是否有效（其含义将在下文中定义）。此类信息通常很容易获得，因为例如服务器在收到无法正确解密的密文时可能会要求重传或终止会话，而这些事件中的任何一个都可以被攻击者检测到。该攻击已被证明在实践中对多种已部署的协议有效。

In our discussion of CBC-mode encryption in Section 3.6.3, we only dealt with the case where the message length was a multiple of the block length of the underlying block cipher $F$. If a message does not satisfy this property, it must be padded before CBC mode is applied; we refer to the result after padding as the encoded data. The padding must allow the receiver to unambiguously recover the original message from the encoded data. One popular padding scheme is defined by the PKCS #7 standard, and works as follows. Assume the original message has an integral number of bytes, and let L denote the block length (in bytes) of the block cipher $F$. Let b > 0 denote the number of bytes that need to be appended to the message in order to make the total length of the resulting encoded data a multiple of the block length. Then we append to the message the integer $b$ (represented in one byte, i.e., two hexadecimal digits) repeated $b$ times. That is, if one byte of padding is needed then the 1-byte string $\mathtt{0x01}$ (written in hexadecimal) is appended; if four bytes of padding are needed then $\mathtt{0x04040404}$ is appended; etc. (Note that $b$ is an integer between 1 and $L$, inclusive—we cannot have $b = 0$ since this would lead to ambiguous padding. Thus, if the original message length is already a multiple of the block length, then $b = L$.) After padding, the encoded data is encrypted using regular CBC-mode encryption.

在 3.6.3 节对 CBC 模式加密的讨论中，我们只处理了消息长度是底层分组密码 $F$ 的分组长度整数倍的情形。如果消息不满足这一性质，则在应用 CBC 模式之前必须对其进行填充；我们将填充后的结果称为编码数据。填充必须使接收方能够从编码数据中无歧义地恢复原始消息。一种流行的填充方案由 PKCS #7 标准定义，其工作方式如下。假设原始消息由整数个字节组成，令 L 表示分组密码 $F$ 的分组长度（以字节计）。令 b > 0 表示为使所得编码数据的总长度成为分组长度整数倍而需要追加到消息的字节数。然后我们向消息追加整数 $b$（用一个字节表示，即两个十六进制数字）重复 $b$ 次。也就是说，如果需要 1 字节填充，则追加 1 字节字符串 $\mathtt{0x01}$（以十六进制书写）；如果需要 4 字节填充，则追加 $\mathtt{0x04040404}$；依此类推。（注意，$b$ 是 1 到 $L$ 之间（含端点）的整数——不能有 $b = 0$，因为这会导致填充歧义。因此，如果原始消息长度已经是分组长度的整数倍，则 $b = L$。）填充之后，使用常规的 CBC 模式加密对编码数据进行加密。

When decrypting, the server first uses CBC-mode decryption as usual to recover the encoded data, and then checks whether the encoded data is correctly padded. (This is easily done: simply read the value $b$ of the final byte and then verify that the final $b$ bytes of the result all have value $b$). If so, the padding is stripped off and the original message returned. Otherwise, the standard procedure is to return a “bad padding” error. This means the server is serving as a “padding oracle” for the adversary: i.e., the adversary can send an arbitrary ciphertext to the server and learn (based on whether a “bad padding” error is returned) whether the underlying encoded data is padded correctly or not. Although this may seem like meaningless information, we show that it enables an adversary to completely recover the original message corresponding to any ciphertext of its choice.

解密时，服务器首先照常使用 CBC 模式解密来恢复编码数据，然后检查编码数据的填充是否正确。（这很容易做到：只需读取最后一个字节的值 $b$，然后验证结果的最后 $b$ 个字节的值是否都为 $b$。）如果是，则剥离填充并返回原始消息。否则，标准过程是返回一个“填充错误”（bad padding）。这意味着服务器正在为敌手充当一个“填充预言机”（padding oracle）：即敌手可以向服务器发送任意密文，并（根据是否返回“填充错误”）获知底层编码数据的填充是否正确。尽管这看似是毫无意义的信息，但我们证明它能使敌手完全恢复其选择的任意密文所对应的原始消息。

We describe the attack on a 3-block ciphertext for simplicity. Let $IV, c_1, c_2$ be a ciphertext observed by the attacker, and let $m_1, m_2$ be the underlying encoded data (unknown to the attacker) that corresponds to a padded message, as discussed above. (Each block is $L$ bytes long.) Note that

$$m_{2}=F_{k}^{-1}(c_{2})\oplus c_{1}\tag{5.1}$$

为简单起见，我们针对一个 3 分组的密文描述该攻击。设 $IV, c_1, c_2$ 为攻击者观察到的密文，设 $m_1, m_2$ 为如上所述对应于已填充消息的底层编码数据（攻击者未知）。（每个分组长 $L$ 字节。）注意

$$m_{2}=F_{k}^{-1}(c_{2})\oplus c_{1}\tag{5.1}$$

where $k$ is the key (which is, of course, not known to the attacker) being used by the honest parties. The second block $m_2$ ends in $\underbrace{\mathtt{0xb}\cdots\mathtt{0xb}}_{b\text{ times}}$ where we let $\mathtt{0xb}$ denote the 1-byte representation of some integer $b$. The key property used in the attack is that certain changes to the ciphertext yield predictable changes in the underlying encoded data after CBC-mode decryption. Specifically, let $c_1^{\prime}$ be identical to $c_1$ except for a modification in the final byte, and consider decryption of the modified ciphertext $IV, c_1^{\prime}, c_2$. This will result in encoded data $m_1^{\prime}, m_2^{\prime}$ where $m_2^{\prime} = F_k^{-1}(c_2) \oplus c_1^{\prime}$. Comparing to Equation (5.1) we see that $m_2^{\prime}$ will be identical to $m_2$ except for a modification in the final byte. (The value of $m_1^{\prime}$ is unpredictable, but this will not adversely affect the attack.) Similarly, if $c_1^{\prime}$ is the same as $c_1$ except for a change in its $i$th byte, then decryption of $IV, c_1^{\prime}, c_2$ will result in $m_1^{\prime}, m_2^{\prime}$ where $m_2^{\prime}$ is the same as $m_2$ except for a change in its $i$th byte. More generally, if $c_1^{\prime} = c_1 \oplus \Delta$ for any string $\Delta$, then decryption of $IV, c_1^{\prime}, c_2$ yields $m_1^{\prime}, m_2^{\prime}$ where $m_2^{\prime} = m_2 \oplus \Delta$. The upshot is that the attacker can exercise significant control over the final block of the encoded data.

其中 $k$ 是诚实方使用的密钥（攻击者当然不知道）。第二个分组 $m_2$ 以 $\underbrace{\mathtt{0xb}\cdots\mathtt{0xb}}_{b\text{ times}}$ 结尾，其中我们用 $\mathtt{0xb}$ 表示某个整数 $b$ 的 1 字节表示。攻击中利用的关键性质是：对密文的某些修改会导致 CBC 模式解密后底层编码数据发生可预测的变化。具体来说，设 $c_1^{\prime}$ 与 $c_1$ 相同，仅最后一个字节被修改，考虑对修改后的密文 $IV, c_1^{\prime}, c_2$ 的解密。这将得到编码数据 $m_1^{\prime}, m_2^{\prime}$，其中 $m_2^{\prime} = F_k^{-1}(c_2) \oplus c_1^{\prime}$。与式 (5.1) 比较可见，$m_2^{\prime}$ 将与 $m_2$ 相同，仅最后一个字节被修改。（$m_1^{\prime}$ 的值不可预测，但这不会对攻击产生不利影响。）类似地，如果 $c_1^{\prime}$ 与 $c_1$ 相同，仅第 $i$ 个字节有改动，那么对 $IV, c_1^{\prime}, c_2$ 的解密将得到 $m_1^{\prime}, m_2^{\prime}$，其中 $m_2^{\prime}$ 与 $m_2$ 相同，仅第 $i$ 个字节有改动。更一般地，如果对任意字符串 $\Delta$ 有 $c_1^{\prime} = c_1 \oplus \Delta$，那么对 $IV, c_1^{\prime}, c_2$ 的解密将得到 $m_1^{\prime}, m_2^{\prime}$，其中 $m_2^{\prime} = m_2 \oplus \Delta$。其结果是，攻击者可以对编码数据的最后一个分组施加显著的控制。

As a warmup, let us see how the adversary can exploit this to learn $b$, the amount of padding. (This reveals the length of the original message.) Recall that upon decryption, the server looks at the value $b$ of the final byte of the encoded data, and then verifies that the final $b$ bytes all have the same value. The attacker begins by modifying the first byte of $c_1$ and sending the resulting ciphertext $IV, c^{\prime}_1, c_2$ to the server. If decryption fails (i.e., the server returns an error) then it must be the case that the server is checking all $L$ bytes of $m^{\prime}_2$, and therefore $b = L$! Otherwise, the attacker learns that $b < L$, and it can then repeat the process with the second byte, and so on. The left-most modified byte for which decryption fails reveals exactly the left-most byte being checked by the server, and so reveals exactly $b$.

作为热身，让我们看看敌手如何利用这一点来获知填充量 $b$。（这会泄露原始消息的长度。）回忆一下，解密时服务器查看编码数据最后一个字节的值 $b$，然后验证最后 $b$ 个字节是否都具有相同的值。攻击者首先修改 $c_1$ 的第一个字节，并将所得密文 $IV, c^{\prime}_1, c_2$ 发送给服务器。如果解密失败（即服务器返回错误），那么服务器必定在检查 $m^{\prime}_2$ 的全部 $L$ 个字节，因此 $b = L$！否则，攻击者获知 $b < L$，然后可以对第二个字节重复此过程，依此类推。使解密失败的最左侧被修改字节，恰好揭示了服务器所检查的最左侧字节，从而恰好揭示了 $b$。

With $b$ known, the attacker can proceed to learn the bytes of the message one-by-one. We illustrate the idea for the final byte of the message, which we denote by $M$. The attacker knows that $m_2$ ends in $\mathtt{0x}M\,\mathtt{0xb}\cdots\mathtt{0xb}$ (with $\mathtt{0xb}$ repeated $b$ times) and wishes to learn $M$. For ${0} \leq i < 2^8$ define

$$\begin{aligned}\Delta_{i}&\overset{\mathrm{def}}{=}\mathtt{0x00}\cdots\mathtt{0x00}\,\mathtt{0x}i\,\overbrace{\mathtt{0x}(b+1)\cdots\mathtt{0x}(b+1)}^{{b}\text{ times}}\\&\oplus\mathtt{0x00}\cdots\mathtt{0x00}\,\mathtt{0x00}\,\overbrace{\mathtt{0xb}\cdots\mathtt{0xb}}^{{b}\text{ times}};\end{aligned}$$

已知 $b$ 后，攻击者可以逐字节地获知消息的各个字节。我们以消息的最后一个字节为例说明这一思想，将其记为 $M$。攻击者知道 $m_2$ 以 $\mathtt{0x}M\,\mathtt{0xb}\cdots\mathtt{0xb}$ 结尾（其中 $\mathtt{0xb}$ 重复 $b$ 次），并希望获知 $M$。对 ${0} \leq i < 2^8$ 定义

$$\begin{aligned}\Delta_{i}&\overset{\mathrm{def}}{=}\mathtt{0x00}\cdots\mathtt{0x00}\,\mathtt{0x}i\,\overbrace{\mathtt{0x}(b+1)\cdots\mathtt{0x}(b+1)}^{{b}\text{ times}}\\&\oplus\mathtt{0x00}\cdots\mathtt{0x00}\,\mathtt{0x00}\,\overbrace{\mathtt{0xb}\cdots\mathtt{0xb}}^{{b}\text{ times}};\end{aligned}$$

i.e., the final $b+1$ bytes of $\Delta_i$ contain the integer $i$ (in hexadecimal) followed by the value $(b+1) \oplus b$ (in hexadecimal) repeated $b$ times. If the attacker submits the ciphertext $IV, c_1 \oplus \Delta_i, c_2$ to the server then, after CBC-mode decryption, the final $b+1$ bytes of the resulting encoded data will equal $\mathtt{0x}(M \oplus i)\,\mathtt{0x}(b+1)\cdots\mathtt{0x}(b+1)$ (with $\mathtt{0x}(b+1)$ repeated $b$ times), and decryption will fail unless $\mathtt{0x}(M \oplus i) = \mathtt{0x}(b+1)$. The attacker tries at most ${2}^8$ values $\Delta_0, \ldots, \Delta_{2^8-1}$ until decryption succeeds for some $\Delta_i$, at which point it learns that $M = \mathtt{0x}(b+1) \oplus \mathtt{0x}i$. We leave it as an exercise to extend this attack so as to learn the next byte of $m_2$, as well as all of $m_1$.

即 $\Delta_i$ 的最后 $b+1$ 个字节包含整数 $i$（以十六进制表示），后接值 $(b+1) \oplus b$（以十六进制表示）重复 $b$ 次。如果攻击者向服务器提交密文 $IV, c_1 \oplus \Delta_i, c_2$，那么经过 CBC 模式解密后，所得编码数据的最后 $b+1$ 个字节将等于 $\mathtt{0x}(M \oplus i)\,\mathtt{0x}(b+1)\cdots\mathtt{0x}(b+1)$（其中 $\mathtt{0x}(b+1)$ 重复 $b$ 次），并且除非 $\mathtt{0x}(M \oplus i) = \mathtt{0x}(b+1)$，否则解密将失败。攻击者最多尝试 ${2}^8$ 个值 $\Delta_0, \ldots, \Delta_{2^8-1}$，直到某个 $\Delta_i$ 解密成功，此时它便获知 $M = \mathtt{0x}(b+1) \oplus \mathtt{0x}i$。至于如何扩展这一攻击以获知 $m_2$ 的下一个字节乃至整个 $m_1$，我们留作练习。

A padding-oracle attack on CAPTCHAs. We have already mentioned that padding-oracle attacks have been carried out on encrypted web traffic. Here we give a second example.

针对 CAPTCHA 的填充预言机攻击。我们已经提到，填充预言机攻击已针对加密的 Web 流量实施过。这里我们给出第二个例子。

A CAPTCHA is a distorted image of, say, an English word that is easy for humans to read, but hard for a computer to process. CAPTCHAs are used in order to ensure that a human user—and not some automated software—is interacting with a webpage.

CAPTCHA（验证码）是诸如一个英文单词的扭曲图像，人类容易辨认，而计算机难以处理。CAPTCHA 用于确保与网页交互的是人类用户——而不是某种自动化软件。

CAPTCHAs can be provided as a separate service run on an independent server. To see how this works, we denote a web server by $\mathcal{S}_W$, a CAPTCHA server by $\mathcal{S}_C$, and a user by $\mathcal{U}$. When $\mathcal{U}$ loads a webpage served by $\mathcal{S}_W$, the following events occur: $\mathcal{S}_W$ encrypts a random English word $w$ using a key $k$ that was initially shared between $\mathcal{S}_W$ and $\mathcal{S}_C$, and sends the resulting ciphertext (along with the webpage) to the user. $\mathcal{U}$ forwards the ciphertext to $\mathcal{S}_C$, who decrypts it, obtains $w$, and renders a distorted image of $w$ (i.e., the CAPTCHA) to $\mathcal{U}$. Finally, $\mathcal{U}$ sends $w$ back to $\mathcal{S}_W$ for verification. Note that $\mathcal{S}_C$ decrypts any ciphertext it receives from $\mathcal{U}$ and will issue a “bad padding” error message if decryption fails, as described earlier. This presents $\mathcal{U}$ with an opportunity to carry out a padding-oracle attack, and thus to solve the CAPTCHA (i.e., to determine $w$) automatically without any human involvement, rendering the CAPTCHA ineffective.

CAPTCHA 可以作为一项独立服务在单独的服务器上提供。为说明其工作方式，我们用 $\mathcal{S}_W$ 表示 Web 服务器，用 $\mathcal{S}_C$ 表示 CAPTCHA 服务器，用 $\mathcal{U}$ 表示用户。当 $\mathcal{U}$ 加载由 $\mathcal{S}_W$ 提供的网页时，会发生以下事件：$\mathcal{S}_W$ 使用最初在 $\mathcal{S}_W$ 与 $\mathcal{S}_C$ 之间共享的密钥 $k$ 加密一个随机英文单词 $w$，并将所得密文（连同网页）发送给用户。$\mathcal{U}$ 将该密文转发给 $\mathcal{S}_C$，后者解密得到 $w$，并将 $w$ 的扭曲图像（即 CAPTCHA）呈现给 $\mathcal{U}$。最后，$\mathcal{U}$ 将 $w$ 发回给 $\mathcal{S}_W$ 进行验证。注意，$\mathcal{S}_C$ 会解密它从 $\mathcal{U}$ 收到的任何密文，并在解密失败时如前所述发出“填充错误”消息。这给 $\mathcal{U}$ 提供了实施填充预言机攻击的机会，从而可以在没有任何人工参与的情况下自动破解 CAPTCHA（即确定 $w$），使 CAPTCHA 失效。

### 5.1.2 Defining CCA-Security　5.1.2 CCA 安全性的定义

What would it mean for an encryption scheme to be secure against chosen-ciphertext attacks? As usual, to define an appropriate notion of security we need to define two things: the assumed abilities of the attacker, and what constitutes a successful attack. For the latter, we will follow the approach we have taken in several previous definitions of security for encryption (e.g., in Definitions 3.8 and 3.21): namely, we give the attacker a challenge ciphertext $c$ that is generated by encrypting one of two possible messages $m_0, m_1$ (each chosen with equal probability), and consider the scheme to be broken if the attacker can determine which message was encrypted with probability significantly better than 1/2.

加密方案抗选择密文攻击安全意味着什么？与往常一样，要定义一个恰当的安全概念，我们需要定义两件事：假定的攻击者能力，以及什么构成一次成功的攻击。对于后者，我们将遵循之前在加密的若干安全定义中采用的方法（例如定义 3.8 和 3.21）：即我们给攻击者一个挑战密文 $c$，它是对两个可能消息 $m_0, m_1$ 之一（各自以等概率选择）加密生成的；如果攻击者能够以显著优于 1/2 的概率确定哪个消息被加密，我们就认为方案被攻破。

How should we model the attacker's capabilities in the present setting? Now, the adversary should have the ability not only to obtain the encryption of messages of its choice (as in a chosen-plaintext attack), but also to obtain the decryption of ciphertexts of its choice (with one exception discussed later). Formally, we give the adversary access to a decryption oracle $\mathsf{Dec}_k(\cdot)$ in addition to an encryption oracle $\mathsf{Enc}_k(\cdot)$. We present the formal definition and defer further discussion.

在当前场景下，我们应如何建模攻击者的能力？现在，敌手不仅应能够获取其选择消息的加密（如选择明文攻击中那样），还应能够获取其选择密文的解密（有一个例外，稍后讨论）。形式化地，我们在加密预言机 $\mathsf{Enc}_k(\cdot)$ 之外，还赋予敌手对解密预言机 $\mathsf{Dec}_k(\cdot)$ 的访问权限。我们先给出形式化定义，进一步的讨论稍后进行。

Consider the following experiment for any private-key encryption scheme $\Pi = (\mathsf{Gen}, \mathsf{Enc}, \mathsf{Dec})$, adversary $\mathcal{A}$, and value $n$ for the security parameter.

考虑以下关于任意私钥加密方案 $\Pi = (\mathsf{Gen}, \mathsf{Enc}, \mathsf{Dec})$、敌手 $\mathcal{A}$ 以及安全参数取值 $n$ 的实验。

The CCA indistinguishability experiment $\mathsf{PrivK}_{A,\Pi}^{\mathsf{cca}}(n)$:
CCA 不可区分性实验 $\mathsf{PrivK}_{A,\Pi}^{\mathsf{cca}}(n)$：

1. A key k is generated by running $\mathsf{Gen}(1^n)$.

   通过运行 $\mathsf{Gen}(1^n)$ 生成密钥 $k$。

2. $\mathcal{A}$ is given input ${1}^n$ and oracle access to $\mathsf{Enc}_k(\cdot)$ and $\mathsf{Dec}_k(\cdot)$. It outputs a pair of equal-length messages $m_0, m_1$.

   $\mathcal{A}$ 获得输入 ${1}^n$ 以及对 $\mathsf{Enc}_k(\cdot)$ 和 $\mathsf{Dec}_k(\cdot)$ 的预言机访问。它输出一对等长消息 $m_0, m_1$。

3. A uniform bit $b \in \{0,1\}$ is chosen, and then a challenge ciphertext $c \leftarrow \mathsf{Enc}_{k}(m_{b})$ is computed and given to A.

   选择一个均匀比特 $b \in \{0,1\}$，然后计算挑战密文 $c \leftarrow \mathsf{Enc}_{k}(m_{b})$ 并将其交给 A。

4. The adversary $\mathcal{A}$ continues to have oracle access to $\mathsf{Enc}_k(\cdot)$ and $\mathsf{Dec}_k(\cdot)$, but is not allowed to query the latter on the challenge ciphertext itself. Eventually, $\mathcal{A}$ outputs a bit $b^{\prime}$.

   敌手 $\mathcal{A}$ 继续拥有对 $\mathsf{Enc}_k(\cdot)$ 和 $\mathsf{Dec}_k(\cdot)$ 的预言机访问，但不允许用挑战密文本身查询后者。最终，$\mathcal{A}$ 输出一个比特 $b^{\prime}$。

5. The output of the experiment is 1 if $b^{\prime} = b$, and 0 otherwise. If the output of the experiment is 1, we say that A succeeds.

   如果 $b^{\prime} = b$，实验输出为 1，否则为 0。如果实验输出为 1，我们称 A 成功。

DEFINITION 5.1 A private-key encryption scheme $\Pi$ has indistinguishable encryptions under a chosen-ciphertext attack, or is CCA-secure, if for all probabilistic polynomial-time adversaries $\mathcal{A}$ there is a negligible function $\mathsf{negl}$ such that:

$$\Pr[\mathsf{PrivK}_{\mathcal{A},\Pi}^{\mathsf{cca}}(n)=1]\leq\frac{1}{2}+\mathsf{negl}(n),$$

where the probability is taken over all randomness used in the experiment.

**定义 5.1** 一个私钥加密方案 $\Pi$ 在选择密文攻击下具有不可区分的加密，或称为 CCA 安全的，如果对于所有概率多项式时间敌手 $\mathcal{A}$，存在一个可忽略函数 $\mathsf{negl}$ 使得：

$$\Pr[\mathsf{PrivK}_{\mathcal{A},\Pi}^{\mathsf{cca}}(n)=1]\leq\frac{1}{2}+\mathsf{negl}(n),$$

其中概率取自实验中使用的所有随机性。

For completeness, we remark that the natural analogue of Theorem 3.23 holds for CCA-security as well—namely, if a scheme has indistinguishable encryptions under a chosen-ciphertext attack then it has indistinguishable multiple encryptions under a chosen-ciphertext attack, defined appropriately.

为完整起见，我们指出定理 3.23 的自然对应结论对 CCA 安全性同样成立——即如果一个方案在选择密文攻击下具有不可区分的加密，那么它在选择密文攻击下具有不可区分的多重加密（经适当定义）。

Discussion. In the experiment considered above, the adversary is given access to a decryption oracle that returns the entire result of decrypting a ciphertext provided by the attacker. In general, this might be much more information than what is available to an attacker in the real world; for example, in the padding-oracle scenario described earlier, the attacker only learns whether decryption results in an error or not. As usual, however, we want to make cryptographic definitions as strong as possible so they are broadly applicable. Since we don't know what information an attacker might be able to learn when a ciphertext it sends is decrypted by a receiver, we make the worst-case assumption that the attacker learns everything.

讨论。在上述实验中，敌手被赋予对解密预言机的访问权限，该预言机会返回对攻击者所提供密文进行解密的完整结果。一般来说，这可能比现实世界中的攻击者所能获得的信息多得多；例如，在前面描述的填充预言机场景中，攻击者只能获知解密是否产生错误。然而，与往常一样，我们希望密码学定义尽可能强，以便广泛适用。由于我们不知道攻击者在接收方解密其发送的密文时可能获知什么信息，我们做最坏情形的假设，即攻击者获知一切。

There is one caveat. In the experiment, the adversary is allowed to submit any ciphertexts of its choice to the decryption oracle except that it may not request decryption of the challenge ciphertext itself. This restriction is clearly necessary or else there is no hope for any encryption scheme to satisfy the definition. Even with this restriction in place, the definition provides meaningful security. In particular, note that in the context of a padding-oracle attack the attacker does not learn anything by getting the receiver to decrypt the challenge ciphertext (since the attacker knows that it will not cause an error), and so a CCA-secure scheme would not be vulnerable to that attack.

有一个注意事项。在实验中，敌手可以向解密预言机提交其选择的任意密文，但不得请求解密挑战密文本身。这一限制显然是必要的，否则任何加密方案都没有希望满足该定义。即使有这一限制，该定义仍提供了有意义的安全性。特别地，注意在填充预言机攻击的语境下，攻击者让接收方解密挑战密文并不能获知任何信息（因为攻击者知道这不会导致错误），因此 CCA 安全的方案不会受到该攻击的威胁。

Insecurity of the schemes we have studied. None of the encryption schemes we have seen thus far is CCA-secure. We demonstrate this for Construction 3.28, where encryption of a message $m$ takes the form $\langle r, F_k(r) \oplus m \rangle$. Consider an adversary $\mathcal{A}$ running in the CCA indistinguishability experiment who chooses $m_0 = 0^n$ and $m_1 = 1^n$. Then, upon receiving a ciphertext $c = \langle r, s \rangle$, the adversary flips the first bit of $s$ and asks for a decryption of the resulting ciphertext $c^\prime$. Since $c^\prime \neq c$, this query is allowed and the decryption oracle answers with either ${10}^{n-1}$ (in which case it is clear that $b = 0$) or ${01}^{n-1}$ (in which case $b = 1$). This example demonstrates that CCA-security is quite stringent. Any encryption scheme that allows ciphertexts to be “manipulated” in a controlled way cannot be CCA-secure. Thus, CCA-security implies a very important property called non-malleability. Loosely speaking, a non-malleable encryption scheme has the property that if the adversary modifies a given ciphertext, the result decrypts to a plaintext that bears no relation to the original one. This is a very useful property for encryption schemes used in complex cryptographic protocols.

我们已研究方案的不安全性。我们迄今见过的所有加密方案都不是 CCA 安全的。我们以构造 3.28 为例说明这一点，其中消息 $m$ 的加密形式为 $\langle r, F_k(r) \oplus m \rangle$。考虑在 CCA 不可区分性实验中运行的敌手 $\mathcal{A}$，它选择 $m_0 = 0^n$ 和 $m_1 = 1^n$。然后，在收到密文 $c = \langle r, s \rangle$ 后，敌手翻转 $s$ 的第一个比特，并请求解密所得密文 $c^\prime$。由于 $c^\prime \neq c$，该查询是允许的，解密预言机将回答 ${10}^{n-1}$（此时显然 $b = 0$）或 ${01}^{n-1}$（此时 $b = 1$）。这个例子表明 CCA 安全性相当严格。任何允许以受控方式“操纵”密文的加密方案都不可能是 CCA 安全的。因此，CCA 安全性蕴含一个非常重要的性质，称为非可塑性（non-malleability）。粗略地说，非可塑加密方案具有这样的性质：如果敌手修改给定的密文，其结果解密出的明文与原始明文没有任何关系。对于用于复杂密码协议的加密方案来说，这是一个非常有用的性质。

## 5.2 Authenticated Encryption　5.2 认证加密

CCA-security is extremely important, but is subsumed by an even stronger notion of security we introduce here. Until now, we have considered how to obtain secrecy (using encryption) and integrity (using message authentication codes) separately. The aim of authenticated encryption, defined below, is to achieve both goals simultaneously. It is best practice to always ensure secrecy and integrity by default in the private-key setting. Indeed, in many applications where secrecy is required it turns out that integrity is essential also. Moreover, a lack of integrity can sometimes lead to a breach of secrecy, as illustrated in the previous section.

CCA 安全性极其重要，但它被我们将在此引入的一个更强的安全概念所涵盖。到目前为止，我们分别考虑了如何获得机密性（使用加密）和完整性（使用消息认证码）。下面定义的认证加密（authenticated encryption）的目标是同时实现这两个目标。在私钥设置下，最佳实践是始终默认确保机密性和完整性。事实上，在许多需要机密性的应用中，完整性也被证明是必不可少的。此外，缺乏完整性有时会导致机密性被破坏，正如上一节所示。

### 5.2.1 Defining Authenticated Encryption　5.2.1 认证加密的定义

We begin, as usual, by defining precisely what we wish to achieve. One way to proceed is to define secrecy and integrity separately. Since we are explicitly concerned with an active adversary here, the natural notion of secrecy is CCA-security. The natural way to define integrity for encryption is via an analogue of the notion of existential unforgeability under an adaptive chosen-message attack that we considered for MACs. (We need a new definition because the syntax of an encryption scheme does not match the syntax of a MAC.) Consider the following experiment defined for a private-key encryption scheme $\Pi = (\mathsf{Gen}, \mathsf{Enc}, \mathsf{Dec})$, adversary $\mathcal{A}$, and value $n$ for the security parameter:

与往常一样，我们首先精确定义我们希望实现的目标。一种做法是分别定义机密性和完整性。由于我们在此明确关注活跃敌手，自然的机密性概念是 CCA 安全性。定义加密完整性的自然方式是类比我们为 MAC 考虑的自适应选择消息攻击下的存在性不可伪造性概念。（我们需要一个新定义，因为加密方案的语法与 MAC 的语法不匹配。）考虑以下关于私钥加密方案 $\Pi = (\mathsf{Gen}, \mathsf{Enc}, \mathsf{Dec})$、敌手 $\mathcal{A}$ 以及安全参数取值 $n$ 定义的实验：

The unforgeable encryption experiment $\mathsf{Enc-Forge}_{\mathcal{A},\Pi}(n)$:
不可伪造加密实验 $\mathsf{Enc-Forge}_{\mathcal{A},\Pi}(n)$：

1. A key $k$ is generated by running $\mathsf{Gen}(1^{n})$.

   通过运行 $\mathsf{Gen}(1^{n})$ 生成密钥 $k$。

2. The adversary $\mathcal{A}$ is given input ${1}^n$ and access to an encryption oracle $\mathsf{Enc}_k(\cdot)$. The adversary eventually outputs a ciphertext $c$. Let $m := \mathsf{Dec}_k(c)$ and let $\mathcal{Q}$ denote the set of all queries that $\mathcal{A}$ submitted to its oracle.

   敌手 $\mathcal{A}$ 获得输入 ${1}^n$ 和对加密预言机 $\mathsf{Enc}_k(\cdot)$ 的访问。敌手最终输出一个密文 $c$。令 $m := \mathsf{Dec}_k(c)$，并令 $\mathcal{Q}$ 表示 $\mathcal{A}$ 提交给其预言机的所有查询的集合。

3. $\mathcal{A}$ succeeds if and only if (1) $m \neq \bot$ and (2) $m \notin \mathcal{Q}$. In that case the output of the experiment is defined to be 1.

   $\mathcal{A}$ 成功当且仅当 (1) $m \neq \bot$ 且 (2) $m \notin \mathcal{Q}$。此时实验的输出定义为 1。

DEFINITION 5.2 A private-key encryption scheme $\Pi$ is unforgeable if for all probabilistic polynomial-time adversaries A, there is a negligible function $\mathsf{negl}$ such that:

$$\Pr[{\mathsf{Enc-Forge}}_{\mathcal{A},\Pi}(n)=1]\leq\mathsf{negl}(n).$$

**定义 5.2** 一个私钥加密方案 $\Pi$ 是不可伪造的，如果对于所有概率多项式时间敌手 A，存在一个可忽略函数 $\mathsf{negl}$ 使得：

$$\Pr[{\mathsf{Enc-Forge}}_{\mathcal{A},\Pi}(n)=1]\leq\mathsf{negl}(n).$$

We may now define an authenticated encryption scheme.

现在我们可以定义认证加密方案了。

DEFINITION 5.3 A private-key encryption scheme is an authenticated encryption (AE) scheme if it is CCA-secure and unforgeable.

**定义 5.3** 一个私钥加密方案是认证加密（AE）方案，如果它是 CCA 安全的且不可伪造的。

It is also possible to capture both the above requirements in a definition involving a single experiment. The experiment is somewhat different from previous experiments we have considered, so we provide some motivation before giving the details. The idea is to consider two different scenarios, and require that they be indistinguishable to an attacker. In the first scenario, which can be viewed as corresponding to the real-world context in which the adversary operates, the attacker is given access to both an encryption oracle and a decryption oracle. In the second case, which can be viewed as corresponding to an “ideal” scenario, these two oracles are changed as follows:

也可以用涉及单个实验的定义来刻画上述两项要求。该实验与我们之前考虑过的实验有些不同，因此在给出细节之前我们先提供一些动机。其思想是考虑两种不同的场景，并要求它们对攻击者不可区分。在第一种场景中——可以看作对应于敌手所处的现实世界环境——攻击者被赋予对加密预言机和解密预言机的访问权限。在第二种情形中——可以看作对应于一个“理想”场景——这两个预言机被修改如下：

- In place of an encryption oracle, the attacker is given access to an oracle that encrypts a 0-string of the correct length. Formally, the attacker is given access to an oracle $\mathsf{Enc}_k^0(\cdot)$ where $\mathsf{Enc}_k^0(m) = \mathsf{Enc}_k(0^{|m|})$. I.e., when requesting an encryption of $m$, the attacker is instead given an encryption of a 0-string of the same length as $m$.

  替代加密预言机的是，攻击者被赋予对一个会加密正确长度 0 串的预言机的访问。形式化地，攻击者被赋予对预言机 $\mathsf{Enc}_k^0(\cdot)$ 的访问，其中 $\mathsf{Enc}_k^0(m) = \mathsf{Enc}_k(0^{|m|})$。即当请求加密 $m$ 时，攻击者实际得到的是一个与 $m$ 等长的 0 串的加密。

- In place of a decryption oracle, the attacker is given access to an oracle $\mathsf{Dec}_{\perp}(\cdot)$ that always returns the error symbol $\perp$.

  替代解密预言机的是，攻击者被赋予对总是返回错误符号 $\perp$ 的预言机 $\mathsf{Dec}_{\perp}(\cdot)$ 的访问。

If an attacker cannot distinguish the first scenario from the second, then this means (1) any new ciphertexts the attacker generates in the real world will be invalid (i.e., will generate an error upon decryption). This not only implies a strong form of integrity, but also makes chosen-ciphertext attacks useless. Moreover, (2) the attacker cannot distinguish a real encryption oracle from an oracle that always encrypts 0s, which implies secrecy.

如果攻击者无法区分第一种场景与第二种场景，那么这意味着 (1) 攻击者在现实世界中生成的任何新密文都是无效的（即解密时将产生错误）。这不仅蕴含了一种强形式的完整性，还使选择密文攻击失去作用。此外，(2) 攻击者无法区分真实的加密预言机与总是加密 0 串的预言机，这蕴含了机密性。

Formally, for a private-key encryption scheme $\Pi$, adversary $\mathcal{A}$, and value n for the security parameter, define the following experiment:

形式化地，对于私钥加密方案 $\Pi$、敌手 $\mathcal{A}$ 以及安全参数取值 n，定义以下实验：

The authenticated-encryption experiment $\mathsf{PrivK}_{\mathcal{A},\Pi}^{\text{ae}}(n)$:

认证加密实验 $\mathsf{PrivK}_{\mathcal{A},\Pi}^{\text{ae}}(n)$：

1. A key $k$ is generated by running $\mathsf{Gen}(1^{n})$.

   通过运行 $\mathsf{Gen}(1^{n})$ 生成密钥 $k$。

2. A uniform bit $b \in \{0,1\}$ is chosen.

   选择一个均匀比特 $b \in \{0,1\}$。

3. The adversary A is given input ${1}^{n}$ and access to two oracles:

   敌手 $\mathcal{A}$ 获得输入 ${1}^{n}$ 和对两个预言机的访问：

   (a) If $b = 0$, then $\mathcal{A}$ is given access to $\mathsf{Enc}_k(\cdot)$ and $\mathsf{Dec}_k(\cdot)$.

   (a) 如果 $b = 0$，则 $\mathcal{A}$ 被赋予对 $\mathsf{Enc}_k(\cdot)$ 和 $\mathsf{Dec}_k(\cdot)$ 的访问。

   (b) If $b = 1$, then $\mathcal{A}$ is given access to $\mathsf{Enc}_{k}^{0}(\cdot)$ and $\mathsf{Dec}_{\perp}(\cdot)$.

   (b) 如果 $b = 1$，则 $\mathcal{A}$ 被赋予对 $\mathsf{Enc}_{k}^{0}(\cdot)$ 和 $\mathsf{Dec}_{\perp}(\cdot)$ 的访问。

   A is not allowed to query a ciphertext c to its second oracle that it previously received as the response from its first oracle.

   $\mathcal{A}$ 不得向其第二个预言机查询它先前作为第一个预言机的响应而收到的密文 $c$。

4. The adversary outputs a bit b'.

   敌手输出一个比特 b'。

5. The output of the experiment is defined to be 1 if $b^{\prime} = b$, and 0 otherwise. In the former case, we say that A succeeds.

   如果 $b^{\prime} = b$，实验的输出定义为 1，否则为 0。前一种情形下，我们称 A 成功。

In the experiment, the attacker is not allowed to submit ciphertexts to the decryption oracle that it received from its encryption oracle, since this would lead to a trivial way to distinguish the two scenarios. We remark that in the "real" case (i.e., when b = 0) the attacker already knows the decryption of those ciphertexts, so there is not much point in making such queries, anyway.

在实验中，攻击者不允许向解密预言机提交它从加密预言机处收到的密文，因为这将导致一种区分两种场景的平凡方法。我们指出，在“真实”情形（即 b = 0）下，攻击者本来就知道那些密文的解密结果，因此无论如何，进行此类查询也没有多大意义。

DEFINITION 5.4 A private-key encryption scheme is an authenticated encryption (AE) scheme if for all probabilistic polynomial-time adversaries A there is a negligible function $\mathsf{negl}$ such that

$$\Pr\left[\mathsf{PrivK}_{\mathcal{A},\Pi}^{\mathsf{ae}}(n)=1\right]\leq\frac{1}{2}+\mathsf{negl}(n).$$

**定义 5.4** 一个私钥加密方案是认证加密（AE）方案，如果对于所有概率多项式时间敌手 A，存在一个可忽略函数 $\mathsf{negl}$ 使得

$$\Pr\left[\mathsf{PrivK}_{\mathcal{A},\Pi}^{\mathsf{ae}}(n)=1\right]\leq\frac{1}{2}+\mathsf{negl}(n).$$

We have given two definitions of authenticated encryption. Fortunately, the definitions are equivalent:

我们给出了认证加密的两个定义。幸运的是，这两个定义是等价的：

THEOREM 5.5 A private-key encryption scheme satisfies Definition 5.3 if and only if it satisfies Definition 5.4.

**定理 5.5** 一个私钥加密方案满足定义 5.3，当且仅当它满足定义 5.4。

Authenticated encryption with associated data. Often, a message m requires both secrecy and integrity but various associated data (e.g., header information) sent along with the message requires integrity only. While it is possible to simply concatenate the message and the associated data (in some way that allows for unambiguous parsing) and then use an AE scheme to encrypt them both, better efficiency can be achieved by providing the associated data with integrity protection only. We omit further details, but note that AE schemes with support for associated data are called authenticated encryption with associated data (AEAD) schemes in the literature.

带关联数据的认证加密。通常，消息 $m$ 同时需要机密性和完整性，但随消息一起发送的各种关联数据（例如头部信息）只需要完整性。虽然可以简单地将消息与关联数据拼接（以某种允许无歧义解析的方式），然后使用 AE 方案将二者一起加密，但只对关联数据提供完整性保护可以获得更高的效率。我们省略进一步的细节，但指出：文献中支持关联数据的 AE 方案称为带关联数据的认证加密（AEAD）方案。

### 5.2.2 CCA Security vs. Authenticated Encryption　5.2.2 CCA 安全性与认证加密

It follows directly from Definition 5.3 that any authenticated encryption scheme is also CCA-secure. The converse, however, is not true, and there are private-key encryption schemes that are CCA-secure but that are not authenticated encryption schemes. You are asked to prove this in Exercise 5.9.

由定义 5.3 直接可知，任何认证加密方案也是 CCA 安全的。然而，反之不然：存在是 CCA 安全的但不是认证加密方案的私钥加密方案。这一点留作习题 5.9 证明。

One can imagine applications where CCA-security is needed but authenticated encryption is not. One example might be when private-key encryption is used for key transport. As a concrete example, say a server gives a tamper-proof hardware token to a user, where the token stores a long-term key $k$. The server can share a fresh, short-term key $k^{\prime}$ with the token (that will remain unknown to the user) by giving the user $\mathsf{Enc}_k(k^{\prime})$; the user is supposed to give this ciphertext to the token, which will decrypt it to obtain $k^{\prime}$. CCA-security is necessary here because chosen-ciphertext attacks can be easily carried out by the user in this context. On the other hand, not much harm is done if the user can generate a valid ciphertext that causes the token to use some arbitrary key $k^{\prime\prime}$ that is uncorrelated with $k^{\prime}$. (Of course, this depends on what the token does with this short-term key.)

可以想象某些应用需要 CCA 安全性而不需要认证加密。一个例子可能是私钥加密用于密钥传输的情形。举个具体的例子：假设服务器向用户发放一个防篡改的硬件令牌，令牌中存储着长期密钥 $k$。服务器可以通过给用户 $\mathsf{Enc}_k(k^{\prime})$ 来与令牌共享一个新的短期密钥 $k^{\prime}$（该密钥将对用户保持未知）；用户应将此密文交给令牌，令牌解密后得到 $k^{\prime}$。这里 CCA 安全性是必要的，因为在此环境中用户很容易实施选择密文攻击。另一方面，如果用户能够生成一个有效密文，使令牌使用某个与 $k^{\prime}$ 不相关的任意密钥 $k^{\prime\prime}$，也不会造成太大危害。（当然，这取决于令牌用这个短期密钥做什么。）

Notwithstanding the above, most applications of private-key encryption in the presence of an active adversary do require integrity. Fortunately, most natural constructions of CCA-secure encryption schemes satisfy the stronger definition of authenticated encryption, anyway. Put differently, there is no reason to ever use a CCA-secure scheme that is not also an authenticated encryption scheme, simply because we don't have any constructions of the former that are more efficient than constructions of the latter.

尽管如此，在活跃敌手存在的情况下，私钥加密的大多数应用确实需要完整性。幸运的是，无论如何，大多数自然的 CCA 安全加密方案构造都满足更强的认证加密定义。换言之，没有理由使用不同时也是认证加密方案的 CCA 安全方案，因为我们尚不知道有任何前者的构造会比后者的构造更高效。

From a conceptual point of view, however, the notions of CCA-security and authenticated encryption are distinct. With regard to CCA-security we are not interested in message integrity per se; rather, we wish to ensure secrecy even against an active adversary who can interfere with the communication from sender to receiver. In contrast, with regard to authenticated encryption we are explicitly interested in the twin goals of secrecy and integrity.

然而，从概念上讲，CCA 安全性与认证加密这两个概念是不同的。就 CCA 安全性而言，我们并不关心消息完整性本身；相反，我们希望即使面对能够干扰发送方到接收方通信的活跃敌手，也能确保机密性。相比之下，就认证加密而言，我们明确关注机密性与完整性这一双重目标。
