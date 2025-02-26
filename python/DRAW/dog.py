import turtle

def draw_filled_circle(t, x, y, radius, fillcolor="", pencolor="black"):
    """
    在 (x, y) 处以圆心为基准，画一个填充圆
    :param t:        turtle 对象
    :param x, y:     圆心坐标
    :param radius:   半径
    :param fillcolor 填充颜色
    :param pencolor: 画笔颜色
    """
    t.penup()
    t.goto(x, y - radius)   # 先移动到圆心正下方，便于 circle() 沿当前位置逆时针画圆
    t.setheading(0)
    t.pendown()
    t.color(pencolor, fillcolor)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()
    t.penup()

def draw_ear(t, x, y, radius=30, extent=180, fillcolor="saddlebrown"):
    """
    画一个简单的“耳朵”形状：从 (x, y) 出发，画一个弧线并回到原点。
    :param x, y:      耳朵根部坐标
    :param radius:    弧形半径
    :param extent:    弧形角度
    :param fillcolor: 填充颜色
    """
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(fillcolor, fillcolor)
    t.begin_fill()
    # 画一个半圆（或部分圆），模拟垂下来的耳朵
    t.setheading(100)       # 根据需要调整画弧的方向
    t.circle(radius, extent)
    t.goto(x, y)            # 回到开始位置，封闭图形
    t.end_fill()
    t.penup()

def draw_eye(t, x, y, radius=5):
    """
    画一个小圆眼睛
    :param x, y:   圆心坐标
    :param radius: 眼睛半径
    """
    draw_filled_circle(t, x, y, radius, fillcolor="black", pencolor="black")

def draw_nose(t, x, y, radius=7):
    """
    画鼻子
    :param x, y:   鼻子圆心坐标
    :param radius: 鼻子大小
    """
    draw_filled_circle(t, x, y, radius, fillcolor="black", pencolor="black")

def draw_mouth(t, x, y):
    """
    画一个简单的嘴巴弧线
    :param x, y: 嘴巴起始坐标（尽量接近鼻子下方）
    """
    t.penup()
    t.goto(x, y)
    t.setheading(-45)   # 调整弧线方向
    t.pendown()
    t.color("black")
    t.width(2)
    # 画一条小弧线作为嘴巴
    t.circle(20, 90)    # 半圆或者 90 度弧都可以
    t.penup()

def draw_leg(t, x, y, width=8, height=40, fillcolor="sandybrown"):
    """
    画一个矩形腿
    :param x, y:      腿的左上角坐标（或根据需要调整为脚的起点）
    :param width:     腿的宽度
    :param height:    腿的长度
    :param fillcolor: 填充颜色
    """
    t.penup()
    t.goto(x, y)
    t.setheading(0)
    t.pendown()
    t.color(fillcolor, fillcolor)
    t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.right(90)
        t.forward(height)
        t.right(90)
    t.end_fill()
    t.penup()

def main():
    screen = turtle.Screen()
    screen.title("可爱的小狗")
    screen.bgcolor("white")

    t = turtle.Turtle()
    t.speed(3)  # 调整画笔速度

    # -------------------
    # 1. 画狗狗的头
    #    设定头部圆心在 (0, 0), 半径 40
    # -------------------
    head_x, head_y = 0, 0
    head_radius = 40
    draw_filled_circle(t, head_x, head_y, head_radius,
                       fillcolor="sandybrown", pencolor="black")

    # -------------------
    # 2. 画左右耳朵
    #    耳朵根部大致在头顶部上方左右各 35 像素
    # -------------------
    draw_ear(t, x=-35, y=head_y + head_radius, radius=30, extent=180,
             fillcolor="saddlebrown")  # 左耳
    draw_ear(t, x= 35, y=head_y + head_radius, radius=30, extent=180,
             fillcolor="saddlebrown")  # 右耳

    # -------------------
    # 3. 画眼睛
    #    眼睛相对于头圆心稍微往上
    # -------------------
    draw_eye(t, head_x - 15, head_y + 15, 5)   # 左眼
    draw_eye(t, head_x + 15, head_y + 15, 5)   # 右眼

    # -------------------
    # 4. 画鼻子
    #    鼻子在圆心略微向下或向上都行，这里设在 (0, 5)
    # -------------------
    draw_nose(t, head_x, head_y + 5, 7)

    # -------------------
    # 5. 画嘴巴
    #    嘴巴可以从鼻子下方一点开始
    # -------------------
    draw_mouth(t, head_x - 10, head_y - 5)

    # -------------------
    # 6. 画身体
    #    为简化，这里用一个大圆表示身体：
    #    身体圆心 (0, -80)，半径 60
    #    使头部和身体略有重叠
    # -------------------
    body_x, body_y = 0, -80
    body_radius = 60
    draw_filled_circle(t, body_x, body_y, body_radius,
                       fillcolor="sandybrown", pencolor="black")

    # -------------------
    # 7. 画四条腿
    #    根据身体最底部 (y = -80 - 60 = -140)，
    #    适当往上或往下一些都可，这里令腿的“左上角”或“参考点”在底部
    # -------------------
    # 前腿（左右稍窄一些），起点靠身体中部靠前
    draw_leg(t, x=-20, y=-140, width=8,  height=40, fillcolor="sandybrown")  # 左前腿
    draw_leg(t, x= 12, y=-140, width=8,  height=40, fillcolor="sandybrown")  # 右前腿

    # 后腿（再往两边一些）
    draw_leg(t, x=-50, y=-140, width=8,  height=40, fillcolor="sandybrown")  # 左后腿
    draw_leg(t, x= 42, y=-140, width=8,  height=40, fillcolor="sandybrown")  # 右后腿

    t.hideturtle()
    turtle.done()

if __name__ == "__main__":
    main()
