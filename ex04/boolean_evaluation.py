import sys 

def eval_formula(formula):
    dic = {
        "!": lambda a: not a,
        "&": lambda b, a: a & b,
        ">": lambda b, a: (not a) | b,
        "=": lambda b, a: b == a,
        "|": lambda b, a: b | a,
        "^": lambda b, a: a ^ b,
    }
    if isinstance(formula, str):
        stack = []
        for i in formula:
            if i in '01':
                stack.append(int(i))
            elif i in "&>=|^" and len(stack) > 1:
                stack.append(dic[i](stack.pop(), stack.pop()))
            elif i in "!" and len(stack) > 0:
                stack.append(dic[i](stack.pop()))
            else:
                return None
        if len(stack) == 1:
            return stack[0]

def make_test(formula, expected):
    print(f"formula == {formula}")
    print(f"EXPECTED: {expected}")
    my_res = eval_formula(formula)
    print(f"MY eval_formula: {my_res}")
    print(f"RESULT IS EQUAL TO EXPECTED : {my_res == expected}")
    print("------------------------")


def main():
    make_test("10&", False)
    make_test("10|", True)
    make_test("11>", True)
    make_test("11^", False)
    make_test("10=", False)
    make_test("10=!", True)
    make_test("1011||=", True)
    make_test("10!", None)
    make_test("1&", None)
    make_test("&10", None)
    make_test("11&0|", True)

if __name__ == "__main__":
    sys.exit(main())