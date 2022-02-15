import sys

def sat(formula):
    print(formula)
    
def make_test(formula, expected):
    # print(f"formula == {formula}")
    # print(f"EXPECTED: {expected}")
    res = sat(formula)
    # print(f"MY SAT: {res}")
    # print(f"RESULT IS EQUAL TO EXPECTED : {res == expected}")
    # print("------------------------")


def main():
    print("------------------------")
    make_test("AA!&", False)
    # make_test("ABCD|&^", True)
    # make_test("ab|", None)
    # make_test("AB|", True)


if __name__ == "__main__":
    sys.exit(main())
