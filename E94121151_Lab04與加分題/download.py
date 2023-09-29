lis = [["A"],["B"],["C"]]
for n in range(3):
    print("輸入",lis[n][0],"學生成績")
    a = int(input("國文成績: "))
    b = int(input("數學成績: "))
    c = int(input("英文成績: "))
    lis[n].append(a)
    lis[n].append(b)
    lis[n].append(c)
    print("國文:",lis[n][1])
    print("數學:",lis[n][2])
    print("英文:",lis[n][3])
for i in range(3):
    lis[i].append(round((lis[i][1]+lis[i][2]+lis[i][3])/3,1))
    print(lis[i])