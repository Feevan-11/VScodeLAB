import turtle
# 'zero': 0,
#     'ra': 1,
#     'sp': 2,
#     'gp': 3,
#     'tp': 4,
#     't0': 5,
#     't1': 6,
#     't2': 7,
#     's0': 8,
#     's1': 9,
#     'a0': 10,
#     'a1': 11,
#     'a2': 12,
#     'a3': 13,
#     'a4': 14,
#     'a5': 15,
#     'a6': 16,
#     'a7': 17,
#     's2': 18,
#     's3': 19,
#     's4': 20,
#     's5': 21,
#     's6': 22,
#     's7': 23,
#     's8': 24,
#     's9': 25,
#     's10': 26,
#     's11': 27,
#     't3': 28,
#     't4': 29,
#     't5': 30,
#     't6': 31
# 设置屏幕
screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.title("小猪fyf")
screen.bgcolor("lightblue")  # 背景颜色

# 创建画笔
pen = turtle.Turtle()
pen.speed(3)  # 画笔速度
pen.pensize(2)
pen.hideturtle()  # 隐藏画笔箭头

# 函数：绘制圆形
def draw_circle(color, x, y, radius):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.color(color)
    pen.begin_fill()
    pen.circle(radius)
    pen.end_fill()

# 函数：绘制椭圆（简化为圆形）
def draw_oval(color, x, y, width, height):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.color(color)
    pen.begin_fill()
    pen.setheading(45)
    for _ in range(2):
        pen.circle(width, 90)
        pen.circle(height, 90)
    pen.end_fill()

# 函数：绘制小猪
def draw_pig():
    # 身体
    draw_circle("pink", 0, -50, 100)

    # 头部
    draw_circle("pink", 0, 80, 60)

    # 左耳朵
    draw_circle("pink", -40, 150, 20)

    # 右耳朵
    draw_circle("pink", 40, 150, 20)

    # 左眼睛
    draw_circle("white", -20, 130, 10)
    draw_circle("black", -20, 135, 5)

    # 右眼睛
    draw_circle("white", 20, 130, 10)
    draw_circle("black", 20, 135, 5)

    # 鼻子
    pen.penup()
    pen.goto(-15, 100)
    pen.pendown()
    pen.color("black")
    pen.begin_fill()
    pen.circle(15)
    pen.end_fill()

    # 嘴巴
    pen.penup()
    pen.goto(-10, 85)
    pen.pendown()
    pen.setheading(-60)
    pen.circle(20, 120)

    # 腿
    draw_circle("pink", 100, 90, 20)
    draw_circle("pink", -90, 90, 20)
    draw_circle("pink",70, -65, 20)
    draw_circle("pink", -50, -65, 20)

    # 尾巴
    pen.penup()
    pen.goto(80, -50)
    pen.pendown()
    pen.color("black")
    pen.width(3)
    pen.setheading(45)
    pen.circle(30, 90)

# 绘制小猪
draw_pig()

# 写字
pen.penup()
pen.goto(0, -200)
pen.pendown()
pen.color("black")
pen.write("姝洁天天开心！", align="center", font=("Arial", 24, "bold"))

# 保持窗口打开
turtle.done()
