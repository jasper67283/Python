# import turtle as t

# t.speed(1)
# t.pensize(5)
# t.pencolor("blue")
# t.fillcolor("blue")
# t.begin_fill()
# for i in range(5):
#     t.forward(200)
#     t.right(144)
# t.end_fill()
# t.done()
f = int(input("請輸入數字: "))
sum = 0
for i in range(f + 1):
    sum = sum + i
print(sum)

for i in range(1, 10):  # 外層迴圈：控制乘數 (1 到 9)
    for j in range(1, 10):  # 內層迴圈：控制被乘數 (1 到 9)
        print(f"{i} x {j} = {i*j}")
    print()
