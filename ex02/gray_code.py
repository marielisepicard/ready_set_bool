import sys 

def gray_code(n):
    if isinstance(n, int) and n >= 0:
        return n ^ (n >> 1)

def make_test(n, expected):
    print(f"N == {n}, binary == {n:b}")
    print(f"EXPECTED: {expected}, binary == [{expected:b}]")
    myGray = gray_code(n)
    print(f"MY gray_code: {myGray}, binary == [{myGray:b}]")
    if myGray is not None:
        print(f"\nRESULT IS EQUAL TO EXPECTED : {myGray == expected}")
    print("------------------------")


def main():
    make_test(0, 0)
    make_test(1, 1)
    make_test(2, 3)
    make_test(3, 2)
    make_test(4, 6)
    make_test(5, 7)
    make_test(6, 5)
    make_test(7, 4)
    make_test(8, 12)
    make_test(42, 63)
    make_test(999999999, 0b100110010101111010110100000000)

if __name__ == "__main__":
    sys.exit(main())