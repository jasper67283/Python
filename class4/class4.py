pwd = int(input("請輸入數字: "))
if pwd % 2 == 0:
    print(f"{pwd}是偶數")
else:
    print(f"{pwd}是奇數")

# 匯入模組
# import turtle  # 匯入模組turtle
import turtle as t  # 匯入模組turtle，並將其命名為t

# from turtle import *  # 匯入模組turtle的所有功能
# from turtle import done  # 匯入模組turtle的done函式

# done()
# turtle.done()

t.speed(100)  # 設定速度為1
t.forward(100)  # 向前移動100單位
t.right(90)  # 向右移動90度
t.forward(100)  # 向前移動100單位
t.right(90)  # 向右移動90度
t.forward(100)  # 向前移動100單位
t.right(90)  # 向右移動90度
t.forward(100)  # 向前移動100單位
t.right(90)  # 向右移動90度
# 發現turtle一開始面向右邊
t.done()  # 讓視窗不要關閉

# for example
# for的組成有三個部份
# for 迴圈變數 in 範圍:
# 迴圈變數只能活在for迴圈中
# 迴圈變數每回合都會從範圍中取出一個值
for i in range(6):  # range 可以產生一組數字, 0~5
    print(i)

for i in range(1, 6):  # range = 1~5
    print(i)

for i in range(1, 6, 2):  # range = 1,3 ,5
    print(i)

import turtle as t

for i in range(4):
    t.forward(1000)  # 向前移動100單位
    t.right(90)  # 向右移動90度

t.done()


import turtle

turtle.color("blue")
turtle.shape("turtle")
turtle.stamp()
turtle.penup()
