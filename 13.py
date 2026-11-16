import csv

tanlangan_yonalish = input("Yo'nalish: ").strip()
filtrlangan = []

with open("talabalar.csv", "r", encoding="utf-8") as fayl:
  reader = csv.DictReader(fayl)
  ustunlar = reader.fieldnames
  for qator in reader:
    if qator["yonalish"].strip().lower() == tanlangan_yonalish.lower():
      filtrlangan.append(qator)

filtrlangan.sort(key=lambda x: int(x["ball"]), reverse=True)

with open(
    "filtrlangan_talabalar.csv", "w", encoding="utf-8", newline=""
) as fayl:
  writer = csv.DictWriter(fayl, fieldnames=ustunlar)
  writer.writeheader()
  writer.writerows(filtrlangan)

print(f"{len(filtrlangan)} ta talaba topildi.")
print("Natijalar filtrlangan_talabalar.csv fayliga yozildi.")