# Chapter 12: Public-Key Encryption　第 12 章　公钥加密

## 12.1 Public-Key Encryption – An Overview　公钥加密——概述

The introduction of public-key encryption marked a revolution in cryptography. Until that time, cryptographers had relied exclusively on shared, secret keys to achieve private communication. Public-key techniques, in contrast, enable parties to communicate privately without having agreed on any secret information in advance. As we have already noted, it is quite amazing and counterintuitive that this is possible: it means that two people on opposite sides of a room who can only communicate by shouting to each other, and have no initial shared secret, can talk in such a way that no one else in the room learns anything about what they are saying!

公钥加密的引入标志着密码学的一场革命。在此之前，密码学家只能依靠共享的秘密密钥来实现私密通信。相比之下，公钥技术使得通信各方无需事先约定任何秘密信息就能私密地通信。正如我们已经指出的，这件事相当令人惊叹且违背直觉：它意味着，处在房间两端、只能互相大声喊话且没有任何预先共享秘密的两个人，也能以房间里其他任何人都无从知晓其谈话内容的方式交谈！

In the setting of private-key encryption, two parties agree on a secret key that can be used, by either party, for both encryption and decryption. Public-key encryption is asymmetric in both these respects. One party (the receiver) generates a pair of keys $(pk, sk)$, called the public key and the private key, respectively. The public key is used by a sender to encrypt a message; the receiver uses the private key to decrypt the resulting ciphertext.

在私钥加密的情形中，通信双方约定一个秘密密钥，双方都可以用它进行加密和解密。公钥加密在这两个方面都是非对称的。其中一方（接收方）生成一对密钥 $(pk, sk)$，分别称为公钥和私钥。发送方用公钥加密消息；接收方用私钥解密所得的密文。

Since the goal is to avoid the need for two parties to meet in advance to agree on any information, how does the sender learn pk? At an abstract level, there are two ways this can occur. Say Alice is the receiver, and Bob is the sender. In the first approach, when Alice learns that Bob wants to communicate with her, she can at that point generate $(pk, sk)$ (assuming she hasn't done so already) and then send $pk$ to Bob in the clear; Bob can then use $pk$ to encrypt his message. We emphasize that the channel between Alice and Bob may be public, but is assumed to be authenticated, meaning that the adversary cannot modify the public key sent by Alice to Bob (and, in particular, cannot replace pk with its own public key). In Section 13.6 we discuss how public keys can be distributed over unauthenticated channels.

既然目标是避免双方事先见面约定任何信息，那么发送方如何得知 $pk$ 呢？在抽象层面上，这有两种实现方式。设 Alice 是接收方，Bob 是发送方。第一种方式是：当 Alice 得知 Bob 想与她通信时，她可以在那时生成 $(pk, sk)$（假设她还没有生成），然后把 $pk$ 明文发送给 Bob；Bob 随后即可用 $pk$ 加密他的消息。我们强调，Alice 与 Bob 之间的信道可以是公开的，但假定它是经过认证的，也就是说敌手无法篡改 Alice 发给 Bob 的公钥（特别地，无法把 $pk$ 替换成它自己的公钥）。在 13.6 节中，我们将讨论如何在未经认证的信道上分发公钥。

An alternative approach is for Alice to generate her keys $(pk, sk)$ in advance, independently of any particular sender. (In fact, at the time of key generation Alice need not be aware that Bob wants to talk to her, or even that Bob exists.) Alice can widely disseminate her public key pk by, say, publishing it on her webpage, putting it on her business cards, or placing it in a public directory. Now, anyone who wishes to communicate privately with Alice can look up her public key and proceed as above. Multiple senders can communicate multiple times with Alice using the same public key pk for encrypting all their communication.

另一种方式是 Alice 预先生成她的密钥 $(pk, sk)$，而不依赖于任何特定的发送方。（事实上，在生成密钥时，Alice 甚至不需要知道 Bob 想和她说话，甚至不需要知道 Bob 的存在。）Alice 可以广泛传播她的公钥 $pk$，比如把它公布在自己的网页上、印在名片上，或放进公共目录里。这样，任何想与 Alice 私密通信的人都可以查到她的公钥，然后按上述方式进行。多个发送方可以使用同一个公钥 $pk$ 来加密他们与 Alice 的全部通信，与她进行多次通信。

Note that pk is inherently public—and can thus be learned easily by an attacker—in either of the above scenarios. In the first case, an adversary eavesdropping on the communication between Alice and Bob obtains pk directly; in the second case, an adversary could just as well look up Alice's public key on its own. We see that the security of public-key encryption cannot rely on secrecy of $pk$, but must instead rely on secrecy of $sk$. It is therefore crucial that Alice not reveal her private key to anyone, including the sender Bob.

注意，在上述两种情形中，$pk$ 本质上都是公开的——因而攻击者可以轻易获知它。在第一种情形中，窃听 Alice 与 Bob 之间通信的敌手可以直接获得 $pk$；在第二种情形中，敌手同样可以自己去查询 Alice 的公钥。由此可见，公钥加密的安全性不能依赖于 $pk$ 的保密性，而必须依赖于 $sk$ 的保密性。因此，Alice 绝不能把她的私钥透露给任何人，包括发送方 Bob，这一点至关重要。

### Comparison to Private-Key Encryption　与私钥加密的比较

Perhaps the most obvious difference between private- and public-key encryption is that the former assumes complete secrecy of all cryptographic keys, whereas the latter requires secrecy only for the private key $sk$. Although this may seem like a minor distinction, the ramifications are huge: in the private-key setting the communicating parties must somehow be able to share the secret key without allowing any third party to learn it, whereas in the public-key setting the public key can be sent from one party to the other over a public channel without compromising security. For parties shouting across a room or, more realistically, communicating over a public WiFi network or the Internet, public-key encryption is the only option.

私钥加密与公钥加密之间最明显的区别也许在于：前者假定所有密码学密钥都完全保密，而后者只要求私钥 $sk$ 保密。这个区别看似微小，影响却极为深远：在私钥情形中，通信双方必须以不让任何第三方获知的方式共享秘密密钥；而在公钥情形中，公钥可以经由公开信道从一方发送给另一方，且不损害安全性。对于隔着房间喊话的双方，或者更现实地，通过公共 WiFi 网络或互联网通信的双方来说，公钥加密是唯一的选择。

Another important distinction is that private-key encryption schemes use the same key for both encryption and decryption, whereas public-key encryption schemes use different keys for each operation. That is, public-key encryption is inherently asymmetric. This asymmetry in the public-key setting means that the roles of sender and receiver are not interchangeable as they are in the private-key setting: a single key-pair allows communication in one direction only. (Bidirectional communication can be achieved in a number of ways; the point is that a single invocation of a public-key encryption scheme forces a distinction between one user who acts as a receiver and other users who act as senders.) In addition, a single instance of a public-key encryption scheme enables multiple senders to communicate privately with a single receiver, in contrast to the private-key case where a secret key shared between two parties enables private communication between those two parties only.

另一个重要区别是：私钥加密方案加密和解密使用同一个密钥，而公钥加密方案对这两种操作使用不同的密钥。也就是说，公钥加密本质上是非对称的。公钥情形中的这种非对称性意味着，发送方与接收方的角色不像私钥情形中那样可以互换：一对密钥只允许单向通信。（双向通信可以通过多种方式实现；关键在于，公钥加密方案的一次使用必然区分出一个充当接收方的用户和其他充当发送方的用户。）此外，公钥加密方案的单个实例允许多个发送方与同一个接收方私密通信；与之形成对比的是，在私钥情形中，两方共享的一个秘密密钥只允许这两方之间私密通信。

Summarizing and elaborating the preceding discussion, we see that public-key encryption has the following advantages relative to private-key encryption:

总结并展开前面的讨论，可以看到公钥加密相对于私钥加密具有以下优点：

- Public-key encryption addresses (to some extent) the key-distribution problem, since communicating parties do not need to secretly share a key in advance of their communication. Two parties can communicate secretly even if all communication between them is monitored.

- 公钥加密（在某种程度上）解决了密钥分发问题，因为通信双方无需在通信之前秘密共享密钥。即使双方之间的所有通信都被监听，他们仍能秘密地通信。

- When a single receiver is communicating with N senders (e.g., an on-line merchant processing credit-card orders from multiple purchasers), it is much more convenient for the receiver to store a single private key $sk$ rather than to share, store, and manage $N$ different secret keys (i.e., one for each sender).

- 当单个接收方与 $N$ 个发送方通信时（例如在线商户处理来自多个购买者的信用卡订单），接收方只存储一个私钥 $sk$，要比共享、存储并管理 $N$ 个不同的秘密密钥（即每个发送方一个）方便得多。

- When using public-key encryption the number and identities of potential senders need not be known at the time of key generation. This allows enormous flexibility in “open systems.”

- 使用公钥加密时，在生成密钥时无需知道潜在发送方的数量和身份。这为“开放系统”带来了极大的灵活性。

The fact that public-key encryption schemes allow anyone to act as a sender can be a drawback when a receiver only wants to receive messages from one specific individual. In that case, an authenticated (private-key) encryption scheme would be a better choice than public-key encryption.

公钥加密方案允许任何人充当发送方，而当接收方只想接收来自某个特定个人的消息时，这一点就可能成为缺点。在这种情况下，（私钥的）认证加密方案会比公钥加密更合适。

The main disadvantage of public-key encryption is that it is roughly $2-3$ orders of magnitude slower than private-key encryption. (It is difficult to give an exact comparison since the relative efficiency depends on the exact schemes under consideration as well as various implementation details.) It can be a challenge to implement public-key encryption in severely resource-constrained devices like smartcards or radio-frequency identification (RFID) tags. Even when a desktop computer is performing cryptographic operations, carrying out thousands of such operations per second (as in the case of a website processing credit-card transactions) may be prohibitive. Thus, when private-key encryption is an option (i.e., if two parties can securely share a key in advance), it should be used.

公钥加密的主要缺点是它比私钥加密大约慢 2～3 个数量级。（很难给出精确的比较，因为相对效率取决于所考虑的具体方案以及各种实现细节。）在智能卡或射频识别（RFID）标签这类资源严重受限的设备上实现公钥加密可能很有挑战性。即便用台式计算机执行密码运算，每秒进行数千次此类运算（例如处理信用卡交易的网站）也可能是无法承受的。因此，当私钥加密可行时（即双方能够事先安全地共享密钥），就应当使用私钥加密。

As we will see in Section 12.3, private-key encryption is used in the public-key setting to improve the efficiency of (public-key) encryption for long messages. A thorough understanding of private-key encryption is therefore crucial for appreciating how public-key encryption is implemented in practice.

正如我们将在 12.3 节中看到的，私钥加密也被用于公钥情形中，以提高（公钥）加密长消息的效率。因此，透彻理解私钥加密对于领会公钥加密在实践中如何实现至关重要。

### Secure Distribution of Public Keys　公钥的安全分发

In our entire discussion thus far, we have implicitly assumed that the adversary is passive; that is, the adversary only eavesdrops on communication between the sender and receiver but does not actively interfere with the communication. Equivalently, we assume the communication channel between the sender and receiver is authenticated, at least for the initial sharing of the public key. If the adversary has the ability to tamper with all communication between the honest parties, and the honest parties share no keys in advance, then privacy simply cannot be achieved. For example, if a receiver Alice sends her public key $pk$ to Bob but the adversary replaces it with a key $pk'$ of its own (for which it knows the matching private key $sk'$), then even though Bob encrypts his message using $pk'$ the adversary will easily be able to recover the message (using $sk'$). A similar attack works if an adversary is able to change the value of Alice's public key that is stored in some public directory, or if the adversary can tamper with the public key as it is transmitted from the public directory to Bob. If Alice and Bob do not share any information in advance, and are not willing to rely on some mutually trusted third party, there is nothing Alice or Bob can do to prevent active attacks of this sort, or even to tell that such an attack is taking place. $^{1}$

