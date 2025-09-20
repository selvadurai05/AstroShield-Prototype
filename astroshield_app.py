import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import time

# --- Page Config ---
st.set_page_config(page_title="AstroShield Prototype", page_icon="☄️", layout="wide")

# --- Title ---
st.markdown("<h1 style='text-align: center; color: #FF4B4B;'>☄️ AstroShield – Asteroid Impact Simulation</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size:18px;'>Prototype Demo – NASA Space Apps Challenge 2025 (Jabalpur Edition)</p>", unsafe_allow_html=True)
st.write("---")

# --- Sidebar Inputs ---
st.sidebar.header("🛠️ Asteroid Parameters")
diameter = st.sidebar.slider("Asteroid Diameter (m)", 10, 10000, 300)
velocity = st.sidebar.slider("Velocity (km/s)", 1, 70, 20)
density = st.sidebar.slider("Density (kg/m³)", 1000, 8000, 3000)
angle = st.sidebar.slider("Impact Angle (degrees)", 10, 90, 45)
population_density = st.sidebar.slider("Population Density (people/km²)", 10, 50000, 1000)

# --- Simulation Animation ---
with st.spinner("🚀 Running asteroid impact simulation..."):
    for i in range(100):
        time.sleep(0.01)
        st.progress(i + 1)

# --- Calculations ---
mass = (4/3) * np.pi * (diameter/2)**3 * density
velocity_mps = velocity * 1000
energy = 0.5 * mass * velocity_mps**2  # Joules
energy_mt = energy / 4.184e15  # Convert to Megatons TNT
crater_diameter = 1.8 * (energy**0.22) / 1000  # km
shockwave_radius = (energy**0.25) / 1000  # km
affected_area = np.pi * (shockwave_radius**2)  # km²
casualties = affected_area * population_density

# --- Results ---
st.subheader("🌍 Impact Results")

col1, col2, col3, col4 = st.columns(4)
col1.metric("Impact Energy", f"{energy_mt:,.2f} Mt TNT")
col2.metric("Crater Diameter", f"{crater_diameter:,.2f} km")
col3.metric("Shockwave Radius", f"{shockwave_radius:,.2f} km")
col4.metric("Casualties", f"{casualties:,.0f}")

# --- Visualization ---
st.subheader("📊 Impact Zone Visualization")

fig, ax = plt.subplots()
circle = plt.Circle((0, 0), shockwave_radius, color="red", alpha=0.4, label="Shockwave")
ax.add_artist(circle)
ax.set_xlim(-shockwave_radius*1.3, shockwave_radius*1.3)
ax.set_ylim(-shockwave_radius*1.3, shockwave_radius*1.3)
ax.set_aspect('equal', 'box')
ax.set_title("Impact Zone (Shockwave Radius)")
ax.legend()
st.pyplot(fig)

# --- Explanation ---
with st.expander("🔍 How these results are calculated"):
    st.markdown("""
    - **Impact Energy** = ½ × mass × velocity²  
    - **Crater Diameter** ≈ 1.8 × (E^0.22)  
    - **Shockwave Radius** ≈ √E (simplified scaling)  
    - **Casualties** = population density × affected area  
    """)

# --- Closing Note ---
st.success("✅ Simulation complete! This prototype demonstrates the **core asteroid impact simulation**. Future versions will include mitigation strategies, VR integration, and real NASA datasets.")
