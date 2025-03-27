import tkinter as tk
from tkinter import messagebox  # 修复：正确导入 messagebox
import turtle as t # 导入turtle模块
from time import sleep

# 初始化全局的 Turtle 实例

t.speed(0)

# 创建一个全局的屏幕对象
screen = t.Screen()

# 创建一个全局变量，用于保存最近绘制的图形函数
last_draw_function = None

# 创建一个全局变量，用于保存填充选项的状态
fill_enabled = tk.BooleanVar(value=False)  # 默认不启用填充

def c():
    """清空屏幕"""
    t.clear()  # 清空当前绘图
    t.penup()
    t.home()  # 将乌龟重置到原点

def How_to_use():
    messagebox.showinfo("使用说明", "1. 点击按钮绘制图形\n2. 点击清空按钮清空屏幕\n3. 点击退出按钮退出程序")

'''
def tianchong(t, draw_function):
    """根据选项填充图形"""
    if fill_enabled.get() == True:  # 检查复选框状态
        t.fillcolor("red")  # 设置填充颜色
        t.begin_fill()  # 开始填充
        draw_function(t)  # 调用绘图逻辑
        t.end_fill()  # 结束填充
    else:
        draw_function(t)  # 仅绘制图形，不填充
'''

def draw_square():
    """绘制一个正方形"""
    global t
    c()
    t.speed(0)
    t.penup()
    t.goto(-50, -50)
    t.pendown()
    for _ in range(4):
        t.forward(100)
        t.right(90)

def draw_rectangle():
    """绘制一个矩形"""
    global last_draw_function
    c()
    t.speed(0)
    t.pendown()
    for _ in range(2):
        t.forward(150)
        t.right(90)
        t.forward(100)
        t.right(90)
    
    last_draw_function = draw_rectangle  # 保存当前绘制的图形逻辑

def draw_circle():
    """绘制一个圆形"""
    global last_draw_function
    c()
    t.pendown()
    t.speed(0)
    t.circle(100)
    
    last_draw_function = draw_circle  # 保存当前绘制的图形逻辑

def draw_ellipse():
    """绘制一个椭圆"""
    c()
    screen.clear()
    t.pendown()
    t.speed(0)
    t.penup()
    t.goto(0, -50)
    t.pendown()
    for _ in range(2):
        t.circle(100, 90)  # 半径为100，绘制90度
        t.circle(50, 90)   # 半径为50，绘制90度
    t.done()

def draw_triangle():
    """绘制一个等边三角形"""
    c()
    global last_draw_function
    t.speed(0)
    t.pendown()
    for _ in range(3):
        t.forward(100)
        t.left(120)
    last_draw_function = lambda t: draw_triangle(t)  # 保存当前绘制的图形逻辑

def draw_hexagon():
    """绘制一个六边形"""
    c()
    global last_draw_function
    t.speed(0)
    t.pendown()
    for _ in range(6):
        t.forward(100)
        t.left(60)
    last_draw_function = lambda t: draw_hexagon(t)  # 保存当前绘制的图形逻辑

def sanyecao():
    """绘制三叶草"""
    global t
    c()
    t.speed(0)
    t.pendown()
    t.penup()
    for i in range(3):
        t.goto(0, 0)
        t.setheading(i * 120)
        t.pendown()
        draw_heart()
        t.penup()

def draw_star():
    """绘制一个五角星"""
    c()
    screen.clear()
    t.pendown()
    t.speed(0)
    for _ in range(5):
        t.forward(150)
        t.right(144)
    t.done()

def draw_spiral():
    """绘制一个螺旋线"""
    c()
    screen.clear()
    t.pendown()
    t.speed(0)
    for i in range(100):
        t.forward(i * 2)
        t.right(45)
    t.done()

def draw_spiral_polygon(sides=6):
    """绘制一个螺旋多边形"""
    screen.clear()
    t.speed(0)
    t.pendown()
    angle = 360 / sides
    for i in range(100):
        t.forward(i * 5)
        t.right(angle + 5)
    t.done()

def draw_octagon():
    """绘制一个八边形"""
    global last_draw_function
    c()
    t.pendown()
    t.speed(0)
    for _ in range(8):
        t.forward(100)
        t.left(45)
    
    last_draw_function = draw_octagon  # 保存当前绘制的图形逻辑

def draw_heart1():
    screen.clear() 
    t.pendown()
    t.speed(0)
    
    
    for _ in range(100):
        
        t.clear()
        t.tracer(0)
        for __ in range(3):
            draw_heart()
        t.update()    
        sleep(0.01)
        
        t.right(1)
        
        


def draw_heart():
    """绘制一个心形"""
    t.speed(0)
    t.pendown()
    t.color("green")
    t.begin_fill()
    t.left(50)
    t.forward(133)
    t.circle(50, 200)
    t.right(140)
    t.circle(50, 200)
    t.forward(133)
    t.end_fill()
    t.right(70)

