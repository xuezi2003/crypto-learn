## 6.5 The Random-Oracle Model　6.5 随机预言机模型

There are several examples of constructions based on cryptographic hash functions that cannot be proven secure based only on the assumption that the hash function is collision or preimage resistant. (We will see some in the following section.) In many cases, there appears to be no simple and reasonable assumption regarding the hash function that is sufficient for proving the construction secure.

有若干基于密码学哈希函数的构造示例，它们无法仅仅基于哈希函数抗碰撞性或原像抗性的假设来证明安全性。（我们将在下一节看到一些。）在许多情况下，似乎不存在关于哈希函数的简单且合理的假设足以证明该构造是安全的。

Faced with this situation, there are several options. One is to look for schemes that can be proven secure based on some reasonable assumption about the underlying hash function. This is a good approach, but it leaves open the question of what to do until such schemes are found. Also, provably secure constructions may be significantly less efficient than other existing approaches that have not been proven secure. (This is a major issue we will encounter in the setting of public-key cryptography.)

面对这种情况，有几种选择。其一是寻找能够基于对底层哈希函数的某个合理假设来证明安全的方案。这是一种好方法，但它留下了一个悬而未决的问题：在这些方案被找到之前该怎么办。此外，可证明安全的构造可能明显不如其他尚未被证明安全的现有方法高效。（这是我们在公钥密码学中将遇到的一个主要问题。）

Another possibility, of course, is to use an existing cryptosystem even if it has no justification for its security other than, perhaps, the fact that the designers tried to attack it and were unsuccessful. This flies in the face of everything we have said about the importance of the rigorous, modern approach to cryptography, and it should be clear that this is unacceptable.

当然，另一种可能是使用现有的密码系统，即使它除了（或许）设计者曾试图攻破它但未获成功这一事实外，对其安全性没有任何正当理由。这有悖于我们此前强调的严格、现代密码学方法的重要性，显然这是不可接受的。

An approach that has been hugely successful in practice, and which offers a “middle ground” between a fully rigorous proof of security on the one hand and no proof whatsoever on the other, is to introduce an idealized model in which to prove the security of cryptographic schemes. Although the idealization may not be an entirely accurate reflection of reality, we can at least derive some measure of confidence in the soundness of a scheme’s design from a proof within the idealized model. As long as the model is reasonable, such proofs are certainly better than no proofs at all.

一种在实践中取得巨大成功、并在严格的安全性证明与完全没有任何证明之间提供“中间地带”的方法，是引入一个理想化模型，在其中证明密码学方案的安全性。尽管理想化可能并非对现实的完全准确反映，但我们至少可以从理想化模型内的证明中获得对该方案设计合理性的某种程度的信心。只要模型是合理的，这样的证明当然比完全没有证明要好。

A popular example of this approach is the random-oracle model, which treats a cryptographic hash function $H$ as a truly random function. (We have already seen an example of this in our discussion of birthday attacks, although there we were analyzing an attack rather than a construction.) More specifically, the random-oracle model posits the existence of a public, random function $H$ that can be evaluated only by “querying” an oracle—which can be thought of as a “black box”—that returns $H(x)$ when given input $x$. (We will discuss how this is to be interpreted in the following section.) To differentiate things, the model we have been using until now (where no random oracle is present) is sometimes called the “standard model,” although at this point the random-oracle model itself is considered quite standard in the literature.

这种方法的一个流行例子是随机预言机模型（random-oracle model），它把密码学哈希函数 $H$ 视为一个真正的随机函数。（我们在对生日攻击的讨论中已经见过这样的例子，尽管那里我们分析的是攻击而非构造。）更具体地说，随机预言机模型假设存在一个公开的随机函数 $H$，它只能通过“查询”一个预言机——可被视为一个“黑盒”——来求值，该预言机在给定输入 $x$ 时返回 $H(x)$。（我们将在下一节讨论应如何解释这一点。）为了区分，我们迄今一直使用的模型（其中没有随机预言机）有时被称为“标准模型”（standard model），尽管此时随机预言机模型本身在文献中已被视为相当标准。

No one claims that a random oracle exists, although there have been suggestions that a random oracle could be implemented in practice using a trusted party (i.e., some server on the Internet). Rather, the random-oracle model provides a formal methodology that can be used to design and validate cryptographic schemes using the following two-step approach:

没有人声称随机预言机存在，尽管有人建议可以使用可信方（即互联网上的某个服务器）在实践中实现随机预言机。相反，随机预言机模型提供了一种形式化方法，可用以下两步法来设计和验证密码学方案：

1. First, a scheme is designed and proven secure in the random-oracle model. That is, we assume the world contains a random oracle, and construct and analyze a cryptographic scheme within this model. Standard cryptographic assumptions of the type we have seen until now may be utilized in the proof of security as well.

   首先，在随机预言机模型中设计一个方案并证明其安全性。即我们假设世界中存在一个随机预言机，并在此模型内构造和分析一个密码学方案。在安全性证明中也可使用我们迄今所见类型的标准密码学假设。

2. When we want to implement the scheme in the real world, a random oracle is not available. Instead, the random oracle is instantiated with an appropriately designed cryptographic hash function $\hat{H}$. (We return to this point at the end of this section.) That is, at each point where the scheme dictates that a party should query the oracle for the value $H(x)$, the party instead computes $\hat{H}(x)$ on its own.

   当我们想在现实世界中实现该方案时，并没有随机预言机可用。相反，需要用经过适当设计的密码学哈希函数 $\hat{H}$ 来实例化随机预言机。（我们将在本节末尾回到这一点。）即，在方案规定某方应向预言机查询值 $H(x)$ 的每个地方，该方转而自行计算 $\hat{H}(x)$。

The hope is that the cryptographic hash function used in the second step is “sufficiently good” at emulating a random oracle, so that the security proof given in the first step will carry over to the real-world instantiation of the scheme. The difficulty here is that there is no theoretical justification for this hope, and in fact there are (contrived) schemes that can be proven secure in the random-oracle model but are insecure no matter how the random oracle is instantiated in the second step. Furthermore, it is not clear (mathematically or heuristically) what it means for a hash function to be “sufficiently good” at emulating a random oracle, nor is it clear that this is an achievable goal. In particular, no concrete instantiation $\hat{H}$ can ever behave like a random function, since $\hat{H}$ is fixed and its code is known. For these reasons, a proof of security in the random-oracle model should be viewed as providing evidence that a scheme has no “inherent design flaws,” but is not a rigorous proof that any real-world instantiation of the scheme is secure. Further discussion on how to interpret proofs in the random-oracle model is given in Section 6.5.2.

希望在于第二步所用的密码学哈希函数在模拟随机预言机方面“足够好”，使得第一步给出的安全性证明能延续到该方案的现实世界实例化。这里的困难在于，这种希望没有理论依据，事实上存在（人为设计的）方案，它们在随机预言机模型中可被证明安全，但无论在第二步中随机预言机如何被实例化都是不安全的。此外，一个哈希函数在模拟随机预言机方面“足够好”意味着什么，这一点（在数学上或启发式上）并不清楚，这是否是一个可实现的目标也不清楚。特别地，没有任何具体的实例化 $\hat{H}$ 能表现得像一个随机函数，因为 $\hat{H}$ 是固定的且其代码是已知的。由于这些原因，随机预言机模型中的安全性证明应被视为提供了一种证据，表明方案没有“固有的设计缺陷”，但并不能严格证明该方案的任何现实世界实例化都是安全的。关于如何解释随机预言机模型中的证明，进一步讨论见 6.5.2 节。

### 6.5.1 The Random-Oracle Model in Detail　6.5.1 随机预言机模型详解

Before continuing, let us pin down exactly what the random-oracle model entails. A good way to think about the random-oracle model is as follows: The oracle is simply a “black box” that takes a bit-string as input and returns a bit-string as output. The internal workings of the box are unknown and inscrutable. Everyone—honest parties as well as the adversary—can interact with the box, where such interaction consists of feeding in a binary string x as input and receiving a binary string y as output; we refer to this as querying the oracle on x, and call x a query made to the oracle. Queries to the oracle are assumed to be private so that if some party queries the oracle on input x then no one else learns x, or even learns that this party queried the oracle at all. This makes sense, because calls to the oracle correspond (in the real-world instantiation) to local evaluations of a cryptographic hash function.

在继续之前，让我们先弄清随机预言机模型究竟意味着什么。理解随机预言机模型的一种好方式如下：预言机不过是一个“黑盒”，它以一个比特串为输入并返回一个比特串作为输出。盒子的内部工作机制是未知的、不可探究的。所有人——诚实方以及敌手——都可以与盒子交互，这种交互就是输入一个二元串 x 并接收一个二元串 y 作为输出；我们把这称为以 x 为输入查询预言机，并称 x 为向预言机所作的一次查询。假设对预言机的查询是私密的：如果某方以 x 为输入查询了预言机，那么没有其他人会得知 x，甚至不会知道该方曾查询过预言机。这是合理的，因为对预言机的调用对应于（在现实世界实例化中）密码学哈希函数的本地求值。

An important property of this “box” is that it is consistent. That is, if the box ever outputs y for a particular input x, then it always outputs the same answer y when given the same input x again. This means that we can view the box as implementing a well-defined function $H$; i.e., we define the function H in terms of the input/output characteristics of the box. For convenience, we thus speak of “querying H” rather than querying the box. No one “knows” the entire function $H$ (except the box itself); at best, all that is known are the values of H on the strings that have been explicitly queried thus far.

这个“盒子”的一个重要性质是它是一致的。即，如果盒子对某个特定输入 $x$ 曾输出过 $y$，那么当再次给定相同输入 $x$ 时，它总是输出相同的答案 $y$。这意味着我们可以把盒子视为实现了一个良定义的函数 $H$；即我们根据盒子的输入/输出特征来定义函数 H。为方便起见，我们因此说“查询 H”而不是查询盒子。没有人“知道”整个函数 $H$（除了盒子本身）；我们至多只知道 H 在迄今已显式查询过的那些串上的取值。

We have already discussed in Chapter 3 what it means to choose a random function $H$. We only reiterate here that there are two equivalent ways to think about the uniform selection of $H$: either view $H$ as being chosen “in one shot” uniformly from the set of all functions on some specified domain and range, or imagine generating outputs for $H$ “on-the-fly,” as needed. Specifically, in the second case we can view the function as being defined by a table that is initially empty. When the oracle receives a query $x$ it first checks whether $x = x_i$ for some pair $(x_i, y_i)$ in the table; if so, the corresponding value $y_i$ is returned. Otherwise, a uniform string $y \in \{0,1\}^{\ell}$ is chosen (for some specified $\ell$), the answer $y$ is returned, and the oracle stores $(x,y)$ in its table. This second viewpoint is often conceptually easier to reason about, and is also technically easier to deal with if $H$ is defined over an infinite domain (e.g., $\{0,1\}^*$).

我们已经在第 3 章讨论过选择一个随机函数 $H$ 意味着什么。我们在此只重申，思考 $H$ 的均匀选择有两种等价方式：要么把 $H$ 视为从某个指定定义域和值域上所有函数的集合中“一次性”均匀地选出的，要么想象根据需要“即时”地为 $H$ 生成输出。具体而言，在第二种情形下，我们可以把函数看作由一张初始为空的表来定义。当预言机收到查询 $x$ 时，它首先检查表中是否存在某个对 $(x_i, y_i)$ 使得 $x = x_i$；若是，则返回相应的值 $y_i$。否则，选择一个均匀串 $y \in \{0,1\}^{\ell}$（对某个指定的 $\ell$），返回答案 $y$，并将 $(x,y)$ 存入预言机的表。这第二种观点在概念上通常更易于推理，并且在 $H$ 定义在无穷定义域（例如 $\{0,1\}^*$）上时在技术上更易处理。

