import time
import sys

lirik = [
    ("Kau curi-curii pandangann...", 2.1),
    ("Kutau kau suka tantangan...", 2.0),
    ("Oh jangan di tahan-tahan...", 1.5),
    ("Aku tau tipemu yang berandalannnn", 1.3),
    ("Tapi jangan komplain soal soal keadaan", 1.4),
    ("Bintang 5 tapi ku bukan ancaman", 1.6),
    ("Aku bukan polisi ku buatmu angkat tangan", 2.0),
    ("Jangan buru-buru kita pelan-pelan...", 2.0)
]

def efek(teks, delay_karakter = 0.07):
    for huruf in teks:
        sys.stdout.write(huruf)
        sys.stdout.flush()
        time.sleep(delay_karakter)
    print()

for baris, delay_lirik in lirik:
    efek(baris)
    time.sleep(delay_lirik)
    