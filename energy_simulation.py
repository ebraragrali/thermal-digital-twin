import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

hours = np.arange(0, 24)

# Statik sistem (sabit yüksek tüketim)
static_energy = 8 + np.random.normal(0.3, 0.5, 24)

# AI optimize sistem (yüksek saatlerde optimize)
optimized_energy = []
for h in hours:
    if 18 <= h <= 23:
        optimized_energy.append(6 + np.random.normal(0.2, 0.3))
    else:
        optimized_energy.append(7 + np.random.normal(0.2, 0.3))

optimized_energy = np.array(optimized_energy)

total_static = np.sum(static_energy)
total_optimized = np.sum(optimized_energy)

saving_percentage = (total_static - total_optimized) / total_static * 100

print("Toplam Statik Enerji:", round(total_static, 2), "kWh")
print("Toplam Optimize Enerji:", round(total_optimized, 2), "kWh")
print("Tasarruf Oranı: %", round(saving_percentage, 2))

plt.plot(hours, static_energy, label="Statik Soğutma")
plt.plot(hours, optimized_energy, label="AI Optimize Soğutma")
plt.xlabel("Saat")
plt.ylabel("Enerji Tüketimi (kWh)")
plt.title("24 Saatlik Enerji Karşılaştırması")
plt.legend()
plt.show()
