import turtle

# 设置屏幕
screen = turtle.Screen()
screen.title("糖葫芦和冰激凌")
screen.bgcolor("lightblue")

# 创建一个画笔
pen = turtle.Turtle()
pen.speed(2)  # 设置最快速度
pen.pensize(2)
pen.hideturtle()

def draw_circle(x, y, radius, color):
    pen.penup()
    pen.goto(x, y - radius)
    pen.pendown()
    pen.color(color)
    pen.begin_fill()
    pen.circle(radius)
    pen.end_fill()

def draw_stick(x, y, length):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.color("saddle brown")
    pen.width(5)
    pen.setheading(90)  # 竖直向上
    pen.forward(length)
    pen.width(1)

def draw_haw(x, y, radius, color):
    draw_circle(x, y, radius, color)

def draw_sugar_haw_hanging(x, y, num_haws, spacing, radius, color):
    for i in range(num_haws):
        draw_haw(x, y + i * spacing, radius, color)

def draw_icee_cream(x, y, cone_width, cone_height, scoop_radius, scoop_color):
    # 绘制冰激凌筒
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.color("sienna")
    pen.begin_fill()
    pen.setheading(-60)
    pen.forward(cone_width)
    pen.setheading(60)
    pen.forward(cone_width)
    pen.setheading(-60)
    pen.forward(cone_width)
    pen.end_fill()

    # 绘制冰激凌球
    draw_circle(x, y + cone_height, scoop_radius, scoop_color)
    draw_circle(x + scoop_radius, y + cone_height + scoop_radius, scoop_radius, scoop_color)
    draw_circle(x - scoop_radius, y + cone_height + scoop_radius, scoop_radius, scoop_color)

# 绘制糖葫芦
def draw_sugar_haws():
    # 绘制糖葫芦的棍子
    draw_stick(-200, -50, 200)

    # 绘制糖葫芦的水果
    colors = ["red", "green", "red", "green", "red"]
    start_x = -200
    start_y = 150
    spacing = 40
    radius = 20
    for i, color in enumerate(colors):
        draw_haw(start_x, start_y + i * spacing, radius, color)

# 绘制冰激凌
def draw_ice_cream():
    # 绘制冰激凌筒
    cone_width = 60
    cone_height = 100
    scoop_radius = 30
    scoop_color = "pink"
    ice_cream_x = 100
    ice_cream_y = -150
    draw_icee_cream(ice_cream_x, ice_cream_y, cone_width, cone_height, scoop_radius, scoop_color)

# 调用绘制函数
draw_sugar_haws()
draw_ice_cream()

# 完成绘制
turtle.done()
