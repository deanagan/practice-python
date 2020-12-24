from itertools import takewhile

class Solution:
    def my_atoi(self, s: str) -> int:
        if not s.strip():
            return 0

        e = ''.join(n for _,n in takewhile( lambda ch: ch[1].isnumeric() or (ch[1] in ('+', '-') and ch[0] == 0), enumerate(s.lstrip()) ))

        try:
            fnum = float(e)
        except ValueError:
            return 0

        num = int(fnum)

        if 0 <= num:
            maxint = pow(2,31) - 1
            if num < maxint:
                return num
            else:
                return maxint
        else:
            minint = pow(-2,31)
            if num > minint:
                return num
            else:
                return minint
