
# This puzzle requires the number of pawns are safe.
# For a pawn to be safe, it must have a supporting pawn with
# a location that is adjacent to its letter and is 1 number below.

import string

def safe_pawns(pawns):
    def get_adjacent_block(pawn):
        unfiltered_adjacent_blocks = [chr(ord(pawn[0].lower()) + adj ) + chr(ord(pawn[1])-1) for adj in range(-1,2) if adj != 0]
        return [f for f in filter(lambda adjpawn : all([len(adjpawn) == 2,
                                               adjpawn[0] in string.ascii_lowercase[:9],
                                               adjpawn[1] in string.digits[1:-1] ]), unfiltered_adjacent_blocks)]

    return (len([t for t in [get_adjacent_block(p) for p in pawns] if bool(set(t).intersection(pawns))]))
        
    
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
