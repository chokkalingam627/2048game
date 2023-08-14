import random

class someclass:
    def __init__(self) -> None:
        pass
    def initiate(self, arr:int):
        for k in range(4):
            print(arr[k])
        print("press w to move up")
        print("press s to move down")
        print("press a to move left")
        print("press d to move right")
        print("Enter command :")
        inp = input()
        return inp
    def checkstate(self, arr:int):
        for i in range(4):
            for j in range(4):
                if arr[i][j] == 0:
                    return "game not over"
        return "game over"
    def insertvalue(self,arr:int):
        while True:
            i = random.randint(0,3)
            j = random.randint(0,3)
            if arr[i][j] == 0:
                arr[i][j] = 2
                return 0
    def moveleft(self, arr:int):
        for i in range(4):
            a = []
            c = 0
            for j in range(4):
                if arr[i][j] != 0:
                    a.append(arr[i][j])
                    c = c + 1
            if c == 0:
                continue
            for j in range(c):
                if j == c - 1:
                    break
                if a[j] == a[j+1]:
                    a[j] = 2 * a[j]
                    a[j+1] = 0
            d = 0
            for j in range(c):
                if a[j] != 0:
                    arr[i][d] = a[j]
                    d = d + 1
            for j in range(d,4):          
                arr[i][j] = 0
        pass
    def moveright(self, arr:int):
        for i in range(4):
            a = []
            c = 0
            for j in range(4):
                if arr[i][j] != 0:
                    a.append(arr[i][j])
                    c = c + 1
            if c == 0:
                continue
            j = c - 1
            while j > 0:
                if a[j] == a[j-1]:
                    a[j] = 2 * a[j]
                    a[j-1] = 0
                j = j - 1
            j = c - 1
            d = 4
            while j >= 0:
                if a[j] != 0:
                    arr[i][d-1] = a[j]
                    d = d - 1
                j = j - 1
            for j in range(d):          
                arr[i][j] = 0
        pass
    def moveup(self, arr:int):
        for i in range(4):
            a = []
            c = 0
            for j in range(4):
                if arr[j][i] != 0:
                    a.append(arr[j][i])
                    c = c + 1
            print(a)
            if c == 0:
                continue
            for j in range(c):
                if j == c - 1:
                    break
                if a[j] == a[j+1]:
                    a[j] = 2 * a[j]
                    a[j+1] = 0
            print("**",a)
            d = 0
            for j in range(c):
                if a[j] != 0:
                    arr[j][i] = a[j]
                    d = d + 1
                    print("+++",arr[j][i],"+++",j,i)
            print("////////////////////////////////////////////////////////////////")
            for k in range(4):
                print(arr[k])
            print("///////////////////////////////////////////////////////////////")
            for j in range(d,4):          
                arr[j][i] = 0
        print("----------------------------------------------------------------")
        for k in range(4):
            print(arr[k])
        print("----------------------------------------------------------------")
        pass
    def movedown(self, arr:int):
        for i in range(4):
            a = []
            c = 0
            for j in range(4):
                if arr[j][i] != 0:
                    a.append(arr[j][i])
                    c = c + 1
            if c == 0:
                continue
            j = c - 1
            while j > 0:
                if a[j] == a[j-1]:
                    a[j] = 2 * a[j]
                    a[j-1] = 0
                j = j - 1
            j = c - 1
            d = 4
            while j >= 0:
                if a[j] != 0:
                    arr[d-1][i] = a[j]
                    d = d - 1
                j = j - 1
            for j in range(d):          
                arr[j][i] = 0
        pass


def startgame():
    print("")
    a = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    s = someclass()
    print("welcome to 2048")
    while(True):
        status = s.checkstate(a)
        if status == "game over":
            print(status)
            break
        p = s.insertvalue(a)
        command = s.initiate(a)
        if command == "w":
            s.moveup(a)
        elif command == "s":
            s.movedown(a)
        elif command == "a":
            s.moveleft(a)
        elif command == "d":
            s.moveright(a)
        else:
            print("incorrect key")
    ##print(a)

startgame()