When we defined pseudorandom functions in Section 3.5.1, we also considered algorithms having oracle access to a random function. Lest there be any confusion, we note that the usage of a random function there is very different from the usage of a random function here. There, a random function was used as a way of defining what it means for a (concrete) keyed function to be pseudorandom. In the random-oracle model, in contrast, the random function is used as part of a construction itself and must somehow be instantiated in the real world if we want a concrete realization of the construction. A pseudorandom function is not a random oracle because it is only pseudorandom if the key is secret. However, in the random-oracle model all parties need to be able to compute the function; thus there can be no secret key.

在 3.5.1 节定义伪随机函数时，我们也考虑过可以对随机函数作预言机访问的算法。为避免混淆，我们在此强调：那里的随机函数用法与这里的截然不同。在那里，随机函数只是用来定义“一个（具体的）带密钥函数是伪随机的”这一概念。相比之下，在随机预言机模型中，随机函数是构造方案本身的一部分；若要得到该方案的具体实现，就必须在现实世界中以某种方式实例化这个随机函数。伪随机函数不是随机预言机，因为它只有在密钥保密的前提下才是伪随机的。然而，在随机预言机模型中，所有参与方都必须能够计算该函数，因此不可能存在秘密密钥。

#### Definitions and Proofs in the Random-Oracle Model　随机预言机模型中的定义与证明

Definitions in the random-oracle model are slightly different from their counterparts in the standard model because the probability spaces considered in each case are not the same. In the standard model a scheme $\Pi$ is secure if for all PPT adversaries A the probability of some event is below some threshold, where this probability is taken over the random choices of the parties running $\Pi$ and those of the adversary A. Assuming the honest parties who use $\Pi$ in the real world make random choices as directed by the scheme, satisfying a definition of this sort guarantees security for real-world usage of $\Pi$.

随机预言机模型中的定义与标准模型中的对应定义略有不同，因为在两种情形下所考虑的概率空间并不相同。在标准模型中，一个方案 $\Pi$ 是安全的，如果对所有 PPT 敌手 $\mathcal{A}$，某事件的概率低于某个阈值，其中该概率取自运行 $\Pi$ 的各方以及敌手 $\mathcal{A}$的随机选择。假设在现实世界中使用 $\Pi$ 的诚实方按方案的指示做出随机选择，满足此类定义就保证了 $\Pi$ 在现实世界中使用的安全性。

In the random-oracle model, in contrast, a scheme $\Pi$ may rely on an oracle $H$. As before, $\Pi$ is secure if for all PPT adversaries $\mathcal{A}$ the probability of some event is below some threshold, but now this probability is taken over random choice of $H$ as well as the random choices of the parties running $\Pi$ and those of the adversary $\mathcal{A}$. When using $\Pi$ in the real world, some (instantiation of) $H$ must be fixed. Unfortunately, security of $\Pi$ is not guaranteed for any particular choice of $H$. This indicates one reason why it is difficult to argue that any concrete instantiation of the oracle $H$ by some fixed function yields a secure scheme. (An additional, technical, difficulty is that once a concrete function $H$ is fixed, the adversary $\mathcal{A}$ is no longer restricted to querying $H$ as an oracle but can instead look at and use the code of $H$ in its attack.)

相比之下，在随机预言机模型中，方案 $\Pi$ 可能依赖于一个预言机 $H$。与之前一样，$\Pi$ 是安全的，如果对所有 PPT 敌手 $\mathcal{A}$，某事件的概率低于某个阈值，但现在该概率还取自 $H$ 的随机选择以及运行 $\Pi$ 的各方和敌手 $\mathcal{A}$ 的随机选择。当在现实世界中使用 $\Pi$ 时，必须固定某个（实例化的）$H$。不幸的是，对于 $H$ 的任何特定选择，$\Pi$ 的安全性都得不到保证。这指出了难以论证下述结论的一个原因：用某个固定函数对预言机 $H$ 的任何具体实例化都能产生安全方案。（另一个技术上的困难是，一旦固定了具体函数 $H$，敌手 $\mathcal{A}$ 就不再被限制为以预言机方式查询 $H$，而是可以在其攻击中查看并使用 $H$ 的代码。）

Proofs in the random-oracle model can exploit the fact that $H$ is chosen at random, and that the only way to evaluate $H(x)$ is to explicitly query $x$ to $H$. Three properties of the random-oracle model are especially useful; we sketch them informally here, and show some simple applications of them in what follows, but caution that a full understanding will likely have to wait until we present formal proofs in the random-oracle model in later chapters.

随机预言机模型中的证明可以利用 $H$ 是随机选择的这一事实，以及求值 $H(x)$ 的唯一方式是显式地向 $H$ 查询 $x$。随机预言机模型有三个特别有用的性质；我们在此非正式地概述它们，并在后文给出一些简单应用；但要提醒的是，要充分理解这些性质，可能得等到我们在后续章节中给出随机预言机模型中的形式化证明。

A first useful property of the random-oracle model is:

随机预言机模型的第一个有用性质是：

If x has not been queried to H, then the value of $H(x)$ is uniform.

如果尚未向 H 查询过 x，则 $H(x)$ 的值是均匀的。

This may seem superficially similar to the guarantee provided by a pseudo-random generator, but is actually much stronger. If $G$ is a pseudorandom generator then $G(x)$ is pseudorandom to an observer assuming $x$ is chosen uniformly at random and is completely unknown to the observer. If $H$ is a random oracle, however, then $H(x)$ is truly uniform to an observer as long as the observer has not queried $x$. This is true even if $x$ is known, or if $x$ is not uniform but is hard to guess. (For example, if $x$ is an $n$-bit string where the first half of $x$ is known and the last half is random then $G(x)$ might be easy to distinguish from random but $H(x)$ will not be.)

这在表面上可能看起来与伪随机生成器所提供的保证类似，但实际上要强得多。如果 $G$ 是伪随机生成器，那么假设 $x$ 是均匀随机选择且对观察者完全未知，则 $G(x)$ 对观察者而言是伪随机的。然而如果 $H$ 是随机预言机，那么只要观察者未曾查询过 $x$，$H(x)$ 对观察者而言就是真正均匀的。即使 $x$ 是已知的，或者 $x$ 不是均匀的但难以猜测，这一点也成立。（例如，如果 $x$ 是一个 $n$ 比特串，其中 $x$ 的前半部分已知而后半部分是随机的，那么 $G(x)$ 可能容易与随机区分，但 $H(x)$ 不会。）

The remaining two properties relate explicitly to proofs by reduction in the random-oracle model. (It may be helpful here to review Section 3.3.2.) As part of the reduction, the random oracle that the adversary A interacts with must be simulated. That is: A will submit queries to, and receive answers from, what it believes to be the oracle, but the reduction itself must now answer these queries. This turns out to give a lot of power. For starters:

其余两个性质与随机预言机模型中的归约证明明确相关。（此处复习 3.3.2 节可能会有帮助。）作为归约的一部分，敌手 $\mathcal{A}$ 与之交互的随机预言机必须被模拟。即：$\mathcal{A}$ 将向它认为是预言机的对象提交查询并接收答案，但归约本身现在必须回答这些查询。事实证明，这赋予了归约很大的能力。首先：

**If A queries x to H, the reduction can see this query and learn x.**

**如果 A 向 H 查询 x，归约就能看到此查询并获知 x。**

This is sometimes called “extractability.” (This does not contradict the fact, mentioned earlier, that queries to the random oracle are “private.” While that is true in the random-oracle model itself, here we are using $\mathcal{A}$ as a subroutine within a reduction that is simulating the random oracle for $\mathcal{A}$.) Finally:

这有时被称为“可提取性”（extractability）。（这与前面提到的事实——对随机预言机的查询是“私密的”——并不矛盾。虽然在随机预言机模型本身中确实如此，但这里我们是在为 $\mathcal{A}$ 模拟随机预言机的归约中将 $\mathcal{A}$ 用作子程序。）最后：

The reduction can set the value of $H(x)$ (i.e., the response to query $x$) to a value of its choice, as long as this value is correctly distributed, i.e., uniform.

归约可以把 $H(x)$ 的值（即对查询 $x$ 的响应）设为其所选的任意值，只要该值分布正确，即服从均匀分布。

This is called “programmability.” There is no counterpart to extractability or programmability once H is instantiated with any concrete function.

这被称为“可编程性”（programmability）。一旦 H 被任何具体函数实例化，可提取性或可编程性就没有对应物了。

#### Simple Illustrations of the Random-Oracle Model　随机预言机模型的简单示例

At this point some examples may be helpful. The examples given here are relatively simple, and do not use the full power of the random-oracle model; they are intended merely to provide a gentle introduction. In what follows, we assume a random oracle mapping $\ell_{in}$-bit inputs to $\ell_{out}$-bit outputs, where $\ell_{in}, \ell_{out} > n$, the security parameter (so $\ell_{in}, \ell_{out}$ are functions of n).

此时一些示例可能有帮助。这里给出的示例相对简单，并未使用随机预言机模型的全部能力；它们只是为了提供一个浅显的入门介绍。在下文中，我们假设一个把 $\ell_{in}$ 比特输入映射到 $\ell_{out}$ 比特输出的随机预言机，其中 $\ell_{in}, \ell_{out} > n$（安全参数），所以 $\ell_{in}, \ell_{out}$ 是 n 的函数。

A random oracle as a pseudorandom generator. We first show that, for $\ell_{out} > \ell_{in}$, a random oracle can be used as a pseudorandom generator. (We do not say that a random oracle is a pseudorandom generator, since a random oracle is not a fixed function.) Formally, we claim that for any PPT adversary A, there is a negligible function $\mathsf{negl}$ such that

作为伪随机生成器的随机预言机。我们首先证明，对于 $\ell_{out} > \ell_{in}$，随机预言机可被用作伪随机生成器。（我们不是说随机预言机就是伪随机生成器，因为随机预言机不是固定函数。）形式化地，我们断言对任意 PPT 敌手 A，存在一个可忽略函数 $\mathsf{negl}$ 使得

$$
\left|\Pr[\mathcal{A}^{H(\cdot)}(y)=1]-\Pr[\mathcal{A}^{H(\cdot)}(H(x))=1]\right|\leq\mathsf{negl}(n),
$$

where in the first case the probability is taken over uniform choice of $H$, uniform choice of $y \in \{0,1\}^{\ell_{out}(n)}$, and the randomness of $\mathcal{A}$, and in the second case the probability is taken over uniform choice of $H$, uniform choice of $x \in \{0,1\}^{\ell_{in}(n)}$, and the randomness of $\mathcal{A}$. We have explicitly indicated that $\mathcal{A}$ has oracle access to $H$ in each case; once $H$ has been chosen then $\mathcal{A}$ can freely make queries to it.

其中第一种情形下概率取自 $H$ 的均匀选择、$y \in \{0,1\}^{\ell_{out}(n)}$ 的均匀选择以及 $\mathcal{A}$ 的随机性，第二种情形下概率取自 $H$ 的均匀选择、$x \in \{0,1\}^{\ell_{in}(n)}$ 的均匀选择以及 $\mathcal{A}$ 的随机性。我们已明确指出在每种情形下 $\mathcal{A}$ 都对 $H$ 有预言机访问；一旦 $H$ 被选定，$\mathcal{A}$ 就可以自由地向它查询。

As a proof sketch, let $S$ denote the set of points on which $\mathcal{A}$ queries $H$; of course, $|S|$ is polynomial in $n$. Observe that in the second case, the probability that $x \in S$ is negligible—this is because $\mathcal{A}$ starts with no information about $x$ (note that $H(x)$ by itself reveals nothing about $x$ because $H$ is a random function), and $S$ is exponentially smaller than $\{0,1\}^{\ell_{in}}$. Moreover, conditioned on $x \notin S$ in the second case, $\mathcal{A}$'s input in each case is a uniform string that is independent of the answers to $\mathcal{A}$'s queries.

