# Appendix A: Mathematical Background

## A.1 Identities and Inequalities

We list some standard identities and inequalities that are used at various points throughout the text.

**THEOREM A.1** (Binomial expansion theorem) Let $x, y$ be real numbers, and let $n$ be a positive integer. Then

$$(x+y)^{n}=\sum_{i=0}^{n}\binom{n}{i}x^{i}y^{n-i}.$$

PROPOSITION A.2 For all $x \geq 1$ it holds that $(1 - 1/x)^x \leq e^{-1}$.

PROPOSITION A.3 For all $x$ it holds that ${1} - x \leq e^{-x}$.

PROPOSITION A.4 For all $x$ with ${0} \leq x \leq 1$ it holds that

$$e^{-x}\leq1-\left(1-\frac{1}{e}\right)\cdot x\leq1-\frac{x}{2}.$$

## A.2 Asymptotic Notation

We use standard notation for expressing asymptotic behavior of functions.

DEFINITION A.5 Let $f(n)$, $g(n)$ be functions from non-negative integers to non-negative reals. Then:

 $f(n) = \mathcal{O}(g(n))$ means that there exist positive integers $c$ and $n^{\prime}$ such that for all $n > n^{\prime}$ it holds that $f(n) \leq c \cdot g(n)$.

 $f(n) = \Omega(g(n))$ means that there exist positive integers $c$ and $n^{\prime}$ such that for all $n > n^{\prime}$ it holds that $f(n) \geq c \cdot g(n)$.

 $f(n) = \Theta(g(n))$ means that there exist positive integers $c_1, c_2$, and $n^{\prime}$ such that for all $n > n^{\prime}$ it holds that $c_1 \cdot g(n) \leq f(n) \leq c_2 \cdot g(n)$.

 $f(n) = o(g(n))$ means that $\lim_{n \to \infty} \frac{f(n)}{g(n)} = 0$.

 $f(n) = \omega(g(n))$ means that $\lim_{n \to \infty} \frac{f(n)}{g(n)} = \infty$.

**Example A.6**

Let $f(n) = n^{4} + 3n + 500$. Then:

 $f(n) = \mathcal{O}(n^4).$

• $f(n) = \mathcal{O}(n^5)$. In fact, $f(n) = o(n^5)$.

• $f(n) = \Omega(n^3 \log n)$. In fact, $f(n) = \omega(n^3 \log n)$.

• $f(n) = \Theta(n^4)$.

## A.3 Basic Probability

We assume the reader is familiar with basic probability theory, on the level of what is covered in a typical undergraduate course on discrete mathematics. Here we simply remind the reader of some notation and basic facts.

If $E$ is an event, then $\bar{E}$ denotes the complement of that event; i.e., $\bar{E}$ is the event that $E$ does not occur. By definition, $\Pr[E] = 1 - \Pr[\bar{E}]$. If $E_1$ and $E_2$ are events, then $E_1 \land E_2$ denotes their conjunction; i.e., $E_1 \land E_2$ is the event that both $E_1$ and $E_2$ occur. By definition, $\Pr[E_1 \land E_2] \leq \Pr[E_1]$. Events $E_1$ and $E_2$ are said to be independent if $\Pr[E_1 \land E_2] = \Pr[E_1] \cdot \Pr[E_2]$.

If $E_1$ and $E_2$ are events, then $E_1 \vee E_2$ denotes the disjunction of $E_1$ and $E_2$; that is, $E_1 \vee E_2$ is the event that either $E_1$ or $E_2$ occurs. It follows from the definition that $\Pr[E_1 \vee E_2] \ge \Pr[E_1]$. The union bound is often a very useful upper bound of this quantity.

**PROPOSITION A.7** (Union Bound)

$$\Pr[E_{1}\vee E_{2}]\leq\Pr[E_{1}]+\Pr[E_{2}].$$

Repeated application of the union bound for any events $E_{1}, \ldots, E_{k}$ gives

$$\Pr\left[\bigvee_{i=1}^{k}E_{i}\right]\leq\sum_{i=1}^{k}\Pr[E_{i}].$$

