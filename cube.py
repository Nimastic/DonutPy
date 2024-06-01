import math
import time

# Cube definition (vertices and edges)
vertices = [(-1, -1, -1), (1, -1, -1), (1, 1, -1), (-1, 1, -1), (-1, -1, 1), (1, -1, 1), (1, 1, 1), (-1, 1, 1)]
edges = [(0, 1), (1, 2), (2, 3), (3, 0), (4, 5), (5, 6), (6, 7), (7, 4), (0, 4), (1, 5), (2, 6), (3, 7)]

# Rotation angles
A = B = 0

def rotate_vertex(v, A, B):
    # Rotation around Y axis, then around X axis
    x, y, z = v
    xz = x * math.cos(B) - z * math.sin(B)
    zx = x * math.sin(B) + z * math.cos(B)
    yz = y * math.cos(A) - zx * math.sin(A)
    zy = y * math.sin(A) + zx * math.cos(A)
    return (xz, yz, zy + 1)  # +1 to avoid division by zero

def project_vertex(v):
    # Orthographic projection
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
    A += 0.03
    B += 0.02
    time.sleep(0.1)
