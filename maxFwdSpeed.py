# maxFwdSpeed.py
power_output_kw = 300
efficiency=0.85
drag_coefficient=0.8
frontal_area_m2=2.5
air_density_kgm3=1.225
# Convert power from kW to Watts
power_watts = power_output_kw * 1000 * efficiency
# Drag force equation: F_drag = 0.5 * Cd * A * rho * v^2
# Power required to overcome drag: P = F_drag * v = 0.5 * Cd * A * rho * v^3
# Solve for v: v = (2 * P / (Cd * A * rho)) ** (1/3)
v_max = (2 * power_watts / (drag_coefficient * frontal_area_m2 * air_density_kgm3)) ** (1/3)
