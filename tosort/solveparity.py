## Solve Parity
def checkio(message):
    ## Variable naming:
    ## [XX,XX,XX] ==> XX is called an elem
    ## 1001 ==> 1,0,0 and 1 are called binaryitem
    ## Filtered out (even parity numbers) are called clean_entry
    ## chr converts a number into ASCII characters
    ## bin converts an integer into binary string
    ## int(XX, 2) converts a binary number into integer
    return ''.join(chr(int(bin(clean_entry)[:-1], 2)) for clean_entry in filter(lambda elem: sum([int(binaryitem) for binaryitem in list(bin(elem)) if binaryitem != 'b']) % 2 == 0, message))
    

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([135, 134, 124, 233,
                    209, 81, 42, 202,
                    198, 194, 229, 215,
                    230, 146, 28, 210,
                    145, 137, 222, 158,
                    49, 81, 214, 157]) == "Checkio"
    assert checkio([144, 100, 200, 202,
                    216, 152, 164, 88,
                    216, 222, 65, 218,
                    175, 217, 248, 222,
                    171, 228, 216, 205,
                    254, 201, 193, 220]) == "Hello World"
