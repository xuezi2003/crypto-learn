# Appendix B: Basic Algorithmic Number Theory

For the cryptographic constructions given in this book to be efficient (i.e., to run in time polynomial in the lengths of their inputs), it is necessary for these constructions to utilize efficient (that is, polynomial-time) algorithms for performing basic number-theoretic operations. Although in some cases there exist “trivial” algorithms that would work, it is still worthwhile to carefully consider their efficiency since for cryptographic applications it is not uncommon to use integers that are thousands of bits long. In other cases obtaining any polynomial-time algorithm requires a bit of cleverness, and an analysis of their performance may rely on non-trivial group-theoretic results.

In Appendix B.1 we describe basic algorithms for integer arithmetic. Here we cover the familiar algorithms for addition, subtraction, etc., as well as the Euclidean algorithm for computing greatest common divisors. We also discuss the extended Euclidean algorithm, assuming there that the reader has covered the material in Section 9.1.1.

In Appendix B.2 we show various algorithms for modular arithmetic. In addition to a brief discussion of basic modular operations (i.e., modular reduction, addition, multiplication, and inversion), we also describe Montgomery multiplication, which can greatly simplify (and speed up) implementations of modular arithmetic. We then discuss algorithms for problems that are less common outside the field of cryptography: exponentiation modulo $N$ (as well as in arbitrary groups) and choosing a uniform element of $\mathbb{Z}_N$ or $\mathbb{Z}_N^*$ (or in an arbitrary group). This section assumes familiarity with the basic group theory covered in Section 9.1.

The material above is used implicitly throughout the second half of the book, although it is not absolutely necessary to read this material in order to follow the book. (In particular, the reader willing to accept the results of this Appendix without proof can simply read the summary of those results in the theorems below.) Appendix B.3, which discusses finding generators in cyclic groups (when the factorization of the group order is known) and assumes the results of Section 9.3.1, contains material that is hardly used at all; it is included for completeness and reference.

Since our goal is only to establish that certain problems can be solved in polynomial time, we have opted for simplicity rather than efficiency in our selection of algorithms and their descriptions (as long as the algorithms run in polynomial time). For this reason, we generally will not be interested in
the exact running times of the algorithms we present beyond establishing that they indeed run in polynomial time. The reader who is seriously interested in implementing these algorithms is forewarned to look at other sources for more efficient alternatives as well as various techniques for speeding up the necessary computations.

The results in this Appendix are summarized by the theorems that follow. Throughout, we assume that any integer $a$ provided as input is written using exactly $\|a\|$ bits; i.e., the high-order bit is 1. In Appendix B.1 we show:

THEOREM B.1 (Integer operations) Given integers $a$ and $b$, it is possible to perform the following operations in time polynomial in $\|a\|$ and $\|b\|$:

1. Computing the sum $a + b$ and the difference $a - b$;

2. Computing the product $ab$;

3. Computing positive integers $q$ and $r < b$ such that $a = qb + r$ (i.e., computing division with remainder);

4. Computing the greatest common divisor of $a$ and $b$, $\gcd(a,b)$;

5. Computing integers $X, Y$ with $Xa + Yb = \gcd(a, b)$.

The following results are proved in Appendix B.2:

THEOREM B.2 (Modular operations) Given integers $N > 1$, $a$, and $b$, it is possible to perform the following operations in time polynomial in $\|a\|$, $\|b\|$, and $\|N\|$:

1. Computing the modular reduction $[a \bmod N]$;

2. Computing the sum $[(a+b)\bmod N]$, the difference $[(a-b)\bmod N]$, and the product $[ab\bmod N]$;

3. Determining whether $a$ is invertible modulo $N$ and, if so, computing the multiplicative inverse $[a^{-1} \bmod N]$;

4. Computing the exponentiation $[a^{b} \bmod N]$.

The following generalizes Theorem B.2(5) to arbitrary groups:

THEOREM B.3 (Group exponentiation) Let $\mathbb{G}$ be a group, written multiplicatively. Let $g$ be an element of the group and let $b$ be a non-negative integer. Then $g^b$ can be computed using $\mathsf{poly}(\|b\|)$ group operations.

THEOREM B.4 (Choosing uniform elements) There exists a randomized algorithm with the following properties: on input N,

• The algorithm runs in time polynomial in $\|N\|$;

• The algorithm outputs fail with probability negligible in $\|N\|$; and

- Conditioned on not outputting fail, the algorithm outputs a uniformly distributed element of $\mathbb{Z}_N$.

An algorithm with analogous properties exists for $\mathbb{Z}_N^*$ as well.

Since the probability that either algorithm referenced in the above theorem outputs fail is negligible, we ignore this possibility (and instead leave it implicit). In Appendix B.2 we also discuss generalizations of the above to the case of selecting a uniform element from any finite group (subject to certain requirements on the representation of group elements).

A proof of the following is in Appendix B.3:

THEOREM B.5 (Testing and finding generators) Let G be a cyclic group of order q, and assume that the group operation and selection of a uniform group element can be carried out in unit time.