到目前为止的讨论中，我们都隐含地假定敌手是被动的；也就是说，敌手只窃听发送方与接收方之间的通信，而不主动干扰通信。等价地说，我们假定发送方与接收方之间的信道是经过认证的，至少在最初共享公钥时是如此。如果敌手有能力篡改诚实双方之间的所有通信，而诚实双方事先又没有共享任何密钥，那么私密性就根本无法实现。例如，接收方 Alice 把她的公钥 $pk$ 发给 Bob，但敌手将其替换成自己的密钥 $pk'$（敌手知道与之匹配的私钥 $sk'$），那么即使 Bob 用 $pk'$ 加密了他的消息，敌手也能轻易地（用 $sk'$）恢复出该消息。如果敌手能够篡改存储在某个公共目录中的 Alice 公钥的值，或者能够在公钥从公共目录传送给 Bob 的途中对其进行篡改，类似的攻击同样奏效。如果 Alice 和 Bob 事先没有共享任何信息，又不愿意依赖某个双方共同信任的第三方，那么他们没有任何办法阻止这类主动攻击，甚至无法察觉此类攻击正在发生。$^{1}$

> $^{1}$ In our “shouting-across-a-room” scenario, Alice and Bob can detect when an adversary interferes with the communication. But this is only because: (1) the adversary cannot prevent Alice’s messages from reaching Bob, and (2) Alice and Bob “share” in advance information (e.g., the sound of their voices) that allows them to “authenticate” their communication.
> $^{1}$ 在我们“隔着房间喊话”的场景中，Alice 与 Bob 能够察觉敌手干扰通信。但这只是因为：(1) 敌手无法阻止 Alice 的消息到达 Bob；(2) Alice 与 Bob 事先“共享”了一些信息（例如彼此的嗓音），使他们得以“认证”自己的通信。

Importantly, our treatment of public-key encryption in this chapter assumes that senders are able to obtain a legitimate copy of the receiver's public key. (This will be implicit in the security definitions we provide.) That is, we assume secure key distribution. This assumption is made not because active attacks of the type discussed above are of no concern—in fact, they represent a serious threat that must be dealt with in any real-world system that uses public-key encryption. Rather, this assumption is made because there exist other mechanisms for preventing active attacks (see, for example, Section 13.6), and it is therefore convenient (and useful) to decouple the study of secure public-key encryption from the study of secure public-key distribution.

重要的是，本章对公钥加密的讨论假定发送方能够获得接收方公钥的真实副本。（这一点将隐含在我们给出的安全定义之中。）也就是说，我们假定密钥分发是安全的。做此假定并不是因为上述那类主动攻击无需担心——事实上，对于任何使用公钥加密的真实系统来说，它们都是必须应对的严重威胁；做此假定是因为存在其他防止主动攻击的机制（例如见 13.6 节），因此把公钥加密安全性的研究与公钥安全分发的研究分开处理，既方便又有用。

## 12.2 Definitions　定义

We begin by defining the syntax of public-key encryption. The definition is very similar to Definition 3.7, with the exception that instead of working with just one key, we now have distinct encryption and decryption keys.

我们首先定义公钥加密的语法。该定义与定义 3.7 非常相似，区别在于现在不再只使用一个密钥，而是使用不同的加密密钥与解密密钥。

DEFINITION 12.1 A public-key encryption scheme is a triple of probabilistic polynomial-time algorithms (Gen, Enc, Dec) such that:

定义 12.1　公钥加密方案是由三个概率多项式时间算法 $(\mathsf{Gen}, \mathsf{Enc}, \mathsf{Dec})$ 构成的三元组，满足：

1. The key-generation algorithm Gen takes as input the security parameter $1^{n}$ and outputs a pair of keys $(pk, sk)$. We refer to the first of these as the public key and the second as the private key. We assume for convenience that $pk$ and $sk$ each has length at least $n$, and that $n$ can be determined from $pk$, $sk$.

   密钥生成算法 $\mathsf{Gen}$ 以安全参数 $1^{n}$ 为输入，输出一对密钥 $(pk, sk)$。我们把前者称为公钥，后者称为私钥。为方便起见，我们假定 $pk$ 和 $sk$ 的长度都至少为 $n$，并且 $n$ 可以从 $pk$、$sk$ 中确定。

The public key $pk$ defines a message space $\mathcal{M}_{pk}$.

公钥 $pk$ 定义了消息空间 $\mathcal{M}_{pk}$。

2. The encryption algorithm Enc takes as input a public key $pk$ and message $m \in \mathcal{M}_{pk}$, and outputs a ciphertext $c$; we denote this by $c \leftarrow \mathsf{Enc}_{pk}(m)$. (Looking ahead, Enc will need to be probabilistic in order to achieve meaningful security.)

   加密算法 $\mathsf{Enc}$ 以一个公钥 $pk$ 和一条消息 $m \in \mathcal{M}_{pk}$ 为输入，输出密文 $c$；记作 $c \leftarrow \mathsf{Enc}_{pk}(m)$。（提前说明：为了实现有意义的安全性，$\mathsf{Enc}$ 必须是概率算法。）

3. The deterministic decryption algorithm Dec takes as input a private key $sk$ and a ciphertext $c$, and outputs a message $m$ or a special symbol $\perp$ denoting failure. We write this as $m := \mathsf{Dec}_{sk}(c)$.

   确定性解密算法 $\mathsf{Dec}$ 以私钥 $sk$ 和密文 $c$ 为输入，输出一条消息 $m$，或者一个表示失败的特殊符号 $\perp$。记作 $m := \mathsf{Dec}_{sk}(c)$。

It is required that, except with negligible probability over the randomness of Gen and Enc, we have $\mathsf{Dec}_{sk}(\mathsf{Enc}_{pk}(m)) = m$ for any message $m \in \mathcal{M}_{pk}$.

要求：除去由 $\mathsf{Gen}$ 与 $\mathsf{Enc}$ 的随机性引起的可忽略概率外，对任意消息 $m \in \mathcal{M}_{pk}$ 都有 $\mathsf{Dec}_{sk}(\mathsf{Enc}_{pk}(m)) = m$。

The important difference from the private-key setting is that the key-generation algorithm Gen now outputs two keys instead of one. The public key $pk$ is used for encryption, while the private key $sk$ is used for decryption. Reiterating our earlier discussion, pk is assumed to be widely distributed so that anyone can encrypt messages for the party who generated this key, but sk must be kept private by the receiver in order for security to possibly hold.

与私钥情形的重要区别在于，密钥生成算法 $\mathsf{Gen}$ 现在输出两个密钥而不是一个。公钥 $pk$ 用于加密，私钥 $sk$ 用于解密。重申前面的讨论：$pk$ 被假定为广泛分发，使得任何人都可以为生成该密钥的一方加密消息；但 $sk$ 必须由接收方保密，安全性才有可能成立。

We allow for a negligible probability of decryption error and, indeed, some of the schemes we present will have a negligible error probability (e.g., if a prime needs to be chosen, but with negligible probability a composite is obtained instead). Despite this, we will generally ignore the issue from here on.

我们允许解密存在可忽略的错误概率；事实上，我们接下来给出的一些方案确实会有可忽略的错误概率（例如，需要选取一个素数时，以可忽略的概率得到的却是一个合数）。尽管如此，此后我们一般会忽略这个问题。

For practical usage of public-key encryption, we will want the message space to be bit-strings of some length (and, in particular, to be independent of the public key). When we describe encryption schemes with some message space $\mathcal{M}_{pk}$, we will in such cases also specify how to encode bit-strings as elements of $\mathcal{M}$ (unless it is obvious). This encoding must be both efficiently computable and efficiently reversible, so the receiver can recover the bit-string that was encrypted.

在公钥加密的实际使用中，我们希望消息空间是某个长度的比特串（特别地，与公钥无关）。当我们描述消息空间为某个 $\mathcal{M}_{pk}$ 的加密方案时，在这种情况下还会指明如何把比特串编码为 $\mathcal{M}$ 中的元素（除非这一点显而易见）。这种编码必须既可高效计算又可高效求逆，以便接收方能够恢复出被加密的比特串。

### 12.2.1 Security against Chosen-Plaintext Attacks　抵抗选择明文攻击的安全性

We initiate our treatment of security by introducing the “natural” counterpart of Definition 3.8 in the public-key setting. Since extensive motivation for this definition (as well as the others we will see) has already been given in Chapter 3, the discussion here will be relatively brief and will focus primarily on the differences between the private-key and the public-key settings.

我们从引入定义 3.8 在公钥情形中的“自然”对应物开始讨论安全性。由于第 3 章已经对这一定义（以及我们将看到的其他定义）给出了详尽的动机说明，这里的讨论将相对简短，主要关注私钥情形与公钥情形之间的差异。

Given a public-key encryption scheme $\Pi = (\mathsf{Gen}, \mathsf{Enc}, \mathsf{Dec})$ and an adversary $\mathcal{A}$, consider the following experiment:

给定一个公钥加密方案 $\Pi = (\mathsf{Gen}, \mathsf{Enc}, \mathsf{Dec})$ 和一个敌手 $\mathcal{A}$，考虑如下实验：