The conditional probability of $E_1$ given $E_2$, denoted $\Pr[E_1 \mid E_2]$, is defined as

$$\Pr[E_{1}\mid E_{2}]\stackrel{\mathrm{def}}{=}\frac{\Pr[E_{1}\wedge E_{2}]}{\Pr[E_{2}]}$$

as long as $\Pr[E_2] \neq 0$. (If $\Pr[E_2] = 0$ then $\Pr[E_1 \mid E_2]$ is undefined.) This represents the probability that event $E_1$ occurs, given that event $E_2$ has occurred. It follows immediately from the definition that

$$\Pr[E_{1}\land E_{2}]=\Pr[E_{1}\mid E_{2}]\cdot\Pr[E_{2}];$$

equality holds even if $\Pr[E_2] = 0$ as long as we interpret multiplication by zero on the right-hand side in the obvious way.

We can now easily derive Bayes' theorem.

THEOREM A.8 (Bayes' Theorem) If $\Pr[E_2] \neq 0$ then

$$\Pr[E_{1}\mid E_{2}]=\frac{\Pr[E_{2}\mid E_{1}]\cdot\Pr[E_{1}]}{\Pr[E_{2}]}.$$

PROOF This follows because

$$\Pr[E_{1}\mid E_{2}]=\frac{\Pr[E_{1}\land E_{2}]}{\Pr[E_{2}]}=\frac{\Pr[E_{2}\land E_{1}]}{\Pr[E_{2}]}=\frac{\Pr[E_{2}\mid E_{1}]\cdot\Pr[E_{1}]}{\Pr[E_{2}]}.$$

Let $E_1, \ldots, E_n$ be disjoint events, so that $\Pr[E_i \land E_j] = 0$ for all $i \neq j$. That is, at most one of the $\{E_i\}$ occur. Assume further that $\Pr[E_i] > 0$ for all $i$. Then for any event $F$

$$\begin{aligned}\Pr[F]&\leq\sum_{i=1}^{n}\Pr[F\land E_{i}]\\&=\sum_{i=1}^{n}\Pr[F\mid E_{i}]\cdot\Pr[E_{i}],\end{aligned}$$

with equality when $\Pr[E_1 \lor \cdots \lor E_n] = 1$. A special case is when we take $E_1$ and $\bar{E}_1$ as our disjoint events. Taking $F = E_1 \lor E_2$ for any event $E_2$, we get a potentially tighter version of the union bound:

$$\begin{align*}\Pr[E_{1}\lor E_{2}]&=\Pr[E_{1}\lor E_{2}\mid E_{1}]\cdot\Pr[E_{1}]+\Pr[E_{1}\lor E_{2}\mid\bar{E}_{1}]\cdot\Pr[\bar{E}_{1}]\\&\leq\Pr[E_{1}]+\Pr[E_{2}\mid\bar{E}_{1}].\end{align*}$$

Extending this to n events we obtain

**PROPOSITION A.9**

$$\Pr[\bigvee_{i=1}^{n}E_{i}]\leq\Pr[E_{1}]+\sum_{i=2}^{n}\Pr[E_{i}\mid\bar{E}_{1}\land\cdots\land\bar{E}_{i-1}].$$

### *Useful Probability Bounds

We review some terminology and state probability bounds that are standard, but may not be encountered in a basic discrete mathematics course. The material here is used only in Section 8.3.

A (discrete, real-valued) random variable $X$ is a variable whose value is assigned probabilistically from some finite set $S$ of real numbers. $X$ is nonnegative if it does not take negative values; it is a ${0}/1$-random variable if $S = \{0,1\}$. The ${0}/1$-random variables $X_1, \ldots, X_k$ are independent if for all $b_1, \ldots, b_k$ it holds that $\Pr[X_1 = b_1 \land \cdots \land X_k = b_k] = \prod_{i=1}^k \Pr[X_i = b_i]$.

We let $\mathsf{Exp}[X]$ denote the expectation of a random variable $X$; if $X$ takes values in a set $S$ then $\mathsf{Exp}[X] \overset{\mathrm{def}}{=} \sum_{s \in S} s \cdot \Pr[X = s]$. One of the most important facts is that expectation is linear; for random variables $X_1, \ldots, X_k$ (with arbitrary dependencies) we have $\mathsf{Exp}[\sum_i X_i] = \sum_i \mathsf{Exp}[X_i]$. If $X_1, X_2$ are independent, then $\mathsf{Exp}[X_i \cdot X_j] = \mathsf{Exp}[X_i] \cdot \mathsf{Exp}[X_j]$.

Markov's inequality is useful when little is known about $X$.

PROPOSITION A.10 (Markov’s inequality) Let $X$ be a non-negative random variable and $v > 0$. Then $\Pr[X \geq v] \leq \mathsf{Exp}[X]/v$.

PROOF Say $X$ takes values in a set S. We have

$$\begin{aligned}\mathrm{Exp}[X]&=\sum_{s\in S}s\cdot\Pr[X=s]\\&\geq\sum_{x\in S,x<v}\Pr[X=x]\cdot0+\sum_{x\in S,x\geq v}v\cdot\Pr[X=x]\\&=v\cdot\Pr[X\geq v].\\ \end{aligned}$$

The desired result follows.

The variance of $X$, denoted $\mathrm{Var}[X]$, measures how much $X$ deviates from its expectation. We have $\mathrm{Var}[X] \stackrel{\mathrm{def}}{=} \mathrm{Exp}[(X - \mathrm{Exp}[X])^2] = \mathrm{Exp}[X^2] - \mathrm{Exp}[X]^2$, and one can easily show that $\mathrm{Var}[aX + b] = a^2\mathrm{Var}[X]$. For a ${0}/1$-random variable $X_i$, we have $\mathrm{Var}[X_i] \leq 1/4$ because in this case $\mathrm{Exp}[X_i] = \mathrm{Exp}[X_i^2]$ and so $\mathrm{Var}[X_i] = \mathrm{Exp}[X_i](1 - \mathrm{Exp}[X_i])$, which is maximized when $\mathrm{Exp}[X_i] = \frac{1}{2}$.

PROPOSITION A.11 (Chebyshev's inequality) Let $X$ be a random variable and $\delta > 0$. Then:

$$\Pr[|X-\mathsf{Exp}[X]|\geq\delta]\leq\frac{\mathsf{Var}[X]}{\delta^{2}}.$$

PROOF Define the non-negative random variable $Y \overset{\mathrm{def}}{=} (X - \mathsf{Exp}[X])^2$ and then apply Markov's inequality. So,

$$\begin{aligned}\Pr[|X-\mathsf{Exp}[X]|\geq\delta]&=\Pr[(X-\mathsf{Exp}[X])^{2}\geq\delta^{2}]\\&\leq\frac{\mathsf{Exp}[(X-\mathsf{Exp}[X])^{2}]}{\delta^{2}}&=\frac{\mathsf{Var}[X]}{\delta^{2}}.\end{aligned}$$

The 0/1-random variables $X_1, \ldots, X_m$ are pairwise independent if for every $i \neq j$ and every $b_i, b_j \in \{0,1\}$ it holds that

$$\Pr[X_{i}=b_{i}~\land~X_{j}=b_{j}]=\Pr[X_{i}=b_{i}]\cdot\Pr[X_{j}=b_{j}].$$

If $X_1, \ldots, X_m$ are pairwise independent then $\mathrm{Var}[\sum_{i=1}^{m} X_i] = \sum_{i=1}^{m} \mathrm{Var}[X_i]$. (This follows since $\mathrm{Exp}[X_i \cdot X_j] = \mathrm{Exp}[X_i] \cdot \mathrm{Exp}[X_j]$ when $i \neq j$, using pairwise independence.) An important corollary of Chebyshev's inequality follows.

COROLLARY A.12 Let $X_1, \ldots, X_m$ be pairwise-independent random variables with the same expectation $\mu$ and variance $\sigma^2$. Then for every $\delta > 0$,

$$\Pr\left[\left|\frac{\sum_{i=1}^{m} X_{i}}{m}-\mu\right|\geq\delta\right]\leq\frac{\sigma^{2}}{\delta^{2}m}.$$

PROOF By linearity of expectation, $\mathsf{Exp}[\sum_{i=1}^{m} X_i/m] = \mu$. Applying Chebyshev's inequality to the random variable $\sum_{i=1}^{m} X_i/m$, we have

$$\Pr\left[\left|\frac{\sum_{i=1}^{m} X_{i}}{m}-\mu\right|\geq\delta\right]\leq\frac{\mathsf{Var}\left[\frac{1}{m}\cdot\sum_{i=1}^{m} X_{i}\right]}{\delta^{2}}.$$

Using pairwise independence, it follows that

$$\mathrm{Var}\left[\frac{1}{m}\cdot\sum_{i=1}^{m}X_{i}\right]=\frac{1}{m^{2}}\sum_{i=1}^{m}\mathrm{Var}[X_{i}]=\frac{1}{m^{2}}\sum_{i=1}^{m}\sigma^{2}=\frac{\sigma^{2}}{m}.$$

The inequality is obtained by combining the above two equations.

Say 0/1-random variables $X_1, \ldots, X_m$ each provides an estimate of some fixed (unknown) bit $b$. That is, $\Pr[X_i = b] \geq 1/2 + \varepsilon$ for all $i$, where $\varepsilon > 0$.

We can estimate $b$ by looking at the value of $X_1$; this estimate will be correct with probability $\Pr[X_1 = b]$. A better estimate can be obtained by looking at the values of $X_1, \ldots, X_m$ and taking the value that occurs the majority of the time. The following allows us to analyze how well this does when $X_1, \ldots, X_m$ are pairwise independent.

PROPOSITION A.13 Fix $\varepsilon > 0$ and $b \in \{0,1\}$, and let $\{X_i\}$ be pairwise-independent, 0/1-random variables for which $\Pr[X_i = b] \geq \frac{1}{2} + \varepsilon$ for all $i$. Consider the process in which $m$ values $X_1, \ldots, X_m$ are recorded and $X$ is set to the value that occurs a strict majority of the time. Then

$$\Pr[X\neq b]\leq\frac{1}{4\cdot\varepsilon^{2}\cdot m}.$$

PROOF By symmetry, we may assume $b = 1$. Then $\mathsf{Exp}[X_i] \geq \frac{1}{2} + \varepsilon$; we assume $\mathsf{Exp}[X_i] = \frac{1}{2} + \varepsilon$ as that is the worst case. Let $X$ denote the strict majority of the $\{X_i\}$, and note that $X \neq 1$ if and only if $\sum_{i=1}^m X_i \leq m/2$. So

$$\begin{aligned}\Pr[X\neq1]&=\Pr\left[\sum_{i=1}^{m}X_{i}\leq m/2\right]\\&=\Pr\left[\frac{\sum_{i=1}^{m}X_{i}}{m}-\frac{1}{2}\leq0\right]\\&=\Pr\left[\frac{\sum_{i=1}^{m}X_{i}}{m}-\left(\frac{1}{2}+\varepsilon\right)\leq-\varepsilon\right]\\&\leq\Pr\left[\left|\frac{\sum_{i=1}^{m}X_{i}}{m}-\left(\frac{1}{2}+\varepsilon\right)\right|\geq\varepsilon\right].\end{aligned}$$

Since $\operatorname{Var}[X_i] \leq 1/4$ for all $i$, applying the previous corollary shows that $\Pr[X \neq 1] \leq \frac{1}{4\varepsilon^2 m}$ as claimed.

A better bound is possible if the $\{X_{i}\}$ are independent:

PROPOSITION A.14 (Chernoff bound) Fix $\varepsilon > 0$ and $b \in \{0,1\}$, and let $\{X_i\}$ be independent 0/1-random variables with $\Pr[X_i = b] = \frac{1}{2} + \varepsilon$ for all $i$. The probability that their majority value is not $b$ is at most $e^{-\varepsilon^2 m/2}$.

## A.4 The “Birthday” Problem

If we choose $q$ elements $y_1, \ldots, y_q$ uniformly from a set of size $N$, what is the probability that there exist distinct $i,j$ with $y_i = y_j$? We refer to the stated event as a collision, and let $\mathsf{coll}(q, N)$ denote the probability of this event. This problem is related to the so-called "birthday" problem, which asks what size group of people we need such that with probability ${1}/2$ some pair of people in the group share a birthday. To see the relationship, let $y_i$ denote the birthday of the $i$th person in the group. If there are $q$ people in the group then we have $q$ values $y_1, \ldots, y_q$ chosen uniformly from $\{1, \ldots, 365\}$, making the simplifying assumption that birthdays are uniformly and independently distributed among the 365 days of a non-leap year. Furthermore, matching birthdays correspond to a collision, i.e., distinct $i,j$ with $y_i = y_j$. So the desired solution to the birthday problem is given by the minimal (integer) value of $q$ for which $\mathsf{coll}(q, 365) \geq 1/2$. (The answer may surprise you—taking $q = 23$ people suffices!)

The following shows that when $q \leq \sqrt{2N}$, the probability of a collision is $\Theta(q^2/N)$; alternately, for $q = \Theta(\sqrt{N})$ the probability of a collision is constant.

LEMMA A.15 Fix a positive integer $N$, and say $q \leq \sqrt{2N}$ elements $y_1, \ldots, y_q$ are chosen uniformly and independently from a set of size $N$. Then

$$\frac{q\cdot(q-1)}{4N}\leq1-e^{-q(q-1)/2N}\leq\mathrm{coll}(q,N)\leq\frac{q\cdot(q-1)}{2N}.$$

PROOF The upper bound, which holds for arbitrary $q$, can be proven by a simple application of the union bound (Proposition A.7). Recall that a collision means that there exist distinct $i,j$ with $y_i = y_j$. Let Coll denote the event of a collision, and let $\mathsf{Coll}_{i,j}$ denote the event that $y_i = y_j$. It is immediate that $\Pr[\mathsf{Coll}_{i,j}] = 1/N$ for any distinct $i,j$. Furthermore, $\mathsf{Coll} = \bigvee_{i \neq j} \mathsf{Coll}_{i,j}$ and so repeated application of the union bound implies that

$$\begin{align*}\Pr\left[\mathsf{Coll}\right]&=\Pr\left[\bigvee_{i\neq j}\mathsf{Coll}_{i,j}\right]\\&\leq\sum_{i\neq j}\Pr\left[\mathsf{Coll}_{i,j}\right]=\binom{q}{2}\cdot\frac{1}{N}.\end{align*}$$

For the lower bound, let $\mathsf{NoColl}_i$ be the event that there is no collision among $y_1, \ldots, y_i$; that is, $y_j \neq y_k$ for all $j < k \leq i$. Then $\mathsf{NoColl}_q = \overline{\mathsf{Coll}}$ is the event that there is no collision at all. If $\mathrm{NoColl}_q$ occurs then $\mathrm{NoColl}_i$ must also have occurred for all $i \leq q$. Thus,

$$\Pr[\mathsf{NoColl}_{q}]=\Pr[\mathsf{NoColl}_{1}]\cdot\Pr[\mathsf{NoColl}_{2}\mid\mathsf{NoColl}_{1}]\cdot\cdot\cdot\Pr[\mathsf{NoColl}_{q}\mid\mathsf{NoColl}_{q-1}].$$

Now, $\Pr[\mathsf{NoColl}_{1}] = 1$ since $y_{1}$ cannot collide with itself. Furthermore, if event $\mathsf{NoColl}_{i}$ occurs then $\{y_{1}, \ldots, y_{i}\}$ contains $i$ distinct values; so, the probability that $y_{i+1}$ collides with one of these values is $\frac{i}{N}$ and hence the probability that $y_{i+1}$ does not collide with any of these values is ${1} - \frac{i}{N}$. This means

$$\Pr[\mathsf{NoColl}_{i+1}\mid\mathsf{NoColl}_{i}]=1-\frac{i}{N},$$

and so

$$\Pr[\mathsf{NoColl}_{q}]=\prod_{i=1}^{q-1}\left(1-\frac{i}{N}\right)\;.$$

Since $i/N < 1$ for all $i$, we have ${1} - \frac{i}{N} \leq e^{-i/N}$ (by Inequality A.3) and so

$$\Pr[\mathsf{NoColl}_{q}]\leq\prod_{i=1}^{q-1}e^{-i/N}=e^{-\sum_{i=1}^{q-1}(i/N)}=e^{-q(q-1)/2N}.$$

We conclude that

$$\Pr[\mathsf{Coll}]=1-\Pr[\mathsf{NoColl}_{q}]\geq1-e^{-q(q-1)/2N}\geq\frac{q(q-1)}{4N},$$

using Inequality A.4 in the last step (note that $q(q-1)/2N < 1$).

As a simple application of Lemma A.15, we show that any pseudorandom permutation is also a pseudorandom function (cf. Proposition 3.26). Recall that a pseudorandom permutation has $\ell_{in} = \ell_{out}$, meaning that its input and output lengths are equal. Our proof here is adapted from [27].

PROPOSITION A.16 If $F$ is a pseudorandom permutation and furthermore $\ell_{out}(n) \geq n$, then $F$ is also a pseudorandom function.

PROOF For simplicity of notation, we assume $\ell_{in} = \ell_{out} = n$. The crux of the proof is to show that a random permutation is indistinguishable (using polynomially many queries) from a random function. Let $D$ be an algorithm, and let $q = q(n)$ be the number of queries that $D$ makes to its oracle. (We assume without loss of generality that $D$ always makes exactly $q$ queries, and that it never repeats a query.) We will allow $D$ to be all-powerful (and hence may assume it is deterministic), but will assume that the number of queries $q$ that it makes is polynomial. We show

$$\left|\Pr_{f\leftarrow\mathsf{Func}_{n}}[D^{f(\cdot)}(1^{n})=1]-\Pr_{f\leftarrow\mathsf{Perm}_{n}}[D^{f(\cdot)}(1^{n})=1]\right|<\frac{q^{2}}{2^{n+1}}. \tag{A.1}$$

The intuition for this is that the only way $D$ can tell that its oracle $f$ is not a permutation is by observing a collision, i.e., two distinct inputs that map to the same output. However, the probability of finding such a collision when querying a random function $q$ times is at most $\mathsf{coll}(q, 2^n) \leq q^2/2^n$, which is negligible for any polynomial $q$.

Formally, let $\mathsf{Coll}$ be the event that two queries by $D$ to its oracle return the same result. We claim first that

$$\Pr_{f\leftarrow\mathsf{Func}_{n}}[D^{f(\cdot)}(1^{n})=1\mid\overline{\mathsf{Coll}}]=\Pr_{f\leftarrow\mathsf{Perm}_{n}}[D^{f(\cdot)}(1^{n})=1]. \tag{A.2}$$

To see this, observe that the behavior of $D$ is completely characterized by the set $S \subseteq (\{0,1\}^n)^q$ of $q$-tuples such that $\vec{a} = (a_1, \ldots, a_q) \in S$ iff $D$ outputs 1 when it receives $a_i$ as the response to its $i$th oracle query for all $i$. Let distinct $\subset(\{0,1\}^n)^q$ denote the set of $q$-tuples where each entry is distinct. When $f$ is a permutation, then each $\vec{a} \in \mathsf{distinct}$ is equally likely and $\vec{a} \notin \mathsf{distinct}$ cannot occur; thus

$$\Pr_{f\leftarrow\mathsf{Perm}_{n}}[D^{f(\cdot)}(1^{n})=1]=\frac{|S\cap\mathsf{distinct}|}{|\mathsf{distinct}|}.$$

When $f$ is a random function, each $q$-tuple in $(\{0,1\}^n)^q$ occurs with probability ${2}^{-nq}$. So, using Bayes' theorem

$$\begin{align*}\Pr_{f\leftarrow\mathsf{Func}_{n}}[D^{f(\cdot)}(1^{n})=1\mid\overline{\mathsf{Coll}}]&=\frac{\Pr_{f\leftarrow\mathsf{Func}_{n}}[D^{f(\cdot)}(1^{n})=1\land\overline{\mathsf{Coll}}]}{\Pr_{f\leftarrow\mathsf{Func}_{n}}[\overline{\mathsf{Coll}}]}\\&=\frac{2^{-nq}\cdot|S\cap\mathsf{distinct}|}{2^{-nq}\cdot|\mathsf{distinct}|}.\end{align*}$$

Equation (A.2) follows.

As a consequence,

$$\begin{aligned}&\left|\Pr_{f\leftarrow\mathsf{Func}_{n}}[D^{f(\cdot)}(1^{n})=1]-\Pr_{f\leftarrow\mathsf{Perm}_{n}}[D^{f(\cdot)}(1^{n})=1]\right|\\&=\left|\Pr_{f\leftarrow\mathsf{Func}_{n}}[D^{f(\cdot)}(1^{n})=1\mid\overline{\mathsf{Coll}}]\cdot\Pr[\overline{\mathsf{Coll}}]\right.\\&\quad\left.+\Pr_{f\leftarrow\mathsf{Func}_{n}}[D^{f(\cdot)}(1^{n})=1\mid\mathsf{Coll}]\cdot\Pr[\mathsf{Coll}]-\Pr_{f\leftarrow\mathsf{Perm}_{n}}[D^{f(\cdot)}(1^{n})=1]\right|\\&=\left|\Pr_{f\leftarrow\mathsf{Func}_{n}}[D^{f(\cdot)}(1^{n})=1\mid\mathsf{Coll}]\cdot\Pr[\mathsf{Coll}]-\Pr_{f\leftarrow\mathsf{Perm}_{n}}[D^{f(\cdot)}(1^{n})=1]\cdot\Pr[\mathsf{Coll}]\right|\\&\leq\Pr[\mathsf{Coll}].\end{aligned}$$

With Lemma A.15, this implies Equation (A.1) and completes the proof.

While the above shows that a pseudorandom permutation (PRP) is asymptotically also a pseudorandom function (PRF), it does also indicate a concrete security gap: namely, a PRP can be distinguished from a PRF with probability $\mathcal{O}(q^2/2^{\ell_{out}(n)})$ using $q$ queries. This is important to keep in mind when using a block cipher and treating it in the analysis as a PRF.

## A.5 *Finite Fields

We use finite fields only sparingly in the book, but we include a definition and some basic facts for completeness. Further details can be found in any textbook on abstract algebra.

DEFINITION A.17 A (finite) field is a (finite) set $\mathbb{F}$ along with two binary operations +, $\cdot$ for which the following hold:

- $\mathbb{F}$ is an abelian group with respect to the operation $+$. We let ${0}$ denote the identity element of this group.

- $\mathbb{F} \setminus \{0\}$ is an abelian group with respect to the operation $\cdot$. We let ${1}$ denote the identity element of this group.

As usual, we often write ab in place of a $\cdot$ b.

• (Distributivity:) For all $a, b, c \in \mathbb{F}$, we have $a \cdot (b + c) = ab + ac$.

The additive inverse of $a \in \mathbb{F}$, denoted by $-a$, is the unique element satisfying $a + (-a) = 0$; we write $b - a$ in place of $b + (-a)$. The multiplicative inverse of $a \in \mathbb{F} \setminus \{0\}$, denoted by $a^{-1}$, is the unique element satisfying $aa^{-1} = 1$; we often write $b/a$ in place of $ba^{-1}$.

**Example A.18**

It follows from the results of Section 9.1.4 that for any prime $p$ the set $\{0, \ldots, p-1\}$ is a finite field with respect to addition and multiplication modulo $p$. We denote this field by $\mathbb{F}_p$.

Finite fields have a rich theory. For our purposes, we need only a few basic facts. The order of $\mathbb{F}$ is the number of elements in $\mathbb{F}$ (assuming it is finite). Recall also that $q$ is a prime power if $q = p^r$ for some prime $p$ and integer $r \geq 1$.

THEOREM A.19 If $\mathbb{F}$ is a finite field, then the order of $\mathbb{F}$ is a prime power. Conversely, for every prime power $q$ there is a finite field of order $q$, which is moreover the unique such field (up to relabeling of the elements).

For $q = p^r$ with $p$ prime, we let $\mathbb{F}_q$ denote the (unique) field of order $q$. We call $p$ the characteristic of $\mathbb{F}_q$.

As in the case of groups, if $n$ is a positive integer and $a \in \mathbb{F}$ then

$$n\cdot a{\stackrel{\mathrm{def}}{=}}\underbrace{a+\cdots+a}_{n\text{ times}}\quad{\mathrm{and}}\quad a^{n}{\stackrel{\mathrm{def}}{=}}\underbrace{a\cdots a}_{n\text{ times}}.$$

The notation is extended for $n \leq 0$ in the natural way.

THEOREM A.20 Let $\mathbb{F}_q$ be a finite field of characteristic $p$. Then for all $a \in \mathbb{F}_q$ we have $p \cdot a = 0$.

Let $q = p^r$ with $p$ prime. For $r = 1$, we have seen in Example A.18 that $\mathbb{F}_q = \mathbb{F}_p$ can be taken to be the set $\{0, \ldots, p-1\}$ under addition and multiplication modulo $p$. We caution, however, that for $r > 1$ the set $\{0, \ldots, q-1\}$ is not a field under addition and multiplication modulo $q$. For example, if we take $q = 3^2 = 9$ then the element 3 does not have a multiplicative inverse modulo 9.

Finite fields of characteristic $p$ can be represented using polynomials over $\mathbb{F}_p$. We give an example to demonstrate the flavor of the construction, without discussing why the construction works or describing the general case. We construct the field $\mathbb{F}_4$ by working with polynomials over $\mathbb{F}_2$. Fix the polynomial $r(x) = x^2 + x + 1$, and note that $r(x)$ has no roots over $\mathbb{F}_2$ since $r(0) = r(1) = 1$ (recall that we are working in $\mathbb{F}_2$, which means that all operations are carried out modulo 2). In the same way that we can introduce the imaginary number $i$ to be a root of $x^2 + 1$ over the reals, we can introduce a value $\omega$ to be a root of $r(x)$ over $\mathbb{F}_2$; that is, $\omega^2 = -\omega - 1$. We then define $\mathbb{F}_4$ to be the set of all degree-1 polynomials in $\omega$ over $\mathbb{F}_2$; that is, $\mathbb{F}_4 = \{0, 1, \omega, \omega + 1\}$. Addition in $\mathbb{F}_4$ will just be regular polynomial addition, remembering that operations on the coefficients are done in $\mathbb{F}_2$ (that is, modulo 2). Multiplication in $\mathbb{F}_4$ will be polynomial multiplication (again, with operations on the coefficients carried out modulo 2) followed by the substitution $\omega^2 = -\omega - 1$; this also ensures that the result lies in $\mathbb{F}_4$. So, for example,

$$\omega+(\omega+1)=2\omega+1=1$$

and

$$\left(\omega+1\right)\cdot\left(\omega+1\right)=\omega^{2}+2\omega+1=\left(-\omega-1\right)+1=-\omega=\omega.$$

Although not obvious, one can check that this is a field; the only difficult condition to verify is that every nonzero element has a multiplicative inverse.

We need only one other result.

THEOREM A.21 Let $\mathbb{F}_q$ be a finite field of order $q$. Then the abelian group $\mathbb{F}_q \setminus \{0\}$ with respect to $\cdot$ is a cyclic group of order $q - 1$.