作为证明梗概，令 $S$ 表示 $\mathcal{A}$ 查询 $H$ 的点集；当然，$|S|$ 是 $n$ 的多项式。注意在第二种情形下，$x \in S$ 的概率是可忽略的——这是因为 $\mathcal{A}$ 一开始没有关于 $x$ 的任何信息（注意 $H(x)$ 本身不透露关于 $x$ 的任何信息，因为 $H$ 是随机函数），且 $S$ 比 $\{0,1\}^{\ell_{in}}$ 指数级地小。此外，在第二种情形下以 $x \notin S$ 为条件，$\mathcal{A}$ 在每种情形下的输入都是一个独立于 $\mathcal{A}$ 查询答案的均匀串。

A random oracle as a collision-resistant hash function. If $\ell_{out} < \ell_{in}$, a random oracle is collision resistant. That is, the success probability of any PPT adversary A in the following experiment is negligible:

作为抗碰撞哈希函数的随机预言机。如果 $\ell_{out} < \ell_{in}$，随机预言机是抗碰撞的。即任何 PPT 敌手 $\mathcal{A}$ 在以下实验中的成功概率是可忽略的：

1. A random function $H$ is chosen.

   选择一个随机函数 $H$。

2. A succeeds if it outputs distinct $x, x^{\prime}$ with $H(x) = H(x^{\prime})$.

   如果 A 输出不同的 $x, x^{\prime}$ 满足 $H(x) = H(x^{\prime})$，则 A 成功。

To see this, assume without loss of generality that $\mathcal{A}$ only outputs values $x, x^{\prime}$ that it had previously queried to the oracle, and that $\mathcal{A}$ never makes the same query to the oracle twice. Letting the oracle queries of $\mathcal{A}$ be $x_1, \ldots, x_q$, with $q = \mathsf{poly}(n)$, it is clear that the probability that $\mathcal{A}$ succeeds is upper-bounded by the probability that $H(x_i) = H(x_j)$ for some $i \neq j$. But this is exactly equal to the probability that if we pick $q$ strings $y_1, \ldots, y_q \in \{0, 1\}^{\ell_{out}}$ independently and uniformly at random, we have $y_i = y_j$ for some $i \neq j$. This is precisely the birthday problem, and so using the results of Appendix A.4 we see that $\mathcal{A}$ succeeds with negligible probability $\mathcal{O}(q^2/2^{\ell_{out}})$.

为看清这一点，不失一般性地假设 $\mathcal{A}$ 只输出它先前向预言机查询过的值 $x, x^{\prime}$，并且 $\mathcal{A}$ 从不向预言机作相同的查询两次。令 $\mathcal{A}$ 的预言机查询为 $x_1, \ldots, x_q$，其中 $q = \mathsf{poly}(n)$。显然，$\mathcal{A}$ 成功的概率以“存在某个 $i \neq j$ 使得 $H(x_i) = H(x_j)$”的概率为上界。但这恰好等于我们独立且均匀随机地选取 $q$ 个串 $y_1, \ldots, y_q \in \{0, 1\}^{\ell_{out}}$ 时存在某个 $i \neq j$ 使得 $y_i = y_j$ 的概率。这正是生日问题，因此使用附录 A.4 的结果，我们看到 $\mathcal{A}$ 以可忽略的概率 $\mathcal{O}(q^2/2^{\ell_{out}})$ 成功。

Constructing a pseudorandom function from a random oracle. It is also rather easy to construct a pseudorandom function in the random-oracle model. Suppose $\ell_{in}(n) = 2n$ and $\ell_{out}(n) = n$, and define

从随机预言机构造伪随机函数。在随机预言机模型中构造伪随机函数也相当容易。假设 $\ell_{in}(n) = 2n$ 且 $\ell_{out}(n) = n$，定义

$$
F_{k}(x)\stackrel{\mathrm{def}}{=}H(k\|x),
$$

where $|k| = |x| = n$. In Exercise 6.15 you are asked to show that this is a pseudorandom function, namely, for any polynomial-time $\mathcal{A}$ the success probability of $\mathcal{A}$ in the following experiment is ${1}/2 + \mathsf{negl}(n)$:

其中 $|k| = |x| = n$。习题 6.15 要求你证明这是一个伪随机函数，即对任意多项式时间 $\mathcal{A}$，$\mathcal{A}$ 在以下实验中的成功概率为 ${1}/2 + \mathsf{negl}(n)$：

1. A function $H$ and values $k \in \{0,1\}^{n}$ and $b \in \{0,1\}$ are chosen uniformly.

   均匀地选择一个函数 $H$ 以及值 $k \in \{0,1\}^{n}$ 和 $b \in \{0,1\}$。

2. If $b = 0$, the adversary $\mathcal{A}$ is given access to an oracle for $F_k(\cdot) = H(k\|\cdot)$. If $b = 1$, then $\mathcal{A}$ is given access to a random function mapping $n$-bit inputs to $n$-bit outputs. (This random function is independent of $H$)

   如果 $b = 0$，敌手 $\mathcal{A}$ 被赋予对 $F_k(\cdot) = H(k\|\cdot)$ 的预言机访问。如果 $b = 1$，则 $\mathcal{A}$ 被赋予对一个把 $n$ 比特输入映射为 $n$ 比特输出的随机函数的访问。（此随机函数独立于 $H$）

3. A outputs a bit $b^{\prime}$, and succeeds if $b^{\prime} = b$.

   A 输出一个比特 $b^{\prime}$，若 $b^{\prime} = b$ 则成功。

In step 2, A can access H in addition to the function oracle provided to it by the experiment. (A pseudorandom function in the random-oracle model must be indistinguishable from a random function that is independent of $H$.)

在第 2 步中，除了实验提供给它的函数预言机外，$A$ 还可以访问 $H$。（随机预言机模型中的伪随机函数必须与独立于 $H$ 的随机函数不可区分。）

An interesting aspect of the above results is that they require no assumptions; they hold even for computationally unbounded adversaries as long as those adversaries are limited to making polynomially many queries to the oracle. This has no real-world counterpart, where computational assumptions are (currently) necessary to prove, e.g., the existence of pseudorandom generators.

上述结果的一个有趣方面是它们不需要任何假设；只要敌手被限制为向预言机作多项式次查询，它们即使对计算无界的敌手也成立。这在现实世界中没有对应物：在那里，（目前）必须依靠计算假设才能证明例如伪随机生成器的存在性。

### 6.5.2 Is the Random-Oracle Methodology Sound?　6.5.2 随机预言机方法学是否可靠？

Schemes designed in the random-oracle model are implemented in the real world by instantiating H with some concrete function. With the mechanics of the random-oracle model behind us, we turn to a more fundamental question:

在随机预言机模型中设计的方案，在现实世界中是通过用某个具体函数实例化 H 来实现的。在掌握了随机预言机模型的机制之后，我们转到一个更根本的问题：

What do proofs of security in the random-oracle model guarantee as far as security of any real-world instantiation?

随机预言机模型中的安全性证明，对于任何现实世界实例化的安全性而言，能保证什么？

This question does not have a definitive answer: there is currently debate within the cryptographic community about how to interpret proofs in the random-oracle model, and active research seeking to determine what, precisely, a proof of security in the random-oracle model implies vis-a-vis the real world. We can only hope to give a flavor of both sides of the debate.

这个问题没有确定的答案：密码学界内部目前对如何解释随机预言机模型中的证明存在争论，也有活跃的研究试图确定随机预言机模型中的安全性证明究竟对现实世界意味着什么。我们只能期望呈现争论双方观点的大致面貌。

Objections to the random-oracle model. The starting point for arguments against using random oracles is simple: as we have already noted, there is no formal justification for believing that a proof of security for some scheme $\Pi$ in the random-oracle model says anything about the security of $\Pi$ in the real world, once the random oracle $H$ has been instantiated with any particular hash function $\hat{H}$. This is more than just theoretical uneasiness. A little thought shows that no hash function can ever act as a “true” random oracle. For example, in the random-oracle model the value $H(x)$ is “completely random” if $x$ was not explicitly queried. The counterpart would be to require that $\hat{H}(x)$ is random (or pseudorandom) if $\hat{H}$ was not explicitly evaluated on $x$. How are we to interpret this in the real world? It is not even clear what it means to “explicitly evaluate” $\hat{H}$: what if an adversary knows a shortcut for computing $\hat{H}$ that does not involve running the actual code of $\hat{H}$? Moreover, $\hat{H}(x)$ cannot possibly be random (or even pseudorandom) since once the adversary learns the description of $\hat{H}$, the value of $\hat{H}$ on all inputs is immediately determined.

对随机预言机模型的反对。反对使用随机预言机的论证，其出发点很简单：如我们已经指出的，没有任何形式化的依据能让人相信，某个方案 $\Pi$ 在随机预言机模型中的安全性证明，在随机预言机 $H$ 被任何特定哈希函数 $\hat{H}$ 实例化之后，还能对 $\Pi$ 在现实世界中的安全性说明任何东西。这不仅仅是理论上的不安。稍加思考可知，没有任何哈希函数能充当“真正的”随机预言机。例如，在随机预言机模型中，如果 $x$ 未被显式查询，则 $H(x)$ 的值是“完全随机的”。其对应物将是要求如果 $\hat{H}$ 未在 $x$ 上被显式求值，则 $\hat{H}(x)$ 是随机的（或伪随机的）。我们在现实世界中该如何解释这一点？甚至不清楚“显式求值” $\hat{H}$ 是什么意思：如果敌手知道一种不涉及运行 $\hat{H}$ 实际代码的、计算 $\hat{H}$ 的捷径呢？此外，$\hat{H}(x)$ 不可能是随机的（甚至是伪随机的），因为一旦敌手得知 $\hat{H}$ 的描述，$\hat{H}$ 在所有输入上的值就立即确定了。

Limitations of the random-oracle model become clearer once we examine the proof techniques introduced earlier. Recall that one proof technique is to use the fact that a reduction can “see” the queries that an adversary A makes to the random oracle. If we replace the random oracle by a particular hash function $\hat{H}$, this means we must provide a description of $\hat{H}$ to the adversary at the beginning of the experiment. But then A can evaluate $\hat{H}$ on its own, without making any explicit queries, and so a reduction will no longer have the ability to “see” any queries made by A. (In fact, as noted previously, the notion of A performing explicit evaluations of $\hat{H}$ may not be true and certainly cannot be formally defined.) Likewise, proofs of security in the random-oracle model allow the reduction to choose the outputs of H as it wishes, something that is clearly not possible when a concrete function is used.

一旦我们考察前面引入的证明技巧，随机预言机模型的局限性就变得更清晰。回忆一种证明技巧是利用归约能够“看到”敌手 $\mathcal{A}$ 向随机预言机所作的查询这一事实。如果我们用某个特定的哈希函数 $\hat{H}$ 替换随机预言机，这意味着我们必须在实验开始时向敌手提供 $\hat{H}$ 的描述。但这样 $A$ 就可以自行求值 $\hat{H}$，而不作任何显式查询，因此归约将不再有能力“看到” $A$ 所作的任何查询。（事实上，如前所述，$A$ 执行 $\hat{H}$ 的显式求值这一概念可能并不真实，当然也无法形式化定义。）同样地，随机预言机模型中的安全性证明允许归约按其意愿选择 $H$ 的输出，这在使用具体函数时显然是不可能的。

Even if we are willing to overlook the above theoretical concerns, a practical problem is that we do not currently have a very good understanding of what it means for a concrete hash function to be "sufficiently good" at instantiating a random oracle. For concreteness, say we want to instantiate the random oracle using some appropriate modification of SHA-2. (SHA-2 is a cryptographic hash function discussed in Section 7.3.2.) While for some particular scheme $\Pi$ it might be reasonable to assume that $\Pi$ is secure when instantiated using SHA-2, it is much less reasonable to assume that SHA-2 can take the place of a random oracle in every scheme designed in the random-oracle model. Indeed, as we have said earlier, we know that $\text{SHA-2}$ is not a random oracle. And it is not hard to design a scheme that is secure in the random-oracle model, but is insecure when the random oracle is replaced by $\text{SHA-2}$.

