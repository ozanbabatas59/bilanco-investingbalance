import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Hisse senedi sembolünü kullanıcıdan al
ticker_symbol = input("Lütfen bir hisse senedi sembolü girin (Örneğin: ASELS.IS): ")

# Hisse senedi verisini al
stock = yf.Ticker(ticker_symbol)

# Bilançoyu al
balance_sheet = stock.balance_sheet

# DataFrame'e dönüştür
balance_sheet_df = pd.DataFrame(balance_sheet)

# Sütun başlıklarını ve satır başlıklarını Türkçeleştir
# Sütun başlıkları için yıl bilgilerini kaldır
balance_sheet_df.columns = balance_sheet_df.columns.astype(str).str.replace(r'\d{4}-\d{2}-\d{2}', '')

# Orijinal satır başlıklarını ve satır sayısını öğren
print("Orijinal Satır Başlıkları:")
print(balance_sheet_df.index)

# Türkçeleştirilmiş satır başlıklarını oluştur
turkish_labels = {
    'Treasury Stock': 'Hazine Hisseleri Sayısı', 
    'Common Stock': 'Adi Hisseler Sayısı', 
    'Ordinary Shares Number': 'Çıkarılan Hisseler', 
    'Net Debt': 'Net Borç',
    'Total Debt': 'Toplam Borç', 
    'Tangible Book Value': 'Maddi Defter Değeri', 
    'Invested Capital': 'Yatırılan Sermaye', 
    'Working Capital': 'Çalışma Sermayesi', 
    'Net PPE': 'Net Maddi Varlıklar',
    'Capital Lease Obligations': 'Sermaye Kira Yükümlülükleri', 
    'Shareholders Equity': 'Ortaklık Hissesi Sermayesi', 
    'Total Capitalization': 'Toplam Sermayeleşme',
    'Total Equity Gross Minority Interest': 'Toplam Özsermaye Brüt Azınlık Payı', 
    'Minority Interest': 'Azınlık Payı', 
    'Shareholders Equity Gross Minority Interest': 'Hissedarların Özsermayesi', 
    'Other Equity Interest': 'Diğer Özsermaye Menfaatleri',
    'Fixed Assets Revaluation Reserve': 'Sabit Kıymetler Yeniden Değerleme Rezervi', 
    'Retained Earnings': 'Dağıtılmamış Kar',
    'Additional Paid In Capital': 'Ek Ödenmiş Sermaye', 
    'Common Stock Equity': 'Sermaye Stoku', 
    'Treasury Stock': 'Ortak Stok',
    'Total Liabilities Net Minority Interest': 'Toplam Yükümlülükler Net Azınlık Payı',
    'Total Non Current Liabilities Net Minority Interest': 'Toplam Uzun Vadeli Yükümlülükler Net Azınlık Payı',
    'Other Non Current Liabilities': 'Diğer Uzun Vadeli Yükümlülükler',
    'Non Current Pension And Other Post Retirement Benefit Plans': 'Uzun Vadeli Emeklilik ve Diğer Emeklilik Sonrası Fayda Planları',
    'Non Current Payables And Other Non Current Liabilities': 'Ticari ve Diğer Borçlar Uzun Vadeli', 
    'Non Current Deferred Revenue': 'Uzun Vadeli Ertelenmiş Gelir',
    'Non Current Deferred Taxes Liabilities': 'Uzun Vadeli Ertelenmiş Vergi Yükümlülükleri',
    'Non Current Debt And Capital Lease Obligation': 'Uzun Vadeli Borç ve Sermaye Kira Yükümlülüğü',
    'Non Current Capital Lease Obligation': 'Uzun Vadeli Sermaye Kira Yükümlülüğü', 
    'Non Current Debt': 'Uzun Vadeli Borç',
    'Non Current Provisions': 'Uzun Vadeli Karşılıklar', 
    'Current Liabilities': 'Cari Yükümlülükler',
    'Other Current Liabilities': 'Diğer Cari Yükümlülükler',
    'Current Debt And Capital Lease Obligation': 'Cari Borç ve Sermaye Kira Yükümlülüğü',
    'Current Capital Lease Obligation': 'Cari Sermaye Kira Yükümlülüğü', 
    'Current Debt': 'Cari Borç',
    'Current Pension And Other Post Retirement Benefit Plans': 'Emeklilik ve Diğer Emeklilik Sonrası Fayda Planları Cari',
    'Current Provisions': 'Cari Karşılıklar', 
    'Payables': 'Ödenecekler', 
    'Other Payables': 'Diğer Ödenecekler', 
    'Total Tax Payable': 'Toplam Vergi Borcu',
    'Account Payable': 'Ödenecek Hesaplar', 
    'Total Assets': 'Toplam Varlıklar', 
    'Total Non Current Assets': 'Toplam Uzun Vadeli Varlıklar',
    'Other Non Current Assets': 'Diğer Uzun Vadeli Varlıklar', 
    'Non Current Prepaid Assets': 'Uzun Vadeli Peşin Ödenmiş Varlıklar',
    'Non Current Deferred Taxes Assets': 'Uzun Vadeli Ertelenmiş Vergi Varlıkları', 
    'Investment In Financial Assets': 'Finansal Varlıklara Yatırım',
    'Available For Sale Securities': 'Satışa Hazır Menkul Kıymetler', 
    'Non Current Equity Investment': 'Uzun Vadeli Özsermaye Yatırımı',
    'Goodwill And Other Intangible Assets': 'Şerefiye ve Diğer Maddi Olmayan Duran Varlıklar', 
    'Other Intangible Assets': 'Diğer Maddi Olmayan Duran Varlıklar',
    'Net Property Plant And Equipment': 'Net Maddi Duran Varlıklar', 
    'Accumulated Depreciation': 'Birikmiş Amortisman', 
    'Gross Property Plant And Equipment': 'Brüt Maddi Duran Varlıklar',
    'Construction In Progress': 'Yapım Aşamasındaki Varlıklar', 
    'Other Properties': 'Diğer Mülkler',
    'Machinery Furniture Equipment': 'Makine, Mobilya, Ekipman', 
    'Buildings And Improvements': 'Binalar ve İyileştirmeler',
    'Land And Improvements': 'Arazi ve İyileştirmeler', 
    'Properties': 'Mülkler', 
    'Current Assets': 'Cari Varlıklar',
    'Other Current Assets': 'Diğer Cari Varlıklar', 
    'Hedging Assets Current': 'Koruma Varlıkları Cari', 
    'Restricted Cash': 'Kısıtlı Nakit',
    'Prepaid Assets': 'Peşin Ödenmiş Varlıklar', 
    'Inventory': 'Envanter', 
    'Inventory Adjustments And Allowances': 'Envanter Ayarlamaları ve Karşılıklar',
    'Other Inventory': 'Diğer Envanterler', 
    'Finished Goods': 'Bitmiş Ürünler', 
    'Work In Progress': 'İşlemdeki İşler',
    'Raw Materials': 'Hammadde', 
    'Other Receivables': 'Diğer Alacaklar', 
    'Tax Receivables': 'Vergi Alacakları',
    'Receivables': 'Alacak Hesapları', 
    'Allowance For Doubtful Accounts Receivable': 'Şüpheli Alacaklar Karşılığı',
    'Gross Accounts Receivable': 'Brüt Alacak Hesapları',
    'Cash Cash Equivalents And Short Term Investments': 'Nakit, Nakit Benzerleri ve Kısa Vadeli Yatırımlar',
    'Other Short Term Investments': 'Diğer Kısa Vadeli Yatırımlar', 
    'Cash And Cash Equivalents': 'Nakit ve Nakit Benzerleri',
    'Cash Equivalents': 'Nakit Benzerleri', 
    'Cash Financial': 'Nakit Finansmanı'
}

