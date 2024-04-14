"""
This file is for our new theme: ov e uzum darnal milionater
Create by: Miqayel Postoyan
Date: 15 April
"""
import time

def chidem(txt):
    with open(txt) as fname:
        cnt = fname.readlines()
    return cnt

def write(user, verj):
    points = open("points.txt", "a")
    points.write(user)
    points.write(": ")
    points.write(str(verj))
    points.write(" $")
    points.write("\n")
    points.close()

def funk(ndata):
    point = 0
    for line in range(len(ndata)):
        time.sleep(1)
        ndatas = ndata[line].split("-")
        print(ndatas[0])
        print(*ndatas[1:-1], sep="\n")
        patas = input("choose the correct answer")
        if patas.lower() == ndatas[-1].lower().strip():
            print("THAT'S RIGHT)))))))))))))))))))")
            point += 100
            print("<<<<<<<<<<<<<<<<<<<<you have", point, "$>>>>>>>>>>>>>>>>>")
        else:
            print("I'TS WRONG(((((((((((((((((((((")
            print("<<<<<<<<<<<<<<<<<<<<you have", point, "$>>>>>>>>>>>>>>>>>")
    return point


def main():
    user = input("name")
    ndata = chidem("a.txt")
    verj = funk(ndata)
    print(verj, "$")
    write(user, verj)

if __name__ == "__main__":
    main()