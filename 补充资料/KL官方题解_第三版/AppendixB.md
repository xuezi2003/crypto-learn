# Appendix B: Basic Algorithmic Number Theory – Solutions

> 来源：*Introduction to Modern Cryptography (3rd Edition)* 官方教师题解（Solutions Manual，**偶数题**）。本文件为 XHTML 原文的手工 Markdown 转写，公式已转为 LaTeX。其中题干与第三版完全一致的**奇数题**，已据第二版官方题解（Solutions Manual, 2nd Edition）补充。

---

## B.1

> **题目**　Prove correctness of the extended Euclidean algorithm.

**Solution.** We prove correctness by induction on the second input $b$. When $b = 1$ then $b$ always divides $a$ and Algorithm B.10 returns $(b, 0, 1)$. This is correct, since $b = \gcd(a, b)$ and ${0} \cdot a + 1 \cdot b = b$.

Assume correctness of Algorithm B.10 for all (positive) values of $b$ up to some bound $B$; we prove that correctness holds for $b = B + 1$. Consider an execution of $\mathsf{eGCD}(a, b)$. If $b \mid a$ then the algorithm returns $(b, 0, 1)$ and this is a correct solution (as above). Otherwise, the algorithm makes a recursive call to $\mathsf{eGCD}(b, r)$ with $r = [a \bmod b]$. Note that ${0} < r < b$. By our inductive assumption, we know that $\mathsf{eGCD}(b, r)$ outputs $(d, X, Y)$ with $d = \gcd(b, r)$ and $Xb + Yr = d$; the final output of the algorithm is $(d, Y, X - Yq)$ where $q$ is such that $a - r = qb$. We can verify correctness of this output as follows:

- Proposition B.6 shows that $d = \gcd(a, b)$.

We have

$$Ya + (X - Yq)b = Ya + Xb - Yqb = Xb + Y(a - qb) = Xb + Yr = d,$$

as required.

---

## B.2

> **题目**　Prove that the extended Euclidean algorithm runs in time polynomial in the lengths of its inputs.

**Solution.** For any given input $(a, b)$, the inputs used in the recursive calls to $\mathsf{eGCD}$ in an execution of Algorithm B.10 are exactly the same as the inputs used in the recursive calls to $\mathsf{GCD}$ in an execution of Algorithm B.7. So the number of recursive calls is identical in each case. Since each recursive step (and, in particular, division-with-remainder) can be done in polynomial time, it follows from Corollary B.9 that the entire algorithm runs in polynomial time.

---

## B.3

> **TODO**　此题为第三版新增习题，第二版无对应。

---

## B.4

> **题目**　Show how to determine that an $n$-bit string is in $\mathbb{Z}_N^*$ in polynomial time.

**Solution.** See Algorithm B.1-S.

**Algorithm B.1-S**

**Determining membership in $\mathbb{Z}_N^*$**

**Input:** Modulus N; integer x

**Output:** Determine whether $x \in \mathbb{Z}_N^*$

**if** $x > N$ or $x = 0$, **return** "no"

**if** $\gcd(x, N) \ne 1$ **return** "no"

**return** "yes"
