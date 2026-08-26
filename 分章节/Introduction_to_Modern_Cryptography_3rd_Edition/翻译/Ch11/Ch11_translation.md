# Chapter 11: Key Management and the Public-Key Revolution　第 11 章　密钥管理与公钥革命

## 11.1 Key Distribution and Key Management　密钥分发与密钥管理

In previous chapters we have seen how private-key cryptography can be used to ensure secrecy and integrity for two parties communicating over an insecure channel, if we are willing to assume those two parties hold a shared, secret key. The question we have deferred since Chapter 1, however, is:

在前几章中我们已经看到，如果我们愿意假设通信双方持有一个共享的秘密密钥，私钥密码学便可以用来为通过不安全信道通信的两方保证机密性与完整性。然而，自第 1 章起我们一直搁置的问题是：

How can the parties share a secret key in the first place?

通信双方究竟如何才能共享一个秘密密钥？

Clearly, the key cannot simply be sent over the insecure communication channel because an eavesdropping adversary would then be able to observe the key and it would no longer be secret. Some other mechanism must be used.

显然，密钥不能直接通过不安全的通信信道发送，否则窃听的敌手就能观察到该密钥，它也就不再是秘密了。因此必须采用某种其他的机制。

In some situations, the parties may have access to a secure channel that they can use to reliably share a secret key. One common example is when the two parties are physically co-located at some point in time, during which they can share a key. Alternatively, the parties might be able to use a trusted courier service as a secure channel. We stress that even if the parties have access to a secure channel at some point, this does not make private-key cryptography useless: in the first example, the parties have a secure channel at one point in time but not later; in the second example, utilizing the secure channel might be slower and more costly than communicating over an insecure channel.

在某些情形下，通信双方可能拥有可用于可靠共享秘密密钥的安全信道。一个常见的例子是两方在某段时间身处同一地点，此时他们可以共享一个密钥；另一种可能是双方利用可信的信使服务作为安全信道。我们强调，即使通信双方在某些时刻能够使用安全信道，这也并不意味着私钥密码学就毫无用处：在第一个例子中，双方只在某一时刻拥有安全信道，此后便不再有；在第二个例子中，利用安全信道的速度可能较慢、成本也可能高于使用不安全信道进行通信。

The above approaches have been used to share keys in government, diplomatic, and military settings. As an example, the “red phone” connecting Moscow and Washington in the 1960s was encrypted using a one-time pad, with keys shared by couriers who flew from one country to the other carrying briefcases full of print-outs. Such approaches can also be used in corporations, e.g., to set up a shared key between a central database and a new employee on his/her first day of work. (We return to this example in the next section.)

上述方法曾用于政府、外交和军事场合中的密钥共享。例如，20 世纪 60 年代连接莫斯科与华盛顿的“红色电话”就采用一次一密加密，其密钥由信使携带装满打印件的公文包往返于两国之间进行分发。这类方法也可以用于公司，例如在新员工入职第一天，为其与中央数据库之间建立共享密钥。（我们在下一节还会回到这个例子。）

Relying on a secure channel to distribute keys, however, does not work well in many other situations. For example, consider a large, multinational corporation in which every pair of employees might need the ability to communicate securely, with their communication protected from other employees as well. It will be inconvenient, to say the least, for each pair of employees to meet so they can securely share a key; for employees working in different cities, this may even be impossible. Even if the current set of employees could somehow share keys with each other, it would be impractical for them to share keys with new employees who join after this initial sharing is done.

然而，依靠安全信道来分发密钥，在很多其他情况下并不可行。例如，考虑一家大型跨国公司，其中任意两名员工都可能需要相互进行安全通信的能力，而且他们的通信还要对其他员工保密。让每一对员工都会面以安全地共享密钥，至少可以说是极为不便的；对于在不同城市工作的员工而言，这甚至根本无法实现。即使现有员工能以某种方式相互共享密钥，要在初始共享完成之后再与新加入的员工共享密钥，也是不现实的。

Even assuming these $N$ employees are somehow able to securely share keys with each other, another significant drawback is that each employee would have to manage and store $N-1$ secret keys (one for each other employee in the company). In fact, this may significantly under-count the number of keys stored by each user, because employees may also need keys to communicate securely with remote resources such as databases, servers, printers, and so on. The proliferation of so many secret keys is a significant logistical problem. Moreover, all these keys must be stored securely. The more keys there are, the harder it is to protect them, and the higher the chance of some keys being stolen by an attacker. Computer systems are often infected by viruses, worms, and other forms of malicious software that can steal secret keys and send them quietly over the network to an attacker. Thus, storing keys on employees’ personal computers is not always a safe solution.

即使假设这 $N$ 名员工能够以某种方式相互安全地共享密钥，另一个显著的缺点是每位员工都必须管理并存储 $N-1$ 个秘密密钥（对公司里其他每位员工各一个）。事实上，这可能大大低估了每个用户所存储密钥的数量，因为员工可能还需要密钥来与数据库、服务器、打印机等远程资源进行安全通信。如此众多的秘密密钥不断累积，本身就是一个严重的后勤管理问题。此外，所有这些密钥都必须被安全地存储。密钥越多，保护起来就越困难，某些密钥被攻击者窃取的概率也越高。计算机系统常常感染病毒、蠕虫以及其他形式的恶意软件，它们能够窃取秘密密钥，并通过网络悄悄将其发送给攻击者。因此，把密钥存储在员工的个人电脑上并不总是安全的做法。

To be clear, potential compromise of secret keys is always a concern, irrespective of the number of keys each party holds. When only a few keys need to be stored, however, there are good solutions available for dealing with this threat. A typical solution today is to store keys on secure hardware such as a smartcard. A smartcard can carry out cryptographic computations using the stored secret keys, ensuring that these keys never make their way onto users’ personal computers. If designed properly, the smartcard can be much more resilient to attack than a personal computer—for example, it typically cannot be infected by malware—and so offers a good means of protecting users’ secret keys. Unfortunately, smartcards are typically quite limited in memory, and so cannot store hundreds (or thousands) of keys; they may also be somewhat expensive and difficult to replace if lost.

需要说明的是，无论各方持有多少密钥，秘密密钥潜在泄露始终是一个隐忧。不过，当只需存储少量密钥时，已有应对这一威胁的良好方案。如今一种典型的做法是将密钥存储在智能卡等安全硬件中。智能卡可以利用存储的秘密密钥执行密码学计算，从而确保这些密钥绝不会进入用户的个人电脑。如果设计得当，智能卡抵御攻击的能力远强于个人电脑——例如它通常不会被恶意软件感染——因而是保护用户秘密密钥的良好手段。遗憾的是，智能卡的内存通常非常有限，无法存储成百上千个密钥；而且它的成本也较高，一旦丢失也不易补办。

The concerns outlined above can all be addressed—in principle, even if not in practice—in “closed” organizations consisting of a well-defined population of users, all of whom are willing to follow the same policies for distributing and storing keys. They break down, however, in “open systems” where users have transient interactions, cannot arrange a physical meeting, and may not even be aware of each other’s existence until the time they first want to communicate. This is, in fact, a more common situation than one might initially realize: consider sending credit-card information to an Internet merchant from whom you have never previously purchased anything, or sending email to someone whom you have never met in person. In such cases, private-key cryptography alone simply does not provide a solution, and we must look further for adequate solutions.

上述种种顾虑，原则上都可以在由明确定义的用户群体构成的“封闭”组织中得到解决——只要所有用户都愿意遵循相同的密钥分发与存储策略，即便实践中未必尽如人意。然而，在“开放系统”中这些办法就行不通了：用户之间的交互是短暂的，无法安排线下会面，甚至在首次想要通信之前可能都不知道彼此的存在。实际上，这种情况比人们最初意识到的更为常见：想想向一位你从未光顾过的网络商家发送信用卡信息，或者给一个从未谋面的人发电子邮件。在这类情形下，仅靠私钥密码学根本无法提供解决方案，我们必须进一步寻找充分的解决途径。

To summarize, there are at least three distinct problems related to the use of private-key cryptography. The first is that of key distribution, the second is that of storing and managing large numbers of secret keys, and the third is the inapplicability of private-key cryptography to open systems.

总而言之，与私钥密码学的使用相关的难题至少有三个：第一个是密钥分发问题，第二个是大量秘密密钥的存储与管理问题，第三个是私钥密码学不适用于开放系统的问题。

## 11.2 A Partial Solution: Key-Distribution Centers　一种部分解决方案：密钥分发中心

One way to address some of the concerns from the previous section is to use a key-distribution center (KDC) to establish shared keys. Consider again the case of a large corporation where all pairs of employees must be able to communicate securely. In such a setting, we can leverage the fact that all employees may trust some entity—say, the system administrator—at least with respect to the security of work-related information. This trusted entity can then act as a KDC and help all the employees share pairwise keys.

