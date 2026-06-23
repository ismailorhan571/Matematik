import streamlit as st

# --- ULTRA MODERN PREMIUM SAYFA AYARLARI ---
st.set_page_config(
    page_title="Matematik Kazanım Odaklı Matrix v6.0",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- LUXURY EXECUTIVE DASHBOARD DESIGN (CSS MASTERBLOCK) ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800&display=swap');
    
    html, body, [data-testid="stAppViewContainer"] {
        background-color: #f8fafc;
        font-family: 'Outfit', sans-serif;
    }
    
    [data-testid="stSidebar"] {
        background-color: #ffffff !important;
        border-right: 1px solid #e2e8f0;
    }
    
    /* Sekme Tasarımları */
    .stTabs [data-baseweb="tab-list"] {
        gap: 16px;
        border-bottom: 2px solid #e2e8f0;
        padding-bottom: 10px;
    }
    .stTabs [data-baseweb="tab"] {
        background-color: #ffffff;
        border: 1px solid #e2e8f0 !important;
        padding: 14px 30px;
        border-radius: 16px;
        font-weight: 600;
        color: #64748b;
        transition: all 0.3s ease;
    }
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #0284c7 0%, #0369a1 100%) !important;
        color: #ffffff !important;
        border-color: transparent !important;
        box-shadow: 0 10px 15px -3px rgba(3, 105, 161, 0.3);
    }

    /* KAZANIM KART MİMARİSİ */
    .kazanim-box {
        background: #ffffff;
        border-radius: 24px;
        padding: 24px;
        border: 1px solid #e2e8f0;
        border-left: 8px solid #0f172a;
        margin-bottom: 20px;
    }
    
    .resource-card {
        background: #ffffff;
        border-radius: 20px;
        padding: 25px;
        border: 1px solid rgba(226, 232, 240, 0.8);
        box-shadow: 0 4px 6px -1px rgba(0,0,0,0.01);
        position: relative;
        overflow: hidden;
        height: 100%;
    }
    .card-pre { border-top: 6px solid #f59e0b; }
    .card-post { border-top: 6px solid #10b981; }

    .card-title {
        color: #0f172a;
        font-size: 20px;
        font-weight: 700;
        margin-bottom: 8px;
    }
    .card-desc {
        color: #475569;
        font-size: 14px;
        line-height: 1.5;
        margin-bottom: 20px;
    }

    .badge {
        display: inline-block;
        padding: 4px 10px;
        border-radius: 8px;
        font-size: 11px;
        font-weight: 700;
        text-transform: uppercase;
    }
    .badge-pre { background-color: #fef3c7; color: #d97706; }
    .badge-post { background-color: #d1fae5; color: #059669; }
</style>
""", unsafe_allow_html=True)

# --- BAŞLIK ALANI ---
st.markdown("<h1 style='color: #0f172a; font-weight: 800; font-size: 38px; letter-spacing: -1px; margin-bottom:4px;'>🎯 Müfredat Senkronlu Kolay Öğrenme Matrisi</h1>", unsafe_allow_html=True)
st.markdown("<p style='color: #475569; font-size: 15px; margin-top:0px;'>Ders öncesi keşif araçları ve ders sonrası eğitsel oyun kaynaklarının arama yapmadan, doğrudan kazanım bazlı eşleşmesi.</p>", unsafe_allow_html=True)
st.write("")

# --- SABİT MÜFREDAT VE DOĞRUDAN LİNK VERİTABANI (ÖRNEK MASTER MATRİS) ---
# Gerçek senaryoda bu havuz tüm alt kazanımlarla doldurulur. Öğretmen tek bir saniye arama yapmaz.
mufredat_matrix = {
    "5. Sınıf": {
        "M.5.1.1.1. Doğal Sayıların Okunması/Yazılması": {
            "kod": "M.5.1.1.1",
            "aciklama": "En çok dokuz basamaklı doğal sayıları okur ve yazar.",
            "ders_oncesi": {
                "platform": "Toy Theater Labs",
                "tur": "Görsel Sanal Manipülatif (Keşif)",
                "detay": "Öğrencinin ders öncesinde basamak kavramını, blokları kaydırarak sıfır zorlanmayla görsel olarak keşfetmesini sağlar.",
                "url": "https://toytheater.com/place-value-cards/"
            },
            "ders_sonrasi": {
                "platform": "Wordwall Matematik Dünyası",
                "tur": "Eğitsel Dijital Oyun (Pekiştirme)",
                "detay": "Ders sonrasında öğrenilen basamakları eğlenceli bir yarışma ve balon patlatma mekaniğiyle kalıcı hale getiren hazır oyun.",
                "url": "https://wordwall.net/tr/resource/17490014/matematik/5-sinif-do%C4%9Fal-sayilar"
            }
        },
        "M.5.1.2.1. Kesirleri Modelleme": {
            "kod": "M.5.1.2.1",
            "aciklama": "Birim kesirleri sayı doğrusunda gösterir ve sıralar.",
            "ders_oncesi": {
                "platform": "PhET Simülasyonları",
                "tur": "Etkileşimli Modelleme Labı",
                "detay": "Çocukların ders öncesinde kesir parçalarını görsel pasta ve barlarla eşleyerek mantığı zorlanmadan kavramasını sağlar.",
                "url": "https://phet.colorado.edu/simulations/sims?html=fractions-intro&locale=tr"
            },
            "ders_sonrasi": {
                "platform": "Blooket Eğitsel Oyun",
                "tur": "Oyunlaştırılmış Turnuva Modülü",
                "detay": "Kesir sıralama becerisini çocukların en sevdiği karakterlerle rekabetçi bir oyun formatında sunan hazır pekiştirme linki.",
                "url": "https://www.blooket.com/"
            }
        }
    },
    "6. Sınıf": {
        "M.6.1.5.1. Kesirlerle Karşılaştırma": {
            "kod": "M.6.1.5.1",
            "aciklama": "Kesirleri karşılaştırır, sıralar ve sayı doğrusunda gösterir.",
            "ders_oncesi": {
                "platform": "GeoGebra Dinamik Dinamik Motoru",
                "tur": "Sayı Doğrusu Görselleştirici",
                "detay": "Pay ve paydayı değiştirerek kesrin sayı doğrusundaki anlık hareketini gösteren ders öncesi hazır görsel döküman.",
                "url": "https://www.geogebra.org/m/xcg6w7um"
            },
            "ders_sonrasi": {
                "platform": "Liveworksheets İnteraktif Odası",
                "tur": "Anlık Dönütlü Eğitsel Görev",
                "detay": "Çocuğun sürükle-bırak yöntemiyle kesirleri büyükten küçüğe dizeceği, sistemin otomatik puan verdiği dijital aktivite.",
                "url": "https://www.liveworksheets.com/"
            }
        }
    },
    "7. Sınıf": {},
    "8. Sınıf": {}
}

# --- SIDEBAR KAZANIM SEÇİM İSTASYONU ---
st.sidebar.markdown("<h2 style='color: #0f172a; font-size: 20px; font-weight: 700; margin-bottom: 15px;'>🗂️ Sınıf ve Kazanım Seçimi</h2>", unsafe_allow_html=True)

siniflar = list(mufredat_matrix.keys())
secilen_sinif = st.sidebar.selectbox("Eğitim Kademesi:", siniflar)

# Seçilen sınıfa ait kazanımları getir
mevcut_kazanimlar = list(mufredat_matrix[secilen_sinif].keys())

if len(mevcut_kazanimlar) == 0:
    st.sidebar.warning("Bu sınıf düzeyi için veri giriş planlaması devam ediyor.")
    st.info("Lütfen örnek veri entegrasyonunu görmek için **5. Sınıf** veya **6. Sınıf** kademesini seçiniz.")
else:
    secilen_kazanim_adi = st.sidebar.selectbox("Hedef MEB Kazanımı:", mevcut_kazanimlar)
    data = mufredat_matrix[secilen_sinif][secilen_kazanim_adi]

    # --- AKTİF KAZANIM KARTI ---
    st.markdown(f"""
    <div class="kazanim-box">
        <div style="font-weight: 800; color: #0284c7; font-size: 13px; letter-spacing:0.5px;">AKTİF SEÇİLİ MEB KODU: {data['kod']}</div>
        <div style="font-size: 20px; font-weight: 700; color: #0f172a; margin-top: 4px;">{secilen_kazanim_adi.split('.', 4)[-1].strip()}</div>
        <div style="font-size: 15px; color: #475569; margin-top: 8px; font-style: italic;">" {data['aciklama']} "</div>
    </div>
    """, unsafe_allow_html=True)

    st.write("")

    # --- İKİLİ STRATEJİK YAPI (DERS ÖNCESİ VE SONRASI SIFIR ARAMA GRUBU) ---
    col1, col2 = st.columns(2)

    with col1:
        pre = data["ders_oncesi"]
        st.markdown(f"""
        <div class="resource-card card-pre">
            <span class="badge badge-pre">⏳ Ders Öncesi / Keşif & Hazırlık</span>
            <div class="card-title" style="margin-top:12px;">{pre['platform']}</div>
            <div style="color: #64748b; font-size: 12px; font-weight: 600; margin-bottom:10px;">🛠️ İçerik Türü: {pre['tur']}</div>
            <div class="card-desc">{pre['detay']}</div>
        </div>
        """, unsafe_allow_html=True)
        st.link_button("🚀 Çocuğa Doğrudan Keşif Linkini Ver", pre["url"], use_container_width=True)

    with col2:
        post = data["ders_sonrasi"]
        st.markdown(f"""
        <div class="resource-card card-post">
            <span class="badge badge-post">🎮 Ders Sonrası / Eğlenceli Oyun</span>
            <div class="card-title" style="margin-top:12px;">{post['platform']}</div>
            <div style="color: #64748b; font-size: 12px; font-weight: 600; margin-bottom:10px;">🕹️ İçerik Türü: {post['tur']}</div>
            <div class="card-desc">{post['detay']}</div>
        </div>
        """, unsafe_allow_html=True)
        st.link_button("🎯 Çocuğu Doğrudan Hazır Oyuna Işınla", post["url"], use_container_width=True)

# --- FOOTER ---
st.markdown("---")
st.markdown("<p style='text-align: center; color: #94a3b8; font-size: 13px;'>Müfredat Kazanım-Kaynak Birebir Eşleme Sistemi. Ortak payda, matematik öğretmenlerine özel olarak üretildi/İSMAİL ORHAN © 2026</p>", unsafe_allow_html=True)
