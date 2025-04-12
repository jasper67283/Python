import turtle as t

t.shape("turtle")
t.color("blue")
t.speed(0)

for i in range(100):
    t.stamp()
    t.penup()
    t.right(133)
    t.forward(i * 2)

t.done()
