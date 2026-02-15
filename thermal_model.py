import numpy as np

class ThermalModel:
    def __init__(self, insulation_coeff=0.8, heat_capacity=500):
        self.insulation_coeff = insulation_coeff
        self.heat_capacity = heat_capacity

    def calculate_internal_temp(self, ambient_temp, cpu_load, current_temp):
        """
        Basit ısı dengesi modeli:
        Yeni sıcaklık = Mevcut sıcaklık + (Dış ortam etkisi + CPU yükü etkisi) / ısıl kapasite
        """

        ambient_effect = (ambient_temp - current_temp) * self.insulation_coeff
        cpu_effect = cpu_load * 0.05  # CPU yükü ısı üretimi

        new_temp = current_temp + (ambient_effect + cpu_effect) / self.heat_capacity * 100

        return new_temp


if __name__ == "__main__":
    model = ThermalModel()

    ambient_temp = 35
    cpu_load = 70
    current_temp = 28

    new_temp = model.calculate_internal_temp(ambient_temp, cpu_load, current_temp)

    print("Yeni Tahmini İç Sıcaklık:", round(new_temp, 2), "°C")
