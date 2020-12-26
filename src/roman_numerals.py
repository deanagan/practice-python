

class Solution:
    def int_to_roman(self, num: int) -> str:
        numbers = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        roman = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']

        result = ''

        while num > 0:
            d = next(i for i in numbers if i <= num)
            num -= d
            result += roman[numbers.index(d)]


        return result
