# 不能輸入23以內的數字
f = int(input("請輸入數字1: "))
t = int(input("請輸入數字2: "))
for n in range(f, t + 1):
    if n > 1:
        ans = "是質數"
        for i in range(2, n):
            if n % i == 0:
                ans = "不是質數"
    if ans == "是質數":
        print(n)
