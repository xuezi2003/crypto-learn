# Properties of Different PSI Protocols

# Motivation

We found that PSI protocols have many different properties. Changing one property may change the design of the entire protocol. Therefore, we categorize the properties in various papers and provide a guide for analyzing a PSI protocol.

# The map of PSI

![画板](<./assets/whiteboard_C7zjwNOS.jpg>)
<!-- 飞书画板 token: C7zjwNOSbh2AKdb4kuTcz18NnOg -->

# References

## Survey

- [MAL23,[CSR](https://www.sciencedirect.com/science/article/pii/S1574013723000345)] Private set intersection: A systematic literature review
- [[VCE24](https://eprint.iacr.org/2023/1777),S&P] SoK: Collusion-resistant Multi-party Private Set Intersections in the Semi-honest Model

# Properties of unbalanced PSI from the literature

|  | Tool | Communication cost | Client's computation cost | Servers | Unbalance | Secure Update | Variant |
|-|-|-|-|-|-|-|-|
| [[BMX21](https://eprint.iacr.org/2021/1349.pdf)]One-sided | AHE&DDH | O(NlogN) | O(NlongN) | 1 | N | Y | PSI |
| [[RA21](https://link.springer.com/article/10.1007/s13389-020-00242-7#citeas)] | DH | O(N) | O(n) | 1 | Y | N | PSI |
| [[DIL+22](https://eprint.iacr.org/2021/1349.pdf)] | DPF | O(n) | O(n) | 2 | Y | Y | PSI-CA |
| [[WY23](https://www.usenix.org/system/files/usenixsecurity23-wu-mingli.pdf)] | FHE&DDH | O(nlogN)  | O(n) | 1 | Y | N | PSI-CA |
| Our protocol | DH&DPF | O(n) | O(n) | 2 | Y | Y | PSI/PSI-CA |