利用密钥分发中心（key-distribution center, KDC）来建立共享密钥，是化解上一节部分顾虑的一条途径。再次考虑那家大型公司的情形：所有员工两两之间都必须能够安全通信。在这种情形下，我们可以利用这样一个事实：所有员工都可能信任某个实体——比如系统管理员——至少在工作信息的安全方面是如此。这个受信任的实体便可以充当 KDC，帮助所有员工共享两两之间的密钥。

When a new employee joins, the KDC can share a key with that employee (in person, in a secure location) as part of that employee’s first day of work. At the same time, the KDC could also distribute shared keys between that employee and all existing employees. That is, when the $i$th employee joins, the KDC could (in addition to sharing a key between itself and this new employee) generate $i-1$ keys $k_1, \ldots, k_{i-1}$, give these keys to the new employee, and then send key $k_j$ to the $j$th existing employee by encrypting it using the key that employee already shares with the KDC. Following this, the new employee shares a key with every other employee (as well as with the KDC).

当新员工加入时，KDC 可以在该员工入职第一天（当面、在安全的地点）与其共享一个密钥。与此同时，KDC 还可以在该员工与所有现有员工之间分发共享密钥。也就是说，当第 $i$ 名员工加入时，KDC 除了在自己与这位新员工之间共享一个密钥之外，还可以生成 $i-1$ 个密钥 $k_1, \ldots, k_{i-1}$，把这些密钥交给新员工，然后利用第 $j$ 名现有员工已与 KDC 共享的密钥对其加密，将密钥 $k_j$ 发送给该员工。经过这一步，新员工便与其他每一位员工（以及 KDC）都共享了密钥。

A better approach, which avoids requiring employees to store and manage multiple keys, is to utilize the KDC in an online fashion to generate keys “on demand” whenever two employees wish to communicate securely. As before, the KDC will share a (different) key with each employee, something that can be done securely on each employee’s first day of work. Say the KDC shares key $k_{A}$ with employee Alice, and $k_{B}$ with employee Bob. At some later time, when Alice wishes to communicate securely with Bob, she can simply send the message ‘I, Alice, want to talk to Bob’ to the KDC. (If desired, this message can be authenticated using the key shared by Alice and the KDC.) The KDC then chooses a new, random key—called a session key—and sends this key $k$ to Alice encrypted using $k_{A}$, and to Bob encrypted using $k_{B}$. (This protocol is too simplistic to be used in practice; see further discussion below.) Once Alice and Bob both recover this session key, they can use it to communicate securely. When they are done with their conversation, they can (and should) erase the session key because they can always contact the KDC again if they wish to communicate at some later time.

一种更好的做法是不要求员工存储和管理多个密钥，而是以在线方式利用 KDC“按需”生成密钥：每当有两名员工希望安全通信时，就现场生成一个。与前面一样，KDC 与每位员工共享一个（不同的）密钥，这件事可以在每位员工入职第一天安全地完成。设 KDC 与员工 Alice 共享密钥 $k_{A}$，与员工 Bob 共享密钥 $k_{B}$。在之后的某个时刻，当 Alice 希望与 Bob 安全通信时，她只需向 KDC 发送消息‘I, Alice, want to talk to Bob’（我是 Alice，我想与 Bob 通信）。（如有需要，可以借助 Alice 与 KDC 共享的密钥对该消息进行认证。）随后，KDC 选取一个新的随机密钥——称为会话密钥——并把该密钥 $k$ 用 $k_{A}$ 加密后发给 Alice，再用 $k_{B}$ 加密后发给 Bob。（这个协议过于简化，不能直接付诸实用；进一步的讨论见下文。）Alice 和 Bob 一旦都恢复出该会话密钥，就可以用它进行安全通信。通信结束后，他们可以（并且应该）擦除这个会话密钥，因为日后若还想通信，随时可以再次联系 KDC。

Consider the advantages of this approach:

我们来考虑这种方法的优势：

1. Each employee needs to store only one long-term secret key (namely, the one they share with the KDC). Employees still need to manage and store session keys, but these are short-term keys that are erased once a communication session concludes.

   每位员工只需存储一个长期秘密密钥（即与 KDC 共享的那一个）。员工仍然需要管理和存储会话密钥，但这些都是短期密钥，一旦通信会话结束就会被擦除。

    The KDC needs to store many long-term keys. However, the KDC can be kept in a secure location and be given the highest possible protection against network attacks.

    KDC 则需要存储许多长期密钥。不过，KDC 可以安置在安全的地点，并获得针对网络攻击的最高级别防护。

2. When an employee joins the organization, all that must be done is to set up a key between this employee and the KDC. No other employees need to update the set of keys they hold.

   当一名员工加入组织时，需要做的只是在该员工与 KDC 之间建立一个密钥，其他任何员工都无需更新自己所持有的密钥集合。

Thus, KDCs can alleviate two of the problems we have seen with regard to private-key cryptography: they can simplify key distribution (since only one new key must be shared when an employee joins, and it is reasonable to assume a secure channel between the KDC and that employee on their first day of work), and can reduce the complexity of key storage (since each employee only needs to store a single key). KDCs go a long way toward making private-key cryptography practical in large organizations where there is a single entity who is trusted by everyone.

因此，KDC 能够缓解我们在私钥密码学中看到的两个问题：它们可以简化密钥分发（因为员工入职时只需共享一个新密钥，而且假定入职第一天 KDC 与该员工之间存在安全信道是合理的），还能降低密钥存储的复杂性（因为每位员工只需存储一个密钥）。在存在一个人人信任的单一实体的大型组织中，KDC 为使私钥密码学切实可行发挥了很大作用。

There are, however, some drawbacks to relying on KDCs:

然而，依赖 KDC 也存在一些缺点：

1. A successful attack on the KDC will result in a complete break of the system: an attacker can compromise all keys and subsequently eavesdrop on all network traffic. This makes the KDC a high-value target. Note that even if the KDC is well-protected against external attacks, there is always the possibility of an insider attack by an employee who has access to the KDC (for example, the IT manager).

   针对 KDC 的成功攻击将导致系统被完全攻破：攻击者可以获取全部密钥，进而窃听所有网络流量。这使得 KDC 成为高价值目标。注意，即使 KDC 对外部攻击防护严密，拥有 KDC 访问权限的员工（例如 IT 经理）发起内部攻击的可能性也始终存在。

2. The KDC is a single point of failure: if the KDC is down, secure communication is temporarily impossible. If employees are constantly contacting the KDC and asking for session keys to be established, the load on the KDC can be very high, thereby increasing the chances that it may fail or be slow to respond.

   KDC 是单一故障点：一旦 KDC 宕机，安全通信就会暂时无法进行。如果员工们不断地联系 KDC 请求建立会话密钥，KDC 的负载可能会非常高，从而增加其发生故障或响应迟缓的可能性。

A simple solution to the second problem is to replicate the KDC. This works (and is done in practice), but also means that there are now more points of attack on the system. Adding more KDCs also makes it more difficult to add new employees, since updates must be securely propagated to every KDC.

解决第二个问题的一个简单办法是复制 KDC。这种做法行之有效（实践中也确实如此），但同时也意味着系统中出现了更多的攻击点。增加更多 KDC 还会让新员工的加入变得更麻烦，因为更新必须被安全地传播到每一个 KDC。

Protocols for key distribution using a KDC. There are a number of protocols in the literature for secure key distribution using a KDC. We mention in particular the Needham–Schroeder protocol, which forms the core of Kerberos, an important and widely used service for performing authentication and supporting secure communication. (Kerberos is used in many universities and corporations, and is the default mechanism for supporting secure networked authentication and communication in Windows and many UNIX systems.) We only highlight one feature of this protocol. When Alice contacts the KDC and asks to communicate with Bob, the KDC does not send the encrypted session key to both Alice and Bob as we have described earlier. Instead, the KDC sends to Alice the session key encrypted under Alice’s key in addition to the session key encrypted under Bob’s key. Alice then forwards the second ciphertext to Bob as in Figure 11.1. The second ciphertext is sometimes called a ticket, and can be viewed as a credential that allows Alice to talk to Bob (and allows Bob to be assured that he is talking to Alice). Indeed, although we have not stressed this point in our discussion, a KDC-based approach can provide a useful means of performing authentication as well. Note also that Alice and Bob need not both be users; Alice might be a user and Bob a resource such as a remote server, a database, or a printer.

**基于 KDC 的密钥分发协议。**

