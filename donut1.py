import math

# Initialize variables
A = B = 0

# Clear the screen
print("\x1b[2J")

while True:
    # Create a buffer for the frame
    z = [0] * 1760
    b = [" "] * 1760

    # Precompute sin/cos values
    sin, cos = math.sin, math.cos

    # Generate the donut
    for j in range(0, 628, 7):  # theta
        for i in range(0, 628, 2):  # phi
            c = sin(i / 100)
            d = cos(j / 100)
            e = sin(A)
            f = sin(j / 100)
            g = cos(A)
            l = cos(i / 100)
            m = cos(B)
            n = sin(B)
            h = d + 2
            D = 1 / (c * h * e + f * g + 5)
            t = c * h * g - f * e
            x = int(40 + 30 * D * (l * h * m - t * n))
            y = int(12 + 15 * D * (l * h * n + t * m))
            o = x + 80 * y
            N = int(8 * ((f * e - c * d * g) * m - c * d * e - f * g - l * d * n))
            if 0 < x < 80 and 0 < y < 22 and D > z[o]:
                z[o] = D
                b[o] = ".,-~:;=!*#$@"[N if N > 0 else 0]

    # Print the frame
    print("\x1b[H")
    for i in range(0, 1760, 80):
        print(''.join(b[i:i+80]))

    # Update angles for rotation
    A += 0.02
    B += 0.02
