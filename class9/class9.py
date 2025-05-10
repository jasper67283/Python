import random  # 匯入模組random

# random.randrange 設定範圍的方式跟 range 一樣, 特性也一樣不包含最後一個數字
# random.randrange 的功能是從範圍中隨機獲取一個數字
print(random.randrange(10))  # 隨機獲取0~9的數字
print(random.randrange(1, 10))  # 隨機獲取1~9的數字
print(random.randrange(1, 10, 2))  # 隨機獲取1~9的數字，每次隨機獲取2個數字

# random. randint 設定範圍的方式跟 int 一樣, 且包含最後一個數字
# 不能跳過數字
print(random.randint(1, 10))  # 隨機獲取1~10的數字

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

# List 清單 (List)
# List 可以存入很多資料, 每筆資料用ˋ , ˋ隔開
# List 可以存入不同的資料類型, 例如整數、字串、浮點數
# List 最外層用ˋ[]ˋ包起來
L = [1, 2, 3, 4, 5]  # 數字
print(L)
# 不同型態混合
L = [1, "hello", 3.14, True, None]
print(L)

# List 取值
# List 取值方式跟字串一樣, 用ˋ[]ˋ取值
# List 取值方式跟字串一樣, 也可以用ˋ[:]ˋ取值
# List 當中資料的編號(index)都從0開始
L = [1, 2, 3, 4, 5]
print(L[0])  # 取第一筆資料
print(L[1])  # 取第二筆資料
print(L[2])  # 取第三筆資料

# List 取值方式跟字串一樣, 也可以用ˋ[:]ˋ取值
# 設定範圍的方式跟 range 一樣, 特性也一樣不包含最後一個數字
print(L[1:4:2])  # 取第二筆資料至第四筆資料, 每次取2個
print(L[0:3])  # 取第一筆資料至第三筆資料
print(L[:3])  # 取第二筆資料至最後一筆資料
print(L[3:])  # 取第四筆資料至最後一筆資料
print(L[:])  # 取所有資料

# list len 列出列表的長度
L = [1, 2, 3, 4, 5]
print(len(L))  # 列出列表的長度

# 務必不要跟index混淆, 因為index只是當中資料的編號, 不是字串的編號

# len 可以搭配 for 迴圈使用來取得list的所有資料
for i in range(len(L)):  # 這裡的i是index
    print(L[i])

for i in L:  # 這裡的i是資料
    print(i)

# 要使用 for 迴圈取得list的所有資料, 必須要先定義一個可變的變數

Ljuice = ["apple juice", "orange juice", "grape juice"]
print(L[:])
