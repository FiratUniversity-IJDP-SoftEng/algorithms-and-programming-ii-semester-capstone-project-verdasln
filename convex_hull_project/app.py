import streamlit as st
from utils.point_generator import generate_random_points
from algorithms.graham_scan import graham_scan
from utils.visualizer import plot_convex_hull

# Başlık
st.title("Convex Hull Algorithms Comparison Tool 🧠")

# Nokta sayısını seç
num_points = st.slider("Kaç tane rastgele nokta üretmek istiyorsun?", min_value=10, max_value=500, value=100)

# Noktaları üret
points = generate_random_points(num_points)

# Butona basınca algoritmayı çalıştır
if st.button("Graham Scan ile Konveks Kabuğu Hesapla"):
    hull, duration = graham_scan(points)
    st.success(f"Graham Scan algoritması {duration:.6f} saniyede tamamlandı.")
    plot_convex_hull(points, hull, title="Graham Scan - Convex Hull")

# Footer
st.markdown("---")
st.markdown("👨‍💻 Created by [Your Name] | Software Engineering Project")