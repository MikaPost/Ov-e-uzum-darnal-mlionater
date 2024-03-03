# ov e uzum darnal milionater
import time

def chidem(txt):
    f = open(txt)
    return f.readlines()

def funk(a):
    point = 0
    for i in range(len(a)):
        time.sleep(1)
        b = a[i].split("-")
        print(b[0])
        print(*b[1:-1], sep="\n")
        patas = input("choose the correct answer")
        if patas.lower() == b[-1].lower().strip():
            print("THAT'S RIGHT)))))))))))))))))))")
            point += 100
            print("<<<<<<<<<<<<<<<<<<<<you have", point, "$>>>>>>>>>>>>>>>>>")
        else:
            print("I'TS WRONG(((((((((((((((((((((")
            print("<<<<<<<<<<<<<<<<<<<<you have", point, "$>>>>>>>>>>>>>>>>>")
    return point

a = chidem("a.txt")
print(funk(a), "$")





