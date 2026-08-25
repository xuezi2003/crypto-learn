# (Non-)uniformity: An Exploration

> This is a working note from Zhongming, and it may need a verrrrry long time to finish. :(

# Preliminaries

**Notations:**

- $\mathcal{P}$, $\mathcal{Q}$ are two primitives, where P and Q are their implementations, respectively.
- B and A are two PPT adversaries to these two primitives, respectively.

![图片](./assets/images/7422930762200465410.png)
<!-- 飞书原始链接: https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=ODdlYzkyMDhkZjhmN2Q0NDM2MDVkMmU2NzcwYzlhNzVfYmMyM2RlYTZiZmZiNjY4NjlkMDIwMmFmNWM1NzM0ZDBfSUQ6NzQyMjkzMDc2MjIwMDQ2NTQxMF8xNzg1NDYxODg2OjE3ODU0NjU0ODZfVjM -->

# Concepts

**General Construction:** (Construction Mapping Q) There exists a mapping Q(·) such that: if P is an efficient implementation for P, Q(P) is an efficient implementation for Q.

**Fully Black-box Constructions:** (Black-box Construction Q) For every (computationally unbounded) oracle P implementing P, Q P implements Q.

Observation 1: Fully black-box construction of Q treats P as an oracle, where general construction can access its code.

**Uniform security reduction (Existential Security):** If there exists an oracle A who can break Q's security, then there exists B who can break P's security.

**Non-uniform security reduction (Constructive Security):** If there exists an PPT adversary A who can break Q's security, then there exists B who can output an instance to break P's security.

Observation 2: Constructive security requires the reduction algorithm to *output a witness of a hardness problem*, while existential secuirty only requires it exists. This is similar to the difference between a ZKPoK and ZKP.

Note 1 (Why constructive security?): Constructive security was introduced by Rogaway to address the tension between existential security and *unkeyed* hash function. Ideally, a construction using hash function should use a *keyed* hash or unkeyed hash *from a function family*; otherwise, the hash function is non-uniform. For a non-uniform hash, there always exists an efficient algorithm that can output a collision using hardcoded input. To overcome this limitation, constructive security requires the reduction algorithm to outputs a collusion of the hash ultilized in the construction, instead of existence of such adversary.

# Examples

**Non-uniform construction.**

**Non-uniform security reduction.**

**The separation of uniform & non-uniform reduction.**

**The impossibility of implementing RO.**

# References

- [[MRH03](https://eprint.iacr.org/2003/161),TCC] Indifferentiability, Impossibility Results on Reductions, and Applications to the Random Oracle Methodology
- [[Rogaway06](https://eprint.iacr.org/2006/281),VietCrypt] Formalizing human ignorance: Collision-resistant hashing without the keys
- [BU08,[ASIACRYPT](https://www.iacr.org/archive/asiacrypt2008/53500293/53500293.pdf)] Limits of Constructive Security Proofs
- [CMLP13,[ITCS](https://www.cs.cornell.edu/~rafael/papers/nonuniform-camera.pdf)] On the Power of Non-uniformity in Proofs of Security