The eavesdropping indistinguishability experiment $\mathsf{PubK}_{\mathcal{A},\Pi}^{\mathsf{eav}}(n)$:

窃听不可区分性实验 $\mathsf{PubK}_{\mathcal{A},\Pi}^{\mathsf{eav}}(n)$：

1. $\mathsf{Gen}(1^{n})$ is run to obtain keys $(pk, sk)$.

   运行 $\mathsf{Gen}(1^{n})$ 得到密钥 $(pk, sk)$。

2. Adversary $\mathcal{A}$ is given $pk$, and outputs a pair of equal-length messages $m_0, m_1 \in \mathcal{M}_{pk}$.

   敌手 $\mathcal{A}$ 获得 $pk$，输出一对等长消息 $m_0, m_1 \in \mathcal{M}_{pk}$。

3. A uniform bit $b \in \{0,1\}$ is chosen, and then a ciphertext $c \leftarrow \mathsf{Enc}_{pk}(m_b)$ is computed and given to $\mathcal{A}$. We call $c$ the challenge ciphertext.

   均匀选取一个比特 $b \in \{0,1\}$，然后计算密文 $c \leftarrow \mathsf{Enc}_{pk}(m_b)$ 并交给 $\mathcal{A}$。我们称 $c$ 为挑战密文。

4. $\mathcal{A}$ outputs a bit $b'$. The output of the experiment is 1 if $b^{\prime} = b$, and 0 otherwise. If $b^{\prime} = b$ we say that $\mathcal{A}$ succeeds.

   $\mathcal{A}$ 输出一个比特 $b'$。若 $b^{\prime} = b$，则实验输出为 1；否则为 0。若 $b^{\prime} = b$，则称 $\mathcal{A}$ 成功。

DEFINITION 12.2 A public-key encryption scheme $\Pi = (\mathsf{Gen}, \mathsf{Enc}, \mathsf{Dec})$ has indistinguishable encryptions in the presence of an eavesdropper if for all probabilistic polynomial-time adversaries $\mathcal{A}$ there is a negligible function $\mathsf{negl}$ such that

定义 12.2　称公钥加密方案 $\Pi = (\mathsf{Gen}, \mathsf{Enc}, \mathsf{Dec})$ 在窃听者存在下具有不可区分的加密，如果对所有概率多项式时间敌手 $\mathcal{A}$，都存在可忽略函数 $\mathsf{negl}$ 使得

$$
\Pr[\mathsf{PubK}_{\mathcal{A},\Pi}^{\mathsf{eav}}(n)=1]\leq\frac{1}{2}+\mathsf{negl}(n).
$$

The main difference between the above definition and Definition 3.8 is that here $\mathcal{A}$ is given the public key $pk$. Furthermore, we allow $\mathcal{A}$ to choose its messages $m_0$ and $m_1$ based on this public key. This is essential when defining security of public-key encryption since, as discussed previously, it makes sense to assume that the adversary knows the public key of the recipient.

上述定义与定义 3.8 的主要区别在于，这里 $\mathcal{A}$ 获得了公钥 $pk$。此外，我们允许 $\mathcal{A}$ 基于该公钥来选择消息 $m_0$ 和 $m_1$。在定义公钥加密的安全性时，这一点必不可少，因为如前所述，假定敌手知道接收方的公钥是合理的。

The seemingly “minor” modification of giving the adversary $\mathcal{A}$ the public key $pk$ has a tremendous impact: it effectively gives $\mathcal{A}$ access to an encryption oracle for free. (The concept of an encryption oracle is explained in Section 3.4.2.) This is true because the adversary, given pk, can encrypt any message m on its own by simply computing $\mathsf{Enc}_{pk}(m)$. (As always, $\mathcal{A}$ is assumed to know the algorithm $\mathsf{Enc}$.) The upshot is that Definition 12.2 is equivalent to CPA-security (i.e., security against chosen-plaintext attacks), where this is defined in a manner analogous to Definition 3.21 with the only difference being that the attacker is given the public key in the corresponding experiment. We thus have:

把公钥 $pk$ 交给敌手 $\mathcal{A}$ 这一看似“微小”的修改影响巨大：它实际上等于免费给了 $\mathcal{A}$ 访问加密预言机的能力。（加密预言机的概念见 3.4.2 节。）这是因为，敌手拿到 $pk$ 后，只需计算 $\mathsf{Enc}_{pk}(m)$ 就能自行加密任意消息 $m$。（与往常一样，假定 $\mathcal{A}$ 知道算法 $\mathsf{Enc}$。）其结果是：定义 12.2 等价于选择明文安全（即抵抗选择明文攻击的安全性），后者的定义方式与定义 3.21 类似，唯一区别是在相应实验中把公钥交给攻击者。于是我们有：

PROPOSITION 12.3 If a public-key encryption scheme has indistinguishable encryptions in the presence of an eavesdropper, it is CPA-secure.

命题 12.3　若一个公钥加密方案在窃听者存在下具有不可区分的加密，则它是选择明文安全的。

This is in contrast to the private-key setting, where there exist schemes that have indistinguishable encryptions in the presence of an eavesdropper but are insecure under a chosen-plaintext attack (see Proposition 3.19). Further differences from the private-key setting that follow almost immediately as consequences of the above are discussed next.

这与私钥情形形成对比：在私钥情形中，存在一些方案在窃听者存在下具有不可区分的加密，却在选择明文攻击下不安全（见命题 3.19）。接下来讨论由上述结论几乎直接导出的、与私钥情形的更多区别。

Impossibility of perfectly secret public-key encryption. Perfectly secret public-key encryption could be defined analogously to Definition 2.3 by conditioning on the entire view of an eavesdropper (i.e., including the public key). Equivalently, it could be defined by extending Definition 12.2 to require that for all adversaries A (not only efficient ones), we have:

**完美保密的公钥加密不可能存在。**
完美保密的公钥加密可以仿照定义 2.3 来定义：以窃听者的整个视图（即包括公钥）为条件。等价地，也可以把定义 12.2 扩展为要求对所有敌手 $\mathcal{A}$（而不仅仅是高效敌手）都有：

$$
\Pr[\mathsf{PubK}_{\mathcal{A},\Pi}^{\mathsf{eav}}(n)=1]=\frac{1}{2}.
$$

In contrast to the private-key setting, however, perfectly secret public-key encryption is impossible, regardless of how long the keys are or how small the message space is. In fact, an unbounded adversary given $pk$ and a ciphertext $c$ computed via $c \leftarrow \mathsf{Enc}_{pk}(m)$ can determine $m$ with probability 1 (assuming errorless encryption). A proof of this is left as Exercise 12.1.

然而，与私钥情形不同，完美保密的公钥加密是不可能实现的，无论密钥多长、消息空间多小。事实上，给定 $pk$ 和由 $c \leftarrow \mathsf{Enc}_{pk}(m)$ 计算出的密文 $c$，一个计算能力无界的敌手可以以概率 1 确定 $m$（假定加密无错误）。这一结论的证明留作习题 12.1。

Insecurity of deterministic public-key encryption. As noted in the context of private-key encryption, no deterministic encryption scheme can be CPA-secure. The same is true here:

**确定性公钥加密的不安全性。**
正如在私钥加密语境中指出的，任何确定性加密方案都不可能是选择明文安全的。这里同样如此：

THEOREM 12.4 No deterministic public-key encryption scheme is CPA-secure.

定理 12.4　任何确定性的公钥加密方案都不是选择明文安全的。

Because Theorem 12.4 is so important, it merits more discussion. The theorem is not an “artefact” of our security definition, or an indication that our definition is too strong. Deterministic public-key encryption schemes are vulnerable to practical attacks in realistic scenarios and should not be used. The reason is that a deterministic scheme not only allows the adversary to determine when the same message is sent twice (as in the private-key setting), but also allows the adversary to recover the message if the set of possible messages is small. For example, consider a professor encrypting students' grades. Here, an eavesdropper knows that each student's grade is one of $\{A, B, C, D, F\}$. If the professor uses a deterministic public-key encryption scheme, an eavesdropper can determine any student's grade by encrypting all possible grades and comparing the results to the corresponding ciphertext.

由于定理 12.4 非常重要，值得多作讨论。该定理并不是我们的安全定义造成的“假象”，也不意味着我们的定义太强。确定性的公钥加密方案在现实场景中容易遭受实际攻击，因此不应使用。原因在于，确定性方案不仅会让敌手能够判断同一消息何时被发送了两次（与私钥情形一样），还使得敌手在可能消息的集合较小时能够恢复出消息。例如，设想一位教授加密学生的成绩。此时窃听者知道每个学生的成绩是 $\{A, B, C, D, F\}$ 之一。如果教授使用确定性的公钥加密方案，窃听者只需加密所有可能的成绩，并把结果与相应的密文比对，就能确定任何学生的成绩。

Although Theorem 12.4 seems deceptively simple, for a long time many real-world systems were designed using deterministic public-key encryption. When public-key encryption was introduced, it is fair to say that the importance of probabilistic encryption was not yet fully realized. The seminal work of Goldwasser and Micali, in which (something equivalent to) Definition 12.2 was proposed and Theorem 12.4 was stated, marked a turning point in the field of cryptography. The importance of pinning down one's intuition in a formal definition and looking at things the right way for the first time—even if seemingly simple in retrospect—should not be underestimated.

尽管定理 12.4 给人的感觉很简单、实则不然，但在相当长的时间里，许多真实系统的设计仍然使用确定性公钥加密。可以说，在公钥加密刚被提出时，人们尚未充分认识到概率加密的重要性。Goldwasser 和 Micali 的开创性工作提出了（与定义 12.2 等价的）定义并陈述了定理 12.4，标志着密码学领域的一个转折点。把直觉落实到形式化定义中、并第一次以正确的方式看待事物——尽管事后看来似乎简单——其重要性不应被低估。

### 12.2.2 Multiple Encryptions　多重加密

As in Chapter 3, it is important to understand the effect of using the same key (in this case, the same public key) for encrypting multiple messages. We could formulate security in such a setting by having an adversary output two lists of plaintexts, as in Definition 3.18. For the reasons discussed in Section 3.4.3, however, we choose instead to use a definition in which the attacker is given access to a “left-or-right” oracle $\mathsf{LR}_{pk,b}$ that, on input a pair of equal-length messages $m_0, m_1$, computes the ciphertext $c \leftarrow \mathsf{Enc}_{pk}(m_b)$ and returns $c$. The attacker is allowed to query this oracle as many times as it likes, and the definition therefore models security when multiple (unknown) messages are encrypted using the same public key.

