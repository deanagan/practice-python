import math

def checkio(opacity):
    
    def is_fibo(number):
        m = (5 * number ** 2) 
        p = lambda x: int(math.sqrt(m+x) + 0.5) ** 2
        if any(p(t) == m+t for t in [4, -4]):
            return True
        else:
            return False   
            
    last_opacity = 10000
    for age in range(5000):
        last_opacity = last_opacity - (age if is_fibo(age) else -1)
        if last_opacity == opacity:
            return age
    
    return 'unknown ghost age'

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(10000) == 0, "Newborn"
    assert checkio(9999) == 1, "1 year"
    assert checkio(9997) == 2, "2 years"
    assert checkio(9994) == 3, "3 years"
    assert checkio(9995) == 4, "4 years"
    assert checkio(9990) == 5, "5 years" 
