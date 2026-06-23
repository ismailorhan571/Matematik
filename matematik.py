import streamlit as st

# --- SAYFA AYARLARI ---
st.set_page_config(
    page_title="Matematik Öğretmenleri İçin Dijital Oyun Havuzu",
    page_icon="📐",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- MODERN VE ŞIK CSS TASARIMI ---
st.markdown("""
<style>
    /* Genel Arka Plan ve Yazı Tipi */
    .main { background-color: #fcfcfd; }
    
    /* Sekme Tasarımları */
    .stTabs [data-baseweb="tab-list"] { gap: 15px; border-bottom: 2px solid #eef2f5; }
    .stTabs [data-baseweb="tab"] {
        background-color: transparent;
        border: none;
        padding: 12px 24px;
        font-weight: 600;
        color: #64748b;
        transition: all 0.3s ease;
    }
    .stTabs [aria-selected="true"] {
        color: #0f172a !important;
        border-bottom: 3px solid #10b981 !important;
    }
    
    /* Premium Kart Tasarımı */
    .card {
        background-color: #ffffff;
        padding: 24px;
        border-radius: 16px;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.04);
        margin-bottom: 20px;
        border: 1px solid #f1f5f9;
        border-top: 4px solid #10b981;
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }
    .card:hover {
        transform: translateY(-2px);
        box-shadow: 0 10px 25px rgba(0, 0, 0, 0.08);
    }
    .card-title { color: #1e293b; font-size: 20px; font-weight: 700; margin-bottom: 8px; }
    .card-desc { color: #64748b; font-size: 14.5px; line-height: 1.6; margin-bottom: 16px; }
    
    /* Badge / Etiket Tasarımları */
    .tag-sinif {
        display: inline-block;
        background-color: #f0fdf4;
        color: #166534;
        padding: 4px 10px;
        border-radius: 8px;
        font-size: 12.5px;
        margin-right: 8px;
        font-weight: 600;
    }
    .tag-konu {
        display: inline-block;
        background-color: #f0f9ff;
        color: #0369a1;
        padding: 4px 10px;
        border-radius: 8px;
        font-size: 12.5px;
        margin-right: 8px;
        font-weight: 600;
    }
</style>
""", unsafe_allow_html=True)

# --- BAŞLIK VE AÇIKLAMA ---
st.markdown("<h1 style='color: #1e293b; font-weight: 800;'>📐 Ortaokul Matematik Öğretmenleri İçin Dijital Materyal Havuzu</h1>", unsafe_allow_html=True)
st.write("Sınıf ve konu seçtiğinizde sizi platformların ana sayfalarına değil, doğrudan o konunun hazır oyun, etkinlik ve simülasyon sayfalarına götürür.")
st.markdown("---")

# --- YAN MENÜ (DİNAMİK VE EKSİKSİZ MEB FİLTRELERİ) ---
st.sidebar.markdown("<h2 style='color: #1e293b; font-size: 20px; font-weight: 700;'>🎯 Müfredat Odaklı Filtre</h2>", unsafe_allow_html=True)

# Sınıf Filtresi
sinif_secenekleri = ["Hepsi", "5. Sınıf", "6. Sınıf", "7. Sınıf", "8. Sınıf"]
secilen_sinif = st.sidebar.selectbox("Sınıf Seviyesi Seçin:", sinif_secenekleri)

# Tüm Sınıfların Birleştirilmiş Konu Havuzu (Genel Arama İçin)
tum_meb_konulari = [
    "Hepsi", "Doğal Sayılar", "Doğal Sayılarla İşlemler", "Çarpanlar ve Katlar", "Kümeler", "Tam Sayılar",
    "Kesirler", "Kesirlerle İşlemler", "Ondalık Gösterim", "Rasyonel Sayılar", "Üslü İfadeler", "Kareköklü İfadeler",
    "Oran ve Orantı", "Yüzdeler", "Cebirsel İfadeler", "Eşitlik ve Denklem", "Doğrusal Denklemler", "Eşitsizlikler",
    "Temel Geometrik Kavramlar", "Doğrular ve Açılar", "Çokgenler", "Üçgenler", "Çember ve Daire", "Eşlik ve Benzerlik",
    "Dönüşüm Geometrisi", "Geometrik Cisimler", "Uzunluk ve Zaman Ölçme", "Alan Ölçme", "Sıvı Ölçme",
    "Veri Toplama ve Analizi", "Olasılık", "Koordinat Sistemi"
]

# Sınıfa Göre Akıllı Konu Listesi Getirme (MEB Kazanımlarına Göre Eksiksiz)
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

secilen_konu = st.sidebar.selectbox("Konu Alanı Seçin:", konu_secenekleri)

st.sidebar.markdown("---")
st.sidebar.info(
    "💡 **Öğretmenler İçin:**\n"
    "MEB müfredatındaki tüm üniteler eklenmiştir. Seçtiğiniz konu, sitelerin arama motorlarına otomatik olarak tam eşleşme ile gönderilir."
)

# --- ANA SAYFA CANLI ARAMA ÇUBUĞU ---
arama_sorgusu = st.text_input("🔍 Kelime ile İçerik Havuzunda Ara:", placeholder="Örn: phet, kesirler, karekök, ebob ekok, denklem...").strip().lower()

# --- NOKTA ATIŞI LİNK VE MATERYAL ÜRETİCİSİ (VERİ VERİTABANI) ---
siteler_havuzu = [
    {
        "isim": "Wordwall Matematik",
        "aciklama": "Seçtiğiniz üniteye ait, öğretmenler tarafından hazırlanmış yüzlerce hazır çarkıfelek, labirent ve bilgi yarışması oyunu.",
        "base_url": "https://wordwall.net/tr/community?localeId=1055&query=",
        "query_format": "{sinif} {konu}",
        "siniflar": ["5. Sınıf", "6. Sınıf", "7. Sınıf", "8. Sınıf"],
        "konular": tum_meb_konulari # Wordwall her konuyu arayabilir
    },
    {
        "isim": "Mathigon & Polypad",
        "aciklama": "Matematiğin sanal laboratuvarı. Cebir karoları, kesir blokları, çokgenler ve dinamik manipulatiflerin yer aldığı etkileşimli panel.",
        "base_url": "https://mathigon.org/polypad",
        "query_format": "", 
        "siniflar": ["5. Sınıf", "6. Sınıf", "7. Sınıf", "8. Sınıf"],
        "konular": tum_meb_konulari
    },
    {
        "isim": "GeoGebra Materyalleri",
        "aciklama": "Özellikle geometri, grafikler, cebir ve denklemler için hazırlanmış dinamik, hareketli öğretmen simülasyon sayfaları.",
        "base_url": "https://www.geogebra.org/search/",
        "query_format": "{sinif} {konu}",
        "siniflar": ["5. Sınıf", "6. Sınıf", "7. Sınıf", "8. Sınıf"],
        "konular": tum_meb_konulari # Geogebra tüm müfredatı arayabilir
    },
    {
        "isim": "PhET İnteraktif Simülasyonlar",
        "aciklama": "Colorado Üniversitesi tarafından üretilen; kesirler, tam sayılar, oran ve denklem terazisi konularında harika dijital laboratuvarlar.",
        "base_url": "https://phet.colorado.edu/tr/simulations/filter?subjects=math&type=html",
        "query_format": "", 
        "siniflar": ["5. Sınıf", "6. Sınıf", "7. Sınıf", "8. Sınıf"],
        "konular": ["Hepsi", "Kesirler", "Kesirlerle İşlemler", "Tam Sayılar", "Oran ve Orantı", "Eşitlik ve Denklem", "Doğrusal Denklemler", "Olasılık", "Alan Ölçme"]
    },
    {
        "isim": "Matific Türkiye",
        "aciklama": "MEB müfredatına tam uyumlu, sınıf seviyenize özel animasyonlu ve senaryolu oyun görevleri.",
        "base_url": "https://www.matific.com/tr/tr/home/maths-zone/",
        "query_format": "", 
        "siniflar": ["5. Sınıf", "6. Sınıf"],
        "konular": tum_meb_konulari
    },
    {
        "isim": "Toy Theater",
        "aciklama": "Özellikle ilköğretim ve ortaokul tabanı için sanal onluk bloklar, saatler ve geometri tahtaları barındıran görselleştirme platformu.",
        "base_url": "https://toytheater.com/category/math/",
        "query_format": "",
        "siniflar": ["5. Sınıf", "6. Sınıf"],
        "konular": ["Hepsi", "Doğal Sayılar", "Doğal Sayılarla İşlemler", "Kesirler", "Uzunluk ve Zaman Ölçme", "Temel Geometrik Kavramlar", "Alan Ölçme"]
    },
    {
        "isim": "Khan Academy",
        "aciklama": "Seçilen sınıf seviyesine ait tüm kazanımları video ve oyunlaştırılmış testlerle sunan eksiksiz eğitim paneli.",
        "base_url": "https://tr.khanacademy.org/math/",
        "query_format": "",
        "siniflar": ["5. Sınıf", "6. Sınıf", "7. Sınıf", "8. Sınıf"],
        "konular": tum_meb_konulari # Khan Academy MEB müfredatının tamamını kapsar
    }
]

# --- NOKTA ATIŞI LİNK OLUŞTURMA VE FİLTRELEME MANTIĞI ---
filtrelenmis_siteler = []

for site in siteler_havuzu:
    sinif_uyumlu = (secilen_sinif == "Hepsi") or (secilen_sinif in site["siniflar"])
    konu_uyumlu = (secilen_konu == "Hepsi") or (secilen_konu in site["konular"])
    
    if sinif_uyumlu and konu_uyumlu:
        sinif_str = "" if secilen_sinif == "Hepsi" else secilen_sinif
        konu_str = "" if secilen_konu == "Hepsi" else secilen_konu
        
        dinamik_url = site["base_url"]
        
        # Wordwall & GeoGebra İçin Tam Müfredat Arama Parametresi
        if site["query_format"] and (sinif_str or konu_str):
            arama_terimi = f"{sinif_str} {konu_str}".strip().replace(" ", "%20")
            dinamik_url = f"{site['base_url']}{arama_terimi}"
            
        # Mathigon Akıllı Yönlendirme (Kavramsal Eşleştirme)
        elif site["isim"] == "Mathigon & Polypad":
            cebir_konulari = ["Cebirsel İfadeler", "Eşitlik ve Denklem", "Doğrusal Denklemler", "Eşitsizlikler"]
            geometri_konulari = ["Temel Geometrik Kavramlar", "Doğrular ve Açılar", "Çokgenler", "Üçgenler", "Çember ve Daire", "Eşlik ve Benzerlik", "Dönüşüm Geometrisi", "Geometrik Cisimler", "Alan Ölçme"]
            sayi_konulari = ["Doğal Sayılar", "Tam Sayılar", "Rasyonel Sayılar", "Kesirler", "Ondalık Gösterim", "Yüzdeler", "Üslü İfadeler", "Kareköklü İfadeler"]
            
            if secilen_konu in cebir_konulari: dinamik_url = "https://mathigon.org/polypad#algebra"
            elif secilen_konu in geometri_konulari: dinamik_url = "https://mathigon.org/polypad#geometry"
            elif secilen_konu in sayi_konulari: dinamik_url = "https://mathigon.org/polypad#numbers"
            elif secilen_konu == "Olasılık" or secilen_konu == "Veri Toplama ve Analizi": dinamik_url = "https://mathigon.org/polypad#probability"
            
        # PhET Nokta Atışı Laboratuvar Yönlendirmesi
        elif site["isim"] == "PhET İnteraktif Simülasyonlar":
            if secilen_konu == "Eşitlik ve Denklem" or secilen_konu == "Doğrusal Denklemler":
                dinamik_url = "https://phet.colorado.edu/sims/html/equality-explorer/latest/equality-explorer_tr.html"
            elif secilen_konu == "Tam Sayılar":
                dinamik_url = "https://phet.colorado.edu/sims/html/number-line-integers/latest/number-line-integers_tr.html"
            elif "Kesir" in secilen_konu:
                dinamik_url = "https://phet.colorado.edu/sims/html/fractions-intro/latest/fractions-intro_tr.html"
            elif secilen_konu == "Alan Ölçme":
                dinamik_url = "https://phet.colorado.edu/sims/html/area-builder/latest/area-builder_tr.html"
                
        # Matific Sınıf Bazlı Tam Eşleşme
        elif site["isim"] == "Matific Türkiye" and secilen_sinif != "Hepsi":
            rakam = secilen_sinif.split(".")[0]
            dinamik_url = f"https://www.matific.com/tr/tr/home/maths-zone/grade-{rakam}/"
            
        # Khan Academy Sınıf Bazlı Tam Eşleşme
        elif site["isim"] == "Khan Academy" and secilen_sinif != "Hepsi":
            rakam = secilen_sinif.split(".")[0]
            dinamik_url = f"https://tr.khanacademy.org/math/{rakam}-sinif"

        # Arama motoru süzgeci
        if arama_sorgusu:
            if (arama_sorgusu in site["isim"].lower() or 
                arama_sorgusu in site["aciklama"].lower() or 
                arama_sorgusu in secilen_konu.lower() or
                arama_sorgusu in secilen_sinif.lower()):
                filtrelenmis_siteler.append({"veri": site, "url": dinamik_url})
        else:
            filtrelenmis_siteler.append({"veri": site, "url": dinamik_url})

# --- SEKMELİ GÖRÜNÜM PANELİ ---
tab1, tab2 = st.tabs(["🎮 Doğrudan Görev & Oyun Havuzu", "📊 MEB Müfredat Strateji Tablosu"])

with tab1:
    st.markdown(f"**Aktif Filtre:** Seviye: `{secilen_sinif}` | Konu: `{secilen_konu}`")
    st.markdown(f"### Bulunan Sonuçlar ({len(filtrelenmis_siteler)} Platform)")
    
    if not filtrelenmis_siteler:
        st.warning("Seçilen kombinasyona veya arama kelimesine uygun direkt yönlendirmeli materyal bulunamadı. Lütfen filtre alanını esnetiniz.")
    else:
        col1, col2 = st.columns(2)
        for idx, item in enumerate(filtrelenmis_siteler):
            site_veri = item["veri"]
            hedef_link = item["url"]
            target_col = col1 if idx % 2 == 0 else col2
            
            with target_col:
                st.markdown(f"""
                <div class="card">
                    <div class="card-title">{site_veri['isim']}</div>
                    <div class="card-desc">{site_veri['aciklama']}</div>
                    <div style="margin-bottom: 15px;">
                        <span class="tag-sinif">📍 {secilen_sinif if secilen_sinif != 'Hepsi' else 'Tüm Ortaokul'}</span>
                        <span class="tag-konu">📖 {secilen_konu if secilen_konu != 'Hepsi' else 'Tüm MEB Konuları'}</span>
                    </div>
                </div>
                """, unsafe_allow_html=True)
                
                buton_metni = f"🚀 Doğrudan {secilen_sinif} {secilen_konu} Sayfasına Git" if secilen_sinif != "Hepsi" or secilen_konu != "Hepsi" else f"🔗 {site_veri['isim']} Sitesine Git"
                st.link_button(buton_metni, hedef_link, use_container_width=True)
                st.write("") 

with tab2:
    st.subheader("📌 Öğretmenler İçin Sınıf ve Konu Odaklı Kullanım Önerileri")
    st.markdown("""
    | Sınıf Seviyesi | En Zorlanılan Üniteler | Dijital Somutlaştırma İçin Önerilen Platformlar |
    | :--- | :--- | :--- |
    | **5. Sınıf** | Kesirler, Ondalık Gösterim, Yüzdeler | *Matific (Oyunlaştırma), Toy Theater (Onluk Bloklar)* |
    | **6. Sınıf** | Oran, Cebirsel İfadeler, Hacim Ölçme | *PhET (Oran Simülasyonu), Mathigon (Cebir Karoları)* |
    | **7. Sınıf** | Eşitlik ve Denklem, Tam Sayılarda İşlemler | *PhET (Denklem Terazisi), GeoGebra (Dinamik Grafikler)* |
    | **8. Sınıf** | LGS Hazırlık, Kareköklü İfadeler, Dönüşüm Geometrisi | *Wordwall (Hız Testleri), Khan Academy (Soru Bankası), Polypad* |
    """)

# --- FOOTER ---
st.markdown("---")
st.markdown("<p style='text-align: center; color: #94a3b8; font-size: 13px;'>Matematik Öğretmenleri Paylaşım Platformu için geliştirilmiştir. İSMAİL ORHAN © 2026</p>", unsafe_allow_html=True)
