import streamlit as st
import urllib.parse

st.set_page_config(
    page_title="Matematik Materyal Motoru Pro v5.3",
    page_icon="📐",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS (önceki + küçük iyileştirmeler)
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800&display=swap');
    html, body, [data-testid="stAppViewContainer"] { background-color: #f8fafc; font-family: 'Outfit', sans-serif; }
    .premium-card {
        background: #ffffff; border-radius: 28px; padding: 28px; margin-bottom: 24px;
        border: 1px solid rgba(226, 232, 240, 0.8); box-shadow: 0 10px 30px -10px rgba(0,0,0,0.03);
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1); position: relative; overflow: hidden;
    }
    .premium-card:hover { transform: translateY(-6px); box-shadow: 0 20px 40px -15px rgba(79,70,229,0.15); }
    .premium-card::before {
        content: ''; position: absolute; top: 0; left: 0; width: 6px; height: 100%;
        background: linear-gradient(180deg, #4f46e5 0%, #3b82f6 100%);
    }
    .badge { display: inline-flex; align-items: center; padding: 6px 14px; border-radius: 9999px;
              font-size: 12px; font-weight: 700; margin-right: 8px; margin-bottom: 8px; }
    .badge-sinif { background-color: #f1f5f9; color: #334155; }
    .badge-konu { background-color: #e0f2fe; color: #0369a1; }
    .badge-pdf { background-color: #fee2e2; color: #b91c1c; }
    .badge-video { background-color: #fef3c7; color: #b45309; }
    .badge-game { background-color: #ecfdf5; color: #065f46; }
    .badge-interaktif { background-color: #f3e8ff; color: #6d28d9; }
</style>
""", unsafe_allow_html=True)

# Session State
if "favoriler" not in st.session_state: st.session_state.favoriler = []

# Başlık
st.markdown("<h1 style='color: #0f172a; font-weight: 800; font-size: 42px; letter-spacing: -1.5px;'>📐 Matematik Materyal Motoru Pro v5.3</h1>", unsafe_allow_html=True)
st.markdown("<p style='color: #475569; font-size: 17px;'>Tek platformda kaliteli materyal, oyun, video, test ve PDF</p>", unsafe_allow_html=True)

# Sidebar
st.sidebar.markdown("### 🎛️ Filtre İstasyonu")
sinif_secenekleri = ["Hepsi", "5. Sınıf", "6. Sınıf", "7. Sınıf", "8. Sınıf"]
secilen_sinif = st.sidebar.selectbox("Sınıf Seviyesi", sinif_secenekleri)

konu_secenekleri = ["Hepsi", "Doğal Sayılar", "Kesirler", "Yüzdeler", "Oran-Orantı", "Cebirsel İfadeler", 
                    "Denklem", "Üslü İfadeler", "Geometri", "Üçgenler", "Çember", "Veri Analizi", "Olasılık"]
secilen_konu = st.sidebar.selectbox("Konu", konu_secenekleri)
ozel_kazanim = st.sidebar.text_input("🔍 Kazanım / Kelime", placeholder="M.8.1.2.1 veya Özdeşlikler").strip()

st.sidebar.markdown("### ⚡ Hızlı Aramalar")
if st.sidebar.button("8. Sınıf Üslü İfadeler"): 
    secilen_sinif, secilen_konu = "8. Sınıf", "Üslü İfadeler"
if st.sidebar.button("7. Sınıf Denklem"): 
    secilen_sinif, secilen_konu = "7. Sınıf", "Denklem"

# GENİŞLETİLMİŞ SİTE HAVUZU
siteler_havuzu = [
    {"isim": "EBA", "aciklama": "Resmi MEB video ve etkileşimli içerikler", "strategy": "native",
     "search_url": "https://www.eba.gov.tr/arama?q={query}", "kategori": "video"},
    
    {"isim": "Khan Academy Türkçe", "aciklama": "Kaliteli video + alıştırma", "strategy": "native",
     "search_url": "https://tr.khanacademy.org/search?query={query}", "kategori": "video"},
    
    {"isim": "GeoGebra", "aciklama": "Dinamik geometri simülasyonları", "strategy": "native",
     "search_url": "https://www.geogebra.org/search/{query}", "kategori": "interaktif"},
    
    {"isim": "Wordwall", "aciklama": "İnteraktif oyun ve etkinlik", "strategy": "native",
     "search_url": "https://wordwall.net/tr/community?query={query}", "kategori": "game"},
    
    {"isim": "Matematik Vakti", "aciklama": "PDF test, çalışma kağıdı, deneme", "strategy": "google_search",
     "target_string": "site:matematikvakti.net {query}", "kategori": "pdf"},
    
    {"isim": "Kerim Hoca", "aciklama": "LGS video, test ve çıkmış soru", "strategy": "native",
     "search_url": "https://kerimhoca.com/?s={query}", "kategori": "video"},
    
    {"isim": "Sinan Sarıtaş", "aciklama": "Oyunlar ve interaktif etkinlikler", "strategy": "google_search",
     "target_string": "site:sinansaritas.com {query}", "kategori": "game"},
    
    {"isim": "Matific", "aciklama": "Oyunlaştırılmış matematik", "strategy": "native",
     "search_url": "https://www.matific.com/tr/tr/home/maths-zone/?q={query}", "kategori": "game"},
    
    {"isim": "Mathigon TR", "aciklama": "İleri seviye interaktif dersler", "strategy": "native",
     "search_url": "https://tr.mathigon.org/?q={query}", "kategori": "interaktif"},
    
    {"isim": "Liveworksheets", "aciklama": "Etkileşimli çalışma yaprakları", "strategy": "native",
     "search_url": "https://www.liveworksheets.com/search?query={query}", "kategori": "interaktif"},
    
    {"isim": "Sorubak", "aciklama": "Soru bankası ve testler", "strategy": "google_search",
     "target_string": "site:sorubak.com {query}", "kategori": "pdf"},
]

# Akıllı Sorgu
terimler = [x for x in [secilen_sinif, secilen_konu, ozel_kazanim] if x != "Hepsi" and x]
if ozel_kazanim and "M." in ozel_kazanim.upper():
    terimler.append("kazanım")
global_query = " ".join(terimler).strip()

# Link Oluşturma
filtrelenmis_siteler = []
for site in siteler_havuzu:
    if global_query:
        try:
            if site["strategy"] == "native":
                encoded = urllib.parse.quote(global_query)
                url = site["search_url"].format(query=encoded)
            else:
                ham = site["target_string"].format(query=global_query)
                encoded = urllib.parse.quote(ham)
                url = f"https://www.google.com/search?q={encoded}"
        except:
            url = site.get("default_url", "#")
    else:
        url = site.get("default_url", site.get("search_url", "#").replace("{query}", "matematik"))
    filtrelenmis_siteler.append({"veri": site, "url": url})

# Tabs
tab1, tab2, tab3 = st.tabs(["🚀 Kaynak Matrisi", "❤️ Favorilerim", "ℹ️ Bilgi"])

with tab1:
    c1, c2, c3 = st.columns(3)
    c1.metric("Müfredat", global_query or "Tüm İçerikler")
    c2.metric("Kaynak Sayısı", len(filtrelenmis_siteler))
    c3.metric("Favori", len(st.session_state.favoriler))

    if st.button("📋 Tüm Linkleri Kopyala", type="primary", use_container_width=True):
        links = "\n\n".join([f"{item['veri']['isim']}\n{item['url']}" for item in filtrelenmis_siteler])
        st.code(links)
        st.success("Linkler hazır!")

    col_left, col_right = st.columns(2)
    for idx, item in enumerate(filtrelenmis_siteler):
        data = item["veri"]
        url = item["url"]
        col = col_left if idx % 2 == 0 else col_right
        
        with col:
            badge_class = f"badge-{data['kategori']}"
            st.markdown(f"""
            <div class="premium-card">
                <span class="badge {badge_class}">{data['kategori'].upper()}</span>
                <h3>{data['isim']}</h3>
                <p>{data['aciklama']}</p>
            </div>
            """, unsafe_allow_html=True)
            
            b1, b2 = st.columns([4,1])
            with b1:
                st.link_button(f"🌐 {data['isim']} Aç", url, use_container_width=True)
            with b2:
                if st.button("❤️", key=f"fav_{idx}"):
                    if not any(f["veri"]["isim"] == data["isim"] for f in st.session_state.favoriler):
                        st.session_state.favoriler.append(item)
                        st.toast("Favorilere eklendi!", icon="❤️")
                    else:
                        st.toast("Zaten favorilerde")

with tab2:
    st.subheader("❤️ Favorilerim")
    if st.session_state.favoriler:
        for fav in st.session_state.favoriler:
            st.link_button(fav["veri"]["isim"], fav["url"])
        if st.button("Tüm Favorileri Temizle"):
            st.session_state.favoriler = []
            st.rerun()
    else:
        st.info("Favori eklemek için kalp butonuna tıklayın.")

with tab3:
    st.info("**İpucu:** Arama yaptıktan sonra 'Tüm Linkleri Kopyala' butonunu kullan. Böylece hepsini öğrencilerine tek mesajda gönderebilirsin.")

st.markdown("---")
st.markdown("<p style='text-align:center; color:#94a3b8;'>İSMAİL ORHAN © 2026 - v5.3</p>", unsafe_allow_html=True)
