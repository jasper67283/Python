import random

i = random.randint(1, 100)
f = int(input("請輸入數字: "))
while f != i:
    if f > i:
        print("在小一點")
    else:
        print("在大一點")
    f = int(input("請輸入數字: "))
else:
    print("正確")