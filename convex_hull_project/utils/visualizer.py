import matplotlib.pyplot as plt
import streamlit as st

def plot_convex_hull(points, hull_points, title="Convex Hull Visualization"):
    xs, ys = zip(*points)
    plt.figure(figsize=(6, 6))
    plt.scatter(xs, ys, label="Input Points", color="blue")

    # Kapatmak için başa dön
    hull_cycle = hull_points + [hull_points[0]]
    hx, hy = zip(*hull_cycle)
    plt.plot(hx, hy, color="red", linewidth=2, label="Convex Hull")

    plt.title(title)
    plt.legend()
    plt.grid(True)
    st.pyplot(plt)