# while 循環
# 這是條件是迴圈, 當條件成立時會執行一次
i = 1
while i <= 10:
    print(i)
    i = i + 1

# 算術指定運算子
# +=, -=, *=, /=, %=
# x = x + 1 等於 x += 1
# x = x - 1 等於 x -= 1
# x = x * 2 等於 x *= 2
# x = x / 2 等於 x /= 2
# x = x % 2 等於 x %= 2

i = 1
while i <= 10:
    i += 1
    print(i)

pwd = input("請輸入密碼: ")
if pwd == "123":
    print("密碼正確")