文献中有许多利用 KDC 进行安全密钥分发的协议。我们特别提及 Needham–Schroeder 协议，它构成了 Kerberos 的核心；Kerberos 是一项重要且被广泛使用的服务，用于执行认证并支持安全通信。（Kerberos 被许多大学和公司采用，并且在 Windows 以及许多 UNIX 系统中都是支持安全网络认证与通信的默认机制。）这里我们只强调该协议的一个特点：当 Alice 联系 KDC 请求与 Bob 通信时，KDC 并不像我们前面描述的那样把加密后的会话密钥分别发送给 Alice 和 Bob，而是把用 Alice 的密钥加密的会话密钥连同用 Bob 的密钥加密的会话密钥一起发送给 Alice。随后，如图 11.1 所示，Alice 把第二个密文转发给 Bob。第二个密文有时被称为票据（ticket），可以看作允许 Alice 与 Bob 交谈的一种凭证（同时也让 Bob 能够确信自己正在与 Alice 交谈）。事实上，尽管我们在讨论中没有强调这一点，基于 KDC 的方法同样可以提供一种有用的认证手段。另请注意，Alice 和 Bob 不必都是用户：Alice 可以是用户，而 Bob 可以是远程服务器、数据库或打印机之类的资源。

![Image](https://lsky.jerryxue.top/i/2026/08/25/6a8d6a63ee094.jpg)

**FIGURE 11.1: A general template for key-distribution protocols. / 图 11.1：密钥分发协议的一般模板。**

The protocol was designed in this way to reduce the load on the KDC. In the protocol as described, the KDC does not need to initiate a second connection to Bob, and need not worry whether Bob is on-line when Alice initiates the protocol. Moreover, if Alice retains the ticket (and her copy of the session key), then she can re-initiate secure communication with Bob by simply re-sending the ticket to Bob, without the involvement of the KDC at all. (In practice, tickets expire and eventually need to be renewed. But a session could be re-established within some acceptable time period.)

该协议之所以这样设计，是为了减轻 KDC 的负载。在上面描述的协议中，KDC 无需再发起与 Bob 的第二条连接，也无需担心 Alice 发起协议时 Bob 是否在线。此外，如果 Alice 保留了票据（以及她那份会话密钥），那么她只需把票据重新发送给 Bob，就能重新与 Bob 建立安全通信，完全无需 KDC 参与。（实践中，票据会过期并最终需要更新，但在某段可接受的时间范围内，会话是可以重新建立的。）

We conclude by noting that in practice the key that Alice shares with the KDC might be a short, easy-to-memorize password. In this case, many additional security problems arise that must be dealt with. We have also been implicitly assuming an attacker who only passively eavesdrops, rather than one who might actively try to interfere with the protocol. We refer the interested reader to the references at the end of this chapter for more information about how such issues can be addressed.

最后我们指出，实践中 Alice 与 KDC 共享的密钥可能是一个简短易记的口令。在这种情况下会出现许多额外的安全问题，必须加以处理。此外，我们一直隐含地假设攻击者只进行被动窃听，而不会主动干扰协议。关于如何应对此类问题，有兴趣的读者可参阅本章末尾的参考文献。

## 11.3 Key Exchange and the Diffie–Hellman Protocol　密钥交换与 Diffie–Hellman 协议

KDCs and protocols like Kerberos are used in practice. But these approaches to the key-distribution problem still require, at some point, a private and authenticated channel that can be used to share keys. (In particular, we assumed the existence of such a channel between the KDC and an employee on his or her first day.) Thus, they still cannot solve the problem of key distribution in open systems like the Internet, where there may be no private channel available between two users who wish to communicate.

KDC 以及类似 Kerberos 的协议在实际中得到应用。但这些解决密钥分发问题的方法在某个环节上仍然需要一个私密且经认证的信道来共享密钥。（具体而言，我们假定了在员工入职第一天，KDC 与该员工之间存在这样的信道。）因此，它们仍然无法解决互联网这类开放系统中的密钥分发问题——在那里，希望通信的两个用户之间可能根本没有可用的私密信道。

To achieve private communication without ever communicating over a private channel, a radically different approach is needed. In 1976, Whitfield Diffie and Martin Hellman published a paper with the innocent-looking title “New Directions in Cryptography.” In that work they observed that there is often asymmetry in the world; in particular, there are certain actions that can be easily performed but not easily reversed. For example, padlocks can be locked without a key (i.e., easily), but cannot be reopened. More strikingly, it is easy to shatter a glass vase but extremely difficult to put it back together.

要在全程不经由私密信道通信的情况下实现私密通信，就需要一种截然不同的方法。1976 年，Whitfield Diffie 和 Martin Hellman 发表了一篇标题看似平淡的论文《密码学的新方向》。他们在文中观察到，世界上常常存在不对称性；特别地，有些动作很容易完成，却不易逆转。例如，挂锁不用钥匙就能锁上（也就是说很容易），但却无法重新打开。更引人注目的是，打碎一个玻璃花瓶轻而易举，而把它复原却极其困难。

Algorithmically (and more relevant for our purposes), it is easy to multiply two large primes but difficult to recover those primes from their product. (This is exactly the factoring problem discussed in previous chapters.) Diffie and Hellman realized that such phenomena could be used to derive interactive protocols for secure key exchange that allow two parties to share a secret key, via communication over a public channel, by having the parties perform operations that an eavesdropper cannot reverse.

从算法的角度看（这也与我们的目的更为相关），两个大素数相乘很容易，但从乘积恢复出这两个素数却很困难。（这正是前几章讨论过的因子分解问题。）Diffie 和 Hellman 意识到，可以让通信双方执行窃听者无法逆转的运算，从而利用这类现象设计出安全密钥交换的交互式协议，使两方能够通过公共信道上的通信共享一个秘密密钥。

The existence of secure key-exchange protocols is quite amazing. It means that you and a friend could agree on a secret by simply shouting across a room (and performing some local computation); the secret would be unknown to anyone else, even if they had listened to everything that was said. Indeed, until 1976 it was generally believed that secure communication could not be done without first sharing some secret information using a private channel.

安全密钥交换协议的存在性着实令人惊叹。这意味着你和一位朋友只需隔着房间互相喊话（再做一点本地计算），就能约定一个秘密；这个秘密其他任何人都无从知晓，哪怕他们听到了所说的一切。事实上，直到 1976 年，人们还普遍认为，如果不先通过私密信道共享某些秘密信息，就不可能实现安全通信。

The influence of Diffie and Hellman’s paper was enormous. In addition to introducing a fundamentally new way of looking at cryptography, it was one of the first steps toward moving cryptography out of the private domain and into the public one. We quote the first two paragraphs of their paper:

Diffie 和 Hellman 论文的影响是巨大的。它不仅引入了一种看待密码学的全新方式，而且是使密码学走出私密领域、走向公开领域的最早几步之一。我们引用他们论文的前两段：

We stand today on the brink of a revolution in cryptography. The development of cheap digital hardware has freed it from the design limitations of mechanical computing and brought the cost of high-grade cryptographic devices down to where they can be used in such commercial applications as remote cash dispensers and computer terminals.

今天，我们正站在密码学一场革命的边缘。廉价数字硬件的发展使密码学摆脱了机械计算的设计局限，把高等级密码装置的成本降到诸如远程取款机和计算机终端之类的商业应用所能承受的水平。

In turn, such applications create a need for new types of cryptographic systems which minimize the necessity of secure key distribution channels. ...At the same time, theoretical developments in information theory and computer science show promise of providing provably secure cryptosystems, changing this ancient art into a science.

反过来，这类应用又催生了对新型密码系统的需求——这类系统应尽量减少对安全密钥分发通道的依赖。……与此同时，信息论与计算机科学的理论进展有望提供可证明安全的密码体制，把这门古老的艺术转变为一门科学。

Diffie and Hellman were not exaggerating, and the revolution they spoke of was due in great part to their work.

Diffie 和 Hellman 并没有言过其实，而他们所说的那场革命在很大程度上正是归功于他们自己的工作。

In this section we present the Diffie–Hellman key-exchange protocol. We prove its security against eavesdropping adversaries or, equivalently, under the assumption that the parties communicate over a public but authenticated channel (so an attacker cannot interfere with their communication). Security against an eavesdropping adversary is a relatively weak guarantee, and in practice key-exchange protocols must satisfy stronger notions of security that are beyond our present scope. (Moreover, we are interested here in the setting where the communicating parties have no prior shared information, in which case there is nothing that can be done to prevent an adversary from impersonating one of the parties. We return to this point later.)

本节介绍 Diffie–Hellman 密钥交换协议。我们将证明它抵抗窃听敌手的安全性，或者等价地说，在通信双方通过公共但经认证的信道进行通信这一假设下（因而攻击者无法干扰他们的通信）证明其安全性。但仅抵抗窃听敌手只是一个相对较弱的安全保证，实际使用的密钥交换协议必须满足更强的安全概念，而这超出了我们当前的讨论范围。（此外，我们这里关心的是通信双方没有任何先验共享信息的设定；在这种情况下，无论如何都无法防止敌手假冒其中一方。这一点我们稍后再谈。）

The setting and definition of security. We consider a setting with two parties—traditionally called Alice and Bob—who run a probabilistic protocol $\Pi$ in order to generate a shared, secret key; $\Pi$ can be viewed as the set of instructions for Alice and Bob in the protocol. Alice and Bob begin by holding the security parameter ${1}^n$; they then run $\Pi$ using (independent) random bits. At the end of the protocol, Alice and Bob output keys $k_A, k_B \in \{0,1\}^n$, respectively. The basic correctness requirement is that $k_A = k_B$. Since we will only deal with protocols that satisfy this requirement, we will speak simply of the key $k = k_A = k_B$ generated in some honest execution of $\Pi$. (Since $\Pi$ is randomized the key will, in general, be different every time $\Pi$ is run.)

**设定的描述与安全性的定义。**

我们考虑包含两方——按惯例称为 Alice 和 Bob——的设定，他们运行一个概率协议 $\Pi$ 来生成共享的秘密密钥；$\Pi$ 可以看作协议中给 Alice 和 Bob 的一组指令。Alice 和 Bob 起初持有安全参数 ${1}^n$，然后使用（相互独立的）随机比特运行 $\Pi$。协议结束时，Alice 和 Bob 分别输出密钥 $k_A, k_B \in \{0,1\}^n$。基本的正确性要求是 $k_A = k_B$。由于我们只讨论满足这一要求的协议，下面就直接称 $\Pi$ 的某次诚实执行所生成的密钥为 $k = k_A = k_B$。（由于 $\Pi$ 是随机化的，每次运行 $\Pi$ 得到的密钥一般来说都不相同。）

We now turn to defining security. Intuitively, a key-exchange protocol is secure if the key output by Alice and Bob is completely hidden from an eavesdropping adversary. This is formally defined by requiring that an adversary who has eavesdropped on an execution of the protocol should be unable to distinguish the key k generated by that execution (and now shared by Alice and Bob) from a uniform key of length n. This is much stronger than simply requiring that the adversary be unable to guess k exactly, and this stronger notion is necessary if the parties will subsequently use k for some cryptographic application (e.g., as a key for a private-key encryption scheme).

现在我们转向安全性的定义。直观地说，如果一个密钥交换协议所输出的密钥在窃听敌手面前是完全隐藏的，那么该协议就是安全的。形式化地说，就是要求窃听了协议一次执行的敌手，无法区分该次执行所生成（且现已由 Alice 和 Bob 共享）的密钥 k 与长度为 n 的均匀密钥。这比仅仅要求敌手无法精确猜出 k 要强得多；而如果双方随后要将 k 用于某个密码学应用（例如作为私钥加密方案的密钥），这个更强的概念就是必要的。

Formalizing the above, let $\Pi$ be a key-exchange protocol, $\mathcal{A}$ an adversary, and $n$ the security parameter. We have the following experiment:

将上述想法形式化：设 $\Pi$ 是一个密钥交换协议，$\mathcal{A}$ 是敌手，$n$ 是安全参数。我们有如下实验：

The key-exchange experiment $\mathsf{KE}_{\mathcal{A},\Pi}^{\mathsf{eav}}(n)$:

密钥交换实验 $\mathsf{KE}_{\mathcal{A},\Pi}^{\mathsf{eav}}(n)$：

1. Two parties holding ${1}^{n}$ execute protocol $\Pi$. This results in a transcript trans containing all the messages sent by the parties, and a key $k$ output by each of the parties.

   持有 ${1}^{n}$ 的两方执行协议 $\Pi$。其结果是一份包含双方所发全部消息的交互记录 trans，以及各方各自输出的密钥 $k$。

2. A uniform bit $b \in \{0,1\}$ is chosen. If $b = 0$ set $\hat{k} := k$, and if $b = 1$ then choose uniform $\hat{k} \in \{0,1\}^n$.

   均匀选取比特 $b \in \{0,1\}$。若 $b = 0$，则置 $\hat{k} := k$；若 $b = 1$，则均匀选取 $\hat{k} \in \{0,1\}^n$。

3. $\mathcal{A}$ is given trans and $\hat{k}$, and outputs a bit $b'$.

   将 trans 和 $\hat{k}$ 交给 $\mathcal{A}$，$\mathcal{A}$ 输出一个比特 $b'$。

4. The output of the experiment is defined to be 1 if $b^{\prime} = b$, and 0 otherwise. (In case $\mathsf{KE}_{\mathcal{A},\Pi}^{\mathsf{eav}}(n) = 1$, we say that $\mathcal{A}$ succeeds.)

   若 $b^{\prime} = b$，则实验的输出定义为 1，否则为 0。（当 $\mathsf{KE}_{\mathcal{A},\Pi}^{\mathsf{eav}}(n) = 1$ 时，我们称 $\mathcal{A}$ 成功。）

$\mathcal{A}$ is given trans to capture the fact that $\mathcal{A}$ eavesdrops on the entire execution of the protocol and thus sees all messages exchanged by the parties. In the real world, $\mathcal{A}$ would not be given any key; in the experiment the adversary is given $\hat{k}$ only as a means of defining what it means for $\mathcal{A}$ to “break” the security of $\Pi$. That is, the adversary succeeds in “breaking” $\Pi$ if it can correctly determine whether the key $\hat{k}$ is the real key corresponding to the given execution of the protocol, or whether $\hat{k}$ is a uniform key that is independent of the transcript.

之所以把 trans 交给 $\mathcal{A}$，是为了刻画 $\mathcal{A}$ 窃听协议整个执行过程、因而能看到双方交换的所有消息这一事实。在现实世界中，$\mathcal{A}$ 不会得到任何密钥；在实验中把 $\hat{k}$ 交给敌手，只是作为一种手段，用来定义 $\mathcal{A}$“攻破”$\Pi$ 的安全性意味着什么。也就是说，如果敌手能够正确判断 $\hat{k}$ 是对应于给定协议执行的真实密钥，还是与交互记录无关的均匀密钥，那么它就成功地“攻破”了 $\Pi$。

As expected, we say $\Pi$ is secure if the adversary succeeds with probability that is at most negligibly greater than 1/2. That is:

正如所期待的那样，如果敌手成功的概率至多比 1/2 大出一个可忽略的量，我们就说 $\Pi$ 是安全的。即：

DEFINITION 11.1 A key-exchange protocol $\Pi$ is secure in the presence of an eavesdropper if for all probabilistic polynomial-time adversaries $\mathcal{A}$ there is a negligible function $\mathsf{negl}$ such that

定义 11.1　若对于所有的概率多项式时间敌手 $\mathcal{A}$，都存在一个可忽略函数 $\mathsf{negl}$ 使得

$$\Pr\left[\mathsf{KE}_{\mathcal{A},\Pi}^{\mathsf{eav}}(n)=1\right]\leq\frac{1}{2}+\mathsf{negl}(n).$$

则称密钥交换协议 $\Pi$ 在窃听者存在的情况下是安全的。

The aim of a key-exchange protocol is almost always to generate a shared key $k$ that will be used by the parties for some further cryptographic purpose, e.g., to encrypt and authenticate their subsequent communication using, say, an authenticated encryption scheme. Intuitively, using a shared key generated by a secure key-exchange protocol should be “as good as” using a key shared over a private channel. It is possible to prove this formally; see Exercise 11.1.

密钥交换协议的目标几乎总是生成一个共享密钥 $k$，供双方用于后续的密码学目的，例如使用经认证的加密方案来加密和认证随后的通信。直观地说，使用由安全密钥交换协议生成的共享密钥，应当与使用经由私密信道共享的密钥“一样好”。这一点可以形式化地证明；参见习题 11.1。

The Diffie–Hellman key-exchange protocol. We now describe the key-exchange protocol that appeared in the original paper by Diffie and Hellman (although they were less formal than we will be here). Let $\mathcal{G}$ be a probabilistic polynomial-time algorithm that, on input ${1}^n$, outputs a description of a cyclic group $\mathbb{G}$, its order $q$ (with $\|q\| = n$), and a generator $g \in \mathbb{G}$. (See Section 9.3.2.) The Diffie–Hellman key-exchange protocol is described formally as Construction 11.2 and illustrated in Figure 11.2.

**Diffie–Hellman 密钥交换协议。**

现在我们描述 Diffie 和 Hellman 原始论文中给出的密钥交换协议（当然，他们不如我们在这里这样形式化）。设 $\mathcal{G}$ 是一个概率多项式时间算法，输入 ${1}^n$ 时输出一个循环群 $\mathbb{G}$ 的描述、它的阶 $q$（满足 $\|q\| = n$）以及一个生成元 $g \in \mathbb{G}$。（参见 9.3.2 节。）Diffie–Hellman 密钥交换协议的形式化描述见构造 11.2，图示见图 11.2。

**CONSTRUCTION 11.2**

**构造 11.2**

• Common input: The security parameter ${1}^{n}$

• 公共输入：安全参数 ${1}^{n}$

• The protocol:

• 协议：

1. Alice runs $\mathcal{G}({1}^{n})$ to obtain $(\mathbb{G}, q, g)$.

   Alice 运行 $\mathcal{G}({1}^{n})$，得到 $(\mathbb{G}, q, g)$。

2. Alice chooses a uniform $x \in \mathbb{Z}_q$, and computes $h_A := g^x$.

   Alice 均匀选取 $x \in \mathbb{Z}_q$，并计算 $h_A := g^x$。

3. Alice sends $(\mathbb{G}, q, g, h_A)$ to Bob.

   Alice 将 $(\mathbb{G}, q, g, h_A)$ 发送给 Bob。

4. Bob receives $(\mathbb{G}, q, g, h_A)$. He chooses a uniform $y \in \mathbb{Z}_q$, and computes $h_B := g^y$. Bob sends $h_B$ to Alice and outputs the key $k_B := h_A^y$.

   Bob 接收 $(\mathbb{G}, q, g, h_A)$。他均匀选取 $y \in \mathbb{Z}_q$，并计算 $h_B := g^y$。Bob 将 $h_B$ 发送给 Alice，并输出密钥 $k_B := h_A^y$。

5. Alice receives $h_{B}$ and outputs the key $k_{A} := h_{B}^{x}$.

   Alice 接收 $h_{B}$，并输出密钥 $k_{A} := h_{B}^{x}$。

![Image](https://lsky.jerryxue.top/i/2026/08/25/6a8d6a67d2222.jpg)

**FIGURE 11.2: The Diffie–Hellman key-exchange protocol. / 图 11.2：Diffie–Hellman 密钥交换协议。**

In our description, we have assumed that Alice generates $(\mathbb{G}, q, g)$ and sends these parameters to Bob as part of her first message. In practice, these parameters are standardized and known to both parties before the protocol begins. In that case Alice need only send $h_A$, and Bob need not wait to receive Alice’s message before computing and sending $h_B$.

在上面的描述中，我们假设由 Alice 生成 $(\mathbb{G}, q, g)$，并在她的第一条消息中把这些参数发送给 Bob。实践中，这些参数是标准化的，协议开始之前双方就已知晓。此时 Alice 只需发送 $h_A$，而 Bob 也无需等到收到 Alice 的消息之后才计算并发送 $h_B$。

It is not hard to see that the protocol is correct: Bob computes the key

不难看出该协议是正确的：Bob 计算出的密钥为

$$k_{B}=h_{A}^{y}=(g^{x})^{y}=g^{xy}$$

and Alice computes the key

而 Alice 计算出的密钥为

$$k_{A}=h_{B}^{x}=(g^{y})^{x}=g^{xy},$$

and so $k_{A} = k_{B}$. (The observant reader will note that the shared key is a group element, not a bit-string. We will return to this point later.)

因此 $k_{A} = k_{B}$。（细心的读者会注意到，共享的密钥是一个群元素而不是比特串。我们稍后会回到这一点。）

Diffie and Hellman did not prove security of their protocol; indeed, the appropriate notions (both the definitional framework as well as the idea of formulating precise assumptions) were not yet in place. Let us see what sort of assumption will be needed in order for the protocol to be secure. A first observation, made by Diffie and Hellman, is that a minimal requirement for security here is that the discrete-logarithm problem be hard relative to $\mathcal{G}$. If not, then an adversary given the transcript (which, in particular, includes $h_A$) can compute the secret value of one of the parties (i.e., $x$) and then easily compute the shared key using that value. So, hardness of the discrete-logarithm problem is necessary for the protocol to be secure. It is not, however, sufficient, as it is possible that there are other ways of computing the key $k_A = k_B$ without explicitly computing $x$ or $y$. The computational Diffie–Hellman assumption—which would only guarantee that the key $g^{xy}$ is hard to compute in its entirety from the transcript—does not suffice either.

Diffie 和 Hellman 并未证明其协议的安全性；事实上，当时相应的概念（无论是定义框架，还是精确表述假设的思想）都尚未确立。我们来看看要使该协议安全需要什么样的假设。Diffie 和 Hellman 给出的第一个观察是：此处安全性的一个最低要求是离散对数问题相对于 $\mathcal{G}$ 是困难的。若非如此，那么敌手拿到交互记录（其中特别包含 $h_A$）后就能计算出某一方的秘密值（即 $x$），进而利用该值轻松算出共享密钥。所以，离散对数问题的困难性是该协议安全的必要条件。但这并不充分，因为完全可能存在其他计算密钥 $k_A = k_B$ 的途径，而无须显式算出 $x$ 或 $y$。计算性 Diffie–Hellman 假设——它只保证从交互记录出发难以完整计算出密钥 $g^{xy}$——同样是不够的。

What is required by Definition 11.1 is that the shared key $g^{xy}$ should be indistinguishable from uniform for any adversary given $g$, $g^x$, and $g^y$. This is exactly the decisional Diffie–Hellman assumption introduced in Section 9.3.2.

定义 11.1 所要求的是：对于给定 $g$、$g^x$ 和 $g^y$ 的任何敌手，共享密钥 $g^{xy}$ 都应当与均匀分布不可区分。这正是 9.3.2 节引入的判定性 Diffie–Hellman 假设。

As we will see, a proof of security for the protocol follows almost immediately from the decisional Diffie–Hellman assumption. This should not be surprising, as the Diffie–Hellman assumptions were introduced—well after Diffie and Hellman published their paper—as a way of abstracting the properties underlying the (conjectured) security of the Diffie–Hellman protocol. Given this, it is fair to ask whether anything is gained by defining and proving security here. By this point in the book, hopefully you are convinced the answer is yes. Precisely defining security for key-exchange protocols forces us to think about exactly what security properties we want; specifying a precise assumption (namely, the decisional Diffie–Hellman assumption) means we can study that assumption independently of any particular application and—once we are convinced of its plausibility—construct other protocols based on it; finally, proving security shows that the assumption does, indeed, suffice for the protocol to meet our desired notion of security.

正如我们将要看到的，该协议的安全性证明几乎可以由判定性 Diffie–Hellman 假设直接推出。这不足为奇，因为 Diffie–Hellman 假设正是在 Diffie 和 Hellman 发表论文很久之后才被提出的，其目的就是抽象出 Diffie–Hellman 协议（猜想上的）安全性背后的性质。鉴于此，自然会有人问：在这里定义并证明安全性究竟能带来什么？读到本书此处，希望你已相信答案是肯定的。为密钥交换协议精确定义安全性，迫使我们认真思考自己到底想要什么样的安全性质；明确表述一个精确的假设（即判定性 Diffie–Hellman 假设），意味着我们可以独立于任何具体应用来研究这一假设，并且——一旦确信其合理性——就能以它为基础构造其他协议；最后，安全性证明表明该假设确实足以让协议达到我们所期望的安全概念。

In our proof of security, we use a modified version of Definition 11.1 in which it is required that the shared key be indistinguishable from a uniform element of $\mathbb{G}$ rather than from a uniform $n$-bit string. This discrepancy will need to be addressed before the protocol can be used in practice—after all, group elements are not typically useful as cryptographic keys, and the representation of a uniform group element will not, in general, be a uniform bit-string—and we briefly discuss one standard way to do so following the proof. For now, we let $\widehat{\mathsf{KE}}_{\mathcal{A},\Pi}^{\mathsf{eav}}(n)$ denote a modified experiment where if $b=1$ then $\hat{k}$ is chosen uniformly from $\mathbb{G}$ rather than uniformly from $\{0,1\}^n$.

在安全性证明中，我们使用定义 11.1 的一个修改版本，其中要求共享密钥与 $\mathbb{G}$ 中的均匀元素不可区分，而不是与均匀的 n 比特串不可区分。这一差异必须在协议付诸实用之前加以解决——毕竟，群元素通常不适合直接用作密码学密钥，而且均匀群元素的表示一般也不是均匀比特串——证明之后我们会简要讨论解决这一问题的一种标准做法。目前，我们用 $\widehat{\mathsf{KE}}_{\mathcal{A},\Pi}^{\mathsf{eav}}(n)$ 表示修改后的实验：其中当 $b=1$ 时，$\hat{k}$ 从 $\mathbb{G}$ 中均匀选取，而非从 $\{0,1\}^n$ 中均匀选取。

THEOREM 11.3 If the decisional Diffie–Hellman problem is hard relative to $\mathcal{G}$, then the Diffie–Hellman key-exchange protocol $\Pi$ is secure in the presence of an eavesdropper (with respect to the modified experiment $\widehat{\mathsf{KE}}_{\mathcal{A},\Pi}^{\mathsf{eav}}$).

定理 11.3　若判定性 Diffie–Hellman 问题相对于 $\mathcal{G}$ 是困难的，则 Diffie–Hellman 密钥交换协议 $\Pi$ 在窃听者存在的情况下是安全的（相对于修改后的实验 $\widehat{\mathsf{KE}}_{\mathcal{A},\Pi}^{\mathsf{eav}}$）。

PROOF Let $\mathcal{A}$ be a PPT adversary. Since $\Pr[b=0] = \Pr[b=1] = 1/2$, we have

证明　设 $\mathcal{A}$ 是一个 PPT 敌手。由于 $\Pr[b=0] = \Pr[b=1] = 1/2$，我们有

$$\begin{align*}\Pr&\left[\widehat{\mathsf{KE}}_{\mathcal{A},\Pi}^{\mathsf{eav}}(n)=1\right]\\&=\frac{1}{2}\cdot\Pr\left[\widehat{\mathsf{KE}}_{\mathcal{A},\Pi}^{\mathsf{eav}}(n)=1\mid b=0\right]+\frac{1}{2}\cdot\Pr\left[\widehat{\mathsf{KE}}_{\mathcal{A},\Pi}^{\mathsf{eav}}(n)=1\mid b=1\right].\end{align*}$$

In experiment $\widehat{\mathsf{KE}}_{\mathcal{A},\Pi}^{\mathsf{eav}}(n)$ the adversary $\mathcal{A}$ receives $(\mathbb{G}, q, g, h_A, h_B, \hat{k})$, where $(\mathbb{G}, q, g, h_A, h_B)$ represents the transcript of the protocol execution, and $\hat{k}$ is either the actual key computed by the parties (if $b = 0$) or a uniform group element (if $b = 1$). Distinguishing between these two cases is exactly
equivalent to solving the decisional Diffie–Hellman problem. That is

在实验 $\widehat{\mathsf{KE}}_{\mathcal{A},\Pi}^{\mathsf{eav}}(n)$ 中，敌手 $\mathcal{A}$ 收到 $(\mathbb{G}, q, g, h_A, h_B, \hat{k})$，其中 $(\mathbb{G}, q, g, h_A, h_B)$ 表示该次协议执行的交互记录，而 $\hat{k}$ 要么是双方实际计算的密钥（当 $b = 0$ 时），要么是一个均匀的群元素（当 $b = 1$ 时）。区分这两种情况恰好等价于求解判定性 Diffie–Hellman 问题。即

$$\begin{aligned}&\Pr\left[\widehat{\mathsf{KE}}_{\mathcal{A},\Pi}^{\mathsf{eav}}(n)=1\right]\\ &=\frac{1}{2}\cdot\Pr\left[\widehat{\mathsf{KE}}_{\mathcal{A},\Pi}^{\mathsf{eav}}(n)=1\mid b=0\right]+\frac{1}{2}\cdot\Pr\left[\widehat{\mathsf{KE}}_{\mathcal{A},\Pi}^{\mathsf{eav}}(n)=1\mid b=1\right]\\ &=\frac{1}{2}\cdot\Pr[\mathcal{A}(\mathbb{G},q,g,g^{x},g^{y},g^{xy})=0]+\frac{1}{2}\cdot\Pr[\mathcal{A}(\mathbb{G},q,g,g^{x},g^{y},g^{z})=1]\\ &=\frac{1}{2}\cdot\left(1-\Pr[\mathcal{A}(\mathbb{G},q,g,g^{x},g^{y},g^{xy})=1]\right)+\frac{1}{2}\cdot\Pr[\mathcal{A}(\mathbb{G},q,g,g^{x},g^{y},g^{z})=1]\\ &=\frac{1}{2}+\frac{1}{2}\cdot\left(\Pr[\mathcal{A}(\mathbb{G},q,g,g^{x},g^{y},g^{z})=1]-\Pr[\mathcal{A}(\mathbb{G},q,g,g^{x},g^{y},g^{xy})=1]\right)\\ &\leq\frac{1}{2}+\frac{1}{2}\cdot\left|\Pr[\mathcal{A}(\mathbb{G},q,g,g^{x},g^{y},g^{z})=1]-\Pr[\mathcal{A}(\mathbb{G},q,g,g^{x},g^{y},g^{xy})=1]\right|,\end{aligned}$$

where the probabilities are all taken over $(\mathbb{G}, q, g)$ output by $\mathcal{G}({1}^n)$, and uniform choice of $x, y, z \in \mathbb{Z}_q$. (Note that since $g$ is a generator, $g^z$ is a uniform element of $\mathbb{G}$ when $z$ is uniformly distributed in $\mathbb{Z}_q$.) If the decisional Diffie–Hellman assumption is hard relative to $\mathcal{G}$, that exactly means that there is a negligible function $\mathsf{negl}$ for which

其中所有概率都是在由 $\mathcal{G}({1}^n)$ 输出的 $(\mathbb{G}, q, g)$ 以及 $x, y, z \in \mathbb{Z}_q$ 的均匀选取上取得的。（注意，由于 $g$ 是生成元，当 $z$ 在 $\mathbb{Z}_q$ 中均匀分布时，$g^z$ 就是 $\mathbb{G}$ 中的一个均匀元素。）若判定性 Diffie–Hellman 问题相对于 $\mathcal{G}$ 是困难的，则这恰好意味着存在可忽略函数 $\mathsf{negl}$ 使得

$$\left|\Pr[\mathcal{A}(\mathbb{G},q,g,g^{x},g^{y},g^{z})=1]-\Pr[\mathcal{A}(\mathbb{G},q,g,g^{x},g^{y},g^{xy})=1]\right|\leq\mathsf{negl}(n).$$

We conclude that

由此我们得出

$$\Pr\left[\widehat{\mathsf{KE}}_{\mathcal{A},\Pi}^{\mathsf{eav}}(n)=1\right]\leq\frac{1}{2}+\frac{1}{2}\cdot\mathsf{negl}(n),$$

completing the proof.

证毕。

Uniform group elements vs. uniform bit-strings. The previous theorem shows that the key output by Alice and Bob in the Diffie–Hellman protocol is indistinguishable (for a polynomial-time eavesdropper) from a uniform group element. In order to use the key for subsequent cryptographic applications—as well as to meet Definition 11.1—the key output by the parties should instead be indistinguishable from a uniform bit-string of the appropriate length. The Diffie–Hellman protocol can be modified to achieve this by having the parties apply an appropriate key-derivation function (cf. Section 6.6.4) to the shared group element $g^{xy}$ they each compute.

**均匀群元素与均匀比特串。**

前面的定理表明，Diffie–Hellman 协议中 Alice 和 Bob 输出的密钥（对多项式时间窃听者而言）与一个均匀群元素不可区分。而为了将该密钥用于后续的密码学应用——也为了满足定义 11.1——双方输出的密钥应当改为与适当长度的均匀比特串不可区分。为此可以修改 Diffie–Hellman 协议：让双方对他们各自计算出的共享群元素 $g^{xy}$ 应用一个适当的密钥派生函数（参见 6.6.4 节）。

Active adversaries. So far we have considered only an eavesdropping adversary. Although eavesdropping attacks are by far the most common (as they are the easiest to carry out), they are by no means the only possible attack. Active attacks, in which the adversary sends messages of its own to one or both of the parties, are also a concern, and any protocol used in practice must be resilient to such attacks as well. When considering active attacks, it is useful to distinguish, informally, between impersonation attacks where the adversary impersonates one party while interacting with the other party, and man-in-the-middle attacks where both honest parties are executing the protocol and the adversary is intercepting and modifying messages being sent from one party to the other. We will not formally define security against either class of attacks, as such definitions are rather involved and cannot be achieved without the parties sharing some information in advance. Nevertheless, it is worth remarking that the Diffie–Hellman protocol is completely insecure against a man-in-the-middle attack. In fact, a man-in-the-middle adversary can act in such a way that Alice and Bob terminate the protocol with different keys $k_{A}$ and $k_{B}$ that are both known to the adversary, yet neither Alice nor Bob can detect that any attack was carried out. We leave the details of this attack as an exercise.

**主动敌手。**

到目前为止我们只考虑了窃听敌手。尽管窃听攻击是迄今为止最常见的攻击（因为它最容易实施），但它绝不是唯一可能的攻击。主动攻击——敌手向一方或双方发送自己的消息——同样值得关注，任何实际使用的协议也都必须能够抵御这类攻击。在考虑主动攻击时，非正式地区分两类攻击是有益的：一类是假冒攻击，敌手在与另一方交互时假冒其中一方；另一类是中间人攻击，两个诚实方都在执行协议，而敌手截获并修改一方发往另一方的消息。我们不会对这两类攻击形式化地定义安全性，因为这样的定义相当复杂，而且在双方没有预先共享任何信息的情况下根本无法实现。尽管如此，值得指出的是，Diffie–Hellman 协议在面对中间人攻击时是完全不安全的。事实上，中间人敌手可以做到让 Alice 和 Bob 分别以不同的密钥 $k_{A}$ 和 $k_{B}$ 结束协议运行，而这两个密钥都为敌手所知，同时 Alice 和 Bob 却都察觉不到发生过任何攻击。这一攻击的细节留作习题。

Diffie–Hellman key exchange in practice. The Diffie–Hellman protocol in its basic form is typically not used in practice due to its insecurity against man-in-the-middle attacks, as discussed above. This does not detract in any way from its importance. The Diffie–Hellman protocol served as the first demonstration that asymmetric techniques (and number-theoretic problems) could be used to alleviate the problems of key distribution in cryptography. Furthermore, the Diffie–Hellman protocol is at the core of standardized key-exchange protocols that are resilient to man-in-the-middle attacks and are in wide use today. One notable example is TLS; see Section 13.7.

**实践中的 Diffie–Hellman 密钥交换。**

如上所述，由于无法抵抗中间人攻击，基本形式的 Diffie–Hellman 协议通常并不直接付诸实用。但这丝毫不会削弱它的重要性。Diffie–Hellman 协议首次展示了非对称技术（以及数论问题）可以用来缓解密码学中的密钥分发问题。此外，Diffie–Hellman 协议处于一些标准化密钥交换协议的核心位置；这些协议能够抵抗中间人攻击，至今仍在广泛使用。一个著名的例子是 TLS；参见 13.7 节。

## 11.4 The Public-Key Revolution　公钥革命

In addition to key exchange, Diffie and Hellman also introduced in their ground-breaking work the notion of public-key (or asymmetric) cryptography. In the public-key setting (in contrast to the private-key setting we have studied until now), a party who wishes to communicate securely generates a pair of keys: a public key that is widely disseminated, and a private key that it keeps secret. (The fact that there are now two different keys is what makes the scheme asymmetric.) Having generated these keys, a party can use them to ensure secrecy for messages it receives using a public-key encryption scheme, or integrity for messages it sends using a digital signature scheme. (See Figure 11.3.) We provide a brief taste of these primitives here, and discuss them in extensive detail in Chapters 12 and 13, respectively.

除密钥交换之外，Diffie 和 Hellman 还在他们开创性的工作中引入了公钥（或非对称）密码学的概念。在公钥设定中（与我们迄今研究的私钥设定相对），希望安全通信的一方会生成一对密钥：一个是被广泛散布的公钥，另一个是自己保密的私钥。（正是存在两个不同密钥这一事实使方案成为非对称的。）生成这对密钥之后，一方就可以用它们确保所收消息的机密性（使用公钥加密方案），或者确保所发消息的完整性（使用数字签名方案）。（见图 11.3。）我们在此先初步了解这些原语，随后分别在第 12 章和第 13 章详细讨论它们。

In a public-key encryption scheme, the public key generated by some party serves as an encryption key; anyone who knows that public key can use it to encrypt messages and generate corresponding ciphertexts. The private key serves as a decryption key and is used by the party who knows it to recover the original message from any ciphertext generated using the matching public key. Furthermore—and it is amazing that something like this exists!—the secrecy of encrypted messages is preserved even against an adversary who knows the public key (but not the private key). In other words, the (public) encryption key is of no use for an attacker trying to decrypt ciphertexts encrypted using that key.

在公钥加密方案中，某一方生成的公钥充当加密密钥；任何知道该公钥的人都可以用它加密消息、生成相应的密文。私钥则充当解密密钥，持有者用它从任何使用对应公钥生成的密文中恢复出原始消息。更进一步——这样的事情居然存在，实在令人惊叹！——即使面对知道公钥（但不知道私钥）的敌手，被加密消息的机密性依然得以保持。换言之，（公开的）加密密钥对试图解密由它加密的密文的攻击者毫无用处。

|  | Private-Key Setting | Public-Key Setting |
| --- | --- | --- |
| Secrecy | Private-key encryption | Public-key encryption |
| Integrity | Message authentication codes | Digital signature schemes |

|  | 私钥设定 | 公钥设定 |
| --- | --- | --- |
| 机密性 | 私钥加密 | 公钥加密 |
| 完整性 | 消息认证码 | 数字签名方案 |

**FIGURE 11.3: Cryptographic primitives in the private-key and the public-key settings. / 图 11.3：私钥设定与公钥设定下的密码学原语。**

To allow for secret communication, then, a receiver can simply send her public key to a potential sender (without having to worry about an eavesdropper who observes it), or publicize her public key on her webpage or in some central database. A public-key encryption scheme thus enables private communication without relying on a private channel for key distribution. $^{1}$

这样一来，为实现秘密通信，接收方只需把她的公钥发给潜在的发送方（无须担心窃听者看到公钥），或者把她的公钥公布在自己的网页上或某个中央数据库中。于是，公钥加密方案使得私密通信不再依赖私密信道来进行密钥分发。$^{1}$

A digital signature scheme is a public-key analogue of a message authentication code (MAC). Here, the private key serves as an “authentication key” (called a signing key) that enables the party who knows this key to generate “authentication tags” (aka signatures) for messages it sends. The public key acts as a verification key, allowing anyone who knows it to verify signatures issued by the sender. As with MACs, a digital signature scheme can be used to prevent undetected tampering of a message; here, however, security holds even against an adversary who knows the public key. The fact that verification is public (i.e., can be done by anyone who knows the public key of the sender) has far-reaching ramifications, as it makes it possible to take a document signed by Alice and present it to a third party (say, a judge) for verification. This property is called non-repudiation and has extensive applications in e-commerce (e.g., for signing legal documents). Digital signatures are also used for the secure distribution of public keys as part of a public-key infrastructure, as discussed in more detail in Section 13.6.

数字签名方案相当于消息认证码（MAC）在公钥场景下的对应物。这里，私钥充当“认证密钥”（称为签名密钥），使持有该密钥的一方能够为其发送的消息生成“认证标签”（即签名）。公钥则充当验证密钥，任何知道公钥的人都可以验证发送方签发的签名。与 MAC 一样，数字签名方案可用于防止消息被篡改而不被发现；不过这里的安全性即使在敌手知道公钥时依然成立。验证是公开的（即任何知道发送方公钥的人都可以执行验证），这一事实影响深远：它使得人们可以把一份由 Alice 签署的文件交给第三方（比如法官）去核验。这一性质称为不可否认性，在电子商务中有着广泛应用（例如签署法律文件）。数字签名还被用于公钥基础设施中公钥的安全分发，详见 13.6 节。

In their paper, Diffie and Hellman set forth the notion of public-key cryptography but did not give any candidate constructions. A year later, Ron Rivest, Adi Shamir, and Len Adleman proposed the RSA problem and presented the first public-key encryption and digital signature schemes based on the hardness of that problem. Variants of their schemes are now among the most widely used cryptosystems today. In 1985, Taher El Gamal presented an encryption scheme that is essentially a slight twist on the Diffie–Hellman key-exchange protocol, variants of which are now also widely used. Thus, although Diffie and Hellman did not succeed in constructing a (non-interactive) public-key encryption scheme, they came very close.

在论文中，Diffie 和 Hellman 提出了公钥密码学的概念，却没有给出任何候选构造。一年之后，Ron Rivest、Adi Shamir 和 Len Adleman 提出了 RSA 问题，并给出了首批基于该问题困难性的公钥加密方案与数字签名方案。他们方案的变体位列当今使用最广泛的密码体制之中。1985 年，Taher El Gamal 提出了一个加密方案，它实质上是 Diffie–Hellman 密钥交换协议的一个小小改动，其变体如今也被广泛使用。因此，尽管 Diffie 和 Hellman 未能成功构造出（非交互式的）公钥加密方案，但他们已经非常接近了。

We conclude by summarizing how public-key cryptography addresses the limitations of the private-key setting discussed in Section 11.1:

最后我们总结一下，公钥密码学是如何应对 11.1 节所讨论的私钥设定的种种局限的：

1. Public-key cryptography allows key distribution to be done over public (but authenticated) channels. This can simplify the distribution and updating of shared, secret keys.

   公钥密码学允许通过公共（但经认证的）信道进行密钥分发。这可以简化共享秘密密钥的分发与更新。

2. Public-key cryptography reduces the need for users to store many secret keys. Consider again the setting of a large corporation where each pair of employees needs the ability to communicate securely. Using public-key cryptography, it suffices for each employee to store just a single private key (their own) and the public keys of all other employees. Importantly, these latter keys do not need to be kept secret; they could even be stored in some central (public) repository.

   公钥密码学减少了用户存储大量秘密密钥的需求。再次考虑大型公司的情形，其中每两名员工都需要能够安全通信。使用公钥密码学，每位员工只需存储一个自己的私钥以及所有其他员工的公钥即可。重要的是，后者无需保密，甚至可以存放在某个中央（公开）存储库中。

3. Finally, public-key cryptography is (more) suitable for open environments where parties who have never previously interacted want the ability to communicate securely. As one commonplace example, a company can post its public key on-line; a user making a purchase can obtain the company’s public key, as needed, when they need to encrypt their credit-card information to send to that company.

   最后，公钥密码学（更）适用于开放环境：此前从未打过交道的各方也希望拥有安全通信的能力。举一个平常的例子，公司可以在网上公布其公钥；购物的用户在需要把自己的信用卡信息加密后发给该公司时，按需获取该公司的公钥即可。

The invention of public-key encryption was a revolution in cryptography. It is no coincidence that until the late 1970s and early 1980s, encryption and cryptography in general belonged to the domain of intelligence and military organizations, and only with the advent of public-key techniques did the use of cryptography become widespread.

公钥加密的发明是密码学的一场革命。20 世纪 70 年代末和 80 年代初之前，加密乃至整个密码学一直属于情报机构和军事组织的领域，直到公钥技术问世，密码学的使用才得以普及——这并非偶然。

Why study private-key cryptography? It should be apparent that public-key cryptography is strictly stronger than private-key cryptography; in particular, any public-key encryption scheme could be used as a private-key encryption scheme. (The communicating users can simply share both the public key and the private key. If secrecy for encrypted messages holds even when the eavesdropper knows the public key, then it clearly holds when the public key is kept secret!) So why did we bother studying private-key cryptography at all? The answer is simple: private-key cryptography is much more efficient than public-key cryptography, and should be used in settings where it is appropriate. That is, in cases where it is possible for communicating parties to share a key, private-key cryptography should be used. This includes small-scale, closed systems of users as well as applications like disk encryption. Moreover, as we will see in Sections 12.3 and 13.7, private-key encryption is used in the public-key setting to obtain better efficiency.

**为什么要研究私钥密码学？**

显而易见，公钥密码学严格强于私钥密码学；特别是，任何公钥加密方案都可以当作私钥加密方案来使用。（通信双方只需同时共享公钥和私钥即可。既然即使在窃听者知道公钥时加密消息仍能保持机密性，那么在公钥保密的情况下显然更不成问题！）那么，我们为什么还要费心研究私钥密码学呢？答案很简单：私钥密码学比公钥密码学高效得多，应当在合适的场合加以使用。也就是说，只要通信双方有可能共享密钥，就应当使用私钥密码学。这包括小规模的封闭用户系统以及磁盘加密之类的应用。此外，正如我们将在 12.3 节和 13.7 节看到的，在公钥设定中也会借助私钥加密来获得更高的效率。

## References and Additional Reading　参考文献与延伸阅读

We have only briefly discussed the problems of key distribution and key management. For more information, we recommend looking at textbooks on network security, such as the one by Kaufman et al. [113].

我们对密钥分发与密钥管理问题的讨论只是点到为止。欲了解更多信息，建议参阅网络安全方面的教材，例如 Kaufman 等人的著作 [113]。

We have not made any attempt to capture the full history of the development of public-key cryptography. Others besides Diffie and Hellman were working on similar ideas in the 1970s. One researcher in particular doing similar and independent work was Ralph Merkle, considered by many to be a co-inventor of public-key cryptography (although he published after Diffie and Hellman). We also mention Michael Rabin, who developed constructions of signature schemes and public-key encryption schemes based on the hardness of factoring about one year after the work of Rivest, Shamir, and Adleman [171]. We highly recommend reading the original paper by Diffie and Hellman [65], and refer the reader to the book by Levy [129] for more on the political and historical aspects of the public-key revolution.

我们并未试图完整梳理公钥密码学的发展历史。除 Diffie 和 Hellman 之外，20 世纪 70 年代还有其他人也在研究类似的想法。其中一位做着相似且独立工作的研究者是 Ralph Merkle，许多人视他为公钥密码学的共同发明人（尽管他的成果发表晚于 Diffie 和 Hellman）。我们还要提到 Michael Rabin，他在 Rivest、Shamir 和 Adleman 的工作 [171] 之后约一年，基于因子分解的困难性给出了签名方案和公钥加密方案的构造。我们强烈推荐阅读 Diffie 和 Hellman 的原始论文 [65]；想进一步了解公钥革命的政治与历史侧面的读者，可参阅 Levy 的著作 [129]。

Interestingly, aspects of public-key cryptography were discovered in the intelligence community before being published in the open scientific literature. In the early 1970s, James Ellis, Clifford Cocks, and Malcolm Williamson of the British intelligence agency GCHQ invented the notion of public-key cryptography, a variant of RSA encryption, and a variant of the Diffie–Hellman key-exchange protocol. Their work was not declassified until 1997. Although the underlying mathematics of public-key cryptography may have been discovered before 1976, it is fair to say that the widespread ramifications of this new technology were not appreciated until Diffie and Hellman came along.

有趣的是，公钥密码学的若干要点在公开发表于学术文献之前，就已由情报界发现。20 世纪 70 年代初，英国情报机构 GCHQ 的 James Ellis、Clifford Cocks 和 Malcolm Williamson 发明了公钥密码学的概念、RSA 加密的一个变体以及 Diffie–Hellman 密钥交换协议的一个变体。他们的工作直到 1997 年才解密。尽管公钥密码学背后的数学可能在 1976 年之前就已被发现，但可以说，直到 Diffie 和 Hellman 出现之后，这项新技术的广泛影响才真正为人们所认识。

## Exercises　习题

11.1 Let $\Pi$ be a key-exchange protocol, and ($\mathsf{Enc},\mathsf{Dec}$) be a private-key encryption scheme. Consider the following interactive protocol $\Pi^{\prime}$ for encrypting a message: first, the sender and receiver run $\Pi$ to generate a shared key $k$. Next, the sender computes $c \leftarrow \mathsf{Enc}_k(m)$ and sends $c$ to the other party, who decrypts and recovers $m$ using $k$.

习题 11.1　设 $\Pi$ 是一个密钥交换协议，($\mathsf{Enc},\mathsf{Dec}$) 是一个私钥加密方案。考虑如下用于加密消息的交互式协议 $\Pi^{\prime}$：首先，发送方与接收方运行 $\Pi$ 以生成共享密钥 $k$；接着，发送方计算 $c \leftarrow \mathsf{Enc}_k(m)$ 并把 $c$ 发送给对方，对方用 $k$ 解密并恢复出 $m$。

(a) Formulate a definition of indistinguishable encryptions in the presence of an eavesdropper (cf. Definition 3.8) appropriate for this interactive setting.

（a）给出适合这一交互式设定的、窃听者存在下的不可区分加密的定义（参照定义 3.8）。

(b) Prove that if $\Pi$ is secure in the presence of an eavesdropper and ($\mathsf{Enc}, \mathsf{Dec}$) has indistinguishable encryptions in the presence of an eavesdropper, then $\Pi^{\prime}$ satisfies your definition.

（b）证明：若 $\Pi$ 在窃听者存在的情况下是安全的，且 ($\mathsf{Enc}, \mathsf{Dec}$) 具有窃听者存在下的不可区分加密性质，则 $\Pi^{\prime}$ 满足你在（a）中给出的定义。

11.2 Show that, for either of the groups considered in Sections 9.3.3 or 9.3.4, a uniform group element (expressed using the natural representation) is easily distinguishable from a uniform bit-string of the same length.

习题 11.2　证明：对于 9.3.3 节或 9.3.4 节中所考虑的任何一个群，均匀群元素（用自然表示表出）都很容易与同等长度的均匀比特串区分开。

11.3 Describe a man-in-the-middle attack on the Diffie–Hellman protocol where the adversary shares a key $k_{A}$ with Alice and a (different) key $k_{B}$ with Bob, and Alice and Bob cannot detect that anything is wrong.

习题 11.3　描述针对 Diffie–Hellman 协议的一次中间人攻击：敌手与 Alice 共享密钥 $k_{A}$、与 Bob 共享（另一个不同的）密钥 $k_{B}$，而 Alice 和 Bob 都无法察觉任何异常。

11.4 Consider the following key-exchange protocol:

习题 11.4　考虑以下密钥交换协议：

(a) Alice chooses uniform $k, r \in \{0,1\}^n$, and sends $s := k \oplus r$ to Bob.

（a）Alice 均匀选取 $k, r \in \{0,1\}^n$，并将 $s := k \oplus r$ 发送给 Bob。

(b) Bob chooses uniform $t \in \{0,1\}^n$, and sends $u := s \oplus t$ to Alice.

（b）Bob 均匀选取 $t \in \{0,1\}^n$，并将 $u := s \oplus t$ 发送给 Alice。

(c) Alice computes $w := u \oplus r$ and sends $w$ to Bob.

（c）Alice 计算 $w := u \oplus r$，并将 $w$ 发送给 Bob。

(d) Alice outputs $k$ and Bob outputs $w \oplus t$.

（d）Alice 输出 $k$，Bob 输出 $w \oplus t$。

Show that Alice and Bob output the same key. Analyze the security of this protocol against a passive eavesdropper.

证明 Alice 和 Bob 输出相同的密钥，并分析该协议抵抗被动窃听者的安全性。
