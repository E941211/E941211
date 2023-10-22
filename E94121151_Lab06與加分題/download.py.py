a = int(input("請輸入一個整數："))
b = int(input("請輸入另一個整數："))
h=a
t=b

def gcd(a, b):
    c = min(a, b)
    d = max(a, b)
    if c == 0:
        print("0沒有gcd")
    else:
        if d % c != 0:
            e = c
            c = d % e
            d = e
            return gcd(c,d)
        elif c == 1:
            print(f"{h} 和 {t} 互質")
        else:
            print(f"{h} 和 {t} 的gcd= {c}")

gcd(a, b)


