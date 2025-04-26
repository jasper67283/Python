import time as t

i = -1
f = int(input("請輸入數字: "))
while i < f:
    print(f)
    f = f - 1
    t.sleep(1)
else:
    print("時間到!")
