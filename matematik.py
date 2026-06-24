import streamlit as st
import urllib.parse

# --- ULTRA MODERN PREMIUM SAYFA AYARLARI ---
st.set_page_config(
    page_title="Matematik Materyal Motoru",
    page_icon="📐",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- LUXURY EXECUTIVE DASHBOARD DESIGN (CSS MASTERBLOCK) ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800&display=swap');
    
    /* Global Alan Düzenlemesi */
    html, body, [data-testid="stAppViewContainer"] {
        background-color: #f8fafc;
        font-family: 'Outfit', sans-serif;
    }
    
    /* Yan Menü Premium Revizyonu */
    [data-testid="stSidebar"] {
        background-color: #ffffff !important;
        border-right: 1px solid #e2e8f0;
    }
    
    /* Üst Sekme Çubuğu Modernizasyonu */
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

    /* ULTRA MODERN GLOW-CARD MİMARİSİ */
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

    /* Kapsül Rozetler */
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
    .badge-origin { background-color: #fef3c7; color: #b45309; }
    
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

# --- BAŞLIK ALANI (HEADER) ---
st.markdown("<h1 style='color: #0f172a; font-weight: 800; font-size: 40px; letter-spacing: -1px; margin-bottom:4px;'>📐 Ortaokul Matematik Dijital Entegrasyon Paneli</h1>", unsafe_allow_html=True)
st.markdown("<p style='color: #475569; font-size: 16px; margin-top:0px;'>Müfredat kazanımları ile tam senkronize çalışan, çok dilli arama optimizasyonlu kurumsal yönetim platformu.</p>", unsafe_allow_html=True)

# --- SIDEBAR CONTROL PANEL ---
st.sidebar.markdown("<h2 style='color: #0f172a; font-size: 22px; font-weight: 700; margin-bottom: 15px;'>🎛️ Parametre İstasyonu</h2>", unsafe_allow_html=True)

sinif_secenekleri = ["Hepsi", "5. Sınıf", "6. Sınıf", "7. Sınıf", "8. Sınıf"]
secilen_sinif = st.sidebar.selectbox("Eğitim Kademesi:", sinif_secenekleri)

konu_secenekleri = ["Hepsi", "Doğal Sayılar", "Doğal Sayılarla İşlemler", "Çarpanlar ve Katlar", "Kümeler", "Tam Sayılar",
                    "Kesirler", "Kesirlerle İşlemler", "Ondalık Gösterim", "Rasyonel Sayılar", "Üslü İfadeler", "Kareköklü İfadeler",
                    "Oran ve Orantı", "Yüzdeler", "Cebirsel İfadeler", "Eşitlik ve Denklem", "Doğrusal Denklemler", "Eşitsizlikler",
                    "Temel Geometrik Kavramlar", "Doğrular ve Açılar", "Çokgenler", "Üçgenler", "Çember ve Daire", "Eşlik ve Benzerlik",
                    "Dönüşüm Geometrisi", "Geometrik Cisimler", "Veri Toplama ve Analizi", "Olasılık", "Koordinat Sistemi"]

secilen_konu = st.sidebar.selectbox("Müfredat Ünitesi:", konu_secenekleri)
ozel_kazanim_sorgu = st.sidebar.text_input("🔍 Odaklanılacak Kazanım Terimi:", placeholder="Örn: M.8.1.2.1 veya Özdeşlikler...").strip()

st.sidebar.markdown("### ⚡ Hızlı Aramalar")
if st.sidebar.button("8. Sınıf Üslü İfadeler"):
    secilen_sinif = "8. Sınıf"
    secilen_konu = "Üslü İfadeler"
if st.sidebar.button("7. Sınıf Denklem"):
    secilen_sinif = "7. Sınıf"
    secilen_konu = "Eşitlik ve Denklem"
if st.sidebar.button("6. Sınıf Oran Orantı"):
    secilen_sinif = "6. Sınıf"
    secilen_konu = "Oran ve Orantı"

# --- ÇOK GENİŞLETİLMİŞ SİTE HAVUZU (Özel ders ve okul için en iyi kaynaklar) ---
siteler_havuzu = [
    {"isim": "EBA", "aciklama": "Milli Eğitim Bakanlığı resmi video ders anlatımları, interaktif içerikler ve akıllı tahta materyalleri. En güvenilir resmi kaynak.", "strategy": "native",
     "search_url": "https://www.eba.gov.tr/arama?q={query}", "kategori": "video", "kaynak": "MEB Resmi"},
    
    {"isim": "Khan Academy Türkçe", "aciklama": "Dünya standartlarında video dersler, alıştırma soruları ve ilerleme takibi. Özel ders için çok ideal.", "strategy": "native",
     "search_url": "https://tr.khanacademy.org/search?query={query}", "kategori": "video", "kaynak": "Khan Academy"},
    
    {"isim": "Wordwall Topluluk", "aciklama": "Öğretmenler tarafından hazırlanmış binlerce interaktif oyun, yarışma ve etkinlik. Öğrenciler bayılıyor.", "strategy": "native",
     "search_url": "https://wordwall.net/tr/community?query={query}", "kategori": "game", "kaynak": "Global Topluluk"},
    
    {"isim": "GeoGebra", "aciklama": "Dinamik geometri simülasyonları, grafik çizimi ve interaktif modelleme. Geometri konuları için vazgeçilmez.", "strategy": "native",
     "search_url": "https://www.geogebra.org/search/{query}", "kategori": "interaktif", "kaynak": "GeoGebra"},
    
    {"isim": "Kerim Hoca", "aciklama": "LGS seviyesinde kaliteli video anlatımlar, test çözümleri ve konu özetleri.", "strategy": "native",
     "search_url": "https://kerimhoca.com/?s={query}", "kategori": "video", "kaynak": "Kerim Hoca"},
    
    {"isim": "Sinan Sarıtaş", "aciklama": "Eğlenceli oyunlar, PDF çalışma kağıtları, etkinlikler ve interaktif materyaller.", "strategy": "google_search",
     "target_string": "site:sinansaritas.com {query}", "kategori": "game", "kaynak": "Sinan Sarıtaş"},
    
    {"isim": "Matematik.biz", "aciklama": "Konu anlatımları, kazanım testleri, çalışma yaprakları ve PDF dökümanlar.", "strategy": "google_search",
     "target_string": "site:matematik.biz {query}", "kategori": "pdf", "kaynak": "Matematik.biz"},
    
    {"isim": "Liveworksheets", "aciklama": "Dünya çapında etkileşimli çalışma yaprakları. Öğrenciler anında dönüt alır.", "strategy": "google_search",
     "target_string": "site:liveworksheets.com {query} matematik", "kategori": "interaktif", "kaynak": "Global"},
    
    {"isim": "Matific Türkiye", "aciklama": "Oyunlaştırılmış, pedagojik matematik öğrenme platformu. Bireysel takip çok güçlü.", "strategy": "google_search",
     "target_string": "matific {query} türkiye", "kategori": "game", "kaynak": "Matific"},
    
    {"isim": "PhET Simülasyon", "aciklama": "Üniversite düzeyinde interaktif simülasyonlar. Kavramları somutlaştırmak için mükemmel.", "strategy": "native",
     "search_url": "https://phet.colorado.edu/tr/simulations/filter?subjects=math&search={query}", "kategori": "interaktif", "kaynak": "PhET"},
    
    {"isim": "Toy Theater", "aciklama": "Eğlenceli matematik oyunları ve sanal manipülatifler.", "strategy": "native",
     "search_url": "https://toytheater.com/category/math-games/", "kategori": "game", "kaynak": "Toy Theater"},
    
    {"isim": "Sorubak", "aciklama": "Zengin soru bankası, tarama testleri ve LGS hazırlık materyalleri.", "strategy": "google_search",
     "target_string": "site:sorubak.com {query}", "kategori": "pdf", "kaynak": "Sorubak"},
]

# --- AKILLI SORGUBULDER ---
terimler = []
if secilen_sinif != "Hepsi": terimler.append(secilen_sinif)
if secilen_konu != "Hepsi": terimler.append(secilen_konu)
if ozel_kazanim_sorgu: terimler.append(ozel_kazanim_sorgu)
if ozel_kazanim_sorgu and "M." in ozel_kazanim_sorgu.upper():
    terimler.append("kazanım")

global_mufredat_string = " ".join(terimler).strip()

# --- LİNK OLUŞTURMA VE SÜZGEÇ ALGORİTMASI ---
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
            link = site.get("search_url", "#")
    else:
        link = site.get("search_url", "#").replace("{query}", "matematik")
    filtrelenmis_siteler.append({"veri": site, "url": link})

# --- SEKMELİ ULTRA MODERN GÖRÜNÜM PANAROMASI ---
tab1, tab2, tab3 = st.tabs(["🚀 Aktif Eğitim Kanalları Matrisi", "❤️ Favorilerim", "📊 Kurumsal Entegrasyon Şeması"])

with tab1:
    c_1, c_2, c_3 = st.columns(3)
    with c_1:
        st.markdown(f'<div class="metric-box"><p style="margin:0;color:#64748b;font-weight:600;font-size:13px;letter-spacing:0.5px;">HEDEFLENEN MÜFREDAT GRUBU</p><h4 style="margin:6px 0 0 0;color:#0f172a;font-weight:700;font-size:16px;">{global_mufredat_string if global_mufredat_string else "Tüm Akademik Havuz Aktif"}</h4></div>', unsafe_allow_html=True)
    with c_2:
        st.markdown(f'<div class="metric-box"><p style="margin:0;color:#64748b;font-weight:600;font-size:13px;letter-spacing:0.5px;">EŞ ZAMANLI ENTEGRE SİSTEM</p><h4 style="margin:6px 0 0 0;color:#4f46e5;font-weight:700;font-size:16px;">{len(filtrelenmis_siteler)} Aktif Veri Kanalı</h4></div>', unsafe_allow_html=True)
    with c_3:
        st.markdown(f'<div class="metric-box"><p style="margin:0;color:#64748b;font-weight:600;font-size:13px;letter-spacing:0.5px;">FAVORİLER</p><h4 style="margin:6px 0 0 0;color:#059669;font-weight:700;font-size:16px;">{len(st.session_state.favoriler)} Kaynak</h4></div>', unsafe_allow_html=True)

    if st.button("📋 Tüm Linkleri Kopyala", type="primary", use_container_width=True):
        link_list = "\n\n".join([f"{item['veri']['isim']}:\n{item['url']}" for item in filtrelenmis_siteler])
        st.code(link_list)
        st.success("✅ Tüm linkler kopyalandı!")

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
                    <span class="badge badge-sinif">📍 {secilen_sinif if secilen_sinif != 'Hepsi' else 'Tüm Kademeler'}</span>
                    <span class="badge badge-konu">📖 {secilen_konu if secilen_konu != 'Hepsi' else 'Genel Müfredat'}</span>
                    <span class="badge {badge_class}">{data.get('kategori','').upper()}</span>
                    <span class="badge badge-origin">🏢 {data.get('kaynak','')}</span>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            colb1, colb2 = st.columns([4,1])
            with colb1:
                st.link_button(f"🎯 {data['isim']} Sayfasını Aç", target_link, use_container_width=True)
            with colb2:
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
    | Entegrasyon Modeli | Operasyonel Süreç | Veri Akış Metodu |
    | :--- | :--- | :--- |
    | **Çok Dilli Veri Optimizasyonu** | Küresel altyapıya sahip harici platformlarda kavramsal eşleşme sağlar. | Otomatik Kavramsal Çeviri Katmanı |
    | **Dinamik URL Yapılandırması** | İç arama yapısı kapalı devre olan sistemlerde doğrudan ilgili hedef dizine odaklanır. | Eş Zamanlı Google İndeks Yönlendirmesi |
    | **Anlık Entegrasyon** | Açık veritabanı sunan platformlarda doğrudan eş zamanlı filtreleme gerçekleştirir. | Native Query Parametre Enjeksiyonu |
    """)

# --- SIDEBAR ALT NOT ---
st.sidebar.markdown("---")
st.sidebar.markdown("<h4 style='color: #0f172a; font-weight:600;'>📌 Operasyonel Bilgi</h4>", unsafe_allow_html=True)
st.sidebar.caption("Sistem üzerindeki tüm yönlendirmeler, kurumsal veri optimizasyonu protokollerine uygun olarak dinamik biçimde güncellenmektedir.")

# --- FOOTER ---
st.markdown("---")
st.markdown("<p style='text-align: center; color: #94a3b8; font-size: 13px; letter-spacing: 0.5px;'>Ortak Payda Matematik Öğretmenleri Kurumsal Dijital Ekosistemi. İSMAİL ORHAN © 2026</p>", unsafe_allow_html=True)
