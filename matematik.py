import streamlit as st
import urllib.parse

# --- SAYFA AYARLARI ---
st.set_page_config(
    page_title="Ortaokul Matematik Dijital Oyun & Materyal Havuzu",
    page_icon="📐",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- PREMIUM KULLANICI ARAYÜZÜ CSS TASARIMI ---
st.markdown("""
<style>
    .main { background-color: #f8fafc; }
    
    /* Sekme Geliştirmeleri */
    .stTabs [data-baseweb="tab-list"] { gap: 20px; border-bottom: 2px solid #e2e8f0; }
    .stTabs [data-baseweb="tab"] {
        background-color: transparent; border: none; padding: 14px 28px;
        font-weight: 700; color: #64748b; font-size: 15px; transition: all 0.2s ease;
    }
    .stTabs [aria-selected="true"] { color: #0f172a !important; border-bottom: 3px solid #10b981 !important; }
    
    /* Gelişmiş Kart Mimarisi */
    .card {
        background-color: #ffffff; padding: 26px; border-radius: 18px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -1px rgba(0, 0, 0, 0.03);
        margin-bottom: 16px; border: 1px solid #e2e8f0; border-top: 5px solid #10b981;
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }
    .card:hover {
        transform: translateY(-3px);
        box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04);
    }
    .card-title { color: #1e293b; font-size: 22px; font-weight: 800; margin-bottom: 6px; }
    .card-desc { color: #475569; font-size: 14.5px; line-height: 1.6; margin-bottom: 18px; }
    
    /* Rozetler (Badges) */
    .tag-sinif { display: inline-block; background-color: #f0fdf4; color: #166534; padding: 5px 12px; border-radius: 8px; font-size: 12.5px; margin-right: 6px; font-weight: 700; }
    .tag-konu { display: inline-block; background-color: #f0f9ff; color: #0369a1; padding: 5px 12px; border-radius: 8px; font-size: 12.5px; margin-right: 6px; font-weight: 700; }
    .tag-kategori { display: inline-block; background-color: #faf5ff; color: #6b21a8; padding: 5px 12px; border-radius: 8px; font-size: 12.5px; margin-right: 6px; font-weight: 700; }
    .tag-kaynak { display: inline-block; background-color: #fff7ed; color: #c2410c; padding: 5px 12px; border-radius: 8px; font-size: 12.5px; margin-right: 6px; font-weight: 700; }
    
    .status-badge { color: #10b981; font-weight: 800; font-size: 13px; float: right; background-color: #ecfdf5; padding: 4px 10px; border-radius: 20px; }
    
    /* İstatistik Paneli */
    .metric-container {
        background: #ffffff; padding: 16px; border-radius: 14px; text-align: center;
        box-shadow: 0 1px 3px rgba(0,0,0,0.05); border: 1px solid #e2e8f0;
    }
</style>
""", unsafe_allow_html=True)

# --- SESSION STATE (FAVORİ YÖNETİMİ) ---
if "favoriler" not in st.session_state:
    st.session_state.favoriler = []

# --- BAŞLIK ALANI ---
st.markdown("<h1 style='color: #1e293b; font-weight: 900; font-size: 36px; margin-bottom:0px;'>📐 Ortaokul Matematik Dijital Materyal & Kazanım Havuzu</h1>", unsafe_allow_html=True)
st.markdown("<p style='color: #64748b; font-size: 16px; margin-top:5px;'>MEB Müfredat uyumlu ulusal ve uluslararası tüm dijital eğitim platformlarının nokta atışı canlı arama motoru.</p>", unsafe_allow_html=True)
st.markdown("---")

# --- YAN MENÜ (DİNAMİK MÜFREDAT MOTORU) ---
st.sidebar.markdown("<h2 style='color: #1e293b; font-size: 22px; font-weight: 800; margin-bottom: 10px;'>🎯 Müfredat ve Kademe</h2>", unsafe_allow_html=True)

sinif_secenekleri = ["Hepsi", "5. Sınıf", "6. Sınıf", "7. Sınıf", "8. Sınıf"]
secilen_sinif = st.sidebar.selectbox("Sınıf Seviyesi:", sinif_secenekleri)

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

secilen_konu = st.sidebar.selectbox("Müfredat Konu Alanı:", konu_secenekleri)

# Manuel Kod veya Özel Kazanım Girişi
ozel_kazanim_sorgu = st.sidebar.text_input("📝 Özel Kazanım Kodu veya Terim:", placeholder="Örn: M.8.1.1.1 veya EBOB...").strip()

# --- GELİŞMİŞ FİLTRE PANELİ ---
st.sidebar.markdown("---")
st.sidebar.subheader("🚀 Profesyonel Katmanlar")
kategori_sec = st.sidebar.multiselect("Materyal Tipi Süzgeci:", ["Oyun", "Simülasyon", "Video", "Manipülatif", "Etkinlik", "Kazanım Testi", "Çalışma Yaprağı"])
lgs_modu = st.sidebar.toggle("🎯 Sadece LGS / Sınav Odaklı Platformlar")

# --- ANA SAYFA SEARCH BAR ---
arama_sorgusu = st.text_input("🔍 Canlı Küresel Kelime Arama (Havuz İçi Detaylı Filtreleme):", placeholder="Örn: phet, eba, yaprak test, veri analizi, simülasyon...").strip().lower()

# --- MATEMATİKSEL MASTER VERİTABANI (EKSİKSİZ TÜM SİTELER) ---
siteler_havuzu = [
    {
        "isim": "EBA (Eğitim Bilişim Ağı)",
        "aciklama": "MEB'in resmi eğitim portalı. Sınıf seviyenize ait resmi video dersler, etkileşimli tahta içerikleri ve bakanlık testleri.",
        "strategy": "native",
        "search_url": "https://www.eba.gov.tr/arama?q={query}",
        "default_url": "https://www.eba.gov.tr",
        "kategoriler": ["Video", "Etkinlik", "Kazanım Testi"],
        "kaynak": "Yerel / MEB",
        "lgs_uyumlu": True
    },
    {
        "isim": "Matematikçiler.com",
        "aciklama": "Ortaokul matematik öğretmenlerinin ana üssü. Kazanım odaklı dijital yaprak testler, online oyunlar ve PDF dökümanları.",
        "strategy": "native",
        "search_url": "https://www.matematikciler.com/?s={query}",
        "default_url": "https://www.matematikciler.com/ortaokul-matematik/",
        "kategoriler": ["Kazanım Testi", "Çalışma Yaprağı", "Oyun"],
        "kaynak": "Yerel / Özel",
        "lgs_uyumlu": True
    },
    {
        "isim": "Wordwall Matematik",
        "aciklama": "Öğretmen toplulukları tarafından MEB kazanımlarına tam uyumlu hazırlanan binlerce çarkıfelek, labirent, test ve yarışma oyunu.",
        "strategy": "native",
        "search_url": "https://wordwall.net/tr/community?localeId=1055&query={query}",
        "default_url": "https://wordwall.net/tr/community?localeId=1055&query=matematik",
        "kategoriler": ["Oyun", "Etkinlik"],
        "kaynak": "Küresel / Açık",
        "lgs_uyumlu": True
    },
    {
        "isim": "GeoGebra Matematik",
        "aciklama": "Geometri, koordinat sistemi, grafikler, açılar ve denklemler için dinamik, hareketli, görsel öğretmen simülasyon araçları.",
        "strategy": "native",
        "search_url": "https://www.geogebra.org/search/{query}",
        "default_url": "https://www.geogebra.org/materials",
        "kategoriler": ["Simülasyon", "Manipülatif"],
        "kaynak": "Küresel / Akademik",
        "lgs_uyumlu": True
    },
    {
        "isim": "Mathigon & Polypad",
        "aciklama": "Matematiğin sanal dijital laboratuvarı. Sanal cebir karoları, kesir blokları, geometri tahtası ve olasılık araçları.",
        "strategy": "concept", 
        "default_url": "https://mathigon.org/polypad",
        "kategoriler": ["Manipülatif", "Simülasyon"],
        "kaynak": "Küresel / Akademik",
        "lgs_uyumlu": True
    },
    {
        "isim": "PhET İnteraktif Simülasyonlar",
        "aciklama": "Colorado Üniversitesi tarafından geliştirilen kesir modelleri, negatif sayılar ve denklem terazisi barındıran dijital laboratuvarlar.",
        "strategy": "native",
        "search_url": "https://phet.colorado.edu/tr/simulations/filter?subjects=math&type=html&searchTerm={query}",
        "default_url": "https://phet.colorado.edu/tr/simulations/filter?subjects=math&type=html",
        "kategoriler": ["Simülasyon"],
        "kaynak": "Küresel / Akademik",
        "lgs_uyumlu": False
    },
    {
        "isim": "Matific Türkiye",
        "aciklama": "Müfredat odaklı, animasyonlu, hikayeleştirilmiş senaryolara sahip ödüllü akıllı matematik oyun ve görev platformu.",
        "strategy": "google_fallback",
        "target_domain": "matific.com/tr/tr",
        "default_url": "https://www.matific.com/tr/tr/home/maths-zone/",
        "kategoriler": ["Oyun"],
        "kaynak": "Küresel / Premium",
        "lgs_uyumlu": False
    },
    {
        "isim": "Toy Theater",
        "aciklama": "Özellikle soyut kavramları somutlaştırmak için onluk taban blokları, kesir daireleri ve interaktif geometri matrisleri.",
        "strategy": "native",
        "search_url": "https://toytheater.com/?s={query}",
        "default_url": "https://toytheater.com/category/math/",
        "kategoriler": ["Manipülatif", "Oyun"],
        "kaynak": "Küresel / Açık",
        "lgs_uyumlu": False
    },
    {
        "isim": "Eğitimhane",
        "aciklama": "Türkiye'nin en büyük öğretmen paylaşım ağı. Matematik zümreleri tarafından yüklenen özgün tarama testleri, yazılı hazırlık kağıtları.",
        "strategy": "native",
        "search_url": "https://www.egitimhane.com/ara.php?q={query}",
        "default_url": "https://www.egitimhane.com",
        "kategoriler": ["Çalışma Yaprağı", "Kazanım Testi"],
        "kaynak": "Yerel / Topluluk",
        "lgs_uyumlu": True
    },
    {
        "isim": "Khan Academy Türkçe",
        "aciklama": "Dünya standartlarında ücretsiz öğrenim paneli. Mikro video ders anlatımları ve adımsal ipuçları içeren yeni nesil kazanım testleri.",
        "strategy": "native",
        "search_url": "https://tr.khanacademy.org/search?page_search_query={query}",
        "default_url": "https://tr.khanacademy.org/math/",
        "kategoriler": ["Video", "Etkinlik", "Kazanım Testi"],
        "kaynak": "Küresel / Vakıf",
        "lgs_uyumlu": True
    },
    {
        "isim": "MEB ÖDS (Öğrenme Değerlendirme Sistemi)",
        "aciklama": "Bakanlığın en güncel soru havuzu. Ölçme, Değerlendirme ve Sınav Hizmetleri Genel Müdürlüğü kaynaklı LGS hazırlık ve kazanım modülleri.",
        "strategy": "google_fallback",
        "target_domain": "ods.eba.gov.tr",
        "default_url": "https://ods.eba.gov.tr",
        "kategoriler": ["Kazanım Testi"],
        "kaynak": "Yerel / MEB",
        "lgs_uyumlu": True
    }
]

# --- AKILLI SORGUBULDER VE TEMİZLİK MOTORU ---
terim_parcalari = []
if secilen_sinif != "Hepsi": 
    terim_parcalari.append(secilen_sinif)
if secilen_konu != "Hepsi": 
    terim_parcalari.append(secilen_konu)
if ozel_kazanim_sorgu: 
    terim_parcalari.append(ozel_kazanim_sorgu)

# Ham arama sorgusu ("Hepsi" kelimelerinden arındırılmış saf kazanım kelimeleri)
saf_arama_sorgusu = " ".join(terim_parcalari).strip()

filtrelenmis_siteler = []

for site in siteler_havuzu:
    # Profesyonel Filtrelerin Kontrolleri
    if lgs_modu and not site["lgs_uyumlu"]: continue
    if kategori_sec and not any(k in site["kategoriler"] for k in kategori_sec): continue
    if arama_sorgusu and (arama_sorgusu not in site["isim"].lower() and arama_sorgusu not in site["aciklama"].lower()): continue
    
    # URL İnşa Algoritması
    if saf_arama_sorgusu:
        # Web formatına kusursuz dönüştürme (URL encoding)
        encoded_query = urllib.parse.quote(saf_arama_sorgusu)
        
        if site["strategy"] == "native":
            dinamik_url = site["search_url"].format(query=encoded_query)
            
        elif site["strategy"] == "google_fallback":
            # 404 Almayı engelleyen, site içi Google indeks tarayıcı mantığı
            g_query = urllib.parse.quote(f"site:{site['target_domain']} {saf_arama_sorgusu}")
            dinamik_url = f"https://www.google.com/search?q={g_query}"
            
        elif site["strategy"] == "concept":
            # Sabit yapılı kavramsal panellerin haritalandırılması
            if secilen_konu in ["Cebirsel İfadeler", "Eşitlik ve Denklem", "Doğrusal Denklemler", "Eşitsizlikler"]:
                dinamik_url = "https://mathigon.org/polypad#algebra"
            elif any(g in secilen_konu for g in ["Geometri", "Açılar", "Çokgenler", "Üçgenler", "Çember", "Dönüşüm"]):
                dinamik_url = "https://mathigon.org/polypad#geometry"
            elif secilen_konu in ["Olasılık", "Veri Toplama ve Analizi"]:
                dinamik_url = "https://mathigon.org/polypad#probability"
            else:
                dinamik_url = "https://mathigon.org/polypad#numbers"
    else:
        dinamik_url = site["default_url"]
        
    filtrelenmis_siteler.append({"veri": site, "url": dinamik_url})

# --- ARAYÜZ GÖRÜNÜMÜ VE SEKMELER ---
tab1, tab2 = st.tabs(["🎯 Canlı Materyal & Görev Havuzu", "📊 MEB Müfredat Sınıf Strateji Matrisi"])

with tab1:
    # Üst Bilgilendirme Göstergeleri
    c_m1, c_m2, c_m3 = st.columns(3)
    with c_m1:
        st.markdown(f'<div class="metric-container"><p style="margin:0;color:#64748b;font-weight:600;">Aktif Sınıf/Kazanım Filtresi</p><h3 style="margin:0;color:#0f172a;font-weight:800;font-size:20px;">{saf_arama_sorgusu if saf_arama_sorgusu else "Tüm MüfredatAçık"}</h3></div>', unsafe_allow_html=True)
    with c_m2:
        st.markdown(f'<div class="metric-container"><p style="margin:0;color:#64748b;font-weight:600;">Erişilebilir Dijital Platform</p><h3 style="margin:0;color:#10b981;font-weight:800;font-size:20px;">{len(filtrelenmis_siteler)} Aktif Kanal</h3></div>', unsafe_allow_html=True)
    with c_m3:
        st.markdown(f'<div class="metric-container"><p style="margin:0;color:#64748b;font-weight:600;">Favoriye Alınanlar</p><h3 style="margin:0;color:#6b21a8;font-weight:800;font-size:20px;">{len(st.session_state.favoriler)} Platform</h3></div>', unsafe_allow_html=True)
        
    st.write("")
    
    if not filtrelenmis_siteler:
        st.error("⚠️ Seçtiğiniz gelişmiş filtre kriterlerine uygun bir platform eşleşmesi bulunamadı. Lütfen süzgeçleri esnetiniz.")
    else:
        col1, col2 = st.columns(2)
        for idx, item in enumerate(filtrelenmis_siteler):
            site_veri = item["veri"]
            hedef_link = item["url"]
            target_col = col1 if idx % 2 == 0 else col2
            
            with target_col:
                kategoriler_html = " ".join([f'<span class="tag-kategori">⚡ {k}</span>' for k in site_veri["kategoriler"]])
                
                # Yönlendirme metoduna dair teknik bilgilendirme rozeti
                method_badge = "● Google Güvenli Dizin" if site_veri["strategy"] == "google_fallback" else "● %100 Doğrudan Entegre"
                
                st.markdown(f"""
                <div class="card">
                    <span class="status-badge">{method_badge}</span>
                    <div class="card-title">{site_veri['isim']}</div>
                    <div class="card-desc">{site_veri['aciklama']}</div>
                    <div style="margin-bottom: 15px;">
                        <span class="tag-sinif">📍 {secilen_sinif if secilen_sinif != 'Hepsi' else 'Tüm Ortaokul'}</span>
                        <span class="tag-konu">📖 {secilen_konu if secilen_konu != 'Hepsi' else 'Tüm Müfredat'}</span>
                        <span class="tag-kaynak">🌐 {site_veri['kaynak']}</span>
                        {kategoriler_html}
                    </div>
                </div>
                """, unsafe_allow_html=True)
                
                btn_c1, btn_c2 = st.columns([3, 1])
                with btn_c1:
                    if site_veri["strategy"] == "google_fallback" and saf_arama_sorgusu:
                        buton_metni = f"🔍 {site_veri['isim']} İçeriklerini Güvenli Listele"
                    elif saf_arama_sorgusu:
                        buton_metni = f"🚀 Doğrudan {site_veri['isim']} Kazanım Sayfasına Git"
                    else:
                        buton_metni = f"🔗 {site_veri['isim']} Ana Giriş Paneline Git"
                        
                    st.link_button(buton_metni, hedef_link, use_container_width=True)
                with btn_c2:
                    if site_veri["isim"] in st.session_state.favoriler:
                        if st.button("⭐ Kaldır", key=f"fav_sys_{idx}", use_container_width=True):
                            st.session_state.favoriler.remove(site_veri["isim"])
                            st.rerun()
                    else:
                        if st.button("☆ Favori", key=f"fav_sys_{idx}", use_container_width=True):
                            st.session_state.favoriler.append(site_veri["isim"])
                            st.rerun()
                st.write("") 

with tab2:
    st.subheader("📊 MEB Müfredat Yapısı ve Dijital Entegrasyon Önerileri")
    st.markdown("""
    | Sınıf Seviyesi | Kritik/Zorlanılan Üniteler | Dijital Somutlaştırma İçin En Efektif Platform Eşleşmesi |
    | :--- | :--- | :--- |
    | **5. Sınıf** | Kesirler, Ondalık Gösterim, Yüzdeler | *Matific (Oyun tabanlı görev), Matematikçiler.com (Yaprak Testler)* |
    | **6. Sınıf** | Oran, Cebirsel İfadeler, Hacim Ölçme | *PhET (Oran Terazisi), Mathigon Polypad (Sanal Somut Bloklar)* |
    | **7. Sınıf** | Eşitlik ve Denklem, Tam Sayılarda İşlemler | *PhET (Denklem Terazisi), GeoGebra (Grafik ve Doğrusal Yapılar)* |
    | **8. Sınıf** | LGS Hazırlık, Kareköklü İfadeler, Çarpanlar ve Katlar | *MEB ÖDS (Soru Havuzu), Wordwall (Süre Sınırlı Hız Oyunları), Khan Academy* |
    """)

# --- YAN MENÜ FAVORİLER TABLOSU ---
st.sidebar.markdown("---")
st.sidebar.subheader("⭐ Sık Kullandığım Platformlar")
if st.session_state.favoriler:
    for fav in st.session_state.favoriler:
        st.sidebar.caption(f"✨ {fav}")
else:
    st.sidebar.info("Hızlı erişim için sık kullandığınız araçları kartların yanından favorileyebilirsiniz.")

# --- FOOTER ---
st.markdown("---")
st.markdown("<p style='text-align: center; color: #94a3b8; font-size: 13px;'>Ortak Payda Matematik Öğretmenleri için geliştirildi. İSMAİL ORHAN © 2026</p>", unsafe_allow_html=True)
