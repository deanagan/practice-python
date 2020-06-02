You are given an expression with numbers, brackets and operators. For this task only the brackets matter. Brackets come in three flavors: "{}" "()" or "[]". Brackets are used to determine scope or to restrict some expression. If a bracket is open, then it must be closed with a closing bracket of the same type. The scope of a bracket must not intersected by another bracket. In this task you should make a decision, whether to correct an expression or not based on the brackets. Do not worry about operators and operands.

Input: An expression with different of types brackets as a string (unicode).

Output: A verdict on the correctness of the expression in boolean (True or False).

Precondition:
There are only brackets ("{}" "()" or "[]"), digits or operators ("+" "-" "*" "/").
0 < len(expression) < 103

import time

def checkio(expression) -> bool:
    bracket_pairs = ('{}', '[]', '()')
    clean = "".join(i if i in ('{','(','[',']',')','}') else '' for i in expression)

    while any(str in clean for str in bracket_pairs):
        clean = clean.replace('()','').replace('[]', '').replace('{}','')

    return len(clean) == 0

def checkio2(expression) -> bool:
    bracket_open = ('{', '[', '(')
    bracket_close = ('}', ']', ')')
    st = []
    for ch in expression:
        if ch in bracket_open:
            st.append(ch)
        elif ch in bracket_close:
            if len(st) > 0 and st[-1] == bracket_open[bracket_close.index(ch)]:
                st.pop()
            else:
                return False
        
    return len(st) == 0

if __name__ == "__main__":
    
    start_time = time.time()
    for reps in range(1000):
        assert checkio2("((5+3)*2+1)") == True, "Simple"
        assert checkio2("{[(3+1)+2]+}") == True, "Different types"
        assert checkio2("(3+{1-1)}") == False, ") is alone inside {}"
        assert checkio2("[1+1]+(2*2)-{3/3}") == True, "Different operators"
        assert checkio2("(({[(((1)-2)+3)-3]/3}-3)") == False, "One is redundant"
        assert checkio2("2+3") == True, "No brackets, no problem"
## Extra tests
        assert checkio2("(3+{1-1)}") == False, "Mismatching brackets"
        assert checkio2("(((([[[{{{3}}}]]]]))))") == False, "Mismatching"
        assert checkio2("(((1+(1+1))))]") == False, "Extra closing at the end"
    print("--- %s milliseconds ---" % ((time.time() - start_time) * 1000))

    start_time = time.time()
    for reps in range(1000):
        assert checkio("((5+3)*2+1)") == True, "Simple"
        assert checkio("{[(3+1)+2]+}") == True, "Different types"
        assert checkio("(3+{1-1)}") == False, ") is alone inside {}"
        assert checkio("[1+1]+(2*2)-{3/3}") == True, "Different operators"
        assert checkio("(({[(((1)-2)+3)-3]/3}-3)") == False, "One is redundant"
        assert checkio("2+3") == True, "No brackets, no problem"
## Extra tests
        assert checkio("(3+{1-1)}") == False, "Mismatching brackets"
        assert checkio("(((([[[{{{3}}}]]]]))))") == False, "Mismatching"
        assert checkio("(((1+(1+1))))]") == False, "Extra closing at the end"
    print("--- %s milliseconds ---" % ((time.time() - start_time) * 1000))
