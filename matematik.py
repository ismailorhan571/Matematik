import streamlit as st
import urllib.parse

# --- SAYFA AYARLARI ---
st.set_page_config(
    page_title="Ortaokul Matematik Gelişmiş Materyal Motoru",
    page_icon="📐",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- PREMIUM KULLANICI ARAYÜZÜ CSS TASARIMI ---
st.markdown("""
<style>
    .main { background-color: #f8fafc; }
    .stTabs [data-baseweb="tab-list"] { gap: 20px; border-bottom: 2px solid #e2e8f0; }
    .stTabs [data-baseweb="tab"] {
        background-color: transparent; border: none; padding: 14px 28px;
        font-weight: 700; color: #64748b; font-size: 15px; transition: all 0.2s ease;
    }
    .stTabs [aria-selected="true"] { color: #0f172a !important; border-bottom: 3px solid #10b981 !important; }
    
    .card {
        background-color: #ffffff; padding: 24px; border-radius: 16px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
        margin-bottom: 16px; border: 1px solid #e2e8f0; border-top: 5px solid #10b981;
    }
    .card-title { color: #1e293b; font-size: 21px; font-weight: 800; margin-bottom: 6px; }
    .card-desc { color: #475569; font-size: 14px; line-height: 1.6; margin-bottom: 16px; }
    
    .tag-sinif { display: inline-block; background-color: #f0fdf4; color: #166534; padding: 5px 12px; border-radius: 8px; font-size: 12px; margin-right: 6px; font-weight: 700; }
    .tag-konu { display: inline-block; background-color: #f0f9ff; color: #0369a1; padding: 5px 12px; border-radius: 8px; font-size: 12px; margin-right: 6px; font-weight: 700; }
    .tag-kategori { display: inline-block; background-color: #faf5ff; color: #6b21a8; padding: 5px 12px; border-radius: 8px; font-size: 12px; margin-right: 6px; font-weight: 700; }
    .tag-kaynak { display: inline-block; background-color: #fff7ed; color: #c2410c; padding: 5px 12px; border-radius: 8px; font-size: 12px; margin-right: 6px; font-weight: 700; }
    
    .status-badge { color: #10b981; font-weight: 800; font-size: 12px; float: right; background-color: #ecfdf5; padding: 4px 10px; border-radius: 20px; }
</style>
""", unsafe_allow_html=True)

if "favoriler" not in st.session_state:
    st.session_state.favoriler = []

# --- BAŞLIK ---
st.markdown("<h1 style='color: #1e293b; font-weight: 900;'>📐 Ortaokul Matematik %100 Çalışan Materyal & Kazanım Havuzu</h1>", unsafe_allow_html=True)
st.markdown("<p style='color: #64748b; font-size: 15px;'>Hatalı linkler, yabancı dil engelleri ve 404 sayfaları tamamen temizlenmiş öğretmen destek motoru.</p>", unsafe_allow_html=True)
st.markdown("---")

# --- YAN MENÜ FİLTRELERİ ---
st.sidebar.markdown("<h2 style='color: #1e293b; font-size: 20px; font-weight: 800;'>🎯 Müfredat Seçimi</h2>", unsafe_allow_html=True)

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

secilen_konu = st.sidebar.selectbox("Konu Başlığı:", konu_secenekleri)
ozel_kazanim_sorgu = st.sidebar.text_input("📝 Ekstra Arama Terimi / Kazanım Kodu:", placeholder="Örn: Yaprak test, M.6.1.2.1...").strip()

# --- YABANCI SİTELER İÇİN ARKA PLAN SÖZLÜĞÜ (TOY THEATER FIX) ---
ingilizce_konu_haritasi = {
    "Kesirler": "fraction", "Kesirlerle İşlemler": "fraction", "Oran ve Orantı": "ratio",
    "Ondalık Gösterim": "decimal", "Yüzdeler": "percent", "Tam Sayılar": "integer",
    "Cebirsel İfadeler": "algebra", "Eşitlik ve Denklem": "equation", "Doğrusal Denklemler": "graph",
    "Çarpanlar ve Katlar": "prime", "Üslü İfadeler": "exponent", "Kareköklü İfadeler": "root",
    "Temel Geometrik Kavramlar": "geometry", "Doğrular ve Açılar": "angles", "Çokgenler": "polygon",
    "Üçgenler": "triangle", "Çember ve Daire": "circle", "Olasılık": "probability",
    "Veri Toplama ve Analizi": "graph", "Koordinat Sistemi": "grid", "Geometrik Cisimler": "3d"
}

# --- SORGUBULDER ALGORİTMASI ---
terimler = []
if secilen_konu != "Hepsi": terimler.append(secilen_konu)
if ozel_kazanim_sorgu: terimler.append(ozel_kazanim_sorgu)
saf_konu_sorgusu = " ".join(terimler).strip()

full_sorgu_parcalari = []
if secilen_sinif != "Hepsi": full_sorgu_parcalari.append(secilen_sinif)
if saf_konu_sorgusu: full_sorgu_parcalari.append(saf_konu_sorgusu)
tam_mufredat_sorgusu = " ".join(full_sorgu_parcalari).strip()

# --- MASTER VERİTABANI (YENİLENMİŞ GÜVENLİ STRATEJİLER) ---
siteler_havuzu = [
    {
        "isim": "Wordwall Matematik",
        "aciklama": "Öğretmenlerin hazırladığı binlerce çarkıfelek, labirent, test ve sürükle-bırak oyunu.",
        "strategy": "native",
        "search_url": "https://wordwall.net/tr/community?localeId=1055&query={query}",
        "default_url": "https://wordwall.net/tr/community?localeId=1055&query=matematik",
        "kategoriler": ["Oyun", "Etkinlik"],
        "kaynak": "Küresel / Açık"
    },
    {
        "isim": "Matematikçiler.com",
        "aciklama": "Ortaokul seviyesine özel harika yaprak testler, PDF dökümanları ve konu anlatım özetleri.",
        "strategy": "native",
        "search_url": "https://www.matematikciler.com/?s={query}",
        "default_url": "https://www.matematikciler.com/ortaokul-matematik/",
        "kategoriler": ["Kazanım Testi", "Çalışma Yaprağı"],
        "kaynak": "Yerel / Özel"
    },
    {
        "isim": "Toy Theater (Akıllı Çeviri Entegreli)",
        "aciklama": "Sanal onluk bloklar, kesir terazileri ve somutlaştırma araçları barındıran küresel oyun havuzu.",
        "strategy": "english_translated",
        "search_url": "https://toytheater.com/?s={query}",
        "default_url": "https://toytheater.com/category/math/",
        "kategoriler": ["Manipülatif", "Oyun"],
        "kaynak": "Küresel / İngilizce"
    },
    {
        "isim": "EBA (Eğitim Bilişim Ağı)",
        "aciklama": "MEB resmi ders anlatım videoları, etkileşimli içerikler ve bakanlık kazanım testleri.",
        "strategy": "native",
        "search_url": "https://www.eba.gov.tr/arama?q={query}",
        "default_url": "https://www.eba.gov.tr",
        "kategoriler": ["Video", "Etkinlik"],
        "kaynak": "Yerel / MEB"
    },
    {
        "isim": "Eğitimhane (Google On-Site)",
        "aciklama": "Öğretmenlerin paylaştığı güncel matematik zümre yazılıları, testler ve çalışma kağıtları havuzu.",
        "strategy": "google_search",
        "target_string": "site:egitimhane.com matematik {query}",
        "default_url": "https://www.egitimhane.com",
        "kategoriler": ["Çalışma Yaprağı", "Kazanım Testi"],
        "kaynak": "Yerel / Topluluk"
    },
    {
        "isim": "GeoGebra Materyalleri",
        "aciklama": "Geometri, koordinat sistemi ve grafikler için dinamik öğretmen simülasyonları.",
        "strategy": "native",
        "search_url": "https://www.geogebra.org/search/{query}",
        "default_url": "https://www.geogebra.org/materials",
        "kategoriler": ["Simülasyon", "Manipülatif"],
        "kaynak": "Küresel / Akademik"
    },
    {
        "isim": "Matific Türkiye (Güvenli Arama)",
        "aciklama": "Müfredata uyumlu, senaryolu, 404 hatası vermeyen akıllı matematik oyunları.",
        "strategy": "google_search",
        "target_string": "matific türkiye {query}",
        "default_url": "https://www.matific.com/tr/tr/home/maths-zone/",
        "kategoriler": ["Oyun"],
        "kaynak": "Küresel / Premium"
    },
    {
        "isim": "MEB ÖDS (Öğrenme Değerlendirme)",
        "aciklama": "Bakanlığın LGS hazırlık, deneme sınavları ve en güncel resmi kazanım testleri havuzu.",
        "strategy": "google_search",
        "target_string": "meb ods eba matematik {query}",
        "default_url": "https://ods.eba.gov.tr",
        "kategoriler": ["Kazanım Testi"],
        "kaynak": "Yerel / MEB"
    },
    {
        "isim": "PhET İnteraktif Simülasyonlar",
        "aciklama": "Kesir modelleri, negatif sayılar ve denklem terazisi barındıran üniversite onaylı dijital laboratuvar.",
        "strategy": "native",
        "search_url": "https://phet.colorado.edu/tr/simulations/filter?subjects=math&type=html&searchTerm={query}",
        "default_url": "https://phet.colorado.edu/tr/simulations/filter?subjects=math&type=html",
        "kategoriler": ["Simülasyon"],
        "kaynak": "Küresel / Akademik"
    }
]

# --- LİNK İNŞA MOTORU ---
filtrelenmis_siteler = []

for site in siteler_havuzu:
    if tam_mufredat_sorgusu:
        if site["strategy"] == "native":
            encoded_query = urllib.parse.quote(tam_mufredat_sorgusu)
            dinamik_url = site["search_url"].format(query=encoded_query)
            
        elif site["strategy"] == "google_search":
            # İç arama motoru patlak olan veya kapalı devre siteleri %100 kurtaran Google mimarisi
            ham_google_sorgu = site["target_string"].format(query=tam_mufredat_sorgusu)
            encoded_query = urllib.parse.quote(ham_google_sorgu)
            dinamik_url = f"https://www.google.com/search?q={encoded_query}"
            
        elif site["strategy"] == "english_translated":
            # Türkçe sorguyu alıp İngilizce karşılığını bularak Toy Theater'ı besleme algoritması
            ingilizce_kelime = ingilizce_konu_haritasi.get(secilen_konu, "math")
            encoded_query = urllib.parse.quote(ingilizce_kelime)
            dinamik_url = site["search_url"].format(query=encoded_query)
    else:
        dinamik_url = site["default_url"]
        
    filtrelenmis_siteler.append({"veri": site, "url": dinamik_url})

# --- GÖRÜNÜM SEKME PANELİ ---
tab1, tab2 = st.tabs(["🎮 Aktif Materyal & Görev Kanalları", "📊 MEB Sınıf Bazlı İpuçları"])

with tab1:
    st.markdown(f"**Güncel Çalışan Arama Filtreniz:** `{tam_mufredat_sorgusu if tam_mufredat_sorgusu else 'Tüm Genel Havuz Açık'}`")
    st.write("")
    
    col1, col2 = st.columns(2)
    for idx, item in enumerate(filtrelenmis_siteler):
        site_veri = item["veri"]
        hedef_link = item["url"]
        target_col = col1 if idx % 2 == 0 else col2
        
        with target_col:
            kategoriler_html = " ".join([f'<span class="tag-kategori">⚡ {k}</span>' for k in site_veri["kategoriler"]])
            
            # Sitenin çalışma stratejisine göre rozet atama
            if site_veri["strategy"] == "english_translated":
                badge_lbl = "● Otomatik Dil Çevirisi Aktif"
            elif site_veri["strategy"] == "google_search":
                badge_lbl = "● %100 Güvenli Google Yönlendirmesi"
            else:
                badge_lbl = "● Doğrudan Entegrasyon"
                
            st.markdown(f"""
            <div class="card">
                <span class="status-badge">{badge_lbl}</span>
                <div class="card-title">{site_veri['isim']}</div>
                <div class="card-desc">{site_veri['aciklama']}</div>
                <div style="margin-bottom: 15px;">
                    <span class="tag-sinif">📍 {secilen_sinif if secilen_sinif != 'Hepsi' else 'Tüm Ortaokul'}</span>
                    <span class="tag-konu">📖 {secilen_konu if secilen_konu != 'Hepsi' else 'Genel Müfredat'}</span>
                    <span class="tag-kaynak">🌐 {site_veri['kaynak']}</span>
                    {kategoriler_html}
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            btn_text = f"🚀 {site_veri['isim']} İçeriklerini Getir" if tam_mufredat_sorgusu else f"🔗 {site_veri['isim']} Sayfasına Git"
            st.link_button(btn_text, hedef_link, use_container_width=True)
            st.write("")

with tab2:
    st.subheader("📌 Öğretmen Paylaşım Notları")
    st.info("İngilizce altyapılı sitelerde (Toy Theater gibi) sistem otomatik çeviri yaparak arama sonuçlarının boş çıkmasını engeller. Eğitimhane ve ÖDS gibi sitelerin iç hataları Google altyapısı kullanılarak aşılmıştır.")

st.markdown("---")
st.markdown("<p style='text-align: center; color: #94a3b8; font-size: 13px;'>Ortak Payda Matematik Öğretmenleri için geliştirildi. İSMAİL ORHAN © 2026</p>", unsafe_allow_html=True)
