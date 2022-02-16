import sys 

def isNumber(number):
    return isinstance(number, int) and (number >= 0)

def adder(a, b):
    if isNumber(a) and isNumber(b):
        xor = a ^ b 
        carry = a & b 
        for i in range (0, 32):
            carry <<= 1
            xorTmp = xor 
            carryTmp = carry 
            xor = xorTmp ^ carryTmp 
            carry = xorTmp & carryTmp 
        return xor 

def make_test(a ,b):
    print(f"A == {a} and B == {b}")
    print(f"REAL SUM: {a + b}")
    res = adder(a, b)
    print(f"MY SUM: {res}")
    if mySum is not None:
        print(f"RESULT IS EQUAL TO EXPECTED : {res == a + b}")
    print("------------------------")

def main():
    make_test(42, 42)
    make_test(1, 9)
    make_test(42.42, 24.24)
    make_test(2, -1)
    make_test(3, 7)

if __name__ == "__main__":
    sys.exit(main())