与第 3 章一样，理解用同一密钥（这里是同一公钥）加密多条消息的影响是很重要的。我们本来可以仿照定义 3.18，让敌手输出两个明文列表来形式化这种情形下的安全性。然而出于 3.4.3 节讨论过的原因，我们选择改用另一种定义：攻击者可以访问一个“左或右”（left-or-right）预言机 $\mathsf{LR}_{pk,b}$，该预言机在输入一对等长消息 $m_0, m_1$ 时，计算密文 $c \leftarrow \mathsf{Enc}_{pk}(m_b)$ 并返回 $c$。攻击者可以任意多次查询该预言机，因此该定义刻画的是用同一公钥加密多条（未知）消息时的安全性。

Formally, consider the following experiment defined for an adversary $\mathcal{A}$ and a public-key encryption scheme $\Pi = (\mathsf{Gen}, \mathsf{Enc}, \mathsf{Dec})$:

严格地说，对敌手 $\mathcal{A}$ 和公钥加密方案 $\Pi = (\mathsf{Gen}, \mathsf{Enc}, \mathsf{Dec})$，考虑如下实验：

The LR-oracle experiment $\mathsf{PubK}_{\mathcal{A},\Pi}^{\mathsf{LR-cpa}}(n)$:

LR 预言机实验 $\mathsf{PubK}_{\mathcal{A},\Pi}^{\mathsf{LR-cpa}}(n)$：

1. $\mathsf{Gen}(1^{n})$ is run to obtain keys (pk, sk).

   运行 $\mathsf{Gen}(1^{n})$ 得到密钥 $(pk, sk)$。

2. A uniform bit $b \in \{0,1\}$ is chosen.

   均匀选取一个比特 $b \in \{0,1\}$。

3. The adversary $\mathcal{A}$ is given input $pk$ and oracle access to $\mathsf{LR}_{pk,b}(\cdot,\cdot)$

   敌手 $\mathcal{A}$ 获得输入 $pk$，并可访问预言机 $\mathsf{LR}_{pk,b}(\cdot,\cdot)$。

4. The adversary $\mathcal{A}$ outputs a bit $b'$.

   敌手 $\mathcal{A}$ 输出一个比特 $b'$。

5. The output of the experiment is defined to be 1 if $b^{\prime} = b$, and 0 otherwise. If $\mathsf{PubK}_{\mathcal{A},\Pi}^{\mathsf{LR-cpa}}(n) = 1$, we say that $\mathcal{A}$ succeeds.

   若 $b^{\prime} = b$，则实验输出定义为 1；否则为 0。若 $\mathsf{PubK}_{\mathcal{A},\Pi}^{\mathsf{LR-cpa}}(n) = 1$，则称 $\mathcal{A}$ 成功。

DEFINITION 12.5 A public-key encryption scheme $\Pi = (\mathsf{Gen}, \mathsf{Enc}, \mathsf{Dec})$ has indistinguishable multiple encryptions if for all probabilistic polynomial-time adversaries $\mathcal{A}$ there exists a negligible function $\mathsf{negl}$ such that:

定义 12.5　称公钥加密方案 $\Pi = (\mathsf{Gen}, \mathsf{Enc}, \mathsf{Dec})$ 具有不可区分的多重加密，如果对所有概率多项式时间敌手 $\mathcal{A}$，都存在可忽略函数 $\mathsf{negl}$ 使得：

$$
\Pr[\mathsf{PubK}_{\mathcal{A},\Pi}^{\mathsf{LR-cpa}}(n)=1]\leq\frac{1}{2}+\mathsf{negl}(n).
$$

We will show that any CPA-secure scheme automatically has indistinguishable multiple encryptions; that is, in the public-key setting, security for encryption of a single message implies security for encryption of multiple messages. This means if we can prove security of some scheme with respect to Definition 12.2, which is simpler and easier to work with, we may then conclude that the scheme satisfies Definition 12.5, a seemingly stronger definition that more accurately models real-world usage of public-key encryption. A proof of the following theorem is given below.

我们将证明，任何选择明文安全的方案都自动具有不可区分的多重加密；也就是说，在公钥情形中，加密单个消息的安全性蕴含加密多个消息的安全性。这意味着，如果我们能就定义 12.2——一个更简单、更便于使用的定义——证明某个方案的安全性，就可以断言该方案满足定义 12.5，后者看似更强，且更准确地刻画了公钥加密的实际使用。下面给出下述定理的证明。

THEOREM 12.6 If public-key encryption scheme $\Pi$ is CPA-secure, then it also has indistinguishable multiple encryptions.

定理 12.6　若公钥加密方案 $\Pi$ 是选择明文安全的，则它也具有不可区分的多重加密。

An analogous result in the private-key setting was stated, but not proved, as Theorem 3.23.

私钥情形中的类似结果曾作为定理 3.23 陈述，但未予证明。

**Encrypting arbitrary-length messages.**

**加密任意长度的消息。**

An immediate consequence of Theorem 12.6 is that a CPA-secure public-key encryption scheme for fixed-length messages implies a public-key encryption scheme for arbitrary-length messages satisfying the same notion of security. We illustrate this in the extreme case when the original scheme encrypts only 1-bit messages. Say $\Pi = (\mathsf{Gen}, \mathsf{Enc}, \mathsf{Dec})$ is an encryption scheme for single-bit messages. We can construct a new scheme $\Pi^{\prime} = (\mathsf{Gen}, \mathsf{Enc}^{\prime}, \mathsf{Dec}^{\prime})$ that has message space $\{0,1\}^*$ by defining $\mathsf{Enc}^{\prime}$ as follows:

定理 12.6 的一个直接推论是：针对定长消息的选择明文安全公钥加密方案，蕴含着一个可加密任意长度消息、且满足同样安全定义的公钥加密方案。我们以极端情形来说明这一点：假设原方案只能加密 1 比特消息。设 $\Pi = (\mathsf{Gen}, \mathsf{Enc}, \mathsf{Dec})$ 是单比特消息的加密方案。我们可以构造一个消息空间为 $\{0,1\}^*$ 的新方案 $\Pi^{\prime} = (\mathsf{Gen}, \mathsf{Enc}^{\prime}, \mathsf{Dec}^{\prime})$，其 $\mathsf{Enc}^{\prime}$ 定义如下：

$$
\mathsf{Enc}_{pk}^{\prime}(m)=\mathsf{Enc}_{pk}(m_{1}),\ldots,\mathsf{Enc}_{pk}(m_{\ell}), \tag{12.1}
$$

where $m = m_1 \cdots m_\ell$. (The decryption algorithm $\mathsf{Dec}^{\prime}$ is constructed in the obvious way.) We have:

其中 $m = m_1 \cdots m_\ell$。（解密算法 $\mathsf{Dec}^{\prime}$ 以显然的方式构造。）我们有：

**CLAIM 12.7** Let $\Pi$ and $\Pi^{\prime}$ be as above. If $\Pi$ is CPA-secure, then so is $\Pi^{\prime}$.

**断言 12.7**　设 $\Pi$ 与 $\Pi^{\prime}$ 如上所述。若 $\Pi$ 是选择明文安全的，则 $\Pi^{\prime}$ 也是。

The claim follows since we can view encryption of the message $m$ using $\Pi^{\prime}$ as encryption of $\ell$ messages $(m_1, \ldots, m_\ell)$ using scheme $\Pi$.

该断言成立，因为用 $\Pi^{\prime}$ 加密消息 $m$ 可以看作是用方案 $\Pi$ 加密 $\ell$ 条消息 $(m_1, \ldots, m_\ell)$。

**A note on terminology.**

**关于术语的说明。**

We have introduced three definitions of security for public-key encryption schemes—indistinguishable encryptions in the presence of an eavesdropper, CPA-security, and indistinguishable multiple encryptions—that are all equivalent. Following the usual convention in the cryptographic literature, we will simply use the term “CPA-security” to refer to schemes meeting these notions of security.

我们已经引入了公钥加密方案的三种安全定义——窃听者存在下不可区分的加密、选择明文安全、不可区分的多重加密——它们彼此等价。遵循密码学文献的惯常约定，我们将统一用“选择明文安全”一词来指代满足这些安全概念的方案。

### \*Proof of Theorem 12.6　\*定理 12.6 的证明

The proof of Theorem 12.6 is rather involved. We therefore provide some intuition before turning to the details. For this intuitive discussion we assume for simplicity that $\mathcal{A}$ makes only two calls to the LR oracle in experiment $\mathsf{PubK}_{\mathcal{A},\Pi}^{\mathsf{LR-cpa}}(n)$. (In the full proof, the number of calls can be arbitrary.)

定理 12.6 的证明相当复杂。因此我们先给出一些直观说明，再进入细节。在这段直观讨论中，为简单起见，我们假定 $\mathcal{A}$ 在实验 $\mathsf{PubK}_{\mathcal{A},\Pi}^{\mathsf{LR-cpa}}(n)$ 中只调用两次 LR 预言机。（在完整证明中，调用次数可以是任意的。）

Fix an arbitrary PPT adversary $\mathcal{A}$ and a CPA-secure public-key encryption scheme $\Pi$, and consider an experiment $\mathsf{PubK}_{\mathcal{A},\Pi}^{\mathsf{LR-cpa2}}(n)$ where $\mathcal{A}$ can make only two queries to the LR oracle. Denote the queries made by $\mathcal{A}$ to the oracle by $(m_{1,0}, m_{1,1})$ and $(m_{2,0}, m_{2,1})$; note that the second pair of messages may depend on the first ciphertext obtained by $\mathcal{A}$ from the oracle. In the experiment, $\mathcal{A}$ receives either a pair of ciphertexts $(\mathsf{Enc}_{pk}(m_{1,0}), \mathsf{Enc}_{pk}(m_{2,0}))$ (if $b = 0$), or a pair of ciphertexts $(\mathsf{Enc}_{pk}(m_{1,1}), \mathsf{Enc}_{pk}(m_{2,1}))$ (if $b = 1$). We write $\mathcal{A}(pk, \mathsf{Enc}_{pk}(m_{1,0}), \mathsf{Enc}_{pk}(m_{2,0}))$ to denote the output of $\mathcal{A}$ in the first case, and analogously for the second.