即使我们愿意忽略上述理论上的担忧，还有一个实际问题：我们目前并不十分清楚，一个具体哈希函数在实例化随机预言机方面“足够好”究竟意味着什么。为具体起见，假设我们想用 SHA-2 的某种适当修改来实例化随机预言机。（SHA-2 是 7.3.2 节讨论的密码学哈希函数。）虽然对于某个特定方案 $\Pi$，假设它用 SHA-2 实例化时是安全的，或许还算合理；但假设 SHA-2 能在随机预言机模型中设计的每个方案里都取代随机预言机，就远没那么合理了。事实上，如我们前面所说，我们知道 $\text{SHA-2}$ 不是随机预言机。设计一个在随机预言机模型中安全、但在随机预言机被 $\text{SHA-2}$ 替换后不安全的方案并不难。

We emphasize that an assumption of the form "SHA-2 acts like a random oracle" is qualitatively different from assumptions such as "SHA-2 is collision resistant" or "AES is a pseudorandom function." The problem lies partly with the fact that there is no satisfactory definition of what the first statement means, while we do have such definitions for the latter two statements.

我们强调，形如“SHA-2 表现得像随机预言机”的假设，与诸如“SHA-2 是抗碰撞的”或“AES 是伪随机函数”等假设在性质上是不同的。问题部分在于：对第一句话的含义没有令人满意的定义，而对后两句话我们确实有这样的定义。

Because of this, using the random-oracle model to prove security of a scheme is qualitatively different from, e.g., introducing a new cryptographic assumption in order to prove a scheme secure in the standard model. Therefore, proofs of security in the random-oracle model are less satisfying than proofs of security in the standard model.

正因如此，使用随机预言机模型来证明方案的安全性，与例如引入一个新的密码学假设以在标准模型中证明方案安全性，在性质上是不同的。因此，随机预言机模型中的安全性证明不如标准模型中的安全性证明令人满意。

Support for the random-oracle model. Given all the problems with the random-oracle model, why use it at all? More to the point: why has the random-oracle model been so influential in the development of modern cryptography (especially current practical usage of cryptography), and why does it continue to be so widely used? As we will see, the random-oracle model enables the design of substantially more-efficient schemes than those we know how to construct in the standard model. As such, there are few (if any) public-key cryptosystems used today having proofs of security in the standard model, while there are numerous deployed schemes having proofs of security in the random-oracle model. In addition, proofs in the random-oracle model are almost universally recognized as lending confidence to the security of schemes being considered for standardization.

对随机预言机模型的支持。鉴于随机预言机模型的所有问题，为什么还要使用它？更切中要害的是：为什么随机预言机模型在现代密码学（尤其是当前的密码学实际使用）的发展中如此有影响力，为什么它继续被如此广泛地使用？正如我们将看到的，在随机预言机模型中，我们能设计出的方案比目前已知能在标准模型中构造的方案高效得多。因此，当今使用的公钥密码系统几乎没有一个在标准模型中有安全性证明，而在随机预言机模型中有安全性证明的已部署方案却为数众多。此外，随机预言机模型中的证明几乎被普遍认为能为正在考虑标准化的方案的安全性提供信心。

The fundamental reason for this is the belief that:

其根本原因在于如下信念：

A proof of security in the random-oracle model is significantly better than no proof at all.

随机预言机模型中的安全性证明比完全没有证明要好得多。

Although some disagree, we offer the following in support of this assertion:

尽管有些人不同意，我们提出以下内容来支持这一断言：

- A proof of security for a scheme in the random-oracle model indicates that the scheme's design is "sound," in the sense that the only possible attacks on a real-world instantiation of the scheme are those that arise due to a weakness in the hash function used to instantiate the random oracle. Thus, if a "good enough" hash function is used to instantiate the random oracle, we should have confidence in the security of the scheme. Moreover, if a given instantiation of the scheme is successfully attacked, we can simply replace the hash function being used with a "better" one.

  一个方案在随机预言机模型中的安全性证明，表明该方案的设计是“健全的”（sound）：对该方案现实世界实例化的唯一可能攻击，只能源于用于实例化随机预言机的哈希函数的弱点。因此，如果使用“足够好”的哈希函数来实例化随机预言机，我们就应当对该方案的安全性抱有信心。此外，如果该方案的某个给定实例化遭到成功攻击，我们只需把所用的哈希函数换成一个“更好的”。

- Importantly, there have been no successful real-world attacks on schemes proven secure in the random-oracle model, when the random oracle was instantiated properly. (We remark that great care must be taken in instantiating the random oracle, as discussed next; see also Exercise 6.11.) This gives evidence of the usefulness of the random-oracle model in designing practical schemes.

  重要的是，只要随机预言机被恰当地实例化，就还没有任何在随机预言机模型中被证明安全的方案遭到过成功的现实世界攻击。（我们指出，在实例化随机预言机时必须非常小心，如下文所讨论；另见习题 6.11。）这为随机预言机模型在设计实用方案方面的有用性提供了证据。

Nevertheless, the above ultimately represent only intuitive speculation as to the usefulness of proofs in the random-oracle model and—all else being equal—proofs without random oracles are preferable.

尽管如此，上述内容最终只代表对随机预言机模型中证明的有用性的直观推测，并且——在其他条件相同的情况下——不用随机预言机的证明更为可取。

#### Instantiating a Random Oracle　实例化随机预言机

Properly instantiating a random oracle is subtle, and a full discussion is beyond the scope of this book. Here we only alert the reader that using an “off-the-shelf” cryptographic hash function without modification is, generally speaking, not a sound approach. For one thing, many cryptographic hash functions are constructed using the Merkle–Damgård transform (cf. Section 6.2), and can be distinguished easily from a random oracle when variable-length inputs are allowed. (See Exercise 6.11.) Also, in some constructions it is necessary for the output of the random oracle to lie in a certain range, which results in additional complications.

恰当地实例化随机预言机相当微妙，完整的讨论超出本书范围。这里我们只提醒读者，不加修改地使用“现成的”密码学哈希函数通常不是一种可靠的方法。首先，许多密码学哈希函数是使用 Merkle–Damgård 变换构造的（参见 6.2 节），当允许变长输入时，它们很容易与随机预言机区分。（见习题 6.11。）此外，在某些构造中，随机预言机的输出需要位于某个特定范围内，这带来了额外的复杂性。

## 6.6 Additional Applications of Hash Functions　6.6 哈希函数的其他应用

We conclude this chapter with a brief discussion of some additional applications of cryptographic hash functions in cryptography and computer security.

本章最后，我们简要讨论密码学哈希函数在密码学和计算机安全中的若干其他应用。

### 6.6.1 Fingerprinting and Deduplication　6.6.1 指纹与去重

If $H$ is a collision-resistant hash function, the hash (or digest) of a file serves as a unique identifier for that file. (If any other file is found to have the same digest, this implies a collision in $H$.) The hash $H(x)$ of a file $x$ can thus serve as a “fingerprint” for $x$, and one can check whether two files are equal by comparing their digests. This simple idea has many applications.

如果 $H$ 是抗碰撞的哈希函数，则一个文件的哈希（或摘要）可作为该文件的唯一标识符。（如果发现任何其他文件与该文件具有相同摘要，则意味着 $H$ 中存在一个碰撞。）因此，文件 $x$ 的哈希 $H(x)$ 可作为 $x$ 的一个“指纹”，并且可以通过比较两个文件的摘要来检查它们是否相等。这一简单思想有众多应用。

- Virus fingerprinting: Virus scanners identify whether incoming files are potential viruses. Often, this is done not by analyzing the incoming file to determine whether it is malicious, but instead simply by checking whether the file is in a database of previously identified viruses. The observation here is that rather than comparing the file to each virus in the database, it suffices to compare the hash of the file to the hashes (i.e., fingerprints) of known viruses. This can lead to improved efficiency, as well as reduced communication if the database is stored remotely.

  病毒指纹（virus fingerprinting）：病毒扫描器判断传入的文件是否为潜在病毒。通常，这并不是靠分析传入文件、判断其是否恶意来完成的，而只是检查该文件是否在先前已识别病毒的数据库中。这里的要点是：与其把文件与数据库中的每个病毒逐一比较，不如将文件的哈希与已知病毒的哈希（即指纹）进行比较。这可带来效率的提升，以及当数据库远程存储时通信的减少。

- Deduplication: Data deduplication is used to eliminate duplicate copies of data, especially in the context of cloud storage where multiple users rely on a single cloud service to store their data. The key insight is that if multiple users wish to store the same file (e.g., a popular video), then the file only needs to be uploaded and stored once and need not be uploaded and stored separately for each user. Deduplication can be achieved by first having a user upload a hash of the new file they want to store; if a file with this hash is already stored on the server, then the cloud-storage provider can simply add a pointer to the existing file to indicate that this specific user has also stored this file, thus saving both communication and storage. The soundness of this approach follows from collision resistance of the hash function.

  去重（deduplication）：数据去重用于消除重复的数据副本，尤其是在多个用户依赖单一云服务来存储其数据的云存储场景中。关键洞察是：如果多个用户希望存储同一个文件（例如一个热门视频），那么该文件只需被上传和存储一次，而不必为每个用户分别上传和存储。去重可以这样实现：首先让用户上传他们想要存储的新文件的哈希；如果具有此哈希的文件已经存储在服务器上，那么云存储提供商只需添加一个指向现有文件的指针，以表明该特定用户也存储了此文件，从而节省通信和存储。这种方法的合理性源于哈希函数的抗碰撞性。

- Peer-to-peer (P2P) file sharing: In P2P file-sharing systems, servers store different files and can advertise the files they hold by broadcasting the hashes of those files. Those hashes serve as unique identifiers for the files, and allow clients to easily find out which servers host a particular file (identified by its hash).

  对等（P2P）文件共享：在 P2P 文件共享系统中，服务器存储不同的文件，并可通过广播这些文件的哈希来公告自己持有的文件。这些哈希作为文件的唯一标识符，使客户端能够轻松地找出哪些服务器托管了某个特定文件（由其哈希标识）。

It may be surprising that a small digest can uniquely identify every file in the world. But this is the guarantee provided by collision-resistant hash functions, which makes them useful in the above settings.

一个小摘要能唯一标识世界上每个文件，这或许令人惊讶。但抗碰撞哈希函数提供的正是这种保证，这也是它们在上述场景中很有用的原因。

### 6.6.2 Merkle Trees　6.6.2 Merkle 树

Consider a client who uploads a file x to a server. When the client later retrieves x, it wants to make sure the server returns the original, unmodified file. The client could simply store x and check that the retrieved file is equal to x, but that defeats the purpose of using the server in the first place. We are looking for a solution in which the storage of the client is small.

考虑一个客户端把文件 x 上传到服务器。当客户端稍后取回 x 时，它希望确保服务器返回的是原始的、未被修改的文件。客户端可以直接存储 x 并检查取回的文件是否等于 x，但这本身就违背了使用服务器的初衷。我们寻找的是一种客户端存储量很小的解决方案。

A natural solution is to use the “fingerprinting” idea from the previous section. The client locally stores the short digest $h := H(x)$; when the server returns a candidate file $x^{\prime}$ the client need only check that $H(x^{\prime}) \overset{?}{=} h$.

一个自然的解决方案是使用上一节的“指纹”思想。客户端在本地存储短摘要 $h := H(x)$；当服务器返回一个候选文件 $x^{\prime}$ 时，客户端只需检查 $H(x^{\prime}) \overset{?}{=} h$。

What happens if we want to extend this solution to multiple files $x_1, \ldots, x_t$? There are two obvious ways of doing this. One is to simply hash each file individually; the client locally stores the digests $h_1, \ldots, h_t$, and verifies retrieved files as before. This has the disadvantage that the client's storage grows linearly in $t$. Another possibility is to hash all the files together. That is, the client computes $h := H(x_1, \ldots, x_t)$ and stores only a single digest $h$. (We assume the client concatenates the files in an unambiguous manner before hashing, so that from the input to $h$ it is possible to determine the original files. This can be done using standard techniques.) The drawback now is that when the client wants to retrieve and verify the $i$th file $x_i$, it needs to retrieve all the files in order to recompute the digest and check the result.

