import sys 

from truth_table import is_letter

class Node:
    def __init__(self, data=None, right=None, left=None):
        self.data = data
        self.right = right
        self.left = left

    def __str__(self):
        if self.left and self.right:
            return self.left.__str__() + self.right.__str__() + self.data
        elif self.right:
            return self.right.__str__() + self.data
        elif self.left:
            return self.left.__str__() + self.data
        else:
            return self.data

def get_good_rule(a):
    rules = {
        "|": lambda b, a: Node("&", right=Node("!", right=b), left=Node("!", right=a)),
        "&": lambda b, a: Node("|", right=Node("!", right=b), left=Node("!", right=a))
    }

    if a.data in "|&":
        return rules[a.data](a.right, a.left)
    else:
        return Node("!", right=a)

def get_negation_normal_form(formula):
    rules = {
        "&": lambda b, a: Node(i, right=b, left=a),
        "|": lambda b, a: Node(i, right=b, left=a),
        ">": lambda b, a: Node("|", left=Node("!", right=a), right=b),
        "^": lambda b, a: Node("|", right=Node("&", right=b, left=Node("!", right=a)), left=Node("&", right=Node("!", right=b), left=a)),
        "=": lambda b, a: Node("|", 
            right=Node("&", 
                right=Node("!", right=b), 
                left=Node("!", right=a)), 
            left=Node("&", right=b, left=a)),
        "!": lambda a: get_good_rule(a)
    }

    stack = []
    for i in formula:
        if is_letter(i):
            stack.append(Node(i))
        elif i in "&|>^=" and len(stack) > 1:
            stack.append(rules[i](stack.pop(), stack.pop()))
        elif i == "!" and len(stack) > 0:
            stack.append(rules[i](stack.pop()))
    if len(stack) == 1:
        return str(stack[0]).replace("!!", "")

def negation_normal_form(formula):
    old_formula = formula
    updated_formula = get_negation_normal_form(formula)

    while old_formula != updated_formula and updated_formula is not None:
        old_formula = updated_formula
        updated_formula = get_negation_normal_form(old_formula)
    return updated_formula

def make_test(formula, expected):
    print(f"formula == {formula}")
    print(f"EXPECTED: {expected}")
    result = negation_normal_form(formula)
    print(f"MY NNF: {result}")
    print(f"RESULT IS EQUAL TO EXPECTED : {result == expected}")
    print("------------------------")

def main():
    make_test("AB&!", "A!B!|")
    make_test("AB|!", "A!B!&")
    make_test("AB>", "A!B|")
    make_test("AB=", "AB&A!B!&|")
    make_test("AB|C&!", "A!B!&C!|")
    make_test("AB^", "AB!&A!B&|")
    make_test("AB^!", "A!B|AB!|&")
    make_test("AB^!!", "AB!&A!B&|")
    make_test("AB|C&!AB|C&!AB|C", None)

if __name__ == "__main__":
    sys.exit(main())