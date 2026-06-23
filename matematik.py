import streamlit as st
import requests

# --- SAYFA AYARLARI ---
st.set_page_config(
    page_title="Matematik Öğretmenleri İçin Dijital Oyun Havuzu",
    page_icon="📐",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- MODERN VE ŞIK CSS TASARIMI ---
st.markdown("""
<style>
    .main { background-color: #fcfcfd; }
    .stTabs [data-baseweb="tab-list"] { gap: 15px; border-bottom: 2px solid #eef2f5; }
    .stTabs [data-baseweb="tab"] {
        background-color: transparent; border: none; padding: 12px 24px;
        font-weight: 600; color: #64748b; transition: all 0.3s ease;
    }
    .stTabs [aria-selected="true"] { color: #0f172a !important; border-bottom: 3px solid #10b981 !important; }
    
    .card {
        background-color: #ffffff; padding: 24px; border-radius: 16px;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.04); margin-bottom: 12px;
        border: 1px solid #f1f5f9; border-top: 4px solid #10b981;
    }
    .card-title { color: #1e293b; font-size: 20px; font-weight: 700; margin-bottom: 8px; }
    .card-desc { color: #64748b; font-size: 14.5px; line-height: 1.6; margin-bottom: 16px; }
    
    .tag-sinif { display: inline-block; background-color: #f0fdf4; color: #166534; padding: 4px 10px; border-radius: 8px; font-size: 12.5px; margin-right: 8px; font-weight: 600; }
    .tag-konu { display: inline-block; background-color: #f0f9ff; color: #0369a1; padding: 4px 10px; border-radius: 8px; font-size: 12.5px; margin-right: 8px; font-weight: 600; }
    .tag-kategori { display: inline-block; background-color: #faf5ff; color: #6b21a8; padding: 4px 10px; border-radius: 8px; font-size: 12.5px; margin-right: 8px; font-weight: 600; }
    .status-active { color: #10b981; font-weight: bold; font-size: 13px; float: right; }
</style>
""", unsafe_allow_html=True)

if "favoriler" not in st.session_state:
    st.session_state.favoriler = []

# --- GÜVENLİ LİNK KONTROLÜ (BOT ENGELİNİ AŞAN BROWSER HEADERS) ---
@st.cache_data(ttl=3600)
def guvenli_link_kontrol(url):
    try:
        # Büyük sitelerin bot engeline takılmamak için tarayıcı taklidi yapıyoruz
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
        r = requests.get(url, headers=headers, timeout=3, stream=True)
        return r.status_code < 400
    except:
        return False

# --- BAŞLIK VE AÇIKLAMA ---
st.markdown("<h1 style='color: #1e293b; font-weight: 800;'>📐 Ortaokul Matematik Öğretmenleri İçin Dijital Materyal Havuzu</h1>", unsafe_allow_html=True)
st.write("Seçtiğiniz sınıf ve konuyu tüm platformların kendi arama motoru sistemlerine otomatik olarak entegre eder ve nokta atışı arama linki üretir.")
st.markdown("---")

# --- YAN MENÜ FİLTRELERİ ---
st.sidebar.markdown("<h2 style='color: #1e293b; font-size: 20px; font-weight: 700;'>🎯 Müfredat Odaklı Filtre</h2>", unsafe_allow_html=True)

sinif_secenekleri = ["Hepsi", "5. Sınıf", "6. Sınıf", "7. Sınıf", "8. Sınıf"]
secilen_sinif = st.sidebar.selectbox("Sınıf Seviyesi Seçin:", sinif_secenekleri)

tum_meb_konulari = [
    "Hepsi", "Doğal Sayılar", "Doğal Sayılarla İşlemler", "Çarpanlar ve Katlar", "Kümeler", "Tam Sayılar",
    "Kesirler", "Kesirlerle İşlemler", "Ondalık Gösterim", "Rasyonel Sayılar", "Üslü İfadeler", "Kareköklü İfadeler",
    "Oran ve Orantı", "Yüzdeler", "Cebirsel İfadeler", "Eşitlik ve Denklem", "Doğrusal Denklemler", "Eşitsizlikler",
    "Temel Geometrik Kavramlar", "Doğrular ve Açılar", "Çokgenler", "Üçgenler", "Çember ve Daire", "Eşlik ve Benzerlik",
    "Dönüşüm Geometrisi", "Geometrik Cisimler", "Uzunluk ve Zaman Ölçme", "Alan Ölçme", "Sıvı Ölçme",
    "Veri Toplama ve Analizi", "Olasılık", "Koordinat Sistemi"
]

if secilen_sinif == "5. Sınıf":
    konu_secenekleri = ["Hepsi", "Doğal Sayılar", "Doğal Sayılarla İşlemler", "Kesirler", "Kesirlerle İşlemler", "Ondalık Gösterim", "Yüzdeler", "Temel Geometrik Kavramlar", "Üçgen ve Dörtgenler", "Veri Toplama ve Analizi", "Uzunluk ve Zaman Ölçme", "Alan Ölçme", "Geometrik Cisimler"]
elif secilen_sinif == "6. Sınıf":
    konu_secenekleri = ["Hepsi", "Doğal Sayılarla İşlemler", "Çarpanlar ve Katlar", "Kümeler", "Tam Sayılar", "Kesirlerle İşlemler", "Ondalık Gösterim", "Oran ve Orantı", "Cebirsel İfadeler", "Veri Toplama ve Analizi", "Doğrular ve Açılar", "Alan Ölçme", "Çember ve Daire", "Geometrik Cisimler", "Sıvı Ölçme"]
elif secilen_sinif == "7. Sınıf":
    konu_secenekleri = ["Hepsi", "Tam Sayılar", "Rasyonel Sayılar", "Cebirsel İfadeler", "Eşitlik ve Denklem", "Oran ve Orantı", "Yüzdeler", "Doğrular ve Açılar", "Çokgenler", "Çember ve Daire", "Veri Toplama ve Analizi", "Geometrik Cisimler"]
elif secilen_sinif == "8. Sınıf":
    konu_secenekleri = ["Hepsi", "Çarpanlar ve Katlar", "Üslü İfadeler", "Kareköklü İfadeler", "Veri Toplama ve Analizi", "Olasılık", "Cebirsel İfadeler", "Doğrusal Denklemler", "Eşitsizlikler", "Üçgenler", "Eşlik ve Benzerlik", "Dönüşüm Geometrisi", "Geometrik Cisimler", "Koordinat Sistemi"]
else:
    konu_secenekleri = tum_meb_konulari

secilen_konu = st.sidebar.selectbox("Konu Alanı Seçin:", konu_secenekleri)

# --- V3 PROFESYONEL FİLTRELER ---
st.sidebar.markdown("---")
st.sidebar.subheader("🚀 Gelişmiş Filtreler")
kategori_sec = st.sidebar.multiselect("Materyal Türü:", ["Oyun", "Simülasyon", "Video", "Manipülatif", "Etkinlik"])
lgs_modu = st.sidebar.toggle("🎯 Sadece LGS Odaklı Siteler")

# --- ANA ARAMA ÇUBUĞU ---
arama_sorgusu = st.text_input("🔍 Kelime ile İçerik Havuzunda Ara:", placeholder="Örn: phet, kesirler, ebob ekok...").strip().lower()

# --- SİTELERİN GERÇEK ARAMA MOTORU URL YAPILARI ---
siteler_havuzu = [
    {
        "isim": "Wordwall Matematik",
        "aciklama": "Öğretmenler tarafından hazırlanmış çarkıfelek, labirent ve bilgi yarışması etkinlikleri.",
        "search_url": "https://wordwall.net/tr/community?localeId=1055&query={query}",
        "default_url": "https://wordwall.net/tr/community?localeId=1055&query=matematik",
        "kategoriler": ["Oyun", "Etkinlik"],
        "lgs_uyumlu": True
    },
    {
        "isim": "GeoGebra Materyalleri",
        "aciklama": "Geometri, grafikler ve denklemler için dinamik, hareketli öğretmen simülasyon sayfaları.",
        "search_url": "https://www.geogebra.org/search/{query}",
        "default_url": "https://www.geogebra.org/materials",
        "kategoriler": ["Simülasyon", "Manipülatif"],
        "lgs_uyumlu": True
    },
    {
        "isim": "Mathigon & Polypad",
        "aciklama": "Matematiğin sanal laboratuvarı. Cebir karoları, kesir blokları ve dinamik paneller.",
        "search_url": "https://mathigon.org/polypad", 
        "default_url": "https://mathigon.org/polypad",
        "kategoriler": ["Manipülatif", "Simülasyon"],
        "lgs_uyumlu": True
    },
    {
        "isim": "PhET İnteraktif Simülasyonlar",
        "aciklama": "Colorado Üniversitesi onaylı kesir, tam sayı ve denklem terazisi simülasyonları.",
        "search_url": "https://phet.colorado.edu/tr/simulations/filter?subjects=math&type=html&searchTerm={query}",
        "default_url": "https://phet.colorado.edu/tr/simulations/filter?subjects=math&type=html",
        "kategoriler": ["Simülasyon"],
        "lgs_uyumlu": False
    },
    {
        "isim": "Matific Türkiye",
        "aciklama": "MEB müfredatına tam uyumlu, sınıf seviyenize özel animasyonlu senaryolu oyun görevleri.",
        "search_url": "https://www.matific.com/tr/tr/home/maths-zone/",
        "default_url": "https://www.matific.com/tr/tr/home/maths-zone/",
        "kategoriler": ["Oyun"],
        "lgs_uyumlu": False
    },
    {
        "isim": "Khan Academy",
        "aciklama": "Tüm kazanımları video ve oyunlaştırılmış testlerle sunan eksiksiz eğitim paneli.",
        "search_url": "https://tr.khanacademy.org/search?page_search_query={query}",
        "default_url": "https://tr.khanacademy.org/math/",
        "kategoriler": ["Video", "Etkinlik"],
        "lgs_uyumlu": True
    }
]

# --- DİNAMİK LİNK MOTORU VE FİLTRELEME ---
filtrelenmis_siteler = []

# Arama terimi oluşturma mantığı
terim_parcalari = []
if secilen_sinif != "Hepsi": terim_parcalari.append(secilen_sinif)
if secilen_konu != "Hepsi": terim_parcalari.append(secilen_konu)
olusturulan_sorgu = " ".join(terim_parcalari).strip()

for site in siteler_havuzu:
    # Filtre Kontrolleri
    if lgs_modu and not site["lgs_uyumlu"]: continue
    if kategori_sec and not any(k in site["kategoriler"] for k in kategori_sec): continue
    if arama_sorgusu and (arama_sorgusu not in site["isim"].lower() and arama_sorgusu not in site["aciklama"].lower()): continue
    
    # URL Oluşturma Parametresi
    if olusturulan_sorgu:
        encoded_sorgu = olusturulan_sorgu.replace(" ", "%20")
        # Özel durum yönlendirmeleri (Mathigon spesifik hashtag urlleri)
        if site["isim"] == "Mathigon & Polypad" and secilen_konu != "Hepsi":
            if secilen_konu in ["Cebirsel İfadeler", "Eşitlik ve Denklem", "Doğrusal Denklemler"]:
                dinamik_url = "https://mathigon.org/polypad#algebra"
            elif "Geometri" in secilen_konu or "Açılar" in secilen_konu or "Çokgenler" in secilen_konu:
                dinamik_url = "https://mathigon.org/polypad#geometry"
            else:
                dinamik_url = "https://mathigon.org/polypad#numbers"
        elif site["isim"] == "Matific Türkiye" and secilen_sinif != "Hepsi":
            rakam = secilen_sinif.split(".")[0]
            dinamik_url = f"https://www.matific.com/tr/tr/home/maths-zone/grade-{rakam}/"
        else:
            dinamik_url = site["search_url"].format(query=encoded_sorgu)
    else:
        dinamik_url = site["default_url"]
        
    filtrelenmis_siteler.append({"veri": site, "url": dinamik_url})

# --- GÖRÜNÜM PANELİ ---
tab1, tab2 = st.tabs(["🎮 Doğrudan Görev & Oyun Havuzu", "📊 MEB Müfredat Strateji Tablosu"])

with tab1:
    st.markdown(f"**Aktif Arama Filtresi:** `{olusturulan_sorgu if olusturulan_sorgu else 'Tüm Müfredat Havuzu'}`")
    
    if not filtrelenmis_siteler:
        st.warning("Kriterlere uygun sonuç bulunamadı.")
    else:
        col1, col2 = st.columns(2)
        for idx, item in enumerate(filtrelenmis_siteler):
            site_veri = item["veri"]
            hedef_link = item["url"]
            target_col = col1 if idx % 2 == 0 else col2
            
            with target_col:
                kategoriler_html = " ".join([f'<span class="tag-kategori">⚡ {k}</span>' for k in site_veri["kategoriler"]])
                
                st.markdown(f"""
                <div class="card">
                    <span class="status-active">● Bağlantı Hazır</span>
                    <div class="card-title">{site_veri['isim']}</div>
                    <div class="card-desc">{site_veri['aciklama']}</div>
                    <div style="margin-bottom: 15px;">
                        <span class="tag-sinif">📍 {secilen_sinif if secilen_sinif != 'Hepsi' else 'Tüm Kademe'}</span>
                        <span class="tag-konu">📖 {secilen_konu if secilen_konu != 'Hepsi' else 'Genel Konular'}</span>
                        {kategoriler_html}
                    </div>
                </div>
                """, unsafe_allow_html=True)
                
                btn_c1, btn_c2 = st.columns([3, 1])
                with btn_c1:
                    buton_metni = f"🚀 {site_veri['isim']} İçinde Ara" if olusturulan_sorgu else f"🔗 {site_veri['isim']} Paneline Git"
                    st.link_button(buton_metni, hedef_link, use_container_width=True)
                with btn_c2:
                    if site_veri["isim"] in st.session_state.favoriler:
                        if st.button("⭐ Kaldır", key=f"fav_{idx}", use_container_width=True):
                            st.session_state.favoriler.remove(site_veri["isim"])
                            st.rerun()
                    else:
                        if st.button("☆ Favori", key=f"fav_{idx}", use_container_width=True):
                            st.session_state.favoriler.append(site_veri["isim"])
                            st.rerun()

with tab2:
    st.subheader("📌 Öğretmenler İçin Sınıf ve Konu Odaklı Kullanım Önerileri")
    st.markdown("""
    | Sınıf Seviyesi | En Zorlanılan Üniteler | Dijital Somutlaştırma İçin Önerilen Platformlar |
    | :--- | :--- | :--- |
    | **5. Sınıf** | Kesirler, Ondalık Gösterim, Yüzdeler | *Matific (Oyunlaştırma), Wordwall Hız Oyunları* |
    | **6. Sınıf** | Oran, Cebirsel İfadeler, Hacim Ölçme | *PhET (Oran Simülasyonu), Mathigon (Cebir Karoları)* |
    | **7. Sınıf** | Eşitlik ve Denklem, Tam Sayılarda İşlemler | *PhET (Denklem Terazisi), GeoGebra (Dinamik Grafikler)* |
    | **8. Sınıf** | LGS Hazırlık, Kareköklü İfadeler, Dönüşüm Geometrisi | *Wordwall (Hız Testleri), Khan Academy (Soru Bankası)* |
    """)

# --- YAN MENÜ FAVORİLER GÖRÜNÜMÜ ---
st.sidebar.markdown("---")
st.sidebar.subheader("⭐ Favori Platformlarım")
if st.session_state.favoriler:
    for fav in st.session_state.favoriler:
        st.sidebar.caption(f"✨ {fav}")
else:
    st.sidebar.info("Henüz favori eklenmedi.")

st.markdown("---")
st.markdown("<p style='text-align: center; color: #94a3b8; font-size: 13px;'>Ortak Payda Matematik Öğretmenleri için geliştirilmiştir. İSMAİL ORHAN © 2026</p>", unsafe_allow_html=True)
