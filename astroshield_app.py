import streamlit as st
import numpy as np

st.set_page_config(page_title="AstroShield Prototype", page_icon="☄️", layout="wide")

st.title("☄️ AstroShield – Asteroid Impact Simulation")
st.write("Prototype Demo – NASA Space Apps Challenge 2025 (Jabalpur Edition)")

# --- User Inputs ---
st.sidebar.header("Asteroid Parameters")
diameter = st.sidebar.slider("Asteroid Diameter (m)", 10, 10000, 300)
velocity = st.sidebar.slider("Velocity (km/s)", 1, 70, 20)
density = st.sidebar.slider("Density (kg/m³)", 1000, 8000, 3000)
angle = st.sidebar.slider("Impact Angle (degrees)", 10, 90, 45)
population_density = st.sidebar.slider("Population Density (people/km²)", 10, 50000, 1000)

# --- Calculations ---
mass = (4/3) * np.pi * (diameter/2)**3 * density
velocity_mps = velocity * 1000
energy = 0.5 * mass * velocity_mps**2  # Joules

# Convert to Megatons of TNT (1 Mt TNT = 4.184e15 J)
energy_mt = energy / 4.184e15

# Crater size (simplified model)
crater_diameter = 1.8 * (energy**0.22) / 1000  # km

# Shockwave radius (approx, km)
shockwave_radius = (energy**0.25) / 1000  

# Casualty estimate (people)
affected_area = np.pi * (shockwave_radius**2)  # km²
casualties = affected_area * population_density

# --- Output ---
st.subheader("🌍 Impact Results")
st.metric("Impact Energy", f"{energy_mt:,.2f} Mt TNT")
st.metric("Estimated Crater Diameter", f"{crater_diameter:,.2f} km")
st.metric("Shockwave Radius", f"{shockwave_radius:,.2f} km")
st.metric("Estimated Casualties", f"{casualties:,.0f} people")

# --- Visualization ---
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
circle = plt.Circle((0, 0), shockwave_radius, color="red", alpha=0.3, label="Shockwave")
ax.add_artist(circle)
ax.set_xlim(-shockwave_radius*1.2, shockwave_radius*1.2)
ax.set_ylim(-shockwave_radius*1.2, shockwave_radius*1.2)
ax.set_aspect('equal', 'box')
ax.set_title("Impact Zone (Shockwave Radius)")
ax.legend()
st.pyplot(fig)

st.info("⚡ Prototype focuses on core asteroid impact simulation. Future versions will add mitigation strategies, VR mode, and real NASA datasets.")