1. There is an algorithm that on input $q$, the prime factorization of $q$, and an element $g \in \mathbb{G}$, runs in $\mathsf{poly}(\|q\|)$ time and decides whether $g$ is a generator of $\mathbb{G}$.

2. There is a randomized algorithm that on input $q$ and the prime factorization of $q$, runs in $\mathsf{poly}(\|q\|)$ time and outputs a generator of $\mathbb{G}$ except with probability negligible in $\|q\|$. Conditioned on the output being a generator, it is uniformly distributed among the generators of $\mathbb{G}$.

## B.1 Integer Arithmetic

### B.1.1 Basic Operations

We begin our exploration of algorithmic number theory with a discussion of integer addition/subtraction, multiplication, and division with remainder. A little thought shows that all these operations can be carried out in time polynomial in the input length using the standard “grade-school” algorithms for these problems. For example, addition of two positive integers $a$ and $b$ with $a > b$ can be done in time linear in $\|a\|$ by stepping one-by-one through the bits of $a$ and $b$, starting with the low-order bits, and computing the corresponding output bit and a “carry bit” at each step. (Details are omitted.) Multiplication of two $n$-bit integers $a$ and $b$, to take another example, can
be done by first generating a list of $n$ integers of length at most ${2}n$ (each of which is equal to $a \cdot 2^{i-1} \cdot b_i$, where $b_i$ is the $i$th bit of $b$) and then adding these $n$ integers together to obtain the final result. (Division with remainder is trickier to implement efficiently, but can also be done.)

Although these grade-school algorithms suffice to demonstrate that the aforementioned problems can be solved in polynomial time, it is interesting to note that these algorithms are in some cases not the best ones available. As an example, the simple algorithm for multiplication given above multiplies two $n$-bit numbers in time $\mathcal{O}(n^2)$, but there exists a better algorithm running in time $\mathcal{O}(n^{\log_2 3})$ (and even that is not the best possible). While the difference is insignificant for numbers of the size we encounter daily, it becomes noticeable when the numbers are large. In cryptographic applications it is not uncommon to use integers that are thousands of bits long (i.e., $n > 1000$), and a judicious choice of which algorithms to use then becomes critical.

### B.1.2 The Euclidean and Extended Euclidean Algorithms

Recall from Section 9.1 that $\gcd(a,b)$, the greatest common divisor of two integers $a$ and $b$, is the largest integer $d$ that divides both $a$ and $b$. We state an easy proposition regarding the greatest common divisor, and then show how this leads to an efficient algorithm for computing $\gcd$'s.

PROPOSITION B.6 Let $a, b > 1$ with $b \nmid a$. Then

$$\gcd(a,b)=\gcd(b,[a\bmod b]).$$

PROOF If $b > a$ the claim is immediate; so, assume $a > b$. Write $a = qb + r$ for $q, r$ positive integers and $r < b$ (cf. Proposition 9.1); note $r > 0$ because $b \nmid a$. Since $r = [a \bmod b]$, it remains to show that $\gcd(a, b) = \gcd(b, r)$.

The claim follows since for any positive integer $d$ we have

$$d\mid a \text{ and } d\mid b\Longleftrightarrow d\mid(a-q b)\text{ and } d\mid b,$$

and $r = a - qb$.

The above suggests the recursive Euclidean algorithm (Algorithm B.7) for computing the greatest common divisor $gcd(a, b)$ of two integers $a$ and $b$. Correctness of the algorithm follows readily from Proposition B.6. As for its running time, we show below that on input $(a, b)$ the algorithm makes fewer than ${2} \cdot \|b\|$ recursive calls. Since checking whether $b$ divides $a$ and computing $[a \bmod b]$ can both be done in time polynomial in $\|a\|$ and $\|b\|$, this implies that the entire algorithm runs in polynomial time.

| ALGORITHM B.7 |
| --- |
| The Euclidean algorithm GCD |
| Input: Integers $a$, $b$ with $a \ge b > 0$ |
| Output: The greatest common divisor of $a$ and $b$ |
| if $b$ divides $a$ |
| return $b$ |
| else return GCD $(b, [a \mod b])$ |

PROPOSITION B.8 Consider an execution of GCD $(a_0, b_0)$ where it holds that $a_0 \geq b_0 > 0$, and let $a_i, b_i$ (for $i = 1, \ldots, \ell$) denote the arguments to the ith recursive call of GCD. Then $b_{i+2} \leq b_i/2$ for ${0} \leq i \leq \ell - 2$.

PROOF First note that for any $a > b$ we have $[a \bmod b] < a/2$. To see this, consider the two cases: If $b \leq a/2$ then $[a \bmod b] < b \leq a/2$ is immediate. On the other hand, if $b > a/2$ then $[a \bmod b] = a - b < a/2$.

Now fix arbitrary $i$ with ${0} \leq i \leq \ell - 2$. Then $b_{i+2} = [a_{i+1} \bmod b_{i+1}] < a_{i+1}/2 = b_i/2$.

COROLLARY B.9 In an execution of algorithm GCD(a,b), there are at most ${2} \| b\| - 2$ recursive calls to GCD.

