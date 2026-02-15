# Turkcell Yeşil Şebeke
## Yapay Zeka Destekli Termo-Dijital İkiz ile Akıllı Soğutma ve Karbon Ayak İzi Optimizasyonu

<p align="center">
  <img src="logo.png" alt="Turkcell Yeşil Şebeke Logo" width="600"/>
</p>

---

##  Proje Özeti

Turkcell Yeşil Şebeke projesi, baz istasyonlarının enerji tüketimini ve karbon emisyonunu azaltmak amacıyla geliştirilen Yapay Zeka destekli bir Termo-Dijital İkiz (Thermal Digital Twin) platformudur.

Mevcut sistemlerde soğutma mekanizmaları statik çalışmakta ve dış ortam koşulları ile trafik yükü gibi değişkenlere dinamik olarak adapte olamamaktadır. Bu durum enerji israfına ve donanım yıpranmasına sebep olmaktadır.

Bu proje kapsamında geliştirilen model:

- Gerçek zamanlı sensör verilerini analiz eder
- Fizik tabanlı ısı denklemlerini simüle eder
- PINNs (Physics-Informed Neural Networks) yaklaşımıyla tahmin üretir
- Soğutma sistemlerini dinamik olarak optimize eder
- Arızaları oluşmadan önce tahmin eder

Amaç; Turkcell altyapısında enerji verimliliğini artırmak, karbon salımını azaltmak ve sürdürülebilir şebeke yönetimi sağlamaktır.

---

##  Sistem Mimarisi

Sistem 7 ana katmandan oluşmaktadır:

1. Sensör Katmanı (Sıcaklık, Vibrasyon, CPU Load)
2. IoT Gateway (MQTT veri iletimi)
3. Edge AI Modülü
4. Termo-Dijital İkiz Motoru
5. Optimizasyon & Karar Mekanizması
6. Fiziksel Kontrol Katmanı (Klima/Fan)
7. Dashboard & İzleme

Kapalı çevrim kontrol mimarisi sayesinde sistem sürekli öğrenir ve kendini optimize eder.

(Detaylı mimari diyagramı için Ek–1 dosyasına bakınız.)

---

##  Kullanılan Teknolojiler

- Python
- NumPy / Pandas
- Matplotlib
- Scikit-Learn
- TensorFlow / PyTorch (PINNs altyapısı için)
- MQTT (IoT veri iletimi)
- Edge Computing
- Microservices Architecture

---

##  Simülasyon Sonuçları

Yapılan 24 saatlik simülasyon analizine göre:

- Statik soğutma tüketimi: ~190 kWh
- AI optimize tüketim: ~150 kWh
- Ortalama tasarruf: %18 – %27

Özellikle yüksek trafik saatlerinde enerji tüketimi anlamlı şekilde azalmaktadır.

Enerji simülasyon kodu:
`energy_simulation.py`

---

##  Karbon Ayak İzi Azaltımı

Varsayım:

- 10.000 aktif baz istasyonu
- İstasyon başı yıllık 12.000 kWh tasarruf

Toplam yıllık tasarruf:

120.000.000 kWh

Türkiye elektrik üretim ortalama emisyon faktörü:
0.43 kg CO₂ / kWh

Yıllık karbon azaltımı:

≈ 51.600 ton CO₂

Bu miktar yaklaşık olarak:
- 22.000 aracın yıllık karbon salımına
- 850.000 ağacın yıllık karbon tutma kapasitesine eşdeğerdir

---

##  Anomali Tespiti

Vibrasyon verileri üzerinden basit anomali tespiti demo uygulaması:

`anomaly_detection_demo.py`

Model, mikro-arızaları oluşmadan önce tespit etmeyi hedeflemektedir.

---

##  Gelecek Yol Haritası

### Aşama 1 – Matematiksel Modelleme
Termodinamik denklemlerle teorik doğrulama

### Aşama 2 – Dijital İkiz Simülasyonu
Gerçek verilerle AI model eğitimi

### Aşama 3 – Shadow Pilot
Pasif izleme modunda saha testi

### Aşama 4 – A/B Testi
Enerji ve performans karşılaştırması

---

##  Ticari Potansiyel

Proje SaaS (Software as a Service) modeli ile:

- Gainsharing (Tasarruf Paylaşımı)
- Yıllık Lisanslama

modeliyle ticarileştirilebilir.

Hedef pazar:
- Telekom operatörleri
- Veri merkezleri
- Endüstriyel tesisler
- Akıllı şehir altyapıları

---

##  Veri Güvenliği ve KVKK

Toplanan veriler teknik ve anonim operasyonel verilerdir.
Kullanıcıya ait kişisel veri işlenmemektedir.

Sistem "Privacy by Design" prensibine uygun tasarlanmıştır.

---

##  Sonuç

Turkcell Yeşil Şebeke projesi, fizik ve yapay zekayı birleştirerek sürdürülebilir telekom altyapısı için ölçeklenebilir ve uygulanabilir bir çözüm sunmaktadır.

Bu repository, projenin simülasyon ve teknik doğrulama çalışmalarını içermektedir.



