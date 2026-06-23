import streamlit as st
import urllib.parse

# --- ULTRA MODERN PREMIUM SAYFA AYARLARI ---
st.set_page_config(
    page_title="Matematik Materyal Motoru Pro v5.1",
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
    
    /* Kart Üzerine Gelindiğinde Neon Işıltı ve Yükselme Efekti */
    .premium-card:hover {
        transform: translateY(-6px);
        box-shadow: 0 20px 40px -15px rgba(79, 70, 229, 0.15);
        border-color: #4f46e5;
    }
    
    /* Sol Dikey Akıllı Gradyan Şeridi */
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
    .badge-sinif { background-color: #f1f5f9; color: #334155; border: 1px solid #e2e8f0; }
    .badge-konu { background-color: #e0f2fe; color: #0369a1; }
    .badge-tip { background-color: #f5f3ff; color: #6d28d9; }
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

    /* Üst Gelişmiş Metrik Panelleri */
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

# --- BAŞLIK ALANI (HEADER) ---
st.markdown("<h1 style='color: #0f172a; font-weight: 800; font-size: 40px; letter-spacing: -1px; margin-bottom:4px;'>📐 Ortaokul Matematik Dijital Entegrasyon Paneli</h1>", unsafe_allow_html=True)
st.markdown("<p style='color: #475569; font-size: 16px; margin-top:0px;'>Müfredat kazanımları ile tam senkronize çalışan, çok dilli arama optimizasyonlu kurumsal yönetim platformu.</p>", unsafe_allow_html=True)
st.write("")

# --- SIDEBAR CONTROL PANEL ---
st.sidebar.markdown("<h2 style='color: #0f172a; font-size: 22px; font-weight: 700; margin-bottom: 15px;'>🎛️ Parametre İstasyonu</h2>", unsafe_allow_html=True)

sinif_secenekleri = ["Hepsi", "5. Sınıf", "6. Sınıf", "7. Sınıf", "8. Sınıf"]
secilen_sinif = st.sidebar.selectbox("Eğitim Kademesi:", sinif_secenekleri)

tum_meb_konulari = [
    "Hepsi", "Doğal Sayılar", "Doğal Sayılarla İşlemler", "Çarpanlar ve Katlar", "Kümeler", "Tam Sayılar",
    "Kesirler", "Kesirlerle İşlemler", "Ondalık Gösterim", "Rasyonel Sayılar", "Üslü İfadeler", "Kareköklü İfadeler",
    "Oran ve Orantı", "Yüzdeler", "Cebirsel İfadeler", "Eşitlik ve Denklem", "Doğrusal Denklemler", "Eşitsizlikler",
    "Temel Geometrik Kavramlar", "Doğrular ve Açılar", "Çokgenler", "Üçgenler", "Çember ve Daire", "Eşlik ve Benzerlik",
    "Dönüşüm Geometrisi", "Geometrik Cisimler", "Uzunluk ve Zaman Ölçme", "Alan Ölçme", "Sıvı Ölçme",
    "Veri Toplama ve Analizi", "Olasılık", "Koordinat Sistemi"
]

if secilen_sinif == "5. Sınıf":
    konu_secenekleri = ["Hepsi", "Doğal Sayılar", "Doğal Sayılarla İşlemler", "Kesirler", "Kesirlerle İşlemler", "Ondalık Göspanım", "Yüzdeler", "Temel Geometrik Kavramlar", "Üçgen ve Dörtgenler", "Veri Toplama ve Analizi", "Uzunluk ve Zaman Ölçme", "Alan Ölçme", "Geometrik Cisimler"]
elif secilen_sinif == "6. Sınıf":
    konu_secenekleri = ["Hepsi", "Doğal Sayılarla İşlemler", "Çarpanlar ve Katlar", "Kümeler", "Tam Sayılar", "Kesirlerle İşlemler", "Ondalık Gösterim", "Oran ve Orantı", "Cebirsel İfadeler", "Veri Toplama ve Analizi", "Doğrular ve Açılar", "Alan Ölçme", "Çember ve Daire", "Geometrik Cisimler", "Sıvı Ölçme"]
elif secilen_sinif == "7. Sınıf":
    konu_secenekleri = ["Hepsi", "Tam Sayılar", "Rasyonel Sayılar", "Cebirsel İfadeler", "Eşitlik ve Denklem", "Oran ve Orantı", "Yüzdeler", "Doğrular ve Açılar", "Çokgenler", "Çember ve Daire", "Veri Toplama ve Analizi", "Geometrik Cisimler"]
elif secilen_sinif == "8. Sınıf":
    konu_secenekleri = ["Hepsi", "Çarpanlar ve Katlar", "Üslü İfadeler", "Kareköklü İfadeler", "Veri Toplama ve Analizi", "Olasılık", "Cebirsel İfadeler", "Doğrusal Denklemler", "Eşitsizlikler", "Üçgenler", "Eşlik ve Benzerlik", "Dönüşüm Geometrisi", "Geometrik Cisimler", "Koordinat Sistemi"]
else:
    konu_secenekleri = tum_meb_konulari

secilen_konu = st.sidebar.selectbox("Müfredat Ünitesi:", konu_secenekleri)
ozel_kazanim_sorgu = st.sidebar.text_input("🔍 Odaklanılacak Kazanım Terimi:", placeholder="Örn: M.8.1.2.1 veya Özdeşlikler...").strip()

# --- KURUMSUR SÖZLÜK VE ÇOK DİLLİ UYUMLULUK KATMANI ---
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

# --- MASTER VERİ REPO (GENİŞLETİLMİŞ EKSİKSİZ HAVUZ) ---
siteler_havuzu = [
    {
        "isim": "Wordwall Topluluk Kitaplığı",
        "aciklama": "Geniş öğretmen ekosistemi tarafından yapılandırılmış, müfredat üniteleriyle uyumlu interaktif matematik oyunları ve yarışma modülleri.",
        "strategy": "native",
        "search_url": "https://wordwall.net/tr/community?localeId=1055&query={query}",
        "default_url": "https://wordwall.net/tr/community?localeId=1055&query=matematik",
        "kategoriler": ["Dijital Oyun", "İnteraktif Uygulama"],
        "kaynak": "Küresel Konsorsiyum"
    },
    {
        "isim": "Matematikçiler.com Portal",
        "aciklama": "Ortaokul düzeyine özgü optimize edilmiş yeni nesil tarama testleri, basılı döküman yaprakları ve konu analiz özetleri.",
        "strategy": "native",
        "search_url": "https://www.matematikciler.com/?s={query}",
        "default_url": "https://www.matematikciler.com/ortaokul-matematik/",
        "kategoriler": ["Kazanım Testi", "Döküman / PDF"],
        "kaynak": "Yerel Akademik Portal"
    },
    {
        "isim": "Derslig Matematik Odası",
        "aciklama": "Ortaokul seviyesinde interaktif ünite görevleri, animasyonlu konu anlatımları ve dijital ölçme araçları barındıran yeni nesil sistem.",
        "strategy": "google_search",
        "target_string": "site:derslig.com matematik {query}",
        "default_url": "https://www.derslig.com",
        "kategoriler": ["İnteraktif Görev", "Ölçme / Değerlendirme"],
        "kaynak": "Yerel Dijital Platform"
    },
    {
        "isim": "Liveworksheets Matematik",
        "aciklama": "Dünya çapındaki eğitimciler tarafından dijitalleştirilmiş, öğrencilerin anlık dönüt alabildiği etkileşimli çalışma yaprakları.",
        "strategy": "native",
        "search_url": "https://www.liveworksheets.com/search?query=matematik+{query}",
        "default_url": "https://www.liveworksheets.com",
        "kategoriler": ["Etkileşimli Yaprak", "Çevrimiçi Görev"],
        "kaynak": "Küresel / Çok Dilli"
    },
    {
        "isim": "Toy Theater Labs",
        "aciklama": "Soyut matematik kuramlarının somut parametrelerle modellenmesini sağlayan sanal manipülatif ve görselleştirme kütüphanesi.",
        "strategy": "english_translated",
        "search_url": "https://toytheater.com/?s={query}",
        "default_url": "https://toytheater.com/category/math/",
        "kategoriler": ["Sanal Manipülatif", "Görsel Modelleme"],
        "kaynak": "Çok Dilli Entegrasyon"
    },
    {
        "isim": "EBA (Eğitim Bilişim Ağı)",
        "aciklama": "Milli Eğitim Bakanlığı'nın resmi uzaktan eğitim altyapısı, video ders anlatımları ve bakanlık onaylı akıllı tahta içerikleri.",
        "strategy": "native",
        "search_url": "https://www.eba.gov.tr/arama?q={query}",
        "default_url": "https://www.eba.gov.tr",
        "kategoriler": ["Resmi Video", "Bakanlık Modülü"],
        "kaynak": "MEB Devlet Arşivi"
    },
    {
        "isim": "Eğitimhane Veri Havuzu",
        "aciklama": "Matematik eğitim toplulukları tarafından paylaşılan dönemlik yazılı sınav örnekleri, tarama formları ve zümre dökümanları.",
        "strategy": "google_search",
        "target_string": "site:egitimhane.com matematik {query}",
        "default_url": "https://www.egitimhane.com",
        "kategoriler": ["Yazılı Örneği", "Çalışma Föyü"],
        "kaynak": "Öğretmen Paylaşım Ağı"
    },
    {
        "isim": "GeoGebra Simülasyon Dünyası",
        "aciklama": "Geometri, analitik düzlem, açılar ve fonksiyon grafiklerinin interaktif olarak incelenebildiği dinamik geometri motoru.",
        "strategy": "native",
        "search_url": "https://www.geogebra.org/search/{query}",
        "default_url": "https://www.geogebra.org/materials",
        "kategoriler": ["Dinamik Geometri", "Analitik Laboratuvar"],
        "kaynak": "Küresel Akademik Enstitü"
    },
    {
        "isim": "Matific Türkiye Odası",
        "aciklama": "Pedagojik esaslara dayalı olarak kurgulanmış oyunlaştırılmış matematik problemleri ve akıllı öğrenme adımları.",
        "strategy": "google_search",
        "target_string": "matific türkiye {query}",
        "default_url": "https://www.matific.com/tr/tr/home/maths-zone/",
        "kategoriler": ["Pedagojik Oyun", "Akıllı Senaryo"],
        "kaynak": "Uluslararası Premium"
    },
    {
        "isim": "MEB ÖDS Seçici Havuz",
        "aciklama": "Ölçme Değerlendirme ve Sınav Hizmetleri Genel Müdürlüğü tarafından yayımlanan LGS odaklı resmi deneme ve kazanım testleri.",
        "strategy": "google_search",
        "target_string": "meb ods eba matematik {query}",
        "default_url": "https://ods.eba.gov.tr",
        "kategoriler": ["LGS Seçki Testi", "Resmi Soru Havuzu"],
        "kaynak": "ÖDS Genel Müdürlüğü"
    },
    {
        "isim": "Sorubak Kaynak Havuzu",
        "aciklama": "Ortaokul müfredat dönemlerine tam uyumlu matematik merkezi sınav hazırlık dokümanları ve öğretmen yaprak test arşivi.",
        "strategy": "google_search",
        "target_string": "site:sorubak.com ortaokul matematik {query}",
        "default_url": "https://www.sorubak.com",
        "kategoriler": ["Tarama Testi", "Sınav Hazırlık"],
        "kaynak": "Eğitim Paylaşım Deposu"
    },
    {
        "isim": "PhET Matematik Laboratuvarı",
        "aciklama": "Üniversite düzeyinde geliştirilmiş, denklemleri ve rasyonel sayı sistemlerini interaktif simülasyonlarla sunan açık kaynaklı yapı.",
        "strategy": "native",
        "search_url": "https://phet.colorado.edu/tr/simulations/filter?subjects=math&type=html&searchTerm={query}",
        "default_url": "https://phet.colorado.edu/tr/simulations/filter?subjects=math&type=html",
        "kategoriler": ["Akademik Modelleme", "Açık Simülasyon"],
        "kaynak": "Colorado University"
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
tab1, tab2 = st.tabs(["🚀 Aktif Eğitim Kanalları Matrisi", "📊 Kurumsal Entegrasyon Şeması"])

with tab1:
    # Üst Bilgi Metrik Konteynerleri
    c_1, c_2, c_3 = st.columns(3)
    with c_1:
        st.markdown(f'<div class="metric-box"><p style="margin:0;color:#64748b;font-weight:600;font-size:13px;letter-spacing:0.5px;">HEDEFLENEN MÜFREDAT GRUBU</p><h4 style="margin:6px 0 0 0;color:#0f172a;font-weight:700;font-size:16px;">{global_mufredat_string if global_mufredat_string else "Tüm Akademik Havuz Aktif"}</h4></div>', unsafe_allow_html=True)
    with c_2:
        st.markdown(f'<div class="metric-box"><p style="margin:0;color:#64748b;font-weight:600;font-size:13px;letter-spacing:0.5px;">EŞ ZAMANLI ENTEGRE SİSTEM</p><h4 style="margin:6px 0 0 0;color:#4f46e5;font-weight:700;font-size:16px;">{len(filtrelenmis_siteler)} Aktif Veri Kanalı</h4></div>', unsafe_allow_html=True)
    with c_3:
        st.markdown(f'<div class="metric-box"><p style="margin:0;color:#64748b;font-weight:600;font-size:13px;letter-spacing:0.5px;">VERİ GÜVENLİK VE AKTARIM</p><h4 style="margin:6px 0 0 0;color:#059669;font-weight:700;font-size:16px;">Eş Zamanlı İndeksleme Aktif</h4></div>', unsafe_allow_html=True)

    st.write("")
    st.write("")

    # İki Sütunlu Ultra Modern Kart Grid Düzeni
    col_left, col_right = st.columns(2)
    
    for index, item in enumerate(filtrelenmis_siteler):
        data = item["veri"]
        target_link = item["url"]
        
        current_col = col_left if index % 2 == 0 else col_right
        
        with current_col:
            if data["strategy"] == "english_translated":
                status_lbl = "🌐 ÇOK DİLLİ OPTİMİZASYON"
            elif data["strategy"] == "google_search":
                status_lbl = "🔍 DIZIN ENDEKSLI"
            else:
                status_lbl = "⚡ ANLIK ENTEGRASYON"
                
            categories_badges = " ".join([f'<span class="badge badge-tip">⚙️ {c}</span>' for c in data["kategoriler"]])
            
            # Ultra Modern Tasarımlı Kart Çıktısı
            st.markdown(f"""
            <div class="premium-card">
                <span class="status-indicator">{status_lbl}</span>
                <div class="card-title">{data['isim']}</div>
                <div class="card-desc">{data['aciklama']}</div>
                <div>
                    <span class="badge badge-sinif">📍 {secilen_sinif if secilen_sinif != 'Hepsi' else 'Tüm Akademik Kademeler'}</span>
                    <span class="badge badge-konu">📖 {secilen_konu if secilen_konu != 'Hepsi' else 'Genel Müfredat'}</span>
                    <span class="badge badge-origin">🏢 {data['kaynak']}</span>
                    {categories_badges}
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            btn_label = f"🎯 {data['isim']} Ünitesine Güvenli Giriş Yap" if global_mufredat_string else f"🔗 {data['isim']} Kurumsal Sayfasını Aç"
            st.link_button(btn_label, target_link, use_container_width=True)
            st.write("")

with tab2:
    st.markdown("<h3 style='color: #0f172a; font-weight:700;'>📊 Platform Veri Senkronizasyonu Altyapı Şeması</h3>", unsafe_allow_html=True)
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
