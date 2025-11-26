# Q1
import math

def distance(A, B):
    return round(math.dist(A, B), 3)

def midpoint(A, B):
    return (round((A[0] + B[0]) / 2, 3),
            round((A[1] + B[1]) / 2, 3))

def line_equation(A, B):
    m = (B[1] - A[1]) / (B[0] - A[0])
    c = A[1] - m * A[0]
    return round(m, 3), round(c, 3)

def reflect_point(A, B, C):
    A2 = A[0] - B[0]
    B2 = A[1] - B[1]
    C2 = A2*C[0] + B2*C[1]
    D2 = A2*A[0] + B2*A[1]
    t = (C2 - D2) / (A2*A2 + B2*B2)
    px = C[0] - A2 * t
    py = C[1] - B2 * t
    return (round(2*px - C[0], 3), round(2*py - C[1], 3))

A = (2, 3)
B = (6, 9)
C = (4, 5)

print("Distance AB =", distance(A, B))
print("Midpoint =", midpoint(A, B))

m, c = line_equation(A, B)
print(f"Line equation: y = {m}x + {c}")

print("Reflection of C =", reflect_point(A, B, C))


# Q2
import math

A = (1, 2)
B = (3, -1)
C = (2, 4)

def mag(V):
    return round(math.hypot(V[0], V[1]), 3)

def dot(U, V):
    return U[0]*V[0] + U[1]*V[1]

def angle(U, V):
    val = dot(U, V) / (math.hypot(U[0],U[1]) * math.hypot(V[0],V[1]))
    return round(math.degrees(math.acos(val)), 3)

R = (A[0] + B[0] + C[0], A[1] + B[1] + C[1])
print(R)

print(mag(A), mag(B), mag(C))

print(dot(A, B), dot(A, C), dot(B, C))

print(angle(A, B), angle(A, C), angle(B, C))

proj_scalar = dot(A, B) / (math.hypot(B[0],B[1])**2)
proj_vec = (round(proj_scalar * B[0], 3), round(proj_scalar * B[1], 3))
print(proj_vec)


# Q3
import math

S = (0, 0)
E = (6, 4)
P = (3, 7)

print(round(math.dist(S, E), 3))

SE = (E[0] - S[0], E[1] - S[1])
SP = (P[0] - S[0], P[1] - S[1])
t = (SE[0]*SP[0] + SE[1]*SP[1]) / (SE[0]**2 + SE[1]**2)
t = max(0, min(1, t))
closest = (round(S[0] + t*SE[0], 3), round(S[1] + t*SE[1], 3))
print(closest)

print(round(math.dist(P, closest), 3))


# Q4
a1, b1, c1 = 2, -1, 5
a2, b2, c2 = 1, 2, 8

det = a1*b2 - a2*b1

if det == 0:
    print("Lines are parallel or coincident.")
else:
    x = (c1*b2 - c2*b1) / det
    y = (a1*c2 - a2*c1) / det
    print((round(x, 3), round(y, 3)))
