import math
import time

# Define the cone's base as a polygon with N sides and an apex
N = 20  # Number of sides on the base polygon for approximation
radius = 1  # Radius of the cone's base
height = 1  # Height from the base to the apex
vertices = [(math.cos(2 * math.pi / N * i) * radius, -1, math.sin(2 * math.pi / N * i) * radius) for i in range(N)] + [(0, height, 0)]

# Edges from base vertices to apex and between adjacent base vertices
edges = [(i, (i + 1) % N) for i in range(N)] + [(i, N) for i in range(N)]

# Rotation angles
A = B = 0

def rotate_vertex(v, A, B):
    x, y, z = v
    # Rotation around Y axis
    x, z = x * math.cos(B) - z * math.sin(B), x * math.sin(B) + z * math.cos(B)
    # Rotation around X axis
    y, z = y * math.cos(A) - z * math.sin(A), y * math.sin(A) + z * math.cos(A)
    return x, y, z

def project_vertex(v):
    x, y, _ = v
    return int(40 + 20 * x), int(12 - 10 * y)

def clear_screen():
    print("\x1b[2J\x1b[H", end='')

def plot_edge(v1, v2, screen):
    x1, y1 = project_vertex(v1)
    x2, y2 = project_vertex(v2)
    dx = x2 - x1
    dy = y2 - y1
    distance = max(abs(dx), abs(dy))
    if distance == 0:
        if 0 <= x1 < 80 and 0 <= y1 < 24:
            screen[int(y1) * 80 + int(x1)] = '#'
        return
    for i in range(distance + 1):
        x = x1 + dx * i / distance
        y = y1 + dy * i / distance
        if 0 <= x < 80 and 0 <= y < 24:
            screen[int(y) * 80 + int(x)] = '#'

def draw_frame(A, B):
    screen = [' '] * (80 * 24)
    rotated_vertices = [rotate_vertex(v, A, B) for v in vertices]
    for edge in edges:
        plot_edge(rotated_vertices[edge[0]], rotated_vertices[edge[1]], screen)
    for i in range(24):
        print(''.join(screen[i * 80:(i + 1) * 80]))

# Animation loop
while True:
    clear_screen()
    draw_frame(A, B)
    A += 0.04  # Adjust rotation speed if needed
    B += 0.03
    time.sleep(0.1)
