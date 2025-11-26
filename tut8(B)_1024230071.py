# Q1 
import math
def polygon_perimeter(P):
    peri=0
    for i in range (len(P)):
        x1,y1=P[i]
        x2,y2=P[(i+1) % len(P)]
        peri+=math.hypot(x2-x1,y2-y1)
    return peri

P=[(2,1),(5,1),(6,4),(3,6),(1,3)]
print("perimeter=",polygon_perimeter(P))


# Q2
def translate_segment(A,B,tx,ty):
    newA=(A[0]+tx,A[1]+ty)
    newB=(B[0]+tx,B[1]+ty)
    return newA,newB

print(translate_segment((3,2),(7,4),4,-2))


# Q3 
import numpy as np
import math

def rotate_point(P, angle):
    x, y = P
    rad = math.radians(angle)
    R = np.array([[math.cos(rad), -math.sin(rad)],
                  [math.sin(rad),  math.cos(rad)]])
    newP = R @ np.array([x, y])
    return newP

print(rotate_point((4,1),45))


# Q4
import numpy as np

T = np.array([[2,2],[5,6],[7,3]])
R = np.array([[1,0],[0,-1]])
new_T = (R @ T.T).T
print(new_T)


# Q5
import numpy as np

def scale_segment(A,B,factor):
    A = np.array(A)*factor
    B = np.array(B)*factor
    return A, B

print(scale_segment((2,2),(6,5),1.5))


# Q6
def point_on_segment(A,B,P):
    Ax,Ay = A
    Bx,By = B
    Px,Py = P
    
    cross = (Px-Ax)*(By-Ay) - (Py-Ay)*(Bx-Ax)
    if cross != 0:
        return False
    
    dot = (Px-Ax)*(Bx-Ax) + (Py-Ay)*(By-Ay)
    if dot < 0:
        return False
    
    sq_len = (Bx-Ax)**2 + (By-Ay)**2
    return dot <= sq_len

print(point_on_segment((1,1),(5,5),(3,3)))


# Q7
import numpy as np
import math

P = np.array([[0,0],[3,3],[0,2],[0,2]])

# 1. Translate by 3
P1 = P + np.array([3,3])

# 2. Rotate 90° CCW
R = np.array([[0,-1],[1,0]])
P2 = (R @ P1.T).T

print(P2)


# Q8
def polygon_area(P):
    s1 = 0
    s2 = 0
    n = len(P)
    
    for i in range(n):
        x1,y1 = P[i]
        x2,y2 = P[(i+1)%n]
        s1 += x1*y2
        s2 += y1*x2
    
    return abs(s1 - s2) / 2

points = [(1,1),(4,1),(6,4),(3,7),(1,4)]
print(polygon_area(points))


# Q9
def orientation(a,b,c):
    return (b[1]-a[1])*(c[0]-b[0]) - (b[0]-a[0])*(c[1]-b[1])

def intersect(A,B,C,D):
    o1 = orientation(A,B,C)
    o2 = orientation(A,B,D)
    o3 = orientation(C,D,A)
    o4 = orientation(C,D,B)
    
    return (o1*o2 < 0) and (o3*o4 < 0)

print(intersect((0,0),(5,5),(0,5),(5,0)))


# Q10
import numpy as np
import math

def hexagon():
    pts = []
    for i in range(6):
        angle = math.radians(60*i)
        pts.append((3*math.cos(angle),3*math.sin(angle)))
    return np.array(pts)

H = hexagon()

# Rotate 60°
R = np.array([[0.5, -math.sqrt(3)/2],
              [math.sqrt(3)/2, 0.5]])
H_rot = (R @ H.T).T

# Translate by (2,-1)
H_final = H_rot + np.array([2,-1])

print(H_final)