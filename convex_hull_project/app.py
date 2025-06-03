import streamlit as st
import matplotlib.pyplot as plt
from utils.algorithms import graham_scan, jarvis_march, quickhull
import random

st.title("Convex Hull Algorithm Comparison")

# Rastgele nokta üret
def generate_points(num_points=10):
    return [(random.randint(0, 100), random.randint(0, 100)) for _ in range(num_points)]

points = generate_points()

# Algoritma seçimi
algorithm = st.selectbox("Choose an algorithm", ["Graham Scan", "Jarvis March", "QuickHull"])

# Algoritmayı uygula
if algorithm == "Graham Scan":
    hull = graham_scan(points)
elif algorithm == "Jarvis March":
    hull = jarvis_march(points)
else:
    hull = quickhull(points)

# Görselleştirme
x_points, y_points = zip(*points)
hx, hy = zip(*hull + [hull[0]])

fig, ax = plt.subplots()
ax.plot(x_points, y_points, 'o', label='Points')
ax.plot(hx, hy, 'r-', label='Convex Hull')
ax.legend()
st.pyplot(fig)