固定任意的概率多项式时间（PPT）敌手 $\mathcal{A}$ 和选择明文安全的公钥加密方案 $\Pi$，考虑实验 $\mathsf{PubK}_{\mathcal{A},\Pi}^{\mathsf{LR-cpa2}}(n)$，其中 $\mathcal{A}$ 只能向 LR 预言机查询两次。把 $\mathcal{A}$ 向预言机发出的查询记为 $(m_{1,0}, m_{1,1})$ 和 $(m_{2,0}, m_{2,1})$；注意第二对消息可能依赖于 $\mathcal{A}$ 从预言机获得的第一个密文。在实验中，$\mathcal{A}$ 要么收到一对密文 $(\mathsf{Enc}_{pk}(m_{1,0}), \mathsf{Enc}_{pk}(m_{2,0}))$（当 $b = 0$ 时），要么收到一对密文 $(\mathsf{Enc}_{pk}(m_{1,1}), \mathsf{Enc}_{pk}(m_{2,1}))$（当 $b = 1$ 时）。我们用 $\mathcal{A}(pk, \mathsf{Enc}_{pk}(m_{1,0}), \mathsf{Enc}_{pk}(m_{2,0}))$ 表示第一种情形下 $\mathcal{A}$ 的输出，第二种情形类似。

Let $\vec{C}_0$ denote the distribution of ciphertext pairs in the first case, and $\vec{C}_1$ the distribution of ciphertext pairs in the second case. To show that Definition 12.5 holds (for $\mathsf{PubK}_{\mathcal{A},\Pi}^{\mathsf{LR-cpa2}}$), we need to prove that $\mathcal{A}$ cannot distinguish between being given a pair of ciphertexts distributed according to $\vec{C}_0$, or a pair of ciphertexts distributed according to $\vec{C}_1$. That is, we need to prove that there is a negligible function $\mathsf{negl}$ such that

令 $\vec{C}_0$ 表示第一种情形下密文对的分布，$\vec{C}_1$ 表示第二种情形下密文对的分布。要证明定义 12.5 成立（对 $\mathsf{PubK}_{\mathcal{A},\Pi}^{\mathsf{LR-cpa2}}$ 而言），需要证明 $\mathcal{A}$ 无法区分以下两种情形：拿到的密文对服从分布 $\vec{C}_0$，还是服从分布 $\vec{C}_1$。也就是说，我们需要证明存在可忽略函数 $\mathsf{negl}$ 使得

$$
\begin{aligned}
&\left|\Pr[\mathcal{A}(pk,\mathsf{Enc}_{pk}(m_{1,0}),\mathsf{Enc}_{pk}(m_{2,0}))=1]\right.\\
&\left.\quad-\Pr[\mathcal{A}(pk,\mathsf{Enc}_{pk}(m_{1,1}),\mathsf{Enc}_{pk}(m_{2,1}))=1]\right|\leq\mathsf{negl}(n).
\end{aligned} \tag{12.2}
$$

(This is equivalent to Definition 12.5 for the same reason that Definition 3.9 is equivalent to Definition 3.8.) To prove this, we will show that

（这与定义 12.5 等价，其理由与定义 3.9 等价于定义 3.8 相同。）为证明这一点，我们将证明：

