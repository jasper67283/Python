# 迴圈的 break 可以用來跳出所屬的迴圈,所以判斷break屬於哪個迴圈時,必須要注意縮排
# 例如:

for i in range(5):
    for j in range(5):
        if i == 2 and j == 2:
            break
        print(f"i = {i}, j = {j}")
# 這裡的 break 只能跳出 for j in range(5): 區塊,因為它屬於 for i in range(5): 區塊

while True:
    print("1. applejuice")
    print("2. orangejuice")
    print("3. grapejuice")
    print("4. quit")
    choice = input("請輸入數字:")
    if choice == "1":
        print("applejuice")
    elif choice == "2":
        print("orangejuice")
    elif choice == "3":
        print("grapejuice")
    elif choice == "4":
        break
    else:
        print("輸入錯誤查無此果汁 請重新輸入")
# continue
# 當 continue 出現在 for 迴圈中時，就會跳出 for 迴圈，並且執行 else 的指令
# 例如:

for i in range(5):
    if i == 2:
        continue
    print(i)
# 這裡的 continue 只能跳出 for i in range(5): 區塊,因為它屬於 for i in range(5): 區塊
# 所以輸出的結果是:
# 0
# 1
# 3
# 4

i = 0
while i < 5:
    if i == 2:
        continue
    print(i)
    i = i + 1
# 這裡的 continue 只能跳出 while i < 5: 區塊,因為它屬於 while i < 5: 區塊

n = int(input("請輸入數字: "))
for i in range(n):
    if i % 10 == 0:
        print("休習一下")
        continue
    print(f"第{i}次跳繩")