PROOF Let $a_i, b_i$ (for $i = 1, \ldots, \ell$) denote the arguments to the $i$th recursive call of GCD. The $\{b_i\}$ are always greater than zero, and the algorithm makes no further recursive calls if it ever happens that $b_i = 1$ (since then $b_i \mid a_i$). The previous proposition indicates that the $\{b_i\}$ decrease by a multiplicative factor of (at least) 2 in every two iterations. It follows that the number of recursive calls to GCD is at most ${2} \cdot (\|b\| - 1)$.

By Proposition 9.2, we know that for positive integers $a, b$ there exist integers $X, Y$ with $Xa + Yb = \gcd(a, b)$. A simple modification of the Euclidean algorithm, called the extended Euclidean algorithm, can be used to find $X, Y$ in addition to computing $\gcd(a, b)$; see Algorithm B.10. You are asked to show correctness of the extended Euclidean algorithm in Exercise B.1, and to prove that the algorithm runs in polynomial time in Exercise B.2.

ALGORITHM B.10
The extended Euclidean algorithm eGCD

Input: Integers $a, b$ with $a \geq b > 0$

Output: $(d, X, Y)$ with $d = \gcd(a, b)$ and $Xa + Yb = d$

if $b$ divides $a$
    return $(b, 0, 1)$
else
    Compute integers $q, r$ with $a = qb + r$ and ${0} < r < b$
 $(d, X, Y) := \mathsf{eGCD}(b, r) \quad // \text{note that } Xb + Yr = d$
    return $(d, Y, X - Yq)$

## B.2 Modular Arithmetic

We now turn our attention to basic arithmetic operations modulo $N > 1$. We will use $\mathbb{Z}_N$ to refer both to the set $\{0, \ldots, N-1\}$ as well as to the group that results by considering addition modulo $N$ among the elements of this set.

### B.2.1 Basic Operations

Efficient algorithms for the basic arithmetic operations over the integers immediately imply efficient algorithms for the corresponding arithmetic operations modulo $N$. For example, computing the modular reduction $[a \mod N]$ can be done in time polynomial in $\|a\|$ and $\|N\|$ by computing division-with-remainder over the integers. Next consider modular operations on two elements $a, b \in \mathbb{Z}_N$ where $\|N\| = n$. (Note that $a, b$ have length at most $n$. Actually, it is convenient to simply assume that all elements of $\mathbb{Z}_N$ have length exactly $n$, padding to the left with ${0}s$ if necessary.) Addition of $a$ and $b$ modulo $N$ can be done by first computing $a + b$, an integer of length at most $n + 1$, and then reducing this intermediate result modulo $N$. Similarly, multiplication modulo $N$ can be performed by first computing the integer $ab$ of length at most ${2}n$ and then reducing the result modulo $N$. Since addition, multiplication, and division-with-remainder can all be done in polynomial time, these give polynomial-time algorithms for addition and multiplication modulo $N$.

### B.2.2 Computing Modular Inverses

Our discussion thus far has shown how to add, subtract, and multiply modulo $N$. One operation we are missing is “division” or, equivalently, computing multiplicative inverses modulo $N$. Recall from Section 9.1.2 that the multiplicative inverse (modulo $N$) of an element $a \in \mathbb{Z}_N$ is an element $a^{-1} \in \mathbb{Z}_N$ such that $a \cdot a^{-1} = 1 \mod N$. Proposition 9.7 shows that $a$ has an inverse if and only if $\gcd(a, N) = 1$, i.e., if and only if $a \in \mathbb{Z}_N^*$. Thus, using the Euclidean algorithm we can easily determine whether a given element $a$ has a multiplicative inverse modulo $N$.

Given $N$ and $a \in \mathbb{Z}_N$ with $\gcd(a, N) = 1$, Proposition 9.2 tells us that there exist integers $X, Y$ with $Xa + YN = 1$. This means that $[X \bmod N]$ is the multiplicative inverse of $a$. Integers $X$ and $Y$ satisfying $Xa + YN = 1$ can be found efficiently using the extended Euclidean algorithm eGCD shown in

| ALGORITHM B.11 |
| --- |
| Computing modular inverses |
| Input: Modulus $N$; element $a$ |
| Output: $[a^{-1} \mod N]$ (if it exists) |
| $(d, X, Y)$ := eGCD $(a, N)$ // note that $Xa + YN = \gcd(a, N)$ |
| if $d \neq 1$ return “a is not invertible modulo $N$” |
| else return $[X \bmod N]$ |

This leads to a polynomial-time algorithm (Algorithm B.11) for computing multiplicative inverses.

### B.2.3 Modular Exponentiation

A more challenging task is that of exponentiation modulo $N$, that is, computing $[a^b \bmod N]$ for base $a \in \mathbb{Z}_N$ and integer exponent $b > 0$. (When $b = 0$ the problem is easy. When $b < 0$ and $a \in \mathbb{Z}_N^*$ then $a^b = (a^{-1})^{-b} \bmod N$ and the problem is reduced to the case of exponentiation with a positive exponent given that we can compute inverses, as discussed in the previous section.) Notice that the basic approach used in the case of addition and multiplication (i.e., computing the integer $a^b$ and then reducing this intermediate result modulo $N$) does not work here: the integer $a^b$ has length $\|a^b\| = \Theta(\log a^b) = \Theta(b \cdot \|a\|)$, and so even storing the intermediate result $a^b$ would require time exponential in $\|b\| = \Theta(\log b)$.

