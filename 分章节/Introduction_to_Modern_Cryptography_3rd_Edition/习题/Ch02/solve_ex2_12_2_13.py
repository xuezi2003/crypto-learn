"""习题 2.12 / 2.13：精确枚举验证 PrivK^eav 实验中各敌手的成功概率。

方案：消息空间为 3 字符字符串（字母表 Z_26）。
- 2.12：周期 t=2 固定，密钥 (k1,k2) 均匀（26^2 个）。
- 2.13：周期 t 均匀取自 {1,2,3}，密钥为长 t 的均匀串。

加密规则：c_i = (m_i + key[i mod t]) mod 26（0 基下标，t=2 时第 1、3 位共用 k1）。

概率用 fractions.Fraction 精确计算：
    Pr[PrivK^eav=1] = 1/2 * Pr[A 输出 0 | b=0] + 1/2 * Pr[A 输出 1 | b=1]

预期结果（与文中手推一致）：
- 2.12：1
- 2.13(a)：Pr[0|b=0]=14/39，Pr[1|b=1]=38/39，合计 2/3
- 2.13(b)：Pr[0|b=0]=53/78，Pr[1|b=1]=77/78，合计 5/6

运行：python solve_ex2_12_2_13.py
"""

from fractions import Fraction
from itertools import product

A = 0  # 'a' 的数值


def to_nums(s):
    return [ord(ch) - ord('a') for ch in s]


def enc(m, key):
    """维吉尼亚加密：m 为数值列表，key 为数值元组（周期 t=len(key)）。"""
    t = len(key)
    return tuple((m[i] + key[i % t]) % 26 for i in range(len(m)))


def success_prob(periods, m0, m1, rule):
    """精确计算 Pr[PrivK^eav=1]。

    periods: 周期列表（各以 1/len(periods) 概率选取）；
    m0, m1: 敌手输出的两条消息（字符串）；
    rule: 判定函数 c -> 0/1（敌手看到密文后的输出）。
    """
    m0, m1 = to_nums(m0), to_nums(m1)
    p_out0_given_b0 = Fraction(0)   # Pr[A 输出 0 | b=0]
    p_out1_given_b1 = Fraction(0)   # Pr[A 输出 1 | b=1]
    for t in periods:
        w = Fraction(1, len(periods)) / Fraction(26 ** t)
        for key in product(range(26), repeat=t):
            c0 = enc(m0, key)
            c1 = enc(m1, key)
            if rule(c0) == 0:
                p_out0_given_b0 += w
            if rule(c1) == 1:
                p_out1_given_b1 += w
    total = Fraction(1, 2) * p_out0_given_b0 + Fraction(1, 2) * p_out1_given_b1
    return p_out0_given_b0, p_out1_given_b1, total


def main():
    # --- 习题 2.12：t=2，m0=aaa，m1=aab；c1==c3 输出 0，否则输出 1
    p0, p1, tot = success_prob([2], "aaa", "aab", lambda c: 0 if c[0] == c[2] else 1)
    print(f"2.12   : Pr[输出0|b=0]={p0}, Pr[输出1|b=1]={p1}, Pr[PrivK=1]={tot}")
    assert tot == 1, "2.12 应为 1"

    # --- 习题 2.13(a)：t∈{1,2,3}，m0=aab，m1=abb；c1==c2 输出 0，否则输出 1
    p0, p1, tot = success_prob([1, 2, 3], "aab", "abb", lambda c: 0 if c[0] == c[1] else 1)
    print(f"2.13(a): Pr[输出0|b=0]={p0}, Pr[输出1|b=1]={p1}, Pr[PrivK=1]={tot}")
    assert (p0, p1, tot) == (Fraction(14, 39), Fraction(38, 39), Fraction(2, 3))

    # --- 习题 2.13(b)：t∈{1,2,3}，m0=aaa，m1=abc；c1==c3 输出 0，否则输出 1
    p0, p1, tot = success_prob([1, 2, 3], "aaa", "abc", lambda c: 0 if c[0] == c[2] else 1)
    print(f"2.13(b): Pr[输出0|b=0]={p0}, Pr[输出1|b=1]={p1}, Pr[PrivK=1]={tot}")
    assert (p0, p1, tot) == (Fraction(53, 78), Fraction(77, 78), Fraction(5, 6))

    print("\n全部与文中结论一致：2.12 → 1；2.13(a) → 2/3；2.13(b) → 5/6 > 2/3。")


if __name__ == "__main__":
    main()
