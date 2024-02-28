import random


def estimate_pi(num_points):
    points_inside_circle = 0

    for _ in range(num_points):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)

        if x ** 2 + y ** 2 < 1:
            points_inside_circle += 1

    return 4 * points_inside_circle / num_points


def main():
    num_points = int(input("Syötä arvottavien pisteiden määrä: "))

    estimated_pi = estimate_pi(num_points)

    print("Piin likiarvo on:", estimated_pi)


