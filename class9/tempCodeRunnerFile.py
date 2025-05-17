import random

a = 0
v = 100
i = random.randint(a, v)
f = int(input("請輸入數字: "))
while f != i:
    if f > i:
        print("在小一點")
        a = f
    else:
        print("在大一點")
        v = f
    f = input(f"請輸入{a}~{v}的整數:")
    i = random.randint(a, v)
else:
    print("正確")
