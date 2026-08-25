## Index of Common Notation

### General notation

- $:=$ refers to deterministic assignment

- If $S$ is a set, then $x \leftarrow S$ denotes that $x$ is chosen uniformly from $S$

- If $A$ is a randomized algorithm, then $y \leftarrow A(x)$ denotes running $A$ on input $x$ with a uniform random tape and assigning the output to $y$. We write $y := A(x; r)$ to denote running $A$ on input $x$ using random tape $r$ and assigning the output to $y$

- $\wedge$ denotes Boolean conjunction (the AND operator)

- $\vee$ denotes Boolean disjunction (the OR operator)

$\oplus$ denotes the exclusive-or (XOR) operator; this operator can be applied to single bits or entire strings (in the latter case, the XOR is bitwise)

$\{0,1\}^{n}$ is the set of all bit-strings of length $n$

$\{0,1\}^{\leq n}$ is the set of all bit-strings of length at most $n$

$\{0,1\}^{*}$ is the set of all finite bit-strings; $\{0,1\}^{+}$ is the set of all non-empty, finite bit-strings

- ${0}^{n}$ (resp., ${1}^{n}$) denotes the string comprised of n zeroes (resp., n ones)

- $\|x\|$ denotes the length of the binary representation of the (positive) integer $x$, written with leading bit 1. Note that $\log x < \|x\| \leq \log x + 1$

- $|x|$ denotes the length of the binary string x (which may have leading 0s), or the absolute value of the real number x

- $\mathcal{O}(\cdot), \Theta(\cdot), \Omega(\cdot), \omega(\cdot)$ are used for asymptotic running times; see Appendix A.2

- 0x denotes that digits are being represented in hexadecimal

- $x\|y$ and $(x,y)$ are used interchangeably to denote concatenation of the strings x and y

- Pr[X] denotes the probability of event X

- $\log x$ denotes the base-2 logarithm of x

### Cryptographic notation

- n is the security parameter

- PPT stands for “probabilistic polynomial time”

$\mathcal{A}^{\mathcal{O}(\cdot)}$ denotes the algorithm $\mathcal{A}$ with oracle access to $\mathcal{O}$

- k typically denotes a secret key (as in private-key encryption and MACs)

- (pk, sk) denotes a public/private key pair (for public-key encryption and digital signatures)

- $\perp$ denotes a generic error

$\mathsf{negl}(n)$ denotes a negligible function; see Definition 3.4

- poly(n) denotes an arbitrary polynomial

- $\mathsf{Func}_{n}$ denotes the set of functions mapping n-bit strings to n-bit strings

$\mathsf{Perm}_{n}$ denotes the set of bijections on n-bit strings

- IV denotes an initialization vector

### Algorithms and procedures

- G denotes a pseudorandom generator

- $F$ denotes a keyed function that is typically a pseudorandom function or permutation

- (Gen, Enc, Dec) denote the key-generation, encryption, and decryption procedures, respectively, for both private- and public-key encryption. For the case of private-key encryption, when Gen is unspecified then Gen(1^n) outputs a uniform $k \in \{0,1\}^n$

- (Gen, Mac, Vrfy) denote the key-generation, tag-generation, and verification procedures, respectively, for a message authentication code. When Gen is unspecified then $\mathsf{Gen}(1^n)$ outputs a uniform $k \in \{0,1\}^n$

- (Gen, Sign, Vrfy) denote the key-generation, signature-generation, and verification procedures, respectively, for a digital signature scheme

- GenPrime denotes a PPT algorithm that, on input ${1}^{n}$, outputs an n-bit prime except with probability negligible in n

- GenModulus denotes a PPT algorithm that, on input ${1}^{n}$, outputs $(N, p, q)$ where $N = pq$ and (except with negligible probability) $p$ and $q$ are $n$-bit primes

- GenRSA denotes a PPT algorithm that, on input ${1}^n$, outputs (except with negligible probability) a modulus $N$, an integer $e > 0$ with $\gcd(e, \phi(N)) = 1$, and an integer $d$ satisfying $ed = 1 \bmod \phi(N)$

- $\mathcal{G}$ denotes a PPT algorithm that, on input ${1}^n$, outputs (except with negligible probability) a description of a cyclic group $\mathbb{G}$, the group order $q$ (with $\|q\| = n$), and a generator $g \in \mathbb{G}$.

### Number theory

- $\mathbb{Z}$ denotes the set of integers

- $a|b$ means a divides b

- $a\nmid b$ means that a does not divide $b$

- gcd $(a, b)$ denotes the greatest common divisor of a and b

- $[a \bmod b]$ denotes the remainder of a when divided by $b$

- $x_1 = x_2 = \cdots = x_n \mod N$ means that $x_1, \ldots, x_n$ are all congruent modulo $N$

- Note: $x = y \bmod N$ means that $x$ and $y$ are congruent modulo $N$, whereas $x = [y \bmod N]$ means that $x$ is equal to the remainder of $y$ when divided by $N$

- $\mathbb{Z}_N$ denotes the additive group of integers modulo $N$ as well as the set $\{0, \ldots, N-1\}$. Note: in Section 14.3 only, we let $\mathbb{Z}_N$ also refer to the set $\{-\lfloor(N-1)/2\rfloor, \ldots, 0, \ldots, \lfloor N/2\rfloor\}$

$\mathbb{Z}_{N}^{*}$ denotes the multiplicative group of invertible integers modulo $N$ (i.e., those that are relatively prime to $N$)

- $\phi(N)$ denotes the size of $\mathbb{Z}_N^*$

- $G$ and $H$ denote groups

$\mathbb{G}_1 \simeq \mathbb{G}_2$ means that groups $\mathbb{G}_1$ and $\mathbb{G}_2$ are isomorphic. If this isomorphism is given by $f$ and $f(x_1) = x_2$ then we write $x_1 \leftrightarrow x_2$

- $g$ is typically a generator of a group

- $\log_{g}h$ denotes the discrete logarithm of $h$ to the base $g$

- $\langle g\rangle$ denotes the group generated by g

- $p$ and $q$ usually denote primes

- $N$ typically denotes the product of two distinct primes $p$ and $q$ of equal length

- $\mathcal{QR}_{p}$ is the set of quadratic residues modulo p

- $\mathcal{QNR}_{p}$ is the set of quadratic non-residues modulo p

- $\mathcal{J}_{p}(x)$ is the Jacobi symbol of x modulo p

$\mathcal{J}_{N}^{+1}$ is the set of elements with Jacobi symbol +1 modulo N

- $\mathcal{J}_{N}^{-1}$ is the set of elements with Jacobi symbol -1 modulo $N$

$\mathcal{Q N R}_{N}^{+1}$ is the set of quadratic non-residues modulo $N$ having Jacobi symbol $+1$

