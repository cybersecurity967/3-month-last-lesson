import csv
import matplotlib.pyplot as plt

FAYL_NOMI = "kitoblar.csv"


def kitoblarni_oqish():
  with open(FAYL_NOMI, "r", encoding="utf-8") as f:
    return list(csv.DictReader(f))


def kitoblarni_korish():
  kitoblar = kitoblarni_oqish()
  print("\n--- Barcha kitoblar ---")
  for k in kitoblar:
    print(
        f"{k['nom'].strip()} | {k['kategoriya'].strip()} | {k['muallif'].strip()}"
        f" — {k['oqilgan'].strip()} marta"
    )


def kitob_qidirish():
  soz = input("Kitob nomini kiriting: ").strip().lower()
  kitoblar = kitoblarni_oqish()
  topilganlar = [k for k in kitoblar if soz in k["nom"].lower()]
  if topilganlar:
    for k in topilganlar:
      print(
          f"Topildi: {k['nom']} ({k['muallif']}) — {k['oqilgan']} marta"
          " o'qilgan"
      )
  else:
    print("Bunday kitob topilmadi.")


def kategoriya_filtrlash():
  kat = input("Kategoriya nomini kiriting: ").strip().lower()
  kitoblar = kitoblarni_oqish()
  mos = [k for k in kitoblar if k["kategoriya"].strip().lower() == kat]
  if mos:
    for k in mos:
      print(f"- {k['nom']} ({k['muallif']})")
  else:
    print("Bu kategoriyada kitob topilmadi.")


def eng_kop_oqilgan():
  kitoblar = kitoblarni_oqish()
  eng_kop = max(kitoblar, key=lambda x: int(x["oqilgan"]))
  print("\nEng ko'p o'qilgan kitob:")
  print(f"{eng_kop['nom'].strip()} — {eng_kop['oqilgan'].strip()} marta")


def kitob_qoshish():
  nom = input("Kitob nomi: ").strip()
  kategoriya = input("Kategoriya: ").strip()
  muallif = input("Muallif: ").strip()
  oqilgan = input("O'qilganlar soni: ").strip()

  with open(FAYL_NOMI, "a", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerow([nom, kategoriya, muallif, oqilgan])
  print("Yangi kitob faylga qo'shildi.")


def grafik_chiqarish():
  kitoblar = kitoblarni_oqish()
  statistika = {}
  for k in kitoblar:
    kat = k["kategoriya"].strip()
    statistika[kat] = statistika.get(kat, 0) + int(k["oqilgan"])

  plt.figure(figsize=(8, 5))
  plt.bar(statistika.keys(), statistika.values(), color="mediumseagreen")
  plt.title("Kategoriyalar bo'yicha o'qilgan kitoblar statistikasi")
  plt.xlabel("Kategoriya")
  plt.ylabel("Jami o'qilgan soni")
  plt.tight_layout()
  plt.show()


def main():
  while True:
    print("\n1. Kitoblarni ko'rish")
    print("2. Kitob qidirish")
    print("3. Kategoriya bo'yicha filtrlash")
    print("4. Eng ko'p o'qilgan kitob")
    print("5. Grafik chiqarish")
    print("6. Yangi kitob qo'shish")
    print("0. Chiqish")

    tanlov = input("Tanlov: ").strip()
    if tanlov == "1":
      kitoblarni_korish()
    elif tanlov == "2":
      kitob_qidirish()
    elif tanlov == "3":
      kategoriya_filtrlash()
    elif tanlov == "4":
      eng_kop_oqilgan()
    elif tanlov == "5":
      grafik_chiqarish()
    elif tanlov == "6":
      kitob_qoshish()
    elif tanlov == "0":
      break
    else:
      print("Notori tanlov!")


if __name__ == "__main__":
  main()