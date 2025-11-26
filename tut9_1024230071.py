# Q1
import tkinter as tk

root = tk.Tk()
root.title("Robot Control Panel")
root.geometry("500x400")
root.configure(bg="yellow")
root.mainloop()


# Q2
import tkinter as tk

root = tk.Tk()
canvas = tk.Canvas(root, width=300, height=300)
canvas.pack()
canvas.create_oval(98, 98, 102, 102, fill="black")
root.mainloop()


# Q3
import tkinter as tk

root = tk.Tk()
canvas = tk.Canvas(root, width=300, height=300)
canvas.pack()
pts = [(20,50), (100,120), (180,90), (250,150)]
canvas.create_line(pts, fill="blue", width=3)
root.mainloop()


# Q4
import tkinter as tk

root = tk.Tk()
canvas = tk.Canvas(root, width=400, height=200)
canvas.pack()
p = canvas.create_oval(10, 90, 20, 100, fill="red")

def move():
    canvas.move(p, 2, 0)
    root.after(20, move)

move()
root.mainloop()


# Q5
import tkinter as tk

root = tk.Tk()
canvas = tk.Canvas(root, width=400, height=300)
canvas.pack()
canvas.create_rectangle(150,100,250,200, fill="gray")
canvas.create_oval(150,200,180,230, fill="black")
canvas.create_oval(220,200,250,230, fill="black")
root.mainloop()


# Q6
import tkinter as tk

root = tk.Tk()
canvas = tk.Canvas(root, width=400, height=300)
canvas.pack()

r = canvas.create_oval(180,130,200,150, fill="red")

def up(): canvas.move(r,0,-10)
def down(): canvas.move(r,0,10)
def left(): canvas.move(r,-10,0)
def right(): canvas.move(r,10,0)

tk.Button(root,text="Up",command=up).pack()
tk.Button(root,text="Down",command=down).pack()
tk.Button(root,text="Left",command=left).pack()
tk.Button(root,text="Right",command=right).pack()

root.mainloop()


# Q7
import tkinter as tk

root = tk.Tk()
canvas = tk.Canvas(root, width=500, height=400)
canvas.pack()

ball = canvas.create_oval(185,135,215,165, fill="blue")

dx, dy = 3, 3

def animate():
    global dx, dy
    canvas.move(ball, dx, dy)
    x1, y1, x2, y2 = canvas.coords(ball)
    if x1 <= 0 or x2 >= 500: dx = -dx
    if y1 <= 0 or y2 >= 400: dy = -dy
    root.after(20, animate)

animate()
root.mainloop()


# Q8
import tkinter as tk

root = tk.Tk()
canvas = tk.Canvas(root, width=500, height=400)
canvas.pack()

robot = canvas.create_oval(45,195,55,205, fill="red")
x, y = 50, 200

def move():
    global x
    if x < 450:
        canvas.move(robot, 2, 0)
        x += 2
        root.after(20, move)

move()
root.mainloop()


# Q9
import tkinter as tk
import math

root = tk.Tk()
canvas = tk.Canvas(root, width=600, height=500)
canvas.pack()

A = (150,300)
D = (400,300)

L2 = 120
L3 = 150
L4 = 130
theta = math.radians(30)

Bx = A[0] + L2*math.cos(theta)
By = A[1] - L2*math.sin(theta)
B = (Bx, By)

C1x, C1y = B[0], B[1]
C2x, C2y = D[0], D[1]

d = math.dist(B, D)

a = (L3*L3 - L4*L4 + d*d) / (2*d)
h = math.sqrt(abs(L3*L3 - a*a))

Px = B[0] + a*(D[0]-B[0])/d
Py = B[1] + a*(D[1]-B[1])/d

Cx = Px + h*(D[1]-B[1])/d
Cy = Py - h*(D[0]-B[0])/d
C = (Cx, Cy)

canvas.create_line(A[0],A[1],B[0],B[1], fill="red", width=3)
canvas.create_line(B[0],B[1],C[0],C[1], fill="green", width=3)
canvas.create_line(C[0],C[1],D[0],D[1], fill="blue", width=3)
canvas.create_line(A[0],A[1],D[0],D[1], fill="black", width=3)

root.mainloop()


# Q10
import tkinter as tk

root = tk.Tk()
canvas = tk.Canvas(root, width=500, height=400)
canvas.pack()

robot = canvas.create_oval(245,195,255,205, fill="red")

def move(event):
    if event.keysym == "Up": canvas.move(robot,0,-5)
    if event.keysym == "Down": canvas.move(robot,0,5)
    if event.keysym == "Left": canvas.move(robot,-5,0)
    if event.keysym == "Right": canvas.move(robot,5,0)
    x1,y1,x2,y2 = canvas.coords(robot)
    canvas.create_line((x1+x2)/2, (y1+y2)/2, (x1+x2)/2, (y1+y2)/2)

def reset():
    canvas.delete("all")
    globals()["robot"] = canvas.create_oval(245,195,255,205, fill="red")

root.bind("<KeyPress>", move)
tk.Button(root,text="RESET",command=reset).pack()

root.mainloop()
