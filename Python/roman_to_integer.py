
def roman_to_int(s):
    """
    Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
    Symbol       Value
    I             1
    V             5
    X             10
    L             50
    C             100
    D             500
    M             1000
    For example, two is written as II in Roman numeral, just two ones added together. Twelve is written as, XII,
    which is simply X + II. The number twenty-seven is written as XXVII, which is XX + V + II.
    """
    dic = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    res = dic[s[-1]]
    for i in range(len(s)-1):
        if dic[s[i]] < dic[s[i+1]]:
            res -= dic[s[i]]
        else:
            res += dic[s[i]]
    return res