如果我们想把此解决方案扩展到多个文件 $x_1, \ldots, x_t$，会怎样？有两种显而易见的方式。其一是简单地单独哈希每个文件；客户端在本地存储摘要 $h_1, \ldots, h_t$，并如前验证取回的文件。其缺点是客户端的存储量随 $t$ 线性增长。另一种可能是把所有文件一起哈希。即客户端计算 $h := H(x_1, \ldots, x_t)$ 并只存储一个摘要 $h$。（我们假设客户端在哈希之前以无歧义的方式拼接文件，使得从 $h$ 的输入可以确定原始文件。这可以使用标准技术来完成。）现在的缺点是，当客户端想要取回并验证第 $i$ 个文件 $x_i$ 时，它需要取回所有文件以重新计算摘要并检查结果。

Merkle trees, introduced by Ralph Merkle, give a tradeoff between these extremes. Assume $t$ is a power of two for simplicity. (The idea can be easily extended when this is not the case.) A Merkle tree computed over input values $x_{1},\ldots,x_{t}$ is simply a binary tree of depth $\log t$ in which hashes of the input values are placed at the leaves, and the value at each internal node is the hash of the values of its two children.

Ralph Merkle 引入的 Merkle 树（Merkle tree）给出了这两个极端之间的折中。为简单起见，假设 $t$ 是 2 的幂。（如果不是这种情况，这一想法也很容易推广。）对输入值 $x_{1},\ldots,x_{t}$ 计算出的 Merkle 树，就是一棵深度为 $\log t$ 的二叉树：输入值的哈希放在叶子处，每个内部节点的值是其两个子节点值的哈希。

Referring to Figure 6.5 where t = 8, for example, each leaf i holds the value $h_i = H(x_i)$; the parent of leaves 3 and 4 holds the value $h_{3...4} = H(h_3, h_4)$; and the parent of the right subtree holds the value

例如，参见图 6.5 中 t = 8 的情形，每个叶子 i 持有值 $h_i = H(x_i)$；叶子 3 和 4 的父节点持有值 $h_{3...4} = H(h_3, h_4)$；而右子树的父节点持有值

$$
h_{5\ldots8}=H(h_{5\ldots6},h_{7\ldots8})=H(H(h_{5},h_{6}),H(h_{7},h_{8})).
$$

