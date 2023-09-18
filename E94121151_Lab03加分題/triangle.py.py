a=input("請輸入第一個邊長: ")
b=input("請輸入第二個邊長: ")
c=input("請輸入第三個邊長: ")
if(a==b==c and int(a)>0 and int(b)>0 and int(c)>0):
    print("這是正三角形")
elif(int(a)+int(b)<=int(c) or int(b)+int(c)<=int(a) or int(a)+int(c)<=int(b) ):
    print("這三個邊長不能構成一個合法的三角形")
elif(a==b or b==c or a==c and int(a)-int(c)!=int(b)-int(c) and int(a)>0 and int(b)>0 and int(c)>0):
    print("這是等腰三角形")
else:
    print("這是一個一般的三角形")
    