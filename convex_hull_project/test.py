print(">> Başlıyoruz...")

from utils.point_generator import generate_random_points

points = generate_random_points(5)

print(">> Üretilen Noktalar:")
for i, p in enumerate(points, 1):
    print(f"{i}. Nokta: {p}")

input(">> Devam etmek için Enter tuşuna bas...")