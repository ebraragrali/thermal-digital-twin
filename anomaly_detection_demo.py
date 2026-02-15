import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

# Normal vibrasyon değerleri
normal_data = np.random.normal(5, 0.5, 100)

# Anomali ekleyelim
normal_data[80:85] += 3

threshold = 7

anomalies = normal_data > threshold

print("Tespit Edilen Anomali Sayısı:", np.sum(anomalies))

plt.plot(normal_data, label="Vibrasyon")
plt.axhline(threshold, color='r', linestyle='--', label="Anomali Eşiği")
plt.scatter(np.where(anomalies), normal_data[anomalies], color='red')
plt.title("Vibrasyon Anomali Tespiti")
plt.legend()
plt.show()