We can address this problem by reducing modulo $N$ at all intermediate steps of the computation, rather than only reducing modulo $N$ at the end. This has the effect of keeping the intermediate results “small” throughout the computation. Even with this important initial observation, it is still nontrivial to design a polynomial-time algorithm for modular exponentiation. Consider the naïve approach of Algorithm B.12, which simply performs $b$ multiplications by $a$. This still runs in time that is exponential in $\|b\|$.

ALGORITHM B.12
A naïve algorithm for modular exponentiation

Input: Modulus $N$; base $a \in \mathbb{Z}_N$; integer exponent $b > 0$
Output: $[a^b \bmod N]$

$x := 1$
for $i = 1$ to $b$:
 $x := [x \cdot a \bmod N]$
return $x$

This naïve algorithm can be viewed as relying on the following recurrence:

$$[a^{b}\bmod N]=[a\cdot a^{b-1}\bmod N]=[a\cdot a\cdot a^{b-2}\bmod N]=\cdots$$

Any algorithm based on this relationship will require $\Theta(b)$ time. We can do better by relying on the following recurrence:

$$[a^{b}\bmod N]=\left\{\begin{matrix}{\left[\left(a^{\frac{b}{2}}\right)^{2}\bmod N\right]}&{{\mathrm{when~}}b{\mathrm{~is~even}}}\\ {\left[a\cdot\left(a^{\frac{b-1}{2}}\right)^{2}\bmod N\right]}&{{\mathrm{when~}}b{\mathrm{~is~odd}}.}\\ \end{matrix}\right.$$

Doing so leads to an algorithm—called, for obvious reasons, “square-and-multiply” (or “repeated squaring”)—that requires only $\mathcal{O}(\log b) = \mathcal{O}(\|b\|)$ modular squarings/multiplications; see Algorithm B.13. In this algorithm, the length of $b$ decreases by 1 in each iteration; it follows that the number of iterations is $\|b\|$, and so the overall algorithm runs in time polynomial in $\|a\|$, $\|b\|$, and $\|N\|$. More precisely, the number of modular squarings is exactly $\|b\|$, and the number of additional modular multiplications is exactly the Hamming weight of $b$ (i.e., the number of 1s in the binary representation of $b$). This explains the preference, discussed in Section 9.2.4, for choosing the public RSA exponent $e$ to have small length/Hamming weight.

ALGORITHM B.13
Algorithm ModExp for efficient modular exponentiation

Input: Modulus $N$; base $a \in \mathbb{Z}_N$; integer exponent $b > 0$
Output: $[a^b \bmod N]$

$x := a$
$t := 1$
// maintain the invariant that the answer is $[t \cdot x^b \bmod N]$
while $b > 0$ do:
    if $b$ is odd
     $t := [t \cdot x \bmod N]$, $b := b - 1$
 $x := [x^2 \bmod N]$, $b := b/2$
return $t$

Fix $a$ and $N$ and consider the modular exponentiation function given by $f_{a,N}(b)=[a^{b}\bmod N]$. We have just seen that computing $f_{a,N}$ is easy. In contrast, computing the inverse of this function—that is, computing $b$ given $a$, $N$, and $[a^{b}\bmod N]$—is believed to be hard for appropriate choice of $a$ and $N$. Inverting this function requires solving the discrete-logarithm problem, something we discuss in detail in Section 9.3.2.

Using precomputation. If the base $a$ is known in advance, and there is a bound on the length of the exponent $b$, then one can use precomputation and a small amount of memory to speed up computation of $[a^b \bmod N]$. Say $\|b\| \leq n$. Then we precompute and store the $n$ values

$$x_{0}:=a,\quad x_{1}:=[a^{2}\bmod N],\quad\ldots,\quad x_{n-1}:=[a^{2^{n-1}}\bmod N].$$

Given exponent b with binary representation $b_{n-1} \cdots b_0$ (written from most to least significant bit), we then have

$$a^{b}=a^{\sum_{i=0}^{n-1}2^{i}\cdot b_{i}}=\prod_{i=0}^{n-1}x_{i}^{b_{i}}\bmod N.$$

Since $b_i \in \{0,1\}$, the number of multiplications needed to compute the result is exactly one less than the Hamming weight of $b$.

#### Exponentiation in Arbitrary Groups

The efficient modular exponentiation algorithm given above carries over in a straightforward way to enable efficient exponentiation in any group, as long as the underlying group operation can be performed efficiently. Specifically, if $\mathbb{G}$ is a group and $g$ is an element of $\mathbb{G}$, then $g^b$ can be computed using at most ${2} \cdot \|b\|$ applications of the underlying group operation. Precomputation could also be used, exactly as described above.

If the order $q$ of $\mathbb{G}$ is known, then $a^b = a^{[b \bmod q]}$ (cf. Proposition 9.53) and this can be used to speed up the computation by reducing $b$ modulo $q$ first.

Considering the (additive) group $\mathbb{Z}_N$, the group exponentiation algorithm just described gives a method for computing the “exponentiation”

$$[b\cdot g\bmod N]\stackrel{\operatorname{def}}{=}[\underbrace{g+\cdots+g}_{b\text{ times}}\bmod N]$$

that differs from the method discussed earlier that relies on standard integer multiplication followed by a modular reduction. In comparing the two approaches to solving the same problem, note that the original algorithm uses specific information about $\mathbb{Z}_N$; in particular, it (essentially) treats the “exponent” $b$ as an element of $\mathbb{Z}_N$ (possibly by reducing $b$ modulo $N$ first). In contrast, the “square-and-multiply” algorithm just presented treats $\mathbb{Z}_N$ only as an abstract group. (Of course, the group operation of addition modulo $N$ relies on the specifics of $\mathbb{Z}_N$.) The point of this discussion is merely to illustrate that some group algorithms are generic (i.e., they apply equally well to all groups) while some group algorithms rely on specific properties of a particular group or class of groups. We saw some examples of this phenomenon in Chapter 10.

### B.2.4 *Montgomery Multiplication

Although division over the integers (and hence modular reduction) can be done in polynomial time, algorithms for integer division are slow in comparison to, say, algorithms for integer multiplication. Montgomery multiplication provides a way to perform modular multiplication without carrying out any expensive modular reductions. Since pre- and postprocessing is required, the method is advantageous only when several modular multiplications will be done in sequence as, e.g., when computing a modular exponentiation.

Fix an odd modulus $N$ with respect to which modular operations are to be done. Let $R > N$ be a power of two, say $R = 2^w$, and note that $\gcd(R, N) = 1$. The key property we will exploit is that division by $R$ is fast: the quotient of $x$ upon division by $R$ is obtained by simply shifting $x$ to the right $w$ positions, and $[x \bmod R]$ is just the $w$ least-significant bits of $x$.

Define the Montgomery representation of $x \in \mathbb{Z}_N^*$ by $\bar{x} \overset{\mathrm{def}}{=} [xR \bmod N]$. Montgomery multiplication of $\bar{x}, \bar{y} \in \mathbb{Z}_N^*$ is defined as

$$\text{Mont}(\bar{x},\bar{y})\stackrel{\mathrm{def}}{=}[\bar{x}\bar{y}R^{-1}\bmod N].$$

(We show below how this can be computed without any expensive modular reductions.) Note that

$$Mont(\bar{x},\bar{y})=\bar{x}\bar{y}R^{-1}=(x R)(y R)R^{-1}=(x y)R=\overline{x y}\bmod N.$$

This means we can multiply several values in $\mathbb{Z}_N$ by (1) converting to the Montgomery representation, (2) carrying out all multiplications using Montgomery multiplication to obtain the final result, and then (3) converting the result from Montgomery representation back to the standard representation.

Let $\alpha \stackrel{\mathrm{def}}{=} [-N^{-1} \bmod R]$, a value which can be precomputed. (Computation of $\alpha$, and conversion to/from Montgomery representation, can also be done without any expensive modular reductions; details are beyond our scope.) To compute $c \stackrel{\mathrm{def}}{=} \text{Mont}(x, y)$ without any expensive modular reductions do:

1. Let $z := x \cdot y$ (over the integers).

2. Set $c^{\prime} := (z + [z\alpha \bmod R] \cdot N) / R$.

3. If $c^{\prime} < N$ then set $c := c^{\prime}$; else set $c := c^{\prime} - N$.

To see that this works, we first need to verify that step 2 is well-defined, namely, that the numerator is divisible by $R$. This follows because

$$z+[z\alpha\bmod R]\cdot N=z+z\alpha N=z-z N^{-1}N=0\bmod R.$$

Next, note that $c^{\prime} = z/R \bmod N$ after step 2; moreover, since $z < N^2 < RN$ we have ${0} < c^{\prime} < (z + RN)/R < 2RN/R = 2N$. But then $[c^{\prime} \bmod N] = c^{\prime}$ if $c^{\prime} < N$, and $[c^{\prime} \bmod N] = c^{\prime} - N$ if $c^{\prime} > N$. We conclude that

$$c=[c^{\prime}\bmod N]=[z/R\bmod N]=[x y R^{-1}\bmod N],$$

as desired.

### B.2.5 Choosing a Uniform Group Element

For cryptographic applications, it is often necessary to choose a uniform element of a group $\mathbb{G}$. We first treat the problem in an abstract setting, and then focus specifically on the cases of $\mathbb{Z}_N$ and $\mathbb{Z}_N^*$.

Note that if $\mathbb{G}$ is a cyclic group of order $q$, and a generator $g \in \mathbb{G}$ is known, then choosing a uniform element $h \in \mathbb{G}$ reduces to choosing a uniform integer $x \in \mathbb{Z}_q$ and setting $h := g^x$. In what follows we make no assumptions on $\mathbb{G}$.

Elements of a group $\mathbb{G}$ must be specified using some representation of these elements as bit-strings, where we assume without any real loss of generality that all elements are represented using strings of the same length. (It is also crucial that there is a unique string representing each group element.) For example, if $\|N\| = n$ then elements of $\mathbb{Z}_N$ can all be represented as strings of length $n$, where the integer $a \in \mathbb{Z}_N$ is padded to the left with ${0}s$ if $\|a\| < n$.

We do not focus much on the issue of representation, since for all the groups considered in this text the representation can simply be taken to be the “natural” one (as in the case of $\mathbb{Z}_N$, above). Note, however, that different representations of the same group can affect the complexity of performing various computations, and so choosing the “right” representation for a given group is often important in practice. Since our goal is only to show polynomial-time algorithms for each of the operations we need (and not to show the most efficient algorithms known), the exact representation used is less important for our purposes. Moreover, most of the “higher-level” algorithms we present use the group operation in a “black-box” manner, so that as long as the group operation can be performed in polynomial time (in some parameter), the resulting algorithm will run in polynomial time as well.

Given a group $\mathbb{G}$ where elements are represented by strings of length $\ell$, a uniform group element can be selected by choosing uniform $\ell$-bit strings until the first string that corresponds to a group element is found. (Note this assumes that testing group membership can be done efficiently.) To obtain an algorithm with bounded running time, we introduce a parameter $t$ bounding the maximum number of times this process is repeated; if all $t$ iterations fail to find an element of $\mathbb{G}$, then the algorithm outputs fail. (An alternative is to output an arbitrary element of $\mathbb{G}$.) That is:

ALGORITHM B.14
Choosing a uniform group element

Input: A (description of a) group $\mathbb{G}$; length-parameter $\ell$; parameter $t$
Output: A uniform element of $\mathbb{G}$
for $i = 1$ to $t$:
Choose uniform $x \in \{0,1\}^{\ell}$
if $x \in \mathbb{G}$ return $x$
return "fail"

It is clear that whenever the above algorithm does not output fail, it outputs a uniformly distributed element of $\mathbb{G}$. This is simply because each element of $\mathbb{G}$ is equally likely to be chosen in any iteration. Formally, if we let $\mathsf{Fail}$ be the event that the algorithm outputs fail, then for any element $g \in \mathbb{G}$ we have

$$\Pr\left[\text{output of the algorithm equals }g\mid\overline{\mathsf{Fail}}\right]=\frac{1}{|\mathbb{G}|}.$$

What is the probability that the algorithm outputs fail? In any iteration the probability that $x \in \mathbb{G}$ is exactly $|\mathbb{G}|/2^\ell$, and so the probability that $x$ does not lie in $\mathbb{G}$ in any of the $t$ iterations is

$$\left(1-\frac{|\mathbb{G}|}{2^\ell}\right)^{t}.$$

There is a trade-off between the running time of Algorithm B.14 and the probability that the algorithm outputs fail: increasing $t$ decreases the probability of failure but increases the worst-case running time. For cryptographic applications we need an algorithm where the worst-case running time is polynomial in the security parameter $n$, while the failure probability is negligible in $n$. Let $K \stackrel{\mathrm{def}}{=} 2^{\ell}/|\mathbb{G}|$. If we set $t := K \cdot n$ then the probability that the algorithm outputs fail is:

$$\left(1-\frac{1}{K}\right)^{K\cdot n}=\left(\left(1-\frac{1}{K}\right)^{K}\right)^{n}\leq\left(e^{-1}\right)^{n}=e^{-n},$$

using Proposition A.2. Thus, if $K = \mathsf{poly}(n)$ (we assume some group-generation algorithm that depends on the security parameter $n$, and so both $|\mathbb{G}|$ and $\ell$ are functions of $n$), we obtain an algorithm with the desired properties.

The case of $\mathbb{Z}_N$. Consider the group $\mathbb{Z}_N$, with $n = \|N\|$. Checking whether an $n$-bit string $x$ (interpreted as a positive integer of length at most $n$) is an element of $\mathbb{Z}_N$ simply requires checking whether $x < N$. Furthermore,

$$\frac{2^{n}}{\left|\mathbb{Z}_{N}\right|}=\frac{2^{n}}{N}\leq\frac{2^{n}}{2^{n-1}}=2,$$

and so we can sample a uniform element of $\mathbb{Z}_N$ in $\mathsf{poly}(n)$ time and with failure probability negligible in $n$.

The case of $\mathbb{Z}_N^*$. Consider next the group $\mathbb{Z}_N^*$, with $n = \|N\|$ as before. Determining whether an $n$-bit string $x$ is an element of $\mathbb{Z}_N^*$ is also easy (see the exercises). Moreover,

$$\frac{2^{n}}{\left|\mathbb{Z}_{N}^{*}\right|}=\frac{2^{n}}{\phi(N)}=\frac{2^{n}}{N}\cdot\frac{N}{\phi(N)}\leq2\cdot\frac{N}{\phi(N)}.$$

A $\mathsf{poly}(n)$ upper-bound is a consequence of the following theorem.

THEOREM B.15 For $N \geq 3$ of length $n$, we have $\frac{N}{\phi(N)} < 2n$.

(Stronger bounds are known, but the above suffices for our purpose.) The theorem can be proved using Bertrand's Postulate (Theorem 9.32), but we content ourselves with a proof in two special cases: when $N$ is prime and when $N$ is a product of two equal-length (distinct) primes.

The analysis is easy when $N$ is an odd prime. Here $\phi(N) = N - 1$ and so

$$\frac{N}{\phi(N)}\leq\frac{2^{n}}{\phi(N)}=\frac{2^{n}}{N-1}\leq\frac{2^{n}}{2^{n-1}}=2$$

(using the fact that $N$ is odd for the second inequality). Consider next the case of $N = pq$ for $p$ and $q$ distinct, odd primes. Then

$$\frac{N}{\phi(N)}=\frac{pq}{(p-1)(q-1)}=\frac{p}{p-1}\cdot\frac{q}{q-1}<\left(\frac{3}{2}\right)\cdot\left(\frac{5}{4}\right)<2.$$

We conclude that when $N$ is prime or the product of two distinct, odd primes, there is an algorithm for generating a uniform element of $\mathbb{Z}_N^*$ that runs in time polynomial in $n = \|N\|$ and outputs fail with probability negligible in $n$.

Throughout this book, when we speak of sampling a uniform element of $\mathbb{Z}_N$ or $\mathbb{Z}_N^*$ we simply ignore the negligible probability of outputting fail with the understanding that this has no significant effect on the analysis.

## B.3 *Finding a Generator of a Cyclic Group

In this section we address the problem of finding a generator of an arbitrary cyclic group $\mathbb{G}$ of order $q$. Here, $q$ does not necessarily denote a prime number; indeed, finding a generator when $q$ is prime is trivial by Corollary 9.56.

We actually show how to sample a uniform generator, proceeding in a manner very similar to that of Section B.2.5. Here, we repeatedly sample uniform elements of $\mathbb{G}$ until we find an element that is a generator. As in Section B.2.5, an analysis of this method requires understanding two things:

- How to efficiently test whether a given element is a generator; and

- the fraction of group elements that are generators.

In order to understand these issues, we first develop a bit of additional group-theoretic background.

### B.3.1 Group-Theoretic Background

We tackle the second issue first. Recall that the order of an element $h$ is the smallest positive integer $i$ for which $h^{i} = 1$. Let $g$ be a generator of a group $\mathbb{G}$ of order $q > 1$; this means the order of $g$ is $q$. Consider an element $h \in \mathbb{G}$ that is not the identity (the identity cannot be a generator of $\mathbb{G}$), and let us ask whether $h$ might also be a generator of $\mathbb{G}$. Since $g$ generates $\mathbb{G}$, we can write $h = g^x$ for some $x \in \{1, \ldots, q-1\}$ (note $x \neq 0$ since $h$ is not the identity). Consider two cases:

Case 1: $\gcd(x,q) = r > 1$. Write $x = \alpha \cdot r$ and $q = \beta \cdot r$ with $\alpha, \beta$ non-zero integers less than q. Then:

$$h^{\beta}=\left(g^{x}\right)^{\beta}=g^{\alpha r\beta}=\left(g^{q}\right)^{\alpha}=1.$$

So the order of $h$ is at most $\beta < q$, and $h$ cannot be a generator of $\mathbb{G}$.

Case 2: $\gcd(x, q) = 1$. Let $i \leq q$ be the order of $h$. Then

$$g^{0}=1=h^{i}=\left(g^{x}\right)^{i}=g^{x i},$$

implying $xi = 0 \bmod q$ by Proposition 9.54. This means that $q \mid xi$. Since $\gcd(x, q) = 1$, however, Proposition 9.3 shows that $q \mid i$ and so $i = q$. We conclude that $h$ is a generator of $\mathbb{G}$.

Summarizing the above, we see that for $x \in \{1, \ldots, q-1\}$ the element $h = g^x$ is a generator of $\mathbb{G}$ exactly when $\gcd(x, q) = 1$. We have thus proved the following:

THEOREM B.16 Let $\mathbb{G}$ be a cyclic group of order $q > 1$ with generator $g$. There are $\phi(q)$ generators of $\mathbb{G}$, and these are exactly given by $\{g^x \mid x \in \mathbb{Z}_q^*\}$.

In particular, if $\mathbb{G}$ is a group of prime order $q$, then it has $\phi(q) = q - 1$ generators—exactly in agreement with Corollary 9.56.

We turn next to the first issue, that of deciding whether a given element $h$ is a generator of $\mathbb{G}$. Of course, one way to check whether $h$ generates $\mathbb{G}$ is to enumerate $\{h^0, h^1, \ldots, h^{q-1}\}$ and see whether this list includes every element of $\mathbb{G}$. This requires time linear in $q$ (i.e., exponential in $\|q\|$) and is therefore unacceptable for our purposes. Another approach, if we already know a generator $g$, is to compute the discrete logarithm $x = \log_g h$ and then apply the previous theorem; in general, however, we may not have such a $g$, and anyway computing the discrete logarithm may itself be a hard problem.

If we know the factorization of q, we can do better.

PROPOSITION B.17 Let $\mathbb{G}$ be a group of order $q$, and let $q = \prod_{i=1}^{k} p_{i}^{e_{i}}$ be the prime factorization of $q$, where the $\{p_{i}\}$ are distinct primes and $e_{i} \geq 1$. Set $q_{i} = q/p_{i}$. Then $h \in \mathbb{G}$ is a generator of $\mathbb{G}$ if and only if

$$h^{q_{i}}\neq1\quad\text{ for }i=1,\ldots,k.$$

PROOF One direction is easy. Say $h^{q_i} = 1$ for some $i$. Then the order of $h$ is at most $q_i < q$, and so $h$ cannot be a generator.

Conversely, say $h$ is not a generator but instead has order $q^{\prime} < q$. By Proposition 9.55, we know $q^{\prime} \mid q$. This implies that $q^{\prime}$ can be written as $q^{\prime} = \prod_{i=1}^{k} p_i^{e_i^{\prime}}$, where $e_i^{\prime} \geq 0$ and for at least one index $j$ we have $e_j^{\prime} < e_j$. But then $q^{\prime}$ divides $q_j = p_j^{e_j - 1} \cdot \prod_{i \neq j} p_i^{e_i}$, and so (using Proposition 9.54) $h^{q_j} = h^{[q_j \bmod q^{\prime}]} = h^0 = 1$.

The proposition does not require $\mathbb{G}$ to be cyclic; if $\mathbb{G}$ is not cyclic then every element $h \in \mathbb{G}$ will satisfy $h^{q_i} = 1$ for some $i$ and there are no generators.

### B.3.2 Efficient Algorithms

Armed with the results of the previous section, we show how to efficiently test whether a given element is a generator, as well as how to efficiently find a generator in an arbitrary group.

Testing if an element is a generator. Proposition B.17 immediately suggests an efficient algorithm for deciding whether a given element $h$ is a generator or not.

**ALGORITHM B.18**

Testing whether an element is a generator
Input: Group order $q$; prime factors $\{p_i\}_{i=1}^k$ of $q$; element $h \in \mathbb{G}$
Output: A decision as to whether $h$ is a generator of $\mathbb{G}$
for $i = 1$ to $k$:
    if $h^{q/p_i} = 1$ return “$h$ is not a generator”
return “$h$ is a generator”

Correctness of the algorithm is evident from Proposition B.17. We now show that the algorithm terminates in time polynomial in $\|q\|$. Since, in each iteration, $h^{q/p_i}$ can be computed in polynomial time, we need only show that the number of iterations $k$ is polynomial. This is the case since an integer $q$ can have no more than $\log_2 q = \mathcal{O}(\|q\|)$ prime factors; this is because

$$q=\prod_{i=1}^{k}p_{i}^{e_{i}}\geq\prod_{i=1}^{k}p_{i}\geq\prod_{i=1}^{k}2=2^{k}$$

and so $k \leq \log_{2} q$.

Algorithm B.18 requires the prime factors of the group order $q$ to be provided as input. Interestingly, there is no known efficient algorithm for testing whether an element of an arbitrary group is a generator when the factors of the group order are not known.

The fraction of elements that are generators. As shown in Theorem B.16, the fraction of elements of a group $\mathbb{G}$ of order $q$ that are generators is $\phi(q)/q$. Theorem B.15 says that $\phi(q)/q = \Omega(1/\|q\|)$. The fraction of elements that are generators is thus sufficiently high to ensure that sampling a polynomial number of elements from the group will yield a generator with all but negligible probability. (The analysis is the same as in Section B.2.5.)

Concrete examples in $\mathbb{Z}_p^*$. Putting everything together, we see there is an efficient probabilistic algorithm for finding a generator of a group $\mathbb{G}$ as long as the factorization of the group order is known. When selecting a group for cryptographic applications, it is therefore important that the group is chosen in such a way that this holds. This explains again the preference, discussed extensively in Section 9.3.2, for working in an appropriate prime-order subgroup of $\mathbb{Z}_p^*$. Another possibility is to use $\mathbb{G} = \mathbb{Z}_p^*$ for $p$ a strong prime (i.e., $p = 2q + 1$ with $q$ also prime), in which case the prime factorization of the group order $p - 1$ is known. One final possibility is to generate a prime $p$ in such a way that the factorization of $p - 1$ is known. Further details are beyond the scope of this book.

## References and Additional Reading

The book by Shoup [183] is highly recommended for those seeking to explore the topics of this chapter in further detail. In particular, bounds on $\phi(N)/N$ (and an asymptotic version of Theorem B.15) can be found in [183, Chapter 5]. Hankerson et al. [91] also provide extensive detail on the implementation of number-theoretic algorithms for cryptography.

## Exercises

B.1 Prove correctness of the extended Euclidean algorithm.

B.2 Prove that the extended Euclidean algorithm runs in time polynomial in the lengths of its inputs.

Hint: First prove a proposition analogous to Proposition B.8.

B.3 Prove that, on input integers $a \geq b > 0$, the extended Euclidean algorithm outputs $(d, X, Y)$ with $|X| \leq b$ and $|Y| \leq a$.

Hint: Use induction on the recursive call.

B.4 Show how to determine that an $n$-bit string is in $\mathbb{Z}_N^*$ in polynomial time.

