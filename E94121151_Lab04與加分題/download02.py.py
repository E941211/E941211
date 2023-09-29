a = int(input("串列的長度: "))
n = 0
lis = []
while len(lis) < a:
    value = input("輸入文字，以逗號間隔: ").split(",")
    lis.append(value) 
print("輸入的list為:",lis)
clc = int(input("輸入刪除值: "))
print("要刪除的值",clc,"刪除後")
while n < len(lis):
    inner_n = 0
    while inner_n < len(lis[n]):
        if int(lis[n][inner_n]) == clc:
            lis.pop(n)
            break
        inner_n += 1
    else:
        n += 1
print("刪除後list:", lis, "刪除後list的長度:", len(lis))