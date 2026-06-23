import streamlit as st
import urllib.parse

# --- ULTRA MODERN PREMIUM SAYFA AYARLARI ---
st.set_page_config(
    page_title="Matematik Materyal Motoru Pro v5.3",
    page_icon="📐",
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
    
    .stTabs [data-baseweb="tab-list"] { gap: 16px; border-bottom: 2px solid #e2e8f0; padding-bottom: 10px; }
    .stTabs [data-baseweb="tab"] {
        background-color: #ffffff; border: 1px solid #e2e8f0 !important; padding: 12px 28px;
        border-radius: 16px; font-weight: 600; color: #64748b; transition: all 0.3s;
    }
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #4f46e5 0%, #2563eb 100%) !important;
        color: #ffffff !important; border-color: transparent !important;
    }

    .premium-card {
        background: #ffffff; border-radius: 28px; padding: 30px; margin-bottom: 24px;
        border: 1px solid rgba(226, 232, 240, 0.8); box-shadow: 0 10px 30px -10px rgba(0, 0, 0, 0.03);
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1); position: relative; overflow: hidden;
    }
    .premium-card:hover {
        transform: translateY(-6px); box-shadow: 0 20px 40px -15px rgba(79, 70, 229, 0.15);
        border-color: #4f46e5;
    }
    .premium-card::before {
        content: ''; position: absolute; top: 0; left: 0; width: 6px; height: 100%;
        background: linear-gradient(180deg, #4f46e5 0%, #3b82f6 100%);
    }

    .card-title { color: #0f172a; font-size: 23px; font-weight: 700; letter-spacing: -0.5px; margin-bottom: 10px; }
    .card-desc { color: #475569; font-size: 15px; line-height: 1.6; margin-bottom: 24px; }

    .badge {
        display: inline-flex; align-items: center; padding: 6px 14px;
        border-radius: 9999px; font-size: 12px; font-weight: 700;
        margin-right: 8px; margin-bottom: 8px;
    }
    .badge-sinif { background-color: #f1f5f9; color: #334155; border: 1px solid #e2e8f0; }
    .badge-konu { background-color: #e0f2fe; color: #0369a1; }
    .badge-pdf { background-color: #fee2e2; color: #b91c1c; }
    .badge-video { background-color: #fef3c7; color: #b45309; }
    .badge-game { background-color: #ecfdf5; color: #065f46; }
    .badge-interaktif { background-color: #f3e8ff; color: #6d28d9; }

    .status-indicator {
        float: right; font-size: 11px; font-weight: 700; text-transform: uppercase;
        background-color: #ecfdf5; color: #065f46; padding: 6px 14px; border-radius: 12px;
    }
</style>
""", unsafe_allow_html=True)

# --- SESSION STATE ---
if "favoriler" not in st.session_state:
    st.session_state.favoriler = []

# --- BAŞLIK ALANI ---
st.markdown("<h1 style='color: #0f172a; font-weight: 800; font-size: 40px; letter-spacing: -1px; margin-bottom:4px;'>📐 Matematik Materyal Motoru Pro v5.3</h1>", unsafe_allow_html=True)
st.markdown("<p style='color: #475569; font-size: 16px; margin-top:0px;'>Müfredata tam uyumlu tek durak materyal, oyun, video ve test platformu</p>", unsafe_allow_html=True)

# --- SIDEBAR ---
st.sidebar.markdown("<h2 style='color: #0f172a; font-size: 22px; font-weight: 700;'>🎛️ Parametre İstasyonu</h2>", unsafe_allow_html=True)

sinif_secenekleri = ["Hepsi", "5. Sınıf", "6. Sınıf", "7. Sınıf", "8. Sınıf"]
secilen_sinif = st.sidebar.selectbox("Eğitim Kademesi:", sinif_secenekleri)

konu_secenekleri = ["Hepsi", "Doğal Sayılar", "Kesirler", "Yüzdeler", "Oran ve Orantı", "Cebirsel İfadeler", 
                    "Denklem", "Üslü İfadeler", "Geometri", "Üçgenler", "Çember ve Daire", 
                    "Veri Toplama ve Analizi", "Olasılık"]
secilen_konu = st.sidebar.selectbox("Müfredat Ünitesi:", konu_secenekleri)

ozel_kazanim_sorgu = st.sidebar.text_input("🔍 Kazanım / Kelime:", placeholder="M.8.1.2.1 veya Özdeşlikler").strip()

st.sidebar.markdown("### ⚡ Hızlı Aramalar")
if st.sidebar.button("8. Sınıf Üslü İfadeler"):
    secilen_sinif = "8. Sınıf"
    secilen_konu = "Üslü İfadeler"
if st.sidebar.button("7. Sınıf Denklem"):
    secilen_sinif = "7. Sınıf"
    secilen_konu = "Denklem"

# --- GENİŞLETİLMİŞ SİTE HAVUZU (Hata riski düşük linkler) ---
siteler_havuzu = [
    {"isim": "EBA", "aciklama": "Resmi MEB video, etkileşimli içerik ve akıllı tahta dersleri", "strategy": "native",
     "search_url": "https://www.eba.gov.tr/arama?q={query}", "kategori": "video", "kaynak": "MEB"},
    
    {"isim": "Khan Academy Türkçe", "aciklama": "Ücretsiz yüksek kaliteli video dersler ve alıştırmalar", "strategy": "native",
     "search_url": "https://tr.khanacademy.org/search?query={query}", "kategori": "video", "kaynak": "Khan"},
    
    {"isim": "GeoGebra", "aciklama": "Dinamik geometri simülasyonları ve interaktif modelleme", "strategy": "native",
     "search_url": "https://www.geogebra.org/search/{query}", "kategori": "interaktif", "kaynak": "GeoGebra"},
    
    {"isim": "Wordwall", "aciklama": "Binlerce öğretmen yapımı interaktif oyun ve yarışma", "strategy": "native",
     "search_url": "https://wordwall.net/tr/community?query={query}", "kategori": "game", "kaynak": "Wordwall"},
    
    {"isim": "Matematik Vakti", "aciklama": "PDF test, çalışma kağıdı, kazanım testleri", "strategy": "google_search",
     "target_string": "site:matematikvakti.net {query}", "kategori": "pdf", "kaynak": "Matematik Vakti"},
    
    {"isim": "Kerim Hoca", "aciklama": "LGS odaklı video anlatım ve test çözümleri", "strategy": "native",
     "search_url": "https://kerimhoca.com/?s={query}", "kategori": "video", "kaynak": "Kerim Hoca"},
    
    {"isim": "Liveworksheets", "aciklama": "Etkileşimli dijital çalışma yaprakları", "strategy": "native",
     "search_url": "https://www.liveworksheets.com/search?query={query}", "kategori": "interaktif", "kaynak": "Global"},
    
    {"isim": "Sorubak", "aciklama": "Soru bankası, tarama testi ve deneme sınavları", "strategy": "google_search",
     "target_string": "site:sorubak.com {query}", "kategori": "pdf", "kaynak": "Sorubak"},
    
    {"isim": "Matific Türkiye", "aciklama": "Oyunlaştırılmış matematik öğrenme platformu", "strategy": "native",
     "search_url": "https://www.matific.com/tr/tr/home/maths-zone/?q={query}", "kategori": "game", "kaynak": "Matific"},
    
    {"isim": "Mathigon TR", "aciklama": "Modern interaktif matematik dersleri", "strategy": "native",
     "search_url": "https://tr.mathigon.org/search?q={query}", "kategori": "interaktif", "kaynak": "Mathigon"},
]

# --- AKILLI SORGUBULDER ---
terimler = []
if secilen_sinif != "Hepsi": terimler.append(secilen_sinif)
if secilen_konu != "Hepsi": terimler.append(secilen_konu)
if ozel_kazanim_sorgu: terimler.append(ozel_kazanim_sorgu)
if ozel_kazanim_sorgu and "M." in ozel_kazanim_sorgu.upper():
    terimler.append("kazanım")

global_mufredat_string = " ".join(terimler).strip()

# --- LİNK OLUŞTURMA (Hata toleransı eklendi) ---
filtrelenmis_siteler = []
for site in siteler_havuzu:
    if global_mufredat_string:
        try:
            if site["strategy"] == "native":
                encoded = urllib.parse.quote(global_mufredat_string)
                link = site["search_url"].format(query=encoded)
            else:
                ham_sorgu = site["target_string"].format(query=global_mufredat_string)
                encoded = urllib.parse.quote(ham_sorgu)
                link = f"https://www.google.com/search?q={encoded}"
        except:
            link = site.get("search_url", "#").replace("{query}", global_mufredat_string)
    else:
        link = site.get("search_url", "#").replace("{query}", "matematik")
        
    filtrelenmis_siteler.append({"veri": site, "url": link})

# --- TABS ---
tab1, tab2, tab3 = st.tabs(["🚀 Aktif Eğitim Kanalları", "❤️ Favorilerim", "📊 Bilgi"])

with tab1:
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown(f'<div class="metric-box"><p style="margin:0;color:#64748b;">HEDEFLENEN MÜFREDAT</p><h4>{global_mufredat_string if global_mufredat_string else "Tüm Havuz"}</h4></div>', unsafe_allow_html=True)
    with c2:
        st.markdown(f'<div class="metric-box"><p style="margin:0;color:#64748b;">AKTİF KANAL</p><h4>{len(filtrelenmis_siteler)} Kaynak</h4></div>', unsafe_allow_html=True)
    with c3:
        st.markdown(f'<div class="metric-box"><p style="margin:0;color:#64748b;">FAVORİ</p><h4>{len(st.session_state.favoriler)}</h4></div>', unsafe_allow_html=True)

    if st.button("📋 Tüm Linkleri Kopyala", type="primary", use_container_width=True):
        link_text = "\n\n".join([f"{item['veri']['isim']}:\n{item['url']}" for item in filtrelenmis_siteler])
        st.code(link_text)
        st.success("Tüm linkler kopyalandı!")

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
            
            colb1, colb2 = st.columns([4,1])
            with colb1:
                st.link_button(f"🎯 {data['isim']} Aç", target_link, use_container_width=True)
            with colb2:
                if st.button("❤️", key=f"fav_{index}"):
                    if not any(f["veri"]["isim"] == data["isim"] for f in st.session_state.favoriler):
                        st.session_state.favoriler.append(item)
                        st.success("Favorilere eklendi ❤️")
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
        st.info("Henüz favori eklenmedi. Kalp butonuna tıklayarak ekleyebilirsiniz.")

with tab3:
    st.markdown("Bu araç öğretmenlerin zamanını kurtarmak için geliştirilmiştir. Sorun yaşadığın herhangi bir site olursa söyle, hemen düzeltelim.")

st.sidebar.caption("Tüm linkler dinamik olarak güncellenir. Ortak patda öğretmenlerine özel geliştirildi  © İSMAİL ORHAN 2026")

st.markdown("---")
st.markdown("<p style='text-align: center; color: #94a3b8; font-size: 13px;'>Ortaokul Matematik Dijital Ekosistemi</p>", unsafe_allow_html=True)
