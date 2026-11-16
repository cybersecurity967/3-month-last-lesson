import csv

tushumlar = {}

with open("savdo.csv", "r", encoding="utf-8") as fayl:
  reader = csv.DictReader(fayl)
  for qator in reader:
    kat = qator["kategoriya"].strip()
    summa = int(qator["narx"]) * int(qator["miqdor"])
    tushumlar[kat] = tushumlar.get(kat, 0) + summa

for kat, summa in tushumlar.items():
  formatlangan = f"{summa:,}".replace(",", " ")
  print(f"{kat}: {formatlangan} so'm")

eng_daromadli = max(tushumlar, key=tushumlar.get)
print(f"Eng daromadli kategoriya: {eng_daromadli}")