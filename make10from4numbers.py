import os
import sys
import time
from typing import List

class Solution:
    def calculate(self, arr: List[int]) -> List[str]:
        if len(arr) != 4:
            return None
        number = [arr[0], arr[1], arr[2], arr[3]]
        tmp = ""
        answer = []
        countN1 = self.getCount(number, arr[0])
        countN2 = self.getCount(number, arr[1])
        countN3 = self.getCount(number, arr[2])
        countN4 = self.getCount(number, arr[3])
        number_length = len(number)
        for i, _ in enumerate(number):
            n1 = number[i]
            usedNumber = [0]*4
            usedNumber[0] = n1
            for j in range(number_length):
                n2 = number[j]
                usedNumber[1] = n2
                for k in range(number_length): 
                    n3 = number[k]
                    usedNumber[2] = n3
                    for l in range(number_length):
                        n4 = number[l]
                        usedNumber[3] = n4
                        if self.getCount(usedNumber, n1) == countN1 \
                        and self.getCount(usedNumber, n2) == countN2 \
                        and self.getCount(usedNumber, n3) == countN3 \
                        and self.getCount(usedNumber, n4) == countN4:
                            tmp += self.calculateEx(str(n1), str(n2), str(n3), str(n4), answer)
        return answer
    
    def getCount(self, arr: List[int], x: int) -> int: 
        count = 0
        number_length = len(arr)
        for i in range(number_length):
            if arr[i] == x:
                count += 1
        return count
    
    def calculateEx(self, n1: str, n2: str, n3: str, n4: str, result: List[str]):
        operator = ["+", "-", "*", "/"]
        tmp = ""
        len_operator = len(operator)
        for i in range(len_operator):
            opt1 = operator[i]
            for j in range(len_operator): 
                opt2 = operator[j]
                for k in range(len_operator): 
                    try:
                        opt3 = operator[k]
                        # ((a op1 b) op2 c) op3 d
                        shiki = "((" + n1 + opt1 + n2 + ")" + opt2 + n3 + ")" + opt3 + n4
                        answer = eval(shiki)
                        if answer == 10:
                            tmp += str(answer) + " = " + shiki
                            self.append_anser(str(int(answer)) + " = " + shiki, result)
                        # (a op1 b) op2 (c op3 d)
                        shiki = "(" + n1 + opt1 + n2 + ")" + opt2 + "(" + n3 + opt3 + n4 + ")"
                        answer = eval(shiki)
                        if answer == 10:
                            tmp += str(answer) + " = " + shiki
                            self.append_anser(str(int(answer)) + " = " + shiki, result)
                        # (a op1 (b op2 c)) op3 d
                        shiki = "(" + n1 + opt1 + "(" + n2 + opt2 + n3 + "))" + opt3 + n4
                        answer = eval(shiki)
                        if answer == 10:
                            tmp += str(answer) + " = " + shiki
                            self.append_anser(str(int(answer)) + " = " + shiki, result)
                        # a op1 ((b op2 c) op3 d)
                        shiki = n1 + opt1 + "((" + n2 + opt2 + n3 + ")" + opt3 + n4 + ")"
                        answer = eval(shiki)
                        if answer == 10:
                            tmp += str(answer) + " = " + shiki
                            self.append_anser(str(int(answer)) + " = " + shiki, result)
                        # a op1 (b op2 (c op3 d))
                        shiki = n1 + opt1 + "(" + n2 + opt2 + "(" + n3 + opt3 + n4 + "))"
                        answer = eval(shiki)
                        if answer == 10:
                            tmp += str(answer) + " = " + shiki
                            self.append_anser(str(int(answer)) + " = " + shiki, result)
                    except:
                        continue
        return tmp

    def checkDuplicate(self, array: List[str], targetStr: str) -> bool:
        for i, _ in enumerate(array):
            if targetStr == array[i]:
                return True
        return False

    def append_anser(self, val: str, arr: List[str]):
        if not val in arr:
            arr.append(val)

def main():
    argv = sys.argv
    argc = len(argv)

    if argc < 2:
        print("Usage: python {0} <testdata.txt>".format(argv[0]))
        exit(0)

    if not os.path.exists(argv[1]):
        print("{0} not found...".format(argv[1]))
        exit(0)

    testDataFile = open(argv[1], "r")
    lines = testDataFile.readlines()

    for temp in lines:
        temp = temp.strip()
        if temp == "":
            continue
        print("args = {0}".format(temp))
        loop_main(temp)
    #   print("Hit Return to continue...")
    #   input()

def loop_main(temp):
    flds = temp.replace("\"", "").replace("[", "").replace("]", "").rstrip()
    arr = [int(_) for _ in flds.split(",")]
    print("arr = {0}".format(arr))

    sl = Solution()
    time0 = time.time()

    result = sl.calculate(arr)

    time1 = time.time()

    for i, res in enumerate(result):
        print("result[{0:04d}] ... {1}".format(i, res))

    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
