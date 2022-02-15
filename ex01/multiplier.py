from adder import adder, isNumber

import sys 

def multiplier(a, b):
    if isNumber(a) and isNumber(b):
        res = 0
        for i in range(32):
            if (b & 1):
                res = addOperation(res, a)
            a <<= 1
            b >>= 1
        return res


def make_test(a ,b):
    print(f"A == {a} and B == {b}")
    realMul =  a * b
    print(f"REAL SUM: {realMul}")
    myMul = multiplier(a, b)
    print(f"MY SUM: {myMul}")
    if myMul is not None:
        print(f"RESULT IS EQUAL TO EXPECTED : {realMul == myMul}")
    print("------------------------")


def main():
    make_test(2, 3)
    make_test(4294967200, 100)
    make_test(3, 4)
    make_test(3, 0)
    make_test(999999999, 42)
    make_test(0, 5)
    make_test(3, 7)
    make_test(7, 3)
    make_test(4, 4)
    make_test(7.3, 5.5)
    make_test(0, -5)

if __name__ == "__main__":
    sys.exit(main())

