from itertools import count

def checkio(wheat):

    pigeons = {}

    for i in count(1):
        for j in range(1, sum(range(i,0,-1)) + 1):            
            pigeons[j] = pigeons.get(j, 0) + 1
            wheat -= 1
            if wheat == 0:
                return max(pigeons.keys())
                
#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(1) == 1, "1st example"
    assert checkio(2) == 1, "2nd example"
    assert checkio(5) == 3, "3rd example"
    assert checkio(10) == 6, "4th example"
