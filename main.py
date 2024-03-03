# ov e uzum darnal milionater
import time

def chidem(txt):
    f = open(txt)
    return f.readlines()

def write(user, verj):
    points = open("points.txt", "a")
    points.write(user)
    points.write(": ")
    points.write(str(verj))
    points.write(" $")
    points.write("\n")
    points.close()

def funk(a):
    point = 0
    for i in range(len(a)):
        # time.sleep(2)
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

user = input("name")
a = chidem("a.txt")
verj = funk(a)
print(verj, "$")
write(user, verj)

