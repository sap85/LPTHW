"""
Given two Roman numerals, return whether the first one is less than the second one:

numcompare("I", "I") => false
numcompare("I", "II") => true
numcompare("II", "I") => false
numcompare("V", "IIII") => false
numcompare("MDCLXV", "MDCLXVI") => true
numcompare("MM", "MDCCCCLXXXXVIIII") => false
"""

dict = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}

def numcompare(x,y):
    first_num =[dict[i] for i in x if i in dict ]
    second_num = [dict[i] for i in y if i in dict ]
    if(sum(first_num) < sum(second_num)):
        print(True)
    else:
        print(False)


numcompare("MM", "MDCCCCLXXXXVIIII")
