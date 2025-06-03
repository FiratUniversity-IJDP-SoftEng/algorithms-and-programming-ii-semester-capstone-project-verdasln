import random

def generate_random_points(n, xmin=0, xmax=1000, ymin=0, ymax=1000):
    points = []
    for _ in range(n):
        x = random.randint(xmin, xmax)
        y = random.randint(ymin, ymax)
        points.append((x, y))
    return points

## generate_random_points(n) fonksiyonu, n adet rastgele nokta üretir.
## Noktalar (x, y) formatında birer tuple olarak döner.
## Koordinatlar 0 ile 1000 arasında rastgele sayılardır.

