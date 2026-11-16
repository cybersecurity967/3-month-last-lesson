jami_soat = 0
eng_kop_xodim = ""
eng_kop_soat = 0

with open("ish_vaqti.txt", "r", encoding="utf-8") as fayl:
  for qator in fayl:
    qismlar = qator.strip().split()
    if len(qismlar) != 2:
      continue
    ism, soat_str = qismlar
    try:
      soat = int(soat_str)
      jami_soat += soat
      if soat > eng_kop_soat:
        eng_kop_soat = soat
        eng_kop_xodim = ism
    except ValueError:
      print(f"Ogohlantirish: {ism} uchun soat qiymati noto‘g‘ri.")

print(f"Jami ish soati: {jami_soat}")
print(f"Eng ko‘p ishlagan: {eng_kop_xodim} — {eng_kop_soat} soat")