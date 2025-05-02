f = int(input("請輸入數字1: "))
t = int(input("請輸入數字2: "))
for i in range(f, t + 1):
    for r in range(2, 23 + 1):
        if i % r == 0:
            print(0)
            break
    else:
        print(i)