# Orijinal ve Türkçeleştirilmiş başlıkları eşleştir ve yeniden ata
balance_sheet_df.index = [turkish_labels.get(item, item) for item in balance_sheet_df.index]

# NaN değerlerini 0 yap (bu adım, NaN olan değerleri 0 olarak değiştirir)
balance_sheet_df = balance_sheet_df.fillna(0)

# Bilançoyu göster
print("\nBilanço Tablosu:")
with pd.option_context('display.max_rows', None, 'display.max_columns', None):
    print(balance_sheet_df)

# Analiz ve tavsiye fonksiyonu
def analyze_balance_sheet(df):
    advice = {}
    
    for col in df.columns:
        net_debt = df.loc['Net Borç', col] if 'Net Borç' in df.index else None
        total_debt = df.loc['Toplam Borç', col] if 'Toplam Borç' in df.index else None
        cash_equiv = df.loc['Nakit ve Nakit Benzerleri', col] if 'Nakit ve Nakit Benzerleri' in df.index else None
        
        if net_debt is None or total_debt is None or cash_equiv is None:
            advice[col] = "Bilgi alınamadı."
        elif net_debt > total_debt * 0.5:
            advice[col] = "Borç seviyesi yüksek. Dikkatli olunmalı."
        elif cash_equiv > total_debt * 0.5:
            advice[col] = "Nakit durumu iyi. Yatırım yapılabilir."
        else:
            advice[col] = "Finansal durum dengeli. Yatırım yapılabilir."
    
    return advice

# Analiz sonuçlarını al
advice = analyze_balance_sheet(balance_sheet_df)

# Tavsiyeleri göster
print("\nDönemsel Bilanço Tavsiyeleri:")
for period, recommendation in advice.items():
    print(f"{period}: {recommendation}")

# Pasta grafiklerini çiz
def plot_pie_chart(advice):
    labels = list(advice.keys())
    sizes = [list(advice.values()).count("Bilgi alınamadı."),
             list(advice.values()).count("Borç seviyesi yüksek. Dikkatli olunmalı."),
             list(advice.values()).count("Nakit durumu iyi. Yatırım yapılabilir."),
             list(advice.values()).count("Finansal durum dengeli. Yatırım yapılabilir.")]
    colors = ['gray', 'red', 'green', 'yellow']
    explode = (0.1, 0, 0, 0)  # Dikkat çekmek için sadece ilk dilimi patlat

    plt.figure(figsize=(10, 7))
    plt.pie(sizes, explode=explode, labels=['Bilgi alınamadı', 'Borç seviyesi yüksek', 'İyi', 'Dengeli'], colors=colors,
            autopct='%1.1f%%', shadow=True, startangle=140)
    plt.axis('equal')  # Daireyi eşit yapmak için
    plt.title('Dönemsel Bilanço Tavsiyeleri')
    plt.show()

plot_pie_chart(advice)
