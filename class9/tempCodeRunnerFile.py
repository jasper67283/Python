juice = ["apple juice", "orange juice", "grape juice", "cola", "water", "milk", "coffee", "tea", "soda", "beer", "break"]
while True:
    for i in range(len(juice)):
        print(f"{i + 1}.{juice[i]}")
    try:
        n = int(input("請輸入數字:"))
    except :
        print("輸入錯誤查無此果汁 請重新輸入")
        continue
    if n == len(juice):
        print("系統關閉")
        break
    elif 1 <= n <= len(juice):
        print(f"您點的商品是{juice[n - 1]}")
    else:
        print("輸入錯誤查無此果汁 請重新輸入")
        
