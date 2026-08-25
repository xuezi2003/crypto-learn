"""习题 2.16：同一 8 位密钥重复用于单字符 ASCII 的一次性密码本——暴力枚举验证推导。

允许的明文字符：空格 0x20、大写 A-Z（0x41-0x5A）、小写 a-z（0x61-0x7A）。
同一密钥 k 下 c_i ^ c_j = m_i ^ m_j，故在允许字符集内枚举与所有观察到的
异或关系一致的明文组合即可。

预期（与文中结论一致）：
- (a) 恰有两组解：{空格, 'p'}（次序不定）；
- (b) 唯一解：(空格, 't', 'e')。

运行：python solve_ex2_16.py
"""

CHARSET = [0x20] + list(range(0x41, 0x5B)) + list(range(0x61, 0x7B))  # 空格, A-Z, a-z


def show(ch):
    return "'空格'" if ch == 0x20 else f"'{chr(ch)}'"


def main():
    # --- (a) c1=1011 0111, c2=1110 0111
    c1, c2 = 0b10110111, 0b11100111
    d = c1 ^ c2
    sols = [(m1, m2) for m1 in CHARSET for m2 in CHARSET if m1 ^ m2 == d]
    print(f"(a) c1^c2 = {d:#04x}，满足 m1^m2 = c1^c2 的合法组合共 {len(sols)} 组：")
    for m1, m2 in sols:
        print(f"    m1={show(m1)} (0x{m1:02X}), m2={show(m2)} (0x{m2:02X})")
    assert sorted(sols) == sorted([(0x20, ord('p')), (ord('p'), 0x20)]), "(a) 应恰为 {空格, p}"
    print("    → 结论：明文字符为空格和 'p'，次序无法确定。")

    # --- (b) c1=0110 0110, c2=0011 0010, c3=0010 0011
    c1, c2, c3 = 0b01100110, 0b00110010, 0b00100011
    d12, d13, d23 = c1 ^ c2, c1 ^ c3, c2 ^ c3
    sols = []
    for m1 in CHARSET:
        m2, m3 = m1 ^ d12, m1 ^ d13
        if m2 in CHARSET and m3 in CHARSET and m2 ^ m3 == d23:
            sols.append((m1, m2, m3))
    print(f"\n(b) c1^c2={d12:#04x}, c1^c3={d13:#04x}, c2^c3={d23:#04x}，"
          f"一致的合法三元组共 {len(sols)} 组：")
    for m1, m2, m3 in sols:
        print(f"    m1={show(m1)}, m2={show(m2)}, m3={show(m3)}")
    assert sols == [(0x20, ord('t'), ord('e'))], "(b) 应唯一为 (空格, t, e)"
    print("    → 结论：三条明文依次为空格、't'、'e'（唯一解）。")

    print("\n全部检查通过。")


if __name__ == "__main__":
    main()
