
"""the3.py dosyasini bu dosyanin oldugu klasore atin"""

import time, threading, os

if not os.path.isfile("the3.py"):
    raise FileNotFoundError("Lutfen the3.py dosyasini bu dosyanin bulundugu klasore atin")
from the3 import pattern_search

images=open("the3I.txt")
results=open("the3R.txt")
patterns=open("the3P.txt")
image=images.read().splitlines()
result=results.read().splitlines()
pattern=patterns.read().splitlines()
wrongs = []

start = time.time()
uzunluk=len(image)
print(f"toplamda {uzunluk} kadar liste vardir. bazi listeler uzun oldugu icin bekletebilir, erken kapatmayin.")
def testing(x):
    start = time.time()
    cevap = pattern_search(eval(pattern[x]), eval(image[x]))
    if cevap==eval(result[x]):
        pass
    else:
        wrongs.append((x,eval(result[x]),cevap))
        

def grading():
    threads = []
    for i in range(uzunluk):
        thread = threading.Thread(target=testing,args=[i])
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()

grading()

if wrongs:
    print("YANLISLAR:")
    for i in wrongs:
        print(f"Case Numarasi: {i[0]}, Dogru Cevap: {i[1]}, Verilen Cevap: {i[2]}")
    print(f"Toplam yanlis sayisi: {len(wrongs)}")
else:
    print("\nTUM CASELER DOGRU")

elapsed = time.time() - start
print(f"Toplamda {'%.2f'%elapsed} sn surdu.")