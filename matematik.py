import streamlit as st
import urllib.parse
import json

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="Matematik Materyal Motoru Pro v5.2",
    page_icon="📐",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- CSS (Önceki + Yeni İyileştirmeler) ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800&display=swap');
    
    html, body, [data-testid="stAppViewContainer"] {
        background-color: #f8fafc;
        font-family: 'Outfit', sans-serif;
    }
    
    .stTabs [data-baseweb="tab-list"] { gap: 16px; }
    .stTabs [data-baseweb="tab"] {
        background-color: #ffffff;
        border: 1px solid #e2e8f0 !important;
        padding: 12px 28px;
        border-radius: 16px;
        font-weight: 600;
    }
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #4f46e5 0%, #2563eb 100%) !important;
        color: white !important;
    }

    .premium-card {
        background: #ffffff;
        border-radius: 28px;
        padding: 28px;
        margin-bottom: 24px;
        border: 1px solid rgba(226, 232, 240, 0.8);
        box-shadow: 0 10px 30px -10px rgba(0, 0, 0, 0.03);
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        position: relative;
        overflow: hidden;
    }
    .premium-card:hover {
        transform: translateY(-6px);
        box-shadow: 0 20px 40px -15px rgba(79, 70, 229, 0.15);
        border-color: #4f46e5;
    }
    .premium-card::before {
        content: '';
        position: absolute;
        top: 0; left: 0; width: 6px; height: 100%;
        background: linear-gradient(180deg, #4f46e5 0%, #3b82f6 100%);
    }

    .badge {
        display: inline-flex; align-items: center; padding: 6px 14px;
        border-radius: 9999px; font-size: 12px; font-weight: 700;
        margin-right: 8px; margin-bottom: 8px;
    }
    .badge-sinif { background-color: #f1f5f9; color: #334155; }
    .badge-konu { background-color: #e0f2fe; color: #0369a1; }
    .badge-pdf { background-color: #fee2e2; color: #b91c1c; }
    .badge-video { background-color: #fef3c7; color: #b45309; }
    .badge-game { background-color: #ecfdf5; color: #065f46; }
    .badge-interaktif { background-color: #f3e8ff; color: #6d28d9; }
</style>
""", unsafe_allow_html=True)

# --- SESSION STATE ---
if "favoriler" not in st.session_state:
    st.session_state.favoriler = []
if "son_arama" not in st.session_state:
    st.session_state.son_arama = ""

# --- BAŞLIK ---
st.markdown("<h1 style='color: #0f172a; font-weight: 800; font-size: 42px; letter-spacing: -1.5px;'>📐 Matematik Materyal Motoru Pro v5.2</h1>", unsafe_allow_html=True)
st.markdown("<p style='color: #475569; font-size: 17px;'>Tek tıkla müfredata uygun kaliteli materyal, oyun, video ve test</p>", unsafe_allow_html=True)

# --- SIDEBAR ---
st.sidebar.markdown("### 🎛️ Filtre İstasyonu")
sinif_secenekleri = ["Hepsi", "5. Sınıf", "6. Sınıf", "7. Sınıf", "8. Sınıf"]
secilen_sinif = st.sidebar.selectbox("Sınıf Seviyesi", sinif_secenekleri)

# Konu seçenekleri (kısaltılmış)
konu_secenekleri = ["Hepsi", "Doğal Sayılar", "Kesirler", "Ondalık Gösterim", "Yüzdeler", "Oran ve Orantı",
                    "Cebirsel İfadeler", "Denklem", "Üslü İfadeler", "Geometri", "Üçgenler", "Çember ve Daire",
                    "Veri Analizi", "Olasılık", "Koordinat Sistemi"]

secilen_konu = st.sidebar.selectbox("Konu", konu_secenekleri)
ozel_kazanim = st.sidebar.text_input("🔍 Kazanım / Kelime", placeholder="M.8.1.2.1 veya Özdeşlikler").strip()

# Hızlı Popüler Butonlar
st.sidebar.markdown("### ⚡ Hızlı Aramalar")
if st.sidebar.button("8. Sınıf Üslü İfadeler"):
    secilen_sinif = "8. Sınıf"; secilen_konu = "Üslü İfadeler"
if st.sidebar.button("7. Sınıf Denklem"):
    secilen_sinif = "7. Sınıf"; secilen_konu = "Denklem"

# --- SİTE HAVUZU (Genişletildi) ---
siteler_havuzu = [
    {"isim": "EBA", "aciklama": "Resmi MEB video ve etkileşimli içerikler", "strategy": "native",
     "search_url": "https://www.eba.gov.tr/arama?q={query}", "default_url": "https://www.eba.gov.tr",
     "kategori": "video", "kaynak": "MEB"},
    
    {"isim": "Khan Academy Türkçe", "aciklama": "Ücretsiz kaliteli video dersler ve alıştırmalar", "strategy": "native",
     "search_url": "https://tr.khanacademy.org/search?query={query}", "default_url": "https://tr.khanacademy.org",
     "kategori": "video", "kaynak": "Khan"},
    
    {"isim": "GeoGebra", "aciklama": "Dinamik geometri ve simülasyonlar", "strategy": "native",
     "search_url": "https://www.geogebra.org/search/{query}", "default_url": "https://www.geogebra.org",
     "kategori": "interaktif", "kaynak": "GeoGebra"},
    
    {"isim": "Wordwall", "aciklama": "Binlerce interaktif oyun ve etkinlik", "strategy": "native",
     "search_url": "https://wordwall.net/tr/community?query={query}", "default_url": "https://wordwall.net",
     "kategori": "game", "kaynak": "Wordwall"},
    
    {"isim": "Matematik.biz", "aciklama": "Konu anlatımı, test ve çalışma kağıtları", "strategy": "google_search",
     "target_string": "site:matematik.biz {query}", "default_url": "https://www.matematik.biz",
     "kategori": "pdf", "kaynak": "Yerel"},
    
    {"isim": "Liveworksheets", "aciklama": "Etkileşimli çalışma yaprakları", "strategy": "native",
     "search_url": "https://www.liveworksheets.com/search?query={query}", "default_url": "https://www.liveworksheets.com",
     "kategori": "interaktif", "kaynak": "Global"},
    
    {"isim": "Kerim Hoca", "aciklama": "LGS odaklı kaliteli video ve dökümanlar", "strategy": "google_search",
     "target_string": "kerim hoca {query}", "default_url": "https://kerimhoca.com",
     "kategori": "video", "kaynak": "Kerim Hoca"},
    
    {"isim": "PhET Simülasyon", "aciklama": "İnteraktif matematik simülasyonları", "strategy": "native",
     "search_url": "https://phet.colorado.edu/tr/simulations?search={query}", "default_url": "https://phet.colorado.edu",
     "kategori": "interaktif", "kaynak": "PhET"},
    
    {"isim": "Sorubak", "aciklama": "Soru bankası ve tarama testleri", "strategy": "google_search",
     "target_string": "site:sorubak.com {query}", "default_url": "https://www.sorubak.com",
     "kategori": "pdf", "kaynak": "Sorubak"},
]

# --- AKILLI SORG ULUŞTURMA ---
terimler = []
if secilen_sinif != "Hepsi":
    terimler.append(secilen_sinif)
if secilen_konu != "Hepsi":
    terimler.append(secilen_konu)
if ozel_kazanim:
    terimler.append(ozel_kazanim)
    if "M." in ozel_kazanim.upper():
        terimler.append("kazanım")

global_query = " ".join(terimler).strip()
st.session_state.son_arama = global_query

# --- LİNK OLUŞTURMA ---
filtrelenmis_siteler = []
for site in siteler_havuzu:
    if global_query:
        if site["strategy"] == "native":
            encoded = urllib.parse.quote(global_query)
            url = site["search_url"].format(query=encoded)
        else:  # google_search
            ham = site["target_string"].format(query=global_query)
            encoded = urllib.parse.quote(ham)
            url = f"https://www.google.com/search?q={encoded}"
    else:
        url = site["default_url"]
    filtrelenmis_siteler.append({"veri": site, "url": url})

# --- TABS ---
tab1, tab2, tab3, tab4 = st.tabs(["🚀 Kaynak Matrisi", "⭐ Hızlı Öneriler", "❤️ Favorilerim", "📊 Bilgi"])

with tab1:
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Hedef Müfredat", global_query if global_query else "Tüm İçerikler")
    with col2:
        st.metric("Aktif Kaynak", len(filtrelenmis_siteler))
    with col3:
        st.metric("Favori", len(st.session_state.favoriler))

    # Tüm linkleri kopyala butonu
    if st.button("📋 Tüm Linkleri Kopyala", type="primary", use_container_width=True):
        link_list = "\n".join([f"{item['veri']['isim']}: {item['url']}" for item in filtrelenmis_siteler])
        st.code(link_list)
        st.success("Linkler kopyalandı! (Yukarıdaki kutuyu seçip kopyalayın)")

    col_left, col_right = st.columns(2)
    for idx, item in enumerate(filtrelenmis_siteler):
        data = item["veri"]
        url = item["url"]
        
        current_col = col_left if idx % 2 == 0 else col_right
        
        with current_col:
            badge_class = {
                "video": "badge-video",
                "game": "badge-game",
                "pdf": "badge-pdf",
                "interaktif": "badge-interaktif"
            }.get(data["kategori"], "badge-interaktif")
            
            st.markdown(f"""
            <div class="premium-card">
                <span class="badge {badge_class}">{data['kategori'].upper()}</span>
                <div style="font-size:22px; font-weight:700; margin:12px 0;">{data['isim']}</div>
                <p style="color:#475569; line-height:1.5;">{data['aciklama']}</p>
                <div style="margin-top:16px;">
                    <span class="badge badge-sinif">📍 {secilen_sinif}</span>
                    <span class="badge badge-konu">📖 {secilen_konu}</span>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            col_btn1, col_btn2 = st.columns([4,1])
            with col_btn1:
                st.link_button(f"🌐 {data['isim']} Aç", url, use_container_width=True)
            with col_btn2:
                if st.button("❤️", key=f"fav_{idx}"):
                    if item not in st.session_state.favoriler:
                        st.session_state.favoriler.append(item)
                        st.success("Favorilere eklendi!")
                    else:
                        st.info("Zaten favorilerde")

with tab2:
    st.subheader("⭐ Bu Kombinasyon İçin Önerilen En İyi Kaynaklar")
    # Burada el ile seçilmiş en iyi kaynakları önerebilirsin
    st.info("Hızlı öneriler yakında daha akıllı hale getirilecek. Şimdilik filtrelerinizi kullanın.")

with tab3:
    st.subheader("❤️ Favorilerim")
    if st.session_state.favoriler:
        for fav in st.session_state.favoriler:
            st.link_button(fav["veri"]["isim"], fav["url"])
        if st.button("Favorileri Temizle"):
            st.session_state.favoriler = []
            st.rerun()
    else:
        st.info("Henüz favori eklemediniz.")

with tab4:
    st.markdown("### Platform Hakkında")
    st.write("Bu araç Ortak payda öğretmenlerine özel olarak geliştirilmiştir.")
    st.caption("İSMAİL ORHAN © 2026 - v5.2")

# Footer
st.markdown("---")
st.markdown("<p style='text-align:center; color:#94a3b8; font-size:14px;'>Ortaokul Matematik Dijital Ekosistemi</p>", unsafe_allow_html=True)
