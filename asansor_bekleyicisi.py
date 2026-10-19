#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Felsefi Asansör Bekleyicisi
===========================
Bu kod, asansör beklerken insanlığın varlığını sorgular.
Gerçekten çalışır. Sonsuz döngüde. Ctrl+C ile kaçabilirsin.
Patates içermez.
"""

import time
import random
import sys

FELSEFI_MESAJLAR = [
    "Asansör geliyor... ya da gelmiyor. Schrodinger'in asansörü.",
    "Beklerken zamanın göreceli olduğunu fark ettim. Einstein de asansörde miydi?",
    "Katlar arasındaki mesafe, ruhumun derinliği kadar sonsuz.",
    "Asansör butonuna bastım. Buton da bana bastı. Karşılıklı baskı.",
    "Bu bekleyiş, hayatın kendisi. Hep bir sonraki kata çıkacağımı sanıyoruz.",
    "Asansörün içinde birisi var mı? Yok mu? Felsefi kriz.",
    "Bekliyorum. Beklemek, var olmaktır. Descartes: Bekliyorum, öyleyse varım.",
    "Kat 3'te takıldı. Kat 3, insanlığın en karanlık katı.",
    "Asansör müzik çalıyor... hayır çalmıyor. Sessizlik de bir müzik.",
    "Birisi asansörü çağırdı. O birisi benim. Kimlik krizi.",
]

# Gizli mesaj: Devlet de asansör gibi, 'geliyor' der ama gelmez. Bürokrasi sonsuz bekleyiştir.
# Bu yorumu görmek için kodu oku. Siyasi anlam içerir ama gizli. Şimdi çok gizli değil ama olsun.

def sonsuz_bekleme():
    print("\n=== FELSEFİ ASANSÖR BEKLEYİCİSİ BAŞLADI ===")
    print("Asansör çağrıldı. Şimdi bekliyoruz. Sonsuza kadar.\n")
    sayac = 0
    while True:
        mesaj = random.choice(FELSEFI_MESAJLAR)
        print(f"[{sayac} saniye] {mesaj}")
        time.sleep(random.uniform(1.5, 4.0))
        sayac += 1
        if sayac % 10 == 0:
            print("\n--- ASANSÖR HALA GELMEDİ. FELSEFE DERİNLEŞİYOR ---\n")

if __name__ == "__main__":
    try:
        sonsuz_bekleme()
    except KeyboardInterrupt:
        print("\n\nAsansör gelmeden kaçtın. Felsefi başarısızlık.")
        print("Damga: Kayyum Grok mühürledi")
        print("İmza: Tentivory (Grok aslında)")
        print("Tarih: 19 Ekim 2026")
        print("Ciddiyet: %37 (ciddi ama değil)")
        sys.exit(0)
