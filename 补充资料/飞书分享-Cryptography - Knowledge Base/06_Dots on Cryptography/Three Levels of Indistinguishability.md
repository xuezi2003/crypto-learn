# Three Levels of Indistinguishability

## Definition

对于两个分布 (Distribution) D1 和 D2，不可区分性刻画了两个集合的相似程度。在这里，不可区分性可分为三个层次：计算 (computational) 不可区分、统计 (statistical) 不可区分、完美 (perfect) 不可区分。

- 完美不可区分很容易理解，即分布 D1 和 D2 完全相同。
- 统计不可区分指分布 D1 和 D2 对于无限计算能力 (unbounded) 的敌手 (区分器) 而言，其区分这两个分布的优势是可忽略的。
- 计算不可区分指分布 D1 和 D2 对于多项式时间 (PPT) 的敌手而言，其区分这两个分布的优势是可忽略的。

|  | **敌手能力** | **敌手优势** |
|-|-|-|
| **完美不可区分** | 无限 | 0 |
| **统计不可区分** | 无限 | 可忽略 |
| **计算不可区分** | 概率多项式时间 | 可忽略 |

一个直观的解释是，在计算不可区分中敌手只能观察到整个分布中 (PPT大小) 的一部分。而在统计和完美不可区分中，敌手可以观察到完整的分布。统计不可区分表示了两个分布所有位置的距离之和依旧是可忽略的。

## Example

**计算 vs. 统计不可区分**

对于一个基于离散对数的加密方案 (e.g., Elgamal Encryption)，其所产生密文对于 PPT 敌手不可区分的，而对于无限制敌手而言是可区分的。这是由于无限制敌手可解离散对数难题。因此，Elgamal 加密仅满足计算不可区分，而不满足统计可区分。

**统计 vs. 完美不可区分**

考虑两个分布 D1 和 D2。假设分布 D2 为从 D1 的域中删除一个随机元素得到，且分布 D1 的域大小为 n。此时，分布 D1 和 D2 显然不满足完全不可区分。而由于两分布仅在一个元素上不同，因此其统计距离为 1。敌手优势为 1/n，假设 n > poly(\lambda) 则分布 D1 和 D2 为统计不分区分。

BTW. 统计不可区分 implies 计算不可区分。

## References

1. [Difference between computational and statistical indistinguishabilities](https://crypto.stackexchange.com/questions/11789/difference-between-computational-and-statistical-indistinguishabilities)
2. [Unbounded distinguishers and statistical indistinguishability](https://crypto.stackexchange.com/questions/107844/unbounded-distinguishers-and-statistical-indistinguishability)
3. [Statistical Zero Knowledge](https://www.comp.nus.edu.sg/~prashant/teaching/CS6230/files/notes/lecture06.pdf)
4. [Pesudorandom Generators](https://resources.mpi-inf.mpg.de/departments/d1/teaching/ws10/EG/notes7.pdf)