dict0={'index':['國文','英文','數學','自然','社會'],'StuA':['50','60','70','80','90'],'StuB':['57','86','73','82','43'],'StuC':['97','96','86','97','83']}
a=0 
b=0 
c=0 
e=0
n=0 
lis=[['A'],['B'],['C']]
suma=0 
sumb=0 
sumc=0 
item1=list(dict0.items())
while n<4:
    print(item1[n])
    n+=1
n=1
while a<5:
    suma=suma+int(item1[1][1][a])
    a+=1
while b<5:
    sumb=sumb+int(item1[2][1][b])
    b+=1
while c<5:
    sumc=sumc+int(item1[3][1][c])
    c+=1
print(lis[0],"學生的平均成績:",suma/5)
print(lis[1],"學生的平均成績:",sumb/5)
print(lis[2],"學生的平均成績:",sumc/5)
sumchi=0 
sumeng=0 
summat=0 
sumsci=0 
sumsoc=0 
while n<4:
    sumchi=sumchi+int(item1[n][1][0])
    n+=1 
n=1
print("國文平均成績:",sumchi/3)
while n<4:
    sumeng=sumeng+int(item1[n][1][1])
    n+=1 
n=1
print("英文平均成績:",sumeng/3)
while n<4:
    summat=summat+int(item1[n][1][2])
    n+=1 
n=1
print("數學平均成績:",summat/3)
while n<4:
    sumsci=sumsci+int(item1[n][1][3])
    n+=1 
n=1
print("自然平均成績:",sumsci/3)
while n<4:
    sumsoc=sumsoc+int(item1[n][1][4])
    n+=1 
n=1
print("社會平均成績:",sumsoc/3)
