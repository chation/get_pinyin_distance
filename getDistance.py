# codding: utf-8
from xpinyin import Pinyin

def getEditDistance(s, t):
    p = Pinyin()
    s = p.get_pinyin(s, ',', tone_marks='numbers')
    t = p.get_pinyin(t, ',', tone_marks='numbers')
    n = len(s)
    m = len(t)
    if n == 0 :
        return m
    if m == 0 :
        return n
    d = [([0] * (m + 1)) for i in range(n + 1)]
    for i in range(0, n + 1):
        d[i][0] = i
    for j in range(0, m + 1):
        d[0][j] = j
    for i in range(1, n + 1):
        s_i = s[i -1]
        for j in range(1, m + 1):
            t_j = t[j -1]
            cost = 0 if s_i == t_j else 1
            d[i][j] = Minimum(d[i - 1][j] + 1, d[i][j - 1] + 1,
                d[i - 1][j - 1] + cost)
    # print(d)
    return d[n][m]

def Minimum(a, b, c):
    im = a if a < b else b
    return im if im < c else c

if __name__ == "__main__":
    print(getEditDistance('张三','张山'))
