import string
from collections import Counter

matn = "Python dasturlash qiziqarli. Python imkoniyatlari keng."

toza_matn = matn.lower().translate(str.maketrans("", "", string.punctuation))
sozlar = toza_matn.split()

eng_uzun_soz = max(sozlar, key=len)

harflar = [belgi for belgi in toza_matn if belgi.isalpha()]
eng_kop_harf = Counter(harflar).most_common(1)[0][0]

soz_soni = Counter(sozlar)
takrorlanmaydigan = [soz for soz in sozlar if soz_soni[soz] == 1]

print(f"So'zlar soni: {len(sozlar)}")
print(f"Eng uzun so'z: {eng_uzun_soz}")
print(f"Eng ko'p uchragan harf: {eng_kop_harf}")
print(f"Takrorlanmaydigan so'zlar: {', '.join(takrorlanmaydigan)}")