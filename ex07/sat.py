import sys

from truth_table import create_truth_table

def sat(formula):
    table = create_truth_table(formula)
    if table == None:
        return None
    column_lenght = len(table[0])
    row_length = len(table)
    res = 0
    for row in table:
        if row[-1] == 1:
            res = 1
    if res == 1:
        return True
    return False


    
def make_test(formula, expected):
    print(f"formula == {formula}")
    print(f"EXPECTED: {expected}")
    res = sat(formula)
    print(f"MY SAT: {res}")
    print(f"RESULT IS EQUAL TO EXPECTED : {res == expected}")
    print("------------------------")


def main():
    print("------------------------")
    make_test("AA!&", False)
    make_test("ABCD|&^", True)
    make_test("ab|", None)
    make_test("AB|", True)

if __name__ == "__main__":
    sys.exit(main())
