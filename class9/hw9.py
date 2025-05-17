"""
回家作業1
修改上課的練習程式，當使用者輸入數值時，程式不僅提示再大再小還需要提示縮小過後的輸入範圍
EX:
請輸入0~100的整數:50
再小一點
請輸入0~50的整數:25
再小一點
請輸入0~25的整數:15
再大一點
請輸入15~25的整數:30
再小一點
請輸入15~25的整數:10
再大一點
請輸入15~25的整數:20
再大一點
請輸入20~25的整數:23
再大一點
請輸入23~25的整數:24
恭喜猜中!
"""

import random

a = 0
v = 100
i = random.randint(a, v)
f = int(input(f"請輸入{a}~{v}的整數:"))
while f != i:
    if f > i:
        print("在小一點")
        v = f
    else:
        print("在大一點")
        a = f
    f = int(input(f"請輸入{a}~{v}的整數:"))
else:
    print("正確")

juice = ["applejuice", "orangejuice", "grapejuice", "break"]
while True:
    print(f"1.{juice[0]}")
    print(f"2.{juice[1]}")
    print(f"3.{juice[2]}")
    print(f"4.{juice[3]}")
    choice = input("請輸入數字:")
    if choice == "1":
        print(f"{juice[0]}")
    elif choice == "2":
        print(f"{juice[1]}")
    elif choice == "3":
        print(f"{juice[2]}")
    elif choice == "4":
        print(f"{juice[3]}")
        break
    else:
        print("輸入錯誤查無此果汁 請重新輸入")

juice = [
    "apple juice",
    "orange juice",
    "grape juice",
    "cola",
    "water",
    "milk",
    "coffee",
    "tea",
    "soda",
    "beer",
    "break",
]
while True:
    for i in range(len(juice)):
        print(f"{i + 1}.{juice[i]}")
    try:
        n = int(input("請輸入數字:"))
    except:
        print("輸入錯誤查無此果汁 請重新輸入")
        continue
    if n == len(juice):
        print("系統關閉")
        break
    elif 1 <= n <= len(juice):
        print(f"您點的商品是{juice[n - 1]}")
    else:
        print("輸入錯誤查無此果汁 請重新輸入")
