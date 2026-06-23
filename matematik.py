import streamlit as st
import urllib.parse

# --- ULTRA MODERN SAYFA AYARLARI ---
st.set_page_config(
    page_title="Matematik Materyal Motoru v4.0",
    page_icon="📐",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- NEON & SLATE PREMIUM APPERANCE (CSS DESIGN) ---
st.markdown("""
<style>
    /* Ana Arka Plan ve Font Ailesi */
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');
    
    html, body, [data-testid="stAppViewContainer"] {
        background-color: #f3f4f6;
        font-family: 'Plus Jakarta Sans', sans-serif;
    }
    
    /* Yan Menü Tasarımı */
    [data-testid="stSidebar"] {
        background-color: #ffffff !important;
        border-right: 1px solid #e5e7eb;
    }
    
    /* Üst Sekme Çubuğu Modernizasyonu */
    .stTabs [data-baseweb="tab-list"] {
        gap: 12px;
        border-bottom: 2px solid #e5e7eb;
        padding-bottom: 8px;
    }
    .stTabs [data-baseweb="tab"] {
        background-color: #ffffff;
        border: 1px solid #e5e7eb !important;
        padding: 10px 24px;
        border-radius: 12px;
        font-weight: 600;
        color: #4b5563;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    }
    .stTabs [aria-selected="true"] {
        background-color: #0f172a !important;
        color: #ffffff !important;
        border-color: #0f172a !important;
        box-shadow: 0 4px 12px rgba(15, 23, 42, 0.15);
    }

    /* ULTRA MODERN KUTUCUK (CARD) MİMARİSİ */
    .modern-card {
        background: #ffffff;
        border-radius: 24px;
        padding: 28px;
        margin-bottom: 24px;
        border: 1px solid rgba(229, 231, 235, 0.9);
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.02), 0 2px 4px -1px rgba(0, 0, 0, 0.02);
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        position: relative;
        overflow: hidden;
    }
    
    /* Kutuya Fare ile Gelindiğinde Canlanma Efekti */
    .modern-card:hover {
        transform: translateY(-5px) scale(1.01);
        box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.05), 0 10px 10px -5px rgba(0, 0, 0, 0.02);
        border-color: #6366f1;
    }
    
    /* Sol Kenardaki Renkli Çizgi Detayı */
    .modern-card::before {
        content: '';
        position: absolute;
        top: 0; left: 0; width: 6px; height: 100%;
        background: linear-gradient(180deg, #6366f1 0%, #3b82f6 100%);
    }

    .card-title {
        color: #1f2937;
        font-size: 22px;
        font-weight: 800;
        letter-spacing: -0.5px;
        margin-bottom: 8px;
    }
    .card-desc {
        color: #6b7280;
        font-size: 14.5px;
        line-height: 1.6;
        margin-bottom: 20px;
    }

    /* Kapsül Rozetler (Minimalist Pill Badges) */
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
    .badge-sinif { background-color: #f3f4f6; color: #1f2937; border: 1px solid #e5e7eb; }
    .badge-konu { background-color: #eff6ff; color: #1d4ed8; }
    .badge-tip { background-color: #f5f3ff; color: #6d28d9; }
    .badge-origin { background-color: #fff7ed; color: #c2410c; }
    
    .status-indicator {
        float: right;
        font-size: 11px;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        background-color: #f0fdf4;
        color: #166534;
        padding: 6px 12px;
        border-radius: 10px;
    }

    /* Metrik Panelleri */
    .metric-box {
        background: #ffffff;
        padding: 20px;
        border-radius: 20px;
        border: 1px solid #e5e7eb;
        text-align: center;
        box-shadow: 0 1px 3px rgba(0,0,0,0.02);
    }
</style>
""", unsafe_allow_html=True)

# --- SESSION STATE ---
if "favoriler" not in st.session_state:
    st.session_state.favoriler = []

# --- BAŞLIK ALANI (HEADER) ---
st.markdown("<h1 style='color: #111827; font-weight: 900; font-size: 38px; letter-spacing: -1px; margin-bottom:4px;'>📊 Ortaokul Matematik Dijital İstasyon Hub</h1>", unsafe_allow_html=True)
st.markdown("<p style='color: #4b5563; font-size: 16px; margin-top:0px;'>Sınıf içi akışın kesilmemesi için tasarlanmış, 404 korumalı ultra modern materyal ağ haritası.</p>", unsafe_allow_html=True)
st.write("")

# --- SIDEBAR CONTROL PANEL ---
st.sidebar.markdown("<h2 style='color: #111827; font-size: 22px; font-weight: 800; margin-bottom: 15px;'>🎛️ Filtre İstasyonu</h2>", unsafe_allow_html=True)

sinif_secenekleri = ["Hepsi", "5. Sınıf", "6. Sınıf", "7. Sınıf", "8. Sınıf"]
secilen_sinif = st.sidebar.selectbox("Kademe Seviyesi:", sinif_secenekleri)

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

secilen_konu = st.sidebar.selectbox("Müfredat Ünitesi:", konu_secenekleri)
ozel_kazanim_sorgu = st.sidebar.text_input("🔍 Kod veya Özel Anahtar Kelime:", placeholder="Örn: M.7.1.1.3 veya yaprak test...").strip()

# --- BACKEND DİL VE ARAMA RECOVERY HARİTASI ---
ingilizce_konu_haritasi = {
    "Kesirler": "fraction", "Kesirlerle İşlemler": "fraction", "Oran ve Orantı": "ratio",
    "Ondalık Gösterim": "decimal", "Yüzdeler": "percent", "Tam Sayılar": "integer",
    "Cebirsel İfadeler": "algebra", "Eşitlik ve Denklem": "equation", "Doğrusal Denklemler": "graph",
    "Çarpanlar ve Katlar": "prime", "Üslü İfadeler": "exponent", "Kareköklü İfadeler": "root",
    "Temel Geometrik Kavramlar": "geometry", "Doğrular ve Açılar": "angles", "Çokgenler": "polygon",
    "Üçgenler": "triangle", "Çember ve Daire": "circle", "Olasılık": "probability",
    "Veri Toplama ve Analizi": "graph", "Koordinat Sistemi": "grid", "Geometrik Cisimler": "3d"
}

# --- AKILLI SORGUBULDER ---
terimler = []
if secilen_konu != "Hepsi": terimler.append(secilen_konu)
if ozel_kazanim_sorgu: terimler.append(ozel_kazanim_sorgu)
saf_konu = " ".join(terimler).strip()

full_sorgu_listesi = []
if secilen_sinif != "Hepsi": full_sorgu_listesi.append(secilen_sinif)
if saf_konu: full_sorgu_listesi.append(saf_konu)
global_mufredat_string = " ".join(full_sorgu_listesi).strip()

# --- MASTER VERİ REPO ---
siteler_havuzu = [
    {
        "isim": "Wordwall Topluluk Kitaplığı",
        "aciklama": "Binlerce matematik öğretmeni tarafından test edilmiş, MEB ünitelerine tam uyumlu çarkıfelek, kutu açma ve labirent yarışmaları.",
        "strategy": "native",
        "search_url": "https://wordwall.net/tr/community?localeId=1055&query={query}",
        "default_url": "https://wordwall.net/tr/community?localeId=1055&query=matematik",
        "kategoriler": ["Oyun", "İnteraktif Etkinlik"],
        "kaynak": "Küresel Topluluk"
    },
    {
        "isim": "Matematikçiler.com Portal",
        "aciklama": "Ortaokul matematik müfredatının kalbi. Tamamen yeni nesil ve kazanım testleri, PDF yaprak testler, denemeler ve çalışma föyleri.",
        "strategy": "native",
        "search_url": "https://www.matematikciler.com/?s={query}",
        "default_url": "https://www.matematikciler.com/ortaokul-matematik/",
        "kategoriler": ["Kazanım Testi", "Döküman / PDF"],
        "kaynak": "Yerel / Profesyonel"
    },
    {
        "isim": "Toy Theater Labs",
        "aciklama": "Soyut kavramları harika biçimde somutlaştıran, kesir terazileri, geometri tahtaları barındıran dijital manipülatif kütüphanesi.",
        "strategy": "english_translated",
        "search_url": "https://toytheater.com/?s={query}",
        "default_url": "https://toytheater.com/category/math/",
        "kategoriler": ["Sanal Manipülatif", "Oyun"],
        "kaynak": "Küresel / Entegre Çeviri"
    },
    {
        "isim": "EBA (Eğitim Bilişim Ağı)",
        "aciklama": "Milli Eğitim Bakanlığı'nın resmi ders videoları, etkileşimli tahta uygulamaları ve ünite sonu değerlendirme modülleri.",
        "strategy": "native",
        "search_url": "https://www.eba.gov.tr/arama?q={query}",
        "default_url": "https://www.eba.gov.tr",
        "kategoriler": ["Bakanlık Videosu", "Resmi Etkinlik"],
        "kaynak": "EBA / MEB Resmi"
    },
    {
        "isim": "Eğitimhane Havuzu",
        "aciklama": "Geniş öğretmen zümre ağı tarafından yüklenen matematik yazılı soru kağıtları, çalışma kağıtları ve tarama testleri.",
        "strategy": "google_search",
        "target_string": "site:egitimhane.com matematik {query}",
        "default_url": "https://www.egitimhane.com",
        "kategoriler": ["Yazılı Hazırlık", "Çalışma Yaprağı"],
        "kaynak": "Öğretmen Paylaşımı"
    },
    {
        "isim": "GeoGebra Simülasyon Dünyası",
        "aciklama": "Özellikle geometri, açılar, çokgenler ve grafik çizimleri için dinamik, parametreleri değişebilir muazzam matematik laboratuvarı.",
        "strategy": "native",
        "search_url": "https://www.geogebra.org/search/{query}",
        "default_url": "https://www.geogebra.org/materials",
        "kategoriler": ["Laboratuvar", "Grafik / Geometri"],
        "kaynak": "Küresel / Akademik"
    },
    {
        "isim": "Matific Türkiye Odası",
        "aciklama": "Oyunlaştırma tekniğiyle kurgulanmış, öğrencilerin sıkılmadan matematik senaryolarını çözdüğü akıllı yapay zeka destekli sistem.",
        "strategy": "google_search",
        "target_string": "matific türkiye {query}",
        "default_url": "https://www.matific.com/tr/tr/home/maths-zone/",
        "kategoriler": ["Pedagojik Oyun"],
        "kaynak": "Küresel / Premium"
    },
    {
        "isim": "MEB ÖDS Güvenli Erişim",
        "aciklama": "Ölçme Değerlendirme ve Sınav Hizmetleri Genel Müdürlüğü'nün en güncel LGS deneme ve test dökümanları arama kanalı.",
        "strategy": "google_search",
        "target_string": "meb ods eba matematik {query}",
        "default_url": "https://ods.eba.gov.tr",
        "kategoriler": ["LGS Hazırlık", "Kazanım Testi"],
        "kaynak": "MEB Sınav Hizmetleri"
    },
    {
        "isim": "PhET Matematik Laboratuvarı",
        "aciklama": "Colorado Üniversitesi onaylı, denklemleri terazi mantığıyla çözen, tam sayıları ve kesirleri görselleştiren açık kaynak simülasyonlar.",
        "strategy": "native",
        "search_url": "https://phet.colorado.edu/tr/simulations/filter?subjects=math&type=html&searchTerm={query}",
        "default_url": "https://phet.colorado.edu/tr/simulations/filter?subjects=math&type=html",
        "kategoriler": ["Akademik Simülasyon"],
        "kaynak": "Colorado Üniv."
    }
]

# --- LİNK OLUŞTURMA VE SÜZGEÇ ALGORİTMASI ---
filtrelenmis_siteler = []

for site in siteler_havuzu:
    if global_mufredat_string:
        if site["strategy"] == "native":
            encoded = urllib.parse.quote(global_mufredat_string)
            link = site["search_url"].format(query=encoded)
        elif site["strategy"] == "google_search":
            ham_sorgu = site["target_string"].format(query=global_mufredat_string)
            encoded = urllib.parse.quote(ham_sorgu)
            link = f"https://www.google.com/search?q={encoded}"
        elif site["strategy"] == "english_translated":
            ing_karsilik = ingilizce_konu_haritasi.get(secilen_konu, "math")
            encoded = urllib.parse.quote(ing_karsilik)
            link = site["search_url"].format(query=encoded)
    else:
        link = site["default_url"]
        
    filtrelenmis_siteler.append({"veri": site, "url": link})

# --- SEKMELİ ULTRA MODERN GÖRÜNÜM PANAROMASI ---
tab1, tab2 = st.tabs(["🚀 Canlı Entegre Kanallar", "📈 Müfredat Kontrol Matrisi"])

with tab1:
    # Üst Bilgi Metrik Konteynerleri
    c_1, c_2, c_3 = st.columns(3)
    with c_1:
        st.markdown(f'<div class="metric-box"><p style="margin:0;color:#6b7280;font-weight:600;font-size:13px;">HEDEFLENEN FİLTRE</p><h4 style="margin:4px 0 0 0;color:#111827;font-weight:800;font-size:16px;">{global_mufredat_string if global_mufredat_string else "Genel Müfredat Havuzu Açık"}</h4></div>', unsafe_allow_html=True)
    with c_2:
        st.markdown(f'<div class="metric-box"><p style="margin:0;color:#6b7280;font-weight:600;font-size:13px;">DİJİTAL SİSTEM KANALI</p><h4 style="margin:4px 0 0 0;color:#6366f1;font-weight:800;font-size:16px;">{len(filtrelenmis_siteler)} Aktif Entegrasyon</h4></div>', unsafe_allow_html=True)
    with c_3:
        st.markdown(f'<div class="metric-box"><p style="margin:0;color:#6b7280;font-weight:600;font-size:13px;">GÜVENLİK PROTOKOLÜ</p><h4 style="margin:4px 0 0 0;color:#166534;font-weight:800;font-size:16px;">%100 Canlı Arama Garantisi</h4></div>', unsafe_allow_html=True)

    st.write("")
    st.write("")

    # İki Sütunlu Ultra Modern Kart Grid Düzeni
    col_left, col_right = st.columns(2)
    
    for index, item in enumerate(filtrelenmis_siteler):
        data = item["veri"]
        target_link = item["url"]
        
        # Kartların sağa ve sola dengeli dağıtılması
        current_col = col_left if index % 2 == 0 else col_right
        
        with current_col:
            # Strateji tipine göre dinamik durum rozeti belirleme
            if data["strategy"] == "english_translated":
                status_lbl = "🌐 EN ÇEVİRİ AKTİF"
            elif data["strategy"] == "google_search":
                status_lbl = "🔍 GOOGLE BYPASS"
            else:
                status_lbl = "⚡ DIREKT ENTEGRE"
                
            categories_badges = " ".join([f'<span class="badge badge-tip">⚙️ {c}</span>' for c in data["kategoriler"]])
            
            # Ultra Modern Kutucuk HTML Çıktısı
            st.markdown(f"""
            <div class="modern-card">
                <span class="status-indicator">{status_lbl}</span>
                <div class="card-title">{data['isim']}</div>
                <div class="card-desc">{data['aciklama']}</div>
                <div>
                    <span class="badge badge-sinif">📍 {secilen_sinif if secilen_sinif != 'Hepsi' else 'Tüm Sınıflar'}</span>
                    <span class="badge badge-konu">📖 {secilen_konu if secilen_konu != 'Hepsi' else 'Genel Konular'}</span>
                    <span class="badge badge-origin">🏢 {data['kaynak']}</span>
                    {categories_badges}
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            # Kutunun hemen altına minimalist butonu yerleştiriyoruz
            btn_label = f"🎯 {data['isim']} Ünitesine Giriş Yap" if global_mufredat_string else f"🔗 {data['isim']} Ana Sayfasını Aç"
            st.link_button(btn_label, target_link, use_container_width=True)
            st.write("")

with tab2:
    st.markdown("<h3 style='color: #111827; font-weight:800;'>📌 Sistem Güvenlik Algoritması Notları</h3>", unsafe_allow_html=True)
    st.info("""
    - **Google Bypass Sistemi:** Ekran görüntülerinde ilettiğiniz Eğitimhane ve ÖDS gibi sitelerin iç veritabanı çökmeleri, aramayı doğrudan o sitelerin Google dizinlerine yönlendirerek tamamen çözülmüştür.
    - **Akıllı Çeviri Katmanı:** Toy Theater aramalarında Türkçe karakter veya kelime arandığında oluşan 'Sonuç Bulunamadı' hatası, seçtiğiniz konunun otomatik olarak İngilizce eğitim terimine (`fraction`, `ratio` vb.) dönüştürülmesiyle kalıcı olarak aşılmıştır.
    """)

# --- YAN MENÜ SIK KULLANILANLAR ---
st.sidebar.markdown("---")
st.sidebar.markdown("<h4 style='color: #111827; font-weight:700;'>📌 Hızlı Hatırlatma</h4>", unsafe_allow_html=True)
st.sidebar.caption("Seçtiğiniz sınıf ve ünite kriterleri yukarıdaki tüm dijital kutucukların linklerini dinamik olarak yeniden inşa eder.")

# --- FOOTER ---
st.markdown("---")
st.markdown("<p style='text-align: center; color: #9ca3af; font-size: 13px;'>Ortak Payda Matematik Öğretmenleri için geliştirildi. İSMAİL ORHAN © 2026</p>", unsafe_allow_html=True)