![Image](https://lsky.jerryxue.top/i/2026/08/22/6a88f9e93f0c9.jpg)

**FIGURE 6.5: A Merkle tree.**

**图 6.5：一棵 Merkle 树。**

Fixing some hash function $H$, we denote by $\mathcal{MT}_{t}$ the function that takes $t$ input values $x_{1},\ldots,x_{t}$, computes the resulting Merkle tree, and outputs the value of the root of the tree. (A keyed hash function yields a keyed function $\mathcal{MT}_{t}$ in the obvious way.) We have:

固定某个哈希函数 $H$，我们用 $\mathcal{MT}_{t}$ 表示这样一个函数：它接受 $t$ 个输入值 $x_{1},\ldots,x_{t}$，计算出相应的 Merkle 树，并输出树根的值。（带密钥的哈希函数以显然的方式产生带密钥的函数 $\mathcal{MT}_{t}$。）我们有：

THEOREM 6.11 If $(\mathsf{Gen}_H, H)$ is collision resistant, then $(\mathsf{Gen}_H, \mathcal{MT}_t)$ is collision resistant for any fixed $t$.

Merkle trees thus provide an alternative to the Merkle–Damgård transform for domain extension of collision-resistant hash functions. (As described, however, Merkle trees are not collision resistant if the number of inputs t is allowed to vary. But they can be generalized fairly easily to handle that case.)

**定理 6.11** 如果 $(\mathsf{Gen}_H, H)$ 是抗碰撞的，那么对任意固定的 $t$，$(\mathsf{Gen}_H, \mathcal{MT}_t)$ 是抗碰撞的。

因此，Merkle 树为抗碰撞哈希函数的域扩展提供了一种 Merkle–Damgård 变换之外的选择。（然而，如所描述的，如果允许输入数目 t 变化，Merkle 树并非抗碰撞的。但它们可以相当容易地推广，以处理那种情形。）

Merkle trees yield an efficient solution to our original problem. Specifically, the client will compute $h := \mathcal{MT}_t(x_1, \ldots, x_t)$, upload $x_1, \ldots, x_t$ to the server, and store $h$ (along with the number of files $t$) locally. When the client wants to retrieve the $i$th file, the server sends $x_i$ along with a “proof” $\pi_i$ that this is the correct value. This proof consists of the values of the nodes in the Merkle tree adjacent to the path from the $i$th leaf to the root. From these values the client can recompute the value of the root and verify that it is equal to the stored value $h$. As an example, consider the Merkle tree in Figure 6.5. The client computes $h_{1\ldots8} := \mathcal{MT}_8(x_1, \ldots, x_8)$, uploads $x_1, \ldots, x_8$ to the server, and stores $h_{1\ldots8}$ locally. When the client retrieves $x_3$, the server sends $x_3$ along with $h_4, h_{1\ldots2}$, and $h_{5\ldots8}$. The client computes $h^{\prime}_3 := H(x_3)$, $h^{\prime}_{3\ldots4} := H(h^{\prime}_3, h_4)$, $h^{\prime}_{1\ldots4} := H(h_{1\ldots2}, h^{\prime}_{3\ldots4})$, and $h^{\prime}_{1\ldots8} := H(h^{\prime}_{1\ldots4}, h_{5\ldots8})$, and then verifies that $h^{\prime}_{1\ldots8} \overset{?}{=} h_{1\ldots8}$. If $H$ is collision resistant and the server tries to send an incorrect file $x^{\prime}_3 \neq x_3$, it will be infeasible for the server to send any proof that will cause verification to succeed. Using this approach, the client's local storage is constant (independent of $t$), and the communication overhead is logarithmic in $t$.

Merkle 树为我们最初的问题给出了一个高效解决方案。具体而言，客户端将计算 $h := \mathcal{MT}_t(x_1, \ldots, x_t)$，把 $x_1, \ldots, x_t$ 上传到服务器，并在本地存储 $h$（连同文件数目 $t$）。当客户端想要取回第 $i$ 个文件时，服务器随 $x_i$ 一起发送一个“证明” $\pi_i$，用来表明 $x_i$ 是正确的值。该证明由 Merkle 树中与从第 $i$ 个叶子到根的路径相邻的节点值组成。根据这些值，客户端可以重新计算根的值并验证它等于所存储的值 $h$。作为例子，考虑图 6.5 中的 Merkle 树。客户端计算 $h_{1\ldots8} := \mathcal{MT}_8(x_1, \ldots, x_8)$，把 $x_1, \ldots, x_8$ 上传到服务器，并在本地存储 $h_{1\ldots8}$。当客户端取回 $x_3$ 时，服务器发送 $x_3$ 以及 $h_4, h_{1\ldots2}$ 和 $h_{5\ldots8}$。客户端计算 $h^{\prime}_3 := H(x_3)$、$h^{\prime}_{3\ldots4} := H(h^{\prime}_3, h_4)$、$h^{\prime}_{1\ldots4} := H(h_{1\ldots2}, h^{\prime}_{3\ldots4})$ 和 $h^{\prime}_{1\ldots8} := H(h^{\prime}_{1\ldots4}, h_{5\ldots8})$，然后验证 $h^{\prime}_{1\ldots8} \overset{?}{=} h_{1\ldots8}$。如果 $H$ 是抗碰撞的且服务器试图发送一个不正确的文件 $x^{\prime}_3 \neq x_3$，那么服务器无法发送任何能使验证成功的证明。使用这种方法，客户端的本地存储是常数（与 $t$ 无关），通信开销是 $t$ 的对数。

### 6.6.3 Password Hashing　6.6.3 口令哈希

One of the most common and important uses of hash functions in computer security is for password protection. Consider a user typing in a password before using their laptop. To authenticate the user, some form of the user's password must be stored somewhere on their laptop. If the user's password is stored in the clear, then an adversary who steals the laptop can read the user's password off the hard drive and then impersonate that user. (It may seem pointless to try to hide one's password from an attacker who can already read the contents of the hard drive. However, files on the hard drive may be encrypted with a key derived from the user's password, and would thus only be accessible after the password is entered. In addition, the user is likely to use the same password for other purposes.)

哈希函数在计算机安全中最常见且最重要的用途之一是口令保护。考虑一个用户在使用其笔记本电脑前输入口令。为认证该用户，必须以某种形式将用户的口令存储在笔记本电脑的某处。如果用户口令以明文存储，那么窃取笔记本电脑的敌手就能从硬盘上读出用户的口令，然后冒充该用户。（在已经能读取硬盘内容的攻击者面前试图隐藏自己的口令，这似乎毫无意义。然而，硬盘上的文件可能用从用户口令派生的密钥加密，因此只有在输入口令后才能访问。此外，用户很可能将同一口令用于其他目的。）

This risk can be mitigated by storing a hash of the password instead of the password itself. That is, the value $hpw = H(pw)$ is stored on the laptop in a password file; later, when the user enters its password pw, the operating system checks whether $H(pw) \overset{?}{=} hpw$ before granting access. The same basic approach is also used for password-based authentication over the web, with a login server holding the password file. Now, if an attacker steals the hard drive (or breaks into the login server), all it obtains is the hash of the password and not the password itself.

这种风险可以通过存储口令的哈希而非口令本身来缓解。即将值 $hpw = H(pw)$ 存储在笔记本电脑的口令文件中；随后，当用户输入其口令 pw 时，操作系统在授予访问权限之前检查是否 $H(pw) \overset{?}{=} hpw$。相同的基本方法也用于基于口令的 Web 认证，由登录服务器持有口令文件。现在，如果攻击者窃取了硬盘（或侵入登录服务器），它所获得的只是口令的哈希而非口令本身。

If the password is chosen from some relatively small space $D$ of possibilities (e.g., $D$ might be a dictionary of English words, in which case $|D| \approx 80,000$), an attacker can enumerate all possible passwords $pw_1, pw_2, \ldots \in D$ and, for each candidate $pw_i$, check whether $H(pw_i) = hpw$. We would like to claim that an attacker can do no better than this. (This would also ensure that the adversary could not learn the password of any user who chose a strong password from a large domain.) Unfortunately, preimage resistance (i.e., one-wayness) of $H$ is not sufficient to imply what we want. For one thing, preimage resistance only says that $H(x)$ is hard to invert when $x$ is chosen uniformly from a large domain. It says nothing about the hardness of inverting $H$ when $x$ is chosen from a small domain, or when $x$ is chosen according to some other distribution. Moreover, preimage resistance says nothing about the concrete amount of time needed to find a preimage. For example, a hash function $H$ for which recovering $x \in \{0,1\}^n$ from $H(x)$ requires time ${2}^{n/2}$ could still qualify as preimage resistant, yet this would mean that a 32-bit uniform password could be recovered in only ${2}^{16}$ time.

如果口令是从一个相对较小的可能空间 $D$ 中选择的（例如 $D$ 可能是一部英语词典，此时 $|D| \approx 80,000$），攻击者可以枚举所有可能的口令 $pw_1, pw_2, \ldots \in D$，并对每个候选 $pw_i$ 检查是否 $H(pw_i) = hpw$。我们希望断言攻击者最多只能做到这样。（这也将确保敌手无法得知任何从大定义域中选择强口令的用户的口令。）不幸的是，$H$ 的原像抗性（即单向性）不足以蕴含我们想要的性质。其一，原像抗性只说明当 $x$ 从大定义域中均匀选择时，$H(x)$ 难以求逆。至于 $x$ 从小定义域中选择、或按某种其他分布选择时求逆 $H$ 的难度，它只字未提。此外，原像抗性对找到原像所需的具体时间量只字未提。例如，一个从 $H(x)$ 恢复 $x \in \{0,1\}^n$ 需要 ${2}^{n/2}$ 时间的哈希函数 $H$ 仍可能符合原像抗性，但这将意味着一个 32 比特的均匀口令只需 ${2}^{16}$ 时间即可被恢复。

If we model $H$ as a random oracle, though, we can formally prove the security we want: namely, recovering $pw$ from $hpw$ (assuming $pw$ is chosen uniformly from $D$) requires $\mathcal{O}(|D|)$ evaluations of $H$, on average.

然而，如果我们将 $H$ 建模为随机预言机，我们就可以形式化地证明我们想要的安全性：即从 $hpw$ 恢复 $pw$（假设 $pw$ 从 $D$ 中均匀选择）平均需要 $\mathcal{O}(|D|)$ 次 $H$ 求值。

The above discussion assumes no preprocessing is done by the attacker. As we have seen in Section 6.4.3, though, preprocessing can be used to generate large tables that enable inversion (even of a random function!) faster than exhaustive search. The tables—called rainbow tables—only need to be generated once, and can be used to recover thousands of passwords in case of a server breach. This is a significant concern in practice: even if a user chooses their password as a random combination of 8 alphanumeric English characters—giving a password space of size $N = 62^8 \approx 2^{47.6}$—there is an attack using time and space $N^{2/3} \approx 2^{32}$ that will be highly effective at recovering the password. Such attacks are routinely carried out in practice.

上述讨论假设攻击者未做任何预处理。然而，正如我们在 6.4.3 节所见，预处理可用于生成大表，使求逆（即使是对随机函数求逆！）能比穷举搜索更快。这些表——称为彩虹表（rainbow table）——只需生成一次，并可在服务器被入侵的情况下用于恢复成千上万个口令。这在实践中是一个重大隐患：即使用户选择其口令为 8 个英文字母数字字符的随机组合——给出大小为 $N = 62^8 \approx {2}^{47.6}$ 的口令空间——也存在使用时间和空间 $N^{2/3} \approx {2}^{32}$ 的攻击，该攻击在恢复口令方面将非常有效。此类攻击在实践中经常被实施。

Mitigation. We briefly describe two mechanisms used to mitigate the threat of password cracking. One technique is to use hash functions that are “moderately hard to compute,” in the sense that they do not add significant overhead when evaluated once (as done by the server when authenticating a user) but are prohibitively expensive to evaluate tens of thousands of times (as would be done by a user in a brute-force attack).

缓解。我们简要描述两种用于缓解口令破解威胁的机制。一种技术是使用“适度难以计算”的哈希函数，其意义在于：当只求值一次（如服务器在认证用户时所做）时它不增加显著开销，但求值成千上万次（如用户在蛮力攻击中所做）则代价高得令人望而却步。

A second mechanism is to introduce a salt. When a user registers their password, the laptop/server will generate a long random value $s$ (a “salt”) unique to that user, and store $(s, hpw = H(s, pw))$ instead of merely storing $H(pw)$ as before. Since $s$ is unknown to the attacker in advance, preprocessing is ineffective and the best an attacker can do is to wait until it obtains the password file and then do a linear-time exhaustive search over the domain $D$. Note also that since a different salt is used for each user, a separate brute-force search is needed to recover each user's password.

第二种机制是引入盐值（salt）。当用户注册其口令时，笔记本电脑/服务器将生成一个对该用户唯一的长随机值 $s$（一个“盐值”），并存储 $(s, hpw = H(s, pw))$ 而非像以前那样只存储 $H(pw)$。由于 $s$ 对攻击者而言事先未知，预处理是无效的，攻击者最多只能等到获得口令文件后对定义域 $D$ 进行线性时间的穷举搜索。还要注意，由于每个用户使用不同的盐值，恢复每个用户的口令都需要单独的蛮力搜索。

### 6.6.4 Key Derivation　6.6.4 密钥派生

Symmetric-key cryptosystems require the secret key to be a uniformly distributed bit-string. Often, however, it is more convenient for two parties to rely on shared information such as a password or biometric data that is not uniformly distributed. (Jumping ahead, in Chapter 11 we will see how parties can interact over a public channel to generate a high-entropy shared secret that is also not necessarily uniformly distributed.) The parties could try to use their nonuniform shared information directly as a secret key, but in general this will not be secure. Moreover, the shared data may not even have the correct format to be used as a secret key (it may be too long, for example).

对称密钥密码系统要求秘密密钥是均匀分布的比特串。然而，对两方来说，依赖诸如口令或生物特征数据这类并非均匀分布的共享信息，往往更方便。（展望第 11 章，我们将看到各方如何通过公开信道交互来生成一个高熵的、但也未必均匀分布的共享秘密。）各方可以尝试直接将其非均匀的共享信息用作秘密密钥，但一般情况下这是不安全的。此外，共享数据甚至可能没有用作秘密密钥的正确格式（例如，它可能太长）。

Truncating the shared secret, or mapping it in some other heuristic way to a string of the correct length, may lose a significant amount of entropy. (We define one notion of entropy more formally below, but for now one can think of entropy as the logarithm of the number of possible shared secrets.) For example, imagine two parties share a password composed of 28 random upper-case English letters, and want to use a cryptosystem with a 128-bit key. Since there are 26 possibilities for each character, there are ${26}^{28} > 2^{130}$ possible passwords. If the password is shared in ASCII format, each character is stored using 8 bits, and so the total length of the password is 224 bits. If the parties truncate their password to the first 128 bits, they will be using only the first 16 characters of their password. Even worse, this will not be a uniformly distributed 128-bit string! The ASCII representations of the letters A–Z lie between 0x41 and 0x5A; in particular, the first 3 bits of every byte are always 010. This means that 37.5% of the bits of the resulting key will be fixed, and the 128-bit key the parties derive will have only about 75 bits of entropy (i.e., there are only ${2}^{75}$ or so possibilities for the key).

截断共享秘密，或以某种其他启发式方式将其映射为正确长度的串，可能丢失大量的熵。（我们在下面更形式化地定义一种熵的概念，但现在可以把熵看作可能共享秘密数目的对数。）例如，设想两方共享一个由 28 个随机大写英文字母组成的口令，并想使用一个 128 比特密钥的密码系统。由于每个字符有 26 种可能，共有 ${26}^{28} > {2}^{130}$ 个可能的口令。如果口令以 ASCII 格式共享，每个字符用 8 比特存储，因此口令总长度为 224 比特。如果各方将其口令截断为前 128 比特，它们将只使用口令的前 16 个字符。更糟的是，这将不是一个均匀分布的 128 比特串！字母 A–Z 的 ASCII 表示介于 0x41 和 0x5A 之间；特别地，每个字节的前 3 个比特总是 010。这意味着所得密钥中 37.5% 的比特将是固定的，各方派生出的 128 比特密钥将只有大约 75 比特的熵（即密钥只有大约 ${2}^{75}$ 种可能）。

What we need is a generic solution for deriving a key of some desired length from a high-entropy (but not necessarily uniform) shared secret. Before continuing, we define the notion of entropy we consider here.

我们需要的是一种通用解决方案，用于从高熵（但不一定均匀）的共享秘密中派生出某个所需长度的密钥。在继续之前，我们定义此处考虑的熵的概念。

DEFINITION 6.12 A probability distribution $\mathcal{X}$ has $m$ bits of min-entropy if for every fixed value $x$ it holds that $\Pr_{X\leftarrow\mathcal{X}}[X=x]\leq2^{-m}$. In other words, even the most likely outcome occurs with probability at most ${2}^{-m}$.

The uniform distribution over a set of size $S$ has min-entropy $\log S$. A distribution in which one element occurs with probability ${1}/10$ and 90 elements each occur with probability ${1}/100$ has min-entropy $\log 10 \approx 3.3$. The min-entropy of a distribution measures the probability with which an attacker can guess a value sampled from that distribution; the attacker's best strategy is to guess the most likely value, and so if the distribution has min-entropy $m$ the attacker's guess is correct with probability at most ${2}^{-m}$. This explains why min-entropy (rather than other notions of entropy) is useful in our context.

**定义 6.12** 一个概率分布 $\mathcal{X}$ 具有 $m$ 比特的最小熵（min-entropy），如果对每个固定值 $x$ 都有 $\Pr_{X\leftarrow\mathcal{X}}[X=x]\leq2^{-m}$。换言之，即使最可能的结果其发生概率也至多为 ${2}^{-m}$。

大小为 $S$ 的集合上的均匀分布具有最小熵 $\log S$。一个元素以概率 ${1}/10$ 出现、90 个元素各以概率 ${1}/100$ 出现的分布具有最小熵 $\log 10 \approx 3.3$。分布的最小熵度量攻击者能以多大概率猜中从该分布中采样的值；攻击者的最佳策略是猜测最可能的值，因此如果分布具有最小熵 $m$，则攻击者猜中的概率至多为 ${2}^{-m}$。这解释了为什么在我们的语境中最小熵（而非其他熵的概念）是有用的。

A key-derivation function provides a way to obtain a (close to) uniformly distributed string from any distribution with high min-entropy. It is not hard to see that if we model a hash function $H$ as a random oracle, then $H$ serves as a good key-derivation function. (As a technical point, we require the original distribution to be independent of $H$. This will normally be the case in practice.) Consider an attacker's uncertainty about $H(X)$, where $X$ is sampled from a distribution with min-entropy $m$. Each of the attacker's queries to $H$ can be viewed as a “guess” for the value of $X$; by assumption on the min-entropy of the distribution, an attacker making $q$ queries to $H$ will query $H(X)$ with probability at most $q \cdot 2^{-m}$. As long as the attacker does not query $H(X)$, the value $H(X)$ is uniform from the attacker's point of view.

密钥派生函数提供了一种从任意具有高最小熵的分布中获得（接近）均匀分布的串的方法。不难看出，如果我们把哈希函数 $H$ 建模为随机预言机，那么 $H$ 就是一个好的密钥派生函数。（作为一个技术点，我们要求原始分布独立于 $H$。这在实践中通常是成立的。）考虑攻击者对 $H(X)$ 的不确定性，其中 $X$ 采样自具有最小熵 $m$ 的分布。攻击者对 $H$ 的每次查询都可视为对 $X$ 值的一次“猜测”；根据对分布最小熵的假设，作 $q$ 次查询的攻击者将以至多 $q \cdot 2^{-m}$ 的概率查询到 $H(X)$。只要攻击者不查询 $H(X)$，值 $H(X)$ 从攻击者的角度看就是均匀的。

It is also possible to design key-derivation functions without relying on the random-oracle model, by using keyed hash functions called (strong) extractors. The key for the extractor must be uniform, but need not be kept secret.

也可以在不依赖随机预言机模型的情况下设计密钥派生函数，方法是使用称为（强）提取器的带密钥哈希函数。提取器的密钥必须是均匀的，但不必保密。

### 6.6.5 Commitment Schemes　6.6.5 承诺方案

A commitment scheme allows one party to “commit” to a value m by sending a commitment com, and then to reveal m (by “opening” the commitment) at a later point in time. We require the following properties to hold:

承诺方案（commitment scheme）允许一方通过发送一个承诺 $\mathsf{com}$ 来“承诺”一个值 $m$，然后在稍后的时刻通过“打开”承诺来揭示 $m$。我们要求以下性质成立：

- Hiding: the commitment com reveals nothing about m.

  隐藏（hiding）：承诺 $\mathsf{com}$ 不透露关于 $m$ 的任何信息。

- Binding: it is infeasible for the committer to output a commitment com that it can later “open” as two different messages $m, m^{\prime}$. (In this sense, com truly “commits” the committer to at most one value.)

  绑定（binding）：承诺者难以输出一个承诺 $\mathsf{com}$，使得它后来能被“打开”为两个不同的消息 $m, m^{\prime}$。（在这个意义上，$\mathsf{com}$ 真正把承诺者“绑定”到至多一个值。）

A commitment scheme can be viewed as a digital envelope: sealing a message m in an envelope and giving the envelope to another party hides m (until the envelope is opened) even though the value of m is fixed (since the contents of the envelope cannot be changed).

承诺方案可被视为一个数字信封：把消息 $m$ 封在信封里并把信封交给另一方，即可隐藏 $m$（直到信封被打开），尽管 $m$ 的值是固定的（因为信封的内容不能被更改）。

Formally, a (non-interactive) commitment scheme is defined by an algorithm $\mathsf{Gen}$ that outputs public parameters $\text{params}$, and a randomized algorithm $\mathsf{Com}$ that takes $\text{params}$ and a message $m \in \{0,1\}^n$ and outputs a commitment $\text{com}$; when we make the randomness used by $\mathsf{Com}$ explicit, we denote it by $r$. A sender commits to m by choosing uniform r, computing $\text{com} := \mathsf{Com}(\text{params}, m; r)$, and sending it to a receiver. The sender can later open com and reveal m by sending m, r to the receiver; the receiver verifies that m is the committed value by checking that $\mathsf{Com}(\text{params}, m; r) \overset{?}{=} \text{com}$.

形式化地，一个（非交互式）承诺方案由两个算法定义：算法 $\mathsf{Gen}$ 输出公开参数 $\text{params}$；随机化算法 $\mathsf{Com}$ 接受 $\text{params}$ 和消息 $m \in \{0,1\}^n$ 并输出承诺 $\text{com}$。当我们把 $\mathsf{Com}$ 使用的随机性显式写出时，将其记为 $r$。发送者通过选择均匀的 r、计算 $\text{com} := \mathsf{Com}(\text{params}, m; r)$ 并将其发送给接收者来承诺 m。发送者稍后可以通过向接收者发送 m, r 来打开 com 并揭示 m；接收者通过检查 $\mathsf{Com}(\text{params}, m; r) \overset{?}{=} \text{com}$ 来验证 m 是所承诺的值。

Hiding means that com reveals nothing about m. This is defined via the following experiment.

隐藏意味着 com 不透露关于 m 的任何信息。这通过以下实验来定义。

#### The commitment hiding experiment $\mathsf{Hiding}_{\mathcal{A},\mathsf{Com}}(n):$

1. Parameters $\text{params} \leftarrow \mathsf{Gen}(1^{n})$ are generated.

2. The adversary $\mathcal{A}$ is given input $\text{params}$, and outputs a pair of messages $m_0, m_1 \in \{0,1\}^n$.

3. A uniform $b \in \{0,1\}$ is chosen and $\text{com} \leftarrow \mathsf{Com}(\text{params}, m_b)$ is computed.

4. The adversary $\mathcal{A}$ is given $\text{com}$ and outputs a bit $b^{\prime}$.

5. The output of the experiment is 1 if and only if $b^{\prime} = b$.

#### 承诺隐藏实验 $\mathsf{Hiding}_{\mathcal{A},\mathsf{Com}}(n)$：

1. 生成参数 $\text{params} \leftarrow \mathsf{Gen}(1^{n})$。

2. 敌手 $\mathcal{A}$ 获得输入 $\text{params}$，并输出一对消息 $m_0, m_1 \in \{0,1\}^n$。

3. 选择一个均匀的 $b \in \{0,1\}$，计算 $\text{com} \leftarrow \mathsf{Com}(\text{params}, m_b)$。

4. 敌手 $\mathcal{A}$ 获得 $\text{com}$ 并输出一个比特 $b^{\prime}$。

5. 当且仅当 $b^{\prime} = b$ 时，实验输出为 1。

Binding means that it is impossible to output a commitment com that can be opened in two different ways.

绑定意味着不可能输出一个能以两种不同方式打开的承诺 $\mathsf{com}$。

#### The commitment binding experiment $\mathsf{Binding}_{\mathcal{A},\mathsf{Com}}(n):$

1. Parameters $\text{params} \leftarrow \mathsf{Gen}(1^{n})$ are generated.

2. $\mathcal{A}$ is given input $\text{params}$ and outputs $(\text{com}, m, r, m^{\prime}, r^{\prime})$.

3. The output of the experiment is defined to be 1 if and only if $m \neq m^{\prime}$ and $\mathsf{Com}(\text{params}, m; r) = \text{com} = \mathsf{Com}(\text{params}, m^{\prime}; r^{\prime})$.

#### 承诺绑定实验 $\mathsf{Binding}_{\mathcal{A},\mathsf{Com}}(n)$：

1. 生成参数 $\text{params} \leftarrow \mathsf{Gen}(1^{n})$。

2. $\mathcal{A}$ 获得输入 $\text{params}$ 并输出 $(\text{com}, m, r, m^{\prime}, r^{\prime})$。

3. 当且仅当 $m \neq m^{\prime}$ 且 $\mathsf{Com}(\text{params}, m; r) = \text{com} = \mathsf{Com}(\text{params}, m^{\prime}; r^{\prime})$ 时，实验的输出定义为 1。

DEFINITION 6.13 A commitment scheme Com is secure if for all PPT adversaries A there is a negligible function $\mathsf{negl}$ such that

$$
\Pr\left[\mathsf{Hiding}_{\mathcal{A},\mathsf{Com}}(n)=1\right]\leq\frac{1}{2}+\mathsf{negl}(n)
$$

and

$$
\Pr\left[\mathsf{Binding}_{\mathcal{A},\mathsf{Com}}(n)=1\right]\leq\mathsf{negl}(n).
$$

**定义 6.13** 承诺方案 Com 是安全的，如果对所有 PPT 敌手 A，存在一个可忽略函数 $\mathsf{negl}$ 使得

$$
\Pr\left[\mathsf{Hiding}_{\mathcal{A},\mathsf{Com}}(n)=1\right]\leq\frac{1}{2}+\mathsf{negl}(n)
$$

且

$$
\Pr\left[\mathsf{Binding}_{\mathcal{A},\mathsf{Com}}(n)=1\right]\leq\mathsf{negl}(n).
$$

It is easy to construct a secure commitment scheme from a random oracle $H$. To commit to a message $m$, the sender chooses uniform $r \in \{0,1\}^n$ and outputs $\text{com} := H(m\|r)$. (In the random-oracle model, $\mathsf{Gen}$ and $\text{params}$ are not needed since $H$, in effect, serves as the public parameters of the scheme.) Binding follows immediately from the fact that $H$ is collision resistant. Intuitively, hiding follows from the fact that an adversary queries $H(\star\|r)$ with only negligible probability (since $r$ is a uniform $n$-bit string); if it never makes a query of this form then $\text{com} = H(m\|r)$ reveals nothing about $m$.

从随机预言机 $H$ 构造一个安全的承诺方案很容易。为承诺一个消息 $m$，发送者选择均匀的 $r \in \{0,1\}^n$ 并输出 $\text{com} := H(m\|r)$。（在随机预言机模型中，$\mathsf{Gen}$ 和 $\text{params}$ 是不需要的，因为 $H$ 实际上充当该方案的公开参数。）绑定性质是 $H$ 抗碰撞的直接推论。直观上，隐藏由如下事实得出：敌手以可忽略的概率查询 $H(\star\|r)$（因为 $r$ 是一个均匀的 $n$ 比特串）；如果它从不作这种形式的查询，则 $\text{com} = H(m\|r)$ 不透露关于 $m$ 的任何信息。

Commitment schemes can be constructed without random oracles (in fact, from one-way functions), but the details are beyond the scope of this book.

承诺方案可以不用随机预言机构造（事实上，可从单向函数构造），但细节超出本书范围。

### References and Additional Reading　参考文献与延伸阅读

Collision-resistant hash functions were formally defined by Damgård [60]. As we have noted, other notions of security for hash functions can also be considered [137, 173]. The Merkle–Damgård transform was introduced independently by Merkle [140] and Damgård [61].

抗碰撞哈希函数由 Damgård [60] 形式化定义。如我们所指出的，哈希函数的其他安全性概念也可被考虑 [137, 173]。Merkle–Damgård 变换由 Merkle [140] 和 Damgård [61] 独立引入。

The hash-and-MAC paradigm is folklore. HMAC was introduced and analyzed by Bellare et al. [16], and subsequently standardized [149].

哈希后认证范式源自民间流传的实践（folklore）。HMAC 由 Bellare 等人 [16] 引入并分析，随后被标准化 [149]。

The small-space birthday attack described in Section 6.4.2 relies on a cycle-finding algorithm of Floyd. Related algorithms and results are described at http://en.wikipedia.org/wiki/Cycle_detection. The idea for finding meaningful collisions using the small-space attack is by Yuval [206]. The possibility of parallelizing collision-finding attacks, which can offer significant speedups in practice, is discussed in detail by van Oorschot and Wiener [198]. Time/space tradeoffs for function inversion were introduced by Hellman [95], with practical improvements—not discussed here—given by Rivest (unpublished) and Oechslin [155] (who coined the term “rainbow tables”).

6.4.2 节描述的小空间生日攻击依赖于 Floyd 的一个环检测算法。相关算法和结果在 http://en.wikipedia.org/wiki/Cycle_detection 中有所描述。使用小空间攻击寻找有意义碰撞的思想归功于 Yuval [206]。van Oorschot 和 Wiener [198] 详细讨论了并行化碰撞寻找攻击的可能性，这在实践中能提供显著的加速。函数求逆的时间/空间折中由 Hellman [95] 引入，Rivest（未发表）和 Oechslin [155]（他创造了“彩虹表”一词）给出了此处未讨论的实际改进。

The first formal treatment of the random-oracle model was given by Bellare and Rogaway [24], although the idea of using a “random-looking” function in cryptographic applications had been suggested previously, most notably by Fiat and Shamir [72]. Proper instantiation of a random oracle from cryptographic hash functions is considered in several papers [24, 25, 26, 56]. The seminal negative result concerning the random-oracle model is that of Canetti et al. [47], who show (contrived) schemes that are secure in the random-oracle model but are insecure for any concrete instantiation of the random oracle.

随机预言机模型的首次形式化处理由 Bellare 和 Rogaway [24] 给出，尽管在密码学应用中使用“看起来随机”的函数的思想先前已被提出，最著名的是 Fiat 和 Shamir [72]。若干论文 [24, 25, 26, 56] 考虑了从密码学哈希函数适当实例化随机预言机。关于随机预言机模型的开创性负面结果是 Canetti 等人 [47] 的，他们展示了（人为设计的）方案，这些方案在随机预言机模型中是安全的，但对随机预言机的任何具体实例化都是不安全的。

Merkle trees go back at least to the 1980s [138]. Designing hash functions to make password cracking difficult is an active area of research; some popular examples of such hash functions include bcrypt and scrypt. A formal treatment of key derivation is given by Krawczyk [123]. Standardized key-derivation functions include HKDF and PBKDF2.

Merkle 树至少可追溯到 20 世纪 80 年代 [138]。设计使口令破解困难的哈希函数是一个活跃的研究领域；此类哈希函数的一些流行示例包括 bcrypt 和 scrypt。Krawczyk [123] 给出了密钥派生的形式化处理。标准化的密钥派生函数包括 HKDF 和 PBKDF2。

### Exercises　习题

6.1 Provide formal definitions for second-preimage resistance and preimage resistance. Then:

6.1 给出第二原像抗性和原像抗性的形式化定义。然后：

(a) Prove that any hash function that is collision resistant is second-preimage resistant.

(b) Prove that if a compression function mapping 2n-bit inputs to n-bit outputs is second-preimage resistant then it is preimage resistant.

(a) 证明任何抗碰撞的哈希函数都是第二原像抗性的。

(b) 证明如果将 2n 比特输入映射到 n 比特输出的压缩函数是第二原像抗性的，那么它是原像抗性的。

6.2 Let $(\mathrm{Gen}_1, H_1)$ and $(\mathrm{Gen}_2, H_2)$ be two hash functions. Define $(\mathrm{Gen}, H)$ so that $\mathrm{Gen}$ runs $\mathrm{Gen}_1$ and $\mathrm{Gen}_2$ to obtain keys $s_1$ and $s_2$, respectively. Then define $H^{s_1, s_2}(x) = H_1^{s_1}(x)\|H_2^{s_2}(x)$.

6.2 设 $(\mathrm{Gen}_1, H_1)$ 和 $(\mathrm{Gen}_2, H_2)$ 是两个哈希函数。定义 $(\mathrm{Gen}, H)$ 使得 $\mathrm{Gen}$ 分别运行 $\mathrm{Gen}_1$ 和 $\mathrm{Gen}_2$ 得到密钥 $s_1$ 和 $s_2$。然后定义 $H^{s_1, s_2}(x) = H_1^{s_1}(x)\|H_2^{s_2}(x)$。

(a) Prove that if at least one of $(\mathrm{Gen}_{1}, H_{1})$ and $(\mathrm{Gen}_{2}, H_{2})$ is collision resistant, then $(\mathrm{Gen}, H)$ is collision resistant.

(b) Determine whether an analogous claim holds for second-preimage resistance and preimage resistance, respectively. Prove your answer in each case.

(a) 证明如果 $(\mathrm{Gen}_{1}, H_{1})$ 和 $(\mathrm{Gen}_{2}, H_{2})$ 中至少有一个是抗碰撞的，那么 $(\mathrm{Gen}, H)$ 是抗碰撞的。

(b) 分别确定类似的结论对第二原像抗性和原像抗性是否成立。在每种情况下证明你的答案。

6.3 Let $(\mathrm{Gen}, H)$ be a collision-resistant hash function. Is $(\mathrm{Gen}, \hat{H})$ defined by $\hat{H}^{s}(x) \stackrel{\mathrm{def}}{=} H^{s}(H^{s}(x))$ necessarily collision resistant?

6.3 设 $(\mathrm{Gen}, H)$ 是抗碰撞哈希函数。由 $\hat{H}^{s}(x) \stackrel{\mathrm{def}}{=} H^{s}(H^{s}(x))$ 定义的 $(\mathrm{Gen}, \hat{H})$ 一定是抗碰撞的吗？

6.4 Provide a formal proof of Theorem 6.4 (i.e., describe the reduction).

6.4 给出定理 6.4 的形式化证明（即描述归约）。

6.5 Generalize the Merkle–Damgård transform to the case where (Gen, h) takes inputs of length $n + 1$ and generates outputs of length $n$. (The hash function you construct should accept inputs of any length $L < 2^n$.) Prove that your transform yields a collision-resistant hash function for arbitrary-length inputs if (Gen, h) is collision resistant.

6.5 将 Merkle–Damgård 变换推广到 (Gen, h) 接受长度为 $n + 1$ 的输入并生成长度为 $n$ 的输出的情形。（你构造的哈希函数应接受任意长度 $L < 2^n$ 的输入。）证明如果 (Gen, h) 是抗碰撞的，则你的变换对任意长度输入产生抗碰撞哈希函数。

6.6 Consider the following modification of the Merkle–Damgård transform:

6.6 考虑 Merkle–Damgård 变换的如下修改：

append a 1 to the input x, followed by enough zeros so that the length of the resulting string is n more than a multiple of $n^{\prime}$. Parse the resulting string as $z_0, x_1, \ldots, x_B$, where $|z_0| = n$ and $|x_i| = n^{\prime}$. Then for $i = 1, \ldots, B$, compute $z_i := h^s(z_{i-1} \| x_i)$; output $z_B$.

向输入 $x$ 追加一个 1，随后追加足够多的零，使得所得串的长度比 $n^{\prime}$ 的整数倍多 n。将所得串解析为 $z_0, x_1, \ldots, x_B$，其中 $|z_0| = n$ 且 $|x_i| = n^{\prime}$。然后对 $i = 1, \ldots, B$，计算 $z_i := h^s(z_{i-1} \| x_i)$；输出 $z_B$。

Show how to find a collision in the resulting hash function when this transform is applied to any compression function (Gen, h).

证明当此变换应用于任意压缩函数 (Gen, h) 时，如何在所得哈希函数中找到一个碰撞。

6.7 Consider the following modification of the Merkle–Damgård transform:

6.7 考虑 Merkle–Damgård 变换的如下修改：

append a 1 to the input x, followed by enough zeros so that the length of the resulting string is a multiple of $n^{\prime}$. Parse the resulting string as the sequence of $n^{\prime}$-bit blocks $x_1, \ldots, x_B$. Set $z_0 := 0^n$. Then for $i = 1, \ldots, B$, compute $z_i := h^s(z_{i-1} \| x_i)$; output $z_B$. Assuming collision-resistant compression functions exist, show that there exists a collision-resistant compression function ( $\mathsf{Gen}, h$) such that this modified transform applied to ( $\mathsf{Gen}, h$) is not collision resistant.

向输入 $x$ 追加一个 1，随后追加足够多的零，使得所得串的长度是 $n^{\prime}$ 的整数倍。将所得串解析为 $n^{\prime}$ 比特块序列 $x_1, \ldots, x_B$。置 $z_0 := 0^n$。然后对 $i = 1, \ldots, B$，计算 $z_i := h^s(z_{i-1} \| x_i)$；输出 $z_B$。假设抗碰撞压缩函数存在，证明存在一个抗碰撞压缩函数 ( $\mathsf{Gen}, h$) 使得此修改后的变换应用于 ( $\mathsf{Gen}, h$) 时不抗碰撞。

Hint: Let h be such that $h^{s}(0^{n}, 0^{n^{\prime}}) = 0^{n}$ for all s.

提示：令 h 满足对所有 s 有 $h^{s}(0^{n}, 0^{n^{\prime}}) = 0^{n}$。

6.8 Assume collision-resistant hash functions exist. Show a construction of a fixed-length hash function (Gen, h) that is not collision resistant, but such that the hash function (Gen, H) obtained from applying the Merkle–Damgård transform to (Gen, h) is collision resistant.

6.8 假设抗碰撞哈希函数存在。给出一个固定长度哈希函数 (Gen, h) 的构造，它不是抗碰撞的，但对其应用 Merkle–Damgård 变换得到的哈希函数 (Gen, H) 是抗碰撞的。

6.9 Prove or disprove: if (Gen, h) is preimage resistant, then so is the hash function (Gen, H) obtained by applying the Merkle–Damgård transform to (Gen, h).

6.9 证明或反驳：如果 (Gen, h) 是原像抗性的，那么对其应用 Merkle–Damgård 变换得到的哈希函数 (Gen, H) 也是原像抗性的。

6.10 Prove or disprove: if (Gen, h) is second-preimage resistant, then so is the hash function (Gen, H) obtained by applying the Merkle–Damgård transform to (Gen, h).

6.10 证明或反驳：如果 (Gen, h) 是第二原像抗性的，那么对其应用 Merkle–Damgård 变换得到的哈希函数 (Gen, H) 也是第二原像抗性的。

6.11 Before HMAC, it was common to define a MAC for arbitrary-length messages by $\mathsf{Mac}_k(m) = H(k\|m)$ where $H$ is a collision-resistant hash function.

6.11 在 HMAC 之前，通常通过 $\mathsf{Mac}_k(m) = H(k\|m)$ 来定义用于任意长度消息的 MAC，其中 $H$ 是抗碰撞哈希函数。

(a) Prove that this is a secure MAC if H is modeled as a random oracle.

(b) Show that this is not a secure MAC when $H$ is constructed via the Merkle–Damgård transform. (Assume $k \in \{0,1\}^n$.)

(a) 证明如果 H 被建模为随机预言机，则这是一个安全的 MAC。

(b) 证明当 $H$ 通过 Merkle–Damgård 变换构造时，这不是一个安全的 MAC。（假设 $k \in \{0,1\}^n$。）

6.12 A student has 3,500 songs on her phone, and chooses songs to play at random. How many songs should the student expect to play before hearing some song twice (with probability at least 50%)?

6.12 一个学生的手机里有 3500 首歌，并随机选择播放。该学生预计要播放多少首歌，才能以至少 50% 的概率听到某首歌两次？

6.13 Sample uniform $y_1, \ldots, y_q \in \{0,1\}^{\ell}$ and $y^{\prime}_1, \ldots, y^{\prime}_q \in \{0,1\}^{\ell}$. What is the probability that there exist $i,j$ such that $y_i = y^{\prime}_j$?

6.13 均匀采样 $y_1, \ldots, y_q \in \{0,1\}^{\ell}$ 和 $y^{\prime}_1, \ldots, y^{\prime}_q \in \{0,1\}^{\ell}$。存在 $i,j$ 使得 $y_i = y^{\prime}_j$ 的概率是多少？

6.14 Fix $H: \{0,1\}^n \to \{0,1\}^{2n}$, and define the keyed function $F: \{0,1\}^n \times \{0,1\}^n \to \{0,1\}^{2n}$ by $F_k(x) = H(k \oplus x)$. Show that an attacker given oracle access to $F_k(\cdot)$ can recover the $n$-bit key $k$ with constant probability in time $\approx 2^{n/2}$ (which is better than a brute-force attack).

6.14 固定 $H: \{0,1\}^n \to \{0,1\}^{2n}$，并由 $F_k(x) = H(k \oplus x)$ 定义带密钥函数 $F: \{0,1\}^n \times \{0,1\}^n \to \{0,1\}^{2n}$。证明一个能访问 $F_k(\cdot)$ 预言机的攻击者能在 $\approx 2^{n/2}$ 时间内以常数概率恢复出 $n$ 比特密钥 $k$（这优于蛮力攻击）。

Hint: Use the previous exercise.

提示：使用前一习题。

6.15 Prove that the keyed function $F$ given in Section 6.5.1 is a pseudorandom function if $H$ is modeled as a random oracle.

6.15 证明如果 $H$ 被建模为随机预言机，则 6.5.1 节给出的带密钥函数 $F$ 是伪随机函数。

6.16 Prove Theorem 6.11.

6.16 证明定理 6.11。

6.17 Show how to find a collision in the Merkle tree construction if $t$ is not fixed. Specifically, show how to find two sets of inputs $x_1, \ldots, x_t$ and $x^{\prime}_1, \ldots, x^{\prime}_{2t}$ such that $\mathcal{MT}_t(x_1, \ldots, x_t) = \mathcal{MT}_{2t}(x^{\prime}_1, \ldots, x^{\prime}_{2t})$.

6.17 证明如果 $t$ 不固定，如何在 Merkle 树构造中找到碰撞。具体地，证明如何找到两组输入 $x_1, \ldots, x_t$ 和 $x^{\prime}_1, \ldots, x^{\prime}_{2t}$ 使得 $\mathcal{MT}_t(x_1, \ldots, x_t) = \mathcal{MT}_{2t}(x^{\prime}_1, \ldots, x^{\prime}_{2t})$。

6.18 Modify the construction of a Merkle tree so that it is collision resistant even when the number of inputs t may vary.

6.18 修改 Merkle 树的构造，使其在输入数目 t 可变时仍抗碰撞。

6.19 Consider the scenario introduced in Section 6.6.2 in which a client stores files on a server and wants to verify that files are returned unmodified.

6.19 考虑 6.6.2 节引入的场景，其中客户端在服务器上存储文件并希望验证文件在返回时未被修改。

(a) Provide a formal definition of security for this setting.

(b) Formalize the protocol based on Merkle trees as discussed in Section 6.6.2.

(c) Prove that your construction is secure relative to your definition under the assumption that $(\mathsf{Gen}_{H}, H)$ is collision resistant.

(a) 给出此场景下安全性的形式化定义。

(b) 将 6.6.2 节中讨论的基于 Merkle 树的协议形式化。

(c) 证明在 $(\mathsf{Gen}_{H}, H)$ 抗碰撞的假设下，相对于你的定义，你的构造是安全的。

6.20 Prove that the commitment scheme discussed in Section 6.6.5 is secure if H is modeled as a random oracle.

6.20 证明如果 H 被建模为随机预言机，则 6.6.5 节讨论的承诺方案是安全的。
