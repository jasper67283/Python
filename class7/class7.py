f = int(input("請輸入數字: "))
a = "是質數"
for i in range(2, f):
    if f % i == 0:
        a = "不是質數"

print(f"數字{f}是質數嗎？{a}")

# for ... else
# 當 for 迴圈結束時，執行 else 的指令
# example:
for i in range(5):
    print(i)
else:
    print("for 迴圈正常結束")

# while ... else
# 當 while 迴圈結束時，執行 else 的指令
# example:
i = 0
while i < 5:
    print(i)
    i = i + 1
else:
    print("while 迴圈正常結束")

import time as t

i = -1
f = int(input("請輸入數字: "))
while i < f:
    print(f)
    f = f - 1
    t.sleep(1)
else:
    print("時間到!")