1. CPA-security of $\Pi$ implies that $\mathcal{A}$ cannot distinguish between the case when it is given a pair of ciphertexts distributed according to $\vec{C}_0$, or a pair of ciphertexts ( $\mathsf{Enc}_{pk}(m_{1,0})$, $\mathsf{Enc}_{pk}(m_{2,1})$), which corresponds to encrypting the first message in $\mathcal{A}$'s first oracle query and the second message in $\mathcal{A}$'s second oracle query. (Although this cannot occur in $\mathsf{PubK}_{\mathcal{A},\Pi}^{\mathsf{LR-cpa2}}(n)$, we can still ask what $\mathcal{A}$'s behavior would be if given such a ciphertext pair.) Let $\vec{C}_{01}$ denote the distribution of ciphertext pairs in this latter case.

   $\Pi$ 的选择明文安全性意味着 $\mathcal{A}$ 无法区分以下两种情形：拿到的密文对服从分布 $\vec{C}_0$，还是拿到密文对（$\mathsf{Enc}_{pk}(m_{1,0})$，$\mathsf{Enc}_{pk}(m_{2,1})$）——后者对应于加密 $\mathcal{A}$ 第一次预言机查询中的第一条消息和第二次查询中的第二条消息。（虽然这种情形不可能在 $\mathsf{PubK}_{\mathcal{A},\Pi}^{\mathsf{LR-cpa2}}(n)$ 中发生，但我们仍可以问：如果给 $\mathcal{A}$ 这样的密文对，它的行为会如何？）令 $\vec{C}_{01}$ 表示后一种情形下密文对的分布。

2. Similarly, CPA-security of $\Pi$ implies that $\mathcal{A}$ cannot distinguish between the case when it is given a pair of ciphertexts distributed according to $\vec{C}_{01}$, or a pair of ciphertexts distributed according to $\vec{C}_{1}$.

   类似地，$\Pi$ 的选择明文安全性意味着 $\mathcal{A}$ 无法区分“拿到的密文对服从分布 $\vec{C}_{01}$”与“拿到的密文对服从分布 $\vec{C}_{1}$”这两种情形。

The above says that $\mathcal{A}$ cannot distinguish between distributions $\vec{C}_0$ and $\vec{C}_{01}$, nor between distributions $\vec{C}_{01}$ and $\vec{C}_1$. We conclude (using simple algebra) that $\mathcal{A}$ cannot distinguish between distributions $\vec{C}_0$ and $\vec{C}_1$.

上述论证表明，$\mathcal{A}$ 既不能区分分布 $\vec{C}_0$ 与 $\vec{C}_{01}$，也不能区分分布 $\vec{C}_{01}$ 与 $\vec{C}_1$。由此（通过简单的代数运算）可以断言：$\mathcal{A}$ 无法区分分布 $\vec{C}_0$ 与 $\vec{C}_1$。

The crux of the proof, then, is showing that $\mathcal{A}$ cannot distinguish between being given a pair of ciphertexts distributed according to $\vec{C}_0$, or a pair of ciphertexts distributed according to $\vec{C}_{01}$. (The other case follows similarly.) That is, we want to show that there is a negligible function $\mathsf{negl}$ for which

因此，证明的关键在于说明 $\mathcal{A}$ 无法区分“拿到服从分布 $\vec{C}_0$ 的密文对”与“拿到服从分布 $\vec{C}_{01}$ 的密文对”这两种情形。（另一种情形可类似证明。）也就是说，我们要证明存在可忽略函数 $\mathsf{negl}$ 使得

$$
\begin{aligned}
&\left|\Pr[\mathcal{A}\left(pk,\mathsf{Enc}_{pk}(m_{1,0}),\mathsf{Enc}_{pk}(m_{2,0})\right)=1]\right.\\
&\left.\quad-\Pr[\mathcal{A}\left(pk,\mathsf{Enc}_{pk}(m_{1,0}),\mathsf{Enc}_{pk}(m_{2,1})\right)=1]\right|\leq\mathsf{negl}(n).
\end{aligned} \tag{12.3}
$$

Note that the only difference between the input of the adversary $\mathcal{A}$ in each case is in the second element. Intuitively, indistinguishability follows from the single-message case since $\mathcal{A}$ can generate $\mathsf{Enc}_{pk}(m_{1,0})$ by itself. Formally, consider the following PPT adversary $\mathcal{A}^{\prime}$ running in experiment $\mathsf{PubK}_{\mathcal{A}^{\prime},\Pi}^{\mathsf{eav}}(n)$:

注意，两种情形下敌手 $\mathcal{A}$ 的输入只有第二个元素不同。直观上，不可区分性可由单消息情形推出，因为 $\mathcal{A}$ 自己可以生成 $\mathsf{Enc}_{pk}(m_{1,0})$。严格地说，考虑如下运行于实验 $\mathsf{PubK}_{\mathcal{A}^{\prime},\Pi}^{\mathsf{eav}}(n)$ 中的 PPT 敌手 $\mathcal{A}^{\prime}$：

**Adversary $\mathcal{A}'$:**

**敌手 $\mathcal{A}^{\prime}$：**

1. On input $pk$, adversary $\mathcal{A}^{\prime}$ runs $\mathcal{A}(pk)$ as a subroutine.

   输入 $pk$ 后，敌手 $\mathcal{A}^{\prime}$ 以子程序方式运行 $\mathcal{A}(pk)$。

2. When $\mathcal{A}$ makes its first query $(m_{1,0}, m_{1,1})$ to the LR oracle, $\mathcal{A}^{\prime}$ computes $c_1 \leftarrow \mathsf{Enc}_{pk}(m_{1,0})$ and returns $c_1$ to $\mathcal{A}$ as the response from the oracle.

   当 $\mathcal{A}$ 向 LR 预言机发出第一次查询 $(m_{1,0}, m_{1,1})$ 时，$\mathcal{A}^{\prime}$ 计算 $c_1 \leftarrow \mathsf{Enc}_{pk}(m_{1,0})$，并把 $c_1$ 作为预言机的应答返回给 $\mathcal{A}$。

3. When $\mathcal{A}$ makes its second query $(m_{2,0}, m_{2,1})$ to the LR oracle, $\mathcal{A}^{\prime}$ outputs $(m_{2,0}, m_{2,1})$ and receives back a challenge ciphertext $c_2$. This is returned to $\mathcal{A}$ as the response from the LR oracle.

   当 $\mathcal{A}$ 向 LR 预言机发出第二次查询 $(m_{2,0}, m_{2,1})$ 时，$\mathcal{A}^{\prime}$ 输出 $(m_{2,0}, m_{2,1})$，并收到返回的挑战密文 $c_2$。随后 $\mathcal{A}^{\prime}$ 把 $c_2$ 作为 LR 预言机的应答返回给 $\mathcal{A}$。

4. $\mathcal{A}^{\prime}$ outputs the bit $b^{\prime}$ output by $\mathcal{A}$.

   $\mathcal{A}^{\prime}$ 输出 $\mathcal{A}$ 所输出的比特 $b^{\prime}$。

Looking at experiment $\mathsf{PubK}_{\mathcal{A}^{\prime},\Pi}^{\mathsf{eav}}(n)$, we see that when $b = 0$ then the challenge ciphertext $c_2$ is computed as $\mathsf{Enc}_{pk}(m_{2,0})$. Thus,

观察实验 $\mathsf{PubK}_{\mathcal{A}^{\prime},\Pi}^{\mathsf{eav}}(n)$，我们看到当 $b = 0$ 时，挑战密文 $c_2$ 按 $\mathsf{Enc}_{pk}(m_{2,0})$ 计算。因此，

$$
\Pr[\mathcal{A}^{\prime}\left(\mathsf{Enc}_{pk}(m_{2,0})\right)=1]=\Pr[\mathcal{A}\left(\mathsf{Enc}_{pk}(m_{1,0}),\mathsf{Enc}_{pk}(m_{2,0})\right)=1]. \tag{12.4}
$$

(We suppress explicit mention of pk to save space.) In contrast, when $b = 1$ in experiment $\mathsf{PubK}_{\mathcal{A}^{\prime},\Pi}^{\mathsf{eav}}(n)$, then $c_2$ is computed as $\mathsf{Enc}_{pk}(m_{2,1})$ and so

（为节省篇幅，这里省略了对 $pk$ 的显式提及。）相反，当实验 $\mathsf{PubK}_{\mathcal{A}^{\prime},\Pi}^{\mathsf{eav}}(n)$ 中 $b = 1$ 时，$c_2$ 按 $\mathsf{Enc}_{pk}(m_{2,1})$ 计算，于是

$$
\Pr[\mathcal{A}^{\prime}\left(\mathsf{Enc}_{pk}(m_{2,1})\right)=1]=\Pr[\mathcal{A}\left(\mathsf{Enc}_{pk}(m_{1,0}),\mathsf{Enc}_{pk}(m_{2,1})\right)=1]. \tag{12.5}
$$

CPA-security of $\Pi$ implies that there is a negligible function $\mathsf{negl}$ such that

$\Pi$ 的选择明文安全性意味着存在可忽略函数 $\mathsf{negl}$ 使得

$$
\left|\Pr[\mathcal{A}^{\prime}(\mathsf{Enc}_{pk}(m_{2,0}))=1]-\Pr[\mathcal{A}^{\prime}(\mathsf{Enc}_{pk}(m_{2,1}))=1]\right|\leq\mathsf{negl}(n).
$$

This, together with Equations (12.4) and (12.5), yields Equation (12.3).

这与式 (12.4)、(12.5) 结合，即得式 (12.3)。

In almost exactly the same way, we can prove that:

用几乎完全相同的方法，可以证明：

$$
\begin{aligned}
&\left|\Pr[\mathcal{A}\left(pk,\mathsf{Enc}_{pk}(m_{1,0}),\mathsf{Enc}_{pk}(m_{2,1})\right)=1]\right.\\
&\left.\quad-\Pr[\mathcal{A}\left(pk,\mathsf{Enc}_{pk}(m_{1,1}),\mathsf{Enc}_{pk}(m_{2,1})\right)=1]\right|\leq\mathsf{negl}(n).
\end{aligned} \tag{12.6}
$$

Equation (12.2) follows by combining Equations (12.3) and (12.6).

将式 (12.3) 与式 (12.6) 结合即得式 (12.2)。

The main complication that arises in the general case is that the number of queries to the LR oracle is no longer fixed but may instead be an arbitrary polynomial of n. In the formal proof this is handled using a hybrid argument. (Hybrid arguments were used also in Chapter 8.)

一般情形下的主要困难在于，对 LR 预言机的查询次数不再是固定的，而可以是 $n$ 的任意多项式。在形式化证明中，这用混合论证来处理。（第 8 章也使用了混合论证。）

PROOF (of Theorem 12.6) Let $\Pi$ be a CPA-secure public-key encryption scheme and $\mathcal{A}$ an arbitrary PPT adversary in experiment $\mathsf{PubK}_{\mathcal{A},\Pi}^{\mathsf{LR-cpa}}(n)$. Let $t = t(n)$ be a polynomial upper bound on the number of queries made by $\mathcal{A}$ to the $\mathsf{LR}$ oracle, and assume without loss of generality that $\mathcal{A}$ always queries the oracle exactly this many times. For a given public key $pk$ and $0 \leq i \leq t$, let $\mathsf{LR}_{pk}^{i}$ denote the oracle that on input $(m_0, m_1)$ returns $\mathsf{Enc}_{pk}(m_0)$ for the first $i$ queries it receives, and returns $\mathsf{Enc}_{pk}(m_1)$ for the next $t - i$ queries it receives. (That is, for the first $i$ queries the first message in the input pair is encrypted, and for the remaining queries the second message in the input pair is encrypted.) We stress that each encryption is computed using uniform, independent randomness. Using this notation, we have

证明（定理 12.6）　设 $\Pi$ 是选择明文安全的公钥加密方案，$\mathcal{A}$ 是实验 $\mathsf{PubK}_{\mathcal{A},\Pi}^{\mathsf{LR-cpa}}(n)$ 中任意的 PPT 敌手。令 $t = t(n)$ 为 $\mathcal{A}$ 向 $\mathsf{LR}$ 预言机查询次数的多项式上界，且不失一般性地假定 $\mathcal{A}$ 总是恰好查询这么多次。对给定的公钥 $pk$ 和 $0 \leq i \leq t$，用 $\mathsf{LR}_{pk}^{i}$ 表示如下预言机：在输入 $(m_0, m_1)$ 时，它对接收到的前 $i$ 次查询返回 $\mathsf{Enc}_{pk}(m_0)$，对接下来的 $t - i$ 次查询返回 $\mathsf{Enc}_{pk}(m_1)$。（也就是说，前 $i$ 次查询加密输入对中的第一条消息，其余查询加密输入对中的第二条消息。）我们强调，每次加密都使用均匀且独立的随机性来计算。采用这一记号，我们有

$$
\Pr\left[\mathsf{PubK}_{\mathcal{A},\Pi}^{\mathsf{LR-cpa}}(n)=1\right]=\frac{1}{2}\cdot\Pr[\mathcal{A}^{\mathsf{LR}_{pk}^{t}}(pk)=0]+\frac{1}{2}\cdot\Pr[\mathcal{A}^{\mathsf{LR}_{pk}^{0}}(pk)=1]
$$

because oracle $\mathsf{LR}_{pk}^{t}$ is equivalent to $\mathsf{LR}_{pk,0}$, and oracle $\mathsf{LR}_{pk}^{0}$ is equivalent to $\mathsf{LR}_{pk,1}$. To prove that $\Pi$ satisfies Definition 12.5, we will show that for any PPT $\mathcal{A}$ there is a negligible function $\mathsf{negl}^{\prime}$ such that

因为预言机 $\mathsf{LR}_{pk}^{t}$ 等价于 $\mathsf{LR}_{pk,0}$，而预言机 $\mathsf{LR}_{pk}^{0}$ 等价于 $\mathsf{LR}_{pk,1}$。为证明 $\Pi$ 满足定义 12.5，我们将证明：对任意 PPT $\mathcal{A}$，都存在可忽略函数 $\mathsf{negl}^{\prime}$ 使得

$$
\left|\Pr[\mathcal{A}^{\mathsf{LR}_{pk}^{t}}(pk)=1]-\Pr[\mathcal{A}^{\mathsf{LR}_{pk}^{0}}(pk)=1]\right|\leq\mathsf{negl}^{\prime}(n).
$$

(As before, this is equivalent to Definition 12.5 for the same reason that Definition 3.9 is equivalent to Definition 3.8.)

（与前面一样，这与定义 12.5 等价，理由与定义 3.9 等价于定义 3.8 相同。）

Consider the following PPT adversary $\mathcal{A}^{\prime}$ that eavesdrops on the encryption of a single message:

考虑如下窃听单条消息加密的 PPT 敌手 $\mathcal{A}^{\prime}$：

Adversary A':

敌手 $\mathcal{A}^{\prime}$：

1. $\mathcal{A}^{\prime}$, given pk, chooses a uniform index $i \leftarrow \{1, \ldots, t\}$

   $\mathcal{A}^{\prime}$ 拿到 $pk$ 后，均匀选取下标 $i \leftarrow \{1, \ldots, t\}$。

2. $\mathcal{A}^{\prime}$ runs $\mathcal{A}(pk)$, answering its jth oracle query $(m_{j,0}, m_{j,1})$ as follows:

   $\mathcal{A}^{\prime}$ 运行 $\mathcal{A}(pk)$，并按如下方式应答其第 $j$ 次预言机查询 $(m_{j,0}, m_{j,1})$：

(a) For $j < i$, adversary $\mathcal{A}^{\prime}$ computes $c_j \leftarrow \mathsf{Enc}_{pk}(m_{j,0})$ and returns $c_j$ to $\mathcal{A}$ as the response from its oracle.

   (a) 当 $j < i$ 时，敌手 $\mathcal{A}^{\prime}$ 计算 $c_j \leftarrow \mathsf{Enc}_{pk}(m_{j,0})$，并把 $c_j$ 作为其预言机的应答返回给 $\mathcal{A}$。

(b) For $j = i$, adversary $\mathcal{A}^{\prime}$ outputs $(m_{j,0}, m_{j,1})$ and receives back a challenge ciphertext $c_j$. This is returned to $\mathcal{A}$ as the response from its oracle.

   (b) 当 $j = i$ 时，敌手 $\mathcal{A}^{\prime}$ 输出 $(m_{j,0}, m_{j,1})$，并收到返回的挑战密文 $c_j$。随后 $\mathcal{A}^{\prime}$ 把 $c_j$ 作为其预言机的应答返回给 $\mathcal{A}$。

(c) For $j > i$, adversary $\mathcal{A}^{\prime}$ computes $c_j \leftarrow \mathsf{Enc}_{pk}(m_{j,1})$ and returns $c_j$ to $\mathcal{A}$ as the response from its oracle.

   (c) 当 $j > i$ 时，敌手 $\mathcal{A}^{\prime}$ 计算 $c_j \leftarrow \mathsf{Enc}_{pk}(m_{j,1})$，并把 $c_j$ 作为其预言机的应答返回给 $\mathcal{A}$。

3. $\mathcal{A}^{\prime}$ outputs the bit $b^{\prime}$ that is output by $\mathcal{A}$.

   $\mathcal{A}^{\prime}$ 输出 $\mathcal{A}$ 所输出的比特 $b^{\prime}$。

Consider experiment $\mathsf{PubK}_{\mathcal{A}^{\prime},\Pi}^{\mathsf{eav}}(n)$. Fixing some choice of $i = i^*$, note that if $c_{i^*}$ is an encryption of $m_{i^*,0}$ then the interaction of $\mathcal{A}$ with its oracle is identical to an interaction with oracle $\mathsf{LR}_{pk}^{i}$. Thus,

考虑实验 $\mathsf{PubK}_{\mathcal{A}^{\prime},\Pi}^{\mathsf{eav}}(n)$。固定某个选择 $i = i^*$，注意若 $c_{i^*}$ 是 $m_{i^*,0}$ 的加密，则 $\mathcal{A}$ 与其预言机的交互和它与预言机 $\mathsf{LR}_{pk}^{i}$ 的交互完全相同。因此，

$$
\begin{aligned}
\Pr[\mathcal{A}^{\prime}\text{ outputs }1\mid b=0]&=\sum_{i^{*}=1}^{t}\Pr[i=i^{*}]\cdot\Pr[\mathcal{A}^{\prime}\text{ outputs }1\mid b=0\land i=i^{*}]\\
&=\sum_{i^{*}=1}^{t}\frac{1}{t}\cdot\Pr\left[\mathcal{A}^{\mathsf{LR}_{pk}^{i^{*}}}(pk)=1\right].
\end{aligned}
$$

On the other hand, if $c_{i^*}$ is an encryption of $m_{i^*,1}$ then the interaction of $\mathcal{A}$ with its oracle is identical to an interaction with oracle $\mathsf{LR}_{pk}^{i^*-1}$, and so

另一方面，若 $c_{i^*}$ 是 $m_{i^*,1}$ 的加密，则 $\mathcal{A}$ 与其预言机的交互和它与预言机 $\mathsf{LR}_{pk}^{i^*-1}$ 的交互完全相同，于是

$$
\begin{aligned}
\Pr[\mathcal{A}^{\prime}\text{ outputs }1\mid b=1]&=\sum_{i^{*}=1}^{t}\Pr[i=i^{*}]\cdot\Pr[\mathcal{A}^{\prime}\text{ outputs }1\mid b=1\land i=i^{*}]\\
&=\sum_{i^{*}=1}^{t}\frac{1}{t}\cdot\Pr\left[\mathcal{A}^{\mathsf{LR}_{pk}^{i^{*}-1}}(pk)=1\right]\\
&=\sum_{i^{*}=0}^{t-1}\frac{1}{t}\cdot\Pr\left[\mathcal{A}^{\mathsf{LR}_{pk}^{i^{*}}}(pk)=1\right].
\end{aligned}
$$

Since $\mathcal{A}^{\prime}$ runs in polynomial time, the assumption that $\Pi$ is CPA-secure means that there exists a negligible function $\mathsf{negl}$ such that

由于 $\mathcal{A}^{\prime}$ 在多项式时间内运行，$\Pi$ 是选择明文安全的这一假定意味着存在可忽略函数 $\mathsf{negl}$ 使得

$$
\left|\Pr[\mathcal{A}^{\prime}\text{ outputs }1\mid b=0]-\Pr[\mathcal{A}^{\prime}\text{ outputs }1\mid b=1]\right|\leq\mathsf{negl}(n).
$$

But this means that

但这意味着

$$
\begin{aligned}
\mathsf{negl}(n)&\geq\left|\sum_{i^{*}=1}^{t}\frac{1}{t}\cdot\Pr\left[\mathcal{A}^{\mathsf{LR}_{pk}^{i^{*}}}(pk)=1\right]-\sum_{i^{*}=0}^{t-1}\frac{1}{t}\cdot\Pr\left[\mathcal{A}^{\mathsf{LR}_{pk}^{i^{*}}}(pk)=1\right]\right|\\
&=\frac{1}{t}\cdot\left|\Pr\left[\mathcal{A}^{\mathsf{LR}_{pk}^{t}}(pk)=1\right]-\Pr\left[\mathcal{A}^{\mathsf{LR}_{pk}^{0}}(pk)=1\right]\right|,
\end{aligned}
$$

since all but one of the terms in each summation cancel. We conclude that

因为每个求和式中除一项外其余各项全部抵消。我们得出结论：

$$
\left|\Pr\left[\mathcal{A}^{\mathsf{LR}_{pk}^{t}}(pk)=1\right]-\Pr\left[\mathcal{A}^{\mathsf{LR}_{pk}^{0}}(pk)=1\right]\right|\leq t(n)\cdot\mathsf{negl}(n). \tag{12.7}
$$

Because $t$ is polynomial, the function $t \cdot \mathsf{negl}(n)$ is negligible. Since $\mathcal{A}$ was an arbitrary PPT adversary, this shows that Equation (12.7) holds and so completes the proof that $\Pi$ has indistinguishable multiple encryptions.

由于 $t$ 是多项式，函数 $t \cdot \mathsf{negl}(n)$ 是可忽略的。又因为 $\mathcal{A}$ 是任意的 PPT 敌手，这表明式 (12.7) 成立，从而完成了“$\Pi$ 具有不可区分的多重加密”的证明。

### 12.2.3 Security against Chosen-Ciphertext Attacks　抵抗选择密文攻击的安全性

Chosen-ciphertext attacks, in which an adversary is able to obtain the decryption of arbitrary ciphertexts of its choice (with one technical restriction described below), are a concern in the public-key setting just as they are in the private-key setting. In fact, they are arguably more of a concern in the public-key setting since in that context a receiver expects to receive ciphertexts from multiple senders who are possibly unknown in advance, whereas a receiver in the private-key setting intends to communicate only with a single, known sender using any particular secret key.

选择密文攻击是指敌手能够获得其自行选择的任意密文的解密结果（受一个下文说明的技术性限制）；与私钥情形一样，这类攻击在公钥情形中同样令人担忧。事实上，可以说它在公钥情形中更值得关注，因为在公钥语境中，接收方预期会收到来自多个发送方的密文，而这些发送方事先可能是未知的；相比之下，私钥情形中的接收方只打算用某个特定的秘密密钥与单个已知的发送方通信。

Assume an eavesdropper $\mathcal{A}$ observes a ciphertext $c$ sent by a sender $\mathcal{S}$ to a receiver $\mathcal{R}$. Broadly speaking, in the public-key setting there are two ways in which $\mathcal{A}$ might carry out a chosen-ciphertext attack:

假设窃听者 $\mathcal{A}$ 观察到发送方 $\mathcal{S}$ 发给接收方 $\mathcal{R}$ 的一个密文 $c$。大致来说，在公钥情形中，$\mathcal{A}$ 可能以两种方式实施选择密文攻击：

- $\mathcal{A}$ might send a modified ciphertext $c^{\prime}$ to $\mathcal{R}$ on behalf of $\mathcal{S}$. (For example, in the context of encrypted e-mail, $\mathcal{A}$ might construct an encrypted e-mail $c^{\prime}$ and forge the “From” field so that it appears the e-mail originated from $\mathcal{S}$.) In this case, although it is unlikely that $\mathcal{A}$ would be able to obtain the entire decryption $m^{\prime}$ of $c^{\prime}$, it might be possible for $\mathcal{A}$ to infer some information about $m^{\prime}$ based on the subsequent behavior of $\mathcal{R}$. Based on this information, $\mathcal{A}$ might be able to learn something about the original message m.

- $\mathcal{A}$ 可能以 $\mathcal{S}$ 的名义向 $\mathcal{R}$ 发送一个修改过的密文 $c^{\prime}$。（例如，在加密电子邮件的语境中，$\mathcal{A}$ 可能构造一封加密邮件 $c^{\prime}$，并伪造“发件人”字段，使其看起来像是发自 $\mathcal{S}$。）在这种情况下，$\mathcal{A}$ 虽然不太可能获得 $c^{\prime}$ 的完整解密结果 $m^{\prime}$，但也许能根据 $\mathcal{R}$ 随后的行为推断出关于 $m^{\prime}$ 的一些信息。基于这些信息，$\mathcal{A}$ 也许能了解到关于原始消息 $m$ 的某些内容。

- $\mathcal{A}$ might send a modified ciphertext $c^{\prime}$ to $\mathcal{R}$ in its own name. In this case, $\mathcal{A}$ might obtain the entire decryption $m^{\prime}$ of $c^{\prime}$ if $\mathcal{R}$ responds directly to $\mathcal{A}$. Even if $\mathcal{A}$ learns nothing about $m^{\prime}$, this modified message may have a known relation to the original message $m$ that can be exploited by $\mathcal{A}$; see the third scenario below for an example.

- $\mathcal{A}$ 可能以自己的名义向 $\mathcal{R}$ 发送一个修改过的密文 $c^{\prime}$。在这种情况下，如果 $\mathcal{R}$ 直接回复 $\mathcal{A}$，$\mathcal{A}$ 就可能获得 $c^{\prime}$ 的完整解密结果 $m^{\prime}$。即使 $\mathcal{A}$ 对 $m^{\prime}$ 一无所知，这个修改后的消息也可能与原始消息 $m$ 存在某种已知的关系，从而被 $\mathcal{A}$ 利用；例子见下面的第三个场景。

The second class of attacks is specific to the setting of public-key encryption, and has no analogue in the private-key case.

第二类攻击是公钥加密情形特有的，在私钥情形中没有对应物。

It is not hard to identify a number of realistic scenarios illustrating the above types of attacks:

不难举出多个说明上述攻击类型的现实场景：

Scenario 1. Say a user $S$ logs in to her bank account by sending to her bank an encryption of her password $pw$ concatenated with a timestamp. Assume further that there are two types of error messages the bank sends: it returns "password incorrect" if the encrypted password does not match the stored password of S, and "timestamp incorrect" if the password is correct but the timestamp is not.

**场景 1。**
设用户 $S$ 登录其银行账户的方式是：向银行发送她的口令 $pw$ 与一个时间戳拼接后的加密。进一步假设银行会发送两类错误消息：若加密的口令与银行存储的 $S$ 的口令不匹配，返回“password incorrect”（口令不正确）；若口令正确但时间戳不正确，返回“timestamp incorrect”（时间戳不正确）。

If an adversary obtains a ciphertext $c$ sent by $\mathcal{S}$ to the bank, the adversary can now mount a chosen-ciphertext attack by sending ciphertexts $c^{\prime}$ to the bank on behalf of $\mathcal{S}$ and observing the error messages that are sent in response. (This is similar to the padding-oracle attack that we saw in Section 5.1.1.) In some cases, this information may be enough to allow the adversary to determine the user's entire password.

如果敌手获得了一个 $\mathcal{S}$ 发给银行的密文 $c$，它现在就可以实施选择密文攻击：以 $\mathcal{S}$ 的名义向银行发送密文 $c^{\prime}$，并观察返回的错误消息。（这与 5.1.1 节中看到的填充预言机攻击类似。）在某些情况下，这些信息可能足以让敌手确定用户的完整口令。

Scenario 2. Say $S$ sends an encrypted e-mail $c$ to $\mathcal{R}$, and this e-mail is observed by $\mathcal{A}$. If $\mathcal{A}$ sends, in its own name, an encrypted e-mail $c^{\prime}$ to $\mathcal{R}$, then $\mathcal{R}$ might reply to this e-mail and quote the decrypted text $m^{\prime}$ corresponding to $c^{\prime}$. In this case, $\mathcal{R}$ is essentially acting as a decryption oracle for $\mathcal{A}$ and might potentially decrypt any ciphertext that $\mathcal{A}$ sends it.

**场景 2。**
设 $S$ 向 $\mathcal{R}$ 发送了一封加密邮件 $c$，且该邮件被 $\mathcal{A}$ 观察到。如果 $\mathcal{A}$ 以自己的名义向 $\mathcal{R}$ 发送加密邮件 $c^{\prime}$，那么 $\mathcal{R}$ 可能会回复这封邮件，并引用 $c^{\prime}$ 对应的解密文本 $m^{\prime}$。此时，$\mathcal{R}$ 实际上充当了 $\mathcal{A}$ 的解密预言机，有可能解密 $\mathcal{A}$ 发给它的任何密文。

Scenario 3. An issue that is closely related to that of chosen-ciphertext security is potential malleability of ciphertexts. We do not provide a formal definition but instead only give the intuitive idea. An encryption scheme is malleable if it has the following property: given an encryption $c$ of some unknown message $m$, it is possible to come up with a ciphertext $c^{\prime}$ that is an encryption of a message $m^{\prime}$ that is related in some known way to m. For example, perhaps given an encryption of m, it is possible to construct an encryption of $m+1$. (Later we will see natural examples of CPA-secure schemes that are malleable; see also Section 15.2.3.)

**场景 3。**
与选择密文安全性密切相关的一个问题是密文潜在的可延展性（malleability）。我们不给出形式化定义，只给出直观概念。称一个加密方案是可延展的，如果它具有如下性质：给定某个未知消息 $m$ 的加密 $c$，可以构造出一个密文 $c^{\prime}$，它是某个与 $m$ 有已知关系的消息 $m^{\prime}$ 的加密。例如，给定 $m$ 的加密，也许可以构造出 $m+1$ 的加密。（稍后我们会看到选择明文安全但可延展的方案的自然例子；另见 15.2.3 节。）

Now imagine that $\mathcal{R}$ is running an auction, where two parties $\mathcal{S}$ and $\mathcal{A}$ submit their bids by encrypting them using the public key of $\mathcal{R}$. If a malleable encryption scheme is used, it may be possible for an adversary $\mathcal{A}$ to always place the higher bid (without bidding the maximum) by carrying out the following attack: wait until $\mathcal{S}$ sends a ciphertext $c$ corresponding to its bid $m$ (that is unknown to $\mathcal{A}$); then send a ciphertext $c^{\prime}$ corresponding to the bid $m^{\prime} = m + 1$. Note that $m$ (and $m^{\prime}$, for that matter) remain unknown to $\mathcal{A}$ until $\mathcal{R}$ announces the results, and so the possibility of such an attack does not contradict the fact that the encryption scheme is CPA-secure. Schemes secure against chosen-ciphertext attacks, on the other hand, can be shown to be non-malleable and so are not vulnerable to such attacks.

现在设想 $\mathcal{R}$ 正在举办一场拍卖，两方 $\mathcal{S}$ 和 $\mathcal{A}$ 通过用 $\mathcal{R}$ 的公钥加密来提交各自的出价。如果使用了可延展的加密方案，敌手 $\mathcal{A}$ 也许能通过实施如下攻击总是报出更高的出价（而不必报出最高价）：等到 $\mathcal{S}$ 发送对应于其出价 $m$（$\mathcal{A}$ 不知道 $m$）的密文 $c$；然后发送对应于出价 $m^{\prime} = m + 1$ 的密文 $c^{\prime}$。注意，在 $\mathcal{R}$ 公布结果之前，$m$（以及 $m^{\prime}$）对 $\mathcal{A}$ 一直是未知的，因此这种攻击的可能性并不与该加密方案是选择明文安全的这一事实相矛盾。另一方面，可以证明，抵抗选择密文攻击的方案是不可延展的，因而不会受到此类攻击的威胁。

**The definition.**

**安全定义。**

Security against chosen-ciphertext attacks is defined by suitable modification of the analogous definition from the private-key setting (Definition 5.1). Given a public-key encryption scheme $\Pi$ and an adversary $\mathcal{A}$, consider the following experiment:

选择密文攻击下的安全性，是通过对私钥情形中的类似定义（定义 5.1）作适当修改来定义的。给定公钥加密方案 $\Pi$ 和敌手 $\mathcal{A}$，考虑如下实验：

**The CCA indistinguishability experiment $\mathsf{PubK}_{\mathcal{A},\Pi}^{\mathsf{cca}}(n)$:**

**CCA 不可区分性实验 $\mathsf{PubK}_{\mathcal{A},\Pi}^{\mathsf{cca}}(n)$：**

1. $\mathsf{Gen}(1^{n})$ is run to obtain keys $(pk, sk)$.

   运行 $\mathsf{Gen}(1^{n})$ 得到密钥 $(pk, sk)$。

2. The adversary $\mathcal{A}$ is given $pk$ and access to a decryption oracle $\mathsf{Dec}_{sk}(\cdot)$. It outputs a pair of messages $m_0, m_1 \in \mathcal{M}_{pk}$ of the same length.

   敌手 $\mathcal{A}$ 获得 $pk$，并可访问解密预言机 $\mathsf{Dec}_{sk}(\cdot)$。它输出一对等长消息 $m_0, m_1 \in \mathcal{M}_{pk}$。

3. A uniform bit $b \in \{0,1\}$ is chosen, and then a ciphertext $c \leftarrow \mathsf{Enc}_{pk}(m_b)$ is computed and given to $\mathcal{A}$.

   均匀选取一个比特 $b \in \{0,1\}$，然后计算密文 $c \leftarrow \mathsf{Enc}_{pk}(m_b)$ 并交给 $\mathcal{A}$。

4. $\mathcal{A}$ continues to interact with the decryption oracle, but may not request a decryption of $c$ itself. Finally, $\mathcal{A}$ outputs a bit $b'$.

   $\mathcal{A}$ 继续与解密预言机交互，但不得请求解密 $c$ 本身。最后，$\mathcal{A}$ 输出一个比特 $b'$。

5. The output of the experiment is defined to be 1 if $b^{\prime} = b$, and 0 otherwise.

   若 $b^{\prime} = b$，则实验输出定义为 1；否则为 0。

DEFINITION 12.8 A public-key encryption scheme $\Pi = (\mathsf{Gen}, \mathsf{Enc}, \mathsf{Dec})$ has indistinguishable encryptions under a chosen-ciphertext attack (or is CCA-secure) if for all probabilistic polynomial-time adversaries $\mathcal{A}$ there exists a negligible function negl such that

定义 12.8　称公钥加密方案 $\Pi = (\mathsf{Gen}, \mathsf{Enc}, \mathsf{Dec})$ 在选择密文攻击下具有不可区分的加密（或者说是选择密文安全的），如果对所有概率多项式时间敌手 $\mathcal{A}$，都存在可忽略函数 $\mathsf{negl}$ 使得

$$
\Pr[\mathsf{PubK}_{\mathcal{A},\Pi}^{\mathsf{cca}}(n)=1]\leq\frac{1}{2}+\mathsf{negl}(n).
$$

The natural analogue of Theorem 12.6 holds for CCA-security as well. That is, if a scheme has indistinguishable encryptions under a chosen-ciphertext attack then it has indistinguishable multiple encryptions under a chosen-ciphertext attack (defined appropriately). Interestingly, however, the analogue of Claim 12.7 does not hold for CCA-security.

定理 12.6 在选择密文安全性下也有自然的类似结论。也就是说，若一个方案在选择密文攻击下具有不可区分的加密，则它在选择密文攻击下具有不可区分的多重加密（需适当定义）。然而有趣的是，断言 12.7 的类似结论对选择密文安全性并不成立。

As in Definition 5.1, we must prevent the attacker from submitting the challenge ciphertext $c$ to the decryption oracle in order for the definition to be achievable. But this restriction does not make the definition meaningless and, in particular, for each of the three motivating scenarios given earlier one can argue that setting $c^{\prime} = c$ is of no benefit to the attacker:

与定义 5.1 一样，为使定义可以达到，我们必须阻止攻击者向解密预言机提交挑战密文 $c$。但这一限制并不会使定义失去意义；特别地，对于前面给出的三个动机场景中的每一个，都可以论证取 $c^{\prime} = c$ 对攻击者没有好处：

- In the first scenario involving password-based login, the attacker learns nothing about $\mathcal{S}$'s password by replaying $c$ since in this case it already knows that the error message "timestamp incorrect" will be returned.

- 在第一个基于口令登录的场景中，攻击者通过重放 $c$ 得不到关于 $\mathcal{S}$ 口令的任何信息，因为此时它已经知道会返回错误消息“timestamp incorrect”。

- In the second scenario involving encrypted email, sending $c^{\prime} = c$ to the receiver would likely make the receiver suspicious and so it would refuse to respond at all.

- 在第二个加密电子邮件的场景中，把 $c^{\prime} = c$ 发给接收方很可能引起接收方的怀疑，从而根本不予回应。

- In the final scenario involving an auction, $\mathcal{R}$ could easily detect cheating if the adversary's encrypted bid is identical to the other party's encrypted bid. Even if $\mathcal{R}$ ignores such cheating, all the attacker achieves by replaying $c$ is to submit the same bid as the honest party.

- 在最后一个拍卖场景中，如果敌手的加密出价与另一方的加密出价完全相同，$\mathcal{R}$ 可以轻易发现作弊。即使 $\mathcal{R}$ 无视这种作弊，攻击者通过重放 $c$ 所达到的效果，也不过是提交与诚实方相同的出价。

An analogue of authenticated encryption? In the setting of private-key encryption, we introduced the notion of authenticated encryption (cf. Section 5.2) and noted that it was even stronger than CCA-security. This notion cannot be translated directly to the context of public-key encryption, where a single public key is used by many senders to communicate to one receiver (in contrast to the private-key case where a given key is used by only two parties to communicate). Nevertheless, an analogue of authenticated encryption can be considered in the public-key setting; see Section 13.8.

**认证加密的类似概念？**
在私钥加密的情形中，我们引入了认证加密的概念（参见 5.2 节），并指出它比选择密文安全性更强。这一概念无法直接平移到公钥加密的语境中：在公钥加密中，单个公钥被多个发送方用来与一个接收方通信（这与私钥情形不同，那里一个给定密钥只由两方用于通信）。尽管如此，在公钥情形中仍可以考虑认证加密的类似概念；见 13.8 节。
