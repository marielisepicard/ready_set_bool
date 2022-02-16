import sys 
from boolean_evaluation import eval_formula


def is_letter(letter):
    return letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def get_header(formula):
    dic = {}
    index = 0
    for letter in formula:
        if is_letter(letter) and letter not in dic.keys():
            dic[letter] = index
            index = index + 1
    return dic 

def construct_table(iterable, length):
    # create sets : (0, 1) for each letter
    couples = []
    for item in range(0, length):
        couples.append(tuple(iterable))

    table = [[]]

    for couple in couples:
        table = [x+[y] for x in table for y in couple]
    return table

def make_translation(formula, line, header):
    translation = []
    for elem in formula:
        if is_letter(elem):
            translation.append(str(line[header[elem]]))
        else:
            
            translation.append(elem)
    concat = ''.join(translation)
    return concat
            
def create_truth_table(formula):
    # {'A': 0, 'B': 1, 'C': 2 ...}
    header = get_header(formula)
    # construct an empty truth table
    table = construct_table((0, 1), len(header))

    for index, line in enumerate(table):
        line_formula = make_translation(formula, line, header)
        line_result = eval_formula(line_formula)
        if line_result is not None:
            line.append({True: 1, False: 0}[line_result])
        else:
            print("InputError")
            return None
    header["="] = 0
    return(table)
    print("------------------------")


def make_test(formula):
    create_truth_table(formula)
    
def main():
    make_test("AB&")
    make_test("AB|")
    make_test("AB=")
    make_test("AB^")
    make_test("AB>")
    make_test("X!X&")
    make_test("Y!Y|")
    make_test("ab|")
    make_test("AB!")


if __name__ == "__main__":
    sys.exit(main())