"""习题 2.8 / 2.9（附 2.10(a)、2.11）数值验证：按引理 2.5 判定各小方案是否完全保密。

判定准则（引理 2.5 / 式 (2.1)）：方案完全保密 ⟺ 对所有 m、m'、c，
    Pr[Enc_K(m)=c] = Pr[Enc_K(m')=c]
（密钥均匀，概率用分数精确表示）。逐一枚举全部 (m, k)，统计每个 m 的
密文分布并两两比较，与文中手推结论对照。

运行：python solve_ex2_8_2_9.py
"""

from fractions import Fraction


def ciphertext_dist(M, K, enc, m):
    """返回 Pr[Enc_K(m)=c] 的分布（dict: c -> Fraction），密钥均匀。"""
    dist = {}
    for k in K:
        c = enc(k, m)
        dist[c] = dist.get(c, Fraction(0)) + Fraction(1, len(K))
    return dist


def is_perfectly_secret(M, K, enc):
    """按引理 2.5 检查：所有 m 的密文分布是否一致。返回 (bool, 反例)。"""
    dists = {m: ciphertext_dist(M, K, enc, m) for m in M}
    all_c = sorted({c for d in dists.values() for c in d})
    for c in all_c:
        for m in M:
            for m2 in M:
                if dists[m].get(c, Fraction(0)) != dists[m2].get(c, Fraction(0)):
                    return False, (m, m2, c, dists[m].get(c, Fraction(0)),
                                   dists[m2].get(c, Fraction(0)))
    return True, None


def check(name, M, K, enc, expected_secret):
    ok, witness = is_perfectly_secret(M, K, enc)
    status = "完全保密" if ok else "不完全保密"
    assert ok == expected_secret, f"{name}: 计算结果 {ok} 与预期 {expected_secret} 不符"
    print(f"{name}: {status}（与文中结论一致）")
    if not ok:
        m, m2, c, p, p2 = witness
        print(f"    反例：Pr[Enc_K({m})={c}] = {p}  ≠  {p2} = Pr[Enc_K({m2})={c}]")


def main():
    # --- 习题 2.8(a)：M={0..4}, K={0..5} 均匀, Enc=(m+k) mod 5 → 不完全保密
    check("2.8(a) M=Z5, K={0..5}, mod 5",
          list(range(5)), list(range(6)), lambda k, m: (m + k) % 5, False)

    # --- 习题 2.8(b)：M={l 位串且末位 0}, K={0,1}^{l-1}, Enc=m^(k||0) → 完全保密
    ell = 4
    M = [m for m in range(2 ** ell) if m & 1 == 0]          # 末位(LSB)为 0
    K = list(range(2 ** (ell - 1)))
    check(f"2.8(b) l={ell}, 末位恒 0, XOR(k||0)",
          M, K, lambda k, m: m ^ (k << 1), True)

    # --- 习题 2.9：Enc=(m+k) mod 3
    check("2.9(a) M={0,1}, K={0,1}",
          [0, 1], [0, 1], lambda k, m: (m + k) % 3, False)
    check("2.9(b) M=K={0,1,2}",
          [0, 1, 2], [0, 1, 2], lambda k, m: (m + k) % 3, True)
    check("2.9(c) M={0,1}, K={0,1,2}",
          [0, 1], [0, 1, 2], lambda k, m: (m + k) % 3, True)

    # --- 习题 2.10(a)：M={0,1}^{<=l}\{空串}, K={0,1}^l, Enc=k_{|m|}^m → 长度泄露
    ell = 3
    M = [format(m, f"0{n}b") for n in range(1, ell + 1) for m in range(2 ** n)]
    K = list(range(2 ** ell))

    def enc_2_10a(k, m):
        n = len(m)
        k_prefix = k >> (ell - n)                            # k 的前 n 位
        return format(int(m, 2) ^ k_prefix, f"0{n}b")

    check(f"2.10(a) l={ell}, Enc=k_|m|^m",
          M, K, enc_2_10a, False)

    # --- 习题 2.11：剔除全零密钥的 OTP → 不完全保密
    ell = 3
    check(f"2.11   l={ell}, K={{0,1}}^{ell}\\{{0^l}} 的 OTP",
          list(range(2 ** ell)), list(range(1, 2 ** ell)), lambda k, m: m ^ k, False)

    print("\n全部检查通过。")


if __name__ == "__main__":
    main()
