import streamlit as pd  # Not: Streamlit standardı 'st' olarak kısaltılır
import streamlit as st

# --- SAYFA AYARLARI ---
st.set_page_config(
    page_title="Matematik Öğretmenleri İçin Dijital Oyun Havuzu",
    page_icon="📐",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- CSS İLE ÖZEL TASARIM ---
st.markdown("""
<style>
    .main { background-color: #f8f9fa; }
    .stTabs [data-baseweb="tab-list"] { gap: 10px; }
    .stTabs [data-baseweb="tab"] {
        background-color: #ffffff;
        border: 1px solid #dee2e6;
        border-radius: 8px 8px 0px 0px;
        padding: 10px 20px;
        font-weight: bold;
        color: #495057;
    }
    .stTabs [aria-selected="true"] {
        background-color: #0d6efd !important;
        color: white !important;
        border-color: #0d6efd !important;
    }
    .card {
        background-color: white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        margin-bottom: 15px;
        border-left: 5px solid #0d6efd;
    }
    .card-title { color: #0d6efd; font-size: 20px; font-weight: bold; margin-bottom: 5px; }
    .card-desc { color: #6c757d; font-size: 14px; margin-bottom: 10px; }
    .tag {
        display: inline-block;
        background-color: #e2e3e5;
        color: #383d41;
        padding: 3px 8px;
        border-radius: 5px;
        font-size: 12px;
        margin-right: 5px;
        font-weight: 500;
    }
</style>
""", unsafe_allow_html=True)

# --- BAŞLIK VE AÇIKLAMA ---
st.title("📐 Ortaokul Matematik Öğretmenleri İçin Dijital Oyun & Materyal Havuzu")
st.write("İlköğretim 5, 6, 7 ve 8. sınıf düzeyinde kullanılabilecek en popüler eğitici oyun, simülasyon ve dijital manipulatif sitelerinin sınıf ve konu bazlı derlemesi.")
st.markdown("---")

# --- VERİ SETİ (GENİŞ VE DETAYLI) ---
siteler = [
    {
        "isim": "Matific",
        "url": "https://www.matific.com/tr/tr/home/",
        "aciklama": "Müfredatla tamamen uyumlu, ödüllü matematik oyunları platformu. Kavramsal anlamayı derinleştirir.",
        "siniflar": ["5. Sınıf", "6. Sınıf"],
        "konular": ["Sayılar ve İşlemler", "Kesirler", "Geometri"]
    },
    {
        "isim": "Mathigon & Polypad",
        "url": "https://mathigon.org/polypad",
        "aciklama": "Matematiğin sanal laboratuvarı. Kesir duvarları, cebir karoları, tangramlar ve dinamik geometri araçları içerir.",
        "siniflar": ["5. Sınıf", "6. Sınıf", "7. Sınıf", "8. Sınıf"],
        "konular": ["Cebir", "Geometri", "Kesirler", "Olasılık", "Sayılar ve İşlemler"]
    },
    {
        "isim": "Wordwall Matematik Oyunları",
        "url": "https://wordwall.net/tr/community?localeId=1055&query=matematik",
        "aciklama": "Öğretmenler tarafından oluşturulmuş binlerce test, çarkıfelek, eşleştirme ve bilgi yarışması oyunu.",
        "siniflar": ["5. Sınıf", "6. Sınıf", "7. Sınıf", "8. Sınıf"],
        "konular": ["Tüm Konular", "Sayılar ve İşlemler", "Cebir", "Geometri", "Veri Analizi"]
    },
    {
        "isim": "PhET İnteraktif Simülasyonlar (Colorado)",
        "url": "https://phet.colorado.edu/tr/simulations/filter?subjects=math&type=html",
        "aciklama": "Oran-orantı, kesirler, tam sayılar ve fonksiyonlar gibi soyut konuları görselleştiren harika simülasyonlar.",
        "siniflar": ["6. Sınıf", "7. Sınıf", "8. Sınıf"],
        "konular": ["Oran ve Orantı", "Tam Sayılar", "Denklemler", "Kesirler"]
    },
    {
        "isim": "GeoGebra Klasik & Materyaller",
        "url": "https://www.geogebra.org/materials",
        "aciklama": "Özellikle 7. ve 8. sınıf geometri, koordinat sistemi ve doğrusal denklemler konuları için dinamik matematik grafikleri.",
        "siniflar": ["7. Sınıf", "8. Sınıf"],
        "konular": ["Geometri", "Koordinat Sistemi", "Doğrusal Denklemler", "Dönüşüm Geometrisi"]
    },
    {
        "isim": "Math Playground",
        "url": "https://www.mathplayground.com/",
        "aciklama": "Sınıflara göre ayrılmış, problem çözme ve mantık yürütmeye dayalı harika ücretsiz İngilizce matematik oyunları.",
        "siniflar": ["5. Sınıf", "6. Sınıf"],
        "konular": ["Sayılar ve İşlemler", "Mantık Oyunları", "Kesirler"]
    },
    {
        "isim": "Toy Theater",
        "url": "https://toytheater.com/category/math/",
        "aciklama": "Özellikle 5. ve 6. sınıflarda somut materyal ihtiyacını karşılayan sanal onluk taban blokları, saatler ve geometri tahtaları.",
        "siniflar": ["5. Sınıf", "6. Sınıf"],
        "konular": ["Sayılar ve İşlemler", "Geometri", "Kesirler"]
    },
    {
        "isim": "Khan Academy Matematik",
        "url": "https://tr.khanacademy.org/math",
        "aciklama": "5. sınıftan 8. sınıfa kadar tüm MEB müfredatını kapsayan, oyunlaştırılmış rozet sistemine sahip ücretsiz öğrenme platformu.",
        "siniflar": ["5. Sınıf", "6. Sınıf", "7. Sınıf", "8. Sınıf"],
        "konular": ["Tüm Konular", "Cebir", "Veri Analizi", "Geometri"]
    }
]

# --- YAN MENÜ (FİLTRELER) ---
st.sidebar.header("🔍 Gelişmiş Filtreleme")

# Sınıf Filtresi
sinif_secenekleri = ["Hepsi", "5. Sınıf", "6. Sınıf", "7. Sınıf", "8. Sınıf"]
secilen_sinif = st.sidebar.selectbox("Sınıf Seviyesi Seçin:", sinif_secenekleri)

# Konu Filtresi
konu_secenekleri = [
    "Hepsi", "Sayılar ve İşlemler", "Kesirler", "Cebir", 
    "Geometri", "Oran ve Orantı", "Tam Sayılar", 
    "Koordinat Sistemi", "Doğrusal Denklemler", "Veri Analizi", "Olasılık"
]
secilen_konu = st.sidebar.selectbox("Konu Alanı Seçin:", konu_secenekleri)

st.sidebar.markdown("---")
st.sidebar.info(
    "💡 **Öğretmenlere İpucu:**\n"
    "Akıllı tahtada kullanırken web sitelerini tam ekran (F11) moduna alarak "
    "öğrencilerin dikkatini daha iyi toplayabilirsiniz."
)

# --- FİLTRELEME MANTIĞI ---
filtrelenmiş_siteler = []
for site in siteler:
    sinif_uyumlu = (secilen_sinif == "Hepsi") or (secilen_sinif in site["siniflar"])
    konu_uyumlu = (secilen_konu == "Hepsi") or (secilen_konu in site["konular"]) or ("Tüm Konular" in site["konular"])
    
    if sinif_uyumlu and konu_uyumlu:
        filtrelenmiş_siteler.append(site)

# --- ANA SAYFA SEKMELERİ ---
tab1, tab2 = st.tabs(["🎮 Oyun ve Materyal Listesi", "📊 Genel Müfredat Dağılımı"])

with tab1:
    st.subheader(f"Bulunan Sonuçlar ({len(filtrelenmiş_siteler)} Platform)")
    
    if not filtrelenmiş_siteler:
        st.warning("Aradığınız kriterlere uygun bir platform bulunamadı. Lütfen filtreleri esnetin.")
    else:
        # Kartları 2'li sütunlar halinde listeleme
        col1, col2 = st.columns(2)
        
        for idx, site in enumerate(filtrelenmiş_siteler):
            # Sütun seçimi
            target_col = col1 if idx % 2 == 0 else col2
            
            with target_col:
                # Özel HTML Kart Tasarımı
                sinif_taglari = "".join([f'<span class="tag">{s}</span>' for s in site["siniflar"]])
                konu_taglari = "".join([f'<span class="tag" style="background-color:#cff4fc; color:#055160;">{k}</span>' for k in site["konular"]])
                
                st.markdown(f"""
                <div class="card">
                    <div class="card-title">{site['isim']}</div>
                    <div class="card-desc">{site['aciklama']}</div>
                    <div style="margin-bottom: 12px;">
                        {sinif_taglari}
                        {konu_taglari}
                    </div>
                </div>
                """, unsafe_allow_html=True)
                
                # Streamlit'in kendi butonu (Link açma işlemi güvenliği için direkt link butonu)
                st.link_button(f"🔗 {site['isim']} Sitesine Git", site["url"], use_container_width=True)
                st.write("") # Boşluk

with tab2:
    st.subheader("📌 Sınıf Seviyelerine Göre Önerilen Dijital Araçlar")
    
    st.markdown("""
    | Sınıf Seviyesi | En Etkili Kullanım Alanı | Önerilen Platformlar |
    | :--- | :--- | :--- |
    | **5. Sınıf** | Kesir Modelleme, Dört İşlem Hızı, Ondalık Gösterim | *Matific, Toy Theater, Math Playground* |
    | **6. Sınıf** | Oran Görselleştirme, Tam Sayılar, Açılar | *PhET Simülasyonları, Wordwall, Mathigon* |
    | **7. Sınıf** | Eşitlik ve Denklem Terazisi, Oran-Orantı, Rasyonel Sayılar | *PhET (Terazi Simülasyonu), Mathigon, GeoGebra* |
    | **8. Sınıf** | LGS Hazırlık, Koordinat Sistemi, Dönüşüm Geometrisi, Olasılık | *GeoGebra, Khan Academy, Polypad* |
    """)

# --- FOOTER ---
st.markdown("---")
st.caption("Matematik Öğretmenleri Paylaşım Platformu için geliştirilmiştir. İSMAİL ORHAN © 2026")