def shu2():
    t.clearscreen()
    t.left(90)
    draw_fractal_tree(100, 30, 10)    

def draw_fractal_tree(tl, ta, ts):
    """绘制分形树"""
    t.pendown()
    
    t.hideturtle()  # 隐藏乌龟
          # 设置最快速度
    
     # 初始方向向上
    t.speed(0)
    if tl >= 3:
        t.pensize(ts)
        t.forward(tl)  # 画树枝
        t.right(ta)  # 右转一定角度
        draw_fractal_tree(tl - 12, ta * 0.8, ts - 1)
        t.left(2 * ta)  # 左转两倍的角度
        draw_fractal_tree(tl - 12, ta * 0.8, ts - 1)
        t.right(ta)  # 右转一定角度
        if tl <= 30:
            t.color("green")
        else:
            t.color("black")
        t.backward(tl)  # 画树枝    

'''
def draw_mandelbrot():
    color = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'purple']
    """绘制曼德布罗集（简单版）"""
    import colorsys
    screen.clear()
    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()
    screen.tracer(0)
    width, height = 800, 800
    screen.setup(width, height)
    screen.setworldcoordinates(-2.5, -2.5, 1.5, 1.5)
    max_iter = 100
    for y in range(-height // 2, height // 2):
        for x in range(-width // 2, width // 2):
            zx, zy = x / (width // 4), y / (height // 4)
            c_val = complex(zx, zy)
            z = 0
            for i in range(max_iter):
                if abs(z) > 2.0:
                    break
                z = z * z + c_val
            color_val = colorsys.hsv_to_rgb(i / max_iter, 1, 1 if i < max_iter else 0)
            t.penup()
            t.goto(zx, zy)
            t.pendown()
            t.dot(2, 'red')
    screen.update()
    turtle.done()
'''

def clear_screen():
    """清空屏幕"""
    screen.clear()

def exit_program():
    """退出程序"""
    try:
        t.bye()  # 关闭turtle窗口
    except t.Terminator:
        pass  # 如果turtle窗口已经关闭，忽略异常
    root.destroy()  # 销毁主窗口，退出程序

def Do_not_click():
    abcdefghijklmn = messagebox.askyesno("警告", "尽量别点确定")
    if abcdefghijklmn == True:
        while True:
            messagebox.showinfo("哈", "哈")
    else:
        messagebox.showinfo("警告", "尽量别点确定")
        while True:
            messagebox.showinfo("哈", "哈")

def fxs(qwerty):
    c()
    draw_fractal_tree(qwerty)

# 创建主窗口
root = tk.Tk()
root.title("画图工具大全v1.0.0")

btn_rectangle = tk.Button(root, text="使用说明（必看）", command=How_to_use)
btn_rectangle.pack(pady=5)

# 添加按钮以触发turtle图形绘制
btn_square = tk.Button(root, text="绘制正方形", command=draw_square)
btn_square.pack(pady=5)

btn_rectangle = tk.Button(root, text="绘制矩形", command=draw_rectangle)
btn_rectangle.pack(pady=5)

btn_circle = tk.Button(root, text="绘制圆形", command=draw_circle)
btn_circle.pack(pady=5)

btn_ellipse = tk.Button(root, text="绘制椭圆", command=draw_ellipse)
btn_ellipse.pack(pady=5)

btn_triangle = tk.Button(root, text="绘制三角形", command=draw_triangle)
btn_triangle.pack(pady=5)

btn_hexagon = tk.Button(root, text="绘制六边形", command=draw_hexagon)
btn_hexagon.pack(pady=5)

btn_star = tk.Button(root, text="绘制五角星", command=draw_star)
btn_star.pack(pady=5)

btn_spiral = tk.Button(root, text="绘制螺旋线", command=draw_spiral)
btn_spiral.pack(pady=5)

btn_octagon = tk.Button(root, text="绘制八边形", command=draw_octagon)
btn_octagon.pack(pady=5)

btn_heart = tk.Button(root, text="绘制三叶草", command=draw_heart1)
btn_heart.pack(pady=5)

btn_spiral_polygon = tk.Button(root, text="绘制螺旋多边形", command=draw_spiral_polygon)
btn_spiral_polygon.pack(pady=5)

btn_fractal_tree = tk.Button(root, text="绘制分形树", command=shu2)
btn_fractal_tree.pack(pady=5)
'''
btn_mandelbrot = tk.Button(root, text="绘制曼德布罗集", command=draw_mandelbrot)
btn_mandelbrot.pack(pady=5)
'''

# 添加清空按钮
btn_clear = tk.Button(root, text="清空屏幕", command=clear_screen)
btn_clear.pack(pady=5)

# 添加退出按钮
btn_exit = tk.Button(root, text="退出程序", command=exit_program)
btn_exit.pack(pady=5)

# 运行主循环
root.mainloop()