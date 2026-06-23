import streamlit as st
import urllib.parse

# --- ULTRA MODERN PREMIUM AYARLAR ---
st.set_page_config(
    page_title="Matematik Materyal Motoru Pro v5.4",
    page_icon="📐",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- CSS MASTERBLOCK (Orijinal uzun tasarım) ---
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
    
    .stTabs [data-baseweb="tab-list"] {
        gap: 16px;
        border-bottom: 2px solid #e2e8f0;
        padding-bottom: 10px;
    }
    .stTabs [data-baseweb="tab"] {
        background-color: #ffffff;
        border: 1px solid #e2e8f0 !important;
        padding: 12px 28px;
        border-radius: 16px;
        font-weight: 600;
        color: #64748b;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    }
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #4f46e5 0%, #2563eb 100%) !important;
        color: #ffffff !important;
        border-color: transparent !important;
        box-shadow: 0 10px 15px -3px rgba(79, 70, 229, 0.3);
    }

    .premium-card {
        background: #ffffff;
        border-radius: 28px;
        padding: 30px;
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

    .card-title {
        color: #0f172a;
        font-size: 23px;
        font-weight: 700;
        letter-spacing: -0.5px;
        margin-bottom: 10px;
    }
    .card-desc {
        color: #475569;
        font-size: 15px;
        line-height: 1.6;
        margin-bottom: 24px;
    }

    .badge {
        display: inline-flex;
        align-items: center;
        padding: 6px 14px;
        border-radius: 9999px;
        font-size: 12px;
        font-weight: 700;
        margin-right: 8px;
        margin-bottom: 8px;
    }
    .badge-sinif { background-color: #f1f5f9; color: #334155; border: 1px solid #e2e8f0; }
    .badge-konu { background-color: #e0f2fe; color: #0369a1; }
    .badge-pdf { background-color: #fee2e2; color: #b91c1c; }
    .badge-video { background-color: #fef3c7; color: #b45309; }
    .badge-game { background-color: #ecfdf5; color: #065f46; }
    .badge-interaktif { background-color: #f3e8ff; color: #6d28d9; }

    .status-indicator {
        float: right;
        font-size: 11px;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        background-color: #ecfdf5;
        color: #065f46;
        padding: 6px 14px;
        border-radius: 12px;
    }

    .metric-box {
        background: #ffffff;
        padding: 24px;
        border-radius: 24px;
        border: 1px solid #e2e8f0;
        text-align: center;
        box-shadow: 0 4px 6px -1px rgba(0,0,0,0.01);
    }
</style>
""", unsafe_allow_html=True)

# --- SESSION STATE ---
if "favoriler" not in st.session_state:
    st.session_state.favoriler = []

# --- BAŞLIK ---
st.markdown("<h1 style='color: #0f172a; font-weight: 800; font-size: 40px; letter-spacing: -1px; margin-bottom:4px;'>📐 Matematik Materyal Motoru Pro v5.4</h1>", unsafe_allow_html=True)
st.markdown("<p style='color: #475569; font-size: 16px; margin-top:0px;'>Müfredata %100 uyumlu tek tıkla materyal, oyun, video, PDF ve interaktif içerik motoru</p>", unsafe_allow_html=True)

# --- SIDEBAR ---
st.sidebar.markdown("<h2 style='color: #0f172a; font-size: 22px; font-weight: 700; margin-bottom: 15px;'>🎛️ Parametre İstasyonu</h2>", unsafe_allow_html=True)

sinif_secenekleri = ["Hepsi", "5. Sınıf", "6. Sınıf", "7. Sınıf", "8. Sınıf"]
secilen_sinif = st.sidebar.selectbox("Eğitim Kademesi:", sinif_secenekleri)

konu_secenekleri = ["Hepsi", "Doğal Sayılar", "Kesirler", "Yüzdeler", "Oran ve Orantı", "Cebirsel İfadeler", 
                    "Eşitlik ve Denklem", "Üslü İfadeler", "Geometri", "Üçgenler", "Çember ve Daire", 
                    "Veri Toplama ve Analizi", "Olasılık", "Koordinat Sistemi"]
secilen_konu = st.sidebar.selectbox("Müfredat Ünitesi:", konu_secenekleri)

ozel_kazanim_sorgu = st.sidebar.text_input("🔍 Odaklanılacak Kazanım / Kelime:", placeholder="M.8.1.2.1 veya Özdeşlikler").strip()

st.sidebar.markdown("### ⚡ Hızlı Aramalar")
if st.sidebar.button("8. Sınıf Üslü İfadeler"):
    secilen_sinif = "8. Sınıf"
    secilen_konu = "Üslü İfadeler"
if st.sidebar.button("7. Sınıf Denklem"):
    secilen_sinif = "7. Sınıf"
    secilen_konu = "Eşitlik ve Denklem"

# --- GÜNCELLENMİŞ VE STABİL SİTE HAVUZU ---
siteler_havuzu = [
    {"isim": "EBA", "aciklama": "MEB resmi video, interaktif ve akıllı tahta içerikleri", "strategy": "native",
     "search_url": "https://www.eba.gov.tr/arama?q={query}", "kategori": "video", "kaynak": "MEB"},
    
    {"isim": "Khan Academy Türkçe", "aciklama": "Yüksek kaliteli video dersler ve alıştırmalar", "strategy": "native",
     "search_url": "https://tr.khanacademy.org/search?query={query}", "kategori": "video", "kaynak": "Khan"},
    
    {"isim": "Wordwall", "aciklama": "Öğretmen yapımı interaktif oyun ve etkinlikler", "strategy": "native",
     "search_url": "https://wordwall.net/tr/community?query={query}", "kategori": "game", "kaynak": "Wordwall"},
    
    {"isim": "GeoGebra", "aciklama": "Dinamik geometri ve simülasyon laboratuvarı", "strategy": "native",
     "search_url": "https://www.geogebra.org/search/{query}", "kategori": "interaktif", "kaynak": "GeoGebra"},
    
    {"isim": "Kerim Hoca", "aciklama": "LGS video anlatım, test ve soru çözümleri", "strategy": "native",
     "search_url": "https://kerimhoca.com/?s={query}", "kategori": "video", "kaynak": "Kerim Hoca"},
    
    {"isim": "Liveworksheets", "aciklama": "Etkileşimli çalışma yaprakları (arama ana sayfadan yapılmalı)", "strategy": "google_search",
     "target_string": "site:liveworksheets.com {query} matematik", "kategori": "interaktif", "kaynak": "Global"},
    
    {"isim": "Matematik Vakti", "aciklama": "PDF test, kazanım testleri ve çalışma kağıtları", "strategy": "google_search",
     "target_string": "site:matematikvakti.net {query}", "kategori": "pdf", "kaynak": "Matematik Vakti"},
    
    {"isim": "Sorubak", "aciklama": "Soru bankası, tarama testi ve deneme", "strategy": "google_search",
     "target_string": "site:sorubak.com {query}", "kategori": "pdf", "kaynak": "Sorubak"},
    
    {"isim": "Matific", "aciklama": "Oyunlaştırılmış matematik platformu", "strategy": "google_search",
     "target_string": "matific {query} türkiye", "kategori": "game", "kaynak": "Matific"},
    
    {"isim": "Toy Theater", "aciklama": "Eğlenceli matematik oyunları ve manipülatifler", "strategy": "google_search",
     "target_string": "site:toytheater.com {query}", "kategori": "game", "kaynak": "Toy Theater"},
]

# --- AKILLI SORG U ---
terimler = []
if secilen_sinif != "Hepsi": terimler.append(secilen_sinif)
if secilen_konu != "Hepsi": terimler.append(secilen_konu)
if ozel_kazanim_sorgu: terimler.append(ozel_kazanim_sorgu)
if ozel_kazanim_sorgu and "M." in ozel_kazanim_sorgu.upper():
    terimler.append("kazanım")

global_mufredat_string = " ".join(terimler).strip()

# --- LİNK OLUŞTURMA (Gelişmiş Hata Toleransı) ---
filtrelenmis_siteler = []
for site in siteler_havuzu:
    if global_mufredat_string:
        try:
            if site["strategy"] == "native":
                encoded = urllib.parse.quote(global_mufredat_string)
                link = site["search_url"].format(query=encoded)
            else:
                ham = site["target_string"].format(query=global_mufredat_string)
                encoded = urllib.parse.quote(ham)
                link = f"https://www.google.com/search?q={encoded}"
        except Exception:
            link = site.get("search_url", "#")
    else:
        link = site.get("search_url", "#").replace("{query}", "matematik")
    
    filtrelenmis_siteler.append({"veri": site, "url": link})

# --- TABS ---
tab1, tab2, tab3 = st.tabs(["🚀 Aktif Eğitim Kanalları Matrisi", "❤️ Favorilerim", "📊 Bilgi"])

with tab1:
    c_1, c_2, c_3 = st.columns(3)
    with c_1:
        st.markdown(f'<div class="metric-box"><p style="margin:0;color:#64748b;font-weight:600;">HEDEFLENEN MÜFREDAT</p><h4 style="margin:6px 0 0 0;color:#0f172a;">{global_mufredat_string if global_mufredat_string else "Tüm Havuz"}</h4></div>', unsafe_allow_html=True)
    with c_2:
        st.markdown(f'<div class="metric-box"><p style="margin:0;color:#64748b;font-weight:600;">AKTİF KANAL</p><h4 style="margin:6px 0 0 0;color:#4f46e5;">{len(filtrelenmis_siteler)} Kaynak</h4></div>', unsafe_allow_html=True)
    with c_3:
        st.markdown(f'<div class="metric-box"><p style="margin:0;color:#64748b;font-weight:600;">FAVORİ</p><h4 style="margin:6px 0 0 0;color:#059669;">{len(st.session_state.favoriler)}</h4></div>', unsafe_allow_html=True)

    if st.button("📋 Tüm Linkleri Tek Tıkla Kopyala", type="primary", use_container_width=True):
        link_list = "\n\n".join([f"{item['veri']['isim']}:\n{item['url']}" for item in filtrelenmis_siteler])
        st.code(link_list)
        st.success("✅ Tüm linkler kopyalandı! Öğrencilerine veya zümreye gönderebilirsin.")

    col_left, col_right = st.columns(2)
    for index, item in enumerate(filtrelenmis_siteler):
        data = item["veri"]
        target_link = item["url"]
        current_col = col_left if index % 2 == 0 else col_right
        
        with current_col:
            badge_class = f"badge-{data.get('kategori', 'interaktif')}"
            st.markdown(f"""
            <div class="premium-card">
                <span class="status-indicator">⚡ AKTİF</span>
                <div class="card-title">{data['isim']}</div>
                <div class="card-desc">{data['aciklama']}</div>
                <div>
                    <span class="badge badge-sinif">📍 {secilen_sinif}</span>
                    <span class="badge badge-konu">📖 {secilen_konu}</span>
                    <span class="badge {badge_class}">{data.get('kategori','').upper()}</span>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            b1, b2 = st.columns([4, 1])
            with b1:
                st.link_button(f"🎯 {data['isim']} Sayfasını Aç", target_link, use_container_width=True)
            with b2:
                if st.button("❤️", key=f"fav_{index}"):
                    if not any(f["veri"]["isim"] == data["isim"] for f in st.session_state.favoriler):
                        st.session_state.favoriler.append(item)
                        st.success("❤️ Favorilere eklendi!")
                    else:
                        st.info("Zaten favorilerde")

with tab2:
    st.subheader("❤️ Favorilerim")
    if st.session_state.favoriler:
        for fav in st.session_state.favoriler:
            st.link_button(fav["veri"]["isim"], fav["url"], use_container_width=True)
        if st.button("Favorileri Temizle"):
            st.session_state.favoriler = []
            st.rerun()
    else:
        st.info("Favori eklemek için kartlardaki ❤️ butonuna tıklayın.")

with tab3:
    st.markdown("""
    **İpuçları:**
    - Bazı sitelerde arama sonuçları Google üzerinden daha iyi çıkıyor.
    - Hata alırsan siteyi direkt tarayıcıda açıp manuel arama yap.
    - Tüm linkleri kopyala butonu öğretmenler için çok işe yarıyor.
    """)

st.sidebar.caption("Dinamik olarak güncelleniyor • © İSMAİL ORHAN 2026")
st.markdown("---")
st.markdown("<p style='text-align: center; color: #94a3b8; font-size: 13px;'>Ortaokul Matematik Dijital Ekosistemi</p>", unsafe_allow_html=True)
