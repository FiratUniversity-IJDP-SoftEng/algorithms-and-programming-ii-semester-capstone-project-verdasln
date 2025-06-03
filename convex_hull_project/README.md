Örneğin projen masaüstündeyse:
cd ~/Desktop/CONVEX_HULL_PROJECT

2. Sanal Ortamı (virtual environment) Aktifleştir

Eğer önceden oluşturduysan:
source venv/bin/activate
yoksa;
python3 -m venv venv
source venv/bin/activate

Gerekli Kütüphaneleri Kur

requirements.txt dosyan varsa:

pip install -r requirements.txt

 Streamlit Uygulamasını Başlat

Proje kök dizininde şu komutu yaz:

streamlit run